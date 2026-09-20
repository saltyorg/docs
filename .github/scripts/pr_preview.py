from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

REPOSITORY_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")


@dataclass(frozen=True)
class PreviewContext:
    repository: str
    pr_number: int
    pr_sha: str
    trigger_conclusion: str
    trigger_run_url: str


@dataclass(frozen=True)
class PreviewReport:
    succeeded: bool
    body: str


def resolve_site_path(artifact_root: Path) -> Path:
    root = artifact_root.resolve()
    for candidate in (root / "site", root):
        resolved = candidate.resolve()
        if resolved.is_relative_to(root) and (resolved / "index.html").is_file():
            return resolved
    raise ValueError("downloaded artifact does not contain a built site index.html")


def resolve_context(
    payload: Mapping[str, object],
    *,
    get_json: Callable[[str], object] | None = None,
) -> PreviewContext:
    repository_data = _mapping(payload.get("repository"), "repository")
    repository = _string(repository_data.get("full_name"), "repository.full_name")
    if not REPOSITORY_RE.fullmatch(repository):
        raise ValueError("repository must use owner/name format")

    workflow_run = _mapping(payload.get("workflow_run"), "workflow_run")
    if workflow_run.get("event") != "pull_request":
        raise ValueError("triggering workflow must be a pull_request run")

    pr_sha = _string(workflow_run.get("head_sha"), "workflow_run.head_sha").lower()
    if not SHA_RE.fullmatch(pr_sha):
        raise ValueError("workflow_run.head_sha must be 40 hexadecimal characters")

    pull_requests = workflow_run.get("pull_requests")
    if not isinstance(pull_requests, list):
        raise ValueError("triggering workflow must identify exactly one pull request")
    if not pull_requests and get_json is not None:
        pull_requests = _resolve_pulls(repository, workflow_run, pr_sha, get_json)
    if len(pull_requests) != 1:
        raise ValueError("triggering workflow must identify exactly one pull request")
    pull_request = _mapping(pull_requests[0], "workflow_run.pull_requests[0]")
    pr_number = _positive_integer(pull_request.get("number"), "pull_request.number")

    if get_json is not None:
        pull_request = _mapping(
            get_json(f"/repos/{repository}/pulls/{pr_number}"), "pull_request"
        )
        if pull_request.get("number") != pr_number or not _matches_run(
            pull_request, repository, workflow_run
        ):
            raise ValueError("pull request identity does not match workflow run")
        if pull_request.get("state") != "open" or pull_request.get("merged_at"):
            raise ValueError("pull request is no longer open")

    pull_head = _mapping(pull_request.get("head"), "pull_request.head")
    associated_sha = _string(pull_head.get("sha"), "pull_request.head.sha").lower()
    if associated_sha != pr_sha:
        raise ValueError(
            "associated pull request head does not match workflow run head"
        )

    conclusion = _string(workflow_run.get("conclusion"), "workflow_run.conclusion")
    run_id = _positive_integer(workflow_run.get("id"), "workflow_run.id")
    run_url = str(
        workflow_run.get("html_url")
        or f"https://github.com/{repository}/actions/runs/{run_id}"
    )
    return PreviewContext(repository, pr_number, pr_sha, conclusion, run_url)


def _resolve_pulls(
    repository: str,
    workflow_run: Mapping[str, object],
    head_sha: str,
    get_json: Callable[[str], object],
) -> list[Mapping[str, object]]:
    candidates = _list_pulls(
        get_json, f"/repos/{repository}/commits/{head_sha}/pulls", {}
    )
    if not candidates:
        source = _mapping(workflow_run.get("head_repository"), "head_repository")
        source_name = _string(source.get("full_name"), "head_repository.full_name")
        if not REPOSITORY_RE.fullmatch(source_name):
            raise ValueError("head repository must use owner/name format")
        _positive_integer(source.get("id"), "head_repository.id")
        branch = _string(workflow_run.get("head_branch"), "workflow_run.head_branch")
        _timestamp(workflow_run.get("created_at"), "workflow_run.created_at")
        candidates = _list_pulls(
            get_json,
            f"/repos/{repository}/pulls",
            {"state": "all", "head": f"{source_name.split('/', 1)[0]}:{branch}"},
        )
    return [pull for pull in candidates if _matches_run(pull, repository, workflow_run)]


def _list_pulls(
    get_json: Callable[[str], object], path: str, query: Mapping[str, object]
) -> list[Mapping[str, object]]:
    pulls = []
    page = 1
    while True:
        result = get_json(f"{path}?{urlencode(dict(query, per_page=100, page=page))}")
        if not isinstance(result, list):
            raise TypeError("GitHub pull requests response must be an array")
        pulls.extend(_mapping(pull, "pull_request") for pull in result)
        if len(result) < 100:
            return pulls
        page += 1


def _matches_run(
    pull: Mapping[str, object], repository: str, workflow_run: Mapping[str, object]
) -> bool:
    """Match trusted identity and lifetime; incomplete candidates fail closed."""
    source = _mapping(workflow_run.get("head_repository"), "head_repository")
    source_id = _positive_integer(source.get("id"), "head_repository.id")
    branch = _string(workflow_run.get("head_branch"), "workflow_run.head_branch")
    run_created = _timestamp(workflow_run.get("created_at"), "workflow_run.created_at")
    _positive_integer(pull.get("number"), "pull_request.number")
    head = _mapping(pull.get("head"), "pull_request.head")
    base = _mapping(pull.get("base"), "pull_request.base")
    head_repo = _mapping(head.get("repo"), "pull_request.head.repo")
    base_repo = _mapping(base.get("repo"), "pull_request.base.repo")
    head_id = _positive_integer(head_repo.get("id"), "pull_request.head.repo.id")
    head_ref = _string(head.get("ref"), "pull_request.head.ref")
    target = _string(base_repo.get("full_name"), "pull_request.base.repo.full_name")
    if not REPOSITORY_RE.fullmatch(target):
        raise ValueError("pull request base repository must use owner/name format")
    if (
        head_id != source_id
        or head_ref != branch
        or target.casefold() != repository.casefold()
    ):
        return False
    opened = _timestamp(pull.get("created_at"), "pull_request.created_at")
    if opened > run_created:
        return False
    state = pull.get("state")
    if state not in ("open", "closed"):
        raise ValueError("pull request state must be open or closed")
    if pull.get("closed_at") is not None:
        closed = _timestamp(pull["closed_at"], "pull_request.closed_at")
        return closed >= run_created
    if state == "closed":
        raise ValueError("closed pull request must identify its closure time")
    return True


def _timestamp(value: object, name: str) -> datetime:
    timestamp = datetime.fromisoformat(_string(value, name).replace("Z", "+00:00"))
    if timestamp.tzinfo is None:
        raise ValueError(f"{name} must include a timezone")
    return timestamp


def build_comment(
    context: PreviewContext,
    *,
    deploy_outcome: str,
    deployment_url: str,
    branch_url: str,
    downstream_run_url: str,
) -> PreviewReport:
    succeeded = context.trigger_conclusion == "success" and deploy_outcome == "success"
    if succeeded and (not deployment_url or not branch_url):
        raise ValueError("successful deployment must provide both preview URLs")

    status = "✅&nbsp; Deploy successful!" if succeeded else "❌&nbsp; Build failed!"
    logs_url = (
        downstream_run_url
        if context.trigger_conclusion == "success"
        else context.trigger_run_url
    )
    rows = [
        f"<tr><td><strong>Latest commit:</strong></td><td><code>{context.pr_sha}</code></td></tr>",
        f"<tr><td><strong>Status:</strong></td><td>&nbsp;{status}</td></tr>",
    ]
    if succeeded:
        rows.extend(
            [
                f"<tr><td><strong>Preview URL:</strong></td><td><a href='{deployment_url}'>{deployment_url}</a></td></tr>",
                f"<tr><td><strong>Branch Preview URL:</strong></td><td><a href='{branch_url}'>{branch_url}</a></td></tr>",
            ]
        )
    rows.append(
        f"<tr><td><strong>Build logs:</strong></td><td><a href='{logs_url}'>View build logs</a></td></tr>"
    )
    return PreviewReport(
        succeeded,
        "Deploying with ⚡ Cloudflare Pages<br><table>" + "".join(rows) + "</table>",
    )


def post_comment(
    *,
    repository: str,
    pr_number: int,
    body: str,
    token: str,
    opener: Callable[..., Any] = urlopen,
) -> None:
    if not REPOSITORY_RE.fullmatch(repository):
        raise ValueError("repository must use owner/name format")
    if pr_number < 1:
        raise ValueError("PR number must be positive")
    if not token:
        raise ValueError("GitHub token must not be empty")
    request = Request(
        f"https://api.github.com/repos/{repository}/issues/{pr_number}/comments",
        data=json.dumps({"body": body}, separators=(",", ":")).encode("utf-8"),
        method="POST",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "saltyorg/docs",
            "X-GitHub-Api-Version": "2026-03-10",
        },
    )
    try:
        with opener(request, timeout=30) as response:
            if response.status != 201:
                raise RuntimeError(
                    f"GitHub comment request returned HTTP {response.status}"
                )
    except HTTPError as error:
        raise RuntimeError(
            f"GitHub comment request returned HTTP {error.code}"
        ) from error
    except URLError as error:
        raise RuntimeError(
            "GitHub comment request ended without a definitive response"
        ) from error


def _load_event(env: Mapping[str, str]) -> dict[str, object]:
    event_path = Path(_env(env, "GITHUB_EVENT_PATH"))
    payload = json.loads(event_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise TypeError("GitHub event payload must be an object")
    return payload


def _resolve_event_context(env: Mapping[str, str]) -> PreviewContext:
    payload = _load_event(env)
    repository = _mapping(payload.get("repository"), "repository")
    if _env(env, "GITHUB_REPOSITORY") != repository.get("full_name"):
        raise ValueError("GITHUB_REPOSITORY does not match event repository")
    token = _env(env, "GITHUB_TOKEN")
    return resolve_context(payload, get_json=lambda path: _get_context_json(path, token))


def _get_context_json(path: str, token: str) -> object:
    request = Request(
        f"https://api.github.com{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "saltyorg/docs",
            "X-GitHub-Api-Version": "2026-03-10",
        },
    )
    try:
        with urlopen(request, timeout=30) as response:
            if response.status != 200:
                raise RuntimeError(
                    f"GitHub context request returned HTTP {response.status}"
                )
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        raise RuntimeError(
            f"GitHub context request returned HTTP {error.code}"
        ) from error
    except (URLError, OSError) as error:
        raise RuntimeError("GitHub context request did not complete") from error
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise RuntimeError("GitHub context request returned invalid JSON") from error


def _write_context(context: PreviewContext, output_path: Path) -> None:
    outputs = {
        "pr-number": str(context.pr_number),
        "pr-sha": context.pr_sha,
        "trigger-conclusion": context.trigger_conclusion,
        "trigger-run-url": context.trigger_run_url,
    }
    with output_path.open("a", encoding="utf-8") as output:
        for name, value in outputs.items():
            if "\n" in value or "\r" in value:
                raise ValueError(f"output {name} must be a single line")
            output.write(f"{name}={value}\n")


def _write_output(name: str, value: str, output_path: Path) -> None:
    if "\n" in value or "\r" in value:
        raise ValueError(f"output {name} must be a single line")
    with output_path.open("a", encoding="utf-8") as output:
        output.write(f"{name}={value}\n")


def _report(env: Mapping[str, str]) -> bool:
    context = _resolve_event_context(env)
    repository = _env(env, "GITHUB_REPOSITORY")
    downstream_url = (
        f"{env.get('GITHUB_SERVER_URL', 'https://github.com')}/"
        f"{repository}/actions/runs/{_env(env, 'GITHUB_RUN_ID')}"
    )
    report = build_comment(
        context,
        deploy_outcome=env.get("DEPLOY_OUTCOME", "skipped"),
        deployment_url=env.get("DEPLOYMENT_URL", ""),
        branch_url=env.get("BRANCH_URL", ""),
        downstream_run_url=downstream_url,
    )
    post_comment(
        repository=repository,
        pr_number=context.pr_number,
        body=report.body,
        token=_env(env, "GITHUB_TOKEN"),
    )
    return report.succeeded


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("resolve", "site-path", "report"))
    args = parser.parse_args(argv)
    try:
        if args.command == "resolve":
            context = _resolve_event_context(os.environ)
            _write_context(context, Path(_env(os.environ, "GITHUB_OUTPUT")))
            return 0
        if args.command == "site-path":
            site_path = resolve_site_path(Path(_env(os.environ, "ARTIFACT_PATH")))
            _write_output(
                "site-path", str(site_path), Path(_env(os.environ, "GITHUB_OUTPUT"))
            )
            return 0
        if _report(os.environ):
            return 0
        print("::error::The PR preview workflow did not complete successfully")
        return 1
    except (OSError, TypeError, ValueError, RuntimeError) as error:
        print(f"::error::PR preview reporting failed: {error}", file=sys.stderr)
        return 1


def _mapping(value: object, name: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise TypeError(f"{name} must be an object")
    return value


def _string(value: object, name: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{name} must be a non-empty string")
    return value


def _positive_integer(value: object, name: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise ValueError(f"{name} must be a positive integer")
    return value


def _env(env: Mapping[str, str], name: str) -> str:
    value = env.get(name, "")
    if not value:
        raise ValueError(f"{name} must not be empty")
    return value


if __name__ == "__main__":
    raise SystemExit(main())

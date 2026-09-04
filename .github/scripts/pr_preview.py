from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
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


def resolve_context(payload: Mapping[str, object]) -> PreviewContext:
    repository_data = _mapping(payload.get("repository"), "repository")
    repository = _string(repository_data.get("full_name"), "repository.full_name")
    if not REPOSITORY_RE.fullmatch(repository):
        raise ValueError("repository must use owner/name format")

    workflow_run = _mapping(payload.get("workflow_run"), "workflow_run")
    if workflow_run.get("event") != "pull_request":
        raise ValueError("triggering workflow must be a pull_request run")

    pull_requests = workflow_run.get("pull_requests")
    if not isinstance(pull_requests, list) or len(pull_requests) != 1:
        raise ValueError("triggering workflow must identify exactly one pull request")
    pull_request = _mapping(pull_requests[0], "workflow_run.pull_requests[0]")
    pr_number = _positive_integer(pull_request.get("number"), "pull_request.number")

    pr_sha = _string(workflow_run.get("head_sha"), "workflow_run.head_sha").lower()
    if not SHA_RE.fullmatch(pr_sha):
        raise ValueError("workflow_run.head_sha must be 40 hexadecimal characters")
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
    context = resolve_context(_load_event(env))
    repository = _env(env, "GITHUB_REPOSITORY")
    if repository != context.repository:
        raise ValueError("GITHUB_REPOSITORY does not match event repository")
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
            context = resolve_context(_load_event(os.environ))
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

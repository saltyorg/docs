from __future__ import annotations

import copy
import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from typing import Self
from unittest.mock import patch
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlsplit
from urllib.request import Request

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pr_preview
from pr_preview import build_comment, post_comment, resolve_context, resolve_site_path


def workflow_run_event(
    *,
    conclusion: str = "failure",
    number: int = 395,
    head_sha: str = "f34bf7168e5884628b18b8e9c7c9470bc10343e2",
) -> dict[str, object]:
    return {
        "repository": {"full_name": "saltyorg/docs"},
        "workflow_run": {
            "id": 33826757856,
            "event": "pull_request",
            "status": "completed",
            "conclusion": conclusion,
            "head_sha": head_sha,
            "html_url": "https://github.com/saltyorg/docs/actions/runs/33826757856",
            "pull_requests": [
                {
                    "number": number,
                    "head": {"sha": head_sha},
                    "base": {"ref": "main"},
                }
            ],
        },
    }


def tracearr_event() -> dict[str, object]:
    """Trusted fields from the successful PR #421 build, attempt 2."""
    return {
        "repository": {"id": 380899057, "full_name": "saltyorg/docs"},
        "workflow_run": {
            "id": 35493343385,
            "event": "pull_request",
            "status": "completed",
            "conclusion": "success",
            "run_attempt": 2,
            "head_sha": "8a1d2f15fad4dcdddcbc34e1a2e8baf085b294fc",
            "head_branch": "tracearr",
            "head_repository": {"id": 1373304386, "full_name": "connorgallopo/docs"},
            "created_at": "2026-09-20T06:05:49Z",
            "html_url": "https://github.com/saltyorg/docs/actions/runs/35493343385",
            "pull_requests": [],
        },
    }


def tracearr_pull() -> dict[str, object]:
    return {
        "number": 421,
        "state": "open",
        "created_at": "2026-09-16T16:15:39Z",
        "closed_at": None,
        "merged_at": None,
        "head": {
            "ref": "tracearr",
            "sha": "8a1d2f15fad4dcdddcbc34e1a2e8baf085b294fc",
            "repo": {"id": 1373304386, "full_name": "connorgallopo/docs"},
        },
        "base": {
            "ref": "main",
            "repo": {"id": 380899057, "full_name": "saltyorg/docs"},
        },
    }


class PreviewAPI:
    """In-memory responses at the external GitHub JSON boundary."""

    def __init__(self) -> None:
        self.commit_pulls: list[object] = []
        self.branch_pages: list[list[object]] = [[tracearr_pull()]]
        self.pull = tracearr_pull()
        self.paths: list[str] = []

    def __call__(self, path: str) -> object:
        self.paths.append(path)
        url = urlsplit(path)
        query = parse_qs(url.query)
        if url.path.endswith("/commits/8a1d2f15fad4dcdddcbc34e1a2e8baf085b294fc/pulls"):
            return copy.deepcopy(self.commit_pulls)
        if url.path == "/repos/saltyorg/docs/pulls":
            if query.get("state") != ["all"] or query.get("per_page") != ["100"]:
                raise AssertionError(f"unexpected branch lookup: {path}")
            return copy.deepcopy(self.branch_pages[int(query["page"][0]) - 1])
        if url.path == "/repos/saltyorg/docs/pulls/421":
            return copy.deepcopy(self.pull)
        raise AssertionError(f"unexpected GitHub request: {path}")


class FakeResponse:
    def __init__(self, payload: object = None, status: int = 201) -> None:
        self.status = status
        self.payload = {} if payload is None else payload

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *args: object) -> None:
        return None

    def read(self) -> bytes:
        return json.dumps(self.payload).encode("utf-8")


class RecordingOpener:
    def __init__(self, error: Exception | None = None) -> None:
        self.error = error
        self.requests: list[Request] = []

    def __call__(self, request: Request, timeout: int) -> FakeResponse:
        self.requests.append(request)
        if self.error:
            raise self.error
        return FakeResponse()


class PreviewContextTests(unittest.TestCase):
    def test_tracearr_empty_event_and_commit_associations_resolve_by_branch(self) -> None:
        api = PreviewAPI()

        context = resolve_context(tracearr_event(), get_json=api)

        self.assertEqual(context.pr_number, 421)
        self.assertEqual(context.pr_sha, "8a1d2f15fad4dcdddcbc34e1a2e8baf085b294fc")
        self.assertEqual(context.trigger_conclusion, "success")
        branch_query = parse_qs(urlsplit(api.paths[1]).query)
        self.assertEqual(branch_query["head"], ["connorgallopo:tracearr"])
        self.assertEqual(api.paths[-1], "/repos/saltyorg/docs/pulls/421")

    def test_event_association_is_refreshed_without_fallback(self) -> None:
        payload = tracearr_event()
        payload["workflow_run"]["pull_requests"] = [
            {"number": 421, "head": {"sha": payload["workflow_run"]["head_sha"]}}
        ]
        api = PreviewAPI()

        self.assertEqual(resolve_context(payload, get_json=api).pr_number, 421)
        self.assertEqual(api.paths, ["/repos/saltyorg/docs/pulls/421"])

    def test_commit_association_precedes_branch_search(self) -> None:
        api = PreviewAPI()
        api.commit_pulls = [tracearr_pull()]

        self.assertEqual(resolve_context(tracearr_event(), get_json=api).pr_number, 421)
        self.assertEqual(len(api.paths), 2)
        self.assertEqual(api.paths[-1], "/repos/saltyorg/docs/pulls/421")

    def test_branch_reuse_and_unrelated_candidates_do_not_match(self) -> None:
        cases = [
            ("old PR", {"closed_at": "2026-09-19T06:05:49Z", "state": "closed"}),
            ("later PR", {"created_at": "2026-09-20T06:05:50Z"}),
            ("foreign source", {"head": {"repo": {"id": 999}}}),
            ("foreign target", {"base": {"repo": {"full_name": "someone/docs"}}}),
            ("wrong branch", {"head": {"ref": "other"}}),
        ]
        for name, updates in cases:
            with self.subTest(name=name):
                api = PreviewAPI()
                unrelated = tracearr_pull()
                for key, value in updates.items():
                    if key in ("head", "base"):
                        for nested_key, nested_value in value.items():
                            if nested_key == "repo":
                                unrelated[key][nested_key].update(nested_value)
                            else:
                                unrelated[key][nested_key] = nested_value
                    else:
                        unrelated[key] = value
                api.branch_pages = [[unrelated]]
                with self.assertRaisesRegex(ValueError, "exactly one"):
                    resolve_context(tracearr_event(), get_json=api)

    def test_ambiguous_or_incomplete_branch_candidates_are_rejected(self) -> None:
        for candidates in ([tracearr_pull(), tracearr_pull()], [tracearr_pull(), {}]):
            with self.subTest(candidates=candidates):
                api = PreviewAPI()
                api.branch_pages = [candidates]
                with self.assertRaises((ValueError, TypeError)):
                    resolve_context(tracearr_event(), get_json=api)

    def test_missing_or_malformed_run_metadata_is_rejected(self) -> None:
        for key, value in (
            ("head_repository", None),
            ("head_repository", {"id": True, "full_name": "connorgallopo/docs"}),
            ("head_branch", ""),
            ("created_at", "2026-09-20"),
            ("created_at", "invalid"),
        ):
            with self.subTest(key=key, value=value):
                payload = tracearr_event()
                payload["workflow_run"][key] = value
                with self.assertRaises((ValueError, TypeError)):
                    resolve_context(payload, get_json=PreviewAPI())

    def test_selected_pr_is_revalidated_before_use(self) -> None:
        for change in (
            "new head", "closed", "new number", "foreign source", "foreign target"
        ):
            with self.subTest(change=change):
                api = PreviewAPI()
                if change == "new head":
                    api.pull["head"]["sha"] = "a" * 40
                elif change == "closed":
                    api.pull.update(state="closed", closed_at="2026-09-20T07:00:00Z")
                elif change == "new number":
                    api.pull["number"] = 422
                elif change == "foreign source":
                    api.pull["head"]["repo"]["id"] = 999
                else:
                    api.pull["base"]["repo"]["full_name"] = "someone/docs"
                with self.assertRaises(ValueError):
                    resolve_context(tracearr_event(), get_json=api)

    def test_branch_lookup_paginates_and_encodes_ref(self) -> None:
        api = PreviewAPI()
        payload = tracearr_event()
        branch = "feature/tracearr+other&docs"
        payload["workflow_run"]["head_branch"] = branch
        api.pull["head"]["ref"] = branch
        old = tracearr_pull()
        old.update(state="closed", closed_at="2026-09-19T00:00:00Z")
        api.branch_pages = [[old] * 100, [copy.deepcopy(api.pull)]]

        self.assertEqual(resolve_context(payload, get_json=api).pr_number, 421)
        queries = [parse_qs(urlsplit(path).query) for path in api.paths[1:-1]]
        self.assertEqual([query["page"] for query in queries], [["1"], ["2"]])
        self.assertEqual(
            [query["head"] for query in queries],
            [[f"connorgallopo:{branch}"]] * 2,
        )

    def test_api_failure_is_not_treated_as_no_association(self) -> None:
        def failure(path: str) -> object:
            raise RuntimeError("GitHub context request returned HTTP 403")

        with self.assertRaisesRegex(RuntimeError, "HTTP 403"):
            resolve_context(tracearr_event(), get_json=failure)

    def test_invalid_fallback_response_shapes_are_rejected(self) -> None:
        for response in ({"message": "invalid response"}, [None]):
            with self.subTest(response=response):
                with self.assertRaises(TypeError):
                    resolve_context(tracearr_event(), get_json=lambda path: response)

    def test_failed_trigger_resolves_pr_from_trusted_workflow_event(self) -> None:
        context = resolve_context(workflow_run_event())

        self.assertEqual(context.repository, "saltyorg/docs")
        self.assertEqual(context.pr_number, 395)
        self.assertEqual(context.pr_sha, "f34bf7168e5884628b18b8e9c7c9470bc10343e2")
        self.assertEqual(context.trigger_conclusion, "failure")
        self.assertEqual(
            context.trigger_run_url,
            "https://github.com/saltyorg/docs/actions/runs/33826757856",
        )

    def test_mismatched_pr_head_is_rejected(self) -> None:
        payload = workflow_run_event()
        payload["workflow_run"]["pull_requests"][0]["head"]["sha"] = "b" * 40

        with self.assertRaisesRegex(ValueError, "does not match"):
            resolve_context(payload)

    def test_multiple_pull_requests_are_rejected(self) -> None:
        payload = workflow_run_event()
        payload["workflow_run"]["pull_requests"].append(
            {"number": 396, "head": {"sha": payload["workflow_run"]["head_sha"]}}
        )

        with self.assertRaisesRegex(ValueError, "exactly one"):
            resolve_context(payload)


class PreviewCommandTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        self.event = root / "event.json"
        self.event.write_text(json.dumps(tracearr_event()), encoding="utf-8")
        self.output = root / "output.txt"
        self.env = {
            "GITHUB_EVENT_PATH": str(self.event),
            "GITHUB_OUTPUT": str(self.output),
            "GITHUB_TOKEN": "secret-token",
            "GITHUB_REPOSITORY": "saltyorg/docs",
            "GITHUB_RUN_ID": "35493442534",
            "DEPLOY_OUTCOME": "success",
            "DEPLOYMENT_URL": "https://preview.docs.pages.dev",
            "BRANCH_URL": "https://pr-421.docs.pages.dev",
        }
        self.api = PreviewAPI()
        self.requests: list[Request] = []
        self.error: Exception | None = None

    def open_request(self, request: Request, timeout: int) -> FakeResponse:
        self.requests.append(request)
        if self.error:
            raise self.error
        prefix = "https://api.github.com"
        if not request.full_url.startswith(prefix + "/repos/saltyorg/docs/"):
            raise AssertionError(f"unexpected request URL: {request.full_url}")
        return FakeResponse(self.api(request.full_url[len(prefix) :]), status=200)

    def run_command(self, command: str) -> tuple[int, str]:
        output = io.StringIO()
        with (
            patch.dict(os.environ, self.env, clear=True),
            patch("pr_preview.urlopen", side_effect=self.open_request),
            redirect_stderr(output),
            redirect_stdout(output),
        ):
            code = pr_preview.main([command])
        return code, output.getvalue()

    def test_resolve_command_writes_verified_context_for_empty_pr_list(self) -> None:
        code, message = self.run_command("resolve")

        self.assertEqual(code, 0, message)
        self.assertEqual(
            self.output.read_text(encoding="utf-8"),
            "pr-number=421\n"
            "pr-sha=8a1d2f15fad4dcdddcbc34e1a2e8baf085b294fc\n"
            "trigger-conclusion=success\n"
            "trigger-run-url=https://github.com/saltyorg/docs/actions/runs/35493343385\n",
        )
        self.assertTrue(
            all(
                request.get_header("Authorization") == "Bearer secret-token"
                for request in self.requests
            )
        )

    def test_report_command_re_resolves_context_and_comments_on_verified_pr(self) -> None:
        with patch("pr_preview.post_comment") as post:
            code, message = self.run_command("report")

        self.assertEqual(code, 0, message)
        self.assertEqual(post.call_args.kwargs["repository"], "saltyorg/docs")
        self.assertEqual(post.call_args.kwargs["pr_number"], 421)
        self.assertIn("Deploy successful", post.call_args.kwargs["body"])
        self.assertEqual(self.api.paths[-1], "/repos/saltyorg/docs/pulls/421")

    def test_current_pr_build_failure_is_still_reported(self) -> None:
        payload = tracearr_event()
        payload["workflow_run"]["conclusion"] = "failure"
        self.event.write_text(json.dumps(payload), encoding="utf-8")
        self.env["DEPLOY_OUTCOME"] = "skipped"

        with patch("pr_preview.post_comment") as post:
            code, message = self.run_command("report")

        self.assertEqual(code, 1)
        self.assertIn("did not complete successfully", message)
        self.assertEqual(post.call_args.kwargs["pr_number"], 421)
        self.assertIn("Build failed", post.call_args.kwargs["body"])
        self.assertIn("35493343385", post.call_args.kwargs["body"])

    def test_stale_or_ambiguous_pr_never_outputs_context_or_posts_comment(self) -> None:
        for mode in ("stale", "ambiguous"):
            for command in ("resolve", "report"):
                with self.subTest(mode=mode, command=command):
                    self.api = PreviewAPI()
                    if mode == "stale":
                        self.api.pull["head"]["sha"] = "c" * 40
                    else:
                        self.api.branch_pages = [[tracearr_pull(), tracearr_pull()]]
                    with patch("pr_preview.post_comment") as post:
                        code, message = self.run_command(command)
                    self.assertEqual(code, 1, message)
                    self.assertFalse(self.output.exists())
                    post.assert_not_called()

    def test_api_errors_are_visible_without_response_or_token_disclosure(self) -> None:
        errors = (
            URLError("secret-token in exception"),
            HTTPError(
                "https://api.github.com/repos/saltyorg/docs/pulls",
                403,
                "secret-token in message",
                {},
                io.BytesIO(b"secret-token in response"),
            ),
        )
        for error in errors:
            with self.subTest(error=type(error).__name__):
                self.error = error
                code, message = self.run_command("resolve")
                self.assertEqual(code, 1)
                self.assertIn("GitHub context request", message)
                self.assertNotIn("secret-token", message)
                self.assertFalse(self.output.exists())

    def test_repository_mismatch_is_rejected_before_api_access(self) -> None:
        self.env["GITHUB_REPOSITORY"] = "someone/docs"

        code, message = self.run_command("resolve")

        self.assertEqual(code, 1)
        self.assertIn("does not match", message)
        self.assertFalse(self.requests)


class SitePathTests(unittest.TestCase):
    def test_legacy_bundle_selects_nested_site_without_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "PR_NUMBER").write_text("395")
            (root / "site").mkdir()
            (root / "site" / "index.html").write_text("site")

            self.assertEqual(resolve_site_path(root), (root / "site").resolve())

    def test_site_only_bundle_selects_artifact_root(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "index.html").write_text("site")

            self.assertEqual(resolve_site_path(root), root.resolve())

    def test_bundle_without_built_site_is_rejected(self) -> None:
        with (
            tempfile.TemporaryDirectory() as directory,
            self.assertRaisesRegex(ValueError, "index.html"),
        ):
            resolve_site_path(Path(directory))


class PreviewReportTests(unittest.TestCase):
    def test_trigger_failure_reports_upstream_logs_without_empty_preview_links(
        self,
    ) -> None:
        context = resolve_context(workflow_run_event())

        report = build_comment(
            context,
            deploy_outcome="skipped",
            deployment_url="",
            branch_url="",
            downstream_run_url="https://github.com/saltyorg/docs/actions/runs/33826841201",
        )

        self.assertFalse(report.succeeded)
        self.assertIn("Build failed", report.body)
        self.assertIn(context.trigger_run_url, report.body)
        self.assertNotIn("Preview URL", report.body)
        self.assertNotIn("33826841201", report.body)

    def test_success_reports_both_preview_urls(self) -> None:
        context = resolve_context(workflow_run_event(conclusion="success", number=415))

        report = build_comment(
            context,
            deploy_outcome="success",
            deployment_url="https://caa9ac61.docs-acq.pages.dev",
            branch_url="https://pr-415.docs-acq.pages.dev",
            downstream_run_url="https://github.com/saltyorg/docs/actions/runs/33826841681",
        )

        self.assertTrue(report.succeeded)
        self.assertIn("Deploy successful", report.body)
        self.assertIn("https://caa9ac61.docs-acq.pages.dev", report.body)
        self.assertIn("https://pr-415.docs-acq.pages.dev", report.body)
        self.assertIn("33826841681", report.body)

    def test_deploy_failure_reports_downstream_logs(self) -> None:
        context = resolve_context(workflow_run_event(conclusion="success"))

        report = build_comment(
            context,
            deploy_outcome="failure",
            deployment_url="",
            branch_url="",
            downstream_run_url="https://github.com/saltyorg/docs/actions/runs/999",
        )

        self.assertFalse(report.succeeded)
        self.assertIn("https://github.com/saltyorg/docs/actions/runs/999", report.body)

    def test_comment_uses_structured_api_request(self) -> None:
        opener = RecordingOpener()

        post_comment(
            repository="saltyorg/docs",
            pr_number=395,
            body="Build failed",
            token="secret-token",
            opener=opener,
        )

        request = opener.requests[0]
        self.assertEqual(
            request.full_url,
            "https://api.github.com/repos/saltyorg/docs/issues/395/comments",
        )
        self.assertEqual(json.loads(request.data or b"{}"), {"body": "Build failed"})
        self.assertEqual(len(opener.requests), 1)

    def test_comment_transport_error_does_not_expose_token(self) -> None:
        opener = RecordingOpener(URLError("connection reset"))

        with self.assertRaises(RuntimeError) as raised:
            post_comment(
                repository="saltyorg/docs",
                pr_number=395,
                body="Build failed",
                token="secret-token",
                opener=opener,
            )

        self.assertNotIn("secret-token", str(raised.exception))


if __name__ == "__main__":
    unittest.main()

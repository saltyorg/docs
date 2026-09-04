from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Self
from urllib.error import URLError
from urllib.request import Request

sys.path.insert(0, str(Path(__file__).resolve().parent))

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


class FakeResponse:
    status = 201

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *args: object) -> None:
        return None

    def read(self) -> bytes:
        return b"{}"


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

#!/usr/bin/env python3
"""
Check documentation coverage for Saltbox and Sandbox roles.

This script:
1. Parses role names from Saltbox and Sandbox repositories
2. Compares them against the docs/apps folder
3. Reports missing documentation
4. Respects ignore lists from .docs-coverage-ignore.yml
"""

import sys
import yaml
from pathlib import Path
from typing import Set, List, Dict


def load_ignore_config(config_path: Path) -> Dict[str, List[str]]:
    """Load the ignore configuration file."""
    if not config_path.exists():
        return {"saltbox": [], "sandbox": []}

    with open(config_path) as f:
        config = yaml.safe_load(f) or {}

    return {
        "saltbox": config.get("saltbox", []),
        "sandbox": config.get("sandbox", [])
    }


def get_roles_from_repo(repo_path: Path) -> Set[str]:
    """Get all role names from a repository."""
    roles_path = repo_path / "roles"

    if not roles_path.exists():
        return set()

    roles = set()
    for role_dir in roles_path.iterdir():
        if role_dir.is_dir():
            # Assume all directories in roles/ are roles
            roles.add(role_dir.name)

    return roles


def get_documented_apps(docs_path: Path, folder: str = "apps") -> Set[str]:
    """Get all documented apps from docs/{folder} folder."""
    apps_path = docs_path / folder

    if not apps_path.exists():
        return set()

    documented = set()
    for doc_file in apps_path.glob("*.md"):
        # Remove .md extension to get app name
        app_name = doc_file.stem
        documented.add(app_name)

    return documented


def generate_issue_body(saltbox_missing: List[str], sandbox_missing: List[str], total_missing: int, workflow_url: str) -> str:
    """Generate the GitHub issue body."""
    body = "## Missing Documentation for Roles\n\n"
    body += f"**Total missing:** {total_missing}\n\n"

    if saltbox_missing:
        body += f"### Saltbox Roles ({len(saltbox_missing)})\n\n"
        for role in saltbox_missing:
            body += f"- [ ] `{role}`\n"
        body += "\n"

    if sandbox_missing:
        body += f"### Sandbox Roles ({len(sandbox_missing)})\n\n"
        for role in sandbox_missing:
            body += f"- [ ] `{role}`\n"
        body += "\n"

    body += "---\n\n"
    if workflow_url:
        body += f"**Workflow run:** {workflow_url}\n\n"
    body += "To ignore any of these roles, add them to `.docs-coverage-ignore.yml`\n\n"
    body += "*This issue is automatically updated by the documentation coverage checker.*"

    return body


def main():
    import json
    import os

    # Paths
    script_dir = Path(__file__).parent
    docs_root = script_dir.parent
    # When running in GitHub Actions, repos are in parent directory of docs
    # When running locally, they should be in the same directory as docs
    parent_dir = docs_root.parent
    saltbox_path = parent_dir / "saltbox"
    sandbox_path = parent_dir / "sandbox"
    config_path = docs_root / ".docs-coverage-ignore.yml"

    # Load ignore configuration
    ignore_config = load_ignore_config(config_path)

    # Ensure ignore config lists are not None
    saltbox_ignored = ignore_config.get("saltbox") or []
    sandbox_ignored = ignore_config.get("sandbox") or []

    # Get roles from repositories
    saltbox_roles_all = get_roles_from_repo(saltbox_path)
    sandbox_roles_all = get_roles_from_repo(sandbox_path)

    # Get documented apps - Saltbox apps are in docs/apps, Sandbox apps are in docs/sandbox/apps
    saltbox_documented_apps = get_documented_apps(docs_root / "docs", "apps")
    sandbox_documented_apps = get_documented_apps(docs_root / "docs", "sandbox/apps")

    # Sanity check: ensure we found roles in both repositories
    if len(saltbox_roles_all) == 0:
        print(f"❌ ERROR: No roles found in Saltbox repository at {saltbox_path}")
        print(f"   Please check that the repository was checked out correctly.")
        sys.exit(1)

    if len(sandbox_roles_all) == 0:
        print(f"❌ ERROR: No roles found in Sandbox repository at {sandbox_path}")
        print(f"   Please check that the repository was checked out correctly.")
        sys.exit(1)

    # Track counts before filtering
    total_ignored = len(saltbox_ignored) + len(sandbox_ignored)

    # Filter out ignored roles for missing docs check
    saltbox_roles = {role for role in saltbox_roles_all if role not in saltbox_ignored}
    sandbox_roles = {role for role in sandbox_roles_all if role not in sandbox_ignored}

    # Find missing documentation - check each repo against its own docs folder
    saltbox_missing = sorted(list(saltbox_roles - saltbox_documented_apps))
    sandbox_missing = sorted(list(sandbox_roles - sandbox_documented_apps))
    total_missing = len(saltbox_missing) + len(sandbox_missing)

    # Find orphaned docs (docs without corresponding roles - check against ALL roles including ignored)
    saltbox_orphaned = sorted(list(saltbox_documented_apps - saltbox_roles_all))
    sandbox_orphaned = sorted(list(sandbox_documented_apps - sandbox_roles_all))
    total_orphaned = len(saltbox_orphaned) + len(sandbox_orphaned)

    # Get workflow URL from environment if available
    workflow_url = os.getenv('GITHUB_WORKFLOW_URL', '')

    # Prepare GitHub Actions output
    github_output = {
        "action": "none",  # none, create_issue, update_issue, close_issue
        "issue_title": "",
        "issue_body": "",
        "close_message": "",
        "saltbox_missing": saltbox_missing,
        "sandbox_missing": sandbox_missing,
        "total_missing": total_missing,
        "total_ignored": total_ignored
    }

    # Report results
    exit_code = 0

    if saltbox_missing or sandbox_missing:
        print("❌ Missing documentation found:\n")

        if saltbox_missing:
            print("Saltbox roles without documentation:")
            for role in saltbox_missing:
                print(f"  - {role}")
            print()

        if sandbox_missing:
            print("Sandbox roles without documentation:")
            for role in sandbox_missing:
                print(f"  - {role}")
            print()

        print(f"Total missing: {total_missing}")
        print(f"\nTo ignore these roles, add them to .docs-coverage-ignore.yml")

        # Prepare issue creation/update data
        github_output["action"] = "create_or_update_issue"
        github_output["issue_title"] = f"📝 Missing documentation for {total_missing} role{'s' if total_missing > 1 else ''}"
        github_output["issue_body"] = generate_issue_body(saltbox_missing, sandbox_missing, total_missing, workflow_url)

        exit_code = 1
    else:
        print("✅ All roles have documentation!")

        # Determine close message based on whether roles were ignored
        if total_ignored > 0:
            github_output["close_message"] = "✅ All missing roles have been documented or added to the ignore list! Closing this issue."
        else:
            github_output["close_message"] = "✅ All roles now have documentation! Closing this issue."

        github_output["action"] = "close_issue"

    # Output JSON for GitHub Actions
    print("\n::group::GitHub Actions Output")
    print(json.dumps(github_output, indent=2))
    print("::endgroup::")

    # Set GitHub Actions outputs using environment file
    github_output_file = os.getenv('GITHUB_OUTPUT')
    if github_output_file:
        with open(github_output_file, 'a') as f:
            f.write(f"action={github_output['action']}\n")
            f.write(f"issue_title={github_output['issue_title']}\n")
            # For multiline output, use heredoc format
            f.write(f"issue_body<<EOF\n{github_output['issue_body']}\nEOF\n")
            f.write(f"close_message={github_output['close_message']}\n")
            f.write(f"total_missing={total_missing}\n")

    # Print orphaned documentation (if any)
    if saltbox_orphaned or sandbox_orphaned:
        print("\n" + "="*60)
        print("⚠️  ORPHANED DOCUMENTATION (docs without roles):")
        print("="*60)

        if saltbox_orphaned:
            print("\nSaltbox docs without corresponding roles:")
            for doc in saltbox_orphaned:
                print(f"  - {doc}")

        if sandbox_orphaned:
            print("\nSandbox docs without corresponding roles:")
            for doc in sandbox_orphaned:
                print(f"  - {doc}")

        print(f"\nTotal orphaned: {total_orphaned}")
        print("These may be deprecated roles or docs that need to be removed/updated.")

    # Print summary statistics
    print("\n" + "="*60)
    print("Summary:")
    print(f"  Saltbox roles: {len(saltbox_roles)}")
    print(f"  Sandbox roles: {len(sandbox_roles)}")
    print(f"  Saltbox documented apps: {len(saltbox_documented_apps)}")
    print(f"  Sandbox documented apps: {len(sandbox_documented_apps)}")
    print(f"  Saltbox ignored: {len(saltbox_ignored)}")
    print(f"  Sandbox ignored: {len(sandbox_ignored)}")
    print(f"  Orphaned docs: {total_orphaned}")
    print("="*60)

    sys.exit(exit_code)


if __name__ == "__main__":
    main()

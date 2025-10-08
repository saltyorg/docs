#!/usr/bin/env python3
"""
Check documentation pages for the Inventory section.

This script:
1. Scans all markdown files in docs/apps and docs/sandbox/apps folders
2. Checks if they contain the managed inventory section markers
3. Reports missing inventory sections
4. Respects ignore lists from .inventory-coverage-ignore.yml
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


def get_app_docs(docs_path: Path, folder: str = "apps") -> Set[str]:
    """Get all app documentation files from docs/{folder} folder."""
    apps_path = docs_path / folder

    if not apps_path.exists():
        return set()

    documented = set()
    for doc_file in apps_path.glob("*.md"):
        # Remove .md extension to get app name
        app_name = doc_file.stem
        documented.add(app_name)

    return documented


def check_inventory_section(doc_file: Path) -> bool:
    """Check if a documentation file contains the inventory section markers."""
    if not doc_file.exists():
        return False

    content = doc_file.read_text()

    # Check for the managed inventory section markers
    has_begin_marker = "<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->" in content
    has_end_marker = "<!-- END SALTBOX MANAGED VARIABLES SECTION -->" in content
    has_inventory_heading = "## Inventory" in content

    return has_begin_marker and has_end_marker and has_inventory_heading


def generate_issue_body(saltbox_missing: List[str], sandbox_missing: List[str], total_missing: int,
                        workflow_url: str) -> str:
    """Generate the GitHub issue body."""
    body = "## Missing Inventory Sections in Documentation\n\n"
    body += f"**Total missing:** {total_missing}\n\n"
    body += "The following app documentation pages are missing the new Inventory section. "
    body += "This section should contain the managed variables section with role configuration options.\n\n"

    if saltbox_missing:
        body += f"### Saltbox Apps ({len(saltbox_missing)})\n\n"
        for app in saltbox_missing:
            body += f"- [ ] [{app}](docs/apps/{app}.md)\n"
        body += "\n"

    if sandbox_missing:
        body += f"### Sandbox Apps ({len(sandbox_missing)})\n\n"
        for app in sandbox_missing:
            body += f"- [ ] [{app}](docs/sandbox/apps/{app}.md)\n"
        body += "\n"

    body += "---\n\n"
    body += "### How to Add the Inventory Section\n\n"
    body += "Add the following section at the end of the app documentation page:\n\n"
    body += "```markdown\n"
    body += "## Inventory\n"
    body += "<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->\n"
    body += "<!-- END SALTBOX MANAGED VARIABLES SECTION -->\n"
    body += "```\n\n"
    body += "---\n\n"

    if workflow_url:
        body += f"**Workflow run:** {workflow_url}\n\n"
    body += "To ignore any of these apps, add them to `.inventory-coverage-ignore.yml`\n\n"
    body += "*This issue is automatically updated by the inventory section checker.*"

    return body


def main():
    import json
    import os

    # Paths
    script_dir = Path(__file__).parent
    docs_root = script_dir.parent
    config_path = docs_root / ".inventory-coverage-ignore.yml"

    # Load ignore configuration
    ignore_config = load_ignore_config(config_path)

    # Ensure ignore config lists are not None
    saltbox_ignored = ignore_config.get("saltbox") or []
    sandbox_ignored = ignore_config.get("sandbox") or []

    # Get documented apps
    saltbox_apps_all = get_app_docs(docs_root / "docs", "apps")
    sandbox_apps_all = get_app_docs(docs_root / "docs", "sandbox/apps")

    # Track counts before filtering
    total_ignored = len(saltbox_ignored) + len(sandbox_ignored)

    # Filter out ignored apps
    saltbox_apps = {app for app in saltbox_apps_all if app not in saltbox_ignored}
    sandbox_apps = {app for app in sandbox_apps_all if app not in sandbox_ignored}

    # Check each app for inventory section
    saltbox_missing = []
    for app in saltbox_apps:
        doc_file = docs_root / "docs" / "apps" / f"{app}.md"
        if not check_inventory_section(doc_file):
            saltbox_missing.append(app)

    sandbox_missing = []
    for app in sandbox_apps:
        doc_file = docs_root / "docs" / "sandbox" / "apps" / f"{app}.md"
        if not check_inventory_section(doc_file):
            sandbox_missing.append(app)

    # Sort results
    saltbox_missing = sorted(saltbox_missing)
    sandbox_missing = sorted(sandbox_missing)
    total_missing = len(saltbox_missing) + len(sandbox_missing)

    # Get workflow URL from environment if available
    workflow_url = os.getenv('GITHUB_WORKFLOW_URL', '')

    # Prepare GitHub Actions output
    github_output = {
        "action": "none",  # none, create_or_update_issue, close_issue
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
        print("❌ App documentation pages missing inventory sections:\n")

        if saltbox_missing:
            print("Saltbox apps without inventory sections:")
            for app in saltbox_missing:
                print(f"  - {app}")
            print()

        if sandbox_missing:
            print("Sandbox apps without inventory sections:")
            for app in sandbox_missing:
                print(f"  - {app}")
            print()

        print(f"Total missing: {total_missing}")
        print(f"\nTo ignore these apps, add them to .inventory-coverage-ignore.yml")

        # Prepare issue creation/update data
        github_output["action"] = "create_or_update_issue"
        github_output["issue_title"] = f"📝 Missing inventory sections in {total_missing} app doc{'s' if total_missing > 1 else ''}"
        github_output["issue_body"] = generate_issue_body(saltbox_missing, sandbox_missing, total_missing,
                                                          workflow_url)

        exit_code = 1
    else:
        print("✅ All app documentation pages have inventory sections!")

        # Determine close message based on whether apps were ignored
        if total_ignored > 0:
            github_output["close_message"] = "✅ All app documentation pages now have inventory sections or have been added to the ignore list! Closing this issue."
        else:
            github_output["close_message"] = "✅ All app documentation pages now have inventory sections! Closing this issue."

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

    # Print summary statistics
    print("\n" + "="*60)
    print("Summary:")
    print(f"  Saltbox apps: {len(saltbox_apps)}")
    print(f"  Sandbox apps: {len(sandbox_apps)}")
    print(f"  Saltbox ignored: {len(saltbox_ignored)}")
    print(f"  Sandbox ignored: {len(sandbox_ignored)}")
    print(f"  Missing inventory sections: {total_missing}")
    print("="*60)

    sys.exit(exit_code)


if __name__ == "__main__":
    main()

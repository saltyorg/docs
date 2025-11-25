#!/usr/bin/env python3
"""
Update sb.md documentation with the latest sb-go --help output.

This script:
1. Downloads the latest sb-go binary from GitHub releases
2. Runs `sb --help` to get the CLI help text
3. Updates the managed section in sb.md with the formatted output
"""

import sys
import re
import tempfile
import subprocess
import stat
from pathlib import Path
from typing import Optional

# GitHub repository details
REPO_OWNER = "saltyorg"
REPO_NAME = "sb-go"
BINARY_NAME = "sb-go"

def get_latest_release_url() -> Optional[str]:
    """Fetch the latest release download URL for the sb-go binary.

    Returns:
        URL to the latest Linux amd64 binary, or None if not found
    """
    import urllib.request
    import json

    api_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases/latest"

    try:
        with urllib.request.urlopen(api_url) as response:
            data = json.loads(response.read())

        # Find the Linux amd64 binary
        for asset in data.get('assets', []):
            name = asset.get('name', '')
            if 'linux' in name.lower() and 'amd64' in name.lower():
                return asset.get('browser_download_url')

        print(f"Error: Could not find Linux amd64 binary in release assets", file=sys.stderr)
        return None

    except Exception as e:
        print(f"Error: Failed to fetch latest release: {e}", file=sys.stderr)
        return None

def download_binary(url: str, dest_path: Path) -> bool:
    """Download the binary from the given URL.

    Args:
        url: URL to download from
        dest_path: Path to save the binary to

    Returns:
        True if successful, False otherwise
    """
    import urllib.request

    try:
        print(f"Downloading from {url}...", file=sys.stderr)
        urllib.request.urlretrieve(url, dest_path)

        # Make executable
        dest_path.chmod(dest_path.stat().st_mode | stat.S_IEXEC)

        print(f"Downloaded to {dest_path}", file=sys.stderr)
        return True

    except Exception as e:
        print(f"Error: Failed to download binary: {e}", file=sys.stderr)
        return False

def get_help_output(binary_path: Path) -> Optional[str]:
    """Run the binary with --help and capture output.

    Args:
        binary_path: Path to the sb-go binary

    Returns:
        Help text output, or None if failed
    """
    try:
        result = subprocess.run(
            [str(binary_path), '-h'],
            capture_output=True,
            text=True,
            timeout=10
        )

        # sb-go returns the help text regardless of exit code
        return result.stdout.strip()

    except subprocess.TimeoutExpired:
        print("Error: Command timed out", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error: Failed to run binary: {e}", file=sys.stderr)
        return None

def format_help_as_markdown(help_text: str) -> str:
    """Format the help output as markdown similar to the current sb.md format.

    Args:
        help_text: Raw help text from sb --help

    Returns:
        Formatted markdown string
    """
    # The output should be in a console code block with termynal comment
    lines = [
        "",
        "<!-- termynal -->",
        "",
        "```console",
        "$ sb --help",
    ]

    # Add each line of help output
    for line in help_text.split('\n'):
        lines.append(line)

    lines.append("```")
    lines.append("")

    return '\n'.join(lines)

def update_docs_file(docs_path: Path, new_content: str) -> bool:
    """Update the documentation file with new content.

    Args:
        docs_path: Path to the sb.md file
        new_content: New content to insert

    Returns:
        True if successful, False otherwise
    """
    try:
        # Read existing content
        with open(docs_path) as f:
            original_content = f.read()

        # Check if managed section exists
        if '<!-- BEGIN SALTBOX MANAGED CLI SECTION -->' not in original_content:
            print(f"Warning: Documentation file does not contain managed section markers", file=sys.stderr)
            print(f"Looking for: <!-- BEGIN SALTBOX MANAGED CLI SECTION -->", file=sys.stderr)

            # Try to replace the existing termynal section
            # Pattern: from "# Saltbox CLI" to the end of the console code block
            pattern = r'(# Saltbox CLI\n)<!-- termynal -->.*?```\n'
            if re.search(pattern, original_content, re.DOTALL):
                print(f"Found existing termynal section, replacing it...", file=sys.stderr)
                replacement = (
                    r'\1<!-- BEGIN SALTBOX MANAGED CLI SECTION -->\n'
                    f'<!-- This section is managed by scripts/update-sb-help.py - DO NOT EDIT MANUALLY -->{new_content}\n'
                    '<!-- END SALTBOX MANAGED CLI SECTION -->\n'
                )
                new_file_content = re.sub(pattern, replacement, original_content, flags=re.DOTALL)
            else:
                print(f"Error: Could not find section to replace", file=sys.stderr)
                return False
        else:
            # Replace the managed section
            pattern = r'<!-- BEGIN SALTBOX MANAGED CLI SECTION -->.*?<!-- END SALTBOX MANAGED CLI SECTION -->'

            def build_replacement(match):
                return f'<!-- BEGIN SALTBOX MANAGED CLI SECTION -->\n<!-- This section is managed by scripts/update-sb-help.py - DO NOT EDIT MANUALLY -->{new_content}\n<!-- END SALTBOX MANAGED CLI SECTION -->'

            new_file_content = re.sub(pattern, build_replacement, original_content, flags=re.DOTALL)

        # Write updated content
        with open(docs_path, 'w') as f:
            f.write(new_file_content)

        print(f"Successfully updated {docs_path}", file=sys.stderr)
        return True

    except Exception as e:
        print(f"Error: Failed to update documentation: {e}", file=sys.stderr)
        return False

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Update sb.md with latest sb-go --help output',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python3 update-sb-help.py
  python3 update-sb-help.py --docs-path /custom/path/sb.md
  python3 update-sb-help.py --binary-path /custom/sb-go
        '''
    )

    parser.add_argument(
        '--docs-path',
        metavar='PATH',
        default='/opt/git/docs/docs/saltbox/basics/sb.md',
        help='Path to sb.md file (default: /opt/git/docs/docs/saltbox/basics/sb.md)'
    )

    parser.add_argument(
        '--binary-path',
        metavar='PATH',
        help='Path to existing sb-go binary (skips download if provided)'
    )

    args = parser.parse_args()

    docs_path = Path(args.docs_path)
    if not docs_path.exists():
        print(f"Error: Documentation file not found: {docs_path}", file=sys.stderr)
        sys.exit(1)

    # Get or download binary and get help output
    if args.binary_path:
        binary_path = Path(args.binary_path)
        if not binary_path.exists():
            print(f"Error: Binary not found: {binary_path}", file=sys.stderr)
            sys.exit(1)

        help_text = get_help_output(binary_path)
        if not help_text:
            sys.exit(1)
    else:
        # Download latest release
        download_url = get_latest_release_url()
        if not download_url:
            sys.exit(1)

        # Create temp directory for download
        with tempfile.TemporaryDirectory() as tmpdir:
            binary_path = Path(tmpdir) / BINARY_NAME

            if not download_binary(download_url, binary_path):
                sys.exit(1)

            # Get help output while binary still exists
            help_text = get_help_output(binary_path)
            if not help_text:
                sys.exit(1)

    # Format as markdown
    markdown_content = format_help_as_markdown(help_text)

    # Update documentation
    if not update_docs_file(docs_path, markdown_content):
        sys.exit(1)

    print("Documentation updated successfully!")

if __name__ == '__main__':
    main()

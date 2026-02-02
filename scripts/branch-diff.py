#!/usr/bin/env python3
"""Generate an HTML diff report comparing two GitHub branches."""

import os
import sys
import tarfile
import tempfile
import shutil
import difflib
import urllib.request
from pathlib import Path
from datetime import datetime
from html import escape

# Default configuration
DEFAULT_REPOS = [
    {
        "url": "https://github.com/saltyorg/Saltbox",
        "branch_a": "pre-role-refactor",
        "branch_b": "master",
        "output": "saltbox.html",
    },
    {
        "url": "https://github.com/saltyorg/Sandbox",
        "branch_a": "pre-role-refactor",
        "branch_b": "master",
        "output": "sandbox.html",
    },
]


def download_branch(repo_path: str, branch: str, dest: Path):
    """Download and extract a branch tarball."""
    url = f"https://codeload.github.com/{repo_path}/tar.gz/refs/heads/{branch}"
    print(f"Fetching {branch}...")
    
    tarball_path = dest.parent / f"{branch}.tar.gz"
    urllib.request.urlretrieve(url, tarball_path)
    
    with tarfile.open(tarball_path, "r:gz") as tar:
        tar.extractall(dest.parent)
    
    # Find extracted directory and rename
    extracted = next(dest.parent.glob(f"*-{branch}*"))
    extracted.rename(dest)
    tarball_path.unlink()


def get_all_files(directory: Path) -> set[str]:
    """Get all file paths relative to directory."""
    files = set()
    for path in directory.rglob("*"):
        if path.is_file():
            files.add(str(path.relative_to(directory)))
    return files


def is_binary(filepath: Path) -> bool:
    """Check if file is binary."""
    try:
        with open(filepath, "rb") as f:
            chunk = f.read(8192)
            return b"\x00" in chunk
    except:
        return True


def generate_diff(file_a: Path | None, file_b: Path | None, filename: str) -> tuple[str, list[str]]:
    """Generate diff lines for a file. Returns (change_type, diff_lines)."""
    
    if file_a is None:
        # Added file
        if is_binary(file_b):
            return "added", ["(Binary file)"]
        content = file_b.read_text(errors="replace").splitlines()
        return "added", [f"+ {line}" for line in content]
    
    if file_b is None:
        # Removed file
        if is_binary(file_a):
            return "removed", ["(Binary file)"]
        content = file_a.read_text(errors="replace").splitlines()
        return "removed", [f"- {line}" for line in content]
    
    # Modified file
    if is_binary(file_a) or is_binary(file_b):
        return "modified", ["(Binary file changed)"]
    
    content_a = file_a.read_text(errors="replace").splitlines()
    content_b = file_b.read_text(errors="replace").splitlines()
    
    diff = list(difflib.unified_diff(content_a, content_b, lineterm=""))
    
    # Skip the --- and +++ header lines
    if len(diff) > 2:
        diff = diff[2:]
    
    return "modified", diff


def generate_html(changes: list[dict], stats: dict, repo_path: str, branch_a: str, branch_b: str) -> str:
    """Generate the HTML report."""
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Branch Diff Report - {repo_path}</title>
    <style>
        :root {{
            --bg-primary: #0d1117;
            --bg-secondary: #161b22;
            --bg-tertiary: #21262d;
            --text-primary: #c9d1d9;
            --text-secondary: #8b949e;
            --border-color: #30363d;
            --accent-green: #238636;
            --accent-red: #da3633;
            --diff-add-bg: rgba(46, 160, 67, 0.15);
            --diff-del-bg: rgba(248, 81, 73, 0.15);
            --diff-add-text: #7ee787;
            --diff-del-text: #ffa198;
            --diff-hunk-bg: rgba(56, 139, 253, 0.15);
            --diff-hunk-text: #79c0ff;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.5;
            padding: 2rem;
        }}
        .container {{ max-width: 1400px; margin: 0 auto; }}
        header {{
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 1.5rem;
            margin-bottom: 2rem;
        }}
        h1 {{ font-size: 1.75rem; font-weight: 600; margin-bottom: 0.5rem; }}
        .meta {{ color: var(--text-secondary); font-size: 0.875rem; }}
        .meta code {{ background: var(--bg-tertiary); padding: 0.1rem 0.4rem; border-radius: 3px; }}
        .summary {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 2rem;
        }}
        .stat-card {{
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 1rem;
        }}
        .stat-card h3 {{
            font-size: 0.75rem;
            text-transform: uppercase;
            color: var(--text-secondary);
            margin-bottom: 0.25rem;
        }}
        .stat-card .value {{ font-size: 1.5rem; font-weight: 600; }}
        .stat-card.added .value {{ color: var(--diff-add-text); }}
        .stat-card.removed .value {{ color: var(--diff-del-text); }}
        .stat-card.modified .value {{ color: var(--diff-hunk-text); }}
        .toc {{
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 1rem;
            margin-bottom: 2rem;
        }}
        .toc h2 {{ font-size: 1rem; margin-bottom: 0.75rem; }}
        .toc-list {{
            list-style: none;
            max-height: 300px;
            overflow-y: auto;
            font-size: 0.875rem;
        }}
        .toc-list li {{ padding: 0.25rem 0; }}
        .toc-list a {{ color: var(--diff-hunk-text); text-decoration: none; }}
        .toc-list a:hover {{ text-decoration: underline; }}
        .badge {{
            font-size: 0.7rem;
            padding: 0.1rem 0.4rem;
            border-radius: 3px;
            margin-left: 0.5rem;
        }}
        .badge.added {{ background: var(--accent-green); color: white; }}
        .badge.removed {{ background: var(--accent-red); color: white; }}
        .badge.modified {{ background: var(--bg-tertiary); color: var(--text-secondary); }}
        .file-section {{
            margin-bottom: 1.5rem;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            overflow: hidden;
        }}
        .file-header {{
            background: var(--bg-secondary);
            padding: 0.75rem 1rem;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        .file-header h3 {{
            font-size: 0.875rem;
            font-weight: 600;
            font-family: ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace;
        }}
        .diff-content {{
            overflow-x: auto;
            font-family: ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace;
            font-size: 0.8rem;
            line-height: 1.4;
        }}
        .diff-content pre {{ margin: 0; padding: 1rem; white-space: pre; }}
        .diff-line {{ display: block; padding: 0 0.5rem; }}
        .diff-line.add {{ background: var(--diff-add-bg); color: var(--diff-add-text); }}
        .diff-line.del {{ background: var(--diff-del-bg); color: var(--diff-del-text); }}
        .diff-line.hunk {{ background: var(--diff-hunk-bg); color: var(--diff-hunk-text); }}
        .diff-line.context {{ color: var(--text-secondary); }}
        .collapse-btn {{
            background: var(--bg-tertiary);
            border: 1px solid var(--border-color);
            color: var(--text-secondary);
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.75rem;
            margin-left: auto;
        }}
        .collapse-btn:hover {{ background: var(--border-color); }}
        .collapsed .diff-content {{ display: none; }}
        footer {{
            margin-top: 3rem;
            padding-top: 1.5rem;
            border-top: 1px solid var(--border-color);
            text-align: center;
            color: var(--text-secondary);
            font-size: 0.875rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Branch Comparison Report</h1>
            <p class="meta">
                <strong>Repository:</strong> {repo_path}<br>
                <strong>Comparing:</strong> <code>{branch_a}</code> → <code>{branch_b}</code><br>
                <strong>Generated:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            </p>
        </header>
        
        <div class="summary">
            <div class="stat-card added">
                <h3>Files Added</h3>
                <div class="value">{stats["added"]}</div>
            </div>
            <div class="stat-card removed">
                <h3>Files Removed</h3>
                <div class="value">{stats["removed"]}</div>
            </div>
            <div class="stat-card modified">
                <h3>Files Modified</h3>
                <div class="value">{stats["modified"]}</div>
            </div>
            <div class="stat-card">
                <h3>Total Changes</h3>
                <div class="value">{stats["added"] + stats["removed"] + stats["modified"]}</div>
            </div>
        </div>
        
        <div class="toc">
            <h2>Changed Files</h2>
            <ul class="toc-list">
'''
    
    # TOC
    for i, change in enumerate(changes):
        html += f'                <li><a href="#file-{i}">{escape(change["file"])}</a><span class="badge {change["type"]}">{change["type"]}</span></li>\n'
    
    html += '''            </ul>
            <div style="margin-top: 0.75rem;">
                <button onclick="document.querySelectorAll('.file-section').forEach(s => s.classList.remove('collapsed'))" style="background: var(--bg-tertiary); border: 1px solid var(--border-color); color: var(--text-secondary); padding: 0.25rem 0.5rem; border-radius: 4px; cursor: pointer; font-size: 0.75rem; margin-right: 0.5rem;">Expand All</button>
                <button onclick="document.querySelectorAll('.file-section').forEach(s => s.classList.add('collapsed'))" style="background: var(--bg-tertiary); border: 1px solid var(--border-color); color: var(--text-secondary); padding: 0.25rem 0.5rem; border-radius: 4px; cursor: pointer; font-size: 0.75rem;">Collapse All</button>
            </div>
        </div>
        
        <main>
'''
    
    # File sections
    for i, change in enumerate(changes):
        html += f'''            <section class="file-section collapsed" id="file-{i}">
                <div class="file-header">
                    <span class="badge {change["type"]}">{change["type"]}</span>
                    <h3>{escape(change["file"])}</h3>
                    <button class="collapse-btn" onclick="this.closest('.file-section').classList.toggle('collapsed')">Toggle</button>
                </div>
                <div class="diff-content"><pre>'''
        
        for line in change["diff"]:
            escaped_line = escape(line)
            if line.startswith("+"):
                html += f'<span class="diff-line add">{escaped_line}</span>'
            elif line.startswith("-"):
                html += f'<span class="diff-line del">{escaped_line}</span>'
            elif line.startswith("@@"):
                html += f'<span class="diff-line hunk">{escaped_line}</span>'
            else:
                html += f'<span class="diff-line context">{escaped_line}</span>'
        
        html += '''</pre></div>
            </section>
'''
    
    html += '''        </main>
        
        <footer>
            <p>Generated by branch-diff.py</p>
        </footer>
    </div>
    
    <script>
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                document.querySelectorAll('.file-section').forEach(s => s.classList.add('collapsed'));
            }
        });
    </script>
</body>
</html>'''
    
    return html


def generate_report(repo_url: str, branch_a: str, branch_b: str, output_file: str):
    """Generate a diff report for a single repository."""
    repo_path = repo_url.replace("https://github.com/", "")
    
    print(f"\n=== Branch Diff Report Generator ===")
    print(f"Repository: {repo_path}")
    print(f"Comparing: {branch_a} vs {branch_b}")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        dir_a = temp_path / branch_a
        dir_b = temp_path / branch_b
        
        download_branch(repo_path, branch_a, dir_a)
        download_branch(repo_path, branch_b, dir_b)
        
        print("Comparing files...")
        
        files_a = get_all_files(dir_a)
        files_b = get_all_files(dir_b)
        
        added = files_b - files_a
        removed = files_a - files_b
        common = files_a & files_b
        
        # Find modified files
        modified = set()
        for f in common:
            path_a = dir_a / f
            path_b = dir_b / f
            if path_a.read_bytes() != path_b.read_bytes():
                modified.add(f)
        
        print(f"Files in {branch_a}: {len(files_a)}")
        print(f"Files in {branch_b}: {len(files_b)}")
        print(f"Added: {len(added)}, Removed: {len(removed)}, Modified: {len(modified)}")
        
        # Generate diffs
        changes = []
        
        for f in sorted(added):
            change_type, diff = generate_diff(None, dir_b / f, f)
            changes.append({"file": f, "type": change_type, "diff": diff})
        
        for f in sorted(removed):
            change_type, diff = generate_diff(dir_a / f, None, f)
            changes.append({"file": f, "type": change_type, "diff": diff})
        
        for f in sorted(modified):
            change_type, diff = generate_diff(dir_a / f, dir_b / f, f)
            changes.append({"file": f, "type": change_type, "diff": diff})
        
        stats = {"added": len(added), "removed": len(removed), "modified": len(modified)}
        
        print(f"Generating HTML report...")
        html = generate_html(changes, stats, repo_path, branch_a, branch_b)
        
        Path(output_file).write_text(html)
        print(f"Report saved to: {output_file}")


def main():
    for repo in DEFAULT_REPOS:
        generate_report(
            repo_url=repo["url"],
            branch_a=repo["branch_a"],
            branch_b=repo["branch_b"],
            output_file=repo["output"],
        )


if __name__ == "__main__":
    main()

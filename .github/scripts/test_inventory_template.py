#!/usr/bin/env python3
"""Exercise the canonical inventory template through the sb-docs consumer."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


TAB_PATTERN = re.compile(r'^=== "([^"]+)"$', re.MULTILINE)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def section(name: str, variables: list[str]) -> str:
    return "\n".join(
        [
            "########################################",
            f"# {name}",
            "########################################",
            *variables,
            "",
        ]
    )


def role_defaults(role: str, sections: list[str], *, empty_docker_plus: bool = False, instances: bool = False) -> str:
    variables = {
        "Basics": [f"{role}_enabled: true"],
        "Docker": [f'{role}_role_docker_image_repo: "example/image"'],
        "Postgres": [f"{role}_postgres_enabled: true"],
    }
    if empty_docker_plus:
        variables["Docker"].append(f'{role}_role_docker_custom_option: "defined"')
    if instances:
        variables["Basics"].insert(0, f'{role}_instances: ["{role}"]')
    return "---\n" + "".join(section(name, variables[name]) for name in sections)


def frontmatter(*, hide_docker: bool = False) -> str:
    hidden = "\n    hide_sections:\n      - Docker" if hide_docker else ""
    return f"---\nsaltbox_automation:\n  inventory:{hidden}\n---\n"


def prepare_layout(root: Path, template: Path) -> Path:
    saltbox = root / "saltbox"
    sandbox = root / "sandbox"
    docs = root / "docs"
    (saltbox / "roles").mkdir(parents=True)
    (sandbox / "roles").mkdir(parents=True)
    (docs / "docs" / "apps").mkdir(parents=True)
    (docs / "docs" / "sandbox" / "apps").mkdir(parents=True)
    (docs / "templates").mkdir(parents=True)
    shutil.copyfile(template, docs / "templates" / "inventory.md.tmpl")

    write(
        saltbox / "inventories" / "group_vars" / "all.yml",
        '---\nfixture: "{{ lookup(\'role_var\', \'_depends_on\', default=\'\') }}"\n',
    )
    write(saltbox / "resources" / "tasks" / "directories" / "create_directories.yml", "---\n[]\n")
    write(
        saltbox / "resources" / "tasks" / "docker" / "create.yml",
        '---\nfixture: "{{ lookup(\'docker_var\', \'_docker_custom_option\', default=\'\') }}"\n',
    )

    cases = {
        "middle": (["Basics", "Docker", "Postgres"], False, False, False),
        "docker_final": (["Basics", "Postgres", "Docker"], False, False, False),
        "docker_hidden": (["Basics", "Docker", "Postgres"], True, False, False),
        "empty_docker_plus": (["Basics", "Docker", "Postgres"], False, True, False),
        "multi": (["Basics", "Docker", "Postgres"], False, False, True),
    }
    for role, (sections, hidden, empty, instances) in cases.items():
        write(
            saltbox / "roles" / role / "defaults" / "main.yml",
            role_defaults(role, sections, empty_docker_plus=empty, instances=instances),
        )
        write(docs / "docs" / "apps" / f"{role}.md", frontmatter(hide_docker=hidden))

    config = root / "config.yml"
    write(
        config,
        f"""repositories:
  saltbox: {saltbox}
  sandbox: {sandbox}
  docs: {docs}
global_overrides:
  variables:
    _depends_on:
      description: Set container dependencies
      default: null
      type: string
docker_overrides:
  ignore_suffixes: []
  variables: {{}}
docker_variables: {{}}
markers:
  variables: SALTBOX MANAGED VARIABLES SECTION
""",
    )
    return config


def generate(sb_docs: Path, config: Path, role: str) -> str:
    result = subprocess.run(
        [str(sb_docs), "--config", str(config), "generate", role],
        check=False,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        raise AssertionError(f"sb-docs generate {role} failed:\n{result.stderr}")
    return result.stdout


def assert_tabs(output: str, expected: list[str], role: str) -> None:
    actual = TAB_PATTERN.findall(output)
    if actual != expected:
        raise AssertionError(f"{role} tabs = {actual!r}, want {expected!r}")


def run(sb_docs: Path, template: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="docs-inventory-template-") as temp:
        config = prepare_layout(Path(temp), template)
        expected_middle = ["Basics", "Docker", "Docker+", "Postgres", "Global Override Options"]
        assert_tabs(generate(sb_docs, config, "middle"), expected_middle, "middle")
        assert_tabs(
            generate(sb_docs, config, "docker_final"),
            ["Basics", "Postgres", "Docker", "Docker+", "Global Override Options"],
            "docker_final",
        )
        assert_tabs(
            generate(sb_docs, config, "docker_hidden"),
            ["Basics", "Postgres", "Global Override Options"],
            "docker_hidden",
        )
        assert_tabs(
            generate(sb_docs, config, "empty_docker_plus"),
            ["Basics", "Docker", "Postgres", "Global Override Options"],
            "empty_docker_plus",
        )
        multi = generate(sb_docs, config, "multi")
        assert_tabs(multi, expected_middle, "multi")
        for variable in ("multi_role_docker_custom_option", "multi2_docker_custom_option"):
            if variable not in multi:
                raise AssertionError(f"multi output does not contain {variable}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sb-docs", type=Path, default=Path("sb-docs"))
    parser.add_argument(
        "--template",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "templates" / "inventory.md.tmpl",
    )
    args = parser.parse_args()
    run(args.sb_docs, args.template)
    print("inventory template consumer scenarios passed")


if __name__ == "__main__":
    main()

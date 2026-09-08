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


def role_defaults(
    role: str,
    sections: list[str],
    *,
    empty_docker_plus: bool = False,
    instances: bool = False,
) -> str:
    variables = {
        "Basics": [f"{role}_enabled: true"],
        "Docker": [f'{role}_role_docker_image_repo: "example/image"'],
        "Postgres": [f"{role}_postgres_enabled: true"],
    }
    if empty_docker_plus:
        variables["Docker"].extend(
            [
                f'{role}_role_docker_custom_option: "defined"',
                f"{role}_role_docker_labeled: false",
                f"{role}_role_docker_gpu_enabled: false",
                f'{role}_role_docker_gpu_mode: "default"',
            ]
        )
    if instances:
        variables["Basics"].insert(0, f'{role}_instances: ["{role}"]')
    return "---\n" + "".join(section(name, variables[name]) for name in sections)


def frontmatter(*, hide_docker: bool = False, example_overrides: str = "") -> str:
    hidden = "\n    hide_sections:\n      - Docker" if hide_docker else ""
    examples = f"\n    example_overrides:\n{example_overrides}" if example_overrides else ""
    return f"---\nsaltbox_automation:\n  inventory:{hidden}{examples}\n---\n"


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
        """---
plain: "{{ lookup('docker_var', '_docker_custom_option', default='') }}"
labeled: "{{ lookup('docker_var', '_docker_labeled', default=false) }}"
gpu_enabled: "{{ lookup('docker_var', '_docker_gpu_enabled', default=false) }}"
gpu_mode: "{{ lookup('docker_var', '_docker_gpu_mode', default='') }}"
""",
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
      example: |
        ```yaml
        {{variable}}: ["{{role}}-legacy"]
        ```
docker_overrides:
  ignore_suffixes: []
  variables:
    _docker_labeled:
      description: A labeled Docker override
      default: "false"
      type: bool
      example: |
        ```yaml
        {{variable}}: true
        ```
    _docker_gpu_enabled:
      default: "false"
      type: bool
    _docker_gpu_mode:
      default: '"default"'
      type: string
  groups:
    - name: GPU
      primary: _docker_gpu_enabled
      companions:
        - _docker_gpu_mode
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


def assert_contains(output: str, expected: str, scenario: str) -> None:
    if expected not in output:
        raise AssertionError(f"{scenario} output does not contain:\n{expected}")


def assert_not_contains(output: str, unexpected: str, scenario: str) -> None:
    if unexpected in output:
        raise AssertionError(f"{scenario} output unexpectedly contains:\n{unexpected}")


def assert_markdown_rendering(output: str, scenario: str) -> None:
    try:
        import markdown
    except ImportError as error:
        raise AssertionError(
            "--render-markdown requires the documentation Python environment"
        ) from error

    rendered = markdown.markdown(
        output,
        extensions=[
            "admonition",
            "attr_list",
            "pymdownx.details",
            "pymdownx.highlight",
            "pymdownx.superfences",
            "pymdownx.tabbed",
        ],
        extension_configs={"pymdownx.tabbed": {"alternate_style": True}},
    )
    for expected in (
        '<div class="admonition example',
        '<details class="variable',
        '<div class="highlight"><pre>',
    ):
        if expected not in rendered:
            raise AssertionError(f"{scenario} rendered HTML does not contain {expected!r}")
    if "````yaml" in rendered:
        raise AssertionError(f"{scenario} leaked a four-backtick fence into rendered HTML")
    if scenario == "multi-instance examples":
        for scope_class in ("sb-show-on-unchecked", "sb-show-on-checked"):
            if f'<div class="admonition example {scope_class}">' not in rendered:
                raise AssertionError(f"{scenario} lost the {scope_class} admonition class")
    if scenario == "native examples" and "complete fence" not in rendered:
        raise AssertionError(f"{scenario} lost content nested inside the longer code fence")


def run(sb_docs: Path, template: Path, *, render_markdown: bool = False) -> None:
    with tempfile.TemporaryDirectory(prefix="docs-inventory-template-") as temp:
        root = Path(temp)
        config = prepare_layout(root, template)
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

        multi_defaults = "---\n" + "".join(
            [
                section("Basics", ['multi_instances: ["multi"]', "multi_enabled: true"]),
                section(
                    "Settings",
                    [
                        "# Advanced - Sub-section Start",
                        'multi_setting: "default"',
                        'multi_instance_only: "default"',
                        "# Advanced - Sub-section End",
                    ],
                ),
                section("Docker", ['multi_role_docker_image_repo: "example/image"']),
                section("Postgres", ["multi_postgres_enabled: true"]),
            ]
        )
        write(root / "saltbox" / "roles" / "multi" / "defaults" / "main.yml", multi_defaults)
        write(
            root / "docs" / "docs" / "apps" / "multi.md",
            frontmatter(
                example_overrides="""      multi_instances: ["multi", "blue"]
      multi_setting: {scope: role}
      multi2_setting: null
      multi2_instance_only: []
      multi_role_docker_image_repo: "role-image"
      multi2_docker_image_repo: "instance-image"
      multi_postgres_enabled: false
      multi2_postgres_enabled: null
      multi_role_docker_custom_option: ["shared"]
      multi2_docker_labeled: false
      multi2_depends_on: []"""),
        )
        multi = generate(sb_docs, config, "multi")
        assert_contains(
            multi,
            """        !!! example "Example Override"

            ```yaml
            multi_instances: ["multi", "blue"]
            ```""",
            "native Basics replacement",
        )
        assert_not_contains(multi, 'multi_instances: ["multi", "multi2"]', "duplicate Basics fallback")
        assert_contains(
            multi,
            """            !!! example sb-show-on-unchecked "Example Override"

                ```yaml
                multi_setting: {scope: role}
                ```

            !!! example sb-show-on-checked "Example Override"

                ```yaml
                multi2_setting: null
                ```""",
            "multi-instance subsection scopes",
        )
        assert_contains(
            multi,
            """            !!! example sb-show-on-checked "Example Override"

                ```yaml
                multi2_instance_only: []
                ```""",
            "instance-only native example without reusable metadata",
        )
        assert_not_contains(
            multi,
            "multi_instance_only: []",
            "missing role-scoped native example",
        )
        assert_contains(
            multi,
            """        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            multi_role_docker_image_repo: "role-image"
            ```

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            multi2_docker_image_repo: "instance-image"
            ```""",
            "multi-instance declared Docker scopes",
        )
        assert_contains(
            multi,
            """        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            multi_postgres_enabled: false
            ```

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            multi2_postgres_enabled: null
            ```""",
            "multi-instance ordinary scopes",
        )
        assert_contains(
            multi,
            """        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            multi_role_docker_custom_option: ["shared"]
            ```

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            multi2_docker_custom_option: ["shared"]
            ```""",
            "Docker+ canonical fallback without metadata",
        )
        assert_contains(
            multi,
            """        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            multi_role_docker_labeled: true
            ```


        !!! example sb-show-on-checked "Example Override"

            ```yaml
            multi2_docker_labeled: false
            ```""",
            "Docker+ reusable role fallback and native instance",
        )
        assert_contains(
            multi,
            """        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            multi_role_depends_on: ["multi-legacy"]
            ```


        !!! example sb-show-on-checked "Example Override"

            ```yaml
            multi2_depends_on: []
            ```""",
            "global reusable role fallback and native instance",
        )

        native_defaults = "---\n" + "".join(
            [
                section(
                    "Basics",
                    [
                        "native_enabled: true",
                        'native_empty: "default"',
                        "# Skip docs",
                        'native_hidden: "internal"',
                    ],
                ),
                section(
                    "Settings",
                    [
                        "# Advanced - Sub-section Start",
                        'native_nested: "default"',
                        "# Advanced - Sub-section End",
                    ],
                ),
                section(
                    "Docker",
                    [
                        'native_role_docker_image_repo: "example/image"',
                        "native_role_docker_gpu_enabled: false",
                    ],
                ),
            ]
        )
        write(root / "saltbox" / "roles" / "native" / "defaults" / "main.yml", native_defaults)
        write(
            root / "docs" / "docs" / "apps" / "native.md",
            frontmatter(
                example_overrides="""      native_enabled: false
      native_empty: ""
      native_nested:
        enabled: false
        note: |-
          ```
          complete fence
      native_role_docker_image_repo: null
      native_role_docker_custom_option: []
      native_role_docker_labeled: false
      native_role_docker_gpu_enabled: true
      native_role_docker_gpu_mode: "compute"
      native_role_depends_on: {}
      native_hidden: "must stay hidden"
"""),
        )
        native = generate(sb_docs, config, "native")
        assert_contains(
            native,
            """        native_enabled: true
        ```

        !!! example "Example Override"

            ```yaml
            native_enabled: false
            ```""",
            "ordinary native scalar",
        )
        assert_contains(
            native,
            """        native_empty: "default"
        ```

        !!! example "Example Override"

            ```yaml
            native_empty: ""
            ```""",
            "empty string",
        )
        assert_contains(
            native,
            """            native_nested: "default"
            ```

            !!! example "Example Override"

                ````yaml
                native_nested:
                  enabled: false
                  note: |-
                    ```
                    complete fence
                ````""",
            "subsection nesting and complete fence",
        )
        assert_contains(
            native,
            """        native_role_docker_image_repo: "example/image"
        ```

        !!! example "Example Override"

            ```yaml
            native_role_docker_image_repo: null
            ```""",
            "declared Docker null",
        )
        assert_contains(
            native,
            """        !!! example "Example Override"

            ```yaml
            native_role_docker_custom_option: []
            ```""",
            "Docker+ without metadata",
        )
        assert_contains(
            native,
            """        !!! example "Example Override"

            ```yaml
            native_role_docker_labeled: false
            ```""",
            "Docker+ with metadata",
        )
        assert_not_contains(native, "native_role_docker_labeled: true", "native replaces reusable Docker example")
        assert_contains(
            native,
            """        !!! example "Example Override"

            ```yaml
            native_role_docker_gpu_enabled: true
            ```""",
            "promoted Docker group primary",
        )
        assert_contains(
            native,
            """        !!! example "Example Override"

            ```yaml
            native_role_docker_gpu_mode: "compute"
            ```""",
            "promoted Docker group companion",
        )
        assert_contains(
            native,
            """        !!! example "Example Override"

            ```yaml
            native_role_depends_on: {}
            ```""",
            "global native example",
        )
        assert_not_contains(native, "native_hidden", "hidden variable")
        if render_markdown:
            assert_markdown_rendering(multi, "multi-instance examples")
            assert_markdown_rendering(native, "native examples")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sb-docs", type=Path, default=Path("sb-docs"))
    parser.add_argument(
        "--template",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "templates" / "inventory.md.tmpl",
    )
    parser.add_argument(
        "--render-markdown",
        action="store_true",
        help="also render scenarios with the documentation Markdown dependencies",
    )
    args = parser.parse_args()
    run(args.sb_docs, args.template, render_markdown=args.render_markdown)
    print("inventory template consumer scenarios passed")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exercise tagged example metadata through MkDocs' page lifecycle."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from mkdocs.config import load_config
from mkdocs.exceptions import PluginError
from mkdocs.structure.files import File
from mkdocs.structure.pages import Page


REPO_ROOT = Path(__file__).resolve().parents[2]


class ExampleMetadataHookTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = load_config(config_file=str(REPO_ROOT / "mkdocs.yml"))
        if not cls.config.plugins.events["page_read_source"]:
            raise AssertionError("mkdocs.yml did not register the example metadata hook")

    def read_page(self, source: bytes) -> tuple[Page, bytes]:
        with tempfile.TemporaryDirectory(prefix="docs-example-metadata-") as temp:
            root = Path(temp)
            source_path = root / "fixture.md"
            source_path.write_bytes(source)
            file = File("fixture.md", str(root), str(root / "site"), True)
            page = Page("Fixture", file, self.config)
            page.read_source(self.config)
            return page, source_path.read_bytes()

    def test_tagged_examples_do_not_hide_metadata_or_expose_frontmatter(self) -> None:
        source = b"""---\r
title: Tagged example\r
tags: [example, yaml]\r
saltbox_automation:\r
  inventory:\r
    example_overrides:\r
      app_secret: !vault |\r
        $ANSIBLE_VAULT;1.1;AES256\r
        ciphertext\r
      app_nested: &nested\r
        value: !unsafe \"{{ user.domain }}\"\r
      app_copy: *nested\r
...\r
# Body\r
\r
```yaml\r
app_secret: !vault |\r
  $ANSIBLE_VAULT;1.1;AES256\r
  ciphertext\r
app_nested:\r
  value: !unsafe \"{{ user.domain }}\"\r
```\r
"""

        page, source_after = self.read_page(source)

        self.assertEqual(page.meta["title"], "Tagged example")
        self.assertEqual(page.meta["tags"], ["example", "yaml"])
        self.assertEqual(
            page.meta["saltbox_automation"]["inventory"]["example_overrides"],
            {},
        )
        self.assertEqual(
            page.markdown,
            """# Body

```yaml
app_secret: !vault |
  $ANSIBLE_VAULT;1.1;AES256
  ciphertext
app_nested:
  value: !unsafe "{{ user.domain }}"
```
""",
        )
        self.assertEqual(source_after, source)

    def test_ordinary_page_keeps_normal_metadata_behavior(self) -> None:
        source = b"""---
title: Ordinary example
tags:
  - ordinary
saltbox_automation:
  inventory:
    example_overrides:
      app_enabled: false
---
# Ordinary body
"""

        page, source_after = self.read_page(source)

        self.assertEqual(page.meta["title"], "Ordinary example")
        self.assertEqual(page.meta["tags"], ["ordinary"])
        self.assertFalse(
            page.meta["saltbox_automation"]["inventory"]["example_overrides"]["app_enabled"]
        )
        self.assertEqual(page.markdown, "# Ordinary body\n")
        self.assertEqual(source_after, source)

    def test_malformed_frontmatter_reports_page_context(self) -> None:
        with self.assertRaisesRegex(PluginError, "fixture.md"):
            self.read_page(
                b"""---
title: Broken
saltbox_automation: [
---
# Body
"""
            )

    def test_alias_shared_outside_examples_is_rejected(self) -> None:
        with self.assertRaisesRegex(PluginError, "alias.*example_overrides"):
            self.read_page(
                b"""---
title: Shared alias
saltbox_automation:
  inventory:
    example_overrides: &examples
      app_secret: !vault ciphertext
copied_examples: *examples
---
# Body
"""
            )


if __name__ == "__main__":
    unittest.main()

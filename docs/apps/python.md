---
icon: material/desktop-classic
status: draft
saltbox_automation:
  sections:
    inventory: false
  app_links:
  - name: Manual
    url: https://www.python.org/doc
    type: documentation
  - name: Releases
    url:
    type: releases
  - name: Community
    url: https://www.python.org/community
    type: community
  project_description:
    name: Python
    summary: |
      a command-line application that executes scripts written in the Python programming language.
    link: https://www.python.org
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Python

## Overview

[Python](https://www.python.org) is a command-line application that executes scripts written in the Python programming language.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://www.python.org/doc){ .md-button .md-button--stretch }

[:fontawesome-solid-newspaper:**Releases**](){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](https://www.python.org/community){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

Saltbox dependency.

```shell
sb install python
```

## Usage

```shell
python3
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        python_version: "custom_value"
        ```

=== "Settings"

    ??? variable string "`python_version`"

        ```yaml
        # Install of Python is handled by uv so any versions they support will be valid here.
        # Type: string
        python_version: "3.8"
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

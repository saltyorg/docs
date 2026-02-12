---
icon: material/cogs
status: draft
hide:
  - tags
tags:
  - common
  - media
  - nano
saltbox_automation:
  project_description:
    name: Common
    summary: |-
      a Saltbox module that sets up common directories, installs essential packages, handles BTRFS optimizations, and configures basic system tools.
    link:
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Common

## Overview

Common is a Saltbox module that sets up common directories, installs essential packages, handles BTRFS optimizations, and configures basic system tools.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

Core Saltbox role.

```shell
sb install common
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        nano_syntax_highlighting_enabled: true
        ```

=== "General"

    ??? variable bool "`nano_syntax_highlighting_enabled`"

        ```yaml
        # Type: bool (true/false)
        nano_syntax_highlighting_enabled: true
        ```

    ??? variable bool "`common_create_media_subfolders`"

        ```yaml
        # Type: bool (true/false)
        common_create_media_subfolders: true
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

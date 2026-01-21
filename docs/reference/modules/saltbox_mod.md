---
icon: material/source-repository
title: Saltbox Mod
status: draft
saltbox_automation:
  project_description:
    name: Saltbox Mod
    summary: |-
      a Saltbox module that creates a local copy of the saltbox_mod repository.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Saltbox Mod

## Overview

Saltbox Mod is a Saltbox module that creates a local copy of the saltbox_mod repository.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install saltbox-mod
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        saltbox_mod_repo: "custom_value"
        ```

=== "General"

    ??? variable string "`saltbox_mod_repo`"

        ```yaml
        # Type: string
        saltbox_mod_repo: "https://github.com/saltyorg/saltbox_mod.git"
        ```

    ??? variable string "`saltbox_mod_branch`"

        ```yaml
        # Type: string
        saltbox_mod_branch: "master"
        ```

    ??? variable bool "`saltbox_mod_force_overwrite`"

        ```yaml
        # Type: bool (true/false)
        saltbox_mod_force_overwrite: false
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

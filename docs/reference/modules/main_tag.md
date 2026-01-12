---
icon: material/tag
title: Main Tag
status: draft
saltbox_automation:
  project_description:
    name: Main Tag
    summary: |
      a Sandbox module that deploys your assigned Sandbox apps stack.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Main Tag

## Overview

Main Tag is a Sandbox module that deploys your assigned Sandbox apps stack.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

Perhaps you have a standard set of sandbox tags that you install. To avoid installing all these individually, you can define a value for this role to allow you to install/update a set of sandbox roles in a similar manner to `sb install saltbox`.

## Deployment

```shell
sb install sandbox-roles
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        sandbox_roles: ["item1", "item2"]
        ```

=== "General"

    ??? variable list "`sandbox_roles`"

        ```yaml
        # Type: list
        sandbox_roles: []
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

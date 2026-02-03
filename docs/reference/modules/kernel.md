---
icon: material/cogs
status: draft
saltbox_automation:
  sections:
    inventory: true
  project_description:
    name: Kernel
    summary: |-
      a Saltbox module that manages the Linux kernel.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Kernel

## Overview

Kernel is a Saltbox module that manages the Linux kernel.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

Core Saltbox role.

```shell
sb install kernel
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        kernel_install_hwe: true
        ```

=== "Settings"

    ??? variable bool "`kernel_install_hwe`"

        ```yaml
        # Setting to true will install the Hardware Enablement kernel package whenever the kernel role is run.
        # Type: bool (true/false)
        kernel_install_hwe: false
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

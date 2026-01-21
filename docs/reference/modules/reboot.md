---
icon: material/play
status: draft
saltbox_automation:
  project_description:
    name: Reboot
    summary: |-
      a Saltbox module that checks for system reboot requirements and optionally reboots the host if configured.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Reboot

## Overview

Reboot is a Saltbox module that checks for system reboot requirements and optionally reboots the host if configured.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

Invoked during main role runs.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        saltbox_auto_reboot: true
        ```

=== "General"

    ??? variable bool "`saltbox_auto_reboot`"

        ```yaml
        # Type: bool (true/false)
        saltbox_auto_reboot: false
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

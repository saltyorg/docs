---
icon: material/cogs
title: Hetzner VLAN
status: draft2
saltbox_automation:
  project_description:
    name: Hetzner VLAN
    summary: |-
      a Saltbox module that configures VLAN interfaces on a Hetzner host.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Hetzner VLAN

## Overview

Hetzner VLAN is a Saltbox module that configures VLAN interfaces on a Hetzner host.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install hetzner-vlan-deploy
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        hetzner_vlan_netplan_apply: true
        ```

=== "General"

    ??? variable bool "`hetzner_vlan_netplan_apply`"

        ```yaml
        # Type: bool (true/false)
        hetzner_vlan_netplan_apply: true
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

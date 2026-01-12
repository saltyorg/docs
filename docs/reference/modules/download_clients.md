---
icon: material/tag
title: Download Clients
status: draft
saltbox_automation:
  project_description:
    name: Download Clients
    summary: |
      a Saltbox module that deploys your assigned download client apps stack.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Download Clients

## Overview

Download Clients is a Saltbox module that deploys your assigned download client apps stack.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install download-clients
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        download_clients_enabled: ["item1", "item2"]
        ```

=== "General"

    ??? variable list "`download_clients_enabled`"

        ```yaml
        # Type: list
        download_clients_enabled: ["qbittorrent", "sabnzbd"]
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

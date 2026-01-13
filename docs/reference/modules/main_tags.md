---
icon: material/tag
title: Main Tags
saltbox_automation:
  project_description:
    name: Main Tags
    summary: |
      a Saltbox module that deploys core roles and your assigned saltbox, mediabox and feederbox apps stacks.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Main Tags

## Overview

Main Tags is a Saltbox module that deploys core roles and your assigned saltbox, mediabox and feederbox apps stacks.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install saltbox
```

```shell
sb install mediabox
```

```shell
sb install feederbox
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        saltbox_roles: ["item1", "item2"]
        ```

=== "General"

    ??? variable list "`saltbox_roles`"

        ```yaml
        # Type: list
        saltbox_roles: ["media_server", "download_clients", "download_indexers", "autoscan", "tautulli", "overseerr", "portainer", "organizr", "sonarr", "radarr", "lidarr", "iperf3", "glances", "btop"]
        ```

    ??? variable list "`mediabox_roles`"

        ```yaml
        # Type: list
        mediabox_roles: ["media_server", "autoscan", "tautulli", "overseerr", "iperf3", "glances", "btop"]
        ```

    ??? variable list "`feederbox_roles`"

        ```yaml
        # Type: list
        feederbox_roles: ["download_clients", "download_indexers", "portainer", "organizr", "sonarr", "radarr", "lidarr", "iperf3", "glances", "btop"]
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

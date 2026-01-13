---
icon: material/tag
title: Media Server
saltbox_automation:
  project_description:
    name: Media Server
    summary: |
      a Saltbox module that deploys your assigned media server apps stack.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Media Server

## Overview

Media Server is a Saltbox module that deploys your assigned media server apps stack.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install media-server
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        media_servers_enabled: ["item1", "item2"]
        ```

=== "General"

    ??? variable list "`media_servers_enabled`"

        ```yaml
        # Type: list
        media_servers_enabled: ["plex"]
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
icon: material/tag
title: Download Indexers
status: draft
saltbox_automation:
  project_description:
    name: Download Indexers
    summary: |
      a Saltbox module that deploys your assigned download indexer apps stack.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Download Indexers

## Overview

Download Indexers is a Saltbox module that deploys your assigned download indexer apps stack.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install download-indexers
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        download_indexers_enabled: ["item1", "item2"]
        ```

=== "General"

    ??? variable list "`download_indexers_enabled`"

        ```yaml
        # Type: list
        download_indexers_enabled: ["jackett", "nzbhydra2"]
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

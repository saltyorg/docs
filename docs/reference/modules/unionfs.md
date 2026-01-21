---
icon: material/server-network-outline
title: UnionFS
status: draft
saltbox_automation:
  inventory:
    hide_sections:
      - MergerFS
  project_description:
    name: UnionFS
    summary: |-
      a Saltbox module that installs and configures MergerFS to create a union filesystem merging local and remote storage paths, managing Docker services during mount operations.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# UnionFS

## Overview

UnionFS is a Saltbox module that installs and configures MergerFS to create a union filesystem merging local and remote storage paths, managing Docker services during mount operations.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

UnionFS is a filesystem service for Linux, FreeBSD and NetBSD which implements a union mount for other file systems.

## Deployment

Core Saltbox role.

```shell
sb install mounts
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        local_mount_branch: "custom_value"
        ```

=== "Global"

    ??? variable string "`local_mount_branch`"

        ```yaml
        # Type: string
        local_mount_branch: "{{ server_local_folder_path }}=RW:"
        ```

    ??? variable string "`custom_mount_branch`"

        ```yaml
        # Type: string
        custom_mount_branch: "" # Format: "/mnt/remote/someremote=NC"
        ```

    ??? variable bool "`mergerfs_override_service`"

        ```yaml
        # Type: bool (true/false)
        mergerfs_override_service: true
        ```

    ??? variable string "`mergerfs_service_name`"

        ```yaml
        # Type: string
        mergerfs_service_name: "saltbox_managed_mergerfs.service"
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

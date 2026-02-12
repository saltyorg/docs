---
icon: material/server-network-outline
status: draft
hide:
  - tags
tags:
  - cloud
  - nfs
  - rclone
  - remote
  - sftp
  - storage
saltbox_automation:
  project_description:
    name: Remote
    summary: |-
      a Saltbox module that manages remote storage mounts.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Remote

## Overview

Remote is a Saltbox module that manages remote storage mounts.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

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
        user_agent: "custom_value"
        ```

=== "Global"

    ??? variable string "`user_agent`"

        ```yaml
        # Type: string
        user_agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36
        ```

    ??? variable string "`rclone_config_path`"

        ```yaml
        # Type: string
        rclone_config_path: "/home/{{ user.name }}/.config/rclone/rclone.conf"
        ```

    ??? variable string "`rclone_vfs_cache_dir`"

        ```yaml
        # Type: string
        rclone_vfs_cache_dir: ""
        ```

    ??? variable string "`rclone_vfs_cache_dir_lookup`"

        ```yaml
        # Type: string
        rclone_vfs_cache_dir_lookup: "{{ lookup('vars', 'rclone_remote_' + rclone_remote_name + '_vfs_cache_dir', default=rclone_vfs_cache_dir) }}"
        ```

    ??? variable string "`rclone_vfs_cache_min_free_space`"

        ```yaml
        # Type: string
        rclone_vfs_cache_min_free_space: "off"
        ```

    ??? variable string "`rclone_vfs_cache_poll_interval`"

        ```yaml
        # Type: string
        rclone_vfs_cache_poll_interval: "1m0s"
        ```

    ??? variable string "`rclone_cloud_dir_cache_time`"

        ```yaml
        # Type: string
        rclone_cloud_dir_cache_time: "8760h"
        ```

    ??? variable string "`rclone_sftp_dir_cache_time`"

        ```yaml
        # Type: string
        rclone_sftp_dir_cache_time: "1m"
        ```

    ??? variable string "`rclone_sftp_chunk_size`"

        ```yaml
        # Read https://rclone.org/sftp/#sftp-chunk-size if you want to change the chunk size
        # Type: string
        rclone_sftp_chunk_size: "32Ki"
        ```

    ??? variable string "`rclone_sftp_concurrency`"

        ```yaml
        # Type: string
        rclone_sftp_concurrency: "64"
        ```

    ??? variable bool "`rclone_sftp_disable_hashcheck`"

        ```yaml
        # Type: bool (true/false)
        rclone_sftp_disable_hashcheck: false
        ```

    ??? variable string "`rclone_service_template`"

        ```yaml
        # Type: string
        rclone_service_template: "saltbox_managed_rclone_"
        ```

    ??? variable string "`rclone_port_lookup`"

        ```yaml
        # Type: string
        rclone_port_lookup: "{{ port_lookup_rclone.meta.port
                             if (port_lookup_rclone.meta.port is defined) and (port_lookup_rclone.meta.port | trim | length > 0)
                             else '5572' }}"
        ```

    ??? variable string "`rclone_remote_port`"

        ```yaml
        # Type: string
        rclone_remote_port: "{{ lookup('vars', 'rclone_remote_' + rclone_remote_name + '_port', default=rclone_port_lookup) }}"
        ```

    ??? variable int "`rclone_remote_port_low_bound`"

        ```yaml
        # Type: int
        rclone_remote_port_low_bound: 5572
        ```

    ??? variable int "`rclone_remote_port_high_bound`"

        ```yaml
        # Type: int
        rclone_remote_port_high_bound: 6072
        ```

    ??? variable string "`rclone_remote_name`"

        ```yaml
        # Type: string
        rclone_remote_name: "{{ item | filter_rclone_remote_name }}"
        ```

    ??? variable string "`rclone_remote_with_path`"

        ```yaml
        # Type: string
        rclone_remote_with_path: "{{ item | filter_rclone_remote_with_path }}"
        ```

    ??? variable string "`rclone_first_remote_name`"

        ```yaml
        # Type: string
        rclone_first_remote_name: "{{ rclone | filter_rclone_first_remote_name }}"
        ```

    ??? variable string "`rclone_first_remote_name_with_path`"

        ```yaml
        # Type: string
        rclone_first_remote_name_with_path: "{{ rclone | filter_rclone_first_remote_name_with_path }}"
        ```

    ??? variable bool "`remote_update_rclone`"

        ```yaml
        # Type: bool (true/false)
        remote_update_rclone: true
        ```

    ??? variable bool "`rclone_enable_metrics`"

        ```yaml
        # Enforces the use of auth (your accounts.yml credentials) on rclone rc when enabled
        # Type: bool (true/false)
        rclone_enable_metrics: false
        ```

=== "Rclone VFS Refresh"

    ??? variable int "`rclone_vfs_refresh_interval`"

        ```yaml
        # Type: int
        rclone_vfs_refresh_interval: 10800
        ```

    ??? variable string "`rclone_vfs_refresh_auth_args`"

        ```yaml
        # Type: string
        rclone_vfs_refresh_auth_args: " --user='{{ user.name }}' --pass='{{ user.pass }}'"
        ```

    ??? variable string "`rclone_vfs_refresh_command`"

        ```yaml
        # Type: string
        rclone_vfs_refresh_command: |-
          /usr/bin/rclone rc vfs/refresh recursive=true --url http://127.0.0.1:{{ rclone_remote_port }}{{ rclone_vfs_refresh_auth_args if (rclone_enable_metrics | bool) else '' }} _async=true
        ```

=== "NFS"

    ??? variable string "`nfs_opts`"

        ```yaml
        # Type: string
        nfs_opts: "nofail,noatime,nolock,intr,tcp,actimeo=1800"
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

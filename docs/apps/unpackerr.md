---
icon: material/docker
hide:
  - tags
tags:
  - unpackerr
saltbox_automation:
  app_links:
    - name: Manual
      url:
      type: documentation
    - name: Releases
      url: https://github.com/hotio/unpackerr/pkgs/container/unpackerr
      type: github
    - name: Community
      url: https://hotio.dev/discord
      type: discord
  project_description:
    name: Unpackerr
    summary: |-
      a lightweight, cross-platform application designed to automatically extract compressed files (like RAR, ZIP, 7Z, TAR, and ISO) from download folders, primarily for use with media management tools such as Radarr, Sonarr, Lidarr.
    link: https://github.com/davidnewhall/unpackerr
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Unpackerr

## Overview

[Unpackerr](https://github.com/davidnewhall/unpackerr) is a lightweight, cross-platform application designed to automatically extract compressed files (like RAR, ZIP, 7Z, TAR, and ISO) from download folders, primarily for use with media management tools such as Radarr, Sonarr, Lidarr.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/hotio/unpackerr/pkgs/container/unpackerr){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://hotio.dev/discord){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install unpackerr
```

## Basics

- [:octicons-link-16: Documentation](https://github.com/davidnewhall/unpackerr){: .header-icons }

The important part of the setup is the setup for the applications. You'll need to change these three settings for each:

```text
[[sonarr]]
  url = "http://sonarr:8989"
  api_key = "YOUR_API_KEY"
# File system path where downloaded Sonarr items are located.
  paths = ['/mnt/unionfs/downloads/torrents/qbittorrent/completed']
```

The `path` will depend on the torrent client you are using and its configuration.

Same setup is required for radarr and lidarr if you are using them.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        unpackerr_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `unpackerr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `unpackerr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`unpackerr_name`"

        ```yaml
        # Type: string
        unpackerr_name: unpackerr
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`unpackerr_role_docker_container`"

        ```yaml
        # Type: string
        unpackerr_role_docker_container: "{{ unpackerr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`unpackerr_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        unpackerr_role_docker_image_pull: true
        ```

    ??? variable string "`unpackerr_role_docker_image_repo`"

        ```yaml
        # Type: string
        unpackerr_role_docker_image_repo: "ghcr.io/hotio/unpackerr"
        ```

    ??? variable string "`unpackerr_role_docker_image_tag`"

        ```yaml
        # Type: string
        unpackerr_role_docker_image_tag: "latest"
        ```

    ??? variable string "`unpackerr_role_docker_image`"

        ```yaml
        # Type: string
        unpackerr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='unpackerr') }}:{{ lookup('role_var', '_docker_image_tag', role='unpackerr') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`unpackerr_role_docker_envs_default`"

        ```yaml
        # Type: dict
        unpackerr_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          UMASK: "002"
        ```

    ??? variable dict "`unpackerr_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        unpackerr_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`unpackerr_role_docker_volumes_default`"

        ```yaml
        # Type: list
        unpackerr_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='unpackerr') }}:/config"
        ```

    ??? variable list "`unpackerr_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        unpackerr_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`unpackerr_role_docker_hostname`"

        ```yaml
        # Type: string
        unpackerr_role_docker_hostname: "{{ unpackerr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`unpackerr_role_docker_networks_alias`"

        ```yaml
        # Type: string
        unpackerr_role_docker_networks_alias: "{{ unpackerr_name }}"
        ```

    ??? variable list "`unpackerr_role_docker_networks_default`"

        ```yaml
        # Type: list
        unpackerr_role_docker_networks_default: []
        ```

    ??? variable list "`unpackerr_role_docker_networks_custom`"

        ```yaml
        # Type: list
        unpackerr_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`unpackerr_role_docker_restart_policy`"

        ```yaml
        # Type: string
        unpackerr_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`unpackerr_role_docker_state`"

        ```yaml
        # Type: string
        unpackerr_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`unpackerr_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        unpackerr_role_docker_blkio_weight:
        ```

    ??? variable int "`unpackerr_role_docker_cpu_period`"

        ```yaml
        # Type: int
        unpackerr_role_docker_cpu_period:
        ```

    ??? variable int "`unpackerr_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        unpackerr_role_docker_cpu_quota:
        ```

    ??? variable int "`unpackerr_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        unpackerr_role_docker_cpu_shares:
        ```

    ??? variable string "`unpackerr_role_docker_cpus`"

        ```yaml
        # Type: string
        unpackerr_role_docker_cpus:
        ```

    ??? variable string "`unpackerr_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        unpackerr_role_docker_cpuset_cpus:
        ```

    ??? variable string "`unpackerr_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        unpackerr_role_docker_cpuset_mems:
        ```

    ??? variable string "`unpackerr_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        unpackerr_role_docker_kernel_memory:
        ```

    ??? variable string "`unpackerr_role_docker_memory`"

        ```yaml
        # Type: string
        unpackerr_role_docker_memory:
        ```

    ??? variable string "`unpackerr_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        unpackerr_role_docker_memory_reservation:
        ```

    ??? variable string "`unpackerr_role_docker_memory_swap`"

        ```yaml
        # Type: string
        unpackerr_role_docker_memory_swap:
        ```

    ??? variable int "`unpackerr_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        unpackerr_role_docker_memory_swappiness:
        ```

    ??? variable string "`unpackerr_role_docker_shm_size`"

        ```yaml
        # Type: string
        unpackerr_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`unpackerr_role_docker_cap_drop`"

        ```yaml
        # Type: list
        unpackerr_role_docker_cap_drop:
        ```

    ??? variable string "`unpackerr_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        unpackerr_role_docker_cgroupns_mode:
        ```

    ??? variable list "`unpackerr_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        unpackerr_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`unpackerr_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        unpackerr_role_docker_device_read_bps:
        ```

    ??? variable list "`unpackerr_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        unpackerr_role_docker_device_read_iops:
        ```

    ??? variable list "`unpackerr_role_docker_device_requests`"

        ```yaml
        # Type: list
        unpackerr_role_docker_device_requests:
        ```

    ??? variable list "`unpackerr_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        unpackerr_role_docker_device_write_bps:
        ```

    ??? variable list "`unpackerr_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        unpackerr_role_docker_device_write_iops:
        ```

    ??? variable list "`unpackerr_role_docker_devices`"

        ```yaml
        # Type: list
        unpackerr_role_docker_devices:
        ```

    ??? variable string "`unpackerr_role_docker_devices_default`"

        ```yaml
        # Type: string
        unpackerr_role_docker_devices_default:
        ```

    ??? variable list "`unpackerr_role_docker_groups`"

        ```yaml
        # Type: list
        unpackerr_role_docker_groups:
        ```

    ??? variable bool "`unpackerr_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        unpackerr_role_docker_privileged:
        ```

    ??? variable list "`unpackerr_role_docker_security_opts`"

        ```yaml
        # Type: list
        unpackerr_role_docker_security_opts:
        ```

    ??? variable string "`unpackerr_role_docker_user`"

        ```yaml
        # Type: string
        unpackerr_role_docker_user:
        ```

    ??? variable string "`unpackerr_role_docker_userns_mode`"

        ```yaml
        # Type: string
        unpackerr_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`unpackerr_role_docker_dns_opts`"

        ```yaml
        # Type: list
        unpackerr_role_docker_dns_opts:
        ```

    ??? variable list "`unpackerr_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        unpackerr_role_docker_dns_search_domains:
        ```

    ??? variable list "`unpackerr_role_docker_dns_servers`"

        ```yaml
        # Type: list
        unpackerr_role_docker_dns_servers:
        ```

    ??? variable string "`unpackerr_role_docker_domainname`"

        ```yaml
        # Type: string
        unpackerr_role_docker_domainname:
        ```

    ??? variable list "`unpackerr_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        unpackerr_role_docker_exposed_ports:
        ```

    ??? variable dict "`unpackerr_role_docker_hosts`"

        ```yaml
        # Type: dict
        unpackerr_role_docker_hosts:
        ```

    ??? variable bool "`unpackerr_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        unpackerr_role_docker_hosts_use_common:
        ```

    ??? variable string "`unpackerr_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        unpackerr_role_docker_ipc_mode:
        ```

    ??? variable list "`unpackerr_role_docker_links`"

        ```yaml
        # Type: list
        unpackerr_role_docker_links:
        ```

    ??? variable string "`unpackerr_role_docker_network_mode`"

        ```yaml
        # Type: string
        unpackerr_role_docker_network_mode:
        ```

    ??? variable string "`unpackerr_role_docker_pid_mode`"

        ```yaml
        # Type: string
        unpackerr_role_docker_pid_mode:
        ```

    ??? variable list "`unpackerr_role_docker_ports`"

        ```yaml
        # Type: list
        unpackerr_role_docker_ports:
        ```

    ??? variable string "`unpackerr_role_docker_uts`"

        ```yaml
        # Type: string
        unpackerr_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`unpackerr_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        unpackerr_role_docker_keep_volumes:
        ```

    ??? variable list "`unpackerr_role_docker_mounts`"

        ```yaml
        # Type: list
        unpackerr_role_docker_mounts:
        ```

    ??? variable dict "`unpackerr_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        unpackerr_role_docker_storage_opts:
        ```

    ??? variable list "`unpackerr_role_docker_tmpfs`"

        ```yaml
        # Type: list
        unpackerr_role_docker_tmpfs:
        ```

    ??? variable string "`unpackerr_role_docker_volume_driver`"

        ```yaml
        # Type: string
        unpackerr_role_docker_volume_driver:
        ```

    ??? variable list "`unpackerr_role_docker_volumes_from`"

        ```yaml
        # Type: list
        unpackerr_role_docker_volumes_from:
        ```

    ??? variable bool "`unpackerr_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        unpackerr_role_docker_volumes_global:
        ```

    ??? variable string "`unpackerr_role_docker_working_dir`"

        ```yaml
        # Type: string
        unpackerr_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`unpackerr_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        unpackerr_role_docker_auto_remove:
        ```

    ??? variable bool "`unpackerr_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        unpackerr_role_docker_cleanup:
        ```

    ??? variable string "`unpackerr_role_docker_force_kill`"

        ```yaml
        # Type: string
        unpackerr_role_docker_force_kill:
        ```

    ??? variable dict "`unpackerr_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        unpackerr_role_docker_healthcheck:
        ```

    ??? variable int "`unpackerr_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        unpackerr_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`unpackerr_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        unpackerr_role_docker_init:
        ```

    ??? variable string "`unpackerr_role_docker_kill_signal`"

        ```yaml
        # Type: string
        unpackerr_role_docker_kill_signal:
        ```

    ??? variable string "`unpackerr_role_docker_log_driver`"

        ```yaml
        # Type: string
        unpackerr_role_docker_log_driver:
        ```

    ??? variable dict "`unpackerr_role_docker_log_options`"

        ```yaml
        # Type: dict
        unpackerr_role_docker_log_options:
        ```

    ??? variable bool "`unpackerr_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        unpackerr_role_docker_oom_killer:
        ```

    ??? variable int "`unpackerr_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        unpackerr_role_docker_oom_score_adj:
        ```

    ??? variable bool "`unpackerr_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        unpackerr_role_docker_output_logs:
        ```

    ??? variable bool "`unpackerr_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        unpackerr_role_docker_paused:
        ```

    ??? variable bool "`unpackerr_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        unpackerr_role_docker_recreate:
        ```

    ??? variable int "`unpackerr_role_docker_restart_retries`"

        ```yaml
        # Type: int
        unpackerr_role_docker_restart_retries:
        ```

    ??? variable int "`unpackerr_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        unpackerr_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`unpackerr_role_docker_capabilities`"

        ```yaml
        # Type: list
        unpackerr_role_docker_capabilities:
        ```

    ??? variable string "`unpackerr_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        unpackerr_role_docker_cgroup_parent:
        ```

    ??? variable list "`unpackerr_role_docker_commands`"

        ```yaml
        # Type: list
        unpackerr_role_docker_commands:
        ```

    ??? variable int "`unpackerr_role_docker_create_timeout`"

        ```yaml
        # Type: int
        unpackerr_role_docker_create_timeout:
        ```

    ??? variable string "`unpackerr_role_docker_entrypoint`"

        ```yaml
        # Type: string
        unpackerr_role_docker_entrypoint:
        ```

    ??? variable string "`unpackerr_role_docker_env_file`"

        ```yaml
        # Type: string
        unpackerr_role_docker_env_file:
        ```

    ??? variable dict "`unpackerr_role_docker_labels`"

        ```yaml
        # Type: dict
        unpackerr_role_docker_labels:
        ```

    ??? variable bool "`unpackerr_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        unpackerr_role_docker_labels_use_common:
        ```

    ??? variable bool "`unpackerr_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        unpackerr_role_docker_read_only:
        ```

    ??? variable string "`unpackerr_role_docker_runtime`"

        ```yaml
        # Type: string
        unpackerr_role_docker_runtime:
        ```

    ??? variable list "`unpackerr_role_docker_sysctls`"

        ```yaml
        # Type: list
        unpackerr_role_docker_sysctls:
        ```

    ??? variable list "`unpackerr_role_docker_ulimits`"

        ```yaml
        # Type: list
        unpackerr_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`unpackerr_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        unpackerr_role_autoheal_enabled: true
        ```

    ??? variable string "`unpackerr_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        unpackerr_role_depends_on: ""
        ```

    ??? variable string "`unpackerr_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        unpackerr_role_depends_on_delay: "0"
        ```

    ??? variable string "`unpackerr_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        unpackerr_role_depends_on_healthchecks:
        ```

    ??? variable bool "`unpackerr_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        unpackerr_role_diun_enabled: true
        ```

    ??? variable bool "`unpackerr_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        unpackerr_role_docker_controller: true
        ```

    ??? variable string "`unpackerr_role_docker_image_repo`"

        ```yaml
        # Type: string
        unpackerr_role_docker_image_repo:
        ```

    ??? variable string "`unpackerr_role_docker_image_tag`"

        ```yaml
        # Type: string
        unpackerr_role_docker_image_tag:
        ```

    ??? variable bool "`unpackerr_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        unpackerr_role_docker_volumes_download:
        ```

    ??? variable string "`unpackerr_role_paths_location`"

        ```yaml
        # Type: string
        unpackerr_role_paths_location:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
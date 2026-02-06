---
icon: material/docker
title: Plex-Trakt-Sync
hide:
  - tags
tags:
  - plextraktsync
  - trakt
saltbox_automation:
  app_links:
    - name: Manual
      url: https://github.com/Taxel/PlexTraktSync/blob/main/README.md#setup
      type: documentation
    - name: Releases
      url: https://github.com/taxel/PlexTraktSync/pkgs/container/plextraktsync
      type: github
    - name: Community
      url: https://github.com/Taxel/PlexTraktSync/discussions
      type: github
  project_description:
    name: Plex-Trakt-Sync
    summary: |-
      a two-way synchronization tool between trakt.tv and Plex Media Server, allowing users to sync media collections, ratings, watched status, and watchlists without requiring a Plex Pass or Trakt VIP subscription.
    link: https://github.com/Taxel/PlexTraktSync
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Plex-Trakt-Sync

## Overview

[Plex-Trakt-Sync](https://github.com/Taxel/PlexTraktSync) is a two-way synchronization tool between trakt.tv and Plex Media Server, allowing users to sync media collections, ratings, watched status, and watchlists without requiring a Plex Pass or Trakt VIP subscription.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/Taxel/PlexTraktSync/blob/main/README.md#setup){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/taxel/PlexTraktSync/pkgs/container/plextraktsync){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Community**](https://github.com/Taxel/PlexTraktSync/discussions){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-plextraktsync
```

## Usage

```shell
docker exec plextraktsync plextraktsync --help
```

Once linked to a Trakt.tv account, the selected Plex user's streaming activity is automatically scrobbled.

## Basics

Sync preferences are available to customize in `/opt/plextraktsync/config.yml`.

The following command will launch an interactive script prompting you for missing credentials (use this to link Trakt.tv):

```shell
docker exec -it plextraktsync plextraktsync login
```

### Reset Plex Settings

The target Plex server is initially set to your main Plex Saltbox instance using the owner account. To reset these credentials:

```shell
docker exec -it plextraktsync plextraktsync plex-login
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        plextraktsync_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `plextraktsync_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `plextraktsync_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`plextraktsync_name`"

        ```yaml
        # Type: string
        plextraktsync_name: plextraktsync
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`plextraktsync_role_docker_container`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_container: "{{ plextraktsync_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`plextraktsync_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        plextraktsync_role_docker_image_pull: true
        ```

    ??? variable string "`plextraktsync_role_docker_image_tag`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_image_tag: "latest"
        ```

    ??? variable string "`plextraktsync_role_docker_image_repo`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_image_repo: "ghcr.io/taxel/plextraktsync"
        ```

    ??? variable string "`plextraktsync_role_docker_image`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='plextraktsync') }}:{{ lookup('role_var', '_docker_image_tag', role='plextraktsync') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`plextraktsync_role_docker_envs_default`"

        ```yaml
        # Type: dict
        plextraktsync_role_docker_envs_default:
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`plextraktsync_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        plextraktsync_role_docker_envs_custom: {}
        ```

    <h5>Commands</h5>

    ??? variable list "`plextraktsync_role_docker_commands_default`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_commands_default:
          - watch
        ```

    ??? variable list "`plextraktsync_role_docker_commands_custom`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_commands_custom: []
        ```

    <h5>Volumes</h5>

    ??? variable list "`plextraktsync_role_docker_volumes_default`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='plextraktsync') }}:/app/config"
        ```

    ??? variable list "`plextraktsync_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`plextraktsync_role_docker_hostname`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_hostname: "{{ plextraktsync_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`plextraktsync_role_docker_networks_alias`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_networks_alias: "{{ plextraktsync_name }}"
        ```

    ??? variable list "`plextraktsync_role_docker_networks_default`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_networks_default: []
        ```

    ??? variable list "`plextraktsync_role_docker_networks_custom`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`plextraktsync_role_docker_restart_policy`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`plextraktsync_role_docker_state`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`plextraktsync_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        plextraktsync_role_docker_blkio_weight:
        ```

    ??? variable int "`plextraktsync_role_docker_cpu_period`"

        ```yaml
        # Type: int
        plextraktsync_role_docker_cpu_period:
        ```

    ??? variable int "`plextraktsync_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        plextraktsync_role_docker_cpu_quota:
        ```

    ??? variable int "`plextraktsync_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        plextraktsync_role_docker_cpu_shares:
        ```

    ??? variable string "`plextraktsync_role_docker_cpus`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_cpus:
        ```

    ??? variable string "`plextraktsync_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_cpuset_cpus:
        ```

    ??? variable string "`plextraktsync_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_cpuset_mems:
        ```

    ??? variable string "`plextraktsync_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_kernel_memory:
        ```

    ??? variable string "`plextraktsync_role_docker_memory`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_memory:
        ```

    ??? variable string "`plextraktsync_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_memory_reservation:
        ```

    ??? variable string "`plextraktsync_role_docker_memory_swap`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_memory_swap:
        ```

    ??? variable int "`plextraktsync_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        plextraktsync_role_docker_memory_swappiness:
        ```

    ??? variable string "`plextraktsync_role_docker_shm_size`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`plextraktsync_role_docker_cap_drop`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_cap_drop:
        ```

    ??? variable string "`plextraktsync_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_cgroupns_mode:
        ```

    ??? variable list "`plextraktsync_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`plextraktsync_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_device_read_bps:
        ```

    ??? variable list "`plextraktsync_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_device_read_iops:
        ```

    ??? variable list "`plextraktsync_role_docker_device_requests`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_device_requests:
        ```

    ??? variable list "`plextraktsync_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_device_write_bps:
        ```

    ??? variable list "`plextraktsync_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_device_write_iops:
        ```

    ??? variable list "`plextraktsync_role_docker_devices`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_devices:
        ```

    ??? variable list "`plextraktsync_role_docker_groups`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_groups:
        ```

    ??? variable bool "`plextraktsync_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        plextraktsync_role_docker_privileged:
        ```

    ??? variable list "`plextraktsync_role_docker_security_opts`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_security_opts:
        ```

    ??? variable string "`plextraktsync_role_docker_user`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_user:
        ```

    ??? variable string "`plextraktsync_role_docker_userns_mode`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`plextraktsync_role_docker_dns_opts`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_dns_opts:
        ```

    ??? variable list "`plextraktsync_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_dns_search_domains:
        ```

    ??? variable list "`plextraktsync_role_docker_dns_servers`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_dns_servers:
        ```

    ??? variable string "`plextraktsync_role_docker_domainname`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_domainname:
        ```

    ??? variable list "`plextraktsync_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_exposed_ports:
        ```

    ??? variable dict "`plextraktsync_role_docker_hosts`"

        ```yaml
        # Type: dict
        plextraktsync_role_docker_hosts:
        ```

    ??? variable bool "`plextraktsync_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        plextraktsync_role_docker_hosts_use_common:
        ```

    ??? variable string "`plextraktsync_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_ipc_mode:
        ```

    ??? variable list "`plextraktsync_role_docker_links`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_links:
        ```

    ??? variable string "`plextraktsync_role_docker_network_mode`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_network_mode:
        ```

    ??? variable string "`plextraktsync_role_docker_pid_mode`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_pid_mode:
        ```

    ??? variable list "`plextraktsync_role_docker_ports`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_ports:
        ```

    ??? variable string "`plextraktsync_role_docker_uts`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`plextraktsync_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        plextraktsync_role_docker_keep_volumes:
        ```

    ??? variable list "`plextraktsync_role_docker_mounts`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_mounts:
        ```

    ??? variable dict "`plextraktsync_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        plextraktsync_role_docker_storage_opts:
        ```

    ??? variable list "`plextraktsync_role_docker_tmpfs`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_tmpfs:
        ```

    ??? variable string "`plextraktsync_role_docker_volume_driver`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_volume_driver:
        ```

    ??? variable list "`plextraktsync_role_docker_volumes_from`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_volumes_from:
        ```

    ??? variable bool "`plextraktsync_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        plextraktsync_role_docker_volumes_global:
        ```

    ??? variable string "`plextraktsync_role_docker_working_dir`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`plextraktsync_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        plextraktsync_role_docker_auto_remove:
        ```

    ??? variable bool "`plextraktsync_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        plextraktsync_role_docker_cleanup:
        ```

    ??? variable string "`plextraktsync_role_docker_force_kill`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_force_kill:
        ```

    ??? variable dict "`plextraktsync_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        plextraktsync_role_docker_healthcheck:
        ```

    ??? variable int "`plextraktsync_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        plextraktsync_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`plextraktsync_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        plextraktsync_role_docker_init:
        ```

    ??? variable string "`plextraktsync_role_docker_kill_signal`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_kill_signal:
        ```

    ??? variable string "`plextraktsync_role_docker_log_driver`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_log_driver:
        ```

    ??? variable dict "`plextraktsync_role_docker_log_options`"

        ```yaml
        # Type: dict
        plextraktsync_role_docker_log_options:
        ```

    ??? variable bool "`plextraktsync_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        plextraktsync_role_docker_oom_killer:
        ```

    ??? variable int "`plextraktsync_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        plextraktsync_role_docker_oom_score_adj:
        ```

    ??? variable bool "`plextraktsync_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        plextraktsync_role_docker_output_logs:
        ```

    ??? variable bool "`plextraktsync_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        plextraktsync_role_docker_paused:
        ```

    ??? variable bool "`plextraktsync_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        plextraktsync_role_docker_recreate:
        ```

    ??? variable int "`plextraktsync_role_docker_restart_retries`"

        ```yaml
        # Type: int
        plextraktsync_role_docker_restart_retries:
        ```

    ??? variable string "`plextraktsync_role_docker_stop_signal`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_stop_signal:
        ```

    ??? variable int "`plextraktsync_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        plextraktsync_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`plextraktsync_role_docker_capabilities`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_capabilities:
        ```

    ??? variable string "`plextraktsync_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_cgroup_parent:
        ```

    ??? variable int "`plextraktsync_role_docker_create_timeout`"

        ```yaml
        # Type: int
        plextraktsync_role_docker_create_timeout:
        ```

    ??? variable string "`plextraktsync_role_docker_dev_dri`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_dev_dri:
        ```

    ??? variable string "`plextraktsync_role_docker_entrypoint`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_entrypoint:
        ```

    ??? variable string "`plextraktsync_role_docker_env_file`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_env_file:
        ```

    ??? variable dict "`plextraktsync_role_docker_labels`"

        ```yaml
        # Type: dict
        plextraktsync_role_docker_labels:
        ```

    ??? variable bool "`plextraktsync_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        plextraktsync_role_docker_labels_use_common:
        ```

    ??? variable bool "`plextraktsync_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        plextraktsync_role_docker_read_only:
        ```

    ??? variable string "`plextraktsync_role_docker_runtime`"

        ```yaml
        # Type: string
        plextraktsync_role_docker_runtime:
        ```

    ??? variable list "`plextraktsync_role_docker_sysctls`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_sysctls:
        ```

    ??? variable list "`plextraktsync_role_docker_ulimits`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`plextraktsync_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        plextraktsync_role_autoheal_enabled: true
        ```

    ??? variable string "`plextraktsync_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        plextraktsync_role_depends_on: ""
        ```

    ??? variable string "`plextraktsync_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        plextraktsync_role_depends_on_delay: "0"
        ```

    ??? variable string "`plextraktsync_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        plextraktsync_role_depends_on_healthchecks:
        ```

    ??? variable bool "`plextraktsync_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        plextraktsync_role_diun_enabled: true
        ```

    ??? variable bool "`plextraktsync_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        plextraktsync_role_docker_controller: true
        ```

    ??? variable list "`plextraktsync_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        plextraktsync_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`plextraktsync_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        plextraktsync_role_docker_volumes_download:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

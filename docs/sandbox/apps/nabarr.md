---
icon: material/docker
hide:
  - tags
tags:
  - nabarr
  - automation
  - rss
saltbox_automation:
  app_links:
    - name: Manual
      url: https://github.com/saltydk/nabarr/blob/master/README.md#introduction
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/saltydk/nabarr/tags
      type: docker
    - name: Community
      url: https://discord.gg/ugfKXpFND8
      type: discord
  project_description:
    name: Nabarr
    summary: |-
      the official Saltbox continuation of *Cloudbox/nabarr*, a tool that monitors RSS feeds from Newznab or Torznab indexing services and automatically adds newly discovered TV shows and movies to Sonarr and Radarr, respectively.
    link: https://github.com/saltydk/nabarr
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Nabarr

## Overview

[Nabarr](https://github.com/saltydk/nabarr) is the official Saltbox continuation of *Cloudbox/nabarr*, a tool that monitors RSS feeds from Newznab or Torznab indexing services and automatically adds newly discovered TV shows and movies to Sonarr and Radarr, respectively.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/saltydk/nabarr/blob/master/README.md#introduction){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/saltydk/nabarr/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://discord.gg/ugfKXpFND8){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-nabarr
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        nabarr_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `nabarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `nabarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`nabarr_name`"

        ```yaml
        # Type: string
        nabarr_name: nabarr
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`nabarr_role_docker_container`"

        ```yaml
        # Type: string
        nabarr_role_docker_container: "{{ nabarr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`nabarr_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        nabarr_role_docker_image_pull: true
        ```

    ??? variable string "`nabarr_role_docker_image_tag`"

        ```yaml
        # Type: string
        nabarr_role_docker_image_tag: "latest"
        ```

    ??? variable string "`nabarr_role_docker_image_repo`"

        ```yaml
        # Type: string
        nabarr_role_docker_image_repo: "saltydk/nabarr"
        ```

    ??? variable string "`nabarr_role_docker_image`"

        ```yaml
        # Type: string
        nabarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='nabarr') }}:{{ lookup('role_var', '_docker_image_tag', role='nabarr') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`nabarr_role_docker_envs_default`"

        ```yaml
        # Type: dict
        nabarr_role_docker_envs_default:
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          APP_VERBOSITY: "0"
        ```

    ??? variable dict "`nabarr_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        nabarr_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`nabarr_role_docker_volumes_default`"

        ```yaml
        # Type: list
        nabarr_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='nabarr') }}:/config"
        ```

    ??? variable list "`nabarr_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        nabarr_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`nabarr_role_docker_hostname`"

        ```yaml
        # Type: string
        nabarr_role_docker_hostname: "{{ nabarr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`nabarr_role_docker_networks_alias`"

        ```yaml
        # Type: string
        nabarr_role_docker_networks_alias: "{{ nabarr_name }}"
        ```

    ??? variable list "`nabarr_role_docker_networks_default`"

        ```yaml
        # Type: list
        nabarr_role_docker_networks_default: []
        ```

    ??? variable list "`nabarr_role_docker_networks_custom`"

        ```yaml
        # Type: list
        nabarr_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`nabarr_role_docker_restart_policy`"

        ```yaml
        # Type: string
        nabarr_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`nabarr_role_docker_state`"

        ```yaml
        # Type: string
        nabarr_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`nabarr_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        nabarr_role_docker_blkio_weight:
        ```

    ??? variable int "`nabarr_role_docker_cpu_period`"

        ```yaml
        # Type: int
        nabarr_role_docker_cpu_period:
        ```

    ??? variable int "`nabarr_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        nabarr_role_docker_cpu_quota:
        ```

    ??? variable int "`nabarr_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        nabarr_role_docker_cpu_shares:
        ```

    ??? variable string "`nabarr_role_docker_cpus`"

        ```yaml
        # Type: string
        nabarr_role_docker_cpus:
        ```

    ??? variable string "`nabarr_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        nabarr_role_docker_cpuset_cpus:
        ```

    ??? variable string "`nabarr_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        nabarr_role_docker_cpuset_mems:
        ```

    ??? variable string "`nabarr_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        nabarr_role_docker_kernel_memory:
        ```

    ??? variable string "`nabarr_role_docker_memory`"

        ```yaml
        # Type: string
        nabarr_role_docker_memory:
        ```

    ??? variable string "`nabarr_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        nabarr_role_docker_memory_reservation:
        ```

    ??? variable string "`nabarr_role_docker_memory_swap`"

        ```yaml
        # Type: string
        nabarr_role_docker_memory_swap:
        ```

    ??? variable int "`nabarr_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        nabarr_role_docker_memory_swappiness:
        ```

    ??? variable string "`nabarr_role_docker_shm_size`"

        ```yaml
        # Type: string
        nabarr_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`nabarr_role_docker_cap_drop`"

        ```yaml
        # Type: list
        nabarr_role_docker_cap_drop:
        ```

    ??? variable string "`nabarr_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        nabarr_role_docker_cgroupns_mode:
        ```

    ??? variable list "`nabarr_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        nabarr_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`nabarr_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        nabarr_role_docker_device_read_bps:
        ```

    ??? variable list "`nabarr_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        nabarr_role_docker_device_read_iops:
        ```

    ??? variable list "`nabarr_role_docker_device_requests`"

        ```yaml
        # Type: list
        nabarr_role_docker_device_requests:
        ```

    ??? variable list "`nabarr_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        nabarr_role_docker_device_write_bps:
        ```

    ??? variable list "`nabarr_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        nabarr_role_docker_device_write_iops:
        ```

    ??? variable list "`nabarr_role_docker_devices`"

        ```yaml
        # Type: list
        nabarr_role_docker_devices:
        ```

    ??? variable string "`nabarr_role_docker_devices_default`"

        ```yaml
        # Type: string
        nabarr_role_docker_devices_default:
        ```

    ??? variable list "`nabarr_role_docker_groups`"

        ```yaml
        # Type: list
        nabarr_role_docker_groups:
        ```

    ??? variable bool "`nabarr_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        nabarr_role_docker_privileged:
        ```

    ??? variable list "`nabarr_role_docker_security_opts`"

        ```yaml
        # Type: list
        nabarr_role_docker_security_opts:
        ```

    ??? variable string "`nabarr_role_docker_user`"

        ```yaml
        # Type: string
        nabarr_role_docker_user:
        ```

    ??? variable string "`nabarr_role_docker_userns_mode`"

        ```yaml
        # Type: string
        nabarr_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`nabarr_role_docker_dns_opts`"

        ```yaml
        # Type: list
        nabarr_role_docker_dns_opts:
        ```

    ??? variable list "`nabarr_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        nabarr_role_docker_dns_search_domains:
        ```

    ??? variable list "`nabarr_role_docker_dns_servers`"

        ```yaml
        # Type: list
        nabarr_role_docker_dns_servers:
        ```

    ??? variable string "`nabarr_role_docker_domainname`"

        ```yaml
        # Type: string
        nabarr_role_docker_domainname:
        ```

    ??? variable list "`nabarr_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        nabarr_role_docker_exposed_ports:
        ```

    ??? variable dict "`nabarr_role_docker_hosts`"

        ```yaml
        # Type: dict
        nabarr_role_docker_hosts:
        ```

    ??? variable bool "`nabarr_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        nabarr_role_docker_hosts_use_common:
        ```

    ??? variable string "`nabarr_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        nabarr_role_docker_ipc_mode:
        ```

    ??? variable list "`nabarr_role_docker_links`"

        ```yaml
        # Type: list
        nabarr_role_docker_links:
        ```

    ??? variable string "`nabarr_role_docker_network_mode`"

        ```yaml
        # Type: string
        nabarr_role_docker_network_mode:
        ```

    ??? variable string "`nabarr_role_docker_pid_mode`"

        ```yaml
        # Type: string
        nabarr_role_docker_pid_mode:
        ```

    ??? variable list "`nabarr_role_docker_ports`"

        ```yaml
        # Type: list
        nabarr_role_docker_ports:
        ```

    ??? variable string "`nabarr_role_docker_uts`"

        ```yaml
        # Type: string
        nabarr_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`nabarr_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        nabarr_role_docker_keep_volumes:
        ```

    ??? variable list "`nabarr_role_docker_mounts`"

        ```yaml
        # Type: list
        nabarr_role_docker_mounts:
        ```

    ??? variable dict "`nabarr_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        nabarr_role_docker_storage_opts:
        ```

    ??? variable list "`nabarr_role_docker_tmpfs`"

        ```yaml
        # Type: list
        nabarr_role_docker_tmpfs:
        ```

    ??? variable string "`nabarr_role_docker_volume_driver`"

        ```yaml
        # Type: string
        nabarr_role_docker_volume_driver:
        ```

    ??? variable list "`nabarr_role_docker_volumes_from`"

        ```yaml
        # Type: list
        nabarr_role_docker_volumes_from:
        ```

    ??? variable bool "`nabarr_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        nabarr_role_docker_volumes_global:
        ```

    ??? variable string "`nabarr_role_docker_working_dir`"

        ```yaml
        # Type: string
        nabarr_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`nabarr_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        nabarr_role_docker_auto_remove:
        ```

    ??? variable bool "`nabarr_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        nabarr_role_docker_cleanup:
        ```

    ??? variable string "`nabarr_role_docker_force_kill`"

        ```yaml
        # Type: string
        nabarr_role_docker_force_kill:
        ```

    ??? variable dict "`nabarr_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        nabarr_role_docker_healthcheck:
        ```

    ??? variable int "`nabarr_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        nabarr_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`nabarr_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        nabarr_role_docker_init:
        ```

    ??? variable string "`nabarr_role_docker_kill_signal`"

        ```yaml
        # Type: string
        nabarr_role_docker_kill_signal:
        ```

    ??? variable string "`nabarr_role_docker_log_driver`"

        ```yaml
        # Type: string
        nabarr_role_docker_log_driver:
        ```

    ??? variable dict "`nabarr_role_docker_log_options`"

        ```yaml
        # Type: dict
        nabarr_role_docker_log_options:
        ```

    ??? variable bool "`nabarr_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        nabarr_role_docker_oom_killer:
        ```

    ??? variable int "`nabarr_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        nabarr_role_docker_oom_score_adj:
        ```

    ??? variable bool "`nabarr_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        nabarr_role_docker_output_logs:
        ```

    ??? variable bool "`nabarr_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        nabarr_role_docker_paused:
        ```

    ??? variable bool "`nabarr_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        nabarr_role_docker_recreate:
        ```

    ??? variable int "`nabarr_role_docker_restart_retries`"

        ```yaml
        # Type: int
        nabarr_role_docker_restart_retries:
        ```

    ??? variable int "`nabarr_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        nabarr_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`nabarr_role_docker_capabilities`"

        ```yaml
        # Type: list
        nabarr_role_docker_capabilities:
        ```

    ??? variable string "`nabarr_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        nabarr_role_docker_cgroup_parent:
        ```

    ??? variable list "`nabarr_role_docker_commands`"

        ```yaml
        # Type: list
        nabarr_role_docker_commands:
        ```

    ??? variable int "`nabarr_role_docker_create_timeout`"

        ```yaml
        # Type: int
        nabarr_role_docker_create_timeout:
        ```

    ??? variable string "`nabarr_role_docker_entrypoint`"

        ```yaml
        # Type: string
        nabarr_role_docker_entrypoint:
        ```

    ??? variable string "`nabarr_role_docker_env_file`"

        ```yaml
        # Type: string
        nabarr_role_docker_env_file:
        ```

    ??? variable dict "`nabarr_role_docker_labels`"

        ```yaml
        # Type: dict
        nabarr_role_docker_labels:
        ```

    ??? variable bool "`nabarr_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        nabarr_role_docker_labels_use_common:
        ```

    ??? variable bool "`nabarr_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        nabarr_role_docker_read_only:
        ```

    ??? variable string "`nabarr_role_docker_runtime`"

        ```yaml
        # Type: string
        nabarr_role_docker_runtime:
        ```

    ??? variable list "`nabarr_role_docker_sysctls`"

        ```yaml
        # Type: list
        nabarr_role_docker_sysctls:
        ```

    ??? variable list "`nabarr_role_docker_ulimits`"

        ```yaml
        # Type: list
        nabarr_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`nabarr_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        nabarr_role_autoheal_enabled: true
        ```

    ??? variable string "`nabarr_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        nabarr_role_depends_on: ""
        ```

    ??? variable string "`nabarr_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        nabarr_role_depends_on_delay: "0"
        ```

    ??? variable string "`nabarr_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        nabarr_role_depends_on_healthchecks:
        ```

    ??? variable bool "`nabarr_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        nabarr_role_diun_enabled: true
        ```

    ??? variable bool "`nabarr_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        nabarr_role_docker_controller: true
        ```

    ??? variable list "`nabarr_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        nabarr_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`nabarr_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        nabarr_role_docker_volumes_download:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

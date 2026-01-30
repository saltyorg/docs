---
icon: material/docker
title: NZBThrottle
hide:
  - tags
tags:
  - nzbthrottle
  - usenet
  - bandwidth
  - automation
saltbox_automation:
  app_links:
    - name: Manual
      url: https://github.com/daghaian/nzbthrottle#readme
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/daghaian/nzbthrottle/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: NZBThrottle
    summary: |-
      a utility that automatically throttles Usenet download speeds based on custom schedules and conditions.
    link: https://github.com/daghaian/nzbthrottle
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# NZBThrottle

## Overview

[NZBThrottle](https://github.com/daghaian/nzbthrottle) is a utility that automatically throttles Usenet download speeds based on custom schedules and conditions.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/daghaian/nzbthrottle#readme){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/daghaian/nzbthrottle/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install nzbthrottle
```

## Usage

NZBThrottle automatically throttles Usenet download speeds based on custom schedules. Configure your download clients (SABnzbd, NZBGet, etc.) and schedules in `/opt/nzbthrottle/config.json`, then restart with `docker restart nzbthrottle`.

Note: Configuration is file-based with no web interface.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        nzbthrottle_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `nzbthrottle_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `nzbthrottle_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`nzbthrottle_name`"

        ```yaml
        # Type: string
        nzbthrottle_name: nzbthrottle
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`nzbthrottle_role_docker_container`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_container: "{{ nzbthrottle_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`nzbthrottle_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_image_pull: true
        ```

    ??? variable string "`nzbthrottle_role_docker_image_repo`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_image_repo: "daghaian/nzbthrottle"
        ```

    ??? variable string "`nzbthrottle_role_docker_image_tag`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_image_tag: "latest"
        ```

    ??? variable string "`nzbthrottle_role_docker_image`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='nzbthrottle') }}:{{ lookup('role_var', '_docker_image_tag', role='nzbthrottle') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`nzbthrottle_role_docker_envs_default`"

        ```yaml
        # Type: dict
        nzbthrottle_role_docker_envs_default:
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`nzbthrottle_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        nzbthrottle_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`nzbthrottle_role_docker_volumes_default`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_volumes_default:
          - "{{ nzbthrottle_role_paths_config_location }}:/nzbthrottle/config.json:ro"
        ```

    ??? variable list "`nzbthrottle_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`nzbthrottle_role_docker_hostname`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_hostname: "{{ nzbthrottle_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`nzbthrottle_role_docker_networks_alias`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_networks_alias: "{{ nzbthrottle_name }}"
        ```

    ??? variable list "`nzbthrottle_role_docker_networks_default`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_networks_default: []
        ```

    ??? variable list "`nzbthrottle_role_docker_networks_custom`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`nzbthrottle_role_docker_restart_policy`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`nzbthrottle_role_docker_state`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`nzbthrottle_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        nzbthrottle_role_docker_blkio_weight:
        ```

    ??? variable int "`nzbthrottle_role_docker_cpu_period`"

        ```yaml
        # Type: int
        nzbthrottle_role_docker_cpu_period:
        ```

    ??? variable int "`nzbthrottle_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        nzbthrottle_role_docker_cpu_quota:
        ```

    ??? variable int "`nzbthrottle_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        nzbthrottle_role_docker_cpu_shares:
        ```

    ??? variable string "`nzbthrottle_role_docker_cpus`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_cpus:
        ```

    ??? variable string "`nzbthrottle_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_cpuset_cpus:
        ```

    ??? variable string "`nzbthrottle_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_cpuset_mems:
        ```

    ??? variable string "`nzbthrottle_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_kernel_memory:
        ```

    ??? variable string "`nzbthrottle_role_docker_memory`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_memory:
        ```

    ??? variable string "`nzbthrottle_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_memory_reservation:
        ```

    ??? variable string "`nzbthrottle_role_docker_memory_swap`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_memory_swap:
        ```

    ??? variable int "`nzbthrottle_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        nzbthrottle_role_docker_memory_swappiness:
        ```

    ??? variable string "`nzbthrottle_role_docker_shm_size`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`nzbthrottle_role_docker_cap_drop`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_cap_drop:
        ```

    ??? variable string "`nzbthrottle_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_cgroupns_mode:
        ```

    ??? variable list "`nzbthrottle_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`nzbthrottle_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_device_read_bps:
        ```

    ??? variable list "`nzbthrottle_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_device_read_iops:
        ```

    ??? variable list "`nzbthrottle_role_docker_device_requests`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_device_requests:
        ```

    ??? variable list "`nzbthrottle_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_device_write_bps:
        ```

    ??? variable list "`nzbthrottle_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_device_write_iops:
        ```

    ??? variable list "`nzbthrottle_role_docker_devices`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_devices:
        ```

    ??? variable string "`nzbthrottle_role_docker_devices_default`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_devices_default:
        ```

    ??? variable list "`nzbthrottle_role_docker_groups`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_groups:
        ```

    ??? variable bool "`nzbthrottle_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_privileged:
        ```

    ??? variable list "`nzbthrottle_role_docker_security_opts`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_security_opts:
        ```

    ??? variable string "`nzbthrottle_role_docker_user`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_user:
        ```

    ??? variable string "`nzbthrottle_role_docker_userns_mode`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`nzbthrottle_role_docker_dns_opts`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_dns_opts:
        ```

    ??? variable list "`nzbthrottle_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_dns_search_domains:
        ```

    ??? variable list "`nzbthrottle_role_docker_dns_servers`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_dns_servers:
        ```

    ??? variable string "`nzbthrottle_role_docker_domainname`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_domainname:
        ```

    ??? variable list "`nzbthrottle_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_exposed_ports:
        ```

    ??? variable dict "`nzbthrottle_role_docker_hosts`"

        ```yaml
        # Type: dict
        nzbthrottle_role_docker_hosts:
        ```

    ??? variable bool "`nzbthrottle_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_hosts_use_common:
        ```

    ??? variable string "`nzbthrottle_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_ipc_mode:
        ```

    ??? variable list "`nzbthrottle_role_docker_links`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_links:
        ```

    ??? variable string "`nzbthrottle_role_docker_network_mode`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_network_mode:
        ```

    ??? variable string "`nzbthrottle_role_docker_pid_mode`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_pid_mode:
        ```

    ??? variable list "`nzbthrottle_role_docker_ports`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_ports:
        ```

    ??? variable string "`nzbthrottle_role_docker_uts`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`nzbthrottle_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_keep_volumes:
        ```

    ??? variable list "`nzbthrottle_role_docker_mounts`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_mounts:
        ```

    ??? variable dict "`nzbthrottle_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        nzbthrottle_role_docker_storage_opts:
        ```

    ??? variable list "`nzbthrottle_role_docker_tmpfs`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_tmpfs:
        ```

    ??? variable string "`nzbthrottle_role_docker_volume_driver`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_volume_driver:
        ```

    ??? variable list "`nzbthrottle_role_docker_volumes_from`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_volumes_from:
        ```

    ??? variable bool "`nzbthrottle_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_volumes_global:
        ```

    ??? variable string "`nzbthrottle_role_docker_working_dir`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`nzbthrottle_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_auto_remove:
        ```

    ??? variable bool "`nzbthrottle_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_cleanup:
        ```

    ??? variable string "`nzbthrottle_role_docker_force_kill`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_force_kill:
        ```

    ??? variable dict "`nzbthrottle_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        nzbthrottle_role_docker_healthcheck:
        ```

    ??? variable int "`nzbthrottle_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        nzbthrottle_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`nzbthrottle_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_init:
        ```

    ??? variable string "`nzbthrottle_role_docker_kill_signal`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_kill_signal:
        ```

    ??? variable string "`nzbthrottle_role_docker_log_driver`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_log_driver:
        ```

    ??? variable dict "`nzbthrottle_role_docker_log_options`"

        ```yaml
        # Type: dict
        nzbthrottle_role_docker_log_options:
        ```

    ??? variable bool "`nzbthrottle_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_oom_killer:
        ```

    ??? variable int "`nzbthrottle_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        nzbthrottle_role_docker_oom_score_adj:
        ```

    ??? variable bool "`nzbthrottle_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_output_logs:
        ```

    ??? variable bool "`nzbthrottle_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_paused:
        ```

    ??? variable bool "`nzbthrottle_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_recreate:
        ```

    ??? variable int "`nzbthrottle_role_docker_restart_retries`"

        ```yaml
        # Type: int
        nzbthrottle_role_docker_restart_retries:
        ```

    ??? variable string "`nzbthrottle_role_docker_stop_signal`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_stop_signal:
        ```

    ??? variable int "`nzbthrottle_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        nzbthrottle_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`nzbthrottle_role_docker_capabilities`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_capabilities:
        ```

    ??? variable string "`nzbthrottle_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_cgroup_parent:
        ```

    ??? variable list "`nzbthrottle_role_docker_commands`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_commands:
        ```

    ??? variable int "`nzbthrottle_role_docker_create_timeout`"

        ```yaml
        # Type: int
        nzbthrottle_role_docker_create_timeout:
        ```

    ??? variable string "`nzbthrottle_role_docker_entrypoint`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_entrypoint:
        ```

    ??? variable string "`nzbthrottle_role_docker_env_file`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_env_file:
        ```

    ??? variable dict "`nzbthrottle_role_docker_labels`"

        ```yaml
        # Type: dict
        nzbthrottle_role_docker_labels:
        ```

    ??? variable bool "`nzbthrottle_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_labels_use_common:
        ```

    ??? variable bool "`nzbthrottle_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_read_only:
        ```

    ??? variable string "`nzbthrottle_role_docker_runtime`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_runtime:
        ```

    ??? variable list "`nzbthrottle_role_docker_sysctls`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_sysctls:
        ```

    ??? variable list "`nzbthrottle_role_docker_ulimits`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`nzbthrottle_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        nzbthrottle_role_autoheal_enabled: true
        ```

    ??? variable string "`nzbthrottle_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        nzbthrottle_role_depends_on: ""
        ```

    ??? variable string "`nzbthrottle_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        nzbthrottle_role_depends_on_delay: "0"
        ```

    ??? variable string "`nzbthrottle_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        nzbthrottle_role_depends_on_healthchecks:
        ```

    ??? variable bool "`nzbthrottle_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        nzbthrottle_role_diun_enabled: true
        ```

    ??? variable bool "`nzbthrottle_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        nzbthrottle_role_docker_controller: true
        ```

    ??? variable list "`nzbthrottle_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`nzbthrottle_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_volumes_download:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

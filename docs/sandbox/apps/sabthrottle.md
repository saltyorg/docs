---
icon: material/docker
hide:
  - tags
tags:
  - sabthrottle
  - automation
  - bandwidth
---

# SABThrottle

## Overview

[SABThrottle](https://github.com/8a8al00ey/sabthrottle) Sabthrottle was designed in order to dynamically control the bandwidth allocation when users are actively streaming from Plex to avoid unnecessary buffering while still allowing the user to download at the fastest rate possible. Remember nzbthrottle from daghaian, yes its exactly like that but for SABnzbd with some additional tweaks.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://github.com/8a8al00ey/sabthrottle#installation){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/8a8al00ey/sabthrottle/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-people-group:**Community**](){ .md-button .md-button--stretch }

</div>

---

## Deployment

```shell
sb install sandbox-sabthrottle
```

## Usage

-   Running the role will autopopulate plex token and plex url.
-   If you require more then 5 stream count just follow the example and add more using proper yml formatting.
-   You can always check logs via

    ```shell
    docker logs -f sabthrottle
    ```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    sabthrottle_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `sabthrottle_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `sabthrottle_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`sabthrottle_name`"

        ```yaml
        # Type: string
        sabthrottle_name: sabthrottle
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`sabthrottle_role_docker_container`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_container: "{{ sabthrottle_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`sabthrottle_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        sabthrottle_role_docker_image_pull: true
        ```

    ??? variable string "`sabthrottle_role_docker_image_repo`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_image_repo: "8a8al00ey/sabthrottle"
        ```

    ??? variable string "`sabthrottle_role_docker_image_tag`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_image_tag: "latest"
        ```

    ??? variable string "`sabthrottle_role_docker_image`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='sabthrottle') }}:{{ lookup('role_var', '_docker_image_tag', role='sabthrottle') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`sabthrottle_role_docker_envs_default`"

        ```yaml
        # Type: dict
        sabthrottle_role_docker_envs_default:
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`sabthrottle_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        sabthrottle_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`sabthrottle_role_docker_volumes_default`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_config_location', role='sabthrottle') }}:/sabthrottle/config.json:ro"
        ```

    ??? variable list "`sabthrottle_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`sabthrottle_role_docker_hostname`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_hostname: "{{ sabthrottle_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`sabthrottle_role_docker_networks_alias`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_networks_alias: "{{ sabthrottle_name }}"
        ```

    ??? variable list "`sabthrottle_role_docker_networks_default`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_networks_default: []
        ```

    ??? variable list "`sabthrottle_role_docker_networks_custom`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`sabthrottle_role_docker_restart_policy`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`sabthrottle_role_docker_state`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`sabthrottle_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        sabthrottle_role_docker_blkio_weight:
        ```

    ??? variable int "`sabthrottle_role_docker_cpu_period`"

        ```yaml
        # Type: int
        sabthrottle_role_docker_cpu_period:
        ```

    ??? variable int "`sabthrottle_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        sabthrottle_role_docker_cpu_quota:
        ```

    ??? variable int "`sabthrottle_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        sabthrottle_role_docker_cpu_shares:
        ```

    ??? variable string "`sabthrottle_role_docker_cpus`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_cpus:
        ```

    ??? variable string "`sabthrottle_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_cpuset_cpus:
        ```

    ??? variable string "`sabthrottle_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_cpuset_mems:
        ```

    ??? variable string "`sabthrottle_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_kernel_memory:
        ```

    ??? variable string "`sabthrottle_role_docker_memory`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_memory:
        ```

    ??? variable string "`sabthrottle_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_memory_reservation:
        ```

    ??? variable string "`sabthrottle_role_docker_memory_swap`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_memory_swap:
        ```

    ??? variable int "`sabthrottle_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        sabthrottle_role_docker_memory_swappiness:
        ```

    ??? variable string "`sabthrottle_role_docker_shm_size`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`sabthrottle_role_docker_cap_drop`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_cap_drop:
        ```

    ??? variable string "`sabthrottle_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_cgroupns_mode:
        ```

    ??? variable list "`sabthrottle_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`sabthrottle_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_device_read_bps:
        ```

    ??? variable list "`sabthrottle_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_device_read_iops:
        ```

    ??? variable list "`sabthrottle_role_docker_device_requests`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_device_requests:
        ```

    ??? variable list "`sabthrottle_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_device_write_bps:
        ```

    ??? variable list "`sabthrottle_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_device_write_iops:
        ```

    ??? variable list "`sabthrottle_role_docker_devices`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_devices:
        ```

    ??? variable string "`sabthrottle_role_docker_devices_default`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_devices_default:
        ```

    ??? variable list "`sabthrottle_role_docker_groups`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_groups:
        ```

    ??? variable bool "`sabthrottle_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        sabthrottle_role_docker_privileged:
        ```

    ??? variable list "`sabthrottle_role_docker_security_opts`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_security_opts:
        ```

    ??? variable string "`sabthrottle_role_docker_user`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_user:
        ```

    ??? variable string "`sabthrottle_role_docker_userns_mode`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`sabthrottle_role_docker_dns_opts`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_dns_opts:
        ```

    ??? variable list "`sabthrottle_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_dns_search_domains:
        ```

    ??? variable list "`sabthrottle_role_docker_dns_servers`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_dns_servers:
        ```

    ??? variable string "`sabthrottle_role_docker_domainname`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_domainname:
        ```

    ??? variable list "`sabthrottle_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_exposed_ports:
        ```

    ??? variable dict "`sabthrottle_role_docker_hosts`"

        ```yaml
        # Type: dict
        sabthrottle_role_docker_hosts:
        ```

    ??? variable bool "`sabthrottle_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        sabthrottle_role_docker_hosts_use_common:
        ```

    ??? variable string "`sabthrottle_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_ipc_mode:
        ```

    ??? variable list "`sabthrottle_role_docker_links`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_links:
        ```

    ??? variable string "`sabthrottle_role_docker_network_mode`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_network_mode:
        ```

    ??? variable string "`sabthrottle_role_docker_pid_mode`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_pid_mode:
        ```

    ??? variable list "`sabthrottle_role_docker_ports`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_ports:
        ```

    ??? variable string "`sabthrottle_role_docker_uts`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`sabthrottle_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        sabthrottle_role_docker_keep_volumes:
        ```

    ??? variable list "`sabthrottle_role_docker_mounts`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_mounts:
        ```

    ??? variable dict "`sabthrottle_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        sabthrottle_role_docker_storage_opts:
        ```

    ??? variable list "`sabthrottle_role_docker_tmpfs`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_tmpfs:
        ```

    ??? variable string "`sabthrottle_role_docker_volume_driver`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_volume_driver:
        ```

    ??? variable list "`sabthrottle_role_docker_volumes_from`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_volumes_from:
        ```

    ??? variable bool "`sabthrottle_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        sabthrottle_role_docker_volumes_global:
        ```

    ??? variable string "`sabthrottle_role_docker_working_dir`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`sabthrottle_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        sabthrottle_role_docker_auto_remove:
        ```

    ??? variable bool "`sabthrottle_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        sabthrottle_role_docker_cleanup:
        ```

    ??? variable string "`sabthrottle_role_docker_force_kill`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_force_kill:
        ```

    ??? variable dict "`sabthrottle_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        sabthrottle_role_docker_healthcheck:
        ```

    ??? variable int "`sabthrottle_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        sabthrottle_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`sabthrottle_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        sabthrottle_role_docker_init:
        ```

    ??? variable string "`sabthrottle_role_docker_kill_signal`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_kill_signal:
        ```

    ??? variable string "`sabthrottle_role_docker_log_driver`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_log_driver:
        ```

    ??? variable dict "`sabthrottle_role_docker_log_options`"

        ```yaml
        # Type: dict
        sabthrottle_role_docker_log_options:
        ```

    ??? variable bool "`sabthrottle_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        sabthrottle_role_docker_oom_killer:
        ```

    ??? variable int "`sabthrottle_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        sabthrottle_role_docker_oom_score_adj:
        ```

    ??? variable bool "`sabthrottle_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        sabthrottle_role_docker_output_logs:
        ```

    ??? variable bool "`sabthrottle_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        sabthrottle_role_docker_paused:
        ```

    ??? variable bool "`sabthrottle_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        sabthrottle_role_docker_recreate:
        ```

    ??? variable int "`sabthrottle_role_docker_restart_retries`"

        ```yaml
        # Type: int
        sabthrottle_role_docker_restart_retries:
        ```

    ??? variable int "`sabthrottle_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        sabthrottle_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`sabthrottle_role_docker_capabilities`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_capabilities:
        ```

    ??? variable string "`sabthrottle_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_cgroup_parent:
        ```

    ??? variable list "`sabthrottle_role_docker_commands`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_commands:
        ```

    ??? variable int "`sabthrottle_role_docker_create_timeout`"

        ```yaml
        # Type: int
        sabthrottle_role_docker_create_timeout:
        ```

    ??? variable string "`sabthrottle_role_docker_entrypoint`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_entrypoint:
        ```

    ??? variable string "`sabthrottle_role_docker_env_file`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_env_file:
        ```

    ??? variable dict "`sabthrottle_role_docker_labels`"

        ```yaml
        # Type: dict
        sabthrottle_role_docker_labels:
        ```

    ??? variable bool "`sabthrottle_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        sabthrottle_role_docker_labels_use_common:
        ```

    ??? variable bool "`sabthrottle_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        sabthrottle_role_docker_read_only:
        ```

    ??? variable string "`sabthrottle_role_docker_runtime`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_runtime:
        ```

    ??? variable list "`sabthrottle_role_docker_sysctls`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_sysctls:
        ```

    ??? variable list "`sabthrottle_role_docker_ulimits`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`sabthrottle_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        sabthrottle_role_autoheal_enabled: true
        ```

    ??? variable string "`sabthrottle_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        sabthrottle_role_depends_on: ""
        ```

    ??? variable string "`sabthrottle_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        sabthrottle_role_depends_on_delay: "0"
        ```

    ??? variable string "`sabthrottle_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        sabthrottle_role_depends_on_healthchecks:
        ```

    ??? variable bool "`sabthrottle_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        sabthrottle_role_diun_enabled: true
        ```

    ??? variable bool "`sabthrottle_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        sabthrottle_role_docker_controller: true
        ```

    ??? variable string "`sabthrottle_role_docker_image_repo`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_image_repo:
        ```

    ??? variable string "`sabthrottle_role_docker_image_tag`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_image_tag:
        ```

    ??? variable bool "`sabthrottle_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        sabthrottle_role_docker_volumes_download:
        ```

    ??? variable string "`sabthrottle_role_paths_config_location`"

        ```yaml
        # Type: string
        sabthrottle_role_paths_config_location:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
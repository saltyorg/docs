---
icon: material/docker
hide:
  - tags
tags:
  - influxdb
  - database
  - timeseries
---

# InfluxDB

## Overview

[InfluxDB](https://www.influxdata.com/products/influxdb/) is an open source time series database for recording metrics, events, and analytics.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](hhttps://docs.influxdata.com/influxdb/v1){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/_/influxdb/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-people-group:**Community**](){ .md-button .md-button--stretch }

</div>

---

!!! note
    This role is version locked to version `1.8.4` to support the `varken` role. To utilize InfluxDB version 2.0, utilize the `influxdb2` role.

## Deployment

```shell
sb install sandbox-influxdb
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        influxdb_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `influxdb_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `influxdb_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`influxdb_name`"

        ```yaml
        # Type: string
        influxdb_name: influxdb
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`influxdb_role_docker_container`"

        ```yaml
        # Type: string
        influxdb_role_docker_container: "{{ influxdb_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`influxdb_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        influxdb_role_docker_image_pull: true
        ```

    ??? variable string "`influxdb_role_docker_image_repo`"

        ```yaml
        # Type: string
        influxdb_role_docker_image_repo: "influxdb"
        ```

    ??? variable string "`influxdb_role_docker_image_tag`"

        ```yaml
        # Type: string
        influxdb_role_docker_image_tag: "1.12"
        ```

    ??? variable string "`influxdb_role_docker_image`"

        ```yaml
        # Type: string
        influxdb_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='influxdb') }}:{{ lookup('role_var', '_docker_image_tag', role='influxdb') }}"
        ```

    <h5>Volumes</h5>

    ??? variable list "`influxdb_role_docker_volumes_default`"

        ```yaml
        # Type: list
        influxdb_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='influxdb') }}:/var/lib/influxdb"
        ```

    ??? variable list "`influxdb_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        influxdb_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`influxdb_role_docker_hostname`"

        ```yaml
        # Type: string
        influxdb_role_docker_hostname: "{{ influxdb_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`influxdb_role_docker_networks_alias`"

        ```yaml
        # Type: string
        influxdb_role_docker_networks_alias: "{{ influxdb_name }}"
        ```

    ??? variable list "`influxdb_role_docker_networks_default`"

        ```yaml
        # Type: list
        influxdb_role_docker_networks_default: []
        ```

    ??? variable list "`influxdb_role_docker_networks_custom`"

        ```yaml
        # Type: list
        influxdb_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`influxdb_role_docker_restart_policy`"

        ```yaml
        # Type: string
        influxdb_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`influxdb_role_docker_state`"

        ```yaml
        # Type: string
        influxdb_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`influxdb_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        influxdb_role_docker_blkio_weight:
        ```

    ??? variable int "`influxdb_role_docker_cpu_period`"

        ```yaml
        # Type: int
        influxdb_role_docker_cpu_period:
        ```

    ??? variable int "`influxdb_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        influxdb_role_docker_cpu_quota:
        ```

    ??? variable int "`influxdb_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        influxdb_role_docker_cpu_shares:
        ```

    ??? variable string "`influxdb_role_docker_cpus`"

        ```yaml
        # Type: string
        influxdb_role_docker_cpus:
        ```

    ??? variable string "`influxdb_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        influxdb_role_docker_cpuset_cpus:
        ```

    ??? variable string "`influxdb_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        influxdb_role_docker_cpuset_mems:
        ```

    ??? variable string "`influxdb_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        influxdb_role_docker_kernel_memory:
        ```

    ??? variable string "`influxdb_role_docker_memory`"

        ```yaml
        # Type: string
        influxdb_role_docker_memory:
        ```

    ??? variable string "`influxdb_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        influxdb_role_docker_memory_reservation:
        ```

    ??? variable string "`influxdb_role_docker_memory_swap`"

        ```yaml
        # Type: string
        influxdb_role_docker_memory_swap:
        ```

    ??? variable int "`influxdb_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        influxdb_role_docker_memory_swappiness:
        ```

    ??? variable string "`influxdb_role_docker_shm_size`"

        ```yaml
        # Type: string
        influxdb_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`influxdb_role_docker_cap_drop`"

        ```yaml
        # Type: list
        influxdb_role_docker_cap_drop:
        ```

    ??? variable string "`influxdb_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        influxdb_role_docker_cgroupns_mode:
        ```

    ??? variable list "`influxdb_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        influxdb_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`influxdb_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        influxdb_role_docker_device_read_bps:
        ```

    ??? variable list "`influxdb_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        influxdb_role_docker_device_read_iops:
        ```

    ??? variable list "`influxdb_role_docker_device_requests`"

        ```yaml
        # Type: list
        influxdb_role_docker_device_requests:
        ```

    ??? variable list "`influxdb_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        influxdb_role_docker_device_write_bps:
        ```

    ??? variable list "`influxdb_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        influxdb_role_docker_device_write_iops:
        ```

    ??? variable list "`influxdb_role_docker_devices`"

        ```yaml
        # Type: list
        influxdb_role_docker_devices:
        ```

    ??? variable string "`influxdb_role_docker_devices_default`"

        ```yaml
        # Type: string
        influxdb_role_docker_devices_default:
        ```

    ??? variable list "`influxdb_role_docker_groups`"

        ```yaml
        # Type: list
        influxdb_role_docker_groups:
        ```

    ??? variable bool "`influxdb_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        influxdb_role_docker_privileged:
        ```

    ??? variable list "`influxdb_role_docker_security_opts`"

        ```yaml
        # Type: list
        influxdb_role_docker_security_opts:
        ```

    ??? variable string "`influxdb_role_docker_user`"

        ```yaml
        # Type: string
        influxdb_role_docker_user:
        ```

    ??? variable string "`influxdb_role_docker_userns_mode`"

        ```yaml
        # Type: string
        influxdb_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`influxdb_role_docker_dns_opts`"

        ```yaml
        # Type: list
        influxdb_role_docker_dns_opts:
        ```

    ??? variable list "`influxdb_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        influxdb_role_docker_dns_search_domains:
        ```

    ??? variable list "`influxdb_role_docker_dns_servers`"

        ```yaml
        # Type: list
        influxdb_role_docker_dns_servers:
        ```

    ??? variable string "`influxdb_role_docker_domainname`"

        ```yaml
        # Type: string
        influxdb_role_docker_domainname:
        ```

    ??? variable list "`influxdb_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        influxdb_role_docker_exposed_ports:
        ```

    ??? variable dict "`influxdb_role_docker_hosts`"

        ```yaml
        # Type: dict
        influxdb_role_docker_hosts:
        ```

    ??? variable bool "`influxdb_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        influxdb_role_docker_hosts_use_common:
        ```

    ??? variable string "`influxdb_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        influxdb_role_docker_ipc_mode:
        ```

    ??? variable list "`influxdb_role_docker_links`"

        ```yaml
        # Type: list
        influxdb_role_docker_links:
        ```

    ??? variable string "`influxdb_role_docker_network_mode`"

        ```yaml
        # Type: string
        influxdb_role_docker_network_mode:
        ```

    ??? variable string "`influxdb_role_docker_pid_mode`"

        ```yaml
        # Type: string
        influxdb_role_docker_pid_mode:
        ```

    ??? variable list "`influxdb_role_docker_ports`"

        ```yaml
        # Type: list
        influxdb_role_docker_ports:
        ```

    ??? variable string "`influxdb_role_docker_uts`"

        ```yaml
        # Type: string
        influxdb_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`influxdb_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        influxdb_role_docker_keep_volumes:
        ```

    ??? variable list "`influxdb_role_docker_mounts`"

        ```yaml
        # Type: list
        influxdb_role_docker_mounts:
        ```

    ??? variable dict "`influxdb_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        influxdb_role_docker_storage_opts:
        ```

    ??? variable list "`influxdb_role_docker_tmpfs`"

        ```yaml
        # Type: list
        influxdb_role_docker_tmpfs:
        ```

    ??? variable string "`influxdb_role_docker_volume_driver`"

        ```yaml
        # Type: string
        influxdb_role_docker_volume_driver:
        ```

    ??? variable list "`influxdb_role_docker_volumes_from`"

        ```yaml
        # Type: list
        influxdb_role_docker_volumes_from:
        ```

    ??? variable bool "`influxdb_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        influxdb_role_docker_volumes_global:
        ```

    ??? variable string "`influxdb_role_docker_working_dir`"

        ```yaml
        # Type: string
        influxdb_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`influxdb_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        influxdb_role_docker_auto_remove:
        ```

    ??? variable bool "`influxdb_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        influxdb_role_docker_cleanup:
        ```

    ??? variable string "`influxdb_role_docker_force_kill`"

        ```yaml
        # Type: string
        influxdb_role_docker_force_kill:
        ```

    ??? variable dict "`influxdb_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        influxdb_role_docker_healthcheck:
        ```

    ??? variable int "`influxdb_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        influxdb_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`influxdb_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        influxdb_role_docker_init:
        ```

    ??? variable string "`influxdb_role_docker_kill_signal`"

        ```yaml
        # Type: string
        influxdb_role_docker_kill_signal:
        ```

    ??? variable string "`influxdb_role_docker_log_driver`"

        ```yaml
        # Type: string
        influxdb_role_docker_log_driver:
        ```

    ??? variable dict "`influxdb_role_docker_log_options`"

        ```yaml
        # Type: dict
        influxdb_role_docker_log_options:
        ```

    ??? variable bool "`influxdb_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        influxdb_role_docker_oom_killer:
        ```

    ??? variable int "`influxdb_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        influxdb_role_docker_oom_score_adj:
        ```

    ??? variable bool "`influxdb_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        influxdb_role_docker_output_logs:
        ```

    ??? variable bool "`influxdb_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        influxdb_role_docker_paused:
        ```

    ??? variable bool "`influxdb_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        influxdb_role_docker_recreate:
        ```

    ??? variable int "`influxdb_role_docker_restart_retries`"

        ```yaml
        # Type: int
        influxdb_role_docker_restart_retries:
        ```

    ??? variable int "`influxdb_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        influxdb_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`influxdb_role_docker_capabilities`"

        ```yaml
        # Type: list
        influxdb_role_docker_capabilities:
        ```

    ??? variable string "`influxdb_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        influxdb_role_docker_cgroup_parent:
        ```

    ??? variable list "`influxdb_role_docker_commands`"

        ```yaml
        # Type: list
        influxdb_role_docker_commands:
        ```

    ??? variable int "`influxdb_role_docker_create_timeout`"

        ```yaml
        # Type: int
        influxdb_role_docker_create_timeout:
        ```

    ??? variable string "`influxdb_role_docker_entrypoint`"

        ```yaml
        # Type: string
        influxdb_role_docker_entrypoint:
        ```

    ??? variable string "`influxdb_role_docker_env_file`"

        ```yaml
        # Type: string
        influxdb_role_docker_env_file:
        ```

    ??? variable dict "`influxdb_role_docker_envs`"

        ```yaml
        # Type: dict
        influxdb_role_docker_envs:
        ```

    ??? variable dict "`influxdb_role_docker_labels`"

        ```yaml
        # Type: dict
        influxdb_role_docker_labels:
        ```

    ??? variable bool "`influxdb_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        influxdb_role_docker_labels_use_common:
        ```

    ??? variable bool "`influxdb_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        influxdb_role_docker_read_only:
        ```

    ??? variable string "`influxdb_role_docker_runtime`"

        ```yaml
        # Type: string
        influxdb_role_docker_runtime:
        ```

    ??? variable list "`influxdb_role_docker_sysctls`"

        ```yaml
        # Type: list
        influxdb_role_docker_sysctls:
        ```

    ??? variable list "`influxdb_role_docker_ulimits`"

        ```yaml
        # Type: list
        influxdb_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`influxdb_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        influxdb_role_autoheal_enabled: true
        ```

    ??? variable string "`influxdb_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        influxdb_role_depends_on: ""
        ```

    ??? variable string "`influxdb_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        influxdb_role_depends_on_delay: "0"
        ```

    ??? variable string "`influxdb_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        influxdb_role_depends_on_healthchecks:
        ```

    ??? variable bool "`influxdb_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        influxdb_role_diun_enabled: true
        ```

    ??? variable bool "`influxdb_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        influxdb_role_docker_controller: true
        ```

    ??? variable string "`influxdb_role_docker_image_repo`"

        ```yaml
        # Type: string
        influxdb_role_docker_image_repo:
        ```

    ??? variable string "`influxdb_role_docker_image_tag`"

        ```yaml
        # Type: string
        influxdb_role_docker_image_tag:
        ```

    ??? variable bool "`influxdb_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        influxdb_role_docker_volumes_download:
        ```

    ??? variable string "`influxdb_role_paths_location`"

        ```yaml
        # Type: string
        influxdb_role_paths_location:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
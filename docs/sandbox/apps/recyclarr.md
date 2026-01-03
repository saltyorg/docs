---
icon: material/docker
hide:
  - tags
tags:
  - recyclarr
  - sonarr
  - radarr
---

# Recyclarr

## Overview

[Recyclarr](https://github.com/recyclarr/recyclarr) automatically synchronizes recommended settings from TRaSH guides to your Sonarr/Radarr instances.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://recyclarr.dev/wiki){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/recyclarr/recyclarr/pkgs/container/recyclarr){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://discord.com/invite/Vau8dZ3){ .md-button .md-button--stretch }

</div>

---

## Configuration

Edit the Recyclarr section in Sandbox `settings.yml` and enter your desired update schedule using standard cron syntax.

```yaml
     recyclarr:
       cron_schedule: "@daily"
```

!!! note
    If you change this value, you must re-run `sb install sandbox-recyclarr` for it take effect.

If a config file does not exist, a default config is generated but it is not functional out of the box. Edit the file `/opt/recyclarr/recyclarr.yml` to provision your Sonarr/Radarr details and preferred settings.

- Configure Sonarr section

  ```yaml
      sonarr:
        sonarr:
          base_url: http://sonarr:8989
          api_key: your_sonarr_api_key
  ```

- Configure Radarr section

  ```yaml
      radarr:
        radarr:
          base_url: http://radarr:7878
          api_key: your_radarr_api_key
  ```

Follow documentation to complete configuration

## Deployment

```shell
sb install sandbox-recyclarr
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables.<span title="View override details for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        recyclarr_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `recyclarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `recyclarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`recyclarr_name`"

        ```yaml
        # Type: string
        recyclarr_name: recyclarr
        ```

=== "Settings"

    ??? variable string "`recyclarr_role_cron_schedule`"

        ```yaml
        # Type: string
        recyclarr_role_cron_schedule: "@daily"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`recyclarr_role_docker_container`"

        ```yaml
        # Type: string
        recyclarr_role_docker_container: "{{ recyclarr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`recyclarr_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        recyclarr_role_docker_image_pull: true
        ```

    ??? variable string "`recyclarr_role_docker_image_repo`"

        ```yaml
        # Type: string
        recyclarr_role_docker_image_repo: "ghcr.io/recyclarr/recyclarr"
        ```

    ??? variable string "`recyclarr_role_docker_image_tag`"

        ```yaml
        # Type: string
        recyclarr_role_docker_image_tag: "latest"
        ```

    ??? variable string "`recyclarr_role_docker_image`"

        ```yaml
        # Type: string
        recyclarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='recyclarr') }}:{{ lookup('role_var', '_docker_image_tag', role='recyclarr') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`recyclarr_role_docker_envs_default`"

        ```yaml
        # Type: dict
        recyclarr_role_docker_envs_default:
          TZ: "{{ tz }}"
          CRON_SCHEDULE: "{{ lookup('role_var', '_cron_schedule', role='recyclarr') }}"
          RECYCLARR_CREATE_CONFIG: "true"
        ```

    ??? variable dict "`recyclarr_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        recyclarr_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`recyclarr_role_docker_volumes_default`"

        ```yaml
        # Type: list
        recyclarr_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='recyclarr') }}:/config"
        ```

    ??? variable list "`recyclarr_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        recyclarr_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`recyclarr_role_docker_hostname`"

        ```yaml
        # Type: string
        recyclarr_role_docker_hostname: "{{ recyclarr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`recyclarr_role_docker_networks_alias`"

        ```yaml
        # Type: string
        recyclarr_role_docker_networks_alias: "{{ recyclarr_name }}"
        ```

    ??? variable list "`recyclarr_role_docker_networks_default`"

        ```yaml
        # Type: list
        recyclarr_role_docker_networks_default: []
        ```

    ??? variable list "`recyclarr_role_docker_networks_custom`"

        ```yaml
        # Type: list
        recyclarr_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`recyclarr_role_docker_restart_policy`"

        ```yaml
        # Type: string
        recyclarr_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`recyclarr_role_docker_state`"

        ```yaml
        # Type: string
        recyclarr_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`recyclarr_role_docker_user`"

        ```yaml
        # Type: string
        recyclarr_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`recyclarr_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        recyclarr_role_docker_blkio_weight:
        ```

    ??? variable int "`recyclarr_role_docker_cpu_period`"

        ```yaml
        # Type: int
        recyclarr_role_docker_cpu_period:
        ```

    ??? variable int "`recyclarr_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        recyclarr_role_docker_cpu_quota:
        ```

    ??? variable int "`recyclarr_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        recyclarr_role_docker_cpu_shares:
        ```

    ??? variable string "`recyclarr_role_docker_cpus`"

        ```yaml
        # Type: string
        recyclarr_role_docker_cpus:
        ```

    ??? variable string "`recyclarr_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        recyclarr_role_docker_cpuset_cpus:
        ```

    ??? variable string "`recyclarr_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        recyclarr_role_docker_cpuset_mems:
        ```

    ??? variable string "`recyclarr_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        recyclarr_role_docker_kernel_memory:
        ```

    ??? variable string "`recyclarr_role_docker_memory`"

        ```yaml
        # Type: string
        recyclarr_role_docker_memory:
        ```

    ??? variable string "`recyclarr_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        recyclarr_role_docker_memory_reservation:
        ```

    ??? variable string "`recyclarr_role_docker_memory_swap`"

        ```yaml
        # Type: string
        recyclarr_role_docker_memory_swap:
        ```

    ??? variable int "`recyclarr_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        recyclarr_role_docker_memory_swappiness:
        ```

    ??? variable string "`recyclarr_role_docker_shm_size`"

        ```yaml
        # Type: string
        recyclarr_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`recyclarr_role_docker_cap_drop`"

        ```yaml
        # Type: list
        recyclarr_role_docker_cap_drop:
        ```

    ??? variable string "`recyclarr_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        recyclarr_role_docker_cgroupns_mode:
        ```

    ??? variable list "`recyclarr_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        recyclarr_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`recyclarr_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        recyclarr_role_docker_device_read_bps:
        ```

    ??? variable list "`recyclarr_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        recyclarr_role_docker_device_read_iops:
        ```

    ??? variable list "`recyclarr_role_docker_device_requests`"

        ```yaml
        # Type: list
        recyclarr_role_docker_device_requests:
        ```

    ??? variable list "`recyclarr_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        recyclarr_role_docker_device_write_bps:
        ```

    ??? variable list "`recyclarr_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        recyclarr_role_docker_device_write_iops:
        ```

    ??? variable list "`recyclarr_role_docker_devices`"

        ```yaml
        # Type: list
        recyclarr_role_docker_devices:
        ```

    ??? variable string "`recyclarr_role_docker_devices_default`"

        ```yaml
        # Type: string
        recyclarr_role_docker_devices_default:
        ```

    ??? variable list "`recyclarr_role_docker_groups`"

        ```yaml
        # Type: list
        recyclarr_role_docker_groups:
        ```

    ??? variable bool "`recyclarr_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        recyclarr_role_docker_privileged:
        ```

    ??? variable list "`recyclarr_role_docker_security_opts`"

        ```yaml
        # Type: list
        recyclarr_role_docker_security_opts:
        ```

    ??? variable string "`recyclarr_role_docker_userns_mode`"

        ```yaml
        # Type: string
        recyclarr_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`recyclarr_role_docker_dns_opts`"

        ```yaml
        # Type: list
        recyclarr_role_docker_dns_opts:
        ```

    ??? variable list "`recyclarr_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        recyclarr_role_docker_dns_search_domains:
        ```

    ??? variable list "`recyclarr_role_docker_dns_servers`"

        ```yaml
        # Type: list
        recyclarr_role_docker_dns_servers:
        ```

    ??? variable string "`recyclarr_role_docker_domainname`"

        ```yaml
        # Type: string
        recyclarr_role_docker_domainname:
        ```

    ??? variable list "`recyclarr_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        recyclarr_role_docker_exposed_ports:
        ```

    ??? variable dict "`recyclarr_role_docker_hosts`"

        ```yaml
        # Type: dict
        recyclarr_role_docker_hosts:
        ```

    ??? variable bool "`recyclarr_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        recyclarr_role_docker_hosts_use_common:
        ```

    ??? variable string "`recyclarr_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        recyclarr_role_docker_ipc_mode:
        ```

    ??? variable list "`recyclarr_role_docker_links`"

        ```yaml
        # Type: list
        recyclarr_role_docker_links:
        ```

    ??? variable string "`recyclarr_role_docker_network_mode`"

        ```yaml
        # Type: string
        recyclarr_role_docker_network_mode:
        ```

    ??? variable string "`recyclarr_role_docker_pid_mode`"

        ```yaml
        # Type: string
        recyclarr_role_docker_pid_mode:
        ```

    ??? variable list "`recyclarr_role_docker_ports`"

        ```yaml
        # Type: list
        recyclarr_role_docker_ports:
        ```

    ??? variable string "`recyclarr_role_docker_uts`"

        ```yaml
        # Type: string
        recyclarr_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`recyclarr_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        recyclarr_role_docker_keep_volumes:
        ```

    ??? variable list "`recyclarr_role_docker_mounts`"

        ```yaml
        # Type: list
        recyclarr_role_docker_mounts:
        ```

    ??? variable dict "`recyclarr_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        recyclarr_role_docker_storage_opts:
        ```

    ??? variable list "`recyclarr_role_docker_tmpfs`"

        ```yaml
        # Type: list
        recyclarr_role_docker_tmpfs:
        ```

    ??? variable string "`recyclarr_role_docker_volume_driver`"

        ```yaml
        # Type: string
        recyclarr_role_docker_volume_driver:
        ```

    ??? variable list "`recyclarr_role_docker_volumes_from`"

        ```yaml
        # Type: list
        recyclarr_role_docker_volumes_from:
        ```

    ??? variable bool "`recyclarr_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        recyclarr_role_docker_volumes_global:
        ```

    ??? variable string "`recyclarr_role_docker_working_dir`"

        ```yaml
        # Type: string
        recyclarr_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`recyclarr_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        recyclarr_role_docker_auto_remove:
        ```

    ??? variable bool "`recyclarr_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        recyclarr_role_docker_cleanup:
        ```

    ??? variable string "`recyclarr_role_docker_force_kill`"

        ```yaml
        # Type: string
        recyclarr_role_docker_force_kill:
        ```

    ??? variable dict "`recyclarr_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        recyclarr_role_docker_healthcheck:
        ```

    ??? variable int "`recyclarr_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        recyclarr_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`recyclarr_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        recyclarr_role_docker_init:
        ```

    ??? variable string "`recyclarr_role_docker_kill_signal`"

        ```yaml
        # Type: string
        recyclarr_role_docker_kill_signal:
        ```

    ??? variable string "`recyclarr_role_docker_log_driver`"

        ```yaml
        # Type: string
        recyclarr_role_docker_log_driver:
        ```

    ??? variable dict "`recyclarr_role_docker_log_options`"

        ```yaml
        # Type: dict
        recyclarr_role_docker_log_options:
        ```

    ??? variable bool "`recyclarr_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        recyclarr_role_docker_oom_killer:
        ```

    ??? variable int "`recyclarr_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        recyclarr_role_docker_oom_score_adj:
        ```

    ??? variable bool "`recyclarr_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        recyclarr_role_docker_output_logs:
        ```

    ??? variable bool "`recyclarr_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        recyclarr_role_docker_paused:
        ```

    ??? variable bool "`recyclarr_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        recyclarr_role_docker_recreate:
        ```

    ??? variable int "`recyclarr_role_docker_restart_retries`"

        ```yaml
        # Type: int
        recyclarr_role_docker_restart_retries:
        ```

    ??? variable int "`recyclarr_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        recyclarr_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`recyclarr_role_docker_capabilities`"

        ```yaml
        # Type: list
        recyclarr_role_docker_capabilities:
        ```

    ??? variable string "`recyclarr_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        recyclarr_role_docker_cgroup_parent:
        ```

    ??? variable list "`recyclarr_role_docker_commands`"

        ```yaml
        # Type: list
        recyclarr_role_docker_commands:
        ```

    ??? variable int "`recyclarr_role_docker_create_timeout`"

        ```yaml
        # Type: int
        recyclarr_role_docker_create_timeout:
        ```

    ??? variable string "`recyclarr_role_docker_entrypoint`"

        ```yaml
        # Type: string
        recyclarr_role_docker_entrypoint:
        ```

    ??? variable string "`recyclarr_role_docker_env_file`"

        ```yaml
        # Type: string
        recyclarr_role_docker_env_file:
        ```

    ??? variable dict "`recyclarr_role_docker_labels`"

        ```yaml
        # Type: dict
        recyclarr_role_docker_labels:
        ```

    ??? variable bool "`recyclarr_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        recyclarr_role_docker_labels_use_common:
        ```

    ??? variable bool "`recyclarr_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        recyclarr_role_docker_read_only:
        ```

    ??? variable string "`recyclarr_role_docker_runtime`"

        ```yaml
        # Type: string
        recyclarr_role_docker_runtime:
        ```

    ??? variable list "`recyclarr_role_docker_sysctls`"

        ```yaml
        # Type: list
        recyclarr_role_docker_sysctls:
        ```

    ??? variable list "`recyclarr_role_docker_ulimits`"

        ```yaml
        # Type: list
        recyclarr_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`recyclarr_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        recyclarr_role_autoheal_enabled: true
        ```

    ??? variable string "`recyclarr_role_cron_schedule`"

        ```yaml
        # Type: string
        recyclarr_role_cron_schedule:
        ```

    ??? variable string "`recyclarr_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        recyclarr_role_depends_on: ""
        ```

    ??? variable string "`recyclarr_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        recyclarr_role_depends_on_delay: "0"
        ```

    ??? variable string "`recyclarr_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        recyclarr_role_depends_on_healthchecks:
        ```

    ??? variable bool "`recyclarr_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        recyclarr_role_diun_enabled: true
        ```

    ??? variable bool "`recyclarr_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        recyclarr_role_docker_controller: true
        ```

    ??? variable string "`recyclarr_role_docker_image_repo`"

        ```yaml
        # Type: string
        recyclarr_role_docker_image_repo:
        ```

    ??? variable string "`recyclarr_role_docker_image_tag`"

        ```yaml
        # Type: string
        recyclarr_role_docker_image_tag:
        ```

    ??? variable bool "`recyclarr_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        recyclarr_role_docker_volumes_download:
        ```

    ??? variable string "`recyclarr_role_paths_location`"

        ```yaml
        # Type: string
        recyclarr_role_paths_location:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
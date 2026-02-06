---
icon: material/docker
hide:
  - tags
tags:
  - diun
saltbox_automation:
  app_links:
    - name: Manual
      url: https://crazymax.dev/diun/notif/discord
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/crazymax/diun/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Diun
    summary: |-
      a CLI application designed to receive notifications when a Docker image is updated on a Docker registry.
    link: https://crazymax.dev/diun
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Diun

## Overview

[Diun](https://crazymax.dev/diun) is a CLI application designed to receive notifications when a Docker image is updated on a Docker registry.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://crazymax.dev/diun/notif/discord){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/crazymax/diun/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install diun
```

## Basics

The config file for diun is located at `/opt/diun/diun.yml`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        diun_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `diun_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `diun_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`diun_name`"

        ```yaml
        # Type: string
        diun_name: diun
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`diun_role_docker_container`"

        ```yaml
        # Type: string
        diun_role_docker_container: "{{ diun_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`diun_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_image_pull: true
        ```

    ??? variable string "`diun_role_docker_image_repo`"

        ```yaml
        # Type: string
        diun_role_docker_image_repo: "crazymax/diun"
        ```

    ??? variable string "`diun_role_docker_image_tag`"

        ```yaml
        # Type: string
        diun_role_docker_image_tag: "latest"
        ```

    ??? variable string "`diun_role_docker_image`"

        ```yaml
        # Type: string
        diun_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='diun') }}:{{ lookup('role_var', '_docker_image_tag', role='diun') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`diun_role_docker_envs_default`"

        ```yaml
        # Type: dict
        diun_role_docker_envs_default:
          TZ: "{{ tz }}"
          LOG_LEVEL: "info"
          LOG_JSON: "false"
        ```

    ??? variable dict "`diun_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        diun_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`diun_role_docker_volumes_default`"

        ```yaml
        # Type: list
        diun_role_docker_volumes_default:
          - "{{ diun_role_paths_location }}/data:/data"
          - "{{ diun_role_paths_location }}/diun.yml:/diun.yml:ro"
          - "/var/run/docker.sock:/var/run/docker.sock"
        ```

    ??? variable list "`diun_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        diun_role_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable dict "`diun_role_docker_labels_default`"

        ```yaml
        # Type: dict
        diun_role_docker_labels_default:
          diun.enable: "true"
        ```

    ??? variable dict "`diun_role_docker_labels_custom`"

        ```yaml
        # Type: dict
        diun_role_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`diun_role_docker_hostname`"

        ```yaml
        # Type: string
        diun_role_docker_hostname: "{{ diun_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`diun_role_docker_networks_alias`"

        ```yaml
        # Type: string
        diun_role_docker_networks_alias: "{{ diun_name }}"
        ```

    ??? variable list "`diun_role_docker_networks_default`"

        ```yaml
        # Type: list
        diun_role_docker_networks_default: []
        ```

    ??? variable list "`diun_role_docker_networks_custom`"

        ```yaml
        # Type: list
        diun_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`diun_role_docker_restart_policy`"

        ```yaml
        # Type: string
        diun_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`diun_role_docker_state`"

        ```yaml
        # Type: string
        diun_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`diun_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        diun_role_docker_blkio_weight:
        ```

    ??? variable int "`diun_role_docker_cpu_period`"

        ```yaml
        # Type: int
        diun_role_docker_cpu_period:
        ```

    ??? variable int "`diun_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        diun_role_docker_cpu_quota:
        ```

    ??? variable int "`diun_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        diun_role_docker_cpu_shares:
        ```

    ??? variable string "`diun_role_docker_cpus`"

        ```yaml
        # Type: string
        diun_role_docker_cpus:
        ```

    ??? variable string "`diun_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        diun_role_docker_cpuset_cpus:
        ```

    ??? variable string "`diun_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        diun_role_docker_cpuset_mems:
        ```

    ??? variable string "`diun_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        diun_role_docker_kernel_memory:
        ```

    ??? variable string "`diun_role_docker_memory`"

        ```yaml
        # Type: string
        diun_role_docker_memory:
        ```

    ??? variable string "`diun_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        diun_role_docker_memory_reservation:
        ```

    ??? variable string "`diun_role_docker_memory_swap`"

        ```yaml
        # Type: string
        diun_role_docker_memory_swap:
        ```

    ??? variable int "`diun_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        diun_role_docker_memory_swappiness:
        ```

    ??? variable string "`diun_role_docker_shm_size`"

        ```yaml
        # Type: string
        diun_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`diun_role_docker_cap_drop`"

        ```yaml
        # Type: list
        diun_role_docker_cap_drop:
        ```

    ??? variable string "`diun_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        diun_role_docker_cgroupns_mode:
        ```

    ??? variable list "`diun_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        diun_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`diun_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        diun_role_docker_device_read_bps:
        ```

    ??? variable list "`diun_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        diun_role_docker_device_read_iops:
        ```

    ??? variable list "`diun_role_docker_device_requests`"

        ```yaml
        # Type: list
        diun_role_docker_device_requests:
        ```

    ??? variable list "`diun_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        diun_role_docker_device_write_bps:
        ```

    ??? variable list "`diun_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        diun_role_docker_device_write_iops:
        ```

    ??? variable list "`diun_role_docker_devices`"

        ```yaml
        # Type: list
        diun_role_docker_devices:
        ```

    ??? variable list "`diun_role_docker_groups`"

        ```yaml
        # Type: list
        diun_role_docker_groups:
        ```

    ??? variable bool "`diun_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_privileged:
        ```

    ??? variable list "`diun_role_docker_security_opts`"

        ```yaml
        # Type: list
        diun_role_docker_security_opts:
        ```

    ??? variable string "`diun_role_docker_user`"

        ```yaml
        # Type: string
        diun_role_docker_user:
        ```

    ??? variable string "`diun_role_docker_userns_mode`"

        ```yaml
        # Type: string
        diun_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`diun_role_docker_dns_opts`"

        ```yaml
        # Type: list
        diun_role_docker_dns_opts:
        ```

    ??? variable list "`diun_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        diun_role_docker_dns_search_domains:
        ```

    ??? variable list "`diun_role_docker_dns_servers`"

        ```yaml
        # Type: list
        diun_role_docker_dns_servers:
        ```

    ??? variable string "`diun_role_docker_domainname`"

        ```yaml
        # Type: string
        diun_role_docker_domainname:
        ```

    ??? variable list "`diun_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        diun_role_docker_exposed_ports:
        ```

    ??? variable dict "`diun_role_docker_hosts`"

        ```yaml
        # Type: dict
        diun_role_docker_hosts:
        ```

    ??? variable bool "`diun_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_hosts_use_common:
        ```

    ??? variable string "`diun_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        diun_role_docker_ipc_mode:
        ```

    ??? variable list "`diun_role_docker_links`"

        ```yaml
        # Type: list
        diun_role_docker_links:
        ```

    ??? variable string "`diun_role_docker_network_mode`"

        ```yaml
        # Type: string
        diun_role_docker_network_mode:
        ```

    ??? variable string "`diun_role_docker_pid_mode`"

        ```yaml
        # Type: string
        diun_role_docker_pid_mode:
        ```

    ??? variable list "`diun_role_docker_ports`"

        ```yaml
        # Type: list
        diun_role_docker_ports:
        ```

    ??? variable string "`diun_role_docker_uts`"

        ```yaml
        # Type: string
        diun_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`diun_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_keep_volumes:
        ```

    ??? variable list "`diun_role_docker_mounts`"

        ```yaml
        # Type: list
        diun_role_docker_mounts:
        ```

    ??? variable dict "`diun_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        diun_role_docker_storage_opts:
        ```

    ??? variable list "`diun_role_docker_tmpfs`"

        ```yaml
        # Type: list
        diun_role_docker_tmpfs:
        ```

    ??? variable string "`diun_role_docker_volume_driver`"

        ```yaml
        # Type: string
        diun_role_docker_volume_driver:
        ```

    ??? variable list "`diun_role_docker_volumes_from`"

        ```yaml
        # Type: list
        diun_role_docker_volumes_from:
        ```

    ??? variable bool "`diun_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_volumes_global:
        ```

    ??? variable string "`diun_role_docker_working_dir`"

        ```yaml
        # Type: string
        diun_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`diun_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_auto_remove:
        ```

    ??? variable bool "`diun_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_cleanup:
        ```

    ??? variable string "`diun_role_docker_force_kill`"

        ```yaml
        # Type: string
        diun_role_docker_force_kill:
        ```

    ??? variable dict "`diun_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        diun_role_docker_healthcheck:
        ```

    ??? variable int "`diun_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        diun_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`diun_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_init:
        ```

    ??? variable string "`diun_role_docker_kill_signal`"

        ```yaml
        # Type: string
        diun_role_docker_kill_signal:
        ```

    ??? variable string "`diun_role_docker_log_driver`"

        ```yaml
        # Type: string
        diun_role_docker_log_driver:
        ```

    ??? variable dict "`diun_role_docker_log_options`"

        ```yaml
        # Type: dict
        diun_role_docker_log_options:
        ```

    ??? variable bool "`diun_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_oom_killer:
        ```

    ??? variable int "`diun_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        diun_role_docker_oom_score_adj:
        ```

    ??? variable bool "`diun_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_output_logs:
        ```

    ??? variable bool "`diun_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_paused:
        ```

    ??? variable bool "`diun_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_recreate:
        ```

    ??? variable int "`diun_role_docker_restart_retries`"

        ```yaml
        # Type: int
        diun_role_docker_restart_retries:
        ```

    ??? variable string "`diun_role_docker_stop_signal`"

        ```yaml
        # Type: string
        diun_role_docker_stop_signal:
        ```

    ??? variable int "`diun_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        diun_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`diun_role_docker_capabilities`"

        ```yaml
        # Type: list
        diun_role_docker_capabilities:
        ```

    ??? variable string "`diun_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        diun_role_docker_cgroup_parent:
        ```

    ??? variable list "`diun_role_docker_commands`"

        ```yaml
        # Type: list
        diun_role_docker_commands:
        ```

    ??? variable int "`diun_role_docker_create_timeout`"

        ```yaml
        # Type: int
        diun_role_docker_create_timeout:
        ```

    ??? variable string "`diun_role_docker_entrypoint`"

        ```yaml
        # Type: string
        diun_role_docker_entrypoint:
        ```

    ??? variable string "`diun_role_docker_env_file`"

        ```yaml
        # Type: string
        diun_role_docker_env_file:
        ```

    ??? variable bool "`diun_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_labels_use_common:
        ```

    ??? variable bool "`diun_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_read_only:
        ```

    ??? variable string "`diun_role_docker_runtime`"

        ```yaml
        # Type: string
        diun_role_docker_runtime:
        ```

    ??? variable list "`diun_role_docker_sysctls`"

        ```yaml
        # Type: list
        diun_role_docker_sysctls:
        ```

    ??? variable list "`diun_role_docker_ulimits`"

        ```yaml
        # Type: list
        diun_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`diun_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        diun_role_autoheal_enabled: true
        ```

    ??? variable string "`diun_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        diun_role_depends_on: ""
        ```

    ??? variable string "`diun_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        diun_role_depends_on_delay: "0"
        ```

    ??? variable string "`diun_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        diun_role_depends_on_healthchecks:
        ```

    ??? variable bool "`diun_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        diun_role_diun_enabled: true
        ```

    ??? variable bool "`diun_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        diun_role_docker_controller: true
        ```

    ??? variable list "`diun_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        diun_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`diun_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_volumes_download:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

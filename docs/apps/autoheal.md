---
icon: material/docker
hide:
  - tags
tags:
  - autoheal
  - docker
  - monitoring
saltbox_automation:
  disabled: false
  sections:
    inventory: true
    overview: true
  inventory:
    show_sections: []
    hide_sections: []
    example_overrides: {}
  app_links:
    - name: Manual
      url: https://github.com/willfarrell/docker-autoheal#readme
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/willfarrell/autoheal/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Autoheal
    summary: |
      a Docker container designed to monitor and automatically restart unhealthy Docker containers.
    link: https://github.com/willfarrell/docker-autoheal
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Autoheal

## Overview

[Autoheal](https://github.com/willfarrell/docker-autoheal) is a Docker container designed to monitor and automatically restart unhealthy Docker containers.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/willfarrell/docker-autoheal#readme){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/willfarrell/autoheal/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install autoheal
```

## Usage

Autoheal works automatically by monitoring Docker containers with health checks. All Saltbox-deployed containers are configured with the appropriate `autoheal` label, so no additional configuration is required after installation.

You can view Autoheal's activity in the container logs:

```shell
docker logs autoheal
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        autoheal_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `autoheal_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `autoheal_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`autoheal_name`"

        ```yaml
        # Type: string
        autoheal_name: autoheal
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`autoheal_role_docker_container`"

        ```yaml
        # Type: string
        autoheal_role_docker_container: "{{ autoheal_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`autoheal_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_image_pull: true
        ```

    ??? variable string "`autoheal_role_docker_image_tag`"

        ```yaml
        # Type: string
        autoheal_role_docker_image_tag: "latest"
        ```

    ??? variable string "`autoheal_role_docker_image`"

        ```yaml
        # Type: string
        autoheal_role_docker_image: "willfarrell/autoheal:{{ autoheal_role_docker_image_tag }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`autoheal_role_docker_envs_default`"

        ```yaml
        # Type: dict
        autoheal_role_docker_envs_default:
          AUTOHEAL_CONTAINER_LABEL: "autoheal"
        ```

    ??? variable dict "`autoheal_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        autoheal_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`autoheal_role_docker_volumes_default`"

        ```yaml
        # Type: list
        autoheal_role_docker_volumes_default:
          - "/var/run/docker.sock:/var/run/docker.sock"
          - "/etc/localtime:/etc/localtime:ro"
        ```

    ??? variable list "`autoheal_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        autoheal_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`autoheal_role_docker_hostname`"

        ```yaml
        # Type: string
        autoheal_role_docker_hostname: "{{ autoheal_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`autoheal_role_docker_networks_alias`"

        ```yaml
        # Type: string
        autoheal_role_docker_networks_alias: "{{ autoheal_name }}"
        ```

    ??? variable list "`autoheal_role_docker_networks_default`"

        ```yaml
        # Type: list
        autoheal_role_docker_networks_default: []
        ```

    ??? variable list "`autoheal_role_docker_networks_custom`"

        ```yaml
        # Type: list
        autoheal_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`autoheal_role_docker_restart_policy`"

        ```yaml
        # Type: string
        autoheal_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`autoheal_role_docker_state`"

        ```yaml
        # Type: string
        autoheal_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`autoheal_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        autoheal_role_docker_blkio_weight:
        ```

    ??? variable int "`autoheal_role_docker_cpu_period`"

        ```yaml
        # Type: int
        autoheal_role_docker_cpu_period:
        ```

    ??? variable int "`autoheal_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        autoheal_role_docker_cpu_quota:
        ```

    ??? variable int "`autoheal_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        autoheal_role_docker_cpu_shares:
        ```

    ??? variable string "`autoheal_role_docker_cpus`"

        ```yaml
        # Type: string
        autoheal_role_docker_cpus:
        ```

    ??? variable string "`autoheal_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        autoheal_role_docker_cpuset_cpus:
        ```

    ??? variable string "`autoheal_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        autoheal_role_docker_cpuset_mems:
        ```

    ??? variable string "`autoheal_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        autoheal_role_docker_kernel_memory:
        ```

    ??? variable string "`autoheal_role_docker_memory`"

        ```yaml
        # Type: string
        autoheal_role_docker_memory:
        ```

    ??? variable string "`autoheal_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        autoheal_role_docker_memory_reservation:
        ```

    ??? variable string "`autoheal_role_docker_memory_swap`"

        ```yaml
        # Type: string
        autoheal_role_docker_memory_swap:
        ```

    ??? variable int "`autoheal_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        autoheal_role_docker_memory_swappiness:
        ```

    ??? variable string "`autoheal_role_docker_shm_size`"

        ```yaml
        # Type: string
        autoheal_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`autoheal_role_docker_cap_drop`"

        ```yaml
        # Type: list
        autoheal_role_docker_cap_drop:
        ```

    ??? variable string "`autoheal_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        autoheal_role_docker_cgroupns_mode:
        ```

    ??? variable list "`autoheal_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        autoheal_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`autoheal_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        autoheal_role_docker_device_read_bps:
        ```

    ??? variable list "`autoheal_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        autoheal_role_docker_device_read_iops:
        ```

    ??? variable list "`autoheal_role_docker_device_requests`"

        ```yaml
        # Type: list
        autoheal_role_docker_device_requests:
        ```

    ??? variable list "`autoheal_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        autoheal_role_docker_device_write_bps:
        ```

    ??? variable list "`autoheal_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        autoheal_role_docker_device_write_iops:
        ```

    ??? variable list "`autoheal_role_docker_devices`"

        ```yaml
        # Type: list
        autoheal_role_docker_devices:
        ```

    ??? variable string "`autoheal_role_docker_devices_default`"

        ```yaml
        # Type: string
        autoheal_role_docker_devices_default:
        ```

    ??? variable list "`autoheal_role_docker_groups`"

        ```yaml
        # Type: list
        autoheal_role_docker_groups:
        ```

    ??? variable bool "`autoheal_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_privileged:
        ```

    ??? variable list "`autoheal_role_docker_security_opts`"

        ```yaml
        # Type: list
        autoheal_role_docker_security_opts:
        ```

    ??? variable string "`autoheal_role_docker_user`"

        ```yaml
        # Type: string
        autoheal_role_docker_user:
        ```

    ??? variable string "`autoheal_role_docker_userns_mode`"

        ```yaml
        # Type: string
        autoheal_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`autoheal_role_docker_dns_opts`"

        ```yaml
        # Type: list
        autoheal_role_docker_dns_opts:
        ```

    ??? variable list "`autoheal_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        autoheal_role_docker_dns_search_domains:
        ```

    ??? variable list "`autoheal_role_docker_dns_servers`"

        ```yaml
        # Type: list
        autoheal_role_docker_dns_servers:
        ```

    ??? variable string "`autoheal_role_docker_domainname`"

        ```yaml
        # Type: string
        autoheal_role_docker_domainname:
        ```

    ??? variable list "`autoheal_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        autoheal_role_docker_exposed_ports:
        ```

    ??? variable dict "`autoheal_role_docker_hosts`"

        ```yaml
        # Type: dict
        autoheal_role_docker_hosts:
        ```

    ??? variable bool "`autoheal_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_hosts_use_common:
        ```

    ??? variable string "`autoheal_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        autoheal_role_docker_ipc_mode:
        ```

    ??? variable list "`autoheal_role_docker_links`"

        ```yaml
        # Type: list
        autoheal_role_docker_links:
        ```

    ??? variable string "`autoheal_role_docker_network_mode`"

        ```yaml
        # Type: string
        autoheal_role_docker_network_mode:
        ```

    ??? variable string "`autoheal_role_docker_pid_mode`"

        ```yaml
        # Type: string
        autoheal_role_docker_pid_mode:
        ```

    ??? variable list "`autoheal_role_docker_ports`"

        ```yaml
        # Type: list
        autoheal_role_docker_ports:
        ```

    ??? variable string "`autoheal_role_docker_uts`"

        ```yaml
        # Type: string
        autoheal_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`autoheal_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_keep_volumes:
        ```

    ??? variable list "`autoheal_role_docker_mounts`"

        ```yaml
        # Type: list
        autoheal_role_docker_mounts:
        ```

    ??? variable dict "`autoheal_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        autoheal_role_docker_storage_opts:
        ```

    ??? variable list "`autoheal_role_docker_tmpfs`"

        ```yaml
        # Type: list
        autoheal_role_docker_tmpfs:
        ```

    ??? variable string "`autoheal_role_docker_volume_driver`"

        ```yaml
        # Type: string
        autoheal_role_docker_volume_driver:
        ```

    ??? variable list "`autoheal_role_docker_volumes_from`"

        ```yaml
        # Type: list
        autoheal_role_docker_volumes_from:
        ```

    ??? variable bool "`autoheal_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_volumes_global:
        ```

    ??? variable string "`autoheal_role_docker_working_dir`"

        ```yaml
        # Type: string
        autoheal_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`autoheal_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_auto_remove:
        ```

    ??? variable bool "`autoheal_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_cleanup:
        ```

    ??? variable string "`autoheal_role_docker_force_kill`"

        ```yaml
        # Type: string
        autoheal_role_docker_force_kill:
        ```

    ??? variable dict "`autoheal_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        autoheal_role_docker_healthcheck:
        ```

    ??? variable int "`autoheal_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        autoheal_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`autoheal_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_init:
        ```

    ??? variable string "`autoheal_role_docker_kill_signal`"

        ```yaml
        # Type: string
        autoheal_role_docker_kill_signal:
        ```

    ??? variable string "`autoheal_role_docker_log_driver`"

        ```yaml
        # Type: string
        autoheal_role_docker_log_driver:
        ```

    ??? variable dict "`autoheal_role_docker_log_options`"

        ```yaml
        # Type: dict
        autoheal_role_docker_log_options:
        ```

    ??? variable bool "`autoheal_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_oom_killer:
        ```

    ??? variable int "`autoheal_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        autoheal_role_docker_oom_score_adj:
        ```

    ??? variable bool "`autoheal_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_output_logs:
        ```

    ??? variable bool "`autoheal_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_paused:
        ```

    ??? variable bool "`autoheal_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_recreate:
        ```

    ??? variable int "`autoheal_role_docker_restart_retries`"

        ```yaml
        # Type: int
        autoheal_role_docker_restart_retries:
        ```

    ??? variable int "`autoheal_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        autoheal_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`autoheal_role_docker_capabilities`"

        ```yaml
        # Type: list
        autoheal_role_docker_capabilities:
        ```

    ??? variable string "`autoheal_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        autoheal_role_docker_cgroup_parent:
        ```

    ??? variable list "`autoheal_role_docker_commands`"

        ```yaml
        # Type: list
        autoheal_role_docker_commands:
        ```

    ??? variable int "`autoheal_role_docker_create_timeout`"

        ```yaml
        # Type: int
        autoheal_role_docker_create_timeout:
        ```

    ??? variable string "`autoheal_role_docker_entrypoint`"

        ```yaml
        # Type: string
        autoheal_role_docker_entrypoint:
        ```

    ??? variable string "`autoheal_role_docker_env_file`"

        ```yaml
        # Type: string
        autoheal_role_docker_env_file:
        ```

    ??? variable dict "`autoheal_role_docker_labels`"

        ```yaml
        # Type: dict
        autoheal_role_docker_labels:
        ```

    ??? variable bool "`autoheal_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_labels_use_common:
        ```

    ??? variable bool "`autoheal_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_read_only:
        ```

    ??? variable string "`autoheal_role_docker_runtime`"

        ```yaml
        # Type: string
        autoheal_role_docker_runtime:
        ```

    ??? variable list "`autoheal_role_docker_sysctls`"

        ```yaml
        # Type: list
        autoheal_role_docker_sysctls:
        ```

    ??? variable list "`autoheal_role_docker_ulimits`"

        ```yaml
        # Type: list
        autoheal_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`autoheal_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        autoheal_role_autoheal_enabled: true
        ```

    ??? variable string "`autoheal_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        autoheal_role_depends_on: ""
        ```

    ??? variable string "`autoheal_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        autoheal_role_depends_on_delay: "0"
        ```

    ??? variable string "`autoheal_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        autoheal_role_depends_on_healthchecks:
        ```

    ??? variable bool "`autoheal_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        autoheal_role_diun_enabled: true
        ```

    ??? variable bool "`autoheal_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        autoheal_role_docker_controller: true
        ```

    ??? variable bool "`autoheal_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_volumes_download:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
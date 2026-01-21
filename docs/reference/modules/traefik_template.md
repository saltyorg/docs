---
icon: material/play
title: Traefik Template
status: draft
saltbox_automation:
  inventory:
    hide_sections:
      - Template Variables
  project_description:
    name: Traefik Template
    summary: |-
      a Saltbox module that generates a Docker Compose template with Traefik configuration.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Traefik Template

## Overview

Traefik Template is a Saltbox module that generates a Docker Compose template with Traefik configuration.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install generate-traefik-template
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        traefik_template_file: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `traefik_template_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `traefik_template_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Settings"

    ??? variable string "`traefik_template_file`"

        ```yaml
        # Type: string
        traefik_template_file: "/tmp/docker-compose.yml"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`traefik_template_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        traefik_template_role_docker_blkio_weight:
        ```

    ??? variable int "`traefik_template_role_docker_cpu_period`"

        ```yaml
        # Type: int
        traefik_template_role_docker_cpu_period:
        ```

    ??? variable int "`traefik_template_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        traefik_template_role_docker_cpu_quota:
        ```

    ??? variable int "`traefik_template_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        traefik_template_role_docker_cpu_shares:
        ```

    ??? variable string "`traefik_template_role_docker_cpus`"

        ```yaml
        # Type: string
        traefik_template_role_docker_cpus:
        ```

    ??? variable string "`traefik_template_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        traefik_template_role_docker_cpuset_cpus:
        ```

    ??? variable string "`traefik_template_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        traefik_template_role_docker_cpuset_mems:
        ```

    ??? variable string "`traefik_template_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        traefik_template_role_docker_kernel_memory:
        ```

    ??? variable string "`traefik_template_role_docker_memory`"

        ```yaml
        # Type: string
        traefik_template_role_docker_memory:
        ```

    ??? variable string "`traefik_template_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        traefik_template_role_docker_memory_reservation:
        ```

    ??? variable string "`traefik_template_role_docker_memory_swap`"

        ```yaml
        # Type: string
        traefik_template_role_docker_memory_swap:
        ```

    ??? variable int "`traefik_template_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        traefik_template_role_docker_memory_swappiness:
        ```

    ??? variable string "`traefik_template_role_docker_shm_size`"

        ```yaml
        # Type: string
        traefik_template_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`traefik_template_role_docker_cap_drop`"

        ```yaml
        # Type: list
        traefik_template_role_docker_cap_drop:
        ```

    ??? variable string "`traefik_template_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        traefik_template_role_docker_cgroupns_mode:
        ```

    ??? variable list "`traefik_template_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        traefik_template_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`traefik_template_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        traefik_template_role_docker_device_read_bps:
        ```

    ??? variable list "`traefik_template_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        traefik_template_role_docker_device_read_iops:
        ```

    ??? variable list "`traefik_template_role_docker_device_requests`"

        ```yaml
        # Type: list
        traefik_template_role_docker_device_requests:
        ```

    ??? variable list "`traefik_template_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        traefik_template_role_docker_device_write_bps:
        ```

    ??? variable list "`traefik_template_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        traefik_template_role_docker_device_write_iops:
        ```

    ??? variable list "`traefik_template_role_docker_devices`"

        ```yaml
        # Type: list
        traefik_template_role_docker_devices:
        ```

    ??? variable string "`traefik_template_role_docker_devices_default`"

        ```yaml
        # Type: string
        traefik_template_role_docker_devices_default:
        ```

    ??? variable list "`traefik_template_role_docker_groups`"

        ```yaml
        # Type: list
        traefik_template_role_docker_groups:
        ```

    ??? variable bool "`traefik_template_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        traefik_template_role_docker_privileged:
        ```

    ??? variable list "`traefik_template_role_docker_security_opts`"

        ```yaml
        # Type: list
        traefik_template_role_docker_security_opts:
        ```

    ??? variable string "`traefik_template_role_docker_user`"

        ```yaml
        # Type: string
        traefik_template_role_docker_user:
        ```

    ??? variable string "`traefik_template_role_docker_userns_mode`"

        ```yaml
        # Type: string
        traefik_template_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`traefik_template_role_docker_dns_opts`"

        ```yaml
        # Type: list
        traefik_template_role_docker_dns_opts:
        ```

    ??? variable list "`traefik_template_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        traefik_template_role_docker_dns_search_domains:
        ```

    ??? variable list "`traefik_template_role_docker_dns_servers`"

        ```yaml
        # Type: list
        traefik_template_role_docker_dns_servers:
        ```

    ??? variable string "`traefik_template_role_docker_domainname`"

        ```yaml
        # Type: string
        traefik_template_role_docker_domainname:
        ```

    ??? variable list "`traefik_template_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        traefik_template_role_docker_exposed_ports:
        ```

    ??? variable string "`traefik_template_role_docker_hostname`"

        ```yaml
        # Type: string
        traefik_template_role_docker_hostname:
        ```

    ??? variable dict "`traefik_template_role_docker_hosts`"

        ```yaml
        # Type: dict
        traefik_template_role_docker_hosts:
        ```

    ??? variable bool "`traefik_template_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        traefik_template_role_docker_hosts_use_common:
        ```

    ??? variable string "`traefik_template_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        traefik_template_role_docker_ipc_mode:
        ```

    ??? variable list "`traefik_template_role_docker_links`"

        ```yaml
        # Type: list
        traefik_template_role_docker_links:
        ```

    ??? variable list "`traefik_template_role_docker_networks`"

        ```yaml
        # Type: list
        traefik_template_role_docker_networks:
        ```

    ??? variable string "`traefik_template_role_docker_pid_mode`"

        ```yaml
        # Type: string
        traefik_template_role_docker_pid_mode:
        ```

    ??? variable list "`traefik_template_role_docker_ports`"

        ```yaml
        # Type: list
        traefik_template_role_docker_ports:
        ```

    ??? variable string "`traefik_template_role_docker_uts`"

        ```yaml
        # Type: string
        traefik_template_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`traefik_template_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        traefik_template_role_docker_keep_volumes:
        ```

    ??? variable list "`traefik_template_role_docker_mounts`"

        ```yaml
        # Type: list
        traefik_template_role_docker_mounts:
        ```

    ??? variable dict "`traefik_template_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        traefik_template_role_docker_storage_opts:
        ```

    ??? variable list "`traefik_template_role_docker_tmpfs`"

        ```yaml
        # Type: list
        traefik_template_role_docker_tmpfs:
        ```

    ??? variable string "`traefik_template_role_docker_volume_driver`"

        ```yaml
        # Type: string
        traefik_template_role_docker_volume_driver:
        ```

    ??? variable list "`traefik_template_role_docker_volumes`"

        ```yaml
        # Type: list
        traefik_template_role_docker_volumes:
        ```

    ??? variable list "`traefik_template_role_docker_volumes_from`"

        ```yaml
        # Type: list
        traefik_template_role_docker_volumes_from:
        ```

    ??? variable bool "`traefik_template_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        traefik_template_role_docker_volumes_global:
        ```

    ??? variable string "`traefik_template_role_docker_working_dir`"

        ```yaml
        # Type: string
        traefik_template_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`traefik_template_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        traefik_template_role_docker_auto_remove:
        ```

    ??? variable bool "`traefik_template_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        traefik_template_role_docker_cleanup:
        ```

    ??? variable string "`traefik_template_role_docker_force_kill`"

        ```yaml
        # Type: string
        traefik_template_role_docker_force_kill:
        ```

    ??? variable dict "`traefik_template_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        traefik_template_role_docker_healthcheck:
        ```

    ??? variable int "`traefik_template_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        traefik_template_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`traefik_template_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        traefik_template_role_docker_init:
        ```

    ??? variable string "`traefik_template_role_docker_kill_signal`"

        ```yaml
        # Type: string
        traefik_template_role_docker_kill_signal:
        ```

    ??? variable string "`traefik_template_role_docker_log_driver`"

        ```yaml
        # Type: string
        traefik_template_role_docker_log_driver:
        ```

    ??? variable dict "`traefik_template_role_docker_log_options`"

        ```yaml
        # Type: dict
        traefik_template_role_docker_log_options:
        ```

    ??? variable bool "`traefik_template_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        traefik_template_role_docker_oom_killer:
        ```

    ??? variable int "`traefik_template_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        traefik_template_role_docker_oom_score_adj:
        ```

    ??? variable bool "`traefik_template_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        traefik_template_role_docker_output_logs:
        ```

    ??? variable bool "`traefik_template_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        traefik_template_role_docker_paused:
        ```

    ??? variable bool "`traefik_template_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        traefik_template_role_docker_recreate:
        ```

    ??? variable string "`traefik_template_role_docker_restart_policy`"

        ```yaml
        # Type: string
        traefik_template_role_docker_restart_policy:
        ```

    ??? variable int "`traefik_template_role_docker_restart_retries`"

        ```yaml
        # Type: int
        traefik_template_role_docker_restart_retries:
        ```

    ??? variable int "`traefik_template_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        traefik_template_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`traefik_template_role_docker_capabilities`"

        ```yaml
        # Type: list
        traefik_template_role_docker_capabilities:
        ```

    ??? variable string "`traefik_template_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        traefik_template_role_docker_cgroup_parent:
        ```

    ??? variable list "`traefik_template_role_docker_commands`"

        ```yaml
        # Type: list
        traefik_template_role_docker_commands:
        ```

    ??? variable string "`traefik_template_role_docker_container`"

        ```yaml
        # Type: string
        traefik_template_role_docker_container:
        ```

    ??? variable int "`traefik_template_role_docker_create_timeout`"

        ```yaml
        # Type: int
        traefik_template_role_docker_create_timeout:
        ```

    ??? variable string "`traefik_template_role_docker_entrypoint`"

        ```yaml
        # Type: string
        traefik_template_role_docker_entrypoint:
        ```

    ??? variable string "`traefik_template_role_docker_env_file`"

        ```yaml
        # Type: string
        traefik_template_role_docker_env_file:
        ```

    ??? variable dict "`traefik_template_role_docker_envs`"

        ```yaml
        # Type: dict
        traefik_template_role_docker_envs:
        ```

    ??? variable string "`traefik_template_role_docker_image`"

        ```yaml
        # Type: string
        traefik_template_role_docker_image:
        ```

    ??? variable bool "`traefik_template_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        traefik_template_role_docker_image_pull:
        ```

    ??? variable dict "`traefik_template_role_docker_labels`"

        ```yaml
        # Type: dict
        traefik_template_role_docker_labels:
        ```

    ??? variable bool "`traefik_template_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        traefik_template_role_docker_labels_use_common:
        ```

    ??? variable bool "`traefik_template_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        traefik_template_role_docker_read_only:
        ```

    ??? variable string "`traefik_template_role_docker_runtime`"

        ```yaml
        # Type: string
        traefik_template_role_docker_runtime:
        ```

    ??? variable list "`traefik_template_role_docker_sysctls`"

        ```yaml
        # Type: list
        traefik_template_role_docker_sysctls:
        ```

    ??? variable list "`traefik_template_role_docker_ulimits`"

        ```yaml
        # Type: list
        traefik_template_role_docker_ulimits:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

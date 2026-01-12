---
icon: material/server-network-outline
title: Docker CE
status: draft
saltbox_automation:
  inventory:
    show_sections:
      - Settings
  app_links:
    - name: Manual
      url: https://docs.docker.com
      type: documentation
    - name: Releases
      url: https://docs.docker.com/engine/release-notes
      type: releases
    - name: Community
      url: https://forums.docker.com
      type: community
  project_description:
    name: Docker CE
    summary: |
      an open-source containerization technology for building and containerizing your applications.
    link: https://www.docker.com/community
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Docker CE

## Overview

[Docker CE](https://www.docker.com/community) is an open-source containerization technology for building and containerizing your applications.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://docs.docker.com){ .md-button .md-button--stretch }

[:fontawesome-solid-newspaper:**Releases**](https://docs.docker.com/engine/release-notes){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](https://forums.docker.com){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

Saltbox dependency.

```shell
sb install docker
```

## Usage

```shell
docker
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        docker_dns: ["item1", "item2"]
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `docker_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `docker_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Settings"

    ??? variable list "`docker_dns`"

        ```yaml
        # Format is ["8.8.8.8", "8.8.4.4"]
        # Type: list
        docker_dns: []
        ```

    ??? variable dict "`docker_config_custom`"

        ```yaml
        # YAML Dictionary that gets combined with the defaults and later converted to json
        # Example of how to remove an option:
        # docker_config_custom:
        # log-opts: "{{ omit }}"
        # Example of how to add options:
        # docker_config_custom:
        # debug: "true"
        # Type: dict
        docker_config_custom: {}
        ```

    ??? variable string "`docker_cpus_default`"

        ```yaml
        # CPU and Memory defaults
        # Type: string
        docker_cpus_default: ""
        ```

    ??? variable string "`docker_memory_default`"

        ```yaml
        # Type: string
        docker_memory_default: ""
        ```

    ??? variable string "`docker_skip_start_during_meta_tag`"

        ```yaml
        # Skip Container startup during core, saltbox, mediabox or feederbox
        # If the kernel has been updated and a reboot will happen
        # Type: string
        docker_skip_start_during_meta_tag: "{{ saltbox_auto_reboot }}"
        ```

    ??? variable bool "`docker_create_image_prune`"

        ```yaml
        # Toggles pruning of dangling images after container creation.
        # Type: bool (true/false)
        docker_create_image_prune: true
        ```

    ??? variable bool "`docker_create_image_prune_delay`"

        ```yaml
        # Type: bool (true/false)
        docker_create_image_prune_delay: true
        ```

    ??? variable int "`docker_create_image_prune_delay_timeout`"

        ```yaml
        # Type: int
        docker_create_image_prune_delay_timeout: 10
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`docker_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        docker_role_docker_blkio_weight:
        ```

    ??? variable int "`docker_role_docker_cpu_period`"

        ```yaml
        # Type: int
        docker_role_docker_cpu_period:
        ```

    ??? variable int "`docker_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        docker_role_docker_cpu_quota:
        ```

    ??? variable int "`docker_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        docker_role_docker_cpu_shares:
        ```

    ??? variable string "`docker_role_docker_cpus`"

        ```yaml
        # Type: string
        docker_role_docker_cpus:
        ```

    ??? variable string "`docker_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        docker_role_docker_cpuset_cpus:
        ```

    ??? variable string "`docker_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        docker_role_docker_cpuset_mems:
        ```

    ??? variable string "`docker_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        docker_role_docker_kernel_memory:
        ```

    ??? variable string "`docker_role_docker_memory`"

        ```yaml
        # Type: string
        docker_role_docker_memory:
        ```

    ??? variable string "`docker_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        docker_role_docker_memory_reservation:
        ```

    ??? variable string "`docker_role_docker_memory_swap`"

        ```yaml
        # Type: string
        docker_role_docker_memory_swap:
        ```

    ??? variable int "`docker_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        docker_role_docker_memory_swappiness:
        ```

    ??? variable string "`docker_role_docker_shm_size`"

        ```yaml
        # Type: string
        docker_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`docker_role_docker_cap_drop`"

        ```yaml
        # Type: list
        docker_role_docker_cap_drop:
        ```

    ??? variable string "`docker_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        docker_role_docker_cgroupns_mode:
        ```

    ??? variable list "`docker_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        docker_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`docker_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        docker_role_docker_device_read_bps:
        ```

    ??? variable list "`docker_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        docker_role_docker_device_read_iops:
        ```

    ??? variable list "`docker_role_docker_device_requests`"

        ```yaml
        # Type: list
        docker_role_docker_device_requests:
        ```

    ??? variable list "`docker_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        docker_role_docker_device_write_bps:
        ```

    ??? variable list "`docker_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        docker_role_docker_device_write_iops:
        ```

    ??? variable list "`docker_role_docker_devices`"

        ```yaml
        # Type: list
        docker_role_docker_devices:
        ```

    ??? variable string "`docker_role_docker_devices_default`"

        ```yaml
        # Type: string
        docker_role_docker_devices_default:
        ```

    ??? variable list "`docker_role_docker_groups`"

        ```yaml
        # Type: list
        docker_role_docker_groups:
        ```

    ??? variable bool "`docker_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_privileged:
        ```

    ??? variable list "`docker_role_docker_security_opts`"

        ```yaml
        # Type: list
        docker_role_docker_security_opts:
        ```

    ??? variable string "`docker_role_docker_user`"

        ```yaml
        # Type: string
        docker_role_docker_user:
        ```

    ??? variable string "`docker_role_docker_userns_mode`"

        ```yaml
        # Type: string
        docker_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`docker_role_docker_dns_opts`"

        ```yaml
        # Type: list
        docker_role_docker_dns_opts:
        ```

    ??? variable list "`docker_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        docker_role_docker_dns_search_domains:
        ```

    ??? variable list "`docker_role_docker_dns_servers`"

        ```yaml
        # Type: list
        docker_role_docker_dns_servers:
        ```

    ??? variable string "`docker_role_docker_domainname`"

        ```yaml
        # Type: string
        docker_role_docker_domainname:
        ```

    ??? variable list "`docker_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        docker_role_docker_exposed_ports:
        ```

    ??? variable string "`docker_role_docker_hostname`"

        ```yaml
        # Type: string
        docker_role_docker_hostname:
        ```

    ??? variable dict "`docker_role_docker_hosts`"

        ```yaml
        # Type: dict
        docker_role_docker_hosts:
        ```

    ??? variable bool "`docker_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_hosts_use_common:
        ```

    ??? variable string "`docker_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        docker_role_docker_ipc_mode:
        ```

    ??? variable list "`docker_role_docker_links`"

        ```yaml
        # Type: list
        docker_role_docker_links:
        ```

    ??? variable string "`docker_role_docker_network_mode`"

        ```yaml
        # Type: string
        docker_role_docker_network_mode:
        ```

    ??? variable list "`docker_role_docker_networks`"

        ```yaml
        # Type: list
        docker_role_docker_networks:
        ```

    ??? variable string "`docker_role_docker_pid_mode`"

        ```yaml
        # Type: string
        docker_role_docker_pid_mode:
        ```

    ??? variable list "`docker_role_docker_ports`"

        ```yaml
        # Type: list
        docker_role_docker_ports:
        ```

    ??? variable string "`docker_role_docker_uts`"

        ```yaml
        # Type: string
        docker_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`docker_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_keep_volumes:
        ```

    ??? variable list "`docker_role_docker_mounts`"

        ```yaml
        # Type: list
        docker_role_docker_mounts:
        ```

    ??? variable dict "`docker_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        docker_role_docker_storage_opts:
        ```

    ??? variable list "`docker_role_docker_tmpfs`"

        ```yaml
        # Type: list
        docker_role_docker_tmpfs:
        ```

    ??? variable string "`docker_role_docker_volume_driver`"

        ```yaml
        # Type: string
        docker_role_docker_volume_driver:
        ```

    ??? variable list "`docker_role_docker_volumes`"

        ```yaml
        # Type: list
        docker_role_docker_volumes:
        ```

    ??? variable list "`docker_role_docker_volumes_from`"

        ```yaml
        # Type: list
        docker_role_docker_volumes_from:
        ```

    ??? variable bool "`docker_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_volumes_global:
        ```

    ??? variable string "`docker_role_docker_working_dir`"

        ```yaml
        # Type: string
        docker_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`docker_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_auto_remove:
        ```

    ??? variable bool "`docker_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_cleanup:
        ```

    ??? variable string "`docker_role_docker_force_kill`"

        ```yaml
        # Type: string
        docker_role_docker_force_kill:
        ```

    ??? variable dict "`docker_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        docker_role_docker_healthcheck:
        ```

    ??? variable int "`docker_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        docker_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`docker_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_init:
        ```

    ??? variable string "`docker_role_docker_kill_signal`"

        ```yaml
        # Type: string
        docker_role_docker_kill_signal:
        ```

    ??? variable string "`docker_role_docker_log_driver`"

        ```yaml
        # Type: string
        docker_role_docker_log_driver:
        ```

    ??? variable dict "`docker_role_docker_log_options`"

        ```yaml
        # Type: dict
        docker_role_docker_log_options:
        ```

    ??? variable bool "`docker_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_oom_killer:
        ```

    ??? variable int "`docker_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        docker_role_docker_oom_score_adj:
        ```

    ??? variable bool "`docker_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_output_logs:
        ```

    ??? variable bool "`docker_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_paused:
        ```

    ??? variable bool "`docker_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_recreate:
        ```

    ??? variable string "`docker_role_docker_restart_policy`"

        ```yaml
        # Type: string
        docker_role_docker_restart_policy:
        ```

    ??? variable int "`docker_role_docker_restart_retries`"

        ```yaml
        # Type: int
        docker_role_docker_restart_retries:
        ```

    ??? variable int "`docker_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        docker_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`docker_role_docker_capabilities`"

        ```yaml
        # Type: list
        docker_role_docker_capabilities:
        ```

    ??? variable string "`docker_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        docker_role_docker_cgroup_parent:
        ```

    ??? variable list "`docker_role_docker_commands`"

        ```yaml
        # Type: list
        docker_role_docker_commands:
        ```

    ??? variable string "`docker_role_docker_container`"

        ```yaml
        # Type: string
        docker_role_docker_container:
        ```

    ??? variable int "`docker_role_docker_create_timeout`"

        ```yaml
        # Type: int
        docker_role_docker_create_timeout:
        ```

    ??? variable string "`docker_role_docker_entrypoint`"

        ```yaml
        # Type: string
        docker_role_docker_entrypoint:
        ```

    ??? variable string "`docker_role_docker_env_file`"

        ```yaml
        # Type: string
        docker_role_docker_env_file:
        ```

    ??? variable dict "`docker_role_docker_envs`"

        ```yaml
        # Type: dict
        docker_role_docker_envs:
        ```

    ??? variable string "`docker_role_docker_image`"

        ```yaml
        # Type: string
        docker_role_docker_image:
        ```

    ??? variable bool "`docker_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_image_pull:
        ```

    ??? variable dict "`docker_role_docker_labels`"

        ```yaml
        # Type: dict
        docker_role_docker_labels:
        ```

    ??? variable bool "`docker_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_labels_use_common:
        ```

    ??? variable bool "`docker_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        docker_role_docker_read_only:
        ```

    ??? variable string "`docker_role_docker_runtime`"

        ```yaml
        # Type: string
        docker_role_docker_runtime:
        ```

    ??? variable list "`docker_role_docker_sysctls`"

        ```yaml
        # Type: list
        docker_role_docker_sysctls:
        ```

    ??? variable list "`docker_role_docker_ulimits`"

        ```yaml
        # Type: list
        docker_role_docker_ulimits:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
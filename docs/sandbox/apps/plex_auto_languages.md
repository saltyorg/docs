---
icon: material/docker
title: Plex Auto Languages
hide:
  - tags
tags:
  - plex-auto-languages
  - plex
  - automation
saltbox_automation:
  app_links:
    - name: Manual
      url: https://github.com/RemiRigal/Plex-Auto-Languages
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/remirigal/plex-auto-languages/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Plex Auto Languages
    summary: |-
      a tool designed to automate the selection of audio and subtitle languages for TV shows in Plex Media Server.
    link: https://github.com/RemiRigal/Plex-Auto-Languages
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Plex Auto Languages

## Overview

[Plex Auto Languages](https://github.com/RemiRigal/Plex-Auto-Languages) is a tool designed to automate the selection of audio and subtitle languages for TV shows in Plex Media Server.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/RemiRigal/Plex-Auto-Languages){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/remirigal/plex-auto-languages/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-plex-auto-languages
```

## Usage

PLex-auto-languages has no UI; it is driven by a config file

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        plex_auto_languages_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `plex_auto_languages_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `plex_auto_languages_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`plex_auto_languages_name`"

        ```yaml
        # Type: string
        plex_auto_languages_name: plex-auto-languages
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`plex_auto_languages_role_docker_container`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_container: "{{ plex_auto_languages_name }}"
        ```

    <h5>Image</h5>

    ??? variable string "`plex_auto_languages_role_docker_image_tag`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_image_tag: "latest"
        ```

    ??? variable string "`plex_auto_languages_role_docker_image_repo`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_image_repo: "journeyover/plex-auto-languages"
        ```

    ??? variable string "`plex_auto_languages_role_docker_image`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='plex_auto_languages') }}:{{ lookup('role_var', '_docker_image_tag', role='plex_auto_languages') }}"
        ```

    ??? variable bool "`plex_auto_languages_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        plex_auto_languages_role_docker_image_pull: true
        ```

    <h5>Envs</h5>

    ??? variable dict "`plex_auto_languages_role_docker_envs_default`"

        ```yaml
        # Type: dict
        plex_auto_languages_role_docker_envs_default:
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`plex_auto_languages_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        plex_auto_languages_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`plex_auto_languages_role_docker_volumes_default`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='plex_auto_languages') }}:/config"
        ```

    ??? variable list "`plex_auto_languages_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`plex_auto_languages_role_docker_hostname`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_hostname: "{{ plex_auto_languages_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`plex_auto_languages_role_docker_networks_alias`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_networks_alias: "{{ plex_auto_languages_name }}"
        ```

    ??? variable list "`plex_auto_languages_role_docker_networks_default`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_networks_default: []
        ```

    ??? variable list "`plex_auto_languages_role_docker_networks_custom`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`plex_auto_languages_role_docker_restart_policy`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`plex_auto_languages_role_docker_state`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_state: started
        ```

    <h5>Stop Timeout</h5>

    ??? variable int "`plex_auto_languages_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        plex_auto_languages_role_docker_stop_timeout: 10
        ```

    <h5>User</h5>

    ??? variable string "`plex_auto_languages_role_docker_user`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`plex_auto_languages_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        plex_auto_languages_role_docker_blkio_weight:
        ```

    ??? variable int "`plex_auto_languages_role_docker_cpu_period`"

        ```yaml
        # Type: int
        plex_auto_languages_role_docker_cpu_period:
        ```

    ??? variable int "`plex_auto_languages_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        plex_auto_languages_role_docker_cpu_quota:
        ```

    ??? variable int "`plex_auto_languages_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        plex_auto_languages_role_docker_cpu_shares:
        ```

    ??? variable string "`plex_auto_languages_role_docker_cpus`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_cpus:
        ```

    ??? variable string "`plex_auto_languages_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_cpuset_cpus:
        ```

    ??? variable string "`plex_auto_languages_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_cpuset_mems:
        ```

    ??? variable string "`plex_auto_languages_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_kernel_memory:
        ```

    ??? variable string "`plex_auto_languages_role_docker_memory`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_memory:
        ```

    ??? variable string "`plex_auto_languages_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_memory_reservation:
        ```

    ??? variable string "`plex_auto_languages_role_docker_memory_swap`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_memory_swap:
        ```

    ??? variable int "`plex_auto_languages_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        plex_auto_languages_role_docker_memory_swappiness:
        ```

    ??? variable string "`plex_auto_languages_role_docker_shm_size`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`plex_auto_languages_role_docker_cap_drop`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_cap_drop:
        ```

    ??? variable string "`plex_auto_languages_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_cgroupns_mode:
        ```

    ??? variable list "`plex_auto_languages_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`plex_auto_languages_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_device_read_bps:
        ```

    ??? variable list "`plex_auto_languages_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_device_read_iops:
        ```

    ??? variable list "`plex_auto_languages_role_docker_device_requests`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_device_requests:
        ```

    ??? variable list "`plex_auto_languages_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_device_write_bps:
        ```

    ??? variable list "`plex_auto_languages_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_device_write_iops:
        ```

    ??? variable list "`plex_auto_languages_role_docker_devices`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_devices:
        ```

    ??? variable list "`plex_auto_languages_role_docker_groups`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_groups:
        ```

    ??? variable bool "`plex_auto_languages_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        plex_auto_languages_role_docker_privileged:
        ```

    ??? variable list "`plex_auto_languages_role_docker_security_opts`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_security_opts:
        ```

    ??? variable string "`plex_auto_languages_role_docker_userns_mode`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`plex_auto_languages_role_docker_dns_opts`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_dns_opts:
        ```

    ??? variable list "`plex_auto_languages_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_dns_search_domains:
        ```

    ??? variable list "`plex_auto_languages_role_docker_dns_servers`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_dns_servers:
        ```

    ??? variable string "`plex_auto_languages_role_docker_domainname`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_domainname:
        ```

    ??? variable list "`plex_auto_languages_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_exposed_ports:
        ```

    ??? variable dict "`plex_auto_languages_role_docker_hosts`"

        ```yaml
        # Type: dict
        plex_auto_languages_role_docker_hosts:
        ```

    ??? variable bool "`plex_auto_languages_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        plex_auto_languages_role_docker_hosts_use_common:
        ```

    ??? variable string "`plex_auto_languages_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_ipc_mode:
        ```

    ??? variable list "`plex_auto_languages_role_docker_links`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_links:
        ```

    ??? variable string "`plex_auto_languages_role_docker_network_mode`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_network_mode:
        ```

    ??? variable string "`plex_auto_languages_role_docker_pid_mode`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_pid_mode:
        ```

    ??? variable list "`plex_auto_languages_role_docker_ports`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_ports:
        ```

    ??? variable string "`plex_auto_languages_role_docker_uts`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`plex_auto_languages_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        plex_auto_languages_role_docker_keep_volumes:
        ```

    ??? variable list "`plex_auto_languages_role_docker_mounts`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_mounts:
        ```

    ??? variable dict "`plex_auto_languages_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        plex_auto_languages_role_docker_storage_opts:
        ```

    ??? variable list "`plex_auto_languages_role_docker_tmpfs`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_tmpfs:
        ```

    ??? variable string "`plex_auto_languages_role_docker_volume_driver`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_volume_driver:
        ```

    ??? variable list "`plex_auto_languages_role_docker_volumes_from`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_volumes_from:
        ```

    ??? variable bool "`plex_auto_languages_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        plex_auto_languages_role_docker_volumes_global:
        ```

    ??? variable string "`plex_auto_languages_role_docker_working_dir`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`plex_auto_languages_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        plex_auto_languages_role_docker_auto_remove:
        ```

    ??? variable bool "`plex_auto_languages_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        plex_auto_languages_role_docker_cleanup:
        ```

    ??? variable string "`plex_auto_languages_role_docker_force_kill`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_force_kill:
        ```

    ??? variable dict "`plex_auto_languages_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        plex_auto_languages_role_docker_healthcheck:
        ```

    ??? variable int "`plex_auto_languages_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        plex_auto_languages_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`plex_auto_languages_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        plex_auto_languages_role_docker_init:
        ```

    ??? variable string "`plex_auto_languages_role_docker_kill_signal`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_kill_signal:
        ```

    ??? variable string "`plex_auto_languages_role_docker_log_driver`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_log_driver:
        ```

    ??? variable dict "`plex_auto_languages_role_docker_log_options`"

        ```yaml
        # Type: dict
        plex_auto_languages_role_docker_log_options:
        ```

    ??? variable bool "`plex_auto_languages_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        plex_auto_languages_role_docker_oom_killer:
        ```

    ??? variable int "`plex_auto_languages_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        plex_auto_languages_role_docker_oom_score_adj:
        ```

    ??? variable bool "`plex_auto_languages_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        plex_auto_languages_role_docker_output_logs:
        ```

    ??? variable bool "`plex_auto_languages_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        plex_auto_languages_role_docker_paused:
        ```

    ??? variable bool "`plex_auto_languages_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        plex_auto_languages_role_docker_recreate:
        ```

    ??? variable int "`plex_auto_languages_role_docker_restart_retries`"

        ```yaml
        # Type: int
        plex_auto_languages_role_docker_restart_retries:
        ```

    ??? variable string "`plex_auto_languages_role_docker_stop_signal`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_stop_signal:
        ```

    <h5>Other Options</h5>

    ??? variable list "`plex_auto_languages_role_docker_capabilities`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_capabilities:
        ```

    ??? variable string "`plex_auto_languages_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_cgroup_parent:
        ```

    ??? variable list "`plex_auto_languages_role_docker_commands`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_commands:
        ```

    ??? variable int "`plex_auto_languages_role_docker_create_timeout`"

        ```yaml
        # Type: int
        plex_auto_languages_role_docker_create_timeout:
        ```

    ??? variable string "`plex_auto_languages_role_docker_dev_dri`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_dev_dri:
        ```

    ??? variable string "`plex_auto_languages_role_docker_entrypoint`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_entrypoint:
        ```

    ??? variable string "`plex_auto_languages_role_docker_env_file`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_env_file:
        ```

    ??? variable dict "`plex_auto_languages_role_docker_labels`"

        ```yaml
        # Type: dict
        plex_auto_languages_role_docker_labels:
        ```

    ??? variable bool "`plex_auto_languages_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        plex_auto_languages_role_docker_labels_use_common:
        ```

    ??? variable bool "`plex_auto_languages_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        plex_auto_languages_role_docker_read_only:
        ```

    ??? variable string "`plex_auto_languages_role_docker_runtime`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_runtime:
        ```

    ??? variable list "`plex_auto_languages_role_docker_sysctls`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_sysctls:
        ```

    ??? variable list "`plex_auto_languages_role_docker_ulimits`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`plex_auto_languages_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        plex_auto_languages_role_autoheal_enabled: true
        ```

    ??? variable string "`plex_auto_languages_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        plex_auto_languages_role_depends_on: ""
        ```

    ??? variable string "`plex_auto_languages_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        plex_auto_languages_role_depends_on_delay: "0"
        ```

    ??? variable string "`plex_auto_languages_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        plex_auto_languages_role_depends_on_healthchecks:
        ```

    ??? variable bool "`plex_auto_languages_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        plex_auto_languages_role_diun_enabled: true
        ```

    ??? variable bool "`plex_auto_languages_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        plex_auto_languages_role_docker_controller: true
        ```

    ??? variable list "`plex_auto_languages_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`plex_auto_languages_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        plex_auto_languages_role_docker_volumes_download:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

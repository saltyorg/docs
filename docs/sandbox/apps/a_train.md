---
icon: material/docker
hide:
  - tags
tags:
  - a-train
  - train
  - google
---

# A-Train

## Overview

A-Train is the official Autoscan trigger that listens for changes within Google Drive. It is the successor of Autoscan's Bernard trigger, which unfortunately contains enough logic errors to prompt a rewrite.

- Supports Shared Drives
- Service Account-based authentication
- Does not support My Drive
- Does not support encrypted files
- Does not support alternative authentication methods

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    a_train_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `a_train_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `a_train_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`a_train_name`"

        ```yaml
        # Type: string
        a_train_name: a-train
        ```

=== "Settings"

    ??? variable list "`a_train_role_remotes`"

        ```yaml
        # Type: list
        a_train_role_remotes: [""]
        ```

=== "Paths"

    ??? variable string "`a_train_role_paths_folder`"

        ```yaml
        # Type: string
        a_train_role_paths_folder: "{{ a_train_name }}"
        ```

    ??? variable string "`a_train_role_paths_location`"

        ```yaml
        # Type: string
        a_train_role_paths_location: "{{ server_appdata_path }}/{{ a_train_role_paths_folder }}"
        ```

    ??? variable string "`a_train_role_paths_config_location`"

        ```yaml
        # Type: string
        a_train_role_paths_config_location: "{{ a_train_role_paths_location }}/a-train.toml"
        ```

    ??? variable string "`a_train_role_paths_sa_location`"

        ```yaml
        # Type: string
        a_train_role_paths_sa_location: "{{ a_train_role_paths_location }}/account.json"
        ```

    ??? variable string "`a_train_role_paths_rclone_config_location`"

        ```yaml
        # Type: string
        a_train_role_paths_rclone_config_location: "/home/{{ user.name }}/.config/rclone/rclone.conf"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`a_train_role_docker_container`"

        ```yaml
        # Type: string
        a_train_role_docker_container: "{{ a_train_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`a_train_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        a_train_role_docker_image_pull: true
        ```

    ??? variable string "`a_train_role_docker_image_repo`"

        ```yaml
        # Type: string
        a_train_role_docker_image_repo: "ghcr.io/m-rots/a-train"
        ```

    ??? variable string "`a_train_role_docker_image_tag`"

        ```yaml
        # Type: string
        a_train_role_docker_image_tag: "latest"
        ```

    ??? variable string "`a_train_role_docker_image`"

        ```yaml
        # Type: string
        a_train_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='a_train') }}:{{ lookup('role_var', '_docker_image_tag', role='a_train') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`a_train_role_docker_envs_default`"

        ```yaml
        # Type: dict
        a_train_role_docker_envs_default:
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`a_train_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        a_train_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`a_train_role_docker_volumes_default`"

        ```yaml
        # Type: list
        a_train_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='a_train') }}:/data"
        ```

    ??? variable list "`a_train_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        a_train_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`a_train_role_docker_hostname`"

        ```yaml
        # Type: string
        a_train_role_docker_hostname: "{{ a_train_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`a_train_role_docker_networks_alias`"

        ```yaml
        # Type: string
        a_train_role_docker_networks_alias: "{{ a_train_name }}"
        ```

    ??? variable list "`a_train_role_docker_networks_default`"

        ```yaml
        # Type: list
        a_train_role_docker_networks_default: []
        ```

    ??? variable list "`a_train_role_docker_networks_custom`"

        ```yaml
        # Type: list
        a_train_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`a_train_role_docker_restart_policy`"

        ```yaml
        # Type: string
        a_train_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`a_train_role_docker_state`"

        ```yaml
        # Type: string
        a_train_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`a_train_role_docker_user`"

        ```yaml
        # Type: string
        a_train_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`a_train_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        a_train_role_docker_blkio_weight:
        ```

    ??? variable int "`a_train_role_docker_cpu_period`"

        ```yaml
        # Type: int
        a_train_role_docker_cpu_period:
        ```

    ??? variable int "`a_train_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        a_train_role_docker_cpu_quota:
        ```

    ??? variable int "`a_train_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        a_train_role_docker_cpu_shares:
        ```

    ??? variable string "`a_train_role_docker_cpus`"

        ```yaml
        # Type: string
        a_train_role_docker_cpus:
        ```

    ??? variable string "`a_train_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        a_train_role_docker_cpuset_cpus:
        ```

    ??? variable string "`a_train_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        a_train_role_docker_cpuset_mems:
        ```

    ??? variable string "`a_train_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        a_train_role_docker_kernel_memory:
        ```

    ??? variable string "`a_train_role_docker_memory`"

        ```yaml
        # Type: string
        a_train_role_docker_memory:
        ```

    ??? variable string "`a_train_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        a_train_role_docker_memory_reservation:
        ```

    ??? variable string "`a_train_role_docker_memory_swap`"

        ```yaml
        # Type: string
        a_train_role_docker_memory_swap:
        ```

    ??? variable int "`a_train_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        a_train_role_docker_memory_swappiness:
        ```

    ??? variable string "`a_train_role_docker_shm_size`"

        ```yaml
        # Type: string
        a_train_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`a_train_role_docker_cap_drop`"

        ```yaml
        # Type: list
        a_train_role_docker_cap_drop:
        ```

    ??? variable string "`a_train_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        a_train_role_docker_cgroupns_mode:
        ```

    ??? variable list "`a_train_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        a_train_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`a_train_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        a_train_role_docker_device_read_bps:
        ```

    ??? variable list "`a_train_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        a_train_role_docker_device_read_iops:
        ```

    ??? variable list "`a_train_role_docker_device_requests`"

        ```yaml
        # Type: list
        a_train_role_docker_device_requests:
        ```

    ??? variable list "`a_train_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        a_train_role_docker_device_write_bps:
        ```

    ??? variable list "`a_train_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        a_train_role_docker_device_write_iops:
        ```

    ??? variable list "`a_train_role_docker_devices`"

        ```yaml
        # Type: list
        a_train_role_docker_devices:
        ```

    ??? variable string "`a_train_role_docker_devices_default`"

        ```yaml
        # Type: string
        a_train_role_docker_devices_default:
        ```

    ??? variable list "`a_train_role_docker_groups`"

        ```yaml
        # Type: list
        a_train_role_docker_groups:
        ```

    ??? variable bool "`a_train_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        a_train_role_docker_privileged:
        ```

    ??? variable list "`a_train_role_docker_security_opts`"

        ```yaml
        # Type: list
        a_train_role_docker_security_opts:
        ```

    ??? variable string "`a_train_role_docker_userns_mode`"

        ```yaml
        # Type: string
        a_train_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`a_train_role_docker_dns_opts`"

        ```yaml
        # Type: list
        a_train_role_docker_dns_opts:
        ```

    ??? variable list "`a_train_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        a_train_role_docker_dns_search_domains:
        ```

    ??? variable list "`a_train_role_docker_dns_servers`"

        ```yaml
        # Type: list
        a_train_role_docker_dns_servers:
        ```

    ??? variable string "`a_train_role_docker_domainname`"

        ```yaml
        # Type: string
        a_train_role_docker_domainname:
        ```

    ??? variable list "`a_train_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        a_train_role_docker_exposed_ports:
        ```

    ??? variable dict "`a_train_role_docker_hosts`"

        ```yaml
        # Type: dict
        a_train_role_docker_hosts:
        ```

    ??? variable bool "`a_train_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        a_train_role_docker_hosts_use_common:
        ```

    ??? variable string "`a_train_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        a_train_role_docker_ipc_mode:
        ```

    ??? variable list "`a_train_role_docker_links`"

        ```yaml
        # Type: list
        a_train_role_docker_links:
        ```

    ??? variable string "`a_train_role_docker_network_mode`"

        ```yaml
        # Type: string
        a_train_role_docker_network_mode:
        ```

    ??? variable string "`a_train_role_docker_pid_mode`"

        ```yaml
        # Type: string
        a_train_role_docker_pid_mode:
        ```

    ??? variable list "`a_train_role_docker_ports`"

        ```yaml
        # Type: list
        a_train_role_docker_ports:
        ```

    ??? variable string "`a_train_role_docker_uts`"

        ```yaml
        # Type: string
        a_train_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`a_train_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        a_train_role_docker_keep_volumes:
        ```

    ??? variable list "`a_train_role_docker_mounts`"

        ```yaml
        # Type: list
        a_train_role_docker_mounts:
        ```

    ??? variable dict "`a_train_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        a_train_role_docker_storage_opts:
        ```

    ??? variable list "`a_train_role_docker_tmpfs`"

        ```yaml
        # Type: list
        a_train_role_docker_tmpfs:
        ```

    ??? variable string "`a_train_role_docker_volume_driver`"

        ```yaml
        # Type: string
        a_train_role_docker_volume_driver:
        ```

    ??? variable list "`a_train_role_docker_volumes_from`"

        ```yaml
        # Type: list
        a_train_role_docker_volumes_from:
        ```

    ??? variable bool "`a_train_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        a_train_role_docker_volumes_global:
        ```

    ??? variable string "`a_train_role_docker_working_dir`"

        ```yaml
        # Type: string
        a_train_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`a_train_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        a_train_role_docker_auto_remove:
        ```

    ??? variable bool "`a_train_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        a_train_role_docker_cleanup:
        ```

    ??? variable string "`a_train_role_docker_force_kill`"

        ```yaml
        # Type: string
        a_train_role_docker_force_kill:
        ```

    ??? variable dict "`a_train_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        a_train_role_docker_healthcheck:
        ```

    ??? variable int "`a_train_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        a_train_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`a_train_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        a_train_role_docker_init:
        ```

    ??? variable string "`a_train_role_docker_kill_signal`"

        ```yaml
        # Type: string
        a_train_role_docker_kill_signal:
        ```

    ??? variable string "`a_train_role_docker_log_driver`"

        ```yaml
        # Type: string
        a_train_role_docker_log_driver:
        ```

    ??? variable dict "`a_train_role_docker_log_options`"

        ```yaml
        # Type: dict
        a_train_role_docker_log_options:
        ```

    ??? variable bool "`a_train_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        a_train_role_docker_oom_killer:
        ```

    ??? variable int "`a_train_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        a_train_role_docker_oom_score_adj:
        ```

    ??? variable bool "`a_train_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        a_train_role_docker_output_logs:
        ```

    ??? variable bool "`a_train_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        a_train_role_docker_paused:
        ```

    ??? variable bool "`a_train_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        a_train_role_docker_recreate:
        ```

    ??? variable int "`a_train_role_docker_restart_retries`"

        ```yaml
        # Type: int
        a_train_role_docker_restart_retries:
        ```

    ??? variable int "`a_train_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        a_train_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`a_train_role_docker_capabilities`"

        ```yaml
        # Type: list
        a_train_role_docker_capabilities:
        ```

    ??? variable string "`a_train_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        a_train_role_docker_cgroup_parent:
        ```

    ??? variable list "`a_train_role_docker_commands`"

        ```yaml
        # Type: list
        a_train_role_docker_commands:
        ```

    ??? variable int "`a_train_role_docker_create_timeout`"

        ```yaml
        # Type: int
        a_train_role_docker_create_timeout:
        ```

    ??? variable string "`a_train_role_docker_entrypoint`"

        ```yaml
        # Type: string
        a_train_role_docker_entrypoint:
        ```

    ??? variable string "`a_train_role_docker_env_file`"

        ```yaml
        # Type: string
        a_train_role_docker_env_file:
        ```

    ??? variable dict "`a_train_role_docker_labels`"

        ```yaml
        # Type: dict
        a_train_role_docker_labels:
        ```

    ??? variable bool "`a_train_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        a_train_role_docker_labels_use_common:
        ```

    ??? variable bool "`a_train_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        a_train_role_docker_read_only:
        ```

    ??? variable string "`a_train_role_docker_runtime`"

        ```yaml
        # Type: string
        a_train_role_docker_runtime:
        ```

    ??? variable list "`a_train_role_docker_sysctls`"

        ```yaml
        # Type: list
        a_train_role_docker_sysctls:
        ```

    ??? variable list "`a_train_role_docker_ulimits`"

        ```yaml
        # Type: list
        a_train_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`a_train_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        a_train_role_autoheal_enabled: true
        ```

    ??? variable string "`a_train_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        a_train_role_depends_on: ""
        ```

    ??? variable string "`a_train_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        a_train_role_depends_on_delay: "0"
        ```

    ??? variable string "`a_train_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        a_train_role_depends_on_healthchecks:
        ```

    ??? variable bool "`a_train_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        a_train_role_diun_enabled: true
        ```

    ??? variable bool "`a_train_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        a_train_role_docker_controller: true
        ```

    ??? variable string "`a_train_role_docker_image_repo`"

        ```yaml
        # Type: string
        a_train_role_docker_image_repo:
        ```

    ??? variable string "`a_train_role_docker_image_tag`"

        ```yaml
        # Type: string
        a_train_role_docker_image_tag:
        ```

    ??? variable bool "`a_train_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        a_train_role_docker_volumes_download:
        ```

    ??? variable string "`a_train_role_paths_location`"

        ```yaml
        # Type: string
        a_train_role_paths_location:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
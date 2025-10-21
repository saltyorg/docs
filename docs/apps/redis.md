---
hide:
  - tags
tags:
  - redis
  - database
  - cache
  - key-value
---

# Redis

## What is it?

Redis is an open-source, in-memory data structure store used as a database, cache, message broker, and streaming engine. It supports various data structures such as strings, hashes, lists, sets, and sorted sets, making it extremely versatile and fast.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://redis.io/){: .header-icons } | [:octicons-link-16: Docs](https://redis.io/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/redis/redis){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/redis){: .header-icons }|

### 1. Installation

``` shell

sb install redis

```

### 2. Setup

Redis is deployed using the official Alpine image with data persisting to `/opt/redis/`. Connect from other containers using `redis://redis:6379`. Multiple instances are supported via the `redis_instances` variable in your [Saltbox inventory](../saltbox/inventory/index.md).

For custom configuration, create `redis.conf` in `/opt/redis/` and configure custom volumes in your inventory. Note: No authentication is configured by default.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `redis_instances`.

    === "Role-level Override"

        Applies to all instances of redis:

        ```yaml
        redis_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `redis2`):

        ```yaml
        redis2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `redis_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `redis_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`redis_instances`"

        ```yaml
        # Type: list
        redis_instances: ["redis"]
        ```

        !!! example

            ```yaml
            # Type: list
            redis_instances: ["redis", "redis2"]
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`redis_role_paths_folder`"

            ```yaml
            # Type: string
            redis_role_paths_folder: "{{ redis_name }}"
            ```

        ??? variable string "`redis_role_paths_location`"

            ```yaml
            # Type: string
            redis_role_paths_location: "{{ server_appdata_path }}/{{ redis_role_paths_folder }}"
            ```

    === "Instance-level"

        ??? variable string "`redis2_paths_folder`"

            ```yaml
            # Type: string
            redis2_paths_folder: "{{ redis_name }}"
            ```

        ??? variable string "`redis2_paths_location`"

            ```yaml
            # Type: string
            redis2_paths_location: "{{ server_appdata_path }}/{{ redis_role_paths_folder }}"
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`redis_role_docker_container`"

            ```yaml
            # Type: string
            redis_role_docker_container: "{{ redis_name }}"
            ```

        ##### Image

        ??? variable bool "`redis_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            redis_role_docker_image_pull: true
            ```

        ??? variable string "`redis_role_docker_image_tag`"

            ```yaml
            # Type: string
            redis_role_docker_image_tag: "alpine"
            ```

        ??? variable string "`redis_role_docker_image_repo`"

            ```yaml
            # Type: string
            redis_role_docker_image_repo: "redis"
            ```

        ??? variable string "`redis_role_docker_image`"

            ```yaml
            # Type: string
            redis_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='redis') }}:{{ lookup('role_var', '_docker_image_tag', role='redis') }}"
            ```

        ##### Envs

        ??? variable dict "`redis_role_docker_envs_default`"

            ```yaml
            # Type: dict
            redis_role_docker_envs_default: 
              TZ: "{{ tz }}"
            ```

        ??? variable dict "`redis_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            redis_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`redis_role_docker_volumes_default`"

            ```yaml
            # Type: list
            redis_role_docker_volumes_default: 
              - "{{ redis_role_paths_location }}:/data"
            ```

        ??? variable list "`redis_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            redis_role_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`redis_role_docker_hostname`"

            ```yaml
            # Type: string
            redis_role_docker_hostname: "{{ redis_name }}"
            ```

        ##### Networks

        ??? variable string "`redis_role_docker_networks_alias`"

            ```yaml
            # Type: string
            redis_role_docker_networks_alias: "{{ redis_name }}"
            ```

        ??? variable list "`redis_role_docker_networks_default`"

            ```yaml
            # Type: list
            redis_role_docker_networks_default: []
            ```

        ??? variable list "`redis_role_docker_networks_custom`"

            ```yaml
            # Type: list
            redis_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`redis_role_docker_restart_policy`"

            ```yaml
            # Type: string
            redis_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`redis_role_docker_state`"

            ```yaml
            # Type: string
            redis_role_docker_state: started
            ```

        ##### User

        ??? variable string "`redis_role_docker_user`"

            ```yaml
            # Type: string
            redis_role_docker_user: "{{ uid }}:{{ gid }}"
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`redis2_docker_container`"

            ```yaml
            # Type: string
            redis2_docker_container: "{{ redis_name }}"
            ```

        ##### Image

        ??? variable bool "`redis2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            redis2_docker_image_pull: true
            ```

        ??? variable string "`redis2_docker_image_tag`"

            ```yaml
            # Type: string
            redis2_docker_image_tag: "alpine"
            ```

        ??? variable string "`redis2_docker_image_repo`"

            ```yaml
            # Type: string
            redis2_docker_image_repo: "redis"
            ```

        ??? variable string "`redis2_docker_image`"

            ```yaml
            # Type: string
            redis2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='redis') }}:{{ lookup('role_var', '_docker_image_tag', role='redis') }}"
            ```

        ##### Envs

        ??? variable dict "`redis2_docker_envs_default`"

            ```yaml
            # Type: dict
            redis2_docker_envs_default: 
              TZ: "{{ tz }}"
            ```

        ??? variable dict "`redis2_docker_envs_custom`"

            ```yaml
            # Type: dict
            redis2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`redis2_docker_volumes_default`"

            ```yaml
            # Type: list
            redis2_docker_volumes_default: 
              - "{{ redis_role_paths_location }}:/data"
            ```

        ??? variable list "`redis2_docker_volumes_custom`"

            ```yaml
            # Type: list
            redis2_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`redis2_docker_hostname`"

            ```yaml
            # Type: string
            redis2_docker_hostname: "{{ redis_name }}"
            ```

        ##### Networks

        ??? variable string "`redis2_docker_networks_alias`"

            ```yaml
            # Type: string
            redis2_docker_networks_alias: "{{ redis_name }}"
            ```

        ??? variable list "`redis2_docker_networks_default`"

            ```yaml
            # Type: list
            redis2_docker_networks_default: []
            ```

        ??? variable list "`redis2_docker_networks_custom`"

            ```yaml
            # Type: list
            redis2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`redis2_docker_restart_policy`"

            ```yaml
            # Type: string
            redis2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`redis2_docker_state`"

            ```yaml
            # Type: string
            redis2_docker_state: started
            ```

        ##### User

        ??? variable string "`redis2_docker_user`"

            ```yaml
            # Type: string
            redis2_docker_user: "{{ uid }}:{{ gid }}"
            ```

=== "Docker+"

    #### Additional Docker Options

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    === "Role-level"

        ##### Resource Limits

        ??? variable int "`redis_role_docker_blkio_weight`"

            ```yaml
            # Type: int
            redis_role_docker_blkio_weight:
            ```

        ??? variable int "`redis_role_docker_cpu_period`"

            ```yaml
            # Type: int
            redis_role_docker_cpu_period:
            ```

        ??? variable int "`redis_role_docker_cpu_quota`"

            ```yaml
            # Type: int
            redis_role_docker_cpu_quota:
            ```

        ??? variable int "`redis_role_docker_cpu_shares`"

            ```yaml
            # Type: int
            redis_role_docker_cpu_shares:
            ```

        ??? variable string "`redis_role_docker_cpus`"

            ```yaml
            # Type: string
            redis_role_docker_cpus:
            ```

        ??? variable string "`redis_role_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            redis_role_docker_cpuset_cpus:
            ```

        ??? variable string "`redis_role_docker_cpuset_mems`"

            ```yaml
            # Type: string
            redis_role_docker_cpuset_mems:
            ```

        ??? variable string "`redis_role_docker_kernel_memory`"

            ```yaml
            # Type: string
            redis_role_docker_kernel_memory:
            ```

        ??? variable string "`redis_role_docker_memory`"

            ```yaml
            # Type: string
            redis_role_docker_memory:
            ```

        ??? variable string "`redis_role_docker_memory_reservation`"

            ```yaml
            # Type: string
            redis_role_docker_memory_reservation:
            ```

        ??? variable string "`redis_role_docker_memory_swap`"

            ```yaml
            # Type: string
            redis_role_docker_memory_swap:
            ```

        ??? variable int "`redis_role_docker_memory_swappiness`"

            ```yaml
            # Type: int
            redis_role_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`redis_role_docker_cap_drop`"

            ```yaml
            # Type: list
            redis_role_docker_cap_drop:
            ```

        ??? variable list "`redis_role_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            redis_role_docker_device_cgroup_rules:
            ```

        ??? variable list "`redis_role_docker_device_read_bps`"

            ```yaml
            # Type: list
            redis_role_docker_device_read_bps:
            ```

        ??? variable list "`redis_role_docker_device_read_iops`"

            ```yaml
            # Type: list
            redis_role_docker_device_read_iops:
            ```

        ??? variable list "`redis_role_docker_device_requests`"

            ```yaml
            # Type: list
            redis_role_docker_device_requests:
            ```

        ??? variable list "`redis_role_docker_device_write_bps`"

            ```yaml
            # Type: list
            redis_role_docker_device_write_bps:
            ```

        ??? variable list "`redis_role_docker_device_write_iops`"

            ```yaml
            # Type: list
            redis_role_docker_device_write_iops:
            ```

        ??? variable list "`redis_role_docker_devices`"

            ```yaml
            # Type: list
            redis_role_docker_devices:
            ```

        ??? variable string "`redis_role_docker_devices_default`"

            ```yaml
            # Type: string
            redis_role_docker_devices_default:
            ```

        ??? variable bool "`redis_role_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            redis_role_docker_privileged:
            ```

        ??? variable list "`redis_role_docker_security_opts`"

            ```yaml
            # Type: list
            redis_role_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`redis_role_docker_dns_opts`"

            ```yaml
            # Type: list
            redis_role_docker_dns_opts:
            ```

        ??? variable list "`redis_role_docker_dns_search_domains`"

            ```yaml
            # Type: list
            redis_role_docker_dns_search_domains:
            ```

        ??? variable list "`redis_role_docker_dns_servers`"

            ```yaml
            # Type: list
            redis_role_docker_dns_servers:
            ```

        ??? variable dict "`redis_role_docker_hosts`"

            ```yaml
            # Type: dict
            redis_role_docker_hosts:
            ```

        ??? variable string "`redis_role_docker_hosts_use_common`"

            ```yaml
            # Type: string
            redis_role_docker_hosts_use_common:
            ```

        ??? variable string "`redis_role_docker_network_mode`"

            ```yaml
            # Type: string
            redis_role_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`redis_role_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            redis_role_docker_keep_volumes:
            ```

        ??? variable list "`redis_role_docker_mounts`"

            ```yaml
            # Type: list
            redis_role_docker_mounts:
            ```

        ??? variable string "`redis_role_docker_volume_driver`"

            ```yaml
            # Type: string
            redis_role_docker_volume_driver:
            ```

        ??? variable list "`redis_role_docker_volumes_from`"

            ```yaml
            # Type: list
            redis_role_docker_volumes_from:
            ```

        ??? variable string "`redis_role_docker_volumes_global`"

            ```yaml
            # Type: string
            redis_role_docker_volumes_global:
            ```

        ??? variable string "`redis_role_docker_working_dir`"

            ```yaml
            # Type: string
            redis_role_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`redis_role_docker_healthcheck`"

            ```yaml
            # Type: dict
            redis_role_docker_healthcheck:
            ```

        ??? variable bool "`redis_role_docker_init`"

            ```yaml
            # Type: bool (true/false)
            redis_role_docker_init:
            ```

        ??? variable string "`redis_role_docker_log_driver`"

            ```yaml
            # Type: string
            redis_role_docker_log_driver:
            ```

        ??? variable dict "`redis_role_docker_log_options`"

            ```yaml
            # Type: dict
            redis_role_docker_log_options:
            ```

        ??? variable bool "`redis_role_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            redis_role_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`redis_role_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            redis_role_docker_auto_remove:
            ```

        ??? variable list "`redis_role_docker_capabilities`"

            ```yaml
            # Type: list
            redis_role_docker_capabilities:
            ```

        ??? variable string "`redis_role_docker_cgroup_parent`"

            ```yaml
            # Type: string
            redis_role_docker_cgroup_parent:
            ```

        ??? variable string "`redis_role_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            redis_role_docker_cgroupns_mode:
            ```

        ??? variable bool "`redis_role_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            redis_role_docker_cleanup:
            ```

        ??? variable list "`redis_role_docker_commands`"

            ```yaml
            # Type: list
            redis_role_docker_commands:
            ```

        ??? variable string "`redis_role_docker_create_timeout`"

            ```yaml
            # Type: string
            redis_role_docker_create_timeout:
            ```

        ??? variable string "`redis_role_docker_domainname`"

            ```yaml
            # Type: string
            redis_role_docker_domainname:
            ```

        ??? variable string "`redis_role_docker_entrypoint`"

            ```yaml
            # Type: string
            redis_role_docker_entrypoint:
            ```

        ??? variable string "`redis_role_docker_env_file`"

            ```yaml
            # Type: string
            redis_role_docker_env_file:
            ```

        ??? variable list "`redis_role_docker_exposed_ports`"

            ```yaml
            # Type: list
            redis_role_docker_exposed_ports:
            ```

        ??? variable string "`redis_role_docker_force_kill`"

            ```yaml
            # Type: string
            redis_role_docker_force_kill:
            ```

        ??? variable list "`redis_role_docker_groups`"

            ```yaml
            # Type: list
            redis_role_docker_groups:
            ```

        ??? variable int "`redis_role_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            redis_role_docker_healthy_wait_timeout:
            ```

        ??? variable string "`redis_role_docker_ipc_mode`"

            ```yaml
            # Type: string
            redis_role_docker_ipc_mode:
            ```

        ??? variable string "`redis_role_docker_kill_signal`"

            ```yaml
            # Type: string
            redis_role_docker_kill_signal:
            ```

        ??? variable dict "`redis_role_docker_labels`"

            ```yaml
            # Type: dict
            redis_role_docker_labels:
            ```

        ??? variable string "`redis_role_docker_labels_use_common`"

            ```yaml
            # Type: string
            redis_role_docker_labels_use_common:
            ```

        ??? variable list "`redis_role_docker_links`"

            ```yaml
            # Type: list
            redis_role_docker_links:
            ```

        ??? variable bool "`redis_role_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            redis_role_docker_oom_killer:
            ```

        ??? variable int "`redis_role_docker_oom_score_adj`"

            ```yaml
            # Type: int
            redis_role_docker_oom_score_adj:
            ```

        ??? variable bool "`redis_role_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            redis_role_docker_paused:
            ```

        ??? variable string "`redis_role_docker_pid_mode`"

            ```yaml
            # Type: string
            redis_role_docker_pid_mode:
            ```

        ??? variable list "`redis_role_docker_ports`"

            ```yaml
            # Type: list
            redis_role_docker_ports:
            ```

        ??? variable bool "`redis_role_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            redis_role_docker_read_only:
            ```

        ??? variable bool "`redis_role_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            redis_role_docker_recreate:
            ```

        ??? variable int "`redis_role_docker_restart_retries`"

            ```yaml
            # Type: int
            redis_role_docker_restart_retries:
            ```

        ??? variable string "`redis_role_docker_runtime`"

            ```yaml
            # Type: string
            redis_role_docker_runtime:
            ```

        ??? variable string "`redis_role_docker_shm_size`"

            ```yaml
            # Type: string
            redis_role_docker_shm_size:
            ```

        ??? variable int "`redis_role_docker_stop_timeout`"

            ```yaml
            # Type: int
            redis_role_docker_stop_timeout:
            ```

        ??? variable dict "`redis_role_docker_storage_opts`"

            ```yaml
            # Type: dict
            redis_role_docker_storage_opts:
            ```

        ??? variable list "`redis_role_docker_sysctls`"

            ```yaml
            # Type: list
            redis_role_docker_sysctls:
            ```

        ??? variable list "`redis_role_docker_tmpfs`"

            ```yaml
            # Type: list
            redis_role_docker_tmpfs:
            ```

        ??? variable list "`redis_role_docker_ulimits`"

            ```yaml
            # Type: list
            redis_role_docker_ulimits:
            ```

        ??? variable string "`redis_role_docker_userns_mode`"

            ```yaml
            # Type: string
            redis_role_docker_userns_mode:
            ```

        ??? variable string "`redis_role_docker_uts`"

            ```yaml
            # Type: string
            redis_role_docker_uts:
            ```

    === "Instance-level"

        ##### Resource Limits

        ??? variable int "`redis2_docker_blkio_weight`"

            ```yaml
            # Type: int
            redis2_docker_blkio_weight:
            ```

        ??? variable int "`redis2_docker_cpu_period`"

            ```yaml
            # Type: int
            redis2_docker_cpu_period:
            ```

        ??? variable int "`redis2_docker_cpu_quota`"

            ```yaml
            # Type: int
            redis2_docker_cpu_quota:
            ```

        ??? variable int "`redis2_docker_cpu_shares`"

            ```yaml
            # Type: int
            redis2_docker_cpu_shares:
            ```

        ??? variable string "`redis2_docker_cpus`"

            ```yaml
            # Type: string
            redis2_docker_cpus:
            ```

        ??? variable string "`redis2_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            redis2_docker_cpuset_cpus:
            ```

        ??? variable string "`redis2_docker_cpuset_mems`"

            ```yaml
            # Type: string
            redis2_docker_cpuset_mems:
            ```

        ??? variable string "`redis2_docker_kernel_memory`"

            ```yaml
            # Type: string
            redis2_docker_kernel_memory:
            ```

        ??? variable string "`redis2_docker_memory`"

            ```yaml
            # Type: string
            redis2_docker_memory:
            ```

        ??? variable string "`redis2_docker_memory_reservation`"

            ```yaml
            # Type: string
            redis2_docker_memory_reservation:
            ```

        ??? variable string "`redis2_docker_memory_swap`"

            ```yaml
            # Type: string
            redis2_docker_memory_swap:
            ```

        ??? variable int "`redis2_docker_memory_swappiness`"

            ```yaml
            # Type: int
            redis2_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`redis2_docker_cap_drop`"

            ```yaml
            # Type: list
            redis2_docker_cap_drop:
            ```

        ??? variable list "`redis2_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            redis2_docker_device_cgroup_rules:
            ```

        ??? variable list "`redis2_docker_device_read_bps`"

            ```yaml
            # Type: list
            redis2_docker_device_read_bps:
            ```

        ??? variable list "`redis2_docker_device_read_iops`"

            ```yaml
            # Type: list
            redis2_docker_device_read_iops:
            ```

        ??? variable list "`redis2_docker_device_requests`"

            ```yaml
            # Type: list
            redis2_docker_device_requests:
            ```

        ??? variable list "`redis2_docker_device_write_bps`"

            ```yaml
            # Type: list
            redis2_docker_device_write_bps:
            ```

        ??? variable list "`redis2_docker_device_write_iops`"

            ```yaml
            # Type: list
            redis2_docker_device_write_iops:
            ```

        ??? variable list "`redis2_docker_devices`"

            ```yaml
            # Type: list
            redis2_docker_devices:
            ```

        ??? variable string "`redis2_docker_devices_default`"

            ```yaml
            # Type: string
            redis2_docker_devices_default:
            ```

        ??? variable bool "`redis2_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            redis2_docker_privileged:
            ```

        ??? variable list "`redis2_docker_security_opts`"

            ```yaml
            # Type: list
            redis2_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`redis2_docker_dns_opts`"

            ```yaml
            # Type: list
            redis2_docker_dns_opts:
            ```

        ??? variable list "`redis2_docker_dns_search_domains`"

            ```yaml
            # Type: list
            redis2_docker_dns_search_domains:
            ```

        ??? variable list "`redis2_docker_dns_servers`"

            ```yaml
            # Type: list
            redis2_docker_dns_servers:
            ```

        ??? variable dict "`redis2_docker_hosts`"

            ```yaml
            # Type: dict
            redis2_docker_hosts:
            ```

        ??? variable string "`redis2_docker_hosts_use_common`"

            ```yaml
            # Type: string
            redis2_docker_hosts_use_common:
            ```

        ??? variable string "`redis2_docker_network_mode`"

            ```yaml
            # Type: string
            redis2_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`redis2_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            redis2_docker_keep_volumes:
            ```

        ??? variable list "`redis2_docker_mounts`"

            ```yaml
            # Type: list
            redis2_docker_mounts:
            ```

        ??? variable string "`redis2_docker_volume_driver`"

            ```yaml
            # Type: string
            redis2_docker_volume_driver:
            ```

        ??? variable list "`redis2_docker_volumes_from`"

            ```yaml
            # Type: list
            redis2_docker_volumes_from:
            ```

        ??? variable string "`redis2_docker_volumes_global`"

            ```yaml
            # Type: string
            redis2_docker_volumes_global:
            ```

        ??? variable string "`redis2_docker_working_dir`"

            ```yaml
            # Type: string
            redis2_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`redis2_docker_healthcheck`"

            ```yaml
            # Type: dict
            redis2_docker_healthcheck:
            ```

        ??? variable bool "`redis2_docker_init`"

            ```yaml
            # Type: bool (true/false)
            redis2_docker_init:
            ```

        ??? variable string "`redis2_docker_log_driver`"

            ```yaml
            # Type: string
            redis2_docker_log_driver:
            ```

        ??? variable dict "`redis2_docker_log_options`"

            ```yaml
            # Type: dict
            redis2_docker_log_options:
            ```

        ??? variable bool "`redis2_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            redis2_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`redis2_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            redis2_docker_auto_remove:
            ```

        ??? variable list "`redis2_docker_capabilities`"

            ```yaml
            # Type: list
            redis2_docker_capabilities:
            ```

        ??? variable string "`redis2_docker_cgroup_parent`"

            ```yaml
            # Type: string
            redis2_docker_cgroup_parent:
            ```

        ??? variable string "`redis2_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            redis2_docker_cgroupns_mode:
            ```

        ??? variable bool "`redis2_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            redis2_docker_cleanup:
            ```

        ??? variable list "`redis2_docker_commands`"

            ```yaml
            # Type: list
            redis2_docker_commands:
            ```

        ??? variable string "`redis2_docker_create_timeout`"

            ```yaml
            # Type: string
            redis2_docker_create_timeout:
            ```

        ??? variable string "`redis2_docker_domainname`"

            ```yaml
            # Type: string
            redis2_docker_domainname:
            ```

        ??? variable string "`redis2_docker_entrypoint`"

            ```yaml
            # Type: string
            redis2_docker_entrypoint:
            ```

        ??? variable string "`redis2_docker_env_file`"

            ```yaml
            # Type: string
            redis2_docker_env_file:
            ```

        ??? variable list "`redis2_docker_exposed_ports`"

            ```yaml
            # Type: list
            redis2_docker_exposed_ports:
            ```

        ??? variable string "`redis2_docker_force_kill`"

            ```yaml
            # Type: string
            redis2_docker_force_kill:
            ```

        ??? variable list "`redis2_docker_groups`"

            ```yaml
            # Type: list
            redis2_docker_groups:
            ```

        ??? variable int "`redis2_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            redis2_docker_healthy_wait_timeout:
            ```

        ??? variable string "`redis2_docker_ipc_mode`"

            ```yaml
            # Type: string
            redis2_docker_ipc_mode:
            ```

        ??? variable string "`redis2_docker_kill_signal`"

            ```yaml
            # Type: string
            redis2_docker_kill_signal:
            ```

        ??? variable dict "`redis2_docker_labels`"

            ```yaml
            # Type: dict
            redis2_docker_labels:
            ```

        ??? variable string "`redis2_docker_labels_use_common`"

            ```yaml
            # Type: string
            redis2_docker_labels_use_common:
            ```

        ??? variable list "`redis2_docker_links`"

            ```yaml
            # Type: list
            redis2_docker_links:
            ```

        ??? variable bool "`redis2_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            redis2_docker_oom_killer:
            ```

        ??? variable int "`redis2_docker_oom_score_adj`"

            ```yaml
            # Type: int
            redis2_docker_oom_score_adj:
            ```

        ??? variable bool "`redis2_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            redis2_docker_paused:
            ```

        ??? variable string "`redis2_docker_pid_mode`"

            ```yaml
            # Type: string
            redis2_docker_pid_mode:
            ```

        ??? variable list "`redis2_docker_ports`"

            ```yaml
            # Type: list
            redis2_docker_ports:
            ```

        ??? variable bool "`redis2_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            redis2_docker_read_only:
            ```

        ??? variable bool "`redis2_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            redis2_docker_recreate:
            ```

        ??? variable int "`redis2_docker_restart_retries`"

            ```yaml
            # Type: int
            redis2_docker_restart_retries:
            ```

        ??? variable string "`redis2_docker_runtime`"

            ```yaml
            # Type: string
            redis2_docker_runtime:
            ```

        ??? variable string "`redis2_docker_shm_size`"

            ```yaml
            # Type: string
            redis2_docker_shm_size:
            ```

        ??? variable int "`redis2_docker_stop_timeout`"

            ```yaml
            # Type: int
            redis2_docker_stop_timeout:
            ```

        ??? variable dict "`redis2_docker_storage_opts`"

            ```yaml
            # Type: dict
            redis2_docker_storage_opts:
            ```

        ??? variable list "`redis2_docker_sysctls`"

            ```yaml
            # Type: list
            redis2_docker_sysctls:
            ```

        ??? variable list "`redis2_docker_tmpfs`"

            ```yaml
            # Type: list
            redis2_docker_tmpfs:
            ```

        ??? variable list "`redis2_docker_ulimits`"

            ```yaml
            # Type: list
            redis2_docker_ulimits:
            ```

        ??? variable string "`redis2_docker_userns_mode`"

            ```yaml
            # Type: string
            redis2_docker_userns_mode:
            ```

        ??? variable string "`redis2_docker_uts`"

            ```yaml
            # Type: string
            redis2_docker_uts:
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`redis_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            redis_role_autoheal_enabled: true
            ```

        ??? variable string "`redis_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            redis_role_depends_on: ""
            ```

        ??? variable string "`redis_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            redis_role_depends_on_delay: "0"
            ```

        ??? variable string "`redis_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            redis_role_depends_on_healthchecks:
            ```

        ??? variable bool "`redis_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            redis_role_diun_enabled: true
            ```

        ??? variable bool "`redis_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            redis_role_dns_enabled: true
            ```

        ??? variable bool "`redis_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            redis_role_docker_controller: true
            ```

        ??? variable bool "`redis_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            redis_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`redis_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            redis_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`redis_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            redis_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`redis_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            redis_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`redis_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            redis_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`redis_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            redis_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`redis_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            redis_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`redis_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            redis_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                redis_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "redis2.{{ user.domain }}"
                  - "redis.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`redis_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            redis_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                redis_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'redis2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`redis_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            redis_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `redis2`):

        ??? variable bool "`redis2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            redis2_autoheal_enabled: true
            ```

        ??? variable string "`redis2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            redis2_depends_on: ""
            ```

        ??? variable string "`redis2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            redis2_depends_on_delay: "0"
            ```

        ??? variable string "`redis2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            redis2_depends_on_healthchecks:
            ```

        ??? variable bool "`redis2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            redis2_diun_enabled: true
            ```

        ??? variable bool "`redis2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            redis2_dns_enabled: true
            ```

        ??? variable bool "`redis2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            redis2_docker_controller: true
            ```

        ??? variable bool "`redis2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            redis2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`redis2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            redis2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`redis2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            redis2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`redis2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            redis2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`redis2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            redis2_traefik_robot_enabled: true
            ```

        ??? variable bool "`redis2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            redis2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`redis2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            redis2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`redis2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            redis2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                redis2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "redis2.{{ user.domain }}"
                  - "redis.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`redis2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            redis2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                redis2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'redis2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`redis2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            redis2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
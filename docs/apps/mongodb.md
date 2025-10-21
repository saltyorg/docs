---
hide:
  - tags
tags:
  - mongodb
  - database
  - nosql
---

# MongoDB

## What is it?

MongoDB is a popular NoSQL document database that stores data in flexible, JSON-like documents. It's designed for scalability and developer productivity, and is used by many applications for data persistence.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.mongodb.com/){: .header-icons } | [:octicons-link-16: Docs](https://www.mongodb.com/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/mongodb/mongo){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/mongo){: .header-icons }|

### 1. Installation

``` shell

sb install mongodb

```

### 2. Setup

MongoDB 6 is deployed in a Docker container with data persisting to `/opt/mongo/`. Connect from other containers using `mongodb://mongo:27017/`. Multiple instances are supported via the `mongodb_instances` variable in your [Saltbox inventory](../saltbox/inventory/index.md).

Note: No authentication is configured by default.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `mongodb_instances`.

    === "Role-level Override"

        Applies to all instances of mongodb:

        ```yaml
        mongodb_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `mongodb2`):

        ```yaml
        mongodb2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `mongodb_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `mongodb_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`mongodb_instances`"

        ```yaml
        # Type: list
        mongodb_instances: ["mongo"]
        ```

        !!! example

            ```yaml
            # Type: list
            mongodb_instances: ["mongodb", "mongodb2"]
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`mongodb_role_paths_folder`"

            ```yaml
            # Type: string
            mongodb_role_paths_folder: "{{ mongodb_name }}"
            ```

        ??? variable string "`mongodb_role_paths_location`"

            ```yaml
            # Type: string
            mongodb_role_paths_location: "{{ server_appdata_path }}/{{ mongodb_role_paths_folder }}"
            ```

    === "Instance-level"

        ??? variable string "`mongodb2_paths_folder`"

            ```yaml
            # Type: string
            mongodb2_paths_folder: "{{ mongodb_name }}"
            ```

        ??? variable string "`mongodb2_paths_location`"

            ```yaml
            # Type: string
            mongodb2_paths_location: "{{ server_appdata_path }}/{{ mongodb_role_paths_folder }}"
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`mongodb_role_docker_container`"

            ```yaml
            # Type: string
            mongodb_role_docker_container: "{{ mongodb_name }}"
            ```

        ##### Image

        ??? variable bool "`mongodb_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            mongodb_role_docker_image_pull: true
            ```

        ??? variable string "`mongodb_role_docker_image_repo`"

            ```yaml
            # Type: string
            mongodb_role_docker_image_repo: "mongo"
            ```

        ??? variable string "`mongodb_role_docker_image_tag`"

            ```yaml
            # Type: string
            mongodb_role_docker_image_tag: "6"
            ```

        ??? variable string "`mongodb_role_docker_image`"

            ```yaml
            # Type: string
            mongodb_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='mongodb') }}:{{ lookup('role_var', '_docker_image_tag', role='mongodb') }}"
            ```

        ##### Envs

        ??? variable dict "`mongodb_role_docker_envs_default`"

            ```yaml
            # Type: dict
            mongodb_role_docker_envs_default: 
              MONGO_DATA_DIR: "/data/db"
              MONGO_LOG_DIR: "/dev/null"
              MONGO_URL: "mongodb://{{ mongodb_name }}:27017/"
            ```

        ??? variable dict "`mongodb_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            mongodb_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`mongodb_role_docker_volumes_default`"

            ```yaml
            # Type: list
            mongodb_role_docker_volumes_default: 
              - "{{ mongodb_role_paths_location }}:/data/db:rw"
              - "{{ mongodb_role_paths_location }}/config:/data/configdb"
            ```

        ??? variable list "`mongodb_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            mongodb_role_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`mongodb_role_docker_hostname`"

            ```yaml
            # Type: string
            mongodb_role_docker_hostname: "{{ mongodb_name }}"
            ```

        ##### Networks

        ??? variable string "`mongodb_role_docker_networks_alias`"

            ```yaml
            # Type: string
            mongodb_role_docker_networks_alias: "{{ mongodb_name }}"
            ```

        ??? variable list "`mongodb_role_docker_networks_default`"

            ```yaml
            # Type: list
            mongodb_role_docker_networks_default: []
            ```

        ??? variable list "`mongodb_role_docker_networks_custom`"

            ```yaml
            # Type: list
            mongodb_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`mongodb_role_docker_restart_policy`"

            ```yaml
            # Type: string
            mongodb_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`mongodb_role_docker_state`"

            ```yaml
            # Type: string
            mongodb_role_docker_state: started
            ```

        ##### User

        ??? variable string "`mongodb_role_docker_user`"

            ```yaml
            # Type: string
            mongodb_role_docker_user: "{{ uid }}:{{ gid }}"
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`mongodb2_docker_container`"

            ```yaml
            # Type: string
            mongodb2_docker_container: "{{ mongodb_name }}"
            ```

        ##### Image

        ??? variable bool "`mongodb2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            mongodb2_docker_image_pull: true
            ```

        ??? variable string "`mongodb2_docker_image_repo`"

            ```yaml
            # Type: string
            mongodb2_docker_image_repo: "mongo"
            ```

        ??? variable string "`mongodb2_docker_image_tag`"

            ```yaml
            # Type: string
            mongodb2_docker_image_tag: "6"
            ```

        ??? variable string "`mongodb2_docker_image`"

            ```yaml
            # Type: string
            mongodb2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='mongodb') }}:{{ lookup('role_var', '_docker_image_tag', role='mongodb') }}"
            ```

        ##### Envs

        ??? variable dict "`mongodb2_docker_envs_default`"

            ```yaml
            # Type: dict
            mongodb2_docker_envs_default: 
              MONGO_DATA_DIR: "/data/db"
              MONGO_LOG_DIR: "/dev/null"
              MONGO_URL: "mongodb://{{ mongodb_name }}:27017/"
            ```

        ??? variable dict "`mongodb2_docker_envs_custom`"

            ```yaml
            # Type: dict
            mongodb2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`mongodb2_docker_volumes_default`"

            ```yaml
            # Type: list
            mongodb2_docker_volumes_default: 
              - "{{ mongodb_role_paths_location }}:/data/db:rw"
              - "{{ mongodb_role_paths_location }}/config:/data/configdb"
            ```

        ??? variable list "`mongodb2_docker_volumes_custom`"

            ```yaml
            # Type: list
            mongodb2_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`mongodb2_docker_hostname`"

            ```yaml
            # Type: string
            mongodb2_docker_hostname: "{{ mongodb_name }}"
            ```

        ##### Networks

        ??? variable string "`mongodb2_docker_networks_alias`"

            ```yaml
            # Type: string
            mongodb2_docker_networks_alias: "{{ mongodb_name }}"
            ```

        ??? variable list "`mongodb2_docker_networks_default`"

            ```yaml
            # Type: list
            mongodb2_docker_networks_default: []
            ```

        ??? variable list "`mongodb2_docker_networks_custom`"

            ```yaml
            # Type: list
            mongodb2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`mongodb2_docker_restart_policy`"

            ```yaml
            # Type: string
            mongodb2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`mongodb2_docker_state`"

            ```yaml
            # Type: string
            mongodb2_docker_state: started
            ```

        ##### User

        ??? variable string "`mongodb2_docker_user`"

            ```yaml
            # Type: string
            mongodb2_docker_user: "{{ uid }}:{{ gid }}"
            ```

=== "Docker+"

    #### Additional Docker Options

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    === "Role-level"

        ##### Resource Limits

        ??? variable int "`mongodb_role_docker_blkio_weight`"

            ```yaml
            # Type: int
            mongodb_role_docker_blkio_weight:
            ```

        ??? variable int "`mongodb_role_docker_cpu_period`"

            ```yaml
            # Type: int
            mongodb_role_docker_cpu_period:
            ```

        ??? variable int "`mongodb_role_docker_cpu_quota`"

            ```yaml
            # Type: int
            mongodb_role_docker_cpu_quota:
            ```

        ??? variable int "`mongodb_role_docker_cpu_shares`"

            ```yaml
            # Type: int
            mongodb_role_docker_cpu_shares:
            ```

        ??? variable string "`mongodb_role_docker_cpus`"

            ```yaml
            # Type: string
            mongodb_role_docker_cpus:
            ```

        ??? variable string "`mongodb_role_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            mongodb_role_docker_cpuset_cpus:
            ```

        ??? variable string "`mongodb_role_docker_cpuset_mems`"

            ```yaml
            # Type: string
            mongodb_role_docker_cpuset_mems:
            ```

        ??? variable string "`mongodb_role_docker_kernel_memory`"

            ```yaml
            # Type: string
            mongodb_role_docker_kernel_memory:
            ```

        ??? variable string "`mongodb_role_docker_memory`"

            ```yaml
            # Type: string
            mongodb_role_docker_memory:
            ```

        ??? variable string "`mongodb_role_docker_memory_reservation`"

            ```yaml
            # Type: string
            mongodb_role_docker_memory_reservation:
            ```

        ??? variable string "`mongodb_role_docker_memory_swap`"

            ```yaml
            # Type: string
            mongodb_role_docker_memory_swap:
            ```

        ??? variable int "`mongodb_role_docker_memory_swappiness`"

            ```yaml
            # Type: int
            mongodb_role_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`mongodb_role_docker_cap_drop`"

            ```yaml
            # Type: list
            mongodb_role_docker_cap_drop:
            ```

        ??? variable list "`mongodb_role_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            mongodb_role_docker_device_cgroup_rules:
            ```

        ??? variable list "`mongodb_role_docker_device_read_bps`"

            ```yaml
            # Type: list
            mongodb_role_docker_device_read_bps:
            ```

        ??? variable list "`mongodb_role_docker_device_read_iops`"

            ```yaml
            # Type: list
            mongodb_role_docker_device_read_iops:
            ```

        ??? variable list "`mongodb_role_docker_device_requests`"

            ```yaml
            # Type: list
            mongodb_role_docker_device_requests:
            ```

        ??? variable list "`mongodb_role_docker_device_write_bps`"

            ```yaml
            # Type: list
            mongodb_role_docker_device_write_bps:
            ```

        ??? variable list "`mongodb_role_docker_device_write_iops`"

            ```yaml
            # Type: list
            mongodb_role_docker_device_write_iops:
            ```

        ??? variable list "`mongodb_role_docker_devices`"

            ```yaml
            # Type: list
            mongodb_role_docker_devices:
            ```

        ??? variable string "`mongodb_role_docker_devices_default`"

            ```yaml
            # Type: string
            mongodb_role_docker_devices_default:
            ```

        ??? variable bool "`mongodb_role_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            mongodb_role_docker_privileged:
            ```

        ??? variable list "`mongodb_role_docker_security_opts`"

            ```yaml
            # Type: list
            mongodb_role_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`mongodb_role_docker_dns_opts`"

            ```yaml
            # Type: list
            mongodb_role_docker_dns_opts:
            ```

        ??? variable list "`mongodb_role_docker_dns_search_domains`"

            ```yaml
            # Type: list
            mongodb_role_docker_dns_search_domains:
            ```

        ??? variable list "`mongodb_role_docker_dns_servers`"

            ```yaml
            # Type: list
            mongodb_role_docker_dns_servers:
            ```

        ??? variable dict "`mongodb_role_docker_hosts`"

            ```yaml
            # Type: dict
            mongodb_role_docker_hosts:
            ```

        ??? variable string "`mongodb_role_docker_hosts_use_common`"

            ```yaml
            # Type: string
            mongodb_role_docker_hosts_use_common:
            ```

        ??? variable string "`mongodb_role_docker_network_mode`"

            ```yaml
            # Type: string
            mongodb_role_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`mongodb_role_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            mongodb_role_docker_keep_volumes:
            ```

        ??? variable list "`mongodb_role_docker_mounts`"

            ```yaml
            # Type: list
            mongodb_role_docker_mounts:
            ```

        ??? variable string "`mongodb_role_docker_volume_driver`"

            ```yaml
            # Type: string
            mongodb_role_docker_volume_driver:
            ```

        ??? variable list "`mongodb_role_docker_volumes_from`"

            ```yaml
            # Type: list
            mongodb_role_docker_volumes_from:
            ```

        ??? variable string "`mongodb_role_docker_volumes_global`"

            ```yaml
            # Type: string
            mongodb_role_docker_volumes_global:
            ```

        ??? variable string "`mongodb_role_docker_working_dir`"

            ```yaml
            # Type: string
            mongodb_role_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`mongodb_role_docker_healthcheck`"

            ```yaml
            # Type: dict
            mongodb_role_docker_healthcheck:
            ```

        ??? variable bool "`mongodb_role_docker_init`"

            ```yaml
            # Type: bool (true/false)
            mongodb_role_docker_init:
            ```

        ??? variable string "`mongodb_role_docker_log_driver`"

            ```yaml
            # Type: string
            mongodb_role_docker_log_driver:
            ```

        ??? variable dict "`mongodb_role_docker_log_options`"

            ```yaml
            # Type: dict
            mongodb_role_docker_log_options:
            ```

        ??? variable bool "`mongodb_role_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            mongodb_role_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`mongodb_role_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            mongodb_role_docker_auto_remove:
            ```

        ??? variable list "`mongodb_role_docker_capabilities`"

            ```yaml
            # Type: list
            mongodb_role_docker_capabilities:
            ```

        ??? variable string "`mongodb_role_docker_cgroup_parent`"

            ```yaml
            # Type: string
            mongodb_role_docker_cgroup_parent:
            ```

        ??? variable string "`mongodb_role_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            mongodb_role_docker_cgroupns_mode:
            ```

        ??? variable bool "`mongodb_role_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            mongodb_role_docker_cleanup:
            ```

        ??? variable list "`mongodb_role_docker_commands`"

            ```yaml
            # Type: list
            mongodb_role_docker_commands:
            ```

        ??? variable string "`mongodb_role_docker_create_timeout`"

            ```yaml
            # Type: string
            mongodb_role_docker_create_timeout:
            ```

        ??? variable string "`mongodb_role_docker_domainname`"

            ```yaml
            # Type: string
            mongodb_role_docker_domainname:
            ```

        ??? variable string "`mongodb_role_docker_entrypoint`"

            ```yaml
            # Type: string
            mongodb_role_docker_entrypoint:
            ```

        ??? variable string "`mongodb_role_docker_env_file`"

            ```yaml
            # Type: string
            mongodb_role_docker_env_file:
            ```

        ??? variable list "`mongodb_role_docker_exposed_ports`"

            ```yaml
            # Type: list
            mongodb_role_docker_exposed_ports:
            ```

        ??? variable string "`mongodb_role_docker_force_kill`"

            ```yaml
            # Type: string
            mongodb_role_docker_force_kill:
            ```

        ??? variable list "`mongodb_role_docker_groups`"

            ```yaml
            # Type: list
            mongodb_role_docker_groups:
            ```

        ??? variable int "`mongodb_role_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            mongodb_role_docker_healthy_wait_timeout:
            ```

        ??? variable string "`mongodb_role_docker_ipc_mode`"

            ```yaml
            # Type: string
            mongodb_role_docker_ipc_mode:
            ```

        ??? variable string "`mongodb_role_docker_kill_signal`"

            ```yaml
            # Type: string
            mongodb_role_docker_kill_signal:
            ```

        ??? variable dict "`mongodb_role_docker_labels`"

            ```yaml
            # Type: dict
            mongodb_role_docker_labels:
            ```

        ??? variable string "`mongodb_role_docker_labels_use_common`"

            ```yaml
            # Type: string
            mongodb_role_docker_labels_use_common:
            ```

        ??? variable list "`mongodb_role_docker_links`"

            ```yaml
            # Type: list
            mongodb_role_docker_links:
            ```

        ??? variable bool "`mongodb_role_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            mongodb_role_docker_oom_killer:
            ```

        ??? variable int "`mongodb_role_docker_oom_score_adj`"

            ```yaml
            # Type: int
            mongodb_role_docker_oom_score_adj:
            ```

        ??? variable bool "`mongodb_role_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            mongodb_role_docker_paused:
            ```

        ??? variable string "`mongodb_role_docker_pid_mode`"

            ```yaml
            # Type: string
            mongodb_role_docker_pid_mode:
            ```

        ??? variable list "`mongodb_role_docker_ports`"

            ```yaml
            # Type: list
            mongodb_role_docker_ports:
            ```

        ??? variable bool "`mongodb_role_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            mongodb_role_docker_read_only:
            ```

        ??? variable bool "`mongodb_role_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            mongodb_role_docker_recreate:
            ```

        ??? variable int "`mongodb_role_docker_restart_retries`"

            ```yaml
            # Type: int
            mongodb_role_docker_restart_retries:
            ```

        ??? variable string "`mongodb_role_docker_runtime`"

            ```yaml
            # Type: string
            mongodb_role_docker_runtime:
            ```

        ??? variable string "`mongodb_role_docker_shm_size`"

            ```yaml
            # Type: string
            mongodb_role_docker_shm_size:
            ```

        ??? variable int "`mongodb_role_docker_stop_timeout`"

            ```yaml
            # Type: int
            mongodb_role_docker_stop_timeout:
            ```

        ??? variable dict "`mongodb_role_docker_storage_opts`"

            ```yaml
            # Type: dict
            mongodb_role_docker_storage_opts:
            ```

        ??? variable list "`mongodb_role_docker_sysctls`"

            ```yaml
            # Type: list
            mongodb_role_docker_sysctls:
            ```

        ??? variable list "`mongodb_role_docker_tmpfs`"

            ```yaml
            # Type: list
            mongodb_role_docker_tmpfs:
            ```

        ??? variable list "`mongodb_role_docker_ulimits`"

            ```yaml
            # Type: list
            mongodb_role_docker_ulimits:
            ```

        ??? variable string "`mongodb_role_docker_userns_mode`"

            ```yaml
            # Type: string
            mongodb_role_docker_userns_mode:
            ```

        ??? variable string "`mongodb_role_docker_uts`"

            ```yaml
            # Type: string
            mongodb_role_docker_uts:
            ```

    === "Instance-level"

        ##### Resource Limits

        ??? variable int "`mongodb2_docker_blkio_weight`"

            ```yaml
            # Type: int
            mongodb2_docker_blkio_weight:
            ```

        ??? variable int "`mongodb2_docker_cpu_period`"

            ```yaml
            # Type: int
            mongodb2_docker_cpu_period:
            ```

        ??? variable int "`mongodb2_docker_cpu_quota`"

            ```yaml
            # Type: int
            mongodb2_docker_cpu_quota:
            ```

        ??? variable int "`mongodb2_docker_cpu_shares`"

            ```yaml
            # Type: int
            mongodb2_docker_cpu_shares:
            ```

        ??? variable string "`mongodb2_docker_cpus`"

            ```yaml
            # Type: string
            mongodb2_docker_cpus:
            ```

        ??? variable string "`mongodb2_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            mongodb2_docker_cpuset_cpus:
            ```

        ??? variable string "`mongodb2_docker_cpuset_mems`"

            ```yaml
            # Type: string
            mongodb2_docker_cpuset_mems:
            ```

        ??? variable string "`mongodb2_docker_kernel_memory`"

            ```yaml
            # Type: string
            mongodb2_docker_kernel_memory:
            ```

        ??? variable string "`mongodb2_docker_memory`"

            ```yaml
            # Type: string
            mongodb2_docker_memory:
            ```

        ??? variable string "`mongodb2_docker_memory_reservation`"

            ```yaml
            # Type: string
            mongodb2_docker_memory_reservation:
            ```

        ??? variable string "`mongodb2_docker_memory_swap`"

            ```yaml
            # Type: string
            mongodb2_docker_memory_swap:
            ```

        ??? variable int "`mongodb2_docker_memory_swappiness`"

            ```yaml
            # Type: int
            mongodb2_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`mongodb2_docker_cap_drop`"

            ```yaml
            # Type: list
            mongodb2_docker_cap_drop:
            ```

        ??? variable list "`mongodb2_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            mongodb2_docker_device_cgroup_rules:
            ```

        ??? variable list "`mongodb2_docker_device_read_bps`"

            ```yaml
            # Type: list
            mongodb2_docker_device_read_bps:
            ```

        ??? variable list "`mongodb2_docker_device_read_iops`"

            ```yaml
            # Type: list
            mongodb2_docker_device_read_iops:
            ```

        ??? variable list "`mongodb2_docker_device_requests`"

            ```yaml
            # Type: list
            mongodb2_docker_device_requests:
            ```

        ??? variable list "`mongodb2_docker_device_write_bps`"

            ```yaml
            # Type: list
            mongodb2_docker_device_write_bps:
            ```

        ??? variable list "`mongodb2_docker_device_write_iops`"

            ```yaml
            # Type: list
            mongodb2_docker_device_write_iops:
            ```

        ??? variable list "`mongodb2_docker_devices`"

            ```yaml
            # Type: list
            mongodb2_docker_devices:
            ```

        ??? variable string "`mongodb2_docker_devices_default`"

            ```yaml
            # Type: string
            mongodb2_docker_devices_default:
            ```

        ??? variable bool "`mongodb2_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            mongodb2_docker_privileged:
            ```

        ??? variable list "`mongodb2_docker_security_opts`"

            ```yaml
            # Type: list
            mongodb2_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`mongodb2_docker_dns_opts`"

            ```yaml
            # Type: list
            mongodb2_docker_dns_opts:
            ```

        ??? variable list "`mongodb2_docker_dns_search_domains`"

            ```yaml
            # Type: list
            mongodb2_docker_dns_search_domains:
            ```

        ??? variable list "`mongodb2_docker_dns_servers`"

            ```yaml
            # Type: list
            mongodb2_docker_dns_servers:
            ```

        ??? variable dict "`mongodb2_docker_hosts`"

            ```yaml
            # Type: dict
            mongodb2_docker_hosts:
            ```

        ??? variable string "`mongodb2_docker_hosts_use_common`"

            ```yaml
            # Type: string
            mongodb2_docker_hosts_use_common:
            ```

        ??? variable string "`mongodb2_docker_network_mode`"

            ```yaml
            # Type: string
            mongodb2_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`mongodb2_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            mongodb2_docker_keep_volumes:
            ```

        ??? variable list "`mongodb2_docker_mounts`"

            ```yaml
            # Type: list
            mongodb2_docker_mounts:
            ```

        ??? variable string "`mongodb2_docker_volume_driver`"

            ```yaml
            # Type: string
            mongodb2_docker_volume_driver:
            ```

        ??? variable list "`mongodb2_docker_volumes_from`"

            ```yaml
            # Type: list
            mongodb2_docker_volumes_from:
            ```

        ??? variable string "`mongodb2_docker_volumes_global`"

            ```yaml
            # Type: string
            mongodb2_docker_volumes_global:
            ```

        ??? variable string "`mongodb2_docker_working_dir`"

            ```yaml
            # Type: string
            mongodb2_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`mongodb2_docker_healthcheck`"

            ```yaml
            # Type: dict
            mongodb2_docker_healthcheck:
            ```

        ??? variable bool "`mongodb2_docker_init`"

            ```yaml
            # Type: bool (true/false)
            mongodb2_docker_init:
            ```

        ??? variable string "`mongodb2_docker_log_driver`"

            ```yaml
            # Type: string
            mongodb2_docker_log_driver:
            ```

        ??? variable dict "`mongodb2_docker_log_options`"

            ```yaml
            # Type: dict
            mongodb2_docker_log_options:
            ```

        ??? variable bool "`mongodb2_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            mongodb2_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`mongodb2_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            mongodb2_docker_auto_remove:
            ```

        ??? variable list "`mongodb2_docker_capabilities`"

            ```yaml
            # Type: list
            mongodb2_docker_capabilities:
            ```

        ??? variable string "`mongodb2_docker_cgroup_parent`"

            ```yaml
            # Type: string
            mongodb2_docker_cgroup_parent:
            ```

        ??? variable string "`mongodb2_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            mongodb2_docker_cgroupns_mode:
            ```

        ??? variable bool "`mongodb2_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            mongodb2_docker_cleanup:
            ```

        ??? variable list "`mongodb2_docker_commands`"

            ```yaml
            # Type: list
            mongodb2_docker_commands:
            ```

        ??? variable string "`mongodb2_docker_create_timeout`"

            ```yaml
            # Type: string
            mongodb2_docker_create_timeout:
            ```

        ??? variable string "`mongodb2_docker_domainname`"

            ```yaml
            # Type: string
            mongodb2_docker_domainname:
            ```

        ??? variable string "`mongodb2_docker_entrypoint`"

            ```yaml
            # Type: string
            mongodb2_docker_entrypoint:
            ```

        ??? variable string "`mongodb2_docker_env_file`"

            ```yaml
            # Type: string
            mongodb2_docker_env_file:
            ```

        ??? variable list "`mongodb2_docker_exposed_ports`"

            ```yaml
            # Type: list
            mongodb2_docker_exposed_ports:
            ```

        ??? variable string "`mongodb2_docker_force_kill`"

            ```yaml
            # Type: string
            mongodb2_docker_force_kill:
            ```

        ??? variable list "`mongodb2_docker_groups`"

            ```yaml
            # Type: list
            mongodb2_docker_groups:
            ```

        ??? variable int "`mongodb2_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            mongodb2_docker_healthy_wait_timeout:
            ```

        ??? variable string "`mongodb2_docker_ipc_mode`"

            ```yaml
            # Type: string
            mongodb2_docker_ipc_mode:
            ```

        ??? variable string "`mongodb2_docker_kill_signal`"

            ```yaml
            # Type: string
            mongodb2_docker_kill_signal:
            ```

        ??? variable dict "`mongodb2_docker_labels`"

            ```yaml
            # Type: dict
            mongodb2_docker_labels:
            ```

        ??? variable string "`mongodb2_docker_labels_use_common`"

            ```yaml
            # Type: string
            mongodb2_docker_labels_use_common:
            ```

        ??? variable list "`mongodb2_docker_links`"

            ```yaml
            # Type: list
            mongodb2_docker_links:
            ```

        ??? variable bool "`mongodb2_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            mongodb2_docker_oom_killer:
            ```

        ??? variable int "`mongodb2_docker_oom_score_adj`"

            ```yaml
            # Type: int
            mongodb2_docker_oom_score_adj:
            ```

        ??? variable bool "`mongodb2_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            mongodb2_docker_paused:
            ```

        ??? variable string "`mongodb2_docker_pid_mode`"

            ```yaml
            # Type: string
            mongodb2_docker_pid_mode:
            ```

        ??? variable list "`mongodb2_docker_ports`"

            ```yaml
            # Type: list
            mongodb2_docker_ports:
            ```

        ??? variable bool "`mongodb2_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            mongodb2_docker_read_only:
            ```

        ??? variable bool "`mongodb2_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            mongodb2_docker_recreate:
            ```

        ??? variable int "`mongodb2_docker_restart_retries`"

            ```yaml
            # Type: int
            mongodb2_docker_restart_retries:
            ```

        ??? variable string "`mongodb2_docker_runtime`"

            ```yaml
            # Type: string
            mongodb2_docker_runtime:
            ```

        ??? variable string "`mongodb2_docker_shm_size`"

            ```yaml
            # Type: string
            mongodb2_docker_shm_size:
            ```

        ??? variable int "`mongodb2_docker_stop_timeout`"

            ```yaml
            # Type: int
            mongodb2_docker_stop_timeout:
            ```

        ??? variable dict "`mongodb2_docker_storage_opts`"

            ```yaml
            # Type: dict
            mongodb2_docker_storage_opts:
            ```

        ??? variable list "`mongodb2_docker_sysctls`"

            ```yaml
            # Type: list
            mongodb2_docker_sysctls:
            ```

        ??? variable list "`mongodb2_docker_tmpfs`"

            ```yaml
            # Type: list
            mongodb2_docker_tmpfs:
            ```

        ??? variable list "`mongodb2_docker_ulimits`"

            ```yaml
            # Type: list
            mongodb2_docker_ulimits:
            ```

        ??? variable string "`mongodb2_docker_userns_mode`"

            ```yaml
            # Type: string
            mongodb2_docker_userns_mode:
            ```

        ??? variable string "`mongodb2_docker_uts`"

            ```yaml
            # Type: string
            mongodb2_docker_uts:
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`mongodb_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            mongodb_role_autoheal_enabled: true
            ```

        ??? variable string "`mongodb_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            mongodb_role_depends_on: ""
            ```

        ??? variable string "`mongodb_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            mongodb_role_depends_on_delay: "0"
            ```

        ??? variable string "`mongodb_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            mongodb_role_depends_on_healthchecks:
            ```

        ??? variable bool "`mongodb_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            mongodb_role_diun_enabled: true
            ```

        ??? variable bool "`mongodb_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            mongodb_role_dns_enabled: true
            ```

        ??? variable bool "`mongodb_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            mongodb_role_docker_controller: true
            ```

        ??? variable bool "`mongodb_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            mongodb_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`mongodb_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            mongodb_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`mongodb_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            mongodb_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`mongodb_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            mongodb_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`mongodb_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            mongodb_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`mongodb_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            mongodb_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`mongodb_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            mongodb_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`mongodb_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            mongodb_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                mongodb_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "mongodb2.{{ user.domain }}"
                  - "mongodb.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`mongodb_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            mongodb_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                mongodb_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'mongodb2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`mongodb_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            mongodb_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `mongodb2`):

        ??? variable bool "`mongodb2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            mongodb2_autoheal_enabled: true
            ```

        ??? variable string "`mongodb2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            mongodb2_depends_on: ""
            ```

        ??? variable string "`mongodb2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            mongodb2_depends_on_delay: "0"
            ```

        ??? variable string "`mongodb2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            mongodb2_depends_on_healthchecks:
            ```

        ??? variable bool "`mongodb2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            mongodb2_diun_enabled: true
            ```

        ??? variable bool "`mongodb2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            mongodb2_dns_enabled: true
            ```

        ??? variable bool "`mongodb2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            mongodb2_docker_controller: true
            ```

        ??? variable bool "`mongodb2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            mongodb2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`mongodb2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            mongodb2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`mongodb2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            mongodb2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`mongodb2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            mongodb2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`mongodb2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            mongodb2_traefik_robot_enabled: true
            ```

        ??? variable bool "`mongodb2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            mongodb2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`mongodb2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            mongodb2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`mongodb2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            mongodb2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                mongodb2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "mongodb2.{{ user.domain }}"
                  - "mongodb.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`mongodb2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            mongodb2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                mongodb2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'mongodb2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`mongodb2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            mongodb2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
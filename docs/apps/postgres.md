---
hide:
  - tags
tags:
  - postgres
---

# Postgres

## What is it?

[Postgres](https://www.postgresql.org/) PostgreSQL, often simply "Postgres", is an object-relational database management system (ORDBMS) with an emphasis on extensibility and standards-compliance.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.postgresql.org/){: .header-icons } | [:octicons-link-16: Docs](https://www.postgresql.org/docs/12/index.html){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/postgres/postgres/tree/REL_12_STABLE){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/postgres){: .header-icons }|

### 1. Installation

``` shell

sb install postgres

```

### 2. Setup

!!! info
    The default password for this container is `password4321`
    To easily manage the db, consider [adminer](../sandbox/apps/adminer.md)

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `postgres_instances`.

    === "Role-level Override"

        Applies to all instances of postgres:

        ```yaml
        postgres_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `postgres2`):

        ```yaml
        postgres2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `postgres_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `postgres_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`postgres_instances`"

        ```yaml
        # Type: list
        postgres_instances: ["postgres"]
        ```

        !!! example

            ```yaml
            # Type: list
            postgres_instances: ["postgres", "postgres2"]
            ```

=== "Settings"

    === "Role-level"

        ??? variable string "`postgres_role_docker_env_password`"

            ```yaml
            # Type: string
            postgres_role_docker_env_password: "password4321"
            ```

        ??? variable string "`postgres_role_docker_env_user`"

            ```yaml
            # Type: string
            postgres_role_docker_env_user: "{{ user.name }}"
            ```

        ??? variable string "`postgres_role_docker_env_db`"

            ```yaml
            # Type: string
            postgres_role_docker_env_db: "saltbox"
            ```

    === "Instance-level"

        ??? variable string "`postgres2_docker_env_password`"

            ```yaml
            # Type: string
            postgres2_docker_env_password: "password4321"
            ```

        ??? variable string "`postgres2_docker_env_user`"

            ```yaml
            # Type: string
            postgres2_docker_env_user: "{{ user.name }}"
            ```

        ??? variable string "`postgres2_docker_env_db`"

            ```yaml
            # Type: string
            postgres2_docker_env_db: "saltbox"
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`postgres_role_paths_folder`"

            ```yaml
            # Type: string
            postgres_role_paths_folder: "{{ postgres_name }}"
            ```

        ??? variable string "`postgres_role_paths_location`"

            ```yaml
            # Type: string
            postgres_role_paths_location: "{{ server_appdata_path }}/{{ postgres_role_paths_folder }}"
            ```

    === "Instance-level"

        ??? variable string "`postgres2_paths_folder`"

            ```yaml
            # Type: string
            postgres2_paths_folder: "{{ postgres_name }}"
            ```

        ??? variable string "`postgres2_paths_location`"

            ```yaml
            # Type: string
            postgres2_paths_location: "{{ server_appdata_path }}/{{ postgres_role_paths_folder }}"
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`postgres_role_docker_container`"

            ```yaml
            # Type: string
            postgres_role_docker_container: "{{ postgres_name }}"
            ```

        ##### Image

        ??? variable bool "`postgres_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            postgres_role_docker_image_pull: true
            ```

        ??? variable string "`postgres_role_docker_image_tag`"

            ```yaml
            # Type: string
            postgres_role_docker_image_tag: "17-alpine"
            ```

        ??? variable string "`postgres_role_docker_image_repo`"

            ```yaml
            # Type: string
            postgres_role_docker_image_repo: "postgres"
            ```

        ??? variable string "`postgres_role_docker_image`"

            ```yaml
            # Type: string
            postgres_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='postgres') }}:{{ lookup('role_var', '_docker_image_tag', role='postgres') }}"
            ```

        ##### Envs

        ??? variable dict "`postgres_role_docker_envs_default`"

            ```yaml
            # Type: dict
            postgres_role_docker_envs_default: 
              TZ: "{{ tz }}"
              PGDATA: "/data"
              POSTGRES_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='postgres') }}"
              POSTGRES_USER: "{{ lookup('role_var', '_docker_env_user', role='postgres') }}"
              POSTGRES_DB: "{{ lookup('role_var', '_docker_env_db', role='postgres') }}"
            ```

        ??? variable dict "`postgres_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            postgres_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`postgres_role_docker_volumes_default`"

            ```yaml
            # Type: list
            postgres_role_docker_volumes_default: 
              - "{{ postgres_role_paths_location }}:/data"
              - "/etc/passwd:/etc/passwd:ro"
            ```

        ??? variable list "`postgres_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            postgres_role_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`postgres_role_docker_hostname`"

            ```yaml
            # Type: string
            postgres_role_docker_hostname: "{{ postgres_name }}"
            ```

        ##### Networks

        ??? variable string "`postgres_role_docker_networks_alias`"

            ```yaml
            # Type: string
            postgres_role_docker_networks_alias: "{{ postgres_name }}"
            ```

        ??? variable list "`postgres_role_docker_networks_default`"

            ```yaml
            # Type: list
            postgres_role_docker_networks_default: []
            ```

        ??? variable list "`postgres_role_docker_networks_custom`"

            ```yaml
            # Type: list
            postgres_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`postgres_role_docker_restart_policy`"

            ```yaml
            # Type: string
            postgres_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`postgres_role_docker_state`"

            ```yaml
            # Type: string
            postgres_role_docker_state: started
            ```

        ##### User

        ??? variable string "`postgres_role_docker_user`"

            ```yaml
            # Type: string
            postgres_role_docker_user: "{{ uid }}:{{ gid }}"
            ```

        ##### SHM size

        ??? variable string "`postgres_role_docker_shm_size`"

            ```yaml
            # Type: string
            postgres_role_docker_shm_size: "128M"
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`postgres2_docker_container`"

            ```yaml
            # Type: string
            postgres2_docker_container: "{{ postgres_name }}"
            ```

        ##### Image

        ??? variable bool "`postgres2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            postgres2_docker_image_pull: true
            ```

        ??? variable string "`postgres2_docker_image_tag`"

            ```yaml
            # Type: string
            postgres2_docker_image_tag: "17-alpine"
            ```

        ??? variable string "`postgres2_docker_image_repo`"

            ```yaml
            # Type: string
            postgres2_docker_image_repo: "postgres"
            ```

        ??? variable string "`postgres2_docker_image`"

            ```yaml
            # Type: string
            postgres2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='postgres') }}:{{ lookup('role_var', '_docker_image_tag', role='postgres') }}"
            ```

        ##### Envs

        ??? variable dict "`postgres2_docker_envs_default`"

            ```yaml
            # Type: dict
            postgres2_docker_envs_default: 
              TZ: "{{ tz }}"
              PGDATA: "/data"
              POSTGRES_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='postgres') }}"
              POSTGRES_USER: "{{ lookup('role_var', '_docker_env_user', role='postgres') }}"
              POSTGRES_DB: "{{ lookup('role_var', '_docker_env_db', role='postgres') }}"
            ```

        ??? variable dict "`postgres2_docker_envs_custom`"

            ```yaml
            # Type: dict
            postgres2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`postgres2_docker_volumes_default`"

            ```yaml
            # Type: list
            postgres2_docker_volumes_default: 
              - "{{ postgres_role_paths_location }}:/data"
              - "/etc/passwd:/etc/passwd:ro"
            ```

        ??? variable list "`postgres2_docker_volumes_custom`"

            ```yaml
            # Type: list
            postgres2_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`postgres2_docker_hostname`"

            ```yaml
            # Type: string
            postgres2_docker_hostname: "{{ postgres_name }}"
            ```

        ##### Networks

        ??? variable string "`postgres2_docker_networks_alias`"

            ```yaml
            # Type: string
            postgres2_docker_networks_alias: "{{ postgres_name }}"
            ```

        ??? variable list "`postgres2_docker_networks_default`"

            ```yaml
            # Type: list
            postgres2_docker_networks_default: []
            ```

        ??? variable list "`postgres2_docker_networks_custom`"

            ```yaml
            # Type: list
            postgres2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`postgres2_docker_restart_policy`"

            ```yaml
            # Type: string
            postgres2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`postgres2_docker_state`"

            ```yaml
            # Type: string
            postgres2_docker_state: started
            ```

        ##### User

        ??? variable string "`postgres2_docker_user`"

            ```yaml
            # Type: string
            postgres2_docker_user: "{{ uid }}:{{ gid }}"
            ```

        ##### SHM size

        ??? variable string "`postgres2_docker_shm_size`"

            ```yaml
            # Type: string
            postgres2_docker_shm_size: "128M"
            ```

=== "Docker+"

    #### Additional Docker Options

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    === "Role-level"

        ##### Resource Limits

        ??? variable int "`postgres_role_docker_blkio_weight`"

            ```yaml
            # Type: int
            postgres_role_docker_blkio_weight:
            ```

        ??? variable int "`postgres_role_docker_cpu_period`"

            ```yaml
            # Type: int
            postgres_role_docker_cpu_period:
            ```

        ??? variable int "`postgres_role_docker_cpu_quota`"

            ```yaml
            # Type: int
            postgres_role_docker_cpu_quota:
            ```

        ??? variable int "`postgres_role_docker_cpu_shares`"

            ```yaml
            # Type: int
            postgres_role_docker_cpu_shares:
            ```

        ??? variable string "`postgres_role_docker_cpus`"

            ```yaml
            # Type: string
            postgres_role_docker_cpus:
            ```

        ??? variable string "`postgres_role_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            postgres_role_docker_cpuset_cpus:
            ```

        ??? variable string "`postgres_role_docker_cpuset_mems`"

            ```yaml
            # Type: string
            postgres_role_docker_cpuset_mems:
            ```

        ??? variable string "`postgres_role_docker_kernel_memory`"

            ```yaml
            # Type: string
            postgres_role_docker_kernel_memory:
            ```

        ??? variable string "`postgres_role_docker_memory`"

            ```yaml
            # Type: string
            postgres_role_docker_memory:
            ```

        ??? variable string "`postgres_role_docker_memory_reservation`"

            ```yaml
            # Type: string
            postgres_role_docker_memory_reservation:
            ```

        ??? variable string "`postgres_role_docker_memory_swap`"

            ```yaml
            # Type: string
            postgres_role_docker_memory_swap:
            ```

        ??? variable int "`postgres_role_docker_memory_swappiness`"

            ```yaml
            # Type: int
            postgres_role_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`postgres_role_docker_cap_drop`"

            ```yaml
            # Type: list
            postgres_role_docker_cap_drop:
            ```

        ??? variable list "`postgres_role_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            postgres_role_docker_device_cgroup_rules:
            ```

        ??? variable list "`postgres_role_docker_device_read_bps`"

            ```yaml
            # Type: list
            postgres_role_docker_device_read_bps:
            ```

        ??? variable list "`postgres_role_docker_device_read_iops`"

            ```yaml
            # Type: list
            postgres_role_docker_device_read_iops:
            ```

        ??? variable list "`postgres_role_docker_device_requests`"

            ```yaml
            # Type: list
            postgres_role_docker_device_requests:
            ```

        ??? variable list "`postgres_role_docker_device_write_bps`"

            ```yaml
            # Type: list
            postgres_role_docker_device_write_bps:
            ```

        ??? variable list "`postgres_role_docker_device_write_iops`"

            ```yaml
            # Type: list
            postgres_role_docker_device_write_iops:
            ```

        ??? variable list "`postgres_role_docker_devices`"

            ```yaml
            # Type: list
            postgres_role_docker_devices:
            ```

        ??? variable string "`postgres_role_docker_devices_default`"

            ```yaml
            # Type: string
            postgres_role_docker_devices_default:
            ```

        ??? variable bool "`postgres_role_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            postgres_role_docker_privileged:
            ```

        ??? variable list "`postgres_role_docker_security_opts`"

            ```yaml
            # Type: list
            postgres_role_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`postgres_role_docker_dns_opts`"

            ```yaml
            # Type: list
            postgres_role_docker_dns_opts:
            ```

        ??? variable list "`postgres_role_docker_dns_search_domains`"

            ```yaml
            # Type: list
            postgres_role_docker_dns_search_domains:
            ```

        ??? variable list "`postgres_role_docker_dns_servers`"

            ```yaml
            # Type: list
            postgres_role_docker_dns_servers:
            ```

        ??? variable dict "`postgres_role_docker_hosts`"

            ```yaml
            # Type: dict
            postgres_role_docker_hosts:
            ```

        ??? variable string "`postgres_role_docker_hosts_use_common`"

            ```yaml
            # Type: string
            postgres_role_docker_hosts_use_common:
            ```

        ??? variable string "`postgres_role_docker_network_mode`"

            ```yaml
            # Type: string
            postgres_role_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`postgres_role_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            postgres_role_docker_keep_volumes:
            ```

        ??? variable list "`postgres_role_docker_mounts`"

            ```yaml
            # Type: list
            postgres_role_docker_mounts:
            ```

        ??? variable string "`postgres_role_docker_volume_driver`"

            ```yaml
            # Type: string
            postgres_role_docker_volume_driver:
            ```

        ??? variable list "`postgres_role_docker_volumes_from`"

            ```yaml
            # Type: list
            postgres_role_docker_volumes_from:
            ```

        ??? variable string "`postgres_role_docker_volumes_global`"

            ```yaml
            # Type: string
            postgres_role_docker_volumes_global:
            ```

        ??? variable string "`postgres_role_docker_working_dir`"

            ```yaml
            # Type: string
            postgres_role_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`postgres_role_docker_healthcheck`"

            ```yaml
            # Type: dict
            postgres_role_docker_healthcheck:
            ```

        ??? variable bool "`postgres_role_docker_init`"

            ```yaml
            # Type: bool (true/false)
            postgres_role_docker_init:
            ```

        ??? variable string "`postgres_role_docker_log_driver`"

            ```yaml
            # Type: string
            postgres_role_docker_log_driver:
            ```

        ??? variable dict "`postgres_role_docker_log_options`"

            ```yaml
            # Type: dict
            postgres_role_docker_log_options:
            ```

        ??? variable bool "`postgres_role_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            postgres_role_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`postgres_role_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            postgres_role_docker_auto_remove:
            ```

        ??? variable list "`postgres_role_docker_capabilities`"

            ```yaml
            # Type: list
            postgres_role_docker_capabilities:
            ```

        ??? variable string "`postgres_role_docker_cgroup_parent`"

            ```yaml
            # Type: string
            postgres_role_docker_cgroup_parent:
            ```

        ??? variable string "`postgres_role_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            postgres_role_docker_cgroupns_mode:
            ```

        ??? variable bool "`postgres_role_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            postgres_role_docker_cleanup:
            ```

        ??? variable list "`postgres_role_docker_commands`"

            ```yaml
            # Type: list
            postgres_role_docker_commands:
            ```

        ??? variable string "`postgres_role_docker_create_timeout`"

            ```yaml
            # Type: string
            postgres_role_docker_create_timeout:
            ```

        ??? variable string "`postgres_role_docker_domainname`"

            ```yaml
            # Type: string
            postgres_role_docker_domainname:
            ```

        ??? variable string "`postgres_role_docker_entrypoint`"

            ```yaml
            # Type: string
            postgres_role_docker_entrypoint:
            ```

        ??? variable string "`postgres_role_docker_env_file`"

            ```yaml
            # Type: string
            postgres_role_docker_env_file:
            ```

        ??? variable list "`postgres_role_docker_exposed_ports`"

            ```yaml
            # Type: list
            postgres_role_docker_exposed_ports:
            ```

        ??? variable string "`postgres_role_docker_force_kill`"

            ```yaml
            # Type: string
            postgres_role_docker_force_kill:
            ```

        ??? variable list "`postgres_role_docker_groups`"

            ```yaml
            # Type: list
            postgres_role_docker_groups:
            ```

        ??? variable int "`postgres_role_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            postgres_role_docker_healthy_wait_timeout:
            ```

        ??? variable string "`postgres_role_docker_ipc_mode`"

            ```yaml
            # Type: string
            postgres_role_docker_ipc_mode:
            ```

        ??? variable string "`postgres_role_docker_kill_signal`"

            ```yaml
            # Type: string
            postgres_role_docker_kill_signal:
            ```

        ??? variable dict "`postgres_role_docker_labels`"

            ```yaml
            # Type: dict
            postgres_role_docker_labels:
            ```

        ??? variable string "`postgres_role_docker_labels_use_common`"

            ```yaml
            # Type: string
            postgres_role_docker_labels_use_common:
            ```

        ??? variable list "`postgres_role_docker_links`"

            ```yaml
            # Type: list
            postgres_role_docker_links:
            ```

        ??? variable bool "`postgres_role_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            postgres_role_docker_oom_killer:
            ```

        ??? variable int "`postgres_role_docker_oom_score_adj`"

            ```yaml
            # Type: int
            postgres_role_docker_oom_score_adj:
            ```

        ??? variable bool "`postgres_role_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            postgres_role_docker_paused:
            ```

        ??? variable string "`postgres_role_docker_pid_mode`"

            ```yaml
            # Type: string
            postgres_role_docker_pid_mode:
            ```

        ??? variable list "`postgres_role_docker_ports`"

            ```yaml
            # Type: list
            postgres_role_docker_ports:
            ```

        ??? variable bool "`postgres_role_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            postgres_role_docker_read_only:
            ```

        ??? variable bool "`postgres_role_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            postgres_role_docker_recreate:
            ```

        ??? variable int "`postgres_role_docker_restart_retries`"

            ```yaml
            # Type: int
            postgres_role_docker_restart_retries:
            ```

        ??? variable string "`postgres_role_docker_runtime`"

            ```yaml
            # Type: string
            postgres_role_docker_runtime:
            ```

        ??? variable int "`postgres_role_docker_stop_timeout`"

            ```yaml
            # Type: int
            postgres_role_docker_stop_timeout:
            ```

        ??? variable dict "`postgres_role_docker_storage_opts`"

            ```yaml
            # Type: dict
            postgres_role_docker_storage_opts:
            ```

        ??? variable list "`postgres_role_docker_sysctls`"

            ```yaml
            # Type: list
            postgres_role_docker_sysctls:
            ```

        ??? variable list "`postgres_role_docker_tmpfs`"

            ```yaml
            # Type: list
            postgres_role_docker_tmpfs:
            ```

        ??? variable list "`postgres_role_docker_ulimits`"

            ```yaml
            # Type: list
            postgres_role_docker_ulimits:
            ```

        ??? variable string "`postgres_role_docker_userns_mode`"

            ```yaml
            # Type: string
            postgres_role_docker_userns_mode:
            ```

        ??? variable string "`postgres_role_docker_uts`"

            ```yaml
            # Type: string
            postgres_role_docker_uts:
            ```

    === "Instance-level"

        ##### Resource Limits

        ??? variable int "`postgres2_docker_blkio_weight`"

            ```yaml
            # Type: int
            postgres2_docker_blkio_weight:
            ```

        ??? variable int "`postgres2_docker_cpu_period`"

            ```yaml
            # Type: int
            postgres2_docker_cpu_period:
            ```

        ??? variable int "`postgres2_docker_cpu_quota`"

            ```yaml
            # Type: int
            postgres2_docker_cpu_quota:
            ```

        ??? variable int "`postgres2_docker_cpu_shares`"

            ```yaml
            # Type: int
            postgres2_docker_cpu_shares:
            ```

        ??? variable string "`postgres2_docker_cpus`"

            ```yaml
            # Type: string
            postgres2_docker_cpus:
            ```

        ??? variable string "`postgres2_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            postgres2_docker_cpuset_cpus:
            ```

        ??? variable string "`postgres2_docker_cpuset_mems`"

            ```yaml
            # Type: string
            postgres2_docker_cpuset_mems:
            ```

        ??? variable string "`postgres2_docker_kernel_memory`"

            ```yaml
            # Type: string
            postgres2_docker_kernel_memory:
            ```

        ??? variable string "`postgres2_docker_memory`"

            ```yaml
            # Type: string
            postgres2_docker_memory:
            ```

        ??? variable string "`postgres2_docker_memory_reservation`"

            ```yaml
            # Type: string
            postgres2_docker_memory_reservation:
            ```

        ??? variable string "`postgres2_docker_memory_swap`"

            ```yaml
            # Type: string
            postgres2_docker_memory_swap:
            ```

        ??? variable int "`postgres2_docker_memory_swappiness`"

            ```yaml
            # Type: int
            postgres2_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`postgres2_docker_cap_drop`"

            ```yaml
            # Type: list
            postgres2_docker_cap_drop:
            ```

        ??? variable list "`postgres2_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            postgres2_docker_device_cgroup_rules:
            ```

        ??? variable list "`postgres2_docker_device_read_bps`"

            ```yaml
            # Type: list
            postgres2_docker_device_read_bps:
            ```

        ??? variable list "`postgres2_docker_device_read_iops`"

            ```yaml
            # Type: list
            postgres2_docker_device_read_iops:
            ```

        ??? variable list "`postgres2_docker_device_requests`"

            ```yaml
            # Type: list
            postgres2_docker_device_requests:
            ```

        ??? variable list "`postgres2_docker_device_write_bps`"

            ```yaml
            # Type: list
            postgres2_docker_device_write_bps:
            ```

        ??? variable list "`postgres2_docker_device_write_iops`"

            ```yaml
            # Type: list
            postgres2_docker_device_write_iops:
            ```

        ??? variable list "`postgres2_docker_devices`"

            ```yaml
            # Type: list
            postgres2_docker_devices:
            ```

        ??? variable string "`postgres2_docker_devices_default`"

            ```yaml
            # Type: string
            postgres2_docker_devices_default:
            ```

        ??? variable bool "`postgres2_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            postgres2_docker_privileged:
            ```

        ??? variable list "`postgres2_docker_security_opts`"

            ```yaml
            # Type: list
            postgres2_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`postgres2_docker_dns_opts`"

            ```yaml
            # Type: list
            postgres2_docker_dns_opts:
            ```

        ??? variable list "`postgres2_docker_dns_search_domains`"

            ```yaml
            # Type: list
            postgres2_docker_dns_search_domains:
            ```

        ??? variable list "`postgres2_docker_dns_servers`"

            ```yaml
            # Type: list
            postgres2_docker_dns_servers:
            ```

        ??? variable dict "`postgres2_docker_hosts`"

            ```yaml
            # Type: dict
            postgres2_docker_hosts:
            ```

        ??? variable string "`postgres2_docker_hosts_use_common`"

            ```yaml
            # Type: string
            postgres2_docker_hosts_use_common:
            ```

        ??? variable string "`postgres2_docker_network_mode`"

            ```yaml
            # Type: string
            postgres2_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`postgres2_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            postgres2_docker_keep_volumes:
            ```

        ??? variable list "`postgres2_docker_mounts`"

            ```yaml
            # Type: list
            postgres2_docker_mounts:
            ```

        ??? variable string "`postgres2_docker_volume_driver`"

            ```yaml
            # Type: string
            postgres2_docker_volume_driver:
            ```

        ??? variable list "`postgres2_docker_volumes_from`"

            ```yaml
            # Type: list
            postgres2_docker_volumes_from:
            ```

        ??? variable string "`postgres2_docker_volumes_global`"

            ```yaml
            # Type: string
            postgres2_docker_volumes_global:
            ```

        ??? variable string "`postgres2_docker_working_dir`"

            ```yaml
            # Type: string
            postgres2_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`postgres2_docker_healthcheck`"

            ```yaml
            # Type: dict
            postgres2_docker_healthcheck:
            ```

        ??? variable bool "`postgres2_docker_init`"

            ```yaml
            # Type: bool (true/false)
            postgres2_docker_init:
            ```

        ??? variable string "`postgres2_docker_log_driver`"

            ```yaml
            # Type: string
            postgres2_docker_log_driver:
            ```

        ??? variable dict "`postgres2_docker_log_options`"

            ```yaml
            # Type: dict
            postgres2_docker_log_options:
            ```

        ??? variable bool "`postgres2_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            postgres2_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`postgres2_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            postgres2_docker_auto_remove:
            ```

        ??? variable list "`postgres2_docker_capabilities`"

            ```yaml
            # Type: list
            postgres2_docker_capabilities:
            ```

        ??? variable string "`postgres2_docker_cgroup_parent`"

            ```yaml
            # Type: string
            postgres2_docker_cgroup_parent:
            ```

        ??? variable string "`postgres2_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            postgres2_docker_cgroupns_mode:
            ```

        ??? variable bool "`postgres2_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            postgres2_docker_cleanup:
            ```

        ??? variable list "`postgres2_docker_commands`"

            ```yaml
            # Type: list
            postgres2_docker_commands:
            ```

        ??? variable string "`postgres2_docker_create_timeout`"

            ```yaml
            # Type: string
            postgres2_docker_create_timeout:
            ```

        ??? variable string "`postgres2_docker_domainname`"

            ```yaml
            # Type: string
            postgres2_docker_domainname:
            ```

        ??? variable string "`postgres2_docker_entrypoint`"

            ```yaml
            # Type: string
            postgres2_docker_entrypoint:
            ```

        ??? variable string "`postgres2_docker_env_file`"

            ```yaml
            # Type: string
            postgres2_docker_env_file:
            ```

        ??? variable list "`postgres2_docker_exposed_ports`"

            ```yaml
            # Type: list
            postgres2_docker_exposed_ports:
            ```

        ??? variable string "`postgres2_docker_force_kill`"

            ```yaml
            # Type: string
            postgres2_docker_force_kill:
            ```

        ??? variable list "`postgres2_docker_groups`"

            ```yaml
            # Type: list
            postgres2_docker_groups:
            ```

        ??? variable int "`postgres2_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            postgres2_docker_healthy_wait_timeout:
            ```

        ??? variable string "`postgres2_docker_ipc_mode`"

            ```yaml
            # Type: string
            postgres2_docker_ipc_mode:
            ```

        ??? variable string "`postgres2_docker_kill_signal`"

            ```yaml
            # Type: string
            postgres2_docker_kill_signal:
            ```

        ??? variable dict "`postgres2_docker_labels`"

            ```yaml
            # Type: dict
            postgres2_docker_labels:
            ```

        ??? variable string "`postgres2_docker_labels_use_common`"

            ```yaml
            # Type: string
            postgres2_docker_labels_use_common:
            ```

        ??? variable list "`postgres2_docker_links`"

            ```yaml
            # Type: list
            postgres2_docker_links:
            ```

        ??? variable bool "`postgres2_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            postgres2_docker_oom_killer:
            ```

        ??? variable int "`postgres2_docker_oom_score_adj`"

            ```yaml
            # Type: int
            postgres2_docker_oom_score_adj:
            ```

        ??? variable bool "`postgres2_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            postgres2_docker_paused:
            ```

        ??? variable string "`postgres2_docker_pid_mode`"

            ```yaml
            # Type: string
            postgres2_docker_pid_mode:
            ```

        ??? variable list "`postgres2_docker_ports`"

            ```yaml
            # Type: list
            postgres2_docker_ports:
            ```

        ??? variable bool "`postgres2_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            postgres2_docker_read_only:
            ```

        ??? variable bool "`postgres2_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            postgres2_docker_recreate:
            ```

        ??? variable int "`postgres2_docker_restart_retries`"

            ```yaml
            # Type: int
            postgres2_docker_restart_retries:
            ```

        ??? variable string "`postgres2_docker_runtime`"

            ```yaml
            # Type: string
            postgres2_docker_runtime:
            ```

        ??? variable int "`postgres2_docker_stop_timeout`"

            ```yaml
            # Type: int
            postgres2_docker_stop_timeout:
            ```

        ??? variable dict "`postgres2_docker_storage_opts`"

            ```yaml
            # Type: dict
            postgres2_docker_storage_opts:
            ```

        ??? variable list "`postgres2_docker_sysctls`"

            ```yaml
            # Type: list
            postgres2_docker_sysctls:
            ```

        ??? variable list "`postgres2_docker_tmpfs`"

            ```yaml
            # Type: list
            postgres2_docker_tmpfs:
            ```

        ??? variable list "`postgres2_docker_ulimits`"

            ```yaml
            # Type: list
            postgres2_docker_ulimits:
            ```

        ??? variable string "`postgres2_docker_userns_mode`"

            ```yaml
            # Type: string
            postgres2_docker_userns_mode:
            ```

        ??? variable string "`postgres2_docker_uts`"

            ```yaml
            # Type: string
            postgres2_docker_uts:
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`postgres_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            postgres_role_autoheal_enabled: true
            ```

        ??? variable string "`postgres_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            postgres_role_depends_on: ""
            ```

        ??? variable string "`postgres_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            postgres_role_depends_on_delay: "0"
            ```

        ??? variable string "`postgres_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            postgres_role_depends_on_healthchecks:
            ```

        ??? variable bool "`postgres_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            postgres_role_diun_enabled: true
            ```

        ??? variable bool "`postgres_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            postgres_role_dns_enabled: true
            ```

        ??? variable bool "`postgres_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            postgres_role_docker_controller: true
            ```

        ??? variable bool "`postgres_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            postgres_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`postgres_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            postgres_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`postgres_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            postgres_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`postgres_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            postgres_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`postgres_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            postgres_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`postgres_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            postgres_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`postgres_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            postgres_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`postgres_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            postgres_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                postgres_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "postgres2.{{ user.domain }}"
                  - "postgres.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`postgres_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            postgres_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                postgres_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'postgres2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`postgres_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            postgres_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `postgres2`):

        ??? variable bool "`postgres2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            postgres2_autoheal_enabled: true
            ```

        ??? variable string "`postgres2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            postgres2_depends_on: ""
            ```

        ??? variable string "`postgres2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            postgres2_depends_on_delay: "0"
            ```

        ??? variable string "`postgres2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            postgres2_depends_on_healthchecks:
            ```

        ??? variable bool "`postgres2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            postgres2_diun_enabled: true
            ```

        ??? variable bool "`postgres2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            postgres2_dns_enabled: true
            ```

        ??? variable bool "`postgres2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            postgres2_docker_controller: true
            ```

        ??? variable bool "`postgres2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            postgres2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`postgres2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            postgres2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`postgres2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            postgres2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`postgres2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            postgres2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`postgres2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            postgres2_traefik_robot_enabled: true
            ```

        ??? variable bool "`postgres2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            postgres2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`postgres2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            postgres2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`postgres2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            postgres2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                postgres2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "postgres2.{{ user.domain }}"
                  - "postgres.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`postgres2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            postgres2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                postgres2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'postgres2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`postgres2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            postgres2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
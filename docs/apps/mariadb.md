---
hide:
  - tags
tags:
  - mariadb
---

# MariaDB

## What is it?

[MariaDB](https://mariadb.org/) MariaDB Server is one of the most popular open source relational databases. It’s made by the original developers of MySQL and guaranteed to stay open source.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://mariadb.org/){: .header-icons } | [:octicons-link-16: Docs](https://mariadb.org/documentation/#getting-started){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/docker-library/official-images/blob/master/library/mariadb){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/mariadb){: .header-icons }|

### 1. Installation

``` shell

sb install mariadb

```

### 2. Setup

!!! info
    The default password for this container is `password321`
    To easily manage the db, consider [adminer](../sandbox/apps/adminer.md)

### Migration Notes

Saltbox recently swapped Docker images used for MariaDB. The migration path that is run for a default `mariadb` instance is roughly as follows:

1. Dump all data to a dump.sql file
2. Move `/opt/mariadb` to `/opt/mariadb_legacy`
3. Provision a new `mariadb` container
4. Import the dump.sql file

The dump file remains on disk at `/opt/mariadb_legacy/dump.sql` post-migration in the event manual intervention is required and the appdata for the legacy image remains on disk at `/opt/mariadb_legacy`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `mariadb_instances`.

    === "Role-level Override"

        Applies to all instances of mariadb:

        ```yaml
        mariadb_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `mariadb2`):

        ```yaml
        mariadb2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `mariadb_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `mariadb_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`mariadb_instances`"

        ```yaml
        # Type: list
        mariadb_instances: ["mariadb"]
        ```

        !!! example

            ```yaml
            # Type: list
            mariadb_instances: ["mariadb", "mariadb2"]
            ```

=== "Settings"

    === "Role-level"

        ??? variable string "`mariadb_role_docker_env_password`"

            ```yaml
            # Type: string
            mariadb_role_docker_env_password: "password321"
            ```

        ??? variable string "`mariadb_role_docker_env_user`"

            ```yaml
            # Type: string
            mariadb_role_docker_env_user: "{{ user.name }}"
            ```

        ??? variable string "`mariadb_role_docker_env_db`"

            ```yaml
            # Type: string
            mariadb_role_docker_env_db: "saltbox"
            ```

    === "Instance-level"

        ??? variable string "`mariadb2_docker_env_password`"

            ```yaml
            # Type: string
            mariadb2_docker_env_password: "password321"
            ```

        ??? variable string "`mariadb2_docker_env_user`"

            ```yaml
            # Type: string
            mariadb2_docker_env_user: "{{ user.name }}"
            ```

        ??? variable string "`mariadb2_docker_env_db`"

            ```yaml
            # Type: string
            mariadb2_docker_env_db: "saltbox"
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`mariadb_role_paths_folder`"

            ```yaml
            # Type: string
            mariadb_role_paths_folder: "{{ mariadb_name }}"
            ```

        ??? variable string "`mariadb_role_paths_location`"

            ```yaml
            # Type: string
            mariadb_role_paths_location: "{{ server_appdata_path }}/{{ mariadb_role_paths_folder }}"
            ```

    === "Instance-level"

        ??? variable string "`mariadb2_paths_folder`"

            ```yaml
            # Type: string
            mariadb2_paths_folder: "{{ mariadb_name }}"
            ```

        ??? variable string "`mariadb2_paths_location`"

            ```yaml
            # Type: string
            mariadb2_paths_location: "{{ server_appdata_path }}/{{ mariadb_role_paths_folder }}"
            ```

=== "Migration Settings"

    === "Role-level"

        ??? variable string "`mariadb_role_docker_envs_mysql_root_password`"

            ```yaml
            # Type: string
            mariadb_role_docker_envs_mysql_root_password: password321
            ```

        ??? variable string "`mariadb_role_docker_image_migration`"

            ```yaml
            # Type: string
            mariadb_role_docker_image_migration: "lscr.io/linuxserver/mariadb:10.6.13"
            ```

        ??? variable list "`mariadb_role_docker_volumes_migration`"

            ```yaml
            # Type: list
            mariadb_role_docker_volumes_migration: 
              - "{{ mariadb_role_paths_location }}:/config"
            ```

    === "Instance-level"

        ??? variable string "`mariadb2_docker_envs_mysql_root_password`"

            ```yaml
            # Type: string
            mariadb2_docker_envs_mysql_root_password: password321
            ```

        ??? variable string "`mariadb2_docker_image_migration`"

            ```yaml
            # Type: string
            mariadb2_docker_image_migration: "lscr.io/linuxserver/mariadb:10.6.13"
            ```

        ??? variable list "`mariadb2_docker_volumes_migration`"

            ```yaml
            # Type: list
                    mariadb2_docker_volumes_migration: 
                      - "{{ mariadb_role_paths_location }}:/config"
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`mariadb_role_docker_container`"

            ```yaml
            # Type: string
            mariadb_role_docker_container: "{{ mariadb_name }}"
            ```

        ##### Image

        ??? variable bool "`mariadb_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            mariadb_role_docker_image_pull: true
            ```

        ??? variable string "`mariadb_role_docker_image_repo`"

            ```yaml
            # Type: string
            mariadb_role_docker_image_repo: "mariadb"
            ```

        ??? variable string "`mariadb_role_docker_image_tag`"

            ```yaml
            # Type: string
            mariadb_role_docker_image_tag: "10"
            ```

        ??? variable string "`mariadb_role_docker_image`"

            ```yaml
            # Type: string
            mariadb_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='mariadb') }}:{{ lookup('role_var', '_docker_image_tag', role='mariadb') }}"
            ```

        ##### Envs

        ??? variable dict "`mariadb_role_docker_envs_default`"

            ```yaml
            # Type: dict
            mariadb_role_docker_envs_default: 
              TZ: "{{ tz }}"
              MARIADB_ROOT_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='mariadb') }}"
              MARIADB_USER: "{{ lookup('role_var', '_docker_env_user', role='mariadb') }}"
              MARIADB_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='mariadb') }}"
              MARIADB_DATABASE: "{{ lookup('role_var', '_docker_env_db', role='mariadb') }}"
              MARIADB_AUTO_UPGRADE: "1"
            ```

        ??? variable dict "`mariadb_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            mariadb_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`mariadb_role_docker_volumes_default`"

            ```yaml
            # Type: list
            mariadb_role_docker_volumes_default: 
              - "{{ mariadb_role_paths_location }}:/var/lib/mysql"
            ```

        ??? variable list "`mariadb_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            mariadb_role_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`mariadb_role_docker_hostname`"

            ```yaml
            # Type: string
            mariadb_role_docker_hostname: "{{ mariadb_name }}"
            ```

        ##### Networks

        ??? variable string "`mariadb_role_docker_networks_alias`"

            ```yaml
            # Type: string
            mariadb_role_docker_networks_alias: "{{ mariadb_name }}"
            ```

        ??? variable list "`mariadb_role_docker_networks_default`"

            ```yaml
            # Type: list
            mariadb_role_docker_networks_default: []
            ```

        ??? variable list "`mariadb_role_docker_networks_custom`"

            ```yaml
            # Type: list
            mariadb_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`mariadb_role_docker_restart_policy`"

            ```yaml
            # Type: string
            mariadb_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`mariadb_role_docker_state`"

            ```yaml
            # Type: string
            mariadb_role_docker_state: started
            ```

        ##### User

        ??? variable string "`mariadb_role_docker_user`"

            ```yaml
            # Type: string
            mariadb_role_docker_user: "{{ uid }}:{{ gid }}"
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`mariadb2_docker_container`"

            ```yaml
            # Type: string
            mariadb2_docker_container: "{{ mariadb_name }}"
            ```

        ##### Image

        ??? variable bool "`mariadb2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            mariadb2_docker_image_pull: true
            ```

        ??? variable string "`mariadb2_docker_image_repo`"

            ```yaml
            # Type: string
            mariadb2_docker_image_repo: "mariadb"
            ```

        ??? variable string "`mariadb2_docker_image_tag`"

            ```yaml
            # Type: string
            mariadb2_docker_image_tag: "10"
            ```

        ??? variable string "`mariadb2_docker_image`"

            ```yaml
            # Type: string
            mariadb2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='mariadb') }}:{{ lookup('role_var', '_docker_image_tag', role='mariadb') }}"
            ```

        ##### Envs

        ??? variable dict "`mariadb2_docker_envs_default`"

            ```yaml
            # Type: dict
                    mariadb2_docker_envs_default: 
                      TZ: "{{ tz }}"
                      MARIADB_ROOT_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='mariadb') }}"
                      MARIADB_USER: "{{ lookup('role_var', '_docker_env_user', role='mariadb') }}"
                      MARIADB_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='mariadb') }}"
                      MARIADB_DATABASE: "{{ lookup('role_var', '_docker_env_db', role='mariadb') }}"
                      MARIADB_AUTO_UPGRADE: "1"
            ```

        ??? variable dict "`mariadb2_docker_envs_custom`"

            ```yaml
            # Type: dict
            mariadb2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`mariadb2_docker_volumes_default`"

            ```yaml
            # Type: list
                    mariadb2_docker_volumes_default: 
                      - "{{ mariadb_role_paths_location }}:/var/lib/mysql"
            ```

        ??? variable list "`mariadb2_docker_volumes_custom`"

            ```yaml
            # Type: list
            mariadb2_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`mariadb2_docker_hostname`"

            ```yaml
            # Type: string
            mariadb2_docker_hostname: "{{ mariadb_name }}"
            ```

        ##### Networks

        ??? variable string "`mariadb2_docker_networks_alias`"

            ```yaml
            # Type: string
            mariadb2_docker_networks_alias: "{{ mariadb_name }}"
            ```

        ??? variable list "`mariadb2_docker_networks_default`"

            ```yaml
            # Type: list
            mariadb2_docker_networks_default: []
            ```

        ??? variable list "`mariadb2_docker_networks_custom`"

            ```yaml
            # Type: list
            mariadb2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`mariadb2_docker_restart_policy`"

            ```yaml
            # Type: string
            mariadb2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`mariadb2_docker_state`"

            ```yaml
            # Type: string
            mariadb2_docker_state: started
            ```

        ##### User

        ??? variable string "`mariadb2_docker_user`"

            ```yaml
            # Type: string
            mariadb2_docker_user: "{{ uid }}:{{ gid }}"
            ```

=== "Docker+"

    #### Additional Docker Options

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    === "Role-level"

        ##### Resource Limits

        ??? variable int "`mariadb_role_docker_blkio_weight`"

            ```yaml
            # Type: int
            mariadb_role_docker_blkio_weight:
            ```

        ??? variable int "`mariadb_role_docker_cpu_period`"

            ```yaml
            # Type: int
            mariadb_role_docker_cpu_period:
            ```

        ??? variable int "`mariadb_role_docker_cpu_quota`"

            ```yaml
            # Type: int
            mariadb_role_docker_cpu_quota:
            ```

        ??? variable int "`mariadb_role_docker_cpu_shares`"

            ```yaml
            # Type: int
            mariadb_role_docker_cpu_shares:
            ```

        ??? variable string "`mariadb_role_docker_cpus`"

            ```yaml
            # Type: string
            mariadb_role_docker_cpus:
            ```

        ??? variable string "`mariadb_role_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            mariadb_role_docker_cpuset_cpus:
            ```

        ??? variable string "`mariadb_role_docker_cpuset_mems`"

            ```yaml
            # Type: string
            mariadb_role_docker_cpuset_mems:
            ```

        ??? variable string "`mariadb_role_docker_kernel_memory`"

            ```yaml
            # Type: string
            mariadb_role_docker_kernel_memory:
            ```

        ??? variable string "`mariadb_role_docker_memory`"

            ```yaml
            # Type: string
            mariadb_role_docker_memory:
            ```

        ??? variable string "`mariadb_role_docker_memory_reservation`"

            ```yaml
            # Type: string
            mariadb_role_docker_memory_reservation:
            ```

        ??? variable string "`mariadb_role_docker_memory_swap`"

            ```yaml
            # Type: string
            mariadb_role_docker_memory_swap:
            ```

        ??? variable int "`mariadb_role_docker_memory_swappiness`"

            ```yaml
            # Type: int
            mariadb_role_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`mariadb_role_docker_cap_drop`"

            ```yaml
            # Type: list
            mariadb_role_docker_cap_drop:
            ```

        ??? variable list "`mariadb_role_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            mariadb_role_docker_device_cgroup_rules:
            ```

        ??? variable list "`mariadb_role_docker_device_read_bps`"

            ```yaml
            # Type: list
            mariadb_role_docker_device_read_bps:
            ```

        ??? variable list "`mariadb_role_docker_device_read_iops`"

            ```yaml
            # Type: list
            mariadb_role_docker_device_read_iops:
            ```

        ??? variable list "`mariadb_role_docker_device_requests`"

            ```yaml
            # Type: list
            mariadb_role_docker_device_requests:
            ```

        ??? variable list "`mariadb_role_docker_device_write_bps`"

            ```yaml
            # Type: list
            mariadb_role_docker_device_write_bps:
            ```

        ??? variable list "`mariadb_role_docker_device_write_iops`"

            ```yaml
            # Type: list
            mariadb_role_docker_device_write_iops:
            ```

        ??? variable list "`mariadb_role_docker_devices`"

            ```yaml
            # Type: list
            mariadb_role_docker_devices:
            ```

        ??? variable string "`mariadb_role_docker_devices_default`"

            ```yaml
            # Type: string
            mariadb_role_docker_devices_default:
            ```

        ??? variable bool "`mariadb_role_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            mariadb_role_docker_privileged:
            ```

        ??? variable list "`mariadb_role_docker_security_opts`"

            ```yaml
            # Type: list
            mariadb_role_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`mariadb_role_docker_dns_opts`"

            ```yaml
            # Type: list
            mariadb_role_docker_dns_opts:
            ```

        ??? variable list "`mariadb_role_docker_dns_search_domains`"

            ```yaml
            # Type: list
            mariadb_role_docker_dns_search_domains:
            ```

        ??? variable list "`mariadb_role_docker_dns_servers`"

            ```yaml
            # Type: list
            mariadb_role_docker_dns_servers:
            ```

        ??? variable dict "`mariadb_role_docker_hosts`"

            ```yaml
            # Type: dict
            mariadb_role_docker_hosts:
            ```

        ??? variable string "`mariadb_role_docker_hosts_use_common`"

            ```yaml
            # Type: string
            mariadb_role_docker_hosts_use_common:
            ```

        ??? variable string "`mariadb_role_docker_network_mode`"

            ```yaml
            # Type: string
            mariadb_role_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`mariadb_role_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            mariadb_role_docker_keep_volumes:
            ```

        ??? variable list "`mariadb_role_docker_mounts`"

            ```yaml
            # Type: list
            mariadb_role_docker_mounts:
            ```

        ??? variable string "`mariadb_role_docker_volume_driver`"

            ```yaml
            # Type: string
            mariadb_role_docker_volume_driver:
            ```

        ??? variable list "`mariadb_role_docker_volumes_from`"

            ```yaml
            # Type: list
            mariadb_role_docker_volumes_from:
            ```

        ??? variable string "`mariadb_role_docker_volumes_global`"

            ```yaml
            # Type: string
            mariadb_role_docker_volumes_global:
            ```

        ??? variable string "`mariadb_role_docker_working_dir`"

            ```yaml
            # Type: string
            mariadb_role_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`mariadb_role_docker_healthcheck`"

            ```yaml
            # Type: dict
            mariadb_role_docker_healthcheck:
            ```

        ??? variable bool "`mariadb_role_docker_init`"

            ```yaml
            # Type: bool (true/false)
            mariadb_role_docker_init:
            ```

        ??? variable string "`mariadb_role_docker_log_driver`"

            ```yaml
            # Type: string
            mariadb_role_docker_log_driver:
            ```

        ??? variable dict "`mariadb_role_docker_log_options`"

            ```yaml
            # Type: dict
            mariadb_role_docker_log_options:
            ```

        ??? variable bool "`mariadb_role_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            mariadb_role_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`mariadb_role_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            mariadb_role_docker_auto_remove:
            ```

        ??? variable list "`mariadb_role_docker_capabilities`"

            ```yaml
            # Type: list
            mariadb_role_docker_capabilities:
            ```

        ??? variable string "`mariadb_role_docker_cgroup_parent`"

            ```yaml
            # Type: string
            mariadb_role_docker_cgroup_parent:
            ```

        ??? variable string "`mariadb_role_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            mariadb_role_docker_cgroupns_mode:
            ```

        ??? variable bool "`mariadb_role_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            mariadb_role_docker_cleanup:
            ```

        ??? variable list "`mariadb_role_docker_commands`"

            ```yaml
            # Type: list
            mariadb_role_docker_commands:
            ```

        ??? variable string "`mariadb_role_docker_create_timeout`"

            ```yaml
            # Type: string
            mariadb_role_docker_create_timeout:
            ```

        ??? variable string "`mariadb_role_docker_domainname`"

            ```yaml
            # Type: string
            mariadb_role_docker_domainname:
            ```

        ??? variable string "`mariadb_role_docker_entrypoint`"

            ```yaml
            # Type: string
            mariadb_role_docker_entrypoint:
            ```

        ??? variable string "`mariadb_role_docker_env_file`"

            ```yaml
            # Type: string
            mariadb_role_docker_env_file:
            ```

        ??? variable list "`mariadb_role_docker_exposed_ports`"

            ```yaml
            # Type: list
            mariadb_role_docker_exposed_ports:
            ```

        ??? variable string "`mariadb_role_docker_force_kill`"

            ```yaml
            # Type: string
            mariadb_role_docker_force_kill:
            ```

        ??? variable list "`mariadb_role_docker_groups`"

            ```yaml
            # Type: list
            mariadb_role_docker_groups:
            ```

        ??? variable int "`mariadb_role_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            mariadb_role_docker_healthy_wait_timeout:
            ```

        ??? variable string "`mariadb_role_docker_ipc_mode`"

            ```yaml
            # Type: string
            mariadb_role_docker_ipc_mode:
            ```

        ??? variable string "`mariadb_role_docker_kill_signal`"

            ```yaml
            # Type: string
            mariadb_role_docker_kill_signal:
            ```

        ??? variable dict "`mariadb_role_docker_labels`"

            ```yaml
            # Type: dict
            mariadb_role_docker_labels:
            ```

        ??? variable string "`mariadb_role_docker_labels_use_common`"

            ```yaml
            # Type: string
            mariadb_role_docker_labels_use_common:
            ```

        ??? variable list "`mariadb_role_docker_links`"

            ```yaml
            # Type: list
            mariadb_role_docker_links:
            ```

        ??? variable bool "`mariadb_role_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            mariadb_role_docker_oom_killer:
            ```

        ??? variable int "`mariadb_role_docker_oom_score_adj`"

            ```yaml
            # Type: int
            mariadb_role_docker_oom_score_adj:
            ```

        ??? variable bool "`mariadb_role_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            mariadb_role_docker_paused:
            ```

        ??? variable string "`mariadb_role_docker_pid_mode`"

            ```yaml
            # Type: string
            mariadb_role_docker_pid_mode:
            ```

        ??? variable list "`mariadb_role_docker_ports`"

            ```yaml
            # Type: list
            mariadb_role_docker_ports:
            ```

        ??? variable bool "`mariadb_role_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            mariadb_role_docker_read_only:
            ```

        ??? variable bool "`mariadb_role_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            mariadb_role_docker_recreate:
            ```

        ??? variable int "`mariadb_role_docker_restart_retries`"

            ```yaml
            # Type: int
            mariadb_role_docker_restart_retries:
            ```

        ??? variable string "`mariadb_role_docker_runtime`"

            ```yaml
            # Type: string
            mariadb_role_docker_runtime:
            ```

        ??? variable string "`mariadb_role_docker_shm_size`"

            ```yaml
            # Type: string
            mariadb_role_docker_shm_size:
            ```

        ??? variable int "`mariadb_role_docker_stop_timeout`"

            ```yaml
            # Type: int
            mariadb_role_docker_stop_timeout:
            ```

        ??? variable dict "`mariadb_role_docker_storage_opts`"

            ```yaml
            # Type: dict
            mariadb_role_docker_storage_opts:
            ```

        ??? variable list "`mariadb_role_docker_sysctls`"

            ```yaml
            # Type: list
            mariadb_role_docker_sysctls:
            ```

        ??? variable list "`mariadb_role_docker_tmpfs`"

            ```yaml
            # Type: list
            mariadb_role_docker_tmpfs:
            ```

        ??? variable list "`mariadb_role_docker_ulimits`"

            ```yaml
            # Type: list
            mariadb_role_docker_ulimits:
            ```

        ??? variable string "`mariadb_role_docker_userns_mode`"

            ```yaml
            # Type: string
            mariadb_role_docker_userns_mode:
            ```

        ??? variable string "`mariadb_role_docker_uts`"

            ```yaml
            # Type: string
            mariadb_role_docker_uts:
            ```

    === "Instance-level"

        ##### Resource Limits

        ??? variable int "`mariadb2_docker_blkio_weight`"

            ```yaml
            # Type: int
            mariadb2_docker_blkio_weight:
            ```

        ??? variable int "`mariadb2_docker_cpu_period`"

            ```yaml
            # Type: int
            mariadb2_docker_cpu_period:
            ```

        ??? variable int "`mariadb2_docker_cpu_quota`"

            ```yaml
            # Type: int
            mariadb2_docker_cpu_quota:
            ```

        ??? variable int "`mariadb2_docker_cpu_shares`"

            ```yaml
            # Type: int
            mariadb2_docker_cpu_shares:
            ```

        ??? variable string "`mariadb2_docker_cpus`"

            ```yaml
            # Type: string
            mariadb2_docker_cpus:
            ```

        ??? variable string "`mariadb2_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            mariadb2_docker_cpuset_cpus:
            ```

        ??? variable string "`mariadb2_docker_cpuset_mems`"

            ```yaml
            # Type: string
            mariadb2_docker_cpuset_mems:
            ```

        ??? variable string "`mariadb2_docker_kernel_memory`"

            ```yaml
            # Type: string
            mariadb2_docker_kernel_memory:
            ```

        ??? variable string "`mariadb2_docker_memory`"

            ```yaml
            # Type: string
            mariadb2_docker_memory:
            ```

        ??? variable string "`mariadb2_docker_memory_reservation`"

            ```yaml
            # Type: string
            mariadb2_docker_memory_reservation:
            ```

        ??? variable string "`mariadb2_docker_memory_swap`"

            ```yaml
            # Type: string
            mariadb2_docker_memory_swap:
            ```

        ??? variable int "`mariadb2_docker_memory_swappiness`"

            ```yaml
            # Type: int
            mariadb2_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`mariadb2_docker_cap_drop`"

            ```yaml
            # Type: list
            mariadb2_docker_cap_drop:
            ```

        ??? variable list "`mariadb2_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            mariadb2_docker_device_cgroup_rules:
            ```

        ??? variable list "`mariadb2_docker_device_read_bps`"

            ```yaml
            # Type: list
            mariadb2_docker_device_read_bps:
            ```

        ??? variable list "`mariadb2_docker_device_read_iops`"

            ```yaml
            # Type: list
            mariadb2_docker_device_read_iops:
            ```

        ??? variable list "`mariadb2_docker_device_requests`"

            ```yaml
            # Type: list
            mariadb2_docker_device_requests:
            ```

        ??? variable list "`mariadb2_docker_device_write_bps`"

            ```yaml
            # Type: list
            mariadb2_docker_device_write_bps:
            ```

        ??? variable list "`mariadb2_docker_device_write_iops`"

            ```yaml
            # Type: list
            mariadb2_docker_device_write_iops:
            ```

        ??? variable list "`mariadb2_docker_devices`"

            ```yaml
            # Type: list
            mariadb2_docker_devices:
            ```

        ??? variable string "`mariadb2_docker_devices_default`"

            ```yaml
            # Type: string
            mariadb2_docker_devices_default:
            ```

        ??? variable bool "`mariadb2_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            mariadb2_docker_privileged:
            ```

        ??? variable list "`mariadb2_docker_security_opts`"

            ```yaml
            # Type: list
            mariadb2_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`mariadb2_docker_dns_opts`"

            ```yaml
            # Type: list
            mariadb2_docker_dns_opts:
            ```

        ??? variable list "`mariadb2_docker_dns_search_domains`"

            ```yaml
            # Type: list
            mariadb2_docker_dns_search_domains:
            ```

        ??? variable list "`mariadb2_docker_dns_servers`"

            ```yaml
            # Type: list
            mariadb2_docker_dns_servers:
            ```

        ??? variable dict "`mariadb2_docker_hosts`"

            ```yaml
            # Type: dict
            mariadb2_docker_hosts:
            ```

        ??? variable string "`mariadb2_docker_hosts_use_common`"

            ```yaml
            # Type: string
            mariadb2_docker_hosts_use_common:
            ```

        ??? variable string "`mariadb2_docker_network_mode`"

            ```yaml
            # Type: string
            mariadb2_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`mariadb2_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            mariadb2_docker_keep_volumes:
            ```

        ??? variable list "`mariadb2_docker_mounts`"

            ```yaml
            # Type: list
            mariadb2_docker_mounts:
            ```

        ??? variable string "`mariadb2_docker_volume_driver`"

            ```yaml
            # Type: string
            mariadb2_docker_volume_driver:
            ```

        ??? variable list "`mariadb2_docker_volumes_from`"

            ```yaml
            # Type: list
            mariadb2_docker_volumes_from:
            ```

        ??? variable string "`mariadb2_docker_volumes_global`"

            ```yaml
            # Type: string
            mariadb2_docker_volumes_global:
            ```

        ??? variable string "`mariadb2_docker_working_dir`"

            ```yaml
            # Type: string
            mariadb2_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`mariadb2_docker_healthcheck`"

            ```yaml
            # Type: dict
            mariadb2_docker_healthcheck:
            ```

        ??? variable bool "`mariadb2_docker_init`"

            ```yaml
            # Type: bool (true/false)
            mariadb2_docker_init:
            ```

        ??? variable string "`mariadb2_docker_log_driver`"

            ```yaml
            # Type: string
            mariadb2_docker_log_driver:
            ```

        ??? variable dict "`mariadb2_docker_log_options`"

            ```yaml
            # Type: dict
            mariadb2_docker_log_options:
            ```

        ??? variable bool "`mariadb2_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            mariadb2_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`mariadb2_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            mariadb2_docker_auto_remove:
            ```

        ??? variable list "`mariadb2_docker_capabilities`"

            ```yaml
            # Type: list
            mariadb2_docker_capabilities:
            ```

        ??? variable string "`mariadb2_docker_cgroup_parent`"

            ```yaml
            # Type: string
            mariadb2_docker_cgroup_parent:
            ```

        ??? variable string "`mariadb2_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            mariadb2_docker_cgroupns_mode:
            ```

        ??? variable bool "`mariadb2_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            mariadb2_docker_cleanup:
            ```

        ??? variable list "`mariadb2_docker_commands`"

            ```yaml
            # Type: list
            mariadb2_docker_commands:
            ```

        ??? variable string "`mariadb2_docker_create_timeout`"

            ```yaml
            # Type: string
            mariadb2_docker_create_timeout:
            ```

        ??? variable string "`mariadb2_docker_domainname`"

            ```yaml
            # Type: string
            mariadb2_docker_domainname:
            ```

        ??? variable string "`mariadb2_docker_entrypoint`"

            ```yaml
            # Type: string
            mariadb2_docker_entrypoint:
            ```

        ??? variable string "`mariadb2_docker_env_file`"

            ```yaml
            # Type: string
            mariadb2_docker_env_file:
            ```

        ??? variable list "`mariadb2_docker_exposed_ports`"

            ```yaml
            # Type: list
            mariadb2_docker_exposed_ports:
            ```

        ??? variable string "`mariadb2_docker_force_kill`"

            ```yaml
            # Type: string
            mariadb2_docker_force_kill:
            ```

        ??? variable list "`mariadb2_docker_groups`"

            ```yaml
            # Type: list
            mariadb2_docker_groups:
            ```

        ??? variable int "`mariadb2_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            mariadb2_docker_healthy_wait_timeout:
            ```

        ??? variable string "`mariadb2_docker_ipc_mode`"

            ```yaml
            # Type: string
            mariadb2_docker_ipc_mode:
            ```

        ??? variable string "`mariadb2_docker_kill_signal`"

            ```yaml
            # Type: string
            mariadb2_docker_kill_signal:
            ```

        ??? variable dict "`mariadb2_docker_labels`"

            ```yaml
            # Type: dict
            mariadb2_docker_labels:
            ```

        ??? variable string "`mariadb2_docker_labels_use_common`"

            ```yaml
            # Type: string
            mariadb2_docker_labels_use_common:
            ```

        ??? variable list "`mariadb2_docker_links`"

            ```yaml
            # Type: list
            mariadb2_docker_links:
            ```

        ??? variable bool "`mariadb2_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            mariadb2_docker_oom_killer:
            ```

        ??? variable int "`mariadb2_docker_oom_score_adj`"

            ```yaml
            # Type: int
            mariadb2_docker_oom_score_adj:
            ```

        ??? variable bool "`mariadb2_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            mariadb2_docker_paused:
            ```

        ??? variable string "`mariadb2_docker_pid_mode`"

            ```yaml
            # Type: string
            mariadb2_docker_pid_mode:
            ```

        ??? variable list "`mariadb2_docker_ports`"

            ```yaml
            # Type: list
            mariadb2_docker_ports:
            ```

        ??? variable bool "`mariadb2_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            mariadb2_docker_read_only:
            ```

        ??? variable bool "`mariadb2_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            mariadb2_docker_recreate:
            ```

        ??? variable int "`mariadb2_docker_restart_retries`"

            ```yaml
            # Type: int
            mariadb2_docker_restart_retries:
            ```

        ??? variable string "`mariadb2_docker_runtime`"

            ```yaml
            # Type: string
            mariadb2_docker_runtime:
            ```

        ??? variable string "`mariadb2_docker_shm_size`"

            ```yaml
            # Type: string
            mariadb2_docker_shm_size:
            ```

        ??? variable int "`mariadb2_docker_stop_timeout`"

            ```yaml
            # Type: int
            mariadb2_docker_stop_timeout:
            ```

        ??? variable dict "`mariadb2_docker_storage_opts`"

            ```yaml
            # Type: dict
            mariadb2_docker_storage_opts:
            ```

        ??? variable list "`mariadb2_docker_sysctls`"

            ```yaml
            # Type: list
            mariadb2_docker_sysctls:
            ```

        ??? variable list "`mariadb2_docker_tmpfs`"

            ```yaml
            # Type: list
            mariadb2_docker_tmpfs:
            ```

        ??? variable list "`mariadb2_docker_ulimits`"

            ```yaml
            # Type: list
            mariadb2_docker_ulimits:
            ```

        ??? variable string "`mariadb2_docker_userns_mode`"

            ```yaml
            # Type: string
            mariadb2_docker_userns_mode:
            ```

        ??? variable string "`mariadb2_docker_uts`"

            ```yaml
            # Type: string
            mariadb2_docker_uts:
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`mariadb_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            mariadb_role_autoheal_enabled: true
            ```

        ??? variable string "`mariadb_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            mariadb_role_depends_on: ""
            ```

        ??? variable string "`mariadb_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            mariadb_role_depends_on_delay: "0"
            ```

        ??? variable string "`mariadb_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            mariadb_role_depends_on_healthchecks:
            ```

        ??? variable bool "`mariadb_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            mariadb_role_diun_enabled: true
            ```

        ??? variable bool "`mariadb_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            mariadb_role_dns_enabled: true
            ```

        ??? variable bool "`mariadb_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            mariadb_role_docker_controller: true
            ```

        ??? variable bool "`mariadb_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            mariadb_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`mariadb_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            mariadb_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`mariadb_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            mariadb_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`mariadb_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            mariadb_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`mariadb_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            mariadb_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`mariadb_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            mariadb_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`mariadb_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            mariadb_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`mariadb_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            mariadb_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                mariadb_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "mariadb2.{{ user.domain }}"
                  - "mariadb.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`mariadb_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            mariadb_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                mariadb_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'mariadb2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`mariadb_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            mariadb_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `mariadb2`):

        ??? variable bool "`mariadb2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            mariadb2_autoheal_enabled: true
            ```

        ??? variable string "`mariadb2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            mariadb2_depends_on: ""
            ```

        ??? variable string "`mariadb2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            mariadb2_depends_on_delay: "0"
            ```

        ??? variable string "`mariadb2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            mariadb2_depends_on_healthchecks:
            ```

        ??? variable bool "`mariadb2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            mariadb2_diun_enabled: true
            ```

        ??? variable bool "`mariadb2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            mariadb2_dns_enabled: true
            ```

        ??? variable bool "`mariadb2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            mariadb2_docker_controller: true
            ```

        ??? variable bool "`mariadb2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            mariadb2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`mariadb2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            mariadb2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`mariadb2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            mariadb2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`mariadb2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            mariadb2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`mariadb2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            mariadb2_traefik_robot_enabled: true
            ```

        ??? variable bool "`mariadb2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            mariadb2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`mariadb2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            mariadb2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`mariadb2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            mariadb2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                mariadb2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "mariadb2.{{ user.domain }}"
                  - "mariadb.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`mariadb2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            mariadb2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                mariadb2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'mariadb2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`mariadb2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            mariadb2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
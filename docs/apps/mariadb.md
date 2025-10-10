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

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
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

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        mariadb_instances: ["mariadb"]

        ```

    === "Example"

        ```yaml
        # Type: list
        mariadb_instances: ["mariadb", "mariadb2"]

        ```

??? example "Settings"

    === "Role-level"

        ```yaml
        # Type: string
        mariadb_role_docker_env_password: "password321"

        # Type: string
        mariadb_role_docker_env_user: "{{ user.name }}"

        # Type: string
        mariadb_role_docker_env_db: "saltbox"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        mariadb2_docker_env_password: "password321"

        # Type: string
        mariadb2_docker_env_user: "{{ user.name }}"

        # Type: string
        mariadb2_docker_env_db: "saltbox"

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        mariadb_role_paths_folder: "{{ mariadb_name }}"

        # Type: string
        mariadb_role_paths_location: "{{ server_appdata_path }}/{{ mariadb_role_paths_folder }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        mariadb2_paths_folder: "{{ mariadb_name }}"

        # Type: string
        mariadb2_paths_location: "{{ server_appdata_path }}/{{ mariadb_role_paths_folder }}"

        ```

??? example "Migration Settings"

    === "Role-level"

        ```yaml
        # Type: string
        mariadb_role_docker_envs_mysql_root_password: password321

        # Type: string
        mariadb_role_docker_image_migration: "lscr.io/linuxserver/mariadb:10.6.13"

        # Type: list
        mariadb_role_docker_volumes_migration: 
          - "{{ mariadb_role_paths_location }}:/config"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        mariadb2_docker_envs_mysql_root_password: password321

        # Type: string
        mariadb2_docker_image_migration: "lscr.io/linuxserver/mariadb:10.6.13"

        # Type: list
        mariadb2_docker_volumes_migration: 
          - "{{ mariadb_role_paths_location }}:/config"

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        mariadb_role_docker_container: "{{ mariadb_name }}"

        # Image
        # Type: bool (true/false)
        mariadb_role_docker_image_pull: true

        # Type: string
        mariadb_role_docker_image_repo: "mariadb"

        # Type: string
        mariadb_role_docker_image_tag: "10"

        # Type: string
        mariadb_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='mariadb') }}:{{ lookup('role_var', '_docker_image_tag', role='mariadb') }}"

        # Envs
        # Type: dict
        mariadb_role_docker_envs_default: 
          TZ: "{{ tz }}"
          MARIADB_ROOT_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='mariadb') }}"
          MARIADB_USER: "{{ lookup('role_var', '_docker_env_user', role='mariadb') }}"
          MARIADB_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='mariadb') }}"
          MARIADB_DATABASE: "{{ lookup('role_var', '_docker_env_db', role='mariadb') }}"
          MARIADB_AUTO_UPGRADE: "1"

        # Type: dict
        mariadb_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        mariadb_role_docker_volumes_default: 
          - "{{ mariadb_role_paths_location }}:/var/lib/mysql"

        # Type: list
        mariadb_role_docker_volumes_custom: []

        # Hostname
        # Type: string
        mariadb_role_docker_hostname: "{{ mariadb_name }}"

        # Networks
        # Type: string
        mariadb_role_docker_networks_alias: "{{ mariadb_name }}"

        # Type: list
        mariadb_role_docker_networks_default: []

        # Type: list
        mariadb_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        mariadb_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        mariadb_role_docker_state: started

        # User
        # Type: string
        mariadb_role_docker_user: "{{ uid }}:{{ gid }}"


        # ---- Additional Docker Options ----
        # The following advanced options are available via create_docker_container
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        mariadb_role_docker_blkio_weight:

        # Type: int
        mariadb_role_docker_cpu_period:

        # Type: int
        mariadb_role_docker_cpu_quota:

        # Type: int
        mariadb_role_docker_cpu_shares:

        # Type: string
        mariadb_role_docker_cpus:

        # Type: string
        mariadb_role_docker_cpuset_cpus:

        # Type: string
        mariadb_role_docker_cpuset_mems:

        # Type: string
        mariadb_role_docker_kernel_memory:

        # Type: string
        mariadb_role_docker_memory:

        # Type: string
        mariadb_role_docker_memory_reservation:

        # Type: string
        mariadb_role_docker_memory_swap:

        # Type: int
        mariadb_role_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        mariadb_role_docker_cap_drop:

        # Type: list
        mariadb_role_docker_device_cgroup_rules:

        # Type: list
        mariadb_role_docker_device_read_bps:

        # Type: list
        mariadb_role_docker_device_read_iops:

        # Type: list
        mariadb_role_docker_device_requests:

        # Type: list
        mariadb_role_docker_device_write_bps:

        # Type: list
        mariadb_role_docker_device_write_iops:

        # Type: list
        mariadb_role_docker_devices:

        # Type: string
        mariadb_role_docker_devices_default:

        # Type: bool (true/false)
        mariadb_role_docker_privileged:

        # Type: list
        mariadb_role_docker_security_opts:

        # Networking
        # Type: list
        mariadb_role_docker_dns_opts:

        # Type: list
        mariadb_role_docker_dns_search_domains:

        # Type: list
        mariadb_role_docker_dns_servers:

        # Type: dict
        mariadb_role_docker_hosts:

        # Type: string
        mariadb_role_docker_hosts_use_common:

        # Type: string
        mariadb_role_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        mariadb_role_docker_keep_volumes:

        # Type: list
        mariadb_role_docker_mounts:

        # Type: string
        mariadb_role_docker_volume_driver:

        # Type: list
        mariadb_role_docker_volumes_from:

        # Type: string
        mariadb_role_docker_volumes_global:

        # Type: string
        mariadb_role_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        mariadb_role_docker_healthcheck:

        # Type: bool (true/false)
        mariadb_role_docker_init:

        # Type: string
        mariadb_role_docker_log_driver:

        # Type: dict
        mariadb_role_docker_log_options:

        # Type: bool (true/false)
        mariadb_role_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        mariadb_role_docker_auto_remove:

        # Type: list
        mariadb_role_docker_capabilities:

        # Type: string
        mariadb_role_docker_cgroup_parent:

        # Type: string
        mariadb_role_docker_cgroupns_mode:

        # Type: bool (true/false)
        mariadb_role_docker_cleanup:

        # Type: list
        mariadb_role_docker_commands:

        # Type: string
        mariadb_role_docker_create_timeout:

        # Type: string
        mariadb_role_docker_domainname:

        # Type: string
        mariadb_role_docker_entrypoint:

        # Type: string
        mariadb_role_docker_env_file:

        # Type: list
        mariadb_role_docker_exposed_ports:

        # Type: string
        mariadb_role_docker_force_kill:

        # Type: list
        mariadb_role_docker_groups:

        # Type: int
        mariadb_role_docker_healthy_wait_timeout:

        # Type: string
        mariadb_role_docker_ipc_mode:

        # Type: string
        mariadb_role_docker_kill_signal:

        # Type: dict
        mariadb_role_docker_labels:

        # Type: string
        mariadb_role_docker_labels_use_common:

        # Type: list
        mariadb_role_docker_links:

        # Type: bool (true/false)
        mariadb_role_docker_oom_killer:

        # Type: int
        mariadb_role_docker_oom_score_adj:

        # Type: bool (true/false)
        mariadb_role_docker_paused:

        # Type: string
        mariadb_role_docker_pid_mode:

        # Type: list
        mariadb_role_docker_ports:

        # Type: bool (true/false)
        mariadb_role_docker_read_only:

        # Type: bool (true/false)
        mariadb_role_docker_recreate:

        # Type: int
        mariadb_role_docker_restart_retries:

        # Type: string
        mariadb_role_docker_runtime:

        # Type: string
        mariadb_role_docker_shm_size:

        # Type: int
        mariadb_role_docker_stop_timeout:

        # Type: dict
        mariadb_role_docker_storage_opts:

        # Type: list
        mariadb_role_docker_sysctls:

        # Type: list
        mariadb_role_docker_tmpfs:

        # Type: list
        mariadb_role_docker_ulimits:

        # Type: string
        mariadb_role_docker_userns_mode:

        # Type: string
        mariadb_role_docker_uts:

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        mariadb2_docker_container: "{{ mariadb_name }}"

        # Image
        # Type: bool (true/false)
        mariadb2_docker_image_pull: true

        # Type: string
        mariadb2_docker_image_repo: "mariadb"

        # Type: string
        mariadb2_docker_image_tag: "10"

        # Type: string
        mariadb2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='mariadb') }}:{{ lookup('role_var', '_docker_image_tag', role='mariadb') }}"

        # Envs
        # Type: dict
        mariadb2_docker_envs_default: 
          TZ: "{{ tz }}"
          MARIADB_ROOT_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='mariadb') }}"
          MARIADB_USER: "{{ lookup('role_var', '_docker_env_user', role='mariadb') }}"
          MARIADB_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='mariadb') }}"
          MARIADB_DATABASE: "{{ lookup('role_var', '_docker_env_db', role='mariadb') }}"
          MARIADB_AUTO_UPGRADE: "1"

        # Type: dict
        mariadb2_docker_envs_custom: {}

        # Volumes
        # Type: list
        mariadb2_docker_volumes_default: 
          - "{{ mariadb_role_paths_location }}:/var/lib/mysql"

        # Type: list
        mariadb2_docker_volumes_custom: []

        # Hostname
        # Type: string
        mariadb2_docker_hostname: "{{ mariadb_name }}"

        # Networks
        # Type: string
        mariadb2_docker_networks_alias: "{{ mariadb_name }}"

        # Type: list
        mariadb2_docker_networks_default: []

        # Type: list
        mariadb2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        mariadb2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        mariadb2_docker_state: started

        # User
        # Type: string
        mariadb2_docker_user: "{{ uid }}:{{ gid }}"


        # ---- Additional Docker Options ----
        # The following advanced options are available via lookup('docker_var', ...)
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        mariadb2_docker_blkio_weight:
        # Type: int
        mariadb2_docker_cpu_period:
        # Type: int
        mariadb2_docker_cpu_quota:
        # Type: int
        mariadb2_docker_cpu_shares:
        # Type: string
        mariadb2_docker_cpus:
        # Type: string
        mariadb2_docker_cpuset_cpus:
        # Type: string
        mariadb2_docker_cpuset_mems:
        # Type: string
        mariadb2_docker_kernel_memory:
        # Type: string
        mariadb2_docker_memory:
        # Type: string
        mariadb2_docker_memory_reservation:
        # Type: string
        mariadb2_docker_memory_swap:
        # Type: int
        mariadb2_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        mariadb2_docker_cap_drop:
        # Type: list
        mariadb2_docker_device_cgroup_rules:
        # Type: list
        mariadb2_docker_device_read_bps:
        # Type: list
        mariadb2_docker_device_read_iops:
        # Type: list
        mariadb2_docker_device_requests:
        # Type: list
        mariadb2_docker_device_write_bps:
        # Type: list
        mariadb2_docker_device_write_iops:
        # Type: list
        mariadb2_docker_devices:
        # Type: string
        mariadb2_docker_devices_default:
        # Type: bool (true/false)
        mariadb2_docker_privileged:
        # Type: list
        mariadb2_docker_security_opts:

        # Networking
        # Type: list
        mariadb2_docker_dns_opts:
        # Type: list
        mariadb2_docker_dns_search_domains:
        # Type: list
        mariadb2_docker_dns_servers:
        # Type: dict
        mariadb2_docker_hosts:
        # Type: string
        mariadb2_docker_hosts_use_common:
        # Type: string
        mariadb2_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        mariadb2_docker_keep_volumes:
        # Type: list
        mariadb2_docker_mounts:
        # Type: string
        mariadb2_docker_volume_driver:
        # Type: list
        mariadb2_docker_volumes_from:
        # Type: string
        mariadb2_docker_volumes_global:
        # Type: string
        mariadb2_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        mariadb2_docker_healthcheck:
        # Type: bool (true/false)
        mariadb2_docker_init:
        # Type: string
        mariadb2_docker_log_driver:
        # Type: dict
        mariadb2_docker_log_options:
        # Type: bool (true/false)
        mariadb2_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        mariadb2_docker_auto_remove:
        # Type: list
        mariadb2_docker_capabilities:
        # Type: string
        mariadb2_docker_cgroup_parent:
        # Type: string
        mariadb2_docker_cgroupns_mode:
        # Type: bool (true/false)
        mariadb2_docker_cleanup:
        # Type: list
        mariadb2_docker_commands:
        # Type: string
        mariadb2_docker_create_timeout:
        # Type: string
        mariadb2_docker_domainname:
        # Type: string
        mariadb2_docker_entrypoint:
        # Type: string
        mariadb2_docker_env_file:
        # Type: list
        mariadb2_docker_exposed_ports:
        # Type: string
        mariadb2_docker_force_kill:
        # Type: list
        mariadb2_docker_groups:
        # Type: int
        mariadb2_docker_healthy_wait_timeout:
        # Type: string
        mariadb2_docker_ipc_mode:
        # Type: string
        mariadb2_docker_kill_signal:
        # Type: dict
        mariadb2_docker_labels:
        # Type: string
        mariadb2_docker_labels_use_common:
        # Type: list
        mariadb2_docker_links:
        # Type: bool (true/false)
        mariadb2_docker_oom_killer:
        # Type: int
        mariadb2_docker_oom_score_adj:
        # Type: bool (true/false)
        mariadb2_docker_paused:
        # Type: string
        mariadb2_docker_pid_mode:
        # Type: list
        mariadb2_docker_ports:
        # Type: bool (true/false)
        mariadb2_docker_read_only:
        # Type: bool (true/false)
        mariadb2_docker_recreate:
        # Type: int
        mariadb2_docker_restart_retries:
        # Type: string
        mariadb2_docker_runtime:
        # Type: string
        mariadb2_docker_shm_size:
        # Type: int
        mariadb2_docker_stop_timeout:
        # Type: dict
        mariadb2_docker_storage_opts:
        # Type: list
        mariadb2_docker_sysctls:
        # Type: list
        mariadb2_docker_tmpfs:
        # Type: list
        mariadb2_docker_ulimits:
        # Type: string
        mariadb2_docker_userns_mode:
        # Type: string
        mariadb2_docker_uts:

        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        mariadb_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        mariadb_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        mariadb_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        mariadb_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        mariadb_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        mariadb_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        mariadb_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        mariadb_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        mariadb_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        mariadb_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        mariadb_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        mariadb_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        mariadb_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        mariadb_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        mariadb_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        mariadb_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        mariadb_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            mariadb_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "mariadb2.{{ user.domain }}"
              - "mariadb.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            mariadb_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'mariadb2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `mariadb2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        mariadb2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        mariadb2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        mariadb2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        mariadb2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        mariadb2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        mariadb2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        mariadb2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        mariadb2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        mariadb2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        mariadb2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        mariadb2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        mariadb2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        mariadb2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        mariadb2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        mariadb2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        mariadb2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        mariadb2_web_scheme:

        ```

        1.  Example:

            ```yaml
            mariadb2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "mariadb2.{{ user.domain }}"
              - "mariadb.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            mariadb2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'mariadb2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

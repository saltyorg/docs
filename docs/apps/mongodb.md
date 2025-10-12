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

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
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

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        mongodb_instances: ["mongo"]

        ```

    === "Example"

        ```yaml
        # Type: list
        mongodb_instances: ["mongodb", "mongodb2"]

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        mongodb_role_paths_folder: "{{ mongodb_name }}"

        # Type: string
        mongodb_role_paths_location: "{{ server_appdata_path }}/{{ mongodb_role_paths_folder }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        mongodb2_paths_folder: "{{ mongodb_name }}"

        # Type: string
        mongodb2_paths_location: "{{ server_appdata_path }}/{{ mongodb_role_paths_folder }}"

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        mongodb_role_docker_container: "{{ mongodb_name }}"

        # Image
        # Type: bool (true/false)
        mongodb_role_docker_image_pull: true

        # Type: string
        mongodb_role_docker_image_repo: "mongo"

        # Type: string
        mongodb_role_docker_image_tag: "6"

        # Type: string
        mongodb_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='mongodb') }}:{{ lookup('role_var', '_docker_image_tag', role='mongodb') }}"

        # Envs
        # Type: dict
        mongodb_role_docker_envs_default: 
          MONGO_DATA_DIR: "/data/db"
          MONGO_LOG_DIR: "/dev/null"
          MONGO_URL: "mongodb://{{ mongodb_name }}:27017/"

        # Type: dict
        mongodb_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        mongodb_role_docker_volumes_default: 
          - "{{ mongodb_role_paths_location }}:/data/db:rw"
          - "{{ mongodb_role_paths_location }}/config:/data/configdb"

        # Type: list
        mongodb_role_docker_volumes_custom: []

        # Hostname
        # Type: string
        mongodb_role_docker_hostname: "{{ mongodb_name }}"

        # Networks
        # Type: string
        mongodb_role_docker_networks_alias: "{{ mongodb_name }}"

        # Type: list
        mongodb_role_docker_networks_default: []

        # Type: list
        mongodb_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        mongodb_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        mongodb_role_docker_state: started

        # User
        # Type: string
        mongodb_role_docker_user: "{{ uid }}:{{ gid }}"


        # ---- Additional Docker Options ----
        # The following advanced options are available via create_docker_container
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        mongodb_role_docker_blkio_weight:

        # Type: int
        mongodb_role_docker_cpu_period:

        # Type: int
        mongodb_role_docker_cpu_quota:

        # Type: int
        mongodb_role_docker_cpu_shares:

        # Type: string
        mongodb_role_docker_cpus:

        # Type: string
        mongodb_role_docker_cpuset_cpus:

        # Type: string
        mongodb_role_docker_cpuset_mems:

        # Type: string
        mongodb_role_docker_kernel_memory:

        # Type: string
        mongodb_role_docker_memory:

        # Type: string
        mongodb_role_docker_memory_reservation:

        # Type: string
        mongodb_role_docker_memory_swap:

        # Type: int
        mongodb_role_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        mongodb_role_docker_cap_drop:

        # Type: list
        mongodb_role_docker_device_cgroup_rules:

        # Type: list
        mongodb_role_docker_device_read_bps:

        # Type: list
        mongodb_role_docker_device_read_iops:

        # Type: list
        mongodb_role_docker_device_requests:

        # Type: list
        mongodb_role_docker_device_write_bps:

        # Type: list
        mongodb_role_docker_device_write_iops:

        # Type: list
        mongodb_role_docker_devices:

        # Type: string
        mongodb_role_docker_devices_default:

        # Type: bool (true/false)
        mongodb_role_docker_privileged:

        # Type: list
        mongodb_role_docker_security_opts:

        # Networking
        # Type: list
        mongodb_role_docker_dns_opts:

        # Type: list
        mongodb_role_docker_dns_search_domains:

        # Type: list
        mongodb_role_docker_dns_servers:

        # Type: dict
        mongodb_role_docker_hosts:

        # Type: string
        mongodb_role_docker_hosts_use_common:

        # Type: string
        mongodb_role_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        mongodb_role_docker_keep_volumes:

        # Type: list
        mongodb_role_docker_mounts:

        # Type: string
        mongodb_role_docker_volume_driver:

        # Type: list
        mongodb_role_docker_volumes_from:

        # Type: string
        mongodb_role_docker_volumes_global:

        # Type: string
        mongodb_role_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        mongodb_role_docker_healthcheck:

        # Type: bool (true/false)
        mongodb_role_docker_init:

        # Type: string
        mongodb_role_docker_log_driver:

        # Type: dict
        mongodb_role_docker_log_options:

        # Type: bool (true/false)
        mongodb_role_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        mongodb_role_docker_auto_remove:

        # Type: list
        mongodb_role_docker_capabilities:

        # Type: string
        mongodb_role_docker_cgroup_parent:

        # Type: string
        mongodb_role_docker_cgroupns_mode:

        # Type: bool (true/false)
        mongodb_role_docker_cleanup:

        # Type: list
        mongodb_role_docker_commands:

        # Type: string
        mongodb_role_docker_create_timeout:

        # Type: string
        mongodb_role_docker_domainname:

        # Type: string
        mongodb_role_docker_entrypoint:

        # Type: string
        mongodb_role_docker_env_file:

        # Type: list
        mongodb_role_docker_exposed_ports:

        # Type: string
        mongodb_role_docker_force_kill:

        # Type: list
        mongodb_role_docker_groups:

        # Type: int
        mongodb_role_docker_healthy_wait_timeout:

        # Type: string
        mongodb_role_docker_ipc_mode:

        # Type: string
        mongodb_role_docker_kill_signal:

        # Type: dict
        mongodb_role_docker_labels:

        # Type: string
        mongodb_role_docker_labels_use_common:

        # Type: list
        mongodb_role_docker_links:

        # Type: bool (true/false)
        mongodb_role_docker_oom_killer:

        # Type: int
        mongodb_role_docker_oom_score_adj:

        # Type: bool (true/false)
        mongodb_role_docker_paused:

        # Type: string
        mongodb_role_docker_pid_mode:

        # Type: list
        mongodb_role_docker_ports:

        # Type: bool (true/false)
        mongodb_role_docker_read_only:

        # Type: bool (true/false)
        mongodb_role_docker_recreate:

        # Type: int
        mongodb_role_docker_restart_retries:

        # Type: string
        mongodb_role_docker_runtime:

        # Type: string
        mongodb_role_docker_shm_size:

        # Type: int
        mongodb_role_docker_stop_timeout:

        # Type: dict
        mongodb_role_docker_storage_opts:

        # Type: list
        mongodb_role_docker_sysctls:

        # Type: list
        mongodb_role_docker_tmpfs:

        # Type: list
        mongodb_role_docker_ulimits:

        # Type: string
        mongodb_role_docker_userns_mode:

        # Type: string
        mongodb_role_docker_uts:

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        mongodb2_docker_container: "{{ mongodb_name }}"

        # Image
        # Type: bool (true/false)
        mongodb2_docker_image_pull: true

        # Type: string
        mongodb2_docker_image_repo: "mongo"

        # Type: string
        mongodb2_docker_image_tag: "6"

        # Type: string
        mongodb2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='mongodb') }}:{{ lookup('role_var', '_docker_image_tag', role='mongodb') }}"

        # Envs
        # Type: dict
        mongodb2_docker_envs_default: 
          MONGO_DATA_DIR: "/data/db"
          MONGO_LOG_DIR: "/dev/null"
          MONGO_URL: "mongodb://{{ mongodb_name }}:27017/"

        # Type: dict
        mongodb2_docker_envs_custom: {}

        # Volumes
        # Type: list
        mongodb2_docker_volumes_default: 
          - "{{ mongodb_role_paths_location }}:/data/db:rw"
          - "{{ mongodb_role_paths_location }}/config:/data/configdb"

        # Type: list
        mongodb2_docker_volumes_custom: []

        # Hostname
        # Type: string
        mongodb2_docker_hostname: "{{ mongodb_name }}"

        # Networks
        # Type: string
        mongodb2_docker_networks_alias: "{{ mongodb_name }}"

        # Type: list
        mongodb2_docker_networks_default: []

        # Type: list
        mongodb2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        mongodb2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        mongodb2_docker_state: started

        # User
        # Type: string
        mongodb2_docker_user: "{{ uid }}:{{ gid }}"


        # ---- Additional Docker Options ----
        # The following advanced options are available via lookup('docker_var', ...)
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        mongodb2_docker_blkio_weight:
        # Type: int
        mongodb2_docker_cpu_period:
        # Type: int
        mongodb2_docker_cpu_quota:
        # Type: int
        mongodb2_docker_cpu_shares:
        # Type: string
        mongodb2_docker_cpus:
        # Type: string
        mongodb2_docker_cpuset_cpus:
        # Type: string
        mongodb2_docker_cpuset_mems:
        # Type: string
        mongodb2_docker_kernel_memory:
        # Type: string
        mongodb2_docker_memory:
        # Type: string
        mongodb2_docker_memory_reservation:
        # Type: string
        mongodb2_docker_memory_swap:
        # Type: int
        mongodb2_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        mongodb2_docker_cap_drop:
        # Type: list
        mongodb2_docker_device_cgroup_rules:
        # Type: list
        mongodb2_docker_device_read_bps:
        # Type: list
        mongodb2_docker_device_read_iops:
        # Type: list
        mongodb2_docker_device_requests:
        # Type: list
        mongodb2_docker_device_write_bps:
        # Type: list
        mongodb2_docker_device_write_iops:
        # Type: list
        mongodb2_docker_devices:
        # Type: string
        mongodb2_docker_devices_default:
        # Type: bool (true/false)
        mongodb2_docker_privileged:
        # Type: list
        mongodb2_docker_security_opts:

        # Networking
        # Type: list
        mongodb2_docker_dns_opts:
        # Type: list
        mongodb2_docker_dns_search_domains:
        # Type: list
        mongodb2_docker_dns_servers:
        # Type: dict
        mongodb2_docker_hosts:
        # Type: string
        mongodb2_docker_hosts_use_common:
        # Type: string
        mongodb2_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        mongodb2_docker_keep_volumes:
        # Type: list
        mongodb2_docker_mounts:
        # Type: string
        mongodb2_docker_volume_driver:
        # Type: list
        mongodb2_docker_volumes_from:
        # Type: string
        mongodb2_docker_volumes_global:
        # Type: string
        mongodb2_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        mongodb2_docker_healthcheck:
        # Type: bool (true/false)
        mongodb2_docker_init:
        # Type: string
        mongodb2_docker_log_driver:
        # Type: dict
        mongodb2_docker_log_options:
        # Type: bool (true/false)
        mongodb2_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        mongodb2_docker_auto_remove:
        # Type: list
        mongodb2_docker_capabilities:
        # Type: string
        mongodb2_docker_cgroup_parent:
        # Type: string
        mongodb2_docker_cgroupns_mode:
        # Type: bool (true/false)
        mongodb2_docker_cleanup:
        # Type: list
        mongodb2_docker_commands:
        # Type: string
        mongodb2_docker_create_timeout:
        # Type: string
        mongodb2_docker_domainname:
        # Type: string
        mongodb2_docker_entrypoint:
        # Type: string
        mongodb2_docker_env_file:
        # Type: list
        mongodb2_docker_exposed_ports:
        # Type: string
        mongodb2_docker_force_kill:
        # Type: list
        mongodb2_docker_groups:
        # Type: int
        mongodb2_docker_healthy_wait_timeout:
        # Type: string
        mongodb2_docker_ipc_mode:
        # Type: string
        mongodb2_docker_kill_signal:
        # Type: dict
        mongodb2_docker_labels:
        # Type: string
        mongodb2_docker_labels_use_common:
        # Type: list
        mongodb2_docker_links:
        # Type: bool (true/false)
        mongodb2_docker_oom_killer:
        # Type: int
        mongodb2_docker_oom_score_adj:
        # Type: bool (true/false)
        mongodb2_docker_paused:
        # Type: string
        mongodb2_docker_pid_mode:
        # Type: list
        mongodb2_docker_ports:
        # Type: bool (true/false)
        mongodb2_docker_read_only:
        # Type: bool (true/false)
        mongodb2_docker_recreate:
        # Type: int
        mongodb2_docker_restart_retries:
        # Type: string
        mongodb2_docker_runtime:
        # Type: string
        mongodb2_docker_shm_size:
        # Type: int
        mongodb2_docker_stop_timeout:
        # Type: dict
        mongodb2_docker_storage_opts:
        # Type: list
        mongodb2_docker_sysctls:
        # Type: list
        mongodb2_docker_tmpfs:
        # Type: list
        mongodb2_docker_ulimits:
        # Type: string
        mongodb2_docker_userns_mode:
        # Type: string
        mongodb2_docker_uts:

        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        mongodb_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        mongodb_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        mongodb_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        mongodb_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        mongodb_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        mongodb_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        mongodb_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        mongodb_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        mongodb_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        mongodb_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        mongodb_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        mongodb_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        mongodb_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        mongodb_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        mongodb_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        mongodb_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        mongodb_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            mongodb_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "mongodb2.{{ user.domain }}"
              - "mongodb.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            mongodb_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'mongodb2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `mongodb2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        mongodb2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        mongodb2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        mongodb2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        mongodb2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        mongodb2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        mongodb2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        mongodb2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        mongodb2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        mongodb2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        mongodb2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        mongodb2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        mongodb2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        mongodb2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        mongodb2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        mongodb2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        mongodb2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        mongodb2_web_scheme:

        ```

        1.  Example:

            ```yaml
            mongodb2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "mongodb2.{{ user.domain }}"
              - "mongodb.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            mongodb2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'mongodb2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

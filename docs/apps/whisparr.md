---
hide:
  - tags
tags:
  - whisparr
---

# Whisparr

## What is it?

[Whisparr](https://wiki.servarr.com/whisparr) is an adult movie collection manager for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new movies and will interface with clients and indexers to grab, sort, and rename them. It can also be configured to automatically upgrade the quality of existing files in the library when a better quality format becomes available. Note that only one type of a given movie is supported. If you want both an 4k version and 1080p version of a given movie you will need multiple instances.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into whisparr with the email and password you set up upon installation.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://wiki.servarr.com/whisparr){: .header-icons } | [:octicons-link-16: Docs](https://wiki.servarr.com/en/whisparr/quick-start-guide){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Whisparr/Whisparr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/whisparr){: .header-icons }|

### 1. Installation

``` shell

sb install whisparr

```

### 2. URL

- To access whisparr, visit `https://whisparr.xDOMAIN_NAMEx`

### 3. Setup

Whisparr works more or less the same as the other apps in the arr suite, since this is a fork of sonarr.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `whisparr_instances`.

    === "Role-level Override"

        Applies to all instances of whisparr:

        ```yaml
        whisparr_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `whisparr2`):

        ```yaml
        whisparr2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `whisparr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `whisparr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        whisparr_instances: ["whisparr"]

        ```

    === "Example"

        ```yaml
        # Type: list
        whisparr_instances: ["whisparr", "whisparr2"]

        ```

??? example "Settings"

    === "Role-level"

        ```yaml
        # Type: bool (true/false)
        whisparr_role_external_auth: true

        ```

    === "Instance-level"

        ```yaml
        # Type: bool (true/false)
        whisparr2_external_auth: true

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        whisparr_paths_folder: "{{ whisparr_name }}"

        # Type: string
        whisparr_paths_location: "{{ server_appdata_path }}/{{ whisparr_paths_folder }}"

        # Type: string
        whisparr_paths_config_location: "{{ whisparr_paths_location }}/config.xml"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        whisparr_paths_folder: "{{ whisparr_name }}"

        # Type: string
        whisparr_paths_location: "{{ server_appdata_path }}/{{ whisparr_paths_folder }}"

        # Type: string
        whisparr_paths_config_location: "{{ whisparr_paths_location }}/config.xml"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        whisparr_role_web_subdomain: "{{ whisparr_name }}"

        # Type: string
        whisparr_role_web_domain: "{{ user.domain }}"

        # Type: string
        whisparr_role_web_port: "6969"

        # Type: string
        whisparr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='whisparr') + '.' + lookup('role_var', '_web_domain', role='whisparr')
                                if (lookup('role_var', '_web_subdomain', role='whisparr') | length > 0)
                                else lookup('role_var', '_web_domain', role='whisparr')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        whisparr2_web_subdomain: "{{ whisparr_name }}"

        # Type: string
        whisparr2_web_domain: "{{ user.domain }}"

        # Type: string
        whisparr2_web_port: "6969"

        # Type: string
        whisparr2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='whisparr') + '.' + lookup('role_var', '_web_domain', role='whisparr')
                            if (lookup('role_var', '_web_subdomain', role='whisparr') | length > 0)
                            else lookup('role_var', '_web_domain', role='whisparr')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        whisparr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='whisparr') }}"

        # Type: string
        whisparr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='whisparr') }}"

        # Type: bool (true/false)
        whisparr_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        whisparr2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='whisparr') }}"

        # Type: string
        whisparr2_dns_zone: "{{ lookup('role_var', '_web_domain', role='whisparr') }}"

        # Type: bool (true/false)
        whisparr2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        whisparr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        whisparr_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                      + (',themepark-' + whisparr_name
                                                        if (lookup('role_var', '_themepark_enabled', role='whisparr') and global_themepark_plugin_enabled)
                                                        else '') }}"

        # Type: string
        whisparr_role_traefik_middleware_custom: ""

        # Type: string
        whisparr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        whisparr_role_traefik_enabled: true

        # Type: bool (true/false)
        whisparr_role_traefik_api_enabled: true

        # Type: string
        whisparr_role_traefik_api_endpoint: "PathPrefix(`/api`)"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        whisparr2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        whisparr2_traefik_middleware_default: "{{ traefik_default_middleware
                                                  + (',themepark-' + whisparr_name
                                                    if (lookup('role_var', '_themepark_enabled', role='whisparr') and global_themepark_plugin_enabled)
                                                    else '') }}"

        # Type: string
        whisparr2_traefik_middleware_custom: ""

        # Type: string
        whisparr2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        whisparr2_traefik_enabled: true

        # Type: bool (true/false)
        whisparr2_traefik_api_enabled: true

        # Type: string
        whisparr2_traefik_api_endpoint: "PathPrefix(`/api`)"

        ```

??? example "Theme"

    === "Role-level"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        whisparr_role_themepark_enabled: false

        # Type: string
        whisparr_role_themepark_app: "whisparr"

        # Type: string
        whisparr_role_themepark_theme: "{{ global_themepark_theme }}"

        # Type: string
        whisparr_role_themepark_domain: "{{ global_themepark_domain }}"

        # Type: list
        whisparr_role_themepark_addons: []

        ```

    === "Instance-level"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        whisparr2_themepark_enabled: false

        # Type: string
        whisparr2_themepark_app: "whisparr"

        # Type: string
        whisparr2_themepark_theme: "{{ global_themepark_theme }}"

        # Type: string
        whisparr2_themepark_domain: "{{ global_themepark_domain }}"

        # Type: list
        whisparr2_themepark_addons: []

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        whisparr_role_docker_container: "{{ whisparr_name }}"

        # Image
        # Type: bool (true/false)
        whisparr_role_docker_image_pull: true

        # Type: string
        whisparr_role_docker_image_repo: "ghcr.io/hotio/whisparr"

        # Type: string
        whisparr_role_docker_image_tag: "nightly"

        # Type: string
        whisparr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='whisparr') }}:{{ lookup('role_var', '_docker_image_tag', role='whisparr') }}"

        # Envs
        # Type: dict
        whisparr_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          UMASK: "002"
          TZ: "{{ tz }}"

        # Type: dict
        whisparr_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        whisparr_role_docker_volumes_default: 
          - "{{ whisparr_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"

        # Type: list
        whisparr_role_docker_volumes_custom: []

        # Labels
        # Type: dict
        whisparr_role_docker_labels_default: {}

        # Type: dict
        whisparr_role_docker_labels_custom: {}

        # Hostname
        # Type: string
        whisparr_role_docker_hostname: "{{ whisparr_name }}"

        # Networks
        # Type: string
        whisparr_role_docker_networks_alias: "{{ whisparr_name }}"

        # Type: list
        whisparr_role_docker_networks_default: []

        # Type: list
        whisparr_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        whisparr_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        whisparr_role_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via create_docker_container
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        whisparr_role_docker_blkio_weight:

        # Type: int
        whisparr_role_docker_cpu_period:

        # Type: int
        whisparr_role_docker_cpu_quota:

        # Type: int
        whisparr_role_docker_cpu_shares:

        # Type: string
        whisparr_role_docker_cpus:

        # Type: string
        whisparr_role_docker_cpuset_cpus:

        # Type: string
        whisparr_role_docker_cpuset_mems:

        # Type: string
        whisparr_role_docker_kernel_memory:

        # Type: string
        whisparr_role_docker_memory:

        # Type: string
        whisparr_role_docker_memory_reservation:

        # Type: string
        whisparr_role_docker_memory_swap:

        # Type: int
        whisparr_role_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        whisparr_role_docker_cap_drop:

        # Type: list
        whisparr_role_docker_device_cgroup_rules:

        # Type: list
        whisparr_role_docker_device_read_bps:

        # Type: list
        whisparr_role_docker_device_read_iops:

        # Type: list
        whisparr_role_docker_device_requests:

        # Type: list
        whisparr_role_docker_device_write_bps:

        # Type: list
        whisparr_role_docker_device_write_iops:

        # Type: list
        whisparr_role_docker_devices:

        # Type: string
        whisparr_role_docker_devices_default:

        # Type: bool (true/false)
        whisparr_role_docker_privileged:

        # Type: list
        whisparr_role_docker_security_opts:

        # Networking
        # Type: list
        whisparr_role_docker_dns_opts:

        # Type: list
        whisparr_role_docker_dns_search_domains:

        # Type: list
        whisparr_role_docker_dns_servers:

        # Type: dict
        whisparr_role_docker_hosts:

        # Type: string
        whisparr_role_docker_hosts_use_common:

        # Type: string
        whisparr_role_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        whisparr_role_docker_keep_volumes:

        # Type: list
        whisparr_role_docker_mounts:

        # Type: string
        whisparr_role_docker_volume_driver:

        # Type: list
        whisparr_role_docker_volumes_from:

        # Type: string
        whisparr_role_docker_volumes_global:

        # Type: string
        whisparr_role_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        whisparr_role_docker_healthcheck:

        # Type: bool (true/false)
        whisparr_role_docker_init:

        # Type: string
        whisparr_role_docker_log_driver:

        # Type: dict
        whisparr_role_docker_log_options:

        # Type: bool (true/false)
        whisparr_role_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        whisparr_role_docker_auto_remove:

        # Type: list
        whisparr_role_docker_capabilities:

        # Type: string
        whisparr_role_docker_cgroup_parent:

        # Type: string
        whisparr_role_docker_cgroupns_mode:

        # Type: bool (true/false)
        whisparr_role_docker_cleanup:

        # Type: list
        whisparr_role_docker_commands:

        # Type: string
        whisparr_role_docker_create_timeout:

        # Type: string
        whisparr_role_docker_domainname:

        # Type: string
        whisparr_role_docker_entrypoint:

        # Type: string
        whisparr_role_docker_env_file:

        # Type: list
        whisparr_role_docker_exposed_ports:

        # Type: string
        whisparr_role_docker_force_kill:

        # Type: list
        whisparr_role_docker_groups:

        # Type: int
        whisparr_role_docker_healthy_wait_timeout:

        # Type: string
        whisparr_role_docker_ipc_mode:

        # Type: string
        whisparr_role_docker_kill_signal:

        # Type: string
        whisparr_role_docker_labels_use_common:

        # Type: list
        whisparr_role_docker_links:

        # Type: bool (true/false)
        whisparr_role_docker_oom_killer:

        # Type: int
        whisparr_role_docker_oom_score_adj:

        # Type: bool (true/false)
        whisparr_role_docker_paused:

        # Type: string
        whisparr_role_docker_pid_mode:

        # Type: list
        whisparr_role_docker_ports:

        # Type: bool (true/false)
        whisparr_role_docker_read_only:

        # Type: bool (true/false)
        whisparr_role_docker_recreate:

        # Type: int
        whisparr_role_docker_restart_retries:

        # Type: string
        whisparr_role_docker_runtime:

        # Type: string
        whisparr_role_docker_shm_size:

        # Type: int
        whisparr_role_docker_stop_timeout:

        # Type: dict
        whisparr_role_docker_storage_opts:

        # Type: list
        whisparr_role_docker_sysctls:

        # Type: list
        whisparr_role_docker_tmpfs:

        # Type: list
        whisparr_role_docker_ulimits:

        # Type: string
        whisparr_role_docker_user:

        # Type: string
        whisparr_role_docker_userns_mode:

        # Type: string
        whisparr_role_docker_uts:

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        whisparr2_docker_container: "{{ whisparr_name }}"

        # Image
        # Type: bool (true/false)
        whisparr2_docker_image_pull: true

        # Type: string
        whisparr2_docker_image_repo: "ghcr.io/hotio/whisparr"

        # Type: string
        whisparr2_docker_image_tag: "nightly"

        # Type: string
        whisparr2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='whisparr') }}:{{ lookup('role_var', '_docker_image_tag', role='whisparr') }}"

        # Envs
        # Type: dict
        whisparr2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          UMASK: "002"
          TZ: "{{ tz }}"

        # Type: dict
        whisparr2_docker_envs_custom: {}

        # Volumes
        # Type: list
        whisparr2_docker_volumes_default: 
          - "{{ whisparr_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"

        # Type: list
        whisparr2_docker_volumes_custom: []

        # Labels
        # Type: dict
        whisparr2_docker_labels_default: {}

        # Type: dict
        whisparr2_docker_labels_custom: {}

        # Hostname
        # Type: string
        whisparr2_docker_hostname: "{{ whisparr_name }}"

        # Networks
        # Type: string
        whisparr2_docker_networks_alias: "{{ whisparr_name }}"

        # Type: list
        whisparr2_docker_networks_default: []

        # Type: list
        whisparr2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        whisparr2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        whisparr2_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via lookup('docker_var', ...)
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        whisparr2_docker_blkio_weight:
        # Type: int
        whisparr2_docker_cpu_period:
        # Type: int
        whisparr2_docker_cpu_quota:
        # Type: int
        whisparr2_docker_cpu_shares:
        # Type: string
        whisparr2_docker_cpus:
        # Type: string
        whisparr2_docker_cpuset_cpus:
        # Type: string
        whisparr2_docker_cpuset_mems:
        # Type: string
        whisparr2_docker_kernel_memory:
        # Type: string
        whisparr2_docker_memory:
        # Type: string
        whisparr2_docker_memory_reservation:
        # Type: string
        whisparr2_docker_memory_swap:
        # Type: int
        whisparr2_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        whisparr2_docker_cap_drop:
        # Type: list
        whisparr2_docker_device_cgroup_rules:
        # Type: list
        whisparr2_docker_device_read_bps:
        # Type: list
        whisparr2_docker_device_read_iops:
        # Type: list
        whisparr2_docker_device_requests:
        # Type: list
        whisparr2_docker_device_write_bps:
        # Type: list
        whisparr2_docker_device_write_iops:
        # Type: list
        whisparr2_docker_devices:
        # Type: string
        whisparr2_docker_devices_default:
        # Type: bool (true/false)
        whisparr2_docker_privileged:
        # Type: list
        whisparr2_docker_security_opts:

        # Networking
        # Type: list
        whisparr2_docker_dns_opts:
        # Type: list
        whisparr2_docker_dns_search_domains:
        # Type: list
        whisparr2_docker_dns_servers:
        # Type: dict
        whisparr2_docker_hosts:
        # Type: string
        whisparr2_docker_hosts_use_common:
        # Type: string
        whisparr2_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        whisparr2_docker_keep_volumes:
        # Type: list
        whisparr2_docker_mounts:
        # Type: string
        whisparr2_docker_volume_driver:
        # Type: list
        whisparr2_docker_volumes_from:
        # Type: string
        whisparr2_docker_volumes_global:
        # Type: string
        whisparr2_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        whisparr2_docker_healthcheck:
        # Type: bool (true/false)
        whisparr2_docker_init:
        # Type: string
        whisparr2_docker_log_driver:
        # Type: dict
        whisparr2_docker_log_options:
        # Type: bool (true/false)
        whisparr2_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        whisparr2_docker_auto_remove:
        # Type: list
        whisparr2_docker_capabilities:
        # Type: string
        whisparr2_docker_cgroup_parent:
        # Type: string
        whisparr2_docker_cgroupns_mode:
        # Type: bool (true/false)
        whisparr2_docker_cleanup:
        # Type: list
        whisparr2_docker_commands:
        # Type: string
        whisparr2_docker_create_timeout:
        # Type: string
        whisparr2_docker_domainname:
        # Type: string
        whisparr2_docker_entrypoint:
        # Type: string
        whisparr2_docker_env_file:
        # Type: list
        whisparr2_docker_exposed_ports:
        # Type: string
        whisparr2_docker_force_kill:
        # Type: list
        whisparr2_docker_groups:
        # Type: int
        whisparr2_docker_healthy_wait_timeout:
        # Type: string
        whisparr2_docker_ipc_mode:
        # Type: string
        whisparr2_docker_kill_signal:
        # Type: string
        whisparr2_docker_labels_use_common:
        # Type: list
        whisparr2_docker_links:
        # Type: bool (true/false)
        whisparr2_docker_oom_killer:
        # Type: int
        whisparr2_docker_oom_score_adj:
        # Type: bool (true/false)
        whisparr2_docker_paused:
        # Type: string
        whisparr2_docker_pid_mode:
        # Type: list
        whisparr2_docker_ports:
        # Type: bool (true/false)
        whisparr2_docker_read_only:
        # Type: bool (true/false)
        whisparr2_docker_recreate:
        # Type: int
        whisparr2_docker_restart_retries:
        # Type: string
        whisparr2_docker_runtime:
        # Type: string
        whisparr2_docker_shm_size:
        # Type: int
        whisparr2_docker_stop_timeout:
        # Type: dict
        whisparr2_docker_storage_opts:
        # Type: list
        whisparr2_docker_sysctls:
        # Type: list
        whisparr2_docker_tmpfs:
        # Type: list
        whisparr2_docker_ulimits:
        # Type: string
        whisparr2_docker_user:
        # Type: string
        whisparr2_docker_userns_mode:
        # Type: string
        whisparr2_docker_uts:

        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        whisparr_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        whisparr_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        whisparr_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        whisparr_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        whisparr_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        whisparr_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        whisparr_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        whisparr_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        whisparr_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        whisparr_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        whisparr_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        whisparr_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        whisparr_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        whisparr_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        whisparr_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        whisparr_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        whisparr_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            whisparr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "whisparr2.{{ user.domain }}"
              - "whisparr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            whisparr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'whisparr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `whisparr2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        whisparr2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        whisparr2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        whisparr2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        whisparr2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        whisparr2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        whisparr2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        whisparr2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        whisparr2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        whisparr2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        whisparr2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        whisparr2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        whisparr2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        whisparr2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        whisparr2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        whisparr2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        whisparr2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        whisparr2_web_scheme:

        ```

        1.  Example:

            ```yaml
            whisparr2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "whisparr2.{{ user.domain }}"
              - "whisparr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            whisparr2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'whisparr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

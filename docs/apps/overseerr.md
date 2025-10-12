---
hide:
  - tags
tags:
  - overseerr
---

# Overseerr

# What is it?

[Overseerr](https://overseerr.dev/) is a request management and media discovery tool built to work with your existing Plex ecosystem.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://overseerr.dev/){: .header-icons } | [:octicons-link-16: Docs](https://docs.overseerr.dev/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/sct/overseerr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/sctx/overseerr){: .header-icons }|

## 1. URL

- To access Overseerr, visit `https://overseerr._yourdomain.com_`

## 2. Settings

This setup needs to take place **AFTER** you've set up Plex, Radarr, and Sonarr, since it involves connections to all three of those.

You will need your API Keys from both Radarr and Sonarr.

1. Click "Sign In" and sign into your Plex account.

![](../images/overseerr/01-overseerr.png)

1. Click the "refresh" icon, then select your Plex server from the dropdown.  Click "Save Changes" to retrieve the libraries from Plex.

![](../images/overseerr/02-overseerr.png)

1. Scroll down and flip the switch on the libraries you want to expose for requests and discovery.  Click "Continue".

![](../images/overseerr/03-overseerr.png)

1. Click "Add Radarr Server".

![](../images/overseerr/04-overseerr.png)

1. On this screen:
    1. Check "Default server"
    2. Enter a name
    3. Enter `radarr` as the hostname
    4. Enter your Radarr API Key
    5. Click "Test" to connect to Radarr and retrieve Quality Profiles, etc.

![](../images/overseerr/05-overseerr.png)

1. Select a Quality, Root Folder, and Minimum Availability, then click "Add Server".  This will return you to the screen from the previous step. Click "Add Sonarr Server"

![](../images/overseerr/06-overseerr.png)

1. On this screen:
    1. Check "Default server"
    2. Enter a name
    3. Enter `sonarr` as the hostname
    4. Enter your Sonarr API Key
    5. Scroll down and click "Test" to connect to Sonarr and retrieve Quality Profiles, etc.

![](../images/overseerr/07-overseerr.png)

1. Select a Quality, Root Folder, and Minimum Availability for standard and Anime series.  Click  "Add Server".

![](../images/overseerr/08-overseerr.png)

1. Click "Finish Setup"

![](../images/overseerr/09-overseerr.png)

1. Click "Settings" over on the left.

![](../images/overseerr/10-overseerr.png)

1. Click "Users" on the left, then "Import Users From Plex"

![](../images/overseerr/11-overseerr.png)

1. Setup is complete.

![](../images/overseerr/12-overseerr.png)

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `overseerr_instances`.

    === "Role-level Override"

        Applies to all instances of overseerr:

        ```yaml
        overseerr_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `overseerr2`):

        ```yaml
        overseerr2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `overseerr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `overseerr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        overseerr_instances: ["overseerr"]

        ```

    === "Example"

        ```yaml
        # Type: list
        overseerr_instances: ["overseerr", "overseerr2"]

        ```

??? example "Settings"

    === "Role-level"

        ```yaml
        # Type: string
        overseerr_role_log_level: "info"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        overseerr2_log_level: "info"

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        overseerr_role_paths_folder: "{{ overseerr_name }}"

        # Type: string
        overseerr_role_paths_location: "{{ server_appdata_path }}/{{ overseerr_role_paths_folder }}"

        # Type: string
        overseerr_role_paths_cache: "{{ overseerr_role_paths_location }}/cache"

        # Type: string
        overseerr_role_paths_config_location: "{{ overseerr_role_paths_location }}/settings.json"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        overseerr2_paths_folder: "{{ overseerr_name }}"

        # Type: string
        overseerr2_paths_location: "{{ server_appdata_path }}/{{ overseerr_role_paths_folder }}"

        # Type: string
        overseerr2_paths_cache: "{{ overseerr_role_paths_location }}/cache"

        # Type: string
        overseerr2_paths_config_location: "{{ overseerr_role_paths_location }}/settings.json"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        overseerr_role_web_subdomain: "{{ overseerr_name }}"

        # Type: string
        overseerr_role_web_domain: "{{ user.domain }}"

        # Type: string
        overseerr_role_web_port: "5055"

        # Type: string
        overseerr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='overseerr') + '.' + lookup('role_var', '_web_domain', role='overseerr')
                                 if (lookup('role_var', '_web_subdomain', role='overseerr') | length > 0)
                                 else lookup('role_var', '_web_domain', role='overseerr')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        overseerr2_web_subdomain: "{{ overseerr_name }}"

        # Type: string
        overseerr2_web_domain: "{{ user.domain }}"

        # Type: string
        overseerr2_web_port: "5055"

        # Type: string
        overseerr2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='overseerr') + '.' + lookup('role_var', '_web_domain', role='overseerr')
                             if (lookup('role_var', '_web_subdomain', role='overseerr') | length > 0)
                             else lookup('role_var', '_web_domain', role='overseerr')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        overseerr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='overseerr') }}"

        # Type: string
        overseerr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='overseerr') }}"

        # Type: bool (true/false)
        overseerr_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        overseerr2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='overseerr') }}"

        # Type: string
        overseerr2_dns_zone: "{{ lookup('role_var', '_web_domain', role='overseerr') }}"

        # Type: bool (true/false)
        overseerr2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        overseerr_role_traefik_sso_middleware: ""

        # Type: string
        overseerr_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                       + (',themepark-' + overseerr_name
                                                         if (lookup('role_var', '_themepark_enabled', role='overseerr') and global_themepark_plugin_enabled)
                                                         else '') }}"

        # Type: string
        overseerr_role_traefik_middleware_custom: ""

        # Type: string
        overseerr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        overseerr_role_traefik_enabled: true

        # Type: bool (true/false)
        overseerr_role_traefik_api_enabled: false

        # Type: string
        overseerr_role_traefik_api_endpoint: ""

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        overseerr2_traefik_sso_middleware: ""

        # Type: string
        overseerr2_traefik_middleware_default: "{{ traefik_default_middleware
                                                   + (',themepark-' + overseerr_name
                                                     if (lookup('role_var', '_themepark_enabled', role='overseerr') and global_themepark_plugin_enabled)
                                                     else '') }}"

        # Type: string
        overseerr2_traefik_middleware_custom: ""

        # Type: string
        overseerr2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        overseerr2_traefik_enabled: true

        # Type: bool (true/false)
        overseerr2_traefik_api_enabled: false

        # Type: string
        overseerr2_traefik_api_endpoint: ""

        ```

??? example "Theme"

    === "Role-level"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        overseerr_role_themepark_enabled: false

        # Type: string
        overseerr_role_themepark_app: "overseerr"

        # Type: string
        overseerr_role_themepark_theme: "{{ global_themepark_theme }}"

        # Type: string
        overseerr_role_themepark_domain: "{{ global_themepark_domain }}"

        # Type: list
        overseerr_role_themepark_addons: []

        ```

    === "Instance-level"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        overseerr2_themepark_enabled: false

        # Type: string
        overseerr2_themepark_app: "overseerr"

        # Type: string
        overseerr2_themepark_theme: "{{ global_themepark_theme }}"

        # Type: string
        overseerr2_themepark_domain: "{{ global_themepark_domain }}"

        # Type: list
        overseerr2_themepark_addons: []

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        overseerr_role_docker_container: "{{ overseerr_name }}"

        # Image
        # Type: bool (true/false)
        overseerr_role_docker_image_pull: true

        # Type: string
        overseerr_role_docker_image_repo: "sctx/overseerr"

        # Type: string
        overseerr_role_docker_image_tag: "latest"

        # Type: string
        overseerr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='overseerr') }}:{{ lookup('role_var', '_docker_image_tag', role='overseerr') }}"

        # Envs
        # Type: dict
        overseerr_role_docker_envs_default: 
          UMASK: "002"
          TZ: "{{ tz }}"
          LOG_LEVEL: "{{ lookup('role_var', '_log_level', role='overseerr') }}"

        # Type: dict
        overseerr_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        overseerr_role_docker_volumes_default: 
          - "{{ overseerr_role_paths_location }}:/app/config"

        # Type: list
        overseerr_role_docker_volumes_custom: []

        # Labels
        # Type: dict
        overseerr_role_docker_labels_default: {}

        # Type: dict
        overseerr_role_docker_labels_custom: {}

        # Hostname
        # Type: string
        overseerr_role_docker_hostname: "{{ overseerr_name }}"

        # Networks
        # Type: string
        overseerr_role_docker_networks_alias: "{{ overseerr_name }}"

        # Type: list
        overseerr_role_docker_networks_default: []

        # Type: list
        overseerr_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        overseerr_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        overseerr_role_docker_state: started

        # User
        # Type: string
        overseerr_role_docker_user: "{{ uid }}:{{ gid }}"


        # ---- Additional Docker Options ----
        # The following advanced options are available via create_docker_container
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        overseerr_role_docker_blkio_weight:

        # Type: int
        overseerr_role_docker_cpu_period:

        # Type: int
        overseerr_role_docker_cpu_quota:

        # Type: int
        overseerr_role_docker_cpu_shares:

        # Type: string
        overseerr_role_docker_cpus:

        # Type: string
        overseerr_role_docker_cpuset_cpus:

        # Type: string
        overseerr_role_docker_cpuset_mems:

        # Type: string
        overseerr_role_docker_kernel_memory:

        # Type: string
        overseerr_role_docker_memory:

        # Type: string
        overseerr_role_docker_memory_reservation:

        # Type: string
        overseerr_role_docker_memory_swap:

        # Type: int
        overseerr_role_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        overseerr_role_docker_cap_drop:

        # Type: list
        overseerr_role_docker_device_cgroup_rules:

        # Type: list
        overseerr_role_docker_device_read_bps:

        # Type: list
        overseerr_role_docker_device_read_iops:

        # Type: list
        overseerr_role_docker_device_requests:

        # Type: list
        overseerr_role_docker_device_write_bps:

        # Type: list
        overseerr_role_docker_device_write_iops:

        # Type: list
        overseerr_role_docker_devices:

        # Type: string
        overseerr_role_docker_devices_default:

        # Type: bool (true/false)
        overseerr_role_docker_privileged:

        # Type: list
        overseerr_role_docker_security_opts:

        # Networking
        # Type: list
        overseerr_role_docker_dns_opts:

        # Type: list
        overseerr_role_docker_dns_search_domains:

        # Type: list
        overseerr_role_docker_dns_servers:

        # Type: dict
        overseerr_role_docker_hosts:

        # Type: string
        overseerr_role_docker_hosts_use_common:

        # Type: string
        overseerr_role_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        overseerr_role_docker_keep_volumes:

        # Type: list
        overseerr_role_docker_mounts:

        # Type: string
        overseerr_role_docker_volume_driver:

        # Type: list
        overseerr_role_docker_volumes_from:

        # Type: string
        overseerr_role_docker_volumes_global:

        # Type: string
        overseerr_role_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        overseerr_role_docker_healthcheck:

        # Type: bool (true/false)
        overseerr_role_docker_init:

        # Type: string
        overseerr_role_docker_log_driver:

        # Type: dict
        overseerr_role_docker_log_options:

        # Type: bool (true/false)
        overseerr_role_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        overseerr_role_docker_auto_remove:

        # Type: list
        overseerr_role_docker_capabilities:

        # Type: string
        overseerr_role_docker_cgroup_parent:

        # Type: string
        overseerr_role_docker_cgroupns_mode:

        # Type: bool (true/false)
        overseerr_role_docker_cleanup:

        # Type: list
        overseerr_role_docker_commands:

        # Type: string
        overseerr_role_docker_create_timeout:

        # Type: string
        overseerr_role_docker_domainname:

        # Type: string
        overseerr_role_docker_entrypoint:

        # Type: string
        overseerr_role_docker_env_file:

        # Type: list
        overseerr_role_docker_exposed_ports:

        # Type: string
        overseerr_role_docker_force_kill:

        # Type: list
        overseerr_role_docker_groups:

        # Type: int
        overseerr_role_docker_healthy_wait_timeout:

        # Type: string
        overseerr_role_docker_ipc_mode:

        # Type: string
        overseerr_role_docker_kill_signal:

        # Type: string
        overseerr_role_docker_labels_use_common:

        # Type: list
        overseerr_role_docker_links:

        # Type: bool (true/false)
        overseerr_role_docker_oom_killer:

        # Type: int
        overseerr_role_docker_oom_score_adj:

        # Type: bool (true/false)
        overseerr_role_docker_paused:

        # Type: string
        overseerr_role_docker_pid_mode:

        # Type: list
        overseerr_role_docker_ports:

        # Type: bool (true/false)
        overseerr_role_docker_read_only:

        # Type: bool (true/false)
        overseerr_role_docker_recreate:

        # Type: int
        overseerr_role_docker_restart_retries:

        # Type: string
        overseerr_role_docker_runtime:

        # Type: string
        overseerr_role_docker_shm_size:

        # Type: int
        overseerr_role_docker_stop_timeout:

        # Type: dict
        overseerr_role_docker_storage_opts:

        # Type: list
        overseerr_role_docker_sysctls:

        # Type: list
        overseerr_role_docker_tmpfs:

        # Type: list
        overseerr_role_docker_ulimits:

        # Type: string
        overseerr_role_docker_userns_mode:

        # Type: string
        overseerr_role_docker_uts:

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        overseerr2_docker_container: "{{ overseerr_name }}"

        # Image
        # Type: bool (true/false)
        overseerr2_docker_image_pull: true

        # Type: string
        overseerr2_docker_image_repo: "sctx/overseerr"

        # Type: string
        overseerr2_docker_image_tag: "latest"

        # Type: string
        overseerr2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='overseerr') }}:{{ lookup('role_var', '_docker_image_tag', role='overseerr') }}"

        # Envs
        # Type: dict
        overseerr2_docker_envs_default: 
          UMASK: "002"
          TZ: "{{ tz }}"
          LOG_LEVEL: "{{ lookup('role_var', '_log_level', role='overseerr') }}"

        # Type: dict
        overseerr2_docker_envs_custom: {}

        # Volumes
        # Type: list
        overseerr2_docker_volumes_default: 
          - "{{ overseerr_role_paths_location }}:/app/config"

        # Type: list
        overseerr2_docker_volumes_custom: []

        # Labels
        # Type: dict
        overseerr2_docker_labels_default: {}

        # Type: dict
        overseerr2_docker_labels_custom: {}

        # Hostname
        # Type: string
        overseerr2_docker_hostname: "{{ overseerr_name }}"

        # Networks
        # Type: string
        overseerr2_docker_networks_alias: "{{ overseerr_name }}"

        # Type: list
        overseerr2_docker_networks_default: []

        # Type: list
        overseerr2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        overseerr2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        overseerr2_docker_state: started

        # User
        # Type: string
        overseerr2_docker_user: "{{ uid }}:{{ gid }}"


        # ---- Additional Docker Options ----
        # The following advanced options are available via lookup('docker_var', ...)
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        overseerr2_docker_blkio_weight:
        # Type: int
        overseerr2_docker_cpu_period:
        # Type: int
        overseerr2_docker_cpu_quota:
        # Type: int
        overseerr2_docker_cpu_shares:
        # Type: string
        overseerr2_docker_cpus:
        # Type: string
        overseerr2_docker_cpuset_cpus:
        # Type: string
        overseerr2_docker_cpuset_mems:
        # Type: string
        overseerr2_docker_kernel_memory:
        # Type: string
        overseerr2_docker_memory:
        # Type: string
        overseerr2_docker_memory_reservation:
        # Type: string
        overseerr2_docker_memory_swap:
        # Type: int
        overseerr2_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        overseerr2_docker_cap_drop:
        # Type: list
        overseerr2_docker_device_cgroup_rules:
        # Type: list
        overseerr2_docker_device_read_bps:
        # Type: list
        overseerr2_docker_device_read_iops:
        # Type: list
        overseerr2_docker_device_requests:
        # Type: list
        overseerr2_docker_device_write_bps:
        # Type: list
        overseerr2_docker_device_write_iops:
        # Type: list
        overseerr2_docker_devices:
        # Type: string
        overseerr2_docker_devices_default:
        # Type: bool (true/false)
        overseerr2_docker_privileged:
        # Type: list
        overseerr2_docker_security_opts:

        # Networking
        # Type: list
        overseerr2_docker_dns_opts:
        # Type: list
        overseerr2_docker_dns_search_domains:
        # Type: list
        overseerr2_docker_dns_servers:
        # Type: dict
        overseerr2_docker_hosts:
        # Type: string
        overseerr2_docker_hosts_use_common:
        # Type: string
        overseerr2_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        overseerr2_docker_keep_volumes:
        # Type: list
        overseerr2_docker_mounts:
        # Type: string
        overseerr2_docker_volume_driver:
        # Type: list
        overseerr2_docker_volumes_from:
        # Type: string
        overseerr2_docker_volumes_global:
        # Type: string
        overseerr2_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        overseerr2_docker_healthcheck:
        # Type: bool (true/false)
        overseerr2_docker_init:
        # Type: string
        overseerr2_docker_log_driver:
        # Type: dict
        overseerr2_docker_log_options:
        # Type: bool (true/false)
        overseerr2_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        overseerr2_docker_auto_remove:
        # Type: list
        overseerr2_docker_capabilities:
        # Type: string
        overseerr2_docker_cgroup_parent:
        # Type: string
        overseerr2_docker_cgroupns_mode:
        # Type: bool (true/false)
        overseerr2_docker_cleanup:
        # Type: list
        overseerr2_docker_commands:
        # Type: string
        overseerr2_docker_create_timeout:
        # Type: string
        overseerr2_docker_domainname:
        # Type: string
        overseerr2_docker_entrypoint:
        # Type: string
        overseerr2_docker_env_file:
        # Type: list
        overseerr2_docker_exposed_ports:
        # Type: string
        overseerr2_docker_force_kill:
        # Type: list
        overseerr2_docker_groups:
        # Type: int
        overseerr2_docker_healthy_wait_timeout:
        # Type: string
        overseerr2_docker_ipc_mode:
        # Type: string
        overseerr2_docker_kill_signal:
        # Type: string
        overseerr2_docker_labels_use_common:
        # Type: list
        overseerr2_docker_links:
        # Type: bool (true/false)
        overseerr2_docker_oom_killer:
        # Type: int
        overseerr2_docker_oom_score_adj:
        # Type: bool (true/false)
        overseerr2_docker_paused:
        # Type: string
        overseerr2_docker_pid_mode:
        # Type: list
        overseerr2_docker_ports:
        # Type: bool (true/false)
        overseerr2_docker_read_only:
        # Type: bool (true/false)
        overseerr2_docker_recreate:
        # Type: int
        overseerr2_docker_restart_retries:
        # Type: string
        overseerr2_docker_runtime:
        # Type: string
        overseerr2_docker_shm_size:
        # Type: int
        overseerr2_docker_stop_timeout:
        # Type: dict
        overseerr2_docker_storage_opts:
        # Type: list
        overseerr2_docker_sysctls:
        # Type: list
        overseerr2_docker_tmpfs:
        # Type: list
        overseerr2_docker_ulimits:
        # Type: string
        overseerr2_docker_userns_mode:
        # Type: string
        overseerr2_docker_uts:

        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        overseerr_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        overseerr_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        overseerr_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        overseerr_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        overseerr_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        overseerr_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        overseerr_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        overseerr_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        overseerr_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        overseerr_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        overseerr_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        overseerr_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        overseerr_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        overseerr_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        overseerr_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        overseerr_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        overseerr_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            overseerr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "overseerr2.{{ user.domain }}"
              - "overseerr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            overseerr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'overseerr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `overseerr2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        overseerr2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        overseerr2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        overseerr2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        overseerr2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        overseerr2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        overseerr2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        overseerr2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        overseerr2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        overseerr2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        overseerr2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        overseerr2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        overseerr2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        overseerr2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        overseerr2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        overseerr2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        overseerr2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        overseerr2_web_scheme:

        ```

        1.  Example:

            ```yaml
            overseerr2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "overseerr2.{{ user.domain }}"
              - "overseerr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            overseerr2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'overseerr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

## Next

Are you setting Saltbox up for the first time?  Continue to [Portainer](portainer.md).

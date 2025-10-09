---
hide:
  - tags
tags:
  - bazarr
---

# Bazarr

## What is it?

[Bazarr](https://www.bazarr.media/) is a companion application to Sonarr and Radarr that manages and downloads subtitles based on your requirements.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.bazarr.media/){: .header-icons } | [:octicons-link-16: Docs](https://wiki.bazarr.media/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/hotio/bazarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/bazarr){: .header-icons }|

### 1. Installation

``` shell

sb install bazarr

```

### 2. URL

- To access Bazarr, visit `https://bazarr._yourdomain.com_`

### 3. Setup

- [:octicons-link-16: Documentation](https://wiki.bazarr.media/){: .header-icons }

- [:octicons-link-16: TraSH Guides](https://trash-guides.info/Bazarr/)

There are some settings that - depending on your specific setup - should be adapted to reduce API calls down to a managable level.

Please refer to the official documentation for an explanation of the settings. Some - potentially out of date(!) - settings are documented in the [FAQs](../faq/bazarr.md).

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `bazarr_instances`.

    === "Role-level Override"

        Applies to all instances of bazarr:

        ```yaml
        bazarr_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `bazarr2`):

        ```yaml
        bazarr2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        bazarr_instances: ["bazarr"]

        ```

    === "Example"

        ```yaml
        # Type: list
        bazarr_instances: ["bazarr", "bazarr2"]

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        bazarr_role_paths_folder: "{{ bazarr_name }}"

        # Type: string
        bazarr_role_paths_location: "{{ server_appdata_path }}/{{ bazarr_role_paths_folder }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        bazarr2_paths_folder: "{{ bazarr_name }}"

        # Type: string
        bazarr2_paths_location: "{{ server_appdata_path }}/{{ bazarr_role_paths_folder }}"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        bazarr_role_web_subdomain: "{{ bazarr_name }}"

        # Type: string
        bazarr_role_web_domain: "{{ user.domain }}"

        # Type: string
        bazarr_role_web_port: "6767"

        # Type: string
        bazarr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='bazarr') + '.' + lookup('role_var', '_web_domain', role='bazarr')
                              if (lookup('role_var', '_web_subdomain', role='bazarr') | length > 0)
                              else lookup('role_var', '_web_domain', role='bazarr')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        bazarr2_web_subdomain: "{{ bazarr_name }}"

        # Type: string
        bazarr2_web_domain: "{{ user.domain }}"

        # Type: string
        bazarr2_web_port: "6767"

        # Type: string
        bazarr2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='bazarr') + '.' + lookup('role_var', '_web_domain', role='bazarr')
                          if (lookup('role_var', '_web_subdomain', role='bazarr') | length > 0)
                          else lookup('role_var', '_web_domain', role='bazarr')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        bazarr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='bazarr') }}"

        # Type: string
        bazarr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='bazarr') }}"

        # Type: bool (true/false)
        bazarr_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        bazarr2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='bazarr') }}"

        # Type: string
        bazarr2_dns_zone: "{{ lookup('role_var', '_web_domain', role='bazarr') }}"

        # Type: bool (true/false)
        bazarr2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        bazarr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        bazarr_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                    + (',themepark-' + bazarr_name
                                                      if (lookup('role_var', '_themepark_enabled', role='bazarr') and global_themepark_plugin_enabled)
                                                      else '') }}"

        # Type: string
        bazarr_role_traefik_middleware_custom: ""

        # Type: string
        bazarr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        bazarr_role_traefik_enabled: true

        # Type: bool (true/false)
        bazarr_role_traefik_api_enabled: true

        # Type: string
        bazarr_role_traefik_api_endpoint: "PathPrefix(`/api`)"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        bazarr2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        bazarr2_traefik_middleware_default: "{{ traefik_default_middleware
                                                + (',themepark-' + bazarr_name
                                                  if (lookup('role_var', '_themepark_enabled', role='bazarr') and global_themepark_plugin_enabled)
                                                  else '') }}"

        # Type: string
        bazarr2_traefik_middleware_custom: ""

        # Type: string
        bazarr2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        bazarr2_traefik_enabled: true

        # Type: bool (true/false)
        bazarr2_traefik_api_enabled: true

        # Type: string
        bazarr2_traefik_api_endpoint: "PathPrefix(`/api`)"

        ```

??? example "Theme"

    === "Role-level"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        bazarr_role_themepark_enabled: false

        # Type: string
        bazarr_role_themepark_app: "bazarr"

        # Type: string
        bazarr_role_themepark_theme: "{{ global_themepark_theme }}"

        # Type: string
        bazarr_role_themepark_domain: "{{ global_themepark_domain }}"

        # Type: list
        bazarr_role_themepark_addons: []

        ```

    === "Instance-level"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        bazarr2_themepark_enabled: false

        # Type: string
        bazarr2_themepark_app: "bazarr"

        # Type: string
        bazarr2_themepark_theme: "{{ global_themepark_theme }}"

        # Type: string
        bazarr2_themepark_domain: "{{ global_themepark_domain }}"

        # Type: list
        bazarr2_themepark_addons: []

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        bazarr_role_docker_container: "{{ bazarr_name }}"

        # Image
        # Type: bool (true/false)
        bazarr_role_docker_image_pull: true

        # Type: string
        bazarr_role_docker_image_repo: "ghcr.io/hotio/bazarr"

        # Type: string
        bazarr_role_docker_image_tag: "latest"

        # Type: string
        bazarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='bazarr') }}:{{ lookup('role_var', '_docker_image_tag', role='bazarr') }}"

        # Envs
        # Type: dict
        bazarr_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          UMASK: "002"
          TZ: "{{ tz }}"

        # Type: dict
        bazarr_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        bazarr_role_docker_volumes_default: 
          - "{{ bazarr_role_paths_location }}:/config"
          - "/opt/scripts:/scripts"

        # Type: list
        bazarr_role_docker_volumes_legacy: 
          - "/mnt/unionfs/Media/Movies:/movies"
          - "/mnt/unionfs/Media/TV:/tv"

        # Type: list
        bazarr_role_docker_volumes_custom: []

        # Labels
        # Type: dict
        bazarr_role_docker_labels_default: {}

        # Type: dict
        bazarr_role_docker_labels_custom: {}

        # Hostname
        # Type: string
        bazarr_role_docker_hostname: "{{ bazarr_name }}"

        # Networks
        # Type: string
        bazarr_role_docker_networks_alias: "{{ bazarr_name }}"

        # Type: list
        bazarr_role_docker_networks_default: []

        # Type: list
        bazarr_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        bazarr_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        bazarr_role_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via create_docker_container
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        bazarr_role_docker_blkio_weight:

        # Type: int
        bazarr_role_docker_cpu_period:

        # Type: int
        bazarr_role_docker_cpu_quota:

        # Type: int
        bazarr_role_docker_cpu_shares:

        # Type: string
        bazarr_role_docker_cpus:

        # Type: string
        bazarr_role_docker_cpuset_cpus:

        # Type: string
        bazarr_role_docker_cpuset_mems:

        # Type: string
        bazarr_role_docker_kernel_memory:

        # Type: string
        bazarr_role_docker_memory:

        # Type: string
        bazarr_role_docker_memory_reservation:

        # Type: string
        bazarr_role_docker_memory_swap:

        # Type: int
        bazarr_role_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        bazarr_role_docker_cap_drop:

        # Type: list
        bazarr_role_docker_device_cgroup_rules:

        # Type: list
        bazarr_role_docker_device_read_bps:

        # Type: list
        bazarr_role_docker_device_read_iops:

        # Type: list
        bazarr_role_docker_device_requests:

        # Type: list
        bazarr_role_docker_device_write_bps:

        # Type: list
        bazarr_role_docker_device_write_iops:

        # Type: list
        bazarr_role_docker_devices:

        # Type: string
        bazarr_role_docker_devices_default:

        # Type: bool (true/false)
        bazarr_role_docker_privileged:

        # Type: list
        bazarr_role_docker_security_opts:

        # Networking
        # Type: list
        bazarr_role_docker_dns_opts:

        # Type: list
        bazarr_role_docker_dns_search_domains:

        # Type: list
        bazarr_role_docker_dns_servers:

        # Type: dict
        bazarr_role_docker_hosts:

        # Type: string
        bazarr_role_docker_hosts_use_common:

        # Type: string
        bazarr_role_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        bazarr_role_docker_keep_volumes:

        # Type: list
        bazarr_role_docker_mounts:

        # Type: string
        bazarr_role_docker_volume_driver:

        # Type: list
        bazarr_role_docker_volumes_from:

        # Type: string
        bazarr_role_docker_volumes_global:

        # Type: string
        bazarr_role_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        bazarr_role_docker_healthcheck:

        # Type: bool (true/false)
        bazarr_role_docker_init:

        # Type: string
        bazarr_role_docker_log_driver:

        # Type: dict
        bazarr_role_docker_log_options:

        # Type: bool (true/false)
        bazarr_role_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        bazarr_role_docker_auto_remove:

        # Type: list
        bazarr_role_docker_capabilities:

        # Type: string
        bazarr_role_docker_cgroup_parent:

        # Type: string
        bazarr_role_docker_cgroupns_mode:

        # Type: bool (true/false)
        bazarr_role_docker_cleanup:

        # Type: list
        bazarr_role_docker_commands:

        # Type: string
        bazarr_role_docker_create_timeout:

        # Type: string
        bazarr_role_docker_domainname:

        # Type: string
        bazarr_role_docker_entrypoint:

        # Type: string
        bazarr_role_docker_env_file:

        # Type: list
        bazarr_role_docker_exposed_ports:

        # Type: string
        bazarr_role_docker_force_kill:

        # Type: list
        bazarr_role_docker_groups:

        # Type: int
        bazarr_role_docker_healthy_wait_timeout:

        # Type: string
        bazarr_role_docker_ipc_mode:

        # Type: string
        bazarr_role_docker_kill_signal:

        # Type: string
        bazarr_role_docker_labels_use_common:

        # Type: list
        bazarr_role_docker_links:

        # Type: bool (true/false)
        bazarr_role_docker_oom_killer:

        # Type: int
        bazarr_role_docker_oom_score_adj:

        # Type: bool (true/false)
        bazarr_role_docker_paused:

        # Type: string
        bazarr_role_docker_pid_mode:

        # Type: list
        bazarr_role_docker_ports:

        # Type: bool (true/false)
        bazarr_role_docker_read_only:

        # Type: bool (true/false)
        bazarr_role_docker_recreate:

        # Type: int
        bazarr_role_docker_restart_retries:

        # Type: string
        bazarr_role_docker_runtime:

        # Type: string
        bazarr_role_docker_shm_size:

        # Type: int
        bazarr_role_docker_stop_timeout:

        # Type: dict
        bazarr_role_docker_storage_opts:

        # Type: list
        bazarr_role_docker_sysctls:

        # Type: list
        bazarr_role_docker_tmpfs:

        # Type: list
        bazarr_role_docker_ulimits:

        # Type: string
        bazarr_role_docker_user:

        # Type: string
        bazarr_role_docker_userns_mode:

        # Type: string
        bazarr_role_docker_uts:

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        bazarr2_docker_container: "{{ bazarr_name }}"

        # Image
        # Type: bool (true/false)
        bazarr2_docker_image_pull: true

        # Type: string
        bazarr2_docker_image_repo: "ghcr.io/hotio/bazarr"

        # Type: string
        bazarr2_docker_image_tag: "latest"

        # Type: string
        bazarr2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='bazarr') }}:{{ lookup('role_var', '_docker_image_tag', role='bazarr') }}"

        # Envs
        # Type: dict
        bazarr2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          UMASK: "002"
          TZ: "{{ tz }}"

        # Type: dict
        bazarr2_docker_envs_custom: {}

        # Volumes
        # Type: list
        bazarr2_docker_volumes_default: 
          - "{{ bazarr_role_paths_location }}:/config"
          - "/opt/scripts:/scripts"

        # Type: list
        bazarr2_docker_volumes_legacy: 
          - "/mnt/unionfs/Media/Movies:/movies"
          - "/mnt/unionfs/Media/TV:/tv"

        # Type: list
        bazarr2_docker_volumes_custom: []

        # Labels
        # Type: dict
        bazarr2_docker_labels_default: {}

        # Type: dict
        bazarr2_docker_labels_custom: {}

        # Hostname
        # Type: string
        bazarr2_docker_hostname: "{{ bazarr_name }}"

        # Networks
        # Type: string
        bazarr2_docker_networks_alias: "{{ bazarr_name }}"

        # Type: list
        bazarr2_docker_networks_default: []

        # Type: list
        bazarr2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        bazarr2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        bazarr2_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via lookup('docker_var', ...)
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        bazarr2_docker_blkio_weight:
        # Type: int
        bazarr2_docker_cpu_period:
        # Type: int
        bazarr2_docker_cpu_quota:
        # Type: int
        bazarr2_docker_cpu_shares:
        # Type: string
        bazarr2_docker_cpus:
        # Type: string
        bazarr2_docker_cpuset_cpus:
        # Type: string
        bazarr2_docker_cpuset_mems:
        # Type: string
        bazarr2_docker_kernel_memory:
        # Type: string
        bazarr2_docker_memory:
        # Type: string
        bazarr2_docker_memory_reservation:
        # Type: string
        bazarr2_docker_memory_swap:
        # Type: int
        bazarr2_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        bazarr2_docker_cap_drop:
        # Type: list
        bazarr2_docker_device_cgroup_rules:
        # Type: list
        bazarr2_docker_device_read_bps:
        # Type: list
        bazarr2_docker_device_read_iops:
        # Type: list
        bazarr2_docker_device_requests:
        # Type: list
        bazarr2_docker_device_write_bps:
        # Type: list
        bazarr2_docker_device_write_iops:
        # Type: list
        bazarr2_docker_devices:
        # Type: string
        bazarr2_docker_devices_default:
        # Type: bool (true/false)
        bazarr2_docker_privileged:
        # Type: list
        bazarr2_docker_security_opts:

        # Networking
        # Type: list
        bazarr2_docker_dns_opts:
        # Type: list
        bazarr2_docker_dns_search_domains:
        # Type: list
        bazarr2_docker_dns_servers:
        # Type: dict
        bazarr2_docker_hosts:
        # Type: string
        bazarr2_docker_hosts_use_common:
        # Type: string
        bazarr2_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        bazarr2_docker_keep_volumes:
        # Type: list
        bazarr2_docker_mounts:
        # Type: string
        bazarr2_docker_volume_driver:
        # Type: list
        bazarr2_docker_volumes_from:
        # Type: string
        bazarr2_docker_volumes_global:
        # Type: string
        bazarr2_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        bazarr2_docker_healthcheck:
        # Type: bool (true/false)
        bazarr2_docker_init:
        # Type: string
        bazarr2_docker_log_driver:
        # Type: dict
        bazarr2_docker_log_options:
        # Type: bool (true/false)
        bazarr2_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        bazarr2_docker_auto_remove:
        # Type: list
        bazarr2_docker_capabilities:
        # Type: string
        bazarr2_docker_cgroup_parent:
        # Type: string
        bazarr2_docker_cgroupns_mode:
        # Type: bool (true/false)
        bazarr2_docker_cleanup:
        # Type: list
        bazarr2_docker_commands:
        # Type: string
        bazarr2_docker_create_timeout:
        # Type: string
        bazarr2_docker_domainname:
        # Type: string
        bazarr2_docker_entrypoint:
        # Type: string
        bazarr2_docker_env_file:
        # Type: list
        bazarr2_docker_exposed_ports:
        # Type: string
        bazarr2_docker_force_kill:
        # Type: list
        bazarr2_docker_groups:
        # Type: int
        bazarr2_docker_healthy_wait_timeout:
        # Type: string
        bazarr2_docker_ipc_mode:
        # Type: string
        bazarr2_docker_kill_signal:
        # Type: string
        bazarr2_docker_labels_use_common:
        # Type: list
        bazarr2_docker_links:
        # Type: bool (true/false)
        bazarr2_docker_oom_killer:
        # Type: int
        bazarr2_docker_oom_score_adj:
        # Type: bool (true/false)
        bazarr2_docker_paused:
        # Type: string
        bazarr2_docker_pid_mode:
        # Type: list
        bazarr2_docker_ports:
        # Type: bool (true/false)
        bazarr2_docker_read_only:
        # Type: bool (true/false)
        bazarr2_docker_recreate:
        # Type: int
        bazarr2_docker_restart_retries:
        # Type: string
        bazarr2_docker_runtime:
        # Type: string
        bazarr2_docker_shm_size:
        # Type: int
        bazarr2_docker_stop_timeout:
        # Type: dict
        bazarr2_docker_storage_opts:
        # Type: list
        bazarr2_docker_sysctls:
        # Type: list
        bazarr2_docker_tmpfs:
        # Type: list
        bazarr2_docker_ulimits:
        # Type: string
        bazarr2_docker_user:
        # Type: string
        bazarr2_docker_userns_mode:
        # Type: string
        bazarr2_docker_uts:

        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        bazarr_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        bazarr_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        bazarr_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        bazarr_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        bazarr_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        bazarr_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        bazarr_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        bazarr_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        bazarr_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        bazarr_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        bazarr_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        bazarr_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        bazarr_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        bazarr_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        bazarr_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        bazarr_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        bazarr_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            bazarr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "bazarr2.{{ user.domain }}"
              - "bazarr.otherdomain.tld"
            ```
            
            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries
            

        2.  Example:

            ```yaml
            bazarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'bazarr2.' + user.domain }}`)"
            ```
            
            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule
            

    === "Instance-level"

        Override for a specific instance (e.g., `bazarr2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        bazarr2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        bazarr2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        bazarr2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        bazarr2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        bazarr2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        bazarr2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        bazarr2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        bazarr2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        bazarr2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        bazarr2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        bazarr2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        bazarr2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        bazarr2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        bazarr2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        bazarr2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        bazarr2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        bazarr2_web_scheme:

        ```

        1.  Example:

            ```yaml
            bazarr2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "bazarr2.{{ user.domain }}"
              - "bazarr.otherdomain.tld"
            ```
            
            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries
            

        2.  Example:

            ```yaml
            bazarr2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'bazarr2.' + user.domain }}`)"
            ```
            
            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule
            

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

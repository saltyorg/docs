---
hide:
  - tags
tags:
  - prowlarr
---

# Prowlarr

## What is it?

[Prowlarr](https://prowlarr.com/) is an indexer manager/proxy built on the popular arr .net/reactjs base stack to integrate with your various PVR apps. Prowlarr supports management of both Torrent Trackers and Usenet Indexers. It integrates seamlessly with Lidarr, Mylar3, Radarr, and Sonarr offering complete management of your indexers with no per app Indexer setup required (we do it all).

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://prowlarr.com/){: .header-icons } | [:octicons-link-16: Docs](https://wiki.servarr.com/prowlarr){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Prowlarr/Prowlarr/){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/prowlarr){: .header-icons }|

### 1. Installation

``` shell

sb install prowlarr

```

### 2. URL

- To access Prowlarr, visit `https://prowlarr._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        prowlarr_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    prowlarr_name: prowlarr

    ```

??? example "Settings"

    ```yaml
    # Type: bool (true/false)
    prowlarr_role_external_auth: true

    ```

??? example "Paths"

    ```yaml
    # Type: string
    prowlarr_role_paths_folder: "{{ prowlarr_name }}"

    # Type: string
    prowlarr_role_paths_location: "{{ server_appdata_path }}/{{ prowlarr_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    prowlarr_role_web_subdomain: "{{ prowlarr_name }}"

    # Type: string
    prowlarr_role_web_domain: "{{ user.domain }}"

    # Type: string
    prowlarr_role_web_port: "9696"

    # Type: string
    prowlarr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='prowlarr') + '.' + lookup('role_var', '_web_domain', role='prowlarr')
                            if (lookup('role_var', '_web_subdomain', role='prowlarr') | length > 0)
                            else lookup('role_var', '_web_domain', role='prowlarr')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    prowlarr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='prowlarr') }}"

    # Type: string
    prowlarr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='prowlarr') }}"

    # Type: bool (true/false)
    prowlarr_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    prowlarr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    prowlarr_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                  + (',themepark-' + prowlarr_name
                                                    if (lookup('role_var', '_themepark_enabled', role='prowlarr') and global_themepark_plugin_enabled)
                                                    else '') }}"

    # Type: string
    prowlarr_role_traefik_middleware_custom: ""

    # Type: string
    prowlarr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    prowlarr_role_traefik_enabled: true

    # Type: bool (true/false)
    prowlarr_role_traefik_api_enabled: true

    # Type: string
    prowlarr_role_traefik_api_endpoint: "PathRegexp(`/[0-9]+/api`) || PathRegexp(`/[0-9]+/download`) || PathPrefix(`/api`) || PathPrefix(`/ping`)"

    ```

??? example "Theme"

    ```yaml
    # Options can be found at https://github.com/themepark-dev/theme.park
    # Type: bool (true/false)
    prowlarr_role_themepark_enabled: false

    # Type: string
    prowlarr_role_themepark_app: "prowlarr"

    # Type: string
    prowlarr_role_themepark_theme: "{{ global_themepark_theme }}"

    # Type: string
    prowlarr_role_themepark_domain: "{{ global_themepark_domain }}"

    # Type: list
    prowlarr_role_themepark_addons: []

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    prowlarr_role_docker_container: "{{ prowlarr_name }}"

    # Image
    # Type: bool (true/false)
    prowlarr_role_docker_image_pull: true

    # Type: string
    prowlarr_role_docker_image_tag: "release"

    # Type: string
    prowlarr_role_docker_image_repo: "ghcr.io/hotio/prowlarr"

    # Type: string
    prowlarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='prowlarr') }}:{{ lookup('role_var', '_docker_image_tag', role='prowlarr') }}"

    # Envs
    # Type: dict
    prowlarr_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      UMASK: "002"
      TZ: "{{ tz }}"

    # Type: dict
    prowlarr_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    prowlarr_role_docker_volumes_default: 
      - "{{ prowlarr_role_paths_location }}:/config"

    # Type: list
    prowlarr_role_docker_volumes_custom: []

    # Labels
    # Type: dict
    prowlarr_role_docker_labels_default: {}

    # Type: dict
    prowlarr_role_docker_labels_custom: {}

    # Hostname
    # Type: string
    prowlarr_role_docker_hostname: "{{ prowlarr_name }}"

    # Networks
    # Type: string
    prowlarr_role_docker_networks_alias: "{{ prowlarr_name }}"

    # Type: list
    prowlarr_role_docker_networks_default: []

    # Type: list
    prowlarr_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    prowlarr_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    prowlarr_role_docker_state: started


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    prowlarr_role_docker_blkio_weight:

    # Type: int
    prowlarr_role_docker_cpu_period:

    # Type: int
    prowlarr_role_docker_cpu_quota:

    # Type: int
    prowlarr_role_docker_cpu_shares:

    # Type: string
    prowlarr_role_docker_cpus:

    # Type: string
    prowlarr_role_docker_cpuset_cpus:

    # Type: string
    prowlarr_role_docker_cpuset_mems:

    # Type: string
    prowlarr_role_docker_kernel_memory:

    # Type: string
    prowlarr_role_docker_memory:

    # Type: string
    prowlarr_role_docker_memory_reservation:

    # Type: string
    prowlarr_role_docker_memory_swap:

    # Type: int
    prowlarr_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    prowlarr_role_docker_cap_drop:

    # Type: list
    prowlarr_role_docker_device_cgroup_rules:

    # Type: list
    prowlarr_role_docker_device_read_bps:

    # Type: list
    prowlarr_role_docker_device_read_iops:

    # Type: list
    prowlarr_role_docker_device_requests:

    # Type: list
    prowlarr_role_docker_device_write_bps:

    # Type: list
    prowlarr_role_docker_device_write_iops:

    # Type: list
    prowlarr_role_docker_devices:

    # Type: string
    prowlarr_role_docker_devices_default:

    # Type: bool (true/false)
    prowlarr_role_docker_privileged:

    # Type: list
    prowlarr_role_docker_security_opts:


    # Networking
    # Type: list
    prowlarr_role_docker_dns_opts:

    # Type: list
    prowlarr_role_docker_dns_search_domains:

    # Type: list
    prowlarr_role_docker_dns_servers:

    # Type: dict
    prowlarr_role_docker_hosts:

    # Type: string
    prowlarr_role_docker_hosts_use_common:

    # Type: string
    prowlarr_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    prowlarr_role_docker_keep_volumes:

    # Type: list
    prowlarr_role_docker_mounts:

    # Type: string
    prowlarr_role_docker_volume_driver:

    # Type: list
    prowlarr_role_docker_volumes_from:

    # Type: string
    prowlarr_role_docker_volumes_global:

    # Type: string
    prowlarr_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    prowlarr_role_docker_healthcheck:

    # Type: bool (true/false)
    prowlarr_role_docker_init:

    # Type: string
    prowlarr_role_docker_log_driver:

    # Type: dict
    prowlarr_role_docker_log_options:

    # Type: bool (true/false)
    prowlarr_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    prowlarr_role_docker_auto_remove:

    # Type: list
    prowlarr_role_docker_capabilities:

    # Type: string
    prowlarr_role_docker_cgroup_parent:

    # Type: string
    prowlarr_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    prowlarr_role_docker_cleanup:

    # Type: list
    prowlarr_role_docker_commands:

    # Type: string
    prowlarr_role_docker_create_timeout:

    # Type: string
    prowlarr_role_docker_domainname:

    # Type: string
    prowlarr_role_docker_entrypoint:

    # Type: string
    prowlarr_role_docker_env_file:

    # Type: list
    prowlarr_role_docker_exposed_ports:

    # Type: string
    prowlarr_role_docker_force_kill:

    # Type: list
    prowlarr_role_docker_groups:

    # Type: int
    prowlarr_role_docker_healthy_wait_timeout:

    # Type: string
    prowlarr_role_docker_ipc_mode:

    # Type: string
    prowlarr_role_docker_kill_signal:

    # Type: string
    prowlarr_role_docker_labels_use_common:

    # Type: list
    prowlarr_role_docker_links:

    # Type: bool (true/false)
    prowlarr_role_docker_oom_killer:

    # Type: int
    prowlarr_role_docker_oom_score_adj:

    # Type: bool (true/false)
    prowlarr_role_docker_paused:

    # Type: string
    prowlarr_role_docker_pid_mode:

    # Type: list
    prowlarr_role_docker_ports:

    # Type: bool (true/false)
    prowlarr_role_docker_read_only:

    # Type: bool (true/false)
    prowlarr_role_docker_recreate:

    # Type: int
    prowlarr_role_docker_restart_retries:

    # Type: string
    prowlarr_role_docker_runtime:

    # Type: string
    prowlarr_role_docker_shm_size:

    # Type: int
    prowlarr_role_docker_stop_timeout:

    # Type: dict
    prowlarr_role_docker_storage_opts:

    # Type: list
    prowlarr_role_docker_sysctls:

    # Type: list
    prowlarr_role_docker_tmpfs:

    # Type: list
    prowlarr_role_docker_ulimits:

    # Type: string
    prowlarr_role_docker_user:

    # Type: string
    prowlarr_role_docker_userns_mode:

    # Type: string
    prowlarr_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    prowlarr_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    prowlarr_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    prowlarr_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    prowlarr_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    prowlarr_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    prowlarr_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    prowlarr_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    prowlarr_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    prowlarr_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    prowlarr_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    prowlarr_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    prowlarr_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    prowlarr_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    prowlarr_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    prowlarr_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    prowlarr_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    prowlarr_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        prowlarr_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "prowlarr2.{{ user.domain }}"
          - "prowlarr.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        prowlarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'prowlarr2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

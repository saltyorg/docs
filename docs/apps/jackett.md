---
hide:
  - tags
tags:
  - jackett
---

# Jackett

# What is it?

[Jackett](https://github.com/Jackett/Jackett) (based on the original work of Matthew Little aka _zone117x_) is a web-based app that acts like a proxy server, directing search queries from download clients (e.g. Sonarr) to torrent tracker sites and sending the results back. Download clients can also use Jackett to fetch RSS feeds from tracker sites. Finally, it can be used as a meta search tool to find torrents, right from within the app.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| :material-home: Project home | [:octicons-link-16: Docs](https://github.com/Jackett/Jackett/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Jackett/Jackett){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/jackett){: .header-icons }|

_Note: If you don't use torrents, you may just skip this page._

## 1. URL

- To access Jackett, visit `http://jackett._yourdomain.com_`

## 2. Settings

   ![](../images/jackett-settings.png)

### Disabling Auto Update

Under "Jackett Configuration":

1. Check "Disable auto update".

1. Check "External access".

1. Click "Apply server settings".

1. The page will now reload.

## 3. Adding Indexers to Sonarr/Radarr

Under "Configured Indexers":

1. Click "Add Indexer" to add your favorite indexers (i.e. [torrent trackers](../reference/usenet-torrent.md)).

2. When adding indexers into [Sonarr](../apps/sonarr.md#__tabbed_3_2)/[Radarr](../apps/radarr.md#__tabbed_3_2), you will need:

    1. Indexer's Torznab Feed

         - Copy this by clicking on "Copy Torznab Feed" button next to the Indexer.

         - You will need to replace...

           - `https` with `http`

           - `jackett.yourdomain.com` with `jackett:9117`

    2. Jacket API Key

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        jackett_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    jackett_name: jackett

    ```

??? example "Paths"

    ```yaml
    # Type: string
    jackett_role_paths_folder: "{{ jackett_name }}"

    # Type: string
    jackett_role_paths_location: "{{ server_appdata_path }}/{{ jackett_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    jackett_role_web_subdomain: "{{ jackett_name }}"

    # Type: string
    jackett_role_web_domain: "{{ user.domain }}"

    # Type: string
    jackett_role_web_port: "9117"

    # Type: string
    jackett_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='jackett') + '.' + lookup('role_var', '_web_domain', role='jackett')
                           if (lookup('role_var', '_web_subdomain', role='jackett') | length > 0)
                           else lookup('role_var', '_web_domain', role='jackett')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    jackett_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='jackett') }}"

    # Type: string
    jackett_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='jackett') }}"

    # Type: bool (true/false)
    jackett_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    jackett_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    jackett_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                 + (',themepark-' + jackett_name
                                                   if (lookup('role_var', '_themepark_enabled', role='jackett') and global_themepark_plugin_enabled)
                                                   else '') }}"

    # Type: string
    jackett_role_traefik_middleware_custom: ""

    # Type: string
    jackett_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    jackett_role_traefik_enabled: true

    # Type: bool (true/false)
    jackett_role_traefik_api_enabled: true

    # Type: string
    jackett_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/dl`)"

    ```

??? example "Theme"

    ```yaml
    # Options can be found at https://github.com/themepark-dev/theme.park
    # Type: bool (true/false)
    jackett_role_themepark_enabled: false

    # Type: string
    jackett_role_themepark_app: "jackett"

    # Type: string
    jackett_role_themepark_theme: "{{ global_themepark_theme }}"

    # Type: string
    jackett_role_themepark_domain: "{{ global_themepark_domain }}"

    # Type: list
    jackett_role_themepark_addons: []

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    jackett_role_docker_container: "{{ jackett_name }}"

    # Image
    # Type: bool (true/false)
    jackett_role_docker_image_pull: true

    # Type: string
    jackett_role_docker_image_repo: "ghcr.io/hotio/jackett"

    # Type: string
    jackett_role_docker_image_tag: "release"

    # Type: string
    jackett_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='jackett') }}:{{ lookup('role_var', '_docker_image_tag', role='jackett') }}"

    # Envs
    # Type: dict
    jackett_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      UMASK: "002"
      TZ: "{{ tz }}"

    # Type: dict
    jackett_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    jackett_role_docker_volumes_default: 
      - "{{ jackett_role_paths_location }}:/config"

    # Type: list
    jackett_role_docker_volumes_custom: []

    # Labels
    # Type: dict
    jackett_role_docker_labels_default: {}

    # Type: dict
    jackett_role_docker_labels_custom: {}

    # Hostname
    # Type: string
    jackett_role_docker_hostname: "{{ jackett_name }}"

    # Networks
    # Type: string
    jackett_role_docker_networks_alias: "{{ jackett_name }}"

    # Type: list
    jackett_role_docker_networks_default: []

    # Type: list
    jackett_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    jackett_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    jackett_role_docker_state: started


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    jackett_role_docker_blkio_weight:

    # Type: int
    jackett_role_docker_cpu_period:

    # Type: int
    jackett_role_docker_cpu_quota:

    # Type: int
    jackett_role_docker_cpu_shares:

    # Type: string
    jackett_role_docker_cpus:

    # Type: string
    jackett_role_docker_cpuset_cpus:

    # Type: string
    jackett_role_docker_cpuset_mems:

    # Type: string
    jackett_role_docker_kernel_memory:

    # Type: string
    jackett_role_docker_memory:

    # Type: string
    jackett_role_docker_memory_reservation:

    # Type: string
    jackett_role_docker_memory_swap:

    # Type: int
    jackett_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    jackett_role_docker_cap_drop:

    # Type: list
    jackett_role_docker_device_cgroup_rules:

    # Type: list
    jackett_role_docker_device_read_bps:

    # Type: list
    jackett_role_docker_device_read_iops:

    # Type: list
    jackett_role_docker_device_requests:

    # Type: list
    jackett_role_docker_device_write_bps:

    # Type: list
    jackett_role_docker_device_write_iops:

    # Type: list
    jackett_role_docker_devices:

    # Type: string
    jackett_role_docker_devices_default:

    # Type: bool (true/false)
    jackett_role_docker_privileged:

    # Type: list
    jackett_role_docker_security_opts:


    # Networking
    # Type: list
    jackett_role_docker_dns_opts:

    # Type: list
    jackett_role_docker_dns_search_domains:

    # Type: list
    jackett_role_docker_dns_servers:

    # Type: dict
    jackett_role_docker_hosts:

    # Type: string
    jackett_role_docker_hosts_use_common:

    # Type: string
    jackett_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    jackett_role_docker_keep_volumes:

    # Type: list
    jackett_role_docker_mounts:

    # Type: string
    jackett_role_docker_volume_driver:

    # Type: list
    jackett_role_docker_volumes_from:

    # Type: string
    jackett_role_docker_volumes_global:

    # Type: string
    jackett_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    jackett_role_docker_healthcheck:

    # Type: bool (true/false)
    jackett_role_docker_init:

    # Type: string
    jackett_role_docker_log_driver:

    # Type: dict
    jackett_role_docker_log_options:

    # Type: bool (true/false)
    jackett_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    jackett_role_docker_auto_remove:

    # Type: list
    jackett_role_docker_capabilities:

    # Type: string
    jackett_role_docker_cgroup_parent:

    # Type: string
    jackett_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    jackett_role_docker_cleanup:

    # Type: list
    jackett_role_docker_commands:

    # Type: string
    jackett_role_docker_create_timeout:

    # Type: string
    jackett_role_docker_domainname:

    # Type: string
    jackett_role_docker_entrypoint:

    # Type: string
    jackett_role_docker_env_file:

    # Type: list
    jackett_role_docker_exposed_ports:

    # Type: string
    jackett_role_docker_force_kill:

    # Type: list
    jackett_role_docker_groups:

    # Type: int
    jackett_role_docker_healthy_wait_timeout:

    # Type: string
    jackett_role_docker_ipc_mode:

    # Type: string
    jackett_role_docker_kill_signal:

    # Type: string
    jackett_role_docker_labels_use_common:

    # Type: list
    jackett_role_docker_links:

    # Type: bool (true/false)
    jackett_role_docker_oom_killer:

    # Type: int
    jackett_role_docker_oom_score_adj:

    # Type: bool (true/false)
    jackett_role_docker_paused:

    # Type: string
    jackett_role_docker_pid_mode:

    # Type: list
    jackett_role_docker_ports:

    # Type: bool (true/false)
    jackett_role_docker_read_only:

    # Type: bool (true/false)
    jackett_role_docker_recreate:

    # Type: int
    jackett_role_docker_restart_retries:

    # Type: string
    jackett_role_docker_runtime:

    # Type: string
    jackett_role_docker_shm_size:

    # Type: int
    jackett_role_docker_stop_timeout:

    # Type: dict
    jackett_role_docker_storage_opts:

    # Type: list
    jackett_role_docker_sysctls:

    # Type: list
    jackett_role_docker_tmpfs:

    # Type: list
    jackett_role_docker_ulimits:

    # Type: string
    jackett_role_docker_user:

    # Type: string
    jackett_role_docker_userns_mode:

    # Type: string
    jackett_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    jackett_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    jackett_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    jackett_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    jackett_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    jackett_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    jackett_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    jackett_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    jackett_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    jackett_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    jackett_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    jackett_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    jackett_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    jackett_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    jackett_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    jackett_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    jackett_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    jackett_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        jackett_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "jackett2.{{ user.domain }}"
          - "jackett.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        jackett_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'jackett2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

## Next

Are you setting Saltbox up for the first time?  Continue to [Plex Media Server](plex.md).

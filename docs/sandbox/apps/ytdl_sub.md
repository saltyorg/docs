---
hide:
  - tags
tags:
  - ytdl-sub
  - youtube
  - downloads
---

# ytdl-sub

## What is it?

[ytdl-sub](https://github.com/jmbannon/ytdl-sub) is a lightweight tool to automate downloading and metadata generation with yt-dlp. It uses YAML files to define subscriptions and prepares media for popular media players like Plex, Jellyfin, Kodi, and Emby.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |
|-------------|-------------|-------------|
| [:octicons-mark-github-16: Github](https://github.com/jmbannon/ytdl-sub){: .header-icons } | [:octicons-link-16: Docs](https://ytdl-sub.readthedocs.io/){: .header-icons } | [:material-docker: Docker](https://github.com/jmbannon/ytdl-sub/pkgs/container/ytdl-sub){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-ytdl-sub
```

### 2. URL

- To access ytdl-sub, visit `https://ytdl-sub.xDOMAIN_NAMEx`

### 3. Setup

The role supports two image types configurable via inventory:

- **GUI Mode** (`ytdl_sub_image_type: "gui"`): Web-based VS Code interface for full management
- **Headless Mode** (`ytdl_sub_image_type: "headless"`): Command-line focused, lightweight deployment (default)

Configure your subscriptions using YAML files in the config directory.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        ytdl_sub_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `ytdl_sub_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `ytdl_sub_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    ytdl_sub_name: ytdl-sub

    ```

??? example "Settings"

    ```yaml
    # Type: string
    ytdl_sub_role_cron_schedule: "0 */6 * * *"

    # Type: string
    ytdl_sub_role_cron_on_start: "true"

    # Type: string
    ytdl_sub_role_image_type: "headless"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    ytdl_sub_role_paths_folder: "{{ ytdl_sub_name }}"

    # Type: string
    ytdl_sub_role_paths_location: "{{ server_appdata_path }}/{{ ytdl_sub_role_paths_folder }}"

    # Type: string
    ytdl_sub_role_paths_download_folder: "/mnt/unionfs/Media/Youtube/{{ ytdl_sub_name }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    ytdl_sub_role_web_subdomain: "{{ ytdl_sub_name }}"

    # Type: string
    ytdl_sub_role_web_domain: "{{ user.domain }}"

    # Type: string
    ytdl_sub_role_web_port: "8080"

    # Type: string
    ytdl_sub_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='ytdl_sub') + '.' + lookup('role_var', '_web_domain', role='ytdl_sub')
                            if (lookup('role_var', '_web_subdomain', role='ytdl_sub') | length > 0)
                            else lookup('role_var', '_web_domain', role='ytdl_sub')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    ytdl_sub_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='ytdl_sub') }}"

    # Type: string
    ytdl_sub_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='ytdl_sub') }}"

    # Type: bool (true/false)
    ytdl_sub_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    ytdl_sub_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    ytdl_sub_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    ytdl_sub_role_traefik_middleware_custom: ""

    # Type: string
    ytdl_sub_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    ytdl_sub_role_traefik_enabled: true

    # Type: bool (true/false)
    ytdl_sub_role_traefik_api_enabled: false

    # Type: string
    ytdl_sub_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    ytdl_sub_role_docker_container: "{{ ytdl_sub_name }}"

    # Image
    # Type: bool (true/false)
    ytdl_sub_role_docker_image_pull: true

    # Type: string
    ytdl_sub_role_docker_image_repo: "{{ 'ghcr.io/jmbannon/ytdl-sub-gui' if lookup('role_var', '_image_type', role='ytdl_sub') == 'gui' else 'ghcr.io/jmbannon/ytdl-sub' }}"

    # Type: string
    ytdl_sub_role_docker_image_tag: "{{ 'latest' if lookup('role_var', '_image_type', role='ytdl_sub') == 'gui' else 'ubuntu-latest' }}"

    # Type: string
    ytdl_sub_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='ytdl_sub') }}:{{ lookup('role_var', '_docker_image_tag', role='ytdl_sub') }}"

    # Envs
    # Type: dict
    ytdl_sub_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"
      CRON_SCHEDULE: "{{ lookup('role_var', '_cron_schedule', role='ytdl_sub') }}"
      CRON_RUN_ON_START: "{{ lookup('role_var', '_cron_on_start', role='ytdl_sub') }}"

    # Type: dict
    ytdl_sub_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    ytdl_sub_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='ytdl_sub') }}:/config"
      - "{{ lookup('role_var', '_paths_download_folder', role='ytdl_sub') }}:/ytdl_sub"
      - "{{ lookup('role_var', '_paths_download_folder', role='ytdl_sub') }}/tv_shows:/tv_shows"
      - "{{ lookup('role_var', '_paths_download_folder', role='ytdl_sub') }}/movies:/movies"
      - "{{ lookup('role_var', '_paths_download_folder', role='ytdl_sub') }}/music_videos:/music_videos"
      - "{{ lookup('role_var', '_paths_download_folder', role='ytdl_sub') }}/music:/music"

    # Type: list
    ytdl_sub_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    ytdl_sub_role_docker_hostname: "{{ ytdl_sub_name }}"

    # Networks
    # Type: string
    ytdl_sub_role_docker_networks_alias: "{{ ytdl_sub_name }}"

    # Type: list
    ytdl_sub_role_docker_networks_default: []

    # Type: list
    ytdl_sub_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    ytdl_sub_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    ytdl_sub_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    ytdl_sub_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    ytdl_sub_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    ytdl_sub_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    ytdl_sub_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    ytdl_sub_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    ytdl_sub_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    ytdl_sub_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    ytdl_sub_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    ytdl_sub_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    ytdl_sub_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    ytdl_sub_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    ytdl_sub_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    ytdl_sub_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    ytdl_sub_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    ytdl_sub_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    ytdl_sub_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    ytdl_sub_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        ytdl_sub_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "ytdl_sub2.{{ user.domain }}"
          - "ytdl_sub.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        ytdl_sub_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'ytdl_sub2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

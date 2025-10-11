---
hide:
  - tags
tags:
  - homepage
  - dashboard
  - static
---

# Homepage

## What is it?

[Homepage](https://github.com/benphelps/homepage) is a modern (fully static, fast), secure (fully proxied), customizable application dashboard with integrations for more than 25 services and translations for over 15 languages. Easily configured via YAML files (or discovery via docker labels).

### Features

- Fast! The entire site is statically generated at build time, so you can expect instant load times
- Full i18n support with automatic language detection
  - Translations for Catalan, Chinese, Dutch, Finnish, French, German, Hebrew, Hungarian, Malay, Norwegian Bokmål, Polish, Portuguese, Portuguese (Brazil), Romanian, Russian, Spanish, Swedish and Yue
- Docker integration
  - Container status (Running / Stopped) & statistics (CPU, Memory, Network)
  - Automatic service discovery (via labels)
- Service integration
  - Sonarr, Radarr, Prowlarr, Bazarr, Lidarr, Emby, Jellyfin, Tautulli, Plex and more

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://gethomepage.dev/){: .header-icons } | [:octicons-link-16: Docs](https://gethomepage.dev/latest/configs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/benphelps/homepage){: .header-icons }|

Recommended install types: Saltbox, Core, Mediabox

### 1. Installation

``` shell

sb install sandbox-homepage

```

### 2. URL

- To access Homepage, visit `https://homepage._yourdomain.com_`

### 3. Setup

This role will add both the homepage container, and the homepage-docker-socket-proxy container. To add services and bookmarks etc. you edit your config files found at `/opt/homepage/config/`. There are several example services and widgets included in the role, just uncomment and fill them in appropriately. The webui will reload and it will be visible shortly after. No need to restart the container.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        homepage_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    homepage_name: homepage

    ```

??? example "Docker Socket Proxy"

    ```yaml
    # Type: dict
    homepage_role_docker_socket_proxy_envs: 
      CONTAINERS: "1"
      POST: "0"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    homepage_role_paths_folder: "{{ homepage_name }}"

    # Type: string
    homepage_role_paths_location: "{{ server_appdata_path }}/{{ homepage_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    homepage_role_web_subdomain: "{{ homepage_name }}"

    # Type: string
    homepage_role_web_domain: "{{ user.domain }}"

    # Type: string
    homepage_role_web_port: "3000"

    # Type: string
    homepage_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='homepage') + '.' + lookup('role_var', '_web_domain', role='homepage')
                            if (lookup('role_var', '_web_subdomain', role='homepage') | length > 0)
                            else lookup('role_var', '_web_domain', role='homepage')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    homepage_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='homepage') }}"

    # Type: string
    homepage_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='homepage') }}"

    # Type: bool (true/false)
    homepage_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    homepage_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    homepage_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    homepage_role_traefik_middleware_custom: ""

    # Type: string
    homepage_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    homepage_role_traefik_enabled: true

    # Type: bool (true/false)
    homepage_role_traefik_api_enabled: false

    # Type: string
    homepage_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    homepage_role_docker_container: "{{ homepage_name }}"

    # Image
    # Type: bool (true/false)
    homepage_role_docker_image_pull: true

    # Type: string
    homepage_role_docker_image_repo: "ghcr.io/gethomepage/homepage"

    # Type: string
    homepage_role_docker_image_tag: "latest"

    # Type: string
    homepage_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='homepage') }}:{{ lookup('role_var', '_docker_image_tag', role='homepage') }}"

    # Envs
    # Type: dict
    homepage_role_docker_envs_default: 
      TZ: "{{ tz }}"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      HOMEPAGE_ALLOWED_HOSTS: "{{ traefik_host + ',' + homepage_name + ':' + lookup('role_var', '_web_port', role='homepage') }}"

    # Type: dict
    homepage_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    homepage_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='homepage') }}/config:/app/config"
      - "{{ lookup('role_var', '_paths_location', role='homepage') }}/images:/app/public/images"
      - "{{ lookup('role_var', '_paths_location', role='homepage') }}/icons:/app/public/icons"

    # Type: list
    homepage_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    homepage_role_docker_hostname: "{{ homepage_name }}"

    # Networks
    # Type: string
    homepage_role_docker_networks_alias: "{{ homepage_name }}"

    # Type: list
    homepage_role_docker_networks_default: []

    # Type: list
    homepage_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    homepage_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    homepage_role_docker_state: started

    # User
    # Type: string
    homepage_role_docker_user: "{{ uid }}:{{ gid }}"

    # Dependencies
    # Type: string
    homepage_role_depends_on: "{{ homepage_name }}-docker-socket-proxy"

    # Type: string
    homepage_role_depends_on_delay: "0"

    # Type: string
    homepage_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    homepage_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    homepage_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    homepage_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    homepage_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    homepage_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    homepage_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    homepage_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    homepage_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    homepage_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    homepage_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    homepage_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    homepage_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    homepage_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    homepage_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    homepage_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    homepage_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    homepage_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        homepage_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "homepage2.{{ user.domain }}"
          - "homepage.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        homepage_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'homepage2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

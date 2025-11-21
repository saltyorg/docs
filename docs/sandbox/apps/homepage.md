---
icon: material/docker
hide:
  - tags
tags:
  - homepage
  - dashboard
  - static
---

# Homepage

## Overview

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

```shell
sb install sandbox-homepage
```

### 2. URL

- To access Homepage, visit <https://homepage.iYOUR_DOMAIN_NAMEi>

### 3. Setup

This role will add both the homepage container, and the homepage-docker-socket-proxy container. To add services and bookmarks etc. you edit your config files found at `/opt/homepage/config/`. There are several example services and widgets included in the role, just uncomment and fill them in appropriately. The webui will reload and it will be visible shortly after. No need to restart the container.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    homepage_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `homepage_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `homepage_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`homepage_name`"

        ```yaml
        # Type: string
        homepage_name: homepage
        ```

=== "Docker Socket Proxy"

    ??? variable dict "`homepage_role_docker_socket_proxy_envs`"

        ```yaml
        # Type: dict
        homepage_role_docker_socket_proxy_envs:
          CONTAINERS: "1"
          POST: "0"
        ```

=== "Paths"

    ??? variable string "`homepage_role_paths_folder`"

        ```yaml
        # Type: string
        homepage_role_paths_folder: "{{ homepage_name }}"
        ```

    ??? variable string "`homepage_role_paths_location`"

        ```yaml
        # Type: string
        homepage_role_paths_location: "{{ server_appdata_path }}/{{ homepage_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`homepage_role_web_subdomain`"

        ```yaml
        # Type: string
        homepage_role_web_subdomain: "{{ homepage_name }}"
        ```

    ??? variable string "`homepage_role_web_domain`"

        ```yaml
        # Type: string
        homepage_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`homepage_role_web_port`"

        ```yaml
        # Type: string
        homepage_role_web_port: "3000"
        ```

    ??? variable string "`homepage_role_web_url`"

        ```yaml
        # Type: string
        homepage_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='homepage') + '.' + lookup('role_var', '_web_domain', role='homepage')
                                if (lookup('role_var', '_web_subdomain', role='homepage') | length > 0)
                                else lookup('role_var', '_web_domain', role='homepage')) }}"
        ```

=== "DNS"

    ??? variable string "`homepage_role_dns_record`"

        ```yaml
        # Type: string
        homepage_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='homepage') }}"
        ```

    ??? variable string "`homepage_role_dns_zone`"

        ```yaml
        # Type: string
        homepage_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='homepage') }}"
        ```

    ??? variable bool "`homepage_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        homepage_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`homepage_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        homepage_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`homepage_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        homepage_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`homepage_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        homepage_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`homepage_role_traefik_certresolver`"

        ```yaml
        # Type: string
        homepage_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`homepage_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        homepage_role_traefik_enabled: true
        ```

    ??? variable bool "`homepage_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        homepage_role_traefik_api_enabled: false
        ```

    ??? variable string "`homepage_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        homepage_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`homepage_role_docker_container`"

        ```yaml
        # Type: string
        homepage_role_docker_container: "{{ homepage_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`homepage_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        homepage_role_docker_image_pull: true
        ```

    ??? variable string "`homepage_role_docker_image_repo`"

        ```yaml
        # Type: string
        homepage_role_docker_image_repo: "ghcr.io/gethomepage/homepage"
        ```

    ??? variable string "`homepage_role_docker_image_tag`"

        ```yaml
        # Type: string
        homepage_role_docker_image_tag: "latest"
        ```

    ??? variable string "`homepage_role_docker_image`"

        ```yaml
        # Type: string
        homepage_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='homepage') }}:{{ lookup('role_var', '_docker_image_tag', role='homepage') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`homepage_role_docker_envs_default`"

        ```yaml
        # Type: dict
        homepage_role_docker_envs_default:
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          HOMEPAGE_ALLOWED_HOSTS: "{{ traefik_host + ',' + homepage_name + ':' + lookup('role_var', '_web_port', role='homepage') }}"
        ```

    ??? variable dict "`homepage_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        homepage_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`homepage_role_docker_volumes_default`"

        ```yaml
        # Type: list
        homepage_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='homepage') }}/config:/app/config"
          - "{{ lookup('role_var', '_paths_location', role='homepage') }}/images:/app/public/images"
          - "{{ lookup('role_var', '_paths_location', role='homepage') }}/icons:/app/public/icons"
        ```

    ??? variable list "`homepage_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        homepage_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`homepage_role_docker_hostname`"

        ```yaml
        # Type: string
        homepage_role_docker_hostname: "{{ homepage_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`homepage_role_docker_networks_alias`"

        ```yaml
        # Type: string
        homepage_role_docker_networks_alias: "{{ homepage_name }}"
        ```

    ??? variable list "`homepage_role_docker_networks_default`"

        ```yaml
        # Type: list
        homepage_role_docker_networks_default: []
        ```

    ??? variable list "`homepage_role_docker_networks_custom`"

        ```yaml
        # Type: list
        homepage_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`homepage_role_docker_restart_policy`"

        ```yaml
        # Type: string
        homepage_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`homepage_role_docker_state`"

        ```yaml
        # Type: string
        homepage_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`homepage_role_docker_user`"

        ```yaml
        # Type: string
        homepage_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

    <h5>Dependencies</h5>

    ??? variable string "`homepage_role_depends_on`"

        ```yaml
        # Type: string
        homepage_role_depends_on: "{{ homepage_name }}-docker-socket-proxy"
        ```

    ??? variable string "`homepage_role_depends_on_delay`"

        ```yaml
        # Type: string
        homepage_role_depends_on_delay: "0"
        ```

    ??? variable string "`homepage_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        homepage_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`homepage_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        homepage_role_autoheal_enabled: true
        ```

    ??? variable string "`homepage_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        homepage_role_depends_on: ""
        ```

    ??? variable string "`homepage_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        homepage_role_depends_on_delay: "0"
        ```

    ??? variable string "`homepage_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        homepage_role_depends_on_healthchecks:
        ```

    ??? variable bool "`homepage_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        homepage_role_diun_enabled: true
        ```

    ??? variable bool "`homepage_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        homepage_role_dns_enabled: true
        ```

    ??? variable bool "`homepage_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        homepage_role_docker_controller: true
        ```

    ??? variable bool "`homepage_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        homepage_role_docker_volumes_download:
        ```

    ??? variable bool "`homepage_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        homepage_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`homepage_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        homepage_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`homepage_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        homepage_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`homepage_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        homepage_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`homepage_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        homepage_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`homepage_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        homepage_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`homepage_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        homepage_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`homepage_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        homepage_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`homepage_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        homepage_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`homepage_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        homepage_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            homepage_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "homepage2.{{ user.domain }}"
              - "homepage.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`homepage_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        homepage_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            homepage_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'homepage2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`homepage_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        homepage_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
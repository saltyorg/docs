---
hide:
  - tags
tags:
  - yourspotify
  - spotify
  - analytics
---

# Yourspotify

## What is it?

[Yourspotify](https://github.com/Yooooomi/your_spotify) is a self-hosted application that tracks what you listen and offers you a dashboard to explore statistics about it! It's composed of a web server which polls the Spotify API every now and then and a web application on which you can explore your statistics.

Note that while the documentation linked here is for the original project, the Docker image linked below is a fork of the original project. Particularly the [linuxserver/your_spotify](https://github.com/linuxserver/docker-your_spotify) image.

!!! info
    By default, the role is **NOT** protected behind your Authelia/SSO middleware. You have to log into the role itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/Yooooomi/your_spotify){: .header-icons } | [:octicons-link-16: Docs](https://github.com/Yooooomi/your_spotify?tab=readme-ov-file#table-of-contents){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/ajnart/Yourspotify){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/your_spotify){: .header-icons }|

Recommended install types: Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-your-spotify

```

### 2. URL

- To access Yourspotify, visit `https://spotify._yourdomain.com_`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    your_spotify_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `your_spotify_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `your_spotify_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`your_spotify_name`"

        ```yaml
        # Type: string
        your_spotify_name: your-spotify
        ```

=== "Settings"

    ??? variable string "`your_spotify_role_public_key`"

        ```yaml
        # Type: string
        your_spotify_role_public_key: ""
        ```

    ??? variable string "`your_spotify_role_secret_key`"

        ```yaml
        # Type: string
        your_spotify_role_secret_key: ""
        ```

=== "Web"

    ??? variable string "`your_spotify_role_web_subdomain`"

        ```yaml
        # Type: string
        your_spotify_role_web_subdomain: "spotify"
        ```

    ??? variable string "`your_spotify_role_web_domain`"

        ```yaml
        # Type: string
        your_spotify_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`your_spotify_role_web_port`"

        ```yaml
        # Type: string
        your_spotify_role_web_port: "80"
        ```

    ??? variable string "`your_spotify_role_web_url`"

        ```yaml
        # Type: string
        your_spotify_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='your_spotify') + '.' + lookup('role_var', '_web_domain', role='your_spotify')
                                    if (lookup('role_var', '_web_subdomain', role='your_spotify') | length > 0)
                                    else lookup('role_var', '_web_domain', role='your_spotify')) }}"
        ```

=== "DNS"

    ??? variable string "`your_spotify_role_dns_record`"

        ```yaml
        # Type: string
        your_spotify_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='your_spotify') }}"
        ```

    ??? variable string "`your_spotify_role_dns_zone`"

        ```yaml
        # Type: string
        your_spotify_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='your_spotify') }}"
        ```

    ??? variable bool "`your_spotify_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        your_spotify_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`your_spotify_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        your_spotify_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`your_spotify_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        your_spotify_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`your_spotify_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        your_spotify_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`your_spotify_role_traefik_certresolver`"

        ```yaml
        # Type: string
        your_spotify_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`your_spotify_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        your_spotify_role_traefik_enabled: true
        ```

    ??? variable bool "`your_spotify_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        your_spotify_role_traefik_api_enabled: false
        ```

    ??? variable string "`your_spotify_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        your_spotify_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`your_spotify_role_docker_container`"

        ```yaml
        # Type: string
        your_spotify_role_docker_container: "{{ your_spotify_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`your_spotify_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        your_spotify_role_docker_image_pull: true
        ```

    ??? variable string "`your_spotify_role_docker_image_repo`"

        ```yaml
        # Type: string
        your_spotify_role_docker_image_repo: "lscr.io/linuxserver/your_spotify"
        ```

    ??? variable string "`your_spotify_role_docker_image_tag`"

        ```yaml
        # Type: string
        your_spotify_role_docker_image_tag: "latest"
        ```

    ??? variable string "`your_spotify_role_docker_image`"

        ```yaml
        # Type: string
        your_spotify_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='your_spotify') }}:{{ lookup('role_var', '_docker_image_tag', role='your_spotify') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`your_spotify_role_docker_envs_default`"

        ```yaml
        # Type: dict
        your_spotify_role_docker_envs_default: 
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          APP_URL: "{{ lookup('role_var', '_web_url', role='your_spotify') }}"
          SPOTIFY_PUBLIC: "{{ lookup('role_var', '_public_key', role='your_spotify') }}"
          SPOTIFY_SECRET: "{{ lookup('role_var', '_secret_key', role='your_spotify') }}"
          CORS: "{{ lookup('role_var', '_web_url', role='your_spotify') + ':443' }}"
          MONGO_ENDPOINT: "mongodb://your-spotify-db:27017/your_spotify"
        ```

    ??? variable dict "`your_spotify_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        your_spotify_role_docker_envs_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`your_spotify_role_docker_hostname`"

        ```yaml
        # Type: string
        your_spotify_role_docker_hostname: "{{ your_spotify_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`your_spotify_role_docker_networks_alias`"

        ```yaml
        # Type: string
        your_spotify_role_docker_networks_alias: "{{ your_spotify_name }}"
        ```

    ??? variable list "`your_spotify_role_docker_networks_default`"

        ```yaml
        # Type: list
        your_spotify_role_docker_networks_default: []
        ```

    ??? variable list "`your_spotify_role_docker_networks_custom`"

        ```yaml
        # Type: list
        your_spotify_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`your_spotify_role_docker_restart_policy`"

        ```yaml
        # Type: string
        your_spotify_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`your_spotify_role_docker_state`"

        ```yaml
        # Type: string
        your_spotify_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`your_spotify_role_depends_on`"

        ```yaml
        # Type: string
        your_spotify_role_depends_on: "your-spotify-db"
        ```

    ??? variable string "`your_spotify_role_depends_on_delay`"

        ```yaml
        # Type: string
        your_spotify_role_depends_on_delay: "0"
        ```

    ??? variable string "`your_spotify_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        your_spotify_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`your_spotify_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        your_spotify_role_autoheal_enabled: true
        ```

    ??? variable string "`your_spotify_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        your_spotify_role_depends_on: ""
        ```

    ??? variable string "`your_spotify_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        your_spotify_role_depends_on_delay: "0"
        ```

    ??? variable string "`your_spotify_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        your_spotify_role_depends_on_healthchecks:
        ```

    ??? variable bool "`your_spotify_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        your_spotify_role_diun_enabled: true
        ```

    ??? variable bool "`your_spotify_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        your_spotify_role_dns_enabled: true
        ```

    ??? variable bool "`your_spotify_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        your_spotify_role_docker_controller: true
        ```

    ??? variable bool "`your_spotify_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        your_spotify_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`your_spotify_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        your_spotify_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`your_spotify_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        your_spotify_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`your_spotify_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        your_spotify_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`your_spotify_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        your_spotify_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`your_spotify_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        your_spotify_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`your_spotify_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        your_spotify_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`your_spotify_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        your_spotify_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`your_spotify_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        your_spotify_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`your_spotify_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        your_spotify_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            your_spotify_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "your_spotify2.{{ user.domain }}"
              - "your_spotify.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`your_spotify_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        your_spotify_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            your_spotify_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'your_spotify2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`your_spotify_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        your_spotify_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
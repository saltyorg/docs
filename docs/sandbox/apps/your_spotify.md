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

sb install sandbox-your_spotify

```

### 2. URL

- To access Yourspotify, visit `https://your_spotify._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        your_spotify_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    your_spotify_name: your-spotify

    ```

??? example "Settings"

    ```yaml
    # Type: string
    your_spotify_role_public_key: ""

    # Type: string
    your_spotify_role_secret_key: ""

    ```

??? example "Web"

    ```yaml
    # Type: string
    your_spotify_role_web_subdomain: "spotify"

    # Type: string
    your_spotify_role_web_domain: "{{ user.domain }}"

    # Type: string
    your_spotify_role_web_port: "80"

    # Type: string
    your_spotify_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='your_spotify') + '.' + lookup('role_var', '_web_domain', role='your_spotify')
                                if (lookup('role_var', '_web_subdomain', role='your_spotify') | length > 0)
                                else lookup('role_var', '_web_domain', role='your_spotify')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    your_spotify_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='your_spotify') }}"

    # Type: string
    your_spotify_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='your_spotify') }}"

    # Type: bool (true/false)
    your_spotify_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    your_spotify_role_traefik_sso_middleware: ""

    # Type: string
    your_spotify_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    your_spotify_role_traefik_middleware_custom: ""

    # Type: string
    your_spotify_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    your_spotify_role_traefik_enabled: true

    # Type: bool (true/false)
    your_spotify_role_traefik_api_enabled: false

    # Type: string
    your_spotify_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    your_spotify_role_docker_container: "{{ your_spotify_name }}"

    # Image
    # Type: bool (true/false)
    your_spotify_role_docker_image_pull: true

    # Type: string
    your_spotify_role_docker_image_repo: "lscr.io/linuxserver/your_spotify"

    # Type: string
    your_spotify_role_docker_image_tag: "latest"

    # Type: string
    your_spotify_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='your_spotify') }}:{{ lookup('role_var', '_docker_image_tag', role='your_spotify') }}"

    # Envs
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

    # Type: dict
    your_spotify_role_docker_envs_custom: {}

    # Hostname
    # Type: string
    your_spotify_role_docker_hostname: "{{ your_spotify_name }}"

    # Networks
    # Type: string
    your_spotify_role_docker_networks_alias: "{{ your_spotify_name }}"

    # Type: list
    your_spotify_role_docker_networks_default: []

    # Type: list
    your_spotify_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    your_spotify_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    your_spotify_role_docker_state: started

    # Dependencies
    # Type: string
    your_spotify_role_depends_on: "your-spotify-db"

    # Type: string
    your_spotify_role_depends_on_delay: "0"

    # Type: string
    your_spotify_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    your_spotify_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    your_spotify_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    your_spotify_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    your_spotify_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    your_spotify_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    your_spotify_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    your_spotify_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    your_spotify_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    your_spotify_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    your_spotify_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    your_spotify_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    your_spotify_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    your_spotify_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    your_spotify_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    your_spotify_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    your_spotify_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    your_spotify_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        your_spotify_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "your_spotify2.{{ user.domain }}"
          - "your_spotify.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        your_spotify_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'your_spotify2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

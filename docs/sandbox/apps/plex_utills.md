---
hide:
  - tags
tags:
  - plex_utills
  - plex
  - utilities
  - management
---

# Plex Utills

## What is it?

[Plex Utills](https://github.com/jkirkcaldy/plex-utills) is a web-based utility collection for managing and maintaining your Plex Media Server. It provides various tools and helpers for common Plex administration tasks.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/jkirkcaldy/plex-utills){: .header-icons } | [:octicons-link-16: Docs](https://github.com/jkirkcaldy/plex-utills#readme){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/jkirkcaldy/plex-utills){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jkirkcaldy/plex-utills){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-plex_utills

```

### 2. URL

- To access Plex Utills, visit `https://plex-utills._yourdomain.com_`

### 3. Setup

- Configuration files are stored in `/opt/plex-utills`
- Application logs are stored in `/opt/plex-utills/logs`
- The `/mnt` directory is mounted at `/films` for media access
- The web interface runs on port 80 internally

!!! tip
    Configure the application through the web interface after your first login.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        plex_utills_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    plex_utills_name: plex-utills

    ```

??? example "Paths"

    ```yaml
    # Type: string
    plex_utills_role_paths_folder: "{{ plex_utills_name }}"

    # Type: string
    plex_utills_role_paths_location: "{{ server_appdata_path }}/{{ plex_utills_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    plex_utills_role_web_subdomain: "{{ plex_utills_name }}"

    # Type: string
    plex_utills_role_web_domain: "{{ user.domain }}"

    # Type: string
    plex_utills_role_web_port: "80"

    # Type: string
    plex_utills_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='plex_utills') + '.' + lookup('role_var', '_web_domain', role='plex_utills')
                               if (lookup('role_var', '_web_subdomain', role='plex_utills') | length > 0)
                               else lookup('role_var', '_web_domain', role='plex_utills')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    plex_utills_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='plex_utills') }}"

    # Type: string
    plex_utills_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='plex_utills') }}"

    # Type: bool (true/false)
    plex_utills_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    plex_utills_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    plex_utills_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    plex_utills_role_traefik_middleware_custom: ""

    # Type: string
    plex_utills_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    plex_utills_role_traefik_enabled: true

    # Type: bool (true/false)
    plex_utills_role_traefik_api_enabled: false

    # Type: string
    plex_utills_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    plex_utills_role_docker_container: "{{ plex_utills_name }}"

    # Image
    # Type: bool (true/false)
    plex_utills_role_docker_image_pull: true

    # Type: string
    plex_utills_role_docker_image_tag: "latest"

    # Type: string
    plex_utills_role_docker_image_repo: "jkirkcaldy/plex-utills"

    # Type: string
    plex_utills_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='plex_utills') }}:{{ lookup('role_var', '_docker_image_tag', role='plex_utills') }}"

    # Envs
    # Type: dict
    plex_utills_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    plex_utills_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    plex_utills_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='plex_utills') }}:/config"
      - "{{ lookup('role_var', '_paths_location', role='plex_utills') }}/logs:/logs"
      - "/mnt:/films"

    # Type: list
    plex_utills_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    plex_utills_role_docker_hostname: "{{ plex_utills_name }}"

    # Networks
    # Type: string
    plex_utills_role_docker_networks_alias: "{{ plex_utills_name }}"

    # Type: list
    plex_utills_role_docker_networks_default: []

    # Type: list
    plex_utills_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    plex_utills_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    plex_utills_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    plex_utills_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    plex_utills_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    plex_utills_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    plex_utills_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    plex_utills_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    plex_utills_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    plex_utills_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    plex_utills_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    plex_utills_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    plex_utills_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    plex_utills_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    plex_utills_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    plex_utills_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    plex_utills_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    plex_utills_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    plex_utills_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    plex_utills_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        plex_utills_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "plex_utills2.{{ user.domain }}"
          - "plex_utills.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        plex_utills_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'plex_utills2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

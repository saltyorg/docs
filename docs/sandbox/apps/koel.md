---
hide:
  - tags
tags:
  - koel
  - music
  - streaming
---

# Koel

## What is it?

[Koel](https://koel.dev/) is a simple web-based personal audio streaming service written in Vue and Laravel that embraces modern web technologies. It features transparent FLAC support, cross-device sync, smart playlists, and multi-user support.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://koel.dev/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/koel/koel){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/phanan/koel){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-koel
```

### 2. URL

- To access Koel, visit `https://koel._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        koel_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `koel_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `koel_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    koel_name: koel

    ```

??? example "Paths"

    ```yaml
    # Type: string
    koel_role_paths_folder: "{{ koel_name }}"

    # Type: string
    koel_role_paths_location: "{{ server_appdata_path }}/{{ koel_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    koel_role_web_subdomain: "{{ koel_name }}"

    # Type: string
    koel_role_web_domain: "{{ user.domain }}"

    # Type: string
    koel_role_web_port: "80"

    # Type: string
    koel_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='koel') + '.' + lookup('role_var', '_web_domain', role='koel')
                        if (lookup('role_var', '_web_subdomain', role='koel') | length > 0)
                        else lookup('role_var', '_web_domain', role='koel')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    koel_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='koel') }}"

    # Type: string
    koel_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='koel') }}"

    # Type: bool (true/false)
    koel_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    koel_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    koel_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    koel_role_traefik_middleware_custom: ""

    # Type: string
    koel_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    koel_role_traefik_enabled: true

    # Type: bool (true/false)
    koel_role_traefik_api_enabled: true

    # Type: string
    koel_role_traefik_api_endpoint: "PathPrefix(`/api`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    koel_role_docker_container: "{{ koel_name }}"

    # Image
    # Type: bool (true/false)
    koel_role_docker_image_pull: true

    # Type: string
    koel_role_docker_image_tag: "latest"

    # Type: string
    koel_role_docker_image_repo: "phanan/koel"

    # Type: string
    koel_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='koel') }}:{{ lookup('role_var', '_docker_image_tag', role='koel') }}"

    # Envs
    # Type: dict
    koel_role_docker_envs_default: 
      TZ: "{{ tz }}"
      DB_CONNECTION: "mysql"
      DB_HOST: "{{ koel_name }}-mariadb"
      DB_PORT: "3306"
      DB_DATABASE: "{{ koel_name }}"
      DB_USERNAME: "root"
      DB_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='mariadb') }}"
      APP_KEY: "base64:{{ koel_secret_key }}"
      APP_URL: "{{ lookup('role_var', '_web_url', role='koel') }}"
      FORCE_HTTPS: "true"

    # Type: dict
    koel_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    koel_role_docker_volumes_default: 
      - "/mnt/unionfs/Media/Music:/music:ro"
      - "{{ lookup('role_var', '_paths_location', role='koel') }}/app/covers:/var/www/html/public/img/covers"
      - "{{ lookup('role_var', '_paths_location', role='koel') }}/app/search-indexes:/var/www/html/storage/search-indexes"

    # Type: list
    koel_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    koel_role_docker_hostname: "{{ koel_name }}"

    # Networks
    # Type: string
    koel_role_docker_networks_alias: "{{ koel_name }}"

    # Type: list
    koel_role_docker_networks_default: []

    # Type: list
    koel_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    koel_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    koel_role_docker_state: started

    # Dependencies
    # Type: string
    koel_role_depends_on: "{{ koel_name }}-mariadb"

    # Type: string
    koel_role_depends_on_delay: "0"

    # Type: string
    koel_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    koel_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    koel_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    koel_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    koel_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    koel_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    koel_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    koel_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    koel_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    koel_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    koel_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    koel_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    koel_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    koel_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    koel_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    koel_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    koel_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    koel_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        koel_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "koel2.{{ user.domain }}"
          - "koel.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        koel_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'koel2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

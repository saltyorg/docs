---
hide:
  - tags
tags:
  - miniflux
  - media
  - rss
---

# miniflux

## What is it?

[Miniflux](https://miniflux.app) is a minimalist and opinionated feed reader.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://miniflux.app){: .header-icons } | [:octicons-link-16: Docs](https://github.com/miniflux/v2){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/miniflux/v2){: .header-icons } | [:material-docker: Docker](https://registry.hub.docker.com/r/miniflux/miniflux){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-miniflux

```

### 2. URL

- To access miniflux, visit `https://miniflux._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        miniflux_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `miniflux_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `miniflux_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    miniflux_name: miniflux

    ```

??? example "Settings"

    ```yaml
    # Type: string
    miniflux_role_admin_username: "{{ user.name }}"

    # Type: string
    miniflux_role_admin_password: "{{ user.pass }}"

    # Type: string
    miniflux_role_create_admin: "1"

    # Type: string
    miniflux_role_run_migrations: "1"

    # Type: bool (true/false)
    miniflux_role_postgres_deploy: true

    # Type: string
    miniflux_role_postgres_name: "{{ miniflux_name }}-postgres"

    # Type: string
    miniflux_role_postgres_user: "{{ postgres_role_docker_env_user }}"

    # Type: string
    miniflux_role_postgres_password: "{{ postgres_role_docker_env_password }}"

    # Type: string
    miniflux_role_postgres_docker_env_db: "miniflux"

    # Type: string
    miniflux_role_postgres_docker_image_tag: "14-alpine"

    # Type: string
    miniflux_role_postgres_docker_image_repo: "postgres"

    # Type: dict
    miniflux_role_postgres_docker_healthcheck: 
      test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='miniflux') }} -U {{ postgres_role_docker_env_user }}"]
      start_period: 20s
      interval: 30s
      retries: 5
      timeout: 5s

    # Type: string
    miniflux_role_postgres_paths_folder: "{{ miniflux_name }}"

    # Type: string
    miniflux_role_postgres_paths_location: "{{ server_appdata_path }}/{{ miniflux_role_postgres_paths_folder }}/postgres"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    miniflux_role_paths_folder: "{{ miniflux_name }}"

    # Type: string
    miniflux_role_paths_location: "{{ server_appdata_path }}/{{ miniflux_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    miniflux_role_web_subdomain: "{{ miniflux_name }}"

    # Type: string
    miniflux_role_web_domain: "{{ user.domain }}"

    # Type: string
    miniflux_role_web_port: "8080"

    # Type: string
    miniflux_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='miniflux') + '.' + lookup('role_var', '_web_domain', role='miniflux')
                            if (lookup('role_var', '_web_subdomain', role='miniflux') | length > 0)
                            else lookup('role_var', '_web_domain', role='miniflux')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    miniflux_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='miniflux') }}"

    # Type: string
    miniflux_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='miniflux') }}"

    # Type: bool (true/false)
    miniflux_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    miniflux_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    miniflux_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    miniflux_role_traefik_middleware_custom: ""

    # Type: string
    miniflux_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    miniflux_role_traefik_enabled: true

    # Type: bool (true/false)
    miniflux_role_traefik_api_enabled: false

    # Type: string
    miniflux_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    miniflux_role_docker_container: "{{ miniflux_name }}"

    # Image
    # Type: bool (true/false)
    miniflux_role_docker_image_pull: true

    # Type: string
    miniflux_role_docker_image_tag: "latest"

    # Type: string
    miniflux_role_docker_image_repo: "miniflux/miniflux"

    # Type: string
    miniflux_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='miniflux') }}:{{ lookup('role_var', '_docker_image_tag', role='miniflux') }}"

    # Envs
    # Type: dict
    miniflux_role_docker_envs_default: 
      DATABASE_URL: "postgres://{{ lookup('role_var', '_postgres_user', role='miniflux') }}:{{ lookup('role_var', '_postgres_password', role='miniflux') }}@{{ lookup('role_var', '_postgres_name', role='miniflux') }}/{{ lookup('role_var', '_postgres_docker_env_db', role='miniflux') }}?sslmode=disable"
      RUN_MIGRATIONS: "{{ lookup('role_var', '_run_migrations', role='miniflux') }}"
      CREATE_ADMIN: "{{ lookup('role_var', '_create_admin', role='miniflux') }}"
      ADMIN_USERNAME: "{{ lookup('role_var', '_admin_username', role='miniflux') }}"
      ADMIN_PASSWORD: "{{ lookup('role_var', '_admin_password', role='miniflux') }}"

    # Type: dict
    miniflux_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    miniflux_role_docker_volumes_default: 
      - /etc/localtime:/etc/localtime:ro

    # Type: list
    miniflux_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    miniflux_role_docker_hostname: "{{ miniflux_name }}"

    # Networks
    # Type: string
    miniflux_role_docker_networks_alias: "{{ miniflux_name }}"

    # Type: list
    miniflux_role_docker_networks_default: []

    # Type: list
    miniflux_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    miniflux_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    miniflux_role_docker_state: started

    # Dependencies
    # Type: string
    minuflux_role_depends_on: "{{ minuflux_role_postgres_name }}"

    # Type: string
    minuflux_role_depends_on_delay: "0"

    # Type: string
    minuflux_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    miniflux_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    miniflux_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    miniflux_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    miniflux_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    miniflux_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    miniflux_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    miniflux_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    miniflux_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    miniflux_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    miniflux_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    miniflux_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    miniflux_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    miniflux_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    miniflux_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    miniflux_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    miniflux_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    miniflux_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        miniflux_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "miniflux2.{{ user.domain }}"
          - "miniflux.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        miniflux_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'miniflux2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
hide:
  - tags
tags:
  - jellystat
  - jellyfin
  - statistics
---

# Jellystat

## What is it?

[Jellystat](https://github.com/CyferShepard/Jellystat) is a free and open source statistics web application for Jellyfin that provides a dashboard with information about the server, libraries, users, and playback activity. Still in development with some expected functionality gaps.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |
|-------------|-------------|-------------|
| [:octicons-mark-github-16: Github](https://github.com/CyferShepard/Jellystat){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/cyfershepard/jellystat){: .header-icons } | [:octicons-law-16: MIT](https://github.com/CyferShepard/Jellystat/blob/main/LICENSE){: .header-icons } |

### 1. Installation

``` shell
sb install sandbox-jellystat
```

### 2. URL

- To access Jellystat, visit `https://jellystat._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        jellystat_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    jellystat_name: jellystat

    ```

??? example "Settings"

    ```yaml
    # Type: bool (true/false)
    jellystat_role_postgres_deploy: true

    # Type: string
    jellystat_role_postgres_name: "{{ jellystat_name }}-postgres"

    # Type: string
    jellystat_role_postgres_user: "{{ postgres_role_docker_env_user }}"

    # Type: string
    jellystat_role_postgres_password: "{{ postgres_role_docker_env_password }}"

    # Type: string
    jellystat_role_postgres_docker_env_db: "jfstat"

    # Type: string
    jellystat_role_postgres_docker_image_tag: "15.2-alpine"

    # Type: string
    jellystat_role_postgres_docker_image_repo: "postgres"

    # Type: dict
    jellystat_role_postgres_docker_healthcheck: 
      test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='jellystat') }} -U {{ postgres_role_docker_env_user }}"]
      start_period: 20s
      interval: 30s
      retries: 5
      timeout: 5s

    # Type: string
    jellystat_role_postgres_paths_folder: "{{ jellystat_name }}"

    # Type: string
    jellystat_role_postgres_paths_location: "{{ server_appdata_path }}/{{ jellystat_role_postgres_paths_folder }}/postgres"

    # Type: string
    jellystat_log_level: "INFO"

    # Type: bool (true/false)
    jellystat_emby: false

    ```

??? example "Paths"

    ```yaml
    # Type: string
    jellystat_role_paths_folder: "{{ jellystat_name }}"

    # Type: string
    jellystat_role_paths_location: "{{ server_appdata_path }}/{{ jellystat_role_paths_folder }}"

    # Type: string
    jellystat_role_paths_jwt_secret_file: "{{ jellystat_role_paths_location }}/jwt_secret.txt"

    ```

??? example "Web"

    ```yaml
    # Type: string
    jellystat_role_web_subdomain: "{{ jellystat_name }}"

    # Type: string
    jellystat_role_web_domain: "{{ user.domain }}"

    # Type: string
    jellystat_role_web_port: "3000"

    # Type: string
    jellystat_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='jellystat') + '.' + lookup('role_var', '_web_domain', role='jellystat')
                             if (lookup('role_var', '_web_subdomain', role='jellystat') | length > 0)
                             else lookup('role_var', '_web_domain', role='jellystat')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    jellystat_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='jellystat') }}"

    # Type: string
    jellystat_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='jellystat') }}"

    # Type: bool (true/false)
    jellystat_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    jellystat_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    jellystat_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    jellystat_role_traefik_middleware_custom: ""

    # Type: string
    jellystat_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    jellystat_role_traefik_enabled: true

    # Type: bool (true/false)
    jellystat_role_traefik_api_enabled: false

    # Type: string
    jellystat_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    jellystat_role_docker_container: "{{ jellystat_name }}"

    # Image
    # Type: bool (true/false)
    jellystat_role_docker_image_pull: true

    # Type: string
    jellystat_role_docker_image_repo: "cyfershepard/jellystat"

    # Type: string
    jellystat_role_docker_image_tag: "latest"

    # Type: string
    jellystat_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='jellystat') }}:{{ lookup('role_var', '_docker_image_tag', role='jellystat') }}"

    # Envs
    # Type: dict
    jellystat_role_docker_envs_default: 
      POSTGRES_USER: "{{ lookup('role_var', '_postgres_user', role='jellystat') }}"
      POSTGRES_PASSWORD: "{{ lookup('role_var', '_postgres_password', role='jellystat') }}"
      POSTGRES_IP: "{{ lookup('role_var', '_postgres_name', role='jellystat') }}"
      POSTGRES_PORT: "5432"
      JWT_SECRET: "{{ jwt_token.stdout }}"

    # Type: dict
    jellystat_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    jellystat_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='jellystat') }}:/app/backend/backup-data"

    # Type: list
    jellystat_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    jellystat_role_docker_hostname: "{{ jellystat_name }}"

    # Networks
    # Type: string
    jellystat_role_docker_networks_alias: "{{ jellystat_name }}"

    # Type: list
    jellystat_role_docker_networks_default: []

    # Type: list
    jellystat_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    jellystat_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    jellystat_role_docker_state: started

    # Dependencies
    # Type: string
    jellystat_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='jellystat') }}"

    # Type: string
    jellystat_role_depends_on_delay: "0"

    # Type: string
    jellystat_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    jellystat_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    jellystat_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    jellystat_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    jellystat_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    jellystat_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    jellystat_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    jellystat_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    jellystat_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    jellystat_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    jellystat_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    jellystat_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    jellystat_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    jellystat_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    jellystat_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    jellystat_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    jellystat_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    jellystat_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        jellystat_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "jellystat2.{{ user.domain }}"
          - "jellystat.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        jellystat_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'jellystat2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

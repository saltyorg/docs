---
hide:
  - tags
tags:
  - linkwarden
  - bookmarks
  - collaboration
---

# LinkWarden

## What is it?

[LinkWarden](https://linkwarden.app/) is a self-hosted collaborative bookmark manager designed to collect, read, annotate, and fully preserve web content. It automatically captures screenshots, PDFs, and HTML files of bookmarked pages to prevent link rot.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://linkwarden.app/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/linkwarden/linkwarden){: .header-icons } | [:material-docker: Docker](https://github.com/linkwarden/linkwarden/pkgs/container/linkwarden){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-linkwarden
```

### 2. URL

- To access LinkWarden, visit `https://linkwarden._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        linkwarden_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    linkwarden_name: linkwarden

    ```

??? example "Settings"

    ```yaml
    # Type: bool (true/false)
    linkwarden_role_postgres_deploy: true

    # Type: string
    linkwarden_role_postgres_name: "{{ linkwarden_name }}-postgres"

    # Type: string
    linkwarden_role_postgres_user: "{{ linkwarden_name }}"

    # Type: string
    linkwarden_role_postgres_password: "{{ linkwarden_name }}"

    # Type: string
    linkwarden_role_postgres_docker_env_db: "{{ linkwarden_name }}"

    # Type: string
    linkwarden_role_postgres_docker_image_tag: "16-alpine"

    # Type: string
    linkwarden_role_postgres_docker_image_repo: "postgres"

    # Type: dict
    linkwarden_role_postgres_docker_healthcheck: 
      test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='linkwarden') }} -U {{ lookup('role_var', '_postgres_user', role='linkwarden') }}"]
      start_period: 20s
      interval: 30s
      retries: 5
      timeout: 5s

    # Type: string
    linkwarden_role_postgres_paths_folder: "{{ linkwarden_name }}"

    # Type: string
    linkwarden_role_postgres_paths_location: "{{ server_appdata_path }}/{{ linkwarden_role_postgres_paths_folder }}/postgres"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    linkwarden_role_paths_folder: "{{ linkwarden_name }}"

    # Type: string
    linkwarden_role_paths_location: "{{ server_appdata_path }}/{{ linkwarden_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    linkwarden_role_web_subdomain: "{{ linkwarden_name }}"

    # Type: string
    linkwarden_role_web_domain: "{{ user.domain }}"

    # Type: string
    linkwarden_role_web_port: "3000"

    # Type: string
    linkwarden_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='linkwarden') + '.' + lookup('role_var', '_web_domain', role='linkwarden')
                              if (lookup('role_var', '_web_subdomain', role='linkwarden') | length > 0)
                              else lookup('role_var', '_web_domain', role='linkwarden')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    linkwarden_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='linkwarden') }}"

    # Type: string
    linkwarden_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='linkwarden') }}"

    # Type: bool (true/false)
    linkwarden_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    linkwarden_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    linkwarden_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    linkwarden_role_traefik_middleware_custom: ""

    # Type: string
    linkwarden_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    linkwarden_role_traefik_enabled: true

    # Type: bool (true/false)
    linkwarden_role_traefik_api_enabled: true

    # Type: string
    linkwarden_role_traefik_api_endpoint: "PathPrefix(`/api`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    linkwarden_role_docker_container: "{{ linkwarden_name }}"

    # Image
    # Type: bool (true/false)
    linkwarden_role_docker_image_pull: true

    # Type: string
    linkwarden_role_docker_image_tag: "latest"

    # Type: string
    linkwarden_role_docker_image_repo: "ghcr.io/linkwarden/linkwarden"

    # Type: string
    linkwarden_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='linkwarden') }}:{{ lookup('role_var', '_docker_image_tag', role='linkwarden') }}"

    # Envs
    # Type: dict
    linkwarden_role_docker_envs_default: 
      TZ: "{{ tz }}"
      NEXT_PUBLIC_CREDENTIALS_ENABLED: "true"
      STORAGE_FOLDER: "/data"
      NEXTAUTH_SECRET: "{{ linkwarden_secret_key.stdout }}"
      NEXTAUTH_URL: "{{ lookup('role_var', '_web_url', role='linkwarden') }}/api/v1/auth"
      DATABASE_URL: "postgresql://{{ lookup('role_var', '_postgres_user', role='linkwarden') }}:{{ lookup('role_var', '_postgres_password', role='linkwarden') }}@{{ lookup('role_var', '_postgres_name', role='linkwarden') }}:5432/{{ lookup('role_var', '_postgres_docker_env_db', role='linkwarden') }}"

    # Type: dict
    linkwarden_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    linkwarden_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='linkwarden') }}:/data/data"

    # Type: list
    linkwarden_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    linkwarden_role_docker_hostname: "{{ linkwarden_name }}"

    # Networks
    # Type: string
    linkwarden_role_docker_networks_alias: "{{ linkwarden_name }}"

    # Type: list
    linkwarden_role_docker_networks_default: []

    # Type: list
    linkwarden_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    linkwarden_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    linkwarden_role_docker_state: started

    # Dependencies
    # Type: string
    linkwarden_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='linkwarden') }}"

    # Type: string
    linkwarden_role_depends_on_delay: "0"

    # Type: string
    linkwarden_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    linkwarden_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    linkwarden_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    linkwarden_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    linkwarden_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    linkwarden_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    linkwarden_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    linkwarden_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    linkwarden_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    linkwarden_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    linkwarden_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    linkwarden_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    linkwarden_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    linkwarden_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    linkwarden_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    linkwarden_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    linkwarden_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    linkwarden_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        linkwarden_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "linkwarden2.{{ user.domain }}"
          - "linkwarden.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        linkwarden_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'linkwarden2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

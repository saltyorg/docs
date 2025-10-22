---
hide:
  - tags
tags:
  - n8n
  - automation
  - workflow
---

# n8n

## What is it?

[n8n - Secure Workflow Automation for Technical Teams](https://n8n.io/) is a workflow automation platform that gives technical teams the flexibility of code with the speed of no-code. With 400+ integrations, native AI capabilities, and a fair-code license, n8n lets you build powerful automations while maintaining full control over your data and deployments.

- **Code When You Need It**: Write JavaScript/Python, add npm packages, or use the visual interface
- **AI-Native Platform**: Build AI agent workflows based on LangChain with your own data and models
- **Full Control**: Self-host with our fair-code license or use our [cloud offering](https://app.n8n.cloud/login)
- **Enterprise-Ready**: Advanced permissions, SSO, and air-gapped deployments
- **Active Community**: 400+ integrations and 900+ ready-to-use [templates](https://n8n.io/workflows)

!!! info
    By default, the role **IS** protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://n8n.io/){: .header-icons } | [:octicons-link-16: Docs](https://docs.n8n.io/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/ajnart/n8n){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/n8nio/n8n){: .header-icons }|

Recommended install types: Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-n8n

```

### 2. URL

- To access n8n, visit `https://n8n.xDOMAIN_NAMEx`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        n8n_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `n8n_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `n8n_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    n8n_name: n8n

    ```

??? example "Settings"

    ```yaml
    # Type: bool (true/false)
    n8n_role_postgres_deploy: true

    # Type: string
    n8n_role_postgres_name: "{{ n8n_name }}-postgres"

    # Type: string
    n8n_role_postgres_user: "{{ postgres_role_docker_env_user }}"

    # Type: string
    n8n_role_postgres_password: "{{ postgres_role_docker_env_password }}"

    # Type: string
    n8n_role_postgres_docker_env_db: "{{ n8n_name }}"

    # Type: string
    n8n_role_postgres_docker_image_tag: "14-alpine"

    # Type: string
    n8n_role_postgres_docker_image_repo: "postgres"

    # Type: dict
    n8n_role_postgres_docker_healthcheck: 
      test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='n8n') }} -U {{ postgres_role_docker_env_user }}"]
      start_period: 20s
      interval: 30s
      retries: 5
      timeout: 5s

    # Type: string
    n8n_role_postgres_paths_folder: "{{ n8n_name }}"

    # Type: string
    n8n_role_postgres_paths_location: "{{ server_appdata_path }}/{{ n8n_role_postgres_paths_folder }}/postgres"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    n8n_role_paths_folder: "{{ n8n_name }}"

    # Type: string
    n8n_role_paths_location: "{{ server_appdata_path }}/{{ n8n_role_paths_folder }}/app"

    ```

??? example "Web"

    ```yaml
    # Type: string
    n8n_role_web_subdomain: "{{ n8n_name }}"

    # Type: string
    n8n_role_web_domain: "{{ user.domain }}"

    # Type: string
    n8n_role_web_port: "5678"

    # Type: string
    n8n_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='n8n') + '.' + lookup('role_var', '_web_domain', role='n8n')
                       if (lookup('role_var', '_web_subdomain', role='n8n') | length > 0)
                       else lookup('role_var', '_web_domain', role='n8n')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    n8n_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='n8n') }}"

    # Type: string
    n8n_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='n8n') }}"

    # Type: bool (true/false)
    n8n_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    n8n_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    n8n_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    n8n_role_traefik_middleware_custom: ""

    # Type: string
    n8n_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    n8n_role_traefik_enabled: true

    # Type: bool (true/false)
    n8n_role_traefik_api_enabled: true

    # Type: string
    n8n_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/webhook`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    n8n_role_docker_container: "{{ n8n_name }}"

    # Image
    # Type: bool (true/false)
    n8n_role_docker_image_pull: true

    # Type: string
    n8n_role_docker_image_tag: "latest"

    # Type: string
    n8n_role_docker_image_repo: "n8nio/n8n"

    # Type: string
    n8n_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='n8n') }}:{{ lookup('role_var', '_docker_image_tag', role='n8n') }}"

    # Envs
    # Type: dict
    n8n_role_docker_envs_default: 
      GENERIC_TIMEZONE: "{{ tz }}"
      TZ: "{{ tz }}"
      DB_TYPE: "postgresdb"
      DB_POSTGRESDB_DATABASE: "{{ lookup('role_var', '_postgres_docker_env_db', role='n8n') }}"
      DB_POSTGRESDB_HOST: "{{ lookup('role_var', '_postgres_name', role='n8n') }}"
      DB_POSTGRESDB_PORT: "5432"
      DB_POSTGRESDB_USER: "{{ lookup('role_var', '_postgres_user', role='n8n') }}"
      DB_POSTGRESDB_PASSWORD: "{{ lookup('role_var', '_postgres_password', role='n8n') }}"
      N8N_EDITOR_BASE_URL: "{{ lookup('role_var', '_web_url', role='n8n') }}"
      N8N_DIAGNOSTICS_ENABLED: "false"
      N8N_HIRING_BANNER_ENABLED: "false"
      N8N_USER_MANAGEMENT_DISABLED: "true"
      N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS: "true"
      WEBHOOK_URL: "{{ lookup('role_var', '_web_url', role='n8n') }}/"
      N8N_PROXY_HOPS: "1"

    # Type: dict
    n8n_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    n8n_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='n8n') }}:/home/node/.n8n"

    # Type: list
    n8n_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    n8n_role_docker_hostname: "{{ n8n_name }}"

    # Networks
    # Type: string
    n8n_role_docker_networks_alias: "{{ n8n_name }}"

    # Type: list
    n8n_role_docker_networks_default: []

    # Type: list
    n8n_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    n8n_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    n8n_role_docker_state: started

    # Dependencies
    # Type: string
    n8n_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='n8n') }}"

    # Type: string
    n8n_role_depends_on_delay: "0"

    # Type: string
    n8n_role_depends_on_healthchecks: "false"

    # User
    # Type: string
    n8n_role_docker_user: "{{ uid }}:{{ gid }}"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    n8n_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    n8n_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    n8n_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    n8n_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    n8n_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    n8n_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    n8n_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    n8n_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    n8n_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    n8n_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    n8n_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    n8n_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    n8n_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    n8n_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    n8n_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    n8n_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    n8n_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        n8n_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "n8n2.{{ user.domain }}"
          - "n8n.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        n8n_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'n8n2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

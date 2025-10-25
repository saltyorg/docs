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

- To access n8n, visit `https://n8n._yourdomain.com_`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    n8n_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `n8n_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `n8n_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`n8n_name`"

        ```yaml
        # Type: string
        n8n_name: n8n
        ```

=== "Settings"

    ??? variable bool "`n8n_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        n8n_role_postgres_deploy: true
        ```

    ??? variable string "`n8n_role_postgres_name`"

        ```yaml
        # Type: string
        n8n_role_postgres_name: "{{ n8n_name }}-postgres"
        ```

    ??? variable string "`n8n_role_postgres_user`"

        ```yaml
        # Type: string
        n8n_role_postgres_user: "{{ postgres_role_docker_env_user }}"
        ```

    ??? variable string "`n8n_role_postgres_password`"

        ```yaml
        # Type: string
        n8n_role_postgres_password: "{{ postgres_role_docker_env_password }}"
        ```

    ??? variable string "`n8n_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        n8n_role_postgres_docker_env_db: "{{ n8n_name }}"
        ```

    ??? variable string "`n8n_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        n8n_role_postgres_docker_image_tag: "14-alpine"
        ```

    ??? variable string "`n8n_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        n8n_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable dict "`n8n_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        n8n_role_postgres_docker_healthcheck: 
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='n8n') }} -U {{ postgres_role_docker_env_user }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`n8n_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        n8n_role_postgres_paths_folder: "{{ n8n_name }}"
        ```

    ??? variable string "`n8n_role_postgres_paths_location`"

        ```yaml
        # Type: string
        n8n_role_postgres_paths_location: "{{ server_appdata_path }}/{{ n8n_role_postgres_paths_folder }}/postgres"
        ```

=== "Paths"

    ??? variable string "`n8n_role_paths_folder`"

        ```yaml
        # Type: string
        n8n_role_paths_folder: "{{ n8n_name }}"
        ```

    ??? variable string "`n8n_role_paths_location`"

        ```yaml
        # Type: string
        n8n_role_paths_location: "{{ server_appdata_path }}/{{ n8n_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`n8n_role_web_subdomain`"

        ```yaml
        # Type: string
        n8n_role_web_subdomain: "{{ n8n_name }}"
        ```

    ??? variable string "`n8n_role_web_domain`"

        ```yaml
        # Type: string
        n8n_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`n8n_role_web_port`"

        ```yaml
        # Type: string
        n8n_role_web_port: "5678"
        ```

    ??? variable string "`n8n_role_web_url`"

        ```yaml
        # Type: string
        n8n_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='n8n') + '.' + lookup('role_var', '_web_domain', role='n8n')
                           if (lookup('role_var', '_web_subdomain', role='n8n') | length > 0)
                           else lookup('role_var', '_web_domain', role='n8n')) }}"
        ```

=== "DNS"

    ??? variable string "`n8n_role_dns_record`"

        ```yaml
        # Type: string
        n8n_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='n8n') }}"
        ```

    ??? variable string "`n8n_role_dns_zone`"

        ```yaml
        # Type: string
        n8n_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='n8n') }}"
        ```

    ??? variable bool "`n8n_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        n8n_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`n8n_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        n8n_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`n8n_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        n8n_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`n8n_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        n8n_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`n8n_role_traefik_certresolver`"

        ```yaml
        # Type: string
        n8n_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`n8n_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        n8n_role_traefik_enabled: true
        ```

    ??? variable bool "`n8n_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        n8n_role_traefik_api_enabled: true
        ```

    ??? variable string "`n8n_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        n8n_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/webhook`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`n8n_role_docker_container`"

        ```yaml
        # Type: string
        n8n_role_docker_container: "{{ n8n_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`n8n_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        n8n_role_docker_image_pull: true
        ```

    ??? variable string "`n8n_role_docker_image_tag`"

        ```yaml
        # Type: string
        n8n_role_docker_image_tag: "latest"
        ```

    ??? variable string "`n8n_role_docker_image_repo`"

        ```yaml
        # Type: string
        n8n_role_docker_image_repo: "n8nio/n8n"
        ```

    ??? variable string "`n8n_role_docker_image`"

        ```yaml
        # Type: string
        n8n_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='n8n') }}:{{ lookup('role_var', '_docker_image_tag', role='n8n') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`n8n_role_docker_envs_default`"

        ```yaml
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
          N8N_RUNNERS_ENABLED: "true"
          N8N_USER_FOLDER: "/data"
        ```

    ??? variable dict "`n8n_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        n8n_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`n8n_role_docker_volumes_default`"

        ```yaml
        # Type: list
        n8n_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='n8n') }}/data:/data"
        ```

    ??? variable list "`n8n_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        n8n_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`n8n_role_docker_hostname`"

        ```yaml
        # Type: string
        n8n_role_docker_hostname: "{{ n8n_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`n8n_role_docker_networks_alias`"

        ```yaml
        # Type: string
        n8n_role_docker_networks_alias: "{{ n8n_name }}"
        ```

    ??? variable list "`n8n_role_docker_networks_default`"

        ```yaml
        # Type: list
        n8n_role_docker_networks_default: []
        ```

    ??? variable list "`n8n_role_docker_networks_custom`"

        ```yaml
        # Type: list
        n8n_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`n8n_role_docker_restart_policy`"

        ```yaml
        # Type: string
        n8n_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`n8n_role_docker_state`"

        ```yaml
        # Type: string
        n8n_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`n8n_role_depends_on`"

        ```yaml
        # Type: string
        n8n_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='n8n') }}"
        ```

    ??? variable string "`n8n_role_depends_on_delay`"

        ```yaml
        # Type: string
        n8n_role_depends_on_delay: "0"
        ```

    ??? variable string "`n8n_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        n8n_role_depends_on_healthchecks: "false"
        ```

    <h5>User</h5>

    ??? variable string "`n8n_role_docker_user`"

        ```yaml
        # Type: string
        n8n_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`n8n_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        n8n_role_autoheal_enabled: true
        ```

    ??? variable string "`n8n_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        n8n_role_depends_on: ""
        ```

    ??? variable string "`n8n_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        n8n_role_depends_on_delay: "0"
        ```

    ??? variable string "`n8n_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        n8n_role_depends_on_healthchecks:
        ```

    ??? variable bool "`n8n_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        n8n_role_diun_enabled: true
        ```

    ??? variable bool "`n8n_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        n8n_role_dns_enabled: true
        ```

    ??? variable bool "`n8n_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        n8n_role_docker_controller: true
        ```

    ??? variable bool "`n8n_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        n8n_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`n8n_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        n8n_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`n8n_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        n8n_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`n8n_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        n8n_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`n8n_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        n8n_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`n8n_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        n8n_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`n8n_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        n8n_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`n8n_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        n8n_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`n8n_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        n8n_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`n8n_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        n8n_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            n8n_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "n8n2.{{ user.domain }}"
              - "n8n.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`n8n_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        n8n_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            n8n_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'n8n2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`n8n_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        n8n_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
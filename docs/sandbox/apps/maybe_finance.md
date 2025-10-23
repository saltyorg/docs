---
hide:
  - tags
tags:
  - maybe-finance
  - finance
  - budgeting
---

# Maybe Finance

## What is it?

[Maybe Finance](https://maybe.co/) is a personal finance app that functions as an operating system for managing finances, with interactive tools and calculators. The open-source version is available under AGPLv3 license but is no longer actively maintained.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://maybe.co/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/maybe-finance/maybe){: .header-icons } | [:material-docker: Docker](https://github.com/maybe-finance/maybe/pkgs/container/maybe){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-maybe-finance
```

### 2. URL

- To access Maybe Finance, visit `https://maybe-finance._yourdomain.com_`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        maybe_finance_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `maybe_finance_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `maybe_finance_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`maybe_finance_name`"

        ```yaml
        # Type: string
        maybe_finance_name: maybe-finance
        ```

=== "Settings"

    ??? variable bool "`maybe_finance_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        maybe_finance_role_postgres_deploy: true
        ```

    ??? variable string "`maybe_finance_role_postgres_name`"

        ```yaml
        # Type: string
        maybe_finance_role_postgres_name: "{{ maybe_finance_name }}-postgres"
        ```

    ??? variable string "`maybe_finance_role_postgres_user`"

        ```yaml
        # Type: string
        maybe_finance_role_postgres_user: "{{ postgres_role_docker_env_user }}"
        ```

    ??? variable string "`maybe_finance_role_postgres_password`"

        ```yaml
        # Type: string
        maybe_finance_role_postgres_password: "{{ postgres_role_docker_env_password }}"
        ```

    ??? variable string "`maybe_finance_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        maybe_finance_role_postgres_docker_env_db: "{{ maybe_finance_name }}"
        ```

    ??? variable string "`maybe_finance_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        maybe_finance_role_postgres_docker_image_tag: "16"
        ```

    ??? variable string "`maybe_finance_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        maybe_finance_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable dict "`maybe_finance_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        maybe_finance_role_postgres_docker_healthcheck: 
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='maybe_finance') }} -U {{ postgres_role_docker_env_user }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`maybe_finance_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        maybe_finance_role_postgres_paths_folder: "{{ maybe_finance_name }}"
        ```

    ??? variable string "`maybe_finance_role_postgres_paths_location`"

        ```yaml
        # Type: string
        maybe_finance_role_postgres_paths_location: "{{ server_appdata_path }}/{{ maybe_finance_role_postgres_paths_folder }}/postgres"
        ```

=== "Paths"

    ??? variable string "`maybe_finance_role_paths_folder`"

        ```yaml
        # Type: string
        maybe_finance_role_paths_folder: "{{ maybe_finance_name }}"
        ```

    ??? variable string "`maybe_finance_role_paths_location`"

        ```yaml
        # Type: string
        maybe_finance_role_paths_location: "{{ server_appdata_path }}/{{ maybe_finance_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`maybe_finance_role_web_subdomain`"

        ```yaml
        # Type: string
        maybe_finance_role_web_subdomain: "{{ maybe_finance_name }}"
        ```

    ??? variable string "`maybe_finance_role_web_domain`"

        ```yaml
        # Type: string
        maybe_finance_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`maybe_finance_role_web_port`"

        ```yaml
        # Type: string
        maybe_finance_role_web_port: "3000"
        ```

    ??? variable string "`maybe_finance_role_web_url`"

        ```yaml
        # Type: string
        maybe_finance_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='maybe_finance') + '.' + lookup('role_var', '_web_domain', role='maybe_finance')
                                     if (lookup('role_var', '_web_subdomain', role='maybe_finance') | length > 0)
                                     else lookup('role_var', '_web_domain', role='maybe_finance')) }}"
        ```

=== "DNS"

    ??? variable string "`maybe_finance_role_dns_record`"

        ```yaml
        # Type: string
        maybe_finance_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='maybe_finance') }}"
        ```

    ??? variable string "`maybe_finance_role_dns_zone`"

        ```yaml
        # Type: string
        maybe_finance_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='maybe_finance') }}"
        ```

    ??? variable bool "`maybe_finance_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        maybe_finance_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`maybe_finance_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        maybe_finance_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`maybe_finance_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        maybe_finance_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`maybe_finance_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        maybe_finance_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`maybe_finance_role_traefik_certresolver`"

        ```yaml
        # Type: string
        maybe_finance_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`maybe_finance_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        maybe_finance_role_traefik_enabled: true
        ```

    ??? variable bool "`maybe_finance_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        maybe_finance_role_traefik_api_enabled: false
        ```

    ??? variable string "`maybe_finance_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        maybe_finance_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`maybe_finance_role_docker_container`"

        ```yaml
        # Type: string
        maybe_finance_role_docker_container: "{{ maybe_finance_name }}"
        ```

    ##### Image

    ??? variable bool "`maybe_finance_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        maybe_finance_role_docker_image_pull: true
        ```

    ??? variable string "`maybe_finance_role_docker_image_tag`"

        ```yaml
        # Type: string
        maybe_finance_role_docker_image_tag: "latest"
        ```

    ??? variable string "`maybe_finance_role_docker_image_repo`"

        ```yaml
        # Type: string
        maybe_finance_role_docker_image_repo: "ghcr.io/maybe-finance/maybe"
        ```

    ??? variable string "`maybe_finance_role_docker_image`"

        ```yaml
        # Type: string
        maybe_finance_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='maybe_finance') }}:{{ lookup('role_var', '_docker_image_tag', role='maybe_finance') }}"
        ```

    ##### Envs

    ??? variable dict "`maybe_finance_role_docker_envs_default`"

        ```yaml
        # Type: dict
        maybe_finance_role_docker_envs_default: 
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          SELF_HOSTED: "true"
          RAILS_FORCE_SSL: "false"
          RAILS_ASSUME_SSL: "false"
          GOOD_JOB_EXECUTION_MODE: "async"
          SECRET_KEY_BASE: "{{ maybe_finance_saltbox_facts.facts.secret_key_base }}"
          DB_USERNAME: "{{ lookup('role_var', '_postgres_user', role='maybe_finance') }}"
          DB_PASSWORD: "{{ lookup('role_var', '_postgres_password', role='maybe_finance') }}"
          DB_HOST: "{{ lookup('role_var', '_postgres_name', role='maybe_finance') }}"
          DB_PORT: "5432"
          REDIS_URL: "redis://{{ maybe_finance_name }}-redis:6379/1"
          POSTGRES_USER: "{{ lookup('role_var', '_postgres_user', role='maybe_finance') }}"
          POSTGRES_PASSWORD: "{{ lookup('role_var', '_postgres_password', role='maybe_finance') }}"
        ```

    ??? variable dict "`maybe_finance_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        maybe_finance_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`maybe_finance_role_docker_volumes_default`"

        ```yaml
        # Type: list
        maybe_finance_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='maybe_finance') }}:/rails/storage"
        ```

    ??? variable list "`maybe_finance_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        maybe_finance_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`maybe_finance_role_docker_hostname`"

        ```yaml
        # Type: string
        maybe_finance_role_docker_hostname: "{{ maybe_finance_name }}"
        ```

    ##### Networks

    ??? variable string "`maybe_finance_role_docker_networks_alias`"

        ```yaml
        # Type: string
        maybe_finance_role_docker_networks_alias: "{{ maybe_finance_name }}"
        ```

    ??? variable list "`maybe_finance_role_docker_networks_default`"

        ```yaml
        # Type: list
        maybe_finance_role_docker_networks_default: []
        ```

    ??? variable list "`maybe_finance_role_docker_networks_custom`"

        ```yaml
        # Type: list
        maybe_finance_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`maybe_finance_role_docker_restart_policy`"

        ```yaml
        # Type: string
        maybe_finance_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`maybe_finance_role_docker_state`"

        ```yaml
        # Type: string
        maybe_finance_role_docker_state: started
        ```

    ##### Dependencies

    ??? variable string "`maybe_finance_role_depends_on`"

        ```yaml
        # Type: string
        maybe_finance_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='maybe_finance') }}"
        ```

    ??? variable string "`maybe_finance_role_depends_on_delay`"

        ```yaml
        # Type: string
        maybe_finance_role_depends_on_delay: "5"
        ```

    ??? variable string "`maybe_finance_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        maybe_finance_role_depends_on_healthchecks: "true"
        ```

=== "Global Override Options"

    ??? variable bool "`maybe_finance_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        maybe_finance_role_autoheal_enabled: true
        ```

    ??? variable string "`maybe_finance_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        maybe_finance_role_depends_on: ""
        ```

    ??? variable string "`maybe_finance_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        maybe_finance_role_depends_on_delay: "0"
        ```

    ??? variable string "`maybe_finance_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        maybe_finance_role_depends_on_healthchecks:
        ```

    ??? variable bool "`maybe_finance_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        maybe_finance_role_diun_enabled: true
        ```

    ??? variable bool "`maybe_finance_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        maybe_finance_role_dns_enabled: true
        ```

    ??? variable bool "`maybe_finance_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        maybe_finance_role_docker_controller: true
        ```

    ??? variable bool "`maybe_finance_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        maybe_finance_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`maybe_finance_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        maybe_finance_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`maybe_finance_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        maybe_finance_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`maybe_finance_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        maybe_finance_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`maybe_finance_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        maybe_finance_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`maybe_finance_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        maybe_finance_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`maybe_finance_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        maybe_finance_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`maybe_finance_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        maybe_finance_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`maybe_finance_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        maybe_finance_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`maybe_finance_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        maybe_finance_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            maybe_finance_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "maybe_finance2.{{ user.domain }}"
              - "maybe_finance.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`maybe_finance_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        maybe_finance_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            maybe_finance_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'maybe_finance2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`maybe_finance_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        maybe_finance_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
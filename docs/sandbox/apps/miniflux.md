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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

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

=== "Basics"

    ??? variable string "`miniflux_name`"

        ```yaml
        # Type: string
        miniflux_name: miniflux
        ```

=== "Settings"

    ??? variable string "`miniflux_role_admin_username`"

        ```yaml
        # Type: string
        miniflux_role_admin_username: "{{ user.name }}"
        ```

    ??? variable string "`miniflux_role_admin_password`"

        ```yaml
        # Type: string
        miniflux_role_admin_password: "{{ user.pass }}"
        ```

    ??? variable string "`miniflux_role_create_admin`"

        ```yaml
        # Type: string
        miniflux_role_create_admin: "1"
        ```

    ??? variable string "`miniflux_role_run_migrations`"

        ```yaml
        # Type: string
        miniflux_role_run_migrations: "1"
        ```

    ??? variable bool "`miniflux_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        miniflux_role_postgres_deploy: true
        ```

    ??? variable string "`miniflux_role_postgres_name`"

        ```yaml
        # Type: string
        miniflux_role_postgres_name: "{{ miniflux_name }}-postgres"
        ```

    ??? variable string "`miniflux_role_postgres_user`"

        ```yaml
        # Type: string
        miniflux_role_postgres_user: "{{ postgres_role_docker_env_user }}"
        ```

    ??? variable string "`miniflux_role_postgres_password`"

        ```yaml
        # Type: string
        miniflux_role_postgres_password: "{{ postgres_role_docker_env_password }}"
        ```

    ??? variable string "`miniflux_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        miniflux_role_postgres_docker_env_db: "miniflux"
        ```

    ??? variable string "`miniflux_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        miniflux_role_postgres_docker_image_tag: "14-alpine"
        ```

    ??? variable string "`miniflux_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        miniflux_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable dict "`miniflux_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        miniflux_role_postgres_docker_healthcheck: 
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='miniflux') }} -U {{ postgres_role_docker_env_user }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`miniflux_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        miniflux_role_postgres_paths_folder: "{{ miniflux_name }}"
        ```

    ??? variable string "`miniflux_role_postgres_paths_location`"

        ```yaml
        # Type: string
        miniflux_role_postgres_paths_location: "{{ server_appdata_path }}/{{ miniflux_role_postgres_paths_folder }}/postgres"
        ```

=== "Paths"

    ??? variable string "`miniflux_role_paths_folder`"

        ```yaml
        # Type: string
        miniflux_role_paths_folder: "{{ miniflux_name }}"
        ```

    ??? variable string "`miniflux_role_paths_location`"

        ```yaml
        # Type: string
        miniflux_role_paths_location: "{{ server_appdata_path }}/{{ miniflux_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`miniflux_role_web_subdomain`"

        ```yaml
        # Type: string
        miniflux_role_web_subdomain: "{{ miniflux_name }}"
        ```

    ??? variable string "`miniflux_role_web_domain`"

        ```yaml
        # Type: string
        miniflux_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`miniflux_role_web_port`"

        ```yaml
        # Type: string
        miniflux_role_web_port: "8080"
        ```

    ??? variable string "`miniflux_role_web_url`"

        ```yaml
        # Type: string
        miniflux_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='miniflux') + '.' + lookup('role_var', '_web_domain', role='miniflux')
                                if (lookup('role_var', '_web_subdomain', role='miniflux') | length > 0)
                                else lookup('role_var', '_web_domain', role='miniflux')) }}"
        ```

=== "DNS"

    ??? variable string "`miniflux_role_dns_record`"

        ```yaml
        # Type: string
        miniflux_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='miniflux') }}"
        ```

    ??? variable string "`miniflux_role_dns_zone`"

        ```yaml
        # Type: string
        miniflux_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='miniflux') }}"
        ```

    ??? variable bool "`miniflux_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        miniflux_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`miniflux_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        miniflux_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`miniflux_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        miniflux_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`miniflux_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        miniflux_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`miniflux_role_traefik_certresolver`"

        ```yaml
        # Type: string
        miniflux_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`miniflux_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        miniflux_role_traefik_enabled: true
        ```

    ??? variable bool "`miniflux_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        miniflux_role_traefik_api_enabled: false
        ```

    ??? variable string "`miniflux_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        miniflux_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`miniflux_role_docker_container`"

        ```yaml
        # Type: string
        miniflux_role_docker_container: "{{ miniflux_name }}"
        ```

    ##### Image

    ??? variable bool "`miniflux_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        miniflux_role_docker_image_pull: true
        ```

    ??? variable string "`miniflux_role_docker_image_tag`"

        ```yaml
        # Type: string
        miniflux_role_docker_image_tag: "latest"
        ```

    ??? variable string "`miniflux_role_docker_image_repo`"

        ```yaml
        # Type: string
        miniflux_role_docker_image_repo: "miniflux/miniflux"
        ```

    ??? variable string "`miniflux_role_docker_image`"

        ```yaml
        # Type: string
        miniflux_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='miniflux') }}:{{ lookup('role_var', '_docker_image_tag', role='miniflux') }}"
        ```

    ##### Envs

    ??? variable dict "`miniflux_role_docker_envs_default`"

        ```yaml
        # Type: dict
        miniflux_role_docker_envs_default: 
          DATABASE_URL: "postgres://{{ lookup('role_var', '_postgres_user', role='miniflux') }}:{{ lookup('role_var', '_postgres_password', role='miniflux') }}@{{ lookup('role_var', '_postgres_name', role='miniflux') }}/{{ lookup('role_var', '_postgres_docker_env_db', role='miniflux') }}?sslmode=disable"
          RUN_MIGRATIONS: "{{ lookup('role_var', '_run_migrations', role='miniflux') }}"
          CREATE_ADMIN: "{{ lookup('role_var', '_create_admin', role='miniflux') }}"
          ADMIN_USERNAME: "{{ lookup('role_var', '_admin_username', role='miniflux') }}"
          ADMIN_PASSWORD: "{{ lookup('role_var', '_admin_password', role='miniflux') }}"
        ```

    ??? variable dict "`miniflux_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        miniflux_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`miniflux_role_docker_volumes_default`"

        ```yaml
        # Type: list
        miniflux_role_docker_volumes_default: 
          - /etc/localtime:/etc/localtime:ro
        ```

    ??? variable list "`miniflux_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        miniflux_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`miniflux_role_docker_hostname`"

        ```yaml
        # Type: string
        miniflux_role_docker_hostname: "{{ miniflux_name }}"
        ```

    ##### Networks

    ??? variable string "`miniflux_role_docker_networks_alias`"

        ```yaml
        # Type: string
        miniflux_role_docker_networks_alias: "{{ miniflux_name }}"
        ```

    ??? variable list "`miniflux_role_docker_networks_default`"

        ```yaml
        # Type: list
        miniflux_role_docker_networks_default: []
        ```

    ??? variable list "`miniflux_role_docker_networks_custom`"

        ```yaml
        # Type: list
        miniflux_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`miniflux_role_docker_restart_policy`"

        ```yaml
        # Type: string
        miniflux_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`miniflux_role_docker_state`"

        ```yaml
        # Type: string
        miniflux_role_docker_state: started
        ```

    ##### Dependencies

    ??? variable string "`minuflux_role_depends_on`"

        ```yaml
        # Type: string
        minuflux_role_depends_on: "{{ minuflux_role_postgres_name }}"
        ```

    ??? variable string "`minuflux_role_depends_on_delay`"

        ```yaml
        # Type: string
        minuflux_role_depends_on_delay: "0"
        ```

    ??? variable string "`minuflux_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        minuflux_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`miniflux_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        miniflux_role_autoheal_enabled: true
        ```

    ??? variable string "`miniflux_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        miniflux_role_depends_on: ""
        ```

    ??? variable string "`miniflux_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        miniflux_role_depends_on_delay: "0"
        ```

    ??? variable string "`miniflux_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        miniflux_role_depends_on_healthchecks:
        ```

    ??? variable bool "`miniflux_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        miniflux_role_diun_enabled: true
        ```

    ??? variable bool "`miniflux_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        miniflux_role_dns_enabled: true
        ```

    ??? variable bool "`miniflux_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        miniflux_role_docker_controller: true
        ```

    ??? variable bool "`miniflux_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        miniflux_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`miniflux_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        miniflux_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`miniflux_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        miniflux_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`miniflux_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        miniflux_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`miniflux_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        miniflux_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`miniflux_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        miniflux_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`miniflux_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        miniflux_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`miniflux_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        miniflux_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            miniflux_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "miniflux2.{{ user.domain }}"
              - "miniflux.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`miniflux_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        miniflux_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            miniflux_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'miniflux2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`miniflux_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        miniflux_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
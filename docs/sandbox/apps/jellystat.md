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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    jellystat_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `jellystat_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `jellystat_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`jellystat_name`"

        ```yaml
        # Type: string
        jellystat_name: jellystat
        ```

=== "Settings"

    ??? variable bool "`jellystat_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_postgres_deploy: true
        ```

    ??? variable string "`jellystat_role_postgres_name`"

        ```yaml
        # Type: string
        jellystat_role_postgres_name: "{{ jellystat_name }}-postgres"
        ```

    ??? variable string "`jellystat_role_postgres_user`"

        ```yaml
        # Type: string
        jellystat_role_postgres_user: "{{ postgres_role_docker_env_user }}"
        ```

    ??? variable string "`jellystat_role_postgres_password`"

        ```yaml
        # Type: string
        jellystat_role_postgres_password: "{{ postgres_role_docker_env_password }}"
        ```

    ??? variable string "`jellystat_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        jellystat_role_postgres_docker_env_db: "jfstat"
        ```

    ??? variable string "`jellystat_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        jellystat_role_postgres_docker_image_tag: "15.2-alpine"
        ```

    ??? variable string "`jellystat_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        jellystat_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable dict "`jellystat_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        jellystat_role_postgres_docker_healthcheck: 
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='jellystat') }} -U {{ postgres_role_docker_env_user }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`jellystat_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        jellystat_role_postgres_paths_folder: "{{ jellystat_name }}"
        ```

    ??? variable string "`jellystat_role_postgres_paths_location`"

        ```yaml
        # Type: string
        jellystat_role_postgres_paths_location: "{{ server_appdata_path }}/{{ jellystat_role_postgres_paths_folder }}/postgres"
        ```

    ??? variable string "`jellystat_log_level`"

        ```yaml
        # Type: string
        jellystat_log_level: "INFO"
        ```

    ??? variable bool "`jellystat_emby`"

        ```yaml
        # Type: bool (true/false)
        jellystat_emby: false
        ```

=== "Paths"

    ??? variable string "`jellystat_role_paths_folder`"

        ```yaml
        # Type: string
        jellystat_role_paths_folder: "{{ jellystat_name }}"
        ```

    ??? variable string "`jellystat_role_paths_location`"

        ```yaml
        # Type: string
        jellystat_role_paths_location: "{{ server_appdata_path }}/{{ jellystat_role_paths_folder }}"
        ```

    ??? variable string "`jellystat_role_paths_jwt_secret_file`"

        ```yaml
        # Type: string
        jellystat_role_paths_jwt_secret_file: "{{ jellystat_role_paths_location }}/jwt_secret.txt"
        ```

=== "Web"

    ??? variable string "`jellystat_role_web_subdomain`"

        ```yaml
        # Type: string
        jellystat_role_web_subdomain: "{{ jellystat_name }}"
        ```

    ??? variable string "`jellystat_role_web_domain`"

        ```yaml
        # Type: string
        jellystat_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`jellystat_role_web_port`"

        ```yaml
        # Type: string
        jellystat_role_web_port: "3000"
        ```

    ??? variable string "`jellystat_role_web_url`"

        ```yaml
        # Type: string
        jellystat_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='jellystat') + '.' + lookup('role_var', '_web_domain', role='jellystat')
                                 if (lookup('role_var', '_web_subdomain', role='jellystat') | length > 0)
                                 else lookup('role_var', '_web_domain', role='jellystat')) }}"
        ```

=== "DNS"

    ??? variable string "`jellystat_role_dns_record`"

        ```yaml
        # Type: string
        jellystat_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='jellystat') }}"
        ```

    ??? variable string "`jellystat_role_dns_zone`"

        ```yaml
        # Type: string
        jellystat_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='jellystat') }}"
        ```

    ??? variable bool "`jellystat_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`jellystat_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        jellystat_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`jellystat_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        jellystat_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`jellystat_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        jellystat_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`jellystat_role_traefik_certresolver`"

        ```yaml
        # Type: string
        jellystat_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`jellystat_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_traefik_enabled: true
        ```

    ??? variable bool "`jellystat_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_traefik_api_enabled: false
        ```

    ??? variable string "`jellystat_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        jellystat_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`jellystat_role_docker_container`"

        ```yaml
        # Type: string
        jellystat_role_docker_container: "{{ jellystat_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`jellystat_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_docker_image_pull: true
        ```

    ??? variable string "`jellystat_role_docker_image_repo`"

        ```yaml
        # Type: string
        jellystat_role_docker_image_repo: "cyfershepard/jellystat"
        ```

    ??? variable string "`jellystat_role_docker_image_tag`"

        ```yaml
        # Type: string
        jellystat_role_docker_image_tag: "latest"
        ```

    ??? variable string "`jellystat_role_docker_image`"

        ```yaml
        # Type: string
        jellystat_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='jellystat') }}:{{ lookup('role_var', '_docker_image_tag', role='jellystat') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`jellystat_role_docker_envs_default`"

        ```yaml
        # Type: dict
        jellystat_role_docker_envs_default: 
          POSTGRES_USER: "{{ lookup('role_var', '_postgres_user', role='jellystat') }}"
          POSTGRES_PASSWORD: "{{ lookup('role_var', '_postgres_password', role='jellystat') }}"
          POSTGRES_IP: "{{ lookup('role_var', '_postgres_name', role='jellystat') }}"
          POSTGRES_PORT: "5432"
          JWT_SECRET: "{{ jwt_token.stdout }}"
        ```

    ??? variable dict "`jellystat_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        jellystat_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`jellystat_role_docker_volumes_default`"

        ```yaml
        # Type: list
        jellystat_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='jellystat') }}:/app/backend/backup-data"
        ```

    ??? variable list "`jellystat_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        jellystat_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`jellystat_role_docker_hostname`"

        ```yaml
        # Type: string
        jellystat_role_docker_hostname: "{{ jellystat_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`jellystat_role_docker_networks_alias`"

        ```yaml
        # Type: string
        jellystat_role_docker_networks_alias: "{{ jellystat_name }}"
        ```

    ??? variable list "`jellystat_role_docker_networks_default`"

        ```yaml
        # Type: list
        jellystat_role_docker_networks_default: []
        ```

    ??? variable list "`jellystat_role_docker_networks_custom`"

        ```yaml
        # Type: list
        jellystat_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`jellystat_role_docker_restart_policy`"

        ```yaml
        # Type: string
        jellystat_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`jellystat_role_docker_state`"

        ```yaml
        # Type: string
        jellystat_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`jellystat_role_depends_on`"

        ```yaml
        # Type: string
        jellystat_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='jellystat') }}"
        ```

    ??? variable string "`jellystat_role_depends_on_delay`"

        ```yaml
        # Type: string
        jellystat_role_depends_on_delay: "0"
        ```

    ??? variable string "`jellystat_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        jellystat_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`jellystat_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        jellystat_role_autoheal_enabled: true
        ```

    ??? variable string "`jellystat_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        jellystat_role_depends_on: ""
        ```

    ??? variable string "`jellystat_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        jellystat_role_depends_on_delay: "0"
        ```

    ??? variable string "`jellystat_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        jellystat_role_depends_on_healthchecks:
        ```

    ??? variable bool "`jellystat_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        jellystat_role_diun_enabled: true
        ```

    ??? variable bool "`jellystat_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        jellystat_role_dns_enabled: true
        ```

    ??? variable bool "`jellystat_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        jellystat_role_docker_controller: true
        ```

    ??? variable bool "`jellystat_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        jellystat_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`jellystat_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        jellystat_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`jellystat_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        jellystat_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`jellystat_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        jellystat_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`jellystat_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`jellystat_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`jellystat_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        jellystat_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`jellystat_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        jellystat_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`jellystat_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        jellystat_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`jellystat_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        jellystat_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            jellystat_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "jellystat2.{{ user.domain }}"
              - "jellystat.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`jellystat_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        jellystat_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            jellystat_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'jellystat2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`jellystat_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        jellystat_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
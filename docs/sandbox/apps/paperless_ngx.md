---
hide:
  - tags
tags:
  - paperless-ngx
  - productivity
  - documents
---

# Paperless NGX

## What is it?

[Paperless NGX](https://github.com/paperless-ngx/paperless-ngx#paperless-ngx) is a simple Django application running in two parts: a Consumer (the thing that does the indexing) and the Web server (the part that lets you search & download already-indexed documents).

Paperless-NGX is forked from paperless-ng to continue the great work and distribute responsibility of supporting and advancing the project among a team of people.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/paperless-ngx/paperless-ngx#paperless-ngx){: .header-icons } | [:octicons-link-16: Docs](https://paperless-ngx.readthedocs.io/en/latest/index.html){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/paperless-ngx/paperless-ngx){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/paperlessngx/paperless-ngx){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-paperless-ngx

```

### 2. URL

- To access pgadmin, visit `https://paperless._yourdomain.com_`

### 3. Setup

!!! info
    Please refer to [this](https://github.com/saltyorg/docs/issues/116#issuecomment-1278733921) comment on the initial PR for questions about google storage!

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        paperless_ngx_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `paperless_ngx_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `paperless_ngx_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`paperless_ngx_name`"

        ```yaml
        # Type: string
        paperless_ngx_name: paperless
        ```

=== "Settings"

    ??? variable bool "`paperless_ngx_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        paperless_ngx_role_postgres_deploy: true
        ```

    ??? variable string "`paperless_ngx_role_postgres_name`"

        ```yaml
        # Type: string
        paperless_ngx_role_postgres_name: "{{ paperless_ngx_name }}-postgres"
        ```

    ??? variable string "`paperless_ngx_role_postgres_user`"

        ```yaml
        # Type: string
        paperless_ngx_role_postgres_user: "{{ postgres_role_docker_env_user }}"
        ```

    ??? variable string "`paperless_ngx_role_postgres_password`"

        ```yaml
        # Type: string
        paperless_ngx_role_postgres_password: "{{ postgres_role_docker_env_password }}"
        ```

    ??? variable string "`paperless_ngx_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        paperless_ngx_role_postgres_docker_env_db: "{{ paperless_ngx_name }}"
        ```

    ??? variable string "`paperless_ngx_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        paperless_ngx_role_postgres_docker_image_tag: "14-alpine"
        ```

    ??? variable string "`paperless_ngx_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        paperless_ngx_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable dict "`paperless_ngx_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        paperless_ngx_role_postgres_docker_healthcheck: 
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='paperless_ngx') }} -U {{ postgres_role_docker_env_user }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`paperless_ngx_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        paperless_ngx_role_postgres_paths_folder: "{{ paperless_ngx_name }}"
        ```

    ??? variable string "`paperless_ngx_role_postgres_paths_location`"

        ```yaml
        # Type: string
        paperless_ngx_role_postgres_paths_location: "{{ server_appdata_path }}/{{ paperless_ngx_role_postgres_paths_folder }}/postgres"
        ```

=== "Paths"

    ??? variable string "`paperless_ngx_role_paths_folder`"

        ```yaml
        # Type: string
        paperless_ngx_role_paths_folder: "{{ paperless_ngx_name }}"
        ```

    ??? variable string "`paperless_ngx_role_paths_location`"

        ```yaml
        # Type: string
        paperless_ngx_role_paths_location: "{{ server_appdata_path }}/{{ paperless_ngx_role_paths_folder }}/app"
        ```

=== "Web"

    ??? variable string "`paperless_ngx_role_web_subdomain`"

        ```yaml
        # Type: string
        paperless_ngx_role_web_subdomain: "{{ paperless_ngx_name }}"
        ```

    ??? variable string "`paperless_ngx_role_web_domain`"

        ```yaml
        # Type: string
        paperless_ngx_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`paperless_ngx_role_web_port`"

        ```yaml
        # Type: string
        paperless_ngx_role_web_port: "8000"
        ```

    ??? variable string "`paperless_ngx_role_web_url`"

        ```yaml
        # Type: string
        paperless_ngx_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='paperless_ngx') + '.' + lookup('role_var', '_web_domain', role='paperless_ngx')
                                     if (lookup('role_var', '_web_subdomain', role='paperless_ngx') | length > 0)
                                     else lookup('role_var', '_web_domain', role='paperless_ngx')) }}"
        ```

=== "DNS"

    ??? variable string "`paperless_ngx_role_dns_record`"

        ```yaml
        # Type: string
        paperless_ngx_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='paperless_ngx') }}"
        ```

    ??? variable string "`paperless_ngx_role_dns_zone`"

        ```yaml
        # Type: string
        paperless_ngx_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='paperless_ngx') }}"
        ```

    ??? variable bool "`paperless_ngx_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        paperless_ngx_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`paperless_ngx_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        paperless_ngx_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`paperless_ngx_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        paperless_ngx_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`paperless_ngx_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        paperless_ngx_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`paperless_ngx_role_traefik_certresolver`"

        ```yaml
        # Type: string
        paperless_ngx_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`paperless_ngx_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        paperless_ngx_role_traefik_enabled: true
        ```

    ??? variable bool "`paperless_ngx_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        paperless_ngx_role_traefik_api_enabled: true
        ```

    ??? variable string "`paperless_ngx_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        paperless_ngx_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/static`)"
        ```

=== "Docker"

    ##### Container

    ??? variable string "`paperless_ngx_role_docker_container`"

        ```yaml
        # Type: string
        paperless_ngx_role_docker_container: "{{ paperless_ngx_name }}"
        ```

    ##### Image

    ??? variable bool "`paperless_ngx_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        paperless_ngx_role_docker_image_pull: true
        ```

    ??? variable string "`paperless_ngx_role_docker_image_tag`"

        ```yaml
        # Type: string
        paperless_ngx_role_docker_image_tag: "latest"
        ```

    ??? variable string "`paperless_ngx_role_docker_image_repo`"

        ```yaml
        # Type: string
        paperless_ngx_role_docker_image_repo: "ghcr.io/paperless-ngx/paperless-ngx"
        ```

    ??? variable string "`paperless_ngx_role_docker_image`"

        ```yaml
        # Type: string
        paperless_ngx_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='paperless_ngx') }}:{{ lookup('role_var', '_docker_image_tag', role='paperless_ngx') }}"
        ```

    ##### Envs

    ??? variable dict "`paperless_ngx_role_docker_envs_default`"

        ```yaml
        # Type: dict
        paperless_ngx_role_docker_envs_default: 
          PAPERLESS_TIME_ZONE: "{{ tz }}"
          USERMAP_UID: "{{ uid }}"
          USERMAP_GID: "{{ gid }}"
          PAPERLESS_REDIS: "redis://{{ paperless_ngx_name }}-redis:6379"
          PAPERLESS_DBHOST: "{{ lookup('role_var', '_postgres_name', role='paperless_ngx') }}"
          PAPERLESS_DBPORT: "5432"
          PAPERLESS_DBNAME: "{{ lookup('role_var', '_postgres_docker_env_db', role='paperless_ngx') }}"
          PAPERLESS_DBPASS: "{{ lookup('role_var', '_postgres_password', role='paperless_ngx') }}"
          PAPERLESS_DBUSER: "{{ lookup('role_var', '_postgres_user', role='paperless_ngx') }}"
          PAPERLESS_URL: "{{ lookup('role_var', '_web_url', role='paperless_ngx') }}"
          PAPERLESS_ENABLE_UPDATE_CHECK: "true"
          PAPERLESS_TRASH_DIR: "../trash/"
          PAPERLESS_TIKA_ENABLED: "1"
          PAPERLESS_TIKA_GOTENBERG_ENDPOINT: http://{{ paperless_ngx_name }}-gotenberg:3000
          PAPERLESS_TIKA_ENDPOINT: "http://{{ paperless_ngx_name }}-tika:9998"
          PAPERLESS_ENABLE_HTTP_REMOTE_USER: "true"
          PAPERLESS_ADMIN_USER: "{{ user.name }}"
          PAPERLESS_ADMIN_PASSWORD: "{{ user.pass }}"
          PAPERLESS_SECRET_KEY: "{{ paperless_ngx_secret_key.stdout }}"
          PAPERLESS_ALLOWED_HOSTS: "*"
          PAPERLESS_CORS_ALLOWED_HOSTS: "http://127.0.0.1,http://::1,http://traefik,http://{{ paperless_ngx_name }},{{ lookup('role_var', '_web_url', role='paperless_ngx') }}"
          PAPERLESS_CSRF_TRUSTED_ORIGINS: "http://127.0.0.1,http://::1,http://traefik,http://{{ paperless_ngx_name }},{{ lookup('role_var', '_web_url', role='paperless_ngx') }}"
        ```

    ??? variable dict "`paperless_ngx_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        paperless_ngx_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`paperless_ngx_role_docker_volumes_default`"

        ```yaml
        # Type: list
        paperless_ngx_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='paperless_ngx') }}/data:/usr/src/paperless/data"
          - "{{ lookup('role_var', '_paths_location', role='paperless_ngx') }}/config:/usr/src/paperless/config"
          - "{{ lookup('role_var', '_paths_location', role='paperless_ngx') }}/consume:/usr/src/paperless/consume"
          - "{{ lookup('role_var', '_paths_location', role='paperless_ngx') }}/media:/usr/src/paperless/media"
          - "{{ lookup('role_var', '_paths_location', role='paperless_ngx') }}/trash:/usr/src/paperless/trash"
        ```

    ??? variable list "`paperless_ngx_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        paperless_ngx_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`paperless_ngx_role_docker_hostname`"

        ```yaml
        # Type: string
        paperless_ngx_role_docker_hostname: "{{ paperless_ngx_name }}"
        ```

    ##### Networks

    ??? variable string "`paperless_ngx_role_docker_networks_alias`"

        ```yaml
        # Type: string
        paperless_ngx_role_docker_networks_alias: "{{ paperless_ngx_name }}"
        ```

    ??? variable list "`paperless_ngx_role_docker_networks_default`"

        ```yaml
        # Type: list
        paperless_ngx_role_docker_networks_default: []
        ```

    ??? variable list "`paperless_ngx_role_docker_networks_custom`"

        ```yaml
        # Type: list
        paperless_ngx_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`paperless_ngx_role_docker_restart_policy`"

        ```yaml
        # Type: string
        paperless_ngx_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`paperless_ngx_role_docker_state`"

        ```yaml
        # Type: string
        paperless_ngx_role_docker_state: started
        ```

    ##### Dependencies

    ??? variable string "`paperless_ngx_role_depends_on`"

        ```yaml
        # Type: string
        paperless_ngx_role_depends_on: "{{ paperless_ngx_role_postgres_name }},{{ paperless_ngx_name }}-redis"
        ```

    ??? variable string "`paperless_ngx_role_depends_on_delay`"

        ```yaml
        # Type: string
        paperless_ngx_role_depends_on_delay: "0"
        ```

    ??? variable string "`paperless_ngx_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        paperless_ngx_role_depends_on_healthchecks: "false"
        ```

    ##### Create Docker Container Timeout

    ??? variable int "`paperless_ngx_docker_create_timeout`"

        ```yaml
        # Type: int
        paperless_ngx_docker_create_timeout: 300
        ```

=== "Global Override Options"

    ??? variable bool "`paperless_ngx_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        paperless_ngx_role_autoheal_enabled: true
        ```

    ??? variable string "`paperless_ngx_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        paperless_ngx_role_depends_on: ""
        ```

    ??? variable string "`paperless_ngx_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        paperless_ngx_role_depends_on_delay: "0"
        ```

    ??? variable string "`paperless_ngx_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        paperless_ngx_role_depends_on_healthchecks:
        ```

    ??? variable bool "`paperless_ngx_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        paperless_ngx_role_diun_enabled: true
        ```

    ??? variable bool "`paperless_ngx_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        paperless_ngx_role_dns_enabled: true
        ```

    ??? variable bool "`paperless_ngx_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        paperless_ngx_role_docker_controller: true
        ```

    ??? variable bool "`paperless_ngx_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        paperless_ngx_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`paperless_ngx_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        paperless_ngx_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`paperless_ngx_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        paperless_ngx_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`paperless_ngx_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        paperless_ngx_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`paperless_ngx_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        paperless_ngx_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`paperless_ngx_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        paperless_ngx_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`paperless_ngx_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        paperless_ngx_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`paperless_ngx_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        paperless_ngx_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`paperless_ngx_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        paperless_ngx_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`paperless_ngx_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        paperless_ngx_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            paperless_ngx_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "paperless_ngx2.{{ user.domain }}"
              - "paperless_ngx.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`paperless_ngx_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        paperless_ngx_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            paperless_ngx_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'paperless_ngx2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`paperless_ngx_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        paperless_ngx_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
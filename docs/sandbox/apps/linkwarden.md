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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        linkwarden_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `linkwarden_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `linkwarden_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`linkwarden_name`"

        ```yaml
        # Type: string
        linkwarden_name: linkwarden
        ```

=== "Settings"

    ??? variable bool "`linkwarden_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_postgres_deploy: true
        ```

    ??? variable string "`linkwarden_role_postgres_name`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_name: "{{ linkwarden_name }}-postgres"
        ```

    ??? variable string "`linkwarden_role_postgres_user`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_user: "{{ linkwarden_name }}"
        ```

    ??? variable string "`linkwarden_role_postgres_password`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_password: "{{ linkwarden_name }}"
        ```

    ??? variable string "`linkwarden_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_docker_env_db: "{{ linkwarden_name }}"
        ```

    ??? variable string "`linkwarden_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_docker_image_tag: "16-alpine"
        ```

    ??? variable string "`linkwarden_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable dict "`linkwarden_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        linkwarden_role_postgres_docker_healthcheck: 
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='linkwarden') }} -U {{ lookup('role_var', '_postgres_user', role='linkwarden') }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`linkwarden_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_paths_folder: "{{ linkwarden_name }}"
        ```

    ??? variable string "`linkwarden_role_postgres_paths_location`"

        ```yaml
        # Type: string
        linkwarden_role_postgres_paths_location: "{{ server_appdata_path }}/{{ linkwarden_role_postgres_paths_folder }}/postgres"
        ```

=== "Paths"

    ??? variable string "`linkwarden_role_paths_folder`"

        ```yaml
        # Type: string
        linkwarden_role_paths_folder: "{{ linkwarden_name }}"
        ```

    ??? variable string "`linkwarden_role_paths_location`"

        ```yaml
        # Type: string
        linkwarden_role_paths_location: "{{ server_appdata_path }}/{{ linkwarden_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`linkwarden_role_web_subdomain`"

        ```yaml
        # Type: string
        linkwarden_role_web_subdomain: "{{ linkwarden_name }}"
        ```

    ??? variable string "`linkwarden_role_web_domain`"

        ```yaml
        # Type: string
        linkwarden_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`linkwarden_role_web_port`"

        ```yaml
        # Type: string
        linkwarden_role_web_port: "3000"
        ```

    ??? variable string "`linkwarden_role_web_url`"

        ```yaml
        # Type: string
        linkwarden_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='linkwarden') + '.' + lookup('role_var', '_web_domain', role='linkwarden')
                                  if (lookup('role_var', '_web_subdomain', role='linkwarden') | length > 0)
                                  else lookup('role_var', '_web_domain', role='linkwarden')) }}"
        ```

=== "DNS"

    ??? variable string "`linkwarden_role_dns_record`"

        ```yaml
        # Type: string
        linkwarden_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='linkwarden') }}"
        ```

    ??? variable string "`linkwarden_role_dns_zone`"

        ```yaml
        # Type: string
        linkwarden_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='linkwarden') }}"
        ```

    ??? variable bool "`linkwarden_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`linkwarden_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        linkwarden_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`linkwarden_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        linkwarden_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`linkwarden_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        linkwarden_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`linkwarden_role_traefik_certresolver`"

        ```yaml
        # Type: string
        linkwarden_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`linkwarden_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_traefik_enabled: true
        ```

    ??? variable bool "`linkwarden_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_traefik_api_enabled: true
        ```

    ??? variable string "`linkwarden_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        linkwarden_role_traefik_api_endpoint: "PathPrefix(`/api`)"
        ```

=== "Docker"

    ##### Container

    ??? variable string "`linkwarden_role_docker_container`"

        ```yaml
        # Type: string
        linkwarden_role_docker_container: "{{ linkwarden_name }}"
        ```

    ##### Image

    ??? variable bool "`linkwarden_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        linkwarden_role_docker_image_pull: true
        ```

    ??? variable string "`linkwarden_role_docker_image_tag`"

        ```yaml
        # Type: string
        linkwarden_role_docker_image_tag: "latest"
        ```

    ??? variable string "`linkwarden_role_docker_image_repo`"

        ```yaml
        # Type: string
        linkwarden_role_docker_image_repo: "ghcr.io/linkwarden/linkwarden"
        ```

    ??? variable string "`linkwarden_role_docker_image`"

        ```yaml
        # Type: string
        linkwarden_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='linkwarden') }}:{{ lookup('role_var', '_docker_image_tag', role='linkwarden') }}"
        ```

    ##### Envs

    ??? variable dict "`linkwarden_role_docker_envs_default`"

        ```yaml
        # Type: dict
        linkwarden_role_docker_envs_default: 
          TZ: "{{ tz }}"
          NEXT_PUBLIC_CREDENTIALS_ENABLED: "true"
          STORAGE_FOLDER: "/data"
          NEXTAUTH_SECRET: "{{ linkwarden_secret_key.stdout }}"
          NEXTAUTH_URL: "{{ lookup('role_var', '_web_url', role='linkwarden') }}/api/v1/auth"
          DATABASE_URL: "postgresql://{{ lookup('role_var', '_postgres_user', role='linkwarden') }}:{{ lookup('role_var', '_postgres_password', role='linkwarden') }}@{{ lookup('role_var', '_postgres_name', role='linkwarden') }}:5432/{{ lookup('role_var', '_postgres_docker_env_db', role='linkwarden') }}"
        ```

    ??? variable dict "`linkwarden_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        linkwarden_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`linkwarden_role_docker_volumes_default`"

        ```yaml
        # Type: list
        linkwarden_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='linkwarden') }}:/data/data"
        ```

    ??? variable list "`linkwarden_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        linkwarden_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`linkwarden_role_docker_hostname`"

        ```yaml
        # Type: string
        linkwarden_role_docker_hostname: "{{ linkwarden_name }}"
        ```

    ##### Networks

    ??? variable string "`linkwarden_role_docker_networks_alias`"

        ```yaml
        # Type: string
        linkwarden_role_docker_networks_alias: "{{ linkwarden_name }}"
        ```

    ??? variable list "`linkwarden_role_docker_networks_default`"

        ```yaml
        # Type: list
        linkwarden_role_docker_networks_default: []
        ```

    ??? variable list "`linkwarden_role_docker_networks_custom`"

        ```yaml
        # Type: list
        linkwarden_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`linkwarden_role_docker_restart_policy`"

        ```yaml
        # Type: string
        linkwarden_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`linkwarden_role_docker_state`"

        ```yaml
        # Type: string
        linkwarden_role_docker_state: started
        ```

    ##### Dependencies

    ??? variable string "`linkwarden_role_depends_on`"

        ```yaml
        # Type: string
        linkwarden_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='linkwarden') }}"
        ```

    ??? variable string "`linkwarden_role_depends_on_delay`"

        ```yaml
        # Type: string
        linkwarden_role_depends_on_delay: "0"
        ```

    ??? variable string "`linkwarden_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        linkwarden_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`linkwarden_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        linkwarden_role_autoheal_enabled: true
        ```

    ??? variable string "`linkwarden_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        linkwarden_role_depends_on: ""
        ```

    ??? variable string "`linkwarden_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        linkwarden_role_depends_on_delay: "0"
        ```

    ??? variable string "`linkwarden_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        linkwarden_role_depends_on_healthchecks:
        ```

    ??? variable bool "`linkwarden_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        linkwarden_role_diun_enabled: true
        ```

    ??? variable bool "`linkwarden_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        linkwarden_role_dns_enabled: true
        ```

    ??? variable bool "`linkwarden_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        linkwarden_role_docker_controller: true
        ```

    ??? variable bool "`linkwarden_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        linkwarden_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`linkwarden_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        linkwarden_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`linkwarden_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        linkwarden_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`linkwarden_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        linkwarden_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`linkwarden_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        linkwarden_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`linkwarden_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        linkwarden_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`linkwarden_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        linkwarden_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`linkwarden_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        linkwarden_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            linkwarden_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "linkwarden2.{{ user.domain }}"
              - "linkwarden.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`linkwarden_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        linkwarden_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            linkwarden_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'linkwarden2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`linkwarden_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        linkwarden_role_web_scheme:
        ```


<!-- END SALTBOX MANAGED VARIABLES SECTION -->

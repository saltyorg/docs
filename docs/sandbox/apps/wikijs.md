---
hide:
  - tags
tags:
  - wikijs
  - documentation
  - wiki
---

# Wikijs

## What is it?

[Wikijs](https://js.wiki/) is a modern, lightweight and powerful wiki app built on NodeJS.

- Manage all aspects of your wiki using the extensive and intuitive admin area.
- Fully customize the appearance of your wiki, including a light and dark mode.
- Make your wiki public, completely private or a mix of both.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into Wikijs with the email and password you set up upon instalation.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://js.wiki/){: .header-icons } | [:octicons-link-16: Docs](https://docs.requarks.io/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/requarks/wiki){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/requarks/wiki){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-wikijs

```

### 2. URL

- To access wikijs, visit `https://wikijs._yourdomain.com_`

### 3. Setup

!!! info
    📢 No default user is configured until you run through the setup screen, so you should ideally run through setup as soon as the container is deployed to secure the site. It is not behind authelia by default.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        wikijs_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `wikijs_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `wikijs_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`wikijs_name`"

        ```yaml
        # Type: string
        wikijs_name: wikijs
        ```

=== "Settings"

    ??? variable bool "`wikijs_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_postgres_deploy: true
        ```

    ??? variable string "`wikijs_role_postgres_name`"

        ```yaml
        # Type: string
        wikijs_role_postgres_name: "{{ wikijs_name }}-postgres"
        ```

    ??? variable string "`wikijs_role_postgres_user`"

        ```yaml
        # Type: string
        wikijs_role_postgres_user: "{{ postgres_role_docker_env_user }}"
        ```

    ??? variable string "`wikijs_role_postgres_password`"

        ```yaml
        # Type: string
        wikijs_role_postgres_password: "{{ postgres_role_docker_env_password }}"
        ```

    ??? variable string "`wikijs_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        wikijs_role_postgres_docker_env_db: "{{ wikijs_name }}"
        ```

    ??? variable string "`wikijs_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        wikijs_role_postgres_docker_image_tag: "15-alpine"
        ```

    ??? variable string "`wikijs_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        wikijs_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable dict "`wikijs_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        wikijs_role_postgres_docker_healthcheck: 
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='wikijs') }} -U {{ postgres_role_docker_env_user }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`wikijs_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        wikijs_role_postgres_paths_folder: "{{ wikijs_name }}"
        ```

    ??? variable string "`wikijs_role_postgres_paths_location`"

        ```yaml
        # Type: string
        wikijs_role_postgres_paths_location: "{{ server_appdata_path }}/{{ wikijs_role_postgres_paths_folder }}/postgres"
        ```

=== "Paths"

    ??? variable string "`wikijs_role_paths_folder`"

        ```yaml
        # Type: string
        wikijs_role_paths_folder: "{{ wikijs_name }}"
        ```

    ??? variable string "`wikijs_role_paths_location`"

        ```yaml
        # Type: string
        wikijs_role_paths_location: "{{ server_appdata_path }}/{{ wikijs_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`wikijs_role_web_subdomain`"

        ```yaml
        # Type: string
        wikijs_role_web_subdomain: "{{ wikijs_name }}"
        ```

    ??? variable string "`wikijs_role_web_domain`"

        ```yaml
        # Type: string
        wikijs_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`wikijs_role_web_port`"

        ```yaml
        # Type: string
        wikijs_role_web_port: "3000"
        ```

    ??? variable string "`wikijs_role_web_url`"

        ```yaml
        # Type: string
        wikijs_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='wikijs') + '.' + lookup('role_var', '_web_domain', role='wikijs')
                              if (lookup('role_var', '_web_subdomain', role='wikijs') | length > 0)
                              else lookup('role_var', '_web_domain', role='wikijs')) }}"
        ```

=== "DNS"

    ??? variable string "`wikijs_role_dns_record`"

        ```yaml
        # Type: string
        wikijs_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='wikijs') }}"
        ```

    ??? variable string "`wikijs_role_dns_zone`"

        ```yaml
        # Type: string
        wikijs_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='wikijs') }}"
        ```

    ??? variable bool "`wikijs_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`wikijs_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        wikijs_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`wikijs_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        wikijs_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`wikijs_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        wikijs_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`wikijs_role_traefik_certresolver`"

        ```yaml
        # Type: string
        wikijs_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`wikijs_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_traefik_enabled: true
        ```

    ??? variable bool "`wikijs_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_traefik_api_enabled: true
        ```

    ??? variable string "`wikijs_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        wikijs_role_traefik_api_endpoint: "PathPrefix(`/graphql`)"
        ```

=== "Docker"

    ##### Container

    ??? variable string "`wikijs_role_docker_container`"

        ```yaml
        # Type: string
        wikijs_role_docker_container: "{{ wikijs_name }}"
        ```

    ##### Image

    ??? variable bool "`wikijs_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_docker_image_pull: true
        ```

    ??? variable string "`wikijs_role_docker_image_repo`"

        ```yaml
        # Type: string
        wikijs_role_docker_image_repo: "ghcr.io/requarks/wiki"
        ```

    ??? variable string "`wikijs_role_docker_image_tag`"

        ```yaml
        # Type: string
        wikijs_role_docker_image_tag: "2"
        ```

    ??? variable string "`wikijs_role_docker_image`"

        ```yaml
        # Type: string
        wikijs_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='wikijs') }}:{{ lookup('role_var', '_docker_image_tag', role='wikijs') }}"
        ```

    ##### Envs

    ??? variable dict "`wikijs_role_docker_envs_default`"

        ```yaml
        # Type: dict
        wikijs_role_docker_envs_default: 
          TZ: "{{ tz }}"
          DB_TYPE: "postgres"
          DB_HOST: "{{ lookup('role_var', '_postgres_name', role='wikijs') }}"
          DB_PORT: "5432"
          DB_USER: "{{ lookup('role_var', '_postgres_user', role='wikijs') }}"
          DB_PASS: "{{ lookup('role_var', '_postgres_password', role='wikijs') }}"
          DB_NAME: "{{ lookup('role_var', '_postgres_docker_env_db', role='wikijs') }}"
        ```

    ??? variable dict "`wikijs_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        wikijs_role_docker_envs_custom: {}
        ```

    ##### Hostname

    ??? variable string "`wikijs_role_docker_hostname`"

        ```yaml
        # Type: string
        wikijs_role_docker_hostname: "{{ wikijs_name }}"
        ```

    ##### Networks

    ??? variable string "`wikijs_role_docker_networks_alias`"

        ```yaml
        # Type: string
        wikijs_role_docker_networks_alias: "{{ wikijs_name }}"
        ```

    ??? variable list "`wikijs_role_docker_networks_default`"

        ```yaml
        # Type: list
        wikijs_role_docker_networks_default: []
        ```

    ??? variable list "`wikijs_role_docker_networks_custom`"

        ```yaml
        # Type: list
        wikijs_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`wikijs_role_docker_restart_policy`"

        ```yaml
        # Type: string
        wikijs_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`wikijs_role_docker_state`"

        ```yaml
        # Type: string
        wikijs_role_docker_state: started
        ```

    ##### Dependencies

    ??? variable string "`wikijs_role_depends_on`"

        ```yaml
        # Type: string
        wikijs_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='wikijs') }}"
        ```

    ??? variable string "`wikijs_role_depends_on_delay`"

        ```yaml
        # Type: string
        wikijs_role_depends_on_delay: "0"
        ```

    ??? variable string "`wikijs_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        wikijs_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`wikijs_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        wikijs_role_autoheal_enabled: true
        ```

    ??? variable string "`wikijs_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        wikijs_role_depends_on: ""
        ```

    ??? variable string "`wikijs_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        wikijs_role_depends_on_delay: "0"
        ```

    ??? variable string "`wikijs_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        wikijs_role_depends_on_healthchecks:
        ```

    ??? variable bool "`wikijs_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        wikijs_role_diun_enabled: true
        ```

    ??? variable bool "`wikijs_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        wikijs_role_dns_enabled: true
        ```

    ??? variable bool "`wikijs_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        wikijs_role_docker_controller: true
        ```

    ??? variable bool "`wikijs_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        wikijs_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`wikijs_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        wikijs_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`wikijs_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        wikijs_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`wikijs_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        wikijs_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`wikijs_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        wikijs_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`wikijs_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        wikijs_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`wikijs_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        wikijs_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`wikijs_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        wikijs_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            wikijs_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "wikijs2.{{ user.domain }}"
              - "wikijs.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`wikijs_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        wikijs_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            wikijs_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'wikijs2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`wikijs_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        wikijs_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
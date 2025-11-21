---
icon: material/docker
hide:
  - tags
tags:
  - joplin
  - productivity
  - notes
---

# Joplin

## Overview

[Joplin](https://joplinapp.org/) is an open source note-taking app. Capture your thoughts and securely access them from any device.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://joplinapp.org/){: .header-icons } | [:octicons-link-16: Docs](https://joplinapp.org/desktop/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/laurent22/joplin){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/florider89/joplin-server){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-joplin

```

### 2. URL

- To access Joplin, visit <https://joplin.iYOUR_DOMAIN_NAMEi>

### 3. Setup

!!! info
    Default login for joplin is
    `email: admin@localhost`
    `password: admin`

Change this asap.

- Visit [here](https://joplinapp.org/e2ee/) to learn how to use end to end encryption. (Very simple)

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    joplin_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `joplin_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `joplin_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`joplin_name`"

        ```yaml
        # Type: string
        joplin_name: joplin
        ```

=== "Settings"

    ??? variable bool "`joplin_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        joplin_role_postgres_deploy: true
        ```

    ??? variable string "`joplin_role_postgres_name`"

        ```yaml
        # Type: string
        joplin_role_postgres_name: "{{ joplin_name }}-postgres"
        ```

    ??? variable string "`joplin_role_postgres_user`"

        ```yaml
        # Type: string
        joplin_role_postgres_user: "joplin"
        ```

    ??? variable string "`joplin_role_postgres_password`"

        ```yaml
        # Type: string
        joplin_role_postgres_password: "joplin"
        ```

    ??? variable string "`joplin_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        joplin_role_postgres_docker_env_db: "joplin"
        ```

    ??? variable string "`joplin_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        joplin_role_postgres_docker_image_tag: "13"
        ```

    ??? variable string "`joplin_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        joplin_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable dict "`joplin_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        joplin_role_postgres_docker_healthcheck:
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='joplin') }} -U {{ lookup('role_var', '_postgres_user', role='joplin') }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`joplin_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        joplin_role_postgres_paths_folder: "{{ joplin_name }}"
        ```

    ??? variable string "`joplin_role_postgres_paths_location`"

        ```yaml
        # Type: string
        joplin_role_postgres_paths_location: "{{ server_appdata_path }}/{{ joplin_role_postgres_paths_folder }}/postgres"
        ```

=== "Paths"

    ??? variable string "`joplin_role_paths_folder`"

        ```yaml
        # Type: string
        joplin_role_paths_folder: "{{ joplin_name }}"
        ```

    ??? variable string "`joplin_role_paths_location`"

        ```yaml
        # Type: string
        joplin_role_paths_location: "{{ server_appdata_path }}/{{ joplin_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`joplin_role_web_subdomain`"

        ```yaml
        # Type: string
        joplin_role_web_subdomain: "{{ joplin_name }}"
        ```

    ??? variable string "`joplin_role_web_domain`"

        ```yaml
        # Type: string
        joplin_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`joplin_role_web_port`"

        ```yaml
        # Type: string
        joplin_role_web_port: "22300"
        ```

    ??? variable string "`joplin_role_web_url`"

        ```yaml
        # Type: string
        joplin_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='joplin') + '.' + lookup('role_var', '_web_domain', role='joplin')
                              if (lookup('role_var', '_web_subdomain', role='joplin') | length > 0)
                              else lookup('role_var', '_web_domain', role='joplin')) }}"
        ```

=== "DNS"

    ??? variable string "`joplin_role_dns_record`"

        ```yaml
        # Type: string
        joplin_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='joplin') }}"
        ```

    ??? variable string "`joplin_role_dns_zone`"

        ```yaml
        # Type: string
        joplin_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='joplin') }}"
        ```

    ??? variable bool "`joplin_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        joplin_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`joplin_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        joplin_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`joplin_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        joplin_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`joplin_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        joplin_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`joplin_role_traefik_certresolver`"

        ```yaml
        # Type: string
        joplin_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`joplin_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        joplin_role_traefik_enabled: true
        ```

    ??? variable bool "`joplin_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        joplin_role_traefik_api_enabled: false
        ```

    ??? variable string "`joplin_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        joplin_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`joplin_role_docker_container`"

        ```yaml
        # Type: string
        joplin_role_docker_container: "{{ joplin_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`joplin_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        joplin_role_docker_image_pull: true
        ```

    ??? variable string "`joplin_role_docker_image_repo`"

        ```yaml
        # Type: string
        joplin_role_docker_image_repo: "joplin/server"
        ```

    ??? variable string "`joplin_role_docker_image_tag`"

        ```yaml
        # Type: string
        joplin_role_docker_image_tag: "latest"
        ```

    ??? variable string "`joplin_role_docker_image`"

        ```yaml
        # Type: string
        joplin_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='joplin') }}:{{ lookup('role_var', '_docker_image_tag', role='joplin') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`joplin_role_docker_envs_default`"

        ```yaml
        # Type: dict
        joplin_role_docker_envs_default:
          TZ: "{{ tz }}"
          APP_BASE_URL: "{{ lookup('role_var', '_web_url', role='joplin') }}"
          APP_PORT: "22300"
          POSTGRES_PASSWORD: "{{ lookup('role_var', '_postgres_password', role='joplin') }}"
          POSTGRES_DATABASE: "{{ lookup('role_var', '_postgres_docker_env_db', role='joplin') }}"
          POSTGRES_USER: "{{ lookup('role_var', '_postgres_user', role='joplin') }}"
          POSTGRES_PORT: "5432"
          POSTGRES_HOST: "{{ lookup('role_var', '_postgres_name', role='joplin') }}"
          DB_CLIENT: "pg"
        ```

    ??? variable dict "`joplin_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        joplin_role_docker_envs_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`joplin_role_docker_hostname`"

        ```yaml
        # Type: string
        joplin_role_docker_hostname: "{{ joplin_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`joplin_role_docker_networks_alias`"

        ```yaml
        # Type: string
        joplin_role_docker_networks_alias: "{{ joplin_name }}"
        ```

    ??? variable list "`joplin_role_docker_networks_default`"

        ```yaml
        # Type: list
        joplin_role_docker_networks_default: []
        ```

    ??? variable list "`joplin_role_docker_networks_custom`"

        ```yaml
        # Type: list
        joplin_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`joplin_role_docker_restart_policy`"

        ```yaml
        # Type: string
        joplin_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`joplin_role_docker_state`"

        ```yaml
        # Type: string
        joplin_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`joplin_role_depends_on`"

        ```yaml
        # Type: string
        joplin_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='joplin') }}"
        ```

    ??? variable string "`joplin_role_depends_on_delay`"

        ```yaml
        # Type: string
        joplin_role_depends_on_delay: "0"
        ```

    ??? variable string "`joplin_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        joplin_role_depends_on_healthchecks: "false"
        ```

    <h5>Create Docker Container Timeout</h5>

    ??? variable int "`joplin_docker_create_timeout`"

        ```yaml
        # Type: int
        joplin_docker_create_timeout: 300
        ```

=== "Global Override Options"

    ??? variable bool "`joplin_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        joplin_role_autoheal_enabled: true
        ```

    ??? variable string "`joplin_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        joplin_role_depends_on: ""
        ```

    ??? variable string "`joplin_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        joplin_role_depends_on_delay: "0"
        ```

    ??? variable string "`joplin_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        joplin_role_depends_on_healthchecks:
        ```

    ??? variable bool "`joplin_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        joplin_role_diun_enabled: true
        ```

    ??? variable bool "`joplin_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        joplin_role_dns_enabled: true
        ```

    ??? variable bool "`joplin_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        joplin_role_docker_controller: true
        ```

    ??? variable bool "`joplin_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        joplin_role_docker_volumes_download:
        ```

    ??? variable bool "`joplin_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        joplin_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`joplin_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        joplin_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`joplin_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        joplin_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`joplin_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        joplin_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`joplin_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        joplin_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`joplin_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        joplin_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`joplin_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        joplin_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`joplin_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        joplin_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`joplin_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        joplin_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`joplin_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        joplin_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            joplin_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "joplin2.{{ user.domain }}"
              - "joplin.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`joplin_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        joplin_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            joplin_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'joplin2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`joplin_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        joplin_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
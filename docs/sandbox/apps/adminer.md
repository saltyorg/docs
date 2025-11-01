---
hide:
  - tags
tags:
  - adminer
  - database
  - mysql
---

# Adminer

## Overview

[Adminer](https://www.adminer.org/) Adminer (formerly phpMinAdmin) is a full-featured database management tool written in PHP. Adminer is available for MySQL, MariaDB, PostgreSQL, SQLite, MS SQL, Oracle, Elasticsearch, MongoDB and others via plugin.

!!! info "Protected Role"
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.adminer.org/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/vrana/adminer/#readme){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/vrana/adminer){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/adminer/){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-adminer

```

### 2. URL

- To access Adminer, visit <https://adminer.iYOUR_DOMAIN_NAMEi>

### 3. Setup

- Default login for [MariaDB](../../apps/mariadb.md)

``` yaml title="Adminer Mariadb Login"
  System: Mysql
  Server: mariadb:3306
  Username: root
  Password: password321
```

- Default login for [Postgres](../../apps/postgres.md)

``` yaml title="Adminer Postgres Login"
  System: PostgreSQL
  Server: postgres:5432
  Username: your_saltbox_user
  Password: password4321
```

??? tip "Adminer Plugins"
    Adminer has a number of plugins available to extend its functionality. You can find them [here](https://www.adminer.org/en/plugins/).

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    adminer_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `adminer_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `adminer_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`adminer_name`"

        ```yaml
        # Type: string
        adminer_name: adminer
        ```

=== "Web"

    ??? variable string "`adminer_role_web_subdomain`"

        ```yaml
        # Type: string
        adminer_role_web_subdomain: "{{ adminer_name }}"
        ```

    ??? variable string "`adminer_role_web_domain`"

        ```yaml
        # Type: string
        adminer_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`adminer_role_web_port`"

        ```yaml
        # Type: string
        adminer_role_web_port: "8080"
        ```

    ??? variable string "`adminer_role_web_url`"

        ```yaml
        # Type: string
        adminer_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='adminer') + '.' + lookup('role_var', '_web_domain', role='adminer')
                               if (lookup('role_var', '_web_subdomain', role='adminer') | length > 0)
                               else lookup('role_var', '_web_domain', role='adminer')) }}"
        ```

=== "DNS"

    ??? variable string "`adminer_role_dns_record`"

        ```yaml
        # Type: string
        adminer_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='adminer') }}"
        ```

    ??? variable string "`adminer_role_dns_zone`"

        ```yaml
        # Type: string
        adminer_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='adminer') }}"
        ```

    ??? variable bool "`adminer_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        adminer_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`adminer_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        adminer_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`adminer_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        adminer_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`adminer_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        adminer_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`adminer_role_traefik_certresolver`"

        ```yaml
        # Type: string
        adminer_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`adminer_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        adminer_role_traefik_enabled: true
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`adminer_role_docker_container`"

        ```yaml
        # Type: string
        adminer_role_docker_container: "{{ adminer_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`adminer_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        adminer_role_docker_image_pull: true
        ```

    ??? variable string "`adminer_role_docker_image_repo`"

        ```yaml
        # Type: string
        adminer_role_docker_image_repo: "adminer"
        ```

    ??? variable string "`adminer_role_docker_image_tag`"

        ```yaml
        # Type: string
        adminer_role_docker_image_tag: "latest"
        ```

    ??? variable string "`adminer_role_docker_image`"

        ```yaml
        # Type: string
        adminer_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='adminer') }}:{{ lookup('role_var', '_docker_image_tag', role='adminer') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`adminer_role_docker_envs_default`"

        ```yaml
        # Type: dict
        adminer_role_docker_envs_default: 
          ADMINER_DEFAULT_SERVER: "mysql"
        ```

    ??? variable dict "`adminer_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        adminer_role_docker_envs_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`adminer_role_docker_hostname`"

        ```yaml
        # Type: string
        adminer_role_docker_hostname: "{{ adminer_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`adminer_role_docker_networks_alias`"

        ```yaml
        # Type: string
        adminer_role_docker_networks_alias: "{{ adminer_name }}"
        ```

    ??? variable list "`adminer_role_docker_networks_default`"

        ```yaml
        # Type: list
        adminer_role_docker_networks_default: []
        ```

    ??? variable list "`adminer_role_docker_networks_custom`"

        ```yaml
        # Type: list
        adminer_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`adminer_role_docker_restart_policy`"

        ```yaml
        # Type: string
        adminer_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`adminer_role_docker_state`"

        ```yaml
        # Type: string
        adminer_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`adminer_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        adminer_role_autoheal_enabled: true
        ```

    ??? variable string "`adminer_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        adminer_role_depends_on: ""
        ```

    ??? variable string "`adminer_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        adminer_role_depends_on_delay: "0"
        ```

    ??? variable string "`adminer_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        adminer_role_depends_on_healthchecks:
        ```

    ??? variable bool "`adminer_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        adminer_role_diun_enabled: true
        ```

    ??? variable bool "`adminer_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        adminer_role_dns_enabled: true
        ```

    ??? variable bool "`adminer_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        adminer_role_docker_controller: true
        ```

    ??? variable bool "`adminer_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        adminer_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`adminer_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        adminer_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`adminer_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        adminer_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`adminer_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        adminer_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`adminer_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        adminer_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`adminer_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        adminer_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`adminer_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        adminer_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`adminer_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        adminer_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`adminer_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        adminer_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`adminer_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        adminer_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            adminer_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "adminer2.{{ user.domain }}"
              - "adminer.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`adminer_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        adminer_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            adminer_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'adminer2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`adminer_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        adminer_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
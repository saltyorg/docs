---
hide:
  - tags
tags:
  - phpmyadmin
  - database
  - admin
---

# phpmyadmin

## What is it?

[phpmyadmin](https://www.phpmyadmin.net/) is a free software tool written in PHP, intended to handle the administration of MySQL over the Web. phpMyAdmin supports a wide range of operations on MySQL and MariaDB. Frequently used operations (managing databases, tables, columns, relations, indexes, users, permissions, etc) can be performed via the user interface, while you still have the ability to directly execute any SQL statement.

- Intuitive web interface
- Support for most MySQL features:
  - browse and drop databases, tables, views, fields and indexes
  - create, copy, drop, rename and alter databases, tables, fields and indexes
  - maintenance server, databases and tables, with proposals on server configuration
  - execute, edit and bookmark any SQL-statement, even batch-queries
  - manage MySQL user accounts and privileges
  - manage stored procedures and triggers
- Import data from CSV and SQL
- Export data to various formats: CSV, SQL, XML, PDF, ISO/IEC 26300 - OpenDocument Text and Spreadsheet, Word, LATEX and others
- Administering multiple servers
- Creating graphics of your database layout in various formats
- Creating complex queries using Query-by-example (QBE)
- Searching globally in a database or a subset of it
- Transforming stored data into any format using a set of predefined functions, like displaying BLOB-data as image or download-link

!!! info
    By default, the role **IS** protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.phpmyadmin.net/){: .header-icons } | [:octicons-link-16: Docs](https://www.phpmyadmin.net/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/phpmyadmin/phpmyadmin){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/phpmyadmin/phpmyadmin/){: .header-icons }|

Recommended install types: Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-phpmyadmin

```

### 2. URL

- To access phpmyadmin, visit `https://phpmyadmin._yourdomain.com_`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        phpmyadmin_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `phpmyadmin_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `phpmyadmin_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`phpmyadmin_name`"

        ```yaml
        # Type: string
        phpmyadmin_name: phpmyadmin
        ```

=== "Web"

    ??? variable string "`phpmyadmin_role_web_subdomain`"

        ```yaml
        # Type: string
        phpmyadmin_role_web_subdomain: "{{ phpmyadmin_name }}"
        ```

    ??? variable string "`phpmyadmin_role_web_domain`"

        ```yaml
        # Type: string
        phpmyadmin_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`phpmyadmin_role_web_port`"

        ```yaml
        # Type: string
        phpmyadmin_role_web_port: "80"
        ```

    ??? variable string "`phpmyadmin_role_web_url`"

        ```yaml
        # Type: string
        phpmyadmin_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='phpmyadmin') + '.' + lookup('role_var', '_web_domain', role='phpmyadmin')
                                  if (lookup('role_var', '_web_subdomain', role='phpmyadmin') | length > 0)
                                  else lookup('role_var', '_web_domain', role='phpmyadmin')) }}"
        ```

=== "DNS"

    ??? variable string "`phpmyadmin_role_dns_record`"

        ```yaml
        # Type: string
        phpmyadmin_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='phpmyadmin') }}"
        ```

    ??? variable string "`phpmyadmin_role_dns_zone`"

        ```yaml
        # Type: string
        phpmyadmin_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='phpmyadmin') }}"
        ```

    ??? variable bool "`phpmyadmin_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        phpmyadmin_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`phpmyadmin_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        phpmyadmin_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`phpmyadmin_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        phpmyadmin_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`phpmyadmin_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        phpmyadmin_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`phpmyadmin_role_traefik_certresolver`"

        ```yaml
        # Type: string
        phpmyadmin_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`phpmyadmin_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        phpmyadmin_role_traefik_enabled: true
        ```

    ??? variable bool "`phpmyadmin_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        phpmyadmin_role_traefik_api_enabled: false
        ```

    ??? variable string "`phpmyadmin_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        phpmyadmin_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`phpmyadmin_role_docker_container`"

        ```yaml
        # Type: string
        phpmyadmin_role_docker_container: "{{ phpmyadmin_name }}"
        ```

    ##### Image

    ??? variable bool "`phpmyadmin_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        phpmyadmin_role_docker_image_pull: true
        ```

    ??? variable string "`phpmyadmin_role_docker_image_tag`"

        ```yaml
        # Type: string
        phpmyadmin_role_docker_image_tag: "latest"
        ```

    ??? variable string "`phpmyadmin_role_docker_image_repo`"

        ```yaml
        # Type: string
        phpmyadmin_role_docker_image_repo: "phpmyadmin"
        ```

    ??? variable string "`phpmyadmin_role_docker_image`"

        ```yaml
        # Type: string
        phpmyadmin_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='phpmyadmin') }}:{{ lookup('role_var', '_docker_image_tag', role='phpmyadmin') }}"
        ```

    ##### Envs

    ??? variable dict "`phpmyadmin_role_docker_envs_default`"

        ```yaml
        # Type: dict
        phpmyadmin_role_docker_envs_default: 
          TZ: "{{ tz }}"
          PMA_ARBITRARY: "1"
          PMA_ABSOLUTE_URI: "{{ lookup('role_var', '_web_url', role='phpmyadmin') }}"
          PMA_VERBOSE: "Saltbox"
          PMA_PORT: "3306"
          HIDE_PHP_VERSION: "true"
        ```

    ??? variable dict "`phpmyadmin_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        phpmyadmin_role_docker_envs_custom: {}
        ```

    ##### Hostname

    ??? variable string "`phpmyadmin_role_docker_hostname`"

        ```yaml
        # Type: string
        phpmyadmin_role_docker_hostname: "{{ phpmyadmin_name }}"
        ```

    ##### Networks

    ??? variable string "`phpmyadmin_role_docker_networks_alias`"

        ```yaml
        # Type: string
        phpmyadmin_role_docker_networks_alias: "{{ phpmyadmin_name }}"
        ```

    ??? variable list "`phpmyadmin_role_docker_networks_default`"

        ```yaml
        # Type: list
        phpmyadmin_role_docker_networks_default: []
        ```

    ??? variable list "`phpmyadmin_role_docker_networks_custom`"

        ```yaml
        # Type: list
        phpmyadmin_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`phpmyadmin_role_docker_restart_policy`"

        ```yaml
        # Type: string
        phpmyadmin_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`phpmyadmin_role_docker_state`"

        ```yaml
        # Type: string
        phpmyadmin_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`phpmyadmin_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        phpmyadmin_role_autoheal_enabled: true
        ```

    ??? variable string "`phpmyadmin_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        phpmyadmin_role_depends_on: ""
        ```

    ??? variable string "`phpmyadmin_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        phpmyadmin_role_depends_on_delay: "0"
        ```

    ??? variable string "`phpmyadmin_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        phpmyadmin_role_depends_on_healthchecks:
        ```

    ??? variable bool "`phpmyadmin_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        phpmyadmin_role_diun_enabled: true
        ```

    ??? variable bool "`phpmyadmin_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        phpmyadmin_role_dns_enabled: true
        ```

    ??? variable bool "`phpmyadmin_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        phpmyadmin_role_docker_controller: true
        ```

    ??? variable bool "`phpmyadmin_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        phpmyadmin_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`phpmyadmin_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        phpmyadmin_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`phpmyadmin_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        phpmyadmin_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`phpmyadmin_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        phpmyadmin_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`phpmyadmin_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        phpmyadmin_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`phpmyadmin_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        phpmyadmin_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`phpmyadmin_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        phpmyadmin_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`phpmyadmin_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        phpmyadmin_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`phpmyadmin_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        phpmyadmin_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`phpmyadmin_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        phpmyadmin_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            phpmyadmin_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "phpmyadmin2.{{ user.domain }}"
              - "phpmyadmin.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`phpmyadmin_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        phpmyadmin_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            phpmyadmin_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'phpmyadmin2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`phpmyadmin_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        phpmyadmin_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
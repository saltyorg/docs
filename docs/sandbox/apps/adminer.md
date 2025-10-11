---
hide:
  - tags
tags:
  - adminer
  - database
  - mysql
---

# Adminer

## What is it?

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

- To access Adminer, visit `https://adminer._yourdomain.com_`

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

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        adminer_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    adminer_name: adminer

    ```

??? example "Web"

    ```yaml
    # Type: string
    adminer_role_web_subdomain: "{{ adminer_name }}"

    # Type: string
    adminer_role_web_domain: "{{ user.domain }}"

    # Type: string
    adminer_role_web_port: "8080"

    # Type: string
    adminer_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='adminer') + '.' + lookup('role_var', '_web_domain', role='adminer')
                           if (lookup('role_var', '_web_subdomain', role='adminer') | length > 0)
                           else lookup('role_var', '_web_domain', role='adminer')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    adminer_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='adminer') }}"

    # Type: string
    adminer_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='adminer') }}"

    # Type: bool (true/false)
    adminer_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    adminer_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    adminer_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    adminer_role_traefik_middleware_custom: ""

    # Type: string
    adminer_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    adminer_role_traefik_enabled: true

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    adminer_role_docker_container: "{{ adminer_name }}"

    # Image
    # Type: bool (true/false)
    adminer_role_docker_image_pull: true

    # Type: string
    adminer_role_docker_image_repo: "adminer"

    # Type: string
    adminer_role_docker_image_tag: "latest"

    # Type: string
    adminer_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='adminer') }}:{{ lookup('role_var', '_docker_image_tag', role='adminer') }}"

    # Envs
    # Type: dict
    adminer_role_docker_envs_default: 
      ADMINER_DEFAULT_SERVER: "mysql"

    # Type: dict
    adminer_role_docker_envs_custom: {}

    # Hostname
    # Type: string
    adminer_role_docker_hostname: "{{ adminer_name }}"

    # Networks
    # Type: string
    adminer_role_docker_networks_alias: "{{ adminer_name }}"

    # Type: list
    adminer_role_docker_networks_default: []

    # Type: list
    adminer_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    adminer_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    adminer_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    adminer_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    adminer_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    adminer_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    adminer_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    adminer_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    adminer_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    adminer_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    adminer_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    adminer_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    adminer_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    adminer_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    adminer_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    adminer_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    adminer_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    adminer_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    adminer_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    adminer_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        adminer_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "adminer2.{{ user.domain }}"
          - "adminer.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        adminer_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'adminer2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

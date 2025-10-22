---
hide:
  - tags
tags:
  - sqlitebrowser
  - database
  - utility
---

# SQLite Browser

## What is it?

[SQLite Browser](https://sqlitebrowser.org/) is a high quality, visual, open source tool to create, design, and edit database files compatible with SQLite.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://sqlitebrowser.org/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/sqlitebrowser/sqlitebrowser/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/sqlitebrowser/sqlitebrowser){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/sqlitebrowser){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-sqlitebrowser

```

### 2. URL

- To access SQLite Browser, visit `https://sqlitebrowser.xDOMAIN_NAMEx`

- By default, the role is protected behind your Authelia/SSO middleware.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        sqlitebrowser_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `sqlitebrowser_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `sqlitebrowser_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    sqlitebrowser_name: sqlitebrowser

    ```

??? example "Paths"

    ```yaml
    # Type: string
    sqlitebrowser_role_paths_folder: "{{ sqlitebrowser_name }}"

    # Type: string
    sqlitebrowser_role_paths_location: "{{ server_appdata_path }}/{{ sqlitebrowser_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    sqlitebrowser_role_web_subdomain: "{{ sqlitebrowser_name }}"

    # Type: string
    sqlitebrowser_role_web_domain: "{{ user.domain }}"

    # Type: string
    sqlitebrowser_role_web_port: "3000"

    # Type: string
    sqlitebrowser_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='sqlitebrowser') + '.' + lookup('role_var', '_web_domain', role='sqlitebrowser')
                                 if (lookup('role_var', '_web_subdomain', role='sqlitebrowser') | length > 0)
                                 else lookup('role_var', '_web_domain', role='sqlitebrowser')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    sqlitebrowser_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='sqlitebrowser') }}"

    # Type: string
    sqlitebrowser_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='sqlitebrowser') }}"

    # Type: bool (true/false)
    sqlitebrowser_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    sqlitebrowser_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    sqlitebrowser_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    sqlitebrowser_role_traefik_middleware_custom: ""

    # Type: string
    sqlitebrowser_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    sqlitebrowser_role_traefik_enabled: true

    # Type: bool (true/false)
    sqlitebrowser_role_traefik_api_enabled: false

    # Type: string
    sqlitebrowser_role_traefik_api_endpoint: ""

    # Type: bool (true/false)
    sqlitebrowser_role_traefik_error_pages_enabled: false

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    sqlitebrowser_role_docker_container: "{{ sqlitebrowser_name }}"

    # Image
    # Type: bool (true/false)
    sqlitebrowser_role_docker_image_pull: true

    # Type: string
    sqlitebrowser_role_docker_image_repo: "lscr.io/linuxserver/sqlitebrowser"

    # Type: string
    sqlitebrowser_role_docker_image_tag: "latest"

    # Type: string
    sqlitebrowser_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='sqlitebrowser') }}:{{ lookup('role_var', '_docker_image_tag', role='sqlitebrowser') }}"

    # Envs
    # Type: dict
    sqlitebrowser_role_docker_envs_default: 
      TZ: "{{ tz }}"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"

    # Type: dict
    sqlitebrowser_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    sqlitebrowser_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='sqlitebrowser') }}:/config"

    # Type: list
    sqlitebrowser_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    sqlitebrowser_role_docker_hostname: "{{ sqlitebrowser_name }}"

    # Networks
    # Type: string
    sqlitebrowser_role_docker_networks_alias: "{{ sqlitebrowser_name }}"

    # Type: list
    sqlitebrowser_role_docker_networks_default: []

    # Type: list
    sqlitebrowser_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    sqlitebrowser_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    sqlitebrowser_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    sqlitebrowser_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    sqlitebrowser_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    sqlitebrowser_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    sqlitebrowser_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    sqlitebrowser_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    sqlitebrowser_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    sqlitebrowser_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    sqlitebrowser_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    sqlitebrowser_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    sqlitebrowser_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    sqlitebrowser_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    sqlitebrowser_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    sqlitebrowser_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    sqlitebrowser_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    sqlitebrowser_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    sqlitebrowser_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    sqlitebrowser_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        sqlitebrowser_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "sqlitebrowser2.{{ user.domain }}"
          - "sqlitebrowser.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        sqlitebrowser_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'sqlitebrowser2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

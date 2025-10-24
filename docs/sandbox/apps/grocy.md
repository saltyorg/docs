---
hide:
  - tags
tags:
  - grocy
  - inventory
  - household
---

# Grocy

## What is it?

[Grocy](https://grocy.info/) is a self-hosted ERP system for groceries and household management. It features barcode scanning, shopping lists, expiration tracking, and comprehensive inventory management for home use.

!!! info
    By default, the role is **NOT** protected behind your Authelia/SSO middleware. You will need to configure authentication within the application.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://grocy.info/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/grocy/grocy){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/grocy){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-grocy
```

### 2. URL

- To access Grocy, visit `https://grocy._yourdomain.com_`

### 3. Setup

Default login is admin/admin. Configure authentication and users through the application settings.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    grocy_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `grocy_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `grocy_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`grocy_name`"

        ```yaml
        # Type: string
        grocy_name: grocy
        ```

=== "Paths"

    ??? variable string "`grocy_role_paths_folder`"

        ```yaml
        # Type: string
        grocy_role_paths_folder: "{{ grocy_name }}"
        ```

    ??? variable string "`grocy_role_paths_location`"

        ```yaml
        # Type: string
        grocy_role_paths_location: "{{ server_appdata_path }}/{{ grocy_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`grocy_role_web_subdomain`"

        ```yaml
        # Type: string
        grocy_role_web_subdomain: "{{ grocy_name }}"
        ```

    ??? variable string "`grocy_role_web_domain`"

        ```yaml
        # Type: string
        grocy_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`grocy_role_web_port`"

        ```yaml
        # Type: string
        grocy_role_web_port: "80"
        ```

    ??? variable string "`grocy_role_web_url`"

        ```yaml
        # Type: string
        grocy_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='grocy') + '.' + lookup('role_var', '_web_domain', role='grocy')
                             if (lookup('role_var', '_web_subdomain', role='grocy') | length > 0)
                             else lookup('role_var', '_web_domain', role='grocy')) }}"
        ```

=== "DNS"

    ??? variable string "`grocy_role_dns_record`"

        ```yaml
        # Type: string
        grocy_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='grocy') }}"
        ```

    ??? variable string "`grocy_role_dns_zone`"

        ```yaml
        # Type: string
        grocy_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='grocy') }}"
        ```

    ??? variable bool "`grocy_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        grocy_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`grocy_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        grocy_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`grocy_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        grocy_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`grocy_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        grocy_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`grocy_role_traefik_certresolver`"

        ```yaml
        # Type: string
        grocy_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`grocy_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        grocy_role_traefik_enabled: true
        ```

    ??? variable bool "`grocy_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        grocy_role_traefik_api_enabled: false
        ```

    ??? variable string "`grocy_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        grocy_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    Container
    { .sb-h5 }

    ??? variable string "`grocy_role_docker_container`"

        ```yaml
        # Type: string
        grocy_role_docker_container: "{{ grocy_name }}"
        ```

    Image
    { .sb-h5 }

    ??? variable bool "`grocy_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        grocy_role_docker_image_pull: true
        ```

    ??? variable string "`grocy_role_docker_image_repo`"

        ```yaml
        # Type: string
        grocy_role_docker_image_repo: "lscr.io/linuxserver/grocy"
        ```

    ??? variable string "`grocy_role_docker_image_tag`"

        ```yaml
        # Type: string
        grocy_role_docker_image_tag: "latest"
        ```

    ??? variable string "`grocy_role_docker_image`"

        ```yaml
        # Type: string
        grocy_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='grocy') }}:{{ lookup('role_var', '_docker_image_tag', role='grocy') }}"
        ```

    Envs
    { .sb-h5 }

    ??? variable dict "`grocy_role_docker_envs_default`"

        ```yaml
        # Type: dict
        grocy_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`grocy_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        grocy_role_docker_envs_custom: {}
        ```

    Volumes
    { .sb-h5 }

    ??? variable list "`grocy_role_docker_volumes_default`"

        ```yaml
        # Type: list
        grocy_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='grocy') }}:/config"
        ```

    ??? variable list "`grocy_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        grocy_role_docker_volumes_custom: []
        ```

    Hostname
    { .sb-h5 }

    ??? variable string "`grocy_role_docker_hostname`"

        ```yaml
        # Type: string
        grocy_role_docker_hostname: "{{ grocy_name }}"
        ```

    Networks
    { .sb-h5 }

    ??? variable string "`grocy_role_docker_networks_alias`"

        ```yaml
        # Type: string
        grocy_role_docker_networks_alias: "{{ grocy_name }}"
        ```

    ??? variable list "`grocy_role_docker_networks_default`"

        ```yaml
        # Type: list
        grocy_role_docker_networks_default: []
        ```

    ??? variable list "`grocy_role_docker_networks_custom`"

        ```yaml
        # Type: list
        grocy_role_docker_networks_custom: []
        ```

    Restart Policy
    { .sb-h5 }

    ??? variable string "`grocy_role_docker_restart_policy`"

        ```yaml
        # Type: string
        grocy_role_docker_restart_policy: unless-stopped
        ```

    State
    { .sb-h5 }

    ??? variable string "`grocy_role_docker_state`"

        ```yaml
        # Type: string
        grocy_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`grocy_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        grocy_role_autoheal_enabled: true
        ```

    ??? variable string "`grocy_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        grocy_role_depends_on: ""
        ```

    ??? variable string "`grocy_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        grocy_role_depends_on_delay: "0"
        ```

    ??? variable string "`grocy_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        grocy_role_depends_on_healthchecks:
        ```

    ??? variable bool "`grocy_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        grocy_role_diun_enabled: true
        ```

    ??? variable bool "`grocy_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        grocy_role_dns_enabled: true
        ```

    ??? variable bool "`grocy_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        grocy_role_docker_controller: true
        ```

    ??? variable bool "`grocy_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        grocy_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`grocy_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        grocy_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`grocy_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        grocy_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`grocy_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        grocy_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`grocy_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        grocy_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`grocy_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        grocy_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`grocy_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        grocy_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`grocy_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        grocy_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`grocy_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        grocy_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`grocy_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        grocy_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            grocy_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "grocy2.{{ user.domain }}"
              - "grocy.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`grocy_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        grocy_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            grocy_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'grocy2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`grocy_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        grocy_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
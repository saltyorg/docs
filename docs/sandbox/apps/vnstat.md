---
hide:
  - tags
tags:
  - vnstat
  - monitoring
  - network
---

# vnStat

## What is it?

[vnStat dashboard](https://github.com/alexandermarston/vnstat-dashboard) is a user-friendly web dashboard for viewing the following:

- Hourly Statistics Chart (using Google Charts)
- Daily & Monthly Statistics Overview
- Top 10 Day Statistics
- Automatically populated interface selection

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/alexandermarston/vnstat-dashboard){: .header-icons } | [:octicons-link-16: Docs](https://github.com/alexandermarston/vnstat-dashboard){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/alexandermarston/vnstat-dashboard){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/amarston/vnstat-dashboard){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-vnstat

```

### 2. URL

- To access vnStat, visit `https://vnstat._yourdomain.com_`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    vnstat_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `vnstat_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `vnstat_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`vnstat_name`"

        ```yaml
        # Type: string
        vnstat_name: vnstat
        ```

=== "Settings"

    ??? variable string "`vnstat_page_refresh`"

        ```yaml
        # Type: string
        vnstat_page_refresh: "0"
        ```

    ??? variable string "`vnstat_rate_unit`"

        ```yaml
        # Type: string
        vnstat_rate_unit: "1" # Used traffic rate unit, 0: bytes, 1: bits
        ```

=== "Web"

    ??? variable string "`vnstat_role_web_subdomain`"

        ```yaml
        # Type: string
        vnstat_role_web_subdomain: "{{ vnstat_name }}"
        ```

    ??? variable string "`vnstat_role_web_domain`"

        ```yaml
        # Type: string
        vnstat_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`vnstat_role_web_port`"

        ```yaml
        # Type: string
        vnstat_role_web_port: "8685"
        ```

    ??? variable string "`vnstat_role_web_url`"

        ```yaml
        # Type: string
        vnstat_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='vnstat') + '.' + lookup('role_var', '_web_domain', role='vnstat')
                              if (lookup('role_var', '_web_subdomain', role='vnstat') | length > 0)
                              else lookup('role_var', '_web_domain', role='vnstat')) }}"
        ```

=== "DNS"

    ??? variable string "`vnstat_role_dns_record`"

        ```yaml
        # Type: string
        vnstat_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='vnstat') }}"
        ```

    ??? variable string "`vnstat_role_dns_zone`"

        ```yaml
        # Type: string
        vnstat_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='vnstat') }}"
        ```

    ??? variable bool "`vnstat_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        vnstat_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`vnstat_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        vnstat_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`vnstat_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        vnstat_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`vnstat_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        vnstat_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`vnstat_role_traefik_certresolver`"

        ```yaml
        # Type: string
        vnstat_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`vnstat_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        vnstat_role_traefik_enabled: true
        ```

    ??? variable bool "`vnstat_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        vnstat_role_traefik_api_enabled: false
        ```

    ??? variable string "`vnstat_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        vnstat_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    Container
    { .sb-h5 }

    ??? variable string "`vnstat_role_docker_container`"

        ```yaml
        # Type: string
        vnstat_role_docker_container: "{{ vnstat_name }}"
        ```

    Image
    { .sb-h5 }

    ??? variable bool "`vnstat_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        vnstat_role_docker_image_pull: true
        ```

    ??? variable string "`vnstat_role_docker_image_repo`"

        ```yaml
        # Type: string
        vnstat_role_docker_image_repo: "vergoh/vnstat"
        ```

    ??? variable string "`vnstat_role_docker_image_tag`"

        ```yaml
        # Type: string
        vnstat_role_docker_image_tag: "latest"
        ```

    ??? variable string "`vnstat_role_docker_image`"

        ```yaml
        # Type: string
        vnstat_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='vnstat') }}:{{ lookup('role_var', '_docker_image_tag', role='vnstat') }}"
        ```

    Envs
    { .sb-h5 }

    ??? variable dict "`vnstat_role_docker_envs_default`"

        ```yaml
        # Type: dict
        vnstat_role_docker_envs_default: 
          TZ: "{{ tz }}"
          HTTP_PORT: "8685"
          PAGE_REFRESH: "{{ vnstat_page_refresh }}"
          RATE_UNIT: "{{ vnstat_rate_unit }}"
          RUN_VNSTATD: "0"
        ```

    ??? variable dict "`vnstat_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        vnstat_role_docker_envs_custom: {}
        ```

    Volumes
    { .sb-h5 }

    ??? variable list "`vnstat_role_docker_volumes_default`"

        ```yaml
        # Type: list
        vnstat_role_docker_volumes_default: 
          - "vnstat:/var/lib/vnstat:ro"
        ```

    ??? variable list "`vnstat_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        vnstat_role_docker_volumes_custom: []
        ```

    Hostname
    { .sb-h5 }

    ??? variable string "`vnstat_role_docker_hostname`"

        ```yaml
        # Type: string
        vnstat_role_docker_hostname: "{{ vnstat_name }}"
        ```

    Networks
    { .sb-h5 }

    ??? variable string "`vnstat_role_docker_networks_alias`"

        ```yaml
        # Type: string
        vnstat_role_docker_networks_alias: "{{ vnstat_name }}"
        ```

    ??? variable list "`vnstat_role_docker_networks_default`"

        ```yaml
        # Type: list
        vnstat_role_docker_networks_default: []
        ```

    ??? variable list "`vnstat_role_docker_networks_custom`"

        ```yaml
        # Type: list
        vnstat_role_docker_networks_custom: []
        ```

    Restart Policy
    { .sb-h5 }

    ??? variable string "`vnstat_role_docker_restart_policy`"

        ```yaml
        # Type: string
        vnstat_role_docker_restart_policy: unless-stopped
        ```

    State
    { .sb-h5 }

    ??? variable string "`vnstat_role_docker_state`"

        ```yaml
        # Type: string
        vnstat_role_docker_state: started
        ```

    Force Kill
    { .sb-h5 }

    ??? variable bool "`vnstat_role_docker_force_kill`"

        ```yaml
        # Type: bool (true/false)
        vnstat_role_docker_force_kill: true
        ```

=== "Global Override Options"

    ??? variable bool "`vnstat_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        vnstat_role_autoheal_enabled: true
        ```

    ??? variable string "`vnstat_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        vnstat_role_depends_on: ""
        ```

    ??? variable string "`vnstat_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        vnstat_role_depends_on_delay: "0"
        ```

    ??? variable string "`vnstat_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        vnstat_role_depends_on_healthchecks:
        ```

    ??? variable bool "`vnstat_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        vnstat_role_diun_enabled: true
        ```

    ??? variable bool "`vnstat_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        vnstat_role_dns_enabled: true
        ```

    ??? variable bool "`vnstat_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        vnstat_role_docker_controller: true
        ```

    ??? variable bool "`vnstat_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        vnstat_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`vnstat_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        vnstat_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`vnstat_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        vnstat_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`vnstat_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        vnstat_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`vnstat_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        vnstat_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`vnstat_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        vnstat_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`vnstat_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        vnstat_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`vnstat_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        vnstat_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`vnstat_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        vnstat_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`vnstat_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        vnstat_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            vnstat_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "vnstat2.{{ user.domain }}"
              - "vnstat.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`vnstat_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        vnstat_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            vnstat_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'vnstat2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`vnstat_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        vnstat_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
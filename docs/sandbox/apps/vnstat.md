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

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        vnstat_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    vnstat_name: vnstat

    ```

??? example "Settings"

    ```yaml
    # Type: string
    vnstat_page_refresh: "0"

    # Type: string
    vnstat_rate_unit: "1" # Used traffic rate unit, 0: bytes, 1: bits

    ```

??? example "Web"

    ```yaml
    # Type: string
    vnstat_role_web_subdomain: "{{ vnstat_name }}"

    # Type: string
    vnstat_role_web_domain: "{{ user.domain }}"

    # Type: string
    vnstat_role_web_port: "8685"

    # Type: string
    vnstat_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='vnstat') + '.' + lookup('role_var', '_web_domain', role='vnstat')
                          if (lookup('role_var', '_web_subdomain', role='vnstat') | length > 0)
                          else lookup('role_var', '_web_domain', role='vnstat')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    vnstat_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='vnstat') }}"

    # Type: string
    vnstat_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='vnstat') }}"

    # Type: bool (true/false)
    vnstat_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    vnstat_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    vnstat_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    vnstat_role_traefik_middleware_custom: ""

    # Type: string
    vnstat_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    vnstat_role_traefik_enabled: true

    # Type: bool (true/false)
    vnstat_role_traefik_api_enabled: false

    # Type: string
    vnstat_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    vnstat_role_docker_container: "{{ vnstat_name }}"

    # Image
    # Type: bool (true/false)
    vnstat_role_docker_image_pull: true

    # Type: string
    vnstat_role_docker_image_repo: "vergoh/vnstat"

    # Type: string
    vnstat_role_docker_image_tag: "latest"

    # Type: string
    vnstat_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='vnstat') }}:{{ lookup('role_var', '_docker_image_tag', role='vnstat') }}"

    # Envs
    # Type: dict
    vnstat_role_docker_envs_default: 
      TZ: "{{ tz }}"
      HTTP_PORT: "8685"
      PAGE_REFRESH: "{{ vnstat_page_refresh }}"
      RATE_UNIT: "{{ vnstat_rate_unit }}"
      RUN_VNSTATD: "0"

    # Type: dict
    vnstat_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    vnstat_role_docker_volumes_default: 
      - "vnstat:/var/lib/vnstat:ro"

    # Type: list
    vnstat_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    vnstat_role_docker_hostname: "{{ vnstat_name }}"

    # Networks
    # Type: string
    vnstat_role_docker_networks_alias: "{{ vnstat_name }}"

    # Type: list
    vnstat_role_docker_networks_default: []

    # Type: list
    vnstat_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    vnstat_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    vnstat_role_docker_state: started

    # Force Kill
    # Type: bool (true/false)
    vnstat_role_docker_force_kill: true

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    vnstat_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    vnstat_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    vnstat_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    vnstat_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    vnstat_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    vnstat_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    vnstat_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    vnstat_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    vnstat_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    vnstat_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    vnstat_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    vnstat_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    vnstat_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    vnstat_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    vnstat_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    vnstat_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    vnstat_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        vnstat_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "vnstat2.{{ user.domain }}"
          - "vnstat.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        vnstat_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'vnstat2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

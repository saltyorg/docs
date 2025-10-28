---
hide:
  - tags
tags:
  - wrapperr
  - statistics
  - analytics
---

# Wrapperr

## What is it?

[Wrapperr](https://github.com/aunefyren/wrapperr) is a website-based platform and API for collecting user stats within a set timeframe using Tautulli. The data is displayed as a statistics-summary, sort of like Spotify Wrapped. Yes, you need Tautulli to have been running beforehand and currently for this to work. Note: Wrapperr is not behind authelia.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project Home](https://github.com/aunefyren/wrapperr){: .header-icons } | [:octicons-link-16: Docs](https://github.com/aunefyren/wrapperr){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/aunefyren/wrapperr){: .header-icons } | [:material-docker: Docker:](https://hub.docker.com/r/aunefyren/wrapperr){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-wrapperr

```

### 2. URL

- To access Wrapperr, visit <https://wrapperr.iYOUR_DOMAIN_NAMEi>

### 3. Setup

- The very first thing you should do after installing Wrapperr is visit <https://wrapperr.iYOUR_DOMAIN_NAMEi> and configure an admin username/password. <br /> **Do this NOW.**

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    wrapperr_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `wrapperr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `wrapperr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`wrapperr_name`"

        ```yaml
        # Type: string
        wrapperr_name: wrapperr
        ```

=== "Paths"

    ??? variable string "`wrapperr_role_paths_folder`"

        ```yaml
        # Type: string
        wrapperr_role_paths_folder: "{{ wrapperr_name }}"
        ```

    ??? variable string "`wrapperr_role_paths_location`"

        ```yaml
        # Type: string
        wrapperr_role_paths_location: "{{ server_appdata_path }}/{{ wrapperr_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`wrapperr_role_web_subdomain`"

        ```yaml
        # Type: string
        wrapperr_role_web_subdomain: "{{ wrapperr_name }}"
        ```

    ??? variable string "`wrapperr_role_web_domain`"

        ```yaml
        # Type: string
        wrapperr_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`wrapperr_role_web_port`"

        ```yaml
        # Type: string
        wrapperr_role_web_port: "8282"
        ```

    ??? variable string "`wrapperr_role_web_url`"

        ```yaml
        # Type: string
        wrapperr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='wrapperr') + '.' + lookup('role_var', '_web_domain', role='wrapperr')
                                if (lookup('role_var', '_web_subdomain', role='wrapperr') | length > 0)
                                else lookup('role_var', '_web_domain', role='wrapperr')) }}"
        ```

=== "DNS"

    ??? variable string "`wrapperr_role_dns_record`"

        ```yaml
        # Type: string
        wrapperr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='wrapperr') }}"
        ```

    ??? variable string "`wrapperr_role_dns_zone`"

        ```yaml
        # Type: string
        wrapperr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='wrapperr') }}"
        ```

    ??? variable bool "`wrapperr_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`wrapperr_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        wrapperr_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`wrapperr_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        wrapperr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`wrapperr_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        wrapperr_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`wrapperr_role_traefik_certresolver`"

        ```yaml
        # Type: string
        wrapperr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`wrapperr_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_traefik_enabled: true
        ```

    ??? variable bool "`wrapperr_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_traefik_api_enabled: false
        ```

    ??? variable string "`wrapperr_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        wrapperr_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`wrapperr_role_docker_container`"

        ```yaml
        # Type: string
        wrapperr_role_docker_container: "{{ wrapperr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`wrapperr_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_docker_image_pull: true
        ```

    ??? variable string "`wrapperr_role_docker_image_repo`"

        ```yaml
        # Type: string
        wrapperr_role_docker_image_repo: "aunefyren/wrapperr"
        ```

    ??? variable string "`wrapperr_role_docker_image_tag`"

        ```yaml
        # Type: string
        wrapperr_role_docker_image_tag: "latest"
        ```

    ??? variable string "`wrapperr_role_docker_image`"

        ```yaml
        # Type: string
        wrapperr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='wrapperr') }}:{{ lookup('role_var', '_docker_image_tag', role='wrapperr') }}"
        ```

    <h5>Volumes</h5>

    ??? variable list "`wrapperr_role_docker_volumes_default`"

        ```yaml
        # Type: list
        wrapperr_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='wrapperr') }}:/app/config"
        ```

    ??? variable list "`wrapperr_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        wrapperr_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`wrapperr_role_docker_hostname`"

        ```yaml
        # Type: string
        wrapperr_role_docker_hostname: "{{ wrapperr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`wrapperr_role_docker_networks_alias`"

        ```yaml
        # Type: string
        wrapperr_role_docker_networks_alias: "{{ wrapperr_name }}"
        ```

    ??? variable list "`wrapperr_role_docker_networks_default`"

        ```yaml
        # Type: list
        wrapperr_role_docker_networks_default: []
        ```

    ??? variable list "`wrapperr_role_docker_networks_custom`"

        ```yaml
        # Type: list
        wrapperr_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`wrapperr_role_docker_restart_policy`"

        ```yaml
        # Type: string
        wrapperr_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`wrapperr_role_docker_state`"

        ```yaml
        # Type: string
        wrapperr_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`wrapperr_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        wrapperr_role_autoheal_enabled: true
        ```

    ??? variable string "`wrapperr_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        wrapperr_role_depends_on: ""
        ```

    ??? variable string "`wrapperr_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        wrapperr_role_depends_on_delay: "0"
        ```

    ??? variable string "`wrapperr_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        wrapperr_role_depends_on_healthchecks:
        ```

    ??? variable bool "`wrapperr_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        wrapperr_role_diun_enabled: true
        ```

    ??? variable bool "`wrapperr_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        wrapperr_role_dns_enabled: true
        ```

    ??? variable bool "`wrapperr_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        wrapperr_role_docker_controller: true
        ```

    ??? variable bool "`wrapperr_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        wrapperr_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`wrapperr_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        wrapperr_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`wrapperr_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        wrapperr_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`wrapperr_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        wrapperr_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`wrapperr_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`wrapperr_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`wrapperr_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        wrapperr_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`wrapperr_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        wrapperr_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`wrapperr_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        wrapperr_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`wrapperr_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        wrapperr_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            wrapperr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "wrapperr2.{{ user.domain }}"
              - "wrapperr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`wrapperr_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        wrapperr_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            wrapperr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'wrapperr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`wrapperr_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        wrapperr_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
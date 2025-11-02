---
icon: material/docker
hide:
  - tags
tags:
  - freshrss
  - media
  - rss
---

# Freshrss

## Overview

[Freshrss](https://freshrss.org/) is a self-hosted RSS and Atom feed aggregator.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://freshrss.org){: .header-icons } | [:octicons-link-16: Docs](https://freshrss.github.io/FreshRSS/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/FreshRSS/FreshRSS){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/freshrss/freshrss){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-freshrss

```

### 2. URL

- To access Freshrss, visit <https://freshrss.iYOUR_DOMAIN_NAMEi>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    freshrss_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `freshrss_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `freshrss_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`freshrss_name`"

        ```yaml
        # Type: string
        freshrss_name: freshrss
        ```

=== "Paths"

    ??? variable string "`freshrss_role_paths_folder`"

        ```yaml
        # Type: string
        freshrss_role_paths_folder: "{{ freshrss_name }}"
        ```

    ??? variable string "`freshrss_role_paths_location`"

        ```yaml
        # Type: string
        freshrss_role_paths_location: "{{ server_appdata_path }}/{{ lookup('role_var', '_paths_folder', role='freshrss') }}"
        ```

=== "Web"

    ??? variable string "`freshrss_role_web_subdomain`"

        ```yaml
        # Type: string
        freshrss_role_web_subdomain: "{{ freshrss_name }}"
        ```

    ??? variable string "`freshrss_role_web_domain`"

        ```yaml
        # Type: string
        freshrss_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`freshrss_role_web_port`"

        ```yaml
        # Type: string
        freshrss_role_web_port: "80"
        ```

    ??? variable string "`freshrss_role_web_url`"

        ```yaml
        # Type: string
        freshrss_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='freshrss') + '.' + lookup('role_var', '_web_domain', role='freshrss')
                                if (lookup('role_var', '_web_subdomain', role='freshrss') | length > 0)
                                else lookup('role_var', '_web_domain', role='freshrss')) }}"
        ```

=== "DNS"

    ??? variable string "`freshrss_role_dns_record`"

        ```yaml
        # Type: string
        freshrss_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='freshrss') }}"
        ```

    ??? variable string "`freshrss_role_dns_zone`"

        ```yaml
        # Type: string
        freshrss_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='freshrss') }}"
        ```

    ??? variable bool "`freshrss_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        freshrss_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`freshrss_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        freshrss_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`freshrss_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        freshrss_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`freshrss_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        freshrss_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`freshrss_role_traefik_certresolver`"

        ```yaml
        # Type: string
        freshrss_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`freshrss_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        freshrss_role_traefik_enabled: true
        ```

    ??? variable bool "`freshrss_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        freshrss_role_traefik_api_enabled: false
        ```

    ??? variable string "`freshrss_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        freshrss_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`freshrss_role_docker_container`"

        ```yaml
        # Type: string
        freshrss_role_docker_container: "{{ freshrss_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`freshrss_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        freshrss_role_docker_image_pull: true
        ```

    ??? variable string "`freshrss_role_docker_image_repo`"

        ```yaml
        # Type: string
        freshrss_role_docker_image_repo: "lscr.io/linuxserver/freshrss"
        ```

    ??? variable string "`freshrss_role_docker_image_tag`"

        ```yaml
        # Type: string
        freshrss_role_docker_image_tag: "amd64-latest"
        ```

    ??? variable string "`freshrss_role_docker_image`"

        ```yaml
        # Type: string
        freshrss_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='freshrss') }}:{{ lookup('role_var', '_docker_image_tag', role='freshrss') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`freshrss_role_docker_envs_default`"

        ```yaml
        # Type: dict
        freshrss_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`freshrss_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        freshrss_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`freshrss_role_docker_volumes_default`"

        ```yaml
        # Type: list
        freshrss_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='freshrss') }}:/config"
        ```

    ??? variable list "`freshrss_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        freshrss_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`freshrss_role_docker_hostname`"

        ```yaml
        # Type: string
        freshrss_role_docker_hostname: "{{ freshrss_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`freshrss_role_docker_networks_alias`"

        ```yaml
        # Type: string
        freshrss_role_docker_networks_alias: "{{ freshrss_name }}"
        ```

    ??? variable list "`freshrss_role_docker_networks_default`"

        ```yaml
        # Type: list
        freshrss_role_docker_networks_default: []
        ```

    ??? variable list "`freshrss_role_docker_networks_custom`"

        ```yaml
        # Type: list
        freshrss_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`freshrss_role_docker_restart_policy`"

        ```yaml
        # Type: string
        freshrss_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`freshrss_role_docker_state`"

        ```yaml
        # Type: string
        freshrss_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`freshrss_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        freshrss_role_autoheal_enabled: true
        ```

    ??? variable string "`freshrss_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        freshrss_role_depends_on: ""
        ```

    ??? variable string "`freshrss_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        freshrss_role_depends_on_delay: "0"
        ```

    ??? variable string "`freshrss_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        freshrss_role_depends_on_healthchecks:
        ```

    ??? variable bool "`freshrss_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        freshrss_role_diun_enabled: true
        ```

    ??? variable bool "`freshrss_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        freshrss_role_dns_enabled: true
        ```

    ??? variable bool "`freshrss_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        freshrss_role_docker_controller: true
        ```

    ??? variable bool "`freshrss_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        freshrss_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`freshrss_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        freshrss_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`freshrss_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        freshrss_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`freshrss_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        freshrss_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`freshrss_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        freshrss_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`freshrss_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        freshrss_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`freshrss_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        freshrss_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`freshrss_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        freshrss_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`freshrss_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        freshrss_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`freshrss_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        freshrss_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            freshrss_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "freshrss2.{{ user.domain }}"
              - "freshrss.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`freshrss_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        freshrss_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            freshrss_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'freshrss2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`freshrss_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        freshrss_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
icon: material/docker
hide:
  - tags
tags:
  - pufferpanel
  - gaming
  - servers
---

# PufferPanel

## Overview

[PufferPanel](https://pufferpanel.com/) is an open-source web-based game server management system designed for both small networks and personal use. It supports Minecraft, Source Dedicated Servers, BungeeCord, and many other game servers.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://pufferpanel.com/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/pufferpanel/pufferpanel){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/pufferpanel/pufferpanel){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-pufferpanel
```

### 2. URL

- To access PufferPanel, visit <https://pufferpanel.iYOUR_DOMAIN_NAMEi>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    pufferpanel_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `pufferpanel_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `pufferpanel_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`pufferpanel_name`"

        ```yaml
        # Type: string
        pufferpanel_name: pufferpanel
        ```

=== "Paths"

    ??? variable string "`pufferpanel_role_paths_folder`"

        ```yaml
        # Type: string
        pufferpanel_role_paths_folder: "{{ pufferpanel_name }}"
        ```

    ??? variable string "`pufferpanel_role_paths_location`"

        ```yaml
        # Type: string
        pufferpanel_role_paths_location: "{{ server_appdata_path }}/{{ pufferpanel_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`pufferpanel_role_web_subdomain`"

        ```yaml
        # Type: string
        pufferpanel_role_web_subdomain: "{{ pufferpanel_name }}"
        ```

    ??? variable string "`pufferpanel_role_web_domain`"

        ```yaml
        # Type: string
        pufferpanel_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`pufferpanel_role_web_port`"

        ```yaml
        # Type: string
        pufferpanel_role_web_port: "8080"
        ```

    ??? variable string "`pufferpanel_role_web_url`"

        ```yaml
        # Type: string
        pufferpanel_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='pufferpanel') + '.' + lookup('role_var', '_web_domain', role='pufferpanel')
                                   if (lookup('role_var', '_web_subdomain', role='pufferpanel') | length > 0)
                                   else lookup('role_var', '_web_domain', role='pufferpanel')) }}"
        ```

=== "DNS"

    ??? variable string "`pufferpanel_role_dns_record`"

        ```yaml
        # Type: string
        pufferpanel_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='pufferpanel') }}"
        ```

    ??? variable string "`pufferpanel_role_dns_zone`"

        ```yaml
        # Type: string
        pufferpanel_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='pufferpanel') }}"
        ```

    ??? variable bool "`pufferpanel_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        pufferpanel_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`pufferpanel_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        pufferpanel_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`pufferpanel_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        pufferpanel_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`pufferpanel_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        pufferpanel_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`pufferpanel_role_traefik_certresolver`"

        ```yaml
        # Type: string
        pufferpanel_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`pufferpanel_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        pufferpanel_role_traefik_enabled: true
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`pufferpanel_role_docker_container`"

        ```yaml
        # Type: string
        pufferpanel_role_docker_container: "{{ pufferpanel_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`pufferpanel_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        pufferpanel_role_docker_image_pull: true
        ```

    ??? variable string "`pufferpanel_role_docker_image_repo`"

        ```yaml
        # Type: string
        pufferpanel_role_docker_image_repo: "pufferpanel/pufferpanel"
        ```

    ??? variable string "`pufferpanel_role_docker_image_tag`"

        ```yaml
        # Type: string
        pufferpanel_role_docker_image_tag: "latest"
        ```

    ??? variable string "`pufferpanel_role_docker_image`"

        ```yaml
        # Type: string
        pufferpanel_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='pufferpanel') }}:{{ lookup('role_var', '_docker_image_tag', role='pufferpanel') }}"
        ```

    <h5>Ports</h5>

    ??? variable list "`pufferpanel_role_docker_ports_defaults`"

        ```yaml
        # Type: list
        pufferpanel_role_docker_ports_defaults: 
          - "5657:5657"
        ```

    ??? variable list "`pufferpanel_role_docker_ports_custom`"

        ```yaml
        # Type: list
        pufferpanel_role_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    ??? variable dict "`pufferpanel_role_docker_envs_default`"

        ```yaml
        # Type: dict
        pufferpanel_role_docker_envs_default: 
          TZ: "{{ tz }}"
          GIN_MODE: "release"
        ```

    ??? variable dict "`pufferpanel_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        pufferpanel_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`pufferpanel_role_docker_volumes_default`"

        ```yaml
        # Type: list
        pufferpanel_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='pufferpanel') }}/config:/etc/pufferpanel"
          - "{{ lookup('role_var', '_paths_location', role='pufferpanel') }}/data:/var/lib/pufferpanel"
          - "{{ lookup('role_var', '_paths_location', role='pufferpanel') }}/logs:/var/log/pufferpanel"
          - "/var/run/docker.sock:/var/run/docker.sock"
        ```

    ??? variable list "`pufferpanel_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        pufferpanel_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`pufferpanel_role_docker_hostname`"

        ```yaml
        # Type: string
        pufferpanel_role_docker_hostname: "{{ pufferpanel_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`pufferpanel_role_docker_networks_alias`"

        ```yaml
        # Type: string
        pufferpanel_role_docker_networks_alias: "{{ pufferpanel_name }}"
        ```

    ??? variable list "`pufferpanel_role_docker_networks_default`"

        ```yaml
        # Type: list
        pufferpanel_role_docker_networks_default: []
        ```

    ??? variable list "`pufferpanel_role_docker_networks_custom`"

        ```yaml
        # Type: list
        pufferpanel_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`pufferpanel_role_docker_restart_policy`"

        ```yaml
        # Type: string
        pufferpanel_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`pufferpanel_role_docker_state`"

        ```yaml
        # Type: string
        pufferpanel_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`pufferpanel_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        pufferpanel_role_autoheal_enabled: true
        ```

    ??? variable string "`pufferpanel_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        pufferpanel_role_depends_on: ""
        ```

    ??? variable string "`pufferpanel_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        pufferpanel_role_depends_on_delay: "0"
        ```

    ??? variable string "`pufferpanel_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        pufferpanel_role_depends_on_healthchecks:
        ```

    ??? variable bool "`pufferpanel_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        pufferpanel_role_diun_enabled: true
        ```

    ??? variable bool "`pufferpanel_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        pufferpanel_role_dns_enabled: true
        ```

    ??? variable bool "`pufferpanel_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        pufferpanel_role_docker_controller: true
        ```

    ??? variable bool "`pufferpanel_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        pufferpanel_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`pufferpanel_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        pufferpanel_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`pufferpanel_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        pufferpanel_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`pufferpanel_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        pufferpanel_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`pufferpanel_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        pufferpanel_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`pufferpanel_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        pufferpanel_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`pufferpanel_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        pufferpanel_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`pufferpanel_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        pufferpanel_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`pufferpanel_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        pufferpanel_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`pufferpanel_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        pufferpanel_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            pufferpanel_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "pufferpanel2.{{ user.domain }}"
              - "pufferpanel.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`pufferpanel_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        pufferpanel_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            pufferpanel_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'pufferpanel2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`pufferpanel_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        pufferpanel_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
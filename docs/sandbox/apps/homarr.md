---
icon: material/docker
hide:
  - tags
tags:
  - homarr
  - dashboard
  - homepage
---

# Homarr

## Overview

[Homarr](https://www.homarr.dev/) is a simple and modern homepage for your server that helps you access all of your services in one place. It integrates with the services you use to display useful information or control them. It's easy to install and supports many different devices.

- Integrates with services you use.
- Search the web directly from your homepage.
- Search overseerr directly from your homepage.
- Real-time status indicator for every service.
- Automatically finds icons while you type the name of a service.
- Widgets that can display all types of information.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://homarr.dev/){: .header-icons } | [:octicons-link-16: Docs](https://homarr.dev/docs/getting-started/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/ajnart/homarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/ajnart/homarr/){: .header-icons }|

Recommended install types: Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-homarr

```

### 2. URL

- To access homarr, visit <https://homarr.iYOUR_DOMAIN_NAMEi>

### 3. Setup

- Default login:

  ``` { .yaml}

  Password: your_normal_password

  ```

- [:octicons-link-16: Documentation: Homarr Docs](https://homarr.dev/docs/getting-started/){: .header-icons }

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    homarr_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `homarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `homarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`homarr_name`"

        ```yaml
        # Type: string
        homarr_name: homarr
        ```

=== "Docker Socket Proxy"

    ??? variable dict "`homarr_role_docker_socket_proxy_envs`"

        ```yaml
        # Type: dict
        homarr_role_docker_socket_proxy_envs: 
          CONTAINERS: "1"
          POST: "0"
        ```

=== "Paths"

    ??? variable string "`homarr_role_paths_folder`"

        ```yaml
        # Type: string
        homarr_role_paths_folder: "{{ homarr_name }}"
        ```

    ??? variable string "`homarr_role_paths_location`"

        ```yaml
        # Type: string
        homarr_role_paths_location: "{{ server_appdata_path }}/{{ homarr_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`homarr_role_web_subdomain`"

        ```yaml
        # Type: string
        homarr_role_web_subdomain: "{{ homarr_name }}"
        ```

    ??? variable string "`homarr_role_web_domain`"

        ```yaml
        # Type: string
        homarr_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`homarr_role_web_port`"

        ```yaml
        # Type: string
        homarr_role_web_port: "7575"
        ```

    ??? variable string "`homarr_role_web_url`"

        ```yaml
        # Type: string
        homarr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='homarr') + '.' + lookup('role_var', '_web_domain', role='homarr')
                              if (lookup('role_var', '_web_subdomain', role='homarr') | length > 0)
                              else lookup('role_var', '_web_domain', role='homarr')) }}"
        ```

=== "DNS"

    ??? variable string "`homarr_role_dns_record`"

        ```yaml
        # Type: string
        homarr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='homarr') }}"
        ```

    ??? variable string "`homarr_role_dns_zone`"

        ```yaml
        # Type: string
        homarr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='homarr') }}"
        ```

    ??? variable bool "`homarr_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        homarr_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`homarr_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        homarr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`homarr_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        homarr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`homarr_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        homarr_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`homarr_role_traefik_certresolver`"

        ```yaml
        # Type: string
        homarr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`homarr_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        homarr_role_traefik_enabled: true
        ```

    ??? variable bool "`homarr_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        homarr_role_traefik_api_enabled: false
        ```

    ??? variable string "`homarr_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        homarr_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`homarr_role_docker_container`"

        ```yaml
        # Type: string
        homarr_role_docker_container: "{{ homarr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`homarr_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        homarr_role_docker_image_pull: true
        ```

    ??? variable string "`homarr_role_docker_image_repo`"

        ```yaml
        # Type: string
        homarr_role_docker_image_repo: "ghcr.io/ajnart/homarr"
        ```

    ??? variable string "`homarr_role_docker_image_tag`"

        ```yaml
        # Type: string
        homarr_role_docker_image_tag: "latest"
        ```

    ??? variable string "`homarr_role_docker_image`"

        ```yaml
        # Type: string
        homarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='homarr') }}:{{ lookup('role_var', '_docker_image_tag', role='homarr') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`homarr_role_docker_envs_default`"

        ```yaml
        # Type: dict
        homarr_role_docker_envs_default: 
          TZ: "{{ tz }}"
          BASE_URL: "{{ lookup('role_var', '_web_subdomain', role='homarr') + '.' + lookup('role_var', '_web_domain', role='homarr') }}"
          PASSWORD: "{{ user.pass }}"
          DOCKER_HOST: "tcp://{{ homarr_name }}-docker-socket-proxy:2375"
          NODE_TLS_REJECT_UNAUTHORIZED: "0"
        ```

    ??? variable dict "`homarr_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        homarr_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`homarr_role_docker_volumes_default`"

        ```yaml
        # Type: list
        homarr_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='homarr') }}:/app/data/configs"
          - "{{ lookup('role_var', '_paths_location', role='homarr') }}/icons:/app/public/icons"
        ```

    ??? variable list "`homarr_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        homarr_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`homarr_role_docker_hostname`"

        ```yaml
        # Type: string
        homarr_role_docker_hostname: "{{ homarr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`homarr_role_docker_networks_alias`"

        ```yaml
        # Type: string
        homarr_role_docker_networks_alias: "{{ homarr_name }}"
        ```

    ??? variable list "`homarr_role_docker_networks_default`"

        ```yaml
        # Type: list
        homarr_role_docker_networks_default: []
        ```

    ??? variable list "`homarr_role_docker_networks_custom`"

        ```yaml
        # Type: list
        homarr_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`homarr_role_docker_restart_policy`"

        ```yaml
        # Type: string
        homarr_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`homarr_role_docker_state`"

        ```yaml
        # Type: string
        homarr_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`homarr_role_depends_on`"

        ```yaml
        # Type: string
        homarr_role_depends_on: "{{ homarr_name }}-docker-socket-proxy"
        ```

    ??? variable string "`homarr_role_depends_on_delay`"

        ```yaml
        # Type: string
        homarr_role_depends_on_delay: "0"
        ```

    ??? variable string "`homarr_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        homarr_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`homarr_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        homarr_role_autoheal_enabled: true
        ```

    ??? variable string "`homarr_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        homarr_role_depends_on: ""
        ```

    ??? variable string "`homarr_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        homarr_role_depends_on_delay: "0"
        ```

    ??? variable string "`homarr_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        homarr_role_depends_on_healthchecks:
        ```

    ??? variable bool "`homarr_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        homarr_role_diun_enabled: true
        ```

    ??? variable bool "`homarr_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        homarr_role_dns_enabled: true
        ```

    ??? variable bool "`homarr_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        homarr_role_docker_controller: true
        ```

    ??? variable bool "`homarr_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        homarr_role_docker_volumes_download:
        ```

    ??? variable bool "`homarr_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        homarr_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`homarr_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        homarr_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`homarr_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        homarr_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`homarr_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        homarr_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`homarr_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        homarr_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`homarr_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        homarr_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`homarr_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        homarr_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`homarr_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        homarr_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`homarr_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        homarr_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`homarr_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        homarr_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            homarr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "homarr2.{{ user.domain }}"
              - "homarr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`homarr_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        homarr_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            homarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'homarr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`homarr_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        homarr_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
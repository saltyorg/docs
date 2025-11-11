---
icon: material/docker
hide:
  - tags
tags:
  - VPN
  - server
---

# Wireguard

## Overview

[Wireguard](https://wireguard.com) is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography.

The Wireguard server is deployed using the [WG-Easy](https://github.com/WeeJeWel/wg-easy) image with a simple Web UI for management.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Wireguard](https://www.wireguard.com/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/WeeJeWel/wg-easy){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/wg-easy/wg-easy){: .header-icons } | [:material-docker: Docker:](https://ghcr.io/wg-easy/wg-easy){: .header-icons } |

### 1. Installation

``` shell

sb install sandbox-wireguard

```

### 2. URL

- To access Wireguard, visit <https://wireguard.iYOUR_DOMAIN_NAMEi>

The password provisioned is your Saltbox password.

### 3. Setup

- Use the Web UI to configure your clients.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    wireguard_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `wireguard_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `wireguard_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`wireguard_name`"

        ```yaml
        # Type: string
        wireguard_name: wireguard
        ```

=== "Settings"

    ??? variable string "`wireguard_listen_port`"

        ```yaml
        # Type: string
        wireguard_listen_port: "51820"
        ```

=== "Paths"

    ??? variable string "`wireguard_role_paths_folder`"

        ```yaml
        # Type: string
        wireguard_role_paths_folder: "{{ wireguard_name }}"
        ```

    ??? variable string "`wireguard_role_paths_location`"

        ```yaml
        # Type: string
        wireguard_role_paths_location: "{{ server_appdata_path }}/{{ wireguard_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`wireguard_role_web_subdomain`"

        ```yaml
        # Type: string
        wireguard_role_web_subdomain: "{{ wireguard_name }}"
        ```

    ??? variable string "`wireguard_role_web_domain`"

        ```yaml
        # Type: string
        wireguard_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`wireguard_role_web_port`"

        ```yaml
        # Type: string
        wireguard_role_web_port: "51821"
        ```

    ??? variable string "`wireguard_role_web_url`"

        ```yaml
        # Type: string
        wireguard_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='wireguard') + '.' + lookup('role_var', '_web_domain', role='wireguard')
                                 if (lookup('role_var', '_web_subdomain', role='wireguard') | length > 0)
                                 else lookup('role_var', '_web_domain', role='wireguard')) }}"
        ```

=== "DNS"

    ??? variable string "`wireguard_role_dns_record`"

        ```yaml
        # Type: string
        wireguard_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='wireguard') }}"
        ```

    ??? variable string "`wireguard_role_dns_zone`"

        ```yaml
        # Type: string
        wireguard_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='wireguard') }}"
        ```

    ??? variable bool "`wireguard_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`wireguard_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        wireguard_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`wireguard_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        wireguard_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`wireguard_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        wireguard_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`wireguard_role_traefik_certresolver`"

        ```yaml
        # Type: string
        wireguard_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`wireguard_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_traefik_enabled: true
        ```

    ??? variable bool "`wireguard_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_traefik_api_enabled: false
        ```

    ??? variable string "`wireguard_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        wireguard_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`wireguard_role_docker_container`"

        ```yaml
        # Type: string
        wireguard_role_docker_container: "{{ wireguard_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`wireguard_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_docker_image_pull: true
        ```

    ??? variable string "`wireguard_role_docker_image_repo`"

        ```yaml
        # Type: string
        wireguard_role_docker_image_repo: "ghcr.io/wg-easy/wg-easy"
        ```

    ??? variable string "`wireguard_role_docker_image_tag`"

        ```yaml
        # Type: string
        wireguard_role_docker_image_tag: "14"
        ```

    ??? variable string "`wireguard_role_docker_image`"

        ```yaml
        # Type: string
        wireguard_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='wireguard') }}:{{ lookup('role_var', '_docker_image_tag', role='wireguard') }}"
        ```

    <h5>Ports</h5>

    ??? variable list "`wireguard_role_docker_ports_defaults`"

        ```yaml
        # Type: list
        wireguard_role_docker_ports_defaults: 
          - "{{ wireguard_listen_port }}:51820/udp"
        ```

    ??? variable list "`wireguard_role_docker_ports_custom`"

        ```yaml
        # Type: list
        wireguard_role_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    ??? variable dict "`wireguard_role_docker_envs_default`"

        ```yaml
        # Type: dict
        wireguard_role_docker_envs_default: 
          TZ: "{{ tz }}"
          WG_HOST: "{{ ip_address_public }}"
          PASSWORD_HASH: "{{ user.pass | password_hash('bcrypt') }}"
          WG_PORT: "{{ wireguard_listen_port }}"
        ```

    ??? variable dict "`wireguard_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        wireguard_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`wireguard_role_docker_volumes_default`"

        ```yaml
        # Type: list
        wireguard_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='wireguard') }}:/etc/wireguard"
        ```

    ??? variable list "`wireguard_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        wireguard_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`wireguard_role_docker_hostname`"

        ```yaml
        # Type: string
        wireguard_role_docker_hostname: "{{ wireguard_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`wireguard_role_docker_networks_alias`"

        ```yaml
        # Type: string
        wireguard_role_docker_networks_alias: "{{ wireguard_name }}"
        ```

    ??? variable list "`wireguard_role_docker_networks_default`"

        ```yaml
        # Type: list
        wireguard_role_docker_networks_default: []
        ```

    ??? variable list "`wireguard_role_docker_networks_custom`"

        ```yaml
        # Type: list
        wireguard_role_docker_networks_custom: []
        ```

    <h5>Capabilities</h5>

    ??? variable list "`wireguard_role_docker_capabilities_default`"

        ```yaml
        # Type: list
        wireguard_role_docker_capabilities_default: 
          - NET_ADMIN
          - SYS_MODULE
        ```

    ??? variable list "`wireguard_role_docker_capabilities_custom`"

        ```yaml
        # Type: list
        wireguard_role_docker_capabilities_custom: []
        ```

    <h5>Sysctls</h5>

    ??? variable dict "`wireguard_role_docker_sysctls`"

        ```yaml
        # Type: dict
        wireguard_role_docker_sysctls: 
          net.ipv4.conf.all.src_valid_mark: "1"
          net.ipv4.ip_forward: "1"
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`wireguard_role_docker_restart_policy`"

        ```yaml
        # Type: string
        wireguard_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`wireguard_role_docker_state`"

        ```yaml
        # Type: string
        wireguard_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`wireguard_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        wireguard_role_autoheal_enabled: true
        ```

    ??? variable string "`wireguard_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        wireguard_role_depends_on: ""
        ```

    ??? variable string "`wireguard_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        wireguard_role_depends_on_delay: "0"
        ```

    ??? variable string "`wireguard_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        wireguard_role_depends_on_healthchecks:
        ```

    ??? variable bool "`wireguard_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        wireguard_role_diun_enabled: true
        ```

    ??? variable bool "`wireguard_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        wireguard_role_dns_enabled: true
        ```

    ??? variable bool "`wireguard_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        wireguard_role_docker_controller: true
        ```

    ??? variable bool "`wireguard_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_docker_volumes_download:
        ```

    ??? variable bool "`wireguard_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        wireguard_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`wireguard_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        wireguard_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`wireguard_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        wireguard_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`wireguard_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        wireguard_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`wireguard_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`wireguard_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        wireguard_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`wireguard_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        wireguard_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`wireguard_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        wireguard_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`wireguard_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        wireguard_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`wireguard_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        wireguard_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            wireguard_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "wireguard2.{{ user.domain }}"
              - "wireguard.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`wireguard_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        wireguard_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            wireguard_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'wireguard2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`wireguard_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        wireguard_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
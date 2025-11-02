---
icon: material/docker
hide:
  - tags
tags:
  - transmissionvpn
  - download
  - vpn
---

# OpenVPN and Transmission with WebUI

## Overview

## THIS DOCUMENTATION IS NOT YET COMPLETED

[transmissionvpn](https://transmissionvpn.url) is a...

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://transmissionvpn.url){: .header-icons } | [:octicons-link-16: Docs](https://transmissionvpn.docs.url){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/transmissionvpn/transmissionvpn){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/transmissionvpn/transmissionvpn){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-transmissionvpn

```

### 2. URL

- To access transmissionvpn, visit <https://transmissionvpn.iYOUR_DOMAIN_NAMEi>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    transmissionvpn_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `transmissionvpn_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `transmissionvpn_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`transmissionvpn_name`"

        ```yaml
        # Type: string
        transmissionvpn_name: transmissionvpn
        ```

=== "Settings"

    ??? variable string "`transmissionvpn_create_tun_device`"

        ```yaml
        # Type: string
        transmissionvpn_create_tun_device: "false"
        ```

    ??? variable string "`transmissionvpn_transmission_home`"

        ```yaml
        # Type: string
        transmissionvpn_transmission_home: "/opt/transmissionvpn"
        ```

    ??? variable string "`transmissionvpn_umask_set`"

        ```yaml
        # Type: string
        transmissionvpn_umask_set: "022"
        ```

=== "Paths"

    ??? variable string "`transmissionvpn_role_paths_folder`"

        ```yaml
        # Type: string
        transmissionvpn_role_paths_folder: "{{ transmissionvpn_name }}"
        ```

    ??? variable string "`transmissionvpn_role_paths_location`"

        ```yaml
        # Type: string
        transmissionvpn_role_paths_location: "{{ server_appdata_path }}/{{ transmissionvpn_role_paths_folder }}"
        ```

    ??? variable string "`transmissionvpn_role_paths_downloads_location`"

        ```yaml
        # Type: string
        transmissionvpn_role_paths_downloads_location: "{{ downloads_torrents_path }}/{{ transmissionvpn_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`transmissionvpn_role_web_subdomain`"

        ```yaml
        # Type: string
        transmissionvpn_role_web_subdomain: "{{ transmissionvpn_name }}"
        ```

    ??? variable string "`transmissionvpn_role_web_domain`"

        ```yaml
        # Type: string
        transmissionvpn_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`transmissionvpn_role_web_port`"

        ```yaml
        # Type: string
        transmissionvpn_role_web_port: "9091"
        ```

    ??? variable string "`transmissionvpn_role_web_url`"

        ```yaml
        # Type: string
        transmissionvpn_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='transmissionvpn') + '.' + lookup('role_var', '_web_domain', role='transmissionvpn')
                                       if (lookup('role_var', '_web_subdomain', role='transmissionvpn') | length > 0)
                                       else lookup('role_var', '_web_domain', role='transmissionvpn')) }}"
        ```

=== "DNS"

    ??? variable string "`transmissionvpn_role_dns_record`"

        ```yaml
        # Type: string
        transmissionvpn_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='transmissionvpn') }}"
        ```

    ??? variable string "`transmissionvpn_role_dns_zone`"

        ```yaml
        # Type: string
        transmissionvpn_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='transmissionvpn') }}"
        ```

    ??? variable bool "`transmissionvpn_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        transmissionvpn_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`transmissionvpn_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        transmissionvpn_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`transmissionvpn_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        transmissionvpn_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`transmissionvpn_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        transmissionvpn_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`transmissionvpn_role_traefik_certresolver`"

        ```yaml
        # Type: string
        transmissionvpn_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`transmissionvpn_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        transmissionvpn_role_traefik_enabled: true
        ```

    ??? variable bool "`transmissionvpn_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        transmissionvpn_role_traefik_api_enabled: false
        ```

    ??? variable string "`transmissionvpn_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        transmissionvpn_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`transmissionvpn_role_docker_container`"

        ```yaml
        # Type: string
        transmissionvpn_role_docker_container: "{{ transmissionvpn_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`transmissionvpn_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        transmissionvpn_role_docker_image_pull: true
        ```

    ??? variable string "`transmissionvpn_role_docker_image_repo`"

        ```yaml
        # Type: string
        transmissionvpn_role_docker_image_repo: "haugene/transmission-openvpn"
        ```

    ??? variable string "`transmissionvpn_role_docker_image_tag`"

        ```yaml
        # Type: string
        transmissionvpn_role_docker_image_tag: "latest"
        ```

    ??? variable string "`transmissionvpn_role_docker_image`"

        ```yaml
        # Type: string
        transmissionvpn_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='transmissionvpn') }}:{{ lookup('role_var', '_docker_image_tag', role='transmissionvpn') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`transmissionvpn_role_docker_envs_default`"

        ```yaml
        # Type: dict
        transmissionvpn_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          OPENVPN_PROVIDER: "{{ transmissionvpn.vpn_prov | default('pia', true) }}"
          OPENVPN_USERNAME: "{{ transmissionvpn.vpn_user | default('username', true) }}"
          OPENVPN_PASSWORD: "{{ transmissionvpn.vpn_pass | default('password', true) }}"
          UMASK_SET: "{{ transmissionvpn_umask_set }}"
          CREATE_TUN_DEVICE: "{{ transmissionvpn_create_tun_device }}"
          TRANSMISSION_HOME: "{{ transmissionvpn_transmission_home }}"
        ```

    ??? variable dict "`transmissionvpn_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        transmissionvpn_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`transmissionvpn_role_docker_volumes_default`"

        ```yaml
        # Type: list
        transmissionvpn_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='transmissionvpn') }}:/config"
          - "{{ lookup('role_var', '_paths_location', role='transmissionvpn') }}/data:/opt/transmissionvpn"
          - "{{ server_appdata_path }}/scripts:/scripts"
          - "{{ lookup('role_var', '_paths_location', role='transmissionvpn') }}/vpn:/etc/openvpn/custom"
          - "{{ lookup('role_var', '_paths_downloads_location', role='transmissionvpn') }}:/data"
        ```

    ??? variable list "`transmissionvpn_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        transmissionvpn_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`transmissionvpn_role_docker_hostname`"

        ```yaml
        # Type: string
        transmissionvpn_role_docker_hostname: "{{ transmissionvpn_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`transmissionvpn_role_docker_networks_alias`"

        ```yaml
        # Type: string
        transmissionvpn_role_docker_networks_alias: "{{ transmissionvpn_name }}"
        ```

    ??? variable list "`transmissionvpn_role_docker_networks_default`"

        ```yaml
        # Type: list
        transmissionvpn_role_docker_networks_default: []
        ```

    ??? variable list "`transmissionvpn_role_docker_networks_custom`"

        ```yaml
        # Type: list
        transmissionvpn_role_docker_networks_custom: []
        ```

    <h5>Capabilities</h5>

    ??? variable list "`transmissionvpn_role_docker_capabilities_default`"

        ```yaml
        # Type: list
        transmissionvpn_role_docker_capabilities_default: 
          - NET_ADMIN
        ```

    ??? variable list "`transmissionvpn_role_docker_capabilities_custom`"

        ```yaml
        # Type: list
        transmissionvpn_role_docker_capabilities_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`transmissionvpn_role_docker_restart_policy`"

        ```yaml
        # Type: string
        transmissionvpn_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`transmissionvpn_role_docker_state`"

        ```yaml
        # Type: string
        transmissionvpn_role_docker_state: started
        ```

    <h5>Sysctls</h5>

    ??? variable dict "`transmissionvpn_role_docker_sysctls`"

        ```yaml
        # Type: dict
        transmissionvpn_role_docker_sysctls: 
          net.ipv4.conf.all.src_valid_mark: "1"
        ```

    <h5>Privileged</h5>

    ??? variable bool "`transmissionvpn_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        transmissionvpn_role_docker_privileged: true
        ```

=== "Global Override Options"

    ??? variable bool "`transmissionvpn_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        transmissionvpn_role_autoheal_enabled: true
        ```

    ??? variable string "`transmissionvpn_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        transmissionvpn_role_depends_on: ""
        ```

    ??? variable string "`transmissionvpn_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        transmissionvpn_role_depends_on_delay: "0"
        ```

    ??? variable string "`transmissionvpn_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        transmissionvpn_role_depends_on_healthchecks:
        ```

    ??? variable bool "`transmissionvpn_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        transmissionvpn_role_diun_enabled: true
        ```

    ??? variable bool "`transmissionvpn_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        transmissionvpn_role_dns_enabled: true
        ```

    ??? variable bool "`transmissionvpn_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        transmissionvpn_role_docker_controller: true
        ```

    ??? variable bool "`transmissionvpn_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        transmissionvpn_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`transmissionvpn_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        transmissionvpn_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`transmissionvpn_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        transmissionvpn_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`transmissionvpn_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        transmissionvpn_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`transmissionvpn_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        transmissionvpn_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`transmissionvpn_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        transmissionvpn_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`transmissionvpn_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        transmissionvpn_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`transmissionvpn_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        transmissionvpn_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`transmissionvpn_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        transmissionvpn_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`transmissionvpn_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        transmissionvpn_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            transmissionvpn_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "transmissionvpn2.{{ user.domain }}"
              - "transmissionvpn.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`transmissionvpn_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        transmissionvpn_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            transmissionvpn_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'transmissionvpn2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`transmissionvpn_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        transmissionvpn_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
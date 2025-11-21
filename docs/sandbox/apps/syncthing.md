---
icon: material/docker
hide:
  - tags
tags:
  - syncthing
  - backup
  - sync
---

# Syncthing

## Overview

[Syncthing](https://syncthing.net/) is a continuous file synchronization program. It synchronizes files between two or more computers in real time, safely protected from prying eyes. Your data is your data alone and you deserve to choose where it is stored, whether it is shared with some third party, and how it's transmitted over the internet.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://syncthing.comnet/){: .header-icons } | [:octicons-link-16: Docs](https://docs.syncthing.net/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/syncthing/syncthing){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/syncthing){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-syncthing

```

### 2. URL

- To access the Syncthing dashboard, visit <https://syncthing.iYOUR_DOMAIN_NAMEi>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    syncthing_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `syncthing_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `syncthing_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`syncthing_name`"

        ```yaml
        # Type: string
        syncthing_name: syncthing
        ```

=== "Paths"

    ??? variable string "`syncthing_role_paths_folder`"

        ```yaml
        # Type: string
        syncthing_role_paths_folder: "{{ syncthing_name }}"
        ```

    ??? variable string "`syncthing_role_paths_location`"

        ```yaml
        # Type: string
        syncthing_role_paths_location: "{{ server_appdata_path }}/{{ syncthing_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`syncthing_role_web_subdomain`"

        ```yaml
        # Type: string
        syncthing_role_web_subdomain: "{{ syncthing_name }}"
        ```

    ??? variable string "`syncthing_role_web_domain`"

        ```yaml
        # Type: string
        syncthing_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`syncthing_role_web_port`"

        ```yaml
        # Type: string
        syncthing_role_web_port: "8384"
        ```

    ??? variable string "`syncthing_role_web_url`"

        ```yaml
        # Type: string
        syncthing_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='syncthing') + '.' + lookup('role_var', '_web_domain', role='syncthing')
                                 if (lookup('role_var', '_web_subdomain', role='syncthing') | length > 0)
                                 else lookup('role_var', '_web_domain', role='syncthing')) }}"
        ```

=== "DNS"

    ??? variable string "`syncthing_role_dns_record`"

        ```yaml
        # Type: string
        syncthing_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='syncthing') }}"
        ```

    ??? variable string "`syncthing_role_dns_zone`"

        ```yaml
        # Type: string
        syncthing_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='syncthing') }}"
        ```

    ??? variable bool "`syncthing_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`syncthing_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        syncthing_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`syncthing_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        syncthing_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`syncthing_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        syncthing_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`syncthing_role_traefik_certresolver`"

        ```yaml
        # Type: string
        syncthing_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`syncthing_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_traefik_enabled: true
        ```

    ??? variable bool "`syncthing_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_traefik_api_enabled: false
        ```

    ??? variable string "`syncthing_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        syncthing_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`syncthing_role_docker_container`"

        ```yaml
        # Type: string
        syncthing_role_docker_container: "{{ syncthing_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`syncthing_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_docker_image_pull: true
        ```

    ??? variable string "`syncthing_role_docker_image_repo`"

        ```yaml
        # Type: string
        syncthing_role_docker_image_repo: "lscr.io/linuxserver/syncthing"
        ```

    ??? variable string "`syncthing_role_docker_image_tag`"

        ```yaml
        # Type: string
        syncthing_role_docker_image_tag: "latest"
        ```

    ??? variable string "`syncthing_role_docker_image`"

        ```yaml
        # Type: string
        syncthing_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='syncthing') }}:{{ lookup('role_var', '_docker_image_tag', role='syncthing') }}"
        ```

    <h5>Ports</h5>

    ??? variable list "`syncthing_role_docker_ports_defaults`"

        ```yaml
        # Type: list
        syncthing_role_docker_ports_defaults:
          - "22000:22000/tcp"
          - "22000:22000/udp"
          - "21027:21027/udp"
        ```

    ??? variable list "`syncthing_role_docker_ports_custom`"

        ```yaml
        # Type: list
        syncthing_role_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    ??? variable dict "`syncthing_role_docker_envs_default`"

        ```yaml
        # Type: dict
        syncthing_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`syncthing_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        syncthing_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`syncthing_role_docker_volumes_default`"

        ```yaml
        # Type: list
        syncthing_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='syncthing') }}:/config"
        ```

    ??? variable list "`syncthing_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        syncthing_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`syncthing_role_docker_hostname`"

        ```yaml
        # Type: string
        syncthing_role_docker_hostname: "{{ syncthing_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`syncthing_role_docker_networks_alias`"

        ```yaml
        # Type: string
        syncthing_role_docker_networks_alias: "{{ syncthing_name }}"
        ```

    ??? variable list "`syncthing_role_docker_networks_default`"

        ```yaml
        # Type: list
        syncthing_role_docker_networks_default: []
        ```

    ??? variable list "`syncthing_role_docker_networks_custom`"

        ```yaml
        # Type: list
        syncthing_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`syncthing_role_docker_restart_policy`"

        ```yaml
        # Type: string
        syncthing_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`syncthing_role_docker_state`"

        ```yaml
        # Type: string
        syncthing_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`syncthing_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        syncthing_role_autoheal_enabled: true
        ```

    ??? variable string "`syncthing_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        syncthing_role_depends_on: ""
        ```

    ??? variable string "`syncthing_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        syncthing_role_depends_on_delay: "0"
        ```

    ??? variable string "`syncthing_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        syncthing_role_depends_on_healthchecks:
        ```

    ??? variable bool "`syncthing_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        syncthing_role_diun_enabled: true
        ```

    ??? variable bool "`syncthing_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        syncthing_role_dns_enabled: true
        ```

    ??? variable bool "`syncthing_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        syncthing_role_docker_controller: true
        ```

    ??? variable bool "`syncthing_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_docker_volumes_download:
        ```

    ??? variable bool "`syncthing_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        syncthing_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`syncthing_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        syncthing_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`syncthing_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        syncthing_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`syncthing_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        syncthing_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`syncthing_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`syncthing_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`syncthing_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        syncthing_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`syncthing_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        syncthing_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`syncthing_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        syncthing_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`syncthing_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        syncthing_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            syncthing_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "syncthing2.{{ user.domain }}"
              - "syncthing.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`syncthing_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        syncthing_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            syncthing_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'syncthing2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`syncthing_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        syncthing_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
icon: material/docker
hide:
  - tags
tags:
  - esphome
  - automation
  - iot
---

# ESPHome

## Overview

[ESPHome](https://esphome.io/)  is an open-source firmware framework that simplifies the process of creating custom firmware for popular WiFi-enabled microcontrollers.

ESPHome is typically installed as a Homeassistant add-on, but when using Homeassistant in a container add-ons are disabled.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://esphome.io/){: .header-icons } | [:octicons-link-16: Docs](https://esphome.io/components/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/imagegenius/docker-esphome/){: .header-icons } | [:material-docker: Docker](https://ghcr.io/esphome/esphome){: .header-icons }|

Using a docker image from ImageGenius since adds user permission mapping (as of 6/10/2025)

### 1. Installation

```shell
sb install sandbox-esphome
```

### 2. URL

- To access ESPHome, visit <https://esphome.iYOUR_DOMAIN_NAMEi>

### 3. Usage

<https://esphome.iYOUR_DOMAIN_NAMEi> is where you can go to manage/add devices, create/store .yaml files, and manage secrets. The .yaml files will be stored in `/opt/esphome/`

See the [ESPHome docs](https://esphome.io/components/) and [ESPHome forums](https://community.home-assistant.io/c/esphome/) for .yaml file creation assistance.

If adding ESPHome into your Homeassistant, it should auto-detect any newly created devices.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    esphome_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `esphome_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `esphome_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`esphome_name`"

        ```yaml
        # Type: string
        esphome_name: esphome
        ```

=== "Paths"

    ??? variable string "`esphome_role_paths_folder`"

        ```yaml
        # Type: string
        esphome_role_paths_folder: "{{ esphome_name }}"
        ```

    ??? variable string "`esphome_role_paths_location`"

        ```yaml
        # Type: string
        esphome_role_paths_location: "{{ server_appdata_path }}/{{ esphome_role_paths_folder }}"
        ```

    ??? variable string "`esphome_role_paths_conf`"

        ```yaml
        # Type: string
        esphome_role_paths_conf: "{{ esphome_role_paths_location }}/configuration.yaml"
        ```

=== "Web"

    ??? variable string "`esphome_role_web_subdomain`"

        ```yaml
        # Type: string
        esphome_role_web_subdomain: "{{ esphome_name }}"
        ```

    ??? variable string "`esphome_role_web_domain`"

        ```yaml
        # Type: string
        esphome_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`esphome_role_web_port`"

        ```yaml
        # Type: string
        esphome_role_web_port: "6052"
        ```

    ??? variable string "`esphome_role_web_url`"

        ```yaml
        # Type: string
        esphome_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='esphome') + '.' + lookup('role_var', '_web_domain', role='esphome')
                               if (lookup('role_var', '_web_subdomain', role='esphome') | length > 0)
                               else lookup('role_var', '_web_domain', role='esphome')) }}"
        ```

=== "DNS"

    ??? variable string "`esphome_role_dns_record`"

        ```yaml
        # Type: string
        esphome_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='esphome') }}"
        ```

    ??? variable string "`esphome_role_dns_zone`"

        ```yaml
        # Type: string
        esphome_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='esphome') }}"
        ```

    ??? variable bool "`esphome_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        esphome_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`esphome_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        esphome_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`esphome_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        esphome_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`esphome_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        esphome_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`esphome_role_traefik_certresolver`"

        ```yaml
        # Type: string
        esphome_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`esphome_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        esphome_role_traefik_enabled: true
        ```

    ??? variable bool "`esphome_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        esphome_role_traefik_api_enabled: false
        ```

    ??? variable string "`esphome_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        esphome_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`esphome_role_docker_container`"

        ```yaml
        # Type: string
        esphome_role_docker_container: "{{ esphome_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`esphome_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        esphome_role_docker_image_pull: true
        ```

    ??? variable string "`esphome_role_docker_image_repo`"

        ```yaml
        # Type: string
        esphome_role_docker_image_repo: "ghcr.io/imagegenius/esphome"
        ```

    ??? variable string "`esphome_role_docker_image_tag`"

        ```yaml
        # Type: string
        esphome_role_docker_image_tag: "latest"
        ```

    ??? variable string "`esphome_role_docker_image`"

        ```yaml
        # Type: string
        esphome_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='esphome') }}:{{ lookup('role_var', '_docker_image_tag', role='esphome') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`esphome_role_docker_envs_default`"

        ```yaml
        # Type: dict
        esphome_role_docker_envs_default:
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
        ```

    ??? variable dict "`esphome_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        esphome_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`esphome_role_docker_volumes_default`"

        ```yaml
        # Type: list
        esphome_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='esphome') }}:/config"
          - /etc/localtime:/etc/localtime:ro
        ```

    ??? variable list "`esphome_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        esphome_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`esphome_role_docker_hostname`"

        ```yaml
        # Type: string
        esphome_role_docker_hostname: "{{ esphome_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`esphome_role_docker_networks_alias`"

        ```yaml
        # Type: string
        esphome_role_docker_networks_alias: "{{ esphome_name }}"
        ```

    ??? variable list "`esphome_role_docker_networks_default`"

        ```yaml
        # Type: list
        esphome_role_docker_networks_default: []
        ```

    ??? variable list "`esphome_role_docker_networks_custom`"

        ```yaml
        # Type: list
        esphome_role_docker_networks_custom: []
        ```

    <h5>Network Mode</h5>

    ??? variable string "`esphome_role_docker_network_mode`"

        ```yaml
        # Type: string
        esphome_role_docker_network_mode: "host"
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`esphome_role_docker_restart_policy`"

        ```yaml
        # Type: string
        esphome_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`esphome_role_docker_state`"

        ```yaml
        # Type: string
        esphome_role_docker_state: started
        ```

    <h5>Privileged</h5>

    ??? variable bool "`esphome_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        esphome_role_docker_privileged: true
        ```

=== "Global Override Options"

    ??? variable bool "`esphome_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        esphome_role_autoheal_enabled: true
        ```

    ??? variable string "`esphome_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        esphome_role_depends_on: ""
        ```

    ??? variable string "`esphome_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        esphome_role_depends_on_delay: "0"
        ```

    ??? variable string "`esphome_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        esphome_role_depends_on_healthchecks:
        ```

    ??? variable bool "`esphome_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        esphome_role_diun_enabled: true
        ```

    ??? variable bool "`esphome_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        esphome_role_dns_enabled: true
        ```

    ??? variable bool "`esphome_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        esphome_role_docker_controller: true
        ```

    ??? variable bool "`esphome_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        esphome_role_docker_volumes_download:
        ```

    ??? variable bool "`esphome_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        esphome_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`esphome_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        esphome_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`esphome_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        esphome_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`esphome_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        esphome_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`esphome_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        esphome_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`esphome_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        esphome_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`esphome_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        esphome_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`esphome_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        esphome_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`esphome_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        esphome_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`esphome_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        esphome_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            esphome_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "esphome2.{{ user.domain }}"
              - "esphome.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`esphome_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        esphome_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            esphome_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'esphome2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`esphome_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        esphome_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
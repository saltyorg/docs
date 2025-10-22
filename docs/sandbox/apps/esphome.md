---
hide:
  - tags
tags:
  - esphome
  - automation
  - iot
---

# ESPHome

## What is it?

[ESPHome](https://esphome.io/)  is an open-source firmware framework that simplifies the process of creating custom firmware for popular WiFi-enabled microcontrollers.

ESPHome is typically installed as a Homeassistant add-on, but when using Homeassistant in a container add-ons are disabled.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://esphome.io/){: .header-icons } | [:octicons-link-16: Docs](https://esphome.io/components/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/imagegenius/docker-esphome/){: .header-icons } | [:material-docker: Docker](https://ghcr.io/esphome/esphome){: .header-icons }|

Using a docker image from ImageGenius since adds user permission mapping (as of 6/10/2025)

### 1. Installation

``` shell
sb install sandbox-esphome

```

### 2. URL

- To access ESPHome, visit `https://esphome.xDOMAIN_NAMEx`

### 3. Usage

`https://esphome.xDOMAIN_NAMEx` is where you can go to manage/add devices, create/store .yaml files, and manage secrets. The .yaml files will be stored in `/opt/esphome/`

See the [ESPHome docs](https://esphome.io/components/) and [ESPHome forums](https://community.home-assistant.io/c/esphome/) for .yaml file creation assistance.

If adding ESPHome into your Homeassistant, it should auto-detect any newly created devices.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        esphome_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `esphome_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `esphome_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    esphome_name: esphome

    ```

??? example "Paths"

    ```yaml
    # Type: string
    esphome_role_paths_folder: "{{ esphome_name }}"

    # Type: string
    esphome_role_paths_location: "{{ server_appdata_path }}/{{ esphome_role_paths_folder }}"

    # Type: string
    esphome_role_paths_conf: "{{ esphome_role_paths_location }}/configuration.yaml"

    ```

??? example "Web"

    ```yaml
    # Type: string
    esphome_role_web_subdomain: "{{ esphome_name }}"

    # Type: string
    esphome_role_web_domain: "{{ user.domain }}"

    # Type: string
    esphome_role_web_port: "6052"

    # Type: string
    esphome_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='esphome') + '.' + lookup('role_var', '_web_domain', role='esphome')
                           if (lookup('role_var', '_web_subdomain', role='esphome') | length > 0)
                           else lookup('role_var', '_web_domain', role='esphome')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    esphome_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='esphome') }}"

    # Type: string
    esphome_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='esphome') }}"

    # Type: bool (true/false)
    esphome_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    esphome_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    esphome_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    esphome_role_traefik_middleware_custom: ""

    # Type: string
    esphome_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    esphome_role_traefik_enabled: true

    # Type: bool (true/false)
    esphome_role_traefik_api_enabled: false

    # Type: string
    esphome_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    esphome_role_docker_container: "{{ esphome_name }}"

    # Image
    # Type: bool (true/false)
    esphome_role_docker_image_pull: true

    # Type: string
    esphome_role_docker_image_repo: "ghcr.io/imagegenius/esphome"

    # Type: string
    esphome_role_docker_image_tag: "latest"

    # Type: string
    esphome_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='esphome') }}:{{ lookup('role_var', '_docker_image_tag', role='esphome') }}"

    # Envs
    # Type: dict
    esphome_role_docker_envs_default: 
      TZ: "{{ tz }}"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"

    # Type: dict
    esphome_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    esphome_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='esphome') }}:/config"
      - /etc/localtime:/etc/localtime:ro

    # Type: list
    esphome_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    esphome_role_docker_hostname: "{{ esphome_name }}"

    # Networks
    # Type: string
    esphome_role_docker_networks_alias: "{{ esphome_name }}"

    # Type: list
    esphome_role_docker_networks_default: []

    # Type: list
    esphome_role_docker_networks_custom: []

    # Network Mode
    # Type: string
    esphome_role_docker_network_mode: "host"

    # Restart Policy
    # Type: string
    esphome_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    esphome_role_docker_state: started

    # Privileged
    # Type: bool (true/false)
    esphome_role_docker_privileged: true

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    esphome_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    esphome_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    esphome_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    esphome_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    esphome_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    esphome_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    esphome_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    esphome_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    esphome_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    esphome_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    esphome_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    esphome_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    esphome_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    esphome_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    esphome_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    esphome_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    esphome_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        esphome_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "esphome2.{{ user.domain }}"
          - "esphome.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        esphome_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'esphome2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

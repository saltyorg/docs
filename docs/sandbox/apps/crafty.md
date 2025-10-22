---
hide:
  - tags
tags:
  - crafty
  - minecraft
  - gaming
---

# Crafty Controller

## What is it?

[Crafty Controller](https://craftycontrol.com/) is a cross-platform Minecraft server control panel with web-based interface. It features server scheduling, interactive console, and support for multiple server types including vanilla, modded, and plugin-based servers.

!!! info
    By default, the role is **NOT** protected behind your Authelia/SSO middleware. You will need to configure authentication within the application.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://craftycontrol.com/){: .header-icons } | [:octicons-mark-github-16: GitLab](https://gitlab.com/crafty-controller/crafty-4){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/arcadiatechnology/crafty-4){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-crafty
```

### 2. URL

- To access Crafty Controller, visit `https://crafty.xDOMAIN_NAMEx`

### 3. Setup

Default credentials are generated on first run and stored in `default-creds.txt` in your app data folder.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        crafty_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `crafty_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `crafty_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    crafty_name: crafty

    ```

??? example "Paths"

    ```yaml
    # Type: string
    crafty_role_paths_folder: "{{ crafty_name }}"

    # Type: string
    crafty_role_paths_group: "root"

    # Type: string
    crafty_role_paths_location: "{{ server_appdata_path }}/{{ crafty_role_paths_folder }}"

    # Type: bool (true/false)
    crafty_role_paths_recurse: true

    ```

??? example "Web"

    ```yaml
    # Type: string
    crafty_role_web_subdomain: "{{ crafty_name }}"

    # Type: string
    crafty_role_web_domain: "{{ user.domain }}"

    # Type: string
    crafty_role_web_port: "8443"

    # Type: string
    crafty_role_web_scheme: "https"

    # Type: string
    crafty_role_web_serverstransport: "skipverify@file"

    # Type: string
    crafty_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='crafty') + '.' + lookup('role_var', '_web_domain', role='crafty')
                          if (lookup('role_var', '_web_subdomain', role='crafty') | length > 0)
                          else lookup('role_var', '_web_domain', role='crafty')) }}"

    # Type: string
    crafty_role_dynmap_web_subdomain: "{{ crafty_name }}-map"

    # Type: string
    crafty_role_dynmap_web_domain: "{{ user.domain }}"

    # Type: string
    crafty_role_dynmap_web_port: "8123"

    # Type: string
    crafty_role_dynmap_host: "{{ lookup('role_var', '_dynmap_web_subdomain', role='crafty')
                                 + '.' + lookup('role_var', '_dynmap_web_domain', role='crafty') }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    crafty_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='crafty') }}"

    # Type: string
    crafty_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='crafty') }}"

    # Type: bool (true/false)
    crafty_role_dns_proxy: "{{ dns_proxied }}"

    # Type: string
    crafty_role_dynmap_dns_record: "{{ lookup('role_var', '_dynmap_web_subdomain', role='crafty') }}"

    # Type: string
    crafty_role_dynmap_dns_zone: "{{ lookup('role_var', '_web_domain', role='crafty') }}"

    # Type: bool (true/false)
    crafty_role_dynmap_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    crafty_role_traefik_sso_middleware: ""

    # Type: string
    crafty_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    crafty_role_traefik_middleware_custom: ""

    # Type: string
    crafty_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    crafty_role_traefik_enabled: true

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    crafty_role_docker_container: "{{ crafty_name }}"

    # Image
    # Type: bool (true/false)
    crafty_role_docker_image_pull: true

    # Type: string
    crafty_role_docker_image_repo: "arcadiatechnology/crafty-4"

    # Type: string
    crafty_role_docker_image_tag: "latest"

    # Type: string
    crafty_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='crafty') }}:{{ lookup('role_var', '_docker_image_tag', role='crafty') }}"

    # Ports
    # Type: list
    crafty_role_docker_ports_defaults: 
      - "19132:19132/udp"
      - "25500-25600:25500-25600"

    # Type: list
    crafty_role_docker_ports_custom: []

    # Envs
    # Type: dict
    crafty_role_docker_envs_default: 
      TZ: "{{ tz }}"

    # Type: dict
    crafty_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    crafty_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='crafty') }}/backups:/crafty/backups"
      - "{{ lookup('role_var', '_paths_location', role='crafty') }}/logs:/crafty/logs"
      - "{{ lookup('role_var', '_paths_location', role='crafty') }}/servers:/crafty/servers"
      - "{{ lookup('role_var', '_paths_location', role='crafty') }}/config:/crafty/app/config"
      - "{{ lookup('role_var', '_paths_location', role='crafty') }}/import:/crafty/import"

    # Type: list
    crafty_role_docker_volumes_custom: []

    # Labels
    # Type: list
    crafty_role_docker_labels_default: 
      - '{ "traefik.http.routers.{{ crafty_name }}-map-http.entrypoints": "web" }'
      - '{ "traefik.http.routers.{{ crafty_name }}-map-http.service": "{{ crafty_name }}-map" }'
      - '{ "traefik.http.routers.{{ crafty_name }}-map-http.rule": "Host(`{{ lookup("role_var", "_dynmap_host", role="crafty") }}`)" }'
      - '{ "traefik.http.routers.{{ crafty_name }}-map-http.middlewares": "{{ traefik_default_middleware_http }}" }'
      - '{ "traefik.http.routers.{{ crafty_name }}-map-http.priority": "20" }'
      - '{ "traefik.http.routers.{{ crafty_name }}-map.entrypoints": "websecure" }'
      - '{ "traefik.http.routers.{{ crafty_name }}-map.service": "{{ crafty_name }}-map" }'
      - '{ "traefik.http.routers.{{ crafty_name }}-map.rule": "Host(`{{ lookup("role_var", "_dynmap_host", role="crafty") }}`)" }'
      - '{ "traefik.http.routers.{{ crafty_name }}-map.tls.options": "securetls@file" }'
      - '{ "traefik.http.routers.{{ crafty_name }}-map.tls.certresolver": "{{ lookup("role_var", "_traefik_certresolver", role="crafty") }}" }'
      - '{ "traefik.http.routers.{{ crafty_name }}-map.middlewares": "{{ traefik_default_middleware }}" }'
      - '{ "traefik.http.routers.{{ crafty_name }}-map.priority": "20" }'
      - '{ "traefik.http.services.{{ crafty_name }}-map.loadbalancer.server.port": "{{ lookup("role_var", "_dynmap_web_port", role="crafty") }}" }'

    # Type: dict
    crafty_role_docker_labels_custom: {}

    # Hostname
    # Type: string
    crafty_role_docker_hostname: "{{ crafty_name }}"

    # Networks
    # Type: string
    crafty_role_docker_networks_alias: "{{ crafty_name }}"

    # Type: list
    crafty_role_docker_networks_default: []

    # Type: list
    crafty_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    crafty_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    crafty_role_docker_state: started

    # Stop Timeout
    # Type: int
    crafty_role_docker_stop_timeout: 900

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    crafty_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    crafty_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    crafty_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    crafty_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    crafty_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    crafty_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    crafty_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    crafty_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    crafty_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    crafty_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    crafty_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    crafty_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    crafty_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    crafty_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    crafty_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    crafty_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    crafty_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        crafty_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "crafty2.{{ user.domain }}"
          - "crafty.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        crafty_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'crafty2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

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

- To access Crafty Controller, visit `https://crafty._yourdomain.com_`

### 3. Setup

Default credentials are generated on first run and stored in `default-creds.txt` in your app data folder.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

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

=== "Basics"

    ??? variable string "`crafty_name`"

        ```yaml
        # Type: string
        crafty_name: crafty
        ```

=== "Paths"

    ??? variable string "`crafty_role_paths_folder`"

        ```yaml
        # Type: string
        crafty_role_paths_folder: "{{ crafty_name }}"
        ```

    ??? variable string "`crafty_role_paths_group`"

        ```yaml
        # Type: string
        crafty_role_paths_group: "root"
        ```

    ??? variable string "`crafty_role_paths_location`"

        ```yaml
        # Type: string
        crafty_role_paths_location: "{{ server_appdata_path }}/{{ crafty_role_paths_folder }}"
        ```

    ??? variable bool "`crafty_role_paths_recurse`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_paths_recurse: true
        ```

=== "Web"

    ??? variable string "`crafty_role_web_subdomain`"

        ```yaml
        # Type: string
        crafty_role_web_subdomain: "{{ crafty_name }}"
        ```

    ??? variable string "`crafty_role_web_domain`"

        ```yaml
        # Type: string
        crafty_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`crafty_role_web_port`"

        ```yaml
        # Type: string
        crafty_role_web_port: "8443"
        ```

    ??? variable string "`crafty_role_web_scheme`"

        ```yaml
        # Type: string
        crafty_role_web_scheme: "https"
        ```

    ??? variable string "`crafty_role_web_serverstransport`"

        ```yaml
        # Type: string
        crafty_role_web_serverstransport: "skipverify@file"
        ```

    ??? variable string "`crafty_role_web_url`"

        ```yaml
        # Type: string
        crafty_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='crafty') + '.' + lookup('role_var', '_web_domain', role='crafty')
                              if (lookup('role_var', '_web_subdomain', role='crafty') | length > 0)
                              else lookup('role_var', '_web_domain', role='crafty')) }}"
        ```

    ??? variable string "`crafty_role_dynmap_web_subdomain`"

        ```yaml
        # Type: string
        crafty_role_dynmap_web_subdomain: "{{ crafty_name }}-map"
        ```

    ??? variable string "`crafty_role_dynmap_web_domain`"

        ```yaml
        # Type: string
        crafty_role_dynmap_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`crafty_role_dynmap_web_port`"

        ```yaml
        # Type: string
        crafty_role_dynmap_web_port: "8123"
        ```

    ??? variable string "`crafty_role_dynmap_host`"

        ```yaml
        # Type: string
        crafty_role_dynmap_host: "{{ lookup('role_var', '_dynmap_web_subdomain', role='crafty')
                                     + '.' + lookup('role_var', '_dynmap_web_domain', role='crafty') }}"
        ```

=== "DNS"

    ??? variable string "`crafty_role_dns_record`"

        ```yaml
        # Type: string
        crafty_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='crafty') }}"
        ```

    ??? variable string "`crafty_role_dns_zone`"

        ```yaml
        # Type: string
        crafty_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='crafty') }}"
        ```

    ??? variable bool "`crafty_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_dns_proxy: "{{ dns_proxied }}"
        ```

    ??? variable string "`crafty_role_dynmap_dns_record`"

        ```yaml
        # Type: string
        crafty_role_dynmap_dns_record: "{{ lookup('role_var', '_dynmap_web_subdomain', role='crafty') }}"
        ```

    ??? variable string "`crafty_role_dynmap_dns_zone`"

        ```yaml
        # Type: string
        crafty_role_dynmap_dns_zone: "{{ lookup('role_var', '_web_domain', role='crafty') }}"
        ```

    ??? variable bool "`crafty_role_dynmap_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_dynmap_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`crafty_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        crafty_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`crafty_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        crafty_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`crafty_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        crafty_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`crafty_role_traefik_certresolver`"

        ```yaml
        # Type: string
        crafty_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`crafty_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_traefik_enabled: true
        ```

=== "Docker"

    ##### Container

    ??? variable string "`crafty_role_docker_container`"

        ```yaml
        # Type: string
        crafty_role_docker_container: "{{ crafty_name }}"
        ```

    ##### Image

    ??? variable bool "`crafty_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_docker_image_pull: true
        ```

    ??? variable string "`crafty_role_docker_image_repo`"

        ```yaml
        # Type: string
        crafty_role_docker_image_repo: "arcadiatechnology/crafty-4"
        ```

    ??? variable string "`crafty_role_docker_image_tag`"

        ```yaml
        # Type: string
        crafty_role_docker_image_tag: "latest"
        ```

    ??? variable string "`crafty_role_docker_image`"

        ```yaml
        # Type: string
        crafty_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='crafty') }}:{{ lookup('role_var', '_docker_image_tag', role='crafty') }}"
        ```

    ##### Ports

    ??? variable list "`crafty_role_docker_ports_defaults`"

        ```yaml
        # Type: list
        crafty_role_docker_ports_defaults: 
          - "19132:19132/udp"
          - "25500-25600:25500-25600"
        ```

    ??? variable list "`crafty_role_docker_ports_custom`"

        ```yaml
        # Type: list
        crafty_role_docker_ports_custom: []
        ```

    ##### Envs

    ??? variable dict "`crafty_role_docker_envs_default`"

        ```yaml
        # Type: dict
        crafty_role_docker_envs_default: 
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`crafty_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        crafty_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`crafty_role_docker_volumes_default`"

        ```yaml
        # Type: list
        crafty_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='crafty') }}/backups:/crafty/backups"
          - "{{ lookup('role_var', '_paths_location', role='crafty') }}/logs:/crafty/logs"
          - "{{ lookup('role_var', '_paths_location', role='crafty') }}/servers:/crafty/servers"
          - "{{ lookup('role_var', '_paths_location', role='crafty') }}/config:/crafty/app/config"
          - "{{ lookup('role_var', '_paths_location', role='crafty') }}/import:/crafty/import"
        ```

    ??? variable list "`crafty_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        crafty_role_docker_volumes_custom: []
        ```

    ##### Labels

    ??? variable list "`crafty_role_docker_labels_default`"

        ```yaml
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
        ```

    ??? variable dict "`crafty_role_docker_labels_custom`"

        ```yaml
        # Type: dict
        crafty_role_docker_labels_custom: {}
        ```

    ##### Hostname

    ??? variable string "`crafty_role_docker_hostname`"

        ```yaml
        # Type: string
        crafty_role_docker_hostname: "{{ crafty_name }}"
        ```

    ##### Networks

    ??? variable string "`crafty_role_docker_networks_alias`"

        ```yaml
        # Type: string
        crafty_role_docker_networks_alias: "{{ crafty_name }}"
        ```

    ??? variable list "`crafty_role_docker_networks_default`"

        ```yaml
        # Type: list
        crafty_role_docker_networks_default: []
        ```

    ??? variable list "`crafty_role_docker_networks_custom`"

        ```yaml
        # Type: list
        crafty_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`crafty_role_docker_restart_policy`"

        ```yaml
        # Type: string
        crafty_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`crafty_role_docker_state`"

        ```yaml
        # Type: string
        crafty_role_docker_state: started
        ```

    ##### Stop Timeout

    ??? variable int "`crafty_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        crafty_role_docker_stop_timeout: 900
        ```

=== "Global Override Options"

    ??? variable bool "`crafty_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        crafty_role_autoheal_enabled: true
        ```

    ??? variable string "`crafty_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        crafty_role_depends_on: ""
        ```

    ??? variable string "`crafty_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        crafty_role_depends_on_delay: "0"
        ```

    ??? variable string "`crafty_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        crafty_role_depends_on_healthchecks:
        ```

    ??? variable bool "`crafty_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        crafty_role_diun_enabled: true
        ```

    ??? variable bool "`crafty_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        crafty_role_dns_enabled: true
        ```

    ??? variable bool "`crafty_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        crafty_role_docker_controller: true
        ```

    ??? variable bool "`crafty_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        crafty_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`crafty_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        crafty_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`crafty_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        crafty_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`crafty_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        crafty_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`crafty_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        crafty_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`crafty_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        crafty_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`crafty_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        crafty_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`crafty_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        crafty_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            crafty_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "crafty2.{{ user.domain }}"
              - "crafty.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`crafty_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        crafty_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            crafty_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'crafty2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`crafty_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        crafty_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
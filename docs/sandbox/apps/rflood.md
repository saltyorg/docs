---
hide:
  - tags
tags:
  - rflood
  - torrent
  - frontend
---

# rFlood

## What is it?

[rFlood](https://github.com/jesec/flood) docker image with rTorrent and the Flood UI, also optional WireGuard VPN support.

## Project Information

- [:material-home: rFlood](https://github.com/jesec/flood){: .header-icons }
- [:octicons-link-16: Docs](https://github.com/jesec/flood/wiki){: .header-icons }
- [:octicons-mark-github-16: Github rTorrent:](https://github.com/jesec/rtorrent){: .header-icons }
- [:octicons-mark-github-16: Github Flood:](https://github.com/jesec/flood){: .header-icons }
- [:material-docker: Docker:](https://hub.docker.com/r/hotio/rflood){: .header-icons }

### 1. Installation

``` shell

sb install sandbox-rflood

```

### 2. URL

- To access rFlood, visit `https://rflood.xDOMAIN_NAMEx`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `rflood_instances`.

    === "Role-level Override"

        Applies to all instances of rflood:

        ```yaml
        rflood_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `rflood2`):

        ```yaml
        rflood2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `rflood_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `rflood_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        rflood_instances: ["rflood"]

        ```

    === "Example"

        ```yaml
        # Type: list
        rflood_instances: ["rflood", "rflood2"]

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        rflood_role_paths_folder: "{{ rflood_name }}"

        # Type: string
        rflood_role_paths_location: "{{ server_appdata_path }}/{{ rflood_role_paths_folder }}"

        # Type: string
        rflood_role_paths_downloads_location: "{{ downloads_torrents_path }}/{{ rflood_role_paths_folder }}"

        # Config files
        # Type: string
        rflood_role_paths_rtorrent_rc_location: "{{ rflood_role_paths_location }}/rtorrent.rc"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        rflood2_paths_folder: "{{ rflood_name }}"

        # Type: string
        rflood2_paths_location: "{{ server_appdata_path }}/{{ rflood_role_paths_folder }}"

        # Type: string
        rflood2_paths_downloads_location: "{{ downloads_torrents_path }}/{{ rflood_role_paths_folder }}"

        # Config files
        # Type: string
        rflood2_paths_rtorrent_rc_location: "{{ rflood_role_paths_location }}/rtorrent.rc"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        rflood_role_web_subdomain: "{{ rflood_name }}"

        # Type: string
        rflood_role_web_domain: "{{ user.domain }}"

        # Type: string
        rflood_role_web_port: "3000"

        # Type: string
        rflood_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='rflood') + '.' + lookup('role_var', '_web_domain', role='rflood')
                              if (lookup('role_var', '_web_subdomain', role='rflood') | length > 0)
                              else lookup('role_var', '_web_domain', role='rflood')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        rflood2_web_subdomain: "{{ rflood_name }}"

        # Type: string
        rflood2_web_domain: "{{ user.domain }}"

        # Type: string
        rflood2_web_port: "3000"

        # Type: string
        rflood2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='rflood') + '.' + lookup('role_var', '_web_domain', role='rflood')
                          if (lookup('role_var', '_web_subdomain', role='rflood') | length > 0)
                          else lookup('role_var', '_web_domain', role='rflood')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        rflood_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='rflood') }}"

        # Type: string
        rflood_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='rflood') }}"

        # Type: bool (true/false)
        rflood_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        rflood2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='rflood') }}"

        # Type: string
        rflood2_dns_zone: "{{ lookup('role_var', '_web_domain', role='rflood') }}"

        # Type: bool (true/false)
        rflood2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        rflood_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        rflood_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        rflood_role_traefik_middleware_custom: ""

        # Type: string
        rflood_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        rflood_role_traefik_enabled: true

        # Disabled for security reasons, no authentication on API /!\
        # Type: bool (true/false)
        rflood_role_traefik_api_enabled: false

        # Type: string
        rflood_role_traefik_api_endpoint: "PathPrefix(`/api`)"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        rflood2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        rflood2_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        rflood2_traefik_middleware_custom: ""

        # Type: string
        rflood2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        rflood2_traefik_enabled: true

        # Disabled for security reasons, no authentication on API /!\
        # Type: bool (true/false)
        rflood2_traefik_api_enabled: false

        # Type: string
        rflood2_traefik_api_endpoint: "PathPrefix(`/api`)"

        ```

??? example "Config"

    === "Role-level"

        ```yaml
        # Type: bool (true/false)
        rflood_role_config_public_trackers: false

        # Type: list
        rflood_role_config_rflood_rc_settings_default: 
          # IP address that is reported to the tracker
          - { option: "network.local_address.set", value: "{{ ip_address_public }}" }
          # Ports
          - { option: "network.port_range.set", value: "{{ lookup('role_var', '_docker_ports_50000', role='rflood') }}-{{ lookup('role_var', '_docker_ports_50000', role='rflood') }}" }
          - { option: "dht.port.set", value: "{{ lookup('role_var', '_docker_ports_6881', role='rflood') }}" }
          # Enable / Disable Public Trackers
          - { option: "dht.mode.set", value: "{{ lookup('role_var', '_config_public_trackers', role='rflood') | ternary('on', 'disable') }}" }
          - { option: "trackers.use_udp.set", value: "{{ lookup('role_var', '_config_public_trackers', role='rflood') | ternary('yes', 'no') }}" }
          - { option: "protocol.pex.set", value: "{{ lookup('role_var', '_config_public_trackers', role='rflood') | ternary('yes', 'no') }}" }
          # Maximum XMLRPC payloads
          - { option: "network.xmlrpc.size_limit.set", value: "20M" }

        # Type: list
        rflood_role_config_rflood_rc_settings_custom: []

        # Type: string
        rflood_role_config_rflood_rc_settings_list: "{{ lookup('role_var', '_config_rflood_rc_settings_default', role='rflood')
                                                        + lookup('role_var', '_config_rflood_rc_settings_custom', role='rflood') }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: bool (true/false)
        rflood2_config_public_trackers: false

        # Type: list
        rflood2_config_rflood_rc_settings_default: 
          # IP address that is reported to the tracker
          - { option: "network.local_address.set", value: "{{ ip_address_public }}" }
          # Ports
          - { option: "network.port_range.set", value: "{{ lookup('role_var', '_docker_ports_50000', role='rflood') }}-{{ lookup('role_var', '_docker_ports_50000', role='rflood') }}" }
          - { option: "dht.port.set", value: "{{ lookup('role_var', '_docker_ports_6881', role='rflood') }}" }
          # Enable / Disable Public Trackers
          - { option: "dht.mode.set", value: "{{ lookup('role_var', '_config_public_trackers', role='rflood') | ternary('on', 'disable') }}" }
          - { option: "trackers.use_udp.set", value: "{{ lookup('role_var', '_config_public_trackers', role='rflood') | ternary('yes', 'no') }}" }
          - { option: "protocol.pex.set", value: "{{ lookup('role_var', '_config_public_trackers', role='rflood') | ternary('yes', 'no') }}" }
          # Maximum XMLRPC payloads
          - { option: "network.xmlrpc.size_limit.set", value: "20M" }

        # Type: list
        rflood2_config_rflood_rc_settings_custom: []

        # Type: string
        rflood2_config_rflood_rc_settings_list: "{{ lookup('role_var', '_config_rflood_rc_settings_default', role='rflood')
                                                    + lookup('role_var', '_config_rflood_rc_settings_custom', role='rflood') }}"

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        rflood_role_docker_container: "{{ rflood_name }}"

        # Image
        # Type: bool (true/false)
        rflood_role_docker_image_pull: true

        # Type: string
        rflood_role_docker_image_repo: "ghcr.io/hotio/rflood"

        # Type: string
        rflood_role_docker_image_tag: "release"

        # Type: string
        rflood_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='rflood') }}:{{ lookup('role_var', '_docker_image_tag', role='rflood') }}"

        # Ports
        # - Internal and External ports need to match for the next set of ports
        # - Lookup available ports and set docker ports accordingly
        # Type: string
        rflood_role_docker_ports_50000: "{{ port_lookup_50000.meta.port
                                         if (port_lookup_50000.meta.port is defined) and (port_lookup_50000.meta.port | trim | length > 0)
                                         else '50000' }}"

        # Type: string
        rflood_role_docker_ports_6881: "{{ port_lookup_6881.meta.port
                                        if (port_lookup_6881.meta.port is defined) and (port_lookup_6881.meta.port | trim | length > 0)
                                        else '6881' }}"

        # Type: list
        rflood_role_docker_ports_defaults: 
          - "{{ lookup('role_var', '_docker_ports_50000', role='rflood') }}:{{ lookup('role_var', '_docker_ports_50000', role='rflood') }}"
          - "{{ lookup('role_var', '_docker_ports_6881', role='rflood') }}:{{ lookup('role_var', '_docker_ports_6881', role='rflood') }}/udp"

        # Type: list
        rflood_role_docker_ports_custom: []

        # Envs
        # Type: dict
        rflood_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          UMASK: "002"
          FLOOD_AUTH: "false"

        # Type: dict
        rflood_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        rflood_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='rflood') }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"

        # Type: list
        rflood_role_docker_volumes_custom: []

        # Hostname
        # Type: string
        rflood_role_docker_hostname: "{{ rflood_name }}"

        # Networks
        # Type: string
        rflood_role_docker_networks_alias: "{{ rflood_name }}"

        # Type: list
        rflood_role_docker_networks_default: []

        # Type: list
        rflood_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        rflood_role_docker_restart_policy: unless-stopped

        # Stop Timeout
        # Type: int
        rflood_role_docker_stop_timeout: 900

        # State
        # Type: string
        rflood_role_docker_state: started

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        rflood2_docker_container: "{{ rflood_name }}"

        # Image
        # Type: bool (true/false)
        rflood2_docker_image_pull: true

        # Type: string
        rflood2_docker_image_repo: "ghcr.io/hotio/rflood"

        # Type: string
        rflood2_docker_image_tag: "release"

        # Type: string
        rflood2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='rflood') }}:{{ lookup('role_var', '_docker_image_tag', role='rflood') }}"

        # Ports
        # - Internal and External ports need to match for the next set of ports
        # - Lookup available ports and set docker ports accordingly
        # Type: string
        rflood2_docker_ports_50000: "{{ port_lookup_50000.meta.port
                                     if (port_lookup_50000.meta.port is defined) and (port_lookup_50000.meta.port | trim | length > 0)
                                     else '50000' }}"

        # Type: string
        rflood2_docker_ports_6881: "{{ port_lookup_6881.meta.port
                                    if (port_lookup_6881.meta.port is defined) and (port_lookup_6881.meta.port | trim | length > 0)
                                    else '6881' }}"

        # Type: list
        rflood2_docker_ports_defaults: 
          - "{{ lookup('role_var', '_docker_ports_50000', role='rflood') }}:{{ lookup('role_var', '_docker_ports_50000', role='rflood') }}"
          - "{{ lookup('role_var', '_docker_ports_6881', role='rflood') }}:{{ lookup('role_var', '_docker_ports_6881', role='rflood') }}/udp"

        # Type: list
        rflood2_docker_ports_custom: []

        # Envs
        # Type: dict
        rflood2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          UMASK: "002"
          FLOOD_AUTH: "false"

        # Type: dict
        rflood2_docker_envs_custom: {}

        # Volumes
        # Type: list
        rflood2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='rflood') }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"

        # Type: list
        rflood2_docker_volumes_custom: []

        # Hostname
        # Type: string
        rflood2_docker_hostname: "{{ rflood_name }}"

        # Networks
        # Type: string
        rflood2_docker_networks_alias: "{{ rflood_name }}"

        # Type: list
        rflood2_docker_networks_default: []

        # Type: list
        rflood2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        rflood2_docker_restart_policy: unless-stopped

        # Stop Timeout
        # Type: int
        rflood2_docker_stop_timeout: 900

        # State
        # Type: string
        rflood2_docker_state: started


        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        rflood_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        rflood_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        rflood_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        rflood_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        rflood_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        rflood_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        rflood_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        rflood_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        rflood_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        rflood_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        rflood_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        rflood_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        rflood_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        rflood_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        rflood_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        rflood_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        rflood_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            rflood_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "rflood2.{{ user.domain }}"
              - "rflood.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            rflood_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'rflood2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `rflood2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        rflood2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        rflood2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        rflood2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        rflood2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        rflood2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        rflood2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        rflood2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        rflood2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        rflood2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        rflood2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        rflood2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        rflood2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        rflood2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        rflood2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        rflood2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        rflood2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        rflood2_web_scheme:

        ```

        1.  Example:

            ```yaml
            rflood2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "rflood2.{{ user.domain }}"
              - "rflood.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            rflood2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'rflood2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

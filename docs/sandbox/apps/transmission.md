---
hide:
  - tags
tags:
  - transmission
  - download
  - torrent
---

# Transmission

## What is it?

[Transmission](https://transmissionbt.com/) is a fast, easy, and free BitTorrent client.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://transmissionbt.com/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/transmission/transmission/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/transmission/transmission){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/transmission){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-transmission

```

### 2. URL

- To access Transmission, visit `https://transmission._yourdomain.com_`

### 3. Setup

- Suggested desktop client is [Transmission Remote GUI](https://github.com/transmission-remote-gui/transgui). It is to be set up with ssl enabled on port 443

- `/watch` is hard-coded in the software and not editable from the settings.json, see related issue. To get around this the folder is mounted to `/mnt/local/downloads/torrents/transmission{{ rolename }}/watch`

- Do not change the published ports if you want to be connectable.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `transmission_instances`.

    === "Role-level Override"

        Applies to all instances of transmission:

        ```yaml
        transmission_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `transmission2`):

        ```yaml
        transmission2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        transmission_instances: ["transmission"]

        ```

    === "Example"

        ```yaml
        # Type: list
        transmission_instances: ["transmission", "transmission2"]

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        transmission_role_paths_folder: "{{ transmission_name }}"

        # Type: string
        transmission_role_paths_location: "{{ server_appdata_path }}/{{ transmission_role_paths_folder }}"

        # Type: string
        transmission_role_paths_downloads_location: "{{ downloads_torrents_path }}/{{ transmission_role_paths_folder }}"

        # Type: string
        transmission_role_paths_setttings_location: "{{ transmission_role_paths_location }}/settings.json"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        transmission2_paths_folder: "{{ transmission_name }}"

        # Type: string
        transmission2_paths_location: "{{ server_appdata_path }}/{{ transmission_role_paths_folder }}"

        # Type: string
        transmission2_paths_downloads_location: "{{ downloads_torrents_path }}/{{ transmission_role_paths_folder }}"

        # Type: string
        transmission2_paths_setttings_location: "{{ transmission_role_paths_location }}/settings.json"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        transmission_role_web_subdomain: "{{ transmission_name }}"

        # Type: string
        transmission_role_web_domain: "{{ user.domain }}"

        # Type: string
        transmission_role_web_port: "9091"

        # Type: string
        transmission_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='transmission') + '.' + lookup('role_var', '_web_domain', role='transmission')
                                    if (lookup('role_var', '_web_subdomain', role='transmission') | length > 0)
                                    else lookup('role_var', '_web_domain', role='transmission')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        transmission2_web_subdomain: "{{ transmission_name }}"

        # Type: string
        transmission2_web_domain: "{{ user.domain }}"

        # Type: string
        transmission2_web_port: "9091"

        # Type: string
        transmission2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='transmission') + '.' + lookup('role_var', '_web_domain', role='transmission')
                                if (lookup('role_var', '_web_subdomain', role='transmission') | length > 0)
                                else lookup('role_var', '_web_domain', role='transmission')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        transmission_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='transmission') }}"

        # Type: string
        transmission_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='transmission') }}"

        # Type: bool (true/false)
        transmission_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        transmission2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='transmission') }}"

        # Type: string
        transmission2_dns_zone: "{{ lookup('role_var', '_web_domain', role='transmission') }}"

        # Type: bool (true/false)
        transmission2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        transmission_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        transmission_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        transmission_role_traefik_middleware_custom: ""

        # Type: string
        transmission_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        transmission_role_traefik_enabled: true

        # Type: bool (true/false)
        transmission_role_traefik_api_enabled: true

        # Type: string
        transmission_role_traefik_api_endpoint: "PathPrefix(`/rpc`)"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        transmission2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        transmission2_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        transmission2_traefik_middleware_custom: ""

        # Type: string
        transmission2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        transmission2_traefik_enabled: true

        # Type: bool (true/false)
        transmission2_traefik_api_enabled: true

        # Type: string
        transmission2_traefik_api_endpoint: "PathPrefix(`/rpc`)"

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        transmission_role_docker_container: "{{ transmission_name }}"

        # Image
        # Type: bool (true/false)
        transmission_role_docker_image_pull: true

        # Type: string
        transmission_role_docker_image_repo: "lscr.io/linuxserver/transmission"

        # Type: string
        transmission_role_docker_image_tag: "latest"

        # Type: string
        transmission_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='transmission') }}:{{ lookup('role_var', '_docker_image_tag', role='transmission') }}"

        # Ports
        # - Internal and External ports need to match for the next set of ports
        # - Lookup available ports and set docker ports accordingly
        # Type: string
        transmission_role_docker_ports_51413: "{{ port_lookup_51413.meta.port
                                               if (port_lookup_51413.meta.port is defined) and (port_lookup_51413.meta.port | trim | length > 0)
                                               else '51413' }}"

        # Type: list
        transmission_role_docker_ports_defaults: 
          - "{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}:{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}"
          - "{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}:{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}/udp"

        # Type: list
        transmission_role_docker_ports_custom: []

        # Envs
        # Type: dict
        transmission_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          UMASK: "002"
          USER: "{{ user.name }}"
          PASS: "{{ user.pass }}"

        # Type: dict
        transmission_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        transmission_role_docker_volumes_default: 
          - "{{ transmission_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
          - "{{ transmission_role_paths_downloads_location }}/watched:/watch"

        # Type: list
        transmission_role_docker_volumes_custom: []

        # Hostname
        # Type: string
        transmission_role_docker_hostname: "{{ transmission_name }}"

        # Networks
        # Type: string
        transmission_role_docker_networks_alias: "{{ transmission_name }}"

        # Type: list
        transmission_role_docker_networks_default: []

        # Type: list
        transmission_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        transmission_role_docker_restart_policy: unless-stopped

        # Stop Timeout
        # Type: int
        transmission_role_docker_stop_timeout: 900

        # State
        # Type: string
        transmission_role_docker_state: started

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        transmission2_docker_container: "{{ transmission_name }}"

        # Image
        # Type: bool (true/false)
        transmission2_docker_image_pull: true

        # Type: string
        transmission2_docker_image_repo: "lscr.io/linuxserver/transmission"

        # Type: string
        transmission2_docker_image_tag: "latest"

        # Type: string
        transmission2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='transmission') }}:{{ lookup('role_var', '_docker_image_tag', role='transmission') }}"

        # Ports
        # - Internal and External ports need to match for the next set of ports
        # - Lookup available ports and set docker ports accordingly
        # Type: string
        transmission2_docker_ports_51413: "{{ port_lookup_51413.meta.port
                                           if (port_lookup_51413.meta.port is defined) and (port_lookup_51413.meta.port | trim | length > 0)
                                           else '51413' }}"

        # Type: list
        transmission2_docker_ports_defaults: 
          - "{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}:{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}"
          - "{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}:{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}/udp"

        # Type: list
        transmission2_docker_ports_custom: []

        # Envs
        # Type: dict
        transmission2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          UMASK: "002"
          USER: "{{ user.name }}"
          PASS: "{{ user.pass }}"

        # Type: dict
        transmission2_docker_envs_custom: {}

        # Volumes
        # Type: list
        transmission2_docker_volumes_default: 
          - "{{ transmission_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
          - "{{ transmission_role_paths_downloads_location }}/watched:/watch"

        # Type: list
        transmission2_docker_volumes_custom: []

        # Hostname
        # Type: string
        transmission2_docker_hostname: "{{ transmission_name }}"

        # Networks
        # Type: string
        transmission2_docker_networks_alias: "{{ transmission_name }}"

        # Type: list
        transmission2_docker_networks_default: []

        # Type: list
        transmission2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        transmission2_docker_restart_policy: unless-stopped

        # Stop Timeout
        # Type: int
        transmission2_docker_stop_timeout: 900

        # State
        # Type: string
        transmission2_docker_state: started


        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        transmission_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        transmission_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        transmission_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        transmission_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        transmission_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        transmission_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        transmission_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        transmission_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        transmission_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        transmission_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        transmission_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        transmission_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        transmission_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        transmission_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        transmission_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        transmission_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        transmission_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            transmission_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "transmission2.{{ user.domain }}"
              - "transmission.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            transmission_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'transmission2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `transmission2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        transmission2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        transmission2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        transmission2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        transmission2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        transmission2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        transmission2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        transmission2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        transmission2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        transmission2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        transmission2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        transmission2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        transmission2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        transmission2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        transmission2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        transmission2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        transmission2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        transmission2_web_scheme:

        ```

        1.  Example:

            ```yaml
            transmission2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "transmission2.{{ user.domain }}"
              - "transmission.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            transmission2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'transmission2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

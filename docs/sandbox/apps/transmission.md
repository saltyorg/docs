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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

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

    When overriding variables that end in `_default` (like `transmission_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `transmission_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`transmission_instances`"

        ```yaml
        # Type: list
        transmission_instances: ["transmission"]
        ```

        !!! example

            ```yaml
            # Type: list
            transmission_instances: ["transmission", "transmission2"]
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`transmission_role_paths_folder`"

            ```yaml
            # Type: string
            transmission_role_paths_folder: "{{ transmission_name }}"
            ```

        ??? variable string "`transmission_role_paths_location`"

            ```yaml
            # Type: string
            transmission_role_paths_location: "{{ server_appdata_path }}/{{ transmission_role_paths_folder }}"
            ```

        ??? variable string "`transmission_role_paths_downloads_location`"

            ```yaml
            # Type: string
            transmission_role_paths_downloads_location: "{{ downloads_torrents_path }}/{{ transmission_role_paths_folder }}"
            ```

        ??? variable string "`transmission_role_paths_setttings_location`"

            ```yaml
            # Type: string
            transmission_role_paths_setttings_location: "{{ transmission_role_paths_location }}/settings.json"
            ```

    === "Instance-level"

        ??? variable string "`transmission2_paths_folder`"

            ```yaml
            # Type: string
            transmission2_paths_folder: "{{ transmission_name }}"
            ```

        ??? variable string "`transmission2_paths_location`"

            ```yaml
            # Type: string
            transmission2_paths_location: "{{ server_appdata_path }}/{{ transmission_role_paths_folder }}"
            ```

        ??? variable string "`transmission2_paths_downloads_location`"

            ```yaml
            # Type: string
            transmission2_paths_downloads_location: "{{ downloads_torrents_path }}/{{ transmission_role_paths_folder }}"
            ```

        ??? variable string "`transmission2_paths_setttings_location`"

            ```yaml
            # Type: string
            transmission2_paths_setttings_location: "{{ transmission_role_paths_location }}/settings.json"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`transmission_role_web_subdomain`"

            ```yaml
            # Type: string
            transmission_role_web_subdomain: "{{ transmission_name }}"
            ```

        ??? variable string "`transmission_role_web_domain`"

            ```yaml
            # Type: string
            transmission_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`transmission_role_web_port`"

            ```yaml
            # Type: string
            transmission_role_web_port: "9091"
            ```

        ??? variable string "`transmission_role_web_url`"

            ```yaml
            # Type: string
            transmission_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='transmission') + '.' + lookup('role_var', '_web_domain', role='transmission')
                                        if (lookup('role_var', '_web_subdomain', role='transmission') | length > 0)
                                        else lookup('role_var', '_web_domain', role='transmission')) }}"
            ```

    === "Instance-level"

        ??? variable string "`transmission2_web_subdomain`"

            ```yaml
            # Type: string
            transmission2_web_subdomain: "{{ transmission_name }}"
            ```

        ??? variable string "`transmission2_web_domain`"

            ```yaml
            # Type: string
            transmission2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`transmission2_web_port`"

            ```yaml
            # Type: string
            transmission2_web_port: "9091"
            ```

        ??? variable string "`transmission2_web_url`"

            ```yaml
            # Type: string
            transmission2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='transmission') + '.' + lookup('role_var', '_web_domain', role='transmission')
                                    if (lookup('role_var', '_web_subdomain', role='transmission') | length > 0)
                                    else lookup('role_var', '_web_domain', role='transmission')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`transmission_role_dns_record`"

            ```yaml
            # Type: string
            transmission_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='transmission') }}"
            ```

        ??? variable string "`transmission_role_dns_zone`"

            ```yaml
            # Type: string
            transmission_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='transmission') }}"
            ```

        ??? variable bool "`transmission_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            transmission_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`transmission2_dns_record`"

            ```yaml
            # Type: string
            transmission2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='transmission') }}"
            ```

        ??? variable string "`transmission2_dns_zone`"

            ```yaml
            # Type: string
            transmission2_dns_zone: "{{ lookup('role_var', '_web_domain', role='transmission') }}"
            ```

        ??? variable bool "`transmission2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            transmission2_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`transmission_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            transmission_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`transmission_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            transmission_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`transmission_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            transmission_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`transmission_role_traefik_certresolver`"

            ```yaml
            # Type: string
            transmission_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`transmission_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            transmission_role_traefik_enabled: true
            ```

        ??? variable bool "`transmission_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            transmission_role_traefik_api_enabled: true
            ```

        ??? variable string "`transmission_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            transmission_role_traefik_api_endpoint: "PathPrefix(`/rpc`)"
            ```

    === "Instance-level"

        ??? variable string "`transmission2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            transmission2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`transmission2_traefik_middleware_default`"

            ```yaml
            # Type: string
            transmission2_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`transmission2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            transmission2_traefik_middleware_custom: ""
            ```

        ??? variable string "`transmission2_traefik_certresolver`"

            ```yaml
            # Type: string
            transmission2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`transmission2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            transmission2_traefik_enabled: true
            ```

        ??? variable bool "`transmission2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            transmission2_traefik_api_enabled: true
            ```

        ??? variable string "`transmission2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            transmission2_traefik_api_endpoint: "PathPrefix(`/rpc`)"
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`transmission_role_docker_container`"

            ```yaml
            # Type: string
            transmission_role_docker_container: "{{ transmission_name }}"
            ```

        ##### Image

        ??? variable bool "`transmission_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            transmission_role_docker_image_pull: true
            ```

        ??? variable string "`transmission_role_docker_image_repo`"

            ```yaml
            # Type: string
            transmission_role_docker_image_repo: "lscr.io/linuxserver/transmission"
            ```

        ??? variable string "`transmission_role_docker_image_tag`"

            ```yaml
            # Type: string
            transmission_role_docker_image_tag: "latest"
            ```

        ??? variable string "`transmission_role_docker_image`"

            ```yaml
            # Type: string
            transmission_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='transmission') }}:{{ lookup('role_var', '_docker_image_tag', role='transmission') }}"
            ```

        ##### Ports

        ##### - Internal and External ports need to match for the next set of ports

        ##### - Lookup available ports and set docker ports accordingly

        ??? variable string "`transmission_role_docker_ports_51413`"

            ```yaml
            # Type: string
            transmission_role_docker_ports_51413: "{{ port_lookup_51413.meta.port
                                                   if (port_lookup_51413.meta.port is defined) and (port_lookup_51413.meta.port | trim | length > 0)
                                                   else '51413' }}"
            ```

        ??? variable list "`transmission_role_docker_ports_defaults`"

            ```yaml
            # Type: list
            transmission_role_docker_ports_defaults: 
              - "{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}:{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}"
              - "{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}:{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}/udp"
            ```

        ??? variable list "`transmission_role_docker_ports_custom`"

            ```yaml
            # Type: list
            transmission_role_docker_ports_custom: []
            ```

        ##### Envs

        ??? variable dict "`transmission_role_docker_envs_default`"

            ```yaml
            # Type: dict
            transmission_role_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              TZ: "{{ tz }}"
              UMASK: "002"
              USER: "{{ user.name }}"
              PASS: "{{ user.pass }}"
            ```

        ??? variable dict "`transmission_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            transmission_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`transmission_role_docker_volumes_default`"

            ```yaml
            # Type: list
            transmission_role_docker_volumes_default: 
              - "{{ transmission_role_paths_location }}:/config"
              - "{{ server_appdata_path }}/scripts:/scripts"
              - "{{ transmission_role_paths_downloads_location }}/watched:/watch"
            ```

        ??? variable list "`transmission_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            transmission_role_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`transmission_role_docker_hostname`"

            ```yaml
            # Type: string
            transmission_role_docker_hostname: "{{ transmission_name }}"
            ```

        ##### Networks

        ??? variable string "`transmission_role_docker_networks_alias`"

            ```yaml
            # Type: string
            transmission_role_docker_networks_alias: "{{ transmission_name }}"
            ```

        ??? variable list "`transmission_role_docker_networks_default`"

            ```yaml
            # Type: list
            transmission_role_docker_networks_default: []
            ```

        ??? variable list "`transmission_role_docker_networks_custom`"

            ```yaml
            # Type: list
            transmission_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`transmission_role_docker_restart_policy`"

            ```yaml
            # Type: string
            transmission_role_docker_restart_policy: unless-stopped
            ```

        ##### Stop Timeout

        ??? variable int "`transmission_role_docker_stop_timeout`"

            ```yaml
            # Type: int
            transmission_role_docker_stop_timeout: 900
            ```

        ##### State

        ??? variable string "`transmission_role_docker_state`"

            ```yaml
            # Type: string
            transmission_role_docker_state: started
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`transmission2_docker_container`"

            ```yaml
            # Type: string
            transmission2_docker_container: "{{ transmission_name }}"
            ```

        ##### Image

        ??? variable bool "`transmission2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            transmission2_docker_image_pull: true
            ```

        ??? variable string "`transmission2_docker_image_repo`"

            ```yaml
            # Type: string
            transmission2_docker_image_repo: "lscr.io/linuxserver/transmission"
            ```

        ??? variable string "`transmission2_docker_image_tag`"

            ```yaml
            # Type: string
            transmission2_docker_image_tag: "latest"
            ```

        ??? variable string "`transmission2_docker_image`"

            ```yaml
            # Type: string
            transmission2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='transmission') }}:{{ lookup('role_var', '_docker_image_tag', role='transmission') }}"
            ```

        ##### Ports

        ##### - Internal and External ports need to match for the next set of ports

        ##### - Lookup available ports and set docker ports accordingly

        ??? variable string "`transmission2_docker_ports_51413`"

            ```yaml
            # Type: string
            transmission2_docker_ports_51413: "{{ port_lookup_51413.meta.port
                                               if (port_lookup_51413.meta.port is defined) and (port_lookup_51413.meta.port | trim | length > 0)
                                               else '51413' }}"
            ```

        ??? variable list "`transmission2_docker_ports_defaults`"

            ```yaml
            # Type: list
            transmission2_docker_ports_defaults: 
              - "{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}:{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}"
              - "{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}:{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}/udp"
            ```

        ??? variable list "`transmission2_docker_ports_custom`"

            ```yaml
            # Type: list
            transmission2_docker_ports_custom: []
            ```

        ##### Envs

        ??? variable dict "`transmission2_docker_envs_default`"

            ```yaml
            # Type: dict
            transmission2_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              TZ: "{{ tz }}"
              UMASK: "002"
              USER: "{{ user.name }}"
              PASS: "{{ user.pass }}"
            ```

        ??? variable dict "`transmission2_docker_envs_custom`"

            ```yaml
            # Type: dict
            transmission2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`transmission2_docker_volumes_default`"

            ```yaml
            # Type: list
            transmission2_docker_volumes_default: 
              - "{{ transmission_role_paths_location }}:/config"
              - "{{ server_appdata_path }}/scripts:/scripts"
              - "{{ transmission_role_paths_downloads_location }}/watched:/watch"
            ```

        ??? variable list "`transmission2_docker_volumes_custom`"

            ```yaml
            # Type: list
            transmission2_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`transmission2_docker_hostname`"

            ```yaml
            # Type: string
            transmission2_docker_hostname: "{{ transmission_name }}"
            ```

        ##### Networks

        ??? variable string "`transmission2_docker_networks_alias`"

            ```yaml
            # Type: string
            transmission2_docker_networks_alias: "{{ transmission_name }}"
            ```

        ??? variable list "`transmission2_docker_networks_default`"

            ```yaml
            # Type: list
            transmission2_docker_networks_default: []
            ```

        ??? variable list "`transmission2_docker_networks_custom`"

            ```yaml
            # Type: list
            transmission2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`transmission2_docker_restart_policy`"

            ```yaml
            # Type: string
            transmission2_docker_restart_policy: unless-stopped
            ```

        ##### Stop Timeout

        ??? variable int "`transmission2_docker_stop_timeout`"

            ```yaml
            # Type: int
            transmission2_docker_stop_timeout: 900
            ```

        ##### State

        ??? variable string "`transmission2_docker_state`"

            ```yaml
            # Type: string
            transmission2_docker_state: started
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`transmission_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            transmission_role_autoheal_enabled: true
            ```

        ??? variable string "`transmission_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            transmission_role_depends_on: ""
            ```

        ??? variable string "`transmission_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            transmission_role_depends_on_delay: "0"
            ```

        ??? variable string "`transmission_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            transmission_role_depends_on_healthchecks:
            ```

        ??? variable bool "`transmission_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            transmission_role_diun_enabled: true
            ```

        ??? variable bool "`transmission_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            transmission_role_dns_enabled: true
            ```

        ??? variable bool "`transmission_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            transmission_role_docker_controller: true
            ```

        ??? variable bool "`transmission_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            transmission_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`transmission_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            transmission_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`transmission_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            transmission_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`transmission_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            transmission_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`transmission_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            transmission_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`transmission_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            transmission_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`transmission_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            transmission_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`transmission_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            transmission_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                transmission_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "transmission2.{{ user.domain }}"
                  - "transmission.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`transmission_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            transmission_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                transmission_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'transmission2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`transmission_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            transmission_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `transmission2`):

        ??? variable bool "`transmission2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            transmission2_autoheal_enabled: true
            ```

        ??? variable string "`transmission2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            transmission2_depends_on: ""
            ```

        ??? variable string "`transmission2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            transmission2_depends_on_delay: "0"
            ```

        ??? variable string "`transmission2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            transmission2_depends_on_healthchecks:
            ```

        ??? variable bool "`transmission2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            transmission2_diun_enabled: true
            ```

        ??? variable bool "`transmission2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            transmission2_dns_enabled: true
            ```

        ??? variable bool "`transmission2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            transmission2_docker_controller: true
            ```

        ??? variable bool "`transmission2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            transmission2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`transmission2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            transmission2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`transmission2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            transmission2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`transmission2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            transmission2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`transmission2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            transmission2_traefik_robot_enabled: true
            ```

        ??? variable bool "`transmission2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            transmission2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`transmission2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            transmission2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`transmission2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            transmission2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                transmission2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "transmission2.{{ user.domain }}"
                  - "transmission.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`transmission2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            transmission2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                transmission2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'transmission2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`transmission2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            transmission2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
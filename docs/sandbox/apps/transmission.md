---
icon: material/docker
hide:
  - tags
tags:
  - transmission
  - download
  - torrent
---

# Transmission

## Overview

[Transmission](https://transmissionbt.com/) is a fast, easy, and free BitTorrent client.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://transmissionbt.com/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/transmission/transmission/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/transmission/transmission){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/transmission){: .header-icons }|

### 1. Installation

```shell
sb install sandbox-transmission
```

### 2. URL

- To access Transmission, visit <https://transmission.iYOUR_DOMAIN_NAMEi>

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

    ```yaml { .sb-show-on-unchecked title="Applies to all instances of transmission:" }
    transmission_role_web_subdomain: "custom"
    ```

    ```yaml { .sb-show-on-checked title="Applies to a specific instance (e.g., `transmission2`):" }
    transmission2_web_subdomain: "custom2"
    ```

<label class="md-button md-button--stretch" for="sb-checkbox--var-level">
   <input type="checkbox" id="sb-checkbox--var-level"><span class="sb-show-on-unchecked">Show instance-level variables</span><span class="sb-show-on-checked">Show role-level variables</span>
</label>

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `transmission_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `transmission_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`transmission_instances`"

        ```yaml
        # Type: list
        transmission_instances: ["transmission"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            transmission_instances: ["transmission", "transmission2"]
            ```

=== "Paths"

    ??? variable string "`transmission_role_paths_folder`{ .sb-show-on-unchecked }`transmission2_paths_folder`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_paths_folder: "{{ transmission_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_paths_folder: "{{ transmission_name }}"
        ```

    ??? variable string "`transmission_role_paths_location`{ .sb-show-on-unchecked }`transmission2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_paths_location: "{{ server_appdata_path }}/{{ transmission_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_paths_location: "{{ server_appdata_path }}/{{ transmission_role_paths_folder }}"
        ```

    ??? variable string "`transmission_role_paths_downloads_location`{ .sb-show-on-unchecked }`transmission2_paths_downloads_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_paths_downloads_location: "{{ downloads_torrents_path }}/{{ transmission_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_paths_downloads_location: "{{ downloads_torrents_path }}/{{ transmission_role_paths_folder }}"
        ```

    ??? variable string "`transmission_role_paths_setttings_location`{ .sb-show-on-unchecked }`transmission2_paths_setttings_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_paths_setttings_location: "{{ transmission_role_paths_location }}/settings.json"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_paths_setttings_location: "{{ transmission_role_paths_location }}/settings.json"
        ```

=== "Web"

    ??? variable string "`transmission_role_web_subdomain`{ .sb-show-on-unchecked }`transmission2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_web_subdomain: "{{ transmission_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_web_subdomain: "{{ transmission_name }}"
        ```

    ??? variable string "`transmission_role_web_domain`{ .sb-show-on-unchecked }`transmission2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`transmission_role_web_port`{ .sb-show-on-unchecked }`transmission2_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_web_port: "9091"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_web_port: "9091"
        ```

    ??? variable string "`transmission_role_web_url`{ .sb-show-on-unchecked }`transmission2_web_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='transmission') + '.' + lookup('role_var', '_web_domain', role='transmission')
                                    if (lookup('role_var', '_web_subdomain', role='transmission') | length > 0)
                                    else lookup('role_var', '_web_domain', role='transmission')) }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='transmission') + '.' + lookup('role_var', '_web_domain', role='transmission')
                                if (lookup('role_var', '_web_subdomain', role='transmission') | length > 0)
                                else lookup('role_var', '_web_domain', role='transmission')) }}"
        ```

=== "DNS"

    ??? variable string "`transmission_role_dns_record`{ .sb-show-on-unchecked }`transmission2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='transmission') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='transmission') }}"
        ```

    ??? variable string "`transmission_role_dns_zone`{ .sb-show-on-unchecked }`transmission2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='transmission') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_dns_zone: "{{ lookup('role_var', '_web_domain', role='transmission') }}"
        ```

    ??? variable bool "`transmission_role_dns_proxy`{ .sb-show-on-unchecked }`transmission2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        transmission_role_dns_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        transmission2_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`transmission_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`transmission2_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`transmission_role_traefik_middleware_default`{ .sb-show-on-unchecked }`transmission2_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`transmission_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`transmission2_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_traefik_middleware_custom: ""
        ```

    ??? variable string "`transmission_role_traefik_certresolver`{ .sb-show-on-unchecked }`transmission2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`transmission_role_traefik_enabled`{ .sb-show-on-unchecked }`transmission2_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        transmission_role_traefik_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        transmission2_traefik_enabled: true
        ```

    ??? variable bool "`transmission_role_traefik_api_enabled`{ .sb-show-on-unchecked }`transmission2_traefik_api_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        transmission_role_traefik_api_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        transmission2_traefik_api_enabled: true
        ```

    ??? variable string "`transmission_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`transmission2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_traefik_api_endpoint: "PathPrefix(`/rpc`)"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_traefik_api_endpoint: "PathPrefix(`/rpc`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`transmission_role_docker_container`{ .sb-show-on-unchecked }`transmission2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_docker_container: "{{ transmission_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_docker_container: "{{ transmission_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`transmission_role_docker_image_pull`{ .sb-show-on-unchecked }`transmission2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        transmission_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        transmission2_docker_image_pull: true
        ```

    ??? variable string "`transmission_role_docker_image_repo`{ .sb-show-on-unchecked }`transmission2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_docker_image_repo: "lscr.io/linuxserver/transmission"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_docker_image_repo: "lscr.io/linuxserver/transmission"
        ```

    ??? variable string "`transmission_role_docker_image_tag`{ .sb-show-on-unchecked }`transmission2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_docker_image_tag: "latest"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_docker_image_tag: "latest"
        ```

    ??? variable string "`transmission_role_docker_image`{ .sb-show-on-unchecked }`transmission2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='transmission') }}:{{ lookup('role_var', '_docker_image_tag', role='transmission') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='transmission') }}:{{ lookup('role_var', '_docker_image_tag', role='transmission') }}"
        ```

    <h5>Ports</h5>

    <h5>- Internal and External ports need to match for the next set of ports</h5>

    <h5>- Lookup available ports and set docker ports accordingly</h5>

    ??? variable string "`transmission_role_docker_ports_51413`{ .sb-show-on-unchecked }`transmission2_docker_ports_51413`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_docker_ports_51413: "{{ port_lookup_51413.meta.port
                                               if (port_lookup_51413.meta.port is defined) and (port_lookup_51413.meta.port | trim | length > 0)
                                               else '51413' }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_docker_ports_51413: "{{ port_lookup_51413.meta.port
                                           if (port_lookup_51413.meta.port is defined) and (port_lookup_51413.meta.port | trim | length > 0)
                                           else '51413' }}"
        ```

    ??? variable list "`transmission_role_docker_ports_defaults`{ .sb-show-on-unchecked }`transmission2_docker_ports_defaults`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        transmission_role_docker_ports_defaults:
          - "{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}:{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}"
          - "{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}:{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}/udp"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        transmission2_docker_ports_defaults: 
          - "{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}:{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}"
          - "{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}:{{ lookup('role_var', '_docker_ports_51413', role='transmission') }}/udp"
        ```

    ??? variable list "`transmission_role_docker_ports_custom`{ .sb-show-on-unchecked }`transmission2_docker_ports_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        transmission_role_docker_ports_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        transmission2_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    ??? variable dict "`transmission_role_docker_envs_default`{ .sb-show-on-unchecked }`transmission2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        transmission_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          UMASK: "002"
          USER: "{{ user.name }}"
          PASS: "{{ user.pass }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        transmission2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          UMASK: "002"
          USER: "{{ user.name }}"
          PASS: "{{ user.pass }}"
        ```

    ??? variable dict "`transmission_role_docker_envs_custom`{ .sb-show-on-unchecked }`transmission2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        transmission_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        transmission2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`transmission_role_docker_volumes_default`{ .sb-show-on-unchecked }`transmission2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        transmission_role_docker_volumes_default:
          - "{{ transmission_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
          - "{{ transmission_role_paths_downloads_location }}/watched:/watch"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        transmission2_docker_volumes_default: 
          - "{{ transmission_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
          - "{{ transmission_role_paths_downloads_location }}/watched:/watch"
        ```

    ??? variable list "`transmission_role_docker_volumes_custom`{ .sb-show-on-unchecked }`transmission2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        transmission_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        transmission2_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`transmission_role_docker_hostname`{ .sb-show-on-unchecked }`transmission2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_docker_hostname: "{{ transmission_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_docker_hostname: "{{ transmission_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`transmission_role_docker_networks_alias`{ .sb-show-on-unchecked }`transmission2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_docker_networks_alias: "{{ transmission_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_docker_networks_alias: "{{ transmission_name }}"
        ```

    ??? variable list "`transmission_role_docker_networks_default`{ .sb-show-on-unchecked }`transmission2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        transmission_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        transmission2_docker_networks_default: []
        ```

    ??? variable list "`transmission_role_docker_networks_custom`{ .sb-show-on-unchecked }`transmission2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        transmission_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        transmission2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`transmission_role_docker_restart_policy`{ .sb-show-on-unchecked }`transmission2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_docker_restart_policy: unless-stopped
        ```

    <h5>Stop Timeout</h5>

    ??? variable int "`transmission_role_docker_stop_timeout`{ .sb-show-on-unchecked }`transmission2_docker_stop_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        transmission_role_docker_stop_timeout: 900
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        transmission2_docker_stop_timeout: 900
        ```

    <h5>State</h5>

    ??? variable string "`transmission_role_docker_state`{ .sb-show-on-unchecked }`transmission2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        transmission_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        transmission2_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`transmission_role_autoheal_enabled`{ .sb-show-on-unchecked }`transmission2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        transmission_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        transmission2_autoheal_enabled: true
        ```

    ??? variable string "`transmission_role_depends_on`{ .sb-show-on-unchecked }`transmission2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        transmission_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        transmission2_depends_on: ""
        ```

    ??? variable string "`transmission_role_depends_on_delay`{ .sb-show-on-unchecked }`transmission2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        transmission_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        transmission2_depends_on_delay: "0"
        ```

    ??? variable string "`transmission_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`transmission2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        transmission_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        transmission2_depends_on_healthchecks:
        ```

    ??? variable bool "`transmission_role_diun_enabled`{ .sb-show-on-unchecked }`transmission2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        transmission_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        transmission2_diun_enabled: true
        ```

    ??? variable bool "`transmission_role_dns_enabled`{ .sb-show-on-unchecked }`transmission2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        transmission_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        transmission2_dns_enabled: true
        ```

    ??? variable bool "`transmission_role_docker_controller`{ .sb-show-on-unchecked }`transmission2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        transmission_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        transmission2_docker_controller: true
        ```

    ??? variable bool "`transmission_role_docker_volumes_download`{ .sb-show-on-unchecked }`transmission2_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        transmission_role_docker_volumes_download:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        transmission2_docker_volumes_download:
        ```

    ??? variable bool "`transmission_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`transmission2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        transmission_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        transmission2_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`transmission_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`transmission2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        transmission_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        transmission2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`transmission_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`transmission2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        transmission_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        transmission2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`transmission_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`transmission2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        transmission_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        transmission2_traefik_gzip_enabled: false
        ```

    ??? variable bool "`transmission_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`transmission2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        transmission_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        transmission2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`transmission_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`transmission2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        transmission_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        transmission2_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`transmission_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`transmission2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        transmission_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        transmission2_traefik_robot_enabled: true
        ```

    ??? variable bool "`transmission_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`transmission2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        transmission_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        transmission2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`transmission_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`transmission2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        transmission_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        transmission2_traefik_wildcard_enabled: true
        ```

    ??? variable list "`transmission_role_web_fqdn_override`{ .sb-show-on-unchecked }`transmission2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        transmission_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        transmission2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            transmission_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "transmission2.{{ user.domain }}"
              - "transmission.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            transmission2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "transmission2.{{ user.domain }}"
              - "transmission.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`transmission_role_web_host_override`{ .sb-show-on-unchecked }`transmission2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        transmission_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        transmission2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            transmission_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'transmission2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            transmission2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'transmission2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`transmission_role_web_scheme`{ .sb-show-on-unchecked }`transmission2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        transmission_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        transmission2_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
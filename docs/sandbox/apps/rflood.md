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

- To access rFlood, visit `https://rflood._yourdomain.com_`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `rflood_instances`.

    ```yaml { .sb-show-on-unchecked title="Applies to all instances of rflood:" }
    rflood_role_web_subdomain: "custom"
    ```

    ```yaml { .sb-show-on-checked title="Applies to a specific instance (e.g., `rflood2`):" }
    rflood2_web_subdomain: "custom2"
    ```

<label class="md-button md-button--stretch" for="sb-checkbox--var-level">
   <input type="checkbox" id="sb-checkbox--var-level"><span class="sb-show-on-unchecked">Show instance-level variables</span><span class="sb-show-on-checked">Show role-level variables</span>
</label>

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `rflood_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `rflood_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`rflood_instances`"

        ```yaml
        # Type: list
        rflood_instances: ["rflood"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            rflood_instances: ["rflood", "rflood2"]
            ```

=== "Paths"

    ??? variable string "`rflood_role_paths_folder`{ .sb-show-on-unchecked }`rflood2_paths_folder`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_paths_folder: "{{ rflood_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_paths_folder: "{{ rflood_name }}"
        ```

    ??? variable string "`rflood_role_paths_location`{ .sb-show-on-unchecked }`rflood2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_paths_location: "{{ server_appdata_path }}/{{ rflood_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_paths_location: "{{ server_appdata_path }}/{{ rflood_role_paths_folder }}"
        ```

    ??? variable string "`rflood_role_paths_downloads_location`{ .sb-show-on-unchecked }`rflood2_paths_downloads_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_paths_downloads_location: "{{ downloads_torrents_path }}/{{ rflood_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_paths_downloads_location: "{{ downloads_torrents_path }}/{{ rflood_role_paths_folder }}"
        ```

    ??? variable string "`rflood_role_paths_rtorrent_rc_location`{ .sb-show-on-unchecked }`rflood2_paths_rtorrent_rc_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Config files
        # Type: string
        rflood_role_paths_rtorrent_rc_location: "{{ rflood_role_paths_location }}/rtorrent.rc"
        ```

        ```yaml { .sb-show-on-checked }
        # Config files
        # Type: string
        rflood2_paths_rtorrent_rc_location: "{{ rflood_role_paths_location }}/rtorrent.rc"
        ```

=== "Web"

    ??? variable string "`rflood_role_web_subdomain`{ .sb-show-on-unchecked }`rflood2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_web_subdomain: "{{ rflood_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_web_subdomain: "{{ rflood_name }}"
        ```

    ??? variable string "`rflood_role_web_domain`{ .sb-show-on-unchecked }`rflood2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`rflood_role_web_port`{ .sb-show-on-unchecked }`rflood2_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_web_port: "3000"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_web_port: "3000"
        ```

    ??? variable string "`rflood_role_web_url`{ .sb-show-on-unchecked }`rflood2_web_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='rflood') + '.' + lookup('role_var', '_web_domain', role='rflood')
                              if (lookup('role_var', '_web_subdomain', role='rflood') | length > 0)
                              else lookup('role_var', '_web_domain', role='rflood')) }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='rflood') + '.' + lookup('role_var', '_web_domain', role='rflood')
                          if (lookup('role_var', '_web_subdomain', role='rflood') | length > 0)
                          else lookup('role_var', '_web_domain', role='rflood')) }}"
        ```

=== "DNS"

    ??? variable string "`rflood_role_dns_record`{ .sb-show-on-unchecked }`rflood2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='rflood') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='rflood') }}"
        ```

    ??? variable string "`rflood_role_dns_zone`{ .sb-show-on-unchecked }`rflood2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='rflood') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_dns_zone: "{{ lookup('role_var', '_web_domain', role='rflood') }}"
        ```

    ??? variable bool "`rflood_role_dns_proxy`{ .sb-show-on-unchecked }`rflood2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_dns_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`rflood_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`rflood2_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`rflood_role_traefik_middleware_default`{ .sb-show-on-unchecked }`rflood2_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`rflood_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`rflood2_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_traefik_middleware_custom: ""
        ```

    ??? variable string "`rflood_role_traefik_certresolver`{ .sb-show-on-unchecked }`rflood2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`rflood_role_traefik_enabled`{ .sb-show-on-unchecked }`rflood2_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_traefik_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_traefik_enabled: true
        ```

    ??? variable bool "`rflood_role_traefik_api_enabled`{ .sb-show-on-unchecked }`rflood2_traefik_api_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Disabled for security reasons, no authentication on API /!\
        # Type: bool (true/false)
        rflood_role_traefik_api_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Disabled for security reasons, no authentication on API /!\
        # Type: bool (true/false)
        rflood2_traefik_api_enabled: false
        ```

    ??? variable string "`rflood_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`rflood2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_traefik_api_endpoint: "PathPrefix(`/api`)"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_traefik_api_endpoint: "PathPrefix(`/api`)"
        ```

=== "Config"

    ??? variable bool "`rflood_role_config_public_trackers`{ .sb-show-on-unchecked }`rflood2_config_public_trackers`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_config_public_trackers: false
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_config_public_trackers: false
        ```

    ??? variable list "`rflood_role_config_rflood_rc_settings_default`{ .sb-show-on-unchecked }`rflood2_config_rflood_rc_settings_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
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
        ```

        ```yaml { .sb-show-on-checked }
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
        ```

    ??? variable list "`rflood_role_config_rflood_rc_settings_custom`{ .sb-show-on-unchecked }`rflood2_config_rflood_rc_settings_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_config_rflood_rc_settings_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_config_rflood_rc_settings_custom: []
        ```

    ??? variable string "`rflood_role_config_rflood_rc_settings_list`{ .sb-show-on-unchecked }`rflood2_config_rflood_rc_settings_list`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_config_rflood_rc_settings_list: "{{ lookup('role_var', '_config_rflood_rc_settings_default', role='rflood')
                                                        + lookup('role_var', '_config_rflood_rc_settings_custom', role='rflood') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_config_rflood_rc_settings_list: "{{ lookup('role_var', '_config_rflood_rc_settings_default', role='rflood')
                                                    + lookup('role_var', '_config_rflood_rc_settings_custom', role='rflood') }}"
        ```

=== "Docker"

    Container
    { .sb-h5 }

    ??? variable string "`rflood_role_docker_container`{ .sb-show-on-unchecked }`rflood2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_container: "{{ rflood_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_container: "{{ rflood_name }}"
        ```

    Image
    { .sb-h5 }

    ??? variable bool "`rflood_role_docker_image_pull`{ .sb-show-on-unchecked }`rflood2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_docker_image_pull: true
        ```

    ??? variable string "`rflood_role_docker_image_repo`{ .sb-show-on-unchecked }`rflood2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_image_repo: "ghcr.io/hotio/rflood"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_image_repo: "ghcr.io/hotio/rflood"
        ```

    ??? variable string "`rflood_role_docker_image_tag`{ .sb-show-on-unchecked }`rflood2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_image_tag: "release"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_image_tag: "release"
        ```

    ??? variable string "`rflood_role_docker_image`{ .sb-show-on-unchecked }`rflood2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='rflood') }}:{{ lookup('role_var', '_docker_image_tag', role='rflood') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='rflood') }}:{{ lookup('role_var', '_docker_image_tag', role='rflood') }}"
        ```

    Ports
    { .sb-h5 }

    - Internal and External ports need to match for the next set of ports
    { .sb-h5 }

    - Lookup available ports and set docker ports accordingly
    { .sb-h5 }

    ??? variable string "`rflood_role_docker_ports_50000`{ .sb-show-on-unchecked }`rflood2_docker_ports_50000`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_ports_50000: "{{ port_lookup_50000.meta.port
                                         if (port_lookup_50000.meta.port is defined) and (port_lookup_50000.meta.port | trim | length > 0)
                                         else '50000' }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_ports_50000: "{{ port_lookup_50000.meta.port
                                     if (port_lookup_50000.meta.port is defined) and (port_lookup_50000.meta.port | trim | length > 0)
                                     else '50000' }}"
        ```

    ??? variable string "`rflood_role_docker_ports_6881`{ .sb-show-on-unchecked }`rflood2_docker_ports_6881`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_ports_6881: "{{ port_lookup_6881.meta.port
                                        if (port_lookup_6881.meta.port is defined) and (port_lookup_6881.meta.port | trim | length > 0)
                                        else '6881' }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_ports_6881: "{{ port_lookup_6881.meta.port
                                    if (port_lookup_6881.meta.port is defined) and (port_lookup_6881.meta.port | trim | length > 0)
                                    else '6881' }}"
        ```

    ??? variable list "`rflood_role_docker_ports_defaults`{ .sb-show-on-unchecked }`rflood2_docker_ports_defaults`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_ports_defaults: 
          - "{{ lookup('role_var', '_docker_ports_50000', role='rflood') }}:{{ lookup('role_var', '_docker_ports_50000', role='rflood') }}"
          - "{{ lookup('role_var', '_docker_ports_6881', role='rflood') }}:{{ lookup('role_var', '_docker_ports_6881', role='rflood') }}/udp"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_ports_defaults: 
          - "{{ lookup('role_var', '_docker_ports_50000', role='rflood') }}:{{ lookup('role_var', '_docker_ports_50000', role='rflood') }}"
          - "{{ lookup('role_var', '_docker_ports_6881', role='rflood') }}:{{ lookup('role_var', '_docker_ports_6881', role='rflood') }}/udp"
        ```

    ??? variable list "`rflood_role_docker_ports_custom`{ .sb-show-on-unchecked }`rflood2_docker_ports_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_ports_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_ports_custom: []
        ```

    Envs
    { .sb-h5 }

    ??? variable dict "`rflood_role_docker_envs_default`{ .sb-show-on-unchecked }`rflood2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        rflood_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          UMASK: "002"
          FLOOD_AUTH: "false"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        rflood2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          UMASK: "002"
          FLOOD_AUTH: "false"
        ```

    ??? variable dict "`rflood_role_docker_envs_custom`{ .sb-show-on-unchecked }`rflood2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        rflood_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        rflood2_docker_envs_custom: {}
        ```

    Volumes
    { .sb-h5 }

    ??? variable list "`rflood_role_docker_volumes_default`{ .sb-show-on-unchecked }`rflood2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='rflood') }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='rflood') }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
        ```

    ??? variable list "`rflood_role_docker_volumes_custom`{ .sb-show-on-unchecked }`rflood2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_volumes_custom: []
        ```

    Hostname
    { .sb-h5 }

    ??? variable string "`rflood_role_docker_hostname`{ .sb-show-on-unchecked }`rflood2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_hostname: "{{ rflood_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_hostname: "{{ rflood_name }}"
        ```

    Networks
    { .sb-h5 }

    ??? variable string "`rflood_role_docker_networks_alias`{ .sb-show-on-unchecked }`rflood2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_networks_alias: "{{ rflood_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_networks_alias: "{{ rflood_name }}"
        ```

    ??? variable list "`rflood_role_docker_networks_default`{ .sb-show-on-unchecked }`rflood2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_networks_default: []
        ```

    ??? variable list "`rflood_role_docker_networks_custom`{ .sb-show-on-unchecked }`rflood2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_networks_custom: []
        ```

    Restart Policy
    { .sb-h5 }

    ??? variable string "`rflood_role_docker_restart_policy`{ .sb-show-on-unchecked }`rflood2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_restart_policy: unless-stopped
        ```

    Stop Timeout
    { .sb-h5 }

    ??? variable int "`rflood_role_docker_stop_timeout`{ .sb-show-on-unchecked }`rflood2_docker_stop_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rflood_role_docker_stop_timeout: 900
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rflood2_docker_stop_timeout: 900
        ```

    State
    { .sb-h5 }

    ??? variable string "`rflood_role_docker_state`{ .sb-show-on-unchecked }`rflood2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`rflood_role_autoheal_enabled`{ .sb-show-on-unchecked }`rflood2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        rflood_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        rflood2_autoheal_enabled: true
        ```

    ??? variable string "`rflood_role_depends_on`{ .sb-show-on-unchecked }`rflood2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        rflood_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        rflood2_depends_on: ""
        ```

    ??? variable string "`rflood_role_depends_on_delay`{ .sb-show-on-unchecked }`rflood2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        rflood_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        rflood2_depends_on_delay: "0"
        ```

    ??? variable string "`rflood_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`rflood2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        rflood_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        rflood2_depends_on_healthchecks:
        ```

    ??? variable bool "`rflood_role_diun_enabled`{ .sb-show-on-unchecked }`rflood2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        rflood_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        rflood2_diun_enabled: true
        ```

    ??? variable bool "`rflood_role_dns_enabled`{ .sb-show-on-unchecked }`rflood2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        rflood_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        rflood2_dns_enabled: true
        ```

    ??? variable bool "`rflood_role_docker_controller`{ .sb-show-on-unchecked }`rflood2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        rflood_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        rflood2_docker_controller: true
        ```

    ??? variable bool "`rflood_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`rflood2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        rflood_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        rflood2_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`rflood_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`rflood2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        rflood_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        rflood2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`rflood_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`rflood2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        rflood_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        rflood2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`rflood_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`rflood2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        rflood_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        rflood2_traefik_gzip_enabled: false
        ```

    ??? variable bool "`rflood_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`rflood2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`rflood_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`rflood2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`rflood_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`rflood2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        rflood_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        rflood2_traefik_robot_enabled: true
        ```

    ??? variable bool "`rflood_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`rflood2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        rflood_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        rflood2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`rflood_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`rflood2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        rflood_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        rflood2_traefik_wildcard_enabled: true
        ```

    ??? variable list "`rflood_role_web_fqdn_override`{ .sb-show-on-unchecked }`rflood2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        rflood_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        rflood2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            rflood_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "rflood2.{{ user.domain }}"
              - "rflood.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            rflood2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "rflood2.{{ user.domain }}"
              - "rflood.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`rflood_role_web_host_override`{ .sb-show-on-unchecked }`rflood2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        rflood_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        rflood2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            rflood_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'rflood2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            rflood2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'rflood2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`rflood_role_web_scheme`{ .sb-show-on-unchecked }`rflood2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        rflood_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        rflood2_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
icon: material/docker
hide:
  - tags
tags:
  - rflood
  - torrent
  - frontend
saltbox_automation:
  disabled: false
  sections:
    inventory: true
    overview: true
  inventory:
    show_sections: []
    hide_sections: []
    example_overrides: {}
  app_links:
    - name: Manual
      url:
      type: documentation
    - name: Releases
      url: https://github.com/hotio/rflood/pkgs/container/rflood
      type: github
    - name: Community
      url: https://hotio.dev/discord
      type: discord
  project_description:
    name: rFlood
    summary: |
      a Docker image with rTorrent and the Flood UI, also optional WireGuard VPN support.
    link: https://github.com/jesec/flood
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# rFlood

## Overview

[rFlood](https://github.com/jesec/flood) is a Docker image with rTorrent and the Flood UI, also optional WireGuard VPN support.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/hotio/rflood/pkgs/container/rflood){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://hotio.dev/discord){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-rflood
```

## Usage

Visit <https://rflood.iYOUR_DOMAIN_NAMEi>.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults<label class="sb-toggle--override-scope md-annotation__index" title="Supports multiple instances! Click to toggle override level"><input type="checkbox" name="scope" hidden/></label>

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  **This role supports multiple instances via `rflood_instances`.**

    !!! example "Example override"

        === "Role-level"

            ```yaml
            rflood_role_web_subdomain: "custom"
            ```

            :material-arrow-right-bottom-bold: Applies to all instances of rflood

        === "Instance-level"

            ```yaml
            rflood2_web_subdomain: "custom2"
            ```

            :material-arrow-right-bottom-bold: Applies to the instance named rflood2

    !!! warning "Avoid overriding variables ending in `_default`"

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

    ??? variable string "`rflood_role_config_rflood_rc_settings_default`{ .sb-show-on-unchecked }`rflood2_config_rflood_rc_settings_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # rtorrent.rc
        # Type: string
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
        # rtorrent.rc
        # Type: string
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

    <h5>Container</h5>

    ??? variable string "`rflood_role_docker_container`{ .sb-show-on-unchecked }`rflood2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_container: "{{ rflood_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_container: "{{ rflood_name }}"
        ```

    <h5>Image</h5>

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

    <h5>Ports</h5>

    <h5>- Internal and External ports need to match for the next set of ports</h5>

    <h5>- Lookup available ports and set docker ports accordingly</h5>

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

    ??? variable list "`rflood_role_docker_ports_default`{ .sb-show-on-unchecked }`rflood2_docker_ports_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_ports_default:
          - "{{ lookup('role_var', '_docker_ports_50000', role='rflood') }}:{{ lookup('role_var', '_docker_ports_50000', role='rflood') }}"
          - "{{ lookup('role_var', '_docker_ports_6881', role='rflood') }}:{{ lookup('role_var', '_docker_ports_6881', role='rflood') }}/udp"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_ports_default:
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

    <h5>Envs</h5>

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

    <h5>Volumes</h5>

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

    <h5>Hostname</h5>

    ??? variable string "`rflood_role_docker_hostname`{ .sb-show-on-unchecked }`rflood2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_hostname: "{{ rflood_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_hostname: "{{ rflood_name }}"
        ```

    <h5>Networks</h5>

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

    <h5>Restart Policy</h5>

    ??? variable string "`rflood_role_docker_restart_policy`{ .sb-show-on-unchecked }`rflood2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_restart_policy: unless-stopped
        ```

    <h5>Stop Timeout</h5>

    ??? variable int "`rflood_role_docker_stop_timeout`{ .sb-show-on-unchecked }`rflood2_docker_stop_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rflood_role_docker_stop_timeout: 900
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rflood2_docker_stop_timeout: 900
        ```

    <h5>State</h5>

    ??? variable string "`rflood_role_docker_state`{ .sb-show-on-unchecked }`rflood2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`rflood_role_docker_blkio_weight`{ .sb-show-on-unchecked }`rflood2_docker_blkio_weight`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rflood_role_docker_blkio_weight:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rflood2_docker_blkio_weight:
        ```

    ??? variable int "`rflood_role_docker_cpu_period`{ .sb-show-on-unchecked }`rflood2_docker_cpu_period`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rflood_role_docker_cpu_period:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rflood2_docker_cpu_period:
        ```

    ??? variable int "`rflood_role_docker_cpu_quota`{ .sb-show-on-unchecked }`rflood2_docker_cpu_quota`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rflood_role_docker_cpu_quota:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rflood2_docker_cpu_quota:
        ```

    ??? variable int "`rflood_role_docker_cpu_shares`{ .sb-show-on-unchecked }`rflood2_docker_cpu_shares`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rflood_role_docker_cpu_shares:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rflood2_docker_cpu_shares:
        ```

    ??? variable string "`rflood_role_docker_cpus`{ .sb-show-on-unchecked }`rflood2_docker_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_cpus:
        ```

    ??? variable string "`rflood_role_docker_cpuset_cpus`{ .sb-show-on-unchecked }`rflood2_docker_cpuset_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_cpuset_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_cpuset_cpus:
        ```

    ??? variable string "`rflood_role_docker_cpuset_mems`{ .sb-show-on-unchecked }`rflood2_docker_cpuset_mems`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_cpuset_mems:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_cpuset_mems:
        ```

    ??? variable string "`rflood_role_docker_kernel_memory`{ .sb-show-on-unchecked }`rflood2_docker_kernel_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_kernel_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_kernel_memory:
        ```

    ??? variable string "`rflood_role_docker_memory`{ .sb-show-on-unchecked }`rflood2_docker_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_memory:
        ```

    ??? variable string "`rflood_role_docker_memory_reservation`{ .sb-show-on-unchecked }`rflood2_docker_memory_reservation`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_memory_reservation:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_memory_reservation:
        ```

    ??? variable string "`rflood_role_docker_memory_swap`{ .sb-show-on-unchecked }`rflood2_docker_memory_swap`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_memory_swap:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_memory_swap:
        ```

    ??? variable int "`rflood_role_docker_memory_swappiness`{ .sb-show-on-unchecked }`rflood2_docker_memory_swappiness`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rflood_role_docker_memory_swappiness:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rflood2_docker_memory_swappiness:
        ```

    ??? variable string "`rflood_role_docker_shm_size`{ .sb-show-on-unchecked }`rflood2_docker_shm_size`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_shm_size:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`rflood_role_docker_cap_drop`{ .sb-show-on-unchecked }`rflood2_docker_cap_drop`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_cap_drop:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_cap_drop:
        ```

    ??? variable string "`rflood_role_docker_cgroupns_mode`{ .sb-show-on-unchecked }`rflood2_docker_cgroupns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_cgroupns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_cgroupns_mode:
        ```

    ??? variable list "`rflood_role_docker_device_cgroup_rules`{ .sb-show-on-unchecked }`rflood2_docker_device_cgroup_rules`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_device_cgroup_rules:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_device_cgroup_rules:
        ```

    ??? variable list "`rflood_role_docker_device_read_bps`{ .sb-show-on-unchecked }`rflood2_docker_device_read_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_device_read_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_device_read_bps:
        ```

    ??? variable list "`rflood_role_docker_device_read_iops`{ .sb-show-on-unchecked }`rflood2_docker_device_read_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_device_read_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_device_read_iops:
        ```

    ??? variable list "`rflood_role_docker_device_requests`{ .sb-show-on-unchecked }`rflood2_docker_device_requests`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_device_requests:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_device_requests:
        ```

    ??? variable list "`rflood_role_docker_device_write_bps`{ .sb-show-on-unchecked }`rflood2_docker_device_write_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_device_write_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_device_write_bps:
        ```

    ??? variable list "`rflood_role_docker_device_write_iops`{ .sb-show-on-unchecked }`rflood2_docker_device_write_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_device_write_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_device_write_iops:
        ```

    ??? variable list "`rflood_role_docker_devices`{ .sb-show-on-unchecked }`rflood2_docker_devices`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_devices:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_devices:
        ```

    ??? variable string "`rflood_role_docker_devices_default`{ .sb-show-on-unchecked }`rflood2_docker_devices_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_devices_default:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_devices_default:
        ```

    ??? variable list "`rflood_role_docker_groups`{ .sb-show-on-unchecked }`rflood2_docker_groups`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_groups:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_groups:
        ```

    ??? variable bool "`rflood_role_docker_privileged`{ .sb-show-on-unchecked }`rflood2_docker_privileged`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_docker_privileged:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_docker_privileged:
        ```

    ??? variable list "`rflood_role_docker_security_opts`{ .sb-show-on-unchecked }`rflood2_docker_security_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_security_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_security_opts:
        ```

    ??? variable string "`rflood_role_docker_user`{ .sb-show-on-unchecked }`rflood2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_user:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_user:
        ```

    ??? variable string "`rflood_role_docker_userns_mode`{ .sb-show-on-unchecked }`rflood2_docker_userns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_userns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`rflood_role_docker_dns_opts`{ .sb-show-on-unchecked }`rflood2_docker_dns_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_dns_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_dns_opts:
        ```

    ??? variable list "`rflood_role_docker_dns_search_domains`{ .sb-show-on-unchecked }`rflood2_docker_dns_search_domains`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_dns_search_domains:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_dns_search_domains:
        ```

    ??? variable list "`rflood_role_docker_dns_servers`{ .sb-show-on-unchecked }`rflood2_docker_dns_servers`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_dns_servers:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_dns_servers:
        ```

    ??? variable string "`rflood_role_docker_domainname`{ .sb-show-on-unchecked }`rflood2_docker_domainname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_domainname:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_domainname:
        ```

    ??? variable list "`rflood_role_docker_exposed_ports`{ .sb-show-on-unchecked }`rflood2_docker_exposed_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_exposed_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_exposed_ports:
        ```

    ??? variable dict "`rflood_role_docker_hosts`{ .sb-show-on-unchecked }`rflood2_docker_hosts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        rflood_role_docker_hosts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        rflood2_docker_hosts:
        ```

    ??? variable bool "`rflood_role_docker_hosts_use_common`{ .sb-show-on-unchecked }`rflood2_docker_hosts_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_docker_hosts_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_docker_hosts_use_common:
        ```

    ??? variable string "`rflood_role_docker_ipc_mode`{ .sb-show-on-unchecked }`rflood2_docker_ipc_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_ipc_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_ipc_mode:
        ```

    ??? variable list "`rflood_role_docker_links`{ .sb-show-on-unchecked }`rflood2_docker_links`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_links:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_links:
        ```

    ??? variable string "`rflood_role_docker_network_mode`{ .sb-show-on-unchecked }`rflood2_docker_network_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_network_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_network_mode:
        ```

    ??? variable string "`rflood_role_docker_pid_mode`{ .sb-show-on-unchecked }`rflood2_docker_pid_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_pid_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_pid_mode:
        ```

    ??? variable string "`rflood_role_docker_uts`{ .sb-show-on-unchecked }`rflood2_docker_uts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_uts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`rflood_role_docker_keep_volumes`{ .sb-show-on-unchecked }`rflood2_docker_keep_volumes`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_docker_keep_volumes:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_docker_keep_volumes:
        ```

    ??? variable list "`rflood_role_docker_mounts`{ .sb-show-on-unchecked }`rflood2_docker_mounts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_mounts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_mounts:
        ```

    ??? variable dict "`rflood_role_docker_storage_opts`{ .sb-show-on-unchecked }`rflood2_docker_storage_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        rflood_role_docker_storage_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        rflood2_docker_storage_opts:
        ```

    ??? variable list "`rflood_role_docker_tmpfs`{ .sb-show-on-unchecked }`rflood2_docker_tmpfs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_tmpfs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_tmpfs:
        ```

    ??? variable string "`rflood_role_docker_volume_driver`{ .sb-show-on-unchecked }`rflood2_docker_volume_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_volume_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_volume_driver:
        ```

    ??? variable list "`rflood_role_docker_volumes_from`{ .sb-show-on-unchecked }`rflood2_docker_volumes_from`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_volumes_from:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_volumes_from:
        ```

    ??? variable bool "`rflood_role_docker_volumes_global`{ .sb-show-on-unchecked }`rflood2_docker_volumes_global`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_docker_volumes_global:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_docker_volumes_global:
        ```

    ??? variable string "`rflood_role_docker_working_dir`{ .sb-show-on-unchecked }`rflood2_docker_working_dir`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_working_dir:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`rflood_role_docker_auto_remove`{ .sb-show-on-unchecked }`rflood2_docker_auto_remove`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_docker_auto_remove:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_docker_auto_remove:
        ```

    ??? variable bool "`rflood_role_docker_cleanup`{ .sb-show-on-unchecked }`rflood2_docker_cleanup`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_docker_cleanup:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_docker_cleanup:
        ```

    ??? variable string "`rflood_role_docker_force_kill`{ .sb-show-on-unchecked }`rflood2_docker_force_kill`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_force_kill:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_force_kill:
        ```

    ??? variable dict "`rflood_role_docker_healthcheck`{ .sb-show-on-unchecked }`rflood2_docker_healthcheck`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        rflood_role_docker_healthcheck:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        rflood2_docker_healthcheck:
        ```

    ??? variable int "`rflood_role_docker_healthy_wait_timeout`{ .sb-show-on-unchecked }`rflood2_docker_healthy_wait_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rflood_role_docker_healthy_wait_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rflood2_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`rflood_role_docker_init`{ .sb-show-on-unchecked }`rflood2_docker_init`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_docker_init:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_docker_init:
        ```

    ??? variable string "`rflood_role_docker_kill_signal`{ .sb-show-on-unchecked }`rflood2_docker_kill_signal`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_kill_signal:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_kill_signal:
        ```

    ??? variable string "`rflood_role_docker_log_driver`{ .sb-show-on-unchecked }`rflood2_docker_log_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_log_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_log_driver:
        ```

    ??? variable dict "`rflood_role_docker_log_options`{ .sb-show-on-unchecked }`rflood2_docker_log_options`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        rflood_role_docker_log_options:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        rflood2_docker_log_options:
        ```

    ??? variable bool "`rflood_role_docker_oom_killer`{ .sb-show-on-unchecked }`rflood2_docker_oom_killer`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_docker_oom_killer:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_docker_oom_killer:
        ```

    ??? variable int "`rflood_role_docker_oom_score_adj`{ .sb-show-on-unchecked }`rflood2_docker_oom_score_adj`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rflood_role_docker_oom_score_adj:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rflood2_docker_oom_score_adj:
        ```

    ??? variable bool "`rflood_role_docker_output_logs`{ .sb-show-on-unchecked }`rflood2_docker_output_logs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_docker_output_logs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_docker_output_logs:
        ```

    ??? variable bool "`rflood_role_docker_paused`{ .sb-show-on-unchecked }`rflood2_docker_paused`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_docker_paused:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_docker_paused:
        ```

    ??? variable bool "`rflood_role_docker_recreate`{ .sb-show-on-unchecked }`rflood2_docker_recreate`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_docker_recreate:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_docker_recreate:
        ```

    ??? variable int "`rflood_role_docker_restart_retries`{ .sb-show-on-unchecked }`rflood2_docker_restart_retries`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rflood_role_docker_restart_retries:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rflood2_docker_restart_retries:
        ```

    <h5>Other Options</h5>

    ??? variable list "`rflood_role_docker_capabilities`{ .sb-show-on-unchecked }`rflood2_docker_capabilities`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_capabilities:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_capabilities:
        ```

    ??? variable string "`rflood_role_docker_cgroup_parent`{ .sb-show-on-unchecked }`rflood2_docker_cgroup_parent`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_cgroup_parent:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_cgroup_parent:
        ```

    ??? variable list "`rflood_role_docker_commands`{ .sb-show-on-unchecked }`rflood2_docker_commands`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_commands:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_commands:
        ```

    ??? variable int "`rflood_role_docker_create_timeout`{ .sb-show-on-unchecked }`rflood2_docker_create_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rflood_role_docker_create_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rflood2_docker_create_timeout:
        ```

    ??? variable string "`rflood_role_docker_entrypoint`{ .sb-show-on-unchecked }`rflood2_docker_entrypoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_entrypoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_entrypoint:
        ```

    ??? variable string "`rflood_role_docker_env_file`{ .sb-show-on-unchecked }`rflood2_docker_env_file`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_env_file:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_env_file:
        ```

    ??? variable dict "`rflood_role_docker_labels`{ .sb-show-on-unchecked }`rflood2_docker_labels`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        rflood_role_docker_labels:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        rflood2_docker_labels:
        ```

    ??? variable bool "`rflood_role_docker_labels_use_common`{ .sb-show-on-unchecked }`rflood2_docker_labels_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_docker_labels_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_docker_labels_use_common:
        ```

    ??? variable bool "`rflood_role_docker_read_only`{ .sb-show-on-unchecked }`rflood2_docker_read_only`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_docker_read_only:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_docker_read_only:
        ```

    ??? variable string "`rflood_role_docker_runtime`{ .sb-show-on-unchecked }`rflood2_docker_runtime`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_runtime:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_runtime:
        ```

    ??? variable list "`rflood_role_docker_sysctls`{ .sb-show-on-unchecked }`rflood2_docker_sysctls`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_sysctls:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_sysctls:
        ```

    ??? variable list "`rflood_role_docker_ulimits`{ .sb-show-on-unchecked }`rflood2_docker_ulimits`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rflood_role_docker_ulimits:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rflood2_docker_ulimits:
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

    ??? variable string "`rflood_role_config_public_trackers`{ .sb-show-on-unchecked }`rflood2_config_public_trackers`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_config_public_trackers:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_config_public_trackers:
        ```

    ??? variable string "`rflood_role_config_rflood_rc_settings_custom`{ .sb-show-on-unchecked }`rflood2_config_rflood_rc_settings_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_config_rflood_rc_settings_custom:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_config_rflood_rc_settings_custom:
        ```

    ??? variable string "`rflood_role_config_rflood_rc_settings_default`{ .sb-show-on-unchecked }`rflood2_config_rflood_rc_settings_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_config_rflood_rc_settings_default:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_config_rflood_rc_settings_default:
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

    ??? variable string "`rflood_role_docker_image_repo`{ .sb-show-on-unchecked }`rflood2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_image_repo:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_image_repo:
        ```

    ??? variable string "`rflood_role_docker_image_tag`{ .sb-show-on-unchecked }`rflood2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_docker_image_tag:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_docker_image_tag:
        ```

    ??? variable string "`rflood_role_docker_ports_50000`{ .sb-show-on-unchecked }`rflood2_docker_ports_50000`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        rflood_role_docker_ports_50000:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        rflood2_docker_ports_50000:
        ```

    ??? variable string "`rflood_role_docker_ports_6881`{ .sb-show-on-unchecked }`rflood2_docker_ports_6881`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        rflood_role_docker_ports_6881:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        rflood2_docker_ports_6881:
        ```

    ??? variable bool "`rflood_role_docker_volumes_download`{ .sb-show-on-unchecked }`rflood2_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rflood_role_docker_volumes_download:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rflood2_docker_volumes_download:
        ```

    ??? variable string "`rflood_role_paths_location`{ .sb-show-on-unchecked }`rflood2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_paths_location:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_paths_location:
        ```

    ??? variable string "`rflood_role_themepark_addons`{ .sb-show-on-unchecked }`rflood2_themepark_addons`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_themepark_addons:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_themepark_addons:
        ```

    ??? variable string "`rflood_role_themepark_app`{ .sb-show-on-unchecked }`rflood2_themepark_app`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_themepark_app:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_themepark_app:
        ```

    ??? variable string "`rflood_role_themepark_theme`{ .sb-show-on-unchecked }`rflood2_themepark_theme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_themepark_theme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_themepark_theme:
        ```

    ??? variable dict "`rflood_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`rflood2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        rflood_role_traefik_api_endpoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        rflood2_traefik_api_endpoint:
        ```

    ??? variable string "`rflood_role_traefik_api_middleware`{ .sb-show-on-unchecked }`rflood2_traefik_api_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_traefik_api_middleware:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_traefik_api_middleware:
        ```

    ??? variable string "`rflood_role_traefik_api_middleware_http`{ .sb-show-on-unchecked }`rflood2_traefik_api_middleware_http`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_traefik_api_middleware_http:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_traefik_api_middleware_http:
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

    ??? variable string "`rflood_role_traefik_certresolver`{ .sb-show-on-unchecked }`rflood2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_traefik_certresolver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_traefik_certresolver:
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

    ??? variable string "`rflood_role_traefik_middleware_http`{ .sb-show-on-unchecked }`rflood2_traefik_middleware_http`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_traefik_middleware_http:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_traefik_middleware_http:
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

    ??? variable string "`rflood_role_traefik_priority`{ .sb-show-on-unchecked }`rflood2_traefik_priority`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_traefik_priority:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_traefik_priority:
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

    ??? variable string "`rflood_role_web_domain`{ .sb-show-on-unchecked }`rflood2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_web_domain:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_web_domain:
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


    ??? variable string "`rflood_role_web_http_port`{ .sb-show-on-unchecked }`rflood2_web_http_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        rflood_role_web_http_port:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        rflood2_web_http_port:
        ```

    ??? variable string "`rflood_role_web_http_scheme`{ .sb-show-on-unchecked }`rflood2_web_http_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string ("http"/"https")
        rflood_role_web_http_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string ("http"/"https")
        rflood2_web_http_scheme:
        ```

    ??? variable dict "`rflood_role_web_http_serverstransport`{ .sb-show-on-unchecked }`rflood2_web_http_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        rflood_role_web_http_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        rflood2_web_http_serverstransport:
        ```

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

    ??? variable dict "`rflood_role_web_serverstransport`{ .sb-show-on-unchecked }`rflood2_web_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        rflood_role_web_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        rflood2_web_serverstransport:
        ```

    ??? variable string "`rflood_role_web_subdomain`{ .sb-show-on-unchecked }`rflood2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rflood_role_web_subdomain:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rflood2_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
icon: material/docker
title: ruTorrent
hide:
  - tags
tags:
  - bittorrent
  - p2p
  - rutorrent
  - torrent
saltbox_automation:
  app_links:
    - name: Manual
      url: https://github.com/Novik/ruTorrent/wiki
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/kudeta/ru-rtorrent/tags
      type: docker
    - name: Community
      url: https://github.com/Novik/ruTorrent/discussions
      type: github
  project_description:
    name: ruTorrent
    summary: |-
      a front-end for the popular, lightweight, and extensible BitTorrent client rTorrent.
    link: https://github.com/Novik/ruTorrent
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# ruTorrent

## Overview

[ruTorrent](https://github.com/Novik/ruTorrent) is a front-end for the popular, lightweight, and extensible BitTorrent client rTorrent.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/Novik/ruTorrent/wiki){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/kudeta/ru-rtorrent/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Community**](https://github.com/Novik/ruTorrent/discussions){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-rutorrent
```

## Usage

Visit <https://rutorrent.iYOUR_DOMAIN_NAMEi>.

### Unpacking

You will most likely want to run [Unpackerr](../../apps/unpackerr.md) for this purpose. If so, it is recommended to disable ruTorrent's *unpack* plugin (along with other plugins you do not require) to save resources.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        rutorrent_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `rutorrent_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `rutorrent_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`rutorrent_name`"

        ```yaml
        # Type: string
        rutorrent_name: rutorrent
        ```

=== "Web"

    ??? variable string "`rutorrent_role_web_subdomain`"

        ```yaml
        # Type: string
        rutorrent_role_web_subdomain: "{{ rutorrent_name }}"
        ```

    ??? variable string "`rutorrent_role_web_domain`"

        ```yaml
        # Type: string
        rutorrent_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`rutorrent_role_web_port`"

        ```yaml
        # Type: string
        rutorrent_role_web_port: "80"
        ```

    ??? variable string "`rutorrent_role_web_url`"

        ```yaml
        # Type: string
        rutorrent_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='rutorrent') + '.' + lookup('role_var', '_web_domain', role='rutorrent')
                                 if (lookup('role_var', '_web_subdomain', role='rutorrent') | length > 0)
                                 else lookup('role_var', '_web_domain', role='rutorrent')) }}"
        ```

=== "DNS"

    ??? variable string "`rutorrent_role_dns_record`"

        ```yaml
        # Type: string
        rutorrent_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='rutorrent') }}"
        ```

    ??? variable string "`rutorrent_role_dns_zone`"

        ```yaml
        # Type: string
        rutorrent_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='rutorrent') }}"
        ```

    ??? variable bool "`rutorrent_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`rutorrent_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        rutorrent_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`rutorrent_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        rutorrent_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                       + (',themepark-' + rutorrent_name
                                                         if (lookup('role_var', '_themepark_enabled', role='rutorrent') and global_themepark_plugin_enabled)
                                                         else '') }}"
        ```

    ??? variable string "`rutorrent_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        rutorrent_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`rutorrent_role_traefik_certresolver`"

        ```yaml
        # Type: string
        rutorrent_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`rutorrent_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_traefik_enabled: true
        ```

    ??? variable bool "`rutorrent_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_traefik_api_enabled: true
        ```

    ??? variable string "`rutorrent_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        rutorrent_role_traefik_api_middleware: "rutorrent-auth,{{ traefik_default_middleware_api }}"
        ```

    ??? variable string "`rutorrent_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        rutorrent_role_traefik_api_endpoint: "PathPrefix(`/RPC2`)"
        ```

=== "Config"

    ??? variable bool "`rutorrent_role_config_public_trackers`"

        ```yaml
        # Toggles if public tracker functionality is enabled
        # Type: bool (true/false)
        rutorrent_role_config_public_trackers: false
        ```

    ??? variable string "`rutorrent_role_config_diskspace_path`"

        ```yaml
        # Path used by the diskspace plugin to check usage
        # Type: string
        rutorrent_role_config_diskspace_path: "/mnt"
        ```

    ??? variable string "`rutorrent_role_config_new_installs_rutorrent_rc_settings_default`"

        ```yaml
        # # New Installs
        # rtorrent.rc
        # Type: string
        rutorrent_role_config_new_installs_rutorrent_rc_settings_default:
          # Minimum number of peers to connect to per torrent
          - { option: "throttle.min_peers.normal.set", value: "1" }
          # Maximum number of simultaneous upload slots per torrent
          - { option: "throttle.max_uploads.set", value: "1024" }
          # Maximum number of simultaneous download slots, globally
          - { option: "throttle.max_downloads.global.set", value: "1024" }
          # Maximum number of simultaneous upload slots, globally
          - { option: "throttle.max_uploads.global.set", value: "1024" }
          # Maximum download rate, globally (KiB); 0 = unlimited
          - { option: "throttle.global_down.max_rate.set_kb", value: "0" }
          # Maximum upload rate, globally (KiB); 0 = unlimited
          - { option: "throttle.global_up.max_rate.set_kb", value: "0" }
          # Maximum number of open files
          - { option: "network.max_open_files.set", value: "1024" }
          # Maximum XMLRPC payloads
          - { option: "network.xmlrpc.size_limit.set", value: "20M" }
          # Encryption Parameters
          - { option: "protocol.encryption.set", value: "allow_incoming,try_outgoing,enable_retry,prefer_plaintext" }
          # Hash check on completion - disabled
          - { option: "pieces.hash.on_completion.set", value: "no" }
          # Disk space allocation - disabled
          - { option: "system.file.allocate.set", value: "0" }
          # Download Directory
          - { option: "directory.default.set", value: "/mnt/unionfs/downloads/torrents/rutorrent/completed" }
          # Watched Directory
          - { option: "schedule", value: 'watch_directory,5,5,"load.start=/mnt/unionfs/downloads/torrents/rutorrent/watched/*.torrent,d.delete_tied="' }
        ```

    ??? variable list "`rutorrent_role_config_new_installs_rutorrent_rc_settings_custom`"

        ```yaml
        # Type: list
        rutorrent_role_config_new_installs_rutorrent_rc_settings_custom: []
        ```

    ??? variable string "`rutorrent_role_config_new_installs_rutorrent_rc_settings_list`"

        ```yaml
        # Type: string
        rutorrent_role_config_new_installs_rutorrent_rc_settings_list: "{{ lookup('role_var', '_config_new_installs_rutorrent_rc_settings_default', role='rutorrent')
                                                                           + lookup('role_var', '_config_new_installs_rutorrent_rc_settings_custom', role='rutorrent') }}"
        ```

    ??? variable string "`rutorrent_role_config_new_installs_php_local_ini_settings_default`"

        ```yaml
        # php-local.ini
        # Type: string
        rutorrent_role_config_new_installs_php_local_ini_settings_default:
          # Maximum Upload File Size via Web Browser (eg Uploading Torrent Files)
          - { option: "upload_max_filesize", value: "20M" }
        ```

    ??? variable list "`rutorrent_role_config_new_installs_php_local_ini_settings_custom`"

        ```yaml
        # Type: list
        rutorrent_role_config_new_installs_php_local_ini_settings_custom: []
        ```

    ??? variable string "`rutorrent_role_config_new_installs_php_local_ini_settings_list`"

        ```yaml
        # Type: string
        rutorrent_role_config_new_installs_php_local_ini_settings_list: "{{ lookup('role_var', '_config_new_installs_php_local_ini_settings_default', role='rutorrent')
                                                                            + lookup('role_var', '_config_new_installs_php_local_ini_settings_custom', role='rutorrent') }}"
        ```

    ??? variable string "`rutorrent_role_config_existing_installs_rutorrent_rc_settings_default`"

        ```yaml
        # # Existing Installs
        # rtorrent.rc
        # Type: string
        rutorrent_role_config_existing_installs_rutorrent_rc_settings_default:
          # Execute - Initiate Plugins
          - { option: "execute", value: "{sh,-c,/usr/bin/php /app/rutorrent/php/initplugins.php abc &}" }
          # IP address that is reported to the tracker
          - { option: "network.local_address.set", value: "{{ ip_address_public }}" }
          # Ports
          - { option: "network.port_range.set", value: "{{ rutorrent_role_docker_ports_51413 }}-{{ rutorrent_role_docker_ports_51413 }}" }
          - { option: "dht.port.set", value: "{{ rutorrent_role_docker_ports_6881 }}" }
          # Enable / Disable Public Trackers
          - { option: "dht.mode.set", value: "{{ lookup('role_var', '_config_public_trackers', role='rutorrent') | ternary('on', 'disable') }}" }
          - { option: "trackers.use_udp.set", value: "{{ lookup('role_var', '_config_public_trackers', role='rutorrent') | ternary('yes', 'no') }}" }
          - { option: "protocol.pex.set", value: "{{ lookup('role_var', '_config_public_trackers', role='rutorrent') | ternary('yes', 'no') }}" }
        ```

    ??? variable list "`rutorrent_role_config_existing_installs_rutorrent_rc_settings_custom`"

        ```yaml
        # Type: list
        rutorrent_role_config_existing_installs_rutorrent_rc_settings_custom: []
        ```

    ??? variable string "`rutorrent_role_config_existing_installs_rutorrent_rc_settings_list`"

        ```yaml
        # Type: string
        rutorrent_role_config_existing_installs_rutorrent_rc_settings_list: "{{ lookup('role_var', '_config_existing_installs_rutorrent_rc_settings_default', role='rutorrent')
                                                                                + lookup('role_var', '_config_existing_installs_rutorrent_rc_settings_custom', role='rutorrent') }}"
        ```

=== "Theme"

    ??? variable bool "`rutorrent_role_themepark_enabled`"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        rutorrent_role_themepark_enabled: false
        ```

    ??? variable string "`rutorrent_role_themepark_app`"

        ```yaml
        # Type: string
        rutorrent_role_themepark_app: "rutorrent"
        ```

    ??? variable string "`rutorrent_role_themepark_theme`"

        ```yaml
        # Type: string
        rutorrent_role_themepark_theme: "{{ global_themepark_theme }}"
        ```

    ??? variable string "`rutorrent_role_themepark_domain`"

        ```yaml
        # Type: string
        rutorrent_role_themepark_domain: "{{ global_themepark_domain }}"
        ```

    ??? variable list "`rutorrent_role_themepark_addons`"

        ```yaml
        # Type: list
        rutorrent_role_themepark_addons: []
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`rutorrent_role_docker_container`"

        ```yaml
        # Type: string
        rutorrent_role_docker_container: "{{ rutorrent_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`rutorrent_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_docker_image_pull: true
        ```

    ??? variable string "`rutorrent_role_docker_image_tag`"

        ```yaml
        # Type: string
        rutorrent_role_docker_image_tag: "latest"
        ```

    ??? variable string "`rutorrent_role_docker_image_repo`"

        ```yaml
        # Type: string
        rutorrent_role_docker_image_repo: "kudeta/ru-rtorrent"
        ```

    ??? variable string "`rutorrent_role_docker_image`"

        ```yaml
        # Type: string
        rutorrent_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='rutorrent') }}:{{ lookup('role_var', '_docker_image_tag', role='rutorrent') }}"
        ```

    <h5>Ports</h5>

    ??? variable string "`rutorrent_role_docker_ports_51413`"

        ```yaml
        # Type: string
        rutorrent_role_docker_ports_51413: "{{ port_lookup_51413.meta.port
                                            if (port_lookup_51413.meta.port is defined) and (port_lookup_51413.meta.port | trim | length > 0)
                                            else '51413' }}"
        ```

    ??? variable string "`rutorrent_role_docker_ports_6881`"

        ```yaml
        # Type: string
        rutorrent_role_docker_ports_6881: "{{ port_lookup_6881.meta.port
                                           if (port_lookup_6881.meta.port is defined) and (port_lookup_6881.meta.port | trim | length > 0)
                                           else '6881' }}"
        ```

    ??? variable list "`rutorrent_role_docker_ports_default`"

        ```yaml
        # Type: list
        rutorrent_role_docker_ports_default:
          - "{{ lookup('role_var', '_docker_ports_51413', role='rutorrent') }}:{{ lookup('role_var', '_docker_ports_51413', role='rutorrent') }}"
          - "{{ lookup('role_var', '_docker_ports_51413', role='rutorrent') }}:{{ lookup('role_var', '_docker_ports_51413', role='rutorrent') }}/udp"
          - "{{ lookup('role_var', '_docker_ports_6881', role='rutorrent') }}:{{ lookup('role_var', '_docker_ports_6881', role='rutorrent') }}/udp"
        ```

    ??? variable list "`rutorrent_role_docker_ports_custom`"

        ```yaml
        # Type: list
        rutorrent_role_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    ??? variable dict "`rutorrent_role_docker_envs_default`"

        ```yaml
        # Type: dict
        rutorrent_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`rutorrent_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        rutorrent_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`rutorrent_role_docker_volumes_default`"

        ```yaml
        # Type: list
        rutorrent_role_docker_volumes_default:
          - "{{ rutorrent_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
        ```

    ??? variable list "`rutorrent_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        rutorrent_role_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable dict "`rutorrent_role_docker_labels_default`"

        ```yaml
        # Type: dict
        rutorrent_role_docker_labels_default:
          traefik.http.middlewares.rutorrent-auth.basicauth.usersfile: "/etc/traefik/auth"
        ```

    ??? variable dict "`rutorrent_role_docker_labels_custom`"

        ```yaml
        # Type: dict
        rutorrent_role_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`rutorrent_role_docker_hostname`"

        ```yaml
        # Type: string
        rutorrent_role_docker_hostname: "{{ rutorrent_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`rutorrent_role_docker_networks_alias`"

        ```yaml
        # Type: string
        rutorrent_role_docker_networks_alias: "{{ rutorrent_name }}"
        ```

    ??? variable list "`rutorrent_role_docker_networks_default`"

        ```yaml
        # Type: list
        rutorrent_role_docker_networks_default: []
        ```

    ??? variable list "`rutorrent_role_docker_networks_custom`"

        ```yaml
        # Type: list
        rutorrent_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`rutorrent_role_docker_restart_policy`"

        ```yaml
        # Type: string
        rutorrent_role_docker_restart_policy: unless-stopped
        ```

    <h5>Stop Timeout</h5>

    ??? variable int "`rutorrent_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        rutorrent_role_docker_stop_timeout: 900
        ```

    <h5>State</h5>

    ??? variable string "`rutorrent_role_docker_state`"

        ```yaml
        # Type: string
        rutorrent_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`rutorrent_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        rutorrent_role_docker_blkio_weight:
        ```

    ??? variable int "`rutorrent_role_docker_cpu_period`"

        ```yaml
        # Type: int
        rutorrent_role_docker_cpu_period:
        ```

    ??? variable int "`rutorrent_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        rutorrent_role_docker_cpu_quota:
        ```

    ??? variable int "`rutorrent_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        rutorrent_role_docker_cpu_shares:
        ```

    ??? variable string "`rutorrent_role_docker_cpus`"

        ```yaml
        # Type: string
        rutorrent_role_docker_cpus:
        ```

    ??? variable string "`rutorrent_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        rutorrent_role_docker_cpuset_cpus:
        ```

    ??? variable string "`rutorrent_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        rutorrent_role_docker_cpuset_mems:
        ```

    ??? variable string "`rutorrent_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        rutorrent_role_docker_kernel_memory:
        ```

    ??? variable string "`rutorrent_role_docker_memory`"

        ```yaml
        # Type: string
        rutorrent_role_docker_memory:
        ```

    ??? variable string "`rutorrent_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        rutorrent_role_docker_memory_reservation:
        ```

    ??? variable string "`rutorrent_role_docker_memory_swap`"

        ```yaml
        # Type: string
        rutorrent_role_docker_memory_swap:
        ```

    ??? variable int "`rutorrent_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        rutorrent_role_docker_memory_swappiness:
        ```

    ??? variable string "`rutorrent_role_docker_shm_size`"

        ```yaml
        # Type: string
        rutorrent_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`rutorrent_role_docker_cap_drop`"

        ```yaml
        # Type: list
        rutorrent_role_docker_cap_drop:
        ```

    ??? variable string "`rutorrent_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        rutorrent_role_docker_cgroupns_mode:
        ```

    ??? variable list "`rutorrent_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        rutorrent_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`rutorrent_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        rutorrent_role_docker_device_read_bps:
        ```

    ??? variable list "`rutorrent_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        rutorrent_role_docker_device_read_iops:
        ```

    ??? variable list "`rutorrent_role_docker_device_requests`"

        ```yaml
        # Type: list
        rutorrent_role_docker_device_requests:
        ```

    ??? variable list "`rutorrent_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        rutorrent_role_docker_device_write_bps:
        ```

    ??? variable list "`rutorrent_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        rutorrent_role_docker_device_write_iops:
        ```

    ??? variable list "`rutorrent_role_docker_devices`"

        ```yaml
        # Type: list
        rutorrent_role_docker_devices:
        ```

    ??? variable list "`rutorrent_role_docker_groups`"

        ```yaml
        # Type: list
        rutorrent_role_docker_groups:
        ```

    ??? variable bool "`rutorrent_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_docker_privileged:
        ```

    ??? variable list "`rutorrent_role_docker_security_opts`"

        ```yaml
        # Type: list
        rutorrent_role_docker_security_opts:
        ```

    ??? variable string "`rutorrent_role_docker_user`"

        ```yaml
        # Type: string
        rutorrent_role_docker_user:
        ```

    ??? variable string "`rutorrent_role_docker_userns_mode`"

        ```yaml
        # Type: string
        rutorrent_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`rutorrent_role_docker_dns_opts`"

        ```yaml
        # Type: list
        rutorrent_role_docker_dns_opts:
        ```

    ??? variable list "`rutorrent_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        rutorrent_role_docker_dns_search_domains:
        ```

    ??? variable list "`rutorrent_role_docker_dns_servers`"

        ```yaml
        # Type: list
        rutorrent_role_docker_dns_servers:
        ```

    ??? variable string "`rutorrent_role_docker_domainname`"

        ```yaml
        # Type: string
        rutorrent_role_docker_domainname:
        ```

    ??? variable list "`rutorrent_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        rutorrent_role_docker_exposed_ports:
        ```

    ??? variable dict "`rutorrent_role_docker_hosts`"

        ```yaml
        # Type: dict
        rutorrent_role_docker_hosts:
        ```

    ??? variable bool "`rutorrent_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_docker_hosts_use_common:
        ```

    ??? variable string "`rutorrent_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        rutorrent_role_docker_ipc_mode:
        ```

    ??? variable list "`rutorrent_role_docker_links`"

        ```yaml
        # Type: list
        rutorrent_role_docker_links:
        ```

    ??? variable string "`rutorrent_role_docker_network_mode`"

        ```yaml
        # Type: string
        rutorrent_role_docker_network_mode:
        ```

    ??? variable string "`rutorrent_role_docker_pid_mode`"

        ```yaml
        # Type: string
        rutorrent_role_docker_pid_mode:
        ```

    ??? variable string "`rutorrent_role_docker_uts`"

        ```yaml
        # Type: string
        rutorrent_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`rutorrent_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_docker_keep_volumes:
        ```

    ??? variable list "`rutorrent_role_docker_mounts`"

        ```yaml
        # Type: list
        rutorrent_role_docker_mounts:
        ```

    ??? variable dict "`rutorrent_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        rutorrent_role_docker_storage_opts:
        ```

    ??? variable list "`rutorrent_role_docker_tmpfs`"

        ```yaml
        # Type: list
        rutorrent_role_docker_tmpfs:
        ```

    ??? variable string "`rutorrent_role_docker_volume_driver`"

        ```yaml
        # Type: string
        rutorrent_role_docker_volume_driver:
        ```

    ??? variable list "`rutorrent_role_docker_volumes_from`"

        ```yaml
        # Type: list
        rutorrent_role_docker_volumes_from:
        ```

    ??? variable bool "`rutorrent_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_docker_volumes_global:
        ```

    ??? variable string "`rutorrent_role_docker_working_dir`"

        ```yaml
        # Type: string
        rutorrent_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`rutorrent_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_docker_auto_remove:
        ```

    ??? variable bool "`rutorrent_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_docker_cleanup:
        ```

    ??? variable string "`rutorrent_role_docker_force_kill`"

        ```yaml
        # Type: string
        rutorrent_role_docker_force_kill:
        ```

    ??? variable dict "`rutorrent_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        rutorrent_role_docker_healthcheck:
        ```

    ??? variable int "`rutorrent_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        rutorrent_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`rutorrent_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_docker_init:
        ```

    ??? variable string "`rutorrent_role_docker_kill_signal`"

        ```yaml
        # Type: string
        rutorrent_role_docker_kill_signal:
        ```

    ??? variable string "`rutorrent_role_docker_log_driver`"

        ```yaml
        # Type: string
        rutorrent_role_docker_log_driver:
        ```

    ??? variable dict "`rutorrent_role_docker_log_options`"

        ```yaml
        # Type: dict
        rutorrent_role_docker_log_options:
        ```

    ??? variable bool "`rutorrent_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_docker_oom_killer:
        ```

    ??? variable int "`rutorrent_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        rutorrent_role_docker_oom_score_adj:
        ```

    ??? variable bool "`rutorrent_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_docker_output_logs:
        ```

    ??? variable bool "`rutorrent_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_docker_paused:
        ```

    ??? variable bool "`rutorrent_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_docker_recreate:
        ```

    ??? variable int "`rutorrent_role_docker_restart_retries`"

        ```yaml
        # Type: int
        rutorrent_role_docker_restart_retries:
        ```

    ??? variable string "`rutorrent_role_docker_stop_signal`"

        ```yaml
        # Type: string
        rutorrent_role_docker_stop_signal:
        ```

    <h5>Other Options</h5>

    ??? variable list "`rutorrent_role_docker_capabilities`"

        ```yaml
        # Type: list
        rutorrent_role_docker_capabilities:
        ```

    ??? variable string "`rutorrent_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        rutorrent_role_docker_cgroup_parent:
        ```

    ??? variable list "`rutorrent_role_docker_commands`"

        ```yaml
        # Type: list
        rutorrent_role_docker_commands:
        ```

    ??? variable int "`rutorrent_role_docker_create_timeout`"

        ```yaml
        # Type: int
        rutorrent_role_docker_create_timeout:
        ```

    ??? variable string "`rutorrent_role_docker_entrypoint`"

        ```yaml
        # Type: string
        rutorrent_role_docker_entrypoint:
        ```

    ??? variable string "`rutorrent_role_docker_env_file`"

        ```yaml
        # Type: string
        rutorrent_role_docker_env_file:
        ```

    ??? variable bool "`rutorrent_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_docker_labels_use_common:
        ```

    ??? variable bool "`rutorrent_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_docker_read_only:
        ```

    ??? variable string "`rutorrent_role_docker_runtime`"

        ```yaml
        # Type: string
        rutorrent_role_docker_runtime:
        ```

    ??? variable list "`rutorrent_role_docker_sysctls`"

        ```yaml
        # Type: list
        rutorrent_role_docker_sysctls:
        ```

    ??? variable list "`rutorrent_role_docker_ulimits`"

        ```yaml
        # Type: list
        rutorrent_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`rutorrent_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        rutorrent_role_autoheal_enabled: true
        ```

    ??? variable string "`rutorrent_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        rutorrent_role_depends_on: ""
        ```

    ??? variable string "`rutorrent_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        rutorrent_role_depends_on_delay: "0"
        ```

    ??? variable string "`rutorrent_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        rutorrent_role_depends_on_healthchecks:
        ```

    ??? variable bool "`rutorrent_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        rutorrent_role_diun_enabled: true
        ```

    ??? variable bool "`rutorrent_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        rutorrent_role_dns_enabled: true
        ```

    ??? variable bool "`rutorrent_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        rutorrent_role_docker_controller: true
        ```

    ??? variable list "`rutorrent_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        rutorrent_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`rutorrent_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_docker_volumes_download:
        ```

    ??? variable string "`rutorrent_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        rutorrent_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`rutorrent_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        rutorrent_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`rutorrent_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        rutorrent_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`rutorrent_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        rutorrent_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`rutorrent_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        rutorrent_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`rutorrent_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        rutorrent_role_traefik_middleware_http:
        ```

    ??? variable bool "`rutorrent_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`rutorrent_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        rutorrent_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`rutorrent_role_traefik_priority`"

        ```yaml
        # Type: string
        rutorrent_role_traefik_priority:
        ```

    ??? variable bool "`rutorrent_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        rutorrent_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`rutorrent_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        rutorrent_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`rutorrent_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        rutorrent_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`rutorrent_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        rutorrent_role_web_api_http_port:
        ```

    ??? variable string "`rutorrent_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        rutorrent_role_web_api_http_scheme:
        ```

    ??? variable dict "`rutorrent_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        rutorrent_role_web_api_http_serverstransport:
        ```

    ??? variable string "`rutorrent_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        rutorrent_role_web_api_port:
        ```

    ??? variable string "`rutorrent_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        rutorrent_role_web_api_scheme:
        ```

    ??? variable dict "`rutorrent_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        rutorrent_role_web_api_serverstransport:
        ```

    ??? variable list "`rutorrent_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        rutorrent_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            rutorrent_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "rutorrent2.{{ user.domain }}"
              - "rutorrent.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`rutorrent_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        rutorrent_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            rutorrent_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'rutorrent2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`rutorrent_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        rutorrent_role_web_http_port:
        ```

    ??? variable string "`rutorrent_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        rutorrent_role_web_http_scheme:
        ```

    ??? variable dict "`rutorrent_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        rutorrent_role_web_http_serverstransport:
        ```

    ??? variable string "`rutorrent_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        rutorrent_role_web_scheme:
        ```

    ??? variable dict "`rutorrent_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        rutorrent_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

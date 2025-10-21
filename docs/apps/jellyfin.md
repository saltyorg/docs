---
hide:
  - tags
tags:
  - jellyfin
---

# Jellyfin

## What is it?

[Jellyfin](https://jellyfin.org/) is the volunteer-built media solution that puts you in control of your media. Stream to any device from your own server, with no strings attached. Your media, your server, your way.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://jellyfin.org/){: .header-icons } | [:octicons-link-16: Docs](https://docs.jellyfin.org/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/jellyfin/jellyfin){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/jellyfin){: .header-icons }|

### 1. Installation

``` shell

sb install jellyfin

```

### 2. URL

- To access Jellyfin, visit `https://jellyfin._yourdomain.com_`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `jellyfin_instances`.

    === "Role-level Override"

        Applies to all instances of jellyfin:

        ```yaml
        jellyfin_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `jellyfin2`):

        ```yaml
        jellyfin2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `jellyfin_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `jellyfin_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`jellyfin_instances`"

        ```yaml
        # Type: list
        jellyfin_instances: ["jellyfin"]
        ```

        !!! example

            ```yaml
            # Type: list
            jellyfin_instances: ["jellyfin", "jellyfin2"]
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`jellyfin_role_paths_folder`"

            ```yaml
            # Type: string
            jellyfin_role_paths_folder: "{{ jellyfin_name }}"
            ```

        ??? variable string "`jellyfin_role_paths_location`"

            ```yaml
            # Type: string
            jellyfin_role_paths_location: "{{ server_appdata_path }}/{{ jellyfin_role_paths_folder }}"
            ```

        ??? variable string "`jellyfin_role_paths_transcodes_location`"

            ```yaml
            # Type: string
            jellyfin_role_paths_transcodes_location: "{{ transcodes_path }}/{{ jellyfin_role_paths_folder }}"
            ```

        ??? variable string "`jellyfin_role_paths_dlna_location`"

            ```yaml
            # Type: string
            jellyfin_role_paths_dlna_location: "{{ jellyfin_role_paths_location }}/dlna.xml"
            ```

        ??? variable string "`jellyfin_role_paths_sys_xml_location`"

            ```yaml
            # Type: string
            jellyfin_role_paths_sys_xml_location: "{{ jellyfin_role_paths_location }}/system.xml"
            ```

        ??? variable string "`jellyfin_role_paths_net_xml_location`"

            ```yaml
            # Type: string
            jellyfin_role_paths_net_xml_location: "{{ jellyfin_role_paths_location }}/network.xml"
            ```

        ??? variable string "`jellyfin_role_paths_xml_location_old`"

            ```yaml
            # Type: string
            jellyfin_role_paths_xml_location_old: "{{ jellyfin_role_paths_location }}/app/config/system.xml"
            ```

    === "Instance-level"

        ??? variable string "`jellyfin2_paths_folder`"

            ```yaml
            # Type: string
            jellyfin2_paths_folder: "{{ jellyfin_name }}"
            ```

        ??? variable string "`jellyfin2_paths_location`"

            ```yaml
            # Type: string
            jellyfin2_paths_location: "{{ server_appdata_path }}/{{ jellyfin_role_paths_folder }}"
            ```

        ??? variable string "`jellyfin2_paths_transcodes_location`"

            ```yaml
            # Type: string
            jellyfin2_paths_transcodes_location: "{{ transcodes_path }}/{{ jellyfin_role_paths_folder }}"
            ```

        ??? variable string "`jellyfin2_paths_dlna_location`"

            ```yaml
            # Type: string
            jellyfin2_paths_dlna_location: "{{ jellyfin_role_paths_location }}/dlna.xml"
            ```

        ??? variable string "`jellyfin2_paths_sys_xml_location`"

            ```yaml
            # Type: string
            jellyfin2_paths_sys_xml_location: "{{ jellyfin_role_paths_location }}/system.xml"
            ```

        ??? variable string "`jellyfin2_paths_net_xml_location`"

            ```yaml
            # Type: string
            jellyfin2_paths_net_xml_location: "{{ jellyfin_role_paths_location }}/network.xml"
            ```

        ??? variable string "`jellyfin2_paths_xml_location_old`"

            ```yaml
            # Type: string
            jellyfin2_paths_xml_location_old: "{{ jellyfin_role_paths_location }}/app/config/system.xml"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`jellyfin_role_web_subdomain`"

            ```yaml
            # Type: string
            jellyfin_role_web_subdomain: "{{ jellyfin_name }}"
            ```

        ??? variable string "`jellyfin_role_web_domain`"

            ```yaml
            # Type: string
            jellyfin_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`jellyfin_role_web_port`"

            ```yaml
            # Type: string
            jellyfin_role_web_port: "8096"
            ```

        ??? variable string "`jellyfin_role_web_url`"

            ```yaml
            # Type: string
            jellyfin_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='jellyfin') + '.' + lookup('role_var', '_web_domain', role='jellyfin')
                                    if (lookup('role_var', '_web_subdomain', role='jellyfin') | length > 0)
                                    else lookup('role_var', '_web_domain', role='jellyfin')) }}"
            ```

    === "Instance-level"

        ??? variable string "`jellyfin2_web_subdomain`"

            ```yaml
            # Type: string
            jellyfin2_web_subdomain: "{{ jellyfin_name }}"
            ```

        ??? variable string "`jellyfin2_web_domain`"

            ```yaml
            # Type: string
            jellyfin2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`jellyfin2_web_port`"

            ```yaml
            # Type: string
            jellyfin2_web_port: "8096"
            ```

        ??? variable string "`jellyfin2_web_url`"

            ```yaml
            # Type: string
                    jellyfin2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='jellyfin') + '.' + lookup('role_var', '_web_domain', role='jellyfin')
                                        if (lookup('role_var', '_web_subdomain', role='jellyfin') | length > 0)
                                        else lookup('role_var', '_web_domain', role='jellyfin')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`jellyfin_role_dns_record`"

            ```yaml
            # Type: string
            jellyfin_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='jellyfin') }}"
            ```

        ??? variable string "`jellyfin_role_dns_zone`"

            ```yaml
            # Type: string
            jellyfin_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='jellyfin') }}"
            ```

        ??? variable bool "`jellyfin_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            jellyfin_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`jellyfin2_dns_record`"

            ```yaml
            # Type: string
            jellyfin2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='jellyfin') }}"
            ```

        ??? variable string "`jellyfin2_dns_zone`"

            ```yaml
            # Type: string
            jellyfin2_dns_zone: "{{ lookup('role_var', '_web_domain', role='jellyfin') }}"
            ```

        ??? variable bool "`jellyfin2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            jellyfin2_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`jellyfin_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            jellyfin_role_traefik_sso_middleware: ""
            ```

        ??? variable string "`jellyfin_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            jellyfin_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`jellyfin_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            jellyfin_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`jellyfin_role_traefik_certresolver`"

            ```yaml
            # Type: string
            jellyfin_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`jellyfin_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            jellyfin_role_traefik_enabled: true
            ```

        ??? variable bool "`jellyfin_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            jellyfin_role_traefik_api_enabled: false
            ```

        ??? variable string "`jellyfin_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            jellyfin_role_traefik_api_endpoint: ""
            ```

        ??? variable bool "`jellyfin_role_traefik_gzip_enabled`"

            ```yaml
            # Type: bool (true/false)
            jellyfin_role_traefik_gzip_enabled: false
            ```

    === "Instance-level"

        ??? variable string "`jellyfin2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            jellyfin2_traefik_sso_middleware: ""
            ```

        ??? variable string "`jellyfin2_traefik_middleware_default`"

            ```yaml
            # Type: string
            jellyfin2_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`jellyfin2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            jellyfin2_traefik_middleware_custom: ""
            ```

        ??? variable string "`jellyfin2_traefik_certresolver`"

            ```yaml
            # Type: string
            jellyfin2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`jellyfin2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            jellyfin2_traefik_enabled: true
            ```

        ??? variable bool "`jellyfin2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            jellyfin2_traefik_api_enabled: false
            ```

        ??? variable string "`jellyfin2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            jellyfin2_traefik_api_endpoint: ""
            ```

        ??? variable bool "`jellyfin2_traefik_gzip_enabled`"

            ```yaml
            # Type: bool (true/false)
            jellyfin2_traefik_gzip_enabled: false
            ```

=== "Config"

    === "Role-level"

        ??? variable list "`jellyfin_role_system_settings_default`"

            ```yaml
            # System
            # Type: list
            jellyfin_role_system_settings_default: 
              - { xpath: 'PublicPort', value: '80' }
              - { xpath: 'PublicHttpsPort', value: '443' }
              - { xpath: 'EnableFolderView', value: 'true' }
              - { xpath: 'QuickConnectAvailable', value: 'true' }
              - { xpath: 'EnableRemoteAccess', value: 'true' }
              - { xpath: 'ServerName', value: 'saltbox' }
            ```

        ??? variable list "`jellyfin_role_system_settings_custom`"

            ```yaml
            # Type: list
            jellyfin_role_system_settings_custom: []
            ```

        ??? variable string "`jellyfin_role_system_settings_list`"

            ```yaml
            # Type: string
            jellyfin_role_system_settings_list: "{{ lookup('role_var', '_system_settings_default', role='jellyfin') + lookup('role_var', '_system_settings_custom', role='jellyfin') }}"
            ```

        ??? variable list "`jellyfin_role_network_settings_default`"

            ```yaml
            # Network
            # Type: list
            jellyfin_role_network_settings_default: 
              - { xpath: 'PublicPort', value: '80' }
              - { xpath: 'PublicHttpsPort', value: '443' }
              - { xpath: 'PublishedServerUriBySubnet/string', value: 'external={{ lookup("role_var", "_web_url", role="jellyfin") }}:443' }
            ```

        ??? variable list "`jellyfin_role_network_settings_custom`"

            ```yaml
            # Type: list
            jellyfin_role_network_settings_custom: []
            ```

        ??? variable string "`jellyfin_role_network_settings_list`"

            ```yaml
            # Type: string
            jellyfin_role_network_settings_list: "{{ lookup('role_var', '_network_settings_default', role='jellyfin') + lookup('role_var', '_network_settings_custom', role='jellyfin') }}"
            ```

    === "Instance-level"

        ??? variable list "`jellyfin2_system_settings_default`"

            # System

            ```yaml
            # Type: list
                    jellyfin2_system_settings_default: 
                      - { xpath: 'PublicPort', value: '80' }
                      - { xpath: 'PublicHttpsPort', value: '443' }
                      - { xpath: 'EnableFolderView', value: 'true' }
                      - { xpath: 'QuickConnectAvailable', value: 'true' }
                      - { xpath: 'EnableRemoteAccess', value: 'true' }
                      - { xpath: 'ServerName', value: 'saltbox' }
            ```

        ??? variable list "`jellyfin2_system_settings_custom`"

            ```yaml
            # Type: list
            jellyfin2_system_settings_custom: []
            ```

        ??? variable string "`jellyfin2_system_settings_list`"

            ```yaml
            # Type: string
            jellyfin2_system_settings_list: "{{ lookup('role_var', '_system_settings_default', role='jellyfin') + lookup('role_var', '_system_settings_custom', role='jellyfin') }}"
            ```

        ??? variable list "`jellyfin2_network_settings_default`"

            # Network

            ```yaml
            # Type: list
                    jellyfin2_network_settings_default: 
                      - { xpath: 'PublicPort', value: '80' }
                      - { xpath: 'PublicHttpsPort', value: '443' }
                      - { xpath: 'PublishedServerUriBySubnet/string', value: 'external={{ lookup("role_var", "_web_url", role="jellyfin") }}:443' }
            ```

        ??? variable list "`jellyfin2_network_settings_custom`"

            ```yaml
            # Type: list
            jellyfin2_network_settings_custom: []
            ```

        ??? variable string "`jellyfin2_network_settings_list`"

            ```yaml
            # Type: string
            jellyfin2_network_settings_list: "{{ lookup('role_var', '_network_settings_default', role='jellyfin') + lookup('role_var', '_network_settings_custom', role='jellyfin') }}"
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`jellyfin_role_docker_container`"

            ```yaml
            # Type: string
            jellyfin_role_docker_container: "{{ jellyfin_name }}"
            ```

        ##### Image

        ??? variable bool "`jellyfin_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            jellyfin_role_docker_image_pull: true
            ```

        ??? variable string "`jellyfin_role_docker_image_repo`"

            ```yaml
            # Type: string
            jellyfin_role_docker_image_repo: "ghcr.io/hotio/jellyfin"
            ```

        ??? variable string "`jellyfin_role_docker_image_tag`"

            ```yaml
            # Type: string
            jellyfin_role_docker_image_tag: "release"
            ```

        ??? variable string "`jellyfin_role_docker_image`"

            ```yaml
            # Type: string
            jellyfin_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='jellyfin') }}:{{ lookup('role_var', '_docker_image_tag', role='jellyfin') }}"
            ```

        ##### Envs

        ??? variable dict "`jellyfin_role_docker_envs_default`"

            ```yaml
            # Type: dict
            jellyfin_role_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              TZ: "{{ tz }}"
              DOTNET_USE_POLLING_FILE_WATCHER: "1"
            ```

        ??? variable dict "`jellyfin_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            jellyfin_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`jellyfin_role_docker_volumes_default`"

            ```yaml
            # Type: list
            jellyfin_role_docker_volumes_default: 
              - "{{ jellyfin_role_paths_location }}:/config:rw"
              - "{{ server_appdata_path }}/scripts:/scripts"
              - "/dev/shm:/dev/shm"
              - "{{ jellyfin_role_paths_transcodes_location }}:/transcode"
            ```

        ??? variable list "`jellyfin_role_docker_volumes_legacy`"

            ```yaml
            # Type: list
            jellyfin_role_docker_volumes_legacy: 
              - "/mnt/unionfs/Media:/data"
            ```

        ??? variable list "`jellyfin_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            jellyfin_role_docker_volumes_custom: []
            ```

        ##### Mounts

        ??? variable list "`jellyfin_role_docker_mounts_default`"

            ```yaml
            # Type: list
            jellyfin_role_docker_mounts_default: 
              - target: /tmp
                type: tmpfs
            ```

        ??? variable list "`jellyfin_role_docker_mounts_custom`"

            ```yaml
            # Type: list
            jellyfin_role_docker_mounts_custom: []
            ```

        ##### Hostname

        ??? variable string "`jellyfin_role_docker_hostname`"

            ```yaml
            # Type: string
            jellyfin_role_docker_hostname: "{{ jellyfin_name }}"
            ```

        ##### Networks

        ??? variable string "`jellyfin_role_docker_networks_alias`"

            ```yaml
            # Type: string
            jellyfin_role_docker_networks_alias: "{{ jellyfin_name }}"
            ```

        ??? variable list "`jellyfin_role_docker_networks_default`"

            ```yaml
            # Type: list
            jellyfin_role_docker_networks_default: []
            ```

        ??? variable list "`jellyfin_role_docker_networks_custom`"

            ```yaml
            # Type: list
            jellyfin_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`jellyfin_role_docker_restart_policy`"

            ```yaml
            # Type: string
            jellyfin_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`jellyfin_role_docker_state`"

            ```yaml
            # Type: string
            jellyfin_role_docker_state: started
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`jellyfin2_docker_container`"

            ```yaml
            # Type: string
            jellyfin2_docker_container: "{{ jellyfin_name }}"
            ```

        ##### Image

        ??? variable bool "`jellyfin2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            jellyfin2_docker_image_pull: true
            ```

        ??? variable string "`jellyfin2_docker_image_repo`"

            ```yaml
            # Type: string
            jellyfin2_docker_image_repo: "ghcr.io/hotio/jellyfin"
            ```

        ??? variable string "`jellyfin2_docker_image_tag`"

            ```yaml
            # Type: string
            jellyfin2_docker_image_tag: "release"
            ```

        ??? variable string "`jellyfin2_docker_image`"

            ```yaml
            # Type: string
            jellyfin2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='jellyfin') }}:{{ lookup('role_var', '_docker_image_tag', role='jellyfin') }}"
            ```

        ##### Envs

        ??? variable dict "`jellyfin2_docker_envs_default`"

            ```yaml
            # Type: dict
                    jellyfin2_docker_envs_default: 
                      PUID: "{{ uid }}"
                      PGID: "{{ gid }}"
                      TZ: "{{ tz }}"
                      DOTNET_USE_POLLING_FILE_WATCHER: "1"
            ```

        ??? variable dict "`jellyfin2_docker_envs_custom`"

            ```yaml
            # Type: dict
            jellyfin2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`jellyfin2_docker_volumes_default`"

            ```yaml
            # Type: list
                    jellyfin2_docker_volumes_default: 
                      - "{{ jellyfin_role_paths_location }}:/config:rw"
                      - "{{ server_appdata_path }}/scripts:/scripts"
                      - "/dev/shm:/dev/shm"
                      - "{{ jellyfin_role_paths_transcodes_location }}:/transcode"
            ```

        ??? variable list "`jellyfin2_docker_volumes_legacy`"

            ```yaml
            # Type: list
                    jellyfin2_docker_volumes_legacy: 
                      - "/mnt/unionfs/Media:/data"
            ```

        ??? variable list "`jellyfin2_docker_volumes_custom`"

            ```yaml
            # Type: list
            jellyfin2_docker_volumes_custom: []
            ```

        ##### Mounts

        ??? variable list "`jellyfin2_docker_mounts_default`"

            ```yaml
            # Type: list
                    jellyfin2_docker_mounts_default: 
                      - target: /tmp
                        type: tmpfs
            ```

        ??? variable list "`jellyfin2_docker_mounts_custom`"

            ```yaml
            # Type: list
            jellyfin2_docker_mounts_custom: []
            ```

        ##### Hostname

        ??? variable string "`jellyfin2_docker_hostname`"

            ```yaml
            # Type: string
            jellyfin2_docker_hostname: "{{ jellyfin_name }}"
            ```

        ##### Networks

        ??? variable string "`jellyfin2_docker_networks_alias`"

            ```yaml
            # Type: string
            jellyfin2_docker_networks_alias: "{{ jellyfin_name }}"
            ```

        ??? variable list "`jellyfin2_docker_networks_default`"

            ```yaml
            # Type: list
            jellyfin2_docker_networks_default: []
            ```

        ??? variable list "`jellyfin2_docker_networks_custom`"

            ```yaml
            # Type: list
            jellyfin2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`jellyfin2_docker_restart_policy`"

            ```yaml
            # Type: string
            jellyfin2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`jellyfin2_docker_state`"

            ```yaml
            # Type: string
            jellyfin2_docker_state: started
            ```

=== "Docker+"

    #### Additional Docker Options

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    === "Role-level"

        ##### Resource Limits

        ??? variable int "`jellyfin_role_docker_blkio_weight`"

            ```yaml
            # Type: int
            jellyfin_role_docker_blkio_weight:
            ```

        ??? variable int "`jellyfin_role_docker_cpu_period`"

            ```yaml
            # Type: int
            jellyfin_role_docker_cpu_period:
            ```

        ??? variable int "`jellyfin_role_docker_cpu_quota`"

            ```yaml
            # Type: int
            jellyfin_role_docker_cpu_quota:
            ```

        ??? variable int "`jellyfin_role_docker_cpu_shares`"

            ```yaml
            # Type: int
            jellyfin_role_docker_cpu_shares:
            ```

        ??? variable string "`jellyfin_role_docker_cpus`"

            ```yaml
            # Type: string
            jellyfin_role_docker_cpus:
            ```

        ??? variable string "`jellyfin_role_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            jellyfin_role_docker_cpuset_cpus:
            ```

        ??? variable string "`jellyfin_role_docker_cpuset_mems`"

            ```yaml
            # Type: string
            jellyfin_role_docker_cpuset_mems:
            ```

        ??? variable string "`jellyfin_role_docker_kernel_memory`"

            ```yaml
            # Type: string
            jellyfin_role_docker_kernel_memory:
            ```

        ??? variable string "`jellyfin_role_docker_memory`"

            ```yaml
            # Type: string
            jellyfin_role_docker_memory:
            ```

        ??? variable string "`jellyfin_role_docker_memory_reservation`"

            ```yaml
            # Type: string
            jellyfin_role_docker_memory_reservation:
            ```

        ??? variable string "`jellyfin_role_docker_memory_swap`"

            ```yaml
            # Type: string
            jellyfin_role_docker_memory_swap:
            ```

        ??? variable int "`jellyfin_role_docker_memory_swappiness`"

            ```yaml
            # Type: int
            jellyfin_role_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`jellyfin_role_docker_cap_drop`"

            ```yaml
            # Type: list
            jellyfin_role_docker_cap_drop:
            ```

        ??? variable list "`jellyfin_role_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            jellyfin_role_docker_device_cgroup_rules:
            ```

        ??? variable list "`jellyfin_role_docker_device_read_bps`"

            ```yaml
            # Type: list
            jellyfin_role_docker_device_read_bps:
            ```

        ??? variable list "`jellyfin_role_docker_device_read_iops`"

            ```yaml
            # Type: list
            jellyfin_role_docker_device_read_iops:
            ```

        ??? variable list "`jellyfin_role_docker_device_requests`"

            ```yaml
            # Type: list
            jellyfin_role_docker_device_requests:
            ```

        ??? variable list "`jellyfin_role_docker_device_write_bps`"

            ```yaml
            # Type: list
            jellyfin_role_docker_device_write_bps:
            ```

        ??? variable list "`jellyfin_role_docker_device_write_iops`"

            ```yaml
            # Type: list
            jellyfin_role_docker_device_write_iops:
            ```

        ??? variable list "`jellyfin_role_docker_devices`"

            ```yaml
            # Type: list
            jellyfin_role_docker_devices:
            ```

        ??? variable string "`jellyfin_role_docker_devices_default`"

            ```yaml
            # Type: string
            jellyfin_role_docker_devices_default:
            ```

        ??? variable bool "`jellyfin_role_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            jellyfin_role_docker_privileged:
            ```

        ??? variable list "`jellyfin_role_docker_security_opts`"

            ```yaml
            # Type: list
            jellyfin_role_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`jellyfin_role_docker_dns_opts`"

            ```yaml
            # Type: list
            jellyfin_role_docker_dns_opts:
            ```

        ??? variable list "`jellyfin_role_docker_dns_search_domains`"

            ```yaml
            # Type: list
            jellyfin_role_docker_dns_search_domains:
            ```

        ??? variable list "`jellyfin_role_docker_dns_servers`"

            ```yaml
            # Type: list
            jellyfin_role_docker_dns_servers:
            ```

        ??? variable dict "`jellyfin_role_docker_hosts`"

            ```yaml
            # Type: dict
            jellyfin_role_docker_hosts:
            ```

        ??? variable string "`jellyfin_role_docker_hosts_use_common`"

            ```yaml
            # Type: string
            jellyfin_role_docker_hosts_use_common:
            ```

        ??? variable string "`jellyfin_role_docker_network_mode`"

            ```yaml
            # Type: string
            jellyfin_role_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`jellyfin_role_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            jellyfin_role_docker_keep_volumes:
            ```

        ??? variable string "`jellyfin_role_docker_volume_driver`"

            ```yaml
            # Type: string
            jellyfin_role_docker_volume_driver:
            ```

        ??? variable list "`jellyfin_role_docker_volumes_from`"

            ```yaml
            # Type: list
            jellyfin_role_docker_volumes_from:
            ```

        ??? variable string "`jellyfin_role_docker_volumes_global`"

            ```yaml
            # Type: string
            jellyfin_role_docker_volumes_global:
            ```

        ??? variable string "`jellyfin_role_docker_working_dir`"

            ```yaml
            # Type: string
            jellyfin_role_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`jellyfin_role_docker_healthcheck`"

            ```yaml
            # Type: dict
            jellyfin_role_docker_healthcheck:
            ```

        ??? variable bool "`jellyfin_role_docker_init`"

            ```yaml
            # Type: bool (true/false)
            jellyfin_role_docker_init:
            ```

        ??? variable string "`jellyfin_role_docker_log_driver`"

            ```yaml
            # Type: string
            jellyfin_role_docker_log_driver:
            ```

        ??? variable dict "`jellyfin_role_docker_log_options`"

            ```yaml
            # Type: dict
            jellyfin_role_docker_log_options:
            ```

        ??? variable bool "`jellyfin_role_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            jellyfin_role_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`jellyfin_role_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            jellyfin_role_docker_auto_remove:
            ```

        ??? variable list "`jellyfin_role_docker_capabilities`"

            ```yaml
            # Type: list
            jellyfin_role_docker_capabilities:
            ```

        ??? variable string "`jellyfin_role_docker_cgroup_parent`"

            ```yaml
            # Type: string
            jellyfin_role_docker_cgroup_parent:
            ```

        ??? variable string "`jellyfin_role_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            jellyfin_role_docker_cgroupns_mode:
            ```

        ??? variable bool "`jellyfin_role_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            jellyfin_role_docker_cleanup:
            ```

        ??? variable list "`jellyfin_role_docker_commands`"

            ```yaml
            # Type: list
            jellyfin_role_docker_commands:
            ```

        ??? variable string "`jellyfin_role_docker_create_timeout`"

            ```yaml
            # Type: string
            jellyfin_role_docker_create_timeout:
            ```

        ??? variable string "`jellyfin_role_docker_domainname`"

            ```yaml
            # Type: string
            jellyfin_role_docker_domainname:
            ```

        ??? variable string "`jellyfin_role_docker_entrypoint`"

            ```yaml
            # Type: string
            jellyfin_role_docker_entrypoint:
            ```

        ??? variable string "`jellyfin_role_docker_env_file`"

            ```yaml
            # Type: string
            jellyfin_role_docker_env_file:
            ```

        ??? variable list "`jellyfin_role_docker_exposed_ports`"

            ```yaml
            # Type: list
            jellyfin_role_docker_exposed_ports:
            ```

        ??? variable string "`jellyfin_role_docker_force_kill`"

            ```yaml
            # Type: string
            jellyfin_role_docker_force_kill:
            ```

        ??? variable list "`jellyfin_role_docker_groups`"

            ```yaml
            # Type: list
            jellyfin_role_docker_groups:
            ```

        ??? variable int "`jellyfin_role_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            jellyfin_role_docker_healthy_wait_timeout:
            ```

        ??? variable string "`jellyfin_role_docker_ipc_mode`"

            ```yaml
            # Type: string
            jellyfin_role_docker_ipc_mode:
            ```

        ??? variable string "`jellyfin_role_docker_kill_signal`"

            ```yaml
            # Type: string
            jellyfin_role_docker_kill_signal:
            ```

        ??? variable dict "`jellyfin_role_docker_labels`"

            ```yaml
            # Type: dict
            jellyfin_role_docker_labels:
            ```

        ??? variable string "`jellyfin_role_docker_labels_use_common`"

            ```yaml
            # Type: string
            jellyfin_role_docker_labels_use_common:
            ```

        ??? variable list "`jellyfin_role_docker_links`"

            ```yaml
            # Type: list
            jellyfin_role_docker_links:
            ```

        ??? variable bool "`jellyfin_role_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            jellyfin_role_docker_oom_killer:
            ```

        ??? variable int "`jellyfin_role_docker_oom_score_adj`"

            ```yaml
            # Type: int
            jellyfin_role_docker_oom_score_adj:
            ```

        ??? variable bool "`jellyfin_role_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            jellyfin_role_docker_paused:
            ```

        ??? variable string "`jellyfin_role_docker_pid_mode`"

            ```yaml
            # Type: string
            jellyfin_role_docker_pid_mode:
            ```

        ??? variable list "`jellyfin_role_docker_ports`"

            ```yaml
            # Type: list
            jellyfin_role_docker_ports:
            ```

        ??? variable bool "`jellyfin_role_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            jellyfin_role_docker_read_only:
            ```

        ??? variable bool "`jellyfin_role_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            jellyfin_role_docker_recreate:
            ```

        ??? variable int "`jellyfin_role_docker_restart_retries`"

            ```yaml
            # Type: int
            jellyfin_role_docker_restart_retries:
            ```

        ??? variable string "`jellyfin_role_docker_runtime`"

            ```yaml
            # Type: string
            jellyfin_role_docker_runtime:
            ```

        ??? variable string "`jellyfin_role_docker_shm_size`"

            ```yaml
            # Type: string
            jellyfin_role_docker_shm_size:
            ```

        ??? variable int "`jellyfin_role_docker_stop_timeout`"

            ```yaml
            # Type: int
            jellyfin_role_docker_stop_timeout:
            ```

        ??? variable dict "`jellyfin_role_docker_storage_opts`"

            ```yaml
            # Type: dict
            jellyfin_role_docker_storage_opts:
            ```

        ??? variable list "`jellyfin_role_docker_sysctls`"

            ```yaml
            # Type: list
            jellyfin_role_docker_sysctls:
            ```

        ??? variable list "`jellyfin_role_docker_tmpfs`"

            ```yaml
            # Type: list
            jellyfin_role_docker_tmpfs:
            ```

        ??? variable list "`jellyfin_role_docker_ulimits`"

            ```yaml
            # Type: list
            jellyfin_role_docker_ulimits:
            ```

        ??? variable string "`jellyfin_role_docker_user`"

            ```yaml
            # Type: string
            jellyfin_role_docker_user:
            ```

        ??? variable string "`jellyfin_role_docker_userns_mode`"

            ```yaml
            # Type: string
            jellyfin_role_docker_userns_mode:
            ```

        ??? variable string "`jellyfin_role_docker_uts`"

            ```yaml
            # Type: string
            jellyfin_role_docker_uts:
            ```

    === "Instance-level"

        ##### Resource Limits

        ??? variable int "`jellyfin2_docker_blkio_weight`"

            ```yaml
            # Type: int
            jellyfin2_docker_blkio_weight:
            ```

        ??? variable int "`jellyfin2_docker_cpu_period`"

            ```yaml
            # Type: int
            jellyfin2_docker_cpu_period:
            ```

        ??? variable int "`jellyfin2_docker_cpu_quota`"

            ```yaml
            # Type: int
            jellyfin2_docker_cpu_quota:
            ```

        ??? variable int "`jellyfin2_docker_cpu_shares`"

            ```yaml
            # Type: int
            jellyfin2_docker_cpu_shares:
            ```

        ??? variable string "`jellyfin2_docker_cpus`"

            ```yaml
            # Type: string
            jellyfin2_docker_cpus:
            ```

        ??? variable string "`jellyfin2_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            jellyfin2_docker_cpuset_cpus:
            ```

        ??? variable string "`jellyfin2_docker_cpuset_mems`"

            ```yaml
            # Type: string
            jellyfin2_docker_cpuset_mems:
            ```

        ??? variable string "`jellyfin2_docker_kernel_memory`"

            ```yaml
            # Type: string
            jellyfin2_docker_kernel_memory:
            ```

        ??? variable string "`jellyfin2_docker_memory`"

            ```yaml
            # Type: string
            jellyfin2_docker_memory:
            ```

        ??? variable string "`jellyfin2_docker_memory_reservation`"

            ```yaml
            # Type: string
            jellyfin2_docker_memory_reservation:
            ```

        ??? variable string "`jellyfin2_docker_memory_swap`"

            ```yaml
            # Type: string
            jellyfin2_docker_memory_swap:
            ```

        ??? variable int "`jellyfin2_docker_memory_swappiness`"

            ```yaml
            # Type: int
            jellyfin2_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`jellyfin2_docker_cap_drop`"

            ```yaml
            # Type: list
            jellyfin2_docker_cap_drop:
            ```

        ??? variable list "`jellyfin2_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            jellyfin2_docker_device_cgroup_rules:
            ```

        ??? variable list "`jellyfin2_docker_device_read_bps`"

            ```yaml
            # Type: list
            jellyfin2_docker_device_read_bps:
            ```

        ??? variable list "`jellyfin2_docker_device_read_iops`"

            ```yaml
            # Type: list
            jellyfin2_docker_device_read_iops:
            ```

        ??? variable list "`jellyfin2_docker_device_requests`"

            ```yaml
            # Type: list
            jellyfin2_docker_device_requests:
            ```

        ??? variable list "`jellyfin2_docker_device_write_bps`"

            ```yaml
            # Type: list
            jellyfin2_docker_device_write_bps:
            ```

        ??? variable list "`jellyfin2_docker_device_write_iops`"

            ```yaml
            # Type: list
            jellyfin2_docker_device_write_iops:
            ```

        ??? variable list "`jellyfin2_docker_devices`"

            ```yaml
            # Type: list
            jellyfin2_docker_devices:
            ```

        ??? variable string "`jellyfin2_docker_devices_default`"

            ```yaml
            # Type: string
            jellyfin2_docker_devices_default:
            ```

        ??? variable bool "`jellyfin2_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            jellyfin2_docker_privileged:
            ```

        ??? variable list "`jellyfin2_docker_security_opts`"

            ```yaml
            # Type: list
            jellyfin2_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`jellyfin2_docker_dns_opts`"

            ```yaml
            # Type: list
            jellyfin2_docker_dns_opts:
            ```

        ??? variable list "`jellyfin2_docker_dns_search_domains`"

            ```yaml
            # Type: list
            jellyfin2_docker_dns_search_domains:
            ```

        ??? variable list "`jellyfin2_docker_dns_servers`"

            ```yaml
            # Type: list
            jellyfin2_docker_dns_servers:
            ```

        ??? variable dict "`jellyfin2_docker_hosts`"

            ```yaml
            # Type: dict
            jellyfin2_docker_hosts:
            ```

        ??? variable string "`jellyfin2_docker_hosts_use_common`"

            ```yaml
            # Type: string
            jellyfin2_docker_hosts_use_common:
            ```

        ??? variable string "`jellyfin2_docker_network_mode`"

            ```yaml
            # Type: string
            jellyfin2_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`jellyfin2_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            jellyfin2_docker_keep_volumes:
            ```

        ??? variable string "`jellyfin2_docker_volume_driver`"

            ```yaml
            # Type: string
            jellyfin2_docker_volume_driver:
            ```

        ??? variable list "`jellyfin2_docker_volumes_from`"

            ```yaml
            # Type: list
            jellyfin2_docker_volumes_from:
            ```

        ??? variable string "`jellyfin2_docker_volumes_global`"

            ```yaml
            # Type: string
            jellyfin2_docker_volumes_global:
            ```

        ??? variable string "`jellyfin2_docker_working_dir`"

            ```yaml
            # Type: string
            jellyfin2_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`jellyfin2_docker_healthcheck`"

            ```yaml
            # Type: dict
            jellyfin2_docker_healthcheck:
            ```

        ??? variable bool "`jellyfin2_docker_init`"

            ```yaml
            # Type: bool (true/false)
            jellyfin2_docker_init:
            ```

        ??? variable string "`jellyfin2_docker_log_driver`"

            ```yaml
            # Type: string
            jellyfin2_docker_log_driver:
            ```

        ??? variable dict "`jellyfin2_docker_log_options`"

            ```yaml
            # Type: dict
            jellyfin2_docker_log_options:
            ```

        ??? variable bool "`jellyfin2_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            jellyfin2_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`jellyfin2_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            jellyfin2_docker_auto_remove:
            ```

        ??? variable list "`jellyfin2_docker_capabilities`"

            ```yaml
            # Type: list
            jellyfin2_docker_capabilities:
            ```

        ??? variable string "`jellyfin2_docker_cgroup_parent`"

            ```yaml
            # Type: string
            jellyfin2_docker_cgroup_parent:
            ```

        ??? variable string "`jellyfin2_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            jellyfin2_docker_cgroupns_mode:
            ```

        ??? variable bool "`jellyfin2_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            jellyfin2_docker_cleanup:
            ```

        ??? variable list "`jellyfin2_docker_commands`"

            ```yaml
            # Type: list
            jellyfin2_docker_commands:
            ```

        ??? variable string "`jellyfin2_docker_create_timeout`"

            ```yaml
            # Type: string
            jellyfin2_docker_create_timeout:
            ```

        ??? variable string "`jellyfin2_docker_domainname`"

            ```yaml
            # Type: string
            jellyfin2_docker_domainname:
            ```

        ??? variable string "`jellyfin2_docker_entrypoint`"

            ```yaml
            # Type: string
            jellyfin2_docker_entrypoint:
            ```

        ??? variable string "`jellyfin2_docker_env_file`"

            ```yaml
            # Type: string
            jellyfin2_docker_env_file:
            ```

        ??? variable list "`jellyfin2_docker_exposed_ports`"

            ```yaml
            # Type: list
            jellyfin2_docker_exposed_ports:
            ```

        ??? variable string "`jellyfin2_docker_force_kill`"

            ```yaml
            # Type: string
            jellyfin2_docker_force_kill:
            ```

        ??? variable list "`jellyfin2_docker_groups`"

            ```yaml
            # Type: list
            jellyfin2_docker_groups:
            ```

        ??? variable int "`jellyfin2_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            jellyfin2_docker_healthy_wait_timeout:
            ```

        ??? variable string "`jellyfin2_docker_ipc_mode`"

            ```yaml
            # Type: string
            jellyfin2_docker_ipc_mode:
            ```

        ??? variable string "`jellyfin2_docker_kill_signal`"

            ```yaml
            # Type: string
            jellyfin2_docker_kill_signal:
            ```

        ??? variable dict "`jellyfin2_docker_labels`"

            ```yaml
            # Type: dict
            jellyfin2_docker_labels:
            ```

        ??? variable string "`jellyfin2_docker_labels_use_common`"

            ```yaml
            # Type: string
            jellyfin2_docker_labels_use_common:
            ```

        ??? variable list "`jellyfin2_docker_links`"

            ```yaml
            # Type: list
            jellyfin2_docker_links:
            ```

        ??? variable bool "`jellyfin2_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            jellyfin2_docker_oom_killer:
            ```

        ??? variable int "`jellyfin2_docker_oom_score_adj`"

            ```yaml
            # Type: int
            jellyfin2_docker_oom_score_adj:
            ```

        ??? variable bool "`jellyfin2_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            jellyfin2_docker_paused:
            ```

        ??? variable string "`jellyfin2_docker_pid_mode`"

            ```yaml
            # Type: string
            jellyfin2_docker_pid_mode:
            ```

        ??? variable list "`jellyfin2_docker_ports`"

            ```yaml
            # Type: list
            jellyfin2_docker_ports:
            ```

        ??? variable bool "`jellyfin2_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            jellyfin2_docker_read_only:
            ```

        ??? variable bool "`jellyfin2_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            jellyfin2_docker_recreate:
            ```

        ??? variable int "`jellyfin2_docker_restart_retries`"

            ```yaml
            # Type: int
            jellyfin2_docker_restart_retries:
            ```

        ??? variable string "`jellyfin2_docker_runtime`"

            ```yaml
            # Type: string
            jellyfin2_docker_runtime:
            ```

        ??? variable string "`jellyfin2_docker_shm_size`"

            ```yaml
            # Type: string
            jellyfin2_docker_shm_size:
            ```

        ??? variable int "`jellyfin2_docker_stop_timeout`"

            ```yaml
            # Type: int
            jellyfin2_docker_stop_timeout:
            ```

        ??? variable dict "`jellyfin2_docker_storage_opts`"

            ```yaml
            # Type: dict
            jellyfin2_docker_storage_opts:
            ```

        ??? variable list "`jellyfin2_docker_sysctls`"

            ```yaml
            # Type: list
            jellyfin2_docker_sysctls:
            ```

        ??? variable list "`jellyfin2_docker_tmpfs`"

            ```yaml
            # Type: list
            jellyfin2_docker_tmpfs:
            ```

        ??? variable list "`jellyfin2_docker_ulimits`"

            ```yaml
            # Type: list
            jellyfin2_docker_ulimits:
            ```

        ??? variable string "`jellyfin2_docker_user`"

            ```yaml
            # Type: string
            jellyfin2_docker_user:
            ```

        ??? variable string "`jellyfin2_docker_userns_mode`"

            ```yaml
            # Type: string
            jellyfin2_docker_userns_mode:
            ```

        ??? variable string "`jellyfin2_docker_uts`"

            ```yaml
            # Type: string
            jellyfin2_docker_uts:
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`jellyfin_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            jellyfin_role_autoheal_enabled: true
            ```

        ??? variable string "`jellyfin_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            jellyfin_role_depends_on: ""
            ```

        ??? variable string "`jellyfin_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            jellyfin_role_depends_on_delay: "0"
            ```

        ??? variable string "`jellyfin_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            jellyfin_role_depends_on_healthchecks:
            ```

        ??? variable bool "`jellyfin_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            jellyfin_role_diun_enabled: true
            ```

        ??? variable bool "`jellyfin_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            jellyfin_role_dns_enabled: true
            ```

        ??? variable bool "`jellyfin_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            jellyfin_role_docker_controller: true
            ```

        ??? variable bool "`jellyfin_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            jellyfin_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`jellyfin_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            jellyfin_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`jellyfin_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            jellyfin_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`jellyfin_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            jellyfin_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`jellyfin_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            jellyfin_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`jellyfin_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            jellyfin_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`jellyfin_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            jellyfin_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`jellyfin_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            jellyfin_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                jellyfin_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "jellyfin2.{{ user.domain }}"
                  - "jellyfin.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`jellyfin_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            jellyfin_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                jellyfin_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'jellyfin2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`jellyfin_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            jellyfin_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `jellyfin2`):

        ??? variable bool "`jellyfin2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            jellyfin2_autoheal_enabled: true
            ```

        ??? variable string "`jellyfin2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            jellyfin2_depends_on: ""
            ```

        ??? variable string "`jellyfin2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            jellyfin2_depends_on_delay: "0"
            ```

        ??? variable string "`jellyfin2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            jellyfin2_depends_on_healthchecks:
            ```

        ??? variable bool "`jellyfin2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            jellyfin2_diun_enabled: true
            ```

        ??? variable bool "`jellyfin2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            jellyfin2_dns_enabled: true
            ```

        ??? variable bool "`jellyfin2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            jellyfin2_docker_controller: true
            ```

        ??? variable bool "`jellyfin2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            jellyfin2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`jellyfin2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            jellyfin2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`jellyfin2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            jellyfin2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`jellyfin2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            jellyfin2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`jellyfin2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            jellyfin2_traefik_robot_enabled: true
            ```

        ??? variable bool "`jellyfin2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            jellyfin2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`jellyfin2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            jellyfin2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`jellyfin2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            jellyfin2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                jellyfin2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "jellyfin2.{{ user.domain }}"
                  - "jellyfin.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`jellyfin2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            jellyfin2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                jellyfin2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'jellyfin2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`jellyfin2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            jellyfin2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
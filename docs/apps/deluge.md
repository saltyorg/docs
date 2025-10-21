---
hide:
  - tags
tags:
  - deluge
---

# Deluge

## What is it?

[Deluge](https://deluge-torrent.org/) is a torrent client that can be used as an alternative to qbittorrent.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://deluge-torrent.org/){: .header-icons } | [:octicons-link-16: Docs](https://dev.deluge-torrent.org/wiki/UserGuide){: .header-icons } | [:octicons-mark-github-16: Github](https://git.deluge-torrent.org/deluge){: .header-icons } | [:material-docker: Docker](https://registry.hub.docker.com/r/linuxserver/deluge){: .header-icons }|

### 1. Installation

``` { .shell }

sb install deluge

```

### 2. URL

- To access Deluge, visit `https://deluge._yourdomain.com_`

!!! info
    **default login**

```yaml
        user: admin
    password: deluge
```

### 3. Setup

- Change login password.

- Click Preferences in the top bar and on the Downloads section enter the following paths: <br />
  - Download to: <br />
    `/mnt/unionfs/downloads/torrents/deluge/incoming`
  - Move completed to: <br />
    `/mnt/unionfs/downloads/torrents/deluge/completed`
  - Autoadd `.torrent files` from: <br />
    `/mnt/unionfs/downloads/torrents/deluge/watched`

- Click the `Plugins` section
  - enable the `labels` plugin.
  - enable and the `Extractor` plugin. <br />
      In order for Sonarr or Radarr to import media packaged within .rar files, they will have to be extracted.
  - After clicking `"Apply"`, select the `Extractor`  plugin on the left. <br />
      Make sure the directory points to the `completed` folder within your Deluge data directory.  <br />
      `/mnt/unionfs/downloads/torrents/deluge/completed` <br />
      Also, make sure that the Create torrent name sub-folder setting is checked.

### 4. Adding to Sonarr/Radarr

To add Deluge as a download client in Sonarr/Radarr use the following settings. Both are able to remove completed torrents after they have finished seeding.

  ![](../images/community/deluge_add_to_arr.png)

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `deluge_instances`.

    === "Role-level Override"

        Applies to all instances of deluge:

        ```yaml
        deluge_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `deluge2`):

        ```yaml
        deluge2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `deluge_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `deluge_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`deluge_instances`"

        ```yaml
        # Type: list
        deluge_instances: ["deluge"]
        ```

        !!! example

            ```yaml
            # Type: list
            deluge_instances: ["deluge", "deluge2"]
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`deluge_role_paths_folder`"

            ```yaml
            # Type: string
            deluge_role_paths_folder: "{{ deluge_name }}"
            ```

        ??? variable string "`deluge_role_paths_location`"

            ```yaml
            # Type: string
            deluge_role_paths_location: "{{ server_appdata_path }}/{{ deluge_role_paths_folder }}"
            ```

        ??? variable string "`deluge_role_paths_conf`"

            ```yaml
            # Type: string
            deluge_role_paths_conf: "{{ deluge_role_paths_location }}/core.conf"
            ```

        ??? variable string "`deluge_role_paths_downloads_location`"

            ```yaml
            # Type: string
            deluge_role_paths_downloads_location: "{{ downloads_torrents_path }}/{{ deluge_role_paths_folder }}"
            ```

    === "Instance-level"

        ??? variable string "`deluge2_paths_folder`"

            ```yaml
            # Type: string
            deluge2_paths_folder: "{{ deluge_name }}"
            ```

        ??? variable string "`deluge2_paths_location`"

            ```yaml
            # Type: string
            deluge2_paths_location: "{{ server_appdata_path }}/{{ deluge_role_paths_folder }}"
            ```

        ??? variable string "`deluge2_paths_conf`"

            ```yaml
            # Type: string
            deluge2_paths_conf: "{{ deluge_role_paths_location }}/core.conf"
            ```

        ??? variable string "`deluge2_paths_downloads_location`"

            ```yaml
            # Type: string
            deluge2_paths_downloads_location: "{{ downloads_torrents_path }}/{{ deluge_role_paths_folder }}"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`deluge_role_web_subdomain`"

            ```yaml
            # Type: string
            deluge_role_web_subdomain: "{{ deluge_name }}"
            ```

        ??? variable string "`deluge_role_web_domain`"

            ```yaml
            # Type: string
            deluge_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`deluge_role_web_port`"

            ```yaml
            # Type: string
            deluge_role_web_port: "8112"
            ```

        ??? variable string "`deluge_role_web_url`"

            ```yaml
            # Type: string
            deluge_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='deluge') + '.' + lookup('role_var', '_web_domain', role='deluge')
                                  if (lookup('role_var', '_web_subdomain', role='deluge') | length > 0)
                                  else lookup('role_var', '_web_domain', role='deluge')) }}"
            ```

    === "Instance-level"

        ??? variable string "`deluge2_web_subdomain`"

            ```yaml
            # Type: string
            deluge2_web_subdomain: "{{ deluge_name }}"
            ```

        ??? variable string "`deluge2_web_domain`"

            ```yaml
            # Type: string
            deluge2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`deluge2_web_port`"

            ```yaml
            # Type: string
            deluge2_web_port: "8112"
            ```

        ??? variable string "`deluge2_web_url`"

            ```yaml
            # Type: string
            deluge2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='deluge') + '.' + lookup('role_var', '_web_domain', role='deluge')
                              if (lookup('role_var', '_web_subdomain', role='deluge') | length > 0)
                              else lookup('role_var', '_web_domain', role='deluge')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`deluge_role_dns_record`"

            ```yaml
            # Type: string
            deluge_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='deluge') }}"
            ```

        ??? variable string "`deluge_role_dns_zone`"

            ```yaml
            # Type: string
            deluge_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='deluge') }}"
            ```

        ??? variable bool "`deluge_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            deluge_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`deluge2_dns_record`"

            ```yaml
            # Type: string
            deluge2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='deluge') }}"
            ```

        ??? variable string "`deluge2_dns_zone`"

            ```yaml
            # Type: string
            deluge2_dns_zone: "{{ lookup('role_var', '_web_domain', role='deluge') }}"
            ```

        ??? variable bool "`deluge2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            deluge2_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`deluge_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            deluge_role_traefik_sso_middleware: ""
            ```

        ??? variable string "`deluge_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            deluge_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                        + (',themepark-' + deluge_name
                                                          if (lookup('role_var', '_themepark_enabled', role='deluge') and global_themepark_plugin_enabled)
                                                          else '') }}"
            ```

        ??? variable string "`deluge_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            deluge_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`deluge_role_traefik_certresolver`"

            ```yaml
            # Type: string
            deluge_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`deluge_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            deluge_role_traefik_enabled: true
            ```

        ??? variable bool "`deluge_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            deluge_role_traefik_api_enabled: false
            ```

        ??? variable string "`deluge_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            deluge_role_traefik_api_endpoint: ""
            ```

    === "Instance-level"

        ??? variable string "`deluge2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            deluge2_traefik_sso_middleware: ""
            ```

        ??? variable string "`deluge2_traefik_middleware_default`"

            ```yaml
            # Type: string
            deluge2_traefik_middleware_default: "{{ traefik_default_middleware
                                                    + (',themepark-' + deluge_name
                                                      if (lookup('role_var', '_themepark_enabled', role='deluge') and global_themepark_plugin_enabled)
                                                      else '') }}"
            ```

        ??? variable string "`deluge2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            deluge2_traefik_middleware_custom: ""
            ```

        ??? variable string "`deluge2_traefik_certresolver`"

            ```yaml
            # Type: string
            deluge2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`deluge2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            deluge2_traefik_enabled: true
            ```

        ??? variable bool "`deluge2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            deluge2_traefik_api_enabled: false
            ```

        ??? variable string "`deluge2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            deluge2_traefik_api_endpoint: ""
            ```

=== "Theme"

    === "Role-level"

        ??? variable bool "`deluge_role_themepark_enabled`"

            ```yaml
            # Options can be found at https://github.com/themepark-dev/theme.park
            # Type: bool (true/false)
            deluge_role_themepark_enabled: false
            ```

        ??? variable string "`deluge_role_themepark_app`"

            ```yaml
            # Type: string
            deluge_role_themepark_app: "deluge"
            ```

        ??? variable string "`deluge_role_themepark_theme`"

            ```yaml
            # Type: string
            deluge_role_themepark_theme: "{{ global_themepark_theme }}"
            ```

        ??? variable string "`deluge_role_themepark_domain`"

            ```yaml
            # Type: string
            deluge_role_themepark_domain: "{{ global_themepark_domain }}"
            ```

        ??? variable list "`deluge_role_themepark_addons`"

            ```yaml
            # Type: list
            deluge_role_themepark_addons: []
            ```

    === "Instance-level"

        ??? variable bool "`deluge2_themepark_enabled`"

            ```yaml
            # Options can be found at https://github.com/themepark-dev/theme.park
            # Type: bool (true/false)
            deluge2_themepark_enabled: false
            ```

        ??? variable string "`deluge2_themepark_app`"

            ```yaml
            # Type: string
            deluge2_themepark_app: "deluge"
            ```

        ??? variable string "`deluge2_themepark_theme`"

            ```yaml
            # Type: string
            deluge2_themepark_theme: "{{ global_themepark_theme }}"
            ```

        ??? variable string "`deluge2_themepark_domain`"

            ```yaml
            # Type: string
            deluge2_themepark_domain: "{{ global_themepark_domain }}"
            ```

        ??? variable list "`deluge2_themepark_addons`"

            ```yaml
            # Type: list
            deluge2_themepark_addons: []
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`deluge_role_docker_container`"

            ```yaml
            # Type: string
            deluge_role_docker_container: "{{ deluge_name }}"
            ```

        ##### Image

        ??? variable bool "`deluge_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            deluge_role_docker_image_pull: true
            ```

        ??? variable string "`deluge_role_docker_image_repo`"

            ```yaml
            # Type: string
            deluge_role_docker_image_repo: "lscr.io/linuxserver/deluge"
            ```

        ??? variable string "`deluge_role_docker_image_tag`"

            ```yaml
            # Type: string
            deluge_role_docker_image_tag: "latest"
            ```

        ??? variable string "`deluge_role_docker_image`"

            ```yaml
            # Type: string
            deluge_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='deluge') }}:{{ lookup('role_var', '_docker_image_tag', role='deluge') }}"
            ```

        ##### Ports

        ??? variable string "`deluge_role_docker_ports_58112`"

            ```yaml
            # Type: string
            deluge_role_docker_ports_58112: "{{ port_lookup_58112.meta.port
                                             if (port_lookup_58112.meta.port is defined) and (port_lookup_58112.meta.port | trim | length > 0)
                                             else '58112' }}"
            ```

        ??? variable list "`deluge_role_docker_ports_default`"

            ```yaml
            # Type: list
            deluge_role_docker_ports_default: 
              - "{{ deluge_role_docker_ports_58112 }}:{{ deluge_role_docker_ports_58112 }}"
              - "{{ deluge_role_docker_ports_58112 }}:{{ deluge_role_docker_ports_58112 }}/udp"
            ```

        ??? variable list "`deluge_role_docker_ports_custom`"

            ```yaml
            # Type: list
            deluge_role_docker_ports_custom: []
            ```

        ##### Envs

        ??? variable dict "`deluge_role_docker_envs_default`"

            ```yaml
            # Type: dict
            deluge_role_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              TZ: "{{ tz }}"
              UMASK: "002"
            ```

        ??? variable dict "`deluge_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            deluge_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`deluge_role_docker_volumes_default`"

            ```yaml
            # Type: list
            deluge_role_docker_volumes_default: 
              - "{{ deluge_role_paths_location }}:/config"
              - "{{ server_appdata_path }}/scripts:/scripts"
            ```

        ??? variable list "`deluge_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            deluge_role_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable dict "`deluge_role_docker_labels_default`"

            ```yaml
            # Type: dict
            deluge_role_docker_labels_default: {}
            ```

        ??? variable dict "`deluge_role_docker_labels_custom`"

            ```yaml
            # Type: dict
            deluge_role_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`deluge_role_docker_hostname`"

            ```yaml
            # Type: string
            deluge_role_docker_hostname: "{{ deluge_name }}"
            ```

        ##### Networks

        ??? variable string "`deluge_role_docker_networks_alias`"

            ```yaml
            # Type: string
            deluge_role_docker_networks_alias: "{{ deluge_name }}"
            ```

        ??? variable list "`deluge_role_docker_networks_default`"

            ```yaml
            # Type: list
            deluge_role_docker_networks_default: []
            ```

        ??? variable list "`deluge_role_docker_networks_custom`"

            ```yaml
            # Type: list
            deluge_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`deluge_role_docker_restart_policy`"

            ```yaml
            # Type: string
            deluge_role_docker_restart_policy: unless-stopped
            ```

        ##### Stop Timeout

        ??? variable int "`deluge_role_docker_stop_timeout`"

            ```yaml
            # Type: int
            deluge_role_docker_stop_timeout: 900
            ```

        ##### State

        ??? variable string "`deluge_role_docker_state`"

            ```yaml
            # Type: string
            deluge_role_docker_state: started
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`deluge2_docker_container`"

            ```yaml
            # Type: string
            deluge2_docker_container: "{{ deluge_name }}"
            ```

        ##### Image

        ??? variable bool "`deluge2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            deluge2_docker_image_pull: true
            ```

        ??? variable string "`deluge2_docker_image_repo`"

            ```yaml
            # Type: string
            deluge2_docker_image_repo: "lscr.io/linuxserver/deluge"
            ```

        ??? variable string "`deluge2_docker_image_tag`"

            ```yaml
            # Type: string
            deluge2_docker_image_tag: "latest"
            ```

        ??? variable string "`deluge2_docker_image`"

            ```yaml
            # Type: string
            deluge2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='deluge') }}:{{ lookup('role_var', '_docker_image_tag', role='deluge') }}"
            ```

        ##### Ports

        ??? variable string "`deluge2_docker_ports_58112`"

            ```yaml
            # Type: string
            deluge2_docker_ports_58112: "{{ port_lookup_58112.meta.port
                                         if (port_lookup_58112.meta.port is defined) and (port_lookup_58112.meta.port | trim | length > 0)
                                         else '58112' }}"
            ```

        ??? variable list "`deluge2_docker_ports_default`"

            ```yaml
            # Type: list
            deluge2_docker_ports_default: 
              - "{{ deluge_role_docker_ports_58112 }}:{{ deluge_role_docker_ports_58112 }}"
              - "{{ deluge_role_docker_ports_58112 }}:{{ deluge_role_docker_ports_58112 }}/udp"
            ```

        ??? variable list "`deluge2_docker_ports_custom`"

            ```yaml
            # Type: list
            deluge2_docker_ports_custom: []
            ```

        ##### Envs

        ??? variable dict "`deluge2_docker_envs_default`"

            ```yaml
            # Type: dict
            deluge2_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              TZ: "{{ tz }}"
              UMASK: "002"
            ```

        ??? variable dict "`deluge2_docker_envs_custom`"

            ```yaml
            # Type: dict
            deluge2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`deluge2_docker_volumes_default`"

            ```yaml
            # Type: list
            deluge2_docker_volumes_default: 
              - "{{ deluge_role_paths_location }}:/config"
              - "{{ server_appdata_path }}/scripts:/scripts"
            ```

        ??? variable list "`deluge2_docker_volumes_custom`"

            ```yaml
            # Type: list
            deluge2_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable dict "`deluge2_docker_labels_default`"

            ```yaml
            # Type: dict
            deluge2_docker_labels_default: {}
            ```

        ??? variable dict "`deluge2_docker_labels_custom`"

            ```yaml
            # Type: dict
            deluge2_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`deluge2_docker_hostname`"

            ```yaml
            # Type: string
            deluge2_docker_hostname: "{{ deluge_name }}"
            ```

        ##### Networks

        ??? variable string "`deluge2_docker_networks_alias`"

            ```yaml
            # Type: string
            deluge2_docker_networks_alias: "{{ deluge_name }}"
            ```

        ??? variable list "`deluge2_docker_networks_default`"

            ```yaml
            # Type: list
            deluge2_docker_networks_default: []
            ```

        ??? variable list "`deluge2_docker_networks_custom`"

            ```yaml
            # Type: list
            deluge2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`deluge2_docker_restart_policy`"

            ```yaml
            # Type: string
            deluge2_docker_restart_policy: unless-stopped
            ```

        ##### Stop Timeout

        ??? variable int "`deluge2_docker_stop_timeout`"

            ```yaml
            # Type: int
            deluge2_docker_stop_timeout: 900
            ```

        ##### State

        ??? variable string "`deluge2_docker_state`"

            ```yaml
            # Type: string
            deluge2_docker_state: started
            ```

=== "Docker+"

    #### Additional Docker Options

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    === "Role-level"

        ##### Resource Limits

        ??? variable int "`deluge_role_docker_blkio_weight`"

            ```yaml
            # Type: int
            deluge_role_docker_blkio_weight:
            ```

        ??? variable int "`deluge_role_docker_cpu_period`"

            ```yaml
            # Type: int
            deluge_role_docker_cpu_period:
            ```

        ??? variable int "`deluge_role_docker_cpu_quota`"

            ```yaml
            # Type: int
            deluge_role_docker_cpu_quota:
            ```

        ??? variable int "`deluge_role_docker_cpu_shares`"

            ```yaml
            # Type: int
            deluge_role_docker_cpu_shares:
            ```

        ??? variable string "`deluge_role_docker_cpus`"

            ```yaml
            # Type: string
            deluge_role_docker_cpus:
            ```

        ??? variable string "`deluge_role_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            deluge_role_docker_cpuset_cpus:
            ```

        ??? variable string "`deluge_role_docker_cpuset_mems`"

            ```yaml
            # Type: string
            deluge_role_docker_cpuset_mems:
            ```

        ??? variable string "`deluge_role_docker_kernel_memory`"

            ```yaml
            # Type: string
            deluge_role_docker_kernel_memory:
            ```

        ??? variable string "`deluge_role_docker_memory`"

            ```yaml
            # Type: string
            deluge_role_docker_memory:
            ```

        ??? variable string "`deluge_role_docker_memory_reservation`"

            ```yaml
            # Type: string
            deluge_role_docker_memory_reservation:
            ```

        ??? variable string "`deluge_role_docker_memory_swap`"

            ```yaml
            # Type: string
            deluge_role_docker_memory_swap:
            ```

        ??? variable int "`deluge_role_docker_memory_swappiness`"

            ```yaml
            # Type: int
            deluge_role_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`deluge_role_docker_cap_drop`"

            ```yaml
            # Type: list
            deluge_role_docker_cap_drop:
            ```

        ??? variable list "`deluge_role_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            deluge_role_docker_device_cgroup_rules:
            ```

        ??? variable list "`deluge_role_docker_device_read_bps`"

            ```yaml
            # Type: list
            deluge_role_docker_device_read_bps:
            ```

        ??? variable list "`deluge_role_docker_device_read_iops`"

            ```yaml
            # Type: list
            deluge_role_docker_device_read_iops:
            ```

        ??? variable list "`deluge_role_docker_device_requests`"

            ```yaml
            # Type: list
            deluge_role_docker_device_requests:
            ```

        ??? variable list "`deluge_role_docker_device_write_bps`"

            ```yaml
            # Type: list
            deluge_role_docker_device_write_bps:
            ```

        ??? variable list "`deluge_role_docker_device_write_iops`"

            ```yaml
            # Type: list
            deluge_role_docker_device_write_iops:
            ```

        ??? variable list "`deluge_role_docker_devices`"

            ```yaml
            # Type: list
            deluge_role_docker_devices:
            ```

        ??? variable string "`deluge_role_docker_devices_default`"

            ```yaml
            # Type: string
            deluge_role_docker_devices_default:
            ```

        ??? variable bool "`deluge_role_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            deluge_role_docker_privileged:
            ```

        ??? variable list "`deluge_role_docker_security_opts`"

            ```yaml
            # Type: list
            deluge_role_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`deluge_role_docker_dns_opts`"

            ```yaml
            # Type: list
            deluge_role_docker_dns_opts:
            ```

        ??? variable list "`deluge_role_docker_dns_search_domains`"

            ```yaml
            # Type: list
            deluge_role_docker_dns_search_domains:
            ```

        ??? variable list "`deluge_role_docker_dns_servers`"

            ```yaml
            # Type: list
            deluge_role_docker_dns_servers:
            ```

        ??? variable dict "`deluge_role_docker_hosts`"

            ```yaml
            # Type: dict
            deluge_role_docker_hosts:
            ```

        ??? variable string "`deluge_role_docker_hosts_use_common`"

            ```yaml
            # Type: string
            deluge_role_docker_hosts_use_common:
            ```

        ??? variable string "`deluge_role_docker_network_mode`"

            ```yaml
            # Type: string
            deluge_role_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`deluge_role_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            deluge_role_docker_keep_volumes:
            ```

        ??? variable list "`deluge_role_docker_mounts`"

            ```yaml
            # Type: list
            deluge_role_docker_mounts:
            ```

        ??? variable string "`deluge_role_docker_volume_driver`"

            ```yaml
            # Type: string
            deluge_role_docker_volume_driver:
            ```

        ??? variable list "`deluge_role_docker_volumes_from`"

            ```yaml
            # Type: list
            deluge_role_docker_volumes_from:
            ```

        ??? variable string "`deluge_role_docker_volumes_global`"

            ```yaml
            # Type: string
            deluge_role_docker_volumes_global:
            ```

        ??? variable string "`deluge_role_docker_working_dir`"

            ```yaml
            # Type: string
            deluge_role_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`deluge_role_docker_healthcheck`"

            ```yaml
            # Type: dict
            deluge_role_docker_healthcheck:
            ```

        ??? variable bool "`deluge_role_docker_init`"

            ```yaml
            # Type: bool (true/false)
            deluge_role_docker_init:
            ```

        ??? variable string "`deluge_role_docker_log_driver`"

            ```yaml
            # Type: string
            deluge_role_docker_log_driver:
            ```

        ??? variable dict "`deluge_role_docker_log_options`"

            ```yaml
            # Type: dict
            deluge_role_docker_log_options:
            ```

        ??? variable bool "`deluge_role_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            deluge_role_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`deluge_role_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            deluge_role_docker_auto_remove:
            ```

        ??? variable list "`deluge_role_docker_capabilities`"

            ```yaml
            # Type: list
            deluge_role_docker_capabilities:
            ```

        ??? variable string "`deluge_role_docker_cgroup_parent`"

            ```yaml
            # Type: string
            deluge_role_docker_cgroup_parent:
            ```

        ??? variable string "`deluge_role_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            deluge_role_docker_cgroupns_mode:
            ```

        ??? variable bool "`deluge_role_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            deluge_role_docker_cleanup:
            ```

        ??? variable list "`deluge_role_docker_commands`"

            ```yaml
            # Type: list
            deluge_role_docker_commands:
            ```

        ??? variable string "`deluge_role_docker_create_timeout`"

            ```yaml
            # Type: string
            deluge_role_docker_create_timeout:
            ```

        ??? variable string "`deluge_role_docker_domainname`"

            ```yaml
            # Type: string
            deluge_role_docker_domainname:
            ```

        ??? variable string "`deluge_role_docker_entrypoint`"

            ```yaml
            # Type: string
            deluge_role_docker_entrypoint:
            ```

        ??? variable string "`deluge_role_docker_env_file`"

            ```yaml
            # Type: string
            deluge_role_docker_env_file:
            ```

        ??? variable list "`deluge_role_docker_exposed_ports`"

            ```yaml
            # Type: list
            deluge_role_docker_exposed_ports:
            ```

        ??? variable string "`deluge_role_docker_force_kill`"

            ```yaml
            # Type: string
            deluge_role_docker_force_kill:
            ```

        ??? variable list "`deluge_role_docker_groups`"

            ```yaml
            # Type: list
            deluge_role_docker_groups:
            ```

        ??? variable int "`deluge_role_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            deluge_role_docker_healthy_wait_timeout:
            ```

        ??? variable string "`deluge_role_docker_ipc_mode`"

            ```yaml
            # Type: string
            deluge_role_docker_ipc_mode:
            ```

        ??? variable string "`deluge_role_docker_kill_signal`"

            ```yaml
            # Type: string
            deluge_role_docker_kill_signal:
            ```

        ??? variable string "`deluge_role_docker_labels_use_common`"

            ```yaml
            # Type: string
            deluge_role_docker_labels_use_common:
            ```

        ??? variable list "`deluge_role_docker_links`"

            ```yaml
            # Type: list
            deluge_role_docker_links:
            ```

        ??? variable bool "`deluge_role_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            deluge_role_docker_oom_killer:
            ```

        ??? variable int "`deluge_role_docker_oom_score_adj`"

            ```yaml
            # Type: int
            deluge_role_docker_oom_score_adj:
            ```

        ??? variable bool "`deluge_role_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            deluge_role_docker_paused:
            ```

        ??? variable string "`deluge_role_docker_pid_mode`"

            ```yaml
            # Type: string
            deluge_role_docker_pid_mode:
            ```

        ??? variable bool "`deluge_role_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            deluge_role_docker_read_only:
            ```

        ??? variable bool "`deluge_role_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            deluge_role_docker_recreate:
            ```

        ??? variable int "`deluge_role_docker_restart_retries`"

            ```yaml
            # Type: int
            deluge_role_docker_restart_retries:
            ```

        ??? variable string "`deluge_role_docker_runtime`"

            ```yaml
            # Type: string
            deluge_role_docker_runtime:
            ```

        ??? variable string "`deluge_role_docker_shm_size`"

            ```yaml
            # Type: string
            deluge_role_docker_shm_size:
            ```

        ??? variable dict "`deluge_role_docker_storage_opts`"

            ```yaml
            # Type: dict
            deluge_role_docker_storage_opts:
            ```

        ??? variable list "`deluge_role_docker_sysctls`"

            ```yaml
            # Type: list
            deluge_role_docker_sysctls:
            ```

        ??? variable list "`deluge_role_docker_tmpfs`"

            ```yaml
            # Type: list
            deluge_role_docker_tmpfs:
            ```

        ??? variable list "`deluge_role_docker_ulimits`"

            ```yaml
            # Type: list
            deluge_role_docker_ulimits:
            ```

        ??? variable string "`deluge_role_docker_user`"

            ```yaml
            # Type: string
            deluge_role_docker_user:
            ```

        ??? variable string "`deluge_role_docker_userns_mode`"

            ```yaml
            # Type: string
            deluge_role_docker_userns_mode:
            ```

        ??? variable string "`deluge_role_docker_uts`"

            ```yaml
            # Type: string
            deluge_role_docker_uts:
            ```

    === "Instance-level"

        ##### Resource Limits

        ??? variable int "`deluge2_docker_blkio_weight`"

            ```yaml
            # Type: int
            deluge2_docker_blkio_weight:
            ```

        ??? variable int "`deluge2_docker_cpu_period`"

            ```yaml
            # Type: int
            deluge2_docker_cpu_period:
            ```

        ??? variable int "`deluge2_docker_cpu_quota`"

            ```yaml
            # Type: int
            deluge2_docker_cpu_quota:
            ```

        ??? variable int "`deluge2_docker_cpu_shares`"

            ```yaml
            # Type: int
            deluge2_docker_cpu_shares:
            ```

        ??? variable string "`deluge2_docker_cpus`"

            ```yaml
            # Type: string
            deluge2_docker_cpus:
            ```

        ??? variable string "`deluge2_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            deluge2_docker_cpuset_cpus:
            ```

        ??? variable string "`deluge2_docker_cpuset_mems`"

            ```yaml
            # Type: string
            deluge2_docker_cpuset_mems:
            ```

        ??? variable string "`deluge2_docker_kernel_memory`"

            ```yaml
            # Type: string
            deluge2_docker_kernel_memory:
            ```

        ??? variable string "`deluge2_docker_memory`"

            ```yaml
            # Type: string
            deluge2_docker_memory:
            ```

        ??? variable string "`deluge2_docker_memory_reservation`"

            ```yaml
            # Type: string
            deluge2_docker_memory_reservation:
            ```

        ??? variable string "`deluge2_docker_memory_swap`"

            ```yaml
            # Type: string
            deluge2_docker_memory_swap:
            ```

        ??? variable int "`deluge2_docker_memory_swappiness`"

            ```yaml
            # Type: int
            deluge2_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`deluge2_docker_cap_drop`"

            ```yaml
            # Type: list
            deluge2_docker_cap_drop:
            ```

        ??? variable list "`deluge2_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            deluge2_docker_device_cgroup_rules:
            ```

        ??? variable list "`deluge2_docker_device_read_bps`"

            ```yaml
            # Type: list
            deluge2_docker_device_read_bps:
            ```

        ??? variable list "`deluge2_docker_device_read_iops`"

            ```yaml
            # Type: list
            deluge2_docker_device_read_iops:
            ```

        ??? variable list "`deluge2_docker_device_requests`"

            ```yaml
            # Type: list
            deluge2_docker_device_requests:
            ```

        ??? variable list "`deluge2_docker_device_write_bps`"

            ```yaml
            # Type: list
            deluge2_docker_device_write_bps:
            ```

        ??? variable list "`deluge2_docker_device_write_iops`"

            ```yaml
            # Type: list
            deluge2_docker_device_write_iops:
            ```

        ??? variable list "`deluge2_docker_devices`"

            ```yaml
            # Type: list
            deluge2_docker_devices:
            ```

        ??? variable string "`deluge2_docker_devices_default`"

            ```yaml
            # Type: string
            deluge2_docker_devices_default:
            ```

        ??? variable bool "`deluge2_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            deluge2_docker_privileged:
            ```

        ??? variable list "`deluge2_docker_security_opts`"

            ```yaml
            # Type: list
            deluge2_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`deluge2_docker_dns_opts`"

            ```yaml
            # Type: list
            deluge2_docker_dns_opts:
            ```

        ??? variable list "`deluge2_docker_dns_search_domains`"

            ```yaml
            # Type: list
            deluge2_docker_dns_search_domains:
            ```

        ??? variable list "`deluge2_docker_dns_servers`"

            ```yaml
            # Type: list
            deluge2_docker_dns_servers:
            ```

        ??? variable dict "`deluge2_docker_hosts`"

            ```yaml
            # Type: dict
            deluge2_docker_hosts:
            ```

        ??? variable string "`deluge2_docker_hosts_use_common`"

            ```yaml
            # Type: string
            deluge2_docker_hosts_use_common:
            ```

        ??? variable string "`deluge2_docker_network_mode`"

            ```yaml
            # Type: string
            deluge2_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`deluge2_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            deluge2_docker_keep_volumes:
            ```

        ??? variable list "`deluge2_docker_mounts`"

            ```yaml
            # Type: list
            deluge2_docker_mounts:
            ```

        ??? variable string "`deluge2_docker_volume_driver`"

            ```yaml
            # Type: string
            deluge2_docker_volume_driver:
            ```

        ??? variable list "`deluge2_docker_volumes_from`"

            ```yaml
            # Type: list
            deluge2_docker_volumes_from:
            ```

        ??? variable string "`deluge2_docker_volumes_global`"

            ```yaml
            # Type: string
            deluge2_docker_volumes_global:
            ```

        ??? variable string "`deluge2_docker_working_dir`"

            ```yaml
            # Type: string
            deluge2_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`deluge2_docker_healthcheck`"

            ```yaml
            # Type: dict
            deluge2_docker_healthcheck:
            ```

        ??? variable bool "`deluge2_docker_init`"

            ```yaml
            # Type: bool (true/false)
            deluge2_docker_init:
            ```

        ??? variable string "`deluge2_docker_log_driver`"

            ```yaml
            # Type: string
            deluge2_docker_log_driver:
            ```

        ??? variable dict "`deluge2_docker_log_options`"

            ```yaml
            # Type: dict
            deluge2_docker_log_options:
            ```

        ??? variable bool "`deluge2_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            deluge2_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`deluge2_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            deluge2_docker_auto_remove:
            ```

        ??? variable list "`deluge2_docker_capabilities`"

            ```yaml
            # Type: list
            deluge2_docker_capabilities:
            ```

        ??? variable string "`deluge2_docker_cgroup_parent`"

            ```yaml
            # Type: string
            deluge2_docker_cgroup_parent:
            ```

        ??? variable string "`deluge2_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            deluge2_docker_cgroupns_mode:
            ```

        ??? variable bool "`deluge2_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            deluge2_docker_cleanup:
            ```

        ??? variable list "`deluge2_docker_commands`"

            ```yaml
            # Type: list
            deluge2_docker_commands:
            ```

        ??? variable string "`deluge2_docker_create_timeout`"

            ```yaml
            # Type: string
            deluge2_docker_create_timeout:
            ```

        ??? variable string "`deluge2_docker_domainname`"

            ```yaml
            # Type: string
            deluge2_docker_domainname:
            ```

        ??? variable string "`deluge2_docker_entrypoint`"

            ```yaml
            # Type: string
            deluge2_docker_entrypoint:
            ```

        ??? variable string "`deluge2_docker_env_file`"

            ```yaml
            # Type: string
            deluge2_docker_env_file:
            ```

        ??? variable list "`deluge2_docker_exposed_ports`"

            ```yaml
            # Type: list
            deluge2_docker_exposed_ports:
            ```

        ??? variable string "`deluge2_docker_force_kill`"

            ```yaml
            # Type: string
            deluge2_docker_force_kill:
            ```

        ??? variable list "`deluge2_docker_groups`"

            ```yaml
            # Type: list
            deluge2_docker_groups:
            ```

        ??? variable int "`deluge2_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            deluge2_docker_healthy_wait_timeout:
            ```

        ??? variable string "`deluge2_docker_ipc_mode`"

            ```yaml
            # Type: string
            deluge2_docker_ipc_mode:
            ```

        ??? variable string "`deluge2_docker_kill_signal`"

            ```yaml
            # Type: string
            deluge2_docker_kill_signal:
            ```

        ??? variable string "`deluge2_docker_labels_use_common`"

            ```yaml
            # Type: string
            deluge2_docker_labels_use_common:
            ```

        ??? variable list "`deluge2_docker_links`"

            ```yaml
            # Type: list
            deluge2_docker_links:
            ```

        ??? variable bool "`deluge2_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            deluge2_docker_oom_killer:
            ```

        ??? variable int "`deluge2_docker_oom_score_adj`"

            ```yaml
            # Type: int
            deluge2_docker_oom_score_adj:
            ```

        ??? variable bool "`deluge2_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            deluge2_docker_paused:
            ```

        ??? variable string "`deluge2_docker_pid_mode`"

            ```yaml
            # Type: string
            deluge2_docker_pid_mode:
            ```

        ??? variable bool "`deluge2_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            deluge2_docker_read_only:
            ```

        ??? variable bool "`deluge2_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            deluge2_docker_recreate:
            ```

        ??? variable int "`deluge2_docker_restart_retries`"

            ```yaml
            # Type: int
            deluge2_docker_restart_retries:
            ```

        ??? variable string "`deluge2_docker_runtime`"

            ```yaml
            # Type: string
            deluge2_docker_runtime:
            ```

        ??? variable string "`deluge2_docker_shm_size`"

            ```yaml
            # Type: string
            deluge2_docker_shm_size:
            ```

        ??? variable dict "`deluge2_docker_storage_opts`"

            ```yaml
            # Type: dict
            deluge2_docker_storage_opts:
            ```

        ??? variable list "`deluge2_docker_sysctls`"

            ```yaml
            # Type: list
            deluge2_docker_sysctls:
            ```

        ??? variable list "`deluge2_docker_tmpfs`"

            ```yaml
            # Type: list
            deluge2_docker_tmpfs:
            ```

        ??? variable list "`deluge2_docker_ulimits`"

            ```yaml
            # Type: list
            deluge2_docker_ulimits:
            ```

        ??? variable string "`deluge2_docker_user`"

            ```yaml
            # Type: string
            deluge2_docker_user:
            ```

        ??? variable string "`deluge2_docker_userns_mode`"

            ```yaml
            # Type: string
            deluge2_docker_userns_mode:
            ```

        ??? variable string "`deluge2_docker_uts`"

            ```yaml
            # Type: string
            deluge2_docker_uts:
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`deluge_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            deluge_role_autoheal_enabled: true
            ```

        ??? variable string "`deluge_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            deluge_role_depends_on: ""
            ```

        ??? variable string "`deluge_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            deluge_role_depends_on_delay: "0"
            ```

        ??? variable string "`deluge_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            deluge_role_depends_on_healthchecks:
            ```

        ??? variable bool "`deluge_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            deluge_role_diun_enabled: true
            ```

        ??? variable bool "`deluge_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            deluge_role_dns_enabled: true
            ```

        ??? variable bool "`deluge_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            deluge_role_docker_controller: true
            ```

        ??? variable bool "`deluge_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            deluge_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`deluge_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            deluge_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`deluge_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            deluge_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`deluge_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            deluge_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`deluge_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            deluge_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`deluge_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            deluge_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`deluge_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            deluge_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`deluge_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            deluge_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                deluge_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "deluge2.{{ user.domain }}"
                  - "deluge.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`deluge_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            deluge_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                deluge_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'deluge2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`deluge_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            deluge_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `deluge2`):

        ??? variable bool "`deluge2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            deluge2_autoheal_enabled: true
            ```

        ??? variable string "`deluge2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            deluge2_depends_on: ""
            ```

        ??? variable string "`deluge2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            deluge2_depends_on_delay: "0"
            ```

        ??? variable string "`deluge2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            deluge2_depends_on_healthchecks:
            ```

        ??? variable bool "`deluge2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            deluge2_diun_enabled: true
            ```

        ??? variable bool "`deluge2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            deluge2_dns_enabled: true
            ```

        ??? variable bool "`deluge2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            deluge2_docker_controller: true
            ```

        ??? variable bool "`deluge2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            deluge2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`deluge2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            deluge2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`deluge2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            deluge2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`deluge2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            deluge2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`deluge2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            deluge2_traefik_robot_enabled: true
            ```

        ??? variable bool "`deluge2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            deluge2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`deluge2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            deluge2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`deluge2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            deluge2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                deluge2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "deluge2.{{ user.domain }}"
                  - "deluge.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`deluge2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            deluge2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                deluge2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'deluge2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`deluge2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            deluge2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
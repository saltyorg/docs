---
hide:
  - tags
tags:
  - qbittorrent
---

# qBittorrent

## What is it?

[qBittorrent](https://www.qbittorrent.org/) is a bittorrent client programmed in C++ / Qt that uses libtorrent (sometimes called libtorrent-rasterbar) by Arvid Norberg.

It aims to be a good alternative to all other bittorrent clients out there. qBittorrent is fast, stable and provides unicode support as well as many features.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.qbittorrent.org/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/qbittorrent/qBittorrent/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/qbittorrent/qBittorrent){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/saltydk/qbittorrent){: .header-icons }|

### 1. Installation

``` shell

sb install qbittorrent

```

### 2. URL

- To access qBittorrent, visit `https://qbittorrent.xDOMAIN_NAMEx`

### 3. Setup

- Access qbittorrent at `https://qbittorrent.xDOMAIN_NAMEx`

- Log in using the username/password you specified in `accounts.yml`

- **OPTIONALLY** go to `Options` -> `Web UI` and set a new username and a strong password.

    ![Authentication Section Screenshot](../images/community/qbit_auth.png)

- Under `Options` -> `Connection`, set the port to 56881.

    ![Port Section Screenshot](../images/community/qbit_port.png)

- Under `Options` -> `Downloads`, set the following;

  - Save files to location: `/mnt/unionfs/downloads/torrents/qbittorrent/completed/`

  - Keep incomplete torrents in: `/mnt/unionfs/downloads/torrents/qbittorrent/incoming/`

  - Copy .torrent files to: `/mnt/unionfs/downloads/torrents/qbittorrent/torrents/`

  - Copy .torrent files for finished downloads to: `/mnt/unionfs/downloads/torrents/qbittorrent/torrents/`

  - Additionally you can set monitored folder to: `/mnt/unionfs/downloads/torrents/qbittorrent/watched/`

  - tick `Run external program on torrent completion` and paste this into the box: `/usr/bin/unrar x -r "%F/." "%F/"`

    ![Hard Disk Section Screenshot](../images/community/qbit_hdd.png)
<!-- markdownlint-disable MD046 -->
!!! warning
      Make sure to choose a strong username/password combination because by default qBittorrent's Web API is completely exposed to the internet!  
      If someone guesses your qBit's credentials, they can, among other things, steal your tracker passkeys and delete torrents (data included).  
      If you don't need the API endpoints exposed, you can disable them using the [inventory system](../saltbox/inventory/index.md) with

      ``` { .yaml }
      qbittorrent_traefik_api_enabled: false
      ```

      and by rerunning the `qbittorrent` tag.
<!-- markdownlint-enable MD046 -->

!!! note
      if you're using private trackers be sure to go to `Options` -> `BitTorrent` and uncheck everything in Privacy section.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `qbittorrent_instances`.

    === "Role-level Override"

        Applies to all instances of qbittorrent:

        ```yaml
        qbittorrent_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `qbittorrent2`):

        ```yaml
        qbittorrent2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `qbittorrent_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `qbittorrent_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        qbittorrent_instances: ["qbittorrent"]

        ```

    === "Example"

        ```yaml
        # Type: list
        qbittorrent_instances: ["qbittorrent", "qbittorrent2"]

        ```

??? example "Settings"

    === "Role-level"

        ```yaml
        # Type: bool (true/false)
        qbittorrent_role_host_install: false

        # Type: string
        qbittorrent_role_webui_custom_headers_enabled: "{{ 'true' if lookup('role_var', '_themepark_enabled', role='qbittorrent') and global_themepark_plugin_enabled else 'false' }}"

        # Type: string
        qbittorrent_role_webui_custom_headers_default: "{{ (qbittorrent_role_themepark_headers if lookup('role_var', '_themepark_enabled', role='qbittorrent') and global_themepark_plugin_enabled else '') }}"

        # Type: string
        qbittorrent_role_webui_custom_headers_custom: ""

        # Options are: Delete or MoveToTrash
        # Type: string
        qbittorrent_role_torrent_content_remove_option: "Delete"

        ```

    === "Instance-level"

        ```yaml
        # Type: bool (true/false)
        qbittorrent2_host_install: false

        # Type: string
        qbittorrent2_webui_custom_headers_enabled: "{{ 'true' if lookup('role_var', '_themepark_enabled', role='qbittorrent') and global_themepark_plugin_enabled else 'false' }}"

        # Type: string
        qbittorrent2_webui_custom_headers_default: "{{ (qbittorrent_role_themepark_headers if lookup('role_var', '_themepark_enabled', role='qbittorrent') and global_themepark_plugin_enabled else '') }}"

        # Type: string
        qbittorrent2_webui_custom_headers_custom: ""

        # Options are: Delete or MoveToTrash
        # Type: string
        qbittorrent2_torrent_content_remove_option: "Delete"

        ```

??? example "Host Install"

    === "Role-level"

        ```yaml
        # Options are: libtorrent1 (latest), libtorrent2 (latest) or legacy (4.3.9)
        # Type: string
        qbittorrent_role_host_branch: libtorrent1

        # Example being "release-4.4.5_v1.2.18"
        # If this is set then the above branch logic is ignored
        # Type: string
        qbittorrent_role_host_specific_version: ""

        # Lookup variables
        # Type: string
        qbittorrent_role_host_download_endpoint: "{{ 'https://github.com/userdocs/qbittorrent-nox-static/releases/download/'
                                                  if lookup('role_var', '_host_branch', role='qbittorrent') != 'legacy'
                                                  else 'https://github.com/userdocs/qbittorrent-nox-static-legacy/releases/download/' }}"

        # Type: string
        qbittorrent_role_host_download_url: "{{ lookup('role_var', '_host_download_endpoint', role='qbittorrent') }}{{ lookup('role_var', '_host_specific_version', role='qbittorrent')
                                                                                                                    if (lookup('role_var', '_host_specific_version', role='qbittorrent') | length > 0)
                                                                                                                    else qbittorrent_release_version.stdout }}/x86_64-qbittorrent-nox"

        # Type: string
        qbittorrent_role_host_release_url: "{{ 'https://github.com/userdocs/qbittorrent-nox-static/releases/latest/download/dependency-version.json'
                                            if lookup('role_var', '_host_branch', role='qbittorrent') != 'legacy'
                                            else 'https://github.com/userdocs/qbittorrent-nox-static-legacy/releases/latest/download/dependency-version.json' }}"

        # Type: string
        qbittorrent_role_host_lookup_libtorrent1: 'release-\(.qbittorrent)_v\(.libtorrent_1_2)'

        # Type: string
        qbittorrent_role_host_lookup_libtorrent2: 'release-\(.qbittorrent)_v\(.libtorrent_2_0)'

        # Type: string
        qbittorrent_role_host_release_lookup: "{{ qbittorrent_role_host_lookup_libtorrent2
                                               if lookup('role_var', '_host_branch', role='qbittorrent') == 'libtorrent2'
                                               else qbittorrent_role_host_lookup_libtorrent1 }}"

        # Type: string
        qbittorrent_role_host_version: |
          curl -sL {{ lookup('role_var', '_host_release_url', role='qbittorrent') }} | jq -r '. | "{{ lookup('role_var', '_host_release_lookup', role='qbittorrent') }}"'

        # Type: string
        qbittorrent_role_service_name: "saltbox_managed_{{ qbittorrent_name }}.service"

        # Type: string
        qbittorrent_role_service_after: "network-online.target docker.service"

        # Type: string
        qbittorrent_role_service_requires: "network-online.target docker.service"

        # Type: string
        qbittorrent_role_service_wants: ""

        ```

    === "Instance-level"

        ```yaml
        # Options are: libtorrent1 (latest), libtorrent2 (latest) or legacy (4.3.9)
        # Type: string
        qbittorrent2_host_branch: libtorrent1

        # Example being "release-4.4.5_v1.2.18"
        # If this is set then the above branch logic is ignored
        # Type: string
        qbittorrent2_host_specific_version: ""

        # Lookup variables
        # Type: string
        qbittorrent2_host_download_endpoint: "{{ 'https://github.com/userdocs/qbittorrent-nox-static/releases/download/'
                                              if lookup('role_var', '_host_branch', role='qbittorrent') != 'legacy'
                                              else 'https://github.com/userdocs/qbittorrent-nox-static-legacy/releases/download/' }}"

        # Type: string
        qbittorrent2_host_download_url: "{{ lookup('role_var', '_host_download_endpoint', role='qbittorrent') }}{{ lookup('role_var', '_host_specific_version', role='qbittorrent')
                                                                                                                if (lookup('role_var', '_host_specific_version', role='qbittorrent') | length > 0)
                                                                                                                else qbittorrent_release_version.stdout }}/x86_64-qbittorrent-nox"

        # Type: string
        qbittorrent2_host_release_url: "{{ 'https://github.com/userdocs/qbittorrent-nox-static/releases/latest/download/dependency-version.json'
                                        if lookup('role_var', '_host_branch', role='qbittorrent') != 'legacy'
                                        else 'https://github.com/userdocs/qbittorrent-nox-static-legacy/releases/latest/download/dependency-version.json' }}"

        # Type: string
        qbittorrent2_host_lookup_libtorrent1: 'release-\(.qbittorrent)_v\(.libtorrent_1_2)'

        # Type: string
        qbittorrent2_host_lookup_libtorrent2: 'release-\(.qbittorrent)_v\(.libtorrent_2_0)'

        # Type: string
        qbittorrent2_host_release_lookup: "{{ qbittorrent_role_host_lookup_libtorrent2
                                           if lookup('role_var', '_host_branch', role='qbittorrent') == 'libtorrent2'
                                           else qbittorrent_role_host_lookup_libtorrent1 }}"

        # Type: string
        qbittorrent2_host_version: |
          curl -sL {{ lookup('role_var', '_host_release_url', role='qbittorrent') }} | jq -r '. | "{{ lookup('role_var', '_host_release_lookup', role='qbittorrent') }}"'

        # Type: string
        qbittorrent2_service_name: "saltbox_managed_{{ qbittorrent_name }}.service"

        # Type: string
        qbittorrent2_service_after: "network-online.target docker.service"

        # Type: string
        qbittorrent2_service_requires: "network-online.target docker.service"

        # Type: string
        qbittorrent2_service_wants: ""

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        qbittorrent_role_paths_folder: "{{ qbittorrent_name }}"

        # Type: string
        qbittorrent_role_paths_location: "{{ server_appdata_path }}/{{ qbittorrent_role_paths_folder }}"

        # Type: string
        qbittorrent_role_paths_downloads_location: "{{ downloads_torrents_path }}/{{ qbittorrent_role_paths_folder }}"

        # Type: string
        qbittorrent_role_paths_conf: "{{ qbittorrent_role_paths_location }}/qBittorrent/qBittorrent.conf"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        qbittorrent2_paths_folder: "{{ qbittorrent_name }}"

        # Type: string
        qbittorrent2_paths_location: "{{ server_appdata_path }}/{{ qbittorrent_role_paths_folder }}"

        # Type: string
        qbittorrent2_paths_downloads_location: "{{ downloads_torrents_path }}/{{ qbittorrent_role_paths_folder }}"

        # Type: string
        qbittorrent2_paths_conf: "{{ qbittorrent_role_paths_location }}/qBittorrent/qBittorrent.conf"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        qbittorrent_role_web_subdomain: "{{ qbittorrent_name }}"

        # Type: string
        qbittorrent_role_web_domain: "{{ user.domain }}"

        # Type: string
        qbittorrent_role_web_port: "8080"

        # Type: string
        qbittorrent_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='qbittorrent') + '.' + lookup('role_var', '_web_domain', role='qbittorrent')
                                   if (lookup('role_var', '_web_subdomain', role='qbittorrent') | length > 0)
                                   else lookup('role_var', '_web_domain', role='qbittorrent')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        qbittorrent2_web_subdomain: "{{ qbittorrent_name }}"

        # Type: string
        qbittorrent2_web_domain: "{{ user.domain }}"

        # Type: string
        qbittorrent2_web_port: "8080"

        # Type: string
        qbittorrent2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='qbittorrent') + '.' + lookup('role_var', '_web_domain', role='qbittorrent')
                               if (lookup('role_var', '_web_subdomain', role='qbittorrent') | length > 0)
                               else lookup('role_var', '_web_domain', role='qbittorrent')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        qbittorrent_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='qbittorrent') }}"

        # Type: string
        qbittorrent_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='qbittorrent') }}"

        # Type: bool (true/false)
        qbittorrent_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        qbittorrent2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='qbittorrent') }}"

        # Type: string
        qbittorrent2_dns_zone: "{{ lookup('role_var', '_web_domain', role='qbittorrent') }}"

        # Type: bool (true/false)
        qbittorrent2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        qbittorrent_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        qbittorrent_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                         + (',themepark-' + qbittorrent_name
                                                           if (lookup('role_var', '_themepark_enabled', role='qbittorrent') and global_themepark_plugin_enabled)
                                                           else '') }}"

        # Type: string
        qbittorrent_role_traefik_middleware_custom: ""

        # Type: string
        qbittorrent_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        qbittorrent_role_traefik_enabled: true

        # Type: bool (true/false)
        qbittorrent_role_traefik_api_enabled: true

        # Type: string
        qbittorrent_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/command`) || PathPrefix(`/query`) || PathPrefix(`/login`) || PathPrefix(`/sync`)"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        qbittorrent2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        qbittorrent2_traefik_middleware_default: "{{ traefik_default_middleware
                                                     + (',themepark-' + qbittorrent_name
                                                       if (lookup('role_var', '_themepark_enabled', role='qbittorrent') and global_themepark_plugin_enabled)
                                                       else '') }}"

        # Type: string
        qbittorrent2_traefik_middleware_custom: ""

        # Type: string
        qbittorrent2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        qbittorrent2_traefik_enabled: true

        # Type: bool (true/false)
        qbittorrent2_traefik_api_enabled: true

        # Type: string
        qbittorrent2_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/command`) || PathPrefix(`/query`) || PathPrefix(`/login`) || PathPrefix(`/sync`)"

        ```

??? example "Theme"

    === "Role-level"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        qbittorrent_role_themepark_enabled: false

        # Type: string
        qbittorrent_role_themepark_app: "qbittorrent"

        # Type: string
        qbittorrent_role_themepark_theme: "{{ global_themepark_theme }}"

        # Type: string
        qbittorrent_role_themepark_domain: "{{ global_themepark_domain }}"

        # Type: list
        qbittorrent_role_themepark_addons: []

        # Type: string
        qbittorrent_role_themepark_headers: "\"content-security-policy: default-src 'self'; style-src 'self' 'unsafe-inline' theme-park.dev raw.githubusercontent.com use.fontawesome.com; img-src 'self' theme-park.dev raw.githubusercontent.com data:; script-src 'self' 'unsafe-inline'; object-src 'none'; form-action 'self'; frame-ancestors 'self'; font-src use.fontawesome.com;\""

        ```

    === "Instance-level"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        qbittorrent2_themepark_enabled: false

        # Type: string
        qbittorrent2_themepark_app: "qbittorrent"

        # Type: string
        qbittorrent2_themepark_theme: "{{ global_themepark_theme }}"

        # Type: string
        qbittorrent2_themepark_domain: "{{ global_themepark_domain }}"

        # Type: list
        qbittorrent2_themepark_addons: []

        # Type: string
        qbittorrent2_themepark_headers: "\"content-security-policy: default-src 'self'; style-src 'self' 'unsafe-inline' theme-park.dev raw.githubusercontent.com use.fontawesome.com; img-src 'self' theme-park.dev raw.githubusercontent.com data:; script-src 'self' 'unsafe-inline'; object-src 'none'; form-action 'self'; frame-ancestors 'self'; font-src use.fontawesome.com;\""

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        qbittorrent_role_docker_container: "{{ qbittorrent_name }}"

        # Image
        # Type: bool (true/false)
        qbittorrent_role_docker_image_pull: true

        # Type: string
        qbittorrent_role_docker_image_repo: "saltydk/qbittorrent"

        # Type: string
        qbittorrent_role_docker_image_tag: "latest"

        # Type: string
        qbittorrent_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='qbittorrent') }}:{{ lookup('role_var', '_docker_image_tag', role='qbittorrent') }}"

        # Ports
        # Type: string
        qbittorrent_role_docker_ports_56881: "{{ port_lookup_56881.meta.port
                                              if (port_lookup_56881.meta.port is defined) and (port_lookup_56881.meta.port | trim | length > 0)
                                              else '56881' }}"

        # Type: string
        qbittorrent_role_docker_ports_8080: "{{ port_lookup_8080.meta.port
                                             if (port_lookup_8080.meta.port is defined) and (port_lookup_8080.meta.port | trim | length > 0)
                                             else '8090' }}"

        # Type: string
        qbittorrent_role_web_port_lookup: "{{ lookup('role_var', '_web_port', role='qbittorrent') }}"

        # Type: list
        qbittorrent_role_docker_ports_defaults: 
          - "{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}:{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}"
          - "{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}:{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}/udp"

        # Type: list
        qbittorrent_role_docker_ports_custom: []

        # Envs
        # Type: dict
        qbittorrent_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          UMASK_SET: "002"
          S6_SERVICES_GRACETIME: "{{ (lookup('role_var', '_docker_stop_timeout', role='qbittorrent') | int * 1000) | string }}"

        # Type: dict
        qbittorrent_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        qbittorrent_role_docker_volumes_default: 
          - "{{ qbittorrent_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"

        # Type: list
        qbittorrent_role_docker_volumes_custom: []

        # Labels
        # Type: dict
        qbittorrent_role_docker_labels_default: {}

        # Type: dict
        qbittorrent_role_docker_labels_custom: {}

        # Hostname
        # Type: string
        qbittorrent_role_docker_hostname: "{{ qbittorrent_name }}"

        # Networks
        # Type: string
        qbittorrent_role_docker_networks_alias: "{{ qbittorrent_name }}"

        # Type: list
        qbittorrent_role_docker_networks_default: []

        # Type: list
        qbittorrent_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        qbittorrent_role_docker_restart_policy: unless-stopped

        # Stop Timeout
        # Type: int
        qbittorrent_role_docker_stop_timeout: 900

        # State
        # Type: string
        qbittorrent_role_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via create_docker_container
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        qbittorrent_role_docker_blkio_weight:

        # Type: int
        qbittorrent_role_docker_cpu_period:

        # Type: int
        qbittorrent_role_docker_cpu_quota:

        # Type: int
        qbittorrent_role_docker_cpu_shares:

        # Type: string
        qbittorrent_role_docker_cpus:

        # Type: string
        qbittorrent_role_docker_cpuset_cpus:

        # Type: string
        qbittorrent_role_docker_cpuset_mems:

        # Type: string
        qbittorrent_role_docker_kernel_memory:

        # Type: string
        qbittorrent_role_docker_memory:

        # Type: string
        qbittorrent_role_docker_memory_reservation:

        # Type: string
        qbittorrent_role_docker_memory_swap:

        # Type: int
        qbittorrent_role_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        qbittorrent_role_docker_cap_drop:

        # Type: list
        qbittorrent_role_docker_device_cgroup_rules:

        # Type: list
        qbittorrent_role_docker_device_read_bps:

        # Type: list
        qbittorrent_role_docker_device_read_iops:

        # Type: list
        qbittorrent_role_docker_device_requests:

        # Type: list
        qbittorrent_role_docker_device_write_bps:

        # Type: list
        qbittorrent_role_docker_device_write_iops:

        # Type: list
        qbittorrent_role_docker_devices:

        # Type: string
        qbittorrent_role_docker_devices_default:

        # Type: bool (true/false)
        qbittorrent_role_docker_privileged:

        # Type: list
        qbittorrent_role_docker_security_opts:

        # Networking
        # Type: list
        qbittorrent_role_docker_dns_opts:

        # Type: list
        qbittorrent_role_docker_dns_search_domains:

        # Type: list
        qbittorrent_role_docker_dns_servers:

        # Type: dict
        qbittorrent_role_docker_hosts:

        # Type: string
        qbittorrent_role_docker_hosts_use_common:

        # Type: string
        qbittorrent_role_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        qbittorrent_role_docker_keep_volumes:

        # Type: list
        qbittorrent_role_docker_mounts:

        # Type: string
        qbittorrent_role_docker_volume_driver:

        # Type: list
        qbittorrent_role_docker_volumes_from:

        # Type: string
        qbittorrent_role_docker_volumes_global:

        # Type: string
        qbittorrent_role_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        qbittorrent_role_docker_healthcheck:

        # Type: bool (true/false)
        qbittorrent_role_docker_init:

        # Type: string
        qbittorrent_role_docker_log_driver:

        # Type: dict
        qbittorrent_role_docker_log_options:

        # Type: bool (true/false)
        qbittorrent_role_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        qbittorrent_role_docker_auto_remove:

        # Type: list
        qbittorrent_role_docker_capabilities:

        # Type: string
        qbittorrent_role_docker_cgroup_parent:

        # Type: string
        qbittorrent_role_docker_cgroupns_mode:

        # Type: bool (true/false)
        qbittorrent_role_docker_cleanup:

        # Type: list
        qbittorrent_role_docker_commands:

        # Type: string
        qbittorrent_role_docker_create_timeout:

        # Type: string
        qbittorrent_role_docker_domainname:

        # Type: string
        qbittorrent_role_docker_entrypoint:

        # Type: string
        qbittorrent_role_docker_env_file:

        # Type: list
        qbittorrent_role_docker_exposed_ports:

        # Type: string
        qbittorrent_role_docker_force_kill:

        # Type: list
        qbittorrent_role_docker_groups:

        # Type: int
        qbittorrent_role_docker_healthy_wait_timeout:

        # Type: string
        qbittorrent_role_docker_ipc_mode:

        # Type: string
        qbittorrent_role_docker_kill_signal:

        # Type: string
        qbittorrent_role_docker_labels_use_common:

        # Type: list
        qbittorrent_role_docker_links:

        # Type: bool (true/false)
        qbittorrent_role_docker_oom_killer:

        # Type: int
        qbittorrent_role_docker_oom_score_adj:

        # Type: bool (true/false)
        qbittorrent_role_docker_paused:

        # Type: string
        qbittorrent_role_docker_pid_mode:

        # Type: bool (true/false)
        qbittorrent_role_docker_read_only:

        # Type: bool (true/false)
        qbittorrent_role_docker_recreate:

        # Type: int
        qbittorrent_role_docker_restart_retries:

        # Type: string
        qbittorrent_role_docker_runtime:

        # Type: string
        qbittorrent_role_docker_shm_size:

        # Type: dict
        qbittorrent_role_docker_storage_opts:

        # Type: list
        qbittorrent_role_docker_sysctls:

        # Type: list
        qbittorrent_role_docker_tmpfs:

        # Type: list
        qbittorrent_role_docker_ulimits:

        # Type: string
        qbittorrent_role_docker_user:

        # Type: string
        qbittorrent_role_docker_userns_mode:

        # Type: string
        qbittorrent_role_docker_uts:

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        qbittorrent2_docker_container: "{{ qbittorrent_name }}"

        # Image
        # Type: bool (true/false)
        qbittorrent2_docker_image_pull: true

        # Type: string
        qbittorrent2_docker_image_repo: "saltydk/qbittorrent"

        # Type: string
        qbittorrent2_docker_image_tag: "latest"

        # Type: string
        qbittorrent2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='qbittorrent') }}:{{ lookup('role_var', '_docker_image_tag', role='qbittorrent') }}"

        # Ports
        # Type: string
        qbittorrent2_docker_ports_56881: "{{ port_lookup_56881.meta.port
                                          if (port_lookup_56881.meta.port is defined) and (port_lookup_56881.meta.port | trim | length > 0)
                                          else '56881' }}"

        # Type: string
        qbittorrent2_docker_ports_8080: "{{ port_lookup_8080.meta.port
                                         if (port_lookup_8080.meta.port is defined) and (port_lookup_8080.meta.port | trim | length > 0)
                                         else '8090' }}"

        # Type: string
        qbittorrent2_web_port_lookup: "{{ lookup('role_var', '_web_port', role='qbittorrent') }}"

        # Type: list
        qbittorrent2_docker_ports_defaults: 
          - "{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}:{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}"
          - "{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}:{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}/udp"

        # Type: list
        qbittorrent2_docker_ports_custom: []

        # Envs
        # Type: dict
        qbittorrent2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          UMASK_SET: "002"
          S6_SERVICES_GRACETIME: "{{ (lookup('role_var', '_docker_stop_timeout', role='qbittorrent') | int * 1000) | string }}"

        # Type: dict
        qbittorrent2_docker_envs_custom: {}

        # Volumes
        # Type: list
        qbittorrent2_docker_volumes_default: 
          - "{{ qbittorrent_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"

        # Type: list
        qbittorrent2_docker_volumes_custom: []

        # Labels
        # Type: dict
        qbittorrent2_docker_labels_default: {}

        # Type: dict
        qbittorrent2_docker_labels_custom: {}

        # Hostname
        # Type: string
        qbittorrent2_docker_hostname: "{{ qbittorrent_name }}"

        # Networks
        # Type: string
        qbittorrent2_docker_networks_alias: "{{ qbittorrent_name }}"

        # Type: list
        qbittorrent2_docker_networks_default: []

        # Type: list
        qbittorrent2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        qbittorrent2_docker_restart_policy: unless-stopped

        # Stop Timeout
        # Type: int
        qbittorrent2_docker_stop_timeout: 900

        # State
        # Type: string
        qbittorrent2_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via lookup('docker_var', ...)
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        qbittorrent2_docker_blkio_weight:
        # Type: int
        qbittorrent2_docker_cpu_period:
        # Type: int
        qbittorrent2_docker_cpu_quota:
        # Type: int
        qbittorrent2_docker_cpu_shares:
        # Type: string
        qbittorrent2_docker_cpus:
        # Type: string
        qbittorrent2_docker_cpuset_cpus:
        # Type: string
        qbittorrent2_docker_cpuset_mems:
        # Type: string
        qbittorrent2_docker_kernel_memory:
        # Type: string
        qbittorrent2_docker_memory:
        # Type: string
        qbittorrent2_docker_memory_reservation:
        # Type: string
        qbittorrent2_docker_memory_swap:
        # Type: int
        qbittorrent2_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        qbittorrent2_docker_cap_drop:
        # Type: list
        qbittorrent2_docker_device_cgroup_rules:
        # Type: list
        qbittorrent2_docker_device_read_bps:
        # Type: list
        qbittorrent2_docker_device_read_iops:
        # Type: list
        qbittorrent2_docker_device_requests:
        # Type: list
        qbittorrent2_docker_device_write_bps:
        # Type: list
        qbittorrent2_docker_device_write_iops:
        # Type: list
        qbittorrent2_docker_devices:
        # Type: string
        qbittorrent2_docker_devices_default:
        # Type: bool (true/false)
        qbittorrent2_docker_privileged:
        # Type: list
        qbittorrent2_docker_security_opts:

        # Networking
        # Type: list
        qbittorrent2_docker_dns_opts:
        # Type: list
        qbittorrent2_docker_dns_search_domains:
        # Type: list
        qbittorrent2_docker_dns_servers:
        # Type: dict
        qbittorrent2_docker_hosts:
        # Type: string
        qbittorrent2_docker_hosts_use_common:
        # Type: string
        qbittorrent2_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        qbittorrent2_docker_keep_volumes:
        # Type: list
        qbittorrent2_docker_mounts:
        # Type: string
        qbittorrent2_docker_volume_driver:
        # Type: list
        qbittorrent2_docker_volumes_from:
        # Type: string
        qbittorrent2_docker_volumes_global:
        # Type: string
        qbittorrent2_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        qbittorrent2_docker_healthcheck:
        # Type: bool (true/false)
        qbittorrent2_docker_init:
        # Type: string
        qbittorrent2_docker_log_driver:
        # Type: dict
        qbittorrent2_docker_log_options:
        # Type: bool (true/false)
        qbittorrent2_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        qbittorrent2_docker_auto_remove:
        # Type: list
        qbittorrent2_docker_capabilities:
        # Type: string
        qbittorrent2_docker_cgroup_parent:
        # Type: string
        qbittorrent2_docker_cgroupns_mode:
        # Type: bool (true/false)
        qbittorrent2_docker_cleanup:
        # Type: list
        qbittorrent2_docker_commands:
        # Type: string
        qbittorrent2_docker_create_timeout:
        # Type: string
        qbittorrent2_docker_domainname:
        # Type: string
        qbittorrent2_docker_entrypoint:
        # Type: string
        qbittorrent2_docker_env_file:
        # Type: list
        qbittorrent2_docker_exposed_ports:
        # Type: string
        qbittorrent2_docker_force_kill:
        # Type: list
        qbittorrent2_docker_groups:
        # Type: int
        qbittorrent2_docker_healthy_wait_timeout:
        # Type: string
        qbittorrent2_docker_ipc_mode:
        # Type: string
        qbittorrent2_docker_kill_signal:
        # Type: string
        qbittorrent2_docker_labels_use_common:
        # Type: list
        qbittorrent2_docker_links:
        # Type: bool (true/false)
        qbittorrent2_docker_oom_killer:
        # Type: int
        qbittorrent2_docker_oom_score_adj:
        # Type: bool (true/false)
        qbittorrent2_docker_paused:
        # Type: string
        qbittorrent2_docker_pid_mode:
        # Type: bool (true/false)
        qbittorrent2_docker_read_only:
        # Type: bool (true/false)
        qbittorrent2_docker_recreate:
        # Type: int
        qbittorrent2_docker_restart_retries:
        # Type: string
        qbittorrent2_docker_runtime:
        # Type: string
        qbittorrent2_docker_shm_size:
        # Type: dict
        qbittorrent2_docker_storage_opts:
        # Type: list
        qbittorrent2_docker_sysctls:
        # Type: list
        qbittorrent2_docker_tmpfs:
        # Type: list
        qbittorrent2_docker_ulimits:
        # Type: string
        qbittorrent2_docker_user:
        # Type: string
        qbittorrent2_docker_userns_mode:
        # Type: string
        qbittorrent2_docker_uts:

        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        qbittorrent_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        qbittorrent_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        qbittorrent_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        qbittorrent_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        qbittorrent_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        qbittorrent_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        qbittorrent_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        qbittorrent_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        qbittorrent_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        qbittorrent_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        qbittorrent_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        qbittorrent_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        qbittorrent_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        qbittorrent_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        qbittorrent_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        qbittorrent_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        qbittorrent_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            qbittorrent_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "qbittorrent2.{{ user.domain }}"
              - "qbittorrent.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            qbittorrent_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'qbittorrent2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `qbittorrent2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        qbittorrent2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        qbittorrent2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        qbittorrent2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        qbittorrent2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        qbittorrent2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        qbittorrent2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        qbittorrent2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        qbittorrent2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        qbittorrent2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        qbittorrent2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        qbittorrent2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        qbittorrent2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        qbittorrent2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        qbittorrent2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        qbittorrent2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        qbittorrent2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        qbittorrent2_web_scheme:

        ```

        1.  Example:

            ```yaml
            qbittorrent2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "qbittorrent2.{{ user.domain }}"
              - "qbittorrent.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            qbittorrent2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'qbittorrent2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

## Next

Are you setting Saltbox up for the first time?  Continue to [NZBHydra2](nzbhydra2.md).

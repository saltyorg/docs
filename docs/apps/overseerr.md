---
hide:
  - tags
tags:
  - overseerr
---

# Overseerr

# What is it?

[Overseerr](https://overseerr.dev/) is a request management and media discovery tool built to work with your existing Plex ecosystem.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://overseerr.dev/){: .header-icons } | [:octicons-link-16: Docs](https://docs.overseerr.dev/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/sct/overseerr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/sctx/overseerr){: .header-icons }|

## 1. URL

- To access Overseerr, visit `https://overseerr._yourdomain.com_`

## 2. Settings

This setup needs to take place **AFTER** you've set up Plex, Radarr, and Sonarr, since it involves connections to all three of those.

You will need your API Keys from both Radarr and Sonarr.

1. Click "Sign In" and sign into your Plex account.

![](../images/overseerr/01-overseerr.png)

1. Click the "refresh" icon, then select your Plex server from the dropdown.  Click "Save Changes" to retrieve the libraries from Plex.

![](../images/overseerr/02-overseerr.png)

1. Scroll down and flip the switch on the libraries you want to expose for requests and discovery.  Click "Continue".

![](../images/overseerr/03-overseerr.png)

1. Click "Add Radarr Server".

![](../images/overseerr/04-overseerr.png)

1. On this screen:
    1. Check "Default server"
    2. Enter a name
    3. Enter `radarr` as the hostname
    4. Enter your Radarr API Key
    5. Click "Test" to connect to Radarr and retrieve Quality Profiles, etc.

![](../images/overseerr/05-overseerr.png)

1. Select a Quality, Root Folder, and Minimum Availability, then click "Add Server".  This will return you to the screen from the previous step. Click "Add Sonarr Server"

![](../images/overseerr/06-overseerr.png)

1. On this screen:
    1. Check "Default server"
    2. Enter a name
    3. Enter `sonarr` as the hostname
    4. Enter your Sonarr API Key
    5. Scroll down and click "Test" to connect to Sonarr and retrieve Quality Profiles, etc.

![](../images/overseerr/07-overseerr.png)

1. Select a Quality, Root Folder, and Minimum Availability for standard and Anime series.  Click  "Add Server".

![](../images/overseerr/08-overseerr.png)

1. Click "Finish Setup"

![](../images/overseerr/09-overseerr.png)

1. Click "Settings" over on the left.

![](../images/overseerr/10-overseerr.png)

1. Click "Users" on the left, then "Import Users From Plex"

![](../images/overseerr/11-overseerr.png)

1. Setup is complete.

![](../images/overseerr/12-overseerr.png)

## Next

Are you setting Saltbox up for the first time?  Continue to [Portainer](portainer.md).

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `overseerr_instances`.

    === "Role-level Override"

        Applies to all instances of overseerr:

        ```yaml
        overseerr_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `overseerr2`):

        ```yaml
        overseerr2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `overseerr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `overseerr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`overseerr_instances`"

        ```yaml
        # Type: list
        overseerr_instances: ["overseerr"]
        ```

        !!! example

            ```yaml
            # Type: list
            overseerr_instances: ["overseerr", "overseerr2"]
            ```

=== "Settings"

    === "Role-level"

        ??? variable string "`overseerr_role_log_level`"

            ```yaml
            # Type: string
            overseerr_role_log_level: "info"
            ```

    === "Instance-level"

        ??? variable string "`overseerr2_log_level`"

            ```yaml
            # Type: string
            overseerr2_log_level: "info"
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`overseerr_role_paths_folder`"

            ```yaml
            # Type: string
            overseerr_role_paths_folder: "{{ overseerr_name }}"
            ```

        ??? variable string "`overseerr_role_paths_location`"

            ```yaml
            # Type: string
            overseerr_role_paths_location: "{{ server_appdata_path }}/{{ overseerr_role_paths_folder }}"
            ```

        ??? variable string "`overseerr_role_paths_cache`"

            ```yaml
            # Type: string
            overseerr_role_paths_cache: "{{ overseerr_role_paths_location }}/cache"
            ```

        ??? variable string "`overseerr_role_paths_config_location`"

            ```yaml
            # Type: string
            overseerr_role_paths_config_location: "{{ overseerr_role_paths_location }}/settings.json"
            ```

    === "Instance-level"

        ??? variable string "`overseerr2_paths_folder`"

            ```yaml
            # Type: string
            overseerr2_paths_folder: "{{ overseerr_name }}"
            ```

        ??? variable string "`overseerr2_paths_location`"

            ```yaml
            # Type: string
            overseerr2_paths_location: "{{ server_appdata_path }}/{{ overseerr_role_paths_folder }}"
            ```

        ??? variable string "`overseerr2_paths_cache`"

            ```yaml
            # Type: string
            overseerr2_paths_cache: "{{ overseerr_role_paths_location }}/cache"
            ```

        ??? variable string "`overseerr2_paths_config_location`"

            ```yaml
            # Type: string
            overseerr2_paths_config_location: "{{ overseerr_role_paths_location }}/settings.json"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`overseerr_role_web_subdomain`"

            ```yaml
            # Type: string
            overseerr_role_web_subdomain: "{{ overseerr_name }}"
            ```

        ??? variable string "`overseerr_role_web_domain`"

            ```yaml
            # Type: string
            overseerr_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`overseerr_role_web_port`"

            ```yaml
            # Type: string
            overseerr_role_web_port: "5055"
            ```

        ??? variable string "`overseerr_role_web_url`"

            ```yaml
            # Type: string
            overseerr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='overseerr') + '.' + lookup('role_var', '_web_domain', role='overseerr')
                                     if (lookup('role_var', '_web_subdomain', role='overseerr') | length > 0)
                                     else lookup('role_var', '_web_domain', role='overseerr')) }}"
            ```

    === "Instance-level"

        ??? variable string "`overseerr2_web_subdomain`"

            ```yaml
            # Type: string
            overseerr2_web_subdomain: "{{ overseerr_name }}"
            ```

        ??? variable string "`overseerr2_web_domain`"

            ```yaml
            # Type: string
            overseerr2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`overseerr2_web_port`"

            ```yaml
            # Type: string
            overseerr2_web_port: "5055"
            ```

        ??? variable string "`overseerr2_web_url`"

            ```yaml
            # Type: string
                    overseerr2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='overseerr') + '.' + lookup('role_var', '_web_domain', role='overseerr')
                                         if (lookup('role_var', '_web_subdomain', role='overseerr') | length > 0)
                                         else lookup('role_var', '_web_domain', role='overseerr')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`overseerr_role_dns_record`"

            ```yaml
            # Type: string
            overseerr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='overseerr') }}"
            ```

        ??? variable string "`overseerr_role_dns_zone`"

            ```yaml
            # Type: string
            overseerr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='overseerr') }}"
            ```

        ??? variable bool "`overseerr_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            overseerr_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`overseerr2_dns_record`"

            ```yaml
            # Type: string
            overseerr2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='overseerr') }}"
            ```

        ??? variable string "`overseerr2_dns_zone`"

            ```yaml
            # Type: string
            overseerr2_dns_zone: "{{ lookup('role_var', '_web_domain', role='overseerr') }}"
            ```

        ??? variable bool "`overseerr2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            overseerr2_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`overseerr_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            overseerr_role_traefik_sso_middleware: ""
            ```

        ??? variable string "`overseerr_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            overseerr_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                           + (',themepark-' + overseerr_name
                                                             if (lookup('role_var', '_themepark_enabled', role='overseerr') and global_themepark_plugin_enabled)
                                                             else '') }}"
            ```

        ??? variable string "`overseerr_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            overseerr_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`overseerr_role_traefik_certresolver`"

            ```yaml
            # Type: string
            overseerr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`overseerr_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            overseerr_role_traefik_enabled: true
            ```

        ??? variable bool "`overseerr_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            overseerr_role_traefik_api_enabled: false
            ```

        ??? variable string "`overseerr_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            overseerr_role_traefik_api_endpoint: ""
            ```

    === "Instance-level"

        ??? variable string "`overseerr2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            overseerr2_traefik_sso_middleware: ""
            ```

        ??? variable string "`overseerr2_traefik_middleware_default`"

            ```yaml
            # Type: string
                    overseerr2_traefik_middleware_default: "{{ traefik_default_middleware
                                                               + (',themepark-' + overseerr_name
                                                                 if (lookup('role_var', '_themepark_enabled', role='overseerr') and global_themepark_plugin_enabled)
                                                                 else '') }}"
            ```

        ??? variable string "`overseerr2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            overseerr2_traefik_middleware_custom: ""
            ```

        ??? variable string "`overseerr2_traefik_certresolver`"

            ```yaml
            # Type: string
            overseerr2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`overseerr2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            overseerr2_traefik_enabled: true
            ```

        ??? variable bool "`overseerr2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            overseerr2_traefik_api_enabled: false
            ```

        ??? variable string "`overseerr2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            overseerr2_traefik_api_endpoint: ""
            ```

=== "Theme"

    === "Role-level"

        ??? variable bool "`overseerr_role_themepark_enabled`"

            ```yaml
            # Options can be found at https://github.com/themepark-dev/theme.park
            # Type: bool (true/false)
            overseerr_role_themepark_enabled: false
            ```

        ??? variable string "`overseerr_role_themepark_app`"

            ```yaml
            # Type: string
            overseerr_role_themepark_app: "overseerr"
            ```

        ??? variable string "`overseerr_role_themepark_theme`"

            ```yaml
            # Type: string
            overseerr_role_themepark_theme: "{{ global_themepark_theme }}"
            ```

        ??? variable string "`overseerr_role_themepark_domain`"

            ```yaml
            # Type: string
            overseerr_role_themepark_domain: "{{ global_themepark_domain }}"
            ```

        ??? variable list "`overseerr_role_themepark_addons`"

            ```yaml
            # Type: list
            overseerr_role_themepark_addons: []
            ```

    === "Instance-level"

        ??? variable bool "`overseerr2_themepark_enabled`"

            # Options can be found at https://github.com/themepark-dev/theme.park

            ```yaml
            # Type: bool (true/false)
            overseerr2_themepark_enabled: false
            ```

        ??? variable string "`overseerr2_themepark_app`"

            ```yaml
            # Type: string
            overseerr2_themepark_app: "overseerr"
            ```

        ??? variable string "`overseerr2_themepark_theme`"

            ```yaml
            # Type: string
            overseerr2_themepark_theme: "{{ global_themepark_theme }}"
            ```

        ??? variable string "`overseerr2_themepark_domain`"

            ```yaml
            # Type: string
            overseerr2_themepark_domain: "{{ global_themepark_domain }}"
            ```

        ??? variable list "`overseerr2_themepark_addons`"

            ```yaml
            # Type: list
            overseerr2_themepark_addons: []
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`overseerr_role_docker_container`"

            ```yaml
            # Type: string
            overseerr_role_docker_container: "{{ overseerr_name }}"
            ```

        ##### Image

        ??? variable bool "`overseerr_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            overseerr_role_docker_image_pull: true
            ```

        ??? variable string "`overseerr_role_docker_image_repo`"

            ```yaml
            # Type: string
            overseerr_role_docker_image_repo: "sctx/overseerr"
            ```

        ??? variable string "`overseerr_role_docker_image_tag`"

            ```yaml
            # Type: string
            overseerr_role_docker_image_tag: "latest"
            ```

        ??? variable string "`overseerr_role_docker_image`"

            ```yaml
            # Type: string
            overseerr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='overseerr') }}:{{ lookup('role_var', '_docker_image_tag', role='overseerr') }}"
            ```

        ##### Envs

        ??? variable dict "`overseerr_role_docker_envs_default`"

            ```yaml
            # Type: dict
            overseerr_role_docker_envs_default: 
              UMASK: "002"
              TZ: "{{ tz }}"
              LOG_LEVEL: "{{ lookup('role_var', '_log_level', role='overseerr') }}"
            ```

        ??? variable dict "`overseerr_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            overseerr_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`overseerr_role_docker_volumes_default`"

            ```yaml
            # Type: list
            overseerr_role_docker_volumes_default: 
              - "{{ overseerr_role_paths_location }}:/app/config"
            ```

        ??? variable list "`overseerr_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            overseerr_role_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable dict "`overseerr_role_docker_labels_default`"

            ```yaml
            # Type: dict
            overseerr_role_docker_labels_default: {}
            ```

        ??? variable dict "`overseerr_role_docker_labels_custom`"

            ```yaml
            # Type: dict
            overseerr_role_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`overseerr_role_docker_hostname`"

            ```yaml
            # Type: string
            overseerr_role_docker_hostname: "{{ overseerr_name }}"
            ```

        ##### Networks

        ??? variable string "`overseerr_role_docker_networks_alias`"

            ```yaml
            # Type: string
            overseerr_role_docker_networks_alias: "{{ overseerr_name }}"
            ```

        ??? variable list "`overseerr_role_docker_networks_default`"

            ```yaml
            # Type: list
            overseerr_role_docker_networks_default: []
            ```

        ??? variable list "`overseerr_role_docker_networks_custom`"

            ```yaml
            # Type: list
            overseerr_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`overseerr_role_docker_restart_policy`"

            ```yaml
            # Type: string
            overseerr_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`overseerr_role_docker_state`"

            ```yaml
            # Type: string
            overseerr_role_docker_state: started
            ```

        ##### User

        ??? variable string "`overseerr_role_docker_user`"

            ```yaml
            # Type: string
            overseerr_role_docker_user: "{{ uid }}:{{ gid }}"
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`overseerr2_docker_container`"

            ```yaml
            # Type: string
            overseerr2_docker_container: "{{ overseerr_name }}"
            ```

        ##### Image

        ??? variable bool "`overseerr2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            overseerr2_docker_image_pull: true
            ```

        ??? variable string "`overseerr2_docker_image_repo`"

            ```yaml
            # Type: string
            overseerr2_docker_image_repo: "sctx/overseerr"
            ```

        ??? variable string "`overseerr2_docker_image_tag`"

            ```yaml
            # Type: string
            overseerr2_docker_image_tag: "latest"
            ```

        ??? variable string "`overseerr2_docker_image`"

            ```yaml
            # Type: string
            overseerr2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='overseerr') }}:{{ lookup('role_var', '_docker_image_tag', role='overseerr') }}"
            ```

        ##### Envs

        ??? variable dict "`overseerr2_docker_envs_default`"

            ```yaml
            # Type: dict
                    overseerr2_docker_envs_default: 
                      UMASK: "002"
                      TZ: "{{ tz }}"
                      LOG_LEVEL: "{{ lookup('role_var', '_log_level', role='overseerr') }}"
            ```

        ??? variable dict "`overseerr2_docker_envs_custom`"

            ```yaml
            # Type: dict
            overseerr2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`overseerr2_docker_volumes_default`"

            ```yaml
            # Type: list
                    overseerr2_docker_volumes_default: 
                      - "{{ overseerr_role_paths_location }}:/app/config"
            ```

        ??? variable list "`overseerr2_docker_volumes_custom`"

            ```yaml
            # Type: list
            overseerr2_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable dict "`overseerr2_docker_labels_default`"

            ```yaml
            # Type: dict
            overseerr2_docker_labels_default: {}
            ```

        ??? variable dict "`overseerr2_docker_labels_custom`"

            ```yaml
            # Type: dict
            overseerr2_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`overseerr2_docker_hostname`"

            ```yaml
            # Type: string
            overseerr2_docker_hostname: "{{ overseerr_name }}"
            ```

        ##### Networks

        ??? variable string "`overseerr2_docker_networks_alias`"

            ```yaml
            # Type: string
            overseerr2_docker_networks_alias: "{{ overseerr_name }}"
            ```

        ??? variable list "`overseerr2_docker_networks_default`"

            ```yaml
            # Type: list
            overseerr2_docker_networks_default: []
            ```

        ??? variable list "`overseerr2_docker_networks_custom`"

            ```yaml
            # Type: list
            overseerr2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`overseerr2_docker_restart_policy`"

            ```yaml
            # Type: string
            overseerr2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`overseerr2_docker_state`"

            ```yaml
            # Type: string
            overseerr2_docker_state: started
            ```

        ##### User

        ??? variable string "`overseerr2_docker_user`"

            ```yaml
            # Type: string
            overseerr2_docker_user: "{{ uid }}:{{ gid }}"
            ```

=== "Docker+"

    #### Additional Docker Options

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    === "Role-level"

        ##### Resource Limits

        ??? variable int "`overseerr_role_docker_blkio_weight`"

            ```yaml
            # Type: int
            overseerr_role_docker_blkio_weight:
            ```

        ??? variable int "`overseerr_role_docker_cpu_period`"

            ```yaml
            # Type: int
            overseerr_role_docker_cpu_period:
            ```

        ??? variable int "`overseerr_role_docker_cpu_quota`"

            ```yaml
            # Type: int
            overseerr_role_docker_cpu_quota:
            ```

        ??? variable int "`overseerr_role_docker_cpu_shares`"

            ```yaml
            # Type: int
            overseerr_role_docker_cpu_shares:
            ```

        ??? variable string "`overseerr_role_docker_cpus`"

            ```yaml
            # Type: string
            overseerr_role_docker_cpus:
            ```

        ??? variable string "`overseerr_role_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            overseerr_role_docker_cpuset_cpus:
            ```

        ??? variable string "`overseerr_role_docker_cpuset_mems`"

            ```yaml
            # Type: string
            overseerr_role_docker_cpuset_mems:
            ```

        ??? variable string "`overseerr_role_docker_kernel_memory`"

            ```yaml
            # Type: string
            overseerr_role_docker_kernel_memory:
            ```

        ??? variable string "`overseerr_role_docker_memory`"

            ```yaml
            # Type: string
            overseerr_role_docker_memory:
            ```

        ??? variable string "`overseerr_role_docker_memory_reservation`"

            ```yaml
            # Type: string
            overseerr_role_docker_memory_reservation:
            ```

        ??? variable string "`overseerr_role_docker_memory_swap`"

            ```yaml
            # Type: string
            overseerr_role_docker_memory_swap:
            ```

        ??? variable int "`overseerr_role_docker_memory_swappiness`"

            ```yaml
            # Type: int
            overseerr_role_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`overseerr_role_docker_cap_drop`"

            ```yaml
            # Type: list
            overseerr_role_docker_cap_drop:
            ```

        ??? variable list "`overseerr_role_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            overseerr_role_docker_device_cgroup_rules:
            ```

        ??? variable list "`overseerr_role_docker_device_read_bps`"

            ```yaml
            # Type: list
            overseerr_role_docker_device_read_bps:
            ```

        ??? variable list "`overseerr_role_docker_device_read_iops`"

            ```yaml
            # Type: list
            overseerr_role_docker_device_read_iops:
            ```

        ??? variable list "`overseerr_role_docker_device_requests`"

            ```yaml
            # Type: list
            overseerr_role_docker_device_requests:
            ```

        ??? variable list "`overseerr_role_docker_device_write_bps`"

            ```yaml
            # Type: list
            overseerr_role_docker_device_write_bps:
            ```

        ??? variable list "`overseerr_role_docker_device_write_iops`"

            ```yaml
            # Type: list
            overseerr_role_docker_device_write_iops:
            ```

        ??? variable list "`overseerr_role_docker_devices`"

            ```yaml
            # Type: list
            overseerr_role_docker_devices:
            ```

        ??? variable string "`overseerr_role_docker_devices_default`"

            ```yaml
            # Type: string
            overseerr_role_docker_devices_default:
            ```

        ??? variable bool "`overseerr_role_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            overseerr_role_docker_privileged:
            ```

        ??? variable list "`overseerr_role_docker_security_opts`"

            ```yaml
            # Type: list
            overseerr_role_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`overseerr_role_docker_dns_opts`"

            ```yaml
            # Type: list
            overseerr_role_docker_dns_opts:
            ```

        ??? variable list "`overseerr_role_docker_dns_search_domains`"

            ```yaml
            # Type: list
            overseerr_role_docker_dns_search_domains:
            ```

        ??? variable list "`overseerr_role_docker_dns_servers`"

            ```yaml
            # Type: list
            overseerr_role_docker_dns_servers:
            ```

        ??? variable dict "`overseerr_role_docker_hosts`"

            ```yaml
            # Type: dict
            overseerr_role_docker_hosts:
            ```

        ??? variable string "`overseerr_role_docker_hosts_use_common`"

            ```yaml
            # Type: string
            overseerr_role_docker_hosts_use_common:
            ```

        ??? variable string "`overseerr_role_docker_network_mode`"

            ```yaml
            # Type: string
            overseerr_role_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`overseerr_role_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            overseerr_role_docker_keep_volumes:
            ```

        ??? variable list "`overseerr_role_docker_mounts`"

            ```yaml
            # Type: list
            overseerr_role_docker_mounts:
            ```

        ??? variable string "`overseerr_role_docker_volume_driver`"

            ```yaml
            # Type: string
            overseerr_role_docker_volume_driver:
            ```

        ??? variable list "`overseerr_role_docker_volumes_from`"

            ```yaml
            # Type: list
            overseerr_role_docker_volumes_from:
            ```

        ??? variable string "`overseerr_role_docker_volumes_global`"

            ```yaml
            # Type: string
            overseerr_role_docker_volumes_global:
            ```

        ??? variable string "`overseerr_role_docker_working_dir`"

            ```yaml
            # Type: string
            overseerr_role_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`overseerr_role_docker_healthcheck`"

            ```yaml
            # Type: dict
            overseerr_role_docker_healthcheck:
            ```

        ??? variable bool "`overseerr_role_docker_init`"

            ```yaml
            # Type: bool (true/false)
            overseerr_role_docker_init:
            ```

        ??? variable string "`overseerr_role_docker_log_driver`"

            ```yaml
            # Type: string
            overseerr_role_docker_log_driver:
            ```

        ??? variable dict "`overseerr_role_docker_log_options`"

            ```yaml
            # Type: dict
            overseerr_role_docker_log_options:
            ```

        ??? variable bool "`overseerr_role_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            overseerr_role_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`overseerr_role_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            overseerr_role_docker_auto_remove:
            ```

        ??? variable list "`overseerr_role_docker_capabilities`"

            ```yaml
            # Type: list
            overseerr_role_docker_capabilities:
            ```

        ??? variable string "`overseerr_role_docker_cgroup_parent`"

            ```yaml
            # Type: string
            overseerr_role_docker_cgroup_parent:
            ```

        ??? variable string "`overseerr_role_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            overseerr_role_docker_cgroupns_mode:
            ```

        ??? variable bool "`overseerr_role_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            overseerr_role_docker_cleanup:
            ```

        ??? variable list "`overseerr_role_docker_commands`"

            ```yaml
            # Type: list
            overseerr_role_docker_commands:
            ```

        ??? variable string "`overseerr_role_docker_create_timeout`"

            ```yaml
            # Type: string
            overseerr_role_docker_create_timeout:
            ```

        ??? variable string "`overseerr_role_docker_domainname`"

            ```yaml
            # Type: string
            overseerr_role_docker_domainname:
            ```

        ??? variable string "`overseerr_role_docker_entrypoint`"

            ```yaml
            # Type: string
            overseerr_role_docker_entrypoint:
            ```

        ??? variable string "`overseerr_role_docker_env_file`"

            ```yaml
            # Type: string
            overseerr_role_docker_env_file:
            ```

        ??? variable list "`overseerr_role_docker_exposed_ports`"

            ```yaml
            # Type: list
            overseerr_role_docker_exposed_ports:
            ```

        ??? variable string "`overseerr_role_docker_force_kill`"

            ```yaml
            # Type: string
            overseerr_role_docker_force_kill:
            ```

        ??? variable list "`overseerr_role_docker_groups`"

            ```yaml
            # Type: list
            overseerr_role_docker_groups:
            ```

        ??? variable int "`overseerr_role_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            overseerr_role_docker_healthy_wait_timeout:
            ```

        ??? variable string "`overseerr_role_docker_ipc_mode`"

            ```yaml
            # Type: string
            overseerr_role_docker_ipc_mode:
            ```

        ??? variable string "`overseerr_role_docker_kill_signal`"

            ```yaml
            # Type: string
            overseerr_role_docker_kill_signal:
            ```

        ??? variable string "`overseerr_role_docker_labels_use_common`"

            ```yaml
            # Type: string
            overseerr_role_docker_labels_use_common:
            ```

        ??? variable list "`overseerr_role_docker_links`"

            ```yaml
            # Type: list
            overseerr_role_docker_links:
            ```

        ??? variable bool "`overseerr_role_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            overseerr_role_docker_oom_killer:
            ```

        ??? variable int "`overseerr_role_docker_oom_score_adj`"

            ```yaml
            # Type: int
            overseerr_role_docker_oom_score_adj:
            ```

        ??? variable bool "`overseerr_role_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            overseerr_role_docker_paused:
            ```

        ??? variable string "`overseerr_role_docker_pid_mode`"

            ```yaml
            # Type: string
            overseerr_role_docker_pid_mode:
            ```

        ??? variable list "`overseerr_role_docker_ports`"

            ```yaml
            # Type: list
            overseerr_role_docker_ports:
            ```

        ??? variable bool "`overseerr_role_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            overseerr_role_docker_read_only:
            ```

        ??? variable bool "`overseerr_role_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            overseerr_role_docker_recreate:
            ```

        ??? variable int "`overseerr_role_docker_restart_retries`"

            ```yaml
            # Type: int
            overseerr_role_docker_restart_retries:
            ```

        ??? variable string "`overseerr_role_docker_runtime`"

            ```yaml
            # Type: string
            overseerr_role_docker_runtime:
            ```

        ??? variable string "`overseerr_role_docker_shm_size`"

            ```yaml
            # Type: string
            overseerr_role_docker_shm_size:
            ```

        ??? variable int "`overseerr_role_docker_stop_timeout`"

            ```yaml
            # Type: int
            overseerr_role_docker_stop_timeout:
            ```

        ??? variable dict "`overseerr_role_docker_storage_opts`"

            ```yaml
            # Type: dict
            overseerr_role_docker_storage_opts:
            ```

        ??? variable list "`overseerr_role_docker_sysctls`"

            ```yaml
            # Type: list
            overseerr_role_docker_sysctls:
            ```

        ??? variable list "`overseerr_role_docker_tmpfs`"

            ```yaml
            # Type: list
            overseerr_role_docker_tmpfs:
            ```

        ??? variable list "`overseerr_role_docker_ulimits`"

            ```yaml
            # Type: list
            overseerr_role_docker_ulimits:
            ```

        ??? variable string "`overseerr_role_docker_userns_mode`"

            ```yaml
            # Type: string
            overseerr_role_docker_userns_mode:
            ```

        ??? variable string "`overseerr_role_docker_uts`"

            ```yaml
            # Type: string
            overseerr_role_docker_uts:
            ```

    === "Instance-level"

        ##### Resource Limits

        ??? variable int "`overseerr2_docker_blkio_weight`"

            ```yaml
            # Type: int
            overseerr2_docker_blkio_weight:
            ```

        ??? variable int "`overseerr2_docker_cpu_period`"

            ```yaml
            # Type: int
            overseerr2_docker_cpu_period:
            ```

        ??? variable int "`overseerr2_docker_cpu_quota`"

            ```yaml
            # Type: int
            overseerr2_docker_cpu_quota:
            ```

        ??? variable int "`overseerr2_docker_cpu_shares`"

            ```yaml
            # Type: int
            overseerr2_docker_cpu_shares:
            ```

        ??? variable string "`overseerr2_docker_cpus`"

            ```yaml
            # Type: string
            overseerr2_docker_cpus:
            ```

        ??? variable string "`overseerr2_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            overseerr2_docker_cpuset_cpus:
            ```

        ??? variable string "`overseerr2_docker_cpuset_mems`"

            ```yaml
            # Type: string
            overseerr2_docker_cpuset_mems:
            ```

        ??? variable string "`overseerr2_docker_kernel_memory`"

            ```yaml
            # Type: string
            overseerr2_docker_kernel_memory:
            ```

        ??? variable string "`overseerr2_docker_memory`"

            ```yaml
            # Type: string
            overseerr2_docker_memory:
            ```

        ??? variable string "`overseerr2_docker_memory_reservation`"

            ```yaml
            # Type: string
            overseerr2_docker_memory_reservation:
            ```

        ??? variable string "`overseerr2_docker_memory_swap`"

            ```yaml
            # Type: string
            overseerr2_docker_memory_swap:
            ```

        ??? variable int "`overseerr2_docker_memory_swappiness`"

            ```yaml
            # Type: int
            overseerr2_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`overseerr2_docker_cap_drop`"

            ```yaml
            # Type: list
            overseerr2_docker_cap_drop:
            ```

        ??? variable list "`overseerr2_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            overseerr2_docker_device_cgroup_rules:
            ```

        ??? variable list "`overseerr2_docker_device_read_bps`"

            ```yaml
            # Type: list
            overseerr2_docker_device_read_bps:
            ```

        ??? variable list "`overseerr2_docker_device_read_iops`"

            ```yaml
            # Type: list
            overseerr2_docker_device_read_iops:
            ```

        ??? variable list "`overseerr2_docker_device_requests`"

            ```yaml
            # Type: list
            overseerr2_docker_device_requests:
            ```

        ??? variable list "`overseerr2_docker_device_write_bps`"

            ```yaml
            # Type: list
            overseerr2_docker_device_write_bps:
            ```

        ??? variable list "`overseerr2_docker_device_write_iops`"

            ```yaml
            # Type: list
            overseerr2_docker_device_write_iops:
            ```

        ??? variable list "`overseerr2_docker_devices`"

            ```yaml
            # Type: list
            overseerr2_docker_devices:
            ```

        ??? variable string "`overseerr2_docker_devices_default`"

            ```yaml
            # Type: string
            overseerr2_docker_devices_default:
            ```

        ??? variable bool "`overseerr2_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            overseerr2_docker_privileged:
            ```

        ??? variable list "`overseerr2_docker_security_opts`"

            ```yaml
            # Type: list
            overseerr2_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`overseerr2_docker_dns_opts`"

            ```yaml
            # Type: list
            overseerr2_docker_dns_opts:
            ```

        ??? variable list "`overseerr2_docker_dns_search_domains`"

            ```yaml
            # Type: list
            overseerr2_docker_dns_search_domains:
            ```

        ??? variable list "`overseerr2_docker_dns_servers`"

            ```yaml
            # Type: list
            overseerr2_docker_dns_servers:
            ```

        ??? variable dict "`overseerr2_docker_hosts`"

            ```yaml
            # Type: dict
            overseerr2_docker_hosts:
            ```

        ??? variable string "`overseerr2_docker_hosts_use_common`"

            ```yaml
            # Type: string
            overseerr2_docker_hosts_use_common:
            ```

        ??? variable string "`overseerr2_docker_network_mode`"

            ```yaml
            # Type: string
            overseerr2_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`overseerr2_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            overseerr2_docker_keep_volumes:
            ```

        ??? variable list "`overseerr2_docker_mounts`"

            ```yaml
            # Type: list
            overseerr2_docker_mounts:
            ```

        ??? variable string "`overseerr2_docker_volume_driver`"

            ```yaml
            # Type: string
            overseerr2_docker_volume_driver:
            ```

        ??? variable list "`overseerr2_docker_volumes_from`"

            ```yaml
            # Type: list
            overseerr2_docker_volumes_from:
            ```

        ??? variable string "`overseerr2_docker_volumes_global`"

            ```yaml
            # Type: string
            overseerr2_docker_volumes_global:
            ```

        ??? variable string "`overseerr2_docker_working_dir`"

            ```yaml
            # Type: string
            overseerr2_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`overseerr2_docker_healthcheck`"

            ```yaml
            # Type: dict
            overseerr2_docker_healthcheck:
            ```

        ??? variable bool "`overseerr2_docker_init`"

            ```yaml
            # Type: bool (true/false)
            overseerr2_docker_init:
            ```

        ??? variable string "`overseerr2_docker_log_driver`"

            ```yaml
            # Type: string
            overseerr2_docker_log_driver:
            ```

        ??? variable dict "`overseerr2_docker_log_options`"

            ```yaml
            # Type: dict
            overseerr2_docker_log_options:
            ```

        ??? variable bool "`overseerr2_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            overseerr2_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`overseerr2_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            overseerr2_docker_auto_remove:
            ```

        ??? variable list "`overseerr2_docker_capabilities`"

            ```yaml
            # Type: list
            overseerr2_docker_capabilities:
            ```

        ??? variable string "`overseerr2_docker_cgroup_parent`"

            ```yaml
            # Type: string
            overseerr2_docker_cgroup_parent:
            ```

        ??? variable string "`overseerr2_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            overseerr2_docker_cgroupns_mode:
            ```

        ??? variable bool "`overseerr2_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            overseerr2_docker_cleanup:
            ```

        ??? variable list "`overseerr2_docker_commands`"

            ```yaml
            # Type: list
            overseerr2_docker_commands:
            ```

        ??? variable string "`overseerr2_docker_create_timeout`"

            ```yaml
            # Type: string
            overseerr2_docker_create_timeout:
            ```

        ??? variable string "`overseerr2_docker_domainname`"

            ```yaml
            # Type: string
            overseerr2_docker_domainname:
            ```

        ??? variable string "`overseerr2_docker_entrypoint`"

            ```yaml
            # Type: string
            overseerr2_docker_entrypoint:
            ```

        ??? variable string "`overseerr2_docker_env_file`"

            ```yaml
            # Type: string
            overseerr2_docker_env_file:
            ```

        ??? variable list "`overseerr2_docker_exposed_ports`"

            ```yaml
            # Type: list
            overseerr2_docker_exposed_ports:
            ```

        ??? variable string "`overseerr2_docker_force_kill`"

            ```yaml
            # Type: string
            overseerr2_docker_force_kill:
            ```

        ??? variable list "`overseerr2_docker_groups`"

            ```yaml
            # Type: list
            overseerr2_docker_groups:
            ```

        ??? variable int "`overseerr2_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            overseerr2_docker_healthy_wait_timeout:
            ```

        ??? variable string "`overseerr2_docker_ipc_mode`"

            ```yaml
            # Type: string
            overseerr2_docker_ipc_mode:
            ```

        ??? variable string "`overseerr2_docker_kill_signal`"

            ```yaml
            # Type: string
            overseerr2_docker_kill_signal:
            ```

        ??? variable string "`overseerr2_docker_labels_use_common`"

            ```yaml
            # Type: string
            overseerr2_docker_labels_use_common:
            ```

        ??? variable list "`overseerr2_docker_links`"

            ```yaml
            # Type: list
            overseerr2_docker_links:
            ```

        ??? variable bool "`overseerr2_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            overseerr2_docker_oom_killer:
            ```

        ??? variable int "`overseerr2_docker_oom_score_adj`"

            ```yaml
            # Type: int
            overseerr2_docker_oom_score_adj:
            ```

        ??? variable bool "`overseerr2_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            overseerr2_docker_paused:
            ```

        ??? variable string "`overseerr2_docker_pid_mode`"

            ```yaml
            # Type: string
            overseerr2_docker_pid_mode:
            ```

        ??? variable list "`overseerr2_docker_ports`"

            ```yaml
            # Type: list
            overseerr2_docker_ports:
            ```

        ??? variable bool "`overseerr2_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            overseerr2_docker_read_only:
            ```

        ??? variable bool "`overseerr2_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            overseerr2_docker_recreate:
            ```

        ??? variable int "`overseerr2_docker_restart_retries`"

            ```yaml
            # Type: int
            overseerr2_docker_restart_retries:
            ```

        ??? variable string "`overseerr2_docker_runtime`"

            ```yaml
            # Type: string
            overseerr2_docker_runtime:
            ```

        ??? variable string "`overseerr2_docker_shm_size`"

            ```yaml
            # Type: string
            overseerr2_docker_shm_size:
            ```

        ??? variable int "`overseerr2_docker_stop_timeout`"

            ```yaml
            # Type: int
            overseerr2_docker_stop_timeout:
            ```

        ??? variable dict "`overseerr2_docker_storage_opts`"

            ```yaml
            # Type: dict
            overseerr2_docker_storage_opts:
            ```

        ??? variable list "`overseerr2_docker_sysctls`"

            ```yaml
            # Type: list
            overseerr2_docker_sysctls:
            ```

        ??? variable list "`overseerr2_docker_tmpfs`"

            ```yaml
            # Type: list
            overseerr2_docker_tmpfs:
            ```

        ??? variable list "`overseerr2_docker_ulimits`"

            ```yaml
            # Type: list
            overseerr2_docker_ulimits:
            ```

        ??? variable string "`overseerr2_docker_userns_mode`"

            ```yaml
            # Type: string
            overseerr2_docker_userns_mode:
            ```

        ??? variable string "`overseerr2_docker_uts`"

            ```yaml
            # Type: string
            overseerr2_docker_uts:
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`overseerr_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            overseerr_role_autoheal_enabled: true
            ```

        ??? variable string "`overseerr_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            overseerr_role_depends_on: ""
            ```

        ??? variable string "`overseerr_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            overseerr_role_depends_on_delay: "0"
            ```

        ??? variable string "`overseerr_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            overseerr_role_depends_on_healthchecks:
            ```

        ??? variable bool "`overseerr_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            overseerr_role_diun_enabled: true
            ```

        ??? variable bool "`overseerr_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            overseerr_role_dns_enabled: true
            ```

        ??? variable bool "`overseerr_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            overseerr_role_docker_controller: true
            ```

        ??? variable bool "`overseerr_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            overseerr_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`overseerr_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            overseerr_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`overseerr_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            overseerr_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`overseerr_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            overseerr_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`overseerr_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            overseerr_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`overseerr_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            overseerr_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`overseerr_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            overseerr_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`overseerr_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            overseerr_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                overseerr_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "overseerr2.{{ user.domain }}"
                  - "overseerr.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`overseerr_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            overseerr_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                overseerr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'overseerr2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`overseerr_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            overseerr_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `overseerr2`):

        ??? variable bool "`overseerr2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            overseerr2_autoheal_enabled: true
            ```

        ??? variable string "`overseerr2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            overseerr2_depends_on: ""
            ```

        ??? variable string "`overseerr2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            overseerr2_depends_on_delay: "0"
            ```

        ??? variable string "`overseerr2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            overseerr2_depends_on_healthchecks:
            ```

        ??? variable bool "`overseerr2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            overseerr2_diun_enabled: true
            ```

        ??? variable bool "`overseerr2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            overseerr2_dns_enabled: true
            ```

        ??? variable bool "`overseerr2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            overseerr2_docker_controller: true
            ```

        ??? variable bool "`overseerr2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            overseerr2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`overseerr2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            overseerr2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`overseerr2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            overseerr2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`overseerr2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            overseerr2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`overseerr2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            overseerr2_traefik_robot_enabled: true
            ```

        ??? variable bool "`overseerr2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            overseerr2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`overseerr2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            overseerr2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`overseerr2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            overseerr2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                overseerr2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "overseerr2.{{ user.domain }}"
                  - "overseerr.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`overseerr2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            overseerr2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                overseerr2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'overseerr2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`overseerr2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            overseerr2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
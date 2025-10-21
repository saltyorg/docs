---
hide:
  - tags
tags:
  - whisparr
---

# Whisparr

## What is it?

[Whisparr](https://wiki.servarr.com/whisparr) is an adult movie collection manager for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new movies and will interface with clients and indexers to grab, sort, and rename them. It can also be configured to automatically upgrade the quality of existing files in the library when a better quality format becomes available. Note that only one type of a given movie is supported. If you want both an 4k version and 1080p version of a given movie you will need multiple instances.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into whisparr with the email and password you set up upon installation.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://wiki.servarr.com/whisparr){: .header-icons } | [:octicons-link-16: Docs](https://wiki.servarr.com/en/whisparr/quick-start-guide){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Whisparr/Whisparr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/whisparr){: .header-icons }|

### 1. Installation

``` shell

sb install whisparr

```

### 2. URL

- To access whisparr, visit `https://whisparr._yourdomain.com_`

### 3. Setup

Whisparr works more or less the same as the other apps in the arr suite, since this is a fork of sonarr.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `whisparr_instances`.

    === "Role-level Override"

        Applies to all instances of whisparr:

        ```yaml
        whisparr_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `whisparr2`):

        ```yaml
        whisparr2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `whisparr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `whisparr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`whisparr_instances`"

        ```yaml
        # Type: list
        whisparr_instances: ["whisparr"]
        ```

        !!! example

            ```yaml
            # Type: list
            whisparr_instances: ["whisparr", "whisparr2"]
            ```

=== "Settings"

    === "Role-level"

        ??? variable bool "`whisparr_role_external_auth`"

            ```yaml
            # Type: bool (true/false)
            whisparr_role_external_auth: true
            ```

    === "Instance-level"

        ??? variable bool "`whisparr2_external_auth`"

            ```yaml
            # Type: bool (true/false)
            whisparr2_external_auth: true
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`whisparr_paths_folder`"

            ```yaml
            # Type: string
            whisparr_paths_folder: "{{ whisparr_name }}"
            ```

        ??? variable string "`whisparr_paths_location`"

            ```yaml
            # Type: string
            whisparr_paths_location: "{{ server_appdata_path }}/{{ whisparr_paths_folder }}"
            ```

        ??? variable string "`whisparr_paths_config_location`"

            ```yaml
            # Type: string
            whisparr_paths_config_location: "{{ whisparr_paths_location }}/config.xml"
            ```

    === "Instance-level"

        ??? variable string "`whisparr_paths_folder`"

            ```yaml
            # Type: string
            whisparr_paths_folder: "{{ whisparr_name }}"
            ```

        ??? variable string "`whisparr_paths_location`"

            ```yaml
            # Type: string
            whisparr_paths_location: "{{ server_appdata_path }}/{{ whisparr_paths_folder }}"
            ```

        ??? variable string "`whisparr_paths_config_location`"

            ```yaml
            # Type: string
            whisparr_paths_config_location: "{{ whisparr_paths_location }}/config.xml"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`whisparr_role_web_subdomain`"

            ```yaml
            # Type: string
            whisparr_role_web_subdomain: "{{ whisparr_name }}"
            ```

        ??? variable string "`whisparr_role_web_domain`"

            ```yaml
            # Type: string
            whisparr_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`whisparr_role_web_port`"

            ```yaml
            # Type: string
            whisparr_role_web_port: "6969"
            ```

        ??? variable string "`whisparr_role_web_url`"

            ```yaml
            # Type: string
            whisparr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='whisparr') + '.' + lookup('role_var', '_web_domain', role='whisparr')
                                    if (lookup('role_var', '_web_subdomain', role='whisparr') | length > 0)
                                    else lookup('role_var', '_web_domain', role='whisparr')) }}"
            ```

    === "Instance-level"

        ??? variable string "`whisparr2_web_subdomain`"

            ```yaml
            # Type: string
            whisparr2_web_subdomain: "{{ whisparr_name }}"
            ```

        ??? variable string "`whisparr2_web_domain`"

            ```yaml
            # Type: string
            whisparr2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`whisparr2_web_port`"

            ```yaml
            # Type: string
            whisparr2_web_port: "6969"
            ```

        ??? variable string "`whisparr2_web_url`"

            ```yaml
            # Type: string
                    whisparr2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='whisparr') + '.' + lookup('role_var', '_web_domain', role='whisparr')
                                        if (lookup('role_var', '_web_subdomain', role='whisparr') | length > 0)
                                        else lookup('role_var', '_web_domain', role='whisparr')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`whisparr_role_dns_record`"

            ```yaml
            # Type: string
            whisparr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='whisparr') }}"
            ```

        ??? variable string "`whisparr_role_dns_zone`"

            ```yaml
            # Type: string
            whisparr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='whisparr') }}"
            ```

        ??? variable bool "`whisparr_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            whisparr_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`whisparr2_dns_record`"

            ```yaml
            # Type: string
            whisparr2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='whisparr') }}"
            ```

        ??? variable string "`whisparr2_dns_zone`"

            ```yaml
            # Type: string
            whisparr2_dns_zone: "{{ lookup('role_var', '_web_domain', role='whisparr') }}"
            ```

        ??? variable bool "`whisparr2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            whisparr2_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`whisparr_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            whisparr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`whisparr_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            whisparr_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                          + (',themepark-' + whisparr_name
                                                            if (lookup('role_var', '_themepark_enabled', role='whisparr') and global_themepark_plugin_enabled)
                                                            else '') }}"
            ```

        ??? variable string "`whisparr_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            whisparr_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`whisparr_role_traefik_certresolver`"

            ```yaml
            # Type: string
            whisparr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`whisparr_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            whisparr_role_traefik_enabled: true
            ```

        ??? variable bool "`whisparr_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            whisparr_role_traefik_api_enabled: true
            ```

        ??? variable string "`whisparr_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            whisparr_role_traefik_api_endpoint: "PathPrefix(`/api`)"
            ```

    === "Instance-level"

        ??? variable string "`whisparr2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            whisparr2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`whisparr2_traefik_middleware_default`"

            ```yaml
            # Type: string
                    whisparr2_traefik_middleware_default: "{{ traefik_default_middleware
                                                              + (',themepark-' + whisparr_name
                                                                if (lookup('role_var', '_themepark_enabled', role='whisparr') and global_themepark_plugin_enabled)
                                                                else '') }}"
            ```

        ??? variable string "`whisparr2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            whisparr2_traefik_middleware_custom: ""
            ```

        ??? variable string "`whisparr2_traefik_certresolver`"

            ```yaml
            # Type: string
            whisparr2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`whisparr2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            whisparr2_traefik_enabled: true
            ```

        ??? variable bool "`whisparr2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            whisparr2_traefik_api_enabled: true
            ```

        ??? variable string "`whisparr2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            whisparr2_traefik_api_endpoint: "PathPrefix(`/api`)"
            ```

=== "Theme"

    === "Role-level"

        ??? variable bool "`whisparr_role_themepark_enabled`"

            ```yaml
            # Options can be found at https://github.com/themepark-dev/theme.park
            # Type: bool (true/false)
            whisparr_role_themepark_enabled: false
            ```

        ??? variable string "`whisparr_role_themepark_app`"

            ```yaml
            # Type: string
            whisparr_role_themepark_app: "whisparr"
            ```

        ??? variable string "`whisparr_role_themepark_theme`"

            ```yaml
            # Type: string
            whisparr_role_themepark_theme: "{{ global_themepark_theme }}"
            ```

        ??? variable string "`whisparr_role_themepark_domain`"

            ```yaml
            # Type: string
            whisparr_role_themepark_domain: "{{ global_themepark_domain }}"
            ```

        ??? variable list "`whisparr_role_themepark_addons`"

            ```yaml
            # Type: list
            whisparr_role_themepark_addons: []
            ```

    === "Instance-level"

        ??? variable bool "`whisparr2_themepark_enabled`"

            # Options can be found at https://github.com/themepark-dev/theme.park

            ```yaml
            # Type: bool (true/false)
            whisparr2_themepark_enabled: false
            ```

        ??? variable string "`whisparr2_themepark_app`"

            ```yaml
            # Type: string
            whisparr2_themepark_app: "whisparr"
            ```

        ??? variable string "`whisparr2_themepark_theme`"

            ```yaml
            # Type: string
            whisparr2_themepark_theme: "{{ global_themepark_theme }}"
            ```

        ??? variable string "`whisparr2_themepark_domain`"

            ```yaml
            # Type: string
            whisparr2_themepark_domain: "{{ global_themepark_domain }}"
            ```

        ??? variable list "`whisparr2_themepark_addons`"

            ```yaml
            # Type: list
            whisparr2_themepark_addons: []
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`whisparr_role_docker_container`"

            ```yaml
            # Type: string
            whisparr_role_docker_container: "{{ whisparr_name }}"
            ```

        ##### Image

        ??? variable bool "`whisparr_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            whisparr_role_docker_image_pull: true
            ```

        ??? variable string "`whisparr_role_docker_image_repo`"

            ```yaml
            # Type: string
            whisparr_role_docker_image_repo: "ghcr.io/hotio/whisparr"
            ```

        ??? variable string "`whisparr_role_docker_image_tag`"

            ```yaml
            # Type: string
            whisparr_role_docker_image_tag: "nightly"
            ```

        ??? variable string "`whisparr_role_docker_image`"

            ```yaml
            # Type: string
            whisparr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='whisparr') }}:{{ lookup('role_var', '_docker_image_tag', role='whisparr') }}"
            ```

        ##### Envs

        ??? variable dict "`whisparr_role_docker_envs_default`"

            ```yaml
            # Type: dict
            whisparr_role_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              UMASK: "002"
              TZ: "{{ tz }}"
            ```

        ??? variable dict "`whisparr_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            whisparr_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`whisparr_role_docker_volumes_default`"

            ```yaml
            # Type: list
            whisparr_role_docker_volumes_default: 
              - "{{ whisparr_paths_location }}:/config"
              - "{{ server_appdata_path }}/scripts:/scripts"
            ```

        ??? variable list "`whisparr_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            whisparr_role_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable dict "`whisparr_role_docker_labels_default`"

            ```yaml
            # Type: dict
            whisparr_role_docker_labels_default: {}
            ```

        ??? variable dict "`whisparr_role_docker_labels_custom`"

            ```yaml
            # Type: dict
            whisparr_role_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`whisparr_role_docker_hostname`"

            ```yaml
            # Type: string
            whisparr_role_docker_hostname: "{{ whisparr_name }}"
            ```

        ##### Networks

        ??? variable string "`whisparr_role_docker_networks_alias`"

            ```yaml
            # Type: string
            whisparr_role_docker_networks_alias: "{{ whisparr_name }}"
            ```

        ??? variable list "`whisparr_role_docker_networks_default`"

            ```yaml
            # Type: list
            whisparr_role_docker_networks_default: []
            ```

        ??? variable list "`whisparr_role_docker_networks_custom`"

            ```yaml
            # Type: list
            whisparr_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`whisparr_role_docker_restart_policy`"

            ```yaml
            # Type: string
            whisparr_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`whisparr_role_docker_state`"

            ```yaml
            # Type: string
            whisparr_role_docker_state: started
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`whisparr2_docker_container`"

            ```yaml
            # Type: string
            whisparr2_docker_container: "{{ whisparr_name }}"
            ```

        ##### Image

        ??? variable bool "`whisparr2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            whisparr2_docker_image_pull: true
            ```

        ??? variable string "`whisparr2_docker_image_repo`"

            ```yaml
            # Type: string
            whisparr2_docker_image_repo: "ghcr.io/hotio/whisparr"
            ```

        ??? variable string "`whisparr2_docker_image_tag`"

            ```yaml
            # Type: string
            whisparr2_docker_image_tag: "nightly"
            ```

        ??? variable string "`whisparr2_docker_image`"

            ```yaml
            # Type: string
            whisparr2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='whisparr') }}:{{ lookup('role_var', '_docker_image_tag', role='whisparr') }}"
            ```

        ##### Envs

        ??? variable dict "`whisparr2_docker_envs_default`"

            ```yaml
            # Type: dict
                    whisparr2_docker_envs_default: 
                      PUID: "{{ uid }}"
                      PGID: "{{ gid }}"
                      UMASK: "002"
                      TZ: "{{ tz }}"
            ```

        ??? variable dict "`whisparr2_docker_envs_custom`"

            ```yaml
            # Type: dict
            whisparr2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`whisparr2_docker_volumes_default`"

            ```yaml
            # Type: list
                    whisparr2_docker_volumes_default: 
                      - "{{ whisparr_paths_location }}:/config"
                      - "{{ server_appdata_path }}/scripts:/scripts"
            ```

        ??? variable list "`whisparr2_docker_volumes_custom`"

            ```yaml
            # Type: list
            whisparr2_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable dict "`whisparr2_docker_labels_default`"

            ```yaml
            # Type: dict
            whisparr2_docker_labels_default: {}
            ```

        ??? variable dict "`whisparr2_docker_labels_custom`"

            ```yaml
            # Type: dict
            whisparr2_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`whisparr2_docker_hostname`"

            ```yaml
            # Type: string
            whisparr2_docker_hostname: "{{ whisparr_name }}"
            ```

        ##### Networks

        ??? variable string "`whisparr2_docker_networks_alias`"

            ```yaml
            # Type: string
            whisparr2_docker_networks_alias: "{{ whisparr_name }}"
            ```

        ??? variable list "`whisparr2_docker_networks_default`"

            ```yaml
            # Type: list
            whisparr2_docker_networks_default: []
            ```

        ??? variable list "`whisparr2_docker_networks_custom`"

            ```yaml
            # Type: list
            whisparr2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`whisparr2_docker_restart_policy`"

            ```yaml
            # Type: string
            whisparr2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`whisparr2_docker_state`"

            ```yaml
            # Type: string
            whisparr2_docker_state: started
            ```

=== "Docker+"

    #### Additional Docker Options

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    === "Role-level"

        ##### Resource Limits

        ??? variable int "`whisparr_role_docker_blkio_weight`"

            ```yaml
            # Type: int
            whisparr_role_docker_blkio_weight:
            ```

        ??? variable int "`whisparr_role_docker_cpu_period`"

            ```yaml
            # Type: int
            whisparr_role_docker_cpu_period:
            ```

        ??? variable int "`whisparr_role_docker_cpu_quota`"

            ```yaml
            # Type: int
            whisparr_role_docker_cpu_quota:
            ```

        ??? variable int "`whisparr_role_docker_cpu_shares`"

            ```yaml
            # Type: int
            whisparr_role_docker_cpu_shares:
            ```

        ??? variable string "`whisparr_role_docker_cpus`"

            ```yaml
            # Type: string
            whisparr_role_docker_cpus:
            ```

        ??? variable string "`whisparr_role_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            whisparr_role_docker_cpuset_cpus:
            ```

        ??? variable string "`whisparr_role_docker_cpuset_mems`"

            ```yaml
            # Type: string
            whisparr_role_docker_cpuset_mems:
            ```

        ??? variable string "`whisparr_role_docker_kernel_memory`"

            ```yaml
            # Type: string
            whisparr_role_docker_kernel_memory:
            ```

        ??? variable string "`whisparr_role_docker_memory`"

            ```yaml
            # Type: string
            whisparr_role_docker_memory:
            ```

        ??? variable string "`whisparr_role_docker_memory_reservation`"

            ```yaml
            # Type: string
            whisparr_role_docker_memory_reservation:
            ```

        ??? variable string "`whisparr_role_docker_memory_swap`"

            ```yaml
            # Type: string
            whisparr_role_docker_memory_swap:
            ```

        ??? variable int "`whisparr_role_docker_memory_swappiness`"

            ```yaml
            # Type: int
            whisparr_role_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`whisparr_role_docker_cap_drop`"

            ```yaml
            # Type: list
            whisparr_role_docker_cap_drop:
            ```

        ??? variable list "`whisparr_role_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            whisparr_role_docker_device_cgroup_rules:
            ```

        ??? variable list "`whisparr_role_docker_device_read_bps`"

            ```yaml
            # Type: list
            whisparr_role_docker_device_read_bps:
            ```

        ??? variable list "`whisparr_role_docker_device_read_iops`"

            ```yaml
            # Type: list
            whisparr_role_docker_device_read_iops:
            ```

        ??? variable list "`whisparr_role_docker_device_requests`"

            ```yaml
            # Type: list
            whisparr_role_docker_device_requests:
            ```

        ??? variable list "`whisparr_role_docker_device_write_bps`"

            ```yaml
            # Type: list
            whisparr_role_docker_device_write_bps:
            ```

        ??? variable list "`whisparr_role_docker_device_write_iops`"

            ```yaml
            # Type: list
            whisparr_role_docker_device_write_iops:
            ```

        ??? variable list "`whisparr_role_docker_devices`"

            ```yaml
            # Type: list
            whisparr_role_docker_devices:
            ```

        ??? variable string "`whisparr_role_docker_devices_default`"

            ```yaml
            # Type: string
            whisparr_role_docker_devices_default:
            ```

        ??? variable bool "`whisparr_role_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            whisparr_role_docker_privileged:
            ```

        ??? variable list "`whisparr_role_docker_security_opts`"

            ```yaml
            # Type: list
            whisparr_role_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`whisparr_role_docker_dns_opts`"

            ```yaml
            # Type: list
            whisparr_role_docker_dns_opts:
            ```

        ??? variable list "`whisparr_role_docker_dns_search_domains`"

            ```yaml
            # Type: list
            whisparr_role_docker_dns_search_domains:
            ```

        ??? variable list "`whisparr_role_docker_dns_servers`"

            ```yaml
            # Type: list
            whisparr_role_docker_dns_servers:
            ```

        ??? variable dict "`whisparr_role_docker_hosts`"

            ```yaml
            # Type: dict
            whisparr_role_docker_hosts:
            ```

        ??? variable string "`whisparr_role_docker_hosts_use_common`"

            ```yaml
            # Type: string
            whisparr_role_docker_hosts_use_common:
            ```

        ??? variable string "`whisparr_role_docker_network_mode`"

            ```yaml
            # Type: string
            whisparr_role_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`whisparr_role_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            whisparr_role_docker_keep_volumes:
            ```

        ??? variable list "`whisparr_role_docker_mounts`"

            ```yaml
            # Type: list
            whisparr_role_docker_mounts:
            ```

        ??? variable string "`whisparr_role_docker_volume_driver`"

            ```yaml
            # Type: string
            whisparr_role_docker_volume_driver:
            ```

        ??? variable list "`whisparr_role_docker_volumes_from`"

            ```yaml
            # Type: list
            whisparr_role_docker_volumes_from:
            ```

        ??? variable string "`whisparr_role_docker_volumes_global`"

            ```yaml
            # Type: string
            whisparr_role_docker_volumes_global:
            ```

        ??? variable string "`whisparr_role_docker_working_dir`"

            ```yaml
            # Type: string
            whisparr_role_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`whisparr_role_docker_healthcheck`"

            ```yaml
            # Type: dict
            whisparr_role_docker_healthcheck:
            ```

        ??? variable bool "`whisparr_role_docker_init`"

            ```yaml
            # Type: bool (true/false)
            whisparr_role_docker_init:
            ```

        ??? variable string "`whisparr_role_docker_log_driver`"

            ```yaml
            # Type: string
            whisparr_role_docker_log_driver:
            ```

        ??? variable dict "`whisparr_role_docker_log_options`"

            ```yaml
            # Type: dict
            whisparr_role_docker_log_options:
            ```

        ??? variable bool "`whisparr_role_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            whisparr_role_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`whisparr_role_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            whisparr_role_docker_auto_remove:
            ```

        ??? variable list "`whisparr_role_docker_capabilities`"

            ```yaml
            # Type: list
            whisparr_role_docker_capabilities:
            ```

        ??? variable string "`whisparr_role_docker_cgroup_parent`"

            ```yaml
            # Type: string
            whisparr_role_docker_cgroup_parent:
            ```

        ??? variable string "`whisparr_role_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            whisparr_role_docker_cgroupns_mode:
            ```

        ??? variable bool "`whisparr_role_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            whisparr_role_docker_cleanup:
            ```

        ??? variable list "`whisparr_role_docker_commands`"

            ```yaml
            # Type: list
            whisparr_role_docker_commands:
            ```

        ??? variable string "`whisparr_role_docker_create_timeout`"

            ```yaml
            # Type: string
            whisparr_role_docker_create_timeout:
            ```

        ??? variable string "`whisparr_role_docker_domainname`"

            ```yaml
            # Type: string
            whisparr_role_docker_domainname:
            ```

        ??? variable string "`whisparr_role_docker_entrypoint`"

            ```yaml
            # Type: string
            whisparr_role_docker_entrypoint:
            ```

        ??? variable string "`whisparr_role_docker_env_file`"

            ```yaml
            # Type: string
            whisparr_role_docker_env_file:
            ```

        ??? variable list "`whisparr_role_docker_exposed_ports`"

            ```yaml
            # Type: list
            whisparr_role_docker_exposed_ports:
            ```

        ??? variable string "`whisparr_role_docker_force_kill`"

            ```yaml
            # Type: string
            whisparr_role_docker_force_kill:
            ```

        ??? variable list "`whisparr_role_docker_groups`"

            ```yaml
            # Type: list
            whisparr_role_docker_groups:
            ```

        ??? variable int "`whisparr_role_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            whisparr_role_docker_healthy_wait_timeout:
            ```

        ??? variable string "`whisparr_role_docker_ipc_mode`"

            ```yaml
            # Type: string
            whisparr_role_docker_ipc_mode:
            ```

        ??? variable string "`whisparr_role_docker_kill_signal`"

            ```yaml
            # Type: string
            whisparr_role_docker_kill_signal:
            ```

        ??? variable string "`whisparr_role_docker_labels_use_common`"

            ```yaml
            # Type: string
            whisparr_role_docker_labels_use_common:
            ```

        ??? variable list "`whisparr_role_docker_links`"

            ```yaml
            # Type: list
            whisparr_role_docker_links:
            ```

        ??? variable bool "`whisparr_role_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            whisparr_role_docker_oom_killer:
            ```

        ??? variable int "`whisparr_role_docker_oom_score_adj`"

            ```yaml
            # Type: int
            whisparr_role_docker_oom_score_adj:
            ```

        ??? variable bool "`whisparr_role_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            whisparr_role_docker_paused:
            ```

        ??? variable string "`whisparr_role_docker_pid_mode`"

            ```yaml
            # Type: string
            whisparr_role_docker_pid_mode:
            ```

        ??? variable list "`whisparr_role_docker_ports`"

            ```yaml
            # Type: list
            whisparr_role_docker_ports:
            ```

        ??? variable bool "`whisparr_role_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            whisparr_role_docker_read_only:
            ```

        ??? variable bool "`whisparr_role_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            whisparr_role_docker_recreate:
            ```

        ??? variable int "`whisparr_role_docker_restart_retries`"

            ```yaml
            # Type: int
            whisparr_role_docker_restart_retries:
            ```

        ??? variable string "`whisparr_role_docker_runtime`"

            ```yaml
            # Type: string
            whisparr_role_docker_runtime:
            ```

        ??? variable string "`whisparr_role_docker_shm_size`"

            ```yaml
            # Type: string
            whisparr_role_docker_shm_size:
            ```

        ??? variable int "`whisparr_role_docker_stop_timeout`"

            ```yaml
            # Type: int
            whisparr_role_docker_stop_timeout:
            ```

        ??? variable dict "`whisparr_role_docker_storage_opts`"

            ```yaml
            # Type: dict
            whisparr_role_docker_storage_opts:
            ```

        ??? variable list "`whisparr_role_docker_sysctls`"

            ```yaml
            # Type: list
            whisparr_role_docker_sysctls:
            ```

        ??? variable list "`whisparr_role_docker_tmpfs`"

            ```yaml
            # Type: list
            whisparr_role_docker_tmpfs:
            ```

        ??? variable list "`whisparr_role_docker_ulimits`"

            ```yaml
            # Type: list
            whisparr_role_docker_ulimits:
            ```

        ??? variable string "`whisparr_role_docker_user`"

            ```yaml
            # Type: string
            whisparr_role_docker_user:
            ```

        ??? variable string "`whisparr_role_docker_userns_mode`"

            ```yaml
            # Type: string
            whisparr_role_docker_userns_mode:
            ```

        ??? variable string "`whisparr_role_docker_uts`"

            ```yaml
            # Type: string
            whisparr_role_docker_uts:
            ```

    === "Instance-level"

        ##### Resource Limits

        ??? variable int "`whisparr2_docker_blkio_weight`"

            ```yaml
            # Type: int
            whisparr2_docker_blkio_weight:
            ```

        ??? variable int "`whisparr2_docker_cpu_period`"

            ```yaml
            # Type: int
            whisparr2_docker_cpu_period:
            ```

        ??? variable int "`whisparr2_docker_cpu_quota`"

            ```yaml
            # Type: int
            whisparr2_docker_cpu_quota:
            ```

        ??? variable int "`whisparr2_docker_cpu_shares`"

            ```yaml
            # Type: int
            whisparr2_docker_cpu_shares:
            ```

        ??? variable string "`whisparr2_docker_cpus`"

            ```yaml
            # Type: string
            whisparr2_docker_cpus:
            ```

        ??? variable string "`whisparr2_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            whisparr2_docker_cpuset_cpus:
            ```

        ??? variable string "`whisparr2_docker_cpuset_mems`"

            ```yaml
            # Type: string
            whisparr2_docker_cpuset_mems:
            ```

        ??? variable string "`whisparr2_docker_kernel_memory`"

            ```yaml
            # Type: string
            whisparr2_docker_kernel_memory:
            ```

        ??? variable string "`whisparr2_docker_memory`"

            ```yaml
            # Type: string
            whisparr2_docker_memory:
            ```

        ??? variable string "`whisparr2_docker_memory_reservation`"

            ```yaml
            # Type: string
            whisparr2_docker_memory_reservation:
            ```

        ??? variable string "`whisparr2_docker_memory_swap`"

            ```yaml
            # Type: string
            whisparr2_docker_memory_swap:
            ```

        ??? variable int "`whisparr2_docker_memory_swappiness`"

            ```yaml
            # Type: int
            whisparr2_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`whisparr2_docker_cap_drop`"

            ```yaml
            # Type: list
            whisparr2_docker_cap_drop:
            ```

        ??? variable list "`whisparr2_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            whisparr2_docker_device_cgroup_rules:
            ```

        ??? variable list "`whisparr2_docker_device_read_bps`"

            ```yaml
            # Type: list
            whisparr2_docker_device_read_bps:
            ```

        ??? variable list "`whisparr2_docker_device_read_iops`"

            ```yaml
            # Type: list
            whisparr2_docker_device_read_iops:
            ```

        ??? variable list "`whisparr2_docker_device_requests`"

            ```yaml
            # Type: list
            whisparr2_docker_device_requests:
            ```

        ??? variable list "`whisparr2_docker_device_write_bps`"

            ```yaml
            # Type: list
            whisparr2_docker_device_write_bps:
            ```

        ??? variable list "`whisparr2_docker_device_write_iops`"

            ```yaml
            # Type: list
            whisparr2_docker_device_write_iops:
            ```

        ??? variable list "`whisparr2_docker_devices`"

            ```yaml
            # Type: list
            whisparr2_docker_devices:
            ```

        ??? variable string "`whisparr2_docker_devices_default`"

            ```yaml
            # Type: string
            whisparr2_docker_devices_default:
            ```

        ??? variable bool "`whisparr2_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            whisparr2_docker_privileged:
            ```

        ??? variable list "`whisparr2_docker_security_opts`"

            ```yaml
            # Type: list
            whisparr2_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`whisparr2_docker_dns_opts`"

            ```yaml
            # Type: list
            whisparr2_docker_dns_opts:
            ```

        ??? variable list "`whisparr2_docker_dns_search_domains`"

            ```yaml
            # Type: list
            whisparr2_docker_dns_search_domains:
            ```

        ??? variable list "`whisparr2_docker_dns_servers`"

            ```yaml
            # Type: list
            whisparr2_docker_dns_servers:
            ```

        ??? variable dict "`whisparr2_docker_hosts`"

            ```yaml
            # Type: dict
            whisparr2_docker_hosts:
            ```

        ??? variable string "`whisparr2_docker_hosts_use_common`"

            ```yaml
            # Type: string
            whisparr2_docker_hosts_use_common:
            ```

        ??? variable string "`whisparr2_docker_network_mode`"

            ```yaml
            # Type: string
            whisparr2_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`whisparr2_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            whisparr2_docker_keep_volumes:
            ```

        ??? variable list "`whisparr2_docker_mounts`"

            ```yaml
            # Type: list
            whisparr2_docker_mounts:
            ```

        ??? variable string "`whisparr2_docker_volume_driver`"

            ```yaml
            # Type: string
            whisparr2_docker_volume_driver:
            ```

        ??? variable list "`whisparr2_docker_volumes_from`"

            ```yaml
            # Type: list
            whisparr2_docker_volumes_from:
            ```

        ??? variable string "`whisparr2_docker_volumes_global`"

            ```yaml
            # Type: string
            whisparr2_docker_volumes_global:
            ```

        ??? variable string "`whisparr2_docker_working_dir`"

            ```yaml
            # Type: string
            whisparr2_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`whisparr2_docker_healthcheck`"

            ```yaml
            # Type: dict
            whisparr2_docker_healthcheck:
            ```

        ??? variable bool "`whisparr2_docker_init`"

            ```yaml
            # Type: bool (true/false)
            whisparr2_docker_init:
            ```

        ??? variable string "`whisparr2_docker_log_driver`"

            ```yaml
            # Type: string
            whisparr2_docker_log_driver:
            ```

        ??? variable dict "`whisparr2_docker_log_options`"

            ```yaml
            # Type: dict
            whisparr2_docker_log_options:
            ```

        ??? variable bool "`whisparr2_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            whisparr2_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`whisparr2_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            whisparr2_docker_auto_remove:
            ```

        ??? variable list "`whisparr2_docker_capabilities`"

            ```yaml
            # Type: list
            whisparr2_docker_capabilities:
            ```

        ??? variable string "`whisparr2_docker_cgroup_parent`"

            ```yaml
            # Type: string
            whisparr2_docker_cgroup_parent:
            ```

        ??? variable string "`whisparr2_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            whisparr2_docker_cgroupns_mode:
            ```

        ??? variable bool "`whisparr2_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            whisparr2_docker_cleanup:
            ```

        ??? variable list "`whisparr2_docker_commands`"

            ```yaml
            # Type: list
            whisparr2_docker_commands:
            ```

        ??? variable string "`whisparr2_docker_create_timeout`"

            ```yaml
            # Type: string
            whisparr2_docker_create_timeout:
            ```

        ??? variable string "`whisparr2_docker_domainname`"

            ```yaml
            # Type: string
            whisparr2_docker_domainname:
            ```

        ??? variable string "`whisparr2_docker_entrypoint`"

            ```yaml
            # Type: string
            whisparr2_docker_entrypoint:
            ```

        ??? variable string "`whisparr2_docker_env_file`"

            ```yaml
            # Type: string
            whisparr2_docker_env_file:
            ```

        ??? variable list "`whisparr2_docker_exposed_ports`"

            ```yaml
            # Type: list
            whisparr2_docker_exposed_ports:
            ```

        ??? variable string "`whisparr2_docker_force_kill`"

            ```yaml
            # Type: string
            whisparr2_docker_force_kill:
            ```

        ??? variable list "`whisparr2_docker_groups`"

            ```yaml
            # Type: list
            whisparr2_docker_groups:
            ```

        ??? variable int "`whisparr2_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            whisparr2_docker_healthy_wait_timeout:
            ```

        ??? variable string "`whisparr2_docker_ipc_mode`"

            ```yaml
            # Type: string
            whisparr2_docker_ipc_mode:
            ```

        ??? variable string "`whisparr2_docker_kill_signal`"

            ```yaml
            # Type: string
            whisparr2_docker_kill_signal:
            ```

        ??? variable string "`whisparr2_docker_labels_use_common`"

            ```yaml
            # Type: string
            whisparr2_docker_labels_use_common:
            ```

        ??? variable list "`whisparr2_docker_links`"

            ```yaml
            # Type: list
            whisparr2_docker_links:
            ```

        ??? variable bool "`whisparr2_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            whisparr2_docker_oom_killer:
            ```

        ??? variable int "`whisparr2_docker_oom_score_adj`"

            ```yaml
            # Type: int
            whisparr2_docker_oom_score_adj:
            ```

        ??? variable bool "`whisparr2_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            whisparr2_docker_paused:
            ```

        ??? variable string "`whisparr2_docker_pid_mode`"

            ```yaml
            # Type: string
            whisparr2_docker_pid_mode:
            ```

        ??? variable list "`whisparr2_docker_ports`"

            ```yaml
            # Type: list
            whisparr2_docker_ports:
            ```

        ??? variable bool "`whisparr2_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            whisparr2_docker_read_only:
            ```

        ??? variable bool "`whisparr2_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            whisparr2_docker_recreate:
            ```

        ??? variable int "`whisparr2_docker_restart_retries`"

            ```yaml
            # Type: int
            whisparr2_docker_restart_retries:
            ```

        ??? variable string "`whisparr2_docker_runtime`"

            ```yaml
            # Type: string
            whisparr2_docker_runtime:
            ```

        ??? variable string "`whisparr2_docker_shm_size`"

            ```yaml
            # Type: string
            whisparr2_docker_shm_size:
            ```

        ??? variable int "`whisparr2_docker_stop_timeout`"

            ```yaml
            # Type: int
            whisparr2_docker_stop_timeout:
            ```

        ??? variable dict "`whisparr2_docker_storage_opts`"

            ```yaml
            # Type: dict
            whisparr2_docker_storage_opts:
            ```

        ??? variable list "`whisparr2_docker_sysctls`"

            ```yaml
            # Type: list
            whisparr2_docker_sysctls:
            ```

        ??? variable list "`whisparr2_docker_tmpfs`"

            ```yaml
            # Type: list
            whisparr2_docker_tmpfs:
            ```

        ??? variable list "`whisparr2_docker_ulimits`"

            ```yaml
            # Type: list
            whisparr2_docker_ulimits:
            ```

        ??? variable string "`whisparr2_docker_user`"

            ```yaml
            # Type: string
            whisparr2_docker_user:
            ```

        ??? variable string "`whisparr2_docker_userns_mode`"

            ```yaml
            # Type: string
            whisparr2_docker_userns_mode:
            ```

        ??? variable string "`whisparr2_docker_uts`"

            ```yaml
            # Type: string
            whisparr2_docker_uts:
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`whisparr_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            whisparr_role_autoheal_enabled: true
            ```

        ??? variable string "`whisparr_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            whisparr_role_depends_on: ""
            ```

        ??? variable string "`whisparr_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            whisparr_role_depends_on_delay: "0"
            ```

        ??? variable string "`whisparr_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            whisparr_role_depends_on_healthchecks:
            ```

        ??? variable bool "`whisparr_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            whisparr_role_diun_enabled: true
            ```

        ??? variable bool "`whisparr_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            whisparr_role_dns_enabled: true
            ```

        ??? variable bool "`whisparr_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            whisparr_role_docker_controller: true
            ```

        ??? variable bool "`whisparr_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            whisparr_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`whisparr_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            whisparr_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`whisparr_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            whisparr_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`whisparr_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            whisparr_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`whisparr_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            whisparr_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`whisparr_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            whisparr_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`whisparr_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            whisparr_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`whisparr_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            whisparr_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                whisparr_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "whisparr2.{{ user.domain }}"
                  - "whisparr.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`whisparr_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            whisparr_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                whisparr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'whisparr2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`whisparr_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            whisparr_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `whisparr2`):

        ??? variable bool "`whisparr2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            whisparr2_autoheal_enabled: true
            ```

        ??? variable string "`whisparr2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            whisparr2_depends_on: ""
            ```

        ??? variable string "`whisparr2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            whisparr2_depends_on_delay: "0"
            ```

        ??? variable string "`whisparr2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            whisparr2_depends_on_healthchecks:
            ```

        ??? variable bool "`whisparr2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            whisparr2_diun_enabled: true
            ```

        ??? variable bool "`whisparr2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            whisparr2_dns_enabled: true
            ```

        ??? variable bool "`whisparr2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            whisparr2_docker_controller: true
            ```

        ??? variable bool "`whisparr2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            whisparr2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`whisparr2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            whisparr2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`whisparr2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            whisparr2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`whisparr2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            whisparr2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`whisparr2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            whisparr2_traefik_robot_enabled: true
            ```

        ??? variable bool "`whisparr2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            whisparr2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`whisparr2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            whisparr2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`whisparr2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            whisparr2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                whisparr2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "whisparr2.{{ user.domain }}"
                  - "whisparr.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`whisparr2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            whisparr2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                whisparr2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'whisparr2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`whisparr2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            whisparr2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
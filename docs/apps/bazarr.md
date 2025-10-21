---
hide:
  - tags
tags:
  - bazarr
---

# Bazarr

## What is it?

[Bazarr](https://www.bazarr.media/) is a companion application to Sonarr and Radarr that manages and downloads subtitles based on your requirements.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.bazarr.media/){: .header-icons } | [:octicons-link-16: Docs](https://wiki.bazarr.media/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/hotio/bazarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/bazarr){: .header-icons }|

### 1. Installation

``` shell

sb install bazarr

```

### 2. URL

- To access Bazarr, visit `https://bazarr._yourdomain.com_`

### 3. Setup

- [:octicons-link-16: Documentation](https://wiki.bazarr.media/){: .header-icons }

- [:octicons-link-16: TraSH Guides](https://trash-guides.info/Bazarr/)

There are some settings that - depending on your specific setup - should be adapted to reduce API calls down to a managable level.

Please refer to the official documentation for an explanation of the settings. Some - potentially out of date(!) - settings are documented in the [FAQs](../faq/bazarr.md).

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `bazarr_instances`.

    === "Role-level Override"

        Applies to all instances of bazarr:

        ```yaml
        bazarr_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `bazarr2`):

        ```yaml
        bazarr2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `bazarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `bazarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`bazarr_instances`"

        ```yaml
        # Type: list
        bazarr_instances: ["bazarr"]
        ```

        !!! example

            ```yaml
            # Type: list
            bazarr_instances: ["bazarr", "bazarr2"]
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`bazarr_role_paths_folder`"

            ```yaml
            # Type: string
            bazarr_role_paths_folder: "{{ bazarr_name }}"
            ```

        ??? variable string "`bazarr_role_paths_location`"

            ```yaml
            # Type: string
            bazarr_role_paths_location: "{{ server_appdata_path }}/{{ bazarr_role_paths_folder }}"
            ```

    === "Instance-level"

        ??? variable string "`bazarr2_paths_folder`"

            ```yaml
            # Type: string
            bazarr2_paths_folder: "{{ bazarr_name }}"
            ```

        ??? variable string "`bazarr2_paths_location`"

            ```yaml
            # Type: string
            bazarr2_paths_location: "{{ server_appdata_path }}/{{ bazarr_role_paths_folder }}"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`bazarr_role_web_subdomain`"

            ```yaml
            # Type: string
            bazarr_role_web_subdomain: "{{ bazarr_name }}"
            ```

        ??? variable string "`bazarr_role_web_domain`"

            ```yaml
            # Type: string
            bazarr_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`bazarr_role_web_port`"

            ```yaml
            # Type: string
            bazarr_role_web_port: "6767"
            ```

        ??? variable string "`bazarr_role_web_url`"

            ```yaml
            # Type: string
            bazarr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='bazarr') + '.' + lookup('role_var', '_web_domain', role='bazarr')
                                  if (lookup('role_var', '_web_subdomain', role='bazarr') | length > 0)
                                  else lookup('role_var', '_web_domain', role='bazarr')) }}"
            ```

    === "Instance-level"

        ??? variable string "`bazarr2_web_subdomain`"

            ```yaml
            # Type: string
            bazarr2_web_subdomain: "{{ bazarr_name }}"
            ```

        ??? variable string "`bazarr2_web_domain`"

            ```yaml
            # Type: string
            bazarr2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`bazarr2_web_port`"

            ```yaml
            # Type: string
            bazarr2_web_port: "6767"
            ```

        ??? variable string "`bazarr2_web_url`"

            ```yaml
            # Type: string
                    bazarr2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='bazarr') + '.' + lookup('role_var', '_web_domain', role='bazarr')
                                      if (lookup('role_var', '_web_subdomain', role='bazarr') | length > 0)
                                      else lookup('role_var', '_web_domain', role='bazarr')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`bazarr_role_dns_record`"

            ```yaml
            # Type: string
            bazarr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='bazarr') }}"
            ```

        ??? variable string "`bazarr_role_dns_zone`"

            ```yaml
            # Type: string
            bazarr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='bazarr') }}"
            ```

        ??? variable bool "`bazarr_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            bazarr_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`bazarr2_dns_record`"

            ```yaml
            # Type: string
            bazarr2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='bazarr') }}"
            ```

        ??? variable string "`bazarr2_dns_zone`"

            ```yaml
            # Type: string
            bazarr2_dns_zone: "{{ lookup('role_var', '_web_domain', role='bazarr') }}"
            ```

        ??? variable bool "`bazarr2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            bazarr2_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`bazarr_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            bazarr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`bazarr_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            bazarr_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                        + (',themepark-' + bazarr_name
                                                          if (lookup('role_var', '_themepark_enabled', role='bazarr') and global_themepark_plugin_enabled)
                                                          else '') }}"
            ```

        ??? variable string "`bazarr_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            bazarr_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`bazarr_role_traefik_certresolver`"

            ```yaml
            # Type: string
            bazarr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`bazarr_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            bazarr_role_traefik_enabled: true
            ```

        ??? variable bool "`bazarr_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            bazarr_role_traefik_api_enabled: true
            ```

        ??? variable string "`bazarr_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            bazarr_role_traefik_api_endpoint: "PathPrefix(`/api`)"
            ```

    === "Instance-level"

        ??? variable string "`bazarr2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            bazarr2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`bazarr2_traefik_middleware_default`"

            ```yaml
            # Type: string
                    bazarr2_traefik_middleware_default: "{{ traefik_default_middleware
                                                            + (',themepark-' + bazarr_name
                                                              if (lookup('role_var', '_themepark_enabled', role='bazarr') and global_themepark_plugin_enabled)
                                                              else '') }}"
            ```

        ??? variable string "`bazarr2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            bazarr2_traefik_middleware_custom: ""
            ```

        ??? variable string "`bazarr2_traefik_certresolver`"

            ```yaml
            # Type: string
            bazarr2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`bazarr2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            bazarr2_traefik_enabled: true
            ```

        ??? variable bool "`bazarr2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            bazarr2_traefik_api_enabled: true
            ```

        ??? variable string "`bazarr2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            bazarr2_traefik_api_endpoint: "PathPrefix(`/api`)"
            ```

=== "Theme"

    === "Role-level"

        ??? variable bool "`bazarr_role_themepark_enabled`"

            ```yaml
            # Options can be found at https://github.com/themepark-dev/theme.park
            # Type: bool (true/false)
            bazarr_role_themepark_enabled: false
            ```

        ??? variable string "`bazarr_role_themepark_app`"

            ```yaml
            # Type: string
            bazarr_role_themepark_app: "bazarr"
            ```

        ??? variable string "`bazarr_role_themepark_theme`"

            ```yaml
            # Type: string
            bazarr_role_themepark_theme: "{{ global_themepark_theme }}"
            ```

        ??? variable string "`bazarr_role_themepark_domain`"

            ```yaml
            # Type: string
            bazarr_role_themepark_domain: "{{ global_themepark_domain }}"
            ```

        ??? variable list "`bazarr_role_themepark_addons`"

            ```yaml
            # Type: list
            bazarr_role_themepark_addons: []
            ```

    === "Instance-level"

        ??? variable bool "`bazarr2_themepark_enabled`"

            # Options can be found at https://github.com/themepark-dev/theme.park

            ```yaml
            # Type: bool (true/false)
            bazarr2_themepark_enabled: false
            ```

        ??? variable string "`bazarr2_themepark_app`"

            ```yaml
            # Type: string
            bazarr2_themepark_app: "bazarr"
            ```

        ??? variable string "`bazarr2_themepark_theme`"

            ```yaml
            # Type: string
            bazarr2_themepark_theme: "{{ global_themepark_theme }}"
            ```

        ??? variable string "`bazarr2_themepark_domain`"

            ```yaml
            # Type: string
            bazarr2_themepark_domain: "{{ global_themepark_domain }}"
            ```

        ??? variable list "`bazarr2_themepark_addons`"

            ```yaml
            # Type: list
            bazarr2_themepark_addons: []
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`bazarr_role_docker_container`"

            ```yaml
            # Type: string
            bazarr_role_docker_container: "{{ bazarr_name }}"
            ```

        ##### Image

        ??? variable bool "`bazarr_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            bazarr_role_docker_image_pull: true
            ```

        ??? variable string "`bazarr_role_docker_image_repo`"

            ```yaml
            # Type: string
            bazarr_role_docker_image_repo: "ghcr.io/hotio/bazarr"
            ```

        ??? variable string "`bazarr_role_docker_image_tag`"

            ```yaml
            # Type: string
            bazarr_role_docker_image_tag: "latest"
            ```

        ??? variable string "`bazarr_role_docker_image`"

            ```yaml
            # Type: string
            bazarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='bazarr') }}:{{ lookup('role_var', '_docker_image_tag', role='bazarr') }}"
            ```

        ##### Envs

        ??? variable dict "`bazarr_role_docker_envs_default`"

            ```yaml
            # Type: dict
            bazarr_role_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              UMASK: "002"
              TZ: "{{ tz }}"
            ```

        ??? variable dict "`bazarr_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            bazarr_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`bazarr_role_docker_volumes_default`"

            ```yaml
            # Type: list
            bazarr_role_docker_volumes_default: 
              - "{{ bazarr_role_paths_location }}:/config"
              - "{{ server_appdata_path }}/scripts:/scripts"
            ```

        ??? variable list "`bazarr_role_docker_volumes_legacy`"

            ```yaml
            # Type: list
            bazarr_role_docker_volumes_legacy: 
              - "/mnt/unionfs/Media/Movies:/movies"
              - "/mnt/unionfs/Media/TV:/tv"
            ```

        ??? variable list "`bazarr_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            bazarr_role_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable dict "`bazarr_role_docker_labels_default`"

            ```yaml
            # Type: dict
            bazarr_role_docker_labels_default: {}
            ```

        ??? variable dict "`bazarr_role_docker_labels_custom`"

            ```yaml
            # Type: dict
            bazarr_role_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`bazarr_role_docker_hostname`"

            ```yaml
            # Type: string
            bazarr_role_docker_hostname: "{{ bazarr_name }}"
            ```

        ##### Networks

        ??? variable string "`bazarr_role_docker_networks_alias`"

            ```yaml
            # Type: string
            bazarr_role_docker_networks_alias: "{{ bazarr_name }}"
            ```

        ??? variable list "`bazarr_role_docker_networks_default`"

            ```yaml
            # Type: list
            bazarr_role_docker_networks_default: []
            ```

        ??? variable list "`bazarr_role_docker_networks_custom`"

            ```yaml
            # Type: list
            bazarr_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`bazarr_role_docker_restart_policy`"

            ```yaml
            # Type: string
            bazarr_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`bazarr_role_docker_state`"

            ```yaml
            # Type: string
            bazarr_role_docker_state: started
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`bazarr2_docker_container`"

            ```yaml
            # Type: string
            bazarr2_docker_container: "{{ bazarr_name }}"
            ```

        ##### Image

        ??? variable bool "`bazarr2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            bazarr2_docker_image_pull: true
            ```

        ??? variable string "`bazarr2_docker_image_repo`"

            ```yaml
            # Type: string
            bazarr2_docker_image_repo: "ghcr.io/hotio/bazarr"
            ```

        ??? variable string "`bazarr2_docker_image_tag`"

            ```yaml
            # Type: string
            bazarr2_docker_image_tag: "latest"
            ```

        ??? variable string "`bazarr2_docker_image`"

            ```yaml
            # Type: string
            bazarr2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='bazarr') }}:{{ lookup('role_var', '_docker_image_tag', role='bazarr') }}"
            ```

        ##### Envs

        ??? variable dict "`bazarr2_docker_envs_default`"

            ```yaml
            # Type: dict
                    bazarr2_docker_envs_default: 
                      PUID: "{{ uid }}"
                      PGID: "{{ gid }}"
                      UMASK: "002"
                      TZ: "{{ tz }}"
            ```

        ??? variable dict "`bazarr2_docker_envs_custom`"

            ```yaml
            # Type: dict
            bazarr2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`bazarr2_docker_volumes_default`"

            ```yaml
            # Type: list
                    bazarr2_docker_volumes_default: 
                      - "{{ bazarr_role_paths_location }}:/config"
                      - "{{ server_appdata_path }}/scripts:/scripts"
            ```

        ??? variable list "`bazarr2_docker_volumes_legacy`"

            ```yaml
            # Type: list
                    bazarr2_docker_volumes_legacy: 
                      - "/mnt/unionfs/Media/Movies:/movies"
                      - "/mnt/unionfs/Media/TV:/tv"
            ```

        ??? variable list "`bazarr2_docker_volumes_custom`"

            ```yaml
            # Type: list
            bazarr2_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable dict "`bazarr2_docker_labels_default`"

            ```yaml
            # Type: dict
            bazarr2_docker_labels_default: {}
            ```

        ??? variable dict "`bazarr2_docker_labels_custom`"

            ```yaml
            # Type: dict
            bazarr2_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`bazarr2_docker_hostname`"

            ```yaml
            # Type: string
            bazarr2_docker_hostname: "{{ bazarr_name }}"
            ```

        ##### Networks

        ??? variable string "`bazarr2_docker_networks_alias`"

            ```yaml
            # Type: string
            bazarr2_docker_networks_alias: "{{ bazarr_name }}"
            ```

        ??? variable list "`bazarr2_docker_networks_default`"

            ```yaml
            # Type: list
            bazarr2_docker_networks_default: []
            ```

        ??? variable list "`bazarr2_docker_networks_custom`"

            ```yaml
            # Type: list
            bazarr2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`bazarr2_docker_restart_policy`"

            ```yaml
            # Type: string
            bazarr2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`bazarr2_docker_state`"

            ```yaml
            # Type: string
            bazarr2_docker_state: started
            ```

=== "Docker+"

    #### Additional Docker Options

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    === "Role-level"

        ##### Resource Limits

        ??? variable int "`bazarr_role_docker_blkio_weight`"

            ```yaml
            # Type: int
            bazarr_role_docker_blkio_weight:
            ```

        ??? variable int "`bazarr_role_docker_cpu_period`"

            ```yaml
            # Type: int
            bazarr_role_docker_cpu_period:
            ```

        ??? variable int "`bazarr_role_docker_cpu_quota`"

            ```yaml
            # Type: int
            bazarr_role_docker_cpu_quota:
            ```

        ??? variable int "`bazarr_role_docker_cpu_shares`"

            ```yaml
            # Type: int
            bazarr_role_docker_cpu_shares:
            ```

        ??? variable string "`bazarr_role_docker_cpus`"

            ```yaml
            # Type: string
            bazarr_role_docker_cpus:
            ```

        ??? variable string "`bazarr_role_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            bazarr_role_docker_cpuset_cpus:
            ```

        ??? variable string "`bazarr_role_docker_cpuset_mems`"

            ```yaml
            # Type: string
            bazarr_role_docker_cpuset_mems:
            ```

        ??? variable string "`bazarr_role_docker_kernel_memory`"

            ```yaml
            # Type: string
            bazarr_role_docker_kernel_memory:
            ```

        ??? variable string "`bazarr_role_docker_memory`"

            ```yaml
            # Type: string
            bazarr_role_docker_memory:
            ```

        ??? variable string "`bazarr_role_docker_memory_reservation`"

            ```yaml
            # Type: string
            bazarr_role_docker_memory_reservation:
            ```

        ??? variable string "`bazarr_role_docker_memory_swap`"

            ```yaml
            # Type: string
            bazarr_role_docker_memory_swap:
            ```

        ??? variable int "`bazarr_role_docker_memory_swappiness`"

            ```yaml
            # Type: int
            bazarr_role_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`bazarr_role_docker_cap_drop`"

            ```yaml
            # Type: list
            bazarr_role_docker_cap_drop:
            ```

        ??? variable list "`bazarr_role_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            bazarr_role_docker_device_cgroup_rules:
            ```

        ??? variable list "`bazarr_role_docker_device_read_bps`"

            ```yaml
            # Type: list
            bazarr_role_docker_device_read_bps:
            ```

        ??? variable list "`bazarr_role_docker_device_read_iops`"

            ```yaml
            # Type: list
            bazarr_role_docker_device_read_iops:
            ```

        ??? variable list "`bazarr_role_docker_device_requests`"

            ```yaml
            # Type: list
            bazarr_role_docker_device_requests:
            ```

        ??? variable list "`bazarr_role_docker_device_write_bps`"

            ```yaml
            # Type: list
            bazarr_role_docker_device_write_bps:
            ```

        ??? variable list "`bazarr_role_docker_device_write_iops`"

            ```yaml
            # Type: list
            bazarr_role_docker_device_write_iops:
            ```

        ??? variable list "`bazarr_role_docker_devices`"

            ```yaml
            # Type: list
            bazarr_role_docker_devices:
            ```

        ??? variable string "`bazarr_role_docker_devices_default`"

            ```yaml
            # Type: string
            bazarr_role_docker_devices_default:
            ```

        ??? variable bool "`bazarr_role_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            bazarr_role_docker_privileged:
            ```

        ??? variable list "`bazarr_role_docker_security_opts`"

            ```yaml
            # Type: list
            bazarr_role_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`bazarr_role_docker_dns_opts`"

            ```yaml
            # Type: list
            bazarr_role_docker_dns_opts:
            ```

        ??? variable list "`bazarr_role_docker_dns_search_domains`"

            ```yaml
            # Type: list
            bazarr_role_docker_dns_search_domains:
            ```

        ??? variable list "`bazarr_role_docker_dns_servers`"

            ```yaml
            # Type: list
            bazarr_role_docker_dns_servers:
            ```

        ??? variable dict "`bazarr_role_docker_hosts`"

            ```yaml
            # Type: dict
            bazarr_role_docker_hosts:
            ```

        ??? variable string "`bazarr_role_docker_hosts_use_common`"

            ```yaml
            # Type: string
            bazarr_role_docker_hosts_use_common:
            ```

        ??? variable string "`bazarr_role_docker_network_mode`"

            ```yaml
            # Type: string
            bazarr_role_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`bazarr_role_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            bazarr_role_docker_keep_volumes:
            ```

        ??? variable list "`bazarr_role_docker_mounts`"

            ```yaml
            # Type: list
            bazarr_role_docker_mounts:
            ```

        ??? variable string "`bazarr_role_docker_volume_driver`"

            ```yaml
            # Type: string
            bazarr_role_docker_volume_driver:
            ```

        ??? variable list "`bazarr_role_docker_volumes_from`"

            ```yaml
            # Type: list
            bazarr_role_docker_volumes_from:
            ```

        ??? variable string "`bazarr_role_docker_volumes_global`"

            ```yaml
            # Type: string
            bazarr_role_docker_volumes_global:
            ```

        ??? variable string "`bazarr_role_docker_working_dir`"

            ```yaml
            # Type: string
            bazarr_role_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`bazarr_role_docker_healthcheck`"

            ```yaml
            # Type: dict
            bazarr_role_docker_healthcheck:
            ```

        ??? variable bool "`bazarr_role_docker_init`"

            ```yaml
            # Type: bool (true/false)
            bazarr_role_docker_init:
            ```

        ??? variable string "`bazarr_role_docker_log_driver`"

            ```yaml
            # Type: string
            bazarr_role_docker_log_driver:
            ```

        ??? variable dict "`bazarr_role_docker_log_options`"

            ```yaml
            # Type: dict
            bazarr_role_docker_log_options:
            ```

        ??? variable bool "`bazarr_role_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            bazarr_role_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`bazarr_role_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            bazarr_role_docker_auto_remove:
            ```

        ??? variable list "`bazarr_role_docker_capabilities`"

            ```yaml
            # Type: list
            bazarr_role_docker_capabilities:
            ```

        ??? variable string "`bazarr_role_docker_cgroup_parent`"

            ```yaml
            # Type: string
            bazarr_role_docker_cgroup_parent:
            ```

        ??? variable string "`bazarr_role_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            bazarr_role_docker_cgroupns_mode:
            ```

        ??? variable bool "`bazarr_role_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            bazarr_role_docker_cleanup:
            ```

        ??? variable list "`bazarr_role_docker_commands`"

            ```yaml
            # Type: list
            bazarr_role_docker_commands:
            ```

        ??? variable string "`bazarr_role_docker_create_timeout`"

            ```yaml
            # Type: string
            bazarr_role_docker_create_timeout:
            ```

        ??? variable string "`bazarr_role_docker_domainname`"

            ```yaml
            # Type: string
            bazarr_role_docker_domainname:
            ```

        ??? variable string "`bazarr_role_docker_entrypoint`"

            ```yaml
            # Type: string
            bazarr_role_docker_entrypoint:
            ```

        ??? variable string "`bazarr_role_docker_env_file`"

            ```yaml
            # Type: string
            bazarr_role_docker_env_file:
            ```

        ??? variable list "`bazarr_role_docker_exposed_ports`"

            ```yaml
            # Type: list
            bazarr_role_docker_exposed_ports:
            ```

        ??? variable string "`bazarr_role_docker_force_kill`"

            ```yaml
            # Type: string
            bazarr_role_docker_force_kill:
            ```

        ??? variable list "`bazarr_role_docker_groups`"

            ```yaml
            # Type: list
            bazarr_role_docker_groups:
            ```

        ??? variable int "`bazarr_role_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            bazarr_role_docker_healthy_wait_timeout:
            ```

        ??? variable string "`bazarr_role_docker_ipc_mode`"

            ```yaml
            # Type: string
            bazarr_role_docker_ipc_mode:
            ```

        ??? variable string "`bazarr_role_docker_kill_signal`"

            ```yaml
            # Type: string
            bazarr_role_docker_kill_signal:
            ```

        ??? variable string "`bazarr_role_docker_labels_use_common`"

            ```yaml
            # Type: string
            bazarr_role_docker_labels_use_common:
            ```

        ??? variable list "`bazarr_role_docker_links`"

            ```yaml
            # Type: list
            bazarr_role_docker_links:
            ```

        ??? variable bool "`bazarr_role_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            bazarr_role_docker_oom_killer:
            ```

        ??? variable int "`bazarr_role_docker_oom_score_adj`"

            ```yaml
            # Type: int
            bazarr_role_docker_oom_score_adj:
            ```

        ??? variable bool "`bazarr_role_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            bazarr_role_docker_paused:
            ```

        ??? variable string "`bazarr_role_docker_pid_mode`"

            ```yaml
            # Type: string
            bazarr_role_docker_pid_mode:
            ```

        ??? variable list "`bazarr_role_docker_ports`"

            ```yaml
            # Type: list
            bazarr_role_docker_ports:
            ```

        ??? variable bool "`bazarr_role_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            bazarr_role_docker_read_only:
            ```

        ??? variable bool "`bazarr_role_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            bazarr_role_docker_recreate:
            ```

        ??? variable int "`bazarr_role_docker_restart_retries`"

            ```yaml
            # Type: int
            bazarr_role_docker_restart_retries:
            ```

        ??? variable string "`bazarr_role_docker_runtime`"

            ```yaml
            # Type: string
            bazarr_role_docker_runtime:
            ```

        ??? variable string "`bazarr_role_docker_shm_size`"

            ```yaml
            # Type: string
            bazarr_role_docker_shm_size:
            ```

        ??? variable int "`bazarr_role_docker_stop_timeout`"

            ```yaml
            # Type: int
            bazarr_role_docker_stop_timeout:
            ```

        ??? variable dict "`bazarr_role_docker_storage_opts`"

            ```yaml
            # Type: dict
            bazarr_role_docker_storage_opts:
            ```

        ??? variable list "`bazarr_role_docker_sysctls`"

            ```yaml
            # Type: list
            bazarr_role_docker_sysctls:
            ```

        ??? variable list "`bazarr_role_docker_tmpfs`"

            ```yaml
            # Type: list
            bazarr_role_docker_tmpfs:
            ```

        ??? variable list "`bazarr_role_docker_ulimits`"

            ```yaml
            # Type: list
            bazarr_role_docker_ulimits:
            ```

        ??? variable string "`bazarr_role_docker_user`"

            ```yaml
            # Type: string
            bazarr_role_docker_user:
            ```

        ??? variable string "`bazarr_role_docker_userns_mode`"

            ```yaml
            # Type: string
            bazarr_role_docker_userns_mode:
            ```

        ??? variable string "`bazarr_role_docker_uts`"

            ```yaml
            # Type: string
            bazarr_role_docker_uts:
            ```

    === "Instance-level"

        ##### Resource Limits

        ??? variable int "`bazarr2_docker_blkio_weight`"

            ```yaml
            # Type: int
            bazarr2_docker_blkio_weight:
            ```

        ??? variable int "`bazarr2_docker_cpu_period`"

            ```yaml
            # Type: int
            bazarr2_docker_cpu_period:
            ```

        ??? variable int "`bazarr2_docker_cpu_quota`"

            ```yaml
            # Type: int
            bazarr2_docker_cpu_quota:
            ```

        ??? variable int "`bazarr2_docker_cpu_shares`"

            ```yaml
            # Type: int
            bazarr2_docker_cpu_shares:
            ```

        ??? variable string "`bazarr2_docker_cpus`"

            ```yaml
            # Type: string
            bazarr2_docker_cpus:
            ```

        ??? variable string "`bazarr2_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            bazarr2_docker_cpuset_cpus:
            ```

        ??? variable string "`bazarr2_docker_cpuset_mems`"

            ```yaml
            # Type: string
            bazarr2_docker_cpuset_mems:
            ```

        ??? variable string "`bazarr2_docker_kernel_memory`"

            ```yaml
            # Type: string
            bazarr2_docker_kernel_memory:
            ```

        ??? variable string "`bazarr2_docker_memory`"

            ```yaml
            # Type: string
            bazarr2_docker_memory:
            ```

        ??? variable string "`bazarr2_docker_memory_reservation`"

            ```yaml
            # Type: string
            bazarr2_docker_memory_reservation:
            ```

        ??? variable string "`bazarr2_docker_memory_swap`"

            ```yaml
            # Type: string
            bazarr2_docker_memory_swap:
            ```

        ??? variable int "`bazarr2_docker_memory_swappiness`"

            ```yaml
            # Type: int
            bazarr2_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`bazarr2_docker_cap_drop`"

            ```yaml
            # Type: list
            bazarr2_docker_cap_drop:
            ```

        ??? variable list "`bazarr2_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            bazarr2_docker_device_cgroup_rules:
            ```

        ??? variable list "`bazarr2_docker_device_read_bps`"

            ```yaml
            # Type: list
            bazarr2_docker_device_read_bps:
            ```

        ??? variable list "`bazarr2_docker_device_read_iops`"

            ```yaml
            # Type: list
            bazarr2_docker_device_read_iops:
            ```

        ??? variable list "`bazarr2_docker_device_requests`"

            ```yaml
            # Type: list
            bazarr2_docker_device_requests:
            ```

        ??? variable list "`bazarr2_docker_device_write_bps`"

            ```yaml
            # Type: list
            bazarr2_docker_device_write_bps:
            ```

        ??? variable list "`bazarr2_docker_device_write_iops`"

            ```yaml
            # Type: list
            bazarr2_docker_device_write_iops:
            ```

        ??? variable list "`bazarr2_docker_devices`"

            ```yaml
            # Type: list
            bazarr2_docker_devices:
            ```

        ??? variable string "`bazarr2_docker_devices_default`"

            ```yaml
            # Type: string
            bazarr2_docker_devices_default:
            ```

        ??? variable bool "`bazarr2_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            bazarr2_docker_privileged:
            ```

        ??? variable list "`bazarr2_docker_security_opts`"

            ```yaml
            # Type: list
            bazarr2_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`bazarr2_docker_dns_opts`"

            ```yaml
            # Type: list
            bazarr2_docker_dns_opts:
            ```

        ??? variable list "`bazarr2_docker_dns_search_domains`"

            ```yaml
            # Type: list
            bazarr2_docker_dns_search_domains:
            ```

        ??? variable list "`bazarr2_docker_dns_servers`"

            ```yaml
            # Type: list
            bazarr2_docker_dns_servers:
            ```

        ??? variable dict "`bazarr2_docker_hosts`"

            ```yaml
            # Type: dict
            bazarr2_docker_hosts:
            ```

        ??? variable string "`bazarr2_docker_hosts_use_common`"

            ```yaml
            # Type: string
            bazarr2_docker_hosts_use_common:
            ```

        ??? variable string "`bazarr2_docker_network_mode`"

            ```yaml
            # Type: string
            bazarr2_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`bazarr2_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            bazarr2_docker_keep_volumes:
            ```

        ??? variable list "`bazarr2_docker_mounts`"

            ```yaml
            # Type: list
            bazarr2_docker_mounts:
            ```

        ??? variable string "`bazarr2_docker_volume_driver`"

            ```yaml
            # Type: string
            bazarr2_docker_volume_driver:
            ```

        ??? variable list "`bazarr2_docker_volumes_from`"

            ```yaml
            # Type: list
            bazarr2_docker_volumes_from:
            ```

        ??? variable string "`bazarr2_docker_volumes_global`"

            ```yaml
            # Type: string
            bazarr2_docker_volumes_global:
            ```

        ??? variable string "`bazarr2_docker_working_dir`"

            ```yaml
            # Type: string
            bazarr2_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`bazarr2_docker_healthcheck`"

            ```yaml
            # Type: dict
            bazarr2_docker_healthcheck:
            ```

        ??? variable bool "`bazarr2_docker_init`"

            ```yaml
            # Type: bool (true/false)
            bazarr2_docker_init:
            ```

        ??? variable string "`bazarr2_docker_log_driver`"

            ```yaml
            # Type: string
            bazarr2_docker_log_driver:
            ```

        ??? variable dict "`bazarr2_docker_log_options`"

            ```yaml
            # Type: dict
            bazarr2_docker_log_options:
            ```

        ??? variable bool "`bazarr2_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            bazarr2_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`bazarr2_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            bazarr2_docker_auto_remove:
            ```

        ??? variable list "`bazarr2_docker_capabilities`"

            ```yaml
            # Type: list
            bazarr2_docker_capabilities:
            ```

        ??? variable string "`bazarr2_docker_cgroup_parent`"

            ```yaml
            # Type: string
            bazarr2_docker_cgroup_parent:
            ```

        ??? variable string "`bazarr2_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            bazarr2_docker_cgroupns_mode:
            ```

        ??? variable bool "`bazarr2_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            bazarr2_docker_cleanup:
            ```

        ??? variable list "`bazarr2_docker_commands`"

            ```yaml
            # Type: list
            bazarr2_docker_commands:
            ```

        ??? variable string "`bazarr2_docker_create_timeout`"

            ```yaml
            # Type: string
            bazarr2_docker_create_timeout:
            ```

        ??? variable string "`bazarr2_docker_domainname`"

            ```yaml
            # Type: string
            bazarr2_docker_domainname:
            ```

        ??? variable string "`bazarr2_docker_entrypoint`"

            ```yaml
            # Type: string
            bazarr2_docker_entrypoint:
            ```

        ??? variable string "`bazarr2_docker_env_file`"

            ```yaml
            # Type: string
            bazarr2_docker_env_file:
            ```

        ??? variable list "`bazarr2_docker_exposed_ports`"

            ```yaml
            # Type: list
            bazarr2_docker_exposed_ports:
            ```

        ??? variable string "`bazarr2_docker_force_kill`"

            ```yaml
            # Type: string
            bazarr2_docker_force_kill:
            ```

        ??? variable list "`bazarr2_docker_groups`"

            ```yaml
            # Type: list
            bazarr2_docker_groups:
            ```

        ??? variable int "`bazarr2_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            bazarr2_docker_healthy_wait_timeout:
            ```

        ??? variable string "`bazarr2_docker_ipc_mode`"

            ```yaml
            # Type: string
            bazarr2_docker_ipc_mode:
            ```

        ??? variable string "`bazarr2_docker_kill_signal`"

            ```yaml
            # Type: string
            bazarr2_docker_kill_signal:
            ```

        ??? variable string "`bazarr2_docker_labels_use_common`"

            ```yaml
            # Type: string
            bazarr2_docker_labels_use_common:
            ```

        ??? variable list "`bazarr2_docker_links`"

            ```yaml
            # Type: list
            bazarr2_docker_links:
            ```

        ??? variable bool "`bazarr2_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            bazarr2_docker_oom_killer:
            ```

        ??? variable int "`bazarr2_docker_oom_score_adj`"

            ```yaml
            # Type: int
            bazarr2_docker_oom_score_adj:
            ```

        ??? variable bool "`bazarr2_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            bazarr2_docker_paused:
            ```

        ??? variable string "`bazarr2_docker_pid_mode`"

            ```yaml
            # Type: string
            bazarr2_docker_pid_mode:
            ```

        ??? variable list "`bazarr2_docker_ports`"

            ```yaml
            # Type: list
            bazarr2_docker_ports:
            ```

        ??? variable bool "`bazarr2_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            bazarr2_docker_read_only:
            ```

        ??? variable bool "`bazarr2_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            bazarr2_docker_recreate:
            ```

        ??? variable int "`bazarr2_docker_restart_retries`"

            ```yaml
            # Type: int
            bazarr2_docker_restart_retries:
            ```

        ??? variable string "`bazarr2_docker_runtime`"

            ```yaml
            # Type: string
            bazarr2_docker_runtime:
            ```

        ??? variable string "`bazarr2_docker_shm_size`"

            ```yaml
            # Type: string
            bazarr2_docker_shm_size:
            ```

        ??? variable int "`bazarr2_docker_stop_timeout`"

            ```yaml
            # Type: int
            bazarr2_docker_stop_timeout:
            ```

        ??? variable dict "`bazarr2_docker_storage_opts`"

            ```yaml
            # Type: dict
            bazarr2_docker_storage_opts:
            ```

        ??? variable list "`bazarr2_docker_sysctls`"

            ```yaml
            # Type: list
            bazarr2_docker_sysctls:
            ```

        ??? variable list "`bazarr2_docker_tmpfs`"

            ```yaml
            # Type: list
            bazarr2_docker_tmpfs:
            ```

        ??? variable list "`bazarr2_docker_ulimits`"

            ```yaml
            # Type: list
            bazarr2_docker_ulimits:
            ```

        ??? variable string "`bazarr2_docker_user`"

            ```yaml
            # Type: string
            bazarr2_docker_user:
            ```

        ??? variable string "`bazarr2_docker_userns_mode`"

            ```yaml
            # Type: string
            bazarr2_docker_userns_mode:
            ```

        ??? variable string "`bazarr2_docker_uts`"

            ```yaml
            # Type: string
            bazarr2_docker_uts:
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`bazarr_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            bazarr_role_autoheal_enabled: true
            ```

        ??? variable string "`bazarr_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            bazarr_role_depends_on: ""
            ```

        ??? variable string "`bazarr_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            bazarr_role_depends_on_delay: "0"
            ```

        ??? variable string "`bazarr_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            bazarr_role_depends_on_healthchecks:
            ```

        ??? variable bool "`bazarr_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            bazarr_role_diun_enabled: true
            ```

        ??? variable bool "`bazarr_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            bazarr_role_dns_enabled: true
            ```

        ??? variable bool "`bazarr_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            bazarr_role_docker_controller: true
            ```

        ??? variable bool "`bazarr_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            bazarr_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`bazarr_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            bazarr_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`bazarr_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            bazarr_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`bazarr_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            bazarr_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`bazarr_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            bazarr_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`bazarr_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            bazarr_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`bazarr_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            bazarr_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`bazarr_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            bazarr_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                bazarr_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "bazarr2.{{ user.domain }}"
                  - "bazarr.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`bazarr_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            bazarr_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                bazarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'bazarr2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`bazarr_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            bazarr_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `bazarr2`):

        ??? variable bool "`bazarr2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            bazarr2_autoheal_enabled: true
            ```

        ??? variable string "`bazarr2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            bazarr2_depends_on: ""
            ```

        ??? variable string "`bazarr2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            bazarr2_depends_on_delay: "0"
            ```

        ??? variable string "`bazarr2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            bazarr2_depends_on_healthchecks:
            ```

        ??? variable bool "`bazarr2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            bazarr2_diun_enabled: true
            ```

        ??? variable bool "`bazarr2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            bazarr2_dns_enabled: true
            ```

        ??? variable bool "`bazarr2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            bazarr2_docker_controller: true
            ```

        ??? variable bool "`bazarr2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            bazarr2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`bazarr2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            bazarr2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`bazarr2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            bazarr2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`bazarr2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            bazarr2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`bazarr2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            bazarr2_traefik_robot_enabled: true
            ```

        ??? variable bool "`bazarr2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            bazarr2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`bazarr2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            bazarr2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`bazarr2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            bazarr2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                bazarr2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "bazarr2.{{ user.domain }}"
                  - "bazarr.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`bazarr2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            bazarr2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                bazarr2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'bazarr2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`bazarr2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            bazarr2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
icon: material/docker
title: SABnzbd
hide:
  - tags
tags:
  - sab
  - sabnzbd
saltbox_automation:
  app_links:
    - name: Manual
      url:
      type: documentation
    - name: Releases
      url: https://github.com/hotio/sabnzbd/pkgs/container/sabnzbd
      type: github
    - name: Community
      url: https://hotio.dev/discord
      type: discord
  project_description:
    name: SABnzbd
    summary: |
      a free, open-source Usenet client designed to simplify downloading files from Usenet by automating the entire process using NZB files, which act as blueprints for locating content on Usenet servers.
    link: https://github.com/sabnzbd/sabnzbd
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# SABnzbd

## Overview

[SABnzbd](https://github.com/sabnzbd/sabnzbd) is a free, open-source Usenet client designed to simplify downloading files from Usenet by automating the entire process using NZB files, which act as blueprints for locating content on Usenet servers.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/hotio/sabnzbd/pkgs/container/sabnzbd){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://hotio.dev/discord){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

!!! abstract cta "Saltbox Setup Process"

    <div data-search-exclude>

    <div>

    Opting out of Usenet?

    <div>

    [**Skip to qBittorrent**:material-fast-forward:](qbittorrent.md){ .md-button }

    </div>

    </div>

    <div>

    Opting for another Usenet client?

    <div>

    [**Explore alternatives**:material-shuffle-variant:](index.md#download-client){ .md-button }

    [**Skip to NZBHydra2**:material-fast-forward:](nzbhydra2.md){ .md-button }

    </div>

    </div>

    </div>

## Deployment

```shell
sb install sabnzbd
```

## Usage

Visit <https://sabnzbd.iYOUR_DOMAIN_NAMEi>.

## Basics

- Go through the setup wizard. You will need to enter server details:

![](../images/sabnzbd/02-sabnzbd.png)

- When you get to the end of the wizard, click "Go To SABnzbd"

![](../images/sabnzbd/03-sabnzbd.png)

- Go to SABnzbd Config

![](../images/sabnzbd/04-sabnzbd.png)

- You will need to add in categories for `sonarr`, `radarr`, and `lidarr`.

  Set a relative directory name for each category.

  You will need a category for each instance of `sonarr`/`radarr`/`lidarr` (for example, if you have a `radarr` and `radarr4k` you will need a category for each)

  SABnzbd requires the server to be filled in to set categories up.

  **This needs to be done BEFORE adding SABnzbd as a downloader to any of those apps.**

![](../images/sabnzbd/05-sabnzbd.png)

- Direct unpack is disabled by default. Configure this as you prefer.

- Make note of the API Key in the "General" section

![](../images/sabnzbd/06-sabnzbd.png)

- When creating the connection in the arrs, use API Key rather than user/pass.

![](../images/sabnzbd/07-sabnzbd.png)

   Note that the category matches between Radarr and SABnzbd. The specific category doesn't matter; just that they match.

## Next

<div class="sb-cta" markdown>

Are you setting Saltbox up for the first time?

<div markdown>

[**Continue to NZBHydra2**:material-forward:](nzbhydra2.md){ .md-button }

</div>

</div>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        sabnzbd_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `sabnzbd_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `sabnzbd_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`sabnzbd_name`"

        ```yaml
        # Type: string
        sabnzbd_name: sabnzbd
        ```

=== "Web"

    ??? variable string "`sabnzbd_role_web_subdomain`"

        ```yaml
        # Type: string
        sabnzbd_role_web_subdomain: "{{ sabnzbd_name }}"
        ```

    ??? variable string "`sabnzbd_role_web_domain`"

        ```yaml
        # Type: string
        sabnzbd_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`sabnzbd_role_web_port`"

        ```yaml
        # Type: string
        sabnzbd_role_web_port: "8080"
        ```

    ??? variable string "`sabnzbd_role_web_url`"

        ```yaml
        # Type: string
        sabnzbd_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='sabnzbd') + '.' + lookup('role_var', '_web_domain', role='sabnzbd')
                               if (lookup('role_var', '_web_subdomain', role='sabnzbd') | length > 0)
                               else lookup('role_var', '_web_domain', role='sabnzbd')) }}"
        ```

    ??? variable string "`sabnzbd_role_web_local_url`"

        ```yaml
        # Type: string
        sabnzbd_role_web_local_url: "{{ 'http://' + sabnzbd_name + ':' + lookup('role_var', '_web_port', role='sabnzbd') }}"
        ```

=== "DNS"

    ??? variable string "`sabnzbd_role_dns_record`"

        ```yaml
        # Type: string
        sabnzbd_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='sabnzbd') }}"
        ```

    ??? variable string "`sabnzbd_role_dns_zone`"

        ```yaml
        # Type: string
        sabnzbd_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='sabnzbd') }}"
        ```

    ??? variable bool "`sabnzbd_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`sabnzbd_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        sabnzbd_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`sabnzbd_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        sabnzbd_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                     + (',themepark-' + sabnzbd_name
                                                       if (lookup('role_var', '_themepark_enabled', role='sabnzbd') and global_themepark_plugin_enabled)
                                                       else '') }}"
        ```

    ??? variable string "`sabnzbd_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        sabnzbd_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`sabnzbd_role_traefik_certresolver`"

        ```yaml
        # Type: string
        sabnzbd_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`sabnzbd_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_traefik_enabled: true
        ```

    ??? variable bool "`sabnzbd_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_traefik_api_enabled: true
        ```

    ??? variable string "`sabnzbd_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        sabnzbd_role_traefik_api_endpoint: "PathPrefix(`/api`)"
        ```

=== "Config"

    ??? variable string "`sabnzbd_role_config_settings_web`"

        ```yaml
        # Type: string
        sabnzbd_role_config_settings_web:
          # Web
          - { option: "host_whitelist", value: "{{ lookup('role_var', '_web_subdomain', role='sabnzbd') }}.{{ lookup('role_var', '_web_domain', role='sabnzbd') }}, {{ sabnzbd_name }}" }
          - { option: "url_base", value: "" }
          - { option: "log_dir", value: "/config/logs" }
        ```

    ??? variable string "`sabnzbd_role_config_settings_default`"

        ```yaml
        # Type: string
        sabnzbd_role_config_settings_default:
          # Web
          - { option: "host_whitelist", value: "{{ lookup('role_var', '_web_subdomain', role='sabnzbd') }}.{{ lookup('role_var', '_web_domain', role='sabnzbd') }}, {{ sabnzbd_name }}" }
          - { option: "url_base", value: "" }
          # Paths
          - { option: "dirscan_dir", value: "{{ lookup('role_var', '_paths_downloads_location', role='sabnzbd') }}/watch" }
          - { option: "download_dir", value: "{{ lookup('role_var', '_paths_downloads_location', role='sabnzbd') }}/incomplete" }
          - { option: "complete_dir", value: "{{ lookup('role_var', '_paths_downloads_location', role='sabnzbd') }}/complete" }
          - { option: "log_dir", value: "/config/logs" }
        ```

    ??? variable list "`sabnzbd_role_config_settings_custom`"

        ```yaml
        # Type: list
        sabnzbd_role_config_settings_custom: []
        ```

    ??? variable string "`sabnzbd_role_config_settings_list`"

        ```yaml
        # Type: string
        sabnzbd_role_config_settings_list: "{{ lookup('role_var', '_config_settings_default', role='sabnzbd')
                                               + lookup('role_var', '_config_settings_custom', role='sabnzbd') }}"
        ```

=== "Theme"

    ??? variable bool "`sabnzbd_role_themepark_enabled`"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        sabnzbd_role_themepark_enabled: false
        ```

    ??? variable string "`sabnzbd_role_themepark_app`"

        ```yaml
        # Type: string
        sabnzbd_role_themepark_app: "sabnzbd"
        ```

    ??? variable string "`sabnzbd_role_themepark_theme`"

        ```yaml
        # Type: string
        sabnzbd_role_themepark_theme: "{{ global_themepark_theme }}"
        ```

    ??? variable string "`sabnzbd_role_themepark_domain`"

        ```yaml
        # Type: string
        sabnzbd_role_themepark_domain: "{{ global_themepark_domain }}"
        ```

    ??? variable list "`sabnzbd_role_themepark_addons`"

        ```yaml
        # Type: list
        sabnzbd_role_themepark_addons: []
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`sabnzbd_role_docker_container`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_container: "{{ sabnzbd_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`sabnzbd_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_docker_image_pull: true
        ```

    ??? variable string "`sabnzbd_role_docker_image_repo`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_image_repo: "ghcr.io/hotio/sabnzbd"
        ```

    ??? variable string "`sabnzbd_role_docker_image_tag`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_image_tag: "latest"
        ```

    ??? variable string "`sabnzbd_role_docker_image`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='sabnzbd') }}:{{ lookup('role_var', '_docker_image_tag', role='sabnzbd') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`sabnzbd_role_docker_envs_default`"

        ```yaml
        # Type: dict
        sabnzbd_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          UMASK: "002"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`sabnzbd_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        sabnzbd_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`sabnzbd_role_docker_volumes_default`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_volumes_default:
          - "{{ sabnzbd_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
        ```

    ??? variable list "`sabnzbd_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable dict "`sabnzbd_role_docker_labels_default`"

        ```yaml
        # Type: dict
        sabnzbd_role_docker_labels_default: {}
        ```

    ??? variable dict "`sabnzbd_role_docker_labels_custom`"

        ```yaml
        # Type: dict
        sabnzbd_role_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`sabnzbd_role_docker_hostname`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_hostname: "{{ sabnzbd_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`sabnzbd_role_docker_networks_alias`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_networks_alias: "{{ sabnzbd_name }}"
        ```

    ??? variable list "`sabnzbd_role_docker_networks_default`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_networks_default: []
        ```

    ??? variable list "`sabnzbd_role_docker_networks_custom`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`sabnzbd_role_docker_restart_policy`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`sabnzbd_role_docker_state`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`sabnzbd_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        sabnzbd_role_docker_blkio_weight:
        ```

    ??? variable int "`sabnzbd_role_docker_cpu_period`"

        ```yaml
        # Type: int
        sabnzbd_role_docker_cpu_period:
        ```

    ??? variable int "`sabnzbd_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        sabnzbd_role_docker_cpu_quota:
        ```

    ??? variable int "`sabnzbd_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        sabnzbd_role_docker_cpu_shares:
        ```

    ??? variable string "`sabnzbd_role_docker_cpus`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_cpus:
        ```

    ??? variable string "`sabnzbd_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_cpuset_cpus:
        ```

    ??? variable string "`sabnzbd_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_cpuset_mems:
        ```

    ??? variable string "`sabnzbd_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_kernel_memory:
        ```

    ??? variable string "`sabnzbd_role_docker_memory`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_memory:
        ```

    ??? variable string "`sabnzbd_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_memory_reservation:
        ```

    ??? variable string "`sabnzbd_role_docker_memory_swap`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_memory_swap:
        ```

    ??? variable int "`sabnzbd_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        sabnzbd_role_docker_memory_swappiness:
        ```

    ??? variable string "`sabnzbd_role_docker_shm_size`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`sabnzbd_role_docker_cap_drop`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_cap_drop:
        ```

    ??? variable string "`sabnzbd_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_cgroupns_mode:
        ```

    ??? variable list "`sabnzbd_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`sabnzbd_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_device_read_bps:
        ```

    ??? variable list "`sabnzbd_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_device_read_iops:
        ```

    ??? variable list "`sabnzbd_role_docker_device_requests`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_device_requests:
        ```

    ??? variable list "`sabnzbd_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_device_write_bps:
        ```

    ??? variable list "`sabnzbd_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_device_write_iops:
        ```

    ??? variable list "`sabnzbd_role_docker_devices`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_devices:
        ```

    ??? variable string "`sabnzbd_role_docker_devices_default`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_devices_default:
        ```

    ??? variable list "`sabnzbd_role_docker_groups`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_groups:
        ```

    ??? variable bool "`sabnzbd_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_docker_privileged:
        ```

    ??? variable list "`sabnzbd_role_docker_security_opts`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_security_opts:
        ```

    ??? variable string "`sabnzbd_role_docker_user`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_user:
        ```

    ??? variable string "`sabnzbd_role_docker_userns_mode`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`sabnzbd_role_docker_dns_opts`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_dns_opts:
        ```

    ??? variable list "`sabnzbd_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_dns_search_domains:
        ```

    ??? variable list "`sabnzbd_role_docker_dns_servers`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_dns_servers:
        ```

    ??? variable string "`sabnzbd_role_docker_domainname`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_domainname:
        ```

    ??? variable list "`sabnzbd_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_exposed_ports:
        ```

    ??? variable dict "`sabnzbd_role_docker_hosts`"

        ```yaml
        # Type: dict
        sabnzbd_role_docker_hosts:
        ```

    ??? variable bool "`sabnzbd_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_docker_hosts_use_common:
        ```

    ??? variable string "`sabnzbd_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_ipc_mode:
        ```

    ??? variable list "`sabnzbd_role_docker_links`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_links:
        ```

    ??? variable string "`sabnzbd_role_docker_network_mode`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_network_mode:
        ```

    ??? variable string "`sabnzbd_role_docker_pid_mode`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_pid_mode:
        ```

    ??? variable list "`sabnzbd_role_docker_ports`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_ports:
        ```

    ??? variable string "`sabnzbd_role_docker_uts`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`sabnzbd_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_docker_keep_volumes:
        ```

    ??? variable list "`sabnzbd_role_docker_mounts`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_mounts:
        ```

    ??? variable dict "`sabnzbd_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        sabnzbd_role_docker_storage_opts:
        ```

    ??? variable list "`sabnzbd_role_docker_tmpfs`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_tmpfs:
        ```

    ??? variable string "`sabnzbd_role_docker_volume_driver`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_volume_driver:
        ```

    ??? variable list "`sabnzbd_role_docker_volumes_from`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_volumes_from:
        ```

    ??? variable bool "`sabnzbd_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_docker_volumes_global:
        ```

    ??? variable string "`sabnzbd_role_docker_working_dir`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`sabnzbd_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_docker_auto_remove:
        ```

    ??? variable bool "`sabnzbd_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_docker_cleanup:
        ```

    ??? variable string "`sabnzbd_role_docker_force_kill`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_force_kill:
        ```

    ??? variable dict "`sabnzbd_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        sabnzbd_role_docker_healthcheck:
        ```

    ??? variable int "`sabnzbd_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        sabnzbd_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`sabnzbd_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_docker_init:
        ```

    ??? variable string "`sabnzbd_role_docker_kill_signal`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_kill_signal:
        ```

    ??? variable string "`sabnzbd_role_docker_log_driver`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_log_driver:
        ```

    ??? variable dict "`sabnzbd_role_docker_log_options`"

        ```yaml
        # Type: dict
        sabnzbd_role_docker_log_options:
        ```

    ??? variable bool "`sabnzbd_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_docker_oom_killer:
        ```

    ??? variable int "`sabnzbd_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        sabnzbd_role_docker_oom_score_adj:
        ```

    ??? variable bool "`sabnzbd_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_docker_output_logs:
        ```

    ??? variable bool "`sabnzbd_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_docker_paused:
        ```

    ??? variable bool "`sabnzbd_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_docker_recreate:
        ```

    ??? variable int "`sabnzbd_role_docker_restart_retries`"

        ```yaml
        # Type: int
        sabnzbd_role_docker_restart_retries:
        ```

    ??? variable int "`sabnzbd_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        sabnzbd_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`sabnzbd_role_docker_capabilities`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_capabilities:
        ```

    ??? variable string "`sabnzbd_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_cgroup_parent:
        ```

    ??? variable list "`sabnzbd_role_docker_commands`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_commands:
        ```

    ??? variable int "`sabnzbd_role_docker_create_timeout`"

        ```yaml
        # Type: int
        sabnzbd_role_docker_create_timeout:
        ```

    ??? variable string "`sabnzbd_role_docker_entrypoint`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_entrypoint:
        ```

    ??? variable string "`sabnzbd_role_docker_env_file`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_env_file:
        ```

    ??? variable bool "`sabnzbd_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_docker_labels_use_common:
        ```

    ??? variable bool "`sabnzbd_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_docker_read_only:
        ```

    ??? variable string "`sabnzbd_role_docker_runtime`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_runtime:
        ```

    ??? variable list "`sabnzbd_role_docker_sysctls`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_sysctls:
        ```

    ??? variable list "`sabnzbd_role_docker_ulimits`"

        ```yaml
        # Type: list
        sabnzbd_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`sabnzbd_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        sabnzbd_role_autoheal_enabled: true
        ```

    ??? variable string "`sabnzbd_role_config_settings_custom`"

        ```yaml
        # Type: string
        sabnzbd_role_config_settings_custom:
        ```

    ??? variable string "`sabnzbd_role_config_settings_default`"

        ```yaml
        # Type: string
        sabnzbd_role_config_settings_default:
        ```

    ??? variable string "`sabnzbd_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        sabnzbd_role_depends_on: ""
        ```

    ??? variable string "`sabnzbd_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        sabnzbd_role_depends_on_delay: "0"
        ```

    ??? variable string "`sabnzbd_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        sabnzbd_role_depends_on_healthchecks:
        ```

    ??? variable bool "`sabnzbd_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        sabnzbd_role_diun_enabled: true
        ```

    ??? variable bool "`sabnzbd_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        sabnzbd_role_dns_enabled: true
        ```

    ??? variable bool "`sabnzbd_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        sabnzbd_role_docker_controller: true
        ```

    ??? variable string "`sabnzbd_role_docker_image_repo`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_image_repo:
        ```

    ??? variable string "`sabnzbd_role_docker_image_tag`"

        ```yaml
        # Type: string
        sabnzbd_role_docker_image_tag:
        ```

    ??? variable bool "`sabnzbd_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_docker_volumes_download:
        ```

    ??? variable string "`sabnzbd_role_paths_downloads_location`"

        ```yaml
        # Type: string
        sabnzbd_role_paths_downloads_location:
        ```

    ??? variable string "`sabnzbd_role_themepark_addons`"

        ```yaml
        # Type: string
        sabnzbd_role_themepark_addons:
        ```

    ??? variable string "`sabnzbd_role_themepark_app`"

        ```yaml
        # Type: string
        sabnzbd_role_themepark_app:
        ```

    ??? variable bool "`sabnzbd_role_themepark_enabled`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_themepark_enabled:
        ```

    ??? variable string "`sabnzbd_role_themepark_theme`"

        ```yaml
        # Type: string
        sabnzbd_role_themepark_theme:
        ```

    ??? variable dict "`sabnzbd_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        sabnzbd_role_traefik_api_endpoint:
        ```

    ??? variable string "`sabnzbd_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        sabnzbd_role_traefik_api_middleware:
        ```

    ??? variable string "`sabnzbd_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        sabnzbd_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`sabnzbd_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        sabnzbd_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`sabnzbd_role_traefik_certresolver`"

        ```yaml
        # Type: string
        sabnzbd_role_traefik_certresolver:
        ```

    ??? variable bool "`sabnzbd_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        sabnzbd_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`sabnzbd_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        sabnzbd_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`sabnzbd_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        sabnzbd_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`sabnzbd_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        sabnzbd_role_traefik_middleware_http:
        ```

    ??? variable bool "`sabnzbd_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`sabnzbd_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        sabnzbd_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`sabnzbd_role_traefik_priority`"

        ```yaml
        # Type: string
        sabnzbd_role_traefik_priority:
        ```

    ??? variable bool "`sabnzbd_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        sabnzbd_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`sabnzbd_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        sabnzbd_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`sabnzbd_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        sabnzbd_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`sabnzbd_role_web_domain`"

        ```yaml
        # Type: string
        sabnzbd_role_web_domain:
        ```

    ??? variable list "`sabnzbd_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        sabnzbd_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            sabnzbd_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "sabnzbd2.{{ user.domain }}"
              - "sabnzbd.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`sabnzbd_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        sabnzbd_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            sabnzbd_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'sabnzbd2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`sabnzbd_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        sabnzbd_role_web_http_port:
        ```

    ??? variable string "`sabnzbd_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        sabnzbd_role_web_http_scheme:
        ```

    ??? variable dict "`sabnzbd_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        sabnzbd_role_web_http_serverstransport:
        ```

    ??? variable string "`sabnzbd_role_web_port`"

        ```yaml
        # Type: string (quoted number)
        sabnzbd_role_web_port:
        ```

    ??? variable string "`sabnzbd_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        sabnzbd_role_web_scheme:
        ```

    ??? variable dict "`sabnzbd_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        sabnzbd_role_web_serverstransport:
        ```

    ??? variable string "`sabnzbd_role_web_subdomain`"

        ```yaml
        # Type: string
        sabnzbd_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
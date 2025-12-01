---
icon: material/docker
hide:
  - tags
tags:
  - jackett
---

# Jackett

## Overview

[hotio/jackett](https://hotio.dev/containers/jackett) is a Docker container image for Jackett.

> [Jackett](https://github.com/Jackett/Jackett) is a free, open-source, self-hosted indexer proxy server that acts as an intermediary between torrent indexing applications like Sonarr, Radarr, and qBittorrent, and various torrent trackers.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/hotio/bazarr/pkgs/container/bazarr){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://hotio.dev/discord){ .md-button .md-button--stretch }

</div>

---

!!! abstract directions "Saltbox Setup Process"

    <div data-search-exclude>

    <div>

    Opting for another indexer manager?

    <div>

    [**Explore alternatives**:material-shuffle-variant:](index.md#indexer-management){ .md-button }

    [**Skip to Sonarr**:material-fast-forward:](sonarr.md){ .md-button }

    </div>

    </div>

    </div>

## Deployment

```shell
sb install jackett
```

## Usage

Visit <http://jackett.iYOUR_DOMAIN_NAMEi>.

## Basics

### Settings

   ![](../images/jackett-settings.png)

### Disabling Auto Update

Under "Jackett Configuration":

1. Check "Disable auto update".

1. Check "External access".

1. Click "Apply server settings".

1. The page will now reload.

### Adding Indexers to Sonarr/Radarr

Under "Configured Indexers":

1. Click "Add Indexer" to add your favorite indexers (i.e. [torrent trackers](../reference/usenet-torrent.md)).

2. When adding indexers into [Sonarr](../apps/sonarr.md#__tabbed_3_2)/[Radarr](../apps/radarr.md#__tabbed_3_2), you will need:

    1. Indexer's Torznab Feed

         - Copy this by clicking on "Copy Torznab Feed" button next to the Indexer.

         - You will need to replace...

           - `https` with `http`

           - `jackett.xYOUR_DOMAIN_NAMEx` with `jackett:9117`

    2. Jacket API Key

## Next

<div class="directions-menu" markdown>

Are you setting Saltbox up for the first time?

<div markdown>

[**Continue to Sonarr**:material-forward:](sonarr.md){ .md-button }

</div>

</div>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    jackett_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `jackett_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `jackett_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`jackett_name`"

        ```yaml
        # Type: string
        jackett_name: jackett
        ```

=== "Paths"

    ??? variable string "`jackett_role_paths_folder`"

        ```yaml
        # Type: string
        jackett_role_paths_folder: "{{ jackett_name }}"
        ```

    ??? variable string "`jackett_role_paths_location`"

        ```yaml
        # Type: string
        jackett_role_paths_location: "{{ server_appdata_path }}/{{ jackett_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`jackett_role_web_subdomain`"

        ```yaml
        # Type: string
        jackett_role_web_subdomain: "{{ jackett_name }}"
        ```

    ??? variable string "`jackett_role_web_domain`"

        ```yaml
        # Type: string
        jackett_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`jackett_role_web_port`"

        ```yaml
        # Type: string
        jackett_role_web_port: "9117"
        ```

    ??? variable string "`jackett_role_web_url`"

        ```yaml
        # Type: string
        jackett_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='jackett') + '.' + lookup('role_var', '_web_domain', role='jackett')
                               if (lookup('role_var', '_web_subdomain', role='jackett') | length > 0)
                               else lookup('role_var', '_web_domain', role='jackett')) }}"
        ```

=== "DNS"

    ??? variable string "`jackett_role_dns_record`"

        ```yaml
        # Type: string
        jackett_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='jackett') }}"
        ```

    ??? variable string "`jackett_role_dns_zone`"

        ```yaml
        # Type: string
        jackett_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='jackett') }}"
        ```

    ??? variable bool "`jackett_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`jackett_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        jackett_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`jackett_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        jackett_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                     + (',themepark-' + jackett_name
                                                       if (lookup('role_var', '_themepark_enabled', role='jackett') and global_themepark_plugin_enabled)
                                                       else '') }}"
        ```

    ??? variable string "`jackett_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        jackett_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`jackett_role_traefik_certresolver`"

        ```yaml
        # Type: string
        jackett_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`jackett_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_traefik_enabled: true
        ```

    ??? variable bool "`jackett_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_traefik_api_enabled: true
        ```

    ??? variable string "`jackett_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        jackett_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/dl`)"
        ```

=== "Theme"

    ??? variable bool "`jackett_role_themepark_enabled`"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        jackett_role_themepark_enabled: false
        ```

    ??? variable string "`jackett_role_themepark_app`"

        ```yaml
        # Type: string
        jackett_role_themepark_app: "jackett"
        ```

    ??? variable string "`jackett_role_themepark_theme`"

        ```yaml
        # Type: string
        jackett_role_themepark_theme: "{{ global_themepark_theme }}"
        ```

    ??? variable string "`jackett_role_themepark_domain`"

        ```yaml
        # Type: string
        jackett_role_themepark_domain: "{{ global_themepark_domain }}"
        ```

    ??? variable list "`jackett_role_themepark_addons`"

        ```yaml
        # Type: list
        jackett_role_themepark_addons: []
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`jackett_role_docker_container`"

        ```yaml
        # Type: string
        jackett_role_docker_container: "{{ jackett_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`jackett_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_docker_image_pull: true
        ```

    ??? variable string "`jackett_role_docker_image_repo`"

        ```yaml
        # Type: string
        jackett_role_docker_image_repo: "ghcr.io/hotio/jackett"
        ```

    ??? variable string "`jackett_role_docker_image_tag`"

        ```yaml
        # Type: string
        jackett_role_docker_image_tag: "release"
        ```

    ??? variable string "`jackett_role_docker_image`"

        ```yaml
        # Type: string
        jackett_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='jackett') }}:{{ lookup('role_var', '_docker_image_tag', role='jackett') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`jackett_role_docker_envs_default`"

        ```yaml
        # Type: dict
        jackett_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          UMASK: "002"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`jackett_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        jackett_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`jackett_role_docker_volumes_default`"

        ```yaml
        # Type: list
        jackett_role_docker_volumes_default:
          - "{{ jackett_role_paths_location }}:/config"
        ```

    ??? variable list "`jackett_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        jackett_role_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable dict "`jackett_role_docker_labels_default`"

        ```yaml
        # Type: dict
        jackett_role_docker_labels_default: {}
        ```

    ??? variable dict "`jackett_role_docker_labels_custom`"

        ```yaml
        # Type: dict
        jackett_role_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`jackett_role_docker_hostname`"

        ```yaml
        # Type: string
        jackett_role_docker_hostname: "{{ jackett_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`jackett_role_docker_networks_alias`"

        ```yaml
        # Type: string
        jackett_role_docker_networks_alias: "{{ jackett_name }}"
        ```

    ??? variable list "`jackett_role_docker_networks_default`"

        ```yaml
        # Type: list
        jackett_role_docker_networks_default: []
        ```

    ??? variable list "`jackett_role_docker_networks_custom`"

        ```yaml
        # Type: list
        jackett_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`jackett_role_docker_restart_policy`"

        ```yaml
        # Type: string
        jackett_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`jackett_role_docker_state`"

        ```yaml
        # Type: string
        jackett_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`jackett_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        jackett_role_docker_blkio_weight:
        ```

    ??? variable int "`jackett_role_docker_cpu_period`"

        ```yaml
        # Type: int
        jackett_role_docker_cpu_period:
        ```

    ??? variable int "`jackett_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        jackett_role_docker_cpu_quota:
        ```

    ??? variable int "`jackett_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        jackett_role_docker_cpu_shares:
        ```

    ??? variable string "`jackett_role_docker_cpus`"

        ```yaml
        # Type: string
        jackett_role_docker_cpus:
        ```

    ??? variable string "`jackett_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        jackett_role_docker_cpuset_cpus:
        ```

    ??? variable string "`jackett_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        jackett_role_docker_cpuset_mems:
        ```

    ??? variable string "`jackett_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        jackett_role_docker_kernel_memory:
        ```

    ??? variable string "`jackett_role_docker_memory`"

        ```yaml
        # Type: string
        jackett_role_docker_memory:
        ```

    ??? variable string "`jackett_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        jackett_role_docker_memory_reservation:
        ```

    ??? variable string "`jackett_role_docker_memory_swap`"

        ```yaml
        # Type: string
        jackett_role_docker_memory_swap:
        ```

    ??? variable int "`jackett_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        jackett_role_docker_memory_swappiness:
        ```

    ??? variable string "`jackett_role_docker_shm_size`"

        ```yaml
        # Type: string
        jackett_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`jackett_role_docker_cap_drop`"

        ```yaml
        # Type: list
        jackett_role_docker_cap_drop:
        ```

    ??? variable string "`jackett_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        jackett_role_docker_cgroupns_mode:
        ```

    ??? variable list "`jackett_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        jackett_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`jackett_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        jackett_role_docker_device_read_bps:
        ```

    ??? variable list "`jackett_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        jackett_role_docker_device_read_iops:
        ```

    ??? variable list "`jackett_role_docker_device_requests`"

        ```yaml
        # Type: list
        jackett_role_docker_device_requests:
        ```

    ??? variable list "`jackett_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        jackett_role_docker_device_write_bps:
        ```

    ??? variable list "`jackett_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        jackett_role_docker_device_write_iops:
        ```

    ??? variable list "`jackett_role_docker_devices`"

        ```yaml
        # Type: list
        jackett_role_docker_devices:
        ```

    ??? variable string "`jackett_role_docker_devices_default`"

        ```yaml
        # Type: string
        jackett_role_docker_devices_default:
        ```

    ??? variable list "`jackett_role_docker_groups`"

        ```yaml
        # Type: list
        jackett_role_docker_groups:
        ```

    ??? variable bool "`jackett_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_docker_privileged:
        ```

    ??? variable list "`jackett_role_docker_security_opts`"

        ```yaml
        # Type: list
        jackett_role_docker_security_opts:
        ```

    ??? variable string "`jackett_role_docker_user`"

        ```yaml
        # Type: string
        jackett_role_docker_user:
        ```

    ??? variable string "`jackett_role_docker_userns_mode`"

        ```yaml
        # Type: string
        jackett_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`jackett_role_docker_dns_opts`"

        ```yaml
        # Type: list
        jackett_role_docker_dns_opts:
        ```

    ??? variable list "`jackett_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        jackett_role_docker_dns_search_domains:
        ```

    ??? variable list "`jackett_role_docker_dns_servers`"

        ```yaml
        # Type: list
        jackett_role_docker_dns_servers:
        ```

    ??? variable string "`jackett_role_docker_domainname`"

        ```yaml
        # Type: string
        jackett_role_docker_domainname:
        ```

    ??? variable list "`jackett_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        jackett_role_docker_exposed_ports:
        ```

    ??? variable dict "`jackett_role_docker_hosts`"

        ```yaml
        # Type: dict
        jackett_role_docker_hosts:
        ```

    ??? variable bool "`jackett_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_docker_hosts_use_common:
        ```

    ??? variable string "`jackett_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        jackett_role_docker_ipc_mode:
        ```

    ??? variable list "`jackett_role_docker_links`"

        ```yaml
        # Type: list
        jackett_role_docker_links:
        ```

    ??? variable string "`jackett_role_docker_network_mode`"

        ```yaml
        # Type: string
        jackett_role_docker_network_mode:
        ```

    ??? variable string "`jackett_role_docker_pid_mode`"

        ```yaml
        # Type: string
        jackett_role_docker_pid_mode:
        ```

    ??? variable list "`jackett_role_docker_ports`"

        ```yaml
        # Type: list
        jackett_role_docker_ports:
        ```

    ??? variable string "`jackett_role_docker_uts`"

        ```yaml
        # Type: string
        jackett_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`jackett_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_docker_keep_volumes:
        ```

    ??? variable list "`jackett_role_docker_mounts`"

        ```yaml
        # Type: list
        jackett_role_docker_mounts:
        ```

    ??? variable dict "`jackett_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        jackett_role_docker_storage_opts:
        ```

    ??? variable list "`jackett_role_docker_tmpfs`"

        ```yaml
        # Type: list
        jackett_role_docker_tmpfs:
        ```

    ??? variable string "`jackett_role_docker_volume_driver`"

        ```yaml
        # Type: string
        jackett_role_docker_volume_driver:
        ```

    ??? variable list "`jackett_role_docker_volumes_from`"

        ```yaml
        # Type: list
        jackett_role_docker_volumes_from:
        ```

    ??? variable bool "`jackett_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_docker_volumes_global:
        ```

    ??? variable string "`jackett_role_docker_working_dir`"

        ```yaml
        # Type: string
        jackett_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`jackett_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_docker_auto_remove:
        ```

    ??? variable bool "`jackett_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_docker_cleanup:
        ```

    ??? variable string "`jackett_role_docker_force_kill`"

        ```yaml
        # Type: string
        jackett_role_docker_force_kill:
        ```

    ??? variable dict "`jackett_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        jackett_role_docker_healthcheck:
        ```

    ??? variable int "`jackett_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        jackett_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`jackett_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_docker_init:
        ```

    ??? variable string "`jackett_role_docker_kill_signal`"

        ```yaml
        # Type: string
        jackett_role_docker_kill_signal:
        ```

    ??? variable string "`jackett_role_docker_log_driver`"

        ```yaml
        # Type: string
        jackett_role_docker_log_driver:
        ```

    ??? variable dict "`jackett_role_docker_log_options`"

        ```yaml
        # Type: dict
        jackett_role_docker_log_options:
        ```

    ??? variable bool "`jackett_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_docker_oom_killer:
        ```

    ??? variable int "`jackett_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        jackett_role_docker_oom_score_adj:
        ```

    ??? variable bool "`jackett_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_docker_output_logs:
        ```

    ??? variable bool "`jackett_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_docker_paused:
        ```

    ??? variable bool "`jackett_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_docker_recreate:
        ```

    ??? variable int "`jackett_role_docker_restart_retries`"

        ```yaml
        # Type: int
        jackett_role_docker_restart_retries:
        ```

    ??? variable int "`jackett_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        jackett_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`jackett_role_docker_capabilities`"

        ```yaml
        # Type: list
        jackett_role_docker_capabilities:
        ```

    ??? variable string "`jackett_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        jackett_role_docker_cgroup_parent:
        ```

    ??? variable list "`jackett_role_docker_commands`"

        ```yaml
        # Type: list
        jackett_role_docker_commands:
        ```

    ??? variable int "`jackett_role_docker_create_timeout`"

        ```yaml
        # Type: int
        jackett_role_docker_create_timeout:
        ```

    ??? variable string "`jackett_role_docker_entrypoint`"

        ```yaml
        # Type: string
        jackett_role_docker_entrypoint:
        ```

    ??? variable string "`jackett_role_docker_env_file`"

        ```yaml
        # Type: string
        jackett_role_docker_env_file:
        ```

    ??? variable bool "`jackett_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_docker_labels_use_common:
        ```

    ??? variable bool "`jackett_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_docker_read_only:
        ```

    ??? variable string "`jackett_role_docker_runtime`"

        ```yaml
        # Type: string
        jackett_role_docker_runtime:
        ```

    ??? variable list "`jackett_role_docker_sysctls`"

        ```yaml
        # Type: list
        jackett_role_docker_sysctls:
        ```

    ??? variable list "`jackett_role_docker_ulimits`"

        ```yaml
        # Type: list
        jackett_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`jackett_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        jackett_role_autoheal_enabled: true
        ```

    ??? variable string "`jackett_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        jackett_role_depends_on: ""
        ```

    ??? variable string "`jackett_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        jackett_role_depends_on_delay: "0"
        ```

    ??? variable string "`jackett_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        jackett_role_depends_on_healthchecks:
        ```

    ??? variable bool "`jackett_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        jackett_role_diun_enabled: true
        ```

    ??? variable bool "`jackett_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        jackett_role_dns_enabled: true
        ```

    ??? variable bool "`jackett_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        jackett_role_docker_controller: true
        ```

    ??? variable string "`jackett_role_docker_image_repo`"

        ```yaml
        # Type: string
        jackett_role_docker_image_repo:
        ```

    ??? variable string "`jackett_role_docker_image_tag`"

        ```yaml
        # Type: string
        jackett_role_docker_image_tag:
        ```

    ??? variable bool "`jackett_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_docker_volumes_download:
        ```

    ??? variable string "`jackett_role_themepark_addons`"

        ```yaml
        # Type: string
        jackett_role_themepark_addons:
        ```

    ??? variable string "`jackett_role_themepark_app`"

        ```yaml
        # Type: string
        jackett_role_themepark_app:
        ```

    ??? variable bool "`jackett_role_themepark_enabled`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_themepark_enabled:
        ```

    ??? variable string "`jackett_role_themepark_theme`"

        ```yaml
        # Type: string
        jackett_role_themepark_theme:
        ```

    ??? variable dict/omit "`jackett_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        jackett_role_traefik_api_endpoint:
        ```

    ??? variable string "`jackett_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        jackett_role_traefik_api_middleware:
        ```

    ??? variable string "`jackett_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        jackett_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`jackett_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        jackett_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`jackett_role_traefik_certresolver`"

        ```yaml
        # Type: string
        jackett_role_traefik_certresolver:
        ```

    ??? variable bool "`jackett_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        jackett_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`jackett_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        jackett_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`jackett_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        jackett_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`jackett_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        jackett_role_traefik_middleware_http:
        ```

    ??? variable bool "`jackett_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`jackett_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        jackett_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`jackett_role_traefik_priority`"

        ```yaml
        # Type: string
        jackett_role_traefik_priority:
        ```

    ??? variable bool "`jackett_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        jackett_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`jackett_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        jackett_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`jackett_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        jackett_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`jackett_role_web_domain`"

        ```yaml
        # Type: string
        jackett_role_web_domain:
        ```

    ??? variable list "`jackett_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        jackett_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            jackett_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "jackett2.{{ user.domain }}"
              - "jackett.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`jackett_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        jackett_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            jackett_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'jackett2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`jackett_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        jackett_role_web_http_port:
        ```

    ??? variable string "`jackett_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        jackett_role_web_http_scheme:
        ```

    ??? variable dict/omit "`jackett_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        jackett_role_web_http_serverstransport:
        ```

    ??? variable string "`jackett_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        jackett_role_web_scheme:
        ```

    ??? variable dict/omit "`jackett_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        jackett_role_web_serverstransport:
        ```

    ??? variable string "`jackett_role_web_subdomain`"

        ```yaml
        # Type: string
        jackett_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
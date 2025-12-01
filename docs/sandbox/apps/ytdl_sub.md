---
icon: material/docker
hide:
  - tags
tags:
  - ytdl-sub
  - youtube
  - downloads
---

# ytdl-sub

## Overview

[ytdl-sub](https://github.com/jmbannon/ytdl-sub) is a lightweight tool to automate downloading and metadata generation with yt-dlp. It uses YAML files to define subscriptions and prepares media for popular media players like Plex, Jellyfin, Kodi, and Emby.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://ytdl-sub.readthedocs.io){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/jmbannon/ytdl-sub/pkgs/container/ytdl-sub){ .md-button .md-button--stretch }

[:fontawesome-solid-people-group:**Community**](){ .md-button .md-button--stretch }

</div>

---

## Deployment

```shell
sb install sandbox-ytdl-sub
```

## Usage

Visit <https://ytdl-sub.iYOUR_DOMAIN_NAMEi>.

## Basics

The role supports two image types configurable via inventory:

- **GUI Mode** (`ytdl_sub_image_type: "gui"`): Web-based VS Code interface for full management
- **Headless Mode** (`ytdl_sub_image_type: "headless"`): Command-line focused, lightweight deployment (default)

Configure your subscriptions using YAML files in the config directory.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    ytdl_sub_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `ytdl_sub_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `ytdl_sub_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`ytdl_sub_name`"

        ```yaml
        # Type: string
        ytdl_sub_name: ytdl-sub
        ```

=== "Settings"

    ??? variable string "`ytdl_sub_role_cron_schedule`"

        ```yaml
        # Type: string
        ytdl_sub_role_cron_schedule: "0 */6 * * *"
        ```

    ??? variable string "`ytdl_sub_role_cron_on_start`"

        ```yaml
        # Type: string
        ytdl_sub_role_cron_on_start: "true"
        ```

    ??? variable string "`ytdl_sub_role_image_type`"

        ```yaml
        # Type: string
        ytdl_sub_role_image_type: "headless"
        ```

=== "Web"

    ??? variable string "`ytdl_sub_role_web_subdomain`"

        ```yaml
        # Type: string
        ytdl_sub_role_web_subdomain: "{{ ytdl_sub_name }}"
        ```

    ??? variable string "`ytdl_sub_role_web_domain`"

        ```yaml
        # Type: string
        ytdl_sub_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`ytdl_sub_role_web_port`"

        ```yaml
        # Type: string
        ytdl_sub_role_web_port: "8080"
        ```

    ??? variable string "`ytdl_sub_role_web_url`"

        ```yaml
        # Type: string
        ytdl_sub_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='ytdl_sub') + '.' + lookup('role_var', '_web_domain', role='ytdl_sub')
                                if (lookup('role_var', '_web_subdomain', role='ytdl_sub') | length > 0)
                                else lookup('role_var', '_web_domain', role='ytdl_sub')) }}"
        ```

=== "DNS"

    ??? variable string "`ytdl_sub_role_dns_record`"

        ```yaml
        # Type: string
        ytdl_sub_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='ytdl_sub') }}"
        ```

    ??? variable string "`ytdl_sub_role_dns_zone`"

        ```yaml
        # Type: string
        ytdl_sub_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='ytdl_sub') }}"
        ```

    ??? variable bool "`ytdl_sub_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`ytdl_sub_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        ytdl_sub_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`ytdl_sub_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        ytdl_sub_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`ytdl_sub_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        ytdl_sub_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`ytdl_sub_role_traefik_certresolver`"

        ```yaml
        # Type: string
        ytdl_sub_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`ytdl_sub_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_traefik_enabled: true
        ```

    ??? variable bool "`ytdl_sub_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_traefik_api_enabled: false
        ```

    ??? variable string "`ytdl_sub_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        ytdl_sub_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`ytdl_sub_role_docker_container`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_container: "{{ ytdl_sub_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`ytdl_sub_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_docker_image_pull: true
        ```

    ??? variable string "`ytdl_sub_role_docker_image_repo`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_image_repo: "{{ 'ghcr.io/jmbannon/ytdl-sub-gui' if lookup('role_var', '_image_type', role='ytdl_sub') == 'gui' else 'ghcr.io/jmbannon/ytdl-sub' }}"
        ```

    ??? variable string "`ytdl_sub_role_docker_image_tag`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_image_tag: "{{ 'latest' if lookup('role_var', '_image_type', role='ytdl_sub') == 'gui' else 'ubuntu-latest' }}"
        ```

    ??? variable string "`ytdl_sub_role_docker_image`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='ytdl_sub') }}:{{ lookup('role_var', '_docker_image_tag', role='ytdl_sub') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`ytdl_sub_role_docker_envs_default`"

        ```yaml
        # Type: dict
        ytdl_sub_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          CRON_SCHEDULE: "{{ lookup('role_var', '_cron_schedule', role='ytdl_sub') }}"
          CRON_RUN_ON_START: "{{ lookup('role_var', '_cron_on_start', role='ytdl_sub') }}"
        ```

    ??? variable dict "`ytdl_sub_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        ytdl_sub_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`ytdl_sub_role_docker_volumes_default`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='ytdl_sub') }}:/config"
          - "{{ lookup('role_var', '_paths_download_folder', role='ytdl_sub') }}:/ytdl_sub"
          - "{{ lookup('role_var', '_paths_download_folder', role='ytdl_sub') }}/tv_shows:/tv_shows"
          - "{{ lookup('role_var', '_paths_download_folder', role='ytdl_sub') }}/movies:/movies"
          - "{{ lookup('role_var', '_paths_download_folder', role='ytdl_sub') }}/music_videos:/music_videos"
          - "{{ lookup('role_var', '_paths_download_folder', role='ytdl_sub') }}/music:/music"
        ```

    ??? variable list "`ytdl_sub_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`ytdl_sub_role_docker_hostname`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_hostname: "{{ ytdl_sub_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`ytdl_sub_role_docker_networks_alias`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_networks_alias: "{{ ytdl_sub_name }}"
        ```

    ??? variable list "`ytdl_sub_role_docker_networks_default`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_networks_default: []
        ```

    ??? variable list "`ytdl_sub_role_docker_networks_custom`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`ytdl_sub_role_docker_restart_policy`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`ytdl_sub_role_docker_state`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`ytdl_sub_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        ytdl_sub_role_docker_blkio_weight:
        ```

    ??? variable int "`ytdl_sub_role_docker_cpu_period`"

        ```yaml
        # Type: int
        ytdl_sub_role_docker_cpu_period:
        ```

    ??? variable int "`ytdl_sub_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        ytdl_sub_role_docker_cpu_quota:
        ```

    ??? variable int "`ytdl_sub_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        ytdl_sub_role_docker_cpu_shares:
        ```

    ??? variable string "`ytdl_sub_role_docker_cpus`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_cpus:
        ```

    ??? variable string "`ytdl_sub_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_cpuset_cpus:
        ```

    ??? variable string "`ytdl_sub_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_cpuset_mems:
        ```

    ??? variable string "`ytdl_sub_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_kernel_memory:
        ```

    ??? variable string "`ytdl_sub_role_docker_memory`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_memory:
        ```

    ??? variable string "`ytdl_sub_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_memory_reservation:
        ```

    ??? variable string "`ytdl_sub_role_docker_memory_swap`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_memory_swap:
        ```

    ??? variable int "`ytdl_sub_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        ytdl_sub_role_docker_memory_swappiness:
        ```

    ??? variable string "`ytdl_sub_role_docker_shm_size`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`ytdl_sub_role_docker_cap_drop`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_cap_drop:
        ```

    ??? variable string "`ytdl_sub_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_cgroupns_mode:
        ```

    ??? variable list "`ytdl_sub_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`ytdl_sub_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_device_read_bps:
        ```

    ??? variable list "`ytdl_sub_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_device_read_iops:
        ```

    ??? variable list "`ytdl_sub_role_docker_device_requests`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_device_requests:
        ```

    ??? variable list "`ytdl_sub_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_device_write_bps:
        ```

    ??? variable list "`ytdl_sub_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_device_write_iops:
        ```

    ??? variable list "`ytdl_sub_role_docker_devices`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_devices:
        ```

    ??? variable string "`ytdl_sub_role_docker_devices_default`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_devices_default:
        ```

    ??? variable list "`ytdl_sub_role_docker_groups`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_groups:
        ```

    ??? variable bool "`ytdl_sub_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_docker_privileged:
        ```

    ??? variable list "`ytdl_sub_role_docker_security_opts`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_security_opts:
        ```

    ??? variable string "`ytdl_sub_role_docker_user`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_user:
        ```

    ??? variable string "`ytdl_sub_role_docker_userns_mode`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`ytdl_sub_role_docker_dns_opts`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_dns_opts:
        ```

    ??? variable list "`ytdl_sub_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_dns_search_domains:
        ```

    ??? variable list "`ytdl_sub_role_docker_dns_servers`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_dns_servers:
        ```

    ??? variable string "`ytdl_sub_role_docker_domainname`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_domainname:
        ```

    ??? variable list "`ytdl_sub_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_exposed_ports:
        ```

    ??? variable dict "`ytdl_sub_role_docker_hosts`"

        ```yaml
        # Type: dict
        ytdl_sub_role_docker_hosts:
        ```

    ??? variable bool "`ytdl_sub_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_docker_hosts_use_common:
        ```

    ??? variable string "`ytdl_sub_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_ipc_mode:
        ```

    ??? variable list "`ytdl_sub_role_docker_links`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_links:
        ```

    ??? variable string "`ytdl_sub_role_docker_network_mode`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_network_mode:
        ```

    ??? variable string "`ytdl_sub_role_docker_pid_mode`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_pid_mode:
        ```

    ??? variable list "`ytdl_sub_role_docker_ports`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_ports:
        ```

    ??? variable string "`ytdl_sub_role_docker_uts`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`ytdl_sub_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_docker_keep_volumes:
        ```

    ??? variable list "`ytdl_sub_role_docker_mounts`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_mounts:
        ```

    ??? variable dict "`ytdl_sub_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        ytdl_sub_role_docker_storage_opts:
        ```

    ??? variable list "`ytdl_sub_role_docker_tmpfs`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_tmpfs:
        ```

    ??? variable string "`ytdl_sub_role_docker_volume_driver`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_volume_driver:
        ```

    ??? variable list "`ytdl_sub_role_docker_volumes_from`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_volumes_from:
        ```

    ??? variable bool "`ytdl_sub_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_docker_volumes_global:
        ```

    ??? variable string "`ytdl_sub_role_docker_working_dir`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`ytdl_sub_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_docker_auto_remove:
        ```

    ??? variable bool "`ytdl_sub_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_docker_cleanup:
        ```

    ??? variable string "`ytdl_sub_role_docker_force_kill`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_force_kill:
        ```

    ??? variable dict "`ytdl_sub_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        ytdl_sub_role_docker_healthcheck:
        ```

    ??? variable int "`ytdl_sub_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        ytdl_sub_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`ytdl_sub_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_docker_init:
        ```

    ??? variable string "`ytdl_sub_role_docker_kill_signal`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_kill_signal:
        ```

    ??? variable string "`ytdl_sub_role_docker_log_driver`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_log_driver:
        ```

    ??? variable dict "`ytdl_sub_role_docker_log_options`"

        ```yaml
        # Type: dict
        ytdl_sub_role_docker_log_options:
        ```

    ??? variable bool "`ytdl_sub_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_docker_oom_killer:
        ```

    ??? variable int "`ytdl_sub_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        ytdl_sub_role_docker_oom_score_adj:
        ```

    ??? variable bool "`ytdl_sub_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_docker_output_logs:
        ```

    ??? variable bool "`ytdl_sub_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_docker_paused:
        ```

    ??? variable bool "`ytdl_sub_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_docker_recreate:
        ```

    ??? variable int "`ytdl_sub_role_docker_restart_retries`"

        ```yaml
        # Type: int
        ytdl_sub_role_docker_restart_retries:
        ```

    ??? variable int "`ytdl_sub_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        ytdl_sub_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`ytdl_sub_role_docker_capabilities`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_capabilities:
        ```

    ??? variable string "`ytdl_sub_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_cgroup_parent:
        ```

    ??? variable list "`ytdl_sub_role_docker_commands`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_commands:
        ```

    ??? variable int "`ytdl_sub_role_docker_create_timeout`"

        ```yaml
        # Type: int
        ytdl_sub_role_docker_create_timeout:
        ```

    ??? variable string "`ytdl_sub_role_docker_entrypoint`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_entrypoint:
        ```

    ??? variable string "`ytdl_sub_role_docker_env_file`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_env_file:
        ```

    ??? variable dict "`ytdl_sub_role_docker_labels`"

        ```yaml
        # Type: dict
        ytdl_sub_role_docker_labels:
        ```

    ??? variable bool "`ytdl_sub_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_docker_labels_use_common:
        ```

    ??? variable bool "`ytdl_sub_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_docker_read_only:
        ```

    ??? variable string "`ytdl_sub_role_docker_runtime`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_runtime:
        ```

    ??? variable list "`ytdl_sub_role_docker_sysctls`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_sysctls:
        ```

    ??? variable list "`ytdl_sub_role_docker_ulimits`"

        ```yaml
        # Type: list
        ytdl_sub_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`ytdl_sub_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        ytdl_sub_role_autoheal_enabled: true
        ```

    ??? variable string "`ytdl_sub_role_cron_on_start`"

        ```yaml
        # Type: string
        ytdl_sub_role_cron_on_start:
        ```

    ??? variable string "`ytdl_sub_role_cron_schedule`"

        ```yaml
        # Type: string
        ytdl_sub_role_cron_schedule:
        ```

    ??? variable string "`ytdl_sub_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        ytdl_sub_role_depends_on: ""
        ```

    ??? variable string "`ytdl_sub_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        ytdl_sub_role_depends_on_delay: "0"
        ```

    ??? variable string "`ytdl_sub_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        ytdl_sub_role_depends_on_healthchecks:
        ```

    ??? variable bool "`ytdl_sub_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        ytdl_sub_role_diun_enabled: true
        ```

    ??? variable bool "`ytdl_sub_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        ytdl_sub_role_dns_enabled: true
        ```

    ??? variable bool "`ytdl_sub_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        ytdl_sub_role_docker_controller: true
        ```

    ??? variable string "`ytdl_sub_role_docker_image_repo`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_image_repo:
        ```

    ??? variable string "`ytdl_sub_role_docker_image_tag`"

        ```yaml
        # Type: string
        ytdl_sub_role_docker_image_tag:
        ```

    ??? variable bool "`ytdl_sub_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_docker_volumes_download:
        ```

    ??? variable string "`ytdl_sub_role_image_type`"

        ```yaml
        # Type: string
        ytdl_sub_role_image_type:
        ```

    ??? variable string "`ytdl_sub_role_paths_download_folder`"

        ```yaml
        # Type: string
        ytdl_sub_role_paths_download_folder:
        ```

    ??? variable string "`ytdl_sub_role_paths_location`"

        ```yaml
        # Type: string
        ytdl_sub_role_paths_location:
        ```

    ??? variable string "`ytdl_sub_role_themepark_addons`"

        ```yaml
        # Type: string
        ytdl_sub_role_themepark_addons:
        ```

    ??? variable string "`ytdl_sub_role_themepark_app`"

        ```yaml
        # Type: string
        ytdl_sub_role_themepark_app:
        ```

    ??? variable string "`ytdl_sub_role_themepark_theme`"

        ```yaml
        # Type: string
        ytdl_sub_role_themepark_theme:
        ```

    ??? variable dict/omit "`ytdl_sub_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        ytdl_sub_role_traefik_api_endpoint:
        ```

    ??? variable string "`ytdl_sub_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        ytdl_sub_role_traefik_api_middleware:
        ```

    ??? variable string "`ytdl_sub_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        ytdl_sub_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`ytdl_sub_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        ytdl_sub_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`ytdl_sub_role_traefik_certresolver`"

        ```yaml
        # Type: string
        ytdl_sub_role_traefik_certresolver:
        ```

    ??? variable bool "`ytdl_sub_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        ytdl_sub_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`ytdl_sub_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        ytdl_sub_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`ytdl_sub_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        ytdl_sub_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`ytdl_sub_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        ytdl_sub_role_traefik_middleware_http:
        ```

    ??? variable bool "`ytdl_sub_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`ytdl_sub_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        ytdl_sub_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`ytdl_sub_role_traefik_priority`"

        ```yaml
        # Type: string
        ytdl_sub_role_traefik_priority:
        ```

    ??? variable bool "`ytdl_sub_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        ytdl_sub_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`ytdl_sub_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        ytdl_sub_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`ytdl_sub_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        ytdl_sub_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`ytdl_sub_role_web_domain`"

        ```yaml
        # Type: string
        ytdl_sub_role_web_domain:
        ```

    ??? variable list "`ytdl_sub_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        ytdl_sub_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            ytdl_sub_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "ytdl_sub2.{{ user.domain }}"
              - "ytdl_sub.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`ytdl_sub_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        ytdl_sub_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            ytdl_sub_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'ytdl_sub2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`ytdl_sub_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        ytdl_sub_role_web_http_port:
        ```

    ??? variable string "`ytdl_sub_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        ytdl_sub_role_web_http_scheme:
        ```

    ??? variable dict/omit "`ytdl_sub_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        ytdl_sub_role_web_http_serverstransport:
        ```

    ??? variable string "`ytdl_sub_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        ytdl_sub_role_web_scheme:
        ```

    ??? variable dict/omit "`ytdl_sub_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        ytdl_sub_role_web_serverstransport:
        ```

    ??? variable string "`ytdl_sub_role_web_subdomain`"

        ```yaml
        # Type: string
        ytdl_sub_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
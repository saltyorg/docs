---
icon: material/docker
hide:
  - tags
tags:
  - tdarr
  - media
  - encoding
---

# Tdarr

## Overview

[Tdarr](https://tdarr.io/) is a cross-platform conditional based transcoding application for automating media library transcode/remux management in order to process your media files as required. For example, you can set rules for the required codecs, containers, languages etc that your media should have which helps keeps things organized and can increase compatability with your devices. A common use for Tdarr is to simply convert video files from h264 to h265 (hevc), saving 40%-50% in size.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://docs.tdarr.io/docs/welcome/what){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/haveagitgat/tdarr/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-people-group:**Community**](){ .md-button .md-button--stretch }

</div>

---

## Deployment

```shell
sb install sandbox-tdarr
```

## Usage

Visit <https://tdarr.iYOUR_DOMAIN_NAMEi>.

## Basics

Tdarr is configured with the following defaults which can be modified via the inventory system.

```yaml
tdarr_server_port: "8266"
tdarr_server_external: false
```

By switching `tdarr_server_external` to `true` the Tdarr server will be accessible externally via the specified `tdarr_server_port` on any hostname or IP address pointing directly to the server.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        tdarr_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `tdarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `tdarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`tdarr_name`"

        ```yaml
        # Type: string
        tdarr_name: tdarr
        ```

=== "Settings"

    ??? variable string "`tdarr_role_server_port`"

        ```yaml
        # Type: string
        tdarr_role_server_port: "8266"
        ```

    ??? variable bool "`tdarr_role_server_external`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_server_external: false
        ```

=== "Web"

    ??? variable string "`tdarr_role_web_subdomain`"

        ```yaml
        # Type: string
        tdarr_role_web_subdomain: "{{ tdarr_name }}"
        ```

    ??? variable string "`tdarr_role_web_domain`"

        ```yaml
        # Type: string
        tdarr_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`tdarr_role_web_port`"

        ```yaml
        # Type: string
        tdarr_role_web_port: "8265"
        ```

    ??? variable string "`tdarr_role_web_url`"

        ```yaml
        # Type: string
        tdarr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='tdarr') + '.' + lookup('role_var', '_web_domain', role='tdarr')
                             if (lookup('role_var', '_web_subdomain', role='tdarr') | length > 0)
                             else lookup('role_var', '_web_domain', role='tdarr')) }}"
        ```

=== "DNS"

    ??? variable string "`tdarr_role_dns_record`"

        ```yaml
        # Type: string
        tdarr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='tdarr') }}"
        ```

    ??? variable string "`tdarr_role_dns_zone`"

        ```yaml
        # Type: string
        tdarr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='tdarr') }}"
        ```

    ??? variable bool "`tdarr_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`tdarr_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        tdarr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`tdarr_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        tdarr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`tdarr_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        tdarr_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`tdarr_role_traefik_certresolver`"

        ```yaml
        # Type: string
        tdarr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`tdarr_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_traefik_enabled: true
        ```

    ??? variable bool "`tdarr_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_traefik_api_enabled: false
        ```

    ??? variable string "`tdarr_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        tdarr_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`tdarr_role_docker_container`"

        ```yaml
        # Type: string
        tdarr_role_docker_container: "{{ tdarr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`tdarr_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_docker_image_pull: true
        ```

    ??? variable string "`tdarr_role_docker_image_repo`"

        ```yaml
        # Type: string
        tdarr_role_docker_image_repo: "haveagitgat/tdarr"
        ```

    ??? variable string "`tdarr_role_docker_image_tag`"

        ```yaml
        # Type: string
        tdarr_role_docker_image_tag: "latest"
        ```

    ??? variable string "`tdarr_role_docker_image`"

        ```yaml
        # Type: string
        tdarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='tdarr') }}:{{ lookup('role_var', '_docker_image_tag', role='tdarr') }}"
        ```

    <h5>Ports</h5>

    ??? variable list "`tdarr_role_docker_ports_default`"

        ```yaml
        # Type: list
        tdarr_role_docker_ports_default:
          - "{{ lookup('role_var', '_server_port', role='tdarr') }}:{{ lookup('role_var', '_server_port', role='tdarr') }}"
        ```

    ??? variable list "`tdarr_role_docker_ports_custom`"

        ```yaml
        # Type: list
        tdarr_role_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    ??? variable dict "`tdarr_role_docker_envs_default`"

        ```yaml
        # Type: dict
        tdarr_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          serverIP: "0.0.0.0"
          webUIPort: "8265"
          serverPort: "{{ lookup('role_var', '_server_port', role='tdarr') }}"
          internalNode: "true"
          inContainer: "true"
        ```

    ??? variable dict "`tdarr_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        tdarr_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`tdarr_role_docker_volumes_default`"

        ```yaml
        # Type: list
        tdarr_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_configs_location', role='tdarr') }}:/app/configs"
          - "{{ lookup('role_var', '_paths_server_location', role='tdarr') }}:/app/server"
          - "{{ lookup('role_var', '_paths_logs_location', role='tdarr') }}:/app/logs"
          - "{{ lookup('role_var', '_paths_transcodes_location', role='tdarr') }}:/temp"
          - "/mnt/unionfs/Media:/media"
          - "/mnt/unionfs/Media/Movies:/movies"
          - "/mnt/unionfs/Media/TV:/tv"
          - "/dev/shm:/dev/shm"
        ```

    ??? variable list "`tdarr_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        tdarr_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`tdarr_role_docker_hostname`"

        ```yaml
        # Type: string
        tdarr_role_docker_hostname: "{{ tdarr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`tdarr_role_docker_networks_alias`"

        ```yaml
        # Type: string
        tdarr_role_docker_networks_alias: "{{ tdarr_name }}"
        ```

    ??? variable list "`tdarr_role_docker_networks_default`"

        ```yaml
        # Type: list
        tdarr_role_docker_networks_default: []
        ```

    ??? variable list "`tdarr_role_docker_networks_custom`"

        ```yaml
        # Type: list
        tdarr_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`tdarr_role_docker_restart_policy`"

        ```yaml
        # Type: string
        tdarr_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`tdarr_role_docker_state`"

        ```yaml
        # Type: string
        tdarr_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`tdarr_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        tdarr_role_docker_blkio_weight:
        ```

    ??? variable int "`tdarr_role_docker_cpu_period`"

        ```yaml
        # Type: int
        tdarr_role_docker_cpu_period:
        ```

    ??? variable int "`tdarr_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        tdarr_role_docker_cpu_quota:
        ```

    ??? variable int "`tdarr_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        tdarr_role_docker_cpu_shares:
        ```

    ??? variable string "`tdarr_role_docker_cpus`"

        ```yaml
        # Type: string
        tdarr_role_docker_cpus:
        ```

    ??? variable string "`tdarr_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        tdarr_role_docker_cpuset_cpus:
        ```

    ??? variable string "`tdarr_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        tdarr_role_docker_cpuset_mems:
        ```

    ??? variable string "`tdarr_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        tdarr_role_docker_kernel_memory:
        ```

    ??? variable string "`tdarr_role_docker_memory`"

        ```yaml
        # Type: string
        tdarr_role_docker_memory:
        ```

    ??? variable string "`tdarr_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        tdarr_role_docker_memory_reservation:
        ```

    ??? variable string "`tdarr_role_docker_memory_swap`"

        ```yaml
        # Type: string
        tdarr_role_docker_memory_swap:
        ```

    ??? variable int "`tdarr_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        tdarr_role_docker_memory_swappiness:
        ```

    ??? variable string "`tdarr_role_docker_shm_size`"

        ```yaml
        # Type: string
        tdarr_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`tdarr_role_docker_cap_drop`"

        ```yaml
        # Type: list
        tdarr_role_docker_cap_drop:
        ```

    ??? variable string "`tdarr_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        tdarr_role_docker_cgroupns_mode:
        ```

    ??? variable list "`tdarr_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        tdarr_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`tdarr_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        tdarr_role_docker_device_read_bps:
        ```

    ??? variable list "`tdarr_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        tdarr_role_docker_device_read_iops:
        ```

    ??? variable list "`tdarr_role_docker_device_requests`"

        ```yaml
        # Type: list
        tdarr_role_docker_device_requests:
        ```

    ??? variable list "`tdarr_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        tdarr_role_docker_device_write_bps:
        ```

    ??? variable list "`tdarr_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        tdarr_role_docker_device_write_iops:
        ```

    ??? variable list "`tdarr_role_docker_devices`"

        ```yaml
        # Type: list
        tdarr_role_docker_devices:
        ```

    ??? variable string "`tdarr_role_docker_devices_default`"

        ```yaml
        # Type: string
        tdarr_role_docker_devices_default:
        ```

    ??? variable list "`tdarr_role_docker_groups`"

        ```yaml
        # Type: list
        tdarr_role_docker_groups:
        ```

    ??? variable bool "`tdarr_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_docker_privileged:
        ```

    ??? variable list "`tdarr_role_docker_security_opts`"

        ```yaml
        # Type: list
        tdarr_role_docker_security_opts:
        ```

    ??? variable string "`tdarr_role_docker_user`"

        ```yaml
        # Type: string
        tdarr_role_docker_user:
        ```

    ??? variable string "`tdarr_role_docker_userns_mode`"

        ```yaml
        # Type: string
        tdarr_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`tdarr_role_docker_dns_opts`"

        ```yaml
        # Type: list
        tdarr_role_docker_dns_opts:
        ```

    ??? variable list "`tdarr_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        tdarr_role_docker_dns_search_domains:
        ```

    ??? variable list "`tdarr_role_docker_dns_servers`"

        ```yaml
        # Type: list
        tdarr_role_docker_dns_servers:
        ```

    ??? variable string "`tdarr_role_docker_domainname`"

        ```yaml
        # Type: string
        tdarr_role_docker_domainname:
        ```

    ??? variable list "`tdarr_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        tdarr_role_docker_exposed_ports:
        ```

    ??? variable dict "`tdarr_role_docker_hosts`"

        ```yaml
        # Type: dict
        tdarr_role_docker_hosts:
        ```

    ??? variable bool "`tdarr_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_docker_hosts_use_common:
        ```

    ??? variable string "`tdarr_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        tdarr_role_docker_ipc_mode:
        ```

    ??? variable list "`tdarr_role_docker_links`"

        ```yaml
        # Type: list
        tdarr_role_docker_links:
        ```

    ??? variable string "`tdarr_role_docker_network_mode`"

        ```yaml
        # Type: string
        tdarr_role_docker_network_mode:
        ```

    ??? variable string "`tdarr_role_docker_pid_mode`"

        ```yaml
        # Type: string
        tdarr_role_docker_pid_mode:
        ```

    ??? variable string "`tdarr_role_docker_uts`"

        ```yaml
        # Type: string
        tdarr_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`tdarr_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_docker_keep_volumes:
        ```

    ??? variable list "`tdarr_role_docker_mounts`"

        ```yaml
        # Type: list
        tdarr_role_docker_mounts:
        ```

    ??? variable dict "`tdarr_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        tdarr_role_docker_storage_opts:
        ```

    ??? variable list "`tdarr_role_docker_tmpfs`"

        ```yaml
        # Type: list
        tdarr_role_docker_tmpfs:
        ```

    ??? variable string "`tdarr_role_docker_volume_driver`"

        ```yaml
        # Type: string
        tdarr_role_docker_volume_driver:
        ```

    ??? variable list "`tdarr_role_docker_volumes_from`"

        ```yaml
        # Type: list
        tdarr_role_docker_volumes_from:
        ```

    ??? variable bool "`tdarr_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_docker_volumes_global:
        ```

    ??? variable string "`tdarr_role_docker_working_dir`"

        ```yaml
        # Type: string
        tdarr_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`tdarr_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_docker_auto_remove:
        ```

    ??? variable bool "`tdarr_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_docker_cleanup:
        ```

    ??? variable string "`tdarr_role_docker_force_kill`"

        ```yaml
        # Type: string
        tdarr_role_docker_force_kill:
        ```

    ??? variable dict "`tdarr_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        tdarr_role_docker_healthcheck:
        ```

    ??? variable int "`tdarr_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        tdarr_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`tdarr_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_docker_init:
        ```

    ??? variable string "`tdarr_role_docker_kill_signal`"

        ```yaml
        # Type: string
        tdarr_role_docker_kill_signal:
        ```

    ??? variable string "`tdarr_role_docker_log_driver`"

        ```yaml
        # Type: string
        tdarr_role_docker_log_driver:
        ```

    ??? variable dict "`tdarr_role_docker_log_options`"

        ```yaml
        # Type: dict
        tdarr_role_docker_log_options:
        ```

    ??? variable bool "`tdarr_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_docker_oom_killer:
        ```

    ??? variable int "`tdarr_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        tdarr_role_docker_oom_score_adj:
        ```

    ??? variable bool "`tdarr_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_docker_output_logs:
        ```

    ??? variable bool "`tdarr_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_docker_paused:
        ```

    ??? variable bool "`tdarr_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_docker_recreate:
        ```

    ??? variable int "`tdarr_role_docker_restart_retries`"

        ```yaml
        # Type: int
        tdarr_role_docker_restart_retries:
        ```

    ??? variable int "`tdarr_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        tdarr_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`tdarr_role_docker_capabilities`"

        ```yaml
        # Type: list
        tdarr_role_docker_capabilities:
        ```

    ??? variable string "`tdarr_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        tdarr_role_docker_cgroup_parent:
        ```

    ??? variable list "`tdarr_role_docker_commands`"

        ```yaml
        # Type: list
        tdarr_role_docker_commands:
        ```

    ??? variable int "`tdarr_role_docker_create_timeout`"

        ```yaml
        # Type: int
        tdarr_role_docker_create_timeout:
        ```

    ??? variable string "`tdarr_role_docker_entrypoint`"

        ```yaml
        # Type: string
        tdarr_role_docker_entrypoint:
        ```

    ??? variable string "`tdarr_role_docker_env_file`"

        ```yaml
        # Type: string
        tdarr_role_docker_env_file:
        ```

    ??? variable dict "`tdarr_role_docker_labels`"

        ```yaml
        # Type: dict
        tdarr_role_docker_labels:
        ```

    ??? variable bool "`tdarr_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_docker_labels_use_common:
        ```

    ??? variable bool "`tdarr_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_docker_read_only:
        ```

    ??? variable string "`tdarr_role_docker_runtime`"

        ```yaml
        # Type: string
        tdarr_role_docker_runtime:
        ```

    ??? variable list "`tdarr_role_docker_sysctls`"

        ```yaml
        # Type: list
        tdarr_role_docker_sysctls:
        ```

    ??? variable list "`tdarr_role_docker_ulimits`"

        ```yaml
        # Type: list
        tdarr_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`tdarr_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        tdarr_role_autoheal_enabled: true
        ```

    ??? variable string "`tdarr_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        tdarr_role_depends_on: ""
        ```

    ??? variable string "`tdarr_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        tdarr_role_depends_on_delay: "0"
        ```

    ??? variable string "`tdarr_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        tdarr_role_depends_on_healthchecks:
        ```

    ??? variable bool "`tdarr_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        tdarr_role_diun_enabled: true
        ```

    ??? variable bool "`tdarr_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        tdarr_role_dns_enabled: true
        ```

    ??? variable bool "`tdarr_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        tdarr_role_docker_controller: true
        ```

    ??? variable string "`tdarr_role_docker_image_repo`"

        ```yaml
        # Type: string
        tdarr_role_docker_image_repo:
        ```

    ??? variable string "`tdarr_role_docker_image_tag`"

        ```yaml
        # Type: string
        tdarr_role_docker_image_tag:
        ```

    ??? variable bool "`tdarr_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_docker_volumes_download:
        ```

    ??? variable string "`tdarr_role_paths_configs_location`"

        ```yaml
        # Type: string
        tdarr_role_paths_configs_location:
        ```

    ??? variable string "`tdarr_role_paths_logs_location`"

        ```yaml
        # Type: string
        tdarr_role_paths_logs_location:
        ```

    ??? variable string "`tdarr_role_paths_server_location`"

        ```yaml
        # Type: string
        tdarr_role_paths_server_location:
        ```

    ??? variable string "`tdarr_role_paths_transcodes_location`"

        ```yaml
        # Type: string
        tdarr_role_paths_transcodes_location:
        ```

    ??? variable string "`tdarr_role_server_port`"

        ```yaml
        # Type: string (quoted number)
        tdarr_role_server_port:
        ```

    ??? variable string "`tdarr_role_themepark_addons`"

        ```yaml
        # Type: string
        tdarr_role_themepark_addons:
        ```

    ??? variable string "`tdarr_role_themepark_app`"

        ```yaml
        # Type: string
        tdarr_role_themepark_app:
        ```

    ??? variable string "`tdarr_role_themepark_theme`"

        ```yaml
        # Type: string
        tdarr_role_themepark_theme:
        ```

    ??? variable dict "`tdarr_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        tdarr_role_traefik_api_endpoint:
        ```

    ??? variable string "`tdarr_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        tdarr_role_traefik_api_middleware:
        ```

    ??? variable string "`tdarr_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        tdarr_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`tdarr_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        tdarr_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`tdarr_role_traefik_certresolver`"

        ```yaml
        # Type: string
        tdarr_role_traefik_certresolver:
        ```

    ??? variable bool "`tdarr_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        tdarr_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`tdarr_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        tdarr_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`tdarr_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        tdarr_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`tdarr_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        tdarr_role_traefik_middleware_http:
        ```

    ??? variable bool "`tdarr_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`tdarr_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`tdarr_role_traefik_priority`"

        ```yaml
        # Type: string
        tdarr_role_traefik_priority:
        ```

    ??? variable bool "`tdarr_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        tdarr_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`tdarr_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        tdarr_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`tdarr_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        tdarr_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`tdarr_role_web_domain`"

        ```yaml
        # Type: string
        tdarr_role_web_domain:
        ```

    ??? variable list "`tdarr_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        tdarr_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            tdarr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "tdarr2.{{ user.domain }}"
              - "tdarr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`tdarr_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        tdarr_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            tdarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'tdarr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`tdarr_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        tdarr_role_web_http_port:
        ```

    ??? variable string "`tdarr_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        tdarr_role_web_http_scheme:
        ```

    ??? variable dict "`tdarr_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        tdarr_role_web_http_serverstransport:
        ```

    ??? variable string "`tdarr_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        tdarr_role_web_scheme:
        ```

    ??? variable dict "`tdarr_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        tdarr_role_web_serverstransport:
        ```

    ??? variable string "`tdarr_role_web_subdomain`"

        ```yaml
        # Type: string
        tdarr_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
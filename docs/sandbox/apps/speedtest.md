---
icon: material/docker
hide:
  - tags
tags:
  - speedtest
  - monitoring
  - network
---

# Speedtest

## Overview

[linuxserver/librespeed](https://docs.linuxserver.io/images/docker-librespeed) is a Docker container image for Speedtest.

> [Speedtest](https://github.com/librespeed/speedtest)  is a very lightweight Speedtest implemented in Javascript, using XMLHttpRequest and Web Workers. [:material-bookshelf:](https://github.com/librespeed/speedtest)

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://docs.linuxserver.io/general/container-customization){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/linuxserver/librespeed/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://linuxserver.io/discord){ .md-button .md-button--stretch }

</div>

---

## Deployment

```shell
sb install sandbox-speedtest
```

## Usage

Visit <https://speedtest.iYOUR_DOMAIN_NAMEi>.

## Basics

To use a custom subdomain, add a custom value for `speedtest_web_subdomain` in the `/srv/git/saltbox/inventories/host_vars/localhost.yml` file. More info can be found [here](../../saltbox/inventory/index.md).

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    speedtest_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `speedtest_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `speedtest_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`speedtest_name`"

        ```yaml
        # Type: string
        speedtest_name: speedtest
        ```

=== "Web"

    ??? variable string "`speedtest_role_web_subdomain`"

        ```yaml
        # Type: string
        speedtest_role_web_subdomain: "{{ speedtest_name }}"
        ```

    ??? variable string "`speedtest_role_web_domain`"

        ```yaml
        # Type: string
        speedtest_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`speedtest_role_web_port`"

        ```yaml
        # Type: string
        speedtest_role_web_port: "80"
        ```

    ??? variable string "`speedtest_role_web_url`"

        ```yaml
        # Type: string
        speedtest_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='speedtest') + '.' + lookup('role_var', '_web_domain', role='speedtest')
                                 if (lookup('role_var', '_web_subdomain', role='speedtest') | length > 0)
                                 else lookup('role_var', '_web_domain', role='speedtest')) }}"
        ```

=== "DNS"

    ??? variable string "`speedtest_role_dns_record`"

        ```yaml
        # Type: string
        speedtest_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='speedtest') }}"
        ```

    ??? variable string "`speedtest_role_dns_zone`"

        ```yaml
        # Type: string
        speedtest_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='speedtest') }}"
        ```

    ??? variable bool "`speedtest_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_dns_proxy: false
        ```

=== "Traefik"

    ??? variable string "`speedtest_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        speedtest_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`speedtest_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        speedtest_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`speedtest_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        speedtest_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`speedtest_role_traefik_certresolver`"

        ```yaml
        # Type: string
        speedtest_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`speedtest_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_traefik_enabled: true
        ```

    ??? variable bool "`speedtest_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_traefik_api_enabled: false
        ```

    ??? variable string "`speedtest_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        speedtest_role_traefik_api_endpoint: ""
        ```

=== "Theme"

    ??? variable bool "`speedtest_role_themepark_enabled`"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        speedtest_role_themepark_enabled: false
        ```

    ??? variable string "`speedtest_role_themepark_theme`"

        ```yaml
        # Type: string
        speedtest_role_themepark_theme: "{{ global_themepark_theme }}"
        ```

    ??? variable string "`speedtest_role_themepark_domain`"

        ```yaml
        # Type: string
        speedtest_role_themepark_domain: "{{ global_themepark_domain }}"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`speedtest_role_docker_container`"

        ```yaml
        # Type: string
        speedtest_role_docker_container: "{{ speedtest_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`speedtest_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_docker_image_pull: true
        ```

    ??? variable string "`speedtest_role_docker_image_repo`"

        ```yaml
        # Type: string
        speedtest_role_docker_image_repo: "lscr.io/linuxserver/librespeed"
        ```

    ??? variable string "`speedtest_role_docker_image_tag`"

        ```yaml
        # Type: string
        speedtest_role_docker_image_tag: "latest"
        ```

    ??? variable string "`speedtest_role_docker_image`"

        ```yaml
        # Type: string
        speedtest_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='speedtest') }}:{{ lookup('role_var', '_docker_image_tag', role='speedtest') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`speedtest_role_docker_envs_default`"

        ```yaml
        # Type: dict
        speedtest_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          PASSWORD: "{{ user.pass }}"
          DB_TYPE: "sqlite"
          DOCKER_MODS: "{{ 'ghcr.io/themepark-dev/theme.park:librespeed' if lookup('role_var', '_themepark_enabled', role='speedtest') else omit }}"
          TP_DOMAIN: "{{ lookup('role_var', '_themepark_domain', role='speedtest') }}"
          TP_THEME: "{{ lookup('role_var', '_themepark_theme', role='speedtest') }}"
        ```

    ??? variable dict "`speedtest_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        speedtest_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`speedtest_role_docker_volumes_default`"

        ```yaml
        # Type: list
        speedtest_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='speedtest') }}:/config"
        ```

    ??? variable list "`speedtest_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        speedtest_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`speedtest_role_docker_hostname`"

        ```yaml
        # Type: string
        speedtest_role_docker_hostname: "{{ speedtest_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`speedtest_role_docker_networks_alias`"

        ```yaml
        # Type: string
        speedtest_role_docker_networks_alias: "{{ speedtest_name }}"
        ```

    ??? variable list "`speedtest_role_docker_networks_default`"

        ```yaml
        # Type: list
        speedtest_role_docker_networks_default: []
        ```

    ??? variable list "`speedtest_role_docker_networks_custom`"

        ```yaml
        # Type: list
        speedtest_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`speedtest_role_docker_restart_policy`"

        ```yaml
        # Type: string
        speedtest_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`speedtest_role_docker_state`"

        ```yaml
        # Type: string
        speedtest_role_docker_state: started
        ```

    <h5>Force Kill</h5>

    ??? variable bool "`speedtest_role_docker_force_kill`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_docker_force_kill: true
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`speedtest_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        speedtest_role_docker_blkio_weight:
        ```

    ??? variable int "`speedtest_role_docker_cpu_period`"

        ```yaml
        # Type: int
        speedtest_role_docker_cpu_period:
        ```

    ??? variable int "`speedtest_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        speedtest_role_docker_cpu_quota:
        ```

    ??? variable int "`speedtest_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        speedtest_role_docker_cpu_shares:
        ```

    ??? variable string "`speedtest_role_docker_cpus`"

        ```yaml
        # Type: string
        speedtest_role_docker_cpus:
        ```

    ??? variable string "`speedtest_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        speedtest_role_docker_cpuset_cpus:
        ```

    ??? variable string "`speedtest_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        speedtest_role_docker_cpuset_mems:
        ```

    ??? variable string "`speedtest_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        speedtest_role_docker_kernel_memory:
        ```

    ??? variable string "`speedtest_role_docker_memory`"

        ```yaml
        # Type: string
        speedtest_role_docker_memory:
        ```

    ??? variable string "`speedtest_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        speedtest_role_docker_memory_reservation:
        ```

    ??? variable string "`speedtest_role_docker_memory_swap`"

        ```yaml
        # Type: string
        speedtest_role_docker_memory_swap:
        ```

    ??? variable int "`speedtest_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        speedtest_role_docker_memory_swappiness:
        ```

    ??? variable string "`speedtest_role_docker_shm_size`"

        ```yaml
        # Type: string
        speedtest_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`speedtest_role_docker_cap_drop`"

        ```yaml
        # Type: list
        speedtest_role_docker_cap_drop:
        ```

    ??? variable string "`speedtest_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        speedtest_role_docker_cgroupns_mode:
        ```

    ??? variable list "`speedtest_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        speedtest_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`speedtest_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        speedtest_role_docker_device_read_bps:
        ```

    ??? variable list "`speedtest_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        speedtest_role_docker_device_read_iops:
        ```

    ??? variable list "`speedtest_role_docker_device_requests`"

        ```yaml
        # Type: list
        speedtest_role_docker_device_requests:
        ```

    ??? variable list "`speedtest_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        speedtest_role_docker_device_write_bps:
        ```

    ??? variable list "`speedtest_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        speedtest_role_docker_device_write_iops:
        ```

    ??? variable list "`speedtest_role_docker_devices`"

        ```yaml
        # Type: list
        speedtest_role_docker_devices:
        ```

    ??? variable string "`speedtest_role_docker_devices_default`"

        ```yaml
        # Type: string
        speedtest_role_docker_devices_default:
        ```

    ??? variable list "`speedtest_role_docker_groups`"

        ```yaml
        # Type: list
        speedtest_role_docker_groups:
        ```

    ??? variable bool "`speedtest_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_docker_privileged:
        ```

    ??? variable list "`speedtest_role_docker_security_opts`"

        ```yaml
        # Type: list
        speedtest_role_docker_security_opts:
        ```

    ??? variable string "`speedtest_role_docker_user`"

        ```yaml
        # Type: string
        speedtest_role_docker_user:
        ```

    ??? variable string "`speedtest_role_docker_userns_mode`"

        ```yaml
        # Type: string
        speedtest_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`speedtest_role_docker_dns_opts`"

        ```yaml
        # Type: list
        speedtest_role_docker_dns_opts:
        ```

    ??? variable list "`speedtest_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        speedtest_role_docker_dns_search_domains:
        ```

    ??? variable list "`speedtest_role_docker_dns_servers`"

        ```yaml
        # Type: list
        speedtest_role_docker_dns_servers:
        ```

    ??? variable string "`speedtest_role_docker_domainname`"

        ```yaml
        # Type: string
        speedtest_role_docker_domainname:
        ```

    ??? variable list "`speedtest_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        speedtest_role_docker_exposed_ports:
        ```

    ??? variable dict "`speedtest_role_docker_hosts`"

        ```yaml
        # Type: dict
        speedtest_role_docker_hosts:
        ```

    ??? variable bool "`speedtest_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_docker_hosts_use_common:
        ```

    ??? variable string "`speedtest_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        speedtest_role_docker_ipc_mode:
        ```

    ??? variable list "`speedtest_role_docker_links`"

        ```yaml
        # Type: list
        speedtest_role_docker_links:
        ```

    ??? variable string "`speedtest_role_docker_network_mode`"

        ```yaml
        # Type: string
        speedtest_role_docker_network_mode:
        ```

    ??? variable string "`speedtest_role_docker_pid_mode`"

        ```yaml
        # Type: string
        speedtest_role_docker_pid_mode:
        ```

    ??? variable list "`speedtest_role_docker_ports`"

        ```yaml
        # Type: list
        speedtest_role_docker_ports:
        ```

    ??? variable string "`speedtest_role_docker_uts`"

        ```yaml
        # Type: string
        speedtest_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`speedtest_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_docker_keep_volumes:
        ```

    ??? variable list "`speedtest_role_docker_mounts`"

        ```yaml
        # Type: list
        speedtest_role_docker_mounts:
        ```

    ??? variable dict "`speedtest_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        speedtest_role_docker_storage_opts:
        ```

    ??? variable list "`speedtest_role_docker_tmpfs`"

        ```yaml
        # Type: list
        speedtest_role_docker_tmpfs:
        ```

    ??? variable string "`speedtest_role_docker_volume_driver`"

        ```yaml
        # Type: string
        speedtest_role_docker_volume_driver:
        ```

    ??? variable list "`speedtest_role_docker_volumes_from`"

        ```yaml
        # Type: list
        speedtest_role_docker_volumes_from:
        ```

    ??? variable bool "`speedtest_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_docker_volumes_global:
        ```

    ??? variable string "`speedtest_role_docker_working_dir`"

        ```yaml
        # Type: string
        speedtest_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`speedtest_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_docker_auto_remove:
        ```

    ??? variable bool "`speedtest_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_docker_cleanup:
        ```

    ??? variable dict "`speedtest_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        speedtest_role_docker_healthcheck:
        ```

    ??? variable int "`speedtest_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        speedtest_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`speedtest_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_docker_init:
        ```

    ??? variable string "`speedtest_role_docker_kill_signal`"

        ```yaml
        # Type: string
        speedtest_role_docker_kill_signal:
        ```

    ??? variable string "`speedtest_role_docker_log_driver`"

        ```yaml
        # Type: string
        speedtest_role_docker_log_driver:
        ```

    ??? variable dict "`speedtest_role_docker_log_options`"

        ```yaml
        # Type: dict
        speedtest_role_docker_log_options:
        ```

    ??? variable bool "`speedtest_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_docker_oom_killer:
        ```

    ??? variable int "`speedtest_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        speedtest_role_docker_oom_score_adj:
        ```

    ??? variable bool "`speedtest_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_docker_output_logs:
        ```

    ??? variable bool "`speedtest_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_docker_paused:
        ```

    ??? variable bool "`speedtest_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_docker_recreate:
        ```

    ??? variable int "`speedtest_role_docker_restart_retries`"

        ```yaml
        # Type: int
        speedtest_role_docker_restart_retries:
        ```

    ??? variable int "`speedtest_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        speedtest_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`speedtest_role_docker_capabilities`"

        ```yaml
        # Type: list
        speedtest_role_docker_capabilities:
        ```

    ??? variable string "`speedtest_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        speedtest_role_docker_cgroup_parent:
        ```

    ??? variable list "`speedtest_role_docker_commands`"

        ```yaml
        # Type: list
        speedtest_role_docker_commands:
        ```

    ??? variable int "`speedtest_role_docker_create_timeout`"

        ```yaml
        # Type: int
        speedtest_role_docker_create_timeout:
        ```

    ??? variable string "`speedtest_role_docker_entrypoint`"

        ```yaml
        # Type: string
        speedtest_role_docker_entrypoint:
        ```

    ??? variable string "`speedtest_role_docker_env_file`"

        ```yaml
        # Type: string
        speedtest_role_docker_env_file:
        ```

    ??? variable dict "`speedtest_role_docker_labels`"

        ```yaml
        # Type: dict
        speedtest_role_docker_labels:
        ```

    ??? variable bool "`speedtest_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_docker_labels_use_common:
        ```

    ??? variable bool "`speedtest_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_docker_read_only:
        ```

    ??? variable string "`speedtest_role_docker_runtime`"

        ```yaml
        # Type: string
        speedtest_role_docker_runtime:
        ```

    ??? variable list "`speedtest_role_docker_sysctls`"

        ```yaml
        # Type: list
        speedtest_role_docker_sysctls:
        ```

    ??? variable list "`speedtest_role_docker_ulimits`"

        ```yaml
        # Type: list
        speedtest_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`speedtest_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        speedtest_role_autoheal_enabled: true
        ```

    ??? variable string "`speedtest_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        speedtest_role_depends_on: ""
        ```

    ??? variable string "`speedtest_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        speedtest_role_depends_on_delay: "0"
        ```

    ??? variable string "`speedtest_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        speedtest_role_depends_on_healthchecks:
        ```

    ??? variable bool "`speedtest_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        speedtest_role_diun_enabled: true
        ```

    ??? variable bool "`speedtest_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        speedtest_role_dns_enabled: true
        ```

    ??? variable bool "`speedtest_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        speedtest_role_docker_controller: true
        ```

    ??? variable string "`speedtest_role_docker_image_repo`"

        ```yaml
        # Type: string
        speedtest_role_docker_image_repo:
        ```

    ??? variable string "`speedtest_role_docker_image_tag`"

        ```yaml
        # Type: string
        speedtest_role_docker_image_tag:
        ```

    ??? variable bool "`speedtest_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_docker_volumes_download:
        ```

    ??? variable string "`speedtest_role_paths_location`"

        ```yaml
        # Type: string
        speedtest_role_paths_location:
        ```

    ??? variable string "`speedtest_role_themepark_addons`"

        ```yaml
        # Type: string
        speedtest_role_themepark_addons:
        ```

    ??? variable string "`speedtest_role_themepark_app`"

        ```yaml
        # Type: string
        speedtest_role_themepark_app:
        ```

    ??? variable string "`speedtest_role_themepark_domain`"

        ```yaml
        # Type: string
        speedtest_role_themepark_domain:
        ```

    ??? variable bool "`speedtest_role_themepark_enabled`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_themepark_enabled:
        ```

    ??? variable string "`speedtest_role_themepark_theme`"

        ```yaml
        # Type: string
        speedtest_role_themepark_theme:
        ```

    ??? variable dict "`speedtest_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        speedtest_role_traefik_api_endpoint:
        ```

    ??? variable string "`speedtest_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        speedtest_role_traefik_api_middleware:
        ```

    ??? variable string "`speedtest_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        speedtest_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`speedtest_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        speedtest_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`speedtest_role_traefik_certresolver`"

        ```yaml
        # Type: string
        speedtest_role_traefik_certresolver:
        ```

    ??? variable bool "`speedtest_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        speedtest_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`speedtest_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        speedtest_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`speedtest_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        speedtest_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`speedtest_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        speedtest_role_traefik_middleware_http:
        ```

    ??? variable bool "`speedtest_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`speedtest_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`speedtest_role_traefik_priority`"

        ```yaml
        # Type: string
        speedtest_role_traefik_priority:
        ```

    ??? variable bool "`speedtest_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        speedtest_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`speedtest_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        speedtest_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`speedtest_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        speedtest_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`speedtest_role_web_domain`"

        ```yaml
        # Type: string
        speedtest_role_web_domain:
        ```

    ??? variable list "`speedtest_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        speedtest_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            speedtest_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "speedtest2.{{ user.domain }}"
              - "speedtest.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`speedtest_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        speedtest_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            speedtest_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'speedtest2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`speedtest_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        speedtest_role_web_http_port:
        ```

    ??? variable string "`speedtest_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        speedtest_role_web_http_scheme:
        ```

    ??? variable dict "`speedtest_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        speedtest_role_web_http_serverstransport:
        ```

    ??? variable string "`speedtest_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        speedtest_role_web_scheme:
        ```

    ??? variable dict "`speedtest_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        speedtest_role_web_serverstransport:
        ```

    ??? variable string "`speedtest_role_web_subdomain`"

        ```yaml
        # Type: string
        speedtest_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
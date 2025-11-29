---
icon: material/docker
hide:
  - tags
tags:
  - gaps
  - media
  - plex
---

# Gaps

## Overview

[Gaps](https://github.com/JasonHHouse/gaps) searches through your Plex Server for all movies, then queries for known movies in the same collection. If those movies don't exist in your library, Gaps will recommend getting those movies, legally of course.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will NOT have to log into the app itself, as basic Auth is disabled by default.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/JasonHHouse/gaps){: .header-icons } | [:octicons-link-16: Docs](https://github.com/JasonHHouse/gaps#-usage-){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/JasonHHouse/gaps){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/housewrecker/gaps){: .header-icons }|

### 1. Installation

```shell
sb install sandbox-gaps
```

### 2. URL

- To access gaps, visit <https://gaps.iYOUR_DOMAIN_NAMEi>

### 3. Setup

- All you need to get started is a [Plex Auth Token](../../reference/plex_auth_token.md?h=plex+token#saltbox-role), and a TMDB api key.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    gaps_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `gaps_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `gaps_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`gaps_name`"

        ```yaml
        # Type: string
        gaps_name: gaps
        ```

=== "Paths"

    ??? variable string "`gaps_role_paths_folder`"

        ```yaml
        # Type: string
        gaps_role_paths_folder: "{{ gaps_name }}"
        ```

    ??? variable string "`gaps_role_paths_location`"

        ```yaml
        # Type: string
        gaps_role_paths_location: "{{ server_appdata_path }}/{{ gaps_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`gaps_role_web_subdomain`"

        ```yaml
        # Type: string
        gaps_role_web_subdomain: "{{ gaps_name }}"
        ```

    ??? variable string "`gaps_role_web_domain`"

        ```yaml
        # Type: string
        gaps_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`gaps_role_web_port`"

        ```yaml
        # Type: string
        gaps_role_web_port: "8484"
        ```

    ??? variable string "`gaps_role_web_url`"

        ```yaml
        # Type: string
        gaps_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='gaps') + '.' + lookup('role_var', '_web_domain', role='gaps')
                            if (lookup('role_var', '_web_subdomain', role='gaps') | length > 0)
                            else lookup('role_var', '_web_domain', role='gaps')) }}"
        ```

=== "DNS"

    ??? variable string "`gaps_role_dns_record`"

        ```yaml
        # Type: string
        gaps_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='gaps') }}"
        ```

    ??? variable string "`gaps_role_dns_zone`"

        ```yaml
        # Type: string
        gaps_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='gaps') }}"
        ```

    ??? variable bool "`gaps_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`gaps_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        gaps_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`gaps_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        gaps_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`gaps_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        gaps_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`gaps_role_traefik_certresolver`"

        ```yaml
        # Type: string
        gaps_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`gaps_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_traefik_enabled: true
        ```

    ??? variable bool "`gaps_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_traefik_api_enabled: false
        ```

    ??? variable string "`gaps_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        gaps_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`gaps_role_docker_container`"

        ```yaml
        # Type: string
        gaps_role_docker_container: "{{ gaps_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`gaps_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_docker_image_pull: true
        ```

    ??? variable string "`gaps_role_docker_image_repo`"

        ```yaml
        # Type: string
        gaps_role_docker_image_repo: "housewrecker/gaps"
        ```

    ??? variable string "`gaps_role_docker_image_tag`"

        ```yaml
        # Type: string
        gaps_role_docker_image_tag: "latest"
        ```

    ??? variable string "`gaps_role_docker_image`"

        ```yaml
        # Type: string
        gaps_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='gaps') }}:{{ lookup('role_var', '_docker_image_tag', role='gaps') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`gaps_role_docker_envs_default`"

        ```yaml
        # Type: dict
        gaps_role_docker_envs_default:
          TZ: "{{ tz }}"
          ENABLE_LOGIN: "false"
          ENABLE_SSL: "false"
        ```

    ??? variable dict "`gaps_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        gaps_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`gaps_role_docker_volumes_default`"

        ```yaml
        # Type: list
        gaps_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='gaps') }}:/usr/data"
        ```

    ??? variable list "`gaps_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        gaps_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`gaps_role_docker_hostname`"

        ```yaml
        # Type: string
        gaps_role_docker_hostname: "{{ gaps_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`gaps_role_docker_networks_alias`"

        ```yaml
        # Type: string
        gaps_role_docker_networks_alias: "{{ gaps_name }}"
        ```

    ??? variable list "`gaps_role_docker_networks_default`"

        ```yaml
        # Type: list
        gaps_role_docker_networks_default: []
        ```

    ??? variable list "`gaps_role_docker_networks_custom`"

        ```yaml
        # Type: list
        gaps_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`gaps_role_docker_restart_policy`"

        ```yaml
        # Type: string
        gaps_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`gaps_role_docker_state`"

        ```yaml
        # Type: string
        gaps_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`gaps_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        gaps_role_docker_blkio_weight:
        ```

    ??? variable int "`gaps_role_docker_cpu_period`"

        ```yaml
        # Type: int
        gaps_role_docker_cpu_period:
        ```

    ??? variable int "`gaps_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        gaps_role_docker_cpu_quota:
        ```

    ??? variable int "`gaps_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        gaps_role_docker_cpu_shares:
        ```

    ??? variable string "`gaps_role_docker_cpus`"

        ```yaml
        # Type: string
        gaps_role_docker_cpus:
        ```

    ??? variable string "`gaps_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        gaps_role_docker_cpuset_cpus:
        ```

    ??? variable string "`gaps_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        gaps_role_docker_cpuset_mems:
        ```

    ??? variable string "`gaps_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        gaps_role_docker_kernel_memory:
        ```

    ??? variable string "`gaps_role_docker_memory`"

        ```yaml
        # Type: string
        gaps_role_docker_memory:
        ```

    ??? variable string "`gaps_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        gaps_role_docker_memory_reservation:
        ```

    ??? variable string "`gaps_role_docker_memory_swap`"

        ```yaml
        # Type: string
        gaps_role_docker_memory_swap:
        ```

    ??? variable int "`gaps_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        gaps_role_docker_memory_swappiness:
        ```

    ??? variable string "`gaps_role_docker_shm_size`"

        ```yaml
        # Type: string
        gaps_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`gaps_role_docker_cap_drop`"

        ```yaml
        # Type: list
        gaps_role_docker_cap_drop:
        ```

    ??? variable string "`gaps_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        gaps_role_docker_cgroupns_mode:
        ```

    ??? variable list "`gaps_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        gaps_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`gaps_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        gaps_role_docker_device_read_bps:
        ```

    ??? variable list "`gaps_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        gaps_role_docker_device_read_iops:
        ```

    ??? variable list "`gaps_role_docker_device_requests`"

        ```yaml
        # Type: list
        gaps_role_docker_device_requests:
        ```

    ??? variable list "`gaps_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        gaps_role_docker_device_write_bps:
        ```

    ??? variable list "`gaps_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        gaps_role_docker_device_write_iops:
        ```

    ??? variable list "`gaps_role_docker_devices`"

        ```yaml
        # Type: list
        gaps_role_docker_devices:
        ```

    ??? variable string "`gaps_role_docker_devices_default`"

        ```yaml
        # Type: string
        gaps_role_docker_devices_default:
        ```

    ??? variable list "`gaps_role_docker_groups`"

        ```yaml
        # Type: list
        gaps_role_docker_groups:
        ```

    ??? variable bool "`gaps_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_docker_privileged:
        ```

    ??? variable list "`gaps_role_docker_security_opts`"

        ```yaml
        # Type: list
        gaps_role_docker_security_opts:
        ```

    ??? variable string "`gaps_role_docker_user`"

        ```yaml
        # Type: string
        gaps_role_docker_user:
        ```

    ??? variable string "`gaps_role_docker_userns_mode`"

        ```yaml
        # Type: string
        gaps_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`gaps_role_docker_dns_opts`"

        ```yaml
        # Type: list
        gaps_role_docker_dns_opts:
        ```

    ??? variable list "`gaps_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        gaps_role_docker_dns_search_domains:
        ```

    ??? variable list "`gaps_role_docker_dns_servers`"

        ```yaml
        # Type: list
        gaps_role_docker_dns_servers:
        ```

    ??? variable string "`gaps_role_docker_domainname`"

        ```yaml
        # Type: string
        gaps_role_docker_domainname:
        ```

    ??? variable list "`gaps_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        gaps_role_docker_exposed_ports:
        ```

    ??? variable dict "`gaps_role_docker_hosts`"

        ```yaml
        # Type: dict
        gaps_role_docker_hosts:
        ```

    ??? variable bool "`gaps_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_docker_hosts_use_common:
        ```

    ??? variable string "`gaps_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        gaps_role_docker_ipc_mode:
        ```

    ??? variable list "`gaps_role_docker_links`"

        ```yaml
        # Type: list
        gaps_role_docker_links:
        ```

    ??? variable string "`gaps_role_docker_network_mode`"

        ```yaml
        # Type: string
        gaps_role_docker_network_mode:
        ```

    ??? variable string "`gaps_role_docker_pid_mode`"

        ```yaml
        # Type: string
        gaps_role_docker_pid_mode:
        ```

    ??? variable list "`gaps_role_docker_ports`"

        ```yaml
        # Type: list
        gaps_role_docker_ports:
        ```

    ??? variable string "`gaps_role_docker_uts`"

        ```yaml
        # Type: string
        gaps_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`gaps_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_docker_keep_volumes:
        ```

    ??? variable list "`gaps_role_docker_mounts`"

        ```yaml
        # Type: list
        gaps_role_docker_mounts:
        ```

    ??? variable dict "`gaps_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        gaps_role_docker_storage_opts:
        ```

    ??? variable list "`gaps_role_docker_tmpfs`"

        ```yaml
        # Type: list
        gaps_role_docker_tmpfs:
        ```

    ??? variable string "`gaps_role_docker_volume_driver`"

        ```yaml
        # Type: string
        gaps_role_docker_volume_driver:
        ```

    ??? variable list "`gaps_role_docker_volumes_from`"

        ```yaml
        # Type: list
        gaps_role_docker_volumes_from:
        ```

    ??? variable bool "`gaps_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_docker_volumes_global:
        ```

    ??? variable string "`gaps_role_docker_working_dir`"

        ```yaml
        # Type: string
        gaps_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`gaps_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_docker_auto_remove:
        ```

    ??? variable bool "`gaps_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_docker_cleanup:
        ```

    ??? variable string "`gaps_role_docker_force_kill`"

        ```yaml
        # Type: string
        gaps_role_docker_force_kill:
        ```

    ??? variable dict "`gaps_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        gaps_role_docker_healthcheck:
        ```

    ??? variable int "`gaps_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        gaps_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`gaps_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_docker_init:
        ```

    ??? variable string "`gaps_role_docker_kill_signal`"

        ```yaml
        # Type: string
        gaps_role_docker_kill_signal:
        ```

    ??? variable string "`gaps_role_docker_log_driver`"

        ```yaml
        # Type: string
        gaps_role_docker_log_driver:
        ```

    ??? variable dict "`gaps_role_docker_log_options`"

        ```yaml
        # Type: dict
        gaps_role_docker_log_options:
        ```

    ??? variable bool "`gaps_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_docker_oom_killer:
        ```

    ??? variable int "`gaps_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        gaps_role_docker_oom_score_adj:
        ```

    ??? variable bool "`gaps_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_docker_output_logs:
        ```

    ??? variable bool "`gaps_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_docker_paused:
        ```

    ??? variable bool "`gaps_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_docker_recreate:
        ```

    ??? variable int "`gaps_role_docker_restart_retries`"

        ```yaml
        # Type: int
        gaps_role_docker_restart_retries:
        ```

    ??? variable int "`gaps_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        gaps_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`gaps_role_docker_capabilities`"

        ```yaml
        # Type: list
        gaps_role_docker_capabilities:
        ```

    ??? variable string "`gaps_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        gaps_role_docker_cgroup_parent:
        ```

    ??? variable list "`gaps_role_docker_commands`"

        ```yaml
        # Type: list
        gaps_role_docker_commands:
        ```

    ??? variable int "`gaps_role_docker_create_timeout`"

        ```yaml
        # Type: int
        gaps_role_docker_create_timeout:
        ```

    ??? variable string "`gaps_role_docker_entrypoint`"

        ```yaml
        # Type: string
        gaps_role_docker_entrypoint:
        ```

    ??? variable string "`gaps_role_docker_env_file`"

        ```yaml
        # Type: string
        gaps_role_docker_env_file:
        ```

    ??? variable dict "`gaps_role_docker_labels`"

        ```yaml
        # Type: dict
        gaps_role_docker_labels:
        ```

    ??? variable bool "`gaps_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_docker_labels_use_common:
        ```

    ??? variable bool "`gaps_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_docker_read_only:
        ```

    ??? variable string "`gaps_role_docker_runtime`"

        ```yaml
        # Type: string
        gaps_role_docker_runtime:
        ```

    ??? variable list "`gaps_role_docker_sysctls`"

        ```yaml
        # Type: list
        gaps_role_docker_sysctls:
        ```

    ??? variable list "`gaps_role_docker_ulimits`"

        ```yaml
        # Type: list
        gaps_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`gaps_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        gaps_role_autoheal_enabled: true
        ```

    ??? variable string "`gaps_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        gaps_role_depends_on: ""
        ```

    ??? variable string "`gaps_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        gaps_role_depends_on_delay: "0"
        ```

    ??? variable string "`gaps_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        gaps_role_depends_on_healthchecks:
        ```

    ??? variable bool "`gaps_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        gaps_role_diun_enabled: true
        ```

    ??? variable bool "`gaps_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        gaps_role_dns_enabled: true
        ```

    ??? variable bool "`gaps_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        gaps_role_docker_controller: true
        ```

    ??? variable string "`gaps_role_docker_image_repo`"

        ```yaml
        # Type: string
        gaps_role_docker_image_repo:
        ```

    ??? variable string "`gaps_role_docker_image_tag`"

        ```yaml
        # Type: string
        gaps_role_docker_image_tag:
        ```

    ??? variable bool "`gaps_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_docker_volumes_download:
        ```

    ??? variable string "`gaps_role_paths_location`"

        ```yaml
        # Type: string
        gaps_role_paths_location:
        ```

    ??? variable string "`gaps_role_themepark_addons`"

        ```yaml
        # Type: string
        gaps_role_themepark_addons:
        ```

    ??? variable string "`gaps_role_themepark_app`"

        ```yaml
        # Type: string
        gaps_role_themepark_app:
        ```

    ??? variable string "`gaps_role_themepark_theme`"

        ```yaml
        # Type: string
        gaps_role_themepark_theme:
        ```

    ??? variable dict/omit "`gaps_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        gaps_role_traefik_api_endpoint:
        ```

    ??? variable string "`gaps_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        gaps_role_traefik_api_middleware:
        ```

    ??? variable string "`gaps_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        gaps_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`gaps_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        gaps_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`gaps_role_traefik_certresolver`"

        ```yaml
        # Type: string
        gaps_role_traefik_certresolver:
        ```

    ??? variable bool "`gaps_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        gaps_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`gaps_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        gaps_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`gaps_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        gaps_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`gaps_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        gaps_role_traefik_middleware_http:
        ```

    ??? variable bool "`gaps_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`gaps_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`gaps_role_traefik_priority`"

        ```yaml
        # Type: string
        gaps_role_traefik_priority:
        ```

    ??? variable bool "`gaps_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        gaps_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`gaps_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        gaps_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`gaps_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        gaps_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`gaps_role_web_domain`"

        ```yaml
        # Type: string
        gaps_role_web_domain:
        ```

    ??? variable list "`gaps_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        gaps_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            gaps_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "gaps2.{{ user.domain }}"
              - "gaps.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`gaps_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        gaps_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            gaps_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'gaps2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`gaps_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        gaps_role_web_http_port:
        ```

    ??? variable string "`gaps_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        gaps_role_web_http_scheme:
        ```

    ??? variable dict/omit "`gaps_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        gaps_role_web_http_serverstransport:
        ```

    ??? variable string "`gaps_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        gaps_role_web_scheme:
        ```

    ??? variable dict/omit "`gaps_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        gaps_role_web_serverstransport:
        ```

    ??? variable string "`gaps_role_web_subdomain`"

        ```yaml
        # Type: string
        gaps_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
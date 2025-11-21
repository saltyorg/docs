---
icon: material/docker
hide:
  - tags
tags:
  - nzbthrottle
  - usenet
  - bandwidth
  - automation
---

# NZBThrottle

## Overview

NZBThrottle is a utility that automatically throttles Usenet download speeds based on custom schedules and conditions. It can dynamically adjust your download client's speed limits to ensure bandwidth is available when you need it most, such as during work hours or peak usage times.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/daghaian/nzbthrottle){: .header-icons } | [:octicons-link-16: Docs](https://github.com/daghaian/nzbthrottle#readme){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/daghaian/nzbthrottle){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/daghaian/nzbthrottle){: .header-icons }|

### 1. Installation

``` shell

sb install nzbthrottle

```

### 2. Setup

NZBThrottle automatically throttles Usenet download speeds based on custom schedules. Configure your download clients (SABnzbd, NZBGet, etc.) and schedules in `/opt/nzbthrottle/config.json`, then restart with `docker restart nzbthrottle`.

Note: Configuration is file-based with no web interface.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    nzbthrottle_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `nzbthrottle_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `nzbthrottle_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`nzbthrottle_name`"

        ```yaml
        # Type: string
        nzbthrottle_name: nzbthrottle
        ```

=== "Paths"

    ??? variable string "`nzbthrottle_role_paths_folder`"

        ```yaml
        # Type: string
        nzbthrottle_role_paths_folder: "{{ nzbthrottle_name }}"
        ```

    ??? variable string "`nzbthrottle_role_paths_location`"

        ```yaml
        # Type: string
        nzbthrottle_role_paths_location: "{{ server_appdata_path }}/{{ nzbthrottle_role_paths_folder }}"
        ```

    ??? variable string "`nzbthrottle_role_paths_config_location`"

        ```yaml
        # Type: string
        nzbthrottle_role_paths_config_location: "{{ nzbthrottle_role_paths_location }}/config.json"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`nzbthrottle_role_docker_container`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_container: "{{ nzbthrottle_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`nzbthrottle_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_image_pull: true
        ```

    ??? variable string "`nzbthrottle_role_docker_image_repo`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_image_repo: "daghaian/nzbthrottle"
        ```

    ??? variable string "`nzbthrottle_role_docker_image_tag`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_image_tag: "latest"
        ```

    ??? variable string "`nzbthrottle_role_docker_image`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='nzbthrottle') }}:{{ lookup('role_var', '_docker_image_tag', role='nzbthrottle') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`nzbthrottle_role_docker_envs_default`"

        ```yaml
        # Type: dict
        nzbthrottle_role_docker_envs_default:
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`nzbthrottle_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        nzbthrottle_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`nzbthrottle_role_docker_volumes_default`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_volumes_default:
          - "{{ nzbthrottle_role_paths_config_location }}:/nzbthrottle/config.json:ro"
        ```

    ??? variable list "`nzbthrottle_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`nzbthrottle_role_docker_hostname`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_hostname: "{{ nzbthrottle_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`nzbthrottle_role_docker_networks_alias`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_networks_alias: "{{ nzbthrottle_name }}"
        ```

    ??? variable list "`nzbthrottle_role_docker_networks_default`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_networks_default: []
        ```

    ??? variable list "`nzbthrottle_role_docker_networks_custom`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`nzbthrottle_role_docker_restart_policy`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`nzbthrottle_role_docker_state`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    <h5>Resource Limits</h5>

    ??? variable int "`nzbthrottle_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        nzbthrottle_role_docker_blkio_weight:
        ```

    ??? variable int "`nzbthrottle_role_docker_cpu_period`"

        ```yaml
        # Type: int
        nzbthrottle_role_docker_cpu_period:
        ```

    ??? variable int "`nzbthrottle_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        nzbthrottle_role_docker_cpu_quota:
        ```

    ??? variable int "`nzbthrottle_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        nzbthrottle_role_docker_cpu_shares:
        ```

    ??? variable string "`nzbthrottle_role_docker_cpus`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_cpus:
        ```

    ??? variable string "`nzbthrottle_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_cpuset_cpus:
        ```

    ??? variable string "`nzbthrottle_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_cpuset_mems:
        ```

    ??? variable string "`nzbthrottle_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_kernel_memory:
        ```

    ??? variable string "`nzbthrottle_role_docker_memory`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_memory:
        ```

    ??? variable string "`nzbthrottle_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_memory_reservation:
        ```

    ??? variable string "`nzbthrottle_role_docker_memory_swap`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_memory_swap:
        ```

    ??? variable int "`nzbthrottle_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        nzbthrottle_role_docker_memory_swappiness:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`nzbthrottle_role_docker_cap_drop`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_cap_drop:
        ```

    ??? variable list "`nzbthrottle_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`nzbthrottle_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_device_read_bps:
        ```

    ??? variable list "`nzbthrottle_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_device_read_iops:
        ```

    ??? variable list "`nzbthrottle_role_docker_device_requests`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_device_requests:
        ```

    ??? variable list "`nzbthrottle_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_device_write_bps:
        ```

    ??? variable list "`nzbthrottle_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_device_write_iops:
        ```

    ??? variable list "`nzbthrottle_role_docker_devices`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_devices:
        ```

    ??? variable string "`nzbthrottle_role_docker_devices_default`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_devices_default:
        ```

    ??? variable bool "`nzbthrottle_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_privileged:
        ```

    ??? variable list "`nzbthrottle_role_docker_security_opts`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_security_opts:
        ```

    <h5>Networking</h5>

    ??? variable list "`nzbthrottle_role_docker_dns_opts`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_dns_opts:
        ```

    ??? variable list "`nzbthrottle_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_dns_search_domains:
        ```

    ??? variable list "`nzbthrottle_role_docker_dns_servers`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_dns_servers:
        ```

    ??? variable dict "`nzbthrottle_role_docker_hosts`"

        ```yaml
        # Type: dict
        nzbthrottle_role_docker_hosts:
        ```

    ??? variable string "`nzbthrottle_role_docker_hosts_use_common`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_hosts_use_common:
        ```

    ??? variable string "`nzbthrottle_role_docker_network_mode`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_network_mode:
        ```

    <h5>Storage</h5>

    ??? variable bool "`nzbthrottle_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_keep_volumes:
        ```

    ??? variable list "`nzbthrottle_role_docker_mounts`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_mounts:
        ```

    ??? variable string "`nzbthrottle_role_docker_volume_driver`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_volume_driver:
        ```

    ??? variable list "`nzbthrottle_role_docker_volumes_from`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_volumes_from:
        ```

    ??? variable string "`nzbthrottle_role_docker_volumes_global`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_volumes_global:
        ```

    ??? variable string "`nzbthrottle_role_docker_working_dir`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable dict "`nzbthrottle_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        nzbthrottle_role_docker_healthcheck:
        ```

    ??? variable bool "`nzbthrottle_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_init:
        ```

    ??? variable string "`nzbthrottle_role_docker_log_driver`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_log_driver:
        ```

    ??? variable dict "`nzbthrottle_role_docker_log_options`"

        ```yaml
        # Type: dict
        nzbthrottle_role_docker_log_options:
        ```

    ??? variable bool "`nzbthrottle_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_output_logs:
        ```

    <h5>Other Options</h5>

    ??? variable bool "`nzbthrottle_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_auto_remove:
        ```

    ??? variable list "`nzbthrottle_role_docker_capabilities`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_capabilities:
        ```

    ??? variable string "`nzbthrottle_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_cgroup_parent:
        ```

    ??? variable string "`nzbthrottle_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_cgroupns_mode:
        ```

    ??? variable bool "`nzbthrottle_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_cleanup:
        ```

    ??? variable list "`nzbthrottle_role_docker_commands`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_commands:
        ```

    ??? variable string "`nzbthrottle_role_docker_create_timeout`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_create_timeout:
        ```

    ??? variable string "`nzbthrottle_role_docker_domainname`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_domainname:
        ```

    ??? variable string "`nzbthrottle_role_docker_entrypoint`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_entrypoint:
        ```

    ??? variable string "`nzbthrottle_role_docker_env_file`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_env_file:
        ```

    ??? variable list "`nzbthrottle_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_exposed_ports:
        ```

    ??? variable string "`nzbthrottle_role_docker_force_kill`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_force_kill:
        ```

    ??? variable list "`nzbthrottle_role_docker_groups`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_groups:
        ```

    ??? variable int "`nzbthrottle_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        nzbthrottle_role_docker_healthy_wait_timeout:
        ```

    ??? variable string "`nzbthrottle_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_ipc_mode:
        ```

    ??? variable string "`nzbthrottle_role_docker_kill_signal`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_kill_signal:
        ```

    ??? variable dict "`nzbthrottle_role_docker_labels`"

        ```yaml
        # Type: dict
        nzbthrottle_role_docker_labels:
        ```

    ??? variable string "`nzbthrottle_role_docker_labels_use_common`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_labels_use_common:
        ```

    ??? variable list "`nzbthrottle_role_docker_links`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_links:
        ```

    ??? variable bool "`nzbthrottle_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_oom_killer:
        ```

    ??? variable int "`nzbthrottle_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        nzbthrottle_role_docker_oom_score_adj:
        ```

    ??? variable bool "`nzbthrottle_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_paused:
        ```

    ??? variable string "`nzbthrottle_role_docker_pid_mode`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_pid_mode:
        ```

    ??? variable list "`nzbthrottle_role_docker_ports`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_ports:
        ```

    ??? variable bool "`nzbthrottle_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_read_only:
        ```

    ??? variable bool "`nzbthrottle_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_recreate:
        ```

    ??? variable int "`nzbthrottle_role_docker_restart_retries`"

        ```yaml
        # Type: int
        nzbthrottle_role_docker_restart_retries:
        ```

    ??? variable string "`nzbthrottle_role_docker_runtime`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_runtime:
        ```

    ??? variable string "`nzbthrottle_role_docker_shm_size`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_shm_size:
        ```

    ??? variable int "`nzbthrottle_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        nzbthrottle_role_docker_stop_timeout:
        ```

    ??? variable dict "`nzbthrottle_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        nzbthrottle_role_docker_storage_opts:
        ```

    ??? variable list "`nzbthrottle_role_docker_sysctls`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_sysctls:
        ```

    ??? variable list "`nzbthrottle_role_docker_tmpfs`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_tmpfs:
        ```

    ??? variable list "`nzbthrottle_role_docker_ulimits`"

        ```yaml
        # Type: list
        nzbthrottle_role_docker_ulimits:
        ```

    ??? variable string "`nzbthrottle_role_docker_user`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_user:
        ```

    ??? variable string "`nzbthrottle_role_docker_userns_mode`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_userns_mode:
        ```

    ??? variable string "`nzbthrottle_role_docker_uts`"

        ```yaml
        # Type: string
        nzbthrottle_role_docker_uts:
        ```

=== "Global Override Options"

    ??? variable bool "`nzbthrottle_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        nzbthrottle_role_autoheal_enabled: true
        ```

    ??? variable string "`nzbthrottle_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        nzbthrottle_role_depends_on: ""
        ```

    ??? variable string "`nzbthrottle_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        nzbthrottle_role_depends_on_delay: "0"
        ```

    ??? variable string "`nzbthrottle_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        nzbthrottle_role_depends_on_healthchecks:
        ```

    ??? variable bool "`nzbthrottle_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        nzbthrottle_role_diun_enabled: true
        ```

    ??? variable bool "`nzbthrottle_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        nzbthrottle_role_dns_enabled: true
        ```

    ??? variable bool "`nzbthrottle_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        nzbthrottle_role_docker_controller: true
        ```

    ??? variable bool "`nzbthrottle_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_docker_volumes_download:
        ```

    ??? variable bool "`nzbthrottle_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        nzbthrottle_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`nzbthrottle_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        nzbthrottle_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`nzbthrottle_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        nzbthrottle_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`nzbthrottle_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        nzbthrottle_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`nzbthrottle_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`nzbthrottle_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        nzbthrottle_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`nzbthrottle_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        nzbthrottle_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`nzbthrottle_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        nzbthrottle_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`nzbthrottle_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        nzbthrottle_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`nzbthrottle_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        nzbthrottle_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            nzbthrottle_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "nzbthrottle2.{{ user.domain }}"
              - "nzbthrottle.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`nzbthrottle_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        nzbthrottle_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            nzbthrottle_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'nzbthrottle2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`nzbthrottle_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        nzbthrottle_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
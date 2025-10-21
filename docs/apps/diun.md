---
hide:
  - tags
tags:
  - diun
---

# diun

## What is it?

[diun](https://crazymax.dev/diun/) Docker Image Update Notifier is a CLI application written in Go and delivered as a single executable (and a Docker image) to receive notifications when a Docker image is updated on a Docker registry.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://crazymax.dev/diun){: .header-icons } | [:octicons-link-16: Docs](https://crazymax.dev/diun/notif/discord){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/crazy-max/diun){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/crazymax/diun){: .header-icons }|

### 1. Installation

``` shell

sb install diun

```

### 2. Setup

- The config file for diun is located at `/opt/diun/diun.yml`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        diun_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `diun_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `diun_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`diun_name`"

        ```yaml
        # Type: string
        diun_name: diun
        ```

=== "Paths"

    ??? variable string "`diun_role_paths_folder`"

        ```yaml
        # Type: string
        diun_role_paths_folder: "{{ diun_name }}"
        ```

    ??? variable string "`diun_role_paths_location`"

        ```yaml
        # Type: string
        diun_role_paths_location: "{{ server_appdata_path }}/{{ diun_role_paths_folder }}"
        ```

=== "Docker"

    ##### Container

    ??? variable string "`diun_role_docker_container`"

        ```yaml
        # Type: string
        diun_role_docker_container: "{{ diun_name }}"
        ```

    ##### Image

    ??? variable bool "`diun_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_image_pull: true
        ```

    ??? variable string "`diun_role_docker_image_repo`"

        ```yaml
        # Type: string
        diun_role_docker_image_repo: "crazymax/diun"
        ```

    ??? variable string "`diun_role_docker_image_tag`"

        ```yaml
        # Type: string
        diun_role_docker_image_tag: "latest"
        ```

    ??? variable string "`diun_role_docker_image`"

        ```yaml
        # Type: string
        diun_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='diun') }}:{{ lookup('role_var', '_docker_image_tag', role='diun') }}"
        ```

    ##### Envs

    ??? variable dict "`diun_role_docker_envs_default`"

        ```yaml
        # Type: dict
        diun_role_docker_envs_default: 
          TZ: "{{ tz }}"
          LOG_LEVEL: "info"
          LOG_JSON: "false"
        ```

    ??? variable dict "`diun_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        diun_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`diun_role_docker_volumes_default`"

        ```yaml
        # Type: list
        diun_role_docker_volumes_default: 
          - "{{ diun_role_paths_location }}/data:/data"
          - "{{ diun_role_paths_location }}/diun.yml:/diun.yml:ro"
          - "/var/run/docker.sock:/var/run/docker.sock"
        ```

    ??? variable list "`diun_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        diun_role_docker_volumes_custom: []
        ```

    ##### Labels

    ??? variable dict "`diun_role_docker_labels_default`"

        ```yaml
        # Type: dict
        diun_role_docker_labels_default: 
          diun.enable: "true"
        ```

    ??? variable dict "`diun_role_docker_labels_custom`"

        ```yaml
        # Type: dict
        diun_role_docker_labels_custom: {}
        ```

    ##### Hostname

    ??? variable string "`diun_role_docker_hostname`"

        ```yaml
        # Type: string
        diun_role_docker_hostname: "{{ diun_name }}"
        ```

    ##### Networks

    ??? variable string "`diun_role_docker_networks_alias`"

        ```yaml
        # Type: string
        diun_role_docker_networks_alias: "{{ diun_name }}"
        ```

    ??? variable list "`diun_role_docker_networks_default`"

        ```yaml
        # Type: list
        diun_role_docker_networks_default: []
        ```

    ??? variable list "`diun_role_docker_networks_custom`"

        ```yaml
        # Type: list
        diun_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`diun_role_docker_restart_policy`"

        ```yaml
        # Type: string
        diun_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`diun_role_docker_state`"

        ```yaml
        # Type: string
        diun_role_docker_state: started
        ```

=== "Docker+"

    #### Additional Docker Options

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    ##### Resource Limits

    ??? variable int "`diun_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        diun_role_docker_blkio_weight:
        ```

    ??? variable int "`diun_role_docker_cpu_period`"

        ```yaml
        # Type: int
        diun_role_docker_cpu_period:
        ```

    ??? variable int "`diun_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        diun_role_docker_cpu_quota:
        ```

    ??? variable int "`diun_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        diun_role_docker_cpu_shares:
        ```

    ??? variable string "`diun_role_docker_cpus`"

        ```yaml
        # Type: string
        diun_role_docker_cpus:
        ```

    ??? variable string "`diun_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        diun_role_docker_cpuset_cpus:
        ```

    ??? variable string "`diun_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        diun_role_docker_cpuset_mems:
        ```

    ??? variable string "`diun_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        diun_role_docker_kernel_memory:
        ```

    ??? variable string "`diun_role_docker_memory`"

        ```yaml
        # Type: string
        diun_role_docker_memory:
        ```

    ??? variable string "`diun_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        diun_role_docker_memory_reservation:
        ```

    ??? variable string "`diun_role_docker_memory_swap`"

        ```yaml
        # Type: string
        diun_role_docker_memory_swap:
        ```

    ??? variable int "`diun_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        diun_role_docker_memory_swappiness:
        ```

    ##### Security & Devices

    ??? variable list "`diun_role_docker_cap_drop`"

        ```yaml
        # Type: list
        diun_role_docker_cap_drop:
        ```

    ??? variable list "`diun_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        diun_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`diun_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        diun_role_docker_device_read_bps:
        ```

    ??? variable list "`diun_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        diun_role_docker_device_read_iops:
        ```

    ??? variable list "`diun_role_docker_device_requests`"

        ```yaml
        # Type: list
        diun_role_docker_device_requests:
        ```

    ??? variable list "`diun_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        diun_role_docker_device_write_bps:
        ```

    ??? variable list "`diun_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        diun_role_docker_device_write_iops:
        ```

    ??? variable list "`diun_role_docker_devices`"

        ```yaml
        # Type: list
        diun_role_docker_devices:
        ```

    ??? variable string "`diun_role_docker_devices_default`"

        ```yaml
        # Type: string
        diun_role_docker_devices_default:
        ```

    ??? variable bool "`diun_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_privileged:
        ```

    ??? variable list "`diun_role_docker_security_opts`"

        ```yaml
        # Type: list
        diun_role_docker_security_opts:
        ```

    ##### Networking

    ??? variable list "`diun_role_docker_dns_opts`"

        ```yaml
        # Type: list
        diun_role_docker_dns_opts:
        ```

    ??? variable list "`diun_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        diun_role_docker_dns_search_domains:
        ```

    ??? variable list "`diun_role_docker_dns_servers`"

        ```yaml
        # Type: list
        diun_role_docker_dns_servers:
        ```

    ??? variable dict "`diun_role_docker_hosts`"

        ```yaml
        # Type: dict
        diun_role_docker_hosts:
        ```

    ??? variable string "`diun_role_docker_hosts_use_common`"

        ```yaml
        # Type: string
        diun_role_docker_hosts_use_common:
        ```

    ??? variable string "`diun_role_docker_network_mode`"

        ```yaml
        # Type: string
        diun_role_docker_network_mode:
        ```

    ##### Storage

    ??? variable bool "`diun_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_keep_volumes:
        ```

    ??? variable list "`diun_role_docker_mounts`"

        ```yaml
        # Type: list
        diun_role_docker_mounts:
        ```

    ??? variable string "`diun_role_docker_volume_driver`"

        ```yaml
        # Type: string
        diun_role_docker_volume_driver:
        ```

    ??? variable list "`diun_role_docker_volumes_from`"

        ```yaml
        # Type: list
        diun_role_docker_volumes_from:
        ```

    ??? variable string "`diun_role_docker_volumes_global`"

        ```yaml
        # Type: string
        diun_role_docker_volumes_global:
        ```

    ??? variable string "`diun_role_docker_working_dir`"

        ```yaml
        # Type: string
        diun_role_docker_working_dir:
        ```

    ##### Monitoring & Lifecycle

    ??? variable dict "`diun_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        diun_role_docker_healthcheck:
        ```

    ??? variable bool "`diun_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_init:
        ```

    ??? variable string "`diun_role_docker_log_driver`"

        ```yaml
        # Type: string
        diun_role_docker_log_driver:
        ```

    ??? variable dict "`diun_role_docker_log_options`"

        ```yaml
        # Type: dict
        diun_role_docker_log_options:
        ```

    ??? variable bool "`diun_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_output_logs:
        ```

    ##### Other Options

    ??? variable bool "`diun_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_auto_remove:
        ```

    ??? variable list "`diun_role_docker_capabilities`"

        ```yaml
        # Type: list
        diun_role_docker_capabilities:
        ```

    ??? variable string "`diun_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        diun_role_docker_cgroup_parent:
        ```

    ??? variable string "`diun_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        diun_role_docker_cgroupns_mode:
        ```

    ??? variable bool "`diun_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_cleanup:
        ```

    ??? variable list "`diun_role_docker_commands`"

        ```yaml
        # Type: list
        diun_role_docker_commands:
        ```

    ??? variable string "`diun_role_docker_create_timeout`"

        ```yaml
        # Type: string
        diun_role_docker_create_timeout:
        ```

    ??? variable string "`diun_role_docker_domainname`"

        ```yaml
        # Type: string
        diun_role_docker_domainname:
        ```

    ??? variable string "`diun_role_docker_entrypoint`"

        ```yaml
        # Type: string
        diun_role_docker_entrypoint:
        ```

    ??? variable string "`diun_role_docker_env_file`"

        ```yaml
        # Type: string
        diun_role_docker_env_file:
        ```

    ??? variable list "`diun_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        diun_role_docker_exposed_ports:
        ```

    ??? variable string "`diun_role_docker_force_kill`"

        ```yaml
        # Type: string
        diun_role_docker_force_kill:
        ```

    ??? variable list "`diun_role_docker_groups`"

        ```yaml
        # Type: list
        diun_role_docker_groups:
        ```

    ??? variable int "`diun_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        diun_role_docker_healthy_wait_timeout:
        ```

    ??? variable string "`diun_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        diun_role_docker_ipc_mode:
        ```

    ??? variable string "`diun_role_docker_kill_signal`"

        ```yaml
        # Type: string
        diun_role_docker_kill_signal:
        ```

    ??? variable string "`diun_role_docker_labels_use_common`"

        ```yaml
        # Type: string
        diun_role_docker_labels_use_common:
        ```

    ??? variable list "`diun_role_docker_links`"

        ```yaml
        # Type: list
        diun_role_docker_links:
        ```

    ??? variable bool "`diun_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_oom_killer:
        ```

    ??? variable int "`diun_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        diun_role_docker_oom_score_adj:
        ```

    ??? variable bool "`diun_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_paused:
        ```

    ??? variable string "`diun_role_docker_pid_mode`"

        ```yaml
        # Type: string
        diun_role_docker_pid_mode:
        ```

    ??? variable list "`diun_role_docker_ports`"

        ```yaml
        # Type: list
        diun_role_docker_ports:
        ```

    ??? variable bool "`diun_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_read_only:
        ```

    ??? variable bool "`diun_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        diun_role_docker_recreate:
        ```

    ??? variable int "`diun_role_docker_restart_retries`"

        ```yaml
        # Type: int
        diun_role_docker_restart_retries:
        ```

    ??? variable string "`diun_role_docker_runtime`"

        ```yaml
        # Type: string
        diun_role_docker_runtime:
        ```

    ??? variable string "`diun_role_docker_shm_size`"

        ```yaml
        # Type: string
        diun_role_docker_shm_size:
        ```

    ??? variable int "`diun_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        diun_role_docker_stop_timeout:
        ```

    ??? variable dict "`diun_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        diun_role_docker_storage_opts:
        ```

    ??? variable list "`diun_role_docker_sysctls`"

        ```yaml
        # Type: list
        diun_role_docker_sysctls:
        ```

    ??? variable list "`diun_role_docker_tmpfs`"

        ```yaml
        # Type: list
        diun_role_docker_tmpfs:
        ```

    ??? variable list "`diun_role_docker_ulimits`"

        ```yaml
        # Type: list
        diun_role_docker_ulimits:
        ```

    ??? variable string "`diun_role_docker_user`"

        ```yaml
        # Type: string
        diun_role_docker_user:
        ```

    ??? variable string "`diun_role_docker_userns_mode`"

        ```yaml
        # Type: string
        diun_role_docker_userns_mode:
        ```

    ??? variable string "`diun_role_docker_uts`"

        ```yaml
        # Type: string
        diun_role_docker_uts:
        ```

=== "Global Override Options"

    ??? variable bool "`diun_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        diun_role_autoheal_enabled: true
        ```

    ??? variable string "`diun_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        diun_role_depends_on: ""
        ```

    ??? variable string "`diun_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        diun_role_depends_on_delay: "0"
        ```

    ??? variable string "`diun_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        diun_role_depends_on_healthchecks:
        ```

    ??? variable bool "`diun_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        diun_role_diun_enabled: true
        ```

    ??? variable bool "`diun_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        diun_role_dns_enabled: true
        ```

    ??? variable bool "`diun_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        diun_role_docker_controller: true
        ```

    ??? variable bool "`diun_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        diun_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`diun_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        diun_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`diun_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        diun_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`diun_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        diun_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`diun_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        diun_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`diun_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        diun_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`diun_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        diun_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`diun_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        diun_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            diun_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "diun2.{{ user.domain }}"
              - "diun.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`diun_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        diun_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            diun_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'diun2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`diun_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        diun_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
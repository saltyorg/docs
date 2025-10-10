---
hide:
  - tags
tags:
  - nzbthrottle
  - usenet
  - bandwidth
  - automation
---

# NZBThrottle

## What is it?

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

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        nzbthrottle_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    nzbthrottle_name: nzbthrottle

    ```

??? example "Paths"

    ```yaml
    # Type: string
    nzbthrottle_role_paths_folder: "{{ nzbthrottle_name }}"

    # Type: string
    nzbthrottle_role_paths_location: "{{ server_appdata_path }}/{{ nzbthrottle_role_paths_folder }}"

    # Type: string
    nzbthrottle_role_paths_config_location: "{{ nzbthrottle_role_paths_location }}/config.json"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    nzbthrottle_role_docker_container: "{{ nzbthrottle_name }}"

    # Image
    # Type: bool (true/false)
    nzbthrottle_role_docker_image_pull: true

    # Type: string
    nzbthrottle_role_docker_image_repo: "daghaian/nzbthrottle"

    # Type: string
    nzbthrottle_role_docker_image_tag: "latest"

    # Type: string
    nzbthrottle_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='nzbthrottle') }}:{{ lookup('role_var', '_docker_image_tag', role='nzbthrottle') }}"

    # Envs
    # Type: dict
    nzbthrottle_role_docker_envs_default: 
      TZ: "{{ tz }}"

    # Type: dict
    nzbthrottle_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    nzbthrottle_role_docker_volumes_default: 
      - "{{ nzbthrottle_role_paths_config_location }}:/nzbthrottle/config.json:ro"

    # Type: list
    nzbthrottle_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    nzbthrottle_role_docker_hostname: "{{ nzbthrottle_name }}"

    # Networks
    # Type: string
    nzbthrottle_role_docker_networks_alias: "{{ nzbthrottle_name }}"

    # Type: list
    nzbthrottle_role_docker_networks_default: []

    # Type: list
    nzbthrottle_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    nzbthrottle_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    nzbthrottle_role_docker_state: started


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    nzbthrottle_role_docker_blkio_weight:

    # Type: int
    nzbthrottle_role_docker_cpu_period:

    # Type: int
    nzbthrottle_role_docker_cpu_quota:

    # Type: int
    nzbthrottle_role_docker_cpu_shares:

    # Type: string
    nzbthrottle_role_docker_cpus:

    # Type: string
    nzbthrottle_role_docker_cpuset_cpus:

    # Type: string
    nzbthrottle_role_docker_cpuset_mems:

    # Type: string
    nzbthrottle_role_docker_kernel_memory:

    # Type: string
    nzbthrottle_role_docker_memory:

    # Type: string
    nzbthrottle_role_docker_memory_reservation:

    # Type: string
    nzbthrottle_role_docker_memory_swap:

    # Type: int
    nzbthrottle_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    nzbthrottle_role_docker_cap_drop:

    # Type: list
    nzbthrottle_role_docker_device_cgroup_rules:

    # Type: list
    nzbthrottle_role_docker_device_read_bps:

    # Type: list
    nzbthrottle_role_docker_device_read_iops:

    # Type: list
    nzbthrottle_role_docker_device_requests:

    # Type: list
    nzbthrottle_role_docker_device_write_bps:

    # Type: list
    nzbthrottle_role_docker_device_write_iops:

    # Type: list
    nzbthrottle_role_docker_devices:

    # Type: string
    nzbthrottle_role_docker_devices_default:

    # Type: bool (true/false)
    nzbthrottle_role_docker_privileged:

    # Type: list
    nzbthrottle_role_docker_security_opts:


    # Networking
    # Type: list
    nzbthrottle_role_docker_dns_opts:

    # Type: list
    nzbthrottle_role_docker_dns_search_domains:

    # Type: list
    nzbthrottle_role_docker_dns_servers:

    # Type: dict
    nzbthrottle_role_docker_hosts:

    # Type: string
    nzbthrottle_role_docker_hosts_use_common:

    # Type: string
    nzbthrottle_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    nzbthrottle_role_docker_keep_volumes:

    # Type: list
    nzbthrottle_role_docker_mounts:

    # Type: string
    nzbthrottle_role_docker_volume_driver:

    # Type: list
    nzbthrottle_role_docker_volumes_from:

    # Type: string
    nzbthrottle_role_docker_volumes_global:

    # Type: string
    nzbthrottle_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    nzbthrottle_role_docker_healthcheck:

    # Type: bool (true/false)
    nzbthrottle_role_docker_init:

    # Type: string
    nzbthrottle_role_docker_log_driver:

    # Type: dict
    nzbthrottle_role_docker_log_options:

    # Type: bool (true/false)
    nzbthrottle_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    nzbthrottle_role_docker_auto_remove:

    # Type: list
    nzbthrottle_role_docker_capabilities:

    # Type: string
    nzbthrottle_role_docker_cgroup_parent:

    # Type: string
    nzbthrottle_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    nzbthrottle_role_docker_cleanup:

    # Type: list
    nzbthrottle_role_docker_commands:

    # Type: string
    nzbthrottle_role_docker_create_timeout:

    # Type: string
    nzbthrottle_role_docker_domainname:

    # Type: string
    nzbthrottle_role_docker_entrypoint:

    # Type: string
    nzbthrottle_role_docker_env_file:

    # Type: list
    nzbthrottle_role_docker_exposed_ports:

    # Type: string
    nzbthrottle_role_docker_force_kill:

    # Type: list
    nzbthrottle_role_docker_groups:

    # Type: int
    nzbthrottle_role_docker_healthy_wait_timeout:

    # Type: string
    nzbthrottle_role_docker_ipc_mode:

    # Type: string
    nzbthrottle_role_docker_kill_signal:

    # Type: dict
    nzbthrottle_role_docker_labels:

    # Type: string
    nzbthrottle_role_docker_labels_use_common:

    # Type: list
    nzbthrottle_role_docker_links:

    # Type: bool (true/false)
    nzbthrottle_role_docker_oom_killer:

    # Type: int
    nzbthrottle_role_docker_oom_score_adj:

    # Type: bool (true/false)
    nzbthrottle_role_docker_paused:

    # Type: string
    nzbthrottle_role_docker_pid_mode:

    # Type: list
    nzbthrottle_role_docker_ports:

    # Type: bool (true/false)
    nzbthrottle_role_docker_read_only:

    # Type: bool (true/false)
    nzbthrottle_role_docker_recreate:

    # Type: int
    nzbthrottle_role_docker_restart_retries:

    # Type: string
    nzbthrottle_role_docker_runtime:

    # Type: string
    nzbthrottle_role_docker_shm_size:

    # Type: int
    nzbthrottle_role_docker_stop_timeout:

    # Type: dict
    nzbthrottle_role_docker_storage_opts:

    # Type: list
    nzbthrottle_role_docker_sysctls:

    # Type: list
    nzbthrottle_role_docker_tmpfs:

    # Type: list
    nzbthrottle_role_docker_ulimits:

    # Type: string
    nzbthrottle_role_docker_user:

    # Type: string
    nzbthrottle_role_docker_userns_mode:

    # Type: string
    nzbthrottle_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    nzbthrottle_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    nzbthrottle_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    nzbthrottle_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    nzbthrottle_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    nzbthrottle_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    nzbthrottle_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    nzbthrottle_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    nzbthrottle_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    nzbthrottle_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    nzbthrottle_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    nzbthrottle_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    nzbthrottle_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    nzbthrottle_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    nzbthrottle_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    nzbthrottle_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    nzbthrottle_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    nzbthrottle_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        nzbthrottle_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "nzbthrottle2.{{ user.domain }}"
          - "nzbthrottle.otherdomain.tld"
        ```
        
        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries
        

    2.  Example:

        ```yaml
        nzbthrottle_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'nzbthrottle2.' + user.domain }}`)"
        ```
        
        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule
        

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

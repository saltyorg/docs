---
hide:
  - tags
tags:
  - unpackerr
---

# Unpackerr

## What is it?

[Unpackerr](https://github.com/davidnewhall/unpackerr) checks for completed downloads and extracts them so Lidarr, Radarr, Sonarr may import them. There are a handful of options out there for extracting and deleting files after your client downloads them.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/davidnewhall/unpackerr){: .header-icons } | [:octicons-link-16: Docs](https://github.com/davidnewhall/unpackerr/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/davidnewhall/unpackerr/){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/unpackerr){: .header-icons }|

### 1. Installation

``` shell

sb install unpackerr

```

### 2. Setup

- [:octicons-link-16: Documentation](https://github.com/davidnewhall/unpackerr){: .header-icons }

The important part of the setup is the setup for the applications.  You'll need to change these three settings for each:

```text
[[sonarr]]
  url = "http://sonarr:8989"
  api_key = "YOUR_API_KEY"
# File system path where downloaded Sonarr items are located.
  paths = ['/mnt/unionfs/downloads/torrents/qbittorrent/completed']
```

The `path` will depend on the torrent client you are using and its configuration.

Same setup is required for radarr and lidarr if you are using them.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        unpackerr_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    unpackerr_name: unpackerr

    ```

??? example "Paths"

    ```yaml
    # Type: string
    unpackerr_role_paths_folder: "{{ unpackerr_name }}"

    # Type: string
    unpackerr_role_paths_location: "{{ server_appdata_path }}/{{ unpackerr_role_paths_folder }}"

    # Type: string
    unpackerr_role_paths_config_location: "{{ unpackerr_role_paths_location }}/unpackerr.conf"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    unpackerr_role_docker_container: "{{ unpackerr_name }}"

    # Image
    # Type: bool (true/false)
    unpackerr_role_docker_image_pull: true

    # Type: string
    unpackerr_role_docker_image_repo: "ghcr.io/hotio/unpackerr"

    # Type: string
    unpackerr_role_docker_image_tag: "latest"

    # Type: string
    unpackerr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='unpackerr') }}:{{ lookup('role_var', '_docker_image_tag', role='unpackerr') }}"

    # Envs
    # Type: dict
    unpackerr_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"
      UMASK: "002"

    # Type: dict
    unpackerr_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    unpackerr_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='unpackerr') }}:/config"

    # Type: list
    unpackerr_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    unpackerr_role_docker_hostname: "{{ unpackerr_name }}"

    # Networks
    # Type: string
    unpackerr_role_docker_networks_alias: "{{ unpackerr_name }}"

    # Type: list
    unpackerr_role_docker_networks_default: []

    # Type: list
    unpackerr_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    unpackerr_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    unpackerr_role_docker_state: started


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    unpackerr_role_docker_blkio_weight:

    # Type: int
    unpackerr_role_docker_cpu_period:

    # Type: int
    unpackerr_role_docker_cpu_quota:

    # Type: int
    unpackerr_role_docker_cpu_shares:

    # Type: string
    unpackerr_role_docker_cpus:

    # Type: string
    unpackerr_role_docker_cpuset_cpus:

    # Type: string
    unpackerr_role_docker_cpuset_mems:

    # Type: string
    unpackerr_role_docker_kernel_memory:

    # Type: string
    unpackerr_role_docker_memory:

    # Type: string
    unpackerr_role_docker_memory_reservation:

    # Type: string
    unpackerr_role_docker_memory_swap:

    # Type: int
    unpackerr_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    unpackerr_role_docker_cap_drop:

    # Type: list
    unpackerr_role_docker_device_cgroup_rules:

    # Type: list
    unpackerr_role_docker_device_read_bps:

    # Type: list
    unpackerr_role_docker_device_read_iops:

    # Type: list
    unpackerr_role_docker_device_requests:

    # Type: list
    unpackerr_role_docker_device_write_bps:

    # Type: list
    unpackerr_role_docker_device_write_iops:

    # Type: list
    unpackerr_role_docker_devices:

    # Type: string
    unpackerr_role_docker_devices_default:

    # Type: bool (true/false)
    unpackerr_role_docker_privileged:

    # Type: list
    unpackerr_role_docker_security_opts:


    # Networking
    # Type: list
    unpackerr_role_docker_dns_opts:

    # Type: list
    unpackerr_role_docker_dns_search_domains:

    # Type: list
    unpackerr_role_docker_dns_servers:

    # Type: dict
    unpackerr_role_docker_hosts:

    # Type: string
    unpackerr_role_docker_hosts_use_common:

    # Type: string
    unpackerr_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    unpackerr_role_docker_keep_volumes:

    # Type: list
    unpackerr_role_docker_mounts:

    # Type: string
    unpackerr_role_docker_volume_driver:

    # Type: list
    unpackerr_role_docker_volumes_from:

    # Type: string
    unpackerr_role_docker_volumes_global:

    # Type: string
    unpackerr_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    unpackerr_role_docker_healthcheck:

    # Type: bool (true/false)
    unpackerr_role_docker_init:

    # Type: string
    unpackerr_role_docker_log_driver:

    # Type: dict
    unpackerr_role_docker_log_options:

    # Type: bool (true/false)
    unpackerr_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    unpackerr_role_docker_auto_remove:

    # Type: list
    unpackerr_role_docker_capabilities:

    # Type: string
    unpackerr_role_docker_cgroup_parent:

    # Type: string
    unpackerr_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    unpackerr_role_docker_cleanup:

    # Type: list
    unpackerr_role_docker_commands:

    # Type: string
    unpackerr_role_docker_create_timeout:

    # Type: string
    unpackerr_role_docker_domainname:

    # Type: string
    unpackerr_role_docker_entrypoint:

    # Type: string
    unpackerr_role_docker_env_file:

    # Type: list
    unpackerr_role_docker_exposed_ports:

    # Type: string
    unpackerr_role_docker_force_kill:

    # Type: list
    unpackerr_role_docker_groups:

    # Type: int
    unpackerr_role_docker_healthy_wait_timeout:

    # Type: string
    unpackerr_role_docker_ipc_mode:

    # Type: string
    unpackerr_role_docker_kill_signal:

    # Type: dict
    unpackerr_role_docker_labels:

    # Type: string
    unpackerr_role_docker_labels_use_common:

    # Type: list
    unpackerr_role_docker_links:

    # Type: bool (true/false)
    unpackerr_role_docker_oom_killer:

    # Type: int
    unpackerr_role_docker_oom_score_adj:

    # Type: bool (true/false)
    unpackerr_role_docker_paused:

    # Type: string
    unpackerr_role_docker_pid_mode:

    # Type: list
    unpackerr_role_docker_ports:

    # Type: bool (true/false)
    unpackerr_role_docker_read_only:

    # Type: bool (true/false)
    unpackerr_role_docker_recreate:

    # Type: int
    unpackerr_role_docker_restart_retries:

    # Type: string
    unpackerr_role_docker_runtime:

    # Type: string
    unpackerr_role_docker_shm_size:

    # Type: int
    unpackerr_role_docker_stop_timeout:

    # Type: dict
    unpackerr_role_docker_storage_opts:

    # Type: list
    unpackerr_role_docker_sysctls:

    # Type: list
    unpackerr_role_docker_tmpfs:

    # Type: list
    unpackerr_role_docker_ulimits:

    # Type: string
    unpackerr_role_docker_user:

    # Type: string
    unpackerr_role_docker_userns_mode:

    # Type: string
    unpackerr_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    unpackerr_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    unpackerr_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    unpackerr_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    unpackerr_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    unpackerr_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    unpackerr_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    unpackerr_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    unpackerr_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    unpackerr_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    unpackerr_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    unpackerr_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    unpackerr_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    unpackerr_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    unpackerr_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    unpackerr_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    unpackerr_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    unpackerr_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        unpackerr_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "unpackerr2.{{ user.domain }}"
          - "unpackerr.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        unpackerr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'unpackerr2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

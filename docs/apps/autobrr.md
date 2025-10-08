---
hide:
  - tags
tags:
  - autobrr
---

# Autobrr

## What is it?

[Autobrr](https://autobrr.com/) is a modern single binary replacement for the autodl-irssi+rutorrent plugin.
autobrr monitors IRC announce channels and torznab RSS feeds to get releases as soon as they are available, with good filtering, and regex support. Go brr.

!!! note
      📢 Work in progress. Expect bugs and breaking changes. Features may be broken or incomplete.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://autobrr.com/){: .header-icons } | [:octicons-link-16: Docs](https://autobrr.com/configuration/indexers/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/autobrr/autobrr){: .header-icons }|

### 1. Installation

``` shell

sb install autobrr

```

### 2. URL

- To access the Autobrr dashboard, visit `https://autobrr._yourdomain.com_`

### 3. Setup

- [:octicons-link-16: Documentation](https://autobrr.com/configuration/indexers){: .header-icons }

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        autobrr_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    autobrr_name: autobrr

    ```

??? example "Paths"

    ```yaml
    # Type: string
    autobrr_role_paths_folder: "{{ autobrr_name }}"

    # Type: string
    autobrr_role_paths_location: "{{ server_appdata_path }}/{{ autobrr_role_paths_folder }}"

    # Type: string
    autobrr_role_paths_config_location: "{{ autobrr_role_paths_location }}/config.toml"

    ```

??? example "Web"

    ```yaml
    # Type: string
    autobrr_role_web_subdomain: "{{ autobrr_name }}"

    # Type: string
    autobrr_role_web_domain: "{{ user.domain }}"

    # Type: string
    autobrr_role_web_port: "7474"

    # Type: string
    autobrr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='autobrr') + '.' + lookup('role_var', '_web_domain', role='autobrr')
                           if (lookup('role_var', '_web_subdomain', role='autobrr') | length > 0)
                           else lookup('role_var', '_web_domain', role='autobrr')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    autobrr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='autobrr') }}"

    # Type: string
    autobrr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='autobrr') }}"

    # Type: bool (true/false)
    autobrr_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    autobrr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    autobrr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    autobrr_role_traefik_middleware_custom: ""

    # Type: string
    autobrr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    autobrr_role_traefik_enabled: true

    # Type: bool (true/false)
    autobrr_role_traefik_api_enabled: true

    # Type: string
    autobrr_role_traefik_api_endpoint: "PathPrefix(`/api`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    autobrr_role_docker_container: "{{ autobrr_name }}"

    # Image
    # Type: bool (true/false)
    autobrr_role_docker_image_pull: true

    # Type: string
    autobrr_role_docker_image_repo: "ghcr.io/autobrr/autobrr"

    # Type: string
    autobrr_role_docker_image_tag: "latest"

    # Type: string
    autobrr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='autobrr') }}:{{ lookup('role_var', '_docker_image_tag', role='autobrr') }}"

    # Envs
    # Type: dict
    autobrr_role_docker_envs_default: 
      AUTOBRR__LOG_PATH: "/config/logs"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    autobrr_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    autobrr_role_docker_volumes_default: 
      - "{{ autobrr_role_paths_location }}:/config"

    # Type: list
    autobrr_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    autobrr_role_docker_hostname: "{{ autobrr_name }}"

    # Networks
    # Type: string
    autobrr_role_docker_networks_alias: "{{ autobrr_name }}"

    # Type: list
    autobrr_role_docker_networks_default: []

    # Type: list
    autobrr_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    autobrr_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    autobrr_role_docker_state: started


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    autobrr_role_docker_blkio_weight:

    # Type: int
    autobrr_role_docker_cpu_period:

    # Type: int
    autobrr_role_docker_cpu_quota:

    # Type: int
    autobrr_role_docker_cpu_shares:

    # Type: string
    autobrr_role_docker_cpus:

    # Type: string
    autobrr_role_docker_cpuset_cpus:

    # Type: string
    autobrr_role_docker_cpuset_mems:

    # Type: string
    autobrr_role_docker_kernel_memory:

    # Type: string
    autobrr_role_docker_memory:

    # Type: string
    autobrr_role_docker_memory_reservation:

    # Type: string
    autobrr_role_docker_memory_swap:

    # Type: int
    autobrr_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    autobrr_role_docker_cap_drop:

    # Type: list
    autobrr_role_docker_device_cgroup_rules:

    # Type: list
    autobrr_role_docker_device_read_bps:

    # Type: list
    autobrr_role_docker_device_read_iops:

    # Type: list
    autobrr_role_docker_device_requests:

    # Type: list
    autobrr_role_docker_device_write_bps:

    # Type: list
    autobrr_role_docker_device_write_iops:

    # Type: list
    autobrr_role_docker_devices:

    # Type: string
    autobrr_role_docker_devices_default:

    # Type: bool (true/false)
    autobrr_role_docker_privileged:

    # Type: list
    autobrr_role_docker_security_opts:


    # Networking
    # Type: list
    autobrr_role_docker_dns_opts:

    # Type: list
    autobrr_role_docker_dns_search_domains:

    # Type: list
    autobrr_role_docker_dns_servers:

    # Type: dict
    autobrr_role_docker_hosts:

    # Type: string
    autobrr_role_docker_hosts_use_common:

    # Type: string
    autobrr_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    autobrr_role_docker_keep_volumes:

    # Type: list
    autobrr_role_docker_mounts:

    # Type: string
    autobrr_role_docker_volume_driver:

    # Type: list
    autobrr_role_docker_volumes_from:

    # Type: string
    autobrr_role_docker_volumes_global:

    # Type: string
    autobrr_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    autobrr_role_docker_healthcheck:

    # Type: bool (true/false)
    autobrr_role_docker_init:

    # Type: string
    autobrr_role_docker_log_driver:

    # Type: dict
    autobrr_role_docker_log_options:

    # Type: bool (true/false)
    autobrr_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    autobrr_role_docker_auto_remove:

    # Type: list
    autobrr_role_docker_capabilities:

    # Type: string
    autobrr_role_docker_cgroup_parent:

    # Type: string
    autobrr_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    autobrr_role_docker_cleanup:

    # Type: list
    autobrr_role_docker_commands:

    # Type: string
    autobrr_role_docker_create_timeout:

    # Type: string
    autobrr_role_docker_domainname:

    # Type: string
    autobrr_role_docker_entrypoint:

    # Type: string
    autobrr_role_docker_env_file:

    # Type: list
    autobrr_role_docker_exposed_ports:

    # Type: string
    autobrr_role_docker_force_kill:

    # Type: list
    autobrr_role_docker_groups:

    # Type: int
    autobrr_role_docker_healthy_wait_timeout:

    # Type: string
    autobrr_role_docker_ipc_mode:

    # Type: string
    autobrr_role_docker_kill_signal:

    # Type: dict
    autobrr_role_docker_labels:

    # Type: string
    autobrr_role_docker_labels_use_common:

    # Type: list
    autobrr_role_docker_links:

    # Type: bool (true/false)
    autobrr_role_docker_oom_killer:

    # Type: int
    autobrr_role_docker_oom_score_adj:

    # Type: bool (true/false)
    autobrr_role_docker_paused:

    # Type: string
    autobrr_role_docker_pid_mode:

    # Type: list
    autobrr_role_docker_ports:

    # Type: bool (true/false)
    autobrr_role_docker_read_only:

    # Type: bool (true/false)
    autobrr_role_docker_recreate:

    # Type: int
    autobrr_role_docker_restart_retries:

    # Type: string
    autobrr_role_docker_runtime:

    # Type: string
    autobrr_role_docker_shm_size:

    # Type: int
    autobrr_role_docker_stop_timeout:

    # Type: dict
    autobrr_role_docker_storage_opts:

    # Type: list
    autobrr_role_docker_sysctls:

    # Type: list
    autobrr_role_docker_tmpfs:

    # Type: list
    autobrr_role_docker_ulimits:

    # Type: string
    autobrr_role_docker_user:

    # Type: string
    autobrr_role_docker_userns_mode:

    # Type: string
    autobrr_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    autobrr_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    autobrr_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    autobrr_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    autobrr_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    autobrr_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    autobrr_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    autobrr_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    autobrr_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    autobrr_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    autobrr_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    autobrr_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    autobrr_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    autobrr_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    autobrr_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: string
    autobrr_role_web_fqdn_override:

    # Override the Traefik web host configuration for the container
    # Type: string
    autobrr_role_web_host_override:

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    autobrr_role_web_scheme:

    ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

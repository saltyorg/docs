---
hide:
  - tags
tags:
  - prometheus
  - monitoring
  - metrics
  - observability
---

# Prometheus

## What is it?

Prometheus is an open-source systems monitoring and alerting toolkit. It collects and stores metrics as time series data, providing a powerful query language (PromQL) for analyzing system behavior and setting up alerts.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://prometheus.io/){: .header-icons } | [:octicons-link-16: Docs](https://prometheus.io/docs/introduction/overview/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/prometheus/prometheus){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/prom/prometheus){: .header-icons }|

### 1. Installation

``` shell

sb install prometheus

```

### 2. URL

- To access Prometheus, visit `https://prometheus._yourdomain.com_`

### 3. Setup

Prometheus provides monitoring and alerting with automatic installation of Node Exporter and cAdvisor for system and container metrics. Configuration is at `/opt/prometheus/prometheus.yml`. Data retention defaults to 15 days but can be configured in your [Saltbox inventory](../saltbox/inventory/index.md) using `prometheus_role_retention` and `prometheus_role_size`.

Add custom scrape targets to the config file and restart with `docker restart prometheus`. Works excellently with Grafana using data source `http://prometheus:9090`.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        prometheus_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    prometheus_name: prometheus

    ```

??? example "Config"

    ```yaml
    # Type: string
    prometheus_role_retention: "15d"

    # Type: string
    prometheus_role_size: "0"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    prometheus_role_paths_folder: "{{ prometheus_name }}"

    # Type: string
    prometheus_role_paths_location: "{{ server_appdata_path }}/{{ prometheus_role_paths_folder }}"

    # Type: string
    prometheus_role_paths_config_path: "{{ prometheus_role_paths_location }}/prometheus.yml"

    ```

??? example "Web"

    ```yaml
    # Type: string
    prometheus_role_web_subdomain: "{{ prometheus_name }}"

    # Type: string
    prometheus_role_web_domain: "{{ user.domain }}"

    # Type: string
    prometheus_role_web_port: "9090"

    # Type: string
    prometheus_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='prometheus') + '.' + lookup('role_var', '_web_domain', role='prometheus')
                              if (lookup('role_var', '_web_subdomain', role='prometheus') | length > 0)
                              else lookup('role_var', '_web_domain', role='prometheus')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    prometheus_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='prometheus') }}"

    # Type: string
    prometheus_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='prometheus') }}"

    # Type: bool (true/false)
    prometheus_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    prometheus_role_traefik_sso_middleware: ""

    # Type: string
    prometheus_role_traefik_middleware_default: "{{ traefik_default_middleware + ',prometheus-auth' }}"

    # Type: string
    prometheus_role_traefik_middleware_custom: ""

    # Type: string
    prometheus_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    prometheus_role_traefik_enabled: true

    # Type: bool (true/false)
    prometheus_role_traefik_api_enabled: false

    # Type: string
    prometheus_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    prometheus_role_docker_container: "{{ prometheus_name }}"

    # Image
    # Type: bool (true/false)
    prometheus_role_docker_image_pull: true

    # Type: string
    prometheus_role_docker_image_tag: "latest"

    # Type: string
    prometheus_role_docker_image_repo: "prom/prometheus"

    # Type: string
    prometheus_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='prometheus') }}:{{ lookup('role_var', '_docker_image_tag', role='prometheus') }}"

    # Envs
    # Type: dict
    prometheus_role_docker_envs_default: 
      TZ: "{{ tz }}"

    # Type: dict
    prometheus_role_docker_envs_custom: {}

    # Commands
    # Type: list
    prometheus_role_docker_commands_default: 
      - "--config.file=/etc/prometheus/prometheus.yml"
      - "--storage.tsdb.path=/data"
      - "--storage.tsdb.retention.time={{ lookup('role_var', '_retention', role='prometheus') }}"
      - "--storage.tsdb.retention.size={{ lookup('role_var', '_size', role='prometheus') }}"

    # Type: list
    prometheus_role_docker_commands_custom: []

    # Volumes
    # Type: list
    prometheus_role_docker_volumes_default: 
      - "{{ prometheus_role_paths_location }}:/etc/prometheus"
      - "{{ prometheus_role_paths_location }}/data:/data"

    # Type: list
    prometheus_role_docker_volumes_custom: []

    # Labels
    # Type: dict
    prometheus_role_docker_labels_default: 
      traefik.http.middlewares.prometheus-auth.basicauth.usersfile: "/etc/traefik/auth"

    # Type: dict
    prometheus_role_docker_labels_custom: {}

    # Hostname
    # Type: string
    prometheus_role_docker_hostname: "{{ prometheus_name }}"

    # Networks
    # Type: string
    prometheus_role_docker_networks_alias: "{{ prometheus_name }}"

    # Type: list
    prometheus_role_docker_networks_default: []

    # Type: list
    prometheus_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    prometheus_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    prometheus_role_docker_state: started

    # User
    # Type: string
    prometheus_role_docker_user: "{{ uid }}:{{ gid }}"


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    prometheus_role_docker_blkio_weight:

    # Type: int
    prometheus_role_docker_cpu_period:

    # Type: int
    prometheus_role_docker_cpu_quota:

    # Type: int
    prometheus_role_docker_cpu_shares:

    # Type: string
    prometheus_role_docker_cpus:

    # Type: string
    prometheus_role_docker_cpuset_cpus:

    # Type: string
    prometheus_role_docker_cpuset_mems:

    # Type: string
    prometheus_role_docker_kernel_memory:

    # Type: string
    prometheus_role_docker_memory:

    # Type: string
    prometheus_role_docker_memory_reservation:

    # Type: string
    prometheus_role_docker_memory_swap:

    # Type: int
    prometheus_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    prometheus_role_docker_cap_drop:

    # Type: list
    prometheus_role_docker_device_cgroup_rules:

    # Type: list
    prometheus_role_docker_device_read_bps:

    # Type: list
    prometheus_role_docker_device_read_iops:

    # Type: list
    prometheus_role_docker_device_requests:

    # Type: list
    prometheus_role_docker_device_write_bps:

    # Type: list
    prometheus_role_docker_device_write_iops:

    # Type: list
    prometheus_role_docker_devices:

    # Type: string
    prometheus_role_docker_devices_default:

    # Type: bool (true/false)
    prometheus_role_docker_privileged:

    # Type: list
    prometheus_role_docker_security_opts:


    # Networking
    # Type: list
    prometheus_role_docker_dns_opts:

    # Type: list
    prometheus_role_docker_dns_search_domains:

    # Type: list
    prometheus_role_docker_dns_servers:

    # Type: dict
    prometheus_role_docker_hosts:

    # Type: string
    prometheus_role_docker_hosts_use_common:

    # Type: string
    prometheus_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    prometheus_role_docker_keep_volumes:

    # Type: list
    prometheus_role_docker_mounts:

    # Type: string
    prometheus_role_docker_volume_driver:

    # Type: list
    prometheus_role_docker_volumes_from:

    # Type: string
    prometheus_role_docker_volumes_global:

    # Type: string
    prometheus_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    prometheus_role_docker_healthcheck:

    # Type: bool (true/false)
    prometheus_role_docker_init:

    # Type: string
    prometheus_role_docker_log_driver:

    # Type: dict
    prometheus_role_docker_log_options:

    # Type: bool (true/false)
    prometheus_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    prometheus_role_docker_auto_remove:

    # Type: list
    prometheus_role_docker_capabilities:

    # Type: string
    prometheus_role_docker_cgroup_parent:

    # Type: string
    prometheus_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    prometheus_role_docker_cleanup:

    # Type: string
    prometheus_role_docker_create_timeout:

    # Type: string
    prometheus_role_docker_domainname:

    # Type: string
    prometheus_role_docker_entrypoint:

    # Type: string
    prometheus_role_docker_env_file:

    # Type: list
    prometheus_role_docker_exposed_ports:

    # Type: string
    prometheus_role_docker_force_kill:

    # Type: list
    prometheus_role_docker_groups:

    # Type: int
    prometheus_role_docker_healthy_wait_timeout:

    # Type: string
    prometheus_role_docker_ipc_mode:

    # Type: string
    prometheus_role_docker_kill_signal:

    # Type: string
    prometheus_role_docker_labels_use_common:

    # Type: list
    prometheus_role_docker_links:

    # Type: bool (true/false)
    prometheus_role_docker_oom_killer:

    # Type: int
    prometheus_role_docker_oom_score_adj:

    # Type: bool (true/false)
    prometheus_role_docker_paused:

    # Type: string
    prometheus_role_docker_pid_mode:

    # Type: list
    prometheus_role_docker_ports:

    # Type: bool (true/false)
    prometheus_role_docker_read_only:

    # Type: bool (true/false)
    prometheus_role_docker_recreate:

    # Type: int
    prometheus_role_docker_restart_retries:

    # Type: string
    prometheus_role_docker_runtime:

    # Type: string
    prometheus_role_docker_shm_size:

    # Type: int
    prometheus_role_docker_stop_timeout:

    # Type: dict
    prometheus_role_docker_storage_opts:

    # Type: list
    prometheus_role_docker_sysctls:

    # Type: list
    prometheus_role_docker_tmpfs:

    # Type: list
    prometheus_role_docker_ulimits:

    # Type: string
    prometheus_role_docker_userns_mode:

    # Type: string
    prometheus_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    prometheus_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    prometheus_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    prometheus_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    prometheus_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    prometheus_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    prometheus_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    prometheus_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    prometheus_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    prometheus_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    prometheus_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    prometheus_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    prometheus_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    prometheus_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    prometheus_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    prometheus_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    prometheus_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    prometheus_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        prometheus_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "prometheus2.{{ user.domain }}"
          - "prometheus.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        prometheus_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'prometheus2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

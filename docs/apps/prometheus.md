---
icon: material/docker
hide:
  - tags
tags:
  - prometheus
  - monitoring
  - metrics
  - observability
---

# Prometheus

## Overview

Prometheus is an open-source systems monitoring and alerting toolkit. It collects and stores metrics as time series data, providing a powerful query language (PromQL) for analyzing system behavior and setting up alerts.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://prometheus.io/){: .header-icons } | [:octicons-link-16: Docs](https://prometheus.io/docs/introduction/overview/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/prometheus/prometheus){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/prom/prometheus){: .header-icons }|

### 1. Installation

```shell
sb install prometheus
```

### 2. URL

- To access Prometheus, visit <https://prometheus.iYOUR_DOMAIN_NAMEi>

### 3. Setup

Prometheus provides monitoring and alerting with automatic installation of Node Exporter and cAdvisor for system and container metrics. Configuration is at `/opt/prometheus/prometheus.yml`. Data retention defaults to 15 days but can be configured in your [Saltbox inventory](../saltbox/inventory/index.md) using `prometheus_role_retention` and `prometheus_role_size`.

Add custom scrape targets to the config file and restart with `docker restart prometheus`. Works excellently with Grafana using data source `http://prometheus:9090`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    prometheus_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `prometheus_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `prometheus_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`prometheus_name`"

        ```yaml
        # Type: string
        prometheus_name: prometheus
        ```

=== "Config"

    ??? variable string "`prometheus_role_retention`"

        ```yaml
        # Type: string
        prometheus_role_retention: "15d"
        ```

    ??? variable string "`prometheus_role_size`"

        ```yaml
        # Type: string
        prometheus_role_size: "0"
        ```

=== "Paths"

    ??? variable string "`prometheus_role_paths_folder`"

        ```yaml
        # Type: string
        prometheus_role_paths_folder: "{{ prometheus_name }}"
        ```

    ??? variable string "`prometheus_role_paths_location`"

        ```yaml
        # Type: string
        prometheus_role_paths_location: "{{ server_appdata_path }}/{{ prometheus_role_paths_folder }}"
        ```

    ??? variable string "`prometheus_role_paths_config_path`"

        ```yaml
        # Type: string
        prometheus_role_paths_config_path: "{{ prometheus_role_paths_location }}/prometheus.yml"
        ```

=== "Web"

    ??? variable string "`prometheus_role_web_subdomain`"

        ```yaml
        # Type: string
        prometheus_role_web_subdomain: "{{ prometheus_name }}"
        ```

    ??? variable string "`prometheus_role_web_domain`"

        ```yaml
        # Type: string
        prometheus_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`prometheus_role_web_port`"

        ```yaml
        # Type: string
        prometheus_role_web_port: "9090"
        ```

    ??? variable string "`prometheus_role_web_url`"

        ```yaml
        # Type: string
        prometheus_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='prometheus') + '.' + lookup('role_var', '_web_domain', role='prometheus')
                                  if (lookup('role_var', '_web_subdomain', role='prometheus') | length > 0)
                                  else lookup('role_var', '_web_domain', role='prometheus')) }}"
        ```

=== "DNS"

    ??? variable string "`prometheus_role_dns_record`"

        ```yaml
        # Type: string
        prometheus_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='prometheus') }}"
        ```

    ??? variable string "`prometheus_role_dns_zone`"

        ```yaml
        # Type: string
        prometheus_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='prometheus') }}"
        ```

    ??? variable bool "`prometheus_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        prometheus_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`prometheus_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        prometheus_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`prometheus_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        prometheus_role_traefik_middleware_default: "{{ traefik_default_middleware + ',prometheus-auth' }}"
        ```

    ??? variable string "`prometheus_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        prometheus_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`prometheus_role_traefik_certresolver`"

        ```yaml
        # Type: string
        prometheus_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`prometheus_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        prometheus_role_traefik_enabled: true
        ```

    ??? variable bool "`prometheus_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        prometheus_role_traefik_api_enabled: false
        ```

    ??? variable string "`prometheus_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        prometheus_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`prometheus_role_docker_container`"

        ```yaml
        # Type: string
        prometheus_role_docker_container: "{{ prometheus_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`prometheus_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        prometheus_role_docker_image_pull: true
        ```

    ??? variable string "`prometheus_role_docker_image_tag`"

        ```yaml
        # Type: string
        prometheus_role_docker_image_tag: "latest"
        ```

    ??? variable string "`prometheus_role_docker_image_repo`"

        ```yaml
        # Type: string
        prometheus_role_docker_image_repo: "prom/prometheus"
        ```

    ??? variable string "`prometheus_role_docker_image`"

        ```yaml
        # Type: string
        prometheus_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='prometheus') }}:{{ lookup('role_var', '_docker_image_tag', role='prometheus') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`prometheus_role_docker_envs_default`"

        ```yaml
        # Type: dict
        prometheus_role_docker_envs_default:
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`prometheus_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        prometheus_role_docker_envs_custom: {}
        ```

    <h5>Commands</h5>

    ??? variable list "`prometheus_role_docker_commands_default`"

        ```yaml
        # Type: list
        prometheus_role_docker_commands_default:
          - "--config.file=/etc/prometheus/prometheus.yml"
          - "--storage.tsdb.path=/data"
          - "--storage.tsdb.retention.time={{ lookup('role_var', '_retention', role='prometheus') }}"
          - "--storage.tsdb.retention.size={{ lookup('role_var', '_size', role='prometheus') }}"
        ```

    ??? variable list "`prometheus_role_docker_commands_custom`"

        ```yaml
        # Type: list
        prometheus_role_docker_commands_custom: []
        ```

    <h5>Volumes</h5>

    ??? variable list "`prometheus_role_docker_volumes_default`"

        ```yaml
        # Type: list
        prometheus_role_docker_volumes_default:
          - "{{ prometheus_role_paths_location }}:/etc/prometheus"
          - "{{ prometheus_role_paths_location }}/data:/data"
        ```

    ??? variable list "`prometheus_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        prometheus_role_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable dict "`prometheus_role_docker_labels_default`"

        ```yaml
        # Type: dict
        prometheus_role_docker_labels_default:
          traefik.http.middlewares.prometheus-auth.basicauth.usersfile: "/etc/traefik/auth"
        ```

    ??? variable dict "`prometheus_role_docker_labels_custom`"

        ```yaml
        # Type: dict
        prometheus_role_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`prometheus_role_docker_hostname`"

        ```yaml
        # Type: string
        prometheus_role_docker_hostname: "{{ prometheus_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`prometheus_role_docker_networks_alias`"

        ```yaml
        # Type: string
        prometheus_role_docker_networks_alias: "{{ prometheus_name }}"
        ```

    ??? variable list "`prometheus_role_docker_networks_default`"

        ```yaml
        # Type: list
        prometheus_role_docker_networks_default: []
        ```

    ??? variable list "`prometheus_role_docker_networks_custom`"

        ```yaml
        # Type: list
        prometheus_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`prometheus_role_docker_restart_policy`"

        ```yaml
        # Type: string
        prometheus_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`prometheus_role_docker_state`"

        ```yaml
        # Type: string
        prometheus_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`prometheus_role_docker_user`"

        ```yaml
        # Type: string
        prometheus_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    <h5>Resource Limits</h5>

    ??? variable int "`prometheus_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        prometheus_role_docker_blkio_weight:
        ```

    ??? variable int "`prometheus_role_docker_cpu_period`"

        ```yaml
        # Type: int
        prometheus_role_docker_cpu_period:
        ```

    ??? variable int "`prometheus_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        prometheus_role_docker_cpu_quota:
        ```

    ??? variable int "`prometheus_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        prometheus_role_docker_cpu_shares:
        ```

    ??? variable string "`prometheus_role_docker_cpus`"

        ```yaml
        # Type: string
        prometheus_role_docker_cpus:
        ```

    ??? variable string "`prometheus_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        prometheus_role_docker_cpuset_cpus:
        ```

    ??? variable string "`prometheus_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        prometheus_role_docker_cpuset_mems:
        ```

    ??? variable string "`prometheus_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        prometheus_role_docker_kernel_memory:
        ```

    ??? variable string "`prometheus_role_docker_memory`"

        ```yaml
        # Type: string
        prometheus_role_docker_memory:
        ```

    ??? variable string "`prometheus_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        prometheus_role_docker_memory_reservation:
        ```

    ??? variable string "`prometheus_role_docker_memory_swap`"

        ```yaml
        # Type: string
        prometheus_role_docker_memory_swap:
        ```

    ??? variable int "`prometheus_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        prometheus_role_docker_memory_swappiness:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`prometheus_role_docker_cap_drop`"

        ```yaml
        # Type: list
        prometheus_role_docker_cap_drop:
        ```

    ??? variable list "`prometheus_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        prometheus_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`prometheus_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        prometheus_role_docker_device_read_bps:
        ```

    ??? variable list "`prometheus_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        prometheus_role_docker_device_read_iops:
        ```

    ??? variable list "`prometheus_role_docker_device_requests`"

        ```yaml
        # Type: list
        prometheus_role_docker_device_requests:
        ```

    ??? variable list "`prometheus_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        prometheus_role_docker_device_write_bps:
        ```

    ??? variable list "`prometheus_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        prometheus_role_docker_device_write_iops:
        ```

    ??? variable list "`prometheus_role_docker_devices`"

        ```yaml
        # Type: list
        prometheus_role_docker_devices:
        ```

    ??? variable string "`prometheus_role_docker_devices_default`"

        ```yaml
        # Type: string
        prometheus_role_docker_devices_default:
        ```

    ??? variable bool "`prometheus_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        prometheus_role_docker_privileged:
        ```

    ??? variable list "`prometheus_role_docker_security_opts`"

        ```yaml
        # Type: list
        prometheus_role_docker_security_opts:
        ```

    <h5>Networking</h5>

    ??? variable list "`prometheus_role_docker_dns_opts`"

        ```yaml
        # Type: list
        prometheus_role_docker_dns_opts:
        ```

    ??? variable list "`prometheus_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        prometheus_role_docker_dns_search_domains:
        ```

    ??? variable list "`prometheus_role_docker_dns_servers`"

        ```yaml
        # Type: list
        prometheus_role_docker_dns_servers:
        ```

    ??? variable dict "`prometheus_role_docker_hosts`"

        ```yaml
        # Type: dict
        prometheus_role_docker_hosts:
        ```

    ??? variable string "`prometheus_role_docker_hosts_use_common`"

        ```yaml
        # Type: string
        prometheus_role_docker_hosts_use_common:
        ```

    ??? variable string "`prometheus_role_docker_network_mode`"

        ```yaml
        # Type: string
        prometheus_role_docker_network_mode:
        ```

    <h5>Storage</h5>

    ??? variable bool "`prometheus_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        prometheus_role_docker_keep_volumes:
        ```

    ??? variable list "`prometheus_role_docker_mounts`"

        ```yaml
        # Type: list
        prometheus_role_docker_mounts:
        ```

    ??? variable string "`prometheus_role_docker_volume_driver`"

        ```yaml
        # Type: string
        prometheus_role_docker_volume_driver:
        ```

    ??? variable list "`prometheus_role_docker_volumes_from`"

        ```yaml
        # Type: list
        prometheus_role_docker_volumes_from:
        ```

    ??? variable string "`prometheus_role_docker_volumes_global`"

        ```yaml
        # Type: string
        prometheus_role_docker_volumes_global:
        ```

    ??? variable string "`prometheus_role_docker_working_dir`"

        ```yaml
        # Type: string
        prometheus_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable dict "`prometheus_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        prometheus_role_docker_healthcheck:
        ```

    ??? variable bool "`prometheus_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        prometheus_role_docker_init:
        ```

    ??? variable string "`prometheus_role_docker_log_driver`"

        ```yaml
        # Type: string
        prometheus_role_docker_log_driver:
        ```

    ??? variable dict "`prometheus_role_docker_log_options`"

        ```yaml
        # Type: dict
        prometheus_role_docker_log_options:
        ```

    ??? variable bool "`prometheus_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        prometheus_role_docker_output_logs:
        ```

    <h5>Other Options</h5>

    ??? variable bool "`prometheus_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        prometheus_role_docker_auto_remove:
        ```

    ??? variable list "`prometheus_role_docker_capabilities`"

        ```yaml
        # Type: list
        prometheus_role_docker_capabilities:
        ```

    ??? variable string "`prometheus_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        prometheus_role_docker_cgroup_parent:
        ```

    ??? variable string "`prometheus_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        prometheus_role_docker_cgroupns_mode:
        ```

    ??? variable bool "`prometheus_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        prometheus_role_docker_cleanup:
        ```

    ??? variable string "`prometheus_role_docker_create_timeout`"

        ```yaml
        # Type: string
        prometheus_role_docker_create_timeout:
        ```

    ??? variable string "`prometheus_role_docker_domainname`"

        ```yaml
        # Type: string
        prometheus_role_docker_domainname:
        ```

    ??? variable string "`prometheus_role_docker_entrypoint`"

        ```yaml
        # Type: string
        prometheus_role_docker_entrypoint:
        ```

    ??? variable string "`prometheus_role_docker_env_file`"

        ```yaml
        # Type: string
        prometheus_role_docker_env_file:
        ```

    ??? variable list "`prometheus_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        prometheus_role_docker_exposed_ports:
        ```

    ??? variable string "`prometheus_role_docker_force_kill`"

        ```yaml
        # Type: string
        prometheus_role_docker_force_kill:
        ```

    ??? variable list "`prometheus_role_docker_groups`"

        ```yaml
        # Type: list
        prometheus_role_docker_groups:
        ```

    ??? variable int "`prometheus_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        prometheus_role_docker_healthy_wait_timeout:
        ```

    ??? variable string "`prometheus_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        prometheus_role_docker_ipc_mode:
        ```

    ??? variable string "`prometheus_role_docker_kill_signal`"

        ```yaml
        # Type: string
        prometheus_role_docker_kill_signal:
        ```

    ??? variable string "`prometheus_role_docker_labels_use_common`"

        ```yaml
        # Type: string
        prometheus_role_docker_labels_use_common:
        ```

    ??? variable list "`prometheus_role_docker_links`"

        ```yaml
        # Type: list
        prometheus_role_docker_links:
        ```

    ??? variable bool "`prometheus_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        prometheus_role_docker_oom_killer:
        ```

    ??? variable int "`prometheus_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        prometheus_role_docker_oom_score_adj:
        ```

    ??? variable bool "`prometheus_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        prometheus_role_docker_paused:
        ```

    ??? variable string "`prometheus_role_docker_pid_mode`"

        ```yaml
        # Type: string
        prometheus_role_docker_pid_mode:
        ```

    ??? variable list "`prometheus_role_docker_ports`"

        ```yaml
        # Type: list
        prometheus_role_docker_ports:
        ```

    ??? variable bool "`prometheus_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        prometheus_role_docker_read_only:
        ```

    ??? variable bool "`prometheus_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        prometheus_role_docker_recreate:
        ```

    ??? variable int "`prometheus_role_docker_restart_retries`"

        ```yaml
        # Type: int
        prometheus_role_docker_restart_retries:
        ```

    ??? variable string "`prometheus_role_docker_runtime`"

        ```yaml
        # Type: string
        prometheus_role_docker_runtime:
        ```

    ??? variable string "`prometheus_role_docker_shm_size`"

        ```yaml
        # Type: string
        prometheus_role_docker_shm_size:
        ```

    ??? variable int "`prometheus_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        prometheus_role_docker_stop_timeout:
        ```

    ??? variable dict "`prometheus_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        prometheus_role_docker_storage_opts:
        ```

    ??? variable list "`prometheus_role_docker_sysctls`"

        ```yaml
        # Type: list
        prometheus_role_docker_sysctls:
        ```

    ??? variable list "`prometheus_role_docker_tmpfs`"

        ```yaml
        # Type: list
        prometheus_role_docker_tmpfs:
        ```

    ??? variable list "`prometheus_role_docker_ulimits`"

        ```yaml
        # Type: list
        prometheus_role_docker_ulimits:
        ```

    ??? variable string "`prometheus_role_docker_userns_mode`"

        ```yaml
        # Type: string
        prometheus_role_docker_userns_mode:
        ```

    ??? variable string "`prometheus_role_docker_uts`"

        ```yaml
        # Type: string
        prometheus_role_docker_uts:
        ```

=== "Global Override Options"

    ??? variable bool "`prometheus_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        prometheus_role_autoheal_enabled: true
        ```

    ??? variable string "`prometheus_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        prometheus_role_depends_on: ""
        ```

    ??? variable string "`prometheus_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        prometheus_role_depends_on_delay: "0"
        ```

    ??? variable string "`prometheus_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        prometheus_role_depends_on_healthchecks:
        ```

    ??? variable bool "`prometheus_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        prometheus_role_diun_enabled: true
        ```

    ??? variable bool "`prometheus_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        prometheus_role_dns_enabled: true
        ```

    ??? variable bool "`prometheus_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        prometheus_role_docker_controller: true
        ```

    ??? variable bool "`prometheus_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        prometheus_role_docker_volumes_download:
        ```

    ??? variable bool "`prometheus_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        prometheus_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`prometheus_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        prometheus_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`prometheus_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        prometheus_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`prometheus_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        prometheus_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`prometheus_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        prometheus_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`prometheus_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        prometheus_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`prometheus_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        prometheus_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`prometheus_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        prometheus_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`prometheus_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        prometheus_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`prometheus_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        prometheus_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            prometheus_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "prometheus2.{{ user.domain }}"
              - "prometheus.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`prometheus_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        prometheus_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            prometheus_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'prometheus2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`prometheus_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        prometheus_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
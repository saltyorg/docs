---
hide:
  - tags
tags:
  - jaeger
  - tracing
  - monitoring
  - observability
---

# Jaeger

## What is it?

Jaeger is an open-source, end-to-end distributed tracing system. It's used for monitoring and troubleshooting microservices-based distributed systems, including distributed context propagation, distributed transaction monitoring, root cause analysis, service dependency analysis, and performance/latency optimization.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.jaegertracing.io/){: .header-icons } | [:octicons-link-16: Docs](https://www.jaegertracing.io/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/jaegertracing/jaeger){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jaegertracing/all-in-one){: .header-icons }|

### 1. Installation

``` shell

sb install jaeger

```

### 2. URL

- To access Jaeger, visit `https://jaeger._yourdomain.com_`

### 3. Setup

Jaeger provides distributed tracing for monitoring microservices. The all-in-one container includes UI, Collector, Query, and Agent components. Configure your applications to send traces to `http://jaeger:14268/api/traces` or use the Zipkin-compatible endpoint at `http://jaeger:9411`.

Note: Data is stored in-memory by default and will be lost when the container restarts.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        jaeger_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `jaeger_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `jaeger_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`jaeger_name`"

        ```yaml
        # Type: string
        jaeger_name: jaeger
        ```

=== "Paths"

    ??? variable string "`jaeger_role_paths_folder`"

        ```yaml
        # Type: string
        jaeger_role_paths_folder: "{{ jaeger_name }}"
        ```

    ??? variable string "`jaeger_role_paths_location`"

        ```yaml
        # Type: string
        jaeger_role_paths_location: "{{ server_appdata_path }}/{{ jaeger_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`jaeger_role_web_subdomain`"

        ```yaml
        # Type: string
        jaeger_role_web_subdomain: "{{ jaeger_name }}"
        ```

    ??? variable string "`jaeger_role_web_domain`"

        ```yaml
        # Type: string
        jaeger_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`jaeger_role_web_port`"

        ```yaml
        # Type: string
        jaeger_role_web_port: "16686"
        ```

    ??? variable string "`jaeger_role_web_url`"

        ```yaml
        # Type: string
        jaeger_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='jaeger') + '.' + lookup('role_var', '_web_domain', role='jaeger')
                              if (lookup('role_var', '_web_subdomain', role='jaeger') | length > 0)
                              else lookup('role_var', '_web_domain', role='jaeger')) }}"
        ```

=== "DNS"

    ??? variable string "`jaeger_role_dns_record`"

        ```yaml
        # Type: string
        jaeger_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='jaeger') }}"
        ```

    ??? variable string "`jaeger_role_dns_zone`"

        ```yaml
        # Type: string
        jaeger_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='jaeger') }}"
        ```

    ??? variable bool "`jaeger_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        jaeger_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`jaeger_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        jaeger_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`jaeger_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        jaeger_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`jaeger_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        jaeger_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`jaeger_role_traefik_certresolver`"

        ```yaml
        # Type: string
        jaeger_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`jaeger_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        jaeger_role_traefik_enabled: true
        ```

    ??? variable bool "`jaeger_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        jaeger_role_traefik_api_enabled: false
        ```

    ??? variable string "`jaeger_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        jaeger_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`jaeger_role_docker_container`"

        ```yaml
        # Type: string
        jaeger_role_docker_container: "{{ jaeger_name }}"
        ```

    ##### Image

    ??? variable bool "`jaeger_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        jaeger_role_docker_image_pull: true
        ```

    ??? variable string "`jaeger_role_docker_image_repo`"

        ```yaml
        # Type: string
        jaeger_role_docker_image_repo: "jaegertracing/all-in-one"
        ```

    ??? variable string "`jaeger_role_docker_image_tag`"

        ```yaml
        # Type: string
        jaeger_role_docker_image_tag: "latest"
        ```

    ??? variable string "`jaeger_role_docker_image`"

        ```yaml
        # Type: string
        jaeger_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='jaeger') }}:{{ lookup('role_var', '_docker_image_tag', role='jaeger') }}"
        ```

    ##### Envs

    ??? variable dict "`jaeger_role_docker_envs_default`"

        ```yaml
        # Type: dict
        jaeger_role_docker_envs_default: 
          TZ: "{{ tz }}"
          COLLECTOR_ZIPKIN_HTTP_PORT: "9411"
        ```

    ??? variable dict "`jaeger_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        jaeger_role_docker_envs_custom: {}
        ```

    ##### Hostname

    ??? variable string "`jaeger_role_docker_hostname`"

        ```yaml
        # Type: string
        jaeger_role_docker_hostname: "{{ jaeger_name }}"
        ```

    ##### Networks

    ??? variable string "`jaeger_role_docker_networks_alias`"

        ```yaml
        # Type: string
        jaeger_role_docker_networks_alias: "{{ jaeger_name }}"
        ```

    ??? variable list "`jaeger_role_docker_networks_default`"

        ```yaml
        # Type: list
        jaeger_role_docker_networks_default: []
        ```

    ??? variable list "`jaeger_role_docker_networks_custom`"

        ```yaml
        # Type: list
        jaeger_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`jaeger_role_docker_restart_policy`"

        ```yaml
        # Type: string
        jaeger_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`jaeger_role_docker_state`"

        ```yaml
        # Type: string
        jaeger_role_docker_state: started
        ```

=== "Docker+"

    #### Additional Docker Options

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    ##### Resource Limits

    ??? variable int "`jaeger_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        jaeger_role_docker_blkio_weight:
        ```

    ??? variable int "`jaeger_role_docker_cpu_period`"

        ```yaml
        # Type: int
        jaeger_role_docker_cpu_period:
        ```

    ??? variable int "`jaeger_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        jaeger_role_docker_cpu_quota:
        ```

    ??? variable int "`jaeger_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        jaeger_role_docker_cpu_shares:
        ```

    ??? variable string "`jaeger_role_docker_cpus`"

        ```yaml
        # Type: string
        jaeger_role_docker_cpus:
        ```

    ??? variable string "`jaeger_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        jaeger_role_docker_cpuset_cpus:
        ```

    ??? variable string "`jaeger_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        jaeger_role_docker_cpuset_mems:
        ```

    ??? variable string "`jaeger_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        jaeger_role_docker_kernel_memory:
        ```

    ??? variable string "`jaeger_role_docker_memory`"

        ```yaml
        # Type: string
        jaeger_role_docker_memory:
        ```

    ??? variable string "`jaeger_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        jaeger_role_docker_memory_reservation:
        ```

    ??? variable string "`jaeger_role_docker_memory_swap`"

        ```yaml
        # Type: string
        jaeger_role_docker_memory_swap:
        ```

    ??? variable int "`jaeger_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        jaeger_role_docker_memory_swappiness:
        ```

    ##### Security & Devices

    ??? variable list "`jaeger_role_docker_cap_drop`"

        ```yaml
        # Type: list
        jaeger_role_docker_cap_drop:
        ```

    ??? variable list "`jaeger_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        jaeger_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`jaeger_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        jaeger_role_docker_device_read_bps:
        ```

    ??? variable list "`jaeger_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        jaeger_role_docker_device_read_iops:
        ```

    ??? variable list "`jaeger_role_docker_device_requests`"

        ```yaml
        # Type: list
        jaeger_role_docker_device_requests:
        ```

    ??? variable list "`jaeger_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        jaeger_role_docker_device_write_bps:
        ```

    ??? variable list "`jaeger_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        jaeger_role_docker_device_write_iops:
        ```

    ??? variable list "`jaeger_role_docker_devices`"

        ```yaml
        # Type: list
        jaeger_role_docker_devices:
        ```

    ??? variable string "`jaeger_role_docker_devices_default`"

        ```yaml
        # Type: string
        jaeger_role_docker_devices_default:
        ```

    ??? variable bool "`jaeger_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        jaeger_role_docker_privileged:
        ```

    ??? variable list "`jaeger_role_docker_security_opts`"

        ```yaml
        # Type: list
        jaeger_role_docker_security_opts:
        ```

    ##### Networking

    ??? variable list "`jaeger_role_docker_dns_opts`"

        ```yaml
        # Type: list
        jaeger_role_docker_dns_opts:
        ```

    ??? variable list "`jaeger_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        jaeger_role_docker_dns_search_domains:
        ```

    ??? variable list "`jaeger_role_docker_dns_servers`"

        ```yaml
        # Type: list
        jaeger_role_docker_dns_servers:
        ```

    ??? variable dict "`jaeger_role_docker_hosts`"

        ```yaml
        # Type: dict
        jaeger_role_docker_hosts:
        ```

    ??? variable string "`jaeger_role_docker_hosts_use_common`"

        ```yaml
        # Type: string
        jaeger_role_docker_hosts_use_common:
        ```

    ??? variable string "`jaeger_role_docker_network_mode`"

        ```yaml
        # Type: string
        jaeger_role_docker_network_mode:
        ```

    ##### Storage

    ??? variable bool "`jaeger_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        jaeger_role_docker_keep_volumes:
        ```

    ??? variable list "`jaeger_role_docker_mounts`"

        ```yaml
        # Type: list
        jaeger_role_docker_mounts:
        ```

    ??? variable string "`jaeger_role_docker_volume_driver`"

        ```yaml
        # Type: string
        jaeger_role_docker_volume_driver:
        ```

    ??? variable list "`jaeger_role_docker_volumes`"

        ```yaml
        # Type: list
        jaeger_role_docker_volumes:
        ```

    ??? variable list "`jaeger_role_docker_volumes_from`"

        ```yaml
        # Type: list
        jaeger_role_docker_volumes_from:
        ```

    ??? variable string "`jaeger_role_docker_volumes_global`"

        ```yaml
        # Type: string
        jaeger_role_docker_volumes_global:
        ```

    ??? variable string "`jaeger_role_docker_working_dir`"

        ```yaml
        # Type: string
        jaeger_role_docker_working_dir:
        ```

    ##### Monitoring & Lifecycle

    ??? variable dict "`jaeger_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        jaeger_role_docker_healthcheck:
        ```

    ??? variable bool "`jaeger_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        jaeger_role_docker_init:
        ```

    ??? variable string "`jaeger_role_docker_log_driver`"

        ```yaml
        # Type: string
        jaeger_role_docker_log_driver:
        ```

    ??? variable dict "`jaeger_role_docker_log_options`"

        ```yaml
        # Type: dict
        jaeger_role_docker_log_options:
        ```

    ??? variable bool "`jaeger_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        jaeger_role_docker_output_logs:
        ```

    ##### Other Options

    ??? variable bool "`jaeger_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        jaeger_role_docker_auto_remove:
        ```

    ??? variable list "`jaeger_role_docker_capabilities`"

        ```yaml
        # Type: list
        jaeger_role_docker_capabilities:
        ```

    ??? variable string "`jaeger_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        jaeger_role_docker_cgroup_parent:
        ```

    ??? variable string "`jaeger_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        jaeger_role_docker_cgroupns_mode:
        ```

    ??? variable bool "`jaeger_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        jaeger_role_docker_cleanup:
        ```

    ??? variable list "`jaeger_role_docker_commands`"

        ```yaml
        # Type: list
        jaeger_role_docker_commands:
        ```

    ??? variable string "`jaeger_role_docker_create_timeout`"

        ```yaml
        # Type: string
        jaeger_role_docker_create_timeout:
        ```

    ??? variable string "`jaeger_role_docker_domainname`"

        ```yaml
        # Type: string
        jaeger_role_docker_domainname:
        ```

    ??? variable string "`jaeger_role_docker_entrypoint`"

        ```yaml
        # Type: string
        jaeger_role_docker_entrypoint:
        ```

    ??? variable string "`jaeger_role_docker_env_file`"

        ```yaml
        # Type: string
        jaeger_role_docker_env_file:
        ```

    ??? variable list "`jaeger_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        jaeger_role_docker_exposed_ports:
        ```

    ??? variable string "`jaeger_role_docker_force_kill`"

        ```yaml
        # Type: string
        jaeger_role_docker_force_kill:
        ```

    ??? variable list "`jaeger_role_docker_groups`"

        ```yaml
        # Type: list
        jaeger_role_docker_groups:
        ```

    ??? variable int "`jaeger_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        jaeger_role_docker_healthy_wait_timeout:
        ```

    ??? variable string "`jaeger_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        jaeger_role_docker_ipc_mode:
        ```

    ??? variable string "`jaeger_role_docker_kill_signal`"

        ```yaml
        # Type: string
        jaeger_role_docker_kill_signal:
        ```

    ??? variable dict "`jaeger_role_docker_labels`"

        ```yaml
        # Type: dict
        jaeger_role_docker_labels:
        ```

    ??? variable string "`jaeger_role_docker_labels_use_common`"

        ```yaml
        # Type: string
        jaeger_role_docker_labels_use_common:
        ```

    ??? variable list "`jaeger_role_docker_links`"

        ```yaml
        # Type: list
        jaeger_role_docker_links:
        ```

    ??? variable bool "`jaeger_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        jaeger_role_docker_oom_killer:
        ```

    ??? variable int "`jaeger_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        jaeger_role_docker_oom_score_adj:
        ```

    ??? variable bool "`jaeger_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        jaeger_role_docker_paused:
        ```

    ??? variable string "`jaeger_role_docker_pid_mode`"

        ```yaml
        # Type: string
        jaeger_role_docker_pid_mode:
        ```

    ??? variable list "`jaeger_role_docker_ports`"

        ```yaml
        # Type: list
        jaeger_role_docker_ports:
        ```

    ??? variable bool "`jaeger_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        jaeger_role_docker_read_only:
        ```

    ??? variable bool "`jaeger_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        jaeger_role_docker_recreate:
        ```

    ??? variable int "`jaeger_role_docker_restart_retries`"

        ```yaml
        # Type: int
        jaeger_role_docker_restart_retries:
        ```

    ??? variable string "`jaeger_role_docker_runtime`"

        ```yaml
        # Type: string
        jaeger_role_docker_runtime:
        ```

    ??? variable string "`jaeger_role_docker_shm_size`"

        ```yaml
        # Type: string
        jaeger_role_docker_shm_size:
        ```

    ??? variable int "`jaeger_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        jaeger_role_docker_stop_timeout:
        ```

    ??? variable dict "`jaeger_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        jaeger_role_docker_storage_opts:
        ```

    ??? variable list "`jaeger_role_docker_sysctls`"

        ```yaml
        # Type: list
        jaeger_role_docker_sysctls:
        ```

    ??? variable list "`jaeger_role_docker_tmpfs`"

        ```yaml
        # Type: list
        jaeger_role_docker_tmpfs:
        ```

    ??? variable list "`jaeger_role_docker_ulimits`"

        ```yaml
        # Type: list
        jaeger_role_docker_ulimits:
        ```

    ??? variable string "`jaeger_role_docker_user`"

        ```yaml
        # Type: string
        jaeger_role_docker_user:
        ```

    ??? variable string "`jaeger_role_docker_userns_mode`"

        ```yaml
        # Type: string
        jaeger_role_docker_userns_mode:
        ```

    ??? variable string "`jaeger_role_docker_uts`"

        ```yaml
        # Type: string
        jaeger_role_docker_uts:
        ```

=== "Global Override Options"

    ??? variable bool "`jaeger_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        jaeger_role_autoheal_enabled: true
        ```

    ??? variable string "`jaeger_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        jaeger_role_depends_on: ""
        ```

    ??? variable string "`jaeger_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        jaeger_role_depends_on_delay: "0"
        ```

    ??? variable string "`jaeger_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        jaeger_role_depends_on_healthchecks:
        ```

    ??? variable bool "`jaeger_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        jaeger_role_diun_enabled: true
        ```

    ??? variable bool "`jaeger_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        jaeger_role_dns_enabled: true
        ```

    ??? variable bool "`jaeger_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        jaeger_role_docker_controller: true
        ```

    ??? variable bool "`jaeger_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        jaeger_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`jaeger_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        jaeger_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`jaeger_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        jaeger_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`jaeger_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        jaeger_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`jaeger_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        jaeger_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`jaeger_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        jaeger_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`jaeger_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        jaeger_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`jaeger_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        jaeger_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`jaeger_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        jaeger_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`jaeger_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        jaeger_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            jaeger_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "jaeger2.{{ user.domain }}"
              - "jaeger.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`jaeger_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        jaeger_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            jaeger_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'jaeger2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`jaeger_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        jaeger_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
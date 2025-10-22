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

- To access Jaeger, visit `https://jaeger.xDOMAIN_NAMEx`

### 3. Setup

Jaeger provides distributed tracing for monitoring microservices. The all-in-one container includes UI, Collector, Query, and Agent components. Configure your applications to send traces to `http://jaeger:14268/api/traces` or use the Zipkin-compatible endpoint at `http://jaeger:9411`.

Note: Data is stored in-memory by default and will be lost when the container restarts.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
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

??? example "Basics"

    ```yaml
    # Type: string
    jaeger_name: jaeger

    ```

??? example "Paths"

    ```yaml
    # Type: string
    jaeger_role_paths_folder: "{{ jaeger_name }}"

    # Type: string
    jaeger_role_paths_location: "{{ server_appdata_path }}/{{ jaeger_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    jaeger_role_web_subdomain: "{{ jaeger_name }}"

    # Type: string
    jaeger_role_web_domain: "{{ user.domain }}"

    # Type: string
    jaeger_role_web_port: "16686"

    # Type: string
    jaeger_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='jaeger') + '.' + lookup('role_var', '_web_domain', role='jaeger')
                          if (lookup('role_var', '_web_subdomain', role='jaeger') | length > 0)
                          else lookup('role_var', '_web_domain', role='jaeger')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    jaeger_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='jaeger') }}"

    # Type: string
    jaeger_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='jaeger') }}"

    # Type: bool (true/false)
    jaeger_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    jaeger_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    jaeger_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    jaeger_role_traefik_middleware_custom: ""

    # Type: string
    jaeger_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    jaeger_role_traefik_enabled: true

    # Type: bool (true/false)
    jaeger_role_traefik_api_enabled: false

    # Type: string
    jaeger_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    jaeger_role_docker_container: "{{ jaeger_name }}"

    # Image
    # Type: bool (true/false)
    jaeger_role_docker_image_pull: true

    # Type: string
    jaeger_role_docker_image_repo: "jaegertracing/all-in-one"

    # Type: string
    jaeger_role_docker_image_tag: "latest"

    # Type: string
    jaeger_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='jaeger') }}:{{ lookup('role_var', '_docker_image_tag', role='jaeger') }}"

    # Envs
    # Type: dict
    jaeger_role_docker_envs_default: 
      TZ: "{{ tz }}"
      COLLECTOR_ZIPKIN_HTTP_PORT: "9411"

    # Type: dict
    jaeger_role_docker_envs_custom: {}

    # Hostname
    # Type: string
    jaeger_role_docker_hostname: "{{ jaeger_name }}"

    # Networks
    # Type: string
    jaeger_role_docker_networks_alias: "{{ jaeger_name }}"

    # Type: list
    jaeger_role_docker_networks_default: []

    # Type: list
    jaeger_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    jaeger_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    jaeger_role_docker_state: started


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    jaeger_role_docker_blkio_weight:

    # Type: int
    jaeger_role_docker_cpu_period:

    # Type: int
    jaeger_role_docker_cpu_quota:

    # Type: int
    jaeger_role_docker_cpu_shares:

    # Type: string
    jaeger_role_docker_cpus:

    # Type: string
    jaeger_role_docker_cpuset_cpus:

    # Type: string
    jaeger_role_docker_cpuset_mems:

    # Type: string
    jaeger_role_docker_kernel_memory:

    # Type: string
    jaeger_role_docker_memory:

    # Type: string
    jaeger_role_docker_memory_reservation:

    # Type: string
    jaeger_role_docker_memory_swap:

    # Type: int
    jaeger_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    jaeger_role_docker_cap_drop:

    # Type: list
    jaeger_role_docker_device_cgroup_rules:

    # Type: list
    jaeger_role_docker_device_read_bps:

    # Type: list
    jaeger_role_docker_device_read_iops:

    # Type: list
    jaeger_role_docker_device_requests:

    # Type: list
    jaeger_role_docker_device_write_bps:

    # Type: list
    jaeger_role_docker_device_write_iops:

    # Type: list
    jaeger_role_docker_devices:

    # Type: string
    jaeger_role_docker_devices_default:

    # Type: bool (true/false)
    jaeger_role_docker_privileged:

    # Type: list
    jaeger_role_docker_security_opts:


    # Networking
    # Type: list
    jaeger_role_docker_dns_opts:

    # Type: list
    jaeger_role_docker_dns_search_domains:

    # Type: list
    jaeger_role_docker_dns_servers:

    # Type: dict
    jaeger_role_docker_hosts:

    # Type: string
    jaeger_role_docker_hosts_use_common:

    # Type: string
    jaeger_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    jaeger_role_docker_keep_volumes:

    # Type: list
    jaeger_role_docker_mounts:

    # Type: string
    jaeger_role_docker_volume_driver:

    # Type: list
    jaeger_role_docker_volumes:

    # Type: list
    jaeger_role_docker_volumes_from:

    # Type: string
    jaeger_role_docker_volumes_global:

    # Type: string
    jaeger_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    jaeger_role_docker_healthcheck:

    # Type: bool (true/false)
    jaeger_role_docker_init:

    # Type: string
    jaeger_role_docker_log_driver:

    # Type: dict
    jaeger_role_docker_log_options:

    # Type: bool (true/false)
    jaeger_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    jaeger_role_docker_auto_remove:

    # Type: list
    jaeger_role_docker_capabilities:

    # Type: string
    jaeger_role_docker_cgroup_parent:

    # Type: string
    jaeger_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    jaeger_role_docker_cleanup:

    # Type: list
    jaeger_role_docker_commands:

    # Type: string
    jaeger_role_docker_create_timeout:

    # Type: string
    jaeger_role_docker_domainname:

    # Type: string
    jaeger_role_docker_entrypoint:

    # Type: string
    jaeger_role_docker_env_file:

    # Type: list
    jaeger_role_docker_exposed_ports:

    # Type: string
    jaeger_role_docker_force_kill:

    # Type: list
    jaeger_role_docker_groups:

    # Type: int
    jaeger_role_docker_healthy_wait_timeout:

    # Type: string
    jaeger_role_docker_ipc_mode:

    # Type: string
    jaeger_role_docker_kill_signal:

    # Type: dict
    jaeger_role_docker_labels:

    # Type: string
    jaeger_role_docker_labels_use_common:

    # Type: list
    jaeger_role_docker_links:

    # Type: bool (true/false)
    jaeger_role_docker_oom_killer:

    # Type: int
    jaeger_role_docker_oom_score_adj:

    # Type: bool (true/false)
    jaeger_role_docker_paused:

    # Type: string
    jaeger_role_docker_pid_mode:

    # Type: list
    jaeger_role_docker_ports:

    # Type: bool (true/false)
    jaeger_role_docker_read_only:

    # Type: bool (true/false)
    jaeger_role_docker_recreate:

    # Type: int
    jaeger_role_docker_restart_retries:

    # Type: string
    jaeger_role_docker_runtime:

    # Type: string
    jaeger_role_docker_shm_size:

    # Type: int
    jaeger_role_docker_stop_timeout:

    # Type: dict
    jaeger_role_docker_storage_opts:

    # Type: list
    jaeger_role_docker_sysctls:

    # Type: list
    jaeger_role_docker_tmpfs:

    # Type: list
    jaeger_role_docker_ulimits:

    # Type: string
    jaeger_role_docker_user:

    # Type: string
    jaeger_role_docker_userns_mode:

    # Type: string
    jaeger_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    jaeger_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    jaeger_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    jaeger_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    jaeger_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    jaeger_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    jaeger_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    jaeger_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    jaeger_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    jaeger_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    jaeger_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    jaeger_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    jaeger_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    jaeger_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    jaeger_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    jaeger_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    jaeger_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    jaeger_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        jaeger_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "jaeger2.{{ user.domain }}"
          - "jaeger.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        jaeger_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'jaeger2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

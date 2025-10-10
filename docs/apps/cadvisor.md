---
hide:
  - tags
tags:
  - cadvisor
  - monitoring
  - docker
---

# cAdvisor

## What is it?

[cAdvisor](https://github.com/google/cadvisor) (Container Advisor) provides container users an understanding of the resource usage and performance characteristics of their running containers. It is a running daemon that collects, aggregates, processes, and exports information about running containers.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/google/cadvisor){: .header-icons } | [:octicons-link-16: Docs](https://github.com/google/cadvisor/tree/master/docs){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/google/cadvisor){: .header-icons } | [:material-docker: Docker](https://gcr.io/cadvisor/cadvisor){: .header-icons }|

### 1. Installation

``` shell

sb install cadvisor

```

### 2. URL

- To access cAdvisor, visit `https://cadvisor._yourdomain.com_`

### 3. Setup

cAdvisor automatically monitors all Docker containers on your system. No additional configuration is required. The web interface provides resource usage, performance metrics, and container information.

cAdvisor is often used with Prometheus and Grafana for advanced metrics collection and visualization.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        cadvisor_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    cadvisor_name: cadvisor

    ```

??? example "Web"

    ```yaml
    # Type: string
    cadvisor_role_web_subdomain: "{{ cadvisor_name }}"

    # Type: string
    cadvisor_role_web_domain: "{{ user.domain }}"

    # Type: string
    cadvisor_role_web_port: "8080"

    # Type: string
    cadvisor_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='cadvisor') + '.' + lookup('role_var', '_web_domain', role='cadvisor')
                            if (lookup('role_var', '_web_subdomain', role='cadvisor') | length > 0)
                            else lookup('role_var', '_web_domain', role='cadvisor')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    cadvisor_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='cadvisor') }}"

    # Type: string
    cadvisor_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='cadvisor') }}"

    # Type: bool (true/false)
    cadvisor_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    cadvisor_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    cadvisor_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    cadvisor_role_traefik_middleware_custom: ""

    # Type: string
    cadvisor_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    cadvisor_role_traefik_enabled: true

    # Type: bool (true/false)
    cadvisor_role_traefik_api_enabled: false

    # Type: string
    cadvisor_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    cadvisor_role_docker_container: "{{ cadvisor_name }}"

    # Image
    # Type: bool (true/false)
    cadvisor_role_docker_image_pull: true

    # Type: string
    cadvisor_role_docker_image_repo: "gcr.io/cadvisor/cadvisor"

    # Type: string
    cadvisor_role_docker_image_tag: "latest"

    # Type: string
    cadvisor_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='cadvisor') }}:{{ lookup('role_var', '_docker_image_tag', role='cadvisor') }}"

    # Envs
    # Type: dict
    cadvisor_role_docker_envs_default: 
      TZ: "{{ tz }}"

    # Type: dict
    cadvisor_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    cadvisor_role_docker_volumes_default: 
      - "/:/rootfs:ro"
      - "/var/run:/var/run:ro"
      - "/sys:/sys:ro"
      - "/var/lib/docker/:/var/lib/docker:ro"
      - "/dev/disk/:/dev/disk:ro"

    # Type: list
    cadvisor_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    cadvisor_role_docker_hostname: "{{ cadvisor_name }}"

    # Networks
    # Type: string
    cadvisor_role_docker_networks_alias: "{{ cadvisor_name }}"

    # Type: list
    cadvisor_role_docker_networks_default: []

    # Type: list
    cadvisor_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    cadvisor_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    cadvisor_role_docker_state: started

    # Privileged
    # Type: bool (true/false)
    cadvisor_role_docker_privileged: true


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    cadvisor_role_docker_blkio_weight:

    # Type: int
    cadvisor_role_docker_cpu_period:

    # Type: int
    cadvisor_role_docker_cpu_quota:

    # Type: int
    cadvisor_role_docker_cpu_shares:

    # Type: string
    cadvisor_role_docker_cpus:

    # Type: string
    cadvisor_role_docker_cpuset_cpus:

    # Type: string
    cadvisor_role_docker_cpuset_mems:

    # Type: string
    cadvisor_role_docker_kernel_memory:

    # Type: string
    cadvisor_role_docker_memory:

    # Type: string
    cadvisor_role_docker_memory_reservation:

    # Type: string
    cadvisor_role_docker_memory_swap:

    # Type: int
    cadvisor_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    cadvisor_role_docker_cap_drop:

    # Type: list
    cadvisor_role_docker_device_cgroup_rules:

    # Type: list
    cadvisor_role_docker_device_read_bps:

    # Type: list
    cadvisor_role_docker_device_read_iops:

    # Type: list
    cadvisor_role_docker_device_requests:

    # Type: list
    cadvisor_role_docker_device_write_bps:

    # Type: list
    cadvisor_role_docker_device_write_iops:

    # Type: list
    cadvisor_role_docker_devices:

    # Type: string
    cadvisor_role_docker_devices_default:

    # Type: list
    cadvisor_role_docker_security_opts:


    # Networking
    # Type: list
    cadvisor_role_docker_dns_opts:

    # Type: list
    cadvisor_role_docker_dns_search_domains:

    # Type: list
    cadvisor_role_docker_dns_servers:

    # Type: dict
    cadvisor_role_docker_hosts:

    # Type: string
    cadvisor_role_docker_hosts_use_common:

    # Type: string
    cadvisor_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    cadvisor_role_docker_keep_volumes:

    # Type: list
    cadvisor_role_docker_mounts:

    # Type: string
    cadvisor_role_docker_volume_driver:

    # Type: list
    cadvisor_role_docker_volumes_from:

    # Type: string
    cadvisor_role_docker_volumes_global:

    # Type: string
    cadvisor_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    cadvisor_role_docker_healthcheck:

    # Type: bool (true/false)
    cadvisor_role_docker_init:

    # Type: string
    cadvisor_role_docker_log_driver:

    # Type: dict
    cadvisor_role_docker_log_options:

    # Type: bool (true/false)
    cadvisor_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    cadvisor_role_docker_auto_remove:

    # Type: list
    cadvisor_role_docker_capabilities:

    # Type: string
    cadvisor_role_docker_cgroup_parent:

    # Type: string
    cadvisor_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    cadvisor_role_docker_cleanup:

    # Type: list
    cadvisor_role_docker_commands:

    # Type: string
    cadvisor_role_docker_create_timeout:

    # Type: string
    cadvisor_role_docker_domainname:

    # Type: string
    cadvisor_role_docker_entrypoint:

    # Type: string
    cadvisor_role_docker_env_file:

    # Type: list
    cadvisor_role_docker_exposed_ports:

    # Type: string
    cadvisor_role_docker_force_kill:

    # Type: list
    cadvisor_role_docker_groups:

    # Type: int
    cadvisor_role_docker_healthy_wait_timeout:

    # Type: string
    cadvisor_role_docker_ipc_mode:

    # Type: string
    cadvisor_role_docker_kill_signal:

    # Type: dict
    cadvisor_role_docker_labels:

    # Type: string
    cadvisor_role_docker_labels_use_common:

    # Type: list
    cadvisor_role_docker_links:

    # Type: bool (true/false)
    cadvisor_role_docker_oom_killer:

    # Type: int
    cadvisor_role_docker_oom_score_adj:

    # Type: bool (true/false)
    cadvisor_role_docker_paused:

    # Type: string
    cadvisor_role_docker_pid_mode:

    # Type: list
    cadvisor_role_docker_ports:

    # Type: bool (true/false)
    cadvisor_role_docker_read_only:

    # Type: bool (true/false)
    cadvisor_role_docker_recreate:

    # Type: int
    cadvisor_role_docker_restart_retries:

    # Type: string
    cadvisor_role_docker_runtime:

    # Type: string
    cadvisor_role_docker_shm_size:

    # Type: int
    cadvisor_role_docker_stop_timeout:

    # Type: dict
    cadvisor_role_docker_storage_opts:

    # Type: list
    cadvisor_role_docker_sysctls:

    # Type: list
    cadvisor_role_docker_tmpfs:

    # Type: list
    cadvisor_role_docker_ulimits:

    # Type: string
    cadvisor_role_docker_user:

    # Type: string
    cadvisor_role_docker_userns_mode:

    # Type: string
    cadvisor_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    cadvisor_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    cadvisor_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    cadvisor_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    cadvisor_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    cadvisor_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    cadvisor_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    cadvisor_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    cadvisor_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    cadvisor_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    cadvisor_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    cadvisor_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    cadvisor_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    cadvisor_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    cadvisor_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    cadvisor_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    cadvisor_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    cadvisor_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        cadvisor_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "cadvisor2.{{ user.domain }}"
          - "cadvisor.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        cadvisor_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'cadvisor2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
hide:
  - tags
tags:
  - nginx
  - web-server
  - reverse-proxy
---

# Nginx

## What is it?

Nginx is a high-performance web server, reverse proxy, and load balancer. This role deploys Nginx using the LinuxServer.io container, providing a simple way to host static websites or act as a reverse proxy for your applications.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://nginx.org/){: .header-icons } | [:octicons-link-16: Docs](https://nginx.org/en/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/nginx/nginx){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/nginx){: .header-icons }|

### 1. Installation

``` shell

sb install nginx

```

### 2. URL

- To access Nginx, visit `https://nginx.xDOMAIN_NAMEx`

### 3. Setup

Nginx is deployed using the LinuxServer.io container with configuration files at `/opt/nginx/`. Place website files in `/opt/nginx/www/` and edit site configs in `/opt/nginx/nginx/site-confs/`. Multiple instances are supported via the `nginx_instances` variable in your [Saltbox inventory](../saltbox/inventory/index.md). Restart with `docker restart nginx` to apply changes.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `nginx_instances`.

    === "Role-level Override"

        Applies to all instances of nginx:

        ```yaml
        nginx_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `nginx2`):

        ```yaml
        nginx2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `nginx_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `nginx_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        nginx_instances: ["nginx"]

        ```

    === "Example"

        ```yaml
        # Type: list
        nginx_instances: ["nginx", "nginx2"]

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        nginx_role_paths_folder: "{{ nginx_name }}"

        # Type: string
        nginx_role_paths_location: "{{ server_appdata_path }}/{{ nginx_role_paths_folder }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        nginx2_paths_folder: "{{ nginx_name }}"

        # Type: string
        nginx2_paths_location: "{{ server_appdata_path }}/{{ nginx_role_paths_folder }}"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        nginx_role_web_subdomain: "{{ nginx_name }}"

        # Type: string
        nginx_role_web_domain: "{{ user.domain }}"

        # Type: string
        nginx_role_web_port: "80"

        # Type: string
        nginx_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='nginx') + '.' + lookup('role_var', '_web_domain', role='nginx')
                             if (lookup('role_var', '_web_subdomain', role='nginx') | length > 0)
                             else lookup('role_var', '_web_domain', role='nginx')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        nginx2_web_subdomain: "{{ nginx_name }}"

        # Type: string
        nginx2_web_domain: "{{ user.domain }}"

        # Type: string
        nginx2_web_port: "80"

        # Type: string
        nginx2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='nginx') + '.' + lookup('role_var', '_web_domain', role='nginx')
                         if (lookup('role_var', '_web_subdomain', role='nginx') | length > 0)
                         else lookup('role_var', '_web_domain', role='nginx')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        nginx_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='nginx') }}"

        # Type: string
        nginx_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='nginx') }}"

        # Type: bool (true/false)
        nginx_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        nginx2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='nginx') }}"

        # Type: string
        nginx2_dns_zone: "{{ lookup('role_var', '_web_domain', role='nginx') }}"

        # Type: bool (true/false)
        nginx2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        nginx_role_traefik_sso_middleware: ""

        # Type: string
        nginx_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        nginx_role_traefik_middleware_custom: ""

        # Type: string
        nginx_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        nginx_role_traefik_enabled: true

        # Type: bool (true/false)
        nginx_role_traefik_api_enabled: false

        # Type: string
        nginx_role_traefik_api_endpoint: ""

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        nginx2_traefik_sso_middleware: ""

        # Type: string
        nginx2_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        nginx2_traefik_middleware_custom: ""

        # Type: string
        nginx2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        nginx2_traefik_enabled: true

        # Type: bool (true/false)
        nginx2_traefik_api_enabled: false

        # Type: string
        nginx2_traefik_api_endpoint: ""

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        nginx_role_docker_container: "{{ nginx_name }}"

        # Image
        # Type: bool (true/false)
        nginx_role_docker_image_pull: true

        # Type: string
        nginx_role_docker_image_repo: "lscr.io/linuxserver/nginx"

        # Type: string
        nginx_role_docker_image_tag: "latest"

        # Type: string
        nginx_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='nginx') }}:{{ lookup('role_var', '_docker_image_tag', role='nginx') }}"

        # Envs
        # Type: dict
        nginx_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"

        # Type: dict
        nginx_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        nginx_role_docker_volumes_default: 
          - "{{ nginx_role_paths_location }}:/config"

        # Type: list
        nginx_role_docker_volumes_custom: []

        # Hostname
        # Type: string
        nginx_role_docker_hostname: "{{ nginx_name }}"

        # Networks
        # Type: string
        nginx_role_docker_networks_alias: "{{ nginx_name }}"

        # Type: list
        nginx_role_docker_networks_default: []

        # Type: list
        nginx_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        nginx_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        nginx_role_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via create_docker_container
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        nginx_role_docker_blkio_weight:

        # Type: int
        nginx_role_docker_cpu_period:

        # Type: int
        nginx_role_docker_cpu_quota:

        # Type: int
        nginx_role_docker_cpu_shares:

        # Type: string
        nginx_role_docker_cpus:

        # Type: string
        nginx_role_docker_cpuset_cpus:

        # Type: string
        nginx_role_docker_cpuset_mems:

        # Type: string
        nginx_role_docker_kernel_memory:

        # Type: string
        nginx_role_docker_memory:

        # Type: string
        nginx_role_docker_memory_reservation:

        # Type: string
        nginx_role_docker_memory_swap:

        # Type: int
        nginx_role_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        nginx_role_docker_cap_drop:

        # Type: list
        nginx_role_docker_device_cgroup_rules:

        # Type: list
        nginx_role_docker_device_read_bps:

        # Type: list
        nginx_role_docker_device_read_iops:

        # Type: list
        nginx_role_docker_device_requests:

        # Type: list
        nginx_role_docker_device_write_bps:

        # Type: list
        nginx_role_docker_device_write_iops:

        # Type: list
        nginx_role_docker_devices:

        # Type: string
        nginx_role_docker_devices_default:

        # Type: bool (true/false)
        nginx_role_docker_privileged:

        # Type: list
        nginx_role_docker_security_opts:

        # Networking
        # Type: list
        nginx_role_docker_dns_opts:

        # Type: list
        nginx_role_docker_dns_search_domains:

        # Type: list
        nginx_role_docker_dns_servers:

        # Type: dict
        nginx_role_docker_hosts:

        # Type: string
        nginx_role_docker_hosts_use_common:

        # Type: string
        nginx_role_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        nginx_role_docker_keep_volumes:

        # Type: list
        nginx_role_docker_mounts:

        # Type: string
        nginx_role_docker_volume_driver:

        # Type: list
        nginx_role_docker_volumes_from:

        # Type: string
        nginx_role_docker_volumes_global:

        # Type: string
        nginx_role_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        nginx_role_docker_healthcheck:

        # Type: bool (true/false)
        nginx_role_docker_init:

        # Type: string
        nginx_role_docker_log_driver:

        # Type: dict
        nginx_role_docker_log_options:

        # Type: bool (true/false)
        nginx_role_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        nginx_role_docker_auto_remove:

        # Type: list
        nginx_role_docker_capabilities:

        # Type: string
        nginx_role_docker_cgroup_parent:

        # Type: string
        nginx_role_docker_cgroupns_mode:

        # Type: bool (true/false)
        nginx_role_docker_cleanup:

        # Type: list
        nginx_role_docker_commands:

        # Type: string
        nginx_role_docker_create_timeout:

        # Type: string
        nginx_role_docker_domainname:

        # Type: string
        nginx_role_docker_entrypoint:

        # Type: string
        nginx_role_docker_env_file:

        # Type: list
        nginx_role_docker_exposed_ports:

        # Type: string
        nginx_role_docker_force_kill:

        # Type: list
        nginx_role_docker_groups:

        # Type: int
        nginx_role_docker_healthy_wait_timeout:

        # Type: string
        nginx_role_docker_ipc_mode:

        # Type: string
        nginx_role_docker_kill_signal:

        # Type: dict
        nginx_role_docker_labels:

        # Type: string
        nginx_role_docker_labels_use_common:

        # Type: list
        nginx_role_docker_links:

        # Type: bool (true/false)
        nginx_role_docker_oom_killer:

        # Type: int
        nginx_role_docker_oom_score_adj:

        # Type: bool (true/false)
        nginx_role_docker_paused:

        # Type: string
        nginx_role_docker_pid_mode:

        # Type: list
        nginx_role_docker_ports:

        # Type: bool (true/false)
        nginx_role_docker_read_only:

        # Type: bool (true/false)
        nginx_role_docker_recreate:

        # Type: int
        nginx_role_docker_restart_retries:

        # Type: string
        nginx_role_docker_runtime:

        # Type: string
        nginx_role_docker_shm_size:

        # Type: int
        nginx_role_docker_stop_timeout:

        # Type: dict
        nginx_role_docker_storage_opts:

        # Type: list
        nginx_role_docker_sysctls:

        # Type: list
        nginx_role_docker_tmpfs:

        # Type: list
        nginx_role_docker_ulimits:

        # Type: string
        nginx_role_docker_user:

        # Type: string
        nginx_role_docker_userns_mode:

        # Type: string
        nginx_role_docker_uts:

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        nginx2_docker_container: "{{ nginx_name }}"

        # Image
        # Type: bool (true/false)
        nginx2_docker_image_pull: true

        # Type: string
        nginx2_docker_image_repo: "lscr.io/linuxserver/nginx"

        # Type: string
        nginx2_docker_image_tag: "latest"

        # Type: string
        nginx2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='nginx') }}:{{ lookup('role_var', '_docker_image_tag', role='nginx') }}"

        # Envs
        # Type: dict
        nginx2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"

        # Type: dict
        nginx2_docker_envs_custom: {}

        # Volumes
        # Type: list
        nginx2_docker_volumes_default: 
          - "{{ nginx_role_paths_location }}:/config"

        # Type: list
        nginx2_docker_volumes_custom: []

        # Hostname
        # Type: string
        nginx2_docker_hostname: "{{ nginx_name }}"

        # Networks
        # Type: string
        nginx2_docker_networks_alias: "{{ nginx_name }}"

        # Type: list
        nginx2_docker_networks_default: []

        # Type: list
        nginx2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        nginx2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        nginx2_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via lookup('docker_var', ...)
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        nginx2_docker_blkio_weight:
        # Type: int
        nginx2_docker_cpu_period:
        # Type: int
        nginx2_docker_cpu_quota:
        # Type: int
        nginx2_docker_cpu_shares:
        # Type: string
        nginx2_docker_cpus:
        # Type: string
        nginx2_docker_cpuset_cpus:
        # Type: string
        nginx2_docker_cpuset_mems:
        # Type: string
        nginx2_docker_kernel_memory:
        # Type: string
        nginx2_docker_memory:
        # Type: string
        nginx2_docker_memory_reservation:
        # Type: string
        nginx2_docker_memory_swap:
        # Type: int
        nginx2_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        nginx2_docker_cap_drop:
        # Type: list
        nginx2_docker_device_cgroup_rules:
        # Type: list
        nginx2_docker_device_read_bps:
        # Type: list
        nginx2_docker_device_read_iops:
        # Type: list
        nginx2_docker_device_requests:
        # Type: list
        nginx2_docker_device_write_bps:
        # Type: list
        nginx2_docker_device_write_iops:
        # Type: list
        nginx2_docker_devices:
        # Type: string
        nginx2_docker_devices_default:
        # Type: bool (true/false)
        nginx2_docker_privileged:
        # Type: list
        nginx2_docker_security_opts:

        # Networking
        # Type: list
        nginx2_docker_dns_opts:
        # Type: list
        nginx2_docker_dns_search_domains:
        # Type: list
        nginx2_docker_dns_servers:
        # Type: dict
        nginx2_docker_hosts:
        # Type: string
        nginx2_docker_hosts_use_common:
        # Type: string
        nginx2_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        nginx2_docker_keep_volumes:
        # Type: list
        nginx2_docker_mounts:
        # Type: string
        nginx2_docker_volume_driver:
        # Type: list
        nginx2_docker_volumes_from:
        # Type: string
        nginx2_docker_volumes_global:
        # Type: string
        nginx2_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        nginx2_docker_healthcheck:
        # Type: bool (true/false)
        nginx2_docker_init:
        # Type: string
        nginx2_docker_log_driver:
        # Type: dict
        nginx2_docker_log_options:
        # Type: bool (true/false)
        nginx2_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        nginx2_docker_auto_remove:
        # Type: list
        nginx2_docker_capabilities:
        # Type: string
        nginx2_docker_cgroup_parent:
        # Type: string
        nginx2_docker_cgroupns_mode:
        # Type: bool (true/false)
        nginx2_docker_cleanup:
        # Type: list
        nginx2_docker_commands:
        # Type: string
        nginx2_docker_create_timeout:
        # Type: string
        nginx2_docker_domainname:
        # Type: string
        nginx2_docker_entrypoint:
        # Type: string
        nginx2_docker_env_file:
        # Type: list
        nginx2_docker_exposed_ports:
        # Type: string
        nginx2_docker_force_kill:
        # Type: list
        nginx2_docker_groups:
        # Type: int
        nginx2_docker_healthy_wait_timeout:
        # Type: string
        nginx2_docker_ipc_mode:
        # Type: string
        nginx2_docker_kill_signal:
        # Type: dict
        nginx2_docker_labels:
        # Type: string
        nginx2_docker_labels_use_common:
        # Type: list
        nginx2_docker_links:
        # Type: bool (true/false)
        nginx2_docker_oom_killer:
        # Type: int
        nginx2_docker_oom_score_adj:
        # Type: bool (true/false)
        nginx2_docker_paused:
        # Type: string
        nginx2_docker_pid_mode:
        # Type: list
        nginx2_docker_ports:
        # Type: bool (true/false)
        nginx2_docker_read_only:
        # Type: bool (true/false)
        nginx2_docker_recreate:
        # Type: int
        nginx2_docker_restart_retries:
        # Type: string
        nginx2_docker_runtime:
        # Type: string
        nginx2_docker_shm_size:
        # Type: int
        nginx2_docker_stop_timeout:
        # Type: dict
        nginx2_docker_storage_opts:
        # Type: list
        nginx2_docker_sysctls:
        # Type: list
        nginx2_docker_tmpfs:
        # Type: list
        nginx2_docker_ulimits:
        # Type: string
        nginx2_docker_user:
        # Type: string
        nginx2_docker_userns_mode:
        # Type: string
        nginx2_docker_uts:

        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        nginx_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        nginx_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        nginx_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        nginx_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        nginx_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        nginx_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        nginx_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        nginx_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        nginx_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        nginx_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        nginx_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        nginx_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        nginx_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        nginx_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        nginx_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        nginx_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        nginx_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            nginx_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "nginx2.{{ user.domain }}"
              - "nginx.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            nginx_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'nginx2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `nginx2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        nginx2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        nginx2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        nginx2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        nginx2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        nginx2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        nginx2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        nginx2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        nginx2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        nginx2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        nginx2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        nginx2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        nginx2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        nginx2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        nginx2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        nginx2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        nginx2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        nginx2_web_scheme:

        ```

        1.  Example:

            ```yaml
            nginx2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "nginx2.{{ user.domain }}"
              - "nginx.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            nginx2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'nginx2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

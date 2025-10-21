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

- To access Nginx, visit `https://nginx._yourdomain.com_`

### 3. Setup

Nginx is deployed using the LinuxServer.io container with configuration files at `/opt/nginx/`. Place website files in `/opt/nginx/www/` and edit site configs in `/opt/nginx/nginx/site-confs/`. Multiple instances are supported via the `nginx_instances` variable in your [Saltbox inventory](../saltbox/inventory/index.md). Restart with `docker restart nginx` to apply changes.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

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

=== "Basics"

    ??? variable list "`nginx_instances`"

        ```yaml
        # Type: list
        nginx_instances: ["nginx"]
        ```

        !!! example

            ```yaml
            # Type: list
            nginx_instances: ["nginx", "nginx2"]
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`nginx_role_paths_folder`"

            ```yaml
            # Type: string
            nginx_role_paths_folder: "{{ nginx_name }}"
            ```

        ??? variable string "`nginx_role_paths_location`"

            ```yaml
            # Type: string
            nginx_role_paths_location: "{{ server_appdata_path }}/{{ nginx_role_paths_folder }}"
            ```

    === "Instance-level"

        ??? variable string "`nginx2_paths_folder`"

            ```yaml
            # Type: string
            nginx2_paths_folder: "{{ nginx_name }}"
            ```

        ??? variable string "`nginx2_paths_location`"

            ```yaml
            # Type: string
            nginx2_paths_location: "{{ server_appdata_path }}/{{ nginx_role_paths_folder }}"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`nginx_role_web_subdomain`"

            ```yaml
            # Type: string
            nginx_role_web_subdomain: "{{ nginx_name }}"
            ```

        ??? variable string "`nginx_role_web_domain`"

            ```yaml
            # Type: string
            nginx_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`nginx_role_web_port`"

            ```yaml
            # Type: string
            nginx_role_web_port: "80"
            ```

        ??? variable string "`nginx_role_web_url`"

            ```yaml
            # Type: string
            nginx_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='nginx') + '.' + lookup('role_var', '_web_domain', role='nginx')
                                 if (lookup('role_var', '_web_subdomain', role='nginx') | length > 0)
                                 else lookup('role_var', '_web_domain', role='nginx')) }}"
            ```

    === "Instance-level"

        ??? variable string "`nginx2_web_subdomain`"

            ```yaml
            # Type: string
            nginx2_web_subdomain: "{{ nginx_name }}"
            ```

        ??? variable string "`nginx2_web_domain`"

            ```yaml
            # Type: string
            nginx2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`nginx2_web_port`"

            ```yaml
            # Type: string
            nginx2_web_port: "80"
            ```

        ??? variable string "`nginx2_web_url`"

            ```yaml
            # Type: string
            nginx2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='nginx') + '.' + lookup('role_var', '_web_domain', role='nginx')
                             if (lookup('role_var', '_web_subdomain', role='nginx') | length > 0)
                             else lookup('role_var', '_web_domain', role='nginx')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`nginx_role_dns_record`"

            ```yaml
            # Type: string
            nginx_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='nginx') }}"
            ```

        ??? variable string "`nginx_role_dns_zone`"

            ```yaml
            # Type: string
            nginx_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='nginx') }}"
            ```

        ??? variable bool "`nginx_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            nginx_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`nginx2_dns_record`"

            ```yaml
            # Type: string
            nginx2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='nginx') }}"
            ```

        ??? variable string "`nginx2_dns_zone`"

            ```yaml
            # Type: string
            nginx2_dns_zone: "{{ lookup('role_var', '_web_domain', role='nginx') }}"
            ```

        ??? variable bool "`nginx2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            nginx2_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`nginx_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            nginx_role_traefik_sso_middleware: ""
            ```

        ??? variable string "`nginx_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            nginx_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`nginx_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            nginx_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`nginx_role_traefik_certresolver`"

            ```yaml
            # Type: string
            nginx_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`nginx_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            nginx_role_traefik_enabled: true
            ```

        ??? variable bool "`nginx_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            nginx_role_traefik_api_enabled: false
            ```

        ??? variable string "`nginx_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            nginx_role_traefik_api_endpoint: ""
            ```

    === "Instance-level"

        ??? variable string "`nginx2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            nginx2_traefik_sso_middleware: ""
            ```

        ??? variable string "`nginx2_traefik_middleware_default`"

            ```yaml
            # Type: string
            nginx2_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`nginx2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            nginx2_traefik_middleware_custom: ""
            ```

        ??? variable string "`nginx2_traefik_certresolver`"

            ```yaml
            # Type: string
            nginx2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`nginx2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            nginx2_traefik_enabled: true
            ```

        ??? variable bool "`nginx2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            nginx2_traefik_api_enabled: false
            ```

        ??? variable string "`nginx2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            nginx2_traefik_api_endpoint: ""
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`nginx_role_docker_container`"

            ```yaml
            # Type: string
            nginx_role_docker_container: "{{ nginx_name }}"
            ```

        ##### Image

        ??? variable bool "`nginx_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            nginx_role_docker_image_pull: true
            ```

        ??? variable string "`nginx_role_docker_image_repo`"

            ```yaml
            # Type: string
            nginx_role_docker_image_repo: "lscr.io/linuxserver/nginx"
            ```

        ??? variable string "`nginx_role_docker_image_tag`"

            ```yaml
            # Type: string
            nginx_role_docker_image_tag: "latest"
            ```

        ??? variable string "`nginx_role_docker_image`"

            ```yaml
            # Type: string
            nginx_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='nginx') }}:{{ lookup('role_var', '_docker_image_tag', role='nginx') }}"
            ```

        ##### Envs

        ??? variable dict "`nginx_role_docker_envs_default`"

            ```yaml
            # Type: dict
            nginx_role_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              TZ: "{{ tz }}"
            ```

        ??? variable dict "`nginx_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            nginx_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`nginx_role_docker_volumes_default`"

            ```yaml
            # Type: list
            nginx_role_docker_volumes_default: 
              - "{{ nginx_role_paths_location }}:/config"
            ```

        ??? variable list "`nginx_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            nginx_role_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`nginx_role_docker_hostname`"

            ```yaml
            # Type: string
            nginx_role_docker_hostname: "{{ nginx_name }}"
            ```

        ##### Networks

        ??? variable string "`nginx_role_docker_networks_alias`"

            ```yaml
            # Type: string
            nginx_role_docker_networks_alias: "{{ nginx_name }}"
            ```

        ??? variable list "`nginx_role_docker_networks_default`"

            ```yaml
            # Type: list
            nginx_role_docker_networks_default: []
            ```

        ??? variable list "`nginx_role_docker_networks_custom`"

            ```yaml
            # Type: list
            nginx_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`nginx_role_docker_restart_policy`"

            ```yaml
            # Type: string
            nginx_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`nginx_role_docker_state`"

            ```yaml
            # Type: string
            nginx_role_docker_state: started
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`nginx2_docker_container`"

            ```yaml
            # Type: string
            nginx2_docker_container: "{{ nginx_name }}"
            ```

        ##### Image

        ??? variable bool "`nginx2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            nginx2_docker_image_pull: true
            ```

        ??? variable string "`nginx2_docker_image_repo`"

            ```yaml
            # Type: string
            nginx2_docker_image_repo: "lscr.io/linuxserver/nginx"
            ```

        ??? variable string "`nginx2_docker_image_tag`"

            ```yaml
            # Type: string
            nginx2_docker_image_tag: "latest"
            ```

        ??? variable string "`nginx2_docker_image`"

            ```yaml
            # Type: string
            nginx2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='nginx') }}:{{ lookup('role_var', '_docker_image_tag', role='nginx') }}"
            ```

        ##### Envs

        ??? variable dict "`nginx2_docker_envs_default`"

            ```yaml
            # Type: dict
            nginx2_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              TZ: "{{ tz }}"
            ```

        ??? variable dict "`nginx2_docker_envs_custom`"

            ```yaml
            # Type: dict
            nginx2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`nginx2_docker_volumes_default`"

            ```yaml
            # Type: list
            nginx2_docker_volumes_default: 
              - "{{ nginx_role_paths_location }}:/config"
            ```

        ??? variable list "`nginx2_docker_volumes_custom`"

            ```yaml
            # Type: list
            nginx2_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`nginx2_docker_hostname`"

            ```yaml
            # Type: string
            nginx2_docker_hostname: "{{ nginx_name }}"
            ```

        ##### Networks

        ??? variable string "`nginx2_docker_networks_alias`"

            ```yaml
            # Type: string
            nginx2_docker_networks_alias: "{{ nginx_name }}"
            ```

        ??? variable list "`nginx2_docker_networks_default`"

            ```yaml
            # Type: list
            nginx2_docker_networks_default: []
            ```

        ??? variable list "`nginx2_docker_networks_custom`"

            ```yaml
            # Type: list
            nginx2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`nginx2_docker_restart_policy`"

            ```yaml
            # Type: string
            nginx2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`nginx2_docker_state`"

            ```yaml
            # Type: string
            nginx2_docker_state: started
            ```

=== "Docker+"

    #### Additional Docker Options

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    === "Role-level"

        ##### Resource Limits

        ??? variable int "`nginx_role_docker_blkio_weight`"

            ```yaml
            # Type: int
            nginx_role_docker_blkio_weight:
            ```

        ??? variable int "`nginx_role_docker_cpu_period`"

            ```yaml
            # Type: int
            nginx_role_docker_cpu_period:
            ```

        ??? variable int "`nginx_role_docker_cpu_quota`"

            ```yaml
            # Type: int
            nginx_role_docker_cpu_quota:
            ```

        ??? variable int "`nginx_role_docker_cpu_shares`"

            ```yaml
            # Type: int
            nginx_role_docker_cpu_shares:
            ```

        ??? variable string "`nginx_role_docker_cpus`"

            ```yaml
            # Type: string
            nginx_role_docker_cpus:
            ```

        ??? variable string "`nginx_role_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            nginx_role_docker_cpuset_cpus:
            ```

        ??? variable string "`nginx_role_docker_cpuset_mems`"

            ```yaml
            # Type: string
            nginx_role_docker_cpuset_mems:
            ```

        ??? variable string "`nginx_role_docker_kernel_memory`"

            ```yaml
            # Type: string
            nginx_role_docker_kernel_memory:
            ```

        ??? variable string "`nginx_role_docker_memory`"

            ```yaml
            # Type: string
            nginx_role_docker_memory:
            ```

        ??? variable string "`nginx_role_docker_memory_reservation`"

            ```yaml
            # Type: string
            nginx_role_docker_memory_reservation:
            ```

        ??? variable string "`nginx_role_docker_memory_swap`"

            ```yaml
            # Type: string
            nginx_role_docker_memory_swap:
            ```

        ??? variable int "`nginx_role_docker_memory_swappiness`"

            ```yaml
            # Type: int
            nginx_role_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`nginx_role_docker_cap_drop`"

            ```yaml
            # Type: list
            nginx_role_docker_cap_drop:
            ```

        ??? variable list "`nginx_role_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            nginx_role_docker_device_cgroup_rules:
            ```

        ??? variable list "`nginx_role_docker_device_read_bps`"

            ```yaml
            # Type: list
            nginx_role_docker_device_read_bps:
            ```

        ??? variable list "`nginx_role_docker_device_read_iops`"

            ```yaml
            # Type: list
            nginx_role_docker_device_read_iops:
            ```

        ??? variable list "`nginx_role_docker_device_requests`"

            ```yaml
            # Type: list
            nginx_role_docker_device_requests:
            ```

        ??? variable list "`nginx_role_docker_device_write_bps`"

            ```yaml
            # Type: list
            nginx_role_docker_device_write_bps:
            ```

        ??? variable list "`nginx_role_docker_device_write_iops`"

            ```yaml
            # Type: list
            nginx_role_docker_device_write_iops:
            ```

        ??? variable list "`nginx_role_docker_devices`"

            ```yaml
            # Type: list
            nginx_role_docker_devices:
            ```

        ??? variable string "`nginx_role_docker_devices_default`"

            ```yaml
            # Type: string
            nginx_role_docker_devices_default:
            ```

        ??? variable bool "`nginx_role_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            nginx_role_docker_privileged:
            ```

        ??? variable list "`nginx_role_docker_security_opts`"

            ```yaml
            # Type: list
            nginx_role_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`nginx_role_docker_dns_opts`"

            ```yaml
            # Type: list
            nginx_role_docker_dns_opts:
            ```

        ??? variable list "`nginx_role_docker_dns_search_domains`"

            ```yaml
            # Type: list
            nginx_role_docker_dns_search_domains:
            ```

        ??? variable list "`nginx_role_docker_dns_servers`"

            ```yaml
            # Type: list
            nginx_role_docker_dns_servers:
            ```

        ??? variable dict "`nginx_role_docker_hosts`"

            ```yaml
            # Type: dict
            nginx_role_docker_hosts:
            ```

        ??? variable string "`nginx_role_docker_hosts_use_common`"

            ```yaml
            # Type: string
            nginx_role_docker_hosts_use_common:
            ```

        ??? variable string "`nginx_role_docker_network_mode`"

            ```yaml
            # Type: string
            nginx_role_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`nginx_role_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            nginx_role_docker_keep_volumes:
            ```

        ??? variable list "`nginx_role_docker_mounts`"

            ```yaml
            # Type: list
            nginx_role_docker_mounts:
            ```

        ??? variable string "`nginx_role_docker_volume_driver`"

            ```yaml
            # Type: string
            nginx_role_docker_volume_driver:
            ```

        ??? variable list "`nginx_role_docker_volumes_from`"

            ```yaml
            # Type: list
            nginx_role_docker_volumes_from:
            ```

        ??? variable string "`nginx_role_docker_volumes_global`"

            ```yaml
            # Type: string
            nginx_role_docker_volumes_global:
            ```

        ??? variable string "`nginx_role_docker_working_dir`"

            ```yaml
            # Type: string
            nginx_role_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`nginx_role_docker_healthcheck`"

            ```yaml
            # Type: dict
            nginx_role_docker_healthcheck:
            ```

        ??? variable bool "`nginx_role_docker_init`"

            ```yaml
            # Type: bool (true/false)
            nginx_role_docker_init:
            ```

        ??? variable string "`nginx_role_docker_log_driver`"

            ```yaml
            # Type: string
            nginx_role_docker_log_driver:
            ```

        ??? variable dict "`nginx_role_docker_log_options`"

            ```yaml
            # Type: dict
            nginx_role_docker_log_options:
            ```

        ??? variable bool "`nginx_role_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            nginx_role_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`nginx_role_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            nginx_role_docker_auto_remove:
            ```

        ??? variable list "`nginx_role_docker_capabilities`"

            ```yaml
            # Type: list
            nginx_role_docker_capabilities:
            ```

        ??? variable string "`nginx_role_docker_cgroup_parent`"

            ```yaml
            # Type: string
            nginx_role_docker_cgroup_parent:
            ```

        ??? variable string "`nginx_role_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            nginx_role_docker_cgroupns_mode:
            ```

        ??? variable bool "`nginx_role_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            nginx_role_docker_cleanup:
            ```

        ??? variable list "`nginx_role_docker_commands`"

            ```yaml
            # Type: list
            nginx_role_docker_commands:
            ```

        ??? variable string "`nginx_role_docker_create_timeout`"

            ```yaml
            # Type: string
            nginx_role_docker_create_timeout:
            ```

        ??? variable string "`nginx_role_docker_domainname`"

            ```yaml
            # Type: string
            nginx_role_docker_domainname:
            ```

        ??? variable string "`nginx_role_docker_entrypoint`"

            ```yaml
            # Type: string
            nginx_role_docker_entrypoint:
            ```

        ??? variable string "`nginx_role_docker_env_file`"

            ```yaml
            # Type: string
            nginx_role_docker_env_file:
            ```

        ??? variable list "`nginx_role_docker_exposed_ports`"

            ```yaml
            # Type: list
            nginx_role_docker_exposed_ports:
            ```

        ??? variable string "`nginx_role_docker_force_kill`"

            ```yaml
            # Type: string
            nginx_role_docker_force_kill:
            ```

        ??? variable list "`nginx_role_docker_groups`"

            ```yaml
            # Type: list
            nginx_role_docker_groups:
            ```

        ??? variable int "`nginx_role_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            nginx_role_docker_healthy_wait_timeout:
            ```

        ??? variable string "`nginx_role_docker_ipc_mode`"

            ```yaml
            # Type: string
            nginx_role_docker_ipc_mode:
            ```

        ??? variable string "`nginx_role_docker_kill_signal`"

            ```yaml
            # Type: string
            nginx_role_docker_kill_signal:
            ```

        ??? variable dict "`nginx_role_docker_labels`"

            ```yaml
            # Type: dict
            nginx_role_docker_labels:
            ```

        ??? variable string "`nginx_role_docker_labels_use_common`"

            ```yaml
            # Type: string
            nginx_role_docker_labels_use_common:
            ```

        ??? variable list "`nginx_role_docker_links`"

            ```yaml
            # Type: list
            nginx_role_docker_links:
            ```

        ??? variable bool "`nginx_role_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            nginx_role_docker_oom_killer:
            ```

        ??? variable int "`nginx_role_docker_oom_score_adj`"

            ```yaml
            # Type: int
            nginx_role_docker_oom_score_adj:
            ```

        ??? variable bool "`nginx_role_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            nginx_role_docker_paused:
            ```

        ??? variable string "`nginx_role_docker_pid_mode`"

            ```yaml
            # Type: string
            nginx_role_docker_pid_mode:
            ```

        ??? variable list "`nginx_role_docker_ports`"

            ```yaml
            # Type: list
            nginx_role_docker_ports:
            ```

        ??? variable bool "`nginx_role_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            nginx_role_docker_read_only:
            ```

        ??? variable bool "`nginx_role_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            nginx_role_docker_recreate:
            ```

        ??? variable int "`nginx_role_docker_restart_retries`"

            ```yaml
            # Type: int
            nginx_role_docker_restart_retries:
            ```

        ??? variable string "`nginx_role_docker_runtime`"

            ```yaml
            # Type: string
            nginx_role_docker_runtime:
            ```

        ??? variable string "`nginx_role_docker_shm_size`"

            ```yaml
            # Type: string
            nginx_role_docker_shm_size:
            ```

        ??? variable int "`nginx_role_docker_stop_timeout`"

            ```yaml
            # Type: int
            nginx_role_docker_stop_timeout:
            ```

        ??? variable dict "`nginx_role_docker_storage_opts`"

            ```yaml
            # Type: dict
            nginx_role_docker_storage_opts:
            ```

        ??? variable list "`nginx_role_docker_sysctls`"

            ```yaml
            # Type: list
            nginx_role_docker_sysctls:
            ```

        ??? variable list "`nginx_role_docker_tmpfs`"

            ```yaml
            # Type: list
            nginx_role_docker_tmpfs:
            ```

        ??? variable list "`nginx_role_docker_ulimits`"

            ```yaml
            # Type: list
            nginx_role_docker_ulimits:
            ```

        ??? variable string "`nginx_role_docker_user`"

            ```yaml
            # Type: string
            nginx_role_docker_user:
            ```

        ??? variable string "`nginx_role_docker_userns_mode`"

            ```yaml
            # Type: string
            nginx_role_docker_userns_mode:
            ```

        ??? variable string "`nginx_role_docker_uts`"

            ```yaml
            # Type: string
            nginx_role_docker_uts:
            ```

    === "Instance-level"

        ##### Resource Limits

        ??? variable int "`nginx2_docker_blkio_weight`"

            ```yaml
            # Type: int
            nginx2_docker_blkio_weight:
            ```

        ??? variable int "`nginx2_docker_cpu_period`"

            ```yaml
            # Type: int
            nginx2_docker_cpu_period:
            ```

        ??? variable int "`nginx2_docker_cpu_quota`"

            ```yaml
            # Type: int
            nginx2_docker_cpu_quota:
            ```

        ??? variable int "`nginx2_docker_cpu_shares`"

            ```yaml
            # Type: int
            nginx2_docker_cpu_shares:
            ```

        ??? variable string "`nginx2_docker_cpus`"

            ```yaml
            # Type: string
            nginx2_docker_cpus:
            ```

        ??? variable string "`nginx2_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            nginx2_docker_cpuset_cpus:
            ```

        ??? variable string "`nginx2_docker_cpuset_mems`"

            ```yaml
            # Type: string
            nginx2_docker_cpuset_mems:
            ```

        ??? variable string "`nginx2_docker_kernel_memory`"

            ```yaml
            # Type: string
            nginx2_docker_kernel_memory:
            ```

        ??? variable string "`nginx2_docker_memory`"

            ```yaml
            # Type: string
            nginx2_docker_memory:
            ```

        ??? variable string "`nginx2_docker_memory_reservation`"

            ```yaml
            # Type: string
            nginx2_docker_memory_reservation:
            ```

        ??? variable string "`nginx2_docker_memory_swap`"

            ```yaml
            # Type: string
            nginx2_docker_memory_swap:
            ```

        ??? variable int "`nginx2_docker_memory_swappiness`"

            ```yaml
            # Type: int
            nginx2_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`nginx2_docker_cap_drop`"

            ```yaml
            # Type: list
            nginx2_docker_cap_drop:
            ```

        ??? variable list "`nginx2_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            nginx2_docker_device_cgroup_rules:
            ```

        ??? variable list "`nginx2_docker_device_read_bps`"

            ```yaml
            # Type: list
            nginx2_docker_device_read_bps:
            ```

        ??? variable list "`nginx2_docker_device_read_iops`"

            ```yaml
            # Type: list
            nginx2_docker_device_read_iops:
            ```

        ??? variable list "`nginx2_docker_device_requests`"

            ```yaml
            # Type: list
            nginx2_docker_device_requests:
            ```

        ??? variable list "`nginx2_docker_device_write_bps`"

            ```yaml
            # Type: list
            nginx2_docker_device_write_bps:
            ```

        ??? variable list "`nginx2_docker_device_write_iops`"

            ```yaml
            # Type: list
            nginx2_docker_device_write_iops:
            ```

        ??? variable list "`nginx2_docker_devices`"

            ```yaml
            # Type: list
            nginx2_docker_devices:
            ```

        ??? variable string "`nginx2_docker_devices_default`"

            ```yaml
            # Type: string
            nginx2_docker_devices_default:
            ```

        ??? variable bool "`nginx2_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            nginx2_docker_privileged:
            ```

        ??? variable list "`nginx2_docker_security_opts`"

            ```yaml
            # Type: list
            nginx2_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`nginx2_docker_dns_opts`"

            ```yaml
            # Type: list
            nginx2_docker_dns_opts:
            ```

        ??? variable list "`nginx2_docker_dns_search_domains`"

            ```yaml
            # Type: list
            nginx2_docker_dns_search_domains:
            ```

        ??? variable list "`nginx2_docker_dns_servers`"

            ```yaml
            # Type: list
            nginx2_docker_dns_servers:
            ```

        ??? variable dict "`nginx2_docker_hosts`"

            ```yaml
            # Type: dict
            nginx2_docker_hosts:
            ```

        ??? variable string "`nginx2_docker_hosts_use_common`"

            ```yaml
            # Type: string
            nginx2_docker_hosts_use_common:
            ```

        ??? variable string "`nginx2_docker_network_mode`"

            ```yaml
            # Type: string
            nginx2_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`nginx2_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            nginx2_docker_keep_volumes:
            ```

        ??? variable list "`nginx2_docker_mounts`"

            ```yaml
            # Type: list
            nginx2_docker_mounts:
            ```

        ??? variable string "`nginx2_docker_volume_driver`"

            ```yaml
            # Type: string
            nginx2_docker_volume_driver:
            ```

        ??? variable list "`nginx2_docker_volumes_from`"

            ```yaml
            # Type: list
            nginx2_docker_volumes_from:
            ```

        ??? variable string "`nginx2_docker_volumes_global`"

            ```yaml
            # Type: string
            nginx2_docker_volumes_global:
            ```

        ??? variable string "`nginx2_docker_working_dir`"

            ```yaml
            # Type: string
            nginx2_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`nginx2_docker_healthcheck`"

            ```yaml
            # Type: dict
            nginx2_docker_healthcheck:
            ```

        ??? variable bool "`nginx2_docker_init`"

            ```yaml
            # Type: bool (true/false)
            nginx2_docker_init:
            ```

        ??? variable string "`nginx2_docker_log_driver`"

            ```yaml
            # Type: string
            nginx2_docker_log_driver:
            ```

        ??? variable dict "`nginx2_docker_log_options`"

            ```yaml
            # Type: dict
            nginx2_docker_log_options:
            ```

        ??? variable bool "`nginx2_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            nginx2_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`nginx2_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            nginx2_docker_auto_remove:
            ```

        ??? variable list "`nginx2_docker_capabilities`"

            ```yaml
            # Type: list
            nginx2_docker_capabilities:
            ```

        ??? variable string "`nginx2_docker_cgroup_parent`"

            ```yaml
            # Type: string
            nginx2_docker_cgroup_parent:
            ```

        ??? variable string "`nginx2_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            nginx2_docker_cgroupns_mode:
            ```

        ??? variable bool "`nginx2_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            nginx2_docker_cleanup:
            ```

        ??? variable list "`nginx2_docker_commands`"

            ```yaml
            # Type: list
            nginx2_docker_commands:
            ```

        ??? variable string "`nginx2_docker_create_timeout`"

            ```yaml
            # Type: string
            nginx2_docker_create_timeout:
            ```

        ??? variable string "`nginx2_docker_domainname`"

            ```yaml
            # Type: string
            nginx2_docker_domainname:
            ```

        ??? variable string "`nginx2_docker_entrypoint`"

            ```yaml
            # Type: string
            nginx2_docker_entrypoint:
            ```

        ??? variable string "`nginx2_docker_env_file`"

            ```yaml
            # Type: string
            nginx2_docker_env_file:
            ```

        ??? variable list "`nginx2_docker_exposed_ports`"

            ```yaml
            # Type: list
            nginx2_docker_exposed_ports:
            ```

        ??? variable string "`nginx2_docker_force_kill`"

            ```yaml
            # Type: string
            nginx2_docker_force_kill:
            ```

        ??? variable list "`nginx2_docker_groups`"

            ```yaml
            # Type: list
            nginx2_docker_groups:
            ```

        ??? variable int "`nginx2_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            nginx2_docker_healthy_wait_timeout:
            ```

        ??? variable string "`nginx2_docker_ipc_mode`"

            ```yaml
            # Type: string
            nginx2_docker_ipc_mode:
            ```

        ??? variable string "`nginx2_docker_kill_signal`"

            ```yaml
            # Type: string
            nginx2_docker_kill_signal:
            ```

        ??? variable dict "`nginx2_docker_labels`"

            ```yaml
            # Type: dict
            nginx2_docker_labels:
            ```

        ??? variable string "`nginx2_docker_labels_use_common`"

            ```yaml
            # Type: string
            nginx2_docker_labels_use_common:
            ```

        ??? variable list "`nginx2_docker_links`"

            ```yaml
            # Type: list
            nginx2_docker_links:
            ```

        ??? variable bool "`nginx2_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            nginx2_docker_oom_killer:
            ```

        ??? variable int "`nginx2_docker_oom_score_adj`"

            ```yaml
            # Type: int
            nginx2_docker_oom_score_adj:
            ```

        ??? variable bool "`nginx2_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            nginx2_docker_paused:
            ```

        ??? variable string "`nginx2_docker_pid_mode`"

            ```yaml
            # Type: string
            nginx2_docker_pid_mode:
            ```

        ??? variable list "`nginx2_docker_ports`"

            ```yaml
            # Type: list
            nginx2_docker_ports:
            ```

        ??? variable bool "`nginx2_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            nginx2_docker_read_only:
            ```

        ??? variable bool "`nginx2_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            nginx2_docker_recreate:
            ```

        ??? variable int "`nginx2_docker_restart_retries`"

            ```yaml
            # Type: int
            nginx2_docker_restart_retries:
            ```

        ??? variable string "`nginx2_docker_runtime`"

            ```yaml
            # Type: string
            nginx2_docker_runtime:
            ```

        ??? variable string "`nginx2_docker_shm_size`"

            ```yaml
            # Type: string
            nginx2_docker_shm_size:
            ```

        ??? variable int "`nginx2_docker_stop_timeout`"

            ```yaml
            # Type: int
            nginx2_docker_stop_timeout:
            ```

        ??? variable dict "`nginx2_docker_storage_opts`"

            ```yaml
            # Type: dict
            nginx2_docker_storage_opts:
            ```

        ??? variable list "`nginx2_docker_sysctls`"

            ```yaml
            # Type: list
            nginx2_docker_sysctls:
            ```

        ??? variable list "`nginx2_docker_tmpfs`"

            ```yaml
            # Type: list
            nginx2_docker_tmpfs:
            ```

        ??? variable list "`nginx2_docker_ulimits`"

            ```yaml
            # Type: list
            nginx2_docker_ulimits:
            ```

        ??? variable string "`nginx2_docker_user`"

            ```yaml
            # Type: string
            nginx2_docker_user:
            ```

        ??? variable string "`nginx2_docker_userns_mode`"

            ```yaml
            # Type: string
            nginx2_docker_userns_mode:
            ```

        ??? variable string "`nginx2_docker_uts`"

            ```yaml
            # Type: string
            nginx2_docker_uts:
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`nginx_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            nginx_role_autoheal_enabled: true
            ```

        ??? variable string "`nginx_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            nginx_role_depends_on: ""
            ```

        ??? variable string "`nginx_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            nginx_role_depends_on_delay: "0"
            ```

        ??? variable string "`nginx_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            nginx_role_depends_on_healthchecks:
            ```

        ??? variable bool "`nginx_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            nginx_role_diun_enabled: true
            ```

        ??? variable bool "`nginx_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            nginx_role_dns_enabled: true
            ```

        ??? variable bool "`nginx_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            nginx_role_docker_controller: true
            ```

        ??? variable bool "`nginx_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            nginx_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`nginx_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            nginx_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`nginx_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            nginx_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`nginx_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            nginx_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`nginx_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            nginx_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`nginx_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            nginx_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`nginx_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            nginx_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`nginx_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            nginx_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                nginx_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "nginx2.{{ user.domain }}"
                  - "nginx.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`nginx_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            nginx_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                nginx_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'nginx2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`nginx_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            nginx_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `nginx2`):

        ??? variable bool "`nginx2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            nginx2_autoheal_enabled: true
            ```

        ??? variable string "`nginx2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            nginx2_depends_on: ""
            ```

        ??? variable string "`nginx2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            nginx2_depends_on_delay: "0"
            ```

        ??? variable string "`nginx2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            nginx2_depends_on_healthchecks:
            ```

        ??? variable bool "`nginx2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            nginx2_diun_enabled: true
            ```

        ??? variable bool "`nginx2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            nginx2_dns_enabled: true
            ```

        ??? variable bool "`nginx2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            nginx2_docker_controller: true
            ```

        ??? variable bool "`nginx2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            nginx2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`nginx2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            nginx2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`nginx2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            nginx2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`nginx2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            nginx2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`nginx2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            nginx2_traefik_robot_enabled: true
            ```

        ??? variable bool "`nginx2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            nginx2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`nginx2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            nginx2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`nginx2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            nginx2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                nginx2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "nginx2.{{ user.domain }}"
                  - "nginx.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`nginx2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            nginx2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                nginx2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'nginx2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`nginx2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            nginx2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
icon: material/docker
hide:
  - tags
tags:
  - nginx
  - web-server
  - reverse-proxy
---

# Nginx

## Overview

Nginx is a high-performance web server, reverse proxy, and load balancer. This role deploys Nginx using the LinuxServer.io container, providing a simple way to host static websites or act as a reverse proxy for your applications.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://nginx.org/){: .header-icons } | [:octicons-link-16: Docs](https://nginx.org/en/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/nginx/nginx){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/nginx){: .header-icons }|

### 1. Installation

``` shell

sb install nginx

```

### 2. URL

- To access Nginx, visit <https://nginx.iYOUR_DOMAIN_NAMEi>

### 3. Setup

Nginx is deployed using the LinuxServer.io container with configuration files at `/opt/nginx/`. Place website files in `/opt/nginx/www/` and edit site configs in `/opt/nginx/nginx/site-confs/`. Multiple instances are supported via the `nginx_instances` variable in your [Saltbox inventory](../saltbox/inventory/index.md). Restart with `docker restart nginx` to apply changes.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `nginx_instances`.

    ```yaml { .sb-show-on-unchecked title="Applies to all instances of nginx:" }
    nginx_role_web_subdomain: "custom"
    ```

    ```yaml { .sb-show-on-checked title="Applies to a specific instance (e.g., `nginx2`):" }
    nginx2_web_subdomain: "custom2"
    ```

<label class="md-button md-button--stretch" for="sb-checkbox--var-level">
   <input type="checkbox" id="sb-checkbox--var-level"><span class="sb-show-on-unchecked">Show instance-level variables</span><span class="sb-show-on-checked">Show role-level variables</span>
</label>

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `nginx_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `nginx_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`nginx_instances`"

        ```yaml
        # Type: list
        nginx_instances: ["nginx"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            nginx_instances: ["nginx", "nginx2"]
            ```

=== "Paths"

    ??? variable string "`nginx_role_paths_folder`{ .sb-show-on-unchecked }`nginx2_paths_folder`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_paths_folder: "{{ nginx_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_paths_folder: "{{ nginx_name }}"
        ```

    ??? variable string "`nginx_role_paths_location`{ .sb-show-on-unchecked }`nginx2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_paths_location: "{{ server_appdata_path }}/{{ nginx_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_paths_location: "{{ server_appdata_path }}/{{ nginx_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`nginx_role_web_subdomain`{ .sb-show-on-unchecked }`nginx2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_web_subdomain: "{{ nginx_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_web_subdomain: "{{ nginx_name }}"
        ```

    ??? variable string "`nginx_role_web_domain`{ .sb-show-on-unchecked }`nginx2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`nginx_role_web_port`{ .sb-show-on-unchecked }`nginx2_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_web_port: "80"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_web_port: "80"
        ```

    ??? variable string "`nginx_role_web_url`{ .sb-show-on-unchecked }`nginx2_web_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='nginx') + '.' + lookup('role_var', '_web_domain', role='nginx')
                             if (lookup('role_var', '_web_subdomain', role='nginx') | length > 0)
                             else lookup('role_var', '_web_domain', role='nginx')) }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='nginx') + '.' + lookup('role_var', '_web_domain', role='nginx')
                         if (lookup('role_var', '_web_subdomain', role='nginx') | length > 0)
                         else lookup('role_var', '_web_domain', role='nginx')) }}"
        ```

=== "DNS"

    ??? variable string "`nginx_role_dns_record`{ .sb-show-on-unchecked }`nginx2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='nginx') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='nginx') }}"
        ```

    ??? variable string "`nginx_role_dns_zone`{ .sb-show-on-unchecked }`nginx2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='nginx') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_dns_zone: "{{ lookup('role_var', '_web_domain', role='nginx') }}"
        ```

    ??? variable bool "`nginx_role_dns_proxy`{ .sb-show-on-unchecked }`nginx2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        nginx_role_dns_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        nginx2_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`nginx_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`nginx2_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_traefik_sso_middleware: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_traefik_sso_middleware: ""
        ```

    ??? variable string "`nginx_role_traefik_middleware_default`{ .sb-show-on-unchecked }`nginx2_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`nginx_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`nginx2_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_traefik_middleware_custom: ""
        ```

    ??? variable string "`nginx_role_traefik_certresolver`{ .sb-show-on-unchecked }`nginx2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`nginx_role_traefik_enabled`{ .sb-show-on-unchecked }`nginx2_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        nginx_role_traefik_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        nginx2_traefik_enabled: true
        ```

    ??? variable bool "`nginx_role_traefik_api_enabled`{ .sb-show-on-unchecked }`nginx2_traefik_api_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        nginx_role_traefik_api_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        nginx2_traefik_api_enabled: false
        ```

    ??? variable string "`nginx_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`nginx2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_traefik_api_endpoint: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`nginx_role_docker_container`{ .sb-show-on-unchecked }`nginx2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_container: "{{ nginx_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_container: "{{ nginx_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`nginx_role_docker_image_pull`{ .sb-show-on-unchecked }`nginx2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        nginx_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        nginx2_docker_image_pull: true
        ```

    ??? variable string "`nginx_role_docker_image_repo`{ .sb-show-on-unchecked }`nginx2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_image_repo: "lscr.io/linuxserver/nginx"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_image_repo: "lscr.io/linuxserver/nginx"
        ```

    ??? variable string "`nginx_role_docker_image_tag`{ .sb-show-on-unchecked }`nginx2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_image_tag: "latest"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_image_tag: "latest"
        ```

    ??? variable string "`nginx_role_docker_image`{ .sb-show-on-unchecked }`nginx2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='nginx') }}:{{ lookup('role_var', '_docker_image_tag', role='nginx') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='nginx') }}:{{ lookup('role_var', '_docker_image_tag', role='nginx') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`nginx_role_docker_envs_default`{ .sb-show-on-unchecked }`nginx2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        nginx_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        nginx2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`nginx_role_docker_envs_custom`{ .sb-show-on-unchecked }`nginx2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        nginx_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        nginx2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`nginx_role_docker_volumes_default`{ .sb-show-on-unchecked }`nginx2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_volumes_default:
          - "{{ nginx_role_paths_location }}:/config"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_volumes_default: 
          - "{{ nginx_role_paths_location }}:/config"
        ```

    ??? variable list "`nginx_role_docker_volumes_custom`{ .sb-show-on-unchecked }`nginx2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`nginx_role_docker_hostname`{ .sb-show-on-unchecked }`nginx2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_hostname: "{{ nginx_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_hostname: "{{ nginx_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`nginx_role_docker_networks_alias`{ .sb-show-on-unchecked }`nginx2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_networks_alias: "{{ nginx_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_networks_alias: "{{ nginx_name }}"
        ```

    ??? variable list "`nginx_role_docker_networks_default`{ .sb-show-on-unchecked }`nginx2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_networks_default: []
        ```

    ??? variable list "`nginx_role_docker_networks_custom`{ .sb-show-on-unchecked }`nginx2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`nginx_role_docker_restart_policy`{ .sb-show-on-unchecked }`nginx2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`nginx_role_docker_state`{ .sb-show-on-unchecked }`nginx2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    <h5>Resource Limits</h5>

    ??? variable int "`nginx_role_docker_blkio_weight`{ .sb-show-on-unchecked }`nginx2_docker_blkio_weight`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        nginx_role_docker_blkio_weight:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        nginx2_docker_blkio_weight:
        ```

    ??? variable int "`nginx_role_docker_cpu_period`{ .sb-show-on-unchecked }`nginx2_docker_cpu_period`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        nginx_role_docker_cpu_period:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        nginx2_docker_cpu_period:
        ```

    ??? variable int "`nginx_role_docker_cpu_quota`{ .sb-show-on-unchecked }`nginx2_docker_cpu_quota`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        nginx_role_docker_cpu_quota:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        nginx2_docker_cpu_quota:
        ```

    ??? variable int "`nginx_role_docker_cpu_shares`{ .sb-show-on-unchecked }`nginx2_docker_cpu_shares`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        nginx_role_docker_cpu_shares:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        nginx2_docker_cpu_shares:
        ```

    ??? variable string "`nginx_role_docker_cpus`{ .sb-show-on-unchecked }`nginx2_docker_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_cpus:
        ```

    ??? variable string "`nginx_role_docker_cpuset_cpus`{ .sb-show-on-unchecked }`nginx2_docker_cpuset_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_cpuset_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_cpuset_cpus:
        ```

    ??? variable string "`nginx_role_docker_cpuset_mems`{ .sb-show-on-unchecked }`nginx2_docker_cpuset_mems`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_cpuset_mems:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_cpuset_mems:
        ```

    ??? variable string "`nginx_role_docker_kernel_memory`{ .sb-show-on-unchecked }`nginx2_docker_kernel_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_kernel_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_kernel_memory:
        ```

    ??? variable string "`nginx_role_docker_memory`{ .sb-show-on-unchecked }`nginx2_docker_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_memory:
        ```

    ??? variable string "`nginx_role_docker_memory_reservation`{ .sb-show-on-unchecked }`nginx2_docker_memory_reservation`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_memory_reservation:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_memory_reservation:
        ```

    ??? variable string "`nginx_role_docker_memory_swap`{ .sb-show-on-unchecked }`nginx2_docker_memory_swap`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_memory_swap:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_memory_swap:
        ```

    ??? variable int "`nginx_role_docker_memory_swappiness`{ .sb-show-on-unchecked }`nginx2_docker_memory_swappiness`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        nginx_role_docker_memory_swappiness:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        nginx2_docker_memory_swappiness:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`nginx_role_docker_cap_drop`{ .sb-show-on-unchecked }`nginx2_docker_cap_drop`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_cap_drop:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_cap_drop:
        ```

    ??? variable list "`nginx_role_docker_device_cgroup_rules`{ .sb-show-on-unchecked }`nginx2_docker_device_cgroup_rules`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_device_cgroup_rules:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_device_cgroup_rules:
        ```

    ??? variable list "`nginx_role_docker_device_read_bps`{ .sb-show-on-unchecked }`nginx2_docker_device_read_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_device_read_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_device_read_bps:
        ```

    ??? variable list "`nginx_role_docker_device_read_iops`{ .sb-show-on-unchecked }`nginx2_docker_device_read_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_device_read_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_device_read_iops:
        ```

    ??? variable list "`nginx_role_docker_device_requests`{ .sb-show-on-unchecked }`nginx2_docker_device_requests`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_device_requests:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_device_requests:
        ```

    ??? variable list "`nginx_role_docker_device_write_bps`{ .sb-show-on-unchecked }`nginx2_docker_device_write_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_device_write_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_device_write_bps:
        ```

    ??? variable list "`nginx_role_docker_device_write_iops`{ .sb-show-on-unchecked }`nginx2_docker_device_write_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_device_write_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_device_write_iops:
        ```

    ??? variable list "`nginx_role_docker_devices`{ .sb-show-on-unchecked }`nginx2_docker_devices`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_devices:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_devices:
        ```

    ??? variable string "`nginx_role_docker_devices_default`{ .sb-show-on-unchecked }`nginx2_docker_devices_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_devices_default:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_devices_default:
        ```

    ??? variable bool "`nginx_role_docker_privileged`{ .sb-show-on-unchecked }`nginx2_docker_privileged`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        nginx_role_docker_privileged:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        nginx2_docker_privileged:
        ```

    ??? variable list "`nginx_role_docker_security_opts`{ .sb-show-on-unchecked }`nginx2_docker_security_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_security_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_security_opts:
        ```

    <h5>Networking</h5>

    ??? variable list "`nginx_role_docker_dns_opts`{ .sb-show-on-unchecked }`nginx2_docker_dns_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_dns_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_dns_opts:
        ```

    ??? variable list "`nginx_role_docker_dns_search_domains`{ .sb-show-on-unchecked }`nginx2_docker_dns_search_domains`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_dns_search_domains:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_dns_search_domains:
        ```

    ??? variable list "`nginx_role_docker_dns_servers`{ .sb-show-on-unchecked }`nginx2_docker_dns_servers`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_dns_servers:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_dns_servers:
        ```

    ??? variable dict "`nginx_role_docker_hosts`{ .sb-show-on-unchecked }`nginx2_docker_hosts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        nginx_role_docker_hosts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        nginx2_docker_hosts:
        ```

    ??? variable string "`nginx_role_docker_hosts_use_common`{ .sb-show-on-unchecked }`nginx2_docker_hosts_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_hosts_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_hosts_use_common:
        ```

    ??? variable string "`nginx_role_docker_network_mode`{ .sb-show-on-unchecked }`nginx2_docker_network_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_network_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_network_mode:
        ```

    <h5>Storage</h5>

    ??? variable bool "`nginx_role_docker_keep_volumes`{ .sb-show-on-unchecked }`nginx2_docker_keep_volumes`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        nginx_role_docker_keep_volumes:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        nginx2_docker_keep_volumes:
        ```

    ??? variable list "`nginx_role_docker_mounts`{ .sb-show-on-unchecked }`nginx2_docker_mounts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_mounts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_mounts:
        ```

    ??? variable string "`nginx_role_docker_volume_driver`{ .sb-show-on-unchecked }`nginx2_docker_volume_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_volume_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_volume_driver:
        ```

    ??? variable list "`nginx_role_docker_volumes_from`{ .sb-show-on-unchecked }`nginx2_docker_volumes_from`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_volumes_from:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_volumes_from:
        ```

    ??? variable string "`nginx_role_docker_volumes_global`{ .sb-show-on-unchecked }`nginx2_docker_volumes_global`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_volumes_global:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_volumes_global:
        ```

    ??? variable string "`nginx_role_docker_working_dir`{ .sb-show-on-unchecked }`nginx2_docker_working_dir`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_working_dir:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable dict "`nginx_role_docker_healthcheck`{ .sb-show-on-unchecked }`nginx2_docker_healthcheck`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        nginx_role_docker_healthcheck:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        nginx2_docker_healthcheck:
        ```

    ??? variable bool "`nginx_role_docker_init`{ .sb-show-on-unchecked }`nginx2_docker_init`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        nginx_role_docker_init:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        nginx2_docker_init:
        ```

    ??? variable string "`nginx_role_docker_log_driver`{ .sb-show-on-unchecked }`nginx2_docker_log_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_log_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_log_driver:
        ```

    ??? variable dict "`nginx_role_docker_log_options`{ .sb-show-on-unchecked }`nginx2_docker_log_options`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        nginx_role_docker_log_options:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        nginx2_docker_log_options:
        ```

    ??? variable bool "`nginx_role_docker_output_logs`{ .sb-show-on-unchecked }`nginx2_docker_output_logs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        nginx_role_docker_output_logs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        nginx2_docker_output_logs:
        ```

    <h5>Other Options</h5>

    ??? variable bool "`nginx_role_docker_auto_remove`{ .sb-show-on-unchecked }`nginx2_docker_auto_remove`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        nginx_role_docker_auto_remove:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        nginx2_docker_auto_remove:
        ```

    ??? variable list "`nginx_role_docker_capabilities`{ .sb-show-on-unchecked }`nginx2_docker_capabilities`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_capabilities:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_capabilities:
        ```

    ??? variable string "`nginx_role_docker_cgroup_parent`{ .sb-show-on-unchecked }`nginx2_docker_cgroup_parent`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_cgroup_parent:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_cgroup_parent:
        ```

    ??? variable string "`nginx_role_docker_cgroupns_mode`{ .sb-show-on-unchecked }`nginx2_docker_cgroupns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_cgroupns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_cgroupns_mode:
        ```

    ??? variable bool "`nginx_role_docker_cleanup`{ .sb-show-on-unchecked }`nginx2_docker_cleanup`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        nginx_role_docker_cleanup:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        nginx2_docker_cleanup:
        ```

    ??? variable list "`nginx_role_docker_commands`{ .sb-show-on-unchecked }`nginx2_docker_commands`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_commands:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_commands:
        ```

    ??? variable string "`nginx_role_docker_create_timeout`{ .sb-show-on-unchecked }`nginx2_docker_create_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_create_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_create_timeout:
        ```

    ??? variable string "`nginx_role_docker_domainname`{ .sb-show-on-unchecked }`nginx2_docker_domainname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_domainname:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_domainname:
        ```

    ??? variable string "`nginx_role_docker_entrypoint`{ .sb-show-on-unchecked }`nginx2_docker_entrypoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_entrypoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_entrypoint:
        ```

    ??? variable string "`nginx_role_docker_env_file`{ .sb-show-on-unchecked }`nginx2_docker_env_file`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_env_file:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_env_file:
        ```

    ??? variable list "`nginx_role_docker_exposed_ports`{ .sb-show-on-unchecked }`nginx2_docker_exposed_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_exposed_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_exposed_ports:
        ```

    ??? variable string "`nginx_role_docker_force_kill`{ .sb-show-on-unchecked }`nginx2_docker_force_kill`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_force_kill:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_force_kill:
        ```

    ??? variable list "`nginx_role_docker_groups`{ .sb-show-on-unchecked }`nginx2_docker_groups`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_groups:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_groups:
        ```

    ??? variable int "`nginx_role_docker_healthy_wait_timeout`{ .sb-show-on-unchecked }`nginx2_docker_healthy_wait_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        nginx_role_docker_healthy_wait_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        nginx2_docker_healthy_wait_timeout:
        ```

    ??? variable string "`nginx_role_docker_ipc_mode`{ .sb-show-on-unchecked }`nginx2_docker_ipc_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_ipc_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_ipc_mode:
        ```

    ??? variable string "`nginx_role_docker_kill_signal`{ .sb-show-on-unchecked }`nginx2_docker_kill_signal`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_kill_signal:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_kill_signal:
        ```

    ??? variable dict "`nginx_role_docker_labels`{ .sb-show-on-unchecked }`nginx2_docker_labels`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        nginx_role_docker_labels:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        nginx2_docker_labels:
        ```

    ??? variable string "`nginx_role_docker_labels_use_common`{ .sb-show-on-unchecked }`nginx2_docker_labels_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_labels_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_labels_use_common:
        ```

    ??? variable list "`nginx_role_docker_links`{ .sb-show-on-unchecked }`nginx2_docker_links`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_links:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_links:
        ```

    ??? variable bool "`nginx_role_docker_oom_killer`{ .sb-show-on-unchecked }`nginx2_docker_oom_killer`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        nginx_role_docker_oom_killer:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        nginx2_docker_oom_killer:
        ```

    ??? variable int "`nginx_role_docker_oom_score_adj`{ .sb-show-on-unchecked }`nginx2_docker_oom_score_adj`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        nginx_role_docker_oom_score_adj:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        nginx2_docker_oom_score_adj:
        ```

    ??? variable bool "`nginx_role_docker_paused`{ .sb-show-on-unchecked }`nginx2_docker_paused`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        nginx_role_docker_paused:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        nginx2_docker_paused:
        ```

    ??? variable string "`nginx_role_docker_pid_mode`{ .sb-show-on-unchecked }`nginx2_docker_pid_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_pid_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_pid_mode:
        ```

    ??? variable list "`nginx_role_docker_ports`{ .sb-show-on-unchecked }`nginx2_docker_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_ports:
        ```

    ??? variable bool "`nginx_role_docker_read_only`{ .sb-show-on-unchecked }`nginx2_docker_read_only`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        nginx_role_docker_read_only:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        nginx2_docker_read_only:
        ```

    ??? variable bool "`nginx_role_docker_recreate`{ .sb-show-on-unchecked }`nginx2_docker_recreate`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        nginx_role_docker_recreate:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        nginx2_docker_recreate:
        ```

    ??? variable int "`nginx_role_docker_restart_retries`{ .sb-show-on-unchecked }`nginx2_docker_restart_retries`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        nginx_role_docker_restart_retries:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        nginx2_docker_restart_retries:
        ```

    ??? variable string "`nginx_role_docker_runtime`{ .sb-show-on-unchecked }`nginx2_docker_runtime`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_runtime:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_runtime:
        ```

    ??? variable string "`nginx_role_docker_shm_size`{ .sb-show-on-unchecked }`nginx2_docker_shm_size`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_shm_size:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_shm_size:
        ```

    ??? variable int "`nginx_role_docker_stop_timeout`{ .sb-show-on-unchecked }`nginx2_docker_stop_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        nginx_role_docker_stop_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        nginx2_docker_stop_timeout:
        ```

    ??? variable dict "`nginx_role_docker_storage_opts`{ .sb-show-on-unchecked }`nginx2_docker_storage_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        nginx_role_docker_storage_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        nginx2_docker_storage_opts:
        ```

    ??? variable list "`nginx_role_docker_sysctls`{ .sb-show-on-unchecked }`nginx2_docker_sysctls`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_sysctls:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_sysctls:
        ```

    ??? variable list "`nginx_role_docker_tmpfs`{ .sb-show-on-unchecked }`nginx2_docker_tmpfs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_tmpfs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_tmpfs:
        ```

    ??? variable list "`nginx_role_docker_ulimits`{ .sb-show-on-unchecked }`nginx2_docker_ulimits`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        nginx_role_docker_ulimits:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        nginx2_docker_ulimits:
        ```

    ??? variable string "`nginx_role_docker_user`{ .sb-show-on-unchecked }`nginx2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_user:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_user:
        ```

    ??? variable string "`nginx_role_docker_userns_mode`{ .sb-show-on-unchecked }`nginx2_docker_userns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_userns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_userns_mode:
        ```

    ??? variable string "`nginx_role_docker_uts`{ .sb-show-on-unchecked }`nginx2_docker_uts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        nginx_role_docker_uts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        nginx2_docker_uts:
        ```

=== "Global Override Options"

    ??? variable bool "`nginx_role_autoheal_enabled`{ .sb-show-on-unchecked }`nginx2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        nginx_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        nginx2_autoheal_enabled: true
        ```

    ??? variable string "`nginx_role_depends_on`{ .sb-show-on-unchecked }`nginx2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        nginx_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        nginx2_depends_on: ""
        ```

    ??? variable string "`nginx_role_depends_on_delay`{ .sb-show-on-unchecked }`nginx2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        nginx_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        nginx2_depends_on_delay: "0"
        ```

    ??? variable string "`nginx_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`nginx2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        nginx_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        nginx2_depends_on_healthchecks:
        ```

    ??? variable bool "`nginx_role_diun_enabled`{ .sb-show-on-unchecked }`nginx2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        nginx_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        nginx2_diun_enabled: true
        ```

    ??? variable bool "`nginx_role_dns_enabled`{ .sb-show-on-unchecked }`nginx2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        nginx_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        nginx2_dns_enabled: true
        ```

    ??? variable bool "`nginx_role_docker_controller`{ .sb-show-on-unchecked }`nginx2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        nginx_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        nginx2_docker_controller: true
        ```

    ??? variable bool "`nginx_role_docker_volumes_download`{ .sb-show-on-unchecked }`nginx2_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        nginx_role_docker_volumes_download:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        nginx2_docker_volumes_download:
        ```

    ??? variable bool "`nginx_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`nginx2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        nginx_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        nginx2_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`nginx_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`nginx2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        nginx_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        nginx2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`nginx_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`nginx2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        nginx_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        nginx2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`nginx_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`nginx2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        nginx_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        nginx2_traefik_gzip_enabled: false
        ```

    ??? variable bool "`nginx_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`nginx2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        nginx_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        nginx2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`nginx_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`nginx2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        nginx_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        nginx2_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`nginx_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`nginx2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        nginx_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        nginx2_traefik_robot_enabled: true
        ```

    ??? variable bool "`nginx_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`nginx2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        nginx_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        nginx2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`nginx_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`nginx2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        nginx_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        nginx2_traefik_wildcard_enabled: true
        ```

    ??? variable list "`nginx_role_web_fqdn_override`{ .sb-show-on-unchecked }`nginx2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        nginx_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        nginx2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            nginx_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "nginx2.{{ user.domain }}"
              - "nginx.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            nginx2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "nginx2.{{ user.domain }}"
              - "nginx.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`nginx_role_web_host_override`{ .sb-show-on-unchecked }`nginx2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        nginx_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        nginx2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            nginx_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'nginx2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            nginx2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'nginx2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`nginx_role_web_scheme`{ .sb-show-on-unchecked }`nginx2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        nginx_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        nginx2_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
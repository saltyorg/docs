---
icon: material/docker
hide:
  - tags
tags:
  - crafty
  - minecraft
  - gaming
---

# Crafty Controller

## Overview

[Crafty Controller](https://craftycontrol.com/) is a cross-platform Minecraft server control panel with web-based interface. It features server scheduling, interactive console, and support for multiple server types including vanilla, modded, and plugin-based servers.

!!! info
    By default, the role is **NOT** protected behind your Authelia/SSO middleware. You will need to configure authentication within the application.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://craftycontrol.com/){: .header-icons } | [:octicons-mark-github-16: GitLab](https://gitlab.com/crafty-controller/crafty-4){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/arcadiatechnology/crafty-4){: .header-icons }|

### 1. Installation

```shell
sb install sandbox-crafty
```

### 2. URL

- To access Crafty Controller, visit <https://crafty.iYOUR_DOMAIN_NAMEi>

### 3. Setup

Default credentials are generated on first run and stored in `default-creds.txt` in your app data folder.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    crafty_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `crafty_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `crafty_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`crafty_name`"

        ```yaml
        # Type: string
        crafty_name: crafty
        ```

=== "Paths"

    ??? variable string "`crafty_role_paths_folder`"

        ```yaml
        # Type: string
        crafty_role_paths_folder: "{{ crafty_name }}"
        ```

    ??? variable string "`crafty_role_paths_group`"

        ```yaml
        # Type: string
        crafty_role_paths_group: "root"
        ```

    ??? variable string "`crafty_role_paths_location`"

        ```yaml
        # Type: string
        crafty_role_paths_location: "{{ server_appdata_path }}/{{ crafty_role_paths_folder }}"
        ```

    ??? variable bool "`crafty_role_paths_recurse`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_paths_recurse: true
        ```

=== "Web"

    ??? variable string "`crafty_role_web_subdomain`"

        ```yaml
        # Type: string
        crafty_role_web_subdomain: "{{ crafty_name }}"
        ```

    ??? variable string "`crafty_role_web_domain`"

        ```yaml
        # Type: string
        crafty_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`crafty_role_web_port`"

        ```yaml
        # Type: string
        crafty_role_web_port: "8443"
        ```

    ??? variable string "`crafty_role_web_scheme`"

        ```yaml
        # Type: string
        crafty_role_web_scheme: "https"
        ```

    ??? variable string "`crafty_role_web_serverstransport`"

        ```yaml
        # Type: string
        crafty_role_web_serverstransport: "skipverify@file"
        ```

    ??? variable string "`crafty_role_web_url`"

        ```yaml
        # Type: string
        crafty_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='crafty') + '.' + lookup('role_var', '_web_domain', role='crafty')
                              if (lookup('role_var', '_web_subdomain', role='crafty') | length > 0)
                              else lookup('role_var', '_web_domain', role='crafty')) }}"
        ```

    ??? variable string "`crafty_role_dynmap_web_subdomain`"

        ```yaml
        # Type: string
        crafty_role_dynmap_web_subdomain: "{{ crafty_name }}-map"
        ```

    ??? variable string "`crafty_role_dynmap_web_domain`"

        ```yaml
        # Type: string
        crafty_role_dynmap_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`crafty_role_dynmap_web_port`"

        ```yaml
        # Type: string
        crafty_role_dynmap_web_port: "8123"
        ```

    ??? variable string "`crafty_role_dynmap_host`"

        ```yaml
        # Type: string
        crafty_role_dynmap_host: "{{ lookup('role_var', '_dynmap_web_subdomain', role='crafty')
                                     + '.' + lookup('role_var', '_dynmap_web_domain', role='crafty') }}"
        ```

=== "DNS"

    ??? variable string "`crafty_role_dns_record`"

        ```yaml
        # Type: string
        crafty_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='crafty') }}"
        ```

    ??? variable string "`crafty_role_dns_zone`"

        ```yaml
        # Type: string
        crafty_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='crafty') }}"
        ```

    ??? variable bool "`crafty_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_dns_proxy: "{{ dns_proxied }}"
        ```

    ??? variable string "`crafty_role_dynmap_dns_record`"

        ```yaml
        # Type: string
        crafty_role_dynmap_dns_record: "{{ lookup('role_var', '_dynmap_web_subdomain', role='crafty') }}"
        ```

    ??? variable string "`crafty_role_dynmap_dns_zone`"

        ```yaml
        # Type: string
        crafty_role_dynmap_dns_zone: "{{ lookup('role_var', '_web_domain', role='crafty') }}"
        ```

    ??? variable bool "`crafty_role_dynmap_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_dynmap_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`crafty_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        crafty_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`crafty_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        crafty_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`crafty_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        crafty_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`crafty_role_traefik_certresolver`"

        ```yaml
        # Type: string
        crafty_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`crafty_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_traefik_enabled: true
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`crafty_role_docker_container`"

        ```yaml
        # Type: string
        crafty_role_docker_container: "{{ crafty_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`crafty_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_docker_image_pull: true
        ```

    ??? variable string "`crafty_role_docker_image_repo`"

        ```yaml
        # Type: string
        crafty_role_docker_image_repo: "arcadiatechnology/crafty-4"
        ```

    ??? variable string "`crafty_role_docker_image_tag`"

        ```yaml
        # Type: string
        crafty_role_docker_image_tag: "latest"
        ```

    ??? variable string "`crafty_role_docker_image`"

        ```yaml
        # Type: string
        crafty_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='crafty') }}:{{ lookup('role_var', '_docker_image_tag', role='crafty') }}"
        ```

    <h5>Ports</h5>

    ??? variable list "`crafty_role_docker_ports_default`"

        ```yaml
        # Type: list
        crafty_role_docker_ports_default:
          - "19132:19132/udp"
          - "25500-25600:25500-25600"
        ```

    ??? variable list "`crafty_role_docker_ports_custom`"

        ```yaml
        # Type: list
        crafty_role_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    ??? variable dict "`crafty_role_docker_envs_default`"

        ```yaml
        # Type: dict
        crafty_role_docker_envs_default:
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`crafty_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        crafty_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`crafty_role_docker_volumes_default`"

        ```yaml
        # Type: list
        crafty_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='crafty') }}/backups:/crafty/backups"
          - "{{ lookup('role_var', '_paths_location', role='crafty') }}/logs:/crafty/logs"
          - "{{ lookup('role_var', '_paths_location', role='crafty') }}/servers:/crafty/servers"
          - "{{ lookup('role_var', '_paths_location', role='crafty') }}/config:/crafty/app/config"
          - "{{ lookup('role_var', '_paths_location', role='crafty') }}/import:/crafty/import"
        ```

    ??? variable list "`crafty_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        crafty_role_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable list "`crafty_role_docker_labels_default`"

        ```yaml
        # Type: list
        crafty_role_docker_labels_default:
          - '{ "traefik.http.routers.{{ crafty_name }}-map-http.entrypoints": "web" }'
          - '{ "traefik.http.routers.{{ crafty_name }}-map-http.service": "{{ crafty_name }}-map" }'
          - '{ "traefik.http.routers.{{ crafty_name }}-map-http.rule": "Host(`{{ lookup("role_var", "_dynmap_host", role="crafty") }}`)" }'
          - '{ "traefik.http.routers.{{ crafty_name }}-map-http.middlewares": "{{ traefik_default_middleware_http }}" }'
          - '{ "traefik.http.routers.{{ crafty_name }}-map-http.priority": "20" }'
          - '{ "traefik.http.routers.{{ crafty_name }}-map.entrypoints": "websecure" }'
          - '{ "traefik.http.routers.{{ crafty_name }}-map.service": "{{ crafty_name }}-map" }'
          - '{ "traefik.http.routers.{{ crafty_name }}-map.rule": "Host(`{{ lookup("role_var", "_dynmap_host", role="crafty") }}`)" }'
          - '{ "traefik.http.routers.{{ crafty_name }}-map.tls.options": "securetls@file" }'
          - '{ "traefik.http.routers.{{ crafty_name }}-map.tls.certresolver": "{{ lookup("role_var", "_traefik_certresolver", role="crafty") }}" }'
          - '{ "traefik.http.routers.{{ crafty_name }}-map.middlewares": "{{ traefik_default_middleware }}" }'
          - '{ "traefik.http.routers.{{ crafty_name }}-map.priority": "20" }'
          - '{ "traefik.http.services.{{ crafty_name }}-map.loadbalancer.server.port": "{{ lookup("role_var", "_dynmap_web_port", role="crafty") }}" }'
        ```

    ??? variable dict "`crafty_role_docker_labels_custom`"

        ```yaml
        # Type: dict
        crafty_role_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`crafty_role_docker_hostname`"

        ```yaml
        # Type: string
        crafty_role_docker_hostname: "{{ crafty_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`crafty_role_docker_networks_alias`"

        ```yaml
        # Type: string
        crafty_role_docker_networks_alias: "{{ crafty_name }}"
        ```

    ??? variable list "`crafty_role_docker_networks_default`"

        ```yaml
        # Type: list
        crafty_role_docker_networks_default: []
        ```

    ??? variable list "`crafty_role_docker_networks_custom`"

        ```yaml
        # Type: list
        crafty_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`crafty_role_docker_restart_policy`"

        ```yaml
        # Type: string
        crafty_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`crafty_role_docker_state`"

        ```yaml
        # Type: string
        crafty_role_docker_state: started
        ```

    <h5>Stop Timeout</h5>

    ??? variable int "`crafty_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        crafty_role_docker_stop_timeout: 900
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`crafty_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        crafty_role_docker_blkio_weight:
        ```

    ??? variable int "`crafty_role_docker_cpu_period`"

        ```yaml
        # Type: int
        crafty_role_docker_cpu_period:
        ```

    ??? variable int "`crafty_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        crafty_role_docker_cpu_quota:
        ```

    ??? variable int "`crafty_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        crafty_role_docker_cpu_shares:
        ```

    ??? variable string "`crafty_role_docker_cpus`"

        ```yaml
        # Type: string
        crafty_role_docker_cpus:
        ```

    ??? variable string "`crafty_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        crafty_role_docker_cpuset_cpus:
        ```

    ??? variable string "`crafty_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        crafty_role_docker_cpuset_mems:
        ```

    ??? variable string "`crafty_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        crafty_role_docker_kernel_memory:
        ```

    ??? variable string "`crafty_role_docker_memory`"

        ```yaml
        # Type: string
        crafty_role_docker_memory:
        ```

    ??? variable string "`crafty_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        crafty_role_docker_memory_reservation:
        ```

    ??? variable string "`crafty_role_docker_memory_swap`"

        ```yaml
        # Type: string
        crafty_role_docker_memory_swap:
        ```

    ??? variable int "`crafty_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        crafty_role_docker_memory_swappiness:
        ```

    ??? variable string "`crafty_role_docker_shm_size`"

        ```yaml
        # Type: string
        crafty_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`crafty_role_docker_cap_drop`"

        ```yaml
        # Type: list
        crafty_role_docker_cap_drop:
        ```

    ??? variable string "`crafty_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        crafty_role_docker_cgroupns_mode:
        ```

    ??? variable list "`crafty_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        crafty_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`crafty_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        crafty_role_docker_device_read_bps:
        ```

    ??? variable list "`crafty_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        crafty_role_docker_device_read_iops:
        ```

    ??? variable list "`crafty_role_docker_device_requests`"

        ```yaml
        # Type: list
        crafty_role_docker_device_requests:
        ```

    ??? variable list "`crafty_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        crafty_role_docker_device_write_bps:
        ```

    ??? variable list "`crafty_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        crafty_role_docker_device_write_iops:
        ```

    ??? variable list "`crafty_role_docker_devices`"

        ```yaml
        # Type: list
        crafty_role_docker_devices:
        ```

    ??? variable string "`crafty_role_docker_devices_default`"

        ```yaml
        # Type: string
        crafty_role_docker_devices_default:
        ```

    ??? variable list "`crafty_role_docker_groups`"

        ```yaml
        # Type: list
        crafty_role_docker_groups:
        ```

    ??? variable bool "`crafty_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_docker_privileged:
        ```

    ??? variable list "`crafty_role_docker_security_opts`"

        ```yaml
        # Type: list
        crafty_role_docker_security_opts:
        ```

    ??? variable string "`crafty_role_docker_user`"

        ```yaml
        # Type: string
        crafty_role_docker_user:
        ```

    ??? variable string "`crafty_role_docker_userns_mode`"

        ```yaml
        # Type: string
        crafty_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`crafty_role_docker_dns_opts`"

        ```yaml
        # Type: list
        crafty_role_docker_dns_opts:
        ```

    ??? variable list "`crafty_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        crafty_role_docker_dns_search_domains:
        ```

    ??? variable list "`crafty_role_docker_dns_servers`"

        ```yaml
        # Type: list
        crafty_role_docker_dns_servers:
        ```

    ??? variable string "`crafty_role_docker_domainname`"

        ```yaml
        # Type: string
        crafty_role_docker_domainname:
        ```

    ??? variable list "`crafty_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        crafty_role_docker_exposed_ports:
        ```

    ??? variable dict "`crafty_role_docker_hosts`"

        ```yaml
        # Type: dict
        crafty_role_docker_hosts:
        ```

    ??? variable bool "`crafty_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_docker_hosts_use_common:
        ```

    ??? variable string "`crafty_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        crafty_role_docker_ipc_mode:
        ```

    ??? variable list "`crafty_role_docker_links`"

        ```yaml
        # Type: list
        crafty_role_docker_links:
        ```

    ??? variable string "`crafty_role_docker_network_mode`"

        ```yaml
        # Type: string
        crafty_role_docker_network_mode:
        ```

    ??? variable string "`crafty_role_docker_pid_mode`"

        ```yaml
        # Type: string
        crafty_role_docker_pid_mode:
        ```

    ??? variable string "`crafty_role_docker_uts`"

        ```yaml
        # Type: string
        crafty_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`crafty_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_docker_keep_volumes:
        ```

    ??? variable list "`crafty_role_docker_mounts`"

        ```yaml
        # Type: list
        crafty_role_docker_mounts:
        ```

    ??? variable dict "`crafty_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        crafty_role_docker_storage_opts:
        ```

    ??? variable list "`crafty_role_docker_tmpfs`"

        ```yaml
        # Type: list
        crafty_role_docker_tmpfs:
        ```

    ??? variable string "`crafty_role_docker_volume_driver`"

        ```yaml
        # Type: string
        crafty_role_docker_volume_driver:
        ```

    ??? variable list "`crafty_role_docker_volumes_from`"

        ```yaml
        # Type: list
        crafty_role_docker_volumes_from:
        ```

    ??? variable bool "`crafty_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_docker_volumes_global:
        ```

    ??? variable string "`crafty_role_docker_working_dir`"

        ```yaml
        # Type: string
        crafty_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`crafty_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_docker_auto_remove:
        ```

    ??? variable bool "`crafty_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_docker_cleanup:
        ```

    ??? variable string "`crafty_role_docker_force_kill`"

        ```yaml
        # Type: string
        crafty_role_docker_force_kill:
        ```

    ??? variable dict "`crafty_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        crafty_role_docker_healthcheck:
        ```

    ??? variable int "`crafty_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        crafty_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`crafty_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_docker_init:
        ```

    ??? variable string "`crafty_role_docker_kill_signal`"

        ```yaml
        # Type: string
        crafty_role_docker_kill_signal:
        ```

    ??? variable string "`crafty_role_docker_log_driver`"

        ```yaml
        # Type: string
        crafty_role_docker_log_driver:
        ```

    ??? variable dict "`crafty_role_docker_log_options`"

        ```yaml
        # Type: dict
        crafty_role_docker_log_options:
        ```

    ??? variable bool "`crafty_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_docker_oom_killer:
        ```

    ??? variable int "`crafty_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        crafty_role_docker_oom_score_adj:
        ```

    ??? variable bool "`crafty_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_docker_output_logs:
        ```

    ??? variable bool "`crafty_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_docker_paused:
        ```

    ??? variable bool "`crafty_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_docker_recreate:
        ```

    ??? variable int "`crafty_role_docker_restart_retries`"

        ```yaml
        # Type: int
        crafty_role_docker_restart_retries:
        ```

    <h5>Other Options</h5>

    ??? variable list "`crafty_role_docker_capabilities`"

        ```yaml
        # Type: list
        crafty_role_docker_capabilities:
        ```

    ??? variable string "`crafty_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        crafty_role_docker_cgroup_parent:
        ```

    ??? variable list "`crafty_role_docker_commands`"

        ```yaml
        # Type: list
        crafty_role_docker_commands:
        ```

    ??? variable int "`crafty_role_docker_create_timeout`"

        ```yaml
        # Type: int
        crafty_role_docker_create_timeout:
        ```

    ??? variable string "`crafty_role_docker_entrypoint`"

        ```yaml
        # Type: string
        crafty_role_docker_entrypoint:
        ```

    ??? variable string "`crafty_role_docker_env_file`"

        ```yaml
        # Type: string
        crafty_role_docker_env_file:
        ```

    ??? variable bool "`crafty_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_docker_labels_use_common:
        ```

    ??? variable bool "`crafty_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_docker_read_only:
        ```

    ??? variable string "`crafty_role_docker_runtime`"

        ```yaml
        # Type: string
        crafty_role_docker_runtime:
        ```

    ??? variable list "`crafty_role_docker_sysctls`"

        ```yaml
        # Type: list
        crafty_role_docker_sysctls:
        ```

    ??? variable list "`crafty_role_docker_ulimits`"

        ```yaml
        # Type: list
        crafty_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`crafty_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        crafty_role_autoheal_enabled: true
        ```

    ??? variable string "`crafty_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        crafty_role_depends_on: ""
        ```

    ??? variable string "`crafty_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        crafty_role_depends_on_delay: "0"
        ```

    ??? variable string "`crafty_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        crafty_role_depends_on_healthchecks:
        ```

    ??? variable bool "`crafty_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        crafty_role_diun_enabled: true
        ```

    ??? variable bool "`crafty_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        crafty_role_dns_enabled: true
        ```

    ??? variable bool "`crafty_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        crafty_role_docker_controller: true
        ```

    ??? variable string "`crafty_role_docker_image_repo`"

        ```yaml
        # Type: string
        crafty_role_docker_image_repo:
        ```

    ??? variable string "`crafty_role_docker_image_tag`"

        ```yaml
        # Type: string
        crafty_role_docker_image_tag:
        ```

    ??? variable bool "`crafty_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_docker_volumes_download:
        ```

    ??? variable string "`crafty_role_dynmap_host`"

        ```yaml
        # Type: string
        crafty_role_dynmap_host:
        ```

    ??? variable string "`crafty_role_dynmap_web_domain`"

        ```yaml
        # Type: string
        crafty_role_dynmap_web_domain:
        ```

    ??? variable string "`crafty_role_dynmap_web_port`"

        ```yaml
        # Type: string (quoted number)
        crafty_role_dynmap_web_port:
        ```

    ??? variable string "`crafty_role_dynmap_web_subdomain`"

        ```yaml
        # Type: string
        crafty_role_dynmap_web_subdomain:
        ```

    ??? variable string "`crafty_role_paths_location`"

        ```yaml
        # Type: string
        crafty_role_paths_location:
        ```

    ??? variable string "`crafty_role_themepark_addons`"

        ```yaml
        # Type: string
        crafty_role_themepark_addons:
        ```

    ??? variable string "`crafty_role_themepark_app`"

        ```yaml
        # Type: string
        crafty_role_themepark_app:
        ```

    ??? variable string "`crafty_role_themepark_theme`"

        ```yaml
        # Type: string
        crafty_role_themepark_theme:
        ```

    ??? variable dict/omit "`crafty_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        crafty_role_traefik_api_endpoint:
        ```

    ??? variable string "`crafty_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        crafty_role_traefik_api_middleware:
        ```

    ??? variable string "`crafty_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        crafty_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`crafty_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        crafty_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`crafty_role_traefik_certresolver`"

        ```yaml
        # Type: string
        crafty_role_traefik_certresolver:
        ```

    ??? variable bool "`crafty_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        crafty_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`crafty_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        crafty_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`crafty_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        crafty_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`crafty_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        crafty_role_traefik_middleware_http:
        ```

    ??? variable bool "`crafty_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`crafty_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        crafty_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`crafty_role_traefik_priority`"

        ```yaml
        # Type: string
        crafty_role_traefik_priority:
        ```

    ??? variable bool "`crafty_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        crafty_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`crafty_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        crafty_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`crafty_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        crafty_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`crafty_role_web_domain`"

        ```yaml
        # Type: string
        crafty_role_web_domain:
        ```

    ??? variable list "`crafty_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        crafty_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            crafty_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "crafty2.{{ user.domain }}"
              - "crafty.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`crafty_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        crafty_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            crafty_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'crafty2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`crafty_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        crafty_role_web_http_port:
        ```

    ??? variable string "`crafty_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        crafty_role_web_http_scheme:
        ```

    ??? variable dict/omit "`crafty_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        crafty_role_web_http_serverstransport:
        ```

    ??? variable string "`crafty_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        crafty_role_web_scheme:
        ```

    ??? variable dict/omit "`crafty_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        crafty_role_web_serverstransport:
        ```

    ??? variable string "`crafty_role_web_subdomain`"

        ```yaml
        # Type: string
        crafty_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
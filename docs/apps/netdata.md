---
hide:
  - tags
tags:
  - netdata
---

# Netdata

## Overview

[Netdata](https://github.com/netdata/netdata/) is distributed, real-time, performance and health monitoring for systems and applications.

Netdata provides insights, in real-time, of everything happening on the systems it runs (including web servers, databases, applications), using highly interactive web dashboards. It can run autonomously, without any third party components, or it can be integrated to existing monitoring toolchains (Prometheus, Graphite, OpenTSDB, Kafka, Grafana, etc).

Netdata is designed to permanently run on all systems (physical & virtual servers, containers, IoT devices), without disrupting their core function.

Netdata is free, open-source software.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/netdata/netdata/){: .header-icons } | [:octicons-link-16: Docs](https://learn.netdata.cloud/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/netdata/netdata/){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/netdata/netdata/){: .header-icons }|

### 1. Installation

``` shell

sb install netdata

```

### 2. URL

- To access Netdata, visit <https://netdata.iYOUR_DOMAIN_NAMEi>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    netdata_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `netdata_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `netdata_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`netdata_name`"

        ```yaml
        # Type: string
        netdata_name: netdata
        ```

=== "Settings"

    ??? variable string "`netdata_role_claim_token`"

        ```yaml
        # Type: string
        netdata_role_claim_token: ""
        ```

    ??? variable string "`netdata_role_claim_url`"

        ```yaml
        # Type: string
        netdata_role_claim_url: ""
        ```

    ??? variable string "`netdata_role_claim_room`"

        ```yaml
        # Type: string
        netdata_role_claim_room: ""
        ```

=== "Docker Socket Proxy"

    ??? variable dict "`netdata_role_docker_socket_proxy_envs`"

        ```yaml
        # Type: dict
        netdata_role_docker_socket_proxy_envs: 
          CONTAINERS: "1"
        ```

=== "Paths"

    ??? variable string "`netdata_role_paths_folder`"

        ```yaml
        # Type: string
        netdata_role_paths_folder: "{{ netdata_name }}"
        ```

    ??? variable string "`netdata_role_paths_location`"

        ```yaml
        # Type: string
        netdata_role_paths_location: "{{ server_appdata_path }}/{{ netdata_role_paths_folder }}"
        ```

    ??? variable string "`netdata_role_paths_config_location`"

        ```yaml
        # Type: string
        netdata_role_paths_config_location: "{{ netdata_role_paths_location }}/config"
        ```

    ??? variable string "`netdata_role_paths_config_file_location`"

        ```yaml
        # Type: string
        netdata_role_paths_config_file_location: "{{ netdata_role_paths_location }}/config/netdata.conf"
        ```

=== "Web"

    ??? variable string "`netdata_role_web_subdomain`"

        ```yaml
        # Type: string
        netdata_role_web_subdomain: "{{ netdata_name }}"
        ```

    ??? variable string "`netdata_role_web_domain`"

        ```yaml
        # Type: string
        netdata_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`netdata_role_web_port`"

        ```yaml
        # Type: string
        netdata_role_web_port: "19999"
        ```

    ??? variable string "`netdata_role_web_url`"

        ```yaml
        # Type: string
        netdata_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='netdata') + '.' + lookup('role_var', '_web_domain', role='netdata')
                               if (lookup('role_var', '_web_subdomain', role='netdata') | length > 0)
                               else lookup('role_var', '_web_domain', role='netdata')) }}"
        ```

=== "DNS"

    ??? variable string "`netdata_role_dns_record`"

        ```yaml
        # Type: string
        netdata_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='netdata') }}"
        ```

    ??? variable string "`netdata_role_dns_zone`"

        ```yaml
        # Type: string
        netdata_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='netdata') }}"
        ```

    ??? variable bool "`netdata_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        netdata_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`netdata_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        netdata_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`netdata_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        netdata_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`netdata_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        netdata_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`netdata_role_traefik_certresolver`"

        ```yaml
        # Type: string
        netdata_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`netdata_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        netdata_role_traefik_enabled: true
        ```

    ??? variable bool "`netdata_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        netdata_role_traefik_api_enabled: false
        ```

    ??? variable string "`netdata_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        netdata_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`netdata_role_docker_container`"

        ```yaml
        # Type: string
        netdata_role_docker_container: "{{ netdata_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`netdata_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        netdata_role_docker_image_pull: true
        ```

    ??? variable string "`netdata_role_docker_image_repo`"

        ```yaml
        # Type: string
        netdata_role_docker_image_repo: "netdata/netdata"
        ```

    ??? variable string "`netdata_role_docker_image_tag`"

        ```yaml
        # Type: string
        netdata_role_docker_image_tag: "latest"
        ```

    ??? variable string "`netdata_role_docker_image`"

        ```yaml
        # Type: string
        netdata_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='netdata') }}:{{ lookup('role_var', '_docker_image_tag', role='netdata') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`netdata_role_docker_envs_default`"

        ```yaml
        # Type: dict
        netdata_role_docker_envs_default: 
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          DOCKER_HOST: "{{ netdata_name }}-docker-socket-proxy:2375"
          NETDATA_CLAIM_TOKEN: "{{ lookup('role_var', '_claim_token', role='netdata') }}"
          NETDATA_CLAIM_URL: "{{ lookup('role_var', '_claim_url', role='netdata') }}"
          NETDATA_CLAIM_ROOMS: "{{ lookup('role_var', '_claim_room', role='netdata') }}"
        ```

    ??? variable dict "`netdata_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        netdata_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`netdata_role_docker_volumes_default`"

        ```yaml
        # Type: list
        netdata_role_docker_volumes_default: 
          - "{{ netdata_role_paths_location }}/config:/etc/netdata"
          - "netdatalib:/var/lib/netdata"
          - "netdatacache:/var/cache/netdata"
          - "/etc/passwd:/host/etc/passwd:ro"
          - "/etc/group:/host/etc/group:ro"
          - "/proc:/host/proc:ro"
          - "/sys:/host/sys:ro"
          - "/etc/os-release:/host/etc/os-release:ro"
          - "/var/log:/host/var/log:ro"
          - "/run/dbus:/run/dbus:ro"
        ```

    ??? variable list "`netdata_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        netdata_role_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable dict "`netdata_role_docker_labels_default`"

        ```yaml
        # Type: dict
        netdata_role_docker_labels_default: {}
        ```

    ??? variable dict "`netdata_role_docker_labels_custom`"

        ```yaml
        # Type: dict
        netdata_role_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`netdata_role_docker_hostname`"

        ```yaml
        # Type: string
        netdata_role_docker_hostname: "{{ netdata_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`netdata_role_docker_networks_alias`"

        ```yaml
        # Type: string
        netdata_role_docker_networks_alias: "{{ netdata_name }}"
        ```

    ??? variable list "`netdata_role_docker_networks_default`"

        ```yaml
        # Type: list
        netdata_role_docker_networks_default: []
        ```

    ??? variable list "`netdata_role_docker_networks_custom`"

        ```yaml
        # Type: list
        netdata_role_docker_networks_custom: []
        ```

    <h5>Capabilities</h5>

    ??? variable list "`netdata_role_docker_capabilities_default`"

        ```yaml
        # Type: list
        netdata_role_docker_capabilities_default: 
          - SYS_PTRACE
          - SYS_ADMIN
        ```

    ??? variable list "`netdata_role_docker_capabilities_custom`"

        ```yaml
        # Type: list
        netdata_role_docker_capabilities_custom: []
        ```

    <h5>Security Opts</h5>

    ??? variable list "`netdata_role_docker_security_opts_default`"

        ```yaml
        # Type: list
        netdata_role_docker_security_opts_default: 
          - apparmor=unconfined
        ```

    ??? variable list "`netdata_role_docker_security_opts_custom`"

        ```yaml
        # Type: list
        netdata_role_docker_security_opts_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`netdata_role_docker_restart_policy`"

        ```yaml
        # Type: string
        netdata_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`netdata_role_docker_state`"

        ```yaml
        # Type: string
        netdata_role_docker_state: started
        ```

    <h5>PID Mode</h5>

    ??? variable string "`netdata_role_docker_pid_mode`"

        ```yaml
        # Type: string
        netdata_role_docker_pid_mode: "host"
        ```

    <h5>Dependencies</h5>

    ??? variable string "`netdata_role_depends_on`"

        ```yaml
        # Type: string
        netdata_role_depends_on: "{{ netdata_name }}-docker-socket-proxy"
        ```

    ??? variable string "`netdata_role_depends_on_delay`"

        ```yaml
        # Type: string
        netdata_role_depends_on_delay: "0"
        ```

    ??? variable string "`netdata_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        netdata_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    <h5>Resource Limits</h5>

    ??? variable int "`netdata_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        netdata_role_docker_blkio_weight:
        ```

    ??? variable int "`netdata_role_docker_cpu_period`"

        ```yaml
        # Type: int
        netdata_role_docker_cpu_period:
        ```

    ??? variable int "`netdata_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        netdata_role_docker_cpu_quota:
        ```

    ??? variable int "`netdata_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        netdata_role_docker_cpu_shares:
        ```

    ??? variable string "`netdata_role_docker_cpus`"

        ```yaml
        # Type: string
        netdata_role_docker_cpus:
        ```

    ??? variable string "`netdata_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        netdata_role_docker_cpuset_cpus:
        ```

    ??? variable string "`netdata_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        netdata_role_docker_cpuset_mems:
        ```

    ??? variable string "`netdata_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        netdata_role_docker_kernel_memory:
        ```

    ??? variable string "`netdata_role_docker_memory`"

        ```yaml
        # Type: string
        netdata_role_docker_memory:
        ```

    ??? variable string "`netdata_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        netdata_role_docker_memory_reservation:
        ```

    ??? variable string "`netdata_role_docker_memory_swap`"

        ```yaml
        # Type: string
        netdata_role_docker_memory_swap:
        ```

    ??? variable int "`netdata_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        netdata_role_docker_memory_swappiness:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`netdata_role_docker_cap_drop`"

        ```yaml
        # Type: list
        netdata_role_docker_cap_drop:
        ```

    ??? variable list "`netdata_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        netdata_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`netdata_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        netdata_role_docker_device_read_bps:
        ```

    ??? variable list "`netdata_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        netdata_role_docker_device_read_iops:
        ```

    ??? variable list "`netdata_role_docker_device_requests`"

        ```yaml
        # Type: list
        netdata_role_docker_device_requests:
        ```

    ??? variable list "`netdata_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        netdata_role_docker_device_write_bps:
        ```

    ??? variable list "`netdata_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        netdata_role_docker_device_write_iops:
        ```

    ??? variable list "`netdata_role_docker_devices`"

        ```yaml
        # Type: list
        netdata_role_docker_devices:
        ```

    ??? variable string "`netdata_role_docker_devices_default`"

        ```yaml
        # Type: string
        netdata_role_docker_devices_default:
        ```

    ??? variable bool "`netdata_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        netdata_role_docker_privileged:
        ```

    <h5>Networking</h5>

    ??? variable list "`netdata_role_docker_dns_opts`"

        ```yaml
        # Type: list
        netdata_role_docker_dns_opts:
        ```

    ??? variable list "`netdata_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        netdata_role_docker_dns_search_domains:
        ```

    ??? variable list "`netdata_role_docker_dns_servers`"

        ```yaml
        # Type: list
        netdata_role_docker_dns_servers:
        ```

    ??? variable dict "`netdata_role_docker_hosts`"

        ```yaml
        # Type: dict
        netdata_role_docker_hosts:
        ```

    ??? variable string "`netdata_role_docker_hosts_use_common`"

        ```yaml
        # Type: string
        netdata_role_docker_hosts_use_common:
        ```

    ??? variable string "`netdata_role_docker_network_mode`"

        ```yaml
        # Type: string
        netdata_role_docker_network_mode:
        ```

    <h5>Storage</h5>

    ??? variable bool "`netdata_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        netdata_role_docker_keep_volumes:
        ```

    ??? variable list "`netdata_role_docker_mounts`"

        ```yaml
        # Type: list
        netdata_role_docker_mounts:
        ```

    ??? variable string "`netdata_role_docker_volume_driver`"

        ```yaml
        # Type: string
        netdata_role_docker_volume_driver:
        ```

    ??? variable list "`netdata_role_docker_volumes_from`"

        ```yaml
        # Type: list
        netdata_role_docker_volumes_from:
        ```

    ??? variable string "`netdata_role_docker_volumes_global`"

        ```yaml
        # Type: string
        netdata_role_docker_volumes_global:
        ```

    ??? variable string "`netdata_role_docker_working_dir`"

        ```yaml
        # Type: string
        netdata_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable dict "`netdata_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        netdata_role_docker_healthcheck:
        ```

    ??? variable bool "`netdata_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        netdata_role_docker_init:
        ```

    ??? variable string "`netdata_role_docker_log_driver`"

        ```yaml
        # Type: string
        netdata_role_docker_log_driver:
        ```

    ??? variable dict "`netdata_role_docker_log_options`"

        ```yaml
        # Type: dict
        netdata_role_docker_log_options:
        ```

    ??? variable bool "`netdata_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        netdata_role_docker_output_logs:
        ```

    <h5>Other Options</h5>

    ??? variable bool "`netdata_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        netdata_role_docker_auto_remove:
        ```

    ??? variable string "`netdata_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        netdata_role_docker_cgroup_parent:
        ```

    ??? variable string "`netdata_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        netdata_role_docker_cgroupns_mode:
        ```

    ??? variable bool "`netdata_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        netdata_role_docker_cleanup:
        ```

    ??? variable list "`netdata_role_docker_commands`"

        ```yaml
        # Type: list
        netdata_role_docker_commands:
        ```

    ??? variable string "`netdata_role_docker_create_timeout`"

        ```yaml
        # Type: string
        netdata_role_docker_create_timeout:
        ```

    ??? variable string "`netdata_role_docker_domainname`"

        ```yaml
        # Type: string
        netdata_role_docker_domainname:
        ```

    ??? variable string "`netdata_role_docker_entrypoint`"

        ```yaml
        # Type: string
        netdata_role_docker_entrypoint:
        ```

    ??? variable string "`netdata_role_docker_env_file`"

        ```yaml
        # Type: string
        netdata_role_docker_env_file:
        ```

    ??? variable list "`netdata_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        netdata_role_docker_exposed_ports:
        ```

    ??? variable string "`netdata_role_docker_force_kill`"

        ```yaml
        # Type: string
        netdata_role_docker_force_kill:
        ```

    ??? variable list "`netdata_role_docker_groups`"

        ```yaml
        # Type: list
        netdata_role_docker_groups:
        ```

    ??? variable int "`netdata_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        netdata_role_docker_healthy_wait_timeout:
        ```

    ??? variable string "`netdata_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        netdata_role_docker_ipc_mode:
        ```

    ??? variable string "`netdata_role_docker_kill_signal`"

        ```yaml
        # Type: string
        netdata_role_docker_kill_signal:
        ```

    ??? variable string "`netdata_role_docker_labels_use_common`"

        ```yaml
        # Type: string
        netdata_role_docker_labels_use_common:
        ```

    ??? variable list "`netdata_role_docker_links`"

        ```yaml
        # Type: list
        netdata_role_docker_links:
        ```

    ??? variable bool "`netdata_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        netdata_role_docker_oom_killer:
        ```

    ??? variable int "`netdata_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        netdata_role_docker_oom_score_adj:
        ```

    ??? variable bool "`netdata_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        netdata_role_docker_paused:
        ```

    ??? variable list "`netdata_role_docker_ports`"

        ```yaml
        # Type: list
        netdata_role_docker_ports:
        ```

    ??? variable bool "`netdata_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        netdata_role_docker_read_only:
        ```

    ??? variable bool "`netdata_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        netdata_role_docker_recreate:
        ```

    ??? variable int "`netdata_role_docker_restart_retries`"

        ```yaml
        # Type: int
        netdata_role_docker_restart_retries:
        ```

    ??? variable string "`netdata_role_docker_runtime`"

        ```yaml
        # Type: string
        netdata_role_docker_runtime:
        ```

    ??? variable string "`netdata_role_docker_shm_size`"

        ```yaml
        # Type: string
        netdata_role_docker_shm_size:
        ```

    ??? variable int "`netdata_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        netdata_role_docker_stop_timeout:
        ```

    ??? variable dict "`netdata_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        netdata_role_docker_storage_opts:
        ```

    ??? variable list "`netdata_role_docker_sysctls`"

        ```yaml
        # Type: list
        netdata_role_docker_sysctls:
        ```

    ??? variable list "`netdata_role_docker_tmpfs`"

        ```yaml
        # Type: list
        netdata_role_docker_tmpfs:
        ```

    ??? variable list "`netdata_role_docker_ulimits`"

        ```yaml
        # Type: list
        netdata_role_docker_ulimits:
        ```

    ??? variable string "`netdata_role_docker_user`"

        ```yaml
        # Type: string
        netdata_role_docker_user:
        ```

    ??? variable string "`netdata_role_docker_userns_mode`"

        ```yaml
        # Type: string
        netdata_role_docker_userns_mode:
        ```

    ??? variable string "`netdata_role_docker_uts`"

        ```yaml
        # Type: string
        netdata_role_docker_uts:
        ```

=== "Global Override Options"

    ??? variable bool "`netdata_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        netdata_role_autoheal_enabled: true
        ```

    ??? variable string "`netdata_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        netdata_role_depends_on: ""
        ```

    ??? variable string "`netdata_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        netdata_role_depends_on_delay: "0"
        ```

    ??? variable string "`netdata_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        netdata_role_depends_on_healthchecks:
        ```

    ??? variable bool "`netdata_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        netdata_role_diun_enabled: true
        ```

    ??? variable bool "`netdata_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        netdata_role_dns_enabled: true
        ```

    ??? variable bool "`netdata_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        netdata_role_docker_controller: true
        ```

    ??? variable bool "`netdata_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        netdata_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`netdata_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        netdata_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`netdata_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        netdata_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`netdata_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        netdata_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`netdata_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        netdata_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`netdata_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        netdata_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`netdata_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        netdata_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`netdata_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        netdata_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`netdata_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        netdata_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`netdata_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        netdata_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            netdata_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "netdata2.{{ user.domain }}"
              - "netdata.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`netdata_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        netdata_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            netdata_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'netdata2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`netdata_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        netdata_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
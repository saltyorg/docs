---
icon: material/docker
hide:
  - tags
tags:
  - reposilite
  - development
  - repository
---

# reposilite

## Overview

[reposilite](https://reposilite.com/) is a...

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://reposilite.com/){: .header-icons } | [:octicons-link-16: Docs](https://reposilite.com/guide/about){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/dzikoysk/reposilite){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/dzikoysk/reposilite){: .header-icons }|

### 1. Installation

```shell
sb install sandbox-reposilite
```

### 2. URL

- To access reposilite, visit <https://reposilite.iYOUR_DOMAIN_NAMEi>

### 3. Usage

- Consult [the doc](https://reposilite.com/guide/docker)

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    reposilite_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `reposilite_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `reposilite_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`reposilite_name`"

        ```yaml
        # Type: string
        reposilite_name: reposilite
        ```

=== "Paths"

    ??? variable string "`reposilite_role_paths_folder`"

        ```yaml
        # Type: string
        reposilite_role_paths_folder: "{{ reposilite_name }}"
        ```

    ??? variable string "`reposilite_role_paths_location`"

        ```yaml
        # Type: string
        reposilite_role_paths_location: "{{ server_appdata_path }}/{{ reposilite_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`reposilite_role_web_subdomain`"

        ```yaml
        # Type: string
        reposilite_role_web_subdomain: "{{ reposilite_name }}"
        ```

    ??? variable string "`reposilite_role_web_domain`"

        ```yaml
        # Type: string
        reposilite_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`reposilite_role_web_port`"

        ```yaml
        # Type: string
        reposilite_role_web_port: "8080"
        ```

    ??? variable string "`reposilite_role_web_url`"

        ```yaml
        # Type: string
        reposilite_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='reposilite') + '.' + lookup('role_var', '_web_domain', role='reposilite')
                                  if (lookup('role_var', '_web_subdomain', role='reposilite') | length > 0)
                                  else lookup('role_var', '_web_domain', role='reposilite')) }}"
        ```

=== "DNS"

    ??? variable string "`reposilite_role_dns_record`"

        ```yaml
        # Type: string
        reposilite_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='reposilite') }}"
        ```

    ??? variable string "`reposilite_role_dns_zone`"

        ```yaml
        # Type: string
        reposilite_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='reposilite') }}"
        ```

    ??? variable bool "`reposilite_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`reposilite_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        reposilite_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`reposilite_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        reposilite_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`reposilite_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        reposilite_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`reposilite_role_traefik_certresolver`"

        ```yaml
        # Type: string
        reposilite_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`reposilite_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_traefik_enabled: true
        ```

    ??? variable bool "`reposilite_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_traefik_api_enabled: true
        ```

    ??? variable string "`reposilite_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        reposilite_role_traefik_api_endpoint: "PathPrefix(`/api`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`reposilite_role_docker_container`"

        ```yaml
        # Type: string
        reposilite_role_docker_container: "{{ reposilite_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`reposilite_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_docker_image_pull: true
        ```

    ??? variable string "`reposilite_role_docker_image_repo`"

        ```yaml
        # Type: string
        reposilite_role_docker_image_repo: "ghcr.io/dzikoysk/reposilite"
        ```

    ??? variable string "`reposilite_role_docker_image_tag`"

        ```yaml
        # Type: string
        reposilite_role_docker_image_tag: "latest"
        ```

    ??? variable string "`reposilite_role_docker_image`"

        ```yaml
        # Type: string
        reposilite_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='reposilite') }}:{{ lookup('role_var', '_docker_image_tag', role='reposilite') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`reposilite_role_docker_envs_default`"

        ```yaml
        # Type: dict
        reposilite_role_docker_envs_default:
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          REPOSILITE_OPTS: "--token {{ user.name }}:{{ user.pass }}"
        ```

    ??? variable dict "`reposilite_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        reposilite_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`reposilite_role_docker_volumes_default`"

        ```yaml
        # Type: list
        reposilite_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='reposilite') }}:/app/data"
        ```

    ??? variable list "`reposilite_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        reposilite_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`reposilite_role_docker_hostname`"

        ```yaml
        # Type: string
        reposilite_role_docker_hostname: "{{ reposilite_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`reposilite_role_docker_networks_alias`"

        ```yaml
        # Type: string
        reposilite_role_docker_networks_alias: "{{ reposilite_name }}"
        ```

    ??? variable list "`reposilite_role_docker_networks_default`"

        ```yaml
        # Type: list
        reposilite_role_docker_networks_default: []
        ```

    ??? variable list "`reposilite_role_docker_networks_custom`"

        ```yaml
        # Type: list
        reposilite_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`reposilite_role_docker_restart_policy`"

        ```yaml
        # Type: string
        reposilite_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`reposilite_role_docker_state`"

        ```yaml
        # Type: string
        reposilite_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`reposilite_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        reposilite_role_docker_blkio_weight:
        ```

    ??? variable int "`reposilite_role_docker_cpu_period`"

        ```yaml
        # Type: int
        reposilite_role_docker_cpu_period:
        ```

    ??? variable int "`reposilite_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        reposilite_role_docker_cpu_quota:
        ```

    ??? variable int "`reposilite_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        reposilite_role_docker_cpu_shares:
        ```

    ??? variable string "`reposilite_role_docker_cpus`"

        ```yaml
        # Type: string
        reposilite_role_docker_cpus:
        ```

    ??? variable string "`reposilite_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        reposilite_role_docker_cpuset_cpus:
        ```

    ??? variable string "`reposilite_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        reposilite_role_docker_cpuset_mems:
        ```

    ??? variable string "`reposilite_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        reposilite_role_docker_kernel_memory:
        ```

    ??? variable string "`reposilite_role_docker_memory`"

        ```yaml
        # Type: string
        reposilite_role_docker_memory:
        ```

    ??? variable string "`reposilite_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        reposilite_role_docker_memory_reservation:
        ```

    ??? variable string "`reposilite_role_docker_memory_swap`"

        ```yaml
        # Type: string
        reposilite_role_docker_memory_swap:
        ```

    ??? variable int "`reposilite_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        reposilite_role_docker_memory_swappiness:
        ```

    ??? variable string "`reposilite_role_docker_shm_size`"

        ```yaml
        # Type: string
        reposilite_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`reposilite_role_docker_cap_drop`"

        ```yaml
        # Type: list
        reposilite_role_docker_cap_drop:
        ```

    ??? variable string "`reposilite_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        reposilite_role_docker_cgroupns_mode:
        ```

    ??? variable list "`reposilite_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        reposilite_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`reposilite_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        reposilite_role_docker_device_read_bps:
        ```

    ??? variable list "`reposilite_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        reposilite_role_docker_device_read_iops:
        ```

    ??? variable list "`reposilite_role_docker_device_requests`"

        ```yaml
        # Type: list
        reposilite_role_docker_device_requests:
        ```

    ??? variable list "`reposilite_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        reposilite_role_docker_device_write_bps:
        ```

    ??? variable list "`reposilite_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        reposilite_role_docker_device_write_iops:
        ```

    ??? variable list "`reposilite_role_docker_devices`"

        ```yaml
        # Type: list
        reposilite_role_docker_devices:
        ```

    ??? variable string "`reposilite_role_docker_devices_default`"

        ```yaml
        # Type: string
        reposilite_role_docker_devices_default:
        ```

    ??? variable list "`reposilite_role_docker_groups`"

        ```yaml
        # Type: list
        reposilite_role_docker_groups:
        ```

    ??? variable bool "`reposilite_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_docker_privileged:
        ```

    ??? variable list "`reposilite_role_docker_security_opts`"

        ```yaml
        # Type: list
        reposilite_role_docker_security_opts:
        ```

    ??? variable string "`reposilite_role_docker_user`"

        ```yaml
        # Type: string
        reposilite_role_docker_user:
        ```

    ??? variable string "`reposilite_role_docker_userns_mode`"

        ```yaml
        # Type: string
        reposilite_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`reposilite_role_docker_dns_opts`"

        ```yaml
        # Type: list
        reposilite_role_docker_dns_opts:
        ```

    ??? variable list "`reposilite_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        reposilite_role_docker_dns_search_domains:
        ```

    ??? variable list "`reposilite_role_docker_dns_servers`"

        ```yaml
        # Type: list
        reposilite_role_docker_dns_servers:
        ```

    ??? variable string "`reposilite_role_docker_domainname`"

        ```yaml
        # Type: string
        reposilite_role_docker_domainname:
        ```

    ??? variable list "`reposilite_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        reposilite_role_docker_exposed_ports:
        ```

    ??? variable dict "`reposilite_role_docker_hosts`"

        ```yaml
        # Type: dict
        reposilite_role_docker_hosts:
        ```

    ??? variable bool "`reposilite_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_docker_hosts_use_common:
        ```

    ??? variable string "`reposilite_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        reposilite_role_docker_ipc_mode:
        ```

    ??? variable list "`reposilite_role_docker_links`"

        ```yaml
        # Type: list
        reposilite_role_docker_links:
        ```

    ??? variable string "`reposilite_role_docker_network_mode`"

        ```yaml
        # Type: string
        reposilite_role_docker_network_mode:
        ```

    ??? variable string "`reposilite_role_docker_pid_mode`"

        ```yaml
        # Type: string
        reposilite_role_docker_pid_mode:
        ```

    ??? variable list "`reposilite_role_docker_ports`"

        ```yaml
        # Type: list
        reposilite_role_docker_ports:
        ```

    ??? variable string "`reposilite_role_docker_uts`"

        ```yaml
        # Type: string
        reposilite_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`reposilite_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_docker_keep_volumes:
        ```

    ??? variable list "`reposilite_role_docker_mounts`"

        ```yaml
        # Type: list
        reposilite_role_docker_mounts:
        ```

    ??? variable dict "`reposilite_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        reposilite_role_docker_storage_opts:
        ```

    ??? variable list "`reposilite_role_docker_tmpfs`"

        ```yaml
        # Type: list
        reposilite_role_docker_tmpfs:
        ```

    ??? variable string "`reposilite_role_docker_volume_driver`"

        ```yaml
        # Type: string
        reposilite_role_docker_volume_driver:
        ```

    ??? variable list "`reposilite_role_docker_volumes_from`"

        ```yaml
        # Type: list
        reposilite_role_docker_volumes_from:
        ```

    ??? variable bool "`reposilite_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_docker_volumes_global:
        ```

    ??? variable string "`reposilite_role_docker_working_dir`"

        ```yaml
        # Type: string
        reposilite_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`reposilite_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_docker_auto_remove:
        ```

    ??? variable bool "`reposilite_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_docker_cleanup:
        ```

    ??? variable string "`reposilite_role_docker_force_kill`"

        ```yaml
        # Type: string
        reposilite_role_docker_force_kill:
        ```

    ??? variable dict "`reposilite_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        reposilite_role_docker_healthcheck:
        ```

    ??? variable int "`reposilite_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        reposilite_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`reposilite_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_docker_init:
        ```

    ??? variable string "`reposilite_role_docker_kill_signal`"

        ```yaml
        # Type: string
        reposilite_role_docker_kill_signal:
        ```

    ??? variable string "`reposilite_role_docker_log_driver`"

        ```yaml
        # Type: string
        reposilite_role_docker_log_driver:
        ```

    ??? variable dict "`reposilite_role_docker_log_options`"

        ```yaml
        # Type: dict
        reposilite_role_docker_log_options:
        ```

    ??? variable bool "`reposilite_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_docker_oom_killer:
        ```

    ??? variable int "`reposilite_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        reposilite_role_docker_oom_score_adj:
        ```

    ??? variable bool "`reposilite_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_docker_output_logs:
        ```

    ??? variable bool "`reposilite_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_docker_paused:
        ```

    ??? variable bool "`reposilite_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_docker_recreate:
        ```

    ??? variable int "`reposilite_role_docker_restart_retries`"

        ```yaml
        # Type: int
        reposilite_role_docker_restart_retries:
        ```

    ??? variable int "`reposilite_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        reposilite_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`reposilite_role_docker_capabilities`"

        ```yaml
        # Type: list
        reposilite_role_docker_capabilities:
        ```

    ??? variable string "`reposilite_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        reposilite_role_docker_cgroup_parent:
        ```

    ??? variable list "`reposilite_role_docker_commands`"

        ```yaml
        # Type: list
        reposilite_role_docker_commands:
        ```

    ??? variable int "`reposilite_role_docker_create_timeout`"

        ```yaml
        # Type: int
        reposilite_role_docker_create_timeout:
        ```

    ??? variable string "`reposilite_role_docker_entrypoint`"

        ```yaml
        # Type: string
        reposilite_role_docker_entrypoint:
        ```

    ??? variable string "`reposilite_role_docker_env_file`"

        ```yaml
        # Type: string
        reposilite_role_docker_env_file:
        ```

    ??? variable dict "`reposilite_role_docker_labels`"

        ```yaml
        # Type: dict
        reposilite_role_docker_labels:
        ```

    ??? variable bool "`reposilite_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_docker_labels_use_common:
        ```

    ??? variable bool "`reposilite_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_docker_read_only:
        ```

    ??? variable string "`reposilite_role_docker_runtime`"

        ```yaml
        # Type: string
        reposilite_role_docker_runtime:
        ```

    ??? variable list "`reposilite_role_docker_sysctls`"

        ```yaml
        # Type: list
        reposilite_role_docker_sysctls:
        ```

    ??? variable list "`reposilite_role_docker_ulimits`"

        ```yaml
        # Type: list
        reposilite_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`reposilite_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        reposilite_role_autoheal_enabled: true
        ```

    ??? variable string "`reposilite_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        reposilite_role_depends_on: ""
        ```

    ??? variable string "`reposilite_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        reposilite_role_depends_on_delay: "0"
        ```

    ??? variable string "`reposilite_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        reposilite_role_depends_on_healthchecks:
        ```

    ??? variable bool "`reposilite_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        reposilite_role_diun_enabled: true
        ```

    ??? variable bool "`reposilite_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        reposilite_role_dns_enabled: true
        ```

    ??? variable bool "`reposilite_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        reposilite_role_docker_controller: true
        ```

    ??? variable string "`reposilite_role_docker_image_repo`"

        ```yaml
        # Type: string
        reposilite_role_docker_image_repo:
        ```

    ??? variable string "`reposilite_role_docker_image_tag`"

        ```yaml
        # Type: string
        reposilite_role_docker_image_tag:
        ```

    ??? variable bool "`reposilite_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_docker_volumes_download:
        ```

    ??? variable string "`reposilite_role_paths_location`"

        ```yaml
        # Type: string
        reposilite_role_paths_location:
        ```

    ??? variable string "`reposilite_role_themepark_addons`"

        ```yaml
        # Type: string
        reposilite_role_themepark_addons:
        ```

    ??? variable string "`reposilite_role_themepark_app`"

        ```yaml
        # Type: string
        reposilite_role_themepark_app:
        ```

    ??? variable string "`reposilite_role_themepark_theme`"

        ```yaml
        # Type: string
        reposilite_role_themepark_theme:
        ```

    ??? variable dict/omit "`reposilite_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        reposilite_role_traefik_api_endpoint:
        ```

    ??? variable string "`reposilite_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        reposilite_role_traefik_api_middleware:
        ```

    ??? variable string "`reposilite_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        reposilite_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`reposilite_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        reposilite_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`reposilite_role_traefik_certresolver`"

        ```yaml
        # Type: string
        reposilite_role_traefik_certresolver:
        ```

    ??? variable bool "`reposilite_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        reposilite_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`reposilite_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        reposilite_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`reposilite_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        reposilite_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`reposilite_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        reposilite_role_traefik_middleware_http:
        ```

    ??? variable bool "`reposilite_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`reposilite_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        reposilite_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`reposilite_role_traefik_priority`"

        ```yaml
        # Type: string
        reposilite_role_traefik_priority:
        ```

    ??? variable bool "`reposilite_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        reposilite_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`reposilite_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        reposilite_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`reposilite_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        reposilite_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`reposilite_role_web_domain`"

        ```yaml
        # Type: string
        reposilite_role_web_domain:
        ```

    ??? variable list "`reposilite_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        reposilite_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            reposilite_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "reposilite2.{{ user.domain }}"
              - "reposilite.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`reposilite_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        reposilite_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            reposilite_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'reposilite2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`reposilite_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        reposilite_role_web_http_port:
        ```

    ??? variable string "`reposilite_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        reposilite_role_web_http_scheme:
        ```

    ??? variable dict/omit "`reposilite_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        reposilite_role_web_http_serverstransport:
        ```

    ??? variable string "`reposilite_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        reposilite_role_web_scheme:
        ```

    ??? variable dict/omit "`reposilite_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        reposilite_role_web_serverstransport:
        ```

    ??? variable string "`reposilite_role_web_subdomain`"

        ```yaml
        # Type: string
        reposilite_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
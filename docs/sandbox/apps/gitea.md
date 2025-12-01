---
icon: material/docker
hide:
  - tags
tags:
  - gitea
  - development
  - git
---

# Gitea

## Overview

[Gitea](https://gitea.io/en-us/) is a community managed lightweight code hosting solution written in Go.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://docs.gitea.io){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/gitea/gitea/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-people-group:**Community**](){ .md-button .md-button--stretch }

</div>

---

## Deployment

```shell
sb install sandbox-gitea
```

## Usage

Visit <https://gitea.iYOUR_DOMAIN_NAMEi>.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    gitea_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `gitea_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `gitea_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`gitea_name`"

        ```yaml
        # Type: string
        gitea_name: gitea
        ```

=== "Paths"

    ??? variable string "`gitea_role_paths_folder`"

        ```yaml
        # Type: string
        gitea_role_paths_folder: "{{ gitea_name }}"
        ```

    ??? variable string "`gitea_role_paths_location`"

        ```yaml
        # Type: string
        gitea_role_paths_location: "{{ server_appdata_path }}/{{ gitea_role_paths_folder }}"
        ```

    ??? variable bool "`gitea_role_paths_recursive`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_paths_recursive: true
        ```

=== "Web"

    ??? variable string "`gitea_role_web_subdomain`"

        ```yaml
        # Type: string
        gitea_role_web_subdomain: "{{ gitea_name }}"
        ```

    ??? variable string "`gitea_role_web_domain`"

        ```yaml
        # Type: string
        gitea_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`gitea_role_web_port`"

        ```yaml
        # Type: string
        gitea_role_web_port: "3000"
        ```

    ??? variable string "`gitea_role_web_url`"

        ```yaml
        # Type: string
        gitea_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='gitea') + '.' + lookup('role_var', '_web_domain', role='gitea')
                             if (lookup('role_var', '_web_subdomain', role='gitea') | length > 0)
                             else lookup('role_var', '_web_domain', role='gitea')) }}"
        ```

=== "DNS"

    ??? variable string "`gitea_role_dns_record`"

        ```yaml
        # Type: string
        gitea_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='gitea') }}"
        ```

    ??? variable string "`gitea_role_dns_zone`"

        ```yaml
        # Type: string
        gitea_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='gitea') }}"
        ```

    ??? variable bool "`gitea_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`gitea_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        gitea_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`gitea_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        gitea_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`gitea_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        gitea_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`gitea_role_traefik_certresolver`"

        ```yaml
        # Type: string
        gitea_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`gitea_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_traefik_enabled: true
        ```

    ??? variable bool "`gitea_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_traefik_api_enabled: false
        ```

    ??? variable string "`gitea_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        gitea_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`gitea_role_docker_container`"

        ```yaml
        # Type: string
        gitea_role_docker_container: "{{ gitea_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`gitea_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_docker_image_pull: true
        ```

    ??? variable string "`gitea_role_docker_image_repo`"

        ```yaml
        # Type: string
        gitea_role_docker_image_repo: "gitea/gitea"
        ```

    ??? variable string "`gitea_role_docker_image_tag`"

        ```yaml
        # Type: string
        gitea_role_docker_image_tag: "latest"
        ```

    ??? variable string "`gitea_role_docker_image`"

        ```yaml
        # Type: string
        gitea_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='gitea') }}:{{ lookup('role_var', '_docker_image_tag', role='gitea') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`gitea_role_docker_envs_default`"

        ```yaml
        # Type: dict
        gitea_role_docker_envs_default:
          USER_UID: "{{ uid }}"
          USER_GID: "{{ gid }}"
          GITEA__database__DB_TYPE: "mysql"
          GITEA__database__HOST: "mariadb:3306"
          GITEA__database__USER: "root"
          GITEA__database__PASSWD: "{{ lookup('role_var', '_docker_env_password', role='mariadb') }}"
          GITEA__database__NAME: "gitea"
          DISABLE_SSH: "true"
          ROOT_URL: "{{ lookup('role_var', '_web_url', role='gitea') }}/"
        ```

    ??? variable dict "`gitea_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        gitea_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`gitea_role_docker_volumes_default`"

        ```yaml
        # Type: list
        gitea_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='gitea') }}:/data"
          - /etc/timezone:/etc/timezone:ro
          - /etc/localtime:/etc/localtime:ro
        ```

    ??? variable list "`gitea_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        gitea_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`gitea_role_docker_hostname`"

        ```yaml
        # Type: string
        gitea_role_docker_hostname: "{{ gitea_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`gitea_role_docker_networks_alias`"

        ```yaml
        # Type: string
        gitea_role_docker_networks_alias: "{{ gitea_name }}"
        ```

    ??? variable list "`gitea_role_docker_networks_default`"

        ```yaml
        # Type: list
        gitea_role_docker_networks_default: []
        ```

    ??? variable list "`gitea_role_docker_networks_custom`"

        ```yaml
        # Type: list
        gitea_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`gitea_role_docker_restart_policy`"

        ```yaml
        # Type: string
        gitea_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`gitea_role_docker_state`"

        ```yaml
        # Type: string
        gitea_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`gitea_role_depends_on`"

        ```yaml
        # Type: string
        gitea_role_depends_on: "mariadb"
        ```

    ??? variable string "`gitea_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        gitea_role_depends_on_delay: "0"
        ```

    ??? variable string "`gitea_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        gitea_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`gitea_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        gitea_role_docker_blkio_weight:
        ```

    ??? variable int "`gitea_role_docker_cpu_period`"

        ```yaml
        # Type: int
        gitea_role_docker_cpu_period:
        ```

    ??? variable int "`gitea_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        gitea_role_docker_cpu_quota:
        ```

    ??? variable int "`gitea_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        gitea_role_docker_cpu_shares:
        ```

    ??? variable string "`gitea_role_docker_cpus`"

        ```yaml
        # Type: string
        gitea_role_docker_cpus:
        ```

    ??? variable string "`gitea_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        gitea_role_docker_cpuset_cpus:
        ```

    ??? variable string "`gitea_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        gitea_role_docker_cpuset_mems:
        ```

    ??? variable string "`gitea_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        gitea_role_docker_kernel_memory:
        ```

    ??? variable string "`gitea_role_docker_memory`"

        ```yaml
        # Type: string
        gitea_role_docker_memory:
        ```

    ??? variable string "`gitea_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        gitea_role_docker_memory_reservation:
        ```

    ??? variable string "`gitea_role_docker_memory_swap`"

        ```yaml
        # Type: string
        gitea_role_docker_memory_swap:
        ```

    ??? variable int "`gitea_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        gitea_role_docker_memory_swappiness:
        ```

    ??? variable string "`gitea_role_docker_shm_size`"

        ```yaml
        # Type: string
        gitea_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`gitea_role_docker_cap_drop`"

        ```yaml
        # Type: list
        gitea_role_docker_cap_drop:
        ```

    ??? variable string "`gitea_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        gitea_role_docker_cgroupns_mode:
        ```

    ??? variable list "`gitea_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        gitea_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`gitea_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        gitea_role_docker_device_read_bps:
        ```

    ??? variable list "`gitea_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        gitea_role_docker_device_read_iops:
        ```

    ??? variable list "`gitea_role_docker_device_requests`"

        ```yaml
        # Type: list
        gitea_role_docker_device_requests:
        ```

    ??? variable list "`gitea_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        gitea_role_docker_device_write_bps:
        ```

    ??? variable list "`gitea_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        gitea_role_docker_device_write_iops:
        ```

    ??? variable list "`gitea_role_docker_devices`"

        ```yaml
        # Type: list
        gitea_role_docker_devices:
        ```

    ??? variable string "`gitea_role_docker_devices_default`"

        ```yaml
        # Type: string
        gitea_role_docker_devices_default:
        ```

    ??? variable list "`gitea_role_docker_groups`"

        ```yaml
        # Type: list
        gitea_role_docker_groups:
        ```

    ??? variable bool "`gitea_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_docker_privileged:
        ```

    ??? variable list "`gitea_role_docker_security_opts`"

        ```yaml
        # Type: list
        gitea_role_docker_security_opts:
        ```

    ??? variable string "`gitea_role_docker_user`"

        ```yaml
        # Type: string
        gitea_role_docker_user:
        ```

    ??? variable string "`gitea_role_docker_userns_mode`"

        ```yaml
        # Type: string
        gitea_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`gitea_role_docker_dns_opts`"

        ```yaml
        # Type: list
        gitea_role_docker_dns_opts:
        ```

    ??? variable list "`gitea_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        gitea_role_docker_dns_search_domains:
        ```

    ??? variable list "`gitea_role_docker_dns_servers`"

        ```yaml
        # Type: list
        gitea_role_docker_dns_servers:
        ```

    ??? variable string "`gitea_role_docker_domainname`"

        ```yaml
        # Type: string
        gitea_role_docker_domainname:
        ```

    ??? variable list "`gitea_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        gitea_role_docker_exposed_ports:
        ```

    ??? variable dict "`gitea_role_docker_hosts`"

        ```yaml
        # Type: dict
        gitea_role_docker_hosts:
        ```

    ??? variable bool "`gitea_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_docker_hosts_use_common:
        ```

    ??? variable string "`gitea_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        gitea_role_docker_ipc_mode:
        ```

    ??? variable list "`gitea_role_docker_links`"

        ```yaml
        # Type: list
        gitea_role_docker_links:
        ```

    ??? variable string "`gitea_role_docker_network_mode`"

        ```yaml
        # Type: string
        gitea_role_docker_network_mode:
        ```

    ??? variable string "`gitea_role_docker_pid_mode`"

        ```yaml
        # Type: string
        gitea_role_docker_pid_mode:
        ```

    ??? variable list "`gitea_role_docker_ports`"

        ```yaml
        # Type: list
        gitea_role_docker_ports:
        ```

    ??? variable string "`gitea_role_docker_uts`"

        ```yaml
        # Type: string
        gitea_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`gitea_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_docker_keep_volumes:
        ```

    ??? variable list "`gitea_role_docker_mounts`"

        ```yaml
        # Type: list
        gitea_role_docker_mounts:
        ```

    ??? variable dict "`gitea_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        gitea_role_docker_storage_opts:
        ```

    ??? variable list "`gitea_role_docker_tmpfs`"

        ```yaml
        # Type: list
        gitea_role_docker_tmpfs:
        ```

    ??? variable string "`gitea_role_docker_volume_driver`"

        ```yaml
        # Type: string
        gitea_role_docker_volume_driver:
        ```

    ??? variable list "`gitea_role_docker_volumes_from`"

        ```yaml
        # Type: list
        gitea_role_docker_volumes_from:
        ```

    ??? variable bool "`gitea_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_docker_volumes_global:
        ```

    ??? variable string "`gitea_role_docker_working_dir`"

        ```yaml
        # Type: string
        gitea_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`gitea_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_docker_auto_remove:
        ```

    ??? variable bool "`gitea_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_docker_cleanup:
        ```

    ??? variable string "`gitea_role_docker_force_kill`"

        ```yaml
        # Type: string
        gitea_role_docker_force_kill:
        ```

    ??? variable dict "`gitea_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        gitea_role_docker_healthcheck:
        ```

    ??? variable int "`gitea_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        gitea_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`gitea_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_docker_init:
        ```

    ??? variable string "`gitea_role_docker_kill_signal`"

        ```yaml
        # Type: string
        gitea_role_docker_kill_signal:
        ```

    ??? variable string "`gitea_role_docker_log_driver`"

        ```yaml
        # Type: string
        gitea_role_docker_log_driver:
        ```

    ??? variable dict "`gitea_role_docker_log_options`"

        ```yaml
        # Type: dict
        gitea_role_docker_log_options:
        ```

    ??? variable bool "`gitea_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_docker_oom_killer:
        ```

    ??? variable int "`gitea_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        gitea_role_docker_oom_score_adj:
        ```

    ??? variable bool "`gitea_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_docker_output_logs:
        ```

    ??? variable bool "`gitea_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_docker_paused:
        ```

    ??? variable bool "`gitea_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_docker_recreate:
        ```

    ??? variable int "`gitea_role_docker_restart_retries`"

        ```yaml
        # Type: int
        gitea_role_docker_restart_retries:
        ```

    ??? variable int "`gitea_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        gitea_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`gitea_role_docker_capabilities`"

        ```yaml
        # Type: list
        gitea_role_docker_capabilities:
        ```

    ??? variable string "`gitea_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        gitea_role_docker_cgroup_parent:
        ```

    ??? variable list "`gitea_role_docker_commands`"

        ```yaml
        # Type: list
        gitea_role_docker_commands:
        ```

    ??? variable int "`gitea_role_docker_create_timeout`"

        ```yaml
        # Type: int
        gitea_role_docker_create_timeout:
        ```

    ??? variable string "`gitea_role_docker_entrypoint`"

        ```yaml
        # Type: string
        gitea_role_docker_entrypoint:
        ```

    ??? variable string "`gitea_role_docker_env_file`"

        ```yaml
        # Type: string
        gitea_role_docker_env_file:
        ```

    ??? variable dict "`gitea_role_docker_labels`"

        ```yaml
        # Type: dict
        gitea_role_docker_labels:
        ```

    ??? variable bool "`gitea_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_docker_labels_use_common:
        ```

    ??? variable bool "`gitea_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_docker_read_only:
        ```

    ??? variable string "`gitea_role_docker_runtime`"

        ```yaml
        # Type: string
        gitea_role_docker_runtime:
        ```

    ??? variable list "`gitea_role_docker_sysctls`"

        ```yaml
        # Type: list
        gitea_role_docker_sysctls:
        ```

    ??? variable list "`gitea_role_docker_ulimits`"

        ```yaml
        # Type: list
        gitea_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`gitea_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        gitea_role_autoheal_enabled: true
        ```

    ??? variable string "`gitea_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        gitea_role_depends_on: ""
        ```

    ??? variable string "`gitea_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        gitea_role_depends_on_delay: "0"
        ```

    ??? variable string "`gitea_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        gitea_role_depends_on_healthchecks:
        ```

    ??? variable bool "`gitea_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        gitea_role_diun_enabled: true
        ```

    ??? variable bool "`gitea_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        gitea_role_dns_enabled: true
        ```

    ??? variable bool "`gitea_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        gitea_role_docker_controller: true
        ```

    ??? variable string "`gitea_role_docker_env_password`"

        ```yaml
        # Type: string
        gitea_role_docker_env_password:
        ```

    ??? variable string "`gitea_role_docker_image_repo`"

        ```yaml
        # Type: string
        gitea_role_docker_image_repo:
        ```

    ??? variable string "`gitea_role_docker_image_tag`"

        ```yaml
        # Type: string
        gitea_role_docker_image_tag:
        ```

    ??? variable bool "`gitea_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_docker_volumes_download:
        ```

    ??? variable string "`gitea_role_paths_location`"

        ```yaml
        # Type: string
        gitea_role_paths_location:
        ```

    ??? variable string "`gitea_role_themepark_addons`"

        ```yaml
        # Type: string
        gitea_role_themepark_addons:
        ```

    ??? variable string "`gitea_role_themepark_app`"

        ```yaml
        # Type: string
        gitea_role_themepark_app:
        ```

    ??? variable string "`gitea_role_themepark_theme`"

        ```yaml
        # Type: string
        gitea_role_themepark_theme:
        ```

    ??? variable dict/omit "`gitea_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        gitea_role_traefik_api_endpoint:
        ```

    ??? variable string "`gitea_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        gitea_role_traefik_api_middleware:
        ```

    ??? variable string "`gitea_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        gitea_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`gitea_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        gitea_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`gitea_role_traefik_certresolver`"

        ```yaml
        # Type: string
        gitea_role_traefik_certresolver:
        ```

    ??? variable bool "`gitea_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        gitea_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`gitea_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        gitea_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`gitea_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        gitea_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`gitea_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        gitea_role_traefik_middleware_http:
        ```

    ??? variable bool "`gitea_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`gitea_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`gitea_role_traefik_priority`"

        ```yaml
        # Type: string
        gitea_role_traefik_priority:
        ```

    ??? variable bool "`gitea_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        gitea_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`gitea_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        gitea_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`gitea_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        gitea_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`gitea_role_web_domain`"

        ```yaml
        # Type: string
        gitea_role_web_domain:
        ```

    ??? variable list "`gitea_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        gitea_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            gitea_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "gitea2.{{ user.domain }}"
              - "gitea.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`gitea_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        gitea_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            gitea_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'gitea2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`gitea_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        gitea_role_web_http_port:
        ```

    ??? variable string "`gitea_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        gitea_role_web_http_scheme:
        ```

    ??? variable dict/omit "`gitea_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        gitea_role_web_http_serverstransport:
        ```

    ??? variable string "`gitea_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        gitea_role_web_scheme:
        ```

    ??? variable dict/omit "`gitea_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        gitea_role_web_serverstransport:
        ```

    ??? variable string "`gitea_role_web_subdomain`"

        ```yaml
        # Type: string
        gitea_role_web_subdomain:
        ```

    ??? variable string "`gitea_role_web_url`"

        ```yaml
        # Type: string
        gitea_role_web_url:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
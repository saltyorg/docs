---
icon: material/docker
hide:
  - tags
tags:
  - dashy
  - dashboard
  - homepage
---

# Dashy

## Overview

[Dashy](https://dashy.to/) is the "Ultimate homepage for your homelab"

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://dashy.to/docs){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/lissy93/dashy/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-people-group:**Community**](){ .md-button .md-button--stretch }

</div>

---

## Deployment

```shell
sb install sandbox-dashy
```

## Usage

Visit <https://dashy.iYOUR_DOMAIN_NAMEi>.

## Basics

To edit your config, edit the `.yaml` file in dashys appdata folder, which is typically located at `/opt/dashy/`. You can also edit the config directly through the UI.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    dashy_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `dashy_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `dashy_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`dashy_name`"

        ```yaml
        # Type: string
        dashy_name: dashy
        ```

=== "Paths"

    ??? variable string "`dashy_role_paths_folder`"

        ```yaml
        # Type: string
        dashy_role_paths_folder: "{{ dashy_name }}"
        ```

    ??? variable string "`dashy_role_paths_location`"

        ```yaml
        # Type: string
        dashy_role_paths_location: "{{ server_appdata_path }}/{{ dashy_role_paths_folder }}"
        ```

    ??? variable string "`dashy_role_paths_config_location`"

        ```yaml
        # Type: string
        dashy_role_paths_config_location: "{{ dashy_role_paths_location }}/conf.yml"
        ```

=== "Web"

    ??? variable string "`dashy_role_web_subdomain`"

        ```yaml
        # Type: string
        dashy_role_web_subdomain: "{{ dashy_name }}"
        ```

    ??? variable string "`dashy_role_web_domain`"

        ```yaml
        # Type: string
        dashy_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`dashy_role_web_port`"

        ```yaml
        # Type: string
        dashy_role_web_port: "8080"
        ```

    ??? variable string "`dashy_role_web_url`"

        ```yaml
        # Type: string
        dashy_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='dashy') + '.' + lookup('role_var', '_web_domain', role='dashy')
                             if (lookup('role_var', '_web_subdomain', role='dashy') | length > 0)
                             else lookup('role_var', '_web_domain', role='dashy')) }}"
        ```

=== "DNS"

    ??? variable string "`dashy_role_dns_record`"

        ```yaml
        # Type: string
        dashy_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='dashy') }}"
        ```

    ??? variable string "`dashy_role_dns_zone`"

        ```yaml
        # Type: string
        dashy_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='dashy') }}"
        ```

    ??? variable bool "`dashy_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`dashy_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        dashy_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`dashy_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        dashy_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`dashy_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        dashy_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`dashy_role_traefik_certresolver`"

        ```yaml
        # Type: string
        dashy_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`dashy_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_traefik_enabled: true
        ```

    ??? variable bool "`dashy_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_traefik_api_enabled: false
        ```

    ??? variable string "`dashy_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        dashy_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`dashy_role_docker_container`"

        ```yaml
        # Type: string
        dashy_role_docker_container: "{{ dashy_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`dashy_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_docker_image_pull: true
        ```

    ??? variable string "`dashy_role_docker_image_repo`"

        ```yaml
        # Type: string
        dashy_role_docker_image_repo: "lissy93/dashy"
        ```

    ??? variable string "`dashy_role_docker_image_tag`"

        ```yaml
        # Type: string
        dashy_role_docker_image_tag: "latest"
        ```

    ??? variable string "`dashy_role_docker_image`"

        ```yaml
        # Type: string
        dashy_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='dashy') }}:{{ lookup('role_var', '_docker_image_tag', role='dashy') }}"
        ```

    <h5>Volumes</h5>

    ??? variable list "`dashy_role_docker_volumes_default`"

        ```yaml
        # Type: list
        dashy_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='dashy') }}:/app/user-data"
        ```

    ??? variable list "`dashy_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        dashy_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`dashy_role_docker_hostname`"

        ```yaml
        # Type: string
        dashy_role_docker_hostname: "{{ dashy_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`dashy_role_docker_networks_alias`"

        ```yaml
        # Type: string
        dashy_role_docker_networks_alias: "{{ dashy_name }}"
        ```

    ??? variable list "`dashy_role_docker_networks_default`"

        ```yaml
        # Type: list
        dashy_role_docker_networks_default: []
        ```

    ??? variable list "`dashy_role_docker_networks_custom`"

        ```yaml
        # Type: list
        dashy_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`dashy_role_docker_restart_policy`"

        ```yaml
        # Type: string
        dashy_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`dashy_role_docker_state`"

        ```yaml
        # Type: string
        dashy_role_docker_state: started
        ```

    <h5>Healthcheck</h5>

    ??? variable dict "`dashy_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        dashy_role_docker_healthcheck:
          test: ["CMD", "yarn", "health-check"]
          interval: 10s
          timeout: 5s
          retries: 10
          start_period: 10s
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`dashy_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        dashy_role_docker_blkio_weight:
        ```

    ??? variable int "`dashy_role_docker_cpu_period`"

        ```yaml
        # Type: int
        dashy_role_docker_cpu_period:
        ```

    ??? variable int "`dashy_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        dashy_role_docker_cpu_quota:
        ```

    ??? variable int "`dashy_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        dashy_role_docker_cpu_shares:
        ```

    ??? variable string "`dashy_role_docker_cpus`"

        ```yaml
        # Type: string
        dashy_role_docker_cpus:
        ```

    ??? variable string "`dashy_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        dashy_role_docker_cpuset_cpus:
        ```

    ??? variable string "`dashy_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        dashy_role_docker_cpuset_mems:
        ```

    ??? variable string "`dashy_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        dashy_role_docker_kernel_memory:
        ```

    ??? variable string "`dashy_role_docker_memory`"

        ```yaml
        # Type: string
        dashy_role_docker_memory:
        ```

    ??? variable string "`dashy_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        dashy_role_docker_memory_reservation:
        ```

    ??? variable string "`dashy_role_docker_memory_swap`"

        ```yaml
        # Type: string
        dashy_role_docker_memory_swap:
        ```

    ??? variable int "`dashy_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        dashy_role_docker_memory_swappiness:
        ```

    ??? variable string "`dashy_role_docker_shm_size`"

        ```yaml
        # Type: string
        dashy_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`dashy_role_docker_cap_drop`"

        ```yaml
        # Type: list
        dashy_role_docker_cap_drop:
        ```

    ??? variable string "`dashy_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        dashy_role_docker_cgroupns_mode:
        ```

    ??? variable list "`dashy_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        dashy_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`dashy_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        dashy_role_docker_device_read_bps:
        ```

    ??? variable list "`dashy_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        dashy_role_docker_device_read_iops:
        ```

    ??? variable list "`dashy_role_docker_device_requests`"

        ```yaml
        # Type: list
        dashy_role_docker_device_requests:
        ```

    ??? variable list "`dashy_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        dashy_role_docker_device_write_bps:
        ```

    ??? variable list "`dashy_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        dashy_role_docker_device_write_iops:
        ```

    ??? variable list "`dashy_role_docker_devices`"

        ```yaml
        # Type: list
        dashy_role_docker_devices:
        ```

    ??? variable string "`dashy_role_docker_devices_default`"

        ```yaml
        # Type: string
        dashy_role_docker_devices_default:
        ```

    ??? variable list "`dashy_role_docker_groups`"

        ```yaml
        # Type: list
        dashy_role_docker_groups:
        ```

    ??? variable bool "`dashy_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_docker_privileged:
        ```

    ??? variable list "`dashy_role_docker_security_opts`"

        ```yaml
        # Type: list
        dashy_role_docker_security_opts:
        ```

    ??? variable string "`dashy_role_docker_user`"

        ```yaml
        # Type: string
        dashy_role_docker_user:
        ```

    ??? variable string "`dashy_role_docker_userns_mode`"

        ```yaml
        # Type: string
        dashy_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`dashy_role_docker_dns_opts`"

        ```yaml
        # Type: list
        dashy_role_docker_dns_opts:
        ```

    ??? variable list "`dashy_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        dashy_role_docker_dns_search_domains:
        ```

    ??? variable list "`dashy_role_docker_dns_servers`"

        ```yaml
        # Type: list
        dashy_role_docker_dns_servers:
        ```

    ??? variable string "`dashy_role_docker_domainname`"

        ```yaml
        # Type: string
        dashy_role_docker_domainname:
        ```

    ??? variable list "`dashy_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        dashy_role_docker_exposed_ports:
        ```

    ??? variable dict "`dashy_role_docker_hosts`"

        ```yaml
        # Type: dict
        dashy_role_docker_hosts:
        ```

    ??? variable bool "`dashy_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_docker_hosts_use_common:
        ```

    ??? variable string "`dashy_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        dashy_role_docker_ipc_mode:
        ```

    ??? variable list "`dashy_role_docker_links`"

        ```yaml
        # Type: list
        dashy_role_docker_links:
        ```

    ??? variable string "`dashy_role_docker_network_mode`"

        ```yaml
        # Type: string
        dashy_role_docker_network_mode:
        ```

    ??? variable string "`dashy_role_docker_pid_mode`"

        ```yaml
        # Type: string
        dashy_role_docker_pid_mode:
        ```

    ??? variable list "`dashy_role_docker_ports`"

        ```yaml
        # Type: list
        dashy_role_docker_ports:
        ```

    ??? variable string "`dashy_role_docker_uts`"

        ```yaml
        # Type: string
        dashy_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`dashy_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_docker_keep_volumes:
        ```

    ??? variable list "`dashy_role_docker_mounts`"

        ```yaml
        # Type: list
        dashy_role_docker_mounts:
        ```

    ??? variable dict "`dashy_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        dashy_role_docker_storage_opts:
        ```

    ??? variable list "`dashy_role_docker_tmpfs`"

        ```yaml
        # Type: list
        dashy_role_docker_tmpfs:
        ```

    ??? variable string "`dashy_role_docker_volume_driver`"

        ```yaml
        # Type: string
        dashy_role_docker_volume_driver:
        ```

    ??? variable list "`dashy_role_docker_volumes_from`"

        ```yaml
        # Type: list
        dashy_role_docker_volumes_from:
        ```

    ??? variable bool "`dashy_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_docker_volumes_global:
        ```

    ??? variable string "`dashy_role_docker_working_dir`"

        ```yaml
        # Type: string
        dashy_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`dashy_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_docker_auto_remove:
        ```

    ??? variable bool "`dashy_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_docker_cleanup:
        ```

    ??? variable string "`dashy_role_docker_force_kill`"

        ```yaml
        # Type: string
        dashy_role_docker_force_kill:
        ```

    ??? variable int "`dashy_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        dashy_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`dashy_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_docker_init:
        ```

    ??? variable string "`dashy_role_docker_kill_signal`"

        ```yaml
        # Type: string
        dashy_role_docker_kill_signal:
        ```

    ??? variable string "`dashy_role_docker_log_driver`"

        ```yaml
        # Type: string
        dashy_role_docker_log_driver:
        ```

    ??? variable dict "`dashy_role_docker_log_options`"

        ```yaml
        # Type: dict
        dashy_role_docker_log_options:
        ```

    ??? variable bool "`dashy_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_docker_oom_killer:
        ```

    ??? variable int "`dashy_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        dashy_role_docker_oom_score_adj:
        ```

    ??? variable bool "`dashy_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_docker_output_logs:
        ```

    ??? variable bool "`dashy_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_docker_paused:
        ```

    ??? variable bool "`dashy_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_docker_recreate:
        ```

    ??? variable int "`dashy_role_docker_restart_retries`"

        ```yaml
        # Type: int
        dashy_role_docker_restart_retries:
        ```

    ??? variable int "`dashy_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        dashy_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`dashy_role_docker_capabilities`"

        ```yaml
        # Type: list
        dashy_role_docker_capabilities:
        ```

    ??? variable string "`dashy_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        dashy_role_docker_cgroup_parent:
        ```

    ??? variable list "`dashy_role_docker_commands`"

        ```yaml
        # Type: list
        dashy_role_docker_commands:
        ```

    ??? variable int "`dashy_role_docker_create_timeout`"

        ```yaml
        # Type: int
        dashy_role_docker_create_timeout:
        ```

    ??? variable string "`dashy_role_docker_entrypoint`"

        ```yaml
        # Type: string
        dashy_role_docker_entrypoint:
        ```

    ??? variable string "`dashy_role_docker_env_file`"

        ```yaml
        # Type: string
        dashy_role_docker_env_file:
        ```

    ??? variable dict "`dashy_role_docker_envs`"

        ```yaml
        # Type: dict
        dashy_role_docker_envs:
        ```

    ??? variable dict "`dashy_role_docker_labels`"

        ```yaml
        # Type: dict
        dashy_role_docker_labels:
        ```

    ??? variable bool "`dashy_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_docker_labels_use_common:
        ```

    ??? variable bool "`dashy_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_docker_read_only:
        ```

    ??? variable string "`dashy_role_docker_runtime`"

        ```yaml
        # Type: string
        dashy_role_docker_runtime:
        ```

    ??? variable list "`dashy_role_docker_sysctls`"

        ```yaml
        # Type: list
        dashy_role_docker_sysctls:
        ```

    ??? variable list "`dashy_role_docker_ulimits`"

        ```yaml
        # Type: list
        dashy_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`dashy_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        dashy_role_autoheal_enabled: true
        ```

    ??? variable string "`dashy_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        dashy_role_depends_on: ""
        ```

    ??? variable string "`dashy_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        dashy_role_depends_on_delay: "0"
        ```

    ??? variable string "`dashy_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        dashy_role_depends_on_healthchecks:
        ```

    ??? variable bool "`dashy_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        dashy_role_diun_enabled: true
        ```

    ??? variable bool "`dashy_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        dashy_role_dns_enabled: true
        ```

    ??? variable bool "`dashy_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        dashy_role_docker_controller: true
        ```

    ??? variable string "`dashy_role_docker_image_repo`"

        ```yaml
        # Type: string
        dashy_role_docker_image_repo:
        ```

    ??? variable string "`dashy_role_docker_image_tag`"

        ```yaml
        # Type: string
        dashy_role_docker_image_tag:
        ```

    ??? variable bool "`dashy_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_docker_volumes_download:
        ```

    ??? variable string "`dashy_role_paths_location`"

        ```yaml
        # Type: string
        dashy_role_paths_location:
        ```

    ??? variable string "`dashy_role_themepark_addons`"

        ```yaml
        # Type: string
        dashy_role_themepark_addons:
        ```

    ??? variable string "`dashy_role_themepark_app`"

        ```yaml
        # Type: string
        dashy_role_themepark_app:
        ```

    ??? variable string "`dashy_role_themepark_theme`"

        ```yaml
        # Type: string
        dashy_role_themepark_theme:
        ```

    ??? variable dict/omit "`dashy_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        dashy_role_traefik_api_endpoint:
        ```

    ??? variable string "`dashy_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        dashy_role_traefik_api_middleware:
        ```

    ??? variable string "`dashy_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        dashy_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`dashy_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        dashy_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`dashy_role_traefik_certresolver`"

        ```yaml
        # Type: string
        dashy_role_traefik_certresolver:
        ```

    ??? variable bool "`dashy_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        dashy_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`dashy_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        dashy_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`dashy_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        dashy_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`dashy_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        dashy_role_traefik_middleware_http:
        ```

    ??? variable bool "`dashy_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`dashy_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        dashy_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`dashy_role_traefik_priority`"

        ```yaml
        # Type: string
        dashy_role_traefik_priority:
        ```

    ??? variable bool "`dashy_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        dashy_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`dashy_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        dashy_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`dashy_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        dashy_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`dashy_role_web_domain`"

        ```yaml
        # Type: string
        dashy_role_web_domain:
        ```

    ??? variable list "`dashy_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        dashy_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            dashy_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "dashy2.{{ user.domain }}"
              - "dashy.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`dashy_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        dashy_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            dashy_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'dashy2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`dashy_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        dashy_role_web_http_port:
        ```

    ??? variable string "`dashy_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        dashy_role_web_http_scheme:
        ```

    ??? variable dict/omit "`dashy_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        dashy_role_web_http_serverstransport:
        ```

    ??? variable string "`dashy_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        dashy_role_web_scheme:
        ```

    ??? variable dict/omit "`dashy_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        dashy_role_web_serverstransport:
        ```

    ??? variable string "`dashy_role_web_subdomain`"

        ```yaml
        # Type: string
        dashy_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
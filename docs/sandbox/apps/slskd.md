---
icon: material/docker
status: draft2
hide:
  - tags
tags:
  - slskd
saltbox_automation:
  app_links:
    - name: Manual
      url:
      type: documentation
    - name: Releases
      url:
      type: github
    - name: Community
      url:
      type: community
  project_description:
    name:
    summary:
    link:
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# 

## Overview

 is 

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-slskd
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        slskd_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `slskd_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `slskd_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`slskd_name`"

        ```yaml
        # Type: string
        slskd_name: slskd
        ```

=== "Web"

    ??? variable string "`slskd_role_web_subdomain`"

        ```yaml
        # Type: string
        slskd_role_web_subdomain: "{{ slskd_name }}"
        ```

    ??? variable string "`slskd_role_web_domain`"

        ```yaml
        # Type: string
        slskd_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`slskd_role_web_port`"

        ```yaml
        # Type: string
        slskd_role_web_port: "5030"
        ```

    ??? variable string "`slskd_role_web_url`"

        ```yaml
        # Type: string
        slskd_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='slskd') + '.' + lookup('role_var', '_web_domain', role='slskd')
                             if (lookup('role_var', '_web_subdomain', role='slskd') | length > 0)
                             else lookup('role_var', '_web_domain', role='slskd')) }}"
        ```

=== "DNS"

    ??? variable string "`slskd_role_dns_record`"

        ```yaml
        # Type: string
        slskd_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='slskd') }}"
        ```

    ??? variable string "`slskd_role_dns_zone`"

        ```yaml
        # Type: string
        slskd_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='slskd') }}"
        ```

    ??? variable bool "`slskd_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`slskd_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        slskd_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`slskd_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        slskd_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`slskd_role_traefik_certresolver`"

        ```yaml
        # Type: string
        slskd_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable string "`slskd_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        slskd_role_traefik_middleware_custom: ""
        ```

    ??? variable bool "`slskd_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_traefik_enabled: true
        ```

    ??? variable bool "`slskd_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_traefik_api_enabled: false
        ```

    ??? variable string "`slskd_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        slskd_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`slskd_role_docker_container`"

        ```yaml
        # Type: string
        slskd_role_docker_container: "{{ slskd_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`slskd_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_docker_image_pull: true
        ```

    ??? variable string "`slskd_role_docker_image_repo`"

        ```yaml
        # Type: string
        slskd_role_docker_image_repo: "ghcr.io/slskd/slskd"
        ```

    ??? variable string "`slskd_role_docker_image_tag`"

        ```yaml
        # Type: string
        slskd_role_docker_image_tag: "latest"
        ```

    ??? variable string "`slskd_role_docker_image`"

        ```yaml
        # Type: string
        slskd_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='slskd') }}:{{ lookup('role_var', '_docker_image_tag', role='slskd') }}"
        ```

    <h5>Ports</h5>

    ??? variable list "`slskd_role_docker_ports_default`"

        ```yaml
        # Type: list
        slskd_role_docker_ports_default:
          - "50300:50300"
        ```

    ??? variable list "`slskd_role_docker_ports_custom`"

        ```yaml
        # Type: list
        slskd_role_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    ??? variable dict "`slskd_role_docker_envs_default`"

        ```yaml
        # Type: dict
        slskd_role_docker_envs_default:
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`slskd_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        slskd_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`slskd_role_docker_volumes_default`"

        ```yaml
        # Type: list
        slskd_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='slskd') }}:/app"
        ```

    ??? variable list "`slskd_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        slskd_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`slskd_role_docker_hostname`"

        ```yaml
        # Type: string
        slskd_role_docker_hostname: "{{ slskd_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`slskd_role_docker_networks_alias`"

        ```yaml
        # Type: string
        slskd_role_docker_networks_alias: "{{ slskd_name }}"
        ```

    ??? variable list "`slskd_role_docker_networks_default`"

        ```yaml
        # Type: list
        slskd_role_docker_networks_default: []
        ```

    ??? variable list "`slskd_role_docker_networks_custom`"

        ```yaml
        # Type: list
        slskd_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`slskd_role_docker_restart_policy`"

        ```yaml
        # Type: string
        slskd_role_docker_restart_policy: unless-stopped
        ```

    <h5>User</h5>

    ??? variable string "`slskd_role_docker_user`"

        ```yaml
        # Type: string
        slskd_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`slskd_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        slskd_role_docker_blkio_weight:
        ```

    ??? variable int "`slskd_role_docker_cpu_period`"

        ```yaml
        # Type: int
        slskd_role_docker_cpu_period:
        ```

    ??? variable int "`slskd_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        slskd_role_docker_cpu_quota:
        ```

    ??? variable int "`slskd_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        slskd_role_docker_cpu_shares:
        ```

    ??? variable string "`slskd_role_docker_cpus`"

        ```yaml
        # Type: string
        slskd_role_docker_cpus:
        ```

    ??? variable string "`slskd_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        slskd_role_docker_cpuset_cpus:
        ```

    ??? variable string "`slskd_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        slskd_role_docker_cpuset_mems:
        ```

    ??? variable string "`slskd_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        slskd_role_docker_kernel_memory:
        ```

    ??? variable string "`slskd_role_docker_memory`"

        ```yaml
        # Type: string
        slskd_role_docker_memory:
        ```

    ??? variable string "`slskd_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        slskd_role_docker_memory_reservation:
        ```

    ??? variable string "`slskd_role_docker_memory_swap`"

        ```yaml
        # Type: string
        slskd_role_docker_memory_swap:
        ```

    ??? variable int "`slskd_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        slskd_role_docker_memory_swappiness:
        ```

    ??? variable string "`slskd_role_docker_shm_size`"

        ```yaml
        # Type: string
        slskd_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`slskd_role_docker_cap_drop`"

        ```yaml
        # Type: list
        slskd_role_docker_cap_drop:
        ```

    ??? variable string "`slskd_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        slskd_role_docker_cgroupns_mode:
        ```

    ??? variable list "`slskd_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        slskd_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`slskd_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        slskd_role_docker_device_read_bps:
        ```

    ??? variable list "`slskd_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        slskd_role_docker_device_read_iops:
        ```

    ??? variable list "`slskd_role_docker_device_requests`"

        ```yaml
        # Type: list
        slskd_role_docker_device_requests:
        ```

    ??? variable list "`slskd_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        slskd_role_docker_device_write_bps:
        ```

    ??? variable list "`slskd_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        slskd_role_docker_device_write_iops:
        ```

    ??? variable list "`slskd_role_docker_devices`"

        ```yaml
        # Type: list
        slskd_role_docker_devices:
        ```

    ??? variable list "`slskd_role_docker_groups`"

        ```yaml
        # Type: list
        slskd_role_docker_groups:
        ```

    ??? variable bool "`slskd_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_docker_privileged:
        ```

    ??? variable list "`slskd_role_docker_security_opts`"

        ```yaml
        # Type: list
        slskd_role_docker_security_opts:
        ```

    ??? variable string "`slskd_role_docker_userns_mode`"

        ```yaml
        # Type: string
        slskd_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`slskd_role_docker_dns_opts`"

        ```yaml
        # Type: list
        slskd_role_docker_dns_opts:
        ```

    ??? variable list "`slskd_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        slskd_role_docker_dns_search_domains:
        ```

    ??? variable list "`slskd_role_docker_dns_servers`"

        ```yaml
        # Type: list
        slskd_role_docker_dns_servers:
        ```

    ??? variable string "`slskd_role_docker_domainname`"

        ```yaml
        # Type: string
        slskd_role_docker_domainname:
        ```

    ??? variable list "`slskd_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        slskd_role_docker_exposed_ports:
        ```

    ??? variable dict "`slskd_role_docker_hosts`"

        ```yaml
        # Type: dict
        slskd_role_docker_hosts:
        ```

    ??? variable bool "`slskd_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_docker_hosts_use_common:
        ```

    ??? variable string "`slskd_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        slskd_role_docker_ipc_mode:
        ```

    ??? variable list "`slskd_role_docker_links`"

        ```yaml
        # Type: list
        slskd_role_docker_links:
        ```

    ??? variable string "`slskd_role_docker_network_mode`"

        ```yaml
        # Type: string
        slskd_role_docker_network_mode:
        ```

    ??? variable string "`slskd_role_docker_pid_mode`"

        ```yaml
        # Type: string
        slskd_role_docker_pid_mode:
        ```

    ??? variable string "`slskd_role_docker_uts`"

        ```yaml
        # Type: string
        slskd_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`slskd_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_docker_keep_volumes:
        ```

    ??? variable list "`slskd_role_docker_mounts`"

        ```yaml
        # Type: list
        slskd_role_docker_mounts:
        ```

    ??? variable dict "`slskd_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        slskd_role_docker_storage_opts:
        ```

    ??? variable list "`slskd_role_docker_tmpfs`"

        ```yaml
        # Type: list
        slskd_role_docker_tmpfs:
        ```

    ??? variable string "`slskd_role_docker_volume_driver`"

        ```yaml
        # Type: string
        slskd_role_docker_volume_driver:
        ```

    ??? variable list "`slskd_role_docker_volumes_from`"

        ```yaml
        # Type: list
        slskd_role_docker_volumes_from:
        ```

    ??? variable bool "`slskd_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_docker_volumes_global:
        ```

    ??? variable string "`slskd_role_docker_working_dir`"

        ```yaml
        # Type: string
        slskd_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`slskd_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_docker_auto_remove:
        ```

    ??? variable bool "`slskd_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_docker_cleanup:
        ```

    ??? variable string "`slskd_role_docker_force_kill`"

        ```yaml
        # Type: string
        slskd_role_docker_force_kill:
        ```

    ??? variable dict "`slskd_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        slskd_role_docker_healthcheck:
        ```

    ??? variable int "`slskd_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        slskd_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`slskd_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_docker_init:
        ```

    ??? variable string "`slskd_role_docker_kill_signal`"

        ```yaml
        # Type: string
        slskd_role_docker_kill_signal:
        ```

    ??? variable string "`slskd_role_docker_log_driver`"

        ```yaml
        # Type: string
        slskd_role_docker_log_driver:
        ```

    ??? variable dict "`slskd_role_docker_log_options`"

        ```yaml
        # Type: dict
        slskd_role_docker_log_options:
        ```

    ??? variable bool "`slskd_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_docker_oom_killer:
        ```

    ??? variable int "`slskd_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        slskd_role_docker_oom_score_adj:
        ```

    ??? variable bool "`slskd_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_docker_output_logs:
        ```

    ??? variable bool "`slskd_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_docker_paused:
        ```

    ??? variable bool "`slskd_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_docker_recreate:
        ```

    ??? variable int "`slskd_role_docker_restart_retries`"

        ```yaml
        # Type: int
        slskd_role_docker_restart_retries:
        ```

    ??? variable string "`slskd_role_docker_stop_signal`"

        ```yaml
        # Type: string
        slskd_role_docker_stop_signal:
        ```

    ??? variable int "`slskd_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        slskd_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`slskd_role_docker_capabilities`"

        ```yaml
        # Type: list
        slskd_role_docker_capabilities:
        ```

    ??? variable string "`slskd_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        slskd_role_docker_cgroup_parent:
        ```

    ??? variable list "`slskd_role_docker_commands`"

        ```yaml
        # Type: list
        slskd_role_docker_commands:
        ```

    ??? variable int "`slskd_role_docker_create_timeout`"

        ```yaml
        # Type: int
        slskd_role_docker_create_timeout:
        ```

    ??? variable string "`slskd_role_docker_entrypoint`"

        ```yaml
        # Type: string
        slskd_role_docker_entrypoint:
        ```

    ??? variable string "`slskd_role_docker_env_file`"

        ```yaml
        # Type: string
        slskd_role_docker_env_file:
        ```

    ??? variable dict "`slskd_role_docker_labels`"

        ```yaml
        # Type: dict
        slskd_role_docker_labels:
        ```

    ??? variable bool "`slskd_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_docker_labels_use_common:
        ```

    ??? variable bool "`slskd_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_docker_read_only:
        ```

    ??? variable string "`slskd_role_docker_runtime`"

        ```yaml
        # Type: string
        slskd_role_docker_runtime:
        ```

    ??? variable list "`slskd_role_docker_sysctls`"

        ```yaml
        # Type: list
        slskd_role_docker_sysctls:
        ```

    ??? variable list "`slskd_role_docker_ulimits`"

        ```yaml
        # Type: list
        slskd_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`slskd_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        slskd_role_autoheal_enabled: true
        ```

    ??? variable string "`slskd_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        slskd_role_depends_on: ""
        ```

    ??? variable string "`slskd_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        slskd_role_depends_on_delay: "0"
        ```

    ??? variable string "`slskd_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        slskd_role_depends_on_healthchecks:
        ```

    ??? variable bool "`slskd_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        slskd_role_diun_enabled: true
        ```

    ??? variable bool "`slskd_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        slskd_role_dns_enabled: true
        ```

    ??? variable bool "`slskd_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        slskd_role_docker_controller: true
        ```

    ??? variable list "`slskd_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        slskd_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`slskd_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_docker_volumes_download:
        ```

    ??? variable string "`slskd_role_themepark_addons`"

        ```yaml
        # Type: string
        slskd_role_themepark_addons:
        ```

    ??? variable string "`slskd_role_themepark_app`"

        ```yaml
        # Type: string
        slskd_role_themepark_app:
        ```

    ??? variable string "`slskd_role_themepark_theme`"

        ```yaml
        # Type: string
        slskd_role_themepark_theme:
        ```

    ??? variable string "`slskd_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        slskd_role_traefik_api_middleware:
        ```

    ??? variable string "`slskd_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        slskd_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`slskd_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        slskd_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`slskd_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        slskd_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`slskd_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        slskd_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`slskd_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        slskd_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`slskd_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        slskd_role_traefik_middleware_http:
        ```

    ??? variable bool "`slskd_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`slskd_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        slskd_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`slskd_role_traefik_priority`"

        ```yaml
        # Type: string
        slskd_role_traefik_priority:
        ```

    ??? variable bool "`slskd_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        slskd_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`slskd_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        slskd_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`slskd_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        slskd_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`slskd_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        slskd_role_web_api_http_port:
        ```

    ??? variable string "`slskd_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        slskd_role_web_api_http_scheme:
        ```

    ??? variable dict "`slskd_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        slskd_role_web_api_http_serverstransport:
        ```

    ??? variable string "`slskd_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        slskd_role_web_api_port:
        ```

    ??? variable string "`slskd_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        slskd_role_web_api_scheme:
        ```

    ??? variable dict "`slskd_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        slskd_role_web_api_serverstransport:
        ```

    ??? variable list "`slskd_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        slskd_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            slskd_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "slskd2.{{ user.domain }}"
              - "slskd.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`slskd_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        slskd_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            slskd_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'slskd2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`slskd_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        slskd_role_web_http_port:
        ```

    ??? variable string "`slskd_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        slskd_role_web_http_scheme:
        ```

    ??? variable dict "`slskd_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        slskd_role_web_http_serverstransport:
        ```

    ??? variable string "`slskd_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        slskd_role_web_scheme:
        ```

    ??? variable dict "`slskd_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        slskd_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

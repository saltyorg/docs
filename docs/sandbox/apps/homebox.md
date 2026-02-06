---
icon: material/docker
hide:
  - tags
tags:
  - homebox
  - productivity
  - inventory
saltbox_automation:
  app_links:
    - name: Manual
      url: https://homebox.software/en/quick-start.html
      type: documentation
    - name: Releases
      url:
      type: releases
    - name: Community
      url:
      type: community
  project_description:
    name: Homebox
    summary: |-
      the inventory and organization system built for the Home User! With a focus on simplicity and ease of use, Homebox is the perfect solution for your home inventory, organization, and management needs.
    link: https://homebox.software/en/
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Homebox

## Overview

[Homebox](https://homebox.software/en/) is the inventory and organization system built for the Home User! With a focus on simplicity and ease of use, Homebox is the perfect solution for your home inventory, organization, and management needs.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://homebox.software/en/quick-start.html){ .md-button .md-button--stretch }

[:fontawesome-solid-newspaper:**Releases**](){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-homebox
```

## Usage

Visit <https://homebox.iYOUR_DOMAIN_NAMEi>.

## Basics

- Create a user in the web ui, add your email and password, then log in.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        homebox_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `homebox_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `homebox_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`homebox_name`"

        ```yaml
        # Type: string
        homebox_name: homebox
        ```

=== "Web"

    ??? variable string "`homebox_role_web_subdomain`"

        ```yaml
        # Type: string
        homebox_role_web_subdomain: "{{ homebox_name }}"
        ```

    ??? variable string "`homebox_role_web_domain`"

        ```yaml
        # Type: string
        homebox_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`homebox_role_web_port`"

        ```yaml
        # Type: string
        homebox_role_web_port: "7745"
        ```

    ??? variable string "`homebox_role_web_url`"

        ```yaml
        # Type: string
        homebox_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='homebox') + '.' + lookup('role_var', '_web_domain', role='homebox')
                               if (lookup('role_var', '_web_subdomain', role='homebox') | length > 0)
                               else lookup('role_var', '_web_domain', role='homebox')) }}"
        ```

=== "DNS"

    ??? variable string "`homebox_role_dns_record`"

        ```yaml
        # Type: string
        homebox_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='homebox') }}"
        ```

    ??? variable string "`homebox_role_dns_zone`"

        ```yaml
        # Type: string
        homebox_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='homebox') }}"
        ```

    ??? variable bool "`homebox_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`homebox_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        homebox_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`homebox_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        homebox_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`homebox_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        homebox_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`homebox_role_traefik_certresolver`"

        ```yaml
        # Type: string
        homebox_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`homebox_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_traefik_enabled: true
        ```

    ??? variable bool "`homebox_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_traefik_api_enabled: false
        ```

    ??? variable string "`homebox_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        homebox_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`homebox_role_docker_container`"

        ```yaml
        # Type: string
        homebox_role_docker_container: "{{ homebox_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`homebox_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_docker_image_pull: true
        ```

    ??? variable string "`homebox_role_docker_image_repo`"

        ```yaml
        # Type: string
        homebox_role_docker_image_repo: "ghcr.io/sysadminsmedia/homebox"
        ```

    ??? variable string "`homebox_role_docker_image_tag`"

        ```yaml
        # Type: string
        homebox_role_docker_image_tag: "latest"
        ```

    ??? variable string "`homebox_role_docker_image`"

        ```yaml
        # Type: string
        homebox_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='homebox') }}:{{ lookup('role_var', '_docker_image_tag', role='homebox') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`homebox_role_docker_envs_default`"

        ```yaml
        # Type: dict
        homebox_role_docker_envs_default:
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          HBOX_LOG_LEVEL: "info"
          HBOX_SWAGGER_SCHEMA: "https"
        ```

    ??? variable dict "`homebox_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        homebox_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`homebox_role_docker_volumes_default`"

        ```yaml
        # Type: list
        homebox_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='homebox') }}:/data"
        ```

    ??? variable list "`homebox_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        homebox_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`homebox_role_docker_hostname`"

        ```yaml
        # Type: string
        homebox_role_docker_hostname: "{{ homebox_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`homebox_role_docker_networks_alias`"

        ```yaml
        # Type: string
        homebox_role_docker_networks_alias: "{{ homebox_name }}"
        ```

    ??? variable list "`homebox_role_docker_networks_default`"

        ```yaml
        # Type: list
        homebox_role_docker_networks_default: []
        ```

    ??? variable list "`homebox_role_docker_networks_custom`"

        ```yaml
        # Type: list
        homebox_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`homebox_role_docker_restart_policy`"

        ```yaml
        # Type: string
        homebox_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`homebox_role_docker_state`"

        ```yaml
        # Type: string
        homebox_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`homebox_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        homebox_role_docker_blkio_weight:
        ```

    ??? variable int "`homebox_role_docker_cpu_period`"

        ```yaml
        # Type: int
        homebox_role_docker_cpu_period:
        ```

    ??? variable int "`homebox_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        homebox_role_docker_cpu_quota:
        ```

    ??? variable int "`homebox_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        homebox_role_docker_cpu_shares:
        ```

    ??? variable string "`homebox_role_docker_cpus`"

        ```yaml
        # Type: string
        homebox_role_docker_cpus:
        ```

    ??? variable string "`homebox_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        homebox_role_docker_cpuset_cpus:
        ```

    ??? variable string "`homebox_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        homebox_role_docker_cpuset_mems:
        ```

    ??? variable string "`homebox_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        homebox_role_docker_kernel_memory:
        ```

    ??? variable string "`homebox_role_docker_memory`"

        ```yaml
        # Type: string
        homebox_role_docker_memory:
        ```

    ??? variable string "`homebox_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        homebox_role_docker_memory_reservation:
        ```

    ??? variable string "`homebox_role_docker_memory_swap`"

        ```yaml
        # Type: string
        homebox_role_docker_memory_swap:
        ```

    ??? variable int "`homebox_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        homebox_role_docker_memory_swappiness:
        ```

    ??? variable string "`homebox_role_docker_shm_size`"

        ```yaml
        # Type: string
        homebox_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`homebox_role_docker_cap_drop`"

        ```yaml
        # Type: list
        homebox_role_docker_cap_drop:
        ```

    ??? variable string "`homebox_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        homebox_role_docker_cgroupns_mode:
        ```

    ??? variable list "`homebox_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        homebox_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`homebox_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        homebox_role_docker_device_read_bps:
        ```

    ??? variable list "`homebox_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        homebox_role_docker_device_read_iops:
        ```

    ??? variable list "`homebox_role_docker_device_requests`"

        ```yaml
        # Type: list
        homebox_role_docker_device_requests:
        ```

    ??? variable list "`homebox_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        homebox_role_docker_device_write_bps:
        ```

    ??? variable list "`homebox_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        homebox_role_docker_device_write_iops:
        ```

    ??? variable list "`homebox_role_docker_devices`"

        ```yaml
        # Type: list
        homebox_role_docker_devices:
        ```

    ??? variable list "`homebox_role_docker_groups`"

        ```yaml
        # Type: list
        homebox_role_docker_groups:
        ```

    ??? variable bool "`homebox_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_docker_privileged:
        ```

    ??? variable list "`homebox_role_docker_security_opts`"

        ```yaml
        # Type: list
        homebox_role_docker_security_opts:
        ```

    ??? variable string "`homebox_role_docker_user`"

        ```yaml
        # Type: string
        homebox_role_docker_user:
        ```

    ??? variable string "`homebox_role_docker_userns_mode`"

        ```yaml
        # Type: string
        homebox_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`homebox_role_docker_dns_opts`"

        ```yaml
        # Type: list
        homebox_role_docker_dns_opts:
        ```

    ??? variable list "`homebox_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        homebox_role_docker_dns_search_domains:
        ```

    ??? variable list "`homebox_role_docker_dns_servers`"

        ```yaml
        # Type: list
        homebox_role_docker_dns_servers:
        ```

    ??? variable string "`homebox_role_docker_domainname`"

        ```yaml
        # Type: string
        homebox_role_docker_domainname:
        ```

    ??? variable list "`homebox_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        homebox_role_docker_exposed_ports:
        ```

    ??? variable dict "`homebox_role_docker_hosts`"

        ```yaml
        # Type: dict
        homebox_role_docker_hosts:
        ```

    ??? variable bool "`homebox_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_docker_hosts_use_common:
        ```

    ??? variable string "`homebox_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        homebox_role_docker_ipc_mode:
        ```

    ??? variable list "`homebox_role_docker_links`"

        ```yaml
        # Type: list
        homebox_role_docker_links:
        ```

    ??? variable string "`homebox_role_docker_network_mode`"

        ```yaml
        # Type: string
        homebox_role_docker_network_mode:
        ```

    ??? variable string "`homebox_role_docker_pid_mode`"

        ```yaml
        # Type: string
        homebox_role_docker_pid_mode:
        ```

    ??? variable list "`homebox_role_docker_ports`"

        ```yaml
        # Type: list
        homebox_role_docker_ports:
        ```

    ??? variable string "`homebox_role_docker_uts`"

        ```yaml
        # Type: string
        homebox_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`homebox_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_docker_keep_volumes:
        ```

    ??? variable list "`homebox_role_docker_mounts`"

        ```yaml
        # Type: list
        homebox_role_docker_mounts:
        ```

    ??? variable dict "`homebox_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        homebox_role_docker_storage_opts:
        ```

    ??? variable list "`homebox_role_docker_tmpfs`"

        ```yaml
        # Type: list
        homebox_role_docker_tmpfs:
        ```

    ??? variable string "`homebox_role_docker_volume_driver`"

        ```yaml
        # Type: string
        homebox_role_docker_volume_driver:
        ```

    ??? variable list "`homebox_role_docker_volumes_from`"

        ```yaml
        # Type: list
        homebox_role_docker_volumes_from:
        ```

    ??? variable bool "`homebox_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_docker_volumes_global:
        ```

    ??? variable string "`homebox_role_docker_working_dir`"

        ```yaml
        # Type: string
        homebox_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`homebox_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_docker_auto_remove:
        ```

    ??? variable bool "`homebox_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_docker_cleanup:
        ```

    ??? variable string "`homebox_role_docker_force_kill`"

        ```yaml
        # Type: string
        homebox_role_docker_force_kill:
        ```

    ??? variable dict "`homebox_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        homebox_role_docker_healthcheck:
        ```

    ??? variable int "`homebox_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        homebox_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`homebox_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_docker_init:
        ```

    ??? variable string "`homebox_role_docker_kill_signal`"

        ```yaml
        # Type: string
        homebox_role_docker_kill_signal:
        ```

    ??? variable string "`homebox_role_docker_log_driver`"

        ```yaml
        # Type: string
        homebox_role_docker_log_driver:
        ```

    ??? variable dict "`homebox_role_docker_log_options`"

        ```yaml
        # Type: dict
        homebox_role_docker_log_options:
        ```

    ??? variable bool "`homebox_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_docker_oom_killer:
        ```

    ??? variable int "`homebox_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        homebox_role_docker_oom_score_adj:
        ```

    ??? variable bool "`homebox_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_docker_output_logs:
        ```

    ??? variable bool "`homebox_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_docker_paused:
        ```

    ??? variable bool "`homebox_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_docker_recreate:
        ```

    ??? variable int "`homebox_role_docker_restart_retries`"

        ```yaml
        # Type: int
        homebox_role_docker_restart_retries:
        ```

    ??? variable string "`homebox_role_docker_stop_signal`"

        ```yaml
        # Type: string
        homebox_role_docker_stop_signal:
        ```

    ??? variable int "`homebox_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        homebox_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`homebox_role_docker_capabilities`"

        ```yaml
        # Type: list
        homebox_role_docker_capabilities:
        ```

    ??? variable string "`homebox_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        homebox_role_docker_cgroup_parent:
        ```

    ??? variable list "`homebox_role_docker_commands`"

        ```yaml
        # Type: list
        homebox_role_docker_commands:
        ```

    ??? variable int "`homebox_role_docker_create_timeout`"

        ```yaml
        # Type: int
        homebox_role_docker_create_timeout:
        ```

    ??? variable string "`homebox_role_docker_dev_dri`"

        ```yaml
        # Type: string
        homebox_role_docker_dev_dri:
        ```

    ??? variable string "`homebox_role_docker_entrypoint`"

        ```yaml
        # Type: string
        homebox_role_docker_entrypoint:
        ```

    ??? variable string "`homebox_role_docker_env_file`"

        ```yaml
        # Type: string
        homebox_role_docker_env_file:
        ```

    ??? variable dict "`homebox_role_docker_labels`"

        ```yaml
        # Type: dict
        homebox_role_docker_labels:
        ```

    ??? variable bool "`homebox_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_docker_labels_use_common:
        ```

    ??? variable bool "`homebox_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_docker_read_only:
        ```

    ??? variable string "`homebox_role_docker_runtime`"

        ```yaml
        # Type: string
        homebox_role_docker_runtime:
        ```

    ??? variable list "`homebox_role_docker_sysctls`"

        ```yaml
        # Type: list
        homebox_role_docker_sysctls:
        ```

    ??? variable list "`homebox_role_docker_ulimits`"

        ```yaml
        # Type: list
        homebox_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`homebox_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        homebox_role_autoheal_enabled: true
        ```

    ??? variable string "`homebox_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        homebox_role_depends_on: ""
        ```

    ??? variable string "`homebox_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        homebox_role_depends_on_delay: "0"
        ```

    ??? variable string "`homebox_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        homebox_role_depends_on_healthchecks:
        ```

    ??? variable bool "`homebox_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        homebox_role_diun_enabled: true
        ```

    ??? variable bool "`homebox_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        homebox_role_dns_enabled: true
        ```

    ??? variable bool "`homebox_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        homebox_role_docker_controller: true
        ```

    ??? variable list "`homebox_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        homebox_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`homebox_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_docker_volumes_download:
        ```

    ??? variable string "`homebox_role_themepark_addons`"

        ```yaml
        # Type: string
        homebox_role_themepark_addons:
        ```

    ??? variable string "`homebox_role_themepark_app`"

        ```yaml
        # Type: string
        homebox_role_themepark_app:
        ```

    ??? variable string "`homebox_role_themepark_theme`"

        ```yaml
        # Type: string
        homebox_role_themepark_theme:
        ```

    ??? variable string "`homebox_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        homebox_role_traefik_api_middleware:
        ```

    ??? variable string "`homebox_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        homebox_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`homebox_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        homebox_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`homebox_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        homebox_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`homebox_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        homebox_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`homebox_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        homebox_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`homebox_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        homebox_role_traefik_middleware_http:
        ```

    ??? variable bool "`homebox_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`homebox_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`homebox_role_traefik_priority`"

        ```yaml
        # Type: string
        homebox_role_traefik_priority:
        ```

    ??? variable bool "`homebox_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        homebox_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`homebox_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        homebox_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`homebox_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        homebox_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`homebox_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        homebox_role_web_api_http_port:
        ```

    ??? variable string "`homebox_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        homebox_role_web_api_http_scheme:
        ```

    ??? variable dict "`homebox_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        homebox_role_web_api_http_serverstransport:
        ```

    ??? variable string "`homebox_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        homebox_role_web_api_port:
        ```

    ??? variable string "`homebox_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        homebox_role_web_api_scheme:
        ```

    ??? variable dict "`homebox_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        homebox_role_web_api_serverstransport:
        ```

    ??? variable list "`homebox_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        homebox_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            homebox_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "homebox2.{{ user.domain }}"
              - "homebox.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`homebox_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        homebox_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            homebox_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'homebox2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`homebox_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        homebox_role_web_http_port:
        ```

    ??? variable string "`homebox_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        homebox_role_web_http_scheme:
        ```

    ??? variable dict "`homebox_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        homebox_role_web_http_serverstransport:
        ```

    ??? variable string "`homebox_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        homebox_role_web_scheme:
        ```

    ??? variable dict "`homebox_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        homebox_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

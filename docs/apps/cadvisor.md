---
title: cAdvisor
icon: material/docker
hide:
  - tags
tags:
  - cadvisor
  - monitoring
  - docker
saltbox_automation:
  app_links:
    - name: Manual
      url: https://github.com/google/cadvisor/tree/master/docs
      type: documentation
    - name: Releases
      url: https://console.cloud.google.com/artifacts/docker/cadvisor/us/gcr.io/cadvisor
      type: releases
    - name: Community
      url:
      type: community
  project_description:
    name: cAdvisor
    summary: |-
      an open-source monitoring tool to collect, aggregate, process, and export resource usage and performance characteristics of running containers.
    link: https://github.com/google/cadvisor
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# cAdvisor

## Overview

[cAdvisor](https://github.com/google/cadvisor) is an open-source monitoring tool to collect, aggregate, process, and export resource usage and performance characteristics of running containers.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/google/cadvisor/tree/master/docs){ .md-button .md-button--stretch }

[:fontawesome-solid-newspaper:**Releases**](https://console.cloud.google.com/artifacts/docker/cadvisor/us/gcr.io/cadvisor){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install cadvisor
```

## Usage

Visit <https://cadvisor.iYOUR_DOMAIN_NAMEi>.

## Basics

cAdvisor automatically monitors all Docker containers on your system. No additional configuration is required. The web interface provides resource usage, performance metrics, and container information.

cAdvisor is often used with Prometheus and Grafana for advanced metrics collection and visualization.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        cadvisor_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `cadvisor_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `cadvisor_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`cadvisor_name`"

        ```yaml
        # Type: string
        cadvisor_name: cadvisor
        ```

=== "Web"

    ??? variable string "`cadvisor_role_web_subdomain`"

        ```yaml
        # Type: string
        cadvisor_role_web_subdomain: "{{ cadvisor_name }}"
        ```

    ??? variable string "`cadvisor_role_web_domain`"

        ```yaml
        # Type: string
        cadvisor_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`cadvisor_role_web_port`"

        ```yaml
        # Type: string
        cadvisor_role_web_port: "8080"
        ```

    ??? variable string "`cadvisor_role_web_url`"

        ```yaml
        # Type: string
        cadvisor_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='cadvisor') + '.' + lookup('role_var', '_web_domain', role='cadvisor')
                                if (lookup('role_var', '_web_subdomain', role='cadvisor') | length > 0)
                                else lookup('role_var', '_web_domain', role='cadvisor')) }}"
        ```

=== "DNS"

    ??? variable string "`cadvisor_role_dns_record`"

        ```yaml
        # Type: string
        cadvisor_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='cadvisor') }}"
        ```

    ??? variable string "`cadvisor_role_dns_zone`"

        ```yaml
        # Type: string
        cadvisor_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='cadvisor') }}"
        ```

    ??? variable bool "`cadvisor_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`cadvisor_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        cadvisor_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`cadvisor_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        cadvisor_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`cadvisor_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        cadvisor_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`cadvisor_role_traefik_certresolver`"

        ```yaml
        # Type: string
        cadvisor_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`cadvisor_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_traefik_enabled: true
        ```

    ??? variable bool "`cadvisor_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_traefik_api_enabled: false
        ```

    ??? variable string "`cadvisor_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        cadvisor_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`cadvisor_role_docker_container`"

        ```yaml
        # Type: string
        cadvisor_role_docker_container: "{{ cadvisor_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`cadvisor_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_docker_image_pull: true
        ```

    ??? variable string "`cadvisor_role_docker_image_repo`"

        ```yaml
        # Type: string
        cadvisor_role_docker_image_repo: "gcr.io/cadvisor/cadvisor"
        ```

    ??? variable string "`cadvisor_role_docker_image_tag`"

        ```yaml
        # Type: string
        cadvisor_role_docker_image_tag: "latest"
        ```

    ??? variable string "`cadvisor_role_docker_image`"

        ```yaml
        # Type: string
        cadvisor_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='cadvisor') }}:{{ lookup('role_var', '_docker_image_tag', role='cadvisor') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`cadvisor_role_docker_envs_default`"

        ```yaml
        # Type: dict
        cadvisor_role_docker_envs_default:
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`cadvisor_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        cadvisor_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`cadvisor_role_docker_volumes_default`"

        ```yaml
        # Type: list
        cadvisor_role_docker_volumes_default:
          - "/:/rootfs:ro"
          - "/var/run:/var/run:ro"
          - "/sys:/sys:ro"
          - "/var/lib/docker/:/var/lib/docker:ro"
          - "/dev/disk/:/dev/disk:ro"
        ```

    ??? variable list "`cadvisor_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        cadvisor_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`cadvisor_role_docker_hostname`"

        ```yaml
        # Type: string
        cadvisor_role_docker_hostname: "{{ cadvisor_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`cadvisor_role_docker_networks_alias`"

        ```yaml
        # Type: string
        cadvisor_role_docker_networks_alias: "{{ cadvisor_name }}"
        ```

    ??? variable list "`cadvisor_role_docker_networks_default`"

        ```yaml
        # Type: list
        cadvisor_role_docker_networks_default: []
        ```

    ??? variable list "`cadvisor_role_docker_networks_custom`"

        ```yaml
        # Type: list
        cadvisor_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`cadvisor_role_docker_restart_policy`"

        ```yaml
        # Type: string
        cadvisor_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`cadvisor_role_docker_state`"

        ```yaml
        # Type: string
        cadvisor_role_docker_state: started
        ```

    <h5>Privileged</h5>

    ??? variable bool "`cadvisor_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_docker_privileged: true
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`cadvisor_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        cadvisor_role_docker_blkio_weight:
        ```

    ??? variable int "`cadvisor_role_docker_cpu_period`"

        ```yaml
        # Type: int
        cadvisor_role_docker_cpu_period:
        ```

    ??? variable int "`cadvisor_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        cadvisor_role_docker_cpu_quota:
        ```

    ??? variable int "`cadvisor_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        cadvisor_role_docker_cpu_shares:
        ```

    ??? variable string "`cadvisor_role_docker_cpus`"

        ```yaml
        # Type: string
        cadvisor_role_docker_cpus:
        ```

    ??? variable string "`cadvisor_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        cadvisor_role_docker_cpuset_cpus:
        ```

    ??? variable string "`cadvisor_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        cadvisor_role_docker_cpuset_mems:
        ```

    ??? variable string "`cadvisor_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        cadvisor_role_docker_kernel_memory:
        ```

    ??? variable string "`cadvisor_role_docker_memory`"

        ```yaml
        # Type: string
        cadvisor_role_docker_memory:
        ```

    ??? variable string "`cadvisor_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        cadvisor_role_docker_memory_reservation:
        ```

    ??? variable string "`cadvisor_role_docker_memory_swap`"

        ```yaml
        # Type: string
        cadvisor_role_docker_memory_swap:
        ```

    ??? variable int "`cadvisor_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        cadvisor_role_docker_memory_swappiness:
        ```

    ??? variable string "`cadvisor_role_docker_shm_size`"

        ```yaml
        # Type: string
        cadvisor_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`cadvisor_role_docker_cap_drop`"

        ```yaml
        # Type: list
        cadvisor_role_docker_cap_drop:
        ```

    ??? variable string "`cadvisor_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        cadvisor_role_docker_cgroupns_mode:
        ```

    ??? variable list "`cadvisor_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        cadvisor_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`cadvisor_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        cadvisor_role_docker_device_read_bps:
        ```

    ??? variable list "`cadvisor_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        cadvisor_role_docker_device_read_iops:
        ```

    ??? variable list "`cadvisor_role_docker_device_requests`"

        ```yaml
        # Type: list
        cadvisor_role_docker_device_requests:
        ```

    ??? variable list "`cadvisor_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        cadvisor_role_docker_device_write_bps:
        ```

    ??? variable list "`cadvisor_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        cadvisor_role_docker_device_write_iops:
        ```

    ??? variable list "`cadvisor_role_docker_devices`"

        ```yaml
        # Type: list
        cadvisor_role_docker_devices:
        ```

    ??? variable list "`cadvisor_role_docker_groups`"

        ```yaml
        # Type: list
        cadvisor_role_docker_groups:
        ```

    ??? variable list "`cadvisor_role_docker_security_opts`"

        ```yaml
        # Type: list
        cadvisor_role_docker_security_opts:
        ```

    ??? variable string "`cadvisor_role_docker_user`"

        ```yaml
        # Type: string
        cadvisor_role_docker_user:
        ```

    ??? variable string "`cadvisor_role_docker_userns_mode`"

        ```yaml
        # Type: string
        cadvisor_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`cadvisor_role_docker_dns_opts`"

        ```yaml
        # Type: list
        cadvisor_role_docker_dns_opts:
        ```

    ??? variable list "`cadvisor_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        cadvisor_role_docker_dns_search_domains:
        ```

    ??? variable list "`cadvisor_role_docker_dns_servers`"

        ```yaml
        # Type: list
        cadvisor_role_docker_dns_servers:
        ```

    ??? variable string "`cadvisor_role_docker_domainname`"

        ```yaml
        # Type: string
        cadvisor_role_docker_domainname:
        ```

    ??? variable list "`cadvisor_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        cadvisor_role_docker_exposed_ports:
        ```

    ??? variable dict "`cadvisor_role_docker_hosts`"

        ```yaml
        # Type: dict
        cadvisor_role_docker_hosts:
        ```

    ??? variable bool "`cadvisor_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_docker_hosts_use_common:
        ```

    ??? variable string "`cadvisor_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        cadvisor_role_docker_ipc_mode:
        ```

    ??? variable list "`cadvisor_role_docker_links`"

        ```yaml
        # Type: list
        cadvisor_role_docker_links:
        ```

    ??? variable string "`cadvisor_role_docker_network_mode`"

        ```yaml
        # Type: string
        cadvisor_role_docker_network_mode:
        ```

    ??? variable string "`cadvisor_role_docker_pid_mode`"

        ```yaml
        # Type: string
        cadvisor_role_docker_pid_mode:
        ```

    ??? variable list "`cadvisor_role_docker_ports`"

        ```yaml
        # Type: list
        cadvisor_role_docker_ports:
        ```

    ??? variable string "`cadvisor_role_docker_uts`"

        ```yaml
        # Type: string
        cadvisor_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`cadvisor_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_docker_keep_volumes:
        ```

    ??? variable list "`cadvisor_role_docker_mounts`"

        ```yaml
        # Type: list
        cadvisor_role_docker_mounts:
        ```

    ??? variable dict "`cadvisor_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        cadvisor_role_docker_storage_opts:
        ```

    ??? variable list "`cadvisor_role_docker_tmpfs`"

        ```yaml
        # Type: list
        cadvisor_role_docker_tmpfs:
        ```

    ??? variable string "`cadvisor_role_docker_volume_driver`"

        ```yaml
        # Type: string
        cadvisor_role_docker_volume_driver:
        ```

    ??? variable list "`cadvisor_role_docker_volumes_from`"

        ```yaml
        # Type: list
        cadvisor_role_docker_volumes_from:
        ```

    ??? variable bool "`cadvisor_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_docker_volumes_global:
        ```

    ??? variable string "`cadvisor_role_docker_working_dir`"

        ```yaml
        # Type: string
        cadvisor_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`cadvisor_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_docker_auto_remove:
        ```

    ??? variable bool "`cadvisor_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_docker_cleanup:
        ```

    ??? variable string "`cadvisor_role_docker_force_kill`"

        ```yaml
        # Type: string
        cadvisor_role_docker_force_kill:
        ```

    ??? variable dict "`cadvisor_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        cadvisor_role_docker_healthcheck:
        ```

    ??? variable int "`cadvisor_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        cadvisor_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`cadvisor_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_docker_init:
        ```

    ??? variable string "`cadvisor_role_docker_kill_signal`"

        ```yaml
        # Type: string
        cadvisor_role_docker_kill_signal:
        ```

    ??? variable string "`cadvisor_role_docker_log_driver`"

        ```yaml
        # Type: string
        cadvisor_role_docker_log_driver:
        ```

    ??? variable dict "`cadvisor_role_docker_log_options`"

        ```yaml
        # Type: dict
        cadvisor_role_docker_log_options:
        ```

    ??? variable bool "`cadvisor_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_docker_oom_killer:
        ```

    ??? variable int "`cadvisor_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        cadvisor_role_docker_oom_score_adj:
        ```

    ??? variable bool "`cadvisor_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_docker_output_logs:
        ```

    ??? variable bool "`cadvisor_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_docker_paused:
        ```

    ??? variable bool "`cadvisor_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_docker_recreate:
        ```

    ??? variable int "`cadvisor_role_docker_restart_retries`"

        ```yaml
        # Type: int
        cadvisor_role_docker_restart_retries:
        ```

    ??? variable string "`cadvisor_role_docker_stop_signal`"

        ```yaml
        # Type: string
        cadvisor_role_docker_stop_signal:
        ```

    ??? variable int "`cadvisor_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        cadvisor_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`cadvisor_role_docker_capabilities`"

        ```yaml
        # Type: list
        cadvisor_role_docker_capabilities:
        ```

    ??? variable string "`cadvisor_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        cadvisor_role_docker_cgroup_parent:
        ```

    ??? variable list "`cadvisor_role_docker_commands`"

        ```yaml
        # Type: list
        cadvisor_role_docker_commands:
        ```

    ??? variable int "`cadvisor_role_docker_create_timeout`"

        ```yaml
        # Type: int
        cadvisor_role_docker_create_timeout:
        ```

    ??? variable string "`cadvisor_role_docker_entrypoint`"

        ```yaml
        # Type: string
        cadvisor_role_docker_entrypoint:
        ```

    ??? variable string "`cadvisor_role_docker_env_file`"

        ```yaml
        # Type: string
        cadvisor_role_docker_env_file:
        ```

    ??? variable dict "`cadvisor_role_docker_labels`"

        ```yaml
        # Type: dict
        cadvisor_role_docker_labels:
        ```

    ??? variable bool "`cadvisor_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_docker_labels_use_common:
        ```

    ??? variable bool "`cadvisor_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_docker_read_only:
        ```

    ??? variable string "`cadvisor_role_docker_runtime`"

        ```yaml
        # Type: string
        cadvisor_role_docker_runtime:
        ```

    ??? variable list "`cadvisor_role_docker_sysctls`"

        ```yaml
        # Type: list
        cadvisor_role_docker_sysctls:
        ```

    ??? variable list "`cadvisor_role_docker_ulimits`"

        ```yaml
        # Type: list
        cadvisor_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`cadvisor_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        cadvisor_role_autoheal_enabled: true
        ```

    ??? variable string "`cadvisor_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        cadvisor_role_depends_on: ""
        ```

    ??? variable string "`cadvisor_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        cadvisor_role_depends_on_delay: "0"
        ```

    ??? variable string "`cadvisor_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        cadvisor_role_depends_on_healthchecks:
        ```

    ??? variable bool "`cadvisor_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        cadvisor_role_diun_enabled: true
        ```

    ??? variable bool "`cadvisor_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        cadvisor_role_dns_enabled: true
        ```

    ??? variable bool "`cadvisor_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        cadvisor_role_docker_controller: true
        ```

    ??? variable list "`cadvisor_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        cadvisor_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`cadvisor_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_docker_volumes_download:
        ```

    ??? variable string "`cadvisor_role_themepark_addons`"

        ```yaml
        # Type: string
        cadvisor_role_themepark_addons:
        ```

    ??? variable string "`cadvisor_role_themepark_app`"

        ```yaml
        # Type: string
        cadvisor_role_themepark_app:
        ```

    ??? variable string "`cadvisor_role_themepark_theme`"

        ```yaml
        # Type: string
        cadvisor_role_themepark_theme:
        ```

    ??? variable string "`cadvisor_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        cadvisor_role_traefik_api_middleware:
        ```

    ??? variable string "`cadvisor_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        cadvisor_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`cadvisor_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        cadvisor_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`cadvisor_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        cadvisor_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`cadvisor_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        cadvisor_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`cadvisor_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        cadvisor_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`cadvisor_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        cadvisor_role_traefik_middleware_http:
        ```

    ??? variable bool "`cadvisor_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`cadvisor_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        cadvisor_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`cadvisor_role_traefik_priority`"

        ```yaml
        # Type: string
        cadvisor_role_traefik_priority:
        ```

    ??? variable bool "`cadvisor_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        cadvisor_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`cadvisor_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        cadvisor_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`cadvisor_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        cadvisor_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`cadvisor_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        cadvisor_role_web_api_http_port:
        ```

    ??? variable string "`cadvisor_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        cadvisor_role_web_api_http_scheme:
        ```

    ??? variable dict "`cadvisor_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        cadvisor_role_web_api_http_serverstransport:
        ```

    ??? variable string "`cadvisor_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        cadvisor_role_web_api_port:
        ```

    ??? variable string "`cadvisor_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        cadvisor_role_web_api_scheme:
        ```

    ??? variable dict "`cadvisor_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        cadvisor_role_web_api_serverstransport:
        ```

    ??? variable list "`cadvisor_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        cadvisor_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            cadvisor_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "cadvisor2.{{ user.domain }}"
              - "cadvisor.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`cadvisor_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        cadvisor_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            cadvisor_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'cadvisor2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`cadvisor_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        cadvisor_role_web_http_port:
        ```

    ??? variable string "`cadvisor_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        cadvisor_role_web_http_scheme:
        ```

    ??? variable dict "`cadvisor_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        cadvisor_role_web_http_serverstransport:
        ```

    ??? variable string "`cadvisor_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        cadvisor_role_web_scheme:
        ```

    ??? variable dict "`cadvisor_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        cadvisor_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

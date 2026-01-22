---
icon: material/docker
title: vaultwarden
hide:
  - tags
tags:
  - vaultwarden
  - passwords
  - security
saltbox_automation:
  app_links:
    - name: Manual
      url: https://github.com/dani-garcia/vaultwarden/wiki
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/vaultwarden/server/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: vaultwarden
    summary: |-
      an alternative implementation of the Bitwarden server API written in Rust and compatible with upstream Bitwarden clients*, perfect for self-hosted deployment where running the official resource-heavy service might not be ideal.
    link: https://github.com/dani-garcia/vaultwarden
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# vaultwarden

## Overview

[vaultwarden](https://github.com/dani-garcia/vaultwarden) is an alternative implementation of the Bitwarden server API written in Rust and compatible with upstream Bitwarden clients*, perfect for self-hosted deployment where running the official resource-heavy service might not be ideal.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/dani-garcia/vaultwarden/wiki){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/vaultwarden/server/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-vaultwarden
```

## Usage

Visit <https://vaultwarden.iYOUR_DOMAIN_NAMEi>.

## Basics

  1. Visit the vaultwarden site at <https://vaultwarden.iYOUR_DOMAIN_NAMEi>

  2. Sign up with any email address and password.

  3. To access the Admin Panel go to <https://vaultwarden.iYOUR_DOMAIN_NAMEi/admin>

  4. You will need to enter an authentication key which you can find in `/opt/vaultwarden/env`. Look for `ADMIN_TOKEN=`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        vaultwarden_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `vaultwarden_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `vaultwarden_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`vaultwarden_name`"

        ```yaml
        # Type: string
        vaultwarden_name: vaultwarden
        ```

=== "Web"

    ??? variable string "`vaultwarden_role_web_subdomain`"

        ```yaml
        # Type: string
        vaultwarden_role_web_subdomain: "{{ vaultwarden_name }}"
        ```

    ??? variable string "`vaultwarden_role_web_domain`"

        ```yaml
        # Type: string
        vaultwarden_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`vaultwarden_role_web_port`"

        ```yaml
        # Type: string
        vaultwarden_role_web_port: "6423"
        ```

    ??? variable string "`vaultwarden_role_web_url`"

        ```yaml
        # Type: string
        vaultwarden_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='vaultwarden') + '.' + lookup('role_var', '_web_domain', role='vaultwarden')
                                   if (lookup('role_var', '_web_subdomain', role='vaultwarden') | length > 0)
                                   else lookup('role_var', '_web_domain', role='vaultwarden')) }}"
        ```

=== "DNS"

    ??? variable string "`vaultwarden_role_dns_record`"

        ```yaml
        # Type: string
        vaultwarden_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='vaultwarden') }}"
        ```

    ??? variable string "`vaultwarden_role_dns_zone`"

        ```yaml
        # Type: string
        vaultwarden_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='vaultwarden') }}"
        ```

    ??? variable bool "`vaultwarden_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`vaultwarden_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        vaultwarden_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`vaultwarden_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        vaultwarden_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`vaultwarden_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        vaultwarden_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`vaultwarden_role_traefik_certresolver`"

        ```yaml
        # Type: string
        vaultwarden_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`vaultwarden_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_traefik_enabled: true
        ```

    ??? variable bool "`vaultwarden_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_traefik_api_enabled: false
        ```

    ??? variable string "`vaultwarden_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        vaultwarden_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`vaultwarden_role_docker_container`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_container: "{{ vaultwarden_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`vaultwarden_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_docker_image_pull: true
        ```

    ??? variable string "`vaultwarden_role_docker_image_repo`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_image_repo: "vaultwarden/server"
        ```

    ??? variable string "`vaultwarden_role_docker_image_tag`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_image_tag: "latest"
        ```

    ??? variable string "`vaultwarden_role_docker_image`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='vaultwarden') }}:{{ lookup('role_var', '_docker_image_tag', role='vaultwarden') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`vaultwarden_role_docker_envs_default`"

        ```yaml
        # Type: dict
        vaultwarden_role_docker_envs_default:
          TZ: "{{ tz }}"
          ROCKET_PORT: "{{ lookup('role_var', '_web_port', role='vaultwarden') }}"
        ```

    ??? variable dict "`vaultwarden_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        vaultwarden_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`vaultwarden_role_docker_volumes_default`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='vaultwarden') }}:/data"
          - "{{ lookup('role_var', '_paths_location', role='vaultwarden') }}/env:/.env"
        ```

    ??? variable list "`vaultwarden_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`vaultwarden_role_docker_hostname`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_hostname: "{{ vaultwarden_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`vaultwarden_role_docker_networks_alias`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_networks_alias: "{{ vaultwarden_name }}"
        ```

    ??? variable list "`vaultwarden_role_docker_networks_default`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_networks_default: []
        ```

    ??? variable list "`vaultwarden_role_docker_networks_custom`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`vaultwarden_role_docker_restart_policy`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`vaultwarden_role_docker_state`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`vaultwarden_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        vaultwarden_role_docker_blkio_weight:
        ```

    ??? variable int "`vaultwarden_role_docker_cpu_period`"

        ```yaml
        # Type: int
        vaultwarden_role_docker_cpu_period:
        ```

    ??? variable int "`vaultwarden_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        vaultwarden_role_docker_cpu_quota:
        ```

    ??? variable int "`vaultwarden_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        vaultwarden_role_docker_cpu_shares:
        ```

    ??? variable string "`vaultwarden_role_docker_cpus`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_cpus:
        ```

    ??? variable string "`vaultwarden_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_cpuset_cpus:
        ```

    ??? variable string "`vaultwarden_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_cpuset_mems:
        ```

    ??? variable string "`vaultwarden_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_kernel_memory:
        ```

    ??? variable string "`vaultwarden_role_docker_memory`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_memory:
        ```

    ??? variable string "`vaultwarden_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_memory_reservation:
        ```

    ??? variable string "`vaultwarden_role_docker_memory_swap`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_memory_swap:
        ```

    ??? variable int "`vaultwarden_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        vaultwarden_role_docker_memory_swappiness:
        ```

    ??? variable string "`vaultwarden_role_docker_shm_size`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`vaultwarden_role_docker_cap_drop`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_cap_drop:
        ```

    ??? variable string "`vaultwarden_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_cgroupns_mode:
        ```

    ??? variable list "`vaultwarden_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`vaultwarden_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_device_read_bps:
        ```

    ??? variable list "`vaultwarden_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_device_read_iops:
        ```

    ??? variable list "`vaultwarden_role_docker_device_requests`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_device_requests:
        ```

    ??? variable list "`vaultwarden_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_device_write_bps:
        ```

    ??? variable list "`vaultwarden_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_device_write_iops:
        ```

    ??? variable list "`vaultwarden_role_docker_devices`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_devices:
        ```

    ??? variable string "`vaultwarden_role_docker_devices_default`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_devices_default:
        ```

    ??? variable list "`vaultwarden_role_docker_groups`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_groups:
        ```

    ??? variable bool "`vaultwarden_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_docker_privileged:
        ```

    ??? variable list "`vaultwarden_role_docker_security_opts`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_security_opts:
        ```

    ??? variable string "`vaultwarden_role_docker_user`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_user:
        ```

    ??? variable string "`vaultwarden_role_docker_userns_mode`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`vaultwarden_role_docker_dns_opts`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_dns_opts:
        ```

    ??? variable list "`vaultwarden_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_dns_search_domains:
        ```

    ??? variable list "`vaultwarden_role_docker_dns_servers`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_dns_servers:
        ```

    ??? variable string "`vaultwarden_role_docker_domainname`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_domainname:
        ```

    ??? variable list "`vaultwarden_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_exposed_ports:
        ```

    ??? variable dict "`vaultwarden_role_docker_hosts`"

        ```yaml
        # Type: dict
        vaultwarden_role_docker_hosts:
        ```

    ??? variable bool "`vaultwarden_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_docker_hosts_use_common:
        ```

    ??? variable string "`vaultwarden_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_ipc_mode:
        ```

    ??? variable list "`vaultwarden_role_docker_links`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_links:
        ```

    ??? variable string "`vaultwarden_role_docker_network_mode`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_network_mode:
        ```

    ??? variable string "`vaultwarden_role_docker_pid_mode`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_pid_mode:
        ```

    ??? variable list "`vaultwarden_role_docker_ports`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_ports:
        ```

    ??? variable string "`vaultwarden_role_docker_uts`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`vaultwarden_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_docker_keep_volumes:
        ```

    ??? variable list "`vaultwarden_role_docker_mounts`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_mounts:
        ```

    ??? variable dict "`vaultwarden_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        vaultwarden_role_docker_storage_opts:
        ```

    ??? variable list "`vaultwarden_role_docker_tmpfs`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_tmpfs:
        ```

    ??? variable string "`vaultwarden_role_docker_volume_driver`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_volume_driver:
        ```

    ??? variable list "`vaultwarden_role_docker_volumes_from`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_volumes_from:
        ```

    ??? variable bool "`vaultwarden_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_docker_volumes_global:
        ```

    ??? variable string "`vaultwarden_role_docker_working_dir`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`vaultwarden_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_docker_auto_remove:
        ```

    ??? variable bool "`vaultwarden_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_docker_cleanup:
        ```

    ??? variable string "`vaultwarden_role_docker_force_kill`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_force_kill:
        ```

    ??? variable dict "`vaultwarden_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        vaultwarden_role_docker_healthcheck:
        ```

    ??? variable int "`vaultwarden_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        vaultwarden_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`vaultwarden_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_docker_init:
        ```

    ??? variable string "`vaultwarden_role_docker_kill_signal`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_kill_signal:
        ```

    ??? variable string "`vaultwarden_role_docker_log_driver`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_log_driver:
        ```

    ??? variable dict "`vaultwarden_role_docker_log_options`"

        ```yaml
        # Type: dict
        vaultwarden_role_docker_log_options:
        ```

    ??? variable bool "`vaultwarden_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_docker_oom_killer:
        ```

    ??? variable int "`vaultwarden_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        vaultwarden_role_docker_oom_score_adj:
        ```

    ??? variable bool "`vaultwarden_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_docker_output_logs:
        ```

    ??? variable bool "`vaultwarden_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_docker_paused:
        ```

    ??? variable bool "`vaultwarden_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_docker_recreate:
        ```

    ??? variable int "`vaultwarden_role_docker_restart_retries`"

        ```yaml
        # Type: int
        vaultwarden_role_docker_restart_retries:
        ```

    ??? variable int "`vaultwarden_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        vaultwarden_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`vaultwarden_role_docker_capabilities`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_capabilities:
        ```

    ??? variable string "`vaultwarden_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_cgroup_parent:
        ```

    ??? variable list "`vaultwarden_role_docker_commands`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_commands:
        ```

    ??? variable int "`vaultwarden_role_docker_create_timeout`"

        ```yaml
        # Type: int
        vaultwarden_role_docker_create_timeout:
        ```

    ??? variable string "`vaultwarden_role_docker_entrypoint`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_entrypoint:
        ```

    ??? variable string "`vaultwarden_role_docker_env_file`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_env_file:
        ```

    ??? variable dict "`vaultwarden_role_docker_labels`"

        ```yaml
        # Type: dict
        vaultwarden_role_docker_labels:
        ```

    ??? variable bool "`vaultwarden_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_docker_labels_use_common:
        ```

    ??? variable bool "`vaultwarden_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_docker_read_only:
        ```

    ??? variable string "`vaultwarden_role_docker_runtime`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_runtime:
        ```

    ??? variable list "`vaultwarden_role_docker_sysctls`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_sysctls:
        ```

    ??? variable list "`vaultwarden_role_docker_ulimits`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`vaultwarden_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        vaultwarden_role_autoheal_enabled: true
        ```

    ??? variable string "`vaultwarden_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        vaultwarden_role_depends_on: ""
        ```

    ??? variable string "`vaultwarden_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        vaultwarden_role_depends_on_delay: "0"
        ```

    ??? variable string "`vaultwarden_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        vaultwarden_role_depends_on_healthchecks:
        ```

    ??? variable bool "`vaultwarden_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        vaultwarden_role_diun_enabled: true
        ```

    ??? variable bool "`vaultwarden_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        vaultwarden_role_dns_enabled: true
        ```

    ??? variable bool "`vaultwarden_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        vaultwarden_role_docker_controller: true
        ```

    ??? variable list "`vaultwarden_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`vaultwarden_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_docker_volumes_download:
        ```

    ??? variable string "`vaultwarden_role_themepark_addons`"

        ```yaml
        # Type: string
        vaultwarden_role_themepark_addons:
        ```

    ??? variable string "`vaultwarden_role_themepark_app`"

        ```yaml
        # Type: string
        vaultwarden_role_themepark_app:
        ```

    ??? variable string "`vaultwarden_role_themepark_theme`"

        ```yaml
        # Type: string
        vaultwarden_role_themepark_theme:
        ```

    ??? variable string "`vaultwarden_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        vaultwarden_role_traefik_api_middleware:
        ```

    ??? variable string "`vaultwarden_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        vaultwarden_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`vaultwarden_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        vaultwarden_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`vaultwarden_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        vaultwarden_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`vaultwarden_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        vaultwarden_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`vaultwarden_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        vaultwarden_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`vaultwarden_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        vaultwarden_role_traefik_middleware_http:
        ```

    ??? variable bool "`vaultwarden_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`vaultwarden_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`vaultwarden_role_traefik_priority`"

        ```yaml
        # Type: string
        vaultwarden_role_traefik_priority:
        ```

    ??? variable bool "`vaultwarden_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        vaultwarden_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`vaultwarden_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        vaultwarden_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`vaultwarden_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        vaultwarden_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`vaultwarden_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        vaultwarden_role_web_api_http_port:
        ```

    ??? variable string "`vaultwarden_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        vaultwarden_role_web_api_http_scheme:
        ```

    ??? variable dict "`vaultwarden_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        vaultwarden_role_web_api_http_serverstransport:
        ```

    ??? variable string "`vaultwarden_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        vaultwarden_role_web_api_port:
        ```

    ??? variable string "`vaultwarden_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        vaultwarden_role_web_api_scheme:
        ```

    ??? variable dict "`vaultwarden_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        vaultwarden_role_web_api_serverstransport:
        ```

    ??? variable list "`vaultwarden_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        vaultwarden_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            vaultwarden_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "vaultwarden2.{{ user.domain }}"
              - "vaultwarden.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`vaultwarden_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        vaultwarden_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            vaultwarden_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'vaultwarden2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`vaultwarden_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        vaultwarden_role_web_http_port:
        ```

    ??? variable string "`vaultwarden_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        vaultwarden_role_web_http_scheme:
        ```

    ??? variable dict "`vaultwarden_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        vaultwarden_role_web_http_serverstransport:
        ```

    ??? variable string "`vaultwarden_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        vaultwarden_role_web_scheme:
        ```

    ??? variable dict "`vaultwarden_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        vaultwarden_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

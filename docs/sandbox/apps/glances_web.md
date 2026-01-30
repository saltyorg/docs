---
icon: material/docker
hide:
  - tags
tags:
  - glances
  - monitoring
  - system
saltbox_automation:
  app_links:
    - name: Manual
      url: https://github.com/nicolargo/glances/wiki
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/nicolargo/glances/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Glances
    summary: |-
      a cross-platform monitoring tool which aims to present a large amount of monitoring information through a curses or Web based interface. The information dynamically adapts depending on the size of the user interface.
    link: http://nicolargo.github.io/glances/
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Glances

## Overview

[Glances](http://nicolargo.github.io/glances/) is a cross-platform monitoring tool which aims to present a large amount of monitoring information through a curses or Web based interface. The information dynamically adapts depending on the size of the user interface.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/nicolargo/glances/wiki){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/nicolargo/glances/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-glances-web
```

## Usage

Visit <https://glances.iYOUR_DOMAIN_NAMEi>.

## Basics

- The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        glances_web_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `glances_web_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `glances_web_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`glances_web_name`"

        ```yaml
        # Type: string
        glances_web_name: glances
        ```

=== "Docker Socket Proxy"

    ??? variable dict "`glances_role_docker_socket_proxy_envs`"

        ```yaml
        # Type: dict
        glances_role_docker_socket_proxy_envs:
          CONTAINERS: "1"
          IMAGES: "1"
        ```

=== "Web"

    ??? variable string "`glances_web_role_web_subdomain`"

        ```yaml
        # Type: string
        glances_web_role_web_subdomain: "{{ glances_web_name }}"
        ```

    ??? variable string "`glances_web_role_web_domain`"

        ```yaml
        # Type: string
        glances_web_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`glances_web_role_web_port`"

        ```yaml
        # Type: string
        glances_web_role_web_port: "61208"
        ```

    ??? variable string "`glances_web_role_web_url`"

        ```yaml
        # Type: string
        glances_web_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='glances_web') + '.' + lookup('role_var', '_web_domain', role='glances_web')
                                   if (lookup('role_var', '_web_subdomain', role='glances_web') | length > 0)
                                   else lookup('role_var', '_web_domain', role='glances_web')) }}"
        ```

=== "DNS"

    ??? variable string "`glances_web_role_dns_record`"

        ```yaml
        # Type: string
        glances_web_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='glances_web') }}"
        ```

    ??? variable string "`glances_web_role_dns_zone`"

        ```yaml
        # Type: string
        glances_web_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='glances_web') }}"
        ```

    ??? variable bool "`glances_web_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`glances_web_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        glances_web_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`glances_web_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        glances_web_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`glances_web_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        glances_web_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`glances_web_role_traefik_certresolver`"

        ```yaml
        # Type: string
        glances_web_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`glances_web_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_traefik_enabled: true
        ```

    ??? variable bool "`glances_web_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_traefik_api_enabled: false
        ```

    ??? variable string "`glances_web_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        glances_web_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`glances_web_role_docker_container`"

        ```yaml
        # Type: string
        glances_web_role_docker_container: "{{ glances_web_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`glances_web_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_docker_image_pull: true
        ```

    ??? variable string "`glances_web_role_docker_image_repo`"

        ```yaml
        # Type: string
        glances_web_role_docker_image_repo: "nicolargo/glances"
        ```

    ??? variable string "`glances_web_role_docker_image_tag`"

        ```yaml
        # Type: string
        glances_web_role_docker_image_tag: "latest-full"
        ```

    ??? variable string "`glances_web_role_docker_image`"

        ```yaml
        # Type: string
        glances_web_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='glances_web') }}:{{ lookup('role_var', '_docker_image_tag', role='glances_web') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`glances_web_role_docker_envs_default`"

        ```yaml
        # Type: dict
        glances_web_role_docker_envs_default:
          UID: "{{ uid }}"
          GID: "{{ gid }}"
          TZ: "{{ tz }}"
          GLANCES_OPT: "-w --bind 172.19.0.1"
          DOCKER_HOST: "tcp://{{ glances_web_name }}-docker-socket-proxy:2375"
        ```

    ??? variable dict "`glances_web_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        glances_web_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`glances_web_role_docker_volumes_default`"

        ```yaml
        # Type: list
        glances_web_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_config_location', role='glances_web') }}:/glances/conf/glances.conf"
        ```

    ??? variable list "`glances_web_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        glances_web_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`glances_web_role_docker_hostname`"

        ```yaml
        # Type: string
        glances_web_role_docker_hostname: "{{ glances_web_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`glances_web_role_docker_network_mode`"

        ```yaml
        # Type: string
        glances_web_role_docker_network_mode: "host"
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`glances_web_role_docker_restart_policy`"

        ```yaml
        # Type: string
        glances_web_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`glances_web_role_docker_state`"

        ```yaml
        # Type: string
        glances_web_role_docker_state: started
        ```

    <h5>Force Kill</h5>

    ??? variable bool "`glances_web_role_docker_force_kill`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_docker_force_kill: true
        ```

    <h5>PID Mode</h5>

    ??? variable string "`glances_web_role_docker_pid_mode`"

        ```yaml
        # Type: string
        glances_web_role_docker_pid_mode: host
        ```

    <h5>Dependencies</h5>

    ??? variable string "`glances_web_role_depends_on`"

        ```yaml
        # Type: string
        glances_web_role_depends_on: "{{ glances_web_name }}-docker-socket-proxy"
        ```

    ??? variable string "`glances_web_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        glances_web_role_depends_on_delay: "0"
        ```

    ??? variable string "`glances_web_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        glances_web_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`glances_web_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        glances_web_role_docker_blkio_weight:
        ```

    ??? variable int "`glances_web_role_docker_cpu_period`"

        ```yaml
        # Type: int
        glances_web_role_docker_cpu_period:
        ```

    ??? variable int "`glances_web_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        glances_web_role_docker_cpu_quota:
        ```

    ??? variable int "`glances_web_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        glances_web_role_docker_cpu_shares:
        ```

    ??? variable string "`glances_web_role_docker_cpus`"

        ```yaml
        # Type: string
        glances_web_role_docker_cpus:
        ```

    ??? variable string "`glances_web_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        glances_web_role_docker_cpuset_cpus:
        ```

    ??? variable string "`glances_web_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        glances_web_role_docker_cpuset_mems:
        ```

    ??? variable string "`glances_web_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        glances_web_role_docker_kernel_memory:
        ```

    ??? variable string "`glances_web_role_docker_memory`"

        ```yaml
        # Type: string
        glances_web_role_docker_memory:
        ```

    ??? variable string "`glances_web_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        glances_web_role_docker_memory_reservation:
        ```

    ??? variable string "`glances_web_role_docker_memory_swap`"

        ```yaml
        # Type: string
        glances_web_role_docker_memory_swap:
        ```

    ??? variable int "`glances_web_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        glances_web_role_docker_memory_swappiness:
        ```

    ??? variable string "`glances_web_role_docker_shm_size`"

        ```yaml
        # Type: string
        glances_web_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`glances_web_role_docker_cap_drop`"

        ```yaml
        # Type: list
        glances_web_role_docker_cap_drop:
        ```

    ??? variable string "`glances_web_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        glances_web_role_docker_cgroupns_mode:
        ```

    ??? variable list "`glances_web_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        glances_web_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`glances_web_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        glances_web_role_docker_device_read_bps:
        ```

    ??? variable list "`glances_web_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        glances_web_role_docker_device_read_iops:
        ```

    ??? variable list "`glances_web_role_docker_device_requests`"

        ```yaml
        # Type: list
        glances_web_role_docker_device_requests:
        ```

    ??? variable list "`glances_web_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        glances_web_role_docker_device_write_bps:
        ```

    ??? variable list "`glances_web_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        glances_web_role_docker_device_write_iops:
        ```

    ??? variable list "`glances_web_role_docker_devices`"

        ```yaml
        # Type: list
        glances_web_role_docker_devices:
        ```

    ??? variable string "`glances_web_role_docker_devices_default`"

        ```yaml
        # Type: string
        glances_web_role_docker_devices_default:
        ```

    ??? variable list "`glances_web_role_docker_groups`"

        ```yaml
        # Type: list
        glances_web_role_docker_groups:
        ```

    ??? variable bool "`glances_web_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_docker_privileged:
        ```

    ??? variable list "`glances_web_role_docker_security_opts`"

        ```yaml
        # Type: list
        glances_web_role_docker_security_opts:
        ```

    ??? variable string "`glances_web_role_docker_user`"

        ```yaml
        # Type: string
        glances_web_role_docker_user:
        ```

    ??? variable string "`glances_web_role_docker_userns_mode`"

        ```yaml
        # Type: string
        glances_web_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`glances_web_role_docker_dns_opts`"

        ```yaml
        # Type: list
        glances_web_role_docker_dns_opts:
        ```

    ??? variable list "`glances_web_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        glances_web_role_docker_dns_search_domains:
        ```

    ??? variable list "`glances_web_role_docker_dns_servers`"

        ```yaml
        # Type: list
        glances_web_role_docker_dns_servers:
        ```

    ??? variable string "`glances_web_role_docker_domainname`"

        ```yaml
        # Type: string
        glances_web_role_docker_domainname:
        ```

    ??? variable list "`glances_web_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        glances_web_role_docker_exposed_ports:
        ```

    ??? variable dict "`glances_web_role_docker_hosts`"

        ```yaml
        # Type: dict
        glances_web_role_docker_hosts:
        ```

    ??? variable bool "`glances_web_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_docker_hosts_use_common:
        ```

    ??? variable string "`glances_web_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        glances_web_role_docker_ipc_mode:
        ```

    ??? variable list "`glances_web_role_docker_links`"

        ```yaml
        # Type: list
        glances_web_role_docker_links:
        ```

    ??? variable list "`glances_web_role_docker_networks`"

        ```yaml
        # Type: list
        glances_web_role_docker_networks:
        ```

    ??? variable list "`glances_web_role_docker_ports`"

        ```yaml
        # Type: list
        glances_web_role_docker_ports:
        ```

    ??? variable string "`glances_web_role_docker_uts`"

        ```yaml
        # Type: string
        glances_web_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`glances_web_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_docker_keep_volumes:
        ```

    ??? variable list "`glances_web_role_docker_mounts`"

        ```yaml
        # Type: list
        glances_web_role_docker_mounts:
        ```

    ??? variable dict "`glances_web_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        glances_web_role_docker_storage_opts:
        ```

    ??? variable list "`glances_web_role_docker_tmpfs`"

        ```yaml
        # Type: list
        glances_web_role_docker_tmpfs:
        ```

    ??? variable string "`glances_web_role_docker_volume_driver`"

        ```yaml
        # Type: string
        glances_web_role_docker_volume_driver:
        ```

    ??? variable list "`glances_web_role_docker_volumes_from`"

        ```yaml
        # Type: list
        glances_web_role_docker_volumes_from:
        ```

    ??? variable bool "`glances_web_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_docker_volumes_global:
        ```

    ??? variable string "`glances_web_role_docker_working_dir`"

        ```yaml
        # Type: string
        glances_web_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`glances_web_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_docker_auto_remove:
        ```

    ??? variable bool "`glances_web_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_docker_cleanup:
        ```

    ??? variable dict "`glances_web_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        glances_web_role_docker_healthcheck:
        ```

    ??? variable int "`glances_web_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        glances_web_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`glances_web_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_docker_init:
        ```

    ??? variable string "`glances_web_role_docker_kill_signal`"

        ```yaml
        # Type: string
        glances_web_role_docker_kill_signal:
        ```

    ??? variable string "`glances_web_role_docker_log_driver`"

        ```yaml
        # Type: string
        glances_web_role_docker_log_driver:
        ```

    ??? variable dict "`glances_web_role_docker_log_options`"

        ```yaml
        # Type: dict
        glances_web_role_docker_log_options:
        ```

    ??? variable bool "`glances_web_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_docker_oom_killer:
        ```

    ??? variable int "`glances_web_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        glances_web_role_docker_oom_score_adj:
        ```

    ??? variable bool "`glances_web_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_docker_output_logs:
        ```

    ??? variable bool "`glances_web_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_docker_paused:
        ```

    ??? variable bool "`glances_web_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_docker_recreate:
        ```

    ??? variable int "`glances_web_role_docker_restart_retries`"

        ```yaml
        # Type: int
        glances_web_role_docker_restart_retries:
        ```

    ??? variable string "`glances_web_role_docker_stop_signal`"

        ```yaml
        # Type: string
        glances_web_role_docker_stop_signal:
        ```

    ??? variable int "`glances_web_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        glances_web_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`glances_web_role_docker_capabilities`"

        ```yaml
        # Type: list
        glances_web_role_docker_capabilities:
        ```

    ??? variable string "`glances_web_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        glances_web_role_docker_cgroup_parent:
        ```

    ??? variable list "`glances_web_role_docker_commands`"

        ```yaml
        # Type: list
        glances_web_role_docker_commands:
        ```

    ??? variable int "`glances_web_role_docker_create_timeout`"

        ```yaml
        # Type: int
        glances_web_role_docker_create_timeout:
        ```

    ??? variable string "`glances_web_role_docker_entrypoint`"

        ```yaml
        # Type: string
        glances_web_role_docker_entrypoint:
        ```

    ??? variable string "`glances_web_role_docker_env_file`"

        ```yaml
        # Type: string
        glances_web_role_docker_env_file:
        ```

    ??? variable dict "`glances_web_role_docker_labels`"

        ```yaml
        # Type: dict
        glances_web_role_docker_labels:
        ```

    ??? variable bool "`glances_web_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_docker_labels_use_common:
        ```

    ??? variable bool "`glances_web_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_docker_read_only:
        ```

    ??? variable string "`glances_web_role_docker_runtime`"

        ```yaml
        # Type: string
        glances_web_role_docker_runtime:
        ```

    ??? variable list "`glances_web_role_docker_sysctls`"

        ```yaml
        # Type: list
        glances_web_role_docker_sysctls:
        ```

    ??? variable list "`glances_web_role_docker_ulimits`"

        ```yaml
        # Type: list
        glances_web_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`glances_web_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        glances_web_role_autoheal_enabled: true
        ```

    ??? variable bool "`glances_web_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        glances_web_role_diun_enabled: true
        ```

    ??? variable bool "`glances_web_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        glances_web_role_dns_enabled: true
        ```

    ??? variable bool "`glances_web_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        glances_web_role_docker_controller: true
        ```

    ??? variable list "`glances_web_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        glances_web_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`glances_web_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_docker_volumes_download:
        ```

    ??? variable string "`glances_web_role_themepark_addons`"

        ```yaml
        # Type: string
        glances_web_role_themepark_addons:
        ```

    ??? variable string "`glances_web_role_themepark_app`"

        ```yaml
        # Type: string
        glances_web_role_themepark_app:
        ```

    ??? variable string "`glances_web_role_themepark_theme`"

        ```yaml
        # Type: string
        glances_web_role_themepark_theme:
        ```

    ??? variable string "`glances_web_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        glances_web_role_traefik_api_middleware:
        ```

    ??? variable string "`glances_web_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        glances_web_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`glances_web_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        glances_web_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`glances_web_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        glances_web_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`glances_web_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        glances_web_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`glances_web_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        glances_web_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`glances_web_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        glances_web_role_traefik_middleware_http:
        ```

    ??? variable bool "`glances_web_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`glances_web_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`glances_web_role_traefik_priority`"

        ```yaml
        # Type: string
        glances_web_role_traefik_priority:
        ```

    ??? variable bool "`glances_web_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        glances_web_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`glances_web_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        glances_web_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`glances_web_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        glances_web_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`glances_web_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        glances_web_role_web_api_http_port:
        ```

    ??? variable string "`glances_web_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        glances_web_role_web_api_http_scheme:
        ```

    ??? variable dict "`glances_web_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        glances_web_role_web_api_http_serverstransport:
        ```

    ??? variable string "`glances_web_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        glances_web_role_web_api_port:
        ```

    ??? variable string "`glances_web_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        glances_web_role_web_api_scheme:
        ```

    ??? variable dict "`glances_web_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        glances_web_role_web_api_serverstransport:
        ```

    ??? variable list "`glances_web_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        glances_web_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            glances_web_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "glances_web2.{{ user.domain }}"
              - "glances_web.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`glances_web_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        glances_web_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            glances_web_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'glances_web2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`glances_web_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        glances_web_role_web_http_port:
        ```

    ??? variable string "`glances_web_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        glances_web_role_web_http_scheme:
        ```

    ??? variable dict "`glances_web_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        glances_web_role_web_http_serverstransport:
        ```

    ??? variable string "`glances_web_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        glances_web_role_web_scheme:
        ```

    ??? variable dict "`glances_web_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        glances_web_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

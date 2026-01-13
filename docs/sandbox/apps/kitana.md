---
icon: material/docker
hide:
  - tags
tags:
  - kitana
  - plex
  - frontend
saltbox_automation:
  app_links:
    - name: Manual
      url: https://github.com/pannal/Kitana
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/pannal/kitana/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Kitana
    summary: |-
      a responsive Plex plugin web frontend.
    link: https://github.com/pannal/Kitana
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Kitana

## Overview

[Kitana](https://github.com/pannal/Kitana) is a responsive Plex plugin web frontend.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/pannal/Kitana){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/pannal/kitana/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-kitana
```

## Usage

Visit <https://kitana.iYOUR_DOMAIN_NAMEi>.

## Basics

- pen your browser and visit your Kitana instance <https://kitana.iYOUR_DOMAIN_NAMEi>

- authenticate against Plex.TV

- select your server (non-owned may not work; local connections are preferred)

- profit

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        kitana_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `kitana_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `kitana_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`kitana_name`"

        ```yaml
        # Type: string
        kitana_name: kitana
        ```

=== "Web"

    ??? variable string "`kitana_role_web_subdomain`"

        ```yaml
        # Type: string
        kitana_role_web_subdomain: "{{ kitana_name }}"
        ```

    ??? variable string "`kitana_role_web_domain`"

        ```yaml
        # Type: string
        kitana_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`kitana_role_web_port`"

        ```yaml
        # Type: string
        kitana_role_web_port: "31337"
        ```

    ??? variable string "`kitana_role_web_url`"

        ```yaml
        # Type: string
        kitana_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='kitana') + '.' + lookup('role_var', '_web_domain', role='kitana')
                              if (lookup('role_var', '_web_subdomain', role='kitana') | length > 0)
                              else lookup('role_var', '_web_domain', role='kitana')) }}"
        ```

=== "DNS"

    ??? variable string "`kitana_role_dns_record`"

        ```yaml
        # Type: string
        kitana_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='kitana') }}"
        ```

    ??? variable string "`kitana_role_dns_zone`"

        ```yaml
        # Type: string
        kitana_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='kitana') }}"
        ```

    ??? variable bool "`kitana_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`kitana_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        kitana_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`kitana_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        kitana_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`kitana_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        kitana_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`kitana_role_traefik_certresolver`"

        ```yaml
        # Type: string
        kitana_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`kitana_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_traefik_enabled: true
        ```

    ??? variable bool "`kitana_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_traefik_api_enabled: false
        ```

    ??? variable string "`kitana_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        kitana_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`kitana_role_docker_container`"

        ```yaml
        # Type: string
        kitana_role_docker_container: "{{ kitana_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`kitana_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_docker_image_pull: true
        ```

    ??? variable string "`kitana_role_docker_image_repo`"

        ```yaml
        # Type: string
        kitana_role_docker_image_repo: "pannal/kitana"
        ```

    ??? variable string "`kitana_role_docker_image_tag`"

        ```yaml
        # Type: string
        kitana_role_docker_image_tag: "latest"
        ```

    ??? variable string "`kitana_role_docker_image`"

        ```yaml
        # Type: string
        kitana_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='kitana') }}:{{ lookup('role_var', '_docker_image_tag', role='kitana') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`kitana_role_docker_envs_default`"

        ```yaml
        # Type: dict
        kitana_role_docker_envs_default:
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`kitana_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        kitana_role_docker_envs_custom: {}
        ```

    <h5>Commands</h5>

    ??? variable list "`kitana_role_docker_commands_default`"

        ```yaml
        # Type: list
        kitana_role_docker_commands_default:
          - "-P"
        ```

    ??? variable list "`kitana_role_docker_commands_custom`"

        ```yaml
        # Type: list
        kitana_role_docker_commands_custom: []
        ```

    <h5>Volumes</h5>

    ??? variable list "`kitana_role_docker_volumes_default`"

        ```yaml
        # Type: list
        kitana_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='kitana') }}:/app/data"
        ```

    ??? variable list "`kitana_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        kitana_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`kitana_role_docker_hostname`"

        ```yaml
        # Type: string
        kitana_role_docker_hostname: "{{ kitana_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`kitana_role_docker_networks_alias`"

        ```yaml
        # Type: string
        kitana_role_docker_networks_alias: "{{ kitana_name }}"
        ```

    ??? variable list "`kitana_role_docker_networks_default`"

        ```yaml
        # Type: list
        kitana_role_docker_networks_default: []
        ```

    ??? variable list "`kitana_role_docker_networks_custom`"

        ```yaml
        # Type: list
        kitana_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`kitana_role_docker_restart_policy`"

        ```yaml
        # Type: string
        kitana_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`kitana_role_docker_state`"

        ```yaml
        # Type: string
        kitana_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`kitana_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        kitana_role_docker_blkio_weight:
        ```

    ??? variable int "`kitana_role_docker_cpu_period`"

        ```yaml
        # Type: int
        kitana_role_docker_cpu_period:
        ```

    ??? variable int "`kitana_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        kitana_role_docker_cpu_quota:
        ```

    ??? variable int "`kitana_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        kitana_role_docker_cpu_shares:
        ```

    ??? variable string "`kitana_role_docker_cpus`"

        ```yaml
        # Type: string
        kitana_role_docker_cpus:
        ```

    ??? variable string "`kitana_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        kitana_role_docker_cpuset_cpus:
        ```

    ??? variable string "`kitana_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        kitana_role_docker_cpuset_mems:
        ```

    ??? variable string "`kitana_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        kitana_role_docker_kernel_memory:
        ```

    ??? variable string "`kitana_role_docker_memory`"

        ```yaml
        # Type: string
        kitana_role_docker_memory:
        ```

    ??? variable string "`kitana_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        kitana_role_docker_memory_reservation:
        ```

    ??? variable string "`kitana_role_docker_memory_swap`"

        ```yaml
        # Type: string
        kitana_role_docker_memory_swap:
        ```

    ??? variable int "`kitana_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        kitana_role_docker_memory_swappiness:
        ```

    ??? variable string "`kitana_role_docker_shm_size`"

        ```yaml
        # Type: string
        kitana_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`kitana_role_docker_cap_drop`"

        ```yaml
        # Type: list
        kitana_role_docker_cap_drop:
        ```

    ??? variable string "`kitana_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        kitana_role_docker_cgroupns_mode:
        ```

    ??? variable list "`kitana_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        kitana_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`kitana_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        kitana_role_docker_device_read_bps:
        ```

    ??? variable list "`kitana_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        kitana_role_docker_device_read_iops:
        ```

    ??? variable list "`kitana_role_docker_device_requests`"

        ```yaml
        # Type: list
        kitana_role_docker_device_requests:
        ```

    ??? variable list "`kitana_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        kitana_role_docker_device_write_bps:
        ```

    ??? variable list "`kitana_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        kitana_role_docker_device_write_iops:
        ```

    ??? variable list "`kitana_role_docker_devices`"

        ```yaml
        # Type: list
        kitana_role_docker_devices:
        ```

    ??? variable string "`kitana_role_docker_devices_default`"

        ```yaml
        # Type: string
        kitana_role_docker_devices_default:
        ```

    ??? variable list "`kitana_role_docker_groups`"

        ```yaml
        # Type: list
        kitana_role_docker_groups:
        ```

    ??? variable bool "`kitana_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_docker_privileged:
        ```

    ??? variable list "`kitana_role_docker_security_opts`"

        ```yaml
        # Type: list
        kitana_role_docker_security_opts:
        ```

    ??? variable string "`kitana_role_docker_user`"

        ```yaml
        # Type: string
        kitana_role_docker_user:
        ```

    ??? variable string "`kitana_role_docker_userns_mode`"

        ```yaml
        # Type: string
        kitana_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`kitana_role_docker_dns_opts`"

        ```yaml
        # Type: list
        kitana_role_docker_dns_opts:
        ```

    ??? variable list "`kitana_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        kitana_role_docker_dns_search_domains:
        ```

    ??? variable list "`kitana_role_docker_dns_servers`"

        ```yaml
        # Type: list
        kitana_role_docker_dns_servers:
        ```

    ??? variable string "`kitana_role_docker_domainname`"

        ```yaml
        # Type: string
        kitana_role_docker_domainname:
        ```

    ??? variable list "`kitana_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        kitana_role_docker_exposed_ports:
        ```

    ??? variable dict "`kitana_role_docker_hosts`"

        ```yaml
        # Type: dict
        kitana_role_docker_hosts:
        ```

    ??? variable bool "`kitana_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_docker_hosts_use_common:
        ```

    ??? variable string "`kitana_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        kitana_role_docker_ipc_mode:
        ```

    ??? variable list "`kitana_role_docker_links`"

        ```yaml
        # Type: list
        kitana_role_docker_links:
        ```

    ??? variable string "`kitana_role_docker_network_mode`"

        ```yaml
        # Type: string
        kitana_role_docker_network_mode:
        ```

    ??? variable string "`kitana_role_docker_pid_mode`"

        ```yaml
        # Type: string
        kitana_role_docker_pid_mode:
        ```

    ??? variable list "`kitana_role_docker_ports`"

        ```yaml
        # Type: list
        kitana_role_docker_ports:
        ```

    ??? variable string "`kitana_role_docker_uts`"

        ```yaml
        # Type: string
        kitana_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`kitana_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_docker_keep_volumes:
        ```

    ??? variable list "`kitana_role_docker_mounts`"

        ```yaml
        # Type: list
        kitana_role_docker_mounts:
        ```

    ??? variable dict "`kitana_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        kitana_role_docker_storage_opts:
        ```

    ??? variable list "`kitana_role_docker_tmpfs`"

        ```yaml
        # Type: list
        kitana_role_docker_tmpfs:
        ```

    ??? variable string "`kitana_role_docker_volume_driver`"

        ```yaml
        # Type: string
        kitana_role_docker_volume_driver:
        ```

    ??? variable list "`kitana_role_docker_volumes_from`"

        ```yaml
        # Type: list
        kitana_role_docker_volumes_from:
        ```

    ??? variable bool "`kitana_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_docker_volumes_global:
        ```

    ??? variable string "`kitana_role_docker_working_dir`"

        ```yaml
        # Type: string
        kitana_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`kitana_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_docker_auto_remove:
        ```

    ??? variable bool "`kitana_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_docker_cleanup:
        ```

    ??? variable string "`kitana_role_docker_force_kill`"

        ```yaml
        # Type: string
        kitana_role_docker_force_kill:
        ```

    ??? variable dict "`kitana_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        kitana_role_docker_healthcheck:
        ```

    ??? variable int "`kitana_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        kitana_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`kitana_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_docker_init:
        ```

    ??? variable string "`kitana_role_docker_kill_signal`"

        ```yaml
        # Type: string
        kitana_role_docker_kill_signal:
        ```

    ??? variable string "`kitana_role_docker_log_driver`"

        ```yaml
        # Type: string
        kitana_role_docker_log_driver:
        ```

    ??? variable dict "`kitana_role_docker_log_options`"

        ```yaml
        # Type: dict
        kitana_role_docker_log_options:
        ```

    ??? variable bool "`kitana_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_docker_oom_killer:
        ```

    ??? variable int "`kitana_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        kitana_role_docker_oom_score_adj:
        ```

    ??? variable bool "`kitana_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_docker_output_logs:
        ```

    ??? variable bool "`kitana_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_docker_paused:
        ```

    ??? variable bool "`kitana_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_docker_recreate:
        ```

    ??? variable int "`kitana_role_docker_restart_retries`"

        ```yaml
        # Type: int
        kitana_role_docker_restart_retries:
        ```

    ??? variable int "`kitana_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        kitana_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`kitana_role_docker_capabilities`"

        ```yaml
        # Type: list
        kitana_role_docker_capabilities:
        ```

    ??? variable string "`kitana_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        kitana_role_docker_cgroup_parent:
        ```

    ??? variable int "`kitana_role_docker_create_timeout`"

        ```yaml
        # Type: int
        kitana_role_docker_create_timeout:
        ```

    ??? variable string "`kitana_role_docker_entrypoint`"

        ```yaml
        # Type: string
        kitana_role_docker_entrypoint:
        ```

    ??? variable string "`kitana_role_docker_env_file`"

        ```yaml
        # Type: string
        kitana_role_docker_env_file:
        ```

    ??? variable dict "`kitana_role_docker_labels`"

        ```yaml
        # Type: dict
        kitana_role_docker_labels:
        ```

    ??? variable bool "`kitana_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_docker_labels_use_common:
        ```

    ??? variable bool "`kitana_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_docker_read_only:
        ```

    ??? variable string "`kitana_role_docker_runtime`"

        ```yaml
        # Type: string
        kitana_role_docker_runtime:
        ```

    ??? variable list "`kitana_role_docker_sysctls`"

        ```yaml
        # Type: list
        kitana_role_docker_sysctls:
        ```

    ??? variable list "`kitana_role_docker_ulimits`"

        ```yaml
        # Type: list
        kitana_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`kitana_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        kitana_role_autoheal_enabled: true
        ```

    ??? variable string "`kitana_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        kitana_role_depends_on: ""
        ```

    ??? variable string "`kitana_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        kitana_role_depends_on_delay: "0"
        ```

    ??? variable string "`kitana_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        kitana_role_depends_on_healthchecks:
        ```

    ??? variable bool "`kitana_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        kitana_role_diun_enabled: true
        ```

    ??? variable bool "`kitana_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        kitana_role_dns_enabled: true
        ```

    ??? variable bool "`kitana_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        kitana_role_docker_controller: true
        ```

    ??? variable string "`kitana_role_docker_image_repo`"

        ```yaml
        # Type: string
        kitana_role_docker_image_repo:
        ```

    ??? variable string "`kitana_role_docker_image_tag`"

        ```yaml
        # Type: string
        kitana_role_docker_image_tag:
        ```

    ??? variable bool "`kitana_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_docker_volumes_download:
        ```

    ??? variable string "`kitana_role_paths_location`"

        ```yaml
        # Type: string
        kitana_role_paths_location:
        ```

    ??? variable string "`kitana_role_themepark_addons`"

        ```yaml
        # Type: string
        kitana_role_themepark_addons:
        ```

    ??? variable string "`kitana_role_themepark_app`"

        ```yaml
        # Type: string
        kitana_role_themepark_app:
        ```

    ??? variable string "`kitana_role_themepark_theme`"

        ```yaml
        # Type: string
        kitana_role_themepark_theme:
        ```

    ??? variable dict "`kitana_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        kitana_role_traefik_api_endpoint:
        ```

    ??? variable string "`kitana_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        kitana_role_traefik_api_middleware:
        ```

    ??? variable string "`kitana_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        kitana_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`kitana_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        kitana_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`kitana_role_traefik_certresolver`"

        ```yaml
        # Type: string
        kitana_role_traefik_certresolver:
        ```

    ??? variable bool "`kitana_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        kitana_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`kitana_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        kitana_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`kitana_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        kitana_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`kitana_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        kitana_role_traefik_middleware_http:
        ```

    ??? variable bool "`kitana_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`kitana_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`kitana_role_traefik_priority`"

        ```yaml
        # Type: string
        kitana_role_traefik_priority:
        ```

    ??? variable bool "`kitana_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        kitana_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`kitana_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        kitana_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`kitana_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        kitana_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`kitana_role_web_domain`"

        ```yaml
        # Type: string
        kitana_role_web_domain:
        ```

    ??? variable list "`kitana_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        kitana_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            kitana_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "kitana2.{{ user.domain }}"
              - "kitana.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`kitana_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        kitana_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            kitana_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'kitana2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`kitana_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        kitana_role_web_http_port:
        ```

    ??? variable string "`kitana_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        kitana_role_web_http_scheme:
        ```

    ??? variable dict "`kitana_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        kitana_role_web_http_serverstransport:
        ```

    ??? variable string "`kitana_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        kitana_role_web_scheme:
        ```

    ??? variable dict "`kitana_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        kitana_role_web_serverstransport:
        ```

    ??? variable string "`kitana_role_web_subdomain`"

        ```yaml
        # Type: string
        kitana_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
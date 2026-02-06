---
icon: material/docker
hide:
  - tags
tags:
  - wrapperr
  - statistics
  - analytics
saltbox_automation:
  app_links:
    - name: Manual
      url: https://github.com/aunefyren/wrapperr/wiki
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/aunefyren/wrapperr/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Wrapperr
    summary: |-
      a website-based platform and API for collecting user stats within a set timeframe using Tautulli. The data is displayed as a statistics-summary, sort of like Spotify Wrapped. Yes, you need Tautulli to have been running beforehand and currently for this to work. Note: Wrapperr is not behind authelia.
    link: https://github.com/aunefyren/wrapperr
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Wrapperr

## Overview

[Wrapperr](https://github.com/aunefyren/wrapperr) is a website-based platform and API for collecting user stats within a set timeframe using Tautulli. The data is displayed as a statistics-summary, sort of like Spotify Wrapped. Yes, you need Tautulli to have been running beforehand and currently for this to work. Note: Wrapperr is not behind authelia.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/aunefyren/wrapperr/wiki){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/aunefyren/wrapperr/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-wrapperr
```

## Usage

Visit <https://wrapperr.iYOUR_DOMAIN_NAMEi>.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        wrapperr_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `wrapperr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `wrapperr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`wrapperr_name`"

        ```yaml
        # Type: string
        wrapperr_name: wrapperr
        ```

=== "Web"

    ??? variable string "`wrapperr_role_web_subdomain`"

        ```yaml
        # Type: string
        wrapperr_role_web_subdomain: "{{ wrapperr_name }}"
        ```

    ??? variable string "`wrapperr_role_web_domain`"

        ```yaml
        # Type: string
        wrapperr_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`wrapperr_role_web_port`"

        ```yaml
        # Type: string
        wrapperr_role_web_port: "8282"
        ```

    ??? variable string "`wrapperr_role_web_url`"

        ```yaml
        # Type: string
        wrapperr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='wrapperr') + '.' + lookup('role_var', '_web_domain', role='wrapperr')
                                if (lookup('role_var', '_web_subdomain', role='wrapperr') | length > 0)
                                else lookup('role_var', '_web_domain', role='wrapperr')) }}"
        ```

=== "DNS"

    ??? variable string "`wrapperr_role_dns_record`"

        ```yaml
        # Type: string
        wrapperr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='wrapperr') }}"
        ```

    ??? variable string "`wrapperr_role_dns_zone`"

        ```yaml
        # Type: string
        wrapperr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='wrapperr') }}"
        ```

    ??? variable bool "`wrapperr_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`wrapperr_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        wrapperr_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`wrapperr_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        wrapperr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`wrapperr_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        wrapperr_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`wrapperr_role_traefik_certresolver`"

        ```yaml
        # Type: string
        wrapperr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`wrapperr_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_traefik_enabled: true
        ```

    ??? variable bool "`wrapperr_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_traefik_api_enabled: false
        ```

    ??? variable string "`wrapperr_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        wrapperr_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`wrapperr_role_docker_container`"

        ```yaml
        # Type: string
        wrapperr_role_docker_container: "{{ wrapperr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`wrapperr_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_docker_image_pull: true
        ```

    ??? variable string "`wrapperr_role_docker_image_repo`"

        ```yaml
        # Type: string
        wrapperr_role_docker_image_repo: "aunefyren/wrapperr"
        ```

    ??? variable string "`wrapperr_role_docker_image_tag`"

        ```yaml
        # Type: string
        wrapperr_role_docker_image_tag: "latest"
        ```

    ??? variable string "`wrapperr_role_docker_image`"

        ```yaml
        # Type: string
        wrapperr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='wrapperr') }}:{{ lookup('role_var', '_docker_image_tag', role='wrapperr') }}"
        ```

    <h5>Volumes</h5>

    ??? variable list "`wrapperr_role_docker_volumes_default`"

        ```yaml
        # Type: list
        wrapperr_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='wrapperr') }}:/app/config"
        ```

    ??? variable list "`wrapperr_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        wrapperr_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`wrapperr_role_docker_hostname`"

        ```yaml
        # Type: string
        wrapperr_role_docker_hostname: "{{ wrapperr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`wrapperr_role_docker_networks_alias`"

        ```yaml
        # Type: string
        wrapperr_role_docker_networks_alias: "{{ wrapperr_name }}"
        ```

    ??? variable list "`wrapperr_role_docker_networks_default`"

        ```yaml
        # Type: list
        wrapperr_role_docker_networks_default: []
        ```

    ??? variable list "`wrapperr_role_docker_networks_custom`"

        ```yaml
        # Type: list
        wrapperr_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`wrapperr_role_docker_restart_policy`"

        ```yaml
        # Type: string
        wrapperr_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`wrapperr_role_docker_state`"

        ```yaml
        # Type: string
        wrapperr_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`wrapperr_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        wrapperr_role_docker_blkio_weight:
        ```

    ??? variable int "`wrapperr_role_docker_cpu_period`"

        ```yaml
        # Type: int
        wrapperr_role_docker_cpu_period:
        ```

    ??? variable int "`wrapperr_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        wrapperr_role_docker_cpu_quota:
        ```

    ??? variable int "`wrapperr_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        wrapperr_role_docker_cpu_shares:
        ```

    ??? variable string "`wrapperr_role_docker_cpus`"

        ```yaml
        # Type: string
        wrapperr_role_docker_cpus:
        ```

    ??? variable string "`wrapperr_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        wrapperr_role_docker_cpuset_cpus:
        ```

    ??? variable string "`wrapperr_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        wrapperr_role_docker_cpuset_mems:
        ```

    ??? variable string "`wrapperr_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        wrapperr_role_docker_kernel_memory:
        ```

    ??? variable string "`wrapperr_role_docker_memory`"

        ```yaml
        # Type: string
        wrapperr_role_docker_memory:
        ```

    ??? variable string "`wrapperr_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        wrapperr_role_docker_memory_reservation:
        ```

    ??? variable string "`wrapperr_role_docker_memory_swap`"

        ```yaml
        # Type: string
        wrapperr_role_docker_memory_swap:
        ```

    ??? variable int "`wrapperr_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        wrapperr_role_docker_memory_swappiness:
        ```

    ??? variable string "`wrapperr_role_docker_shm_size`"

        ```yaml
        # Type: string
        wrapperr_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`wrapperr_role_docker_cap_drop`"

        ```yaml
        # Type: list
        wrapperr_role_docker_cap_drop:
        ```

    ??? variable string "`wrapperr_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        wrapperr_role_docker_cgroupns_mode:
        ```

    ??? variable list "`wrapperr_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        wrapperr_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`wrapperr_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        wrapperr_role_docker_device_read_bps:
        ```

    ??? variable list "`wrapperr_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        wrapperr_role_docker_device_read_iops:
        ```

    ??? variable list "`wrapperr_role_docker_device_requests`"

        ```yaml
        # Type: list
        wrapperr_role_docker_device_requests:
        ```

    ??? variable list "`wrapperr_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        wrapperr_role_docker_device_write_bps:
        ```

    ??? variable list "`wrapperr_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        wrapperr_role_docker_device_write_iops:
        ```

    ??? variable list "`wrapperr_role_docker_devices`"

        ```yaml
        # Type: list
        wrapperr_role_docker_devices:
        ```

    ??? variable list "`wrapperr_role_docker_groups`"

        ```yaml
        # Type: list
        wrapperr_role_docker_groups:
        ```

    ??? variable bool "`wrapperr_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_docker_privileged:
        ```

    ??? variable list "`wrapperr_role_docker_security_opts`"

        ```yaml
        # Type: list
        wrapperr_role_docker_security_opts:
        ```

    ??? variable string "`wrapperr_role_docker_user`"

        ```yaml
        # Type: string
        wrapperr_role_docker_user:
        ```

    ??? variable string "`wrapperr_role_docker_userns_mode`"

        ```yaml
        # Type: string
        wrapperr_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`wrapperr_role_docker_dns_opts`"

        ```yaml
        # Type: list
        wrapperr_role_docker_dns_opts:
        ```

    ??? variable list "`wrapperr_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        wrapperr_role_docker_dns_search_domains:
        ```

    ??? variable list "`wrapperr_role_docker_dns_servers`"

        ```yaml
        # Type: list
        wrapperr_role_docker_dns_servers:
        ```

    ??? variable string "`wrapperr_role_docker_domainname`"

        ```yaml
        # Type: string
        wrapperr_role_docker_domainname:
        ```

    ??? variable list "`wrapperr_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        wrapperr_role_docker_exposed_ports:
        ```

    ??? variable dict "`wrapperr_role_docker_hosts`"

        ```yaml
        # Type: dict
        wrapperr_role_docker_hosts:
        ```

    ??? variable bool "`wrapperr_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_docker_hosts_use_common:
        ```

    ??? variable string "`wrapperr_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        wrapperr_role_docker_ipc_mode:
        ```

    ??? variable list "`wrapperr_role_docker_links`"

        ```yaml
        # Type: list
        wrapperr_role_docker_links:
        ```

    ??? variable string "`wrapperr_role_docker_network_mode`"

        ```yaml
        # Type: string
        wrapperr_role_docker_network_mode:
        ```

    ??? variable string "`wrapperr_role_docker_pid_mode`"

        ```yaml
        # Type: string
        wrapperr_role_docker_pid_mode:
        ```

    ??? variable list "`wrapperr_role_docker_ports`"

        ```yaml
        # Type: list
        wrapperr_role_docker_ports:
        ```

    ??? variable string "`wrapperr_role_docker_uts`"

        ```yaml
        # Type: string
        wrapperr_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`wrapperr_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_docker_keep_volumes:
        ```

    ??? variable list "`wrapperr_role_docker_mounts`"

        ```yaml
        # Type: list
        wrapperr_role_docker_mounts:
        ```

    ??? variable dict "`wrapperr_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        wrapperr_role_docker_storage_opts:
        ```

    ??? variable list "`wrapperr_role_docker_tmpfs`"

        ```yaml
        # Type: list
        wrapperr_role_docker_tmpfs:
        ```

    ??? variable string "`wrapperr_role_docker_volume_driver`"

        ```yaml
        # Type: string
        wrapperr_role_docker_volume_driver:
        ```

    ??? variable list "`wrapperr_role_docker_volumes_from`"

        ```yaml
        # Type: list
        wrapperr_role_docker_volumes_from:
        ```

    ??? variable bool "`wrapperr_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_docker_volumes_global:
        ```

    ??? variable string "`wrapperr_role_docker_working_dir`"

        ```yaml
        # Type: string
        wrapperr_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`wrapperr_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_docker_auto_remove:
        ```

    ??? variable bool "`wrapperr_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_docker_cleanup:
        ```

    ??? variable string "`wrapperr_role_docker_force_kill`"

        ```yaml
        # Type: string
        wrapperr_role_docker_force_kill:
        ```

    ??? variable dict "`wrapperr_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        wrapperr_role_docker_healthcheck:
        ```

    ??? variable int "`wrapperr_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        wrapperr_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`wrapperr_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_docker_init:
        ```

    ??? variable string "`wrapperr_role_docker_kill_signal`"

        ```yaml
        # Type: string
        wrapperr_role_docker_kill_signal:
        ```

    ??? variable string "`wrapperr_role_docker_log_driver`"

        ```yaml
        # Type: string
        wrapperr_role_docker_log_driver:
        ```

    ??? variable dict "`wrapperr_role_docker_log_options`"

        ```yaml
        # Type: dict
        wrapperr_role_docker_log_options:
        ```

    ??? variable bool "`wrapperr_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_docker_oom_killer:
        ```

    ??? variable int "`wrapperr_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        wrapperr_role_docker_oom_score_adj:
        ```

    ??? variable bool "`wrapperr_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_docker_output_logs:
        ```

    ??? variable bool "`wrapperr_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_docker_paused:
        ```

    ??? variable bool "`wrapperr_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_docker_recreate:
        ```

    ??? variable int "`wrapperr_role_docker_restart_retries`"

        ```yaml
        # Type: int
        wrapperr_role_docker_restart_retries:
        ```

    ??? variable string "`wrapperr_role_docker_stop_signal`"

        ```yaml
        # Type: string
        wrapperr_role_docker_stop_signal:
        ```

    ??? variable int "`wrapperr_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        wrapperr_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`wrapperr_role_docker_capabilities`"

        ```yaml
        # Type: list
        wrapperr_role_docker_capabilities:
        ```

    ??? variable string "`wrapperr_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        wrapperr_role_docker_cgroup_parent:
        ```

    ??? variable list "`wrapperr_role_docker_commands`"

        ```yaml
        # Type: list
        wrapperr_role_docker_commands:
        ```

    ??? variable int "`wrapperr_role_docker_create_timeout`"

        ```yaml
        # Type: int
        wrapperr_role_docker_create_timeout:
        ```

    ??? variable string "`wrapperr_role_docker_dev_dri`"

        ```yaml
        # Type: string
        wrapperr_role_docker_dev_dri:
        ```

    ??? variable string "`wrapperr_role_docker_entrypoint`"

        ```yaml
        # Type: string
        wrapperr_role_docker_entrypoint:
        ```

    ??? variable string "`wrapperr_role_docker_env_file`"

        ```yaml
        # Type: string
        wrapperr_role_docker_env_file:
        ```

    ??? variable dict "`wrapperr_role_docker_envs`"

        ```yaml
        # Type: dict
        wrapperr_role_docker_envs:
        ```

    ??? variable dict "`wrapperr_role_docker_labels`"

        ```yaml
        # Type: dict
        wrapperr_role_docker_labels:
        ```

    ??? variable bool "`wrapperr_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_docker_labels_use_common:
        ```

    ??? variable bool "`wrapperr_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_docker_read_only:
        ```

    ??? variable string "`wrapperr_role_docker_runtime`"

        ```yaml
        # Type: string
        wrapperr_role_docker_runtime:
        ```

    ??? variable list "`wrapperr_role_docker_sysctls`"

        ```yaml
        # Type: list
        wrapperr_role_docker_sysctls:
        ```

    ??? variable list "`wrapperr_role_docker_ulimits`"

        ```yaml
        # Type: list
        wrapperr_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`wrapperr_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        wrapperr_role_autoheal_enabled: true
        ```

    ??? variable string "`wrapperr_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        wrapperr_role_depends_on: ""
        ```

    ??? variable string "`wrapperr_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        wrapperr_role_depends_on_delay: "0"
        ```

    ??? variable string "`wrapperr_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        wrapperr_role_depends_on_healthchecks:
        ```

    ??? variable bool "`wrapperr_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        wrapperr_role_diun_enabled: true
        ```

    ??? variable bool "`wrapperr_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        wrapperr_role_dns_enabled: true
        ```

    ??? variable bool "`wrapperr_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        wrapperr_role_docker_controller: true
        ```

    ??? variable list "`wrapperr_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        wrapperr_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`wrapperr_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_docker_volumes_download:
        ```

    ??? variable string "`wrapperr_role_themepark_addons`"

        ```yaml
        # Type: string
        wrapperr_role_themepark_addons:
        ```

    ??? variable string "`wrapperr_role_themepark_app`"

        ```yaml
        # Type: string
        wrapperr_role_themepark_app:
        ```

    ??? variable string "`wrapperr_role_themepark_theme`"

        ```yaml
        # Type: string
        wrapperr_role_themepark_theme:
        ```

    ??? variable string "`wrapperr_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        wrapperr_role_traefik_api_middleware:
        ```

    ??? variable string "`wrapperr_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        wrapperr_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`wrapperr_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        wrapperr_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`wrapperr_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        wrapperr_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`wrapperr_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        wrapperr_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`wrapperr_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        wrapperr_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`wrapperr_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        wrapperr_role_traefik_middleware_http:
        ```

    ??? variable bool "`wrapperr_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`wrapperr_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        wrapperr_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`wrapperr_role_traefik_priority`"

        ```yaml
        # Type: string
        wrapperr_role_traefik_priority:
        ```

    ??? variable bool "`wrapperr_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        wrapperr_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`wrapperr_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        wrapperr_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`wrapperr_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        wrapperr_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`wrapperr_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        wrapperr_role_web_api_http_port:
        ```

    ??? variable string "`wrapperr_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        wrapperr_role_web_api_http_scheme:
        ```

    ??? variable dict "`wrapperr_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        wrapperr_role_web_api_http_serverstransport:
        ```

    ??? variable string "`wrapperr_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        wrapperr_role_web_api_port:
        ```

    ??? variable string "`wrapperr_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        wrapperr_role_web_api_scheme:
        ```

    ??? variable dict "`wrapperr_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        wrapperr_role_web_api_serverstransport:
        ```

    ??? variable list "`wrapperr_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        wrapperr_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            wrapperr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "wrapperr2.{{ user.domain }}"
              - "wrapperr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`wrapperr_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        wrapperr_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            wrapperr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'wrapperr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`wrapperr_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        wrapperr_role_web_http_port:
        ```

    ??? variable string "`wrapperr_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        wrapperr_role_web_http_scheme:
        ```

    ??? variable dict "`wrapperr_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        wrapperr_role_web_http_serverstransport:
        ```

    ??? variable string "`wrapperr_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        wrapperr_role_web_scheme:
        ```

    ??? variable dict "`wrapperr_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        wrapperr_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

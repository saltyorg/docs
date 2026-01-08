---
icon: material/docker
hide:
  - tags
tags:
  - syncthing
  - backup
  - sync
saltbox_automation:
  disabled: false
  sections:
    inventory: true
    overview: true
  inventory:
    show_sections: []
    hide_sections: []
    example_overrides: {}
  app_links:
    - name: Manual
      url: https://docs.syncthing.net
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/linuxserver/syncthing/tags
      type: docker
    - name: Community
      url: https://linuxserver.io/discord
      type: discord
  project_description:
    name: Syncthing
    summary: |
      a free, open-source, peer-to-peer file synchronization utility designed to sync files between devices on a local network or over the Internet.
    link: https://syncthing.net
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Syncthing

## Overview

[Syncthing](https://syncthing.net) is a free, open-source, peer-to-peer file synchronization utility designed to sync files between devices on a local network or over the Internet.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://docs.syncthing.net){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/linuxserver/syncthing/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://linuxserver.io/discord){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-syncthing
```

## Usage

Visit <https://syncthing.iYOUR_DOMAIN_NAMEi>.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        syncthing_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `syncthing_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `syncthing_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`syncthing_name`"

        ```yaml
        # Type: string
        syncthing_name: syncthing
        ```

=== "Web"

    ??? variable string "`syncthing_role_web_subdomain`"

        ```yaml
        # Type: string
        syncthing_role_web_subdomain: "{{ syncthing_name }}"
        ```

    ??? variable string "`syncthing_role_web_domain`"

        ```yaml
        # Type: string
        syncthing_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`syncthing_role_web_port`"

        ```yaml
        # Type: string
        syncthing_role_web_port: "8384"
        ```

    ??? variable string "`syncthing_role_web_url`"

        ```yaml
        # Type: string
        syncthing_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='syncthing') + '.' + lookup('role_var', '_web_domain', role='syncthing')
                                 if (lookup('role_var', '_web_subdomain', role='syncthing') | length > 0)
                                 else lookup('role_var', '_web_domain', role='syncthing')) }}"
        ```

=== "DNS"

    ??? variable string "`syncthing_role_dns_record`"

        ```yaml
        # Type: string
        syncthing_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='syncthing') }}"
        ```

    ??? variable string "`syncthing_role_dns_zone`"

        ```yaml
        # Type: string
        syncthing_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='syncthing') }}"
        ```

    ??? variable bool "`syncthing_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`syncthing_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        syncthing_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`syncthing_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        syncthing_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`syncthing_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        syncthing_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`syncthing_role_traefik_certresolver`"

        ```yaml
        # Type: string
        syncthing_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`syncthing_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_traefik_enabled: true
        ```

    ??? variable bool "`syncthing_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_traefik_api_enabled: false
        ```

    ??? variable string "`syncthing_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        syncthing_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`syncthing_role_docker_container`"

        ```yaml
        # Type: string
        syncthing_role_docker_container: "{{ syncthing_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`syncthing_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_docker_image_pull: true
        ```

    ??? variable string "`syncthing_role_docker_image_repo`"

        ```yaml
        # Type: string
        syncthing_role_docker_image_repo: "lscr.io/linuxserver/syncthing"
        ```

    ??? variable string "`syncthing_role_docker_image_tag`"

        ```yaml
        # Type: string
        syncthing_role_docker_image_tag: "latest"
        ```

    ??? variable string "`syncthing_role_docker_image`"

        ```yaml
        # Type: string
        syncthing_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='syncthing') }}:{{ lookup('role_var', '_docker_image_tag', role='syncthing') }}"
        ```

    <h5>Ports</h5>

    ??? variable list "`syncthing_role_docker_ports_default`"

        ```yaml
        # Type: list
        syncthing_role_docker_ports_default:
          - "22000:22000/tcp"
          - "22000:22000/udp"
          - "21027:21027/udp"
        ```

    ??? variable list "`syncthing_role_docker_ports_custom`"

        ```yaml
        # Type: list
        syncthing_role_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    ??? variable dict "`syncthing_role_docker_envs_default`"

        ```yaml
        # Type: dict
        syncthing_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`syncthing_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        syncthing_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`syncthing_role_docker_volumes_default`"

        ```yaml
        # Type: list
        syncthing_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='syncthing') }}:/config"
        ```

    ??? variable list "`syncthing_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        syncthing_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`syncthing_role_docker_hostname`"

        ```yaml
        # Type: string
        syncthing_role_docker_hostname: "{{ syncthing_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`syncthing_role_docker_networks_alias`"

        ```yaml
        # Type: string
        syncthing_role_docker_networks_alias: "{{ syncthing_name }}"
        ```

    ??? variable list "`syncthing_role_docker_networks_default`"

        ```yaml
        # Type: list
        syncthing_role_docker_networks_default: []
        ```

    ??? variable list "`syncthing_role_docker_networks_custom`"

        ```yaml
        # Type: list
        syncthing_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`syncthing_role_docker_restart_policy`"

        ```yaml
        # Type: string
        syncthing_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`syncthing_role_docker_state`"

        ```yaml
        # Type: string
        syncthing_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`syncthing_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        syncthing_role_docker_blkio_weight:
        ```

    ??? variable int "`syncthing_role_docker_cpu_period`"

        ```yaml
        # Type: int
        syncthing_role_docker_cpu_period:
        ```

    ??? variable int "`syncthing_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        syncthing_role_docker_cpu_quota:
        ```

    ??? variable int "`syncthing_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        syncthing_role_docker_cpu_shares:
        ```

    ??? variable string "`syncthing_role_docker_cpus`"

        ```yaml
        # Type: string
        syncthing_role_docker_cpus:
        ```

    ??? variable string "`syncthing_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        syncthing_role_docker_cpuset_cpus:
        ```

    ??? variable string "`syncthing_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        syncthing_role_docker_cpuset_mems:
        ```

    ??? variable string "`syncthing_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        syncthing_role_docker_kernel_memory:
        ```

    ??? variable string "`syncthing_role_docker_memory`"

        ```yaml
        # Type: string
        syncthing_role_docker_memory:
        ```

    ??? variable string "`syncthing_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        syncthing_role_docker_memory_reservation:
        ```

    ??? variable string "`syncthing_role_docker_memory_swap`"

        ```yaml
        # Type: string
        syncthing_role_docker_memory_swap:
        ```

    ??? variable int "`syncthing_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        syncthing_role_docker_memory_swappiness:
        ```

    ??? variable string "`syncthing_role_docker_shm_size`"

        ```yaml
        # Type: string
        syncthing_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`syncthing_role_docker_cap_drop`"

        ```yaml
        # Type: list
        syncthing_role_docker_cap_drop:
        ```

    ??? variable string "`syncthing_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        syncthing_role_docker_cgroupns_mode:
        ```

    ??? variable list "`syncthing_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        syncthing_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`syncthing_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        syncthing_role_docker_device_read_bps:
        ```

    ??? variable list "`syncthing_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        syncthing_role_docker_device_read_iops:
        ```

    ??? variable list "`syncthing_role_docker_device_requests`"

        ```yaml
        # Type: list
        syncthing_role_docker_device_requests:
        ```

    ??? variable list "`syncthing_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        syncthing_role_docker_device_write_bps:
        ```

    ??? variable list "`syncthing_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        syncthing_role_docker_device_write_iops:
        ```

    ??? variable list "`syncthing_role_docker_devices`"

        ```yaml
        # Type: list
        syncthing_role_docker_devices:
        ```

    ??? variable string "`syncthing_role_docker_devices_default`"

        ```yaml
        # Type: string
        syncthing_role_docker_devices_default:
        ```

    ??? variable list "`syncthing_role_docker_groups`"

        ```yaml
        # Type: list
        syncthing_role_docker_groups:
        ```

    ??? variable bool "`syncthing_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_docker_privileged:
        ```

    ??? variable list "`syncthing_role_docker_security_opts`"

        ```yaml
        # Type: list
        syncthing_role_docker_security_opts:
        ```

    ??? variable string "`syncthing_role_docker_user`"

        ```yaml
        # Type: string
        syncthing_role_docker_user:
        ```

    ??? variable string "`syncthing_role_docker_userns_mode`"

        ```yaml
        # Type: string
        syncthing_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`syncthing_role_docker_dns_opts`"

        ```yaml
        # Type: list
        syncthing_role_docker_dns_opts:
        ```

    ??? variable list "`syncthing_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        syncthing_role_docker_dns_search_domains:
        ```

    ??? variable list "`syncthing_role_docker_dns_servers`"

        ```yaml
        # Type: list
        syncthing_role_docker_dns_servers:
        ```

    ??? variable string "`syncthing_role_docker_domainname`"

        ```yaml
        # Type: string
        syncthing_role_docker_domainname:
        ```

    ??? variable list "`syncthing_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        syncthing_role_docker_exposed_ports:
        ```

    ??? variable dict "`syncthing_role_docker_hosts`"

        ```yaml
        # Type: dict
        syncthing_role_docker_hosts:
        ```

    ??? variable bool "`syncthing_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_docker_hosts_use_common:
        ```

    ??? variable string "`syncthing_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        syncthing_role_docker_ipc_mode:
        ```

    ??? variable list "`syncthing_role_docker_links`"

        ```yaml
        # Type: list
        syncthing_role_docker_links:
        ```

    ??? variable string "`syncthing_role_docker_network_mode`"

        ```yaml
        # Type: string
        syncthing_role_docker_network_mode:
        ```

    ??? variable string "`syncthing_role_docker_pid_mode`"

        ```yaml
        # Type: string
        syncthing_role_docker_pid_mode:
        ```

    ??? variable string "`syncthing_role_docker_uts`"

        ```yaml
        # Type: string
        syncthing_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`syncthing_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_docker_keep_volumes:
        ```

    ??? variable list "`syncthing_role_docker_mounts`"

        ```yaml
        # Type: list
        syncthing_role_docker_mounts:
        ```

    ??? variable dict "`syncthing_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        syncthing_role_docker_storage_opts:
        ```

    ??? variable list "`syncthing_role_docker_tmpfs`"

        ```yaml
        # Type: list
        syncthing_role_docker_tmpfs:
        ```

    ??? variable string "`syncthing_role_docker_volume_driver`"

        ```yaml
        # Type: string
        syncthing_role_docker_volume_driver:
        ```

    ??? variable list "`syncthing_role_docker_volumes_from`"

        ```yaml
        # Type: list
        syncthing_role_docker_volumes_from:
        ```

    ??? variable bool "`syncthing_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_docker_volumes_global:
        ```

    ??? variable string "`syncthing_role_docker_working_dir`"

        ```yaml
        # Type: string
        syncthing_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`syncthing_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_docker_auto_remove:
        ```

    ??? variable bool "`syncthing_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_docker_cleanup:
        ```

    ??? variable string "`syncthing_role_docker_force_kill`"

        ```yaml
        # Type: string
        syncthing_role_docker_force_kill:
        ```

    ??? variable dict "`syncthing_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        syncthing_role_docker_healthcheck:
        ```

    ??? variable int "`syncthing_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        syncthing_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`syncthing_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_docker_init:
        ```

    ??? variable string "`syncthing_role_docker_kill_signal`"

        ```yaml
        # Type: string
        syncthing_role_docker_kill_signal:
        ```

    ??? variable string "`syncthing_role_docker_log_driver`"

        ```yaml
        # Type: string
        syncthing_role_docker_log_driver:
        ```

    ??? variable dict "`syncthing_role_docker_log_options`"

        ```yaml
        # Type: dict
        syncthing_role_docker_log_options:
        ```

    ??? variable bool "`syncthing_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_docker_oom_killer:
        ```

    ??? variable int "`syncthing_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        syncthing_role_docker_oom_score_adj:
        ```

    ??? variable bool "`syncthing_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_docker_output_logs:
        ```

    ??? variable bool "`syncthing_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_docker_paused:
        ```

    ??? variable bool "`syncthing_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_docker_recreate:
        ```

    ??? variable int "`syncthing_role_docker_restart_retries`"

        ```yaml
        # Type: int
        syncthing_role_docker_restart_retries:
        ```

    ??? variable int "`syncthing_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        syncthing_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`syncthing_role_docker_capabilities`"

        ```yaml
        # Type: list
        syncthing_role_docker_capabilities:
        ```

    ??? variable string "`syncthing_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        syncthing_role_docker_cgroup_parent:
        ```

    ??? variable list "`syncthing_role_docker_commands`"

        ```yaml
        # Type: list
        syncthing_role_docker_commands:
        ```

    ??? variable int "`syncthing_role_docker_create_timeout`"

        ```yaml
        # Type: int
        syncthing_role_docker_create_timeout:
        ```

    ??? variable string "`syncthing_role_docker_entrypoint`"

        ```yaml
        # Type: string
        syncthing_role_docker_entrypoint:
        ```

    ??? variable string "`syncthing_role_docker_env_file`"

        ```yaml
        # Type: string
        syncthing_role_docker_env_file:
        ```

    ??? variable dict "`syncthing_role_docker_labels`"

        ```yaml
        # Type: dict
        syncthing_role_docker_labels:
        ```

    ??? variable bool "`syncthing_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_docker_labels_use_common:
        ```

    ??? variable bool "`syncthing_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_docker_read_only:
        ```

    ??? variable string "`syncthing_role_docker_runtime`"

        ```yaml
        # Type: string
        syncthing_role_docker_runtime:
        ```

    ??? variable list "`syncthing_role_docker_sysctls`"

        ```yaml
        # Type: list
        syncthing_role_docker_sysctls:
        ```

    ??? variable list "`syncthing_role_docker_ulimits`"

        ```yaml
        # Type: list
        syncthing_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`syncthing_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        syncthing_role_autoheal_enabled: true
        ```

    ??? variable string "`syncthing_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        syncthing_role_depends_on: ""
        ```

    ??? variable string "`syncthing_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        syncthing_role_depends_on_delay: "0"
        ```

    ??? variable string "`syncthing_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        syncthing_role_depends_on_healthchecks:
        ```

    ??? variable bool "`syncthing_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        syncthing_role_diun_enabled: true
        ```

    ??? variable bool "`syncthing_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        syncthing_role_dns_enabled: true
        ```

    ??? variable bool "`syncthing_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        syncthing_role_docker_controller: true
        ```

    ??? variable string "`syncthing_role_docker_image_repo`"

        ```yaml
        # Type: string
        syncthing_role_docker_image_repo:
        ```

    ??? variable string "`syncthing_role_docker_image_tag`"

        ```yaml
        # Type: string
        syncthing_role_docker_image_tag:
        ```

    ??? variable bool "`syncthing_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_docker_volumes_download:
        ```

    ??? variable string "`syncthing_role_paths_location`"

        ```yaml
        # Type: string
        syncthing_role_paths_location:
        ```

    ??? variable string "`syncthing_role_themepark_addons`"

        ```yaml
        # Type: string
        syncthing_role_themepark_addons:
        ```

    ??? variable string "`syncthing_role_themepark_app`"

        ```yaml
        # Type: string
        syncthing_role_themepark_app:
        ```

    ??? variable string "`syncthing_role_themepark_theme`"

        ```yaml
        # Type: string
        syncthing_role_themepark_theme:
        ```

    ??? variable dict "`syncthing_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        syncthing_role_traefik_api_endpoint:
        ```

    ??? variable string "`syncthing_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        syncthing_role_traefik_api_middleware:
        ```

    ??? variable string "`syncthing_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        syncthing_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`syncthing_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        syncthing_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`syncthing_role_traefik_certresolver`"

        ```yaml
        # Type: string
        syncthing_role_traefik_certresolver:
        ```

    ??? variable bool "`syncthing_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        syncthing_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`syncthing_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        syncthing_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`syncthing_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        syncthing_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`syncthing_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        syncthing_role_traefik_middleware_http:
        ```

    ??? variable bool "`syncthing_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`syncthing_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        syncthing_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`syncthing_role_traefik_priority`"

        ```yaml
        # Type: string
        syncthing_role_traefik_priority:
        ```

    ??? variable bool "`syncthing_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        syncthing_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`syncthing_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        syncthing_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`syncthing_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        syncthing_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`syncthing_role_web_domain`"

        ```yaml
        # Type: string
        syncthing_role_web_domain:
        ```

    ??? variable list "`syncthing_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        syncthing_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            syncthing_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "syncthing2.{{ user.domain }}"
              - "syncthing.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`syncthing_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        syncthing_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            syncthing_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'syncthing2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`syncthing_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        syncthing_role_web_http_port:
        ```

    ??? variable string "`syncthing_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        syncthing_role_web_http_scheme:
        ```

    ??? variable dict "`syncthing_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        syncthing_role_web_http_serverstransport:
        ```

    ??? variable string "`syncthing_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        syncthing_role_web_scheme:
        ```

    ??? variable dict "`syncthing_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        syncthing_role_web_serverstransport:
        ```

    ??? variable string "`syncthing_role_web_subdomain`"

        ```yaml
        # Type: string
        syncthing_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
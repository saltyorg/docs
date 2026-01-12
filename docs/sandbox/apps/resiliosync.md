---
icon: material/docker
title: Resilio Sync
hide:
  - tags
tags:
  - resiliosync
  - backup
  - sync
saltbox_automation:
  app_links:
    - name: Manual
      url: https://help.resilio.com/hc/en-us/categories/200140177-Get-started-with-Sync
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/resilio/sync/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Resilio Sync
    summary: |
      a proprietary peer-to-peer file synchronization tool that enables users to sync files directly between devices using a modified version of the BitTorrent protocol, without relying on centralized cloud storage.
    link: https://www.resilio.com/sync
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Resilio Sync

## Overview

[Resilio Sync](https://www.resilio.com/sync) is a proprietary peer-to-peer file synchronization tool that enables users to sync files directly between devices using a modified version of the BitTorrent protocol, without relying on centralized cloud storage.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://help.resilio.com/hc/en-us/categories/200140177-Get-started-with-Sync){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/resilio/sync/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-resiliosync
```

## Usage

Visit <https://resiliosync.iYOUR_DOMAIN_NAMEi>.

## Basics

- [:octicons-link-16: Documentation: Resilio Sync Docs](https://help.resilio.com/hc/en-us/articles/204754939-Comprehensive-guide-to-syncing-Desktop-Desktop-){: .header-icons }

- Note: The default data port for this container is 55555. Sync will try to use this port for data transfer, if the port is not open Sync will automatically use a [relay server](https://help.resilio.com/hc/en-us/articles/204754779-What-is-a-Relay-Server-) to make your connection. For best performance, please ensure this port is opened in your firewall.
- Sync's data port can be customized by changing the [Sync settings](https://help.resilio.com/hc/en-us/articles/204762669-Sync-Preferences) as well as adding the following to `/srv/git/saltbox/inventories/host_vars/localhost.yml` and rerunning the installation tag:

```yaml
resiliosync_data_port: "#####"
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        resiliosync_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `resiliosync_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `resiliosync_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`resiliosync_name`"

        ```yaml
        # Type: string
        resiliosync_name: resiliosync
        ```

=== "Settings"

    ??? variable string "`resiliosync_role_data_port`"

        ```yaml
        # Type: string
        resiliosync_role_data_port: "55555"
        ```

=== "Web"

    ??? variable string "`resiliosync_role_web_subdomain`"

        ```yaml
        # Type: string
        resiliosync_role_web_subdomain: "{{ resiliosync_name }}"
        ```

    ??? variable string "`resiliosync_role_web_domain`"

        ```yaml
        # Type: string
        resiliosync_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`resiliosync_role_web_port`"

        ```yaml
        # Type: string
        resiliosync_role_web_port: "8888"
        ```

    ??? variable string "`resiliosync_role_web_url`"

        ```yaml
        # Type: string
        resiliosync_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='resiliosync') + '.' + lookup('role_var', '_web_domain', role='resiliosync')
                                   if (lookup('role_var', '_web_subdomain', role='resiliosync') | length > 0)
                                   else lookup('role_var', '_web_domain', role='resiliosync')) }}"
        ```

=== "DNS"

    ??? variable string "`resiliosync_role_dns_record`"

        ```yaml
        # Type: string
        resiliosync_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='resiliosync') }}"
        ```

    ??? variable string "`resiliosync_role_dns_zone`"

        ```yaml
        # Type: string
        resiliosync_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='resiliosync') }}"
        ```

    ??? variable bool "`resiliosync_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`resiliosync_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        resiliosync_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`resiliosync_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        resiliosync_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`resiliosync_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        resiliosync_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`resiliosync_role_traefik_certresolver`"

        ```yaml
        # Type: string
        resiliosync_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`resiliosync_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_traefik_enabled: true
        ```

    ??? variable bool "`resiliosync_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_traefik_api_enabled: false
        ```

    ??? variable string "`resiliosync_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        resiliosync_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`resiliosync_role_docker_container`"

        ```yaml
        # Type: string
        resiliosync_role_docker_container: "{{ resiliosync_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`resiliosync_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_docker_image_pull: true
        ```

    ??? variable string "`resiliosync_role_docker_image_repo`"

        ```yaml
        # Type: string
        resiliosync_role_docker_image_repo: "resilio/sync"
        ```

    ??? variable string "`resiliosync_role_docker_image_tag`"

        ```yaml
        # Type: string
        resiliosync_role_docker_image_tag: "latest"
        ```

    ??? variable string "`resiliosync_role_docker_image`"

        ```yaml
        # Type: string
        resiliosync_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='resiliosync') }}:{{ lookup('role_var', '_docker_image_tag', role='resiliosync') }}"
        ```

    <h5>Ports</h5>

    ??? variable list "`resiliosync_role_docker_ports_default`"

        ```yaml
        # Type: list
        resiliosync_role_docker_ports_default:
          - "{{ lookup('role_var', '_data_port', role='resiliosync') }}:{{ lookup('role_var', '_data_port', role='resiliosync') }}"
        ```

    ??? variable list "`resiliosync_role_docker_ports_custom`"

        ```yaml
        # Type: list
        resiliosync_role_docker_ports_custom: []
        ```

    <h5>Volumes</h5>

    ??? variable bool "`resiliosync_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_docker_volumes_global: false
        ```

    ??? variable list "`resiliosync_role_docker_volumes_default`"

        ```yaml
        # Type: list
        resiliosync_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='resiliosync') }}:/mnt/sync"
          - "/mnt:/mnt/mounted_folders/mnt"
          - "/home:/mnt/mounted_folders/home"
        ```

    ??? variable list "`resiliosync_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        resiliosync_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`resiliosync_role_docker_hostname`"

        ```yaml
        # Type: string
        resiliosync_role_docker_hostname: "{{ resiliosync_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`resiliosync_role_docker_networks_alias`"

        ```yaml
        # Type: string
        resiliosync_role_docker_networks_alias: "{{ resiliosync_name }}"
        ```

    ??? variable list "`resiliosync_role_docker_networks_default`"

        ```yaml
        # Type: list
        resiliosync_role_docker_networks_default: []
        ```

    ??? variable list "`resiliosync_role_docker_networks_custom`"

        ```yaml
        # Type: list
        resiliosync_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`resiliosync_role_docker_restart_policy`"

        ```yaml
        # Type: string
        resiliosync_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`resiliosync_role_docker_state`"

        ```yaml
        # Type: string
        resiliosync_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`resiliosync_role_docker_user`"

        ```yaml
        # Type: string
        resiliosync_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`resiliosync_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        resiliosync_role_docker_blkio_weight:
        ```

    ??? variable int "`resiliosync_role_docker_cpu_period`"

        ```yaml
        # Type: int
        resiliosync_role_docker_cpu_period:
        ```

    ??? variable int "`resiliosync_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        resiliosync_role_docker_cpu_quota:
        ```

    ??? variable int "`resiliosync_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        resiliosync_role_docker_cpu_shares:
        ```

    ??? variable string "`resiliosync_role_docker_cpus`"

        ```yaml
        # Type: string
        resiliosync_role_docker_cpus:
        ```

    ??? variable string "`resiliosync_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        resiliosync_role_docker_cpuset_cpus:
        ```

    ??? variable string "`resiliosync_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        resiliosync_role_docker_cpuset_mems:
        ```

    ??? variable string "`resiliosync_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        resiliosync_role_docker_kernel_memory:
        ```

    ??? variable string "`resiliosync_role_docker_memory`"

        ```yaml
        # Type: string
        resiliosync_role_docker_memory:
        ```

    ??? variable string "`resiliosync_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        resiliosync_role_docker_memory_reservation:
        ```

    ??? variable string "`resiliosync_role_docker_memory_swap`"

        ```yaml
        # Type: string
        resiliosync_role_docker_memory_swap:
        ```

    ??? variable int "`resiliosync_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        resiliosync_role_docker_memory_swappiness:
        ```

    ??? variable string "`resiliosync_role_docker_shm_size`"

        ```yaml
        # Type: string
        resiliosync_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`resiliosync_role_docker_cap_drop`"

        ```yaml
        # Type: list
        resiliosync_role_docker_cap_drop:
        ```

    ??? variable string "`resiliosync_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        resiliosync_role_docker_cgroupns_mode:
        ```

    ??? variable list "`resiliosync_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        resiliosync_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`resiliosync_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        resiliosync_role_docker_device_read_bps:
        ```

    ??? variable list "`resiliosync_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        resiliosync_role_docker_device_read_iops:
        ```

    ??? variable list "`resiliosync_role_docker_device_requests`"

        ```yaml
        # Type: list
        resiliosync_role_docker_device_requests:
        ```

    ??? variable list "`resiliosync_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        resiliosync_role_docker_device_write_bps:
        ```

    ??? variable list "`resiliosync_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        resiliosync_role_docker_device_write_iops:
        ```

    ??? variable list "`resiliosync_role_docker_devices`"

        ```yaml
        # Type: list
        resiliosync_role_docker_devices:
        ```

    ??? variable string "`resiliosync_role_docker_devices_default`"

        ```yaml
        # Type: string
        resiliosync_role_docker_devices_default:
        ```

    ??? variable list "`resiliosync_role_docker_groups`"

        ```yaml
        # Type: list
        resiliosync_role_docker_groups:
        ```

    ??? variable bool "`resiliosync_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_docker_privileged:
        ```

    ??? variable list "`resiliosync_role_docker_security_opts`"

        ```yaml
        # Type: list
        resiliosync_role_docker_security_opts:
        ```

    ??? variable string "`resiliosync_role_docker_userns_mode`"

        ```yaml
        # Type: string
        resiliosync_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`resiliosync_role_docker_dns_opts`"

        ```yaml
        # Type: list
        resiliosync_role_docker_dns_opts:
        ```

    ??? variable list "`resiliosync_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        resiliosync_role_docker_dns_search_domains:
        ```

    ??? variable list "`resiliosync_role_docker_dns_servers`"

        ```yaml
        # Type: list
        resiliosync_role_docker_dns_servers:
        ```

    ??? variable string "`resiliosync_role_docker_domainname`"

        ```yaml
        # Type: string
        resiliosync_role_docker_domainname:
        ```

    ??? variable list "`resiliosync_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        resiliosync_role_docker_exposed_ports:
        ```

    ??? variable dict "`resiliosync_role_docker_hosts`"

        ```yaml
        # Type: dict
        resiliosync_role_docker_hosts:
        ```

    ??? variable bool "`resiliosync_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_docker_hosts_use_common:
        ```

    ??? variable string "`resiliosync_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        resiliosync_role_docker_ipc_mode:
        ```

    ??? variable list "`resiliosync_role_docker_links`"

        ```yaml
        # Type: list
        resiliosync_role_docker_links:
        ```

    ??? variable string "`resiliosync_role_docker_network_mode`"

        ```yaml
        # Type: string
        resiliosync_role_docker_network_mode:
        ```

    ??? variable string "`resiliosync_role_docker_pid_mode`"

        ```yaml
        # Type: string
        resiliosync_role_docker_pid_mode:
        ```

    ??? variable string "`resiliosync_role_docker_uts`"

        ```yaml
        # Type: string
        resiliosync_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`resiliosync_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_docker_keep_volumes:
        ```

    ??? variable list "`resiliosync_role_docker_mounts`"

        ```yaml
        # Type: list
        resiliosync_role_docker_mounts:
        ```

    ??? variable dict "`resiliosync_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        resiliosync_role_docker_storage_opts:
        ```

    ??? variable list "`resiliosync_role_docker_tmpfs`"

        ```yaml
        # Type: list
        resiliosync_role_docker_tmpfs:
        ```

    ??? variable string "`resiliosync_role_docker_volume_driver`"

        ```yaml
        # Type: string
        resiliosync_role_docker_volume_driver:
        ```

    ??? variable list "`resiliosync_role_docker_volumes_from`"

        ```yaml
        # Type: list
        resiliosync_role_docker_volumes_from:
        ```

    ??? variable string "`resiliosync_role_docker_working_dir`"

        ```yaml
        # Type: string
        resiliosync_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`resiliosync_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_docker_auto_remove:
        ```

    ??? variable bool "`resiliosync_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_docker_cleanup:
        ```

    ??? variable string "`resiliosync_role_docker_force_kill`"

        ```yaml
        # Type: string
        resiliosync_role_docker_force_kill:
        ```

    ??? variable dict "`resiliosync_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        resiliosync_role_docker_healthcheck:
        ```

    ??? variable int "`resiliosync_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        resiliosync_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`resiliosync_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_docker_init:
        ```

    ??? variable string "`resiliosync_role_docker_kill_signal`"

        ```yaml
        # Type: string
        resiliosync_role_docker_kill_signal:
        ```

    ??? variable string "`resiliosync_role_docker_log_driver`"

        ```yaml
        # Type: string
        resiliosync_role_docker_log_driver:
        ```

    ??? variable dict "`resiliosync_role_docker_log_options`"

        ```yaml
        # Type: dict
        resiliosync_role_docker_log_options:
        ```

    ??? variable bool "`resiliosync_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_docker_oom_killer:
        ```

    ??? variable int "`resiliosync_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        resiliosync_role_docker_oom_score_adj:
        ```

    ??? variable bool "`resiliosync_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_docker_output_logs:
        ```

    ??? variable bool "`resiliosync_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_docker_paused:
        ```

    ??? variable bool "`resiliosync_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_docker_recreate:
        ```

    ??? variable int "`resiliosync_role_docker_restart_retries`"

        ```yaml
        # Type: int
        resiliosync_role_docker_restart_retries:
        ```

    ??? variable int "`resiliosync_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        resiliosync_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`resiliosync_role_docker_capabilities`"

        ```yaml
        # Type: list
        resiliosync_role_docker_capabilities:
        ```

    ??? variable string "`resiliosync_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        resiliosync_role_docker_cgroup_parent:
        ```

    ??? variable list "`resiliosync_role_docker_commands`"

        ```yaml
        # Type: list
        resiliosync_role_docker_commands:
        ```

    ??? variable int "`resiliosync_role_docker_create_timeout`"

        ```yaml
        # Type: int
        resiliosync_role_docker_create_timeout:
        ```

    ??? variable string "`resiliosync_role_docker_entrypoint`"

        ```yaml
        # Type: string
        resiliosync_role_docker_entrypoint:
        ```

    ??? variable string "`resiliosync_role_docker_env_file`"

        ```yaml
        # Type: string
        resiliosync_role_docker_env_file:
        ```

    ??? variable dict "`resiliosync_role_docker_envs`"

        ```yaml
        # Type: dict
        resiliosync_role_docker_envs:
        ```

    ??? variable dict "`resiliosync_role_docker_labels`"

        ```yaml
        # Type: dict
        resiliosync_role_docker_labels:
        ```

    ??? variable bool "`resiliosync_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_docker_labels_use_common:
        ```

    ??? variable bool "`resiliosync_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_docker_read_only:
        ```

    ??? variable string "`resiliosync_role_docker_runtime`"

        ```yaml
        # Type: string
        resiliosync_role_docker_runtime:
        ```

    ??? variable list "`resiliosync_role_docker_sysctls`"

        ```yaml
        # Type: list
        resiliosync_role_docker_sysctls:
        ```

    ??? variable list "`resiliosync_role_docker_ulimits`"

        ```yaml
        # Type: list
        resiliosync_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`resiliosync_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        resiliosync_role_autoheal_enabled: true
        ```

    ??? variable string "`resiliosync_role_data_port`"

        ```yaml
        # Type: string (quoted number)
        resiliosync_role_data_port:
        ```

    ??? variable string "`resiliosync_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        resiliosync_role_depends_on: ""
        ```

    ??? variable string "`resiliosync_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        resiliosync_role_depends_on_delay: "0"
        ```

    ??? variable string "`resiliosync_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        resiliosync_role_depends_on_healthchecks:
        ```

    ??? variable bool "`resiliosync_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        resiliosync_role_diun_enabled: true
        ```

    ??? variable bool "`resiliosync_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        resiliosync_role_dns_enabled: true
        ```

    ??? variable bool "`resiliosync_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        resiliosync_role_docker_controller: true
        ```

    ??? variable string "`resiliosync_role_docker_image_repo`"

        ```yaml
        # Type: string
        resiliosync_role_docker_image_repo:
        ```

    ??? variable string "`resiliosync_role_docker_image_tag`"

        ```yaml
        # Type: string
        resiliosync_role_docker_image_tag:
        ```

    ??? variable bool "`resiliosync_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_docker_volumes_download:
        ```

    ??? variable string "`resiliosync_role_paths_location`"

        ```yaml
        # Type: string
        resiliosync_role_paths_location:
        ```

    ??? variable string "`resiliosync_role_themepark_addons`"

        ```yaml
        # Type: string
        resiliosync_role_themepark_addons:
        ```

    ??? variable string "`resiliosync_role_themepark_app`"

        ```yaml
        # Type: string
        resiliosync_role_themepark_app:
        ```

    ??? variable string "`resiliosync_role_themepark_theme`"

        ```yaml
        # Type: string
        resiliosync_role_themepark_theme:
        ```

    ??? variable dict "`resiliosync_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        resiliosync_role_traefik_api_endpoint:
        ```

    ??? variable string "`resiliosync_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        resiliosync_role_traefik_api_middleware:
        ```

    ??? variable string "`resiliosync_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        resiliosync_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`resiliosync_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        resiliosync_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`resiliosync_role_traefik_certresolver`"

        ```yaml
        # Type: string
        resiliosync_role_traefik_certresolver:
        ```

    ??? variable bool "`resiliosync_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        resiliosync_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`resiliosync_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        resiliosync_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`resiliosync_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        resiliosync_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`resiliosync_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        resiliosync_role_traefik_middleware_http:
        ```

    ??? variable bool "`resiliosync_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`resiliosync_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`resiliosync_role_traefik_priority`"

        ```yaml
        # Type: string
        resiliosync_role_traefik_priority:
        ```

    ??? variable bool "`resiliosync_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        resiliosync_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`resiliosync_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        resiliosync_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`resiliosync_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        resiliosync_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`resiliosync_role_web_domain`"

        ```yaml
        # Type: string
        resiliosync_role_web_domain:
        ```

    ??? variable list "`resiliosync_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        resiliosync_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            resiliosync_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "resiliosync2.{{ user.domain }}"
              - "resiliosync.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`resiliosync_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        resiliosync_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            resiliosync_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'resiliosync2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`resiliosync_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        resiliosync_role_web_http_port:
        ```

    ??? variable string "`resiliosync_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        resiliosync_role_web_http_scheme:
        ```

    ??? variable dict "`resiliosync_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        resiliosync_role_web_http_serverstransport:
        ```

    ??? variable string "`resiliosync_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        resiliosync_role_web_scheme:
        ```

    ??? variable dict "`resiliosync_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        resiliosync_role_web_serverstransport:
        ```

    ??? variable string "`resiliosync_role_web_subdomain`"

        ```yaml
        # Type: string
        resiliosync_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
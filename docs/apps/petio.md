---
icon: material/docker
hide:
  - tags
tags:
  - petio
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
      url: https://docs.petio.tv
      type: documentation
    - name: Releases
      url: https://github.com/petio-team/petio/pkgs/container/petio
      type: github
    - name: Community
      url: https://discord.gg/bseGmrUd3N
      type: discord
  project_description:
    name: Petio
    summary: |
      a third party companion app available to Plex server owners to allow their users to request, review and discover content.
    link: https://petio.tv
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Petio

## Overview

[Petio](https://petio.tv) is a third party companion app available to Plex server owners to allow their users to request, review and discover content.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://docs.petio.tv){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/petio-team/petio/pkgs/container/petio){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://discord.gg/bseGmrUd3N){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install petio
```

## Usage

Visit <https://petio.iYOUR_DOMAIN_NAMEi>.

## Basics

- Click Login With Plex and follow the steps to log in.

- After you log in with Plex you will need to specify your Petio specific admin credentials, by default it uses your Plex username and email but you still need to specify your own password.

- After setting up your credentials, you need to pick your Plex server.

- MongoDB: Use `petio-mongo:27017` (assumes default instance and therefore default petio_name otherwise it is the value of `petio_name` plus the `-mongo:27017` suffix)

- Once the last step is finished, you will be presented with a login screen. Use your Plex username and the password you set up on Step 2. You can now get started with configuring Radarr, Sonarr and start requesting!

- See the Petio documentation for more information.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        petio_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `petio_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `petio_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`petio_name`"

        ```yaml
        # Type: string
        petio_name: petio
        ```

=== "Settings"

    ??? variable string "`petio_role_mongodb_version`"

        ```yaml
        # Type: string
        petio_role_mongodb_version: "4.4"
        ```

=== "Web"

    ??? variable string "`petio_role_web_subdomain`"

        ```yaml
        # Type: string
        petio_role_web_subdomain: "{{ petio_name }}"
        ```

    ??? variable string "`petio_role_web_domain`"

        ```yaml
        # Type: string
        petio_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`petio_role_web_port`"

        ```yaml
        # Type: string
        petio_role_web_port: "7777"
        ```

    ??? variable string "`petio_role_web_url`"

        ```yaml
        # Type: string
        petio_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='petio') + '.' + lookup('role_var', '_web_domain', role='petio')
                             if (lookup('role_var', '_web_subdomain', role='petio') | length > 0)
                             else lookup('role_var', '_web_domain', role='petio')) }}"
        ```

=== "DNS"

    ??? variable string "`petio_role_dns_record`"

        ```yaml
        # Type: string
        petio_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='petio') }}"
        ```

    ??? variable string "`petio_role_dns_zone`"

        ```yaml
        # Type: string
        petio_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='petio') }}"
        ```

    ??? variable bool "`petio_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        petio_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`petio_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        petio_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`petio_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        petio_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`petio_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        petio_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`petio_role_traefik_certresolver`"

        ```yaml
        # Type: string
        petio_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`petio_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        petio_role_traefik_enabled: true
        ```

    ??? variable bool "`petio_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        petio_role_traefik_api_enabled: false
        ```

    ??? variable string "`petio_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        petio_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`petio_role_docker_container`"

        ```yaml
        # Type: string
        petio_role_docker_container: "{{ petio_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`petio_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        petio_role_docker_image_pull: true
        ```

    ??? variable string "`petio_role_docker_image_repo`"

        ```yaml
        # Type: string
        petio_role_docker_image_repo: "ghcr.io/petio-team/petio"
        ```

    ??? variable string "`petio_role_docker_image_tag`"

        ```yaml
        # Type: string
        petio_role_docker_image_tag: "latest"
        ```

    ??? variable string "`petio_role_docker_image`"

        ```yaml
        # Type: string
        petio_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='petio') }}:{{ lookup('role_var', '_docker_image_tag', role='petio') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`petio_role_docker_envs_default`"

        ```yaml
        # Type: dict
        petio_role_docker_envs_default:
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`petio_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        petio_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`petio_role_docker_volumes_default`"

        ```yaml
        # Type: list
        petio_role_docker_volumes_default:
          - "{{ petio_role_paths_location }}:/app/api/config"
        ```

    ??? variable list "`petio_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        petio_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`petio_role_docker_hostname`"

        ```yaml
        # Type: string
        petio_role_docker_hostname: "{{ petio_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`petio_role_docker_networks_alias`"

        ```yaml
        # Type: string
        petio_role_docker_networks_alias: "{{ petio_name }}"
        ```

    ??? variable list "`petio_role_docker_networks_default`"

        ```yaml
        # Type: list
        petio_role_docker_networks_default: []
        ```

    ??? variable list "`petio_role_docker_networks_custom`"

        ```yaml
        # Type: list
        petio_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`petio_role_docker_restart_policy`"

        ```yaml
        # Type: string
        petio_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`petio_role_docker_state`"

        ```yaml
        # Type: string
        petio_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`petio_role_docker_user`"

        ```yaml
        # Type: string
        petio_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

    <h5>Dependencies</h5>

    ??? variable string "`petio_role_depends_on`"

        ```yaml
        # Type: string
        petio_role_depends_on: "{{ petio_name }}-mongo"
        ```

    ??? variable string "`petio_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        petio_role_depends_on_delay: "0"
        ```

    ??? variable string "`petio_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        petio_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`petio_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        petio_role_docker_blkio_weight:
        ```

    ??? variable int "`petio_role_docker_cpu_period`"

        ```yaml
        # Type: int
        petio_role_docker_cpu_period:
        ```

    ??? variable int "`petio_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        petio_role_docker_cpu_quota:
        ```

    ??? variable int "`petio_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        petio_role_docker_cpu_shares:
        ```

    ??? variable string "`petio_role_docker_cpus`"

        ```yaml
        # Type: string
        petio_role_docker_cpus:
        ```

    ??? variable string "`petio_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        petio_role_docker_cpuset_cpus:
        ```

    ??? variable string "`petio_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        petio_role_docker_cpuset_mems:
        ```

    ??? variable string "`petio_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        petio_role_docker_kernel_memory:
        ```

    ??? variable string "`petio_role_docker_memory`"

        ```yaml
        # Type: string
        petio_role_docker_memory:
        ```

    ??? variable string "`petio_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        petio_role_docker_memory_reservation:
        ```

    ??? variable string "`petio_role_docker_memory_swap`"

        ```yaml
        # Type: string
        petio_role_docker_memory_swap:
        ```

    ??? variable int "`petio_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        petio_role_docker_memory_swappiness:
        ```

    ??? variable string "`petio_role_docker_shm_size`"

        ```yaml
        # Type: string
        petio_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`petio_role_docker_cap_drop`"

        ```yaml
        # Type: list
        petio_role_docker_cap_drop:
        ```

    ??? variable string "`petio_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        petio_role_docker_cgroupns_mode:
        ```

    ??? variable list "`petio_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        petio_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`petio_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        petio_role_docker_device_read_bps:
        ```

    ??? variable list "`petio_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        petio_role_docker_device_read_iops:
        ```

    ??? variable list "`petio_role_docker_device_requests`"

        ```yaml
        # Type: list
        petio_role_docker_device_requests:
        ```

    ??? variable list "`petio_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        petio_role_docker_device_write_bps:
        ```

    ??? variable list "`petio_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        petio_role_docker_device_write_iops:
        ```

    ??? variable list "`petio_role_docker_devices`"

        ```yaml
        # Type: list
        petio_role_docker_devices:
        ```

    ??? variable string "`petio_role_docker_devices_default`"

        ```yaml
        # Type: string
        petio_role_docker_devices_default:
        ```

    ??? variable list "`petio_role_docker_groups`"

        ```yaml
        # Type: list
        petio_role_docker_groups:
        ```

    ??? variable bool "`petio_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        petio_role_docker_privileged:
        ```

    ??? variable list "`petio_role_docker_security_opts`"

        ```yaml
        # Type: list
        petio_role_docker_security_opts:
        ```

    ??? variable string "`petio_role_docker_userns_mode`"

        ```yaml
        # Type: string
        petio_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`petio_role_docker_dns_opts`"

        ```yaml
        # Type: list
        petio_role_docker_dns_opts:
        ```

    ??? variable list "`petio_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        petio_role_docker_dns_search_domains:
        ```

    ??? variable list "`petio_role_docker_dns_servers`"

        ```yaml
        # Type: list
        petio_role_docker_dns_servers:
        ```

    ??? variable string "`petio_role_docker_domainname`"

        ```yaml
        # Type: string
        petio_role_docker_domainname:
        ```

    ??? variable list "`petio_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        petio_role_docker_exposed_ports:
        ```

    ??? variable dict "`petio_role_docker_hosts`"

        ```yaml
        # Type: dict
        petio_role_docker_hosts:
        ```

    ??? variable bool "`petio_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        petio_role_docker_hosts_use_common:
        ```

    ??? variable string "`petio_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        petio_role_docker_ipc_mode:
        ```

    ??? variable list "`petio_role_docker_links`"

        ```yaml
        # Type: list
        petio_role_docker_links:
        ```

    ??? variable string "`petio_role_docker_network_mode`"

        ```yaml
        # Type: string
        petio_role_docker_network_mode:
        ```

    ??? variable string "`petio_role_docker_pid_mode`"

        ```yaml
        # Type: string
        petio_role_docker_pid_mode:
        ```

    ??? variable list "`petio_role_docker_ports`"

        ```yaml
        # Type: list
        petio_role_docker_ports:
        ```

    ??? variable string "`petio_role_docker_uts`"

        ```yaml
        # Type: string
        petio_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`petio_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        petio_role_docker_keep_volumes:
        ```

    ??? variable list "`petio_role_docker_mounts`"

        ```yaml
        # Type: list
        petio_role_docker_mounts:
        ```

    ??? variable dict "`petio_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        petio_role_docker_storage_opts:
        ```

    ??? variable list "`petio_role_docker_tmpfs`"

        ```yaml
        # Type: list
        petio_role_docker_tmpfs:
        ```

    ??? variable string "`petio_role_docker_volume_driver`"

        ```yaml
        # Type: string
        petio_role_docker_volume_driver:
        ```

    ??? variable list "`petio_role_docker_volumes_from`"

        ```yaml
        # Type: list
        petio_role_docker_volumes_from:
        ```

    ??? variable bool "`petio_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        petio_role_docker_volumes_global:
        ```

    ??? variable string "`petio_role_docker_working_dir`"

        ```yaml
        # Type: string
        petio_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`petio_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        petio_role_docker_auto_remove:
        ```

    ??? variable bool "`petio_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        petio_role_docker_cleanup:
        ```

    ??? variable string "`petio_role_docker_force_kill`"

        ```yaml
        # Type: string
        petio_role_docker_force_kill:
        ```

    ??? variable dict "`petio_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        petio_role_docker_healthcheck:
        ```

    ??? variable int "`petio_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        petio_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`petio_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        petio_role_docker_init:
        ```

    ??? variable string "`petio_role_docker_kill_signal`"

        ```yaml
        # Type: string
        petio_role_docker_kill_signal:
        ```

    ??? variable string "`petio_role_docker_log_driver`"

        ```yaml
        # Type: string
        petio_role_docker_log_driver:
        ```

    ??? variable dict "`petio_role_docker_log_options`"

        ```yaml
        # Type: dict
        petio_role_docker_log_options:
        ```

    ??? variable bool "`petio_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        petio_role_docker_oom_killer:
        ```

    ??? variable int "`petio_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        petio_role_docker_oom_score_adj:
        ```

    ??? variable bool "`petio_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        petio_role_docker_output_logs:
        ```

    ??? variable bool "`petio_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        petio_role_docker_paused:
        ```

    ??? variable bool "`petio_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        petio_role_docker_recreate:
        ```

    ??? variable int "`petio_role_docker_restart_retries`"

        ```yaml
        # Type: int
        petio_role_docker_restart_retries:
        ```

    ??? variable int "`petio_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        petio_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`petio_role_docker_capabilities`"

        ```yaml
        # Type: list
        petio_role_docker_capabilities:
        ```

    ??? variable string "`petio_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        petio_role_docker_cgroup_parent:
        ```

    ??? variable list "`petio_role_docker_commands`"

        ```yaml
        # Type: list
        petio_role_docker_commands:
        ```

    ??? variable int "`petio_role_docker_create_timeout`"

        ```yaml
        # Type: int
        petio_role_docker_create_timeout:
        ```

    ??? variable string "`petio_role_docker_entrypoint`"

        ```yaml
        # Type: string
        petio_role_docker_entrypoint:
        ```

    ??? variable string "`petio_role_docker_env_file`"

        ```yaml
        # Type: string
        petio_role_docker_env_file:
        ```

    ??? variable dict "`petio_role_docker_labels`"

        ```yaml
        # Type: dict
        petio_role_docker_labels:
        ```

    ??? variable bool "`petio_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        petio_role_docker_labels_use_common:
        ```

    ??? variable bool "`petio_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        petio_role_docker_read_only:
        ```

    ??? variable string "`petio_role_docker_runtime`"

        ```yaml
        # Type: string
        petio_role_docker_runtime:
        ```

    ??? variable list "`petio_role_docker_sysctls`"

        ```yaml
        # Type: list
        petio_role_docker_sysctls:
        ```

    ??? variable list "`petio_role_docker_ulimits`"

        ```yaml
        # Type: list
        petio_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`petio_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        petio_role_autoheal_enabled: true
        ```

    ??? variable string "`petio_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        petio_role_depends_on: ""
        ```

    ??? variable string "`petio_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        petio_role_depends_on_delay: "0"
        ```

    ??? variable string "`petio_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        petio_role_depends_on_healthchecks:
        ```

    ??? variable bool "`petio_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        petio_role_diun_enabled: true
        ```

    ??? variable bool "`petio_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        petio_role_dns_enabled: true
        ```

    ??? variable bool "`petio_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        petio_role_docker_controller: true
        ```

    ??? variable string "`petio_role_docker_image_repo`"

        ```yaml
        # Type: string
        petio_role_docker_image_repo:
        ```

    ??? variable string "`petio_role_docker_image_tag`"

        ```yaml
        # Type: string
        petio_role_docker_image_tag:
        ```

    ??? variable bool "`petio_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        petio_role_docker_volumes_download:
        ```

    ??? variable string "`petio_role_themepark_addons`"

        ```yaml
        # Type: string
        petio_role_themepark_addons:
        ```

    ??? variable string "`petio_role_themepark_app`"

        ```yaml
        # Type: string
        petio_role_themepark_app:
        ```

    ??? variable string "`petio_role_themepark_theme`"

        ```yaml
        # Type: string
        petio_role_themepark_theme:
        ```

    ??? variable dict "`petio_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        petio_role_traefik_api_endpoint:
        ```

    ??? variable string "`petio_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        petio_role_traefik_api_middleware:
        ```

    ??? variable string "`petio_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        petio_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`petio_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        petio_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`petio_role_traefik_certresolver`"

        ```yaml
        # Type: string
        petio_role_traefik_certresolver:
        ```

    ??? variable bool "`petio_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        petio_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`petio_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        petio_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`petio_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        petio_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`petio_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        petio_role_traefik_middleware_http:
        ```

    ??? variable bool "`petio_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        petio_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`petio_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        petio_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`petio_role_traefik_priority`"

        ```yaml
        # Type: string
        petio_role_traefik_priority:
        ```

    ??? variable bool "`petio_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        petio_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`petio_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        petio_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`petio_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        petio_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`petio_role_web_domain`"

        ```yaml
        # Type: string
        petio_role_web_domain:
        ```

    ??? variable list "`petio_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        petio_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            petio_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "petio2.{{ user.domain }}"
              - "petio.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`petio_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        petio_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            petio_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'petio2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`petio_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        petio_role_web_http_port:
        ```

    ??? variable string "`petio_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        petio_role_web_http_scheme:
        ```

    ??? variable dict "`petio_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        petio_role_web_http_serverstransport:
        ```

    ??? variable string "`petio_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        petio_role_web_scheme:
        ```

    ??? variable dict "`petio_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        petio_role_web_serverstransport:
        ```

    ??? variable string "`petio_role_web_subdomain`"

        ```yaml
        # Type: string
        petio_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
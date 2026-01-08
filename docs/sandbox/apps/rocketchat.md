---
icon: material/docker
status: draft
hide:
  - tags
tags:
  - rocketchat
  - communication
  - chat
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
      url:
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/rocketchat/rocketchat/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: rocketchat
    summary: |
      a...
    link:
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# rocketchat

## Overview

[rocketchat]() is a...

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/rocketchat/rocketchat/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-rocketchat
```

## Usage

Visit <https://rocketchat.iYOUR_DOMAIN_NAMEi>.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        rocketchat_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `rocketchat_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `rocketchat_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`rocketchat_name`"

        ```yaml
        # Type: string
        rocketchat_name: rocketchat
        ```

=== "Settings"

    ??? variable string "`rocketchat_mongodb_role_docker_image_tag`"

        ```yaml
        # Type: string
        rocketchat_mongodb_role_docker_image_tag: "6"
        ```

    ??? variable list "`rocketchat_mongodb_role_docker_commands`"

        ```yaml
        # Type: list
        rocketchat_mongodb_role_docker_commands:
          - "mongod --oplogSize 128 --replSet rs0"
        ```

    ??? variable list "`rocketchat_mongodb_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        rocketchat_mongodb_role_docker_volumes_custom:
          - "{{ lookup('role_var', '_paths_location', role='rocketchat') }}/init-mongo.js:/docker-entrypoint-initdb.d/init-mongo.js:ro"
        ```

    ??? variable string "`rockatchat_mongodb_role_paths_location`"

        ```yaml
        # Type: string
        rockatchat_mongodb_role_paths_location: "{{ lookup('role_var', '_paths_location', role='rocketchat') }}/mongo"
        ```

=== "Web"

    ??? variable string "`rocketchat_role_web_subdomain`"

        ```yaml
        # Type: string
        rocketchat_role_web_subdomain: "{{ rocketchat_name }}"
        ```

    ??? variable string "`rocketchat_role_web_domain`"

        ```yaml
        # Type: string
        rocketchat_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`rocketchat_role_web_port`"

        ```yaml
        # Type: string
        rocketchat_role_web_port: "3000"
        ```

    ??? variable string "`rocketchat_role_web_url`"

        ```yaml
        # Type: string
        rocketchat_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='rocketchat') + '.' + lookup('role_var', '_web_domain', role='rocketchat')
                                  if (lookup('role_var', '_web_subdomain', role='rocketchat') | length > 0)
                                  else lookup('role_var', '_web_domain', role='rocketchat')) }}"
        ```

=== "DNS"

    ??? variable string "`rocketchat_role_dns_record`"

        ```yaml
        # Type: string
        rocketchat_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='rocketchat') }}"
        ```

    ??? variable string "`rocketchat_role_dns_zone`"

        ```yaml
        # Type: string
        rocketchat_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='rocketchat') }}"
        ```

    ??? variable bool "`rocketchat_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`rocketchat_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        rocketchat_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`rocketchat_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        rocketchat_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`rocketchat_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        rocketchat_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`rocketchat_role_traefik_certresolver`"

        ```yaml
        # Type: string
        rocketchat_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`rocketchat_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_traefik_enabled: true
        ```

    ??? variable bool "`rocketchat_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_traefik_api_enabled: false
        ```

    ??? variable string "`rocketchat_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        rocketchat_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`rocketchat_role_docker_container`"

        ```yaml
        # Type: string
        rocketchat_role_docker_container: "{{ rocketchat_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`rocketchat_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_docker_image_pull: true
        ```

    ??? variable string "`rocketchat_role_docker_image_tag`"

        ```yaml
        # Type: string
        rocketchat_role_docker_image_tag: "latest"
        ```

    ??? variable string "`rocketchat_role_docker_image_repo`"

        ```yaml
        # Type: string
        rocketchat_role_docker_image_repo: "rocketchat/rocket.chat"
        ```

    ??? variable string "`rocketchat_role_docker_image`"

        ```yaml
        # Type: string
        rocketchat_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='rocketchat') }}:{{ lookup('role_var', '_docker_image_tag', role='rocketchat') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`rocketchat_role_docker_envs_default`"

        ```yaml
        # Type: dict
        rocketchat_role_docker_envs_default:
          TZ: "{{ tz }}"
          ROOT_URL: "{{ lookup('role_var', '_web_url', role='rocketchat') }}"
          MONGO_URL: "mongodb://rocketchat-mongo:27017/rocketchat?replicaSet=rs0&directConnection=true"
          MONGO_OPLOG_URL: "mongodb://rocketchat-mongo:27017/local?replicaSet=rs0&directConnection=true"
          DEPLOY_METHOD: "docker"
        ```

    ??? variable dict "`rocketchat_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        rocketchat_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`rocketchat_role_docker_volumes_default`"

        ```yaml
        # Type: list
        rocketchat_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='rocketchat') }}/uploads:/app/uploads"
        ```

    ??? variable list "`rocketchat_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        rocketchat_role_docker_volumes_custom: []
        ```

    <h5>Mounts</h5>

    ??? variable list "`rocketchat_role_docker_mounts_default`"

        ```yaml
        # Type: list
        rocketchat_role_docker_mounts_default:
          - target: /tmp
            type: tmpfs
        ```

    ??? variable list "`rocketchat_role_docker_mounts_custom`"

        ```yaml
        # Type: list
        rocketchat_role_docker_mounts_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`rocketchat_role_docker_hostname`"

        ```yaml
        # Type: string
        rocketchat_role_docker_hostname: "{{ rocketchat_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`rocketchat_role_docker_networks_alias`"

        ```yaml
        # Type: string
        rocketchat_role_docker_networks_alias: "{{ rocketchat_name }}"
        ```

    ??? variable list "`rocketchat_role_docker_networks_default`"

        ```yaml
        # Type: list
        rocketchat_role_docker_networks_default: []
        ```

    ??? variable list "`rocketchat_role_docker_networks_custom`"

        ```yaml
        # Type: list
        rocketchat_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`rocketchat_role_docker_restart_policy`"

        ```yaml
        # Type: string
        rocketchat_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`rocketchat_role_docker_state`"

        ```yaml
        # Type: string
        rocketchat_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`rocketchat_role_depends_on`"

        ```yaml
        # Type: string
        rocketchat_role_depends_on: "rocketchat_db"
        ```

    ??? variable string "`rocketchat_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        rocketchat_role_depends_on_delay: "0"
        ```

    ??? variable string "`rocketchat_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        rocketchat_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`rocketchat_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        rocketchat_role_docker_blkio_weight:
        ```

    ??? variable int "`rocketchat_role_docker_cpu_period`"

        ```yaml
        # Type: int
        rocketchat_role_docker_cpu_period:
        ```

    ??? variable int "`rocketchat_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        rocketchat_role_docker_cpu_quota:
        ```

    ??? variable int "`rocketchat_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        rocketchat_role_docker_cpu_shares:
        ```

    ??? variable string "`rocketchat_role_docker_cpus`"

        ```yaml
        # Type: string
        rocketchat_role_docker_cpus:
        ```

    ??? variable string "`rocketchat_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        rocketchat_role_docker_cpuset_cpus:
        ```

    ??? variable string "`rocketchat_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        rocketchat_role_docker_cpuset_mems:
        ```

    ??? variable string "`rocketchat_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        rocketchat_role_docker_kernel_memory:
        ```

    ??? variable string "`rocketchat_role_docker_memory`"

        ```yaml
        # Type: string
        rocketchat_role_docker_memory:
        ```

    ??? variable string "`rocketchat_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        rocketchat_role_docker_memory_reservation:
        ```

    ??? variable string "`rocketchat_role_docker_memory_swap`"

        ```yaml
        # Type: string
        rocketchat_role_docker_memory_swap:
        ```

    ??? variable int "`rocketchat_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        rocketchat_role_docker_memory_swappiness:
        ```

    ??? variable string "`rocketchat_role_docker_shm_size`"

        ```yaml
        # Type: string
        rocketchat_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`rocketchat_role_docker_cap_drop`"

        ```yaml
        # Type: list
        rocketchat_role_docker_cap_drop:
        ```

    ??? variable string "`rocketchat_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        rocketchat_role_docker_cgroupns_mode:
        ```

    ??? variable list "`rocketchat_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        rocketchat_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`rocketchat_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        rocketchat_role_docker_device_read_bps:
        ```

    ??? variable list "`rocketchat_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        rocketchat_role_docker_device_read_iops:
        ```

    ??? variable list "`rocketchat_role_docker_device_requests`"

        ```yaml
        # Type: list
        rocketchat_role_docker_device_requests:
        ```

    ??? variable list "`rocketchat_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        rocketchat_role_docker_device_write_bps:
        ```

    ??? variable list "`rocketchat_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        rocketchat_role_docker_device_write_iops:
        ```

    ??? variable list "`rocketchat_role_docker_devices`"

        ```yaml
        # Type: list
        rocketchat_role_docker_devices:
        ```

    ??? variable string "`rocketchat_role_docker_devices_default`"

        ```yaml
        # Type: string
        rocketchat_role_docker_devices_default:
        ```

    ??? variable list "`rocketchat_role_docker_groups`"

        ```yaml
        # Type: list
        rocketchat_role_docker_groups:
        ```

    ??? variable bool "`rocketchat_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_docker_privileged:
        ```

    ??? variable list "`rocketchat_role_docker_security_opts`"

        ```yaml
        # Type: list
        rocketchat_role_docker_security_opts:
        ```

    ??? variable string "`rocketchat_role_docker_user`"

        ```yaml
        # Type: string
        rocketchat_role_docker_user:
        ```

    ??? variable string "`rocketchat_role_docker_userns_mode`"

        ```yaml
        # Type: string
        rocketchat_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`rocketchat_role_docker_dns_opts`"

        ```yaml
        # Type: list
        rocketchat_role_docker_dns_opts:
        ```

    ??? variable list "`rocketchat_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        rocketchat_role_docker_dns_search_domains:
        ```

    ??? variable list "`rocketchat_role_docker_dns_servers`"

        ```yaml
        # Type: list
        rocketchat_role_docker_dns_servers:
        ```

    ??? variable string "`rocketchat_role_docker_domainname`"

        ```yaml
        # Type: string
        rocketchat_role_docker_domainname:
        ```

    ??? variable list "`rocketchat_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        rocketchat_role_docker_exposed_ports:
        ```

    ??? variable dict "`rocketchat_role_docker_hosts`"

        ```yaml
        # Type: dict
        rocketchat_role_docker_hosts:
        ```

    ??? variable bool "`rocketchat_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_docker_hosts_use_common:
        ```

    ??? variable string "`rocketchat_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        rocketchat_role_docker_ipc_mode:
        ```

    ??? variable list "`rocketchat_role_docker_links`"

        ```yaml
        # Type: list
        rocketchat_role_docker_links:
        ```

    ??? variable string "`rocketchat_role_docker_network_mode`"

        ```yaml
        # Type: string
        rocketchat_role_docker_network_mode:
        ```

    ??? variable string "`rocketchat_role_docker_pid_mode`"

        ```yaml
        # Type: string
        rocketchat_role_docker_pid_mode:
        ```

    ??? variable list "`rocketchat_role_docker_ports`"

        ```yaml
        # Type: list
        rocketchat_role_docker_ports:
        ```

    ??? variable string "`rocketchat_role_docker_uts`"

        ```yaml
        # Type: string
        rocketchat_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`rocketchat_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_docker_keep_volumes:
        ```

    ??? variable dict "`rocketchat_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        rocketchat_role_docker_storage_opts:
        ```

    ??? variable list "`rocketchat_role_docker_tmpfs`"

        ```yaml
        # Type: list
        rocketchat_role_docker_tmpfs:
        ```

    ??? variable string "`rocketchat_role_docker_volume_driver`"

        ```yaml
        # Type: string
        rocketchat_role_docker_volume_driver:
        ```

    ??? variable list "`rocketchat_role_docker_volumes_from`"

        ```yaml
        # Type: list
        rocketchat_role_docker_volumes_from:
        ```

    ??? variable bool "`rocketchat_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_docker_volumes_global:
        ```

    ??? variable string "`rocketchat_role_docker_working_dir`"

        ```yaml
        # Type: string
        rocketchat_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`rocketchat_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_docker_auto_remove:
        ```

    ??? variable bool "`rocketchat_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_docker_cleanup:
        ```

    ??? variable string "`rocketchat_role_docker_force_kill`"

        ```yaml
        # Type: string
        rocketchat_role_docker_force_kill:
        ```

    ??? variable dict "`rocketchat_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        rocketchat_role_docker_healthcheck:
        ```

    ??? variable int "`rocketchat_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        rocketchat_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`rocketchat_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_docker_init:
        ```

    ??? variable string "`rocketchat_role_docker_kill_signal`"

        ```yaml
        # Type: string
        rocketchat_role_docker_kill_signal:
        ```

    ??? variable string "`rocketchat_role_docker_log_driver`"

        ```yaml
        # Type: string
        rocketchat_role_docker_log_driver:
        ```

    ??? variable dict "`rocketchat_role_docker_log_options`"

        ```yaml
        # Type: dict
        rocketchat_role_docker_log_options:
        ```

    ??? variable bool "`rocketchat_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_docker_oom_killer:
        ```

    ??? variable int "`rocketchat_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        rocketchat_role_docker_oom_score_adj:
        ```

    ??? variable bool "`rocketchat_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_docker_output_logs:
        ```

    ??? variable bool "`rocketchat_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_docker_paused:
        ```

    ??? variable bool "`rocketchat_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_docker_recreate:
        ```

    ??? variable int "`rocketchat_role_docker_restart_retries`"

        ```yaml
        # Type: int
        rocketchat_role_docker_restart_retries:
        ```

    ??? variable int "`rocketchat_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        rocketchat_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`rocketchat_role_docker_capabilities`"

        ```yaml
        # Type: list
        rocketchat_role_docker_capabilities:
        ```

    ??? variable string "`rocketchat_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        rocketchat_role_docker_cgroup_parent:
        ```

    ??? variable list "`rocketchat_role_docker_commands`"

        ```yaml
        # Type: list
        rocketchat_role_docker_commands:
        ```

    ??? variable int "`rocketchat_role_docker_create_timeout`"

        ```yaml
        # Type: int
        rocketchat_role_docker_create_timeout:
        ```

    ??? variable string "`rocketchat_role_docker_entrypoint`"

        ```yaml
        # Type: string
        rocketchat_role_docker_entrypoint:
        ```

    ??? variable string "`rocketchat_role_docker_env_file`"

        ```yaml
        # Type: string
        rocketchat_role_docker_env_file:
        ```

    ??? variable dict "`rocketchat_role_docker_labels`"

        ```yaml
        # Type: dict
        rocketchat_role_docker_labels:
        ```

    ??? variable bool "`rocketchat_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_docker_labels_use_common:
        ```

    ??? variable bool "`rocketchat_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_docker_read_only:
        ```

    ??? variable string "`rocketchat_role_docker_runtime`"

        ```yaml
        # Type: string
        rocketchat_role_docker_runtime:
        ```

    ??? variable list "`rocketchat_role_docker_sysctls`"

        ```yaml
        # Type: list
        rocketchat_role_docker_sysctls:
        ```

    ??? variable list "`rocketchat_role_docker_ulimits`"

        ```yaml
        # Type: list
        rocketchat_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`rocketchat_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        rocketchat_role_autoheal_enabled: true
        ```

    ??? variable string "`rocketchat_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        rocketchat_role_depends_on: ""
        ```

    ??? variable string "`rocketchat_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        rocketchat_role_depends_on_delay: "0"
        ```

    ??? variable string "`rocketchat_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        rocketchat_role_depends_on_healthchecks:
        ```

    ??? variable bool "`rocketchat_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        rocketchat_role_diun_enabled: true
        ```

    ??? variable bool "`rocketchat_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        rocketchat_role_dns_enabled: true
        ```

    ??? variable bool "`rocketchat_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        rocketchat_role_docker_controller: true
        ```

    ??? variable string "`rocketchat_role_docker_image_repo`"

        ```yaml
        # Type: string
        rocketchat_role_docker_image_repo:
        ```

    ??? variable string "`rocketchat_role_docker_image_tag`"

        ```yaml
        # Type: string
        rocketchat_role_docker_image_tag:
        ```

    ??? variable bool "`rocketchat_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_docker_volumes_download:
        ```

    ??? variable string "`rocketchat_role_paths_location`"

        ```yaml
        # Type: string
        rocketchat_role_paths_location:
        ```

    ??? variable string "`rocketchat_role_themepark_addons`"

        ```yaml
        # Type: string
        rocketchat_role_themepark_addons:
        ```

    ??? variable string "`rocketchat_role_themepark_app`"

        ```yaml
        # Type: string
        rocketchat_role_themepark_app:
        ```

    ??? variable string "`rocketchat_role_themepark_theme`"

        ```yaml
        # Type: string
        rocketchat_role_themepark_theme:
        ```

    ??? variable dict "`rocketchat_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        rocketchat_role_traefik_api_endpoint:
        ```

    ??? variable string "`rocketchat_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        rocketchat_role_traefik_api_middleware:
        ```

    ??? variable string "`rocketchat_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        rocketchat_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`rocketchat_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        rocketchat_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`rocketchat_role_traefik_certresolver`"

        ```yaml
        # Type: string
        rocketchat_role_traefik_certresolver:
        ```

    ??? variable bool "`rocketchat_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        rocketchat_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`rocketchat_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        rocketchat_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`rocketchat_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        rocketchat_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`rocketchat_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        rocketchat_role_traefik_middleware_http:
        ```

    ??? variable bool "`rocketchat_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`rocketchat_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`rocketchat_role_traefik_priority`"

        ```yaml
        # Type: string
        rocketchat_role_traefik_priority:
        ```

    ??? variable bool "`rocketchat_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        rocketchat_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`rocketchat_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        rocketchat_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`rocketchat_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        rocketchat_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`rocketchat_role_web_domain`"

        ```yaml
        # Type: string
        rocketchat_role_web_domain:
        ```

    ??? variable list "`rocketchat_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        rocketchat_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            rocketchat_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "rocketchat2.{{ user.domain }}"
              - "rocketchat.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`rocketchat_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        rocketchat_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            rocketchat_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'rocketchat2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`rocketchat_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        rocketchat_role_web_http_port:
        ```

    ??? variable string "`rocketchat_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        rocketchat_role_web_http_scheme:
        ```

    ??? variable dict "`rocketchat_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        rocketchat_role_web_http_serverstransport:
        ```

    ??? variable string "`rocketchat_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        rocketchat_role_web_scheme:
        ```

    ??? variable dict "`rocketchat_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        rocketchat_role_web_serverstransport:
        ```

    ??? variable string "`rocketchat_role_web_subdomain`"

        ```yaml
        # Type: string
        rocketchat_role_web_subdomain:
        ```

    ??? variable string "`rocketchat_role_web_url`"

        ```yaml
        # Type: string
        rocketchat_role_web_url:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
icon: material/docker
hide:
  - tags
tags:
  - wikijs
  - documentation
  - wiki
saltbox_automation:
  app_links:
    - name: Manual
      url: https://docs.requarks.io
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/requarks/wiki/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Wikijs
    summary: |-
      a modern, lightweight and powerful wiki app built on NodeJS.
    link: https://js.wiki/
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Wikijs

## Overview

[Wikijs](https://js.wiki/) is a modern, lightweight and powerful wiki app built on NodeJS.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://docs.requarks.io){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/requarks/wiki/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-wikijs
```

## Usage

Visit <https://wikijs.iYOUR_DOMAIN_NAMEi>.

## Basics

!!! info
    📢 No default user is configured until you run through the setup screen, so you should ideally run through setup as soon as the container is deployed to secure the site. It is not behind authelia by default.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        wikijs_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `wikijs_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `wikijs_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`wikijs_name`"

        ```yaml
        # Type: string
        wikijs_name: wikijs
        ```

=== "Settings"

    ??? variable bool "`wikijs_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_postgres_deploy: true
        ```

    ??? variable string "`wikijs_role_postgres_name`"

        ```yaml
        # Type: string
        wikijs_role_postgres_name: "{{ wikijs_name }}-postgres"
        ```

    ??? variable string "`wikijs_role_postgres_user`"

        ```yaml
        # Type: string
        wikijs_role_postgres_user: "{{ postgres_role_docker_env_user }}"
        ```

    ??? variable string "`wikijs_role_postgres_password`"

        ```yaml
        # Type: string
        wikijs_role_postgres_password: "{{ postgres_role_docker_env_password }}"
        ```

    ??? variable string "`wikijs_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        wikijs_role_postgres_docker_env_db: "{{ wikijs_name }}"
        ```

    ??? variable string "`wikijs_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        wikijs_role_postgres_docker_image_tag: "15-alpine"
        ```

    ??? variable string "`wikijs_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        wikijs_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable dict "`wikijs_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        wikijs_role_postgres_docker_healthcheck:
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='wikijs') }} -U {{ postgres_role_docker_env_user }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`wikijs_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        wikijs_role_postgres_paths_folder: "{{ wikijs_name }}"
        ```

    ??? variable string "`wikijs_role_postgres_paths_location`"

        ```yaml
        # Type: string
        wikijs_role_postgres_paths_location: "{{ server_appdata_path }}/{{ wikijs_role_postgres_paths_folder }}/postgres"
        ```

=== "Web"

    ??? variable string "`wikijs_role_web_subdomain`"

        ```yaml
        # Type: string
        wikijs_role_web_subdomain: "{{ wikijs_name }}"
        ```

    ??? variable string "`wikijs_role_web_domain`"

        ```yaml
        # Type: string
        wikijs_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`wikijs_role_web_port`"

        ```yaml
        # Type: string
        wikijs_role_web_port: "3000"
        ```

    ??? variable string "`wikijs_role_web_url`"

        ```yaml
        # Type: string
        wikijs_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='wikijs') + '.' + lookup('role_var', '_web_domain', role='wikijs')
                              if (lookup('role_var', '_web_subdomain', role='wikijs') | length > 0)
                              else lookup('role_var', '_web_domain', role='wikijs')) }}"
        ```

=== "DNS"

    ??? variable string "`wikijs_role_dns_record`"

        ```yaml
        # Type: string
        wikijs_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='wikijs') }}"
        ```

    ??? variable string "`wikijs_role_dns_zone`"

        ```yaml
        # Type: string
        wikijs_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='wikijs') }}"
        ```

    ??? variable bool "`wikijs_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`wikijs_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        wikijs_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`wikijs_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        wikijs_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`wikijs_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        wikijs_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`wikijs_role_traefik_certresolver`"

        ```yaml
        # Type: string
        wikijs_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`wikijs_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_traefik_enabled: true
        ```

    ??? variable bool "`wikijs_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_traefik_api_enabled: true
        ```

    ??? variable string "`wikijs_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        wikijs_role_traefik_api_endpoint: "PathPrefix(`/graphql`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`wikijs_role_docker_container`"

        ```yaml
        # Type: string
        wikijs_role_docker_container: "{{ wikijs_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`wikijs_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_docker_image_pull: true
        ```

    ??? variable string "`wikijs_role_docker_image_repo`"

        ```yaml
        # Type: string
        wikijs_role_docker_image_repo: "ghcr.io/requarks/wiki"
        ```

    ??? variable string "`wikijs_role_docker_image_tag`"

        ```yaml
        # Type: string
        wikijs_role_docker_image_tag: "2"
        ```

    ??? variable string "`wikijs_role_docker_image`"

        ```yaml
        # Type: string
        wikijs_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='wikijs') }}:{{ lookup('role_var', '_docker_image_tag', role='wikijs') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`wikijs_role_docker_envs_default`"

        ```yaml
        # Type: dict
        wikijs_role_docker_envs_default:
          TZ: "{{ tz }}"
          DB_TYPE: "postgres"
          DB_HOST: "{{ lookup('role_var', '_postgres_name', role='wikijs') }}"
          DB_PORT: "5432"
          DB_USER: "{{ lookup('role_var', '_postgres_user', role='wikijs') }}"
          DB_PASS: "{{ lookup('role_var', '_postgres_password', role='wikijs') }}"
          DB_NAME: "{{ lookup('role_var', '_postgres_docker_env_db', role='wikijs') }}"
        ```

    ??? variable dict "`wikijs_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        wikijs_role_docker_envs_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`wikijs_role_docker_hostname`"

        ```yaml
        # Type: string
        wikijs_role_docker_hostname: "{{ wikijs_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`wikijs_role_docker_networks_alias`"

        ```yaml
        # Type: string
        wikijs_role_docker_networks_alias: "{{ wikijs_name }}"
        ```

    ??? variable list "`wikijs_role_docker_networks_default`"

        ```yaml
        # Type: list
        wikijs_role_docker_networks_default: []
        ```

    ??? variable list "`wikijs_role_docker_networks_custom`"

        ```yaml
        # Type: list
        wikijs_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`wikijs_role_docker_restart_policy`"

        ```yaml
        # Type: string
        wikijs_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`wikijs_role_docker_state`"

        ```yaml
        # Type: string
        wikijs_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`wikijs_role_depends_on`"

        ```yaml
        # Type: string
        wikijs_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='wikijs') }}"
        ```

    ??? variable string "`wikijs_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        wikijs_role_depends_on_delay: "0"
        ```

    ??? variable string "`wikijs_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        wikijs_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`wikijs_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        wikijs_role_docker_blkio_weight:
        ```

    ??? variable int "`wikijs_role_docker_cpu_period`"

        ```yaml
        # Type: int
        wikijs_role_docker_cpu_period:
        ```

    ??? variable int "`wikijs_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        wikijs_role_docker_cpu_quota:
        ```

    ??? variable int "`wikijs_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        wikijs_role_docker_cpu_shares:
        ```

    ??? variable string "`wikijs_role_docker_cpus`"

        ```yaml
        # Type: string
        wikijs_role_docker_cpus:
        ```

    ??? variable string "`wikijs_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        wikijs_role_docker_cpuset_cpus:
        ```

    ??? variable string "`wikijs_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        wikijs_role_docker_cpuset_mems:
        ```

    ??? variable string "`wikijs_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        wikijs_role_docker_kernel_memory:
        ```

    ??? variable string "`wikijs_role_docker_memory`"

        ```yaml
        # Type: string
        wikijs_role_docker_memory:
        ```

    ??? variable string "`wikijs_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        wikijs_role_docker_memory_reservation:
        ```

    ??? variable string "`wikijs_role_docker_memory_swap`"

        ```yaml
        # Type: string
        wikijs_role_docker_memory_swap:
        ```

    ??? variable int "`wikijs_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        wikijs_role_docker_memory_swappiness:
        ```

    ??? variable string "`wikijs_role_docker_shm_size`"

        ```yaml
        # Type: string
        wikijs_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`wikijs_role_docker_cap_drop`"

        ```yaml
        # Type: list
        wikijs_role_docker_cap_drop:
        ```

    ??? variable string "`wikijs_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        wikijs_role_docker_cgroupns_mode:
        ```

    ??? variable list "`wikijs_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        wikijs_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`wikijs_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        wikijs_role_docker_device_read_bps:
        ```

    ??? variable list "`wikijs_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        wikijs_role_docker_device_read_iops:
        ```

    ??? variable list "`wikijs_role_docker_device_requests`"

        ```yaml
        # Type: list
        wikijs_role_docker_device_requests:
        ```

    ??? variable list "`wikijs_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        wikijs_role_docker_device_write_bps:
        ```

    ??? variable list "`wikijs_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        wikijs_role_docker_device_write_iops:
        ```

    ??? variable list "`wikijs_role_docker_devices`"

        ```yaml
        # Type: list
        wikijs_role_docker_devices:
        ```

    ??? variable string "`wikijs_role_docker_devices_default`"

        ```yaml
        # Type: string
        wikijs_role_docker_devices_default:
        ```

    ??? variable list "`wikijs_role_docker_groups`"

        ```yaml
        # Type: list
        wikijs_role_docker_groups:
        ```

    ??? variable bool "`wikijs_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_docker_privileged:
        ```

    ??? variable list "`wikijs_role_docker_security_opts`"

        ```yaml
        # Type: list
        wikijs_role_docker_security_opts:
        ```

    ??? variable string "`wikijs_role_docker_user`"

        ```yaml
        # Type: string
        wikijs_role_docker_user:
        ```

    ??? variable string "`wikijs_role_docker_userns_mode`"

        ```yaml
        # Type: string
        wikijs_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`wikijs_role_docker_dns_opts`"

        ```yaml
        # Type: list
        wikijs_role_docker_dns_opts:
        ```

    ??? variable list "`wikijs_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        wikijs_role_docker_dns_search_domains:
        ```

    ??? variable list "`wikijs_role_docker_dns_servers`"

        ```yaml
        # Type: list
        wikijs_role_docker_dns_servers:
        ```

    ??? variable string "`wikijs_role_docker_domainname`"

        ```yaml
        # Type: string
        wikijs_role_docker_domainname:
        ```

    ??? variable list "`wikijs_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        wikijs_role_docker_exposed_ports:
        ```

    ??? variable dict "`wikijs_role_docker_hosts`"

        ```yaml
        # Type: dict
        wikijs_role_docker_hosts:
        ```

    ??? variable bool "`wikijs_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_docker_hosts_use_common:
        ```

    ??? variable string "`wikijs_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        wikijs_role_docker_ipc_mode:
        ```

    ??? variable list "`wikijs_role_docker_links`"

        ```yaml
        # Type: list
        wikijs_role_docker_links:
        ```

    ??? variable string "`wikijs_role_docker_network_mode`"

        ```yaml
        # Type: string
        wikijs_role_docker_network_mode:
        ```

    ??? variable string "`wikijs_role_docker_pid_mode`"

        ```yaml
        # Type: string
        wikijs_role_docker_pid_mode:
        ```

    ??? variable list "`wikijs_role_docker_ports`"

        ```yaml
        # Type: list
        wikijs_role_docker_ports:
        ```

    ??? variable string "`wikijs_role_docker_uts`"

        ```yaml
        # Type: string
        wikijs_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`wikijs_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_docker_keep_volumes:
        ```

    ??? variable list "`wikijs_role_docker_mounts`"

        ```yaml
        # Type: list
        wikijs_role_docker_mounts:
        ```

    ??? variable dict "`wikijs_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        wikijs_role_docker_storage_opts:
        ```

    ??? variable list "`wikijs_role_docker_tmpfs`"

        ```yaml
        # Type: list
        wikijs_role_docker_tmpfs:
        ```

    ??? variable string "`wikijs_role_docker_volume_driver`"

        ```yaml
        # Type: string
        wikijs_role_docker_volume_driver:
        ```

    ??? variable list "`wikijs_role_docker_volumes`"

        ```yaml
        # Type: list
        wikijs_role_docker_volumes:
        ```

    ??? variable list "`wikijs_role_docker_volumes_from`"

        ```yaml
        # Type: list
        wikijs_role_docker_volumes_from:
        ```

    ??? variable bool "`wikijs_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_docker_volumes_global:
        ```

    ??? variable string "`wikijs_role_docker_working_dir`"

        ```yaml
        # Type: string
        wikijs_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`wikijs_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_docker_auto_remove:
        ```

    ??? variable bool "`wikijs_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_docker_cleanup:
        ```

    ??? variable string "`wikijs_role_docker_force_kill`"

        ```yaml
        # Type: string
        wikijs_role_docker_force_kill:
        ```

    ??? variable dict "`wikijs_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        wikijs_role_docker_healthcheck:
        ```

    ??? variable int "`wikijs_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        wikijs_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`wikijs_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_docker_init:
        ```

    ??? variable string "`wikijs_role_docker_kill_signal`"

        ```yaml
        # Type: string
        wikijs_role_docker_kill_signal:
        ```

    ??? variable string "`wikijs_role_docker_log_driver`"

        ```yaml
        # Type: string
        wikijs_role_docker_log_driver:
        ```

    ??? variable dict "`wikijs_role_docker_log_options`"

        ```yaml
        # Type: dict
        wikijs_role_docker_log_options:
        ```

    ??? variable bool "`wikijs_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_docker_oom_killer:
        ```

    ??? variable int "`wikijs_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        wikijs_role_docker_oom_score_adj:
        ```

    ??? variable bool "`wikijs_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_docker_output_logs:
        ```

    ??? variable bool "`wikijs_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_docker_paused:
        ```

    ??? variable bool "`wikijs_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_docker_recreate:
        ```

    ??? variable int "`wikijs_role_docker_restart_retries`"

        ```yaml
        # Type: int
        wikijs_role_docker_restart_retries:
        ```

    ??? variable int "`wikijs_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        wikijs_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`wikijs_role_docker_capabilities`"

        ```yaml
        # Type: list
        wikijs_role_docker_capabilities:
        ```

    ??? variable string "`wikijs_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        wikijs_role_docker_cgroup_parent:
        ```

    ??? variable list "`wikijs_role_docker_commands`"

        ```yaml
        # Type: list
        wikijs_role_docker_commands:
        ```

    ??? variable int "`wikijs_role_docker_create_timeout`"

        ```yaml
        # Type: int
        wikijs_role_docker_create_timeout:
        ```

    ??? variable string "`wikijs_role_docker_entrypoint`"

        ```yaml
        # Type: string
        wikijs_role_docker_entrypoint:
        ```

    ??? variable string "`wikijs_role_docker_env_file`"

        ```yaml
        # Type: string
        wikijs_role_docker_env_file:
        ```

    ??? variable dict "`wikijs_role_docker_labels`"

        ```yaml
        # Type: dict
        wikijs_role_docker_labels:
        ```

    ??? variable bool "`wikijs_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_docker_labels_use_common:
        ```

    ??? variable bool "`wikijs_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_docker_read_only:
        ```

    ??? variable string "`wikijs_role_docker_runtime`"

        ```yaml
        # Type: string
        wikijs_role_docker_runtime:
        ```

    ??? variable list "`wikijs_role_docker_sysctls`"

        ```yaml
        # Type: list
        wikijs_role_docker_sysctls:
        ```

    ??? variable list "`wikijs_role_docker_ulimits`"

        ```yaml
        # Type: list
        wikijs_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`wikijs_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        wikijs_role_autoheal_enabled: true
        ```

    ??? variable string "`wikijs_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        wikijs_role_depends_on: ""
        ```

    ??? variable string "`wikijs_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        wikijs_role_depends_on_delay: "0"
        ```

    ??? variable string "`wikijs_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        wikijs_role_depends_on_healthchecks:
        ```

    ??? variable bool "`wikijs_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        wikijs_role_diun_enabled: true
        ```

    ??? variable bool "`wikijs_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        wikijs_role_dns_enabled: true
        ```

    ??? variable bool "`wikijs_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        wikijs_role_docker_controller: true
        ```

    ??? variable string "`wikijs_role_docker_image_repo`"

        ```yaml
        # Type: string
        wikijs_role_docker_image_repo:
        ```

    ??? variable string "`wikijs_role_docker_image_tag`"

        ```yaml
        # Type: string
        wikijs_role_docker_image_tag:
        ```

    ??? variable bool "`wikijs_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_docker_volumes_download:
        ```

    ??? variable string "`wikijs_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        wikijs_role_postgres_docker_env_db:
        ```

    ??? variable string "`wikijs_role_postgres_name`"

        ```yaml
        # Type: string
        wikijs_role_postgres_name:
        ```

    ??? variable string "`wikijs_role_postgres_password`"

        ```yaml
        # Type: string
        wikijs_role_postgres_password:
        ```

    ??? variable string "`wikijs_role_postgres_user`"

        ```yaml
        # Type: string
        wikijs_role_postgres_user:
        ```

    ??? variable string "`wikijs_role_themepark_addons`"

        ```yaml
        # Type: string
        wikijs_role_themepark_addons:
        ```

    ??? variable string "`wikijs_role_themepark_app`"

        ```yaml
        # Type: string
        wikijs_role_themepark_app:
        ```

    ??? variable string "`wikijs_role_themepark_theme`"

        ```yaml
        # Type: string
        wikijs_role_themepark_theme:
        ```

    ??? variable dict "`wikijs_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        wikijs_role_traefik_api_endpoint:
        ```

    ??? variable string "`wikijs_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        wikijs_role_traefik_api_middleware:
        ```

    ??? variable string "`wikijs_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        wikijs_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`wikijs_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        wikijs_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`wikijs_role_traefik_certresolver`"

        ```yaml
        # Type: string
        wikijs_role_traefik_certresolver:
        ```

    ??? variable bool "`wikijs_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        wikijs_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`wikijs_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        wikijs_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`wikijs_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        wikijs_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`wikijs_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        wikijs_role_traefik_middleware_http:
        ```

    ??? variable bool "`wikijs_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`wikijs_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        wikijs_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`wikijs_role_traefik_priority`"

        ```yaml
        # Type: string
        wikijs_role_traefik_priority:
        ```

    ??? variable bool "`wikijs_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        wikijs_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`wikijs_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        wikijs_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`wikijs_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        wikijs_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`wikijs_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        wikijs_role_web_api_http_port:
        ```

    ??? variable string "`wikijs_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        wikijs_role_web_api_http_scheme:
        ```

    ??? variable dict "`wikijs_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        wikijs_role_web_api_http_serverstransport:
        ```

    ??? variable string "`wikijs_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        wikijs_role_web_api_port:
        ```

    ??? variable string "`wikijs_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        wikijs_role_web_api_scheme:
        ```

    ??? variable dict "`wikijs_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        wikijs_role_web_api_serverstransport:
        ```

    ??? variable string "`wikijs_role_web_domain`"

        ```yaml
        # Type: string
        wikijs_role_web_domain:
        ```

    ??? variable list "`wikijs_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        wikijs_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            wikijs_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "wikijs2.{{ user.domain }}"
              - "wikijs.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`wikijs_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        wikijs_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            wikijs_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'wikijs2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`wikijs_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        wikijs_role_web_http_port:
        ```

    ??? variable string "`wikijs_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        wikijs_role_web_http_scheme:
        ```

    ??? variable dict "`wikijs_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        wikijs_role_web_http_serverstransport:
        ```

    ??? variable string "`wikijs_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        wikijs_role_web_scheme:
        ```

    ??? variable dict "`wikijs_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        wikijs_role_web_serverstransport:
        ```

    ??? variable string "`wikijs_role_web_subdomain`"

        ```yaml
        # Type: string
        wikijs_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
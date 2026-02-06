---
icon: material/docker
status: outdated
hide:
  - tags
tags:
  - immich
  - photos
  - backup
saltbox_automation:
  app_links:
    - name: Manual
      url: https://immich.app/docs/overview/introduction
      type: documentation
    - name: Releases
      url:
      type: releases
    - name: Community
      url:
      type: community
  project_description:
    name: Immich
    summary: |-
      a self-hosted photo and video backup tool, similar to google photos and apple photos.
    link: https://immich.app/
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Immich

## Overview

[Immich](https://immich.app/) is a self-hosted photo and video backup tool, similar to google photos and apple photos.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://immich.app/docs/overview/introduction){ .md-button .md-button--stretch }

[:fontawesome-solid-newspaper:**Releases**](){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-immich
```

## Usage

Visit <https://immich.iYOUR_DOMAIN_NAMEi>.

## Basics

!!! info
    📢 Again, no default user is configured until you run through the setup screen, so you would ideally run through setup as soon as immich is deployed to secure the site. It is not behind authelia by default.

???tip
    In Administration > Settings is a button to copy the current admin configuration to your clipboard. So you can just grab it from there, and paste it into a file.

If you would like to have the config file available, create a new config file (e.g. immich.config, and the config format is `.json`) and map it in inventory; just keep in mind that this disallows you from configuring Immich admin settings from the web ui.

```yaml
immich_docker_envs_custom:
  IMMICH_CONFIG_FILE: "/config/immich.config"
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        immich_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `immich_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `immich_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`immich_name`"

        ```yaml
        # Type: string
        immich_name: immich
        ```

=== "Settings"

    ??? variable string "`immich_role_photos_location`"

        ```yaml
        # Type: string
        immich_role_photos_location: "/mnt/unionfs/Media/Photos"
        ```

    ??? variable bool "`immich_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        immich_role_postgres_deploy: true
        ```

    ??? variable string "`immich_role_postgres_name`"

        ```yaml
        # Type: string
        immich_role_postgres_name: "{{ immich_name }}-postgres"
        ```

    ??? variable string "`immich_role_postgres_user`"

        ```yaml
        # If empty it will fallback to postgres role default
        # Type: string
        immich_role_postgres_user: ""
        ```

    ??? variable string "`immich_role_postgres_password`"

        ```yaml
        # If empty it will fallback to postgres role default
        # Type: string
        immich_role_postgres_password: ""
        ```

    ??? variable string "`immich_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        immich_role_postgres_docker_env_db: "{{ immich_name }}"
        ```

    ??? variable string "`immich_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        immich_role_postgres_docker_image_tag: "14-vectorchord0.4.3-pgvectors0.2.0"
        ```

    ??? variable string "`immich_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        immich_role_postgres_docker_image_repo: "ghcr.io/immich-app/postgres"
        ```

    ??? variable dict "`immich_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        immich_role_postgres_docker_healthcheck:
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='immich') }} -U {{ lookup('role_var', '_postgres_user', role='immich') if (lookup('role_var', '_postgres_user', role='immich') | length > 0) else lookup('role_var', '_docker_env_user', role='postgres') }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`immich_role_postgres_docker_shm_size`"

        ```yaml
        # Type: string
        immich_role_postgres_docker_shm_size: "128M"
        ```

    ??? variable string "`immich_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        immich_role_postgres_paths_folder: "{{ immich_name }}"
        ```

    ??? variable string "`immich_role_postgres_paths_location`"

        ```yaml
        # Type: string
        immich_role_postgres_paths_location: "{{ server_appdata_path }}/{{ immich_role_postgres_paths_folder }}/postgres"
        ```

    ??? variable dict "`immich_role_postgres_docker_envs_custom`"

        ```yaml
        # Type: dict
        immich_role_postgres_docker_envs_custom:
          POSTGRES_INITDB_ARGS: '--data-checksums'
        ```

=== "Web"

    ??? variable string "`immich_role_web_subdomain`"

        ```yaml
        # Type: string
        immich_role_web_subdomain: "{{ immich_name }}"
        ```

    ??? variable string "`immich_role_web_domain`"

        ```yaml
        # Type: string
        immich_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`immich_role_web_port`"

        ```yaml
        # Type: string
        immich_role_web_port: "8080"
        ```

    ??? variable string "`immich_role_web_url`"

        ```yaml
        # Type: string
        immich_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='immich') + '.' + lookup('role_var', '_web_domain', role='immich')
                              if (lookup('role_var', '_web_subdomain', role='immich') | length > 0)
                              else lookup('role_var', '_web_domain', role='immich')) }}"
        ```

=== "DNS"

    ??? variable string "`immich_role_dns_record`"

        ```yaml
        # Type: string
        immich_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='immich') }}"
        ```

    ??? variable string "`immich_role_dns_zone`"

        ```yaml
        # Type: string
        immich_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='immich') }}"
        ```

    ??? variable bool "`immich_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        immich_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`immich_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        immich_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`immich_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        immich_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`immich_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        immich_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`immich_role_traefik_certresolver`"

        ```yaml
        # Type: string
        immich_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`immich_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        immich_role_traefik_enabled: true
        ```

    ??? variable bool "`immich_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        immich_role_traefik_api_enabled: false
        ```

    ??? variable string "`immich_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        immich_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`immich_role_docker_container`"

        ```yaml
        # Type: string
        immich_role_docker_container: "{{ immich_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`immich_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        immich_role_docker_image_pull: true
        ```

    ??? variable string "`immich_role_docker_image_repo`"

        ```yaml
        # Type: string
        immich_role_docker_image_repo: "ghcr.io/imagegenius/immich"
        ```

    ??? variable string "`immich_role_docker_image_tag`"

        ```yaml
        # Type: string
        immich_role_docker_image_tag: "latest"
        ```

    ??? variable string "`immich_role_docker_image`"

        ```yaml
        # Type: string
        immich_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='immich') }}:{{ lookup('role_var', '_docker_image_tag', role='immich') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`immich_role_docker_envs_default`"

        ```yaml
        # Type: dict
        immich_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          DB_HOSTNAME: "{{ lookup('role_var', '_postgres_name', role='immich') }}"
          DB_USERNAME: "{{ lookup('role_var', '_postgres_user', role='immich')
                         if (lookup('role_var', '_postgres_user', role='immich') | length > 0)
                         else lookup('role_var', '_docker_env_user', role='postgres') }}"
          DB_PASSWORD: "{{ lookup('role_var', '_postgres_password', role='immich')
                         if (lookup('role_var', '_postgres_password', role='immich') | length > 0)
                         else lookup('role_var', '_docker_env_password', role='postgres') }}"
          DB_DATABASE_NAME: "{{ lookup('role_var', '_postgres_docker_env_db', role='immich') }}"
          REDIS_HOSTNAME: "{{ immich_name }}-redis"
          DISABLE_MACHINE_LEARNING: "false"
          MACHINE_LEARNING_WORKERS: "1"
          MACHINE_LEARNING_WORKER_TIMEOUT: "120"
        ```

    ??? variable dict "`immich_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        immich_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`immich_role_docker_volumes_default`"

        ```yaml
        # Type: list
        immich_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='immich') }}:/config"
          - "{{ lookup('role_var', '_photos_location', role='immich') }}:/photos"
        ```

    ??? variable list "`immich_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        immich_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`immich_role_docker_hostname`"

        ```yaml
        # Type: string
        immich_role_docker_hostname: "{{ immich_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`immich_role_docker_networks_alias`"

        ```yaml
        # Type: string
        immich_role_docker_networks_alias: "{{ immich_name }}"
        ```

    ??? variable list "`immich_role_docker_networks_default`"

        ```yaml
        # Type: list
        immich_role_docker_networks_default: []
        ```

    ??? variable list "`immich_role_docker_networks_custom`"

        ```yaml
        # Type: list
        immich_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`immich_role_docker_restart_policy`"

        ```yaml
        # Type: string
        immich_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`immich_role_docker_state`"

        ```yaml
        # Type: string
        immich_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`immich_role_depends_on`"

        ```yaml
        # Type: string
        immich_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='immich') }},{{ immich_name }}-redis"
        ```

    ??? variable string "`immich_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        immich_role_depends_on_delay: "0"
        ```

    ??? variable string "`immich_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        immich_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`immich_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        immich_role_docker_blkio_weight:
        ```

    ??? variable int "`immich_role_docker_cpu_period`"

        ```yaml
        # Type: int
        immich_role_docker_cpu_period:
        ```

    ??? variable int "`immich_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        immich_role_docker_cpu_quota:
        ```

    ??? variable int "`immich_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        immich_role_docker_cpu_shares:
        ```

    ??? variable string "`immich_role_docker_cpus`"

        ```yaml
        # Type: string
        immich_role_docker_cpus:
        ```

    ??? variable string "`immich_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        immich_role_docker_cpuset_cpus:
        ```

    ??? variable string "`immich_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        immich_role_docker_cpuset_mems:
        ```

    ??? variable string "`immich_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        immich_role_docker_kernel_memory:
        ```

    ??? variable string "`immich_role_docker_memory`"

        ```yaml
        # Type: string
        immich_role_docker_memory:
        ```

    ??? variable string "`immich_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        immich_role_docker_memory_reservation:
        ```

    ??? variable string "`immich_role_docker_memory_swap`"

        ```yaml
        # Type: string
        immich_role_docker_memory_swap:
        ```

    ??? variable int "`immich_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        immich_role_docker_memory_swappiness:
        ```

    ??? variable string "`immich_role_docker_shm_size`"

        ```yaml
        # Type: string
        immich_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`immich_role_docker_cap_drop`"

        ```yaml
        # Type: list
        immich_role_docker_cap_drop:
        ```

    ??? variable string "`immich_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        immich_role_docker_cgroupns_mode:
        ```

    ??? variable list "`immich_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        immich_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`immich_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        immich_role_docker_device_read_bps:
        ```

    ??? variable list "`immich_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        immich_role_docker_device_read_iops:
        ```

    ??? variable list "`immich_role_docker_device_requests`"

        ```yaml
        # Type: list
        immich_role_docker_device_requests:
        ```

    ??? variable list "`immich_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        immich_role_docker_device_write_bps:
        ```

    ??? variable list "`immich_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        immich_role_docker_device_write_iops:
        ```

    ??? variable list "`immich_role_docker_devices`"

        ```yaml
        # Type: list
        immich_role_docker_devices:
        ```

    ??? variable list "`immich_role_docker_groups`"

        ```yaml
        # Type: list
        immich_role_docker_groups:
        ```

    ??? variable bool "`immich_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        immich_role_docker_privileged:
        ```

    ??? variable list "`immich_role_docker_security_opts`"

        ```yaml
        # Type: list
        immich_role_docker_security_opts:
        ```

    ??? variable string "`immich_role_docker_user`"

        ```yaml
        # Type: string
        immich_role_docker_user:
        ```

    ??? variable string "`immich_role_docker_userns_mode`"

        ```yaml
        # Type: string
        immich_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`immich_role_docker_dns_opts`"

        ```yaml
        # Type: list
        immich_role_docker_dns_opts:
        ```

    ??? variable list "`immich_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        immich_role_docker_dns_search_domains:
        ```

    ??? variable list "`immich_role_docker_dns_servers`"

        ```yaml
        # Type: list
        immich_role_docker_dns_servers:
        ```

    ??? variable string "`immich_role_docker_domainname`"

        ```yaml
        # Type: string
        immich_role_docker_domainname:
        ```

    ??? variable list "`immich_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        immich_role_docker_exposed_ports:
        ```

    ??? variable dict "`immich_role_docker_hosts`"

        ```yaml
        # Type: dict
        immich_role_docker_hosts:
        ```

    ??? variable bool "`immich_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        immich_role_docker_hosts_use_common:
        ```

    ??? variable string "`immich_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        immich_role_docker_ipc_mode:
        ```

    ??? variable list "`immich_role_docker_links`"

        ```yaml
        # Type: list
        immich_role_docker_links:
        ```

    ??? variable string "`immich_role_docker_network_mode`"

        ```yaml
        # Type: string
        immich_role_docker_network_mode:
        ```

    ??? variable string "`immich_role_docker_pid_mode`"

        ```yaml
        # Type: string
        immich_role_docker_pid_mode:
        ```

    ??? variable list "`immich_role_docker_ports`"

        ```yaml
        # Type: list
        immich_role_docker_ports:
        ```

    ??? variable string "`immich_role_docker_uts`"

        ```yaml
        # Type: string
        immich_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`immich_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        immich_role_docker_keep_volumes:
        ```

    ??? variable list "`immich_role_docker_mounts`"

        ```yaml
        # Type: list
        immich_role_docker_mounts:
        ```

    ??? variable dict "`immich_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        immich_role_docker_storage_opts:
        ```

    ??? variable list "`immich_role_docker_tmpfs`"

        ```yaml
        # Type: list
        immich_role_docker_tmpfs:
        ```

    ??? variable string "`immich_role_docker_volume_driver`"

        ```yaml
        # Type: string
        immich_role_docker_volume_driver:
        ```

    ??? variable list "`immich_role_docker_volumes_from`"

        ```yaml
        # Type: list
        immich_role_docker_volumes_from:
        ```

    ??? variable bool "`immich_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        immich_role_docker_volumes_global:
        ```

    ??? variable string "`immich_role_docker_working_dir`"

        ```yaml
        # Type: string
        immich_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`immich_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        immich_role_docker_auto_remove:
        ```

    ??? variable bool "`immich_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        immich_role_docker_cleanup:
        ```

    ??? variable string "`immich_role_docker_force_kill`"

        ```yaml
        # Type: string
        immich_role_docker_force_kill:
        ```

    ??? variable dict "`immich_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        immich_role_docker_healthcheck:
        ```

    ??? variable int "`immich_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        immich_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`immich_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        immich_role_docker_init:
        ```

    ??? variable string "`immich_role_docker_kill_signal`"

        ```yaml
        # Type: string
        immich_role_docker_kill_signal:
        ```

    ??? variable string "`immich_role_docker_log_driver`"

        ```yaml
        # Type: string
        immich_role_docker_log_driver:
        ```

    ??? variable dict "`immich_role_docker_log_options`"

        ```yaml
        # Type: dict
        immich_role_docker_log_options:
        ```

    ??? variable bool "`immich_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        immich_role_docker_oom_killer:
        ```

    ??? variable int "`immich_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        immich_role_docker_oom_score_adj:
        ```

    ??? variable bool "`immich_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        immich_role_docker_output_logs:
        ```

    ??? variable bool "`immich_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        immich_role_docker_paused:
        ```

    ??? variable bool "`immich_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        immich_role_docker_recreate:
        ```

    ??? variable int "`immich_role_docker_restart_retries`"

        ```yaml
        # Type: int
        immich_role_docker_restart_retries:
        ```

    ??? variable string "`immich_role_docker_stop_signal`"

        ```yaml
        # Type: string
        immich_role_docker_stop_signal:
        ```

    ??? variable int "`immich_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        immich_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`immich_role_docker_capabilities`"

        ```yaml
        # Type: list
        immich_role_docker_capabilities:
        ```

    ??? variable string "`immich_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        immich_role_docker_cgroup_parent:
        ```

    ??? variable list "`immich_role_docker_commands`"

        ```yaml
        # Type: list
        immich_role_docker_commands:
        ```

    ??? variable int "`immich_role_docker_create_timeout`"

        ```yaml
        # Type: int
        immich_role_docker_create_timeout:
        ```

    ??? variable string "`immich_role_docker_dev_dri`"

        ```yaml
        # Type: string
        immich_role_docker_dev_dri:
        ```

    ??? variable string "`immich_role_docker_entrypoint`"

        ```yaml
        # Type: string
        immich_role_docker_entrypoint:
        ```

    ??? variable string "`immich_role_docker_env_file`"

        ```yaml
        # Type: string
        immich_role_docker_env_file:
        ```

    ??? variable dict "`immich_role_docker_labels`"

        ```yaml
        # Type: dict
        immich_role_docker_labels:
        ```

    ??? variable bool "`immich_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        immich_role_docker_labels_use_common:
        ```

    ??? variable bool "`immich_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        immich_role_docker_read_only:
        ```

    ??? variable string "`immich_role_docker_runtime`"

        ```yaml
        # Type: string
        immich_role_docker_runtime:
        ```

    ??? variable list "`immich_role_docker_sysctls`"

        ```yaml
        # Type: list
        immich_role_docker_sysctls:
        ```

    ??? variable list "`immich_role_docker_ulimits`"

        ```yaml
        # Type: list
        immich_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`immich_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        immich_role_autoheal_enabled: true
        ```

    ??? variable bool "`immich_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        immich_role_diun_enabled: true
        ```

    ??? variable bool "`immich_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        immich_role_dns_enabled: true
        ```

    ??? variable bool "`immich_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        immich_role_docker_controller: true
        ```

    ??? variable list "`immich_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        immich_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`immich_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        immich_role_docker_volumes_download:
        ```

    ??? variable string "`immich_role_themepark_addons`"

        ```yaml
        # Type: string
        immich_role_themepark_addons:
        ```

    ??? variable string "`immich_role_themepark_app`"

        ```yaml
        # Type: string
        immich_role_themepark_app:
        ```

    ??? variable string "`immich_role_themepark_theme`"

        ```yaml
        # Type: string
        immich_role_themepark_theme:
        ```

    ??? variable string "`immich_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        immich_role_traefik_api_middleware:
        ```

    ??? variable string "`immich_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        immich_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`immich_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        immich_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`immich_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        immich_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`immich_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        immich_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`immich_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        immich_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`immich_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        immich_role_traefik_middleware_http:
        ```

    ??? variable bool "`immich_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        immich_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`immich_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        immich_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`immich_role_traefik_priority`"

        ```yaml
        # Type: string
        immich_role_traefik_priority:
        ```

    ??? variable bool "`immich_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        immich_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`immich_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        immich_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`immich_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        immich_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`immich_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        immich_role_web_api_http_port:
        ```

    ??? variable string "`immich_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        immich_role_web_api_http_scheme:
        ```

    ??? variable dict "`immich_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        immich_role_web_api_http_serverstransport:
        ```

    ??? variable string "`immich_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        immich_role_web_api_port:
        ```

    ??? variable string "`immich_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        immich_role_web_api_scheme:
        ```

    ??? variable dict "`immich_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        immich_role_web_api_serverstransport:
        ```

    ??? variable list "`immich_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        immich_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            immich_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "immich2.{{ user.domain }}"
              - "immich.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`immich_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        immich_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            immich_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'immich2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`immich_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        immich_role_web_http_port:
        ```

    ??? variable string "`immich_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        immich_role_web_http_scheme:
        ```

    ??? variable dict "`immich_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        immich_role_web_http_serverstransport:
        ```

    ??? variable string "`immich_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        immich_role_web_scheme:
        ```

    ??? variable dict "`immich_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        immich_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

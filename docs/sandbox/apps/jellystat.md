---
icon: material/docker
hide:
  - tags
tags:
  - jellystat
  - jellyfin
  - statistics
saltbox_automation:
  app_links:
    - name: Manual
      url:
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/cyfershepard/jellystat/tags
      type: docker
    - name: Community
      url: https://discord.gg/9SMBj2RyEe
      type: discord
  project_description:
    name: Jellystat
    summary: |-
      a free and open source statistics web application for Jellyfin that provides a dashboard with information about the server, libraries, users, and playback activity. Still in development with some expected functionality gaps.
    link: https://github.com/CyferShepard/Jellystat
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Jellystat

## Overview

[Jellystat](https://github.com/CyferShepard/Jellystat) is a free and open source statistics web application for Jellyfin that provides a dashboard with information about the server, libraries, users, and playback activity. Still in development with some expected functionality gaps.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/cyfershepard/jellystat/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://discord.gg/9SMBj2RyEe){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-jellystat
```

## Usage

Visit <https://jellystat.iYOUR_DOMAIN_NAMEi>.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        jellystat_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `jellystat_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `jellystat_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`jellystat_name`"

        ```yaml
        # Type: string
        jellystat_name: jellystat
        ```

=== "Settings"

    ??? variable bool "`jellystat_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_postgres_deploy: true
        ```

    ??? variable string "`jellystat_role_postgres_name`"

        ```yaml
        # Type: string
        jellystat_role_postgres_name: "{{ jellystat_name }}-postgres"
        ```

    ??? variable string "`jellystat_role_postgres_user`"

        ```yaml
        # If empty it will fallback to postgres role default
        # Type: string
        jellystat_role_postgres_user: ""
        ```

    ??? variable string "`jellystat_role_postgres_password`"

        ```yaml
        # If empty it will fallback to postgres role default
        # Type: string
        jellystat_role_postgres_password: ""
        ```

    ??? variable string "`jellystat_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        jellystat_role_postgres_docker_env_db: "jfstat"
        ```

    ??? variable string "`jellystat_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        jellystat_role_postgres_docker_image_tag: "15.2-alpine"
        ```

    ??? variable string "`jellystat_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        jellystat_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable dict "`jellystat_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        jellystat_role_postgres_docker_healthcheck:
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='jellystat') }} -U {{ lookup('role_var', '_postgres_user', role='jellystat') if (lookup('role_var', '_postgres_user', role='jellystat') | length > 0) else lookup('role_var', '_docker_env_user', role='postgres') }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`jellystat_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        jellystat_role_postgres_paths_folder: "{{ jellystat_name }}"
        ```

    ??? variable string "`jellystat_role_postgres_paths_location`"

        ```yaml
        # Type: string
        jellystat_role_postgres_paths_location: "{{ server_appdata_path }}/{{ jellystat_role_postgres_paths_folder }}/postgres"
        ```

    ??? variable string "`jellystat_log_level`"

        ```yaml
        # Type: string
        jellystat_log_level: "INFO"
        ```

    ??? variable bool "`jellystat_emby`"

        ```yaml
        # Type: bool (true/false)
        jellystat_emby: false
        ```

=== "Web"

    ??? variable string "`jellystat_role_web_subdomain`"

        ```yaml
        # Type: string
        jellystat_role_web_subdomain: "{{ jellystat_name }}"
        ```

    ??? variable string "`jellystat_role_web_domain`"

        ```yaml
        # Type: string
        jellystat_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`jellystat_role_web_port`"

        ```yaml
        # Type: string
        jellystat_role_web_port: "3000"
        ```

    ??? variable string "`jellystat_role_web_url`"

        ```yaml
        # Type: string
        jellystat_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='jellystat') + '.' + lookup('role_var', '_web_domain', role='jellystat')
                                 if (lookup('role_var', '_web_subdomain', role='jellystat') | length > 0)
                                 else lookup('role_var', '_web_domain', role='jellystat')) }}"
        ```

=== "DNS"

    ??? variable string "`jellystat_role_dns_record`"

        ```yaml
        # Type: string
        jellystat_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='jellystat') }}"
        ```

    ??? variable string "`jellystat_role_dns_zone`"

        ```yaml
        # Type: string
        jellystat_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='jellystat') }}"
        ```

    ??? variable bool "`jellystat_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`jellystat_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        jellystat_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`jellystat_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        jellystat_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`jellystat_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        jellystat_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`jellystat_role_traefik_certresolver`"

        ```yaml
        # Type: string
        jellystat_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`jellystat_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_traefik_enabled: true
        ```

    ??? variable bool "`jellystat_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_traefik_api_enabled: false
        ```

    ??? variable string "`jellystat_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        jellystat_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`jellystat_role_docker_container`"

        ```yaml
        # Type: string
        jellystat_role_docker_container: "{{ jellystat_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`jellystat_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_docker_image_pull: true
        ```

    ??? variable string "`jellystat_role_docker_image_repo`"

        ```yaml
        # Type: string
        jellystat_role_docker_image_repo: "cyfershepard/jellystat"
        ```

    ??? variable string "`jellystat_role_docker_image_tag`"

        ```yaml
        # Type: string
        jellystat_role_docker_image_tag: "latest"
        ```

    ??? variable string "`jellystat_role_docker_image`"

        ```yaml
        # Type: string
        jellystat_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='jellystat') }}:{{ lookup('role_var', '_docker_image_tag', role='jellystat') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`jellystat_role_docker_envs_default`"

        ```yaml
        # Type: dict
        jellystat_role_docker_envs_default:
          POSTGRES_USER: "{{ lookup('role_var', '_postgres_user', role='jellystat')
                          if (lookup('role_var', '_postgres_user', role='jellystat') | length > 0)
                          else lookup('role_var', '_docker_env_user', role='postgres') }}"
          POSTGRES_PASSWORD: "{{ lookup('role_var', '_postgres_password', role='jellystat')
                              if (lookup('role_var', '_postgres_password', role='jellystat') | length > 0)
                              else lookup('role_var', '_docker_env_password', role='postgres') }}"
          POSTGRES_IP: "{{ lookup('role_var', '_postgres_name', role='jellystat') }}"
          POSTGRES_PORT: "5432"
          JWT_SECRET: "{{ jwt_token.stdout }}"
        ```

    ??? variable dict "`jellystat_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        jellystat_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`jellystat_role_docker_volumes_default`"

        ```yaml
        # Type: list
        jellystat_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='jellystat') }}:/app/backend/backup-data"
        ```

    ??? variable list "`jellystat_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        jellystat_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`jellystat_role_docker_hostname`"

        ```yaml
        # Type: string
        jellystat_role_docker_hostname: "{{ jellystat_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`jellystat_role_docker_networks_alias`"

        ```yaml
        # Type: string
        jellystat_role_docker_networks_alias: "{{ jellystat_name }}"
        ```

    ??? variable list "`jellystat_role_docker_networks_default`"

        ```yaml
        # Type: list
        jellystat_role_docker_networks_default: []
        ```

    ??? variable list "`jellystat_role_docker_networks_custom`"

        ```yaml
        # Type: list
        jellystat_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`jellystat_role_docker_restart_policy`"

        ```yaml
        # Type: string
        jellystat_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`jellystat_role_docker_state`"

        ```yaml
        # Type: string
        jellystat_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`jellystat_role_depends_on`"

        ```yaml
        # Type: string
        jellystat_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='jellystat') }}"
        ```

    ??? variable string "`jellystat_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        jellystat_role_depends_on_delay: "0"
        ```

    ??? variable string "`jellystat_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        jellystat_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`jellystat_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        jellystat_role_docker_blkio_weight:
        ```

    ??? variable int "`jellystat_role_docker_cpu_period`"

        ```yaml
        # Type: int
        jellystat_role_docker_cpu_period:
        ```

    ??? variable int "`jellystat_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        jellystat_role_docker_cpu_quota:
        ```

    ??? variable int "`jellystat_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        jellystat_role_docker_cpu_shares:
        ```

    ??? variable string "`jellystat_role_docker_cpus`"

        ```yaml
        # Type: string
        jellystat_role_docker_cpus:
        ```

    ??? variable string "`jellystat_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        jellystat_role_docker_cpuset_cpus:
        ```

    ??? variable string "`jellystat_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        jellystat_role_docker_cpuset_mems:
        ```

    ??? variable string "`jellystat_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        jellystat_role_docker_kernel_memory:
        ```

    ??? variable string "`jellystat_role_docker_memory`"

        ```yaml
        # Type: string
        jellystat_role_docker_memory:
        ```

    ??? variable string "`jellystat_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        jellystat_role_docker_memory_reservation:
        ```

    ??? variable string "`jellystat_role_docker_memory_swap`"

        ```yaml
        # Type: string
        jellystat_role_docker_memory_swap:
        ```

    ??? variable int "`jellystat_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        jellystat_role_docker_memory_swappiness:
        ```

    ??? variable string "`jellystat_role_docker_shm_size`"

        ```yaml
        # Type: string
        jellystat_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`jellystat_role_docker_cap_drop`"

        ```yaml
        # Type: list
        jellystat_role_docker_cap_drop:
        ```

    ??? variable string "`jellystat_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        jellystat_role_docker_cgroupns_mode:
        ```

    ??? variable list "`jellystat_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        jellystat_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`jellystat_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        jellystat_role_docker_device_read_bps:
        ```

    ??? variable list "`jellystat_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        jellystat_role_docker_device_read_iops:
        ```

    ??? variable list "`jellystat_role_docker_device_requests`"

        ```yaml
        # Type: list
        jellystat_role_docker_device_requests:
        ```

    ??? variable list "`jellystat_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        jellystat_role_docker_device_write_bps:
        ```

    ??? variable list "`jellystat_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        jellystat_role_docker_device_write_iops:
        ```

    ??? variable list "`jellystat_role_docker_devices`"

        ```yaml
        # Type: list
        jellystat_role_docker_devices:
        ```

    ??? variable list "`jellystat_role_docker_groups`"

        ```yaml
        # Type: list
        jellystat_role_docker_groups:
        ```

    ??? variable bool "`jellystat_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_docker_privileged:
        ```

    ??? variable list "`jellystat_role_docker_security_opts`"

        ```yaml
        # Type: list
        jellystat_role_docker_security_opts:
        ```

    ??? variable string "`jellystat_role_docker_user`"

        ```yaml
        # Type: string
        jellystat_role_docker_user:
        ```

    ??? variable string "`jellystat_role_docker_userns_mode`"

        ```yaml
        # Type: string
        jellystat_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`jellystat_role_docker_dns_opts`"

        ```yaml
        # Type: list
        jellystat_role_docker_dns_opts:
        ```

    ??? variable list "`jellystat_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        jellystat_role_docker_dns_search_domains:
        ```

    ??? variable list "`jellystat_role_docker_dns_servers`"

        ```yaml
        # Type: list
        jellystat_role_docker_dns_servers:
        ```

    ??? variable string "`jellystat_role_docker_domainname`"

        ```yaml
        # Type: string
        jellystat_role_docker_domainname:
        ```

    ??? variable list "`jellystat_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        jellystat_role_docker_exposed_ports:
        ```

    ??? variable dict "`jellystat_role_docker_hosts`"

        ```yaml
        # Type: dict
        jellystat_role_docker_hosts:
        ```

    ??? variable bool "`jellystat_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_docker_hosts_use_common:
        ```

    ??? variable string "`jellystat_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        jellystat_role_docker_ipc_mode:
        ```

    ??? variable list "`jellystat_role_docker_links`"

        ```yaml
        # Type: list
        jellystat_role_docker_links:
        ```

    ??? variable string "`jellystat_role_docker_network_mode`"

        ```yaml
        # Type: string
        jellystat_role_docker_network_mode:
        ```

    ??? variable string "`jellystat_role_docker_pid_mode`"

        ```yaml
        # Type: string
        jellystat_role_docker_pid_mode:
        ```

    ??? variable list "`jellystat_role_docker_ports`"

        ```yaml
        # Type: list
        jellystat_role_docker_ports:
        ```

    ??? variable string "`jellystat_role_docker_uts`"

        ```yaml
        # Type: string
        jellystat_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`jellystat_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_docker_keep_volumes:
        ```

    ??? variable list "`jellystat_role_docker_mounts`"

        ```yaml
        # Type: list
        jellystat_role_docker_mounts:
        ```

    ??? variable dict "`jellystat_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        jellystat_role_docker_storage_opts:
        ```

    ??? variable list "`jellystat_role_docker_tmpfs`"

        ```yaml
        # Type: list
        jellystat_role_docker_tmpfs:
        ```

    ??? variable string "`jellystat_role_docker_volume_driver`"

        ```yaml
        # Type: string
        jellystat_role_docker_volume_driver:
        ```

    ??? variable list "`jellystat_role_docker_volumes_from`"

        ```yaml
        # Type: list
        jellystat_role_docker_volumes_from:
        ```

    ??? variable bool "`jellystat_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_docker_volumes_global:
        ```

    ??? variable string "`jellystat_role_docker_working_dir`"

        ```yaml
        # Type: string
        jellystat_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`jellystat_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_docker_auto_remove:
        ```

    ??? variable bool "`jellystat_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_docker_cleanup:
        ```

    ??? variable string "`jellystat_role_docker_force_kill`"

        ```yaml
        # Type: string
        jellystat_role_docker_force_kill:
        ```

    ??? variable dict "`jellystat_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        jellystat_role_docker_healthcheck:
        ```

    ??? variable int "`jellystat_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        jellystat_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`jellystat_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_docker_init:
        ```

    ??? variable string "`jellystat_role_docker_kill_signal`"

        ```yaml
        # Type: string
        jellystat_role_docker_kill_signal:
        ```

    ??? variable string "`jellystat_role_docker_log_driver`"

        ```yaml
        # Type: string
        jellystat_role_docker_log_driver:
        ```

    ??? variable dict "`jellystat_role_docker_log_options`"

        ```yaml
        # Type: dict
        jellystat_role_docker_log_options:
        ```

    ??? variable bool "`jellystat_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_docker_oom_killer:
        ```

    ??? variable int "`jellystat_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        jellystat_role_docker_oom_score_adj:
        ```

    ??? variable bool "`jellystat_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_docker_output_logs:
        ```

    ??? variable bool "`jellystat_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_docker_paused:
        ```

    ??? variable bool "`jellystat_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_docker_recreate:
        ```

    ??? variable int "`jellystat_role_docker_restart_retries`"

        ```yaml
        # Type: int
        jellystat_role_docker_restart_retries:
        ```

    ??? variable string "`jellystat_role_docker_stop_signal`"

        ```yaml
        # Type: string
        jellystat_role_docker_stop_signal:
        ```

    ??? variable int "`jellystat_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        jellystat_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`jellystat_role_docker_capabilities`"

        ```yaml
        # Type: list
        jellystat_role_docker_capabilities:
        ```

    ??? variable string "`jellystat_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        jellystat_role_docker_cgroup_parent:
        ```

    ??? variable list "`jellystat_role_docker_commands`"

        ```yaml
        # Type: list
        jellystat_role_docker_commands:
        ```

    ??? variable int "`jellystat_role_docker_create_timeout`"

        ```yaml
        # Type: int
        jellystat_role_docker_create_timeout:
        ```

    ??? variable string "`jellystat_role_docker_dev_dri`"

        ```yaml
        # Type: string
        jellystat_role_docker_dev_dri:
        ```

    ??? variable string "`jellystat_role_docker_entrypoint`"

        ```yaml
        # Type: string
        jellystat_role_docker_entrypoint:
        ```

    ??? variable string "`jellystat_role_docker_env_file`"

        ```yaml
        # Type: string
        jellystat_role_docker_env_file:
        ```

    ??? variable dict "`jellystat_role_docker_labels`"

        ```yaml
        # Type: dict
        jellystat_role_docker_labels:
        ```

    ??? variable bool "`jellystat_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_docker_labels_use_common:
        ```

    ??? variable bool "`jellystat_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_docker_read_only:
        ```

    ??? variable string "`jellystat_role_docker_runtime`"

        ```yaml
        # Type: string
        jellystat_role_docker_runtime:
        ```

    ??? variable list "`jellystat_role_docker_sysctls`"

        ```yaml
        # Type: list
        jellystat_role_docker_sysctls:
        ```

    ??? variable list "`jellystat_role_docker_ulimits`"

        ```yaml
        # Type: list
        jellystat_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`jellystat_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        jellystat_role_autoheal_enabled: true
        ```

    ??? variable bool "`jellystat_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        jellystat_role_diun_enabled: true
        ```

    ??? variable bool "`jellystat_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        jellystat_role_dns_enabled: true
        ```

    ??? variable bool "`jellystat_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        jellystat_role_docker_controller: true
        ```

    ??? variable list "`jellystat_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        jellystat_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`jellystat_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_docker_volumes_download:
        ```

    ??? variable string "`jellystat_role_themepark_addons`"

        ```yaml
        # Type: string
        jellystat_role_themepark_addons:
        ```

    ??? variable string "`jellystat_role_themepark_app`"

        ```yaml
        # Type: string
        jellystat_role_themepark_app:
        ```

    ??? variable string "`jellystat_role_themepark_theme`"

        ```yaml
        # Type: string
        jellystat_role_themepark_theme:
        ```

    ??? variable string "`jellystat_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        jellystat_role_traefik_api_middleware:
        ```

    ??? variable string "`jellystat_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        jellystat_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`jellystat_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        jellystat_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`jellystat_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        jellystat_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`jellystat_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        jellystat_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`jellystat_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        jellystat_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`jellystat_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        jellystat_role_traefik_middleware_http:
        ```

    ??? variable bool "`jellystat_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`jellystat_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        jellystat_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`jellystat_role_traefik_priority`"

        ```yaml
        # Type: string
        jellystat_role_traefik_priority:
        ```

    ??? variable bool "`jellystat_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        jellystat_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`jellystat_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        jellystat_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`jellystat_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        jellystat_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`jellystat_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        jellystat_role_web_api_http_port:
        ```

    ??? variable string "`jellystat_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        jellystat_role_web_api_http_scheme:
        ```

    ??? variable dict "`jellystat_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        jellystat_role_web_api_http_serverstransport:
        ```

    ??? variable string "`jellystat_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        jellystat_role_web_api_port:
        ```

    ??? variable string "`jellystat_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        jellystat_role_web_api_scheme:
        ```

    ??? variable dict "`jellystat_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        jellystat_role_web_api_serverstransport:
        ```

    ??? variable list "`jellystat_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        jellystat_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            jellystat_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "jellystat2.{{ user.domain }}"
              - "jellystat.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`jellystat_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        jellystat_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            jellystat_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'jellystat2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`jellystat_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        jellystat_role_web_http_port:
        ```

    ??? variable string "`jellystat_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        jellystat_role_web_http_scheme:
        ```

    ??? variable dict "`jellystat_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        jellystat_role_web_http_serverstransport:
        ```

    ??? variable string "`jellystat_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        jellystat_role_web_scheme:
        ```

    ??? variable dict "`jellystat_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        jellystat_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

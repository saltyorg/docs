---
icon: material/docker
title: Tube Archivist
hide:
  - tags
tags:
  - tubearchivist
  - media
  - youtube 
saltbox_automation:
  app_links:
    - name: Manual
      url: https://github.com/tubearchivist/tubearchivist/wiki
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/bbilly1/tubearchivist/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Tube Archivist
    summary: |
      a self-hosted YouTube media server designed to help users download, index, and organize their favorite YouTube content for offline viewing.
    link: https://www.tubearchivist.com/
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Tube Archivist

## Overview

[Tube Archivist](https://www.tubearchivist.com/) is a self-hosted YouTube media server designed to help users download, index, and organize their favorite YouTube content for offline viewing.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/tubearchivist/tubearchivist/wiki){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/bbilly1/tubearchivist/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-tubearchivist
```

## Usage

Visit <https://tubearchivist.iYOUR_DOMAIN_NAMEi>.

## Basics

- Default login:

  ```yaml
  Username: "your user from accounts.yml"
  Password: your_normal_password
  ```

!!!note
   Tubearchivist adds the downloaded media to `/mnt/unionfs/downloads/tubearchivist/YT_CHANNEL_NAME`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        tubearchivist_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `tubearchivist_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `tubearchivist_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`tubearchivist_name`"

        ```yaml
        # Type: string
        tubearchivist_name: tubearchivist
        ```

=== "Settings"

    ??? variable string "`tubearchivist_role_enable_cast`"

        ```yaml
        # Type: string
        tubearchivist_role_enable_cast: "false"
        ```

=== "Web"

    ??? variable string "`tubearchivist_role_web_subdomain`"

        ```yaml
        # Type: string
        tubearchivist_role_web_subdomain: "{{ tubearchivist_name }}"
        ```

    ??? variable string "`tubearchivist_role_web_domain`"

        ```yaml
        # Type: string
        tubearchivist_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`tubearchivist_role_web_port`"

        ```yaml
        # Type: string
        tubearchivist_role_web_port: "8000"
        ```

    ??? variable string "`tubearchivist_role_web_url`"

        ```yaml
        # Type: string
        tubearchivist_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='tubearchivist') + '.' + lookup('role_var', '_web_domain', role='tubearchivist')
                                     if (lookup('role_var', '_web_subdomain', role='tubearchivist') | length > 0)
                                     else lookup('role_var', '_web_domain', role='tubearchivist')) }}"
        ```

=== "DNS"

    ??? variable string "`tubearchivist_role_dns_record`"

        ```yaml
        # Type: string
        tubearchivist_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='tubearchivist') }}"
        ```

    ??? variable string "`tubearchivist_role_dns_zone`"

        ```yaml
        # Type: string
        tubearchivist_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='tubearchivist') }}"
        ```

    ??? variable bool "`tubearchivist_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`tubearchivist_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        tubearchivist_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`tubearchivist_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        tubearchivist_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`tubearchivist_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        tubearchivist_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`tubearchivist_role_traefik_certresolver`"

        ```yaml
        # Type: string
        tubearchivist_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`tubearchivist_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_traefik_enabled: true
        ```

    ??? variable bool "`tubearchivist_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_traefik_api_enabled: true
        ```

    ??? variable string "`tubearchivist_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        tubearchivist_role_traefik_api_endpoint: "PathPrefix(`/api`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`tubearchivist_role_docker_container`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_container: "{{ tubearchivist_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`tubearchivist_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_docker_image_pull: true
        ```

    ??? variable string "`tubearchivist_role_docker_image_tag`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_image_tag: "v0.4.13"
        ```

    ??? variable string "`tubearchivist_role_docker_image_repo`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_image_repo: "bbilly1/tubearchivist"
        ```

    ??? variable string "`tubearchivist_role_docker_image`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='tubearchivist') }}:{{ lookup('role_var', '_docker_image_tag', role='tubearchivist') }}"
        ```

    <h5>Envs</h5>

    ??? variable string "`tubearchivist_role_docker_envs_http_header`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_envs_http_header: "{{ 'HTTP_REMOTE_USER'
                                                     if ('authelia' in lookup('role_var', '_traefik_sso_middleware', role='tubearchivist'))
                                                     else ('HTTP_X_AUTHENTIK_USERNAME'
                                                          if ('authentik' in lookup('role_var', '_traefik_sso_middleware', role='tubearchivist'))
                                                          else '') }}"
        ```

    ??? variable dict "`tubearchivist_role_docker_envs_default`"

        ```yaml
        # Type: dict
        tubearchivist_role_docker_envs_default:
          TZ: "{{ tz }}"
          ES_URL: "http://{{ tubearchivist_name }}-elasticsearch:9200"
          REDIS_HOST: "{{ tubearchivist_name }}-redis"
          HOST_UID: "{{ uid }}"
          HOST_GID: "{{ gid }}"
          TA_HOST: "localhost 127.0.0.1 {{ tubearchivist_name }} {{ lookup('role_var', '_web_subdomain', role='tubearchivist') + '.' + lookup('role_var', '_web_domain', role='tubearchivist') }} {{ lookup('role_var', '_web_url', role='tubearchivist') }}"
          TA_ENABLE_AUTH_PROXY: "{{ 'true' if (lookup('role_var', '_traefik_sso_middleware', role='tubearchivist') | length > 0) else omit }}"
          TA_AUTH_PROXY_USERNAME_HEADER: "{{ lookup('role_var', '_docker_envs_http_header', role='tubearchivist') if (lookup('role_var', '_traefik_sso_middleware', role='tubearchivist') | length > 0) else omit }}"
          TA_USERNAME: "{{ user.name }}"
          TA_PASSWORD: "{{ user.pass }}"
          ELASTIC_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='elasticsearch') }}"
          ENABLE_CAST: "{{ lookup('role_var', '_enable_cast', role='tubearchivist') }}"
        ```

    ??? variable dict "`tubearchivist_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        tubearchivist_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`tubearchivist_role_docker_volumes_default`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_downloads_location', role='tubearchivist') }}/:/youtube"
          - "{{ lookup('role_var', '_paths_location', role='tubearchivist') }}/cache:/cache"
        ```

    ??? variable list "`tubearchivist_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`tubearchivist_role_docker_hostname`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_hostname: "{{ tubearchivist_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`tubearchivist_role_docker_networks_alias`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_networks_alias: "{{ tubearchivist_name }}"
        ```

    ??? variable list "`tubearchivist_role_docker_networks_default`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_networks_default: []
        ```

    ??? variable list "`tubearchivist_role_docker_networks_custom`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`tubearchivist_role_docker_restart_policy`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`tubearchivist_role_docker_state`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`tubearchivist_role_depends_on`"

        ```yaml
        # Type: string
        tubearchivist_role_depends_on: "{{ tubearchivist_name }}-elasticsearch,{{ tubearchivist_name }}-redis"
        ```

    ??? variable string "`tubearchivist_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        tubearchivist_role_depends_on_delay: "0"
        ```

    ??? variable string "`tubearchivist_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        tubearchivist_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`tubearchivist_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        tubearchivist_role_docker_blkio_weight:
        ```

    ??? variable int "`tubearchivist_role_docker_cpu_period`"

        ```yaml
        # Type: int
        tubearchivist_role_docker_cpu_period:
        ```

    ??? variable int "`tubearchivist_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        tubearchivist_role_docker_cpu_quota:
        ```

    ??? variable int "`tubearchivist_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        tubearchivist_role_docker_cpu_shares:
        ```

    ??? variable string "`tubearchivist_role_docker_cpus`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_cpus:
        ```

    ??? variable string "`tubearchivist_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_cpuset_cpus:
        ```

    ??? variable string "`tubearchivist_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_cpuset_mems:
        ```

    ??? variable string "`tubearchivist_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_kernel_memory:
        ```

    ??? variable string "`tubearchivist_role_docker_memory`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_memory:
        ```

    ??? variable string "`tubearchivist_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_memory_reservation:
        ```

    ??? variable string "`tubearchivist_role_docker_memory_swap`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_memory_swap:
        ```

    ??? variable int "`tubearchivist_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        tubearchivist_role_docker_memory_swappiness:
        ```

    ??? variable string "`tubearchivist_role_docker_shm_size`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`tubearchivist_role_docker_cap_drop`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_cap_drop:
        ```

    ??? variable string "`tubearchivist_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_cgroupns_mode:
        ```

    ??? variable list "`tubearchivist_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`tubearchivist_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_device_read_bps:
        ```

    ??? variable list "`tubearchivist_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_device_read_iops:
        ```

    ??? variable list "`tubearchivist_role_docker_device_requests`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_device_requests:
        ```

    ??? variable list "`tubearchivist_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_device_write_bps:
        ```

    ??? variable list "`tubearchivist_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_device_write_iops:
        ```

    ??? variable list "`tubearchivist_role_docker_devices`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_devices:
        ```

    ??? variable string "`tubearchivist_role_docker_devices_default`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_devices_default:
        ```

    ??? variable list "`tubearchivist_role_docker_groups`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_groups:
        ```

    ??? variable bool "`tubearchivist_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_docker_privileged:
        ```

    ??? variable list "`tubearchivist_role_docker_security_opts`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_security_opts:
        ```

    ??? variable string "`tubearchivist_role_docker_user`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_user:
        ```

    ??? variable string "`tubearchivist_role_docker_userns_mode`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`tubearchivist_role_docker_dns_opts`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_dns_opts:
        ```

    ??? variable list "`tubearchivist_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_dns_search_domains:
        ```

    ??? variable list "`tubearchivist_role_docker_dns_servers`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_dns_servers:
        ```

    ??? variable string "`tubearchivist_role_docker_domainname`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_domainname:
        ```

    ??? variable list "`tubearchivist_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_exposed_ports:
        ```

    ??? variable dict "`tubearchivist_role_docker_hosts`"

        ```yaml
        # Type: dict
        tubearchivist_role_docker_hosts:
        ```

    ??? variable bool "`tubearchivist_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_docker_hosts_use_common:
        ```

    ??? variable string "`tubearchivist_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_ipc_mode:
        ```

    ??? variable list "`tubearchivist_role_docker_links`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_links:
        ```

    ??? variable string "`tubearchivist_role_docker_network_mode`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_network_mode:
        ```

    ??? variable string "`tubearchivist_role_docker_pid_mode`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_pid_mode:
        ```

    ??? variable list "`tubearchivist_role_docker_ports`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_ports:
        ```

    ??? variable string "`tubearchivist_role_docker_uts`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`tubearchivist_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_docker_keep_volumes:
        ```

    ??? variable list "`tubearchivist_role_docker_mounts`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_mounts:
        ```

    ??? variable dict "`tubearchivist_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        tubearchivist_role_docker_storage_opts:
        ```

    ??? variable list "`tubearchivist_role_docker_tmpfs`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_tmpfs:
        ```

    ??? variable string "`tubearchivist_role_docker_volume_driver`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_volume_driver:
        ```

    ??? variable list "`tubearchivist_role_docker_volumes_from`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_volumes_from:
        ```

    ??? variable bool "`tubearchivist_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_docker_volumes_global:
        ```

    ??? variable string "`tubearchivist_role_docker_working_dir`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`tubearchivist_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_docker_auto_remove:
        ```

    ??? variable bool "`tubearchivist_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_docker_cleanup:
        ```

    ??? variable string "`tubearchivist_role_docker_force_kill`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_force_kill:
        ```

    ??? variable dict "`tubearchivist_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        tubearchivist_role_docker_healthcheck:
        ```

    ??? variable int "`tubearchivist_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        tubearchivist_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`tubearchivist_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_docker_init:
        ```

    ??? variable string "`tubearchivist_role_docker_kill_signal`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_kill_signal:
        ```

    ??? variable string "`tubearchivist_role_docker_log_driver`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_log_driver:
        ```

    ??? variable dict "`tubearchivist_role_docker_log_options`"

        ```yaml
        # Type: dict
        tubearchivist_role_docker_log_options:
        ```

    ??? variable bool "`tubearchivist_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_docker_oom_killer:
        ```

    ??? variable int "`tubearchivist_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        tubearchivist_role_docker_oom_score_adj:
        ```

    ??? variable bool "`tubearchivist_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_docker_output_logs:
        ```

    ??? variable bool "`tubearchivist_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_docker_paused:
        ```

    ??? variable bool "`tubearchivist_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_docker_recreate:
        ```

    ??? variable int "`tubearchivist_role_docker_restart_retries`"

        ```yaml
        # Type: int
        tubearchivist_role_docker_restart_retries:
        ```

    ??? variable int "`tubearchivist_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        tubearchivist_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`tubearchivist_role_docker_capabilities`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_capabilities:
        ```

    ??? variable string "`tubearchivist_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_cgroup_parent:
        ```

    ??? variable list "`tubearchivist_role_docker_commands`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_commands:
        ```

    ??? variable int "`tubearchivist_role_docker_create_timeout`"

        ```yaml
        # Type: int
        tubearchivist_role_docker_create_timeout:
        ```

    ??? variable string "`tubearchivist_role_docker_entrypoint`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_entrypoint:
        ```

    ??? variable string "`tubearchivist_role_docker_env_file`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_env_file:
        ```

    ??? variable dict "`tubearchivist_role_docker_labels`"

        ```yaml
        # Type: dict
        tubearchivist_role_docker_labels:
        ```

    ??? variable bool "`tubearchivist_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_docker_labels_use_common:
        ```

    ??? variable bool "`tubearchivist_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_docker_read_only:
        ```

    ??? variable string "`tubearchivist_role_docker_runtime`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_runtime:
        ```

    ??? variable list "`tubearchivist_role_docker_sysctls`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_sysctls:
        ```

    ??? variable list "`tubearchivist_role_docker_ulimits`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`tubearchivist_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        tubearchivist_role_autoheal_enabled: true
        ```

    ??? variable string "`tubearchivist_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        tubearchivist_role_depends_on: ""
        ```

    ??? variable string "`tubearchivist_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        tubearchivist_role_depends_on_delay: "0"
        ```

    ??? variable string "`tubearchivist_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        tubearchivist_role_depends_on_healthchecks:
        ```

    ??? variable bool "`tubearchivist_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        tubearchivist_role_diun_enabled: true
        ```

    ??? variable bool "`tubearchivist_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        tubearchivist_role_dns_enabled: true
        ```

    ??? variable bool "`tubearchivist_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        tubearchivist_role_docker_controller: true
        ```

    ??? variable string "`tubearchivist_role_docker_env_password`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_env_password:
        ```

    ??? variable string "`tubearchivist_role_docker_envs_http_header`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_envs_http_header:
        ```

    ??? variable string "`tubearchivist_role_docker_image_repo`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_image_repo:
        ```

    ??? variable string "`tubearchivist_role_docker_image_tag`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_image_tag:
        ```

    ??? variable bool "`tubearchivist_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_docker_volumes_download:
        ```

    ??? variable string "`tubearchivist_role_enable_cast`"

        ```yaml
        # Type: string
        tubearchivist_role_enable_cast:
        ```

    ??? variable string "`tubearchivist_role_paths_downloads_location`"

        ```yaml
        # Type: string
        tubearchivist_role_paths_downloads_location:
        ```

    ??? variable string "`tubearchivist_role_paths_location`"

        ```yaml
        # Type: string
        tubearchivist_role_paths_location:
        ```

    ??? variable string "`tubearchivist_role_themepark_addons`"

        ```yaml
        # Type: string
        tubearchivist_role_themepark_addons:
        ```

    ??? variable string "`tubearchivist_role_themepark_app`"

        ```yaml
        # Type: string
        tubearchivist_role_themepark_app:
        ```

    ??? variable string "`tubearchivist_role_themepark_theme`"

        ```yaml
        # Type: string
        tubearchivist_role_themepark_theme:
        ```

    ??? variable dict "`tubearchivist_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        tubearchivist_role_traefik_api_endpoint:
        ```

    ??? variable string "`tubearchivist_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        tubearchivist_role_traefik_api_middleware:
        ```

    ??? variable string "`tubearchivist_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        tubearchivist_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`tubearchivist_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        tubearchivist_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`tubearchivist_role_traefik_certresolver`"

        ```yaml
        # Type: string
        tubearchivist_role_traefik_certresolver:
        ```

    ??? variable bool "`tubearchivist_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        tubearchivist_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`tubearchivist_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        tubearchivist_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`tubearchivist_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        tubearchivist_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`tubearchivist_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        tubearchivist_role_traefik_middleware_http:
        ```

    ??? variable bool "`tubearchivist_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`tubearchivist_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`tubearchivist_role_traefik_priority`"

        ```yaml
        # Type: string
        tubearchivist_role_traefik_priority:
        ```

    ??? variable bool "`tubearchivist_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        tubearchivist_role_traefik_robot_enabled: true
        ```

    ??? variable string "`tubearchivist_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        tubearchivist_role_traefik_sso_middleware:
        ```

    ??? variable bool "`tubearchivist_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        tubearchivist_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`tubearchivist_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        tubearchivist_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`tubearchivist_role_web_domain`"

        ```yaml
        # Type: string
        tubearchivist_role_web_domain:
        ```

    ??? variable list "`tubearchivist_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        tubearchivist_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            tubearchivist_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "tubearchivist2.{{ user.domain }}"
              - "tubearchivist.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`tubearchivist_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        tubearchivist_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            tubearchivist_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'tubearchivist2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`tubearchivist_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        tubearchivist_role_web_http_port:
        ```

    ??? variable string "`tubearchivist_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        tubearchivist_role_web_http_scheme:
        ```

    ??? variable dict "`tubearchivist_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        tubearchivist_role_web_http_serverstransport:
        ```

    ??? variable string "`tubearchivist_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        tubearchivist_role_web_scheme:
        ```

    ??? variable dict "`tubearchivist_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        tubearchivist_role_web_serverstransport:
        ```

    ??? variable string "`tubearchivist_role_web_subdomain`"

        ```yaml
        # Type: string
        tubearchivist_role_web_subdomain:
        ```

    ??? variable string "`tubearchivist_role_web_url`"

        ```yaml
        # Type: string
        tubearchivist_role_web_url:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
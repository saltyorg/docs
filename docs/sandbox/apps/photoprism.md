---
icon: material/docker
title: Photoprism®
hide:
  - tags
tags:
  - photoprism
  - photos
  - ai
saltbox_automation:
  app_links:
    - name: Manual
      url: https://docs.photoprism.app
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/photoprism/photoprism/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Photoprism®
    summary: |
      an AI-Powered Photos App for the Decentralized Web. It makes use of the latest technologies to tag and find pictures automatically without getting in your way. You can run it at home, on a private server, or in the cloud.
    link: https://photoprism.app/
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Photoprism®

## Overview

[Photoprism®](https://photoprism.app/) is an AI-Powered Photos App for the Decentralized Web. It makes use of the latest technologies to tag and find pictures automatically without getting in your way. You can run it at home, on a private server, or in the cloud.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://docs.photoprism.app){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/photoprism/photoprism/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-photoprism
```

## Usage

Visit <https://photoprism.iYOUR_DOMAIN_NAMEi>.

## Basics

- Default login:

  ```yaml
  Username: admin
  Password: your_normal_password
  ```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        photoprism_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `photoprism_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `photoprism_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`photoprism_name`"

        ```yaml
        # Type: string
        photoprism_name: photoprism
        ```

=== "Web"

    ??? variable string "`photoprism_role_web_subdomain`"

        ```yaml
        # Type: string
        photoprism_role_web_subdomain: "{{ photoprism_name }}"
        ```

    ??? variable string "`photoprism_role_web_domain`"

        ```yaml
        # Type: string
        photoprism_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`photoprism_role_web_port`"

        ```yaml
        # Type: string
        photoprism_role_web_port: "2342"
        ```

    ??? variable string "`photoprism_role_web_url`"

        ```yaml
        # Type: string
        photoprism_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='photoprism') + '.' + lookup('role_var', '_web_domain', role='photoprism')
                                  if (lookup('role_var', '_web_subdomain', role='photoprism') | length > 0)
                                  else lookup('role_var', '_web_domain', role='photoprism')) }}"
        ```

=== "DNS"

    ??? variable string "`photoprism_role_dns_record`"

        ```yaml
        # Type: string
        photoprism_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='photoprism') }}"
        ```

    ??? variable string "`photoprism_role_dns_zone`"

        ```yaml
        # Type: string
        photoprism_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='photoprism') }}"
        ```

    ??? variable bool "`photoprism_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`photoprism_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        photoprism_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`photoprism_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        photoprism_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`photoprism_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        photoprism_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`photoprism_role_traefik_certresolver`"

        ```yaml
        # Type: string
        photoprism_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`photoprism_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_traefik_enabled: true
        ```

    ??? variable bool "`photoprism_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_traefik_api_enabled: false
        ```

    ??? variable string "`photoprism_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        photoprism_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`photoprism_role_docker_container`"

        ```yaml
        # Type: string
        photoprism_role_docker_container: "{{ photoprism_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`photoprism_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_docker_image_pull: true
        ```

    ??? variable string "`photoprism_role_docker_image_tag`"

        ```yaml
        # Type: string
        photoprism_role_docker_image_tag: "latest"
        ```

    ??? variable string "`photoprism_role_docker_image_repo`"

        ```yaml
        # Type: string
        photoprism_role_docker_image_repo: "photoprism/photoprism"
        ```

    ??? variable string "`photoprism_role_docker_image`"

        ```yaml
        # Type: string
        photoprism_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='photoprism') }}:{{ lookup('role_var', '_docker_image_tag', role='photoprism') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`photoprism_role_docker_envs_default`"

        ```yaml
        # Type: dict
        photoprism_role_docker_envs_default:
          PHOTOPRISM_ADMIN_PASSWORD: "{{ user.pass }}"
          PHOTOPRISM_AUTH_MODE: "password"
          PHOTOPRISM_SITE_URL: "{{ lookup('role_var', '_web_url', role='photoprism') }}"
          PHOTOPRISM_ORIGINALS_LIMIT: "5000"
          PHOTOPRISM_HTTP_COMPRESSION: "gzip"
          PHOTOPRISM_LOG_LEVEL: "info"
          PHOTOPRISM_READONLY: "false"
          PHOTOPRISM_EXPERIMENTAL: "false"
          PHOTOPRISM_DISABLE_CHOWN: "false"
          PHOTOPRISM_DISABLE_WEBDAV: "false"
          PHOTOPRISM_DISABLE_SETTINGS: "false"
          PHOTOPRISM_DISABLE_TENSORFLOW: "false"
          PHOTOPRISM_DISABLE_FACES: "false"
          PHOTOPRISM_DISABLE_CLASSIFICATION: "false"
          PHOTOPRISM_DISABLE_RAW: "false"
          PHOTOPRISM_RAW_PRESETS: "false"
          PHOTOPRISM_JPEG_QUALITY: "85"
          PHOTOPRISM_DETECT_NSFW: "false"
          PHOTOPRISM_UPLOAD_NSFW: "false"
          PHOTOPRISM_DATABASE_DRIVER: "mysql"
          PHOTOPRISM_DATABASE_SERVER: "mariadb:3306"
          PHOTOPRISM_DATABASE_NAME: "photoprisms"
          PHOTOPRISM_DATABASE_USER: "root"
          PHOTOPRISM_DATABASE_PASSWORD: "password321"
          PHOTOPRISM_SITE_CAPTION: "AI-Powered Photos App"
          PHOTOPRISM_SITE_DESCRIPTION: "Trying out PhotoPrism!"
          PHOTOPRISM_SITE_AUTHOR: "{{ user.name }}"
          PHOTOPRISM_INIT: "gpu tensorflow"
        ```

    ??? variable dict "`photoprism_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        photoprism_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`photoprism_role_docker_volumes_default`"

        ```yaml
        # Type: list
        photoprism_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='photoprism') }}/originals:/photoprism/originals"
          - "{{ lookup('role_var', '_paths_location', role='photoprism') }}/import:/photoprism/import"
          - "{{ lookup('role_var', '_paths_location', role='photoprism') }}/storage:/photoprism/storage"
        ```

    ??? variable list "`photoprism_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        photoprism_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`photoprism_role_docker_hostname`"

        ```yaml
        # Type: string
        photoprism_role_docker_hostname: "{{ photoprism_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`photoprism_role_docker_networks_alias`"

        ```yaml
        # Type: string
        photoprism_role_docker_networks_alias: "{{ photoprism_name }}"
        ```

    ??? variable list "`photoprism_role_docker_networks_default`"

        ```yaml
        # Type: list
        photoprism_role_docker_networks_default: []
        ```

    ??? variable list "`photoprism_role_docker_networks_custom`"

        ```yaml
        # Type: list
        photoprism_role_docker_networks_custom: []
        ```

    <h5>Security Opts</h5>

    ??? variable list "`photoprism_role_docker_security_opts_default`"

        ```yaml
        # Type: list
        photoprism_role_docker_security_opts_default:
          - "seccomp=unconfined"
          - "apparmor=unconfined"
        ```

    ??? variable list "`photoprism_role_docker_security_opts_custom`"

        ```yaml
        # Type: list
        photoprism_role_docker_security_opts_custom: []
        ```

    <h5>Working Directory</h5>

    ??? variable string "`photoprism_role_docker_working_dir`"

        ```yaml
        # Type: string
        photoprism_role_docker_working_dir: "/photoprism"
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`photoprism_role_docker_restart_policy`"

        ```yaml
        # Type: string
        photoprism_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`photoprism_role_docker_state`"

        ```yaml
        # Type: string
        photoprism_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`photoprism_role_docker_user`"

        ```yaml
        # Type: string
        photoprism_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

    <h5>Dependencies</h5>

    ??? variable string "`photoprism_role_depends_on`"

        ```yaml
        # Type: string
        photoprism_role_depends_on: "mariadb"
        ```

    ??? variable string "`photoprism_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        photoprism_role_depends_on_delay: "0"
        ```

    ??? variable string "`photoprism_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        photoprism_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`photoprism_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        photoprism_role_docker_blkio_weight:
        ```

    ??? variable int "`photoprism_role_docker_cpu_period`"

        ```yaml
        # Type: int
        photoprism_role_docker_cpu_period:
        ```

    ??? variable int "`photoprism_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        photoprism_role_docker_cpu_quota:
        ```

    ??? variable int "`photoprism_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        photoprism_role_docker_cpu_shares:
        ```

    ??? variable string "`photoprism_role_docker_cpus`"

        ```yaml
        # Type: string
        photoprism_role_docker_cpus:
        ```

    ??? variable string "`photoprism_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        photoprism_role_docker_cpuset_cpus:
        ```

    ??? variable string "`photoprism_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        photoprism_role_docker_cpuset_mems:
        ```

    ??? variable string "`photoprism_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        photoprism_role_docker_kernel_memory:
        ```

    ??? variable string "`photoprism_role_docker_memory`"

        ```yaml
        # Type: string
        photoprism_role_docker_memory:
        ```

    ??? variable string "`photoprism_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        photoprism_role_docker_memory_reservation:
        ```

    ??? variable string "`photoprism_role_docker_memory_swap`"

        ```yaml
        # Type: string
        photoprism_role_docker_memory_swap:
        ```

    ??? variable int "`photoprism_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        photoprism_role_docker_memory_swappiness:
        ```

    ??? variable string "`photoprism_role_docker_shm_size`"

        ```yaml
        # Type: string
        photoprism_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`photoprism_role_docker_cap_drop`"

        ```yaml
        # Type: list
        photoprism_role_docker_cap_drop:
        ```

    ??? variable string "`photoprism_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        photoprism_role_docker_cgroupns_mode:
        ```

    ??? variable list "`photoprism_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        photoprism_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`photoprism_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        photoprism_role_docker_device_read_bps:
        ```

    ??? variable list "`photoprism_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        photoprism_role_docker_device_read_iops:
        ```

    ??? variable list "`photoprism_role_docker_device_requests`"

        ```yaml
        # Type: list
        photoprism_role_docker_device_requests:
        ```

    ??? variable list "`photoprism_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        photoprism_role_docker_device_write_bps:
        ```

    ??? variable list "`photoprism_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        photoprism_role_docker_device_write_iops:
        ```

    ??? variable list "`photoprism_role_docker_devices`"

        ```yaml
        # Type: list
        photoprism_role_docker_devices:
        ```

    ??? variable string "`photoprism_role_docker_devices_default`"

        ```yaml
        # Type: string
        photoprism_role_docker_devices_default:
        ```

    ??? variable list "`photoprism_role_docker_groups`"

        ```yaml
        # Type: list
        photoprism_role_docker_groups:
        ```

    ??? variable bool "`photoprism_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_docker_privileged:
        ```

    ??? variable string "`photoprism_role_docker_userns_mode`"

        ```yaml
        # Type: string
        photoprism_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`photoprism_role_docker_dns_opts`"

        ```yaml
        # Type: list
        photoprism_role_docker_dns_opts:
        ```

    ??? variable list "`photoprism_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        photoprism_role_docker_dns_search_domains:
        ```

    ??? variable list "`photoprism_role_docker_dns_servers`"

        ```yaml
        # Type: list
        photoprism_role_docker_dns_servers:
        ```

    ??? variable string "`photoprism_role_docker_domainname`"

        ```yaml
        # Type: string
        photoprism_role_docker_domainname:
        ```

    ??? variable list "`photoprism_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        photoprism_role_docker_exposed_ports:
        ```

    ??? variable dict "`photoprism_role_docker_hosts`"

        ```yaml
        # Type: dict
        photoprism_role_docker_hosts:
        ```

    ??? variable bool "`photoprism_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_docker_hosts_use_common:
        ```

    ??? variable string "`photoprism_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        photoprism_role_docker_ipc_mode:
        ```

    ??? variable list "`photoprism_role_docker_links`"

        ```yaml
        # Type: list
        photoprism_role_docker_links:
        ```

    ??? variable string "`photoprism_role_docker_network_mode`"

        ```yaml
        # Type: string
        photoprism_role_docker_network_mode:
        ```

    ??? variable string "`photoprism_role_docker_pid_mode`"

        ```yaml
        # Type: string
        photoprism_role_docker_pid_mode:
        ```

    ??? variable list "`photoprism_role_docker_ports`"

        ```yaml
        # Type: list
        photoprism_role_docker_ports:
        ```

    ??? variable string "`photoprism_role_docker_uts`"

        ```yaml
        # Type: string
        photoprism_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`photoprism_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_docker_keep_volumes:
        ```

    ??? variable list "`photoprism_role_docker_mounts`"

        ```yaml
        # Type: list
        photoprism_role_docker_mounts:
        ```

    ??? variable dict "`photoprism_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        photoprism_role_docker_storage_opts:
        ```

    ??? variable list "`photoprism_role_docker_tmpfs`"

        ```yaml
        # Type: list
        photoprism_role_docker_tmpfs:
        ```

    ??? variable string "`photoprism_role_docker_volume_driver`"

        ```yaml
        # Type: string
        photoprism_role_docker_volume_driver:
        ```

    ??? variable list "`photoprism_role_docker_volumes_from`"

        ```yaml
        # Type: list
        photoprism_role_docker_volumes_from:
        ```

    ??? variable bool "`photoprism_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_docker_volumes_global:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`photoprism_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_docker_auto_remove:
        ```

    ??? variable bool "`photoprism_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_docker_cleanup:
        ```

    ??? variable string "`photoprism_role_docker_force_kill`"

        ```yaml
        # Type: string
        photoprism_role_docker_force_kill:
        ```

    ??? variable dict "`photoprism_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        photoprism_role_docker_healthcheck:
        ```

    ??? variable int "`photoprism_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        photoprism_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`photoprism_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_docker_init:
        ```

    ??? variable string "`photoprism_role_docker_kill_signal`"

        ```yaml
        # Type: string
        photoprism_role_docker_kill_signal:
        ```

    ??? variable string "`photoprism_role_docker_log_driver`"

        ```yaml
        # Type: string
        photoprism_role_docker_log_driver:
        ```

    ??? variable dict "`photoprism_role_docker_log_options`"

        ```yaml
        # Type: dict
        photoprism_role_docker_log_options:
        ```

    ??? variable bool "`photoprism_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_docker_oom_killer:
        ```

    ??? variable int "`photoprism_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        photoprism_role_docker_oom_score_adj:
        ```

    ??? variable bool "`photoprism_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_docker_output_logs:
        ```

    ??? variable bool "`photoprism_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_docker_paused:
        ```

    ??? variable bool "`photoprism_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_docker_recreate:
        ```

    ??? variable int "`photoprism_role_docker_restart_retries`"

        ```yaml
        # Type: int
        photoprism_role_docker_restart_retries:
        ```

    ??? variable int "`photoprism_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        photoprism_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`photoprism_role_docker_capabilities`"

        ```yaml
        # Type: list
        photoprism_role_docker_capabilities:
        ```

    ??? variable string "`photoprism_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        photoprism_role_docker_cgroup_parent:
        ```

    ??? variable list "`photoprism_role_docker_commands`"

        ```yaml
        # Type: list
        photoprism_role_docker_commands:
        ```

    ??? variable int "`photoprism_role_docker_create_timeout`"

        ```yaml
        # Type: int
        photoprism_role_docker_create_timeout:
        ```

    ??? variable string "`photoprism_role_docker_entrypoint`"

        ```yaml
        # Type: string
        photoprism_role_docker_entrypoint:
        ```

    ??? variable string "`photoprism_role_docker_env_file`"

        ```yaml
        # Type: string
        photoprism_role_docker_env_file:
        ```

    ??? variable dict "`photoprism_role_docker_labels`"

        ```yaml
        # Type: dict
        photoprism_role_docker_labels:
        ```

    ??? variable bool "`photoprism_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_docker_labels_use_common:
        ```

    ??? variable bool "`photoprism_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_docker_read_only:
        ```

    ??? variable string "`photoprism_role_docker_runtime`"

        ```yaml
        # Type: string
        photoprism_role_docker_runtime:
        ```

    ??? variable list "`photoprism_role_docker_sysctls`"

        ```yaml
        # Type: list
        photoprism_role_docker_sysctls:
        ```

    ??? variable list "`photoprism_role_docker_ulimits`"

        ```yaml
        # Type: list
        photoprism_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`photoprism_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        photoprism_role_autoheal_enabled: true
        ```

    ??? variable string "`photoprism_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        photoprism_role_depends_on: ""
        ```

    ??? variable string "`photoprism_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        photoprism_role_depends_on_delay: "0"
        ```

    ??? variable string "`photoprism_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        photoprism_role_depends_on_healthchecks:
        ```

    ??? variable bool "`photoprism_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        photoprism_role_diun_enabled: true
        ```

    ??? variable bool "`photoprism_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        photoprism_role_dns_enabled: true
        ```

    ??? variable bool "`photoprism_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        photoprism_role_docker_controller: true
        ```

    ??? variable string "`photoprism_role_docker_image_repo`"

        ```yaml
        # Type: string
        photoprism_role_docker_image_repo:
        ```

    ??? variable string "`photoprism_role_docker_image_tag`"

        ```yaml
        # Type: string
        photoprism_role_docker_image_tag:
        ```

    ??? variable bool "`photoprism_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_docker_volumes_download:
        ```

    ??? variable string "`photoprism_role_paths_location`"

        ```yaml
        # Type: string
        photoprism_role_paths_location:
        ```

    ??? variable string "`photoprism_role_themepark_addons`"

        ```yaml
        # Type: string
        photoprism_role_themepark_addons:
        ```

    ??? variable string "`photoprism_role_themepark_app`"

        ```yaml
        # Type: string
        photoprism_role_themepark_app:
        ```

    ??? variable string "`photoprism_role_themepark_theme`"

        ```yaml
        # Type: string
        photoprism_role_themepark_theme:
        ```

    ??? variable dict "`photoprism_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        photoprism_role_traefik_api_endpoint:
        ```

    ??? variable string "`photoprism_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        photoprism_role_traefik_api_middleware:
        ```

    ??? variable string "`photoprism_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        photoprism_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`photoprism_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        photoprism_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`photoprism_role_traefik_certresolver`"

        ```yaml
        # Type: string
        photoprism_role_traefik_certresolver:
        ```

    ??? variable bool "`photoprism_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        photoprism_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`photoprism_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        photoprism_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`photoprism_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        photoprism_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`photoprism_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        photoprism_role_traefik_middleware_http:
        ```

    ??? variable bool "`photoprism_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`photoprism_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`photoprism_role_traefik_priority`"

        ```yaml
        # Type: string
        photoprism_role_traefik_priority:
        ```

    ??? variable bool "`photoprism_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        photoprism_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`photoprism_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        photoprism_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`photoprism_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        photoprism_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`photoprism_role_web_domain`"

        ```yaml
        # Type: string
        photoprism_role_web_domain:
        ```

    ??? variable list "`photoprism_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        photoprism_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            photoprism_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "photoprism2.{{ user.domain }}"
              - "photoprism.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`photoprism_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        photoprism_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            photoprism_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'photoprism2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`photoprism_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        photoprism_role_web_http_port:
        ```

    ??? variable string "`photoprism_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        photoprism_role_web_http_scheme:
        ```

    ??? variable dict "`photoprism_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        photoprism_role_web_http_serverstransport:
        ```

    ??? variable string "`photoprism_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        photoprism_role_web_scheme:
        ```

    ??? variable dict "`photoprism_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        photoprism_role_web_serverstransport:
        ```

    ??? variable string "`photoprism_role_web_subdomain`"

        ```yaml
        # Type: string
        photoprism_role_web_subdomain:
        ```

    ??? variable string "`photoprism_role_web_url`"

        ```yaml
        # Type: string
        photoprism_role_web_url:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
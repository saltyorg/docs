---
icon: material/docker
title: BookStack
hide:
  - tags
tags:
  - bookstack
  - wiki
  - documentation
saltbox_automation:
  app_links:
    - name: Manual
      url: https://www.bookstackapp.com/docs
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/linuxserver/bookstack/tags
      type: docker
    - name: Community
      url: https://linuxserver.io/discord
      type: discord
  project_description:
    name: BookStack
    summary: |
      a simple, self-hosted, easy-to-use platform for organising and storing information.
    link: https://www.bookstackapp.com
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# BookStack

## Overview

[BookStack](https://www.bookstackapp.com) is a simple, self-hosted, easy-to-use platform for organising and storing information.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://www.bookstackapp.com/docs){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/linuxserver/bookstack/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://linuxserver.io/discord){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-bookstack
```

## Usage

Visit <https://bookstack.iYOUR_DOMAIN_NAMEi>.

## Basics

- Log in using the default admin details `admin@admin.com` with a password of `password`. You should change these details **immediately** after logging in for the first time.

- Optional configuration such as SMTP can be done by editing the `.env` file located at:

```
/opt/bookstack/www/.env
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        bookstack_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `bookstack_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `bookstack_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`bookstack_name`"

        ```yaml
        # Type: string
        bookstack_name: bookstack
        ```

=== "Web"

    ??? variable string "`bookstack_role_web_subdomain`"

        ```yaml
        # Type: string
        bookstack_role_web_subdomain: "{{ bookstack_name }}"
        ```

    ??? variable string "`bookstack_role_web_domain`"

        ```yaml
        # Type: string
        bookstack_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`bookstack_role_web_port`"

        ```yaml
        # Type: string
        bookstack_role_web_port: "80"
        ```

    ??? variable string "`bookstack_role_web_url`"

        ```yaml
        # Type: string
        bookstack_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='bookstack') + '.' + lookup('role_var', '_web_domain', role='bookstack')
                                 if (lookup('role_var', '_web_subdomain', role='bookstack') | length > 0)
                                 else lookup('role_var', '_web_domain', role='bookstack')) }}"
        ```

=== "DNS"

    ??? variable string "`bookstack_role_dns_record`"

        ```yaml
        # Type: string
        bookstack_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='bookstack') }}"
        ```

    ??? variable string "`bookstack_role_dns_zone`"

        ```yaml
        # Type: string
        bookstack_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='bookstack') }}"
        ```

    ??? variable bool "`bookstack_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`bookstack_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        bookstack_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`bookstack_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        bookstack_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`bookstack_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        bookstack_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`bookstack_role_traefik_certresolver`"

        ```yaml
        # Type: string
        bookstack_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`bookstack_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_traefik_enabled: true
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`bookstack_role_docker_container`"

        ```yaml
        # Type: string
        bookstack_role_docker_container: "{{ bookstack_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`bookstack_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_docker_image_pull: true
        ```

    ??? variable string "`bookstack_role_docker_image_repo`"

        ```yaml
        # Type: string
        bookstack_role_docker_image_repo: "lscr.io/linuxserver/bookstack"
        ```

    ??? variable string "`bookstack_role_docker_image_tag`"

        ```yaml
        # Type: string
        bookstack_role_docker_image_tag: "latest"
        ```

    ??? variable string "`bookstack_role_docker_image`"

        ```yaml
        # Type: string
        bookstack_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='bookstack') }}:{{ lookup('role_var', '_docker_image_tag', role='bookstack') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`bookstack_role_docker_envs_default`"

        ```yaml
        # Type: dict
        bookstack_role_docker_envs_default:
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          APP_KEY: "{{ bookstack_saltbox_facts.facts.app_key }}"
          APP_URL: "{{ lookup('role_var', '_web_url', role='bookstack') }}"
          DB_HOST: "mariadb"
          DB_PORT: "3306"
          DB_USERNAME: "root"
          DB_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='mariadb') }}"
          DB_DATABASE: bookstackapp
        ```

    ??? variable dict "`bookstack_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        bookstack_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`bookstack_role_docker_volumes_default`"

        ```yaml
        # Type: list
        bookstack_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='bookstack') }}:/config"
        ```

    ??? variable list "`bookstack_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        bookstack_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`bookstack_role_docker_hostname`"

        ```yaml
        # Type: string
        bookstack_role_docker_hostname: "{{ bookstack_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`bookstack_role_docker_networks_alias`"

        ```yaml
        # Type: string
        bookstack_role_docker_networks_alias: "{{ bookstack_name }}"
        ```

    ??? variable list "`bookstack_role_docker_networks_default`"

        ```yaml
        # Type: list
        bookstack_role_docker_networks_default: []
        ```

    ??? variable list "`bookstack_role_docker_networks_custom`"

        ```yaml
        # Type: list
        bookstack_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`bookstack_role_docker_restart_policy`"

        ```yaml
        # Type: string
        bookstack_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`bookstack_role_docker_state`"

        ```yaml
        # Type: string
        bookstack_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`bookstack_role_depends_on`"

        ```yaml
        # Type: string
        bookstack_role_depends_on: "mariadb"
        ```

    ??? variable string "`bookstack_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        bookstack_role_depends_on_delay: "0"
        ```

    ??? variable string "`bookstack_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        bookstack_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`bookstack_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        bookstack_role_docker_blkio_weight:
        ```

    ??? variable int "`bookstack_role_docker_cpu_period`"

        ```yaml
        # Type: int
        bookstack_role_docker_cpu_period:
        ```

    ??? variable int "`bookstack_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        bookstack_role_docker_cpu_quota:
        ```

    ??? variable int "`bookstack_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        bookstack_role_docker_cpu_shares:
        ```

    ??? variable string "`bookstack_role_docker_cpus`"

        ```yaml
        # Type: string
        bookstack_role_docker_cpus:
        ```

    ??? variable string "`bookstack_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        bookstack_role_docker_cpuset_cpus:
        ```

    ??? variable string "`bookstack_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        bookstack_role_docker_cpuset_mems:
        ```

    ??? variable string "`bookstack_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        bookstack_role_docker_kernel_memory:
        ```

    ??? variable string "`bookstack_role_docker_memory`"

        ```yaml
        # Type: string
        bookstack_role_docker_memory:
        ```

    ??? variable string "`bookstack_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        bookstack_role_docker_memory_reservation:
        ```

    ??? variable string "`bookstack_role_docker_memory_swap`"

        ```yaml
        # Type: string
        bookstack_role_docker_memory_swap:
        ```

    ??? variable int "`bookstack_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        bookstack_role_docker_memory_swappiness:
        ```

    ??? variable string "`bookstack_role_docker_shm_size`"

        ```yaml
        # Type: string
        bookstack_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`bookstack_role_docker_cap_drop`"

        ```yaml
        # Type: list
        bookstack_role_docker_cap_drop:
        ```

    ??? variable string "`bookstack_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        bookstack_role_docker_cgroupns_mode:
        ```

    ??? variable list "`bookstack_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        bookstack_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`bookstack_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        bookstack_role_docker_device_read_bps:
        ```

    ??? variable list "`bookstack_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        bookstack_role_docker_device_read_iops:
        ```

    ??? variable list "`bookstack_role_docker_device_requests`"

        ```yaml
        # Type: list
        bookstack_role_docker_device_requests:
        ```

    ??? variable list "`bookstack_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        bookstack_role_docker_device_write_bps:
        ```

    ??? variable list "`bookstack_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        bookstack_role_docker_device_write_iops:
        ```

    ??? variable list "`bookstack_role_docker_devices`"

        ```yaml
        # Type: list
        bookstack_role_docker_devices:
        ```

    ??? variable string "`bookstack_role_docker_devices_default`"

        ```yaml
        # Type: string
        bookstack_role_docker_devices_default:
        ```

    ??? variable list "`bookstack_role_docker_groups`"

        ```yaml
        # Type: list
        bookstack_role_docker_groups:
        ```

    ??? variable bool "`bookstack_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_docker_privileged:
        ```

    ??? variable list "`bookstack_role_docker_security_opts`"

        ```yaml
        # Type: list
        bookstack_role_docker_security_opts:
        ```

    ??? variable string "`bookstack_role_docker_user`"

        ```yaml
        # Type: string
        bookstack_role_docker_user:
        ```

    ??? variable string "`bookstack_role_docker_userns_mode`"

        ```yaml
        # Type: string
        bookstack_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`bookstack_role_docker_dns_opts`"

        ```yaml
        # Type: list
        bookstack_role_docker_dns_opts:
        ```

    ??? variable list "`bookstack_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        bookstack_role_docker_dns_search_domains:
        ```

    ??? variable list "`bookstack_role_docker_dns_servers`"

        ```yaml
        # Type: list
        bookstack_role_docker_dns_servers:
        ```

    ??? variable string "`bookstack_role_docker_domainname`"

        ```yaml
        # Type: string
        bookstack_role_docker_domainname:
        ```

    ??? variable list "`bookstack_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        bookstack_role_docker_exposed_ports:
        ```

    ??? variable dict "`bookstack_role_docker_hosts`"

        ```yaml
        # Type: dict
        bookstack_role_docker_hosts:
        ```

    ??? variable bool "`bookstack_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_docker_hosts_use_common:
        ```

    ??? variable string "`bookstack_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        bookstack_role_docker_ipc_mode:
        ```

    ??? variable list "`bookstack_role_docker_links`"

        ```yaml
        # Type: list
        bookstack_role_docker_links:
        ```

    ??? variable string "`bookstack_role_docker_network_mode`"

        ```yaml
        # Type: string
        bookstack_role_docker_network_mode:
        ```

    ??? variable string "`bookstack_role_docker_pid_mode`"

        ```yaml
        # Type: string
        bookstack_role_docker_pid_mode:
        ```

    ??? variable list "`bookstack_role_docker_ports`"

        ```yaml
        # Type: list
        bookstack_role_docker_ports:
        ```

    ??? variable string "`bookstack_role_docker_uts`"

        ```yaml
        # Type: string
        bookstack_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`bookstack_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_docker_keep_volumes:
        ```

    ??? variable list "`bookstack_role_docker_mounts`"

        ```yaml
        # Type: list
        bookstack_role_docker_mounts:
        ```

    ??? variable dict "`bookstack_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        bookstack_role_docker_storage_opts:
        ```

    ??? variable list "`bookstack_role_docker_tmpfs`"

        ```yaml
        # Type: list
        bookstack_role_docker_tmpfs:
        ```

    ??? variable string "`bookstack_role_docker_volume_driver`"

        ```yaml
        # Type: string
        bookstack_role_docker_volume_driver:
        ```

    ??? variable list "`bookstack_role_docker_volumes_from`"

        ```yaml
        # Type: list
        bookstack_role_docker_volumes_from:
        ```

    ??? variable bool "`bookstack_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_docker_volumes_global:
        ```

    ??? variable string "`bookstack_role_docker_working_dir`"

        ```yaml
        # Type: string
        bookstack_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`bookstack_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_docker_auto_remove:
        ```

    ??? variable bool "`bookstack_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_docker_cleanup:
        ```

    ??? variable string "`bookstack_role_docker_force_kill`"

        ```yaml
        # Type: string
        bookstack_role_docker_force_kill:
        ```

    ??? variable dict "`bookstack_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        bookstack_role_docker_healthcheck:
        ```

    ??? variable int "`bookstack_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        bookstack_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`bookstack_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_docker_init:
        ```

    ??? variable string "`bookstack_role_docker_kill_signal`"

        ```yaml
        # Type: string
        bookstack_role_docker_kill_signal:
        ```

    ??? variable string "`bookstack_role_docker_log_driver`"

        ```yaml
        # Type: string
        bookstack_role_docker_log_driver:
        ```

    ??? variable dict "`bookstack_role_docker_log_options`"

        ```yaml
        # Type: dict
        bookstack_role_docker_log_options:
        ```

    ??? variable bool "`bookstack_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_docker_oom_killer:
        ```

    ??? variable int "`bookstack_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        bookstack_role_docker_oom_score_adj:
        ```

    ??? variable bool "`bookstack_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_docker_output_logs:
        ```

    ??? variable bool "`bookstack_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_docker_paused:
        ```

    ??? variable bool "`bookstack_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_docker_recreate:
        ```

    ??? variable int "`bookstack_role_docker_restart_retries`"

        ```yaml
        # Type: int
        bookstack_role_docker_restart_retries:
        ```

    ??? variable int "`bookstack_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        bookstack_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`bookstack_role_docker_capabilities`"

        ```yaml
        # Type: list
        bookstack_role_docker_capabilities:
        ```

    ??? variable string "`bookstack_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        bookstack_role_docker_cgroup_parent:
        ```

    ??? variable list "`bookstack_role_docker_commands`"

        ```yaml
        # Type: list
        bookstack_role_docker_commands:
        ```

    ??? variable int "`bookstack_role_docker_create_timeout`"

        ```yaml
        # Type: int
        bookstack_role_docker_create_timeout:
        ```

    ??? variable string "`bookstack_role_docker_entrypoint`"

        ```yaml
        # Type: string
        bookstack_role_docker_entrypoint:
        ```

    ??? variable string "`bookstack_role_docker_env_file`"

        ```yaml
        # Type: string
        bookstack_role_docker_env_file:
        ```

    ??? variable dict "`bookstack_role_docker_labels`"

        ```yaml
        # Type: dict
        bookstack_role_docker_labels:
        ```

    ??? variable bool "`bookstack_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_docker_labels_use_common:
        ```

    ??? variable bool "`bookstack_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_docker_read_only:
        ```

    ??? variable string "`bookstack_role_docker_runtime`"

        ```yaml
        # Type: string
        bookstack_role_docker_runtime:
        ```

    ??? variable list "`bookstack_role_docker_sysctls`"

        ```yaml
        # Type: list
        bookstack_role_docker_sysctls:
        ```

    ??? variable list "`bookstack_role_docker_ulimits`"

        ```yaml
        # Type: list
        bookstack_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`bookstack_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        bookstack_role_autoheal_enabled: true
        ```

    ??? variable string "`bookstack_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        bookstack_role_depends_on: ""
        ```

    ??? variable string "`bookstack_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        bookstack_role_depends_on_delay: "0"
        ```

    ??? variable string "`bookstack_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        bookstack_role_depends_on_healthchecks:
        ```

    ??? variable bool "`bookstack_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        bookstack_role_diun_enabled: true
        ```

    ??? variable bool "`bookstack_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        bookstack_role_dns_enabled: true
        ```

    ??? variable bool "`bookstack_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        bookstack_role_docker_controller: true
        ```

    ??? variable string "`bookstack_role_docker_env_password`"

        ```yaml
        # Type: string
        bookstack_role_docker_env_password:
        ```

    ??? variable string "`bookstack_role_docker_image_repo`"

        ```yaml
        # Type: string
        bookstack_role_docker_image_repo:
        ```

    ??? variable string "`bookstack_role_docker_image_tag`"

        ```yaml
        # Type: string
        bookstack_role_docker_image_tag:
        ```

    ??? variable bool "`bookstack_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_docker_volumes_download:
        ```

    ??? variable string "`bookstack_role_paths_location`"

        ```yaml
        # Type: string
        bookstack_role_paths_location:
        ```

    ??? variable string "`bookstack_role_themepark_addons`"

        ```yaml
        # Type: string
        bookstack_role_themepark_addons:
        ```

    ??? variable string "`bookstack_role_themepark_app`"

        ```yaml
        # Type: string
        bookstack_role_themepark_app:
        ```

    ??? variable string "`bookstack_role_themepark_theme`"

        ```yaml
        # Type: string
        bookstack_role_themepark_theme:
        ```

    ??? variable dict "`bookstack_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        bookstack_role_traefik_api_endpoint:
        ```

    ??? variable string "`bookstack_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        bookstack_role_traefik_api_middleware:
        ```

    ??? variable string "`bookstack_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        bookstack_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`bookstack_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        bookstack_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`bookstack_role_traefik_certresolver`"

        ```yaml
        # Type: string
        bookstack_role_traefik_certresolver:
        ```

    ??? variable bool "`bookstack_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        bookstack_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`bookstack_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        bookstack_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`bookstack_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        bookstack_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`bookstack_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        bookstack_role_traefik_middleware_http:
        ```

    ??? variable bool "`bookstack_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`bookstack_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`bookstack_role_traefik_priority`"

        ```yaml
        # Type: string
        bookstack_role_traefik_priority:
        ```

    ??? variable bool "`bookstack_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        bookstack_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`bookstack_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        bookstack_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`bookstack_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        bookstack_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`bookstack_role_web_domain`"

        ```yaml
        # Type: string
        bookstack_role_web_domain:
        ```

    ??? variable list "`bookstack_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        bookstack_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            bookstack_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "bookstack2.{{ user.domain }}"
              - "bookstack.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`bookstack_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        bookstack_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            bookstack_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'bookstack2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`bookstack_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        bookstack_role_web_http_port:
        ```

    ??? variable string "`bookstack_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        bookstack_role_web_http_scheme:
        ```

    ??? variable dict "`bookstack_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        bookstack_role_web_http_serverstransport:
        ```

    ??? variable string "`bookstack_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        bookstack_role_web_scheme:
        ```

    ??? variable dict "`bookstack_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        bookstack_role_web_serverstransport:
        ```

    ??? variable string "`bookstack_role_web_subdomain`"

        ```yaml
        # Type: string
        bookstack_role_web_subdomain:
        ```

    ??? variable string "`bookstack_role_web_url`"

        ```yaml
        # Type: string
        bookstack_role_web_url:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
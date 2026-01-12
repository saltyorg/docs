---
icon: material/docker
title: PlexShare
hide:
  - tags
tags:
  - plexshare
  - plex
  - sharing
saltbox_automation:
  app_links:
    - name: Manual
      url:
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/chewbaka/plexshare/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: PlexShare
    summary: |
      a standalone web application that provides management of local users and multiple Plex servers with their libraries. It allows users to access libraries from all registered servers through a single interface without requiring plex.tv registration.
    link: https://chewbaka69.github.io/PlexShare/
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# PlexShare

## Overview

[PlexShare](https://chewbaka69.github.io/PlexShare/) is a standalone web application that provides management of local users and multiple Plex servers with their libraries. It allows users to access libraries from all registered servers through a single interface without requiring plex.tv registration.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/chewbaka/plexshare/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-plexshare
```

## Usage

Visit <https://plexshare.iYOUR_DOMAIN_NAMEi>.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        plexshare_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `plexshare_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `plexshare_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`plexshare_name`"

        ```yaml
        # Type: string
        plexshare_name: plexshare
        ```

=== "Web"

    ??? variable string "`plexshare_role_web_subdomain`"

        ```yaml
        # Type: string
        plexshare_role_web_subdomain: "{{ plexshare_name }}"
        ```

    ??? variable string "`plexshare_role_web_domain`"

        ```yaml
        # Type: string
        plexshare_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`plexshare_role_web_port`"

        ```yaml
        # Type: string
        plexshare_role_web_port: "80"
        ```

    ??? variable string "`plexshare_role_web_url`"

        ```yaml
        # Type: string
        plexshare_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='plexshare') + '.' + lookup('role_var', '_web_domain', role='plexshare')
                                 if (lookup('role_var', '_web_subdomain', role='plexshare') | length > 0)
                                 else lookup('role_var', '_web_domain', role='plexshare')) }}"
        ```

=== "DNS"

    ??? variable string "`plexshare_role_dns_record`"

        ```yaml
        # Type: string
        plexshare_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='plexshare') }}"
        ```

    ??? variable string "`plexshare_role_dns_zone`"

        ```yaml
        # Type: string
        plexshare_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='plexshare') }}"
        ```

    ??? variable bool "`plexshare_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`plexshare_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        plexshare_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`plexshare_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        plexshare_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`plexshare_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        plexshare_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`plexshare_role_traefik_certresolver`"

        ```yaml
        # Type: string
        plexshare_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`plexshare_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_traefik_enabled: true
        ```

    ??? variable bool "`plexshare_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_traefik_api_enabled: false
        ```

    ??? variable string "`plexshare_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        plexshare_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`plexshare_role_docker_container`"

        ```yaml
        # Type: string
        plexshare_role_docker_container: "{{ plexshare_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`plexshare_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_docker_image_pull: true
        ```

    ??? variable string "`plexshare_role_docker_image_tag`"

        ```yaml
        # Type: string
        plexshare_role_docker_image_tag: "latest"
        ```

    ??? variable string "`plexshare_role_docker_image_repo`"

        ```yaml
        # Type: string
        plexshare_role_docker_image_repo: "chewbaka/plexshare"
        ```

    ??? variable string "`plexshare_role_docker_image`"

        ```yaml
        # Type: string
        plexshare_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='plexshare') }}:{{ lookup('role_var', '_docker_image_tag', role='plexshare') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`plexshare_role_docker_envs_default`"

        ```yaml
        # Type: dict
        plexshare_role_docker_envs_default:
          TZ: "{{ tz }}"
          WEB_DOCUMENT_ROOT: "/app/public"
          WEB_DOCUMENT_INDEX: "index.php"
          LOG_STDOUT: "./var/log/plexshare.stdout.log"
          LOG_STDERR: "./var/log/plexshare.stderr.log"
          PHP_POST_MAX_SIZE: "20M"
          PHP_MEMORY_LIMIT: "521M"
          PHP_MAX_EXECUTION_TIME: "300"
          PHP_DATE_TIMEZONE: "{{ tz }}"
          COMPOSER_VERSION: "1"
          BASE_URL: "{{ lookup('role_var', '_web_url', role='plexshare') }}/"
        ```

    ??? variable dict "`plexshare_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        plexshare_role_docker_envs_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`plexshare_role_docker_hostname`"

        ```yaml
        # Type: string
        plexshare_role_docker_hostname: "{{ plexshare_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`plexshare_role_docker_networks_alias`"

        ```yaml
        # Type: string
        plexshare_role_docker_networks_alias: "{{ plexshare_name }}"
        ```

    ??? variable list "`plexshare_role_docker_networks_default`"

        ```yaml
        # Type: list
        plexshare_role_docker_networks_default: []
        ```

    ??? variable list "`plexshare_role_docker_networks_custom`"

        ```yaml
        # Type: list
        plexshare_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`plexshare_role_docker_restart_policy`"

        ```yaml
        # Type: string
        plexshare_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`plexshare_role_docker_state`"

        ```yaml
        # Type: string
        plexshare_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`plexshare_role_depends_on`"

        ```yaml
        # Type: string
        plexshare_role_depends_on: "{{ plexshare_name }}-mariadb"
        ```

    ??? variable string "`plexshare_role_depends_on_delay`"

        ```yaml
        # Type: string (quoted number)
        plexshare_role_depends_on_delay: "0"
        ```

    ??? variable string "`plexshare_role_depends_on_healthchecks`"

        ```yaml
        # Type: string ("true"/"false")
        plexshare_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`plexshare_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        plexshare_role_docker_blkio_weight:
        ```

    ??? variable int "`plexshare_role_docker_cpu_period`"

        ```yaml
        # Type: int
        plexshare_role_docker_cpu_period:
        ```

    ??? variable int "`plexshare_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        plexshare_role_docker_cpu_quota:
        ```

    ??? variable int "`plexshare_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        plexshare_role_docker_cpu_shares:
        ```

    ??? variable string "`plexshare_role_docker_cpus`"

        ```yaml
        # Type: string
        plexshare_role_docker_cpus:
        ```

    ??? variable string "`plexshare_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        plexshare_role_docker_cpuset_cpus:
        ```

    ??? variable string "`plexshare_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        plexshare_role_docker_cpuset_mems:
        ```

    ??? variable string "`plexshare_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        plexshare_role_docker_kernel_memory:
        ```

    ??? variable string "`plexshare_role_docker_memory`"

        ```yaml
        # Type: string
        plexshare_role_docker_memory:
        ```

    ??? variable string "`plexshare_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        plexshare_role_docker_memory_reservation:
        ```

    ??? variable string "`plexshare_role_docker_memory_swap`"

        ```yaml
        # Type: string
        plexshare_role_docker_memory_swap:
        ```

    ??? variable int "`plexshare_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        plexshare_role_docker_memory_swappiness:
        ```

    ??? variable string "`plexshare_role_docker_shm_size`"

        ```yaml
        # Type: string
        plexshare_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`plexshare_role_docker_cap_drop`"

        ```yaml
        # Type: list
        plexshare_role_docker_cap_drop:
        ```

    ??? variable string "`plexshare_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        plexshare_role_docker_cgroupns_mode:
        ```

    ??? variable list "`plexshare_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        plexshare_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`plexshare_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        plexshare_role_docker_device_read_bps:
        ```

    ??? variable list "`plexshare_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        plexshare_role_docker_device_read_iops:
        ```

    ??? variable list "`plexshare_role_docker_device_requests`"

        ```yaml
        # Type: list
        plexshare_role_docker_device_requests:
        ```

    ??? variable list "`plexshare_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        plexshare_role_docker_device_write_bps:
        ```

    ??? variable list "`plexshare_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        plexshare_role_docker_device_write_iops:
        ```

    ??? variable list "`plexshare_role_docker_devices`"

        ```yaml
        # Type: list
        plexshare_role_docker_devices:
        ```

    ??? variable string "`plexshare_role_docker_devices_default`"

        ```yaml
        # Type: string
        plexshare_role_docker_devices_default:
        ```

    ??? variable list "`plexshare_role_docker_groups`"

        ```yaml
        # Type: list
        plexshare_role_docker_groups:
        ```

    ??? variable bool "`plexshare_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_docker_privileged:
        ```

    ??? variable list "`plexshare_role_docker_security_opts`"

        ```yaml
        # Type: list
        plexshare_role_docker_security_opts:
        ```

    ??? variable string "`plexshare_role_docker_user`"

        ```yaml
        # Type: string
        plexshare_role_docker_user:
        ```

    ??? variable string "`plexshare_role_docker_userns_mode`"

        ```yaml
        # Type: string
        plexshare_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`plexshare_role_docker_dns_opts`"

        ```yaml
        # Type: list
        plexshare_role_docker_dns_opts:
        ```

    ??? variable list "`plexshare_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        plexshare_role_docker_dns_search_domains:
        ```

    ??? variable list "`plexshare_role_docker_dns_servers`"

        ```yaml
        # Type: list
        plexshare_role_docker_dns_servers:
        ```

    ??? variable string "`plexshare_role_docker_domainname`"

        ```yaml
        # Type: string
        plexshare_role_docker_domainname:
        ```

    ??? variable list "`plexshare_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        plexshare_role_docker_exposed_ports:
        ```

    ??? variable dict "`plexshare_role_docker_hosts`"

        ```yaml
        # Type: dict
        plexshare_role_docker_hosts:
        ```

    ??? variable bool "`plexshare_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_docker_hosts_use_common:
        ```

    ??? variable string "`plexshare_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        plexshare_role_docker_ipc_mode:
        ```

    ??? variable list "`plexshare_role_docker_links`"

        ```yaml
        # Type: list
        plexshare_role_docker_links:
        ```

    ??? variable string "`plexshare_role_docker_network_mode`"

        ```yaml
        # Type: string
        plexshare_role_docker_network_mode:
        ```

    ??? variable string "`plexshare_role_docker_pid_mode`"

        ```yaml
        # Type: string
        plexshare_role_docker_pid_mode:
        ```

    ??? variable list "`plexshare_role_docker_ports`"

        ```yaml
        # Type: list
        plexshare_role_docker_ports:
        ```

    ??? variable string "`plexshare_role_docker_uts`"

        ```yaml
        # Type: string
        plexshare_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`plexshare_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_docker_keep_volumes:
        ```

    ??? variable list "`plexshare_role_docker_mounts`"

        ```yaml
        # Type: list
        plexshare_role_docker_mounts:
        ```

    ??? variable dict "`plexshare_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        plexshare_role_docker_storage_opts:
        ```

    ??? variable list "`plexshare_role_docker_tmpfs`"

        ```yaml
        # Type: list
        plexshare_role_docker_tmpfs:
        ```

    ??? variable string "`plexshare_role_docker_volume_driver`"

        ```yaml
        # Type: string
        plexshare_role_docker_volume_driver:
        ```

    ??? variable list "`plexshare_role_docker_volumes`"

        ```yaml
        # Type: list
        plexshare_role_docker_volumes:
        ```

    ??? variable list "`plexshare_role_docker_volumes_from`"

        ```yaml
        # Type: list
        plexshare_role_docker_volumes_from:
        ```

    ??? variable bool "`plexshare_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_docker_volumes_global:
        ```

    ??? variable string "`plexshare_role_docker_working_dir`"

        ```yaml
        # Type: string
        plexshare_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`plexshare_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_docker_auto_remove:
        ```

    ??? variable bool "`plexshare_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_docker_cleanup:
        ```

    ??? variable string "`plexshare_role_docker_force_kill`"

        ```yaml
        # Type: string
        plexshare_role_docker_force_kill:
        ```

    ??? variable dict "`plexshare_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        plexshare_role_docker_healthcheck:
        ```

    ??? variable int "`plexshare_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        plexshare_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`plexshare_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_docker_init:
        ```

    ??? variable string "`plexshare_role_docker_kill_signal`"

        ```yaml
        # Type: string
        plexshare_role_docker_kill_signal:
        ```

    ??? variable string "`plexshare_role_docker_log_driver`"

        ```yaml
        # Type: string
        plexshare_role_docker_log_driver:
        ```

    ??? variable dict "`plexshare_role_docker_log_options`"

        ```yaml
        # Type: dict
        plexshare_role_docker_log_options:
        ```

    ??? variable bool "`plexshare_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_docker_oom_killer:
        ```

    ??? variable int "`plexshare_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        plexshare_role_docker_oom_score_adj:
        ```

    ??? variable bool "`plexshare_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_docker_output_logs:
        ```

    ??? variable bool "`plexshare_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_docker_paused:
        ```

    ??? variable bool "`plexshare_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_docker_recreate:
        ```

    ??? variable int "`plexshare_role_docker_restart_retries`"

        ```yaml
        # Type: int
        plexshare_role_docker_restart_retries:
        ```

    ??? variable int "`plexshare_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        plexshare_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`plexshare_role_docker_capabilities`"

        ```yaml
        # Type: list
        plexshare_role_docker_capabilities:
        ```

    ??? variable string "`plexshare_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        plexshare_role_docker_cgroup_parent:
        ```

    ??? variable list "`plexshare_role_docker_commands`"

        ```yaml
        # Type: list
        plexshare_role_docker_commands:
        ```

    ??? variable int "`plexshare_role_docker_create_timeout`"

        ```yaml
        # Type: int
        plexshare_role_docker_create_timeout:
        ```

    ??? variable string "`plexshare_role_docker_entrypoint`"

        ```yaml
        # Type: string
        plexshare_role_docker_entrypoint:
        ```

    ??? variable string "`plexshare_role_docker_env_file`"

        ```yaml
        # Type: string
        plexshare_role_docker_env_file:
        ```

    ??? variable dict "`plexshare_role_docker_labels`"

        ```yaml
        # Type: dict
        plexshare_role_docker_labels:
        ```

    ??? variable bool "`plexshare_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_docker_labels_use_common:
        ```

    ??? variable bool "`plexshare_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_docker_read_only:
        ```

    ??? variable string "`plexshare_role_docker_runtime`"

        ```yaml
        # Type: string
        plexshare_role_docker_runtime:
        ```

    ??? variable list "`plexshare_role_docker_sysctls`"

        ```yaml
        # Type: list
        plexshare_role_docker_sysctls:
        ```

    ??? variable list "`plexshare_role_docker_ulimits`"

        ```yaml
        # Type: list
        plexshare_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`plexshare_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        plexshare_role_autoheal_enabled: true
        ```

    ??? variable string "`plexshare_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        plexshare_role_depends_on: ""
        ```

    ??? variable string "`plexshare_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        plexshare_role_depends_on_delay: "0"
        ```

    ??? variable string "`plexshare_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        plexshare_role_depends_on_healthchecks:
        ```

    ??? variable bool "`plexshare_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        plexshare_role_diun_enabled: true
        ```

    ??? variable bool "`plexshare_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        plexshare_role_dns_enabled: true
        ```

    ??? variable bool "`plexshare_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        plexshare_role_docker_controller: true
        ```

    ??? variable string "`plexshare_role_docker_image_repo`"

        ```yaml
        # Type: string
        plexshare_role_docker_image_repo:
        ```

    ??? variable string "`plexshare_role_docker_image_tag`"

        ```yaml
        # Type: string
        plexshare_role_docker_image_tag:
        ```

    ??? variable bool "`plexshare_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_docker_volumes_download:
        ```

    ??? variable string "`plexshare_role_themepark_addons`"

        ```yaml
        # Type: string
        plexshare_role_themepark_addons:
        ```

    ??? variable string "`plexshare_role_themepark_app`"

        ```yaml
        # Type: string
        plexshare_role_themepark_app:
        ```

    ??? variable string "`plexshare_role_themepark_theme`"

        ```yaml
        # Type: string
        plexshare_role_themepark_theme:
        ```

    ??? variable dict "`plexshare_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        plexshare_role_traefik_api_endpoint:
        ```

    ??? variable string "`plexshare_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        plexshare_role_traefik_api_middleware:
        ```

    ??? variable string "`plexshare_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        plexshare_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`plexshare_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        plexshare_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`plexshare_role_traefik_certresolver`"

        ```yaml
        # Type: string
        plexshare_role_traefik_certresolver:
        ```

    ??? variable bool "`plexshare_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        plexshare_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`plexshare_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        plexshare_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`plexshare_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        plexshare_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`plexshare_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        plexshare_role_traefik_middleware_http:
        ```

    ??? variable bool "`plexshare_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`plexshare_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`plexshare_role_traefik_priority`"

        ```yaml
        # Type: string
        plexshare_role_traefik_priority:
        ```

    ??? variable bool "`plexshare_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        plexshare_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`plexshare_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        plexshare_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`plexshare_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        plexshare_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`plexshare_role_web_domain`"

        ```yaml
        # Type: string
        plexshare_role_web_domain:
        ```

    ??? variable list "`plexshare_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        plexshare_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            plexshare_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "plexshare2.{{ user.domain }}"
              - "plexshare.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`plexshare_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        plexshare_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            plexshare_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'plexshare2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`plexshare_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        plexshare_role_web_http_port:
        ```

    ??? variable string "`plexshare_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        plexshare_role_web_http_scheme:
        ```

    ??? variable dict "`plexshare_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        plexshare_role_web_http_serverstransport:
        ```

    ??? variable string "`plexshare_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        plexshare_role_web_scheme:
        ```

    ??? variable dict "`plexshare_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        plexshare_role_web_serverstransport:
        ```

    ??? variable string "`plexshare_role_web_subdomain`"

        ```yaml
        # Type: string
        plexshare_role_web_subdomain:
        ```

    ??? variable string "`plexshare_role_web_url`"

        ```yaml
        # Type: string
        plexshare_role_web_url:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
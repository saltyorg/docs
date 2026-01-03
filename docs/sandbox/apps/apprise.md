---
icon: material/docker
hide:
  - tags
tags:
  - apprise
  - notifications
  - alerts
---

# Apprise API

## Overview

[linuxserver/apprise-api](https://docs.linuxserver.io/images/docker-apprise-api) is a Docker container image for Apprise.

> [Apprise API](https://github.com/caronc/apprise-api) is an open-source, lightweight REST framework that provides a unified interface to send notifications to over 100 services—such as email, SMS, Slack, Telegram, and Discord—via a single API. [:material-bookshelf:](https://apprise.apps.merit.edu/)

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://docs.linuxserver.io/general/container-customization){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/linuxserver/apprise-api/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://linuxserver.io/discord){ .md-button .md-button--stretch }

</div>

---

!!! note
    Saltbox has a built-in Apprise client that can be used to send notifications. This container is not only used to provide a web UI for configuring and managing notifications, but it also exposes an API. This API allows for programmatic interaction, enabling other applications or scripts to send notifications through the Apprise service. For more information, see the [Apprise Client Docs](https://github.com/caronc/apprise/wiki).

## Deployment

```shell
sb install sandbox-apprise
```

## Usage

Visit <https://apprise.iYOUR_DOMAIN_NAMEi>.

## Basics

The instance runs on the Docker network accessible to other saltbox network containers at `http://apprise:8000`

The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#__tabbed_2_1) file located in `/srv/git/saltbox/accounts.yml`

A typical apprise URL would look like this:

<https://apprise.iYOUR_DOMAIN_NAMEi/notify?service=discord&title=Hello&body=World>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables.<span title="View override details for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        apprise_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `apprise_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `apprise_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`apprise_name`"

        ```yaml
        # Type: string
        apprise_name: apprise
        ```

=== "Web"

    ??? variable string "`apprise_role_web_subdomain`"

        ```yaml
        # Type: string
        apprise_role_web_subdomain: "{{ apprise_name }}"
        ```

    ??? variable string "`apprise_role_web_domain`"

        ```yaml
        # Type: string
        apprise_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`apprise_role_web_port`"

        ```yaml
        # Type: string
        apprise_role_web_port: "8000"
        ```

    ??? variable string "`apprise_role_web_url`"

        ```yaml
        # Type: string
        apprise_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='apprise') + '.' + lookup('role_var', '_web_domain', role='apprise')
                               if (lookup('role_var', '_web_subdomain', role='apprise') | length > 0)
                               else lookup('role_var', '_web_domain', role='apprise')) }}"
        ```

=== "DNS"

    ??? variable string "`apprise_role_dns_record`"

        ```yaml
        # Type: string
        apprise_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='apprise') }}"
        ```

    ??? variable string "`apprise_role_dns_zone`"

        ```yaml
        # Type: string
        apprise_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='apprise') }}"
        ```

    ??? variable bool "`apprise_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`apprise_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        apprise_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`apprise_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        apprise_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`apprise_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        apprise_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`apprise_role_traefik_certresolver`"

        ```yaml
        # Type: string
        apprise_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`apprise_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_traefik_enabled: true
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`apprise_role_docker_container`"

        ```yaml
        # Type: string
        apprise_role_docker_container: "{{ apprise_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`apprise_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_docker_image_pull: true
        ```

    ??? variable string "`apprise_role_docker_image_repo`"

        ```yaml
        # Type: string
        apprise_role_docker_image_repo: "lscr.io/linuxserver/apprise-api"
        ```

    ??? variable string "`apprise_role_docker_image_tag`"

        ```yaml
        # Type: string
        apprise_role_docker_image_tag: "latest"
        ```

    ??? variable string "`apprise_role_docker_image`"

        ```yaml
        # Type: string
        apprise_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='apprise') }}:{{ lookup('role_var', '_docker_image_tag', role='apprise') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`apprise_role_docker_envs_default`"

        ```yaml
        # Type: dict
        apprise_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`apprise_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        apprise_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`apprise_role_docker_volumes_default`"

        ```yaml
        # Type: list
        apprise_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='apprise') }}:/config"
        ```

    ??? variable list "`apprise_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        apprise_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`apprise_role_docker_hostname`"

        ```yaml
        # Type: string
        apprise_role_docker_hostname: "{{ apprise_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`apprise_role_docker_networks_alias`"

        ```yaml
        # Type: string
        apprise_role_docker_networks_alias: "{{ apprise_name }}"
        ```

    ??? variable list "`apprise_role_docker_networks_default`"

        ```yaml
        # Type: list
        apprise_role_docker_networks_default: []
        ```

    ??? variable list "`apprise_role_docker_networks_custom`"

        ```yaml
        # Type: list
        apprise_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`apprise_role_docker_restart_policy`"

        ```yaml
        # Type: string
        apprise_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`apprise_role_docker_state`"

        ```yaml
        # Type: string
        apprise_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`apprise_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        apprise_role_docker_blkio_weight:
        ```

    ??? variable int "`apprise_role_docker_cpu_period`"

        ```yaml
        # Type: int
        apprise_role_docker_cpu_period:
        ```

    ??? variable int "`apprise_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        apprise_role_docker_cpu_quota:
        ```

    ??? variable int "`apprise_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        apprise_role_docker_cpu_shares:
        ```

    ??? variable string "`apprise_role_docker_cpus`"

        ```yaml
        # Type: string
        apprise_role_docker_cpus:
        ```

    ??? variable string "`apprise_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        apprise_role_docker_cpuset_cpus:
        ```

    ??? variable string "`apprise_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        apprise_role_docker_cpuset_mems:
        ```

    ??? variable string "`apprise_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        apprise_role_docker_kernel_memory:
        ```

    ??? variable string "`apprise_role_docker_memory`"

        ```yaml
        # Type: string
        apprise_role_docker_memory:
        ```

    ??? variable string "`apprise_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        apprise_role_docker_memory_reservation:
        ```

    ??? variable string "`apprise_role_docker_memory_swap`"

        ```yaml
        # Type: string
        apprise_role_docker_memory_swap:
        ```

    ??? variable int "`apprise_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        apprise_role_docker_memory_swappiness:
        ```

    ??? variable string "`apprise_role_docker_shm_size`"

        ```yaml
        # Type: string
        apprise_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`apprise_role_docker_cap_drop`"

        ```yaml
        # Type: list
        apprise_role_docker_cap_drop:
        ```

    ??? variable string "`apprise_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        apprise_role_docker_cgroupns_mode:
        ```

    ??? variable list "`apprise_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        apprise_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`apprise_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        apprise_role_docker_device_read_bps:
        ```

    ??? variable list "`apprise_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        apprise_role_docker_device_read_iops:
        ```

    ??? variable list "`apprise_role_docker_device_requests`"

        ```yaml
        # Type: list
        apprise_role_docker_device_requests:
        ```

    ??? variable list "`apprise_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        apprise_role_docker_device_write_bps:
        ```

    ??? variable list "`apprise_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        apprise_role_docker_device_write_iops:
        ```

    ??? variable list "`apprise_role_docker_devices`"

        ```yaml
        # Type: list
        apprise_role_docker_devices:
        ```

    ??? variable string "`apprise_role_docker_devices_default`"

        ```yaml
        # Type: string
        apprise_role_docker_devices_default:
        ```

    ??? variable list "`apprise_role_docker_groups`"

        ```yaml
        # Type: list
        apprise_role_docker_groups:
        ```

    ??? variable bool "`apprise_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_docker_privileged:
        ```

    ??? variable list "`apprise_role_docker_security_opts`"

        ```yaml
        # Type: list
        apprise_role_docker_security_opts:
        ```

    ??? variable string "`apprise_role_docker_user`"

        ```yaml
        # Type: string
        apprise_role_docker_user:
        ```

    ??? variable string "`apprise_role_docker_userns_mode`"

        ```yaml
        # Type: string
        apprise_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`apprise_role_docker_dns_opts`"

        ```yaml
        # Type: list
        apprise_role_docker_dns_opts:
        ```

    ??? variable list "`apprise_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        apprise_role_docker_dns_search_domains:
        ```

    ??? variable list "`apprise_role_docker_dns_servers`"

        ```yaml
        # Type: list
        apprise_role_docker_dns_servers:
        ```

    ??? variable string "`apprise_role_docker_domainname`"

        ```yaml
        # Type: string
        apprise_role_docker_domainname:
        ```

    ??? variable list "`apprise_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        apprise_role_docker_exposed_ports:
        ```

    ??? variable dict "`apprise_role_docker_hosts`"

        ```yaml
        # Type: dict
        apprise_role_docker_hosts:
        ```

    ??? variable bool "`apprise_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_docker_hosts_use_common:
        ```

    ??? variable string "`apprise_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        apprise_role_docker_ipc_mode:
        ```

    ??? variable list "`apprise_role_docker_links`"

        ```yaml
        # Type: list
        apprise_role_docker_links:
        ```

    ??? variable string "`apprise_role_docker_network_mode`"

        ```yaml
        # Type: string
        apprise_role_docker_network_mode:
        ```

    ??? variable string "`apprise_role_docker_pid_mode`"

        ```yaml
        # Type: string
        apprise_role_docker_pid_mode:
        ```

    ??? variable list "`apprise_role_docker_ports`"

        ```yaml
        # Type: list
        apprise_role_docker_ports:
        ```

    ??? variable string "`apprise_role_docker_uts`"

        ```yaml
        # Type: string
        apprise_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`apprise_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_docker_keep_volumes:
        ```

    ??? variable list "`apprise_role_docker_mounts`"

        ```yaml
        # Type: list
        apprise_role_docker_mounts:
        ```

    ??? variable dict "`apprise_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        apprise_role_docker_storage_opts:
        ```

    ??? variable list "`apprise_role_docker_tmpfs`"

        ```yaml
        # Type: list
        apprise_role_docker_tmpfs:
        ```

    ??? variable string "`apprise_role_docker_volume_driver`"

        ```yaml
        # Type: string
        apprise_role_docker_volume_driver:
        ```

    ??? variable list "`apprise_role_docker_volumes_from`"

        ```yaml
        # Type: list
        apprise_role_docker_volumes_from:
        ```

    ??? variable bool "`apprise_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_docker_volumes_global:
        ```

    ??? variable string "`apprise_role_docker_working_dir`"

        ```yaml
        # Type: string
        apprise_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`apprise_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_docker_auto_remove:
        ```

    ??? variable bool "`apprise_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_docker_cleanup:
        ```

    ??? variable string "`apprise_role_docker_force_kill`"

        ```yaml
        # Type: string
        apprise_role_docker_force_kill:
        ```

    ??? variable dict "`apprise_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        apprise_role_docker_healthcheck:
        ```

    ??? variable int "`apprise_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        apprise_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`apprise_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_docker_init:
        ```

    ??? variable string "`apprise_role_docker_kill_signal`"

        ```yaml
        # Type: string
        apprise_role_docker_kill_signal:
        ```

    ??? variable string "`apprise_role_docker_log_driver`"

        ```yaml
        # Type: string
        apprise_role_docker_log_driver:
        ```

    ??? variable dict "`apprise_role_docker_log_options`"

        ```yaml
        # Type: dict
        apprise_role_docker_log_options:
        ```

    ??? variable bool "`apprise_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_docker_oom_killer:
        ```

    ??? variable int "`apprise_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        apprise_role_docker_oom_score_adj:
        ```

    ??? variable bool "`apprise_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_docker_output_logs:
        ```

    ??? variable bool "`apprise_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_docker_paused:
        ```

    ??? variable bool "`apprise_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_docker_recreate:
        ```

    ??? variable int "`apprise_role_docker_restart_retries`"

        ```yaml
        # Type: int
        apprise_role_docker_restart_retries:
        ```

    ??? variable int "`apprise_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        apprise_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`apprise_role_docker_capabilities`"

        ```yaml
        # Type: list
        apprise_role_docker_capabilities:
        ```

    ??? variable string "`apprise_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        apprise_role_docker_cgroup_parent:
        ```

    ??? variable list "`apprise_role_docker_commands`"

        ```yaml
        # Type: list
        apprise_role_docker_commands:
        ```

    ??? variable int "`apprise_role_docker_create_timeout`"

        ```yaml
        # Type: int
        apprise_role_docker_create_timeout:
        ```

    ??? variable string "`apprise_role_docker_entrypoint`"

        ```yaml
        # Type: string
        apprise_role_docker_entrypoint:
        ```

    ??? variable string "`apprise_role_docker_env_file`"

        ```yaml
        # Type: string
        apprise_role_docker_env_file:
        ```

    ??? variable dict "`apprise_role_docker_labels`"

        ```yaml
        # Type: dict
        apprise_role_docker_labels:
        ```

    ??? variable bool "`apprise_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_docker_labels_use_common:
        ```

    ??? variable bool "`apprise_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_docker_read_only:
        ```

    ??? variable string "`apprise_role_docker_runtime`"

        ```yaml
        # Type: string
        apprise_role_docker_runtime:
        ```

    ??? variable list "`apprise_role_docker_sysctls`"

        ```yaml
        # Type: list
        apprise_role_docker_sysctls:
        ```

    ??? variable list "`apprise_role_docker_ulimits`"

        ```yaml
        # Type: list
        apprise_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`apprise_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        apprise_role_autoheal_enabled: true
        ```

    ??? variable string "`apprise_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        apprise_role_depends_on: ""
        ```

    ??? variable string "`apprise_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        apprise_role_depends_on_delay: "0"
        ```

    ??? variable string "`apprise_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        apprise_role_depends_on_healthchecks:
        ```

    ??? variable bool "`apprise_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        apprise_role_diun_enabled: true
        ```

    ??? variable bool "`apprise_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        apprise_role_dns_enabled: true
        ```

    ??? variable bool "`apprise_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        apprise_role_docker_controller: true
        ```

    ??? variable string "`apprise_role_docker_image_repo`"

        ```yaml
        # Type: string
        apprise_role_docker_image_repo:
        ```

    ??? variable string "`apprise_role_docker_image_tag`"

        ```yaml
        # Type: string
        apprise_role_docker_image_tag:
        ```

    ??? variable bool "`apprise_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_docker_volumes_download:
        ```

    ??? variable string "`apprise_role_paths_location`"

        ```yaml
        # Type: string
        apprise_role_paths_location:
        ```

    ??? variable string "`apprise_role_themepark_addons`"

        ```yaml
        # Type: string
        apprise_role_themepark_addons:
        ```

    ??? variable string "`apprise_role_themepark_app`"

        ```yaml
        # Type: string
        apprise_role_themepark_app:
        ```

    ??? variable string "`apprise_role_themepark_theme`"

        ```yaml
        # Type: string
        apprise_role_themepark_theme:
        ```

    ??? variable dict "`apprise_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        apprise_role_traefik_api_endpoint:
        ```

    ??? variable string "`apprise_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        apprise_role_traefik_api_middleware:
        ```

    ??? variable string "`apprise_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        apprise_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`apprise_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        apprise_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`apprise_role_traefik_certresolver`"

        ```yaml
        # Type: string
        apprise_role_traefik_certresolver:
        ```

    ??? variable bool "`apprise_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        apprise_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`apprise_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        apprise_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`apprise_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        apprise_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`apprise_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        apprise_role_traefik_middleware_http:
        ```

    ??? variable bool "`apprise_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`apprise_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`apprise_role_traefik_priority`"

        ```yaml
        # Type: string
        apprise_role_traefik_priority:
        ```

    ??? variable bool "`apprise_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        apprise_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`apprise_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        apprise_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`apprise_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        apprise_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`apprise_role_web_domain`"

        ```yaml
        # Type: string
        apprise_role_web_domain:
        ```

    ??? variable list "`apprise_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        apprise_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            apprise_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "apprise2.{{ user.domain }}"
              - "apprise.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`apprise_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        apprise_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            apprise_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'apprise2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`apprise_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        apprise_role_web_http_port:
        ```

    ??? variable string "`apprise_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        apprise_role_web_http_scheme:
        ```

    ??? variable dict "`apprise_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        apprise_role_web_http_serverstransport:
        ```

    ??? variable string "`apprise_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        apprise_role_web_scheme:
        ```

    ??? variable dict "`apprise_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        apprise_role_web_serverstransport:
        ```

    ??? variable string "`apprise_role_web_subdomain`"

        ```yaml
        # Type: string
        apprise_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
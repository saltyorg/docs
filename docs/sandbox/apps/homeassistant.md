---
icon: material/docker
hide:
  - tags
tags:
  - homeassistant
  - automation
  - iot
---

# Home Assistant

## Overview

[linuxserver/homeassistant](https://docs.linuxserver.io/images/docker-homeassistant) is a Docker container image for Homeassistant.

> [Homeassistant](https://www.home-assistant.io/) is a tool designed for (open source) home automation that puts local control and privacy first. Powered by a worldwide community of tinkerers and DIY enthusiasts. [:material-bookshelf:](https://www.home-assistant.io/docs/)

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://docs.linuxserver.io/general/container-customization){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/linuxserver/homeassistant/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://linuxserver.io/discord){ .md-button .md-button--stretch }

</div>

---

## Deployment

```shell
sb install sandbox-homeassistant
```

## Usage

Visit <https://homeassistant.iYOUR_DOMAIN_NAMEi>.

## Basics

Home Assistant is pretty versatile and works with a lot of different apps/containers, some of which we have roles for. See [MQTT](mqtt.md) for using Mosquitto to communicate with local and remote devices. We also have [Node Red](node_red.md), which is a platform for multiple types of automations.

??? Note "Nabu Casa"
    You don't NEED to use Nabu Casa to access Home Assistant remotely. You can use a reverse proxy to access it remotely. However, if you want to use Nabu Casa, you can use the [Nabu Casa](https://www.nabucasa.com/) integration to connect to Home Assistant. It is a paid service, but it is a good way to support the Home Assistant project. That said, the Home Assistant role is set up to work with a reverse proxy, so you can use that instead.

### Addons

You can also use the [Home Assistant Community Store (HACS)](https://hacs.xyz/) to add more functionality to Home Assistant. For instance, adding the Node Red Companion, a "custom" integration for node-red-contrib-home-assistant-websocket. It allows you to integrate Node-RED with Home Assistant. For more information, see the [Node Red](node_red.md) page.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        homeassistant_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `homeassistant_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `homeassistant_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`homeassistant_name`"

        ```yaml
        # Type: string
        homeassistant_name: homeassistant
        ```

=== "Web"

    ??? variable string "`homeassistant_role_web_subdomain`"

        ```yaml
        # Type: string
        homeassistant_role_web_subdomain: "{{ homeassistant_name }}"
        ```

    ??? variable string "`homeassistant_role_web_domain`"

        ```yaml
        # Type: string
        homeassistant_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`homeassistant_role_web_port`"

        ```yaml
        # Type: string
        homeassistant_role_web_port: "8123"
        ```

    ??? variable string "`homeassistant_role_web_url`"

        ```yaml
        # Type: string
        homeassistant_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='homeassistant') + '.' + lookup('role_var', '_web_domain', role='homeassistant')
                                     if (lookup('role_var', '_web_subdomain', role='homeassistant') | length > 0)
                                     else lookup('role_var', '_web_domain', role='homeassistant')) }}"
        ```

=== "DNS"

    ??? variable string "`homeassistant_role_dns_record`"

        ```yaml
        # Type: string
        homeassistant_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='homeassistant') }}"
        ```

    ??? variable string "`homeassistant_role_dns_zone`"

        ```yaml
        # Type: string
        homeassistant_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='homeassistant') }}"
        ```

    ??? variable bool "`homeassistant_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`homeassistant_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        homeassistant_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`homeassistant_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        homeassistant_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`homeassistant_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        homeassistant_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`homeassistant_role_traefik_certresolver`"

        ```yaml
        # Type: string
        homeassistant_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`homeassistant_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_traefik_enabled: true
        ```

    ??? variable bool "`homeassistant_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_traefik_api_enabled: false
        ```

    ??? variable string "`homeassistant_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        homeassistant_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`homeassistant_role_docker_container`"

        ```yaml
        # Type: string
        homeassistant_role_docker_container: "{{ homeassistant_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`homeassistant_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_docker_image_pull: true
        ```

    ??? variable string "`homeassistant_role_docker_image_repo`"

        ```yaml
        # Type: string
        homeassistant_role_docker_image_repo: "lscr.io/linuxserver/homeassistant"
        ```

    ??? variable string "`homeassistant_role_docker_image_tag`"

        ```yaml
        # Type: string
        homeassistant_role_docker_image_tag: "latest"
        ```

    ??? variable string "`homeassistant_role_docker_image`"

        ```yaml
        # Type: string
        homeassistant_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='homeassistant') }}:{{ lookup('role_var', '_docker_image_tag', role='homeassistant') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`homeassistant_role_docker_envs_default`"

        ```yaml
        # Type: dict
        homeassistant_role_docker_envs_default:
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
        ```

    ??? variable dict "`homeassistant_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        homeassistant_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`homeassistant_role_docker_volumes_default`"

        ```yaml
        # Type: list
        homeassistant_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='homeassistant') }}:/config"
          - "/etc/localtime:/etc/localtime:ro"
          - "/run/dbus:/run/dbus:ro"
        ```

    ??? variable list "`homeassistant_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        homeassistant_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`homeassistant_role_docker_hostname`"

        ```yaml
        # Type: string
        homeassistant_role_docker_hostname: "{{ homeassistant_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`homeassistant_role_docker_networks_alias`"

        ```yaml
        # Type: string
        homeassistant_role_docker_networks_alias: "{{ homeassistant_name }}"
        ```

    ??? variable list "`homeassistant_role_docker_networks_default`"

        ```yaml
        # Type: list
        homeassistant_role_docker_networks_default: []
        ```

    ??? variable list "`homeassistant_role_docker_networks_custom`"

        ```yaml
        # Type: list
        homeassistant_role_docker_networks_custom: []
        ```

    <h5>Network Mode</h5>

    ??? variable string "`homeassistant_role_docker_network_mode`"

        ```yaml
        # Type: string
        homeassistant_role_docker_network_mode: "host"
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`homeassistant_role_docker_restart_policy`"

        ```yaml
        # Type: string
        homeassistant_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`homeassistant_role_docker_state`"

        ```yaml
        # Type: string
        homeassistant_role_docker_state: started
        ```

    <h5>Privileged</h5>

    ??? variable bool "`homeassistant_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_docker_privileged: true
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`homeassistant_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        homeassistant_role_docker_blkio_weight:
        ```

    ??? variable int "`homeassistant_role_docker_cpu_period`"

        ```yaml
        # Type: int
        homeassistant_role_docker_cpu_period:
        ```

    ??? variable int "`homeassistant_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        homeassistant_role_docker_cpu_quota:
        ```

    ??? variable int "`homeassistant_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        homeassistant_role_docker_cpu_shares:
        ```

    ??? variable string "`homeassistant_role_docker_cpus`"

        ```yaml
        # Type: string
        homeassistant_role_docker_cpus:
        ```

    ??? variable string "`homeassistant_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        homeassistant_role_docker_cpuset_cpus:
        ```

    ??? variable string "`homeassistant_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        homeassistant_role_docker_cpuset_mems:
        ```

    ??? variable string "`homeassistant_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        homeassistant_role_docker_kernel_memory:
        ```

    ??? variable string "`homeassistant_role_docker_memory`"

        ```yaml
        # Type: string
        homeassistant_role_docker_memory:
        ```

    ??? variable string "`homeassistant_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        homeassistant_role_docker_memory_reservation:
        ```

    ??? variable string "`homeassistant_role_docker_memory_swap`"

        ```yaml
        # Type: string
        homeassistant_role_docker_memory_swap:
        ```

    ??? variable int "`homeassistant_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        homeassistant_role_docker_memory_swappiness:
        ```

    ??? variable string "`homeassistant_role_docker_shm_size`"

        ```yaml
        # Type: string
        homeassistant_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`homeassistant_role_docker_cap_drop`"

        ```yaml
        # Type: list
        homeassistant_role_docker_cap_drop:
        ```

    ??? variable string "`homeassistant_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        homeassistant_role_docker_cgroupns_mode:
        ```

    ??? variable list "`homeassistant_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        homeassistant_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`homeassistant_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        homeassistant_role_docker_device_read_bps:
        ```

    ??? variable list "`homeassistant_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        homeassistant_role_docker_device_read_iops:
        ```

    ??? variable list "`homeassistant_role_docker_device_requests`"

        ```yaml
        # Type: list
        homeassistant_role_docker_device_requests:
        ```

    ??? variable list "`homeassistant_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        homeassistant_role_docker_device_write_bps:
        ```

    ??? variable list "`homeassistant_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        homeassistant_role_docker_device_write_iops:
        ```

    ??? variable list "`homeassistant_role_docker_devices`"

        ```yaml
        # Type: list
        homeassistant_role_docker_devices:
        ```

    ??? variable string "`homeassistant_role_docker_devices_default`"

        ```yaml
        # Type: string
        homeassistant_role_docker_devices_default:
        ```

    ??? variable list "`homeassistant_role_docker_groups`"

        ```yaml
        # Type: list
        homeassistant_role_docker_groups:
        ```

    ??? variable list "`homeassistant_role_docker_security_opts`"

        ```yaml
        # Type: list
        homeassistant_role_docker_security_opts:
        ```

    ??? variable string "`homeassistant_role_docker_user`"

        ```yaml
        # Type: string
        homeassistant_role_docker_user:
        ```

    ??? variable string "`homeassistant_role_docker_userns_mode`"

        ```yaml
        # Type: string
        homeassistant_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`homeassistant_role_docker_dns_opts`"

        ```yaml
        # Type: list
        homeassistant_role_docker_dns_opts:
        ```

    ??? variable list "`homeassistant_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        homeassistant_role_docker_dns_search_domains:
        ```

    ??? variable list "`homeassistant_role_docker_dns_servers`"

        ```yaml
        # Type: list
        homeassistant_role_docker_dns_servers:
        ```

    ??? variable string "`homeassistant_role_docker_domainname`"

        ```yaml
        # Type: string
        homeassistant_role_docker_domainname:
        ```

    ??? variable list "`homeassistant_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        homeassistant_role_docker_exposed_ports:
        ```

    ??? variable dict "`homeassistant_role_docker_hosts`"

        ```yaml
        # Type: dict
        homeassistant_role_docker_hosts:
        ```

    ??? variable bool "`homeassistant_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_docker_hosts_use_common:
        ```

    ??? variable string "`homeassistant_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        homeassistant_role_docker_ipc_mode:
        ```

    ??? variable list "`homeassistant_role_docker_links`"

        ```yaml
        # Type: list
        homeassistant_role_docker_links:
        ```

    ??? variable string "`homeassistant_role_docker_pid_mode`"

        ```yaml
        # Type: string
        homeassistant_role_docker_pid_mode:
        ```

    ??? variable list "`homeassistant_role_docker_ports`"

        ```yaml
        # Type: list
        homeassistant_role_docker_ports:
        ```

    ??? variable string "`homeassistant_role_docker_uts`"

        ```yaml
        # Type: string
        homeassistant_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`homeassistant_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_docker_keep_volumes:
        ```

    ??? variable list "`homeassistant_role_docker_mounts`"

        ```yaml
        # Type: list
        homeassistant_role_docker_mounts:
        ```

    ??? variable dict "`homeassistant_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        homeassistant_role_docker_storage_opts:
        ```

    ??? variable list "`homeassistant_role_docker_tmpfs`"

        ```yaml
        # Type: list
        homeassistant_role_docker_tmpfs:
        ```

    ??? variable string "`homeassistant_role_docker_volume_driver`"

        ```yaml
        # Type: string
        homeassistant_role_docker_volume_driver:
        ```

    ??? variable list "`homeassistant_role_docker_volumes_from`"

        ```yaml
        # Type: list
        homeassistant_role_docker_volumes_from:
        ```

    ??? variable bool "`homeassistant_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_docker_volumes_global:
        ```

    ??? variable string "`homeassistant_role_docker_working_dir`"

        ```yaml
        # Type: string
        homeassistant_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`homeassistant_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_docker_auto_remove:
        ```

    ??? variable bool "`homeassistant_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_docker_cleanup:
        ```

    ??? variable string "`homeassistant_role_docker_force_kill`"

        ```yaml
        # Type: string
        homeassistant_role_docker_force_kill:
        ```

    ??? variable dict "`homeassistant_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        homeassistant_role_docker_healthcheck:
        ```

    ??? variable int "`homeassistant_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        homeassistant_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`homeassistant_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_docker_init:
        ```

    ??? variable string "`homeassistant_role_docker_kill_signal`"

        ```yaml
        # Type: string
        homeassistant_role_docker_kill_signal:
        ```

    ??? variable string "`homeassistant_role_docker_log_driver`"

        ```yaml
        # Type: string
        homeassistant_role_docker_log_driver:
        ```

    ??? variable dict "`homeassistant_role_docker_log_options`"

        ```yaml
        # Type: dict
        homeassistant_role_docker_log_options:
        ```

    ??? variable bool "`homeassistant_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_docker_oom_killer:
        ```

    ??? variable int "`homeassistant_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        homeassistant_role_docker_oom_score_adj:
        ```

    ??? variable bool "`homeassistant_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_docker_output_logs:
        ```

    ??? variable bool "`homeassistant_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_docker_paused:
        ```

    ??? variable bool "`homeassistant_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_docker_recreate:
        ```

    ??? variable int "`homeassistant_role_docker_restart_retries`"

        ```yaml
        # Type: int
        homeassistant_role_docker_restart_retries:
        ```

    ??? variable int "`homeassistant_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        homeassistant_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`homeassistant_role_docker_capabilities`"

        ```yaml
        # Type: list
        homeassistant_role_docker_capabilities:
        ```

    ??? variable string "`homeassistant_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        homeassistant_role_docker_cgroup_parent:
        ```

    ??? variable list "`homeassistant_role_docker_commands`"

        ```yaml
        # Type: list
        homeassistant_role_docker_commands:
        ```

    ??? variable int "`homeassistant_role_docker_create_timeout`"

        ```yaml
        # Type: int
        homeassistant_role_docker_create_timeout:
        ```

    ??? variable string "`homeassistant_role_docker_entrypoint`"

        ```yaml
        # Type: string
        homeassistant_role_docker_entrypoint:
        ```

    ??? variable string "`homeassistant_role_docker_env_file`"

        ```yaml
        # Type: string
        homeassistant_role_docker_env_file:
        ```

    ??? variable dict "`homeassistant_role_docker_labels`"

        ```yaml
        # Type: dict
        homeassistant_role_docker_labels:
        ```

    ??? variable bool "`homeassistant_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_docker_labels_use_common:
        ```

    ??? variable bool "`homeassistant_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_docker_read_only:
        ```

    ??? variable string "`homeassistant_role_docker_runtime`"

        ```yaml
        # Type: string
        homeassistant_role_docker_runtime:
        ```

    ??? variable list "`homeassistant_role_docker_sysctls`"

        ```yaml
        # Type: list
        homeassistant_role_docker_sysctls:
        ```

    ??? variable list "`homeassistant_role_docker_ulimits`"

        ```yaml
        # Type: list
        homeassistant_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`homeassistant_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        homeassistant_role_autoheal_enabled: true
        ```

    ??? variable string "`homeassistant_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        homeassistant_role_depends_on: ""
        ```

    ??? variable string "`homeassistant_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        homeassistant_role_depends_on_delay: "0"
        ```

    ??? variable string "`homeassistant_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        homeassistant_role_depends_on_healthchecks:
        ```

    ??? variable bool "`homeassistant_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        homeassistant_role_diun_enabled: true
        ```

    ??? variable bool "`homeassistant_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        homeassistant_role_dns_enabled: true
        ```

    ??? variable bool "`homeassistant_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        homeassistant_role_docker_controller: true
        ```

    ??? variable string "`homeassistant_role_docker_image_repo`"

        ```yaml
        # Type: string
        homeassistant_role_docker_image_repo:
        ```

    ??? variable string "`homeassistant_role_docker_image_tag`"

        ```yaml
        # Type: string
        homeassistant_role_docker_image_tag:
        ```

    ??? variable bool "`homeassistant_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_docker_volumes_download:
        ```

    ??? variable string "`homeassistant_role_paths_location`"

        ```yaml
        # Type: string
        homeassistant_role_paths_location:
        ```

    ??? variable string "`homeassistant_role_themepark_addons`"

        ```yaml
        # Type: string
        homeassistant_role_themepark_addons:
        ```

    ??? variable string "`homeassistant_role_themepark_app`"

        ```yaml
        # Type: string
        homeassistant_role_themepark_app:
        ```

    ??? variable string "`homeassistant_role_themepark_theme`"

        ```yaml
        # Type: string
        homeassistant_role_themepark_theme:
        ```

    ??? variable dict "`homeassistant_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        homeassistant_role_traefik_api_endpoint:
        ```

    ??? variable string "`homeassistant_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        homeassistant_role_traefik_api_middleware:
        ```

    ??? variable string "`homeassistant_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        homeassistant_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`homeassistant_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        homeassistant_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`homeassistant_role_traefik_certresolver`"

        ```yaml
        # Type: string
        homeassistant_role_traefik_certresolver:
        ```

    ??? variable bool "`homeassistant_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        homeassistant_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`homeassistant_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        homeassistant_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`homeassistant_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        homeassistant_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`homeassistant_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        homeassistant_role_traefik_middleware_http:
        ```

    ??? variable bool "`homeassistant_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`homeassistant_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`homeassistant_role_traefik_priority`"

        ```yaml
        # Type: string
        homeassistant_role_traefik_priority:
        ```

    ??? variable bool "`homeassistant_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        homeassistant_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`homeassistant_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        homeassistant_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`homeassistant_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        homeassistant_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`homeassistant_role_web_domain`"

        ```yaml
        # Type: string
        homeassistant_role_web_domain:
        ```

    ??? variable list "`homeassistant_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        homeassistant_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            homeassistant_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "homeassistant2.{{ user.domain }}"
              - "homeassistant.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`homeassistant_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        homeassistant_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            homeassistant_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'homeassistant2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`homeassistant_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        homeassistant_role_web_http_port:
        ```

    ??? variable string "`homeassistant_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        homeassistant_role_web_http_scheme:
        ```

    ??? variable dict "`homeassistant_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        homeassistant_role_web_http_serverstransport:
        ```

    ??? variable string "`homeassistant_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        homeassistant_role_web_scheme:
        ```

    ??? variable dict "`homeassistant_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        homeassistant_role_web_serverstransport:
        ```

    ??? variable string "`homeassistant_role_web_subdomain`"

        ```yaml
        # Type: string
        homeassistant_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
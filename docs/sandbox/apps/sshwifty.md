---
icon: material/docker
hide:
  - tags
tags:
  - sshwifty
  - networking
  - ssh
---

# Sshwifty

## Overview

[Sshwifty](https://github.com/nirui/sshwifty) is an SSH and Telnet connector made for the Web. It can be deployed on your computer or server to provide SSH and Telnet access interface for any compatible (standard) web browser.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://github.com/nirui/sshwifty){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/niruix/sshwifty/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-people-group:**Community**](){ .md-button .md-button--stretch }

</div>

---

## Deployment

```shell
sb install sandbox-sshwifty
```

## Usage

Visit <https://sshwifty.iYOUR_DOMAIN_NAMEi>.

## Basics

- The pre-configured password is taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables.<span title="View override details for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        sshwifty_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `sshwifty_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `sshwifty_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`sshwifty_name`"

        ```yaml
        # Type: string
        sshwifty_name: sshwifty
        ```

=== "Web"

    ??? variable string "`sshwifty_role_web_subdomain`"

        ```yaml
        # Type: string
        sshwifty_role_web_subdomain: "{{ sshwifty_name }}"
        ```

    ??? variable string "`sshwifty_role_web_domain`"

        ```yaml
        # Type: string
        sshwifty_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`sshwifty_role_web_port`"

        ```yaml
        # Type: string
        sshwifty_role_web_port: "8182"
        ```

    ??? variable string "`sshwifty_role_web_url`"

        ```yaml
        # Type: string
        sshwifty_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='sshwifty') + '.' + lookup('role_var', '_web_domain', role='sshwifty')
                                if (lookup('role_var', '_web_subdomain', role='sshwifty') | length > 0)
                                else lookup('role_var', '_web_domain', role='sshwifty')) }}"
        ```

=== "DNS"

    ??? variable string "`sshwifty_role_dns_record`"

        ```yaml
        # Type: string
        sshwifty_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='sshwifty') }}"
        ```

    ??? variable string "`sshwifty_role_dns_zone`"

        ```yaml
        # Type: string
        sshwifty_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='sshwifty') }}"
        ```

    ??? variable bool "`sshwifty_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`sshwifty_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        sshwifty_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`sshwifty_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        sshwifty_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`sshwifty_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        sshwifty_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`sshwifty_role_traefik_certresolver`"

        ```yaml
        # Type: string
        sshwifty_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`sshwifty_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_traefik_enabled: true
        ```

    ??? variable bool "`sshwifty_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_traefik_api_enabled: false
        ```

    ??? variable string "`sshwifty_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        sshwifty_role_traefik_api_endpoint: ""
        ```

    ??? variable bool "`sshwifty_role_traefik_error_pages_enabled`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_traefik_error_pages_enabled: false
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`sshwifty_role_docker_container`"

        ```yaml
        # Type: string
        sshwifty_role_docker_container: "{{ sshwifty_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`sshwifty_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_docker_image_pull: true
        ```

    ??? variable string "`sshwifty_role_docker_image_repo`"

        ```yaml
        # Type: string
        sshwifty_role_docker_image_repo: "niruix/sshwifty"
        ```

    ??? variable string "`sshwifty_role_docker_image_tag`"

        ```yaml
        # Type: string
        sshwifty_role_docker_image_tag: "latest"
        ```

    ??? variable string "`sshwifty_role_docker_image`"

        ```yaml
        # Type: string
        sshwifty_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='sshwifty') }}:{{ lookup('role_var', '_docker_image_tag', role='sshwifty') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`sshwifty_role_docker_envs_default`"

        ```yaml
        # Type: dict
        sshwifty_role_docker_envs_default:
          SSHWIFTY_CONFIG: "/config/sshwifty.conf.json"
        ```

    ??? variable dict "`sshwifty_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        sshwifty_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`sshwifty_role_docker_volumes_default`"

        ```yaml
        # Type: list
        sshwifty_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='sshwifty') }}/config:/config"
        ```

    ??? variable list "`sshwifty_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        sshwifty_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`sshwifty_role_docker_hostname`"

        ```yaml
        # Type: string
        sshwifty_role_docker_hostname: "{{ sshwifty_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`sshwifty_role_docker_networks_alias`"

        ```yaml
        # Type: string
        sshwifty_role_docker_networks_alias: "{{ sshwifty_name }}"
        ```

    ??? variable list "`sshwifty_role_docker_networks_default`"

        ```yaml
        # Type: list
        sshwifty_role_docker_networks_default: []
        ```

    ??? variable list "`sshwifty_role_docker_networks_custom`"

        ```yaml
        # Type: list
        sshwifty_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`sshwifty_role_docker_restart_policy`"

        ```yaml
        # Type: string
        sshwifty_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`sshwifty_role_docker_state`"

        ```yaml
        # Type: string
        sshwifty_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`sshwifty_role_docker_user`"

        ```yaml
        # Type: string
        sshwifty_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`sshwifty_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        sshwifty_role_docker_blkio_weight:
        ```

    ??? variable int "`sshwifty_role_docker_cpu_period`"

        ```yaml
        # Type: int
        sshwifty_role_docker_cpu_period:
        ```

    ??? variable int "`sshwifty_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        sshwifty_role_docker_cpu_quota:
        ```

    ??? variable int "`sshwifty_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        sshwifty_role_docker_cpu_shares:
        ```

    ??? variable string "`sshwifty_role_docker_cpus`"

        ```yaml
        # Type: string
        sshwifty_role_docker_cpus:
        ```

    ??? variable string "`sshwifty_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        sshwifty_role_docker_cpuset_cpus:
        ```

    ??? variable string "`sshwifty_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        sshwifty_role_docker_cpuset_mems:
        ```

    ??? variable string "`sshwifty_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        sshwifty_role_docker_kernel_memory:
        ```

    ??? variable string "`sshwifty_role_docker_memory`"

        ```yaml
        # Type: string
        sshwifty_role_docker_memory:
        ```

    ??? variable string "`sshwifty_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        sshwifty_role_docker_memory_reservation:
        ```

    ??? variable string "`sshwifty_role_docker_memory_swap`"

        ```yaml
        # Type: string
        sshwifty_role_docker_memory_swap:
        ```

    ??? variable int "`sshwifty_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        sshwifty_role_docker_memory_swappiness:
        ```

    ??? variable string "`sshwifty_role_docker_shm_size`"

        ```yaml
        # Type: string
        sshwifty_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`sshwifty_role_docker_cap_drop`"

        ```yaml
        # Type: list
        sshwifty_role_docker_cap_drop:
        ```

    ??? variable string "`sshwifty_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        sshwifty_role_docker_cgroupns_mode:
        ```

    ??? variable list "`sshwifty_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        sshwifty_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`sshwifty_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        sshwifty_role_docker_device_read_bps:
        ```

    ??? variable list "`sshwifty_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        sshwifty_role_docker_device_read_iops:
        ```

    ??? variable list "`sshwifty_role_docker_device_requests`"

        ```yaml
        # Type: list
        sshwifty_role_docker_device_requests:
        ```

    ??? variable list "`sshwifty_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        sshwifty_role_docker_device_write_bps:
        ```

    ??? variable list "`sshwifty_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        sshwifty_role_docker_device_write_iops:
        ```

    ??? variable list "`sshwifty_role_docker_devices`"

        ```yaml
        # Type: list
        sshwifty_role_docker_devices:
        ```

    ??? variable string "`sshwifty_role_docker_devices_default`"

        ```yaml
        # Type: string
        sshwifty_role_docker_devices_default:
        ```

    ??? variable list "`sshwifty_role_docker_groups`"

        ```yaml
        # Type: list
        sshwifty_role_docker_groups:
        ```

    ??? variable bool "`sshwifty_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_docker_privileged:
        ```

    ??? variable list "`sshwifty_role_docker_security_opts`"

        ```yaml
        # Type: list
        sshwifty_role_docker_security_opts:
        ```

    ??? variable string "`sshwifty_role_docker_userns_mode`"

        ```yaml
        # Type: string
        sshwifty_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`sshwifty_role_docker_dns_opts`"

        ```yaml
        # Type: list
        sshwifty_role_docker_dns_opts:
        ```

    ??? variable list "`sshwifty_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        sshwifty_role_docker_dns_search_domains:
        ```

    ??? variable list "`sshwifty_role_docker_dns_servers`"

        ```yaml
        # Type: list
        sshwifty_role_docker_dns_servers:
        ```

    ??? variable string "`sshwifty_role_docker_domainname`"

        ```yaml
        # Type: string
        sshwifty_role_docker_domainname:
        ```

    ??? variable list "`sshwifty_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        sshwifty_role_docker_exposed_ports:
        ```

    ??? variable dict "`sshwifty_role_docker_hosts`"

        ```yaml
        # Type: dict
        sshwifty_role_docker_hosts:
        ```

    ??? variable bool "`sshwifty_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_docker_hosts_use_common:
        ```

    ??? variable string "`sshwifty_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        sshwifty_role_docker_ipc_mode:
        ```

    ??? variable list "`sshwifty_role_docker_links`"

        ```yaml
        # Type: list
        sshwifty_role_docker_links:
        ```

    ??? variable string "`sshwifty_role_docker_network_mode`"

        ```yaml
        # Type: string
        sshwifty_role_docker_network_mode:
        ```

    ??? variable string "`sshwifty_role_docker_pid_mode`"

        ```yaml
        # Type: string
        sshwifty_role_docker_pid_mode:
        ```

    ??? variable list "`sshwifty_role_docker_ports`"

        ```yaml
        # Type: list
        sshwifty_role_docker_ports:
        ```

    ??? variable string "`sshwifty_role_docker_uts`"

        ```yaml
        # Type: string
        sshwifty_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`sshwifty_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_docker_keep_volumes:
        ```

    ??? variable list "`sshwifty_role_docker_mounts`"

        ```yaml
        # Type: list
        sshwifty_role_docker_mounts:
        ```

    ??? variable dict "`sshwifty_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        sshwifty_role_docker_storage_opts:
        ```

    ??? variable list "`sshwifty_role_docker_tmpfs`"

        ```yaml
        # Type: list
        sshwifty_role_docker_tmpfs:
        ```

    ??? variable string "`sshwifty_role_docker_volume_driver`"

        ```yaml
        # Type: string
        sshwifty_role_docker_volume_driver:
        ```

    ??? variable list "`sshwifty_role_docker_volumes_from`"

        ```yaml
        # Type: list
        sshwifty_role_docker_volumes_from:
        ```

    ??? variable bool "`sshwifty_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_docker_volumes_global:
        ```

    ??? variable string "`sshwifty_role_docker_working_dir`"

        ```yaml
        # Type: string
        sshwifty_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`sshwifty_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_docker_auto_remove:
        ```

    ??? variable bool "`sshwifty_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_docker_cleanup:
        ```

    ??? variable string "`sshwifty_role_docker_force_kill`"

        ```yaml
        # Type: string
        sshwifty_role_docker_force_kill:
        ```

    ??? variable dict "`sshwifty_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        sshwifty_role_docker_healthcheck:
        ```

    ??? variable int "`sshwifty_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        sshwifty_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`sshwifty_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_docker_init:
        ```

    ??? variable string "`sshwifty_role_docker_kill_signal`"

        ```yaml
        # Type: string
        sshwifty_role_docker_kill_signal:
        ```

    ??? variable string "`sshwifty_role_docker_log_driver`"

        ```yaml
        # Type: string
        sshwifty_role_docker_log_driver:
        ```

    ??? variable dict "`sshwifty_role_docker_log_options`"

        ```yaml
        # Type: dict
        sshwifty_role_docker_log_options:
        ```

    ??? variable bool "`sshwifty_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_docker_oom_killer:
        ```

    ??? variable int "`sshwifty_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        sshwifty_role_docker_oom_score_adj:
        ```

    ??? variable bool "`sshwifty_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_docker_output_logs:
        ```

    ??? variable bool "`sshwifty_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_docker_paused:
        ```

    ??? variable bool "`sshwifty_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_docker_recreate:
        ```

    ??? variable int "`sshwifty_role_docker_restart_retries`"

        ```yaml
        # Type: int
        sshwifty_role_docker_restart_retries:
        ```

    ??? variable int "`sshwifty_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        sshwifty_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`sshwifty_role_docker_capabilities`"

        ```yaml
        # Type: list
        sshwifty_role_docker_capabilities:
        ```

    ??? variable string "`sshwifty_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        sshwifty_role_docker_cgroup_parent:
        ```

    ??? variable list "`sshwifty_role_docker_commands`"

        ```yaml
        # Type: list
        sshwifty_role_docker_commands:
        ```

    ??? variable int "`sshwifty_role_docker_create_timeout`"

        ```yaml
        # Type: int
        sshwifty_role_docker_create_timeout:
        ```

    ??? variable string "`sshwifty_role_docker_entrypoint`"

        ```yaml
        # Type: string
        sshwifty_role_docker_entrypoint:
        ```

    ??? variable string "`sshwifty_role_docker_env_file`"

        ```yaml
        # Type: string
        sshwifty_role_docker_env_file:
        ```

    ??? variable dict "`sshwifty_role_docker_labels`"

        ```yaml
        # Type: dict
        sshwifty_role_docker_labels:
        ```

    ??? variable bool "`sshwifty_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_docker_labels_use_common:
        ```

    ??? variable bool "`sshwifty_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_docker_read_only:
        ```

    ??? variable string "`sshwifty_role_docker_runtime`"

        ```yaml
        # Type: string
        sshwifty_role_docker_runtime:
        ```

    ??? variable list "`sshwifty_role_docker_sysctls`"

        ```yaml
        # Type: list
        sshwifty_role_docker_sysctls:
        ```

    ??? variable list "`sshwifty_role_docker_ulimits`"

        ```yaml
        # Type: list
        sshwifty_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`sshwifty_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        sshwifty_role_autoheal_enabled: true
        ```

    ??? variable string "`sshwifty_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        sshwifty_role_depends_on: ""
        ```

    ??? variable string "`sshwifty_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        sshwifty_role_depends_on_delay: "0"
        ```

    ??? variable string "`sshwifty_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        sshwifty_role_depends_on_healthchecks:
        ```

    ??? variable bool "`sshwifty_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        sshwifty_role_diun_enabled: true
        ```

    ??? variable bool "`sshwifty_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        sshwifty_role_dns_enabled: true
        ```

    ??? variable bool "`sshwifty_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        sshwifty_role_docker_controller: true
        ```

    ??? variable string "`sshwifty_role_docker_image_repo`"

        ```yaml
        # Type: string
        sshwifty_role_docker_image_repo:
        ```

    ??? variable string "`sshwifty_role_docker_image_tag`"

        ```yaml
        # Type: string
        sshwifty_role_docker_image_tag:
        ```

    ??? variable bool "`sshwifty_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_docker_volumes_download:
        ```

    ??? variable string "`sshwifty_role_paths_location`"

        ```yaml
        # Type: string
        sshwifty_role_paths_location:
        ```

    ??? variable string "`sshwifty_role_themepark_addons`"

        ```yaml
        # Type: string
        sshwifty_role_themepark_addons:
        ```

    ??? variable string "`sshwifty_role_themepark_app`"

        ```yaml
        # Type: string
        sshwifty_role_themepark_app:
        ```

    ??? variable string "`sshwifty_role_themepark_theme`"

        ```yaml
        # Type: string
        sshwifty_role_themepark_theme:
        ```

    ??? variable dict "`sshwifty_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        sshwifty_role_traefik_api_endpoint:
        ```

    ??? variable string "`sshwifty_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        sshwifty_role_traefik_api_middleware:
        ```

    ??? variable string "`sshwifty_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        sshwifty_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`sshwifty_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        sshwifty_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`sshwifty_role_traefik_certresolver`"

        ```yaml
        # Type: string
        sshwifty_role_traefik_certresolver:
        ```

    ??? variable bool "`sshwifty_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        sshwifty_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`sshwifty_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        sshwifty_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`sshwifty_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        sshwifty_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`sshwifty_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        sshwifty_role_traefik_middleware_http:
        ```

    ??? variable bool "`sshwifty_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`sshwifty_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`sshwifty_role_traefik_priority`"

        ```yaml
        # Type: string
        sshwifty_role_traefik_priority:
        ```

    ??? variable bool "`sshwifty_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        sshwifty_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`sshwifty_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        sshwifty_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`sshwifty_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        sshwifty_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`sshwifty_role_web_domain`"

        ```yaml
        # Type: string
        sshwifty_role_web_domain:
        ```

    ??? variable list "`sshwifty_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        sshwifty_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            sshwifty_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "sshwifty2.{{ user.domain }}"
              - "sshwifty.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`sshwifty_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        sshwifty_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            sshwifty_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'sshwifty2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`sshwifty_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        sshwifty_role_web_http_port:
        ```

    ??? variable string "`sshwifty_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        sshwifty_role_web_http_scheme:
        ```

    ??? variable dict "`sshwifty_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        sshwifty_role_web_http_serverstransport:
        ```

    ??? variable string "`sshwifty_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        sshwifty_role_web_scheme:
        ```

    ??? variable dict "`sshwifty_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        sshwifty_role_web_serverstransport:
        ```

    ??? variable string "`sshwifty_role_web_subdomain`"

        ```yaml
        # Type: string
        sshwifty_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
icon: material/docker
hide:
  - tags
tags:
  - komga
  - media
  - comics
saltbox_automation:
  app_links:
    - name: Manual
      url: https://komga.org/installation/docker.html
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/gotson/komga/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Komga
    summary: |-
      a free and open source comics/mangas server.
    link: https://komga.org/
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Komga

## Overview

[Komga](https://komga.org/) is a free and open source comics/mangas server.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://komga.org/installation/docker.html){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/gotson/komga/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-komga
```

## Usage

Visit <https://komga.iYOUR_DOMAIN_NAMEi>.

## Basics

- On first opening you will be asked to create a user account. <br />
  Choose an email and password, then click on Create User Account.

- Komga expects comics to be stored in `/mnt/unionfs/Media/Comics`.

- `/mnt` is accessible to the container as well.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        komga_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `komga_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `komga_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`komga_name`"

        ```yaml
        # Type: string
        komga_name: komga
        ```

=== "Web"

    ??? variable string "`komga_role_web_subdomain`"

        ```yaml
        # Type: string
        komga_role_web_subdomain: "{{ komga_name }}"
        ```

    ??? variable string "`komga_role_web_domain`"

        ```yaml
        # Type: string
        komga_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`komga_role_web_port`"

        ```yaml
        # Type: string
        komga_role_web_port: "25600"
        ```

    ??? variable string "`komga_role_web_url`"

        ```yaml
        # Type: string
        komga_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='komga') + '.' + lookup('role_var', '_web_domain', role='komga')
                             if (lookup('role_var', '_web_subdomain', role='komga') | length > 0)
                             else lookup('role_var', '_web_domain', role='komga')) }}"
        ```

=== "DNS"

    ??? variable string "`komga_role_dns_record`"

        ```yaml
        # Type: string
        komga_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='komga') }}"
        ```

    ??? variable string "`komga_role_dns_zone`"

        ```yaml
        # Type: string
        komga_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='komga') }}"
        ```

    ??? variable bool "`komga_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        komga_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`komga_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        komga_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`komga_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        komga_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`komga_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        komga_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`komga_role_traefik_certresolver`"

        ```yaml
        # Type: string
        komga_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`komga_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        komga_role_traefik_enabled: true
        ```

    ??? variable bool "`komga_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        komga_role_traefik_api_enabled: false
        ```

    ??? variable string "`komga_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        komga_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`komga_role_docker_container`"

        ```yaml
        # Type: string
        komga_role_docker_container: "{{ komga_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`komga_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        komga_role_docker_image_pull: true
        ```

    ??? variable string "`komga_role_docker_image_tag`"

        ```yaml
        # Type: string
        komga_role_docker_image_tag: "latest"
        ```

    ??? variable string "`komga_role_docker_image_repo`"

        ```yaml
        # Type: string
        komga_role_docker_image_repo: "gotson/komga"
        ```

    ??? variable string "`komga_role_docker_image`"

        ```yaml
        # Type: string
        komga_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='komga') }}:{{ lookup('role_var', '_docker_image_tag', role='komga') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`komga_role_docker_envs_default`"

        ```yaml
        # Type: dict
        komga_role_docker_envs_default:
          KOMGA_CORS_ALLOWEDORIGINS: "*"
        ```

    ??? variable dict "`komga_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        komga_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`komga_role_docker_volumes_default`"

        ```yaml
        # Type: list
        komga_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='komga') }}:/config"
          - "/mnt/unionfs/Media/Comics:/comics"
        ```

    ??? variable list "`komga_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        komga_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`komga_role_docker_hostname`"

        ```yaml
        # Type: string
        komga_role_docker_hostname: "{{ komga_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`komga_role_docker_networks_alias`"

        ```yaml
        # Type: string
        komga_role_docker_networks_alias: "{{ komga_name }}"
        ```

    ??? variable list "`komga_role_docker_networks_default`"

        ```yaml
        # Type: list
        komga_role_docker_networks_default: []
        ```

    ??? variable list "`komga_role_docker_networks_custom`"

        ```yaml
        # Type: list
        komga_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`komga_role_docker_restart_policy`"

        ```yaml
        # Type: string
        komga_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`komga_role_docker_state`"

        ```yaml
        # Type: string
        komga_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`komga_role_docker_user`"

        ```yaml
        # Type: string
        komga_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`komga_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        komga_role_docker_blkio_weight:
        ```

    ??? variable int "`komga_role_docker_cpu_period`"

        ```yaml
        # Type: int
        komga_role_docker_cpu_period:
        ```

    ??? variable int "`komga_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        komga_role_docker_cpu_quota:
        ```

    ??? variable int "`komga_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        komga_role_docker_cpu_shares:
        ```

    ??? variable string "`komga_role_docker_cpus`"

        ```yaml
        # Type: string
        komga_role_docker_cpus:
        ```

    ??? variable string "`komga_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        komga_role_docker_cpuset_cpus:
        ```

    ??? variable string "`komga_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        komga_role_docker_cpuset_mems:
        ```

    ??? variable string "`komga_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        komga_role_docker_kernel_memory:
        ```

    ??? variable string "`komga_role_docker_memory`"

        ```yaml
        # Type: string
        komga_role_docker_memory:
        ```

    ??? variable string "`komga_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        komga_role_docker_memory_reservation:
        ```

    ??? variable string "`komga_role_docker_memory_swap`"

        ```yaml
        # Type: string
        komga_role_docker_memory_swap:
        ```

    ??? variable int "`komga_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        komga_role_docker_memory_swappiness:
        ```

    ??? variable string "`komga_role_docker_shm_size`"

        ```yaml
        # Type: string
        komga_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`komga_role_docker_cap_drop`"

        ```yaml
        # Type: list
        komga_role_docker_cap_drop:
        ```

    ??? variable string "`komga_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        komga_role_docker_cgroupns_mode:
        ```

    ??? variable list "`komga_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        komga_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`komga_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        komga_role_docker_device_read_bps:
        ```

    ??? variable list "`komga_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        komga_role_docker_device_read_iops:
        ```

    ??? variable list "`komga_role_docker_device_requests`"

        ```yaml
        # Type: list
        komga_role_docker_device_requests:
        ```

    ??? variable list "`komga_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        komga_role_docker_device_write_bps:
        ```

    ??? variable list "`komga_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        komga_role_docker_device_write_iops:
        ```

    ??? variable list "`komga_role_docker_devices`"

        ```yaml
        # Type: list
        komga_role_docker_devices:
        ```

    ??? variable string "`komga_role_docker_devices_default`"

        ```yaml
        # Type: string
        komga_role_docker_devices_default:
        ```

    ??? variable list "`komga_role_docker_groups`"

        ```yaml
        # Type: list
        komga_role_docker_groups:
        ```

    ??? variable bool "`komga_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        komga_role_docker_privileged:
        ```

    ??? variable list "`komga_role_docker_security_opts`"

        ```yaml
        # Type: list
        komga_role_docker_security_opts:
        ```

    ??? variable string "`komga_role_docker_userns_mode`"

        ```yaml
        # Type: string
        komga_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`komga_role_docker_dns_opts`"

        ```yaml
        # Type: list
        komga_role_docker_dns_opts:
        ```

    ??? variable list "`komga_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        komga_role_docker_dns_search_domains:
        ```

    ??? variable list "`komga_role_docker_dns_servers`"

        ```yaml
        # Type: list
        komga_role_docker_dns_servers:
        ```

    ??? variable string "`komga_role_docker_domainname`"

        ```yaml
        # Type: string
        komga_role_docker_domainname:
        ```

    ??? variable list "`komga_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        komga_role_docker_exposed_ports:
        ```

    ??? variable dict "`komga_role_docker_hosts`"

        ```yaml
        # Type: dict
        komga_role_docker_hosts:
        ```

    ??? variable bool "`komga_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        komga_role_docker_hosts_use_common:
        ```

    ??? variable string "`komga_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        komga_role_docker_ipc_mode:
        ```

    ??? variable list "`komga_role_docker_links`"

        ```yaml
        # Type: list
        komga_role_docker_links:
        ```

    ??? variable string "`komga_role_docker_network_mode`"

        ```yaml
        # Type: string
        komga_role_docker_network_mode:
        ```

    ??? variable string "`komga_role_docker_pid_mode`"

        ```yaml
        # Type: string
        komga_role_docker_pid_mode:
        ```

    ??? variable list "`komga_role_docker_ports`"

        ```yaml
        # Type: list
        komga_role_docker_ports:
        ```

    ??? variable string "`komga_role_docker_uts`"

        ```yaml
        # Type: string
        komga_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`komga_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        komga_role_docker_keep_volumes:
        ```

    ??? variable list "`komga_role_docker_mounts`"

        ```yaml
        # Type: list
        komga_role_docker_mounts:
        ```

    ??? variable dict "`komga_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        komga_role_docker_storage_opts:
        ```

    ??? variable list "`komga_role_docker_tmpfs`"

        ```yaml
        # Type: list
        komga_role_docker_tmpfs:
        ```

    ??? variable string "`komga_role_docker_volume_driver`"

        ```yaml
        # Type: string
        komga_role_docker_volume_driver:
        ```

    ??? variable list "`komga_role_docker_volumes_from`"

        ```yaml
        # Type: list
        komga_role_docker_volumes_from:
        ```

    ??? variable bool "`komga_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        komga_role_docker_volumes_global:
        ```

    ??? variable string "`komga_role_docker_working_dir`"

        ```yaml
        # Type: string
        komga_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`komga_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        komga_role_docker_auto_remove:
        ```

    ??? variable bool "`komga_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        komga_role_docker_cleanup:
        ```

    ??? variable string "`komga_role_docker_force_kill`"

        ```yaml
        # Type: string
        komga_role_docker_force_kill:
        ```

    ??? variable dict "`komga_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        komga_role_docker_healthcheck:
        ```

    ??? variable int "`komga_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        komga_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`komga_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        komga_role_docker_init:
        ```

    ??? variable string "`komga_role_docker_kill_signal`"

        ```yaml
        # Type: string
        komga_role_docker_kill_signal:
        ```

    ??? variable string "`komga_role_docker_log_driver`"

        ```yaml
        # Type: string
        komga_role_docker_log_driver:
        ```

    ??? variable dict "`komga_role_docker_log_options`"

        ```yaml
        # Type: dict
        komga_role_docker_log_options:
        ```

    ??? variable bool "`komga_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        komga_role_docker_oom_killer:
        ```

    ??? variable int "`komga_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        komga_role_docker_oom_score_adj:
        ```

    ??? variable bool "`komga_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        komga_role_docker_output_logs:
        ```

    ??? variable bool "`komga_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        komga_role_docker_paused:
        ```

    ??? variable bool "`komga_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        komga_role_docker_recreate:
        ```

    ??? variable int "`komga_role_docker_restart_retries`"

        ```yaml
        # Type: int
        komga_role_docker_restart_retries:
        ```

    ??? variable int "`komga_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        komga_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`komga_role_docker_capabilities`"

        ```yaml
        # Type: list
        komga_role_docker_capabilities:
        ```

    ??? variable string "`komga_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        komga_role_docker_cgroup_parent:
        ```

    ??? variable list "`komga_role_docker_commands`"

        ```yaml
        # Type: list
        komga_role_docker_commands:
        ```

    ??? variable int "`komga_role_docker_create_timeout`"

        ```yaml
        # Type: int
        komga_role_docker_create_timeout:
        ```

    ??? variable string "`komga_role_docker_entrypoint`"

        ```yaml
        # Type: string
        komga_role_docker_entrypoint:
        ```

    ??? variable string "`komga_role_docker_env_file`"

        ```yaml
        # Type: string
        komga_role_docker_env_file:
        ```

    ??? variable dict "`komga_role_docker_labels`"

        ```yaml
        # Type: dict
        komga_role_docker_labels:
        ```

    ??? variable bool "`komga_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        komga_role_docker_labels_use_common:
        ```

    ??? variable bool "`komga_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        komga_role_docker_read_only:
        ```

    ??? variable string "`komga_role_docker_runtime`"

        ```yaml
        # Type: string
        komga_role_docker_runtime:
        ```

    ??? variable list "`komga_role_docker_sysctls`"

        ```yaml
        # Type: list
        komga_role_docker_sysctls:
        ```

    ??? variable list "`komga_role_docker_ulimits`"

        ```yaml
        # Type: list
        komga_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`komga_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        komga_role_autoheal_enabled: true
        ```

    ??? variable string "`komga_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        komga_role_depends_on: ""
        ```

    ??? variable string "`komga_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        komga_role_depends_on_delay: "0"
        ```

    ??? variable string "`komga_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        komga_role_depends_on_healthchecks:
        ```

    ??? variable bool "`komga_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        komga_role_diun_enabled: true
        ```

    ??? variable bool "`komga_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        komga_role_dns_enabled: true
        ```

    ??? variable bool "`komga_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        komga_role_docker_controller: true
        ```

    ??? variable list "`komga_role_docker_networks_alias_custom`"

        ```yaml
        # Type: list
        komga_role_docker_networks_alias_custom:
        ```

    ??? variable bool "`komga_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        komga_role_docker_volumes_download:
        ```

    ??? variable string "`komga_role_themepark_addons`"

        ```yaml
        # Type: string
        komga_role_themepark_addons:
        ```

    ??? variable string "`komga_role_themepark_app`"

        ```yaml
        # Type: string
        komga_role_themepark_app:
        ```

    ??? variable string "`komga_role_themepark_theme`"

        ```yaml
        # Type: string
        komga_role_themepark_theme:
        ```

    ??? variable string "`komga_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        komga_role_traefik_api_middleware:
        ```

    ??? variable string "`komga_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        komga_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`komga_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        komga_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`komga_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        komga_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`komga_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        komga_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`komga_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        komga_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`komga_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        komga_role_traefik_middleware_http:
        ```

    ??? variable bool "`komga_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        komga_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`komga_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        komga_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`komga_role_traefik_priority`"

        ```yaml
        # Type: string
        komga_role_traefik_priority:
        ```

    ??? variable bool "`komga_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        komga_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`komga_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        komga_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`komga_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        komga_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`komga_role_web_api_http_port`"

        ```yaml
        # Type: string (quoted number)
        komga_role_web_api_http_port:
        ```

    ??? variable string "`komga_role_web_api_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        komga_role_web_api_http_scheme:
        ```

    ??? variable dict "`komga_role_web_api_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        komga_role_web_api_http_serverstransport:
        ```

    ??? variable string "`komga_role_web_api_port`"

        ```yaml
        # Type: string (quoted number)
        komga_role_web_api_port:
        ```

    ??? variable string "`komga_role_web_api_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        komga_role_web_api_scheme:
        ```

    ??? variable dict "`komga_role_web_api_serverstransport`"

        ```yaml
        # Type: dict/omit
        komga_role_web_api_serverstransport:
        ```

    ??? variable list "`komga_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        komga_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            komga_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "komga2.{{ user.domain }}"
              - "komga.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`komga_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        komga_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            komga_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'komga2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`komga_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        komga_role_web_http_port:
        ```

    ??? variable string "`komga_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        komga_role_web_http_scheme:
        ```

    ??? variable dict "`komga_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        komga_role_web_http_serverstransport:
        ```

    ??? variable string "`komga_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        komga_role_web_scheme:
        ```

    ??? variable dict "`komga_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        komga_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
icon: material/docker
hide:
  - tags
tags:
  - karakeep
  - media
  - music 
saltbox_automation:
  app_links:
    - name: Manual
      url: https://docs.karakeep.app
      type: documentation
    - name: Releases
      url: https://github.com/karakeep-app/karakeep/pkgs/container/karakeep
      type: github
    - name: Community
      url: https://discord.gg/NrgeYywsFh
      type: discord
  project_description:
    name: Karakeep
    summary: |
      an open source "Bookmark Everything" app that uses AI for automatically tagging the content you throw at it. The app is built with self-hosting as a first class citizen.
    link: https://karakeep.app/
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Karakeep

## Overview

[Karakeep](https://karakeep.app/) is an open source "Bookmark Everything" app that uses AI for automatically tagging the content you throw at it. The app is built with self-hosting as a first class citizen.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://docs.karakeep.app){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/karakeep-app/karakeep/pkgs/container/karakeep){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://discord.gg/NrgeYywsFh){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Configuration

Use the `sb inventory` system to set any environment variables that are desired such as OpenAI API keys, downloading videos, document size limits, etc

See [Karakeep Configuration](https://docs.karakeep.app/configuration) for supported variables

## Deployment

```shell
sb install sandbox-karakeep
```

## Usage

Visit `https://karakeep.app/`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        karakeep_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `karakeep_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `karakeep_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`karakeep_name`"

        ```yaml
        # Type: string
        karakeep_name: karakeep
        ```

=== "Container Dependant Variables"

    ??? variable string "`karakeep_meili_name`"

        ```yaml
        # Type: string
        karakeep_meili_name: "meilisearch"
        ```

    ??? variable string "`karakeep_meili_port`"

        ```yaml
        # Type: string
        karakeep_meili_port: "7700"
        ```

    ??? variable string "`karakeep_chrome_name`"

        ```yaml
        # Type: string
        karakeep_chrome_name: "chrome"
        ```

    ??? variable string "`karakeep_chrome_port`"

        ```yaml
        # Type: string
        karakeep_chrome_port: "9222"
        ```

=== "Web"

    ??? variable string "`karakeep_role_web_subdomain`"

        ```yaml
        # Type: string
        karakeep_role_web_subdomain: "{{ karakeep_name }}"
        ```

    ??? variable string "`karakeep_role_web_domain`"

        ```yaml
        # Type: string
        karakeep_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`karakeep_role_web_port`"

        ```yaml
        # Type: string
        karakeep_role_web_port: "3000"
        ```

    ??? variable string "`karakeep_role_web_url`"

        ```yaml
        # Type: string
        karakeep_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='karakeep') + '.' + lookup('role_var', '_web_domain', role='karakeep')
                                if (lookup('role_var', '_web_subdomain', role='karakeep') | length > 0)
                                else lookup('role_var', '_web_domain', role='karakeep')) }}"
        ```

=== "DNS"

    ??? variable string "`karakeep_role_dns_record`"

        ```yaml
        # Type: string
        karakeep_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='karakeep') }}"
        ```

    ??? variable string "`karakeep_role_dns_zone`"

        ```yaml
        # Type: string
        karakeep_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='karakeep') }}"
        ```

    ??? variable bool "`karakeep_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`karakeep_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        karakeep_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`karakeep_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        karakeep_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`karakeep_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        karakeep_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`karakeep_role_traefik_certresolver`"

        ```yaml
        # Type: string
        karakeep_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`karakeep_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_traefik_enabled: true
        ```

    ??? variable bool "`karakeep_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_traefik_api_enabled: false
        ```

    ??? variable string "`karakeep_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        karakeep_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`karakeep_role_docker_container`"

        ```yaml
        # Type: string
        karakeep_role_docker_container: "{{ karakeep_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`karakeep_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_docker_image_pull: true
        ```

    ??? variable string "`karakeep_role_docker_image_repo`"

        ```yaml
        # Type: string
        karakeep_role_docker_image_repo: "ghcr.io/karakeep-app/karakeep"
        ```

    ??? variable string "`karakeep_role_docker_image_tag`"

        ```yaml
        # Type: string
        karakeep_role_docker_image_tag: "release"
        ```

    ??? variable string "`karakeep_role_docker_image`"

        ```yaml
        # Type: string
        karakeep_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='karakeep') }}:{{ lookup('role_var', '_docker_image_tag', role='karakeep') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`karakeep_role_docker_envs_default`"

        ```yaml
        # Type: dict
        karakeep_role_docker_envs_default:
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          HOARDER_VERSION: "release"
          MEILI_ADDR: "{{ 'http://' + karakeep_meili_name + ':' + karakeep_meili_port }}"
          BROWSER_WEB_URL: "{{ 'http://' + karakeep_chrome_name + ':' + karakeep_chrome_port }}"
          NEXTAUTH_SECRET: "{{ karakeep_saltbox_facts.facts.secret_key }}"
          MEILI_MASTER_KEY: "{{ meilisearch_saltbox_facts.facts.secret_key }}"
          NEXTAUTH_URL: "{{ lookup('role_var', '_web_url', role='karakeep') }}"
          DATA_DIR: "/data"
        ```

    ??? variable dict "`karakeep_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        karakeep_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`karakeep_role_docker_volumes_default`"

        ```yaml
        # Type: list
        karakeep_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='karakeep') }}/data:/data"
        ```

    ??? variable list "`karakeep_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        karakeep_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`karakeep_role_docker_hostname`"

        ```yaml
        # Type: string
        karakeep_role_docker_hostname: "{{ karakeep_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`karakeep_role_docker_networks_alias`"

        ```yaml
        # Type: string
        karakeep_role_docker_networks_alias: "{{ karakeep_name }}"
        ```

    ??? variable list "`karakeep_role_docker_networks_default`"

        ```yaml
        # Type: list
        karakeep_role_docker_networks_default: []
        ```

    ??? variable list "`karakeep_role_docker_networks_custom`"

        ```yaml
        # Type: list
        karakeep_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`karakeep_role_docker_restart_policy`"

        ```yaml
        # Type: string
        karakeep_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`karakeep_role_docker_state`"

        ```yaml
        # Type: string
        karakeep_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`karakeep_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        karakeep_role_docker_blkio_weight:
        ```

    ??? variable int "`karakeep_role_docker_cpu_period`"

        ```yaml
        # Type: int
        karakeep_role_docker_cpu_period:
        ```

    ??? variable int "`karakeep_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        karakeep_role_docker_cpu_quota:
        ```

    ??? variable int "`karakeep_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        karakeep_role_docker_cpu_shares:
        ```

    ??? variable string "`karakeep_role_docker_cpus`"

        ```yaml
        # Type: string
        karakeep_role_docker_cpus:
        ```

    ??? variable string "`karakeep_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        karakeep_role_docker_cpuset_cpus:
        ```

    ??? variable string "`karakeep_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        karakeep_role_docker_cpuset_mems:
        ```

    ??? variable string "`karakeep_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        karakeep_role_docker_kernel_memory:
        ```

    ??? variable string "`karakeep_role_docker_memory`"

        ```yaml
        # Type: string
        karakeep_role_docker_memory:
        ```

    ??? variable string "`karakeep_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        karakeep_role_docker_memory_reservation:
        ```

    ??? variable string "`karakeep_role_docker_memory_swap`"

        ```yaml
        # Type: string
        karakeep_role_docker_memory_swap:
        ```

    ??? variable int "`karakeep_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        karakeep_role_docker_memory_swappiness:
        ```

    ??? variable string "`karakeep_role_docker_shm_size`"

        ```yaml
        # Type: string
        karakeep_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`karakeep_role_docker_cap_drop`"

        ```yaml
        # Type: list
        karakeep_role_docker_cap_drop:
        ```

    ??? variable string "`karakeep_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        karakeep_role_docker_cgroupns_mode:
        ```

    ??? variable list "`karakeep_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        karakeep_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`karakeep_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        karakeep_role_docker_device_read_bps:
        ```

    ??? variable list "`karakeep_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        karakeep_role_docker_device_read_iops:
        ```

    ??? variable list "`karakeep_role_docker_device_requests`"

        ```yaml
        # Type: list
        karakeep_role_docker_device_requests:
        ```

    ??? variable list "`karakeep_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        karakeep_role_docker_device_write_bps:
        ```

    ??? variable list "`karakeep_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        karakeep_role_docker_device_write_iops:
        ```

    ??? variable list "`karakeep_role_docker_devices`"

        ```yaml
        # Type: list
        karakeep_role_docker_devices:
        ```

    ??? variable string "`karakeep_role_docker_devices_default`"

        ```yaml
        # Type: string
        karakeep_role_docker_devices_default:
        ```

    ??? variable list "`karakeep_role_docker_groups`"

        ```yaml
        # Type: list
        karakeep_role_docker_groups:
        ```

    ??? variable bool "`karakeep_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_docker_privileged:
        ```

    ??? variable list "`karakeep_role_docker_security_opts`"

        ```yaml
        # Type: list
        karakeep_role_docker_security_opts:
        ```

    ??? variable string "`karakeep_role_docker_user`"

        ```yaml
        # Type: string
        karakeep_role_docker_user:
        ```

    ??? variable string "`karakeep_role_docker_userns_mode`"

        ```yaml
        # Type: string
        karakeep_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`karakeep_role_docker_dns_opts`"

        ```yaml
        # Type: list
        karakeep_role_docker_dns_opts:
        ```

    ??? variable list "`karakeep_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        karakeep_role_docker_dns_search_domains:
        ```

    ??? variable list "`karakeep_role_docker_dns_servers`"

        ```yaml
        # Type: list
        karakeep_role_docker_dns_servers:
        ```

    ??? variable string "`karakeep_role_docker_domainname`"

        ```yaml
        # Type: string
        karakeep_role_docker_domainname:
        ```

    ??? variable list "`karakeep_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        karakeep_role_docker_exposed_ports:
        ```

    ??? variable dict "`karakeep_role_docker_hosts`"

        ```yaml
        # Type: dict
        karakeep_role_docker_hosts:
        ```

    ??? variable bool "`karakeep_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_docker_hosts_use_common:
        ```

    ??? variable string "`karakeep_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        karakeep_role_docker_ipc_mode:
        ```

    ??? variable list "`karakeep_role_docker_links`"

        ```yaml
        # Type: list
        karakeep_role_docker_links:
        ```

    ??? variable string "`karakeep_role_docker_network_mode`"

        ```yaml
        # Type: string
        karakeep_role_docker_network_mode:
        ```

    ??? variable string "`karakeep_role_docker_pid_mode`"

        ```yaml
        # Type: string
        karakeep_role_docker_pid_mode:
        ```

    ??? variable list "`karakeep_role_docker_ports`"

        ```yaml
        # Type: list
        karakeep_role_docker_ports:
        ```

    ??? variable string "`karakeep_role_docker_uts`"

        ```yaml
        # Type: string
        karakeep_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`karakeep_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_docker_keep_volumes:
        ```

    ??? variable list "`karakeep_role_docker_mounts`"

        ```yaml
        # Type: list
        karakeep_role_docker_mounts:
        ```

    ??? variable dict "`karakeep_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        karakeep_role_docker_storage_opts:
        ```

    ??? variable list "`karakeep_role_docker_tmpfs`"

        ```yaml
        # Type: list
        karakeep_role_docker_tmpfs:
        ```

    ??? variable string "`karakeep_role_docker_volume_driver`"

        ```yaml
        # Type: string
        karakeep_role_docker_volume_driver:
        ```

    ??? variable list "`karakeep_role_docker_volumes_from`"

        ```yaml
        # Type: list
        karakeep_role_docker_volumes_from:
        ```

    ??? variable bool "`karakeep_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_docker_volumes_global:
        ```

    ??? variable string "`karakeep_role_docker_working_dir`"

        ```yaml
        # Type: string
        karakeep_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`karakeep_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_docker_auto_remove:
        ```

    ??? variable bool "`karakeep_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_docker_cleanup:
        ```

    ??? variable string "`karakeep_role_docker_force_kill`"

        ```yaml
        # Type: string
        karakeep_role_docker_force_kill:
        ```

    ??? variable dict "`karakeep_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        karakeep_role_docker_healthcheck:
        ```

    ??? variable int "`karakeep_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        karakeep_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`karakeep_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_docker_init:
        ```

    ??? variable string "`karakeep_role_docker_kill_signal`"

        ```yaml
        # Type: string
        karakeep_role_docker_kill_signal:
        ```

    ??? variable string "`karakeep_role_docker_log_driver`"

        ```yaml
        # Type: string
        karakeep_role_docker_log_driver:
        ```

    ??? variable dict "`karakeep_role_docker_log_options`"

        ```yaml
        # Type: dict
        karakeep_role_docker_log_options:
        ```

    ??? variable bool "`karakeep_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_docker_oom_killer:
        ```

    ??? variable int "`karakeep_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        karakeep_role_docker_oom_score_adj:
        ```

    ??? variable bool "`karakeep_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_docker_output_logs:
        ```

    ??? variable bool "`karakeep_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_docker_paused:
        ```

    ??? variable bool "`karakeep_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_docker_recreate:
        ```

    ??? variable int "`karakeep_role_docker_restart_retries`"

        ```yaml
        # Type: int
        karakeep_role_docker_restart_retries:
        ```

    ??? variable int "`karakeep_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        karakeep_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`karakeep_role_docker_capabilities`"

        ```yaml
        # Type: list
        karakeep_role_docker_capabilities:
        ```

    ??? variable string "`karakeep_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        karakeep_role_docker_cgroup_parent:
        ```

    ??? variable list "`karakeep_role_docker_commands`"

        ```yaml
        # Type: list
        karakeep_role_docker_commands:
        ```

    ??? variable int "`karakeep_role_docker_create_timeout`"

        ```yaml
        # Type: int
        karakeep_role_docker_create_timeout:
        ```

    ??? variable string "`karakeep_role_docker_entrypoint`"

        ```yaml
        # Type: string
        karakeep_role_docker_entrypoint:
        ```

    ??? variable string "`karakeep_role_docker_env_file`"

        ```yaml
        # Type: string
        karakeep_role_docker_env_file:
        ```

    ??? variable dict "`karakeep_role_docker_labels`"

        ```yaml
        # Type: dict
        karakeep_role_docker_labels:
        ```

    ??? variable bool "`karakeep_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_docker_labels_use_common:
        ```

    ??? variable bool "`karakeep_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_docker_read_only:
        ```

    ??? variable string "`karakeep_role_docker_runtime`"

        ```yaml
        # Type: string
        karakeep_role_docker_runtime:
        ```

    ??? variable list "`karakeep_role_docker_sysctls`"

        ```yaml
        # Type: list
        karakeep_role_docker_sysctls:
        ```

    ??? variable list "`karakeep_role_docker_ulimits`"

        ```yaml
        # Type: list
        karakeep_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`karakeep_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        karakeep_role_autoheal_enabled: true
        ```

    ??? variable string "`karakeep_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        karakeep_role_depends_on: ""
        ```

    ??? variable string "`karakeep_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        karakeep_role_depends_on_delay: "0"
        ```

    ??? variable string "`karakeep_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        karakeep_role_depends_on_healthchecks:
        ```

    ??? variable bool "`karakeep_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        karakeep_role_diun_enabled: true
        ```

    ??? variable bool "`karakeep_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        karakeep_role_dns_enabled: true
        ```

    ??? variable bool "`karakeep_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        karakeep_role_docker_controller: true
        ```

    ??? variable string "`karakeep_role_docker_image_repo`"

        ```yaml
        # Type: string
        karakeep_role_docker_image_repo:
        ```

    ??? variable string "`karakeep_role_docker_image_tag`"

        ```yaml
        # Type: string
        karakeep_role_docker_image_tag:
        ```

    ??? variable bool "`karakeep_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_docker_volumes_download:
        ```

    ??? variable string "`karakeep_role_paths_location`"

        ```yaml
        # Type: string
        karakeep_role_paths_location:
        ```

    ??? variable string "`karakeep_role_themepark_addons`"

        ```yaml
        # Type: string
        karakeep_role_themepark_addons:
        ```

    ??? variable string "`karakeep_role_themepark_app`"

        ```yaml
        # Type: string
        karakeep_role_themepark_app:
        ```

    ??? variable string "`karakeep_role_themepark_theme`"

        ```yaml
        # Type: string
        karakeep_role_themepark_theme:
        ```

    ??? variable dict "`karakeep_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        karakeep_role_traefik_api_endpoint:
        ```

    ??? variable string "`karakeep_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        karakeep_role_traefik_api_middleware:
        ```

    ??? variable string "`karakeep_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        karakeep_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`karakeep_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        karakeep_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`karakeep_role_traefik_certresolver`"

        ```yaml
        # Type: string
        karakeep_role_traefik_certresolver:
        ```

    ??? variable bool "`karakeep_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        karakeep_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`karakeep_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        karakeep_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`karakeep_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        karakeep_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`karakeep_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        karakeep_role_traefik_middleware_http:
        ```

    ??? variable bool "`karakeep_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`karakeep_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`karakeep_role_traefik_priority`"

        ```yaml
        # Type: string
        karakeep_role_traefik_priority:
        ```

    ??? variable bool "`karakeep_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        karakeep_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`karakeep_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        karakeep_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`karakeep_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        karakeep_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`karakeep_role_web_domain`"

        ```yaml
        # Type: string
        karakeep_role_web_domain:
        ```

    ??? variable list "`karakeep_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        karakeep_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            karakeep_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "karakeep2.{{ user.domain }}"
              - "karakeep.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`karakeep_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        karakeep_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            karakeep_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'karakeep2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`karakeep_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        karakeep_role_web_http_port:
        ```

    ??? variable string "`karakeep_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        karakeep_role_web_http_scheme:
        ```

    ??? variable dict "`karakeep_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        karakeep_role_web_http_serverstransport:
        ```

    ??? variable string "`karakeep_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        karakeep_role_web_scheme:
        ```

    ??? variable dict "`karakeep_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        karakeep_role_web_serverstransport:
        ```

    ??? variable string "`karakeep_role_web_subdomain`"

        ```yaml
        # Type: string
        karakeep_role_web_subdomain:
        ```

    ??? variable string "`karakeep_role_web_url`"

        ```yaml
        # Type: string
        karakeep_role_web_url:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
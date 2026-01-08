---
icon: material/docker
hide:
  - tags
tags:
  - factorio
  - gaming
  - server
saltbox_automation:
  disabled: false
  sections:
    inventory: true
    overview: true
  inventory:
    show_sections: []
    hide_sections: []
    example_overrides: {}
  app_links:
    - name: Manual
      url: https://wiki.factorio.com/Multiplayer
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/goofball222/factorio/tags
      type: docker
    - name: Community
      url:
      type: community
  project_description:
    name: Factorio
    summary: |
      a sandbox video game in which you build and maintain your own factories to produce basic resources.
    link: https://www.factorio.com
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Factorio

## Overview

[Factorio](https://www.factorio.com) is a sandbox video game in which you build and maintain your own factories to produce basic resources.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://wiki.factorio.com/Multiplayer){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/goofball222/factorio/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Configuration

- Set to install the latest Factorio experimental (1.1.x) build. Fix to a certain version using the [inventory system](../../saltbox/inventory/index.md).

## Deployment

```shell
sb install sandbox-factorio
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        factorio_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `factorio_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `factorio_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`factorio_name`"

        ```yaml
        # Type: string
        factorio_name: factorio
        ```

=== "Web"

    ??? variable string "`factorio_role_web_subdomain`"

        ```yaml
        # Type: string
        factorio_role_web_subdomain: "{{ factorio_name }}"
        ```

    ??? variable string "`factorio_role_web_domain`"

        ```yaml
        # Type: string
        factorio_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`factorio_role_web_port`"

        ```yaml
        # Type: string
        factorio_role_web_port: ""
        ```

=== "DNS"

    ??? variable string "`factorio_role_dns_record`"

        ```yaml
        # Type: string
        factorio_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='factorio') }}"
        ```

    ??? variable string "`factorio_role_dns_zone`"

        ```yaml
        # Type: string
        factorio_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='factorio') }}"
        ```

    ??? variable bool "`factorio_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_dns_proxy: false
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`factorio_role_docker_container`"

        ```yaml
        # Type: string
        factorio_role_docker_container: "{{ factorio_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`factorio_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_docker_image_pull: true
        ```

    ??? variable string "`factorio_role_docker_image_repo`"

        ```yaml
        # Type: string
        factorio_role_docker_image_repo: "goofball222/factorio"
        ```

    ??? variable string "`factorio_role_docker_image_tag`"

        ```yaml
        # Type: string
        factorio_role_docker_image_tag: "experimental"
        ```

    ??? variable string "`factorio_role_docker_image`"

        ```yaml
        # Type: string
        factorio_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='factorio') }}:{{ lookup('role_var', '_docker_image_tag', role='factorio') }}"
        ```

    <h5>Ports</h5>

    ??? variable list "`factorio_role_docker_ports_default`"

        ```yaml
        # Type: list
        factorio_role_docker_ports_default:
          - "27015:27015/tcp"
          - "34197:34197/udp"
        ```

    ??? variable list "`factorio_role_docker_ports_custom`"

        ```yaml
        # Type: list
        factorio_role_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    ??? variable dict "`factorio_role_docker_envs_default`"

        ```yaml
        # Type: dict
        factorio_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`factorio_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        factorio_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`factorio_role_docker_volumes_default`"

        ```yaml
        # Type: list
        factorio_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='factorio') }}:/factorio"
        ```

    ??? variable list "`factorio_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        factorio_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`factorio_role_docker_hostname`"

        ```yaml
        # Type: string
        factorio_role_docker_hostname: "{{ factorio_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`factorio_role_docker_networks_alias`"

        ```yaml
        # Type: string
        factorio_role_docker_networks_alias: "{{ factorio_name }}"
        ```

    ??? variable list "`factorio_role_docker_networks_default`"

        ```yaml
        # Type: list
        factorio_role_docker_networks_default: []
        ```

    ??? variable list "`factorio_role_docker_networks_custom`"

        ```yaml
        # Type: list
        factorio_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`factorio_role_docker_restart_policy`"

        ```yaml
        # Type: string
        factorio_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`factorio_role_docker_state`"

        ```yaml
        # Type: string
        factorio_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`factorio_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        factorio_role_docker_blkio_weight:
        ```

    ??? variable int "`factorio_role_docker_cpu_period`"

        ```yaml
        # Type: int
        factorio_role_docker_cpu_period:
        ```

    ??? variable int "`factorio_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        factorio_role_docker_cpu_quota:
        ```

    ??? variable int "`factorio_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        factorio_role_docker_cpu_shares:
        ```

    ??? variable string "`factorio_role_docker_cpus`"

        ```yaml
        # Type: string
        factorio_role_docker_cpus:
        ```

    ??? variable string "`factorio_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        factorio_role_docker_cpuset_cpus:
        ```

    ??? variable string "`factorio_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        factorio_role_docker_cpuset_mems:
        ```

    ??? variable string "`factorio_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        factorio_role_docker_kernel_memory:
        ```

    ??? variable string "`factorio_role_docker_memory`"

        ```yaml
        # Type: string
        factorio_role_docker_memory:
        ```

    ??? variable string "`factorio_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        factorio_role_docker_memory_reservation:
        ```

    ??? variable string "`factorio_role_docker_memory_swap`"

        ```yaml
        # Type: string
        factorio_role_docker_memory_swap:
        ```

    ??? variable int "`factorio_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        factorio_role_docker_memory_swappiness:
        ```

    ??? variable string "`factorio_role_docker_shm_size`"

        ```yaml
        # Type: string
        factorio_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`factorio_role_docker_cap_drop`"

        ```yaml
        # Type: list
        factorio_role_docker_cap_drop:
        ```

    ??? variable string "`factorio_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        factorio_role_docker_cgroupns_mode:
        ```

    ??? variable list "`factorio_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        factorio_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`factorio_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        factorio_role_docker_device_read_bps:
        ```

    ??? variable list "`factorio_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        factorio_role_docker_device_read_iops:
        ```

    ??? variable list "`factorio_role_docker_device_requests`"

        ```yaml
        # Type: list
        factorio_role_docker_device_requests:
        ```

    ??? variable list "`factorio_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        factorio_role_docker_device_write_bps:
        ```

    ??? variable list "`factorio_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        factorio_role_docker_device_write_iops:
        ```

    ??? variable list "`factorio_role_docker_devices`"

        ```yaml
        # Type: list
        factorio_role_docker_devices:
        ```

    ??? variable string "`factorio_role_docker_devices_default`"

        ```yaml
        # Type: string
        factorio_role_docker_devices_default:
        ```

    ??? variable list "`factorio_role_docker_groups`"

        ```yaml
        # Type: list
        factorio_role_docker_groups:
        ```

    ??? variable bool "`factorio_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_docker_privileged:
        ```

    ??? variable list "`factorio_role_docker_security_opts`"

        ```yaml
        # Type: list
        factorio_role_docker_security_opts:
        ```

    ??? variable string "`factorio_role_docker_user`"

        ```yaml
        # Type: string
        factorio_role_docker_user:
        ```

    ??? variable string "`factorio_role_docker_userns_mode`"

        ```yaml
        # Type: string
        factorio_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`factorio_role_docker_dns_opts`"

        ```yaml
        # Type: list
        factorio_role_docker_dns_opts:
        ```

    ??? variable list "`factorio_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        factorio_role_docker_dns_search_domains:
        ```

    ??? variable list "`factorio_role_docker_dns_servers`"

        ```yaml
        # Type: list
        factorio_role_docker_dns_servers:
        ```

    ??? variable string "`factorio_role_docker_domainname`"

        ```yaml
        # Type: string
        factorio_role_docker_domainname:
        ```

    ??? variable list "`factorio_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        factorio_role_docker_exposed_ports:
        ```

    ??? variable dict "`factorio_role_docker_hosts`"

        ```yaml
        # Type: dict
        factorio_role_docker_hosts:
        ```

    ??? variable bool "`factorio_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_docker_hosts_use_common:
        ```

    ??? variable string "`factorio_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        factorio_role_docker_ipc_mode:
        ```

    ??? variable list "`factorio_role_docker_links`"

        ```yaml
        # Type: list
        factorio_role_docker_links:
        ```

    ??? variable string "`factorio_role_docker_network_mode`"

        ```yaml
        # Type: string
        factorio_role_docker_network_mode:
        ```

    ??? variable string "`factorio_role_docker_pid_mode`"

        ```yaml
        # Type: string
        factorio_role_docker_pid_mode:
        ```

    ??? variable string "`factorio_role_docker_uts`"

        ```yaml
        # Type: string
        factorio_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`factorio_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_docker_keep_volumes:
        ```

    ??? variable list "`factorio_role_docker_mounts`"

        ```yaml
        # Type: list
        factorio_role_docker_mounts:
        ```

    ??? variable dict "`factorio_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        factorio_role_docker_storage_opts:
        ```

    ??? variable list "`factorio_role_docker_tmpfs`"

        ```yaml
        # Type: list
        factorio_role_docker_tmpfs:
        ```

    ??? variable string "`factorio_role_docker_volume_driver`"

        ```yaml
        # Type: string
        factorio_role_docker_volume_driver:
        ```

    ??? variable list "`factorio_role_docker_volumes_from`"

        ```yaml
        # Type: list
        factorio_role_docker_volumes_from:
        ```

    ??? variable bool "`factorio_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_docker_volumes_global:
        ```

    ??? variable string "`factorio_role_docker_working_dir`"

        ```yaml
        # Type: string
        factorio_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`factorio_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_docker_auto_remove:
        ```

    ??? variable bool "`factorio_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_docker_cleanup:
        ```

    ??? variable string "`factorio_role_docker_force_kill`"

        ```yaml
        # Type: string
        factorio_role_docker_force_kill:
        ```

    ??? variable dict "`factorio_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        factorio_role_docker_healthcheck:
        ```

    ??? variable int "`factorio_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        factorio_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`factorio_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_docker_init:
        ```

    ??? variable string "`factorio_role_docker_kill_signal`"

        ```yaml
        # Type: string
        factorio_role_docker_kill_signal:
        ```

    ??? variable string "`factorio_role_docker_log_driver`"

        ```yaml
        # Type: string
        factorio_role_docker_log_driver:
        ```

    ??? variable dict "`factorio_role_docker_log_options`"

        ```yaml
        # Type: dict
        factorio_role_docker_log_options:
        ```

    ??? variable bool "`factorio_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_docker_oom_killer:
        ```

    ??? variable int "`factorio_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        factorio_role_docker_oom_score_adj:
        ```

    ??? variable bool "`factorio_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_docker_output_logs:
        ```

    ??? variable bool "`factorio_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_docker_paused:
        ```

    ??? variable bool "`factorio_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_docker_recreate:
        ```

    ??? variable int "`factorio_role_docker_restart_retries`"

        ```yaml
        # Type: int
        factorio_role_docker_restart_retries:
        ```

    ??? variable int "`factorio_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        factorio_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`factorio_role_docker_capabilities`"

        ```yaml
        # Type: list
        factorio_role_docker_capabilities:
        ```

    ??? variable string "`factorio_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        factorio_role_docker_cgroup_parent:
        ```

    ??? variable list "`factorio_role_docker_commands`"

        ```yaml
        # Type: list
        factorio_role_docker_commands:
        ```

    ??? variable int "`factorio_role_docker_create_timeout`"

        ```yaml
        # Type: int
        factorio_role_docker_create_timeout:
        ```

    ??? variable string "`factorio_role_docker_entrypoint`"

        ```yaml
        # Type: string
        factorio_role_docker_entrypoint:
        ```

    ??? variable string "`factorio_role_docker_env_file`"

        ```yaml
        # Type: string
        factorio_role_docker_env_file:
        ```

    ??? variable dict "`factorio_role_docker_labels`"

        ```yaml
        # Type: dict
        factorio_role_docker_labels:
        ```

    ??? variable bool "`factorio_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_docker_labels_use_common:
        ```

    ??? variable bool "`factorio_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_docker_read_only:
        ```

    ??? variable string "`factorio_role_docker_runtime`"

        ```yaml
        # Type: string
        factorio_role_docker_runtime:
        ```

    ??? variable list "`factorio_role_docker_sysctls`"

        ```yaml
        # Type: list
        factorio_role_docker_sysctls:
        ```

    ??? variable list "`factorio_role_docker_ulimits`"

        ```yaml
        # Type: list
        factorio_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`factorio_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        factorio_role_autoheal_enabled: true
        ```

    ??? variable string "`factorio_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        factorio_role_depends_on: ""
        ```

    ??? variable string "`factorio_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        factorio_role_depends_on_delay: "0"
        ```

    ??? variable string "`factorio_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        factorio_role_depends_on_healthchecks:
        ```

    ??? variable bool "`factorio_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        factorio_role_diun_enabled: true
        ```

    ??? variable bool "`factorio_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        factorio_role_dns_enabled: true
        ```

    ??? variable bool "`factorio_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        factorio_role_docker_controller: true
        ```

    ??? variable string "`factorio_role_docker_image_repo`"

        ```yaml
        # Type: string
        factorio_role_docker_image_repo:
        ```

    ??? variable string "`factorio_role_docker_image_tag`"

        ```yaml
        # Type: string
        factorio_role_docker_image_tag:
        ```

    ??? variable bool "`factorio_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_docker_volumes_download:
        ```

    ??? variable string "`factorio_role_paths_location`"

        ```yaml
        # Type: string
        factorio_role_paths_location:
        ```

    ??? variable string "`factorio_role_web_domain`"

        ```yaml
        # Type: string
        factorio_role_web_domain:
        ```

    ??? variable list "`factorio_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        factorio_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            factorio_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "factorio2.{{ user.domain }}"
              - "factorio.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`factorio_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        factorio_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            factorio_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'factorio2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`factorio_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        factorio_role_web_http_port:
        ```

    ??? variable string "`factorio_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        factorio_role_web_http_scheme:
        ```

    ??? variable dict "`factorio_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        factorio_role_web_http_serverstransport:
        ```

    ??? variable string "`factorio_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        factorio_role_web_scheme:
        ```

    ??? variable dict "`factorio_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        factorio_role_web_serverstransport:
        ```

    ??? variable string "`factorio_role_web_subdomain`"

        ```yaml
        # Type: string
        factorio_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
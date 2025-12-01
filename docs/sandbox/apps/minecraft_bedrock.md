---
icon: material/docker
tags:
  - Minecraft
---

# Minecraft Bedrock

## Overview

[Minecraft Bedrock](https://github.com/itzg/docker-minecraft-bedrock-server) is a server for the multi-platform version of Minecraft.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://github.com/itzg/docker-minecraft-bedrock-server){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/itzg/minecraft-bedrock-server/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-people-group:**Community**](){ .md-button .md-button--stretch }

</div>

---

!!! note
    📢 This server will expose the port UDP 19132

## Deployment

```shell
sb install sandbox-minecraft-bedrock
```

## Usage

- The server will be accessible at `minecraft-bedrock.xYOUR_DOMAIN_NAMEx` or `_yourserverip_:19132`

!!! warning "Cloudflare CDN"
    If you are using Cloudflare, you will need to disable the proxy for the subdomain(s) to work correctly. This can be done by clicking the orange cloud next to the subdomain in the DNS settings. Or specify it in the inventory using `minecraft-bedrock_dns_proxy: false` if you have the global toggle on. Otherwise you won't be able to reach the minecraft server at all.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    minecraft_bedrock_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `minecraft_bedrock_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `minecraft_bedrock_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`minecraft_bedrock_name`"

        ```yaml
        # Type: string
        minecraft_bedrock_name: minecraft-bedrock
        ```

=== "Settings"

    ??? variable string "`minecraft_bedrock_role_version`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_version: "LATEST"
        ```

=== "Paths"

    ??? variable string "`minecraft_bedrock_role_paths_folder`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_paths_folder: "{{ minecraft_bedrock_name }}"
        ```

    ??? variable string "`minecraft_bedrock_role_paths_location`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_paths_location: "{{ server_appdata_path }}/{{ minecraft_bedrock_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`minecraft_bedrock_role_web_subdomain`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_web_subdomain: "{{ minecraft_bedrock_name }}"
        ```

    ??? variable string "`minecraft_bedrock_role_web_domain`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_web_domain: "{{ user.domain }}"
        ```

=== "DNS"

    ??? variable string "`minecraft_bedrock_role_dns_record`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='minecraft_bedrock') }}"
        ```

    ??? variable string "`minecraft_bedrock_role_dns_zone`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='minecraft_bedrock') }}"
        ```

    ??? variable bool "`minecraft_bedrock_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_dns_proxy: false
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`minecraft_bedrock_role_docker_container`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_container: "{{ minecraft_bedrock_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`minecraft_bedrock_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_docker_image_pull: true
        ```

    ??? variable string "`minecraft_bedrock_role_docker_image_tag`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_image_tag: "latest"
        ```

    ??? variable string "`minecraft_bedrock_role_docker_image_repo`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_image_repo: "itzg/minecraft-bedrock-server"
        ```

    ??? variable string "`minecraft_bedrock_role_docker_image`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='minecraft_bedrock') }}:{{ lookup('role_var', '_docker_image_tag', role='minecraft_bedrock') }}"
        ```

    <h5>Ports</h5>

    ??? variable list "`minecraft_bedrock_role_docker_ports_default`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_ports_default:
          - "19132:19132/udp"
        ```

    ??? variable list "`minecraft_bedrock_role_docker_ports_custom`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    ??? variable dict "`minecraft_bedrock_role_docker_envs_default`"

        ```yaml
        # Type: dict
        minecraft_bedrock_role_docker_envs_default:
          TZ: "{{ tz }}"
          UID: "{{ uid }}"
          GID: "{{ gid }}"
          EULA: "TRUE"
          VERSION: "{{ lookup('role_var', '_version', role='minecraft_bedrock') }}"
        ```

    ??? variable dict "`minecraft_bedrock_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        minecraft_bedrock_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`minecraft_bedrock_role_docker_volumes_default`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='minecraft_bedrock') }}:/data"
        ```

    ??? variable list "`minecraft_bedrock_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`minecraft_bedrock_role_docker_hostname`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_hostname: "{{ minecraft_bedrock_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`minecraft_bedrock_role_docker_networks_alias`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_networks_alias: "{{ minecraft_bedrock_name }}"
        ```

    ??? variable list "`minecraft_bedrock_role_docker_networks_default`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_networks_default: []
        ```

    ??? variable list "`minecraft_bedrock_role_docker_networks_custom`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`minecraft_bedrock_role_docker_restart_policy`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`minecraft_bedrock_role_docker_state`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`minecraft_bedrock_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        minecraft_bedrock_role_docker_blkio_weight:
        ```

    ??? variable int "`minecraft_bedrock_role_docker_cpu_period`"

        ```yaml
        # Type: int
        minecraft_bedrock_role_docker_cpu_period:
        ```

    ??? variable int "`minecraft_bedrock_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        minecraft_bedrock_role_docker_cpu_quota:
        ```

    ??? variable int "`minecraft_bedrock_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        minecraft_bedrock_role_docker_cpu_shares:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_cpus`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_cpus:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_cpuset_cpus:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_cpuset_mems:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_kernel_memory:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_memory`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_memory:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_memory_reservation:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_memory_swap`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_memory_swap:
        ```

    ??? variable int "`minecraft_bedrock_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        minecraft_bedrock_role_docker_memory_swappiness:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_shm_size`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`minecraft_bedrock_role_docker_cap_drop`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_cap_drop:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_cgroupns_mode:
        ```

    ??? variable list "`minecraft_bedrock_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`minecraft_bedrock_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_device_read_bps:
        ```

    ??? variable list "`minecraft_bedrock_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_device_read_iops:
        ```

    ??? variable list "`minecraft_bedrock_role_docker_device_requests`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_device_requests:
        ```

    ??? variable list "`minecraft_bedrock_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_device_write_bps:
        ```

    ??? variable list "`minecraft_bedrock_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_device_write_iops:
        ```

    ??? variable list "`minecraft_bedrock_role_docker_devices`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_devices:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_devices_default`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_devices_default:
        ```

    ??? variable list "`minecraft_bedrock_role_docker_groups`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_groups:
        ```

    ??? variable bool "`minecraft_bedrock_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_docker_privileged:
        ```

    ??? variable list "`minecraft_bedrock_role_docker_security_opts`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_security_opts:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_user`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_user:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_userns_mode`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`minecraft_bedrock_role_docker_dns_opts`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_dns_opts:
        ```

    ??? variable list "`minecraft_bedrock_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_dns_search_domains:
        ```

    ??? variable list "`minecraft_bedrock_role_docker_dns_servers`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_dns_servers:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_domainname`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_domainname:
        ```

    ??? variable list "`minecraft_bedrock_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_exposed_ports:
        ```

    ??? variable dict "`minecraft_bedrock_role_docker_hosts`"

        ```yaml
        # Type: dict
        minecraft_bedrock_role_docker_hosts:
        ```

    ??? variable bool "`minecraft_bedrock_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_docker_hosts_use_common:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_ipc_mode:
        ```

    ??? variable list "`minecraft_bedrock_role_docker_links`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_links:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_network_mode`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_network_mode:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_pid_mode`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_pid_mode:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_uts`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`minecraft_bedrock_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_docker_keep_volumes:
        ```

    ??? variable list "`minecraft_bedrock_role_docker_mounts`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_mounts:
        ```

    ??? variable dict "`minecraft_bedrock_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        minecraft_bedrock_role_docker_storage_opts:
        ```

    ??? variable list "`minecraft_bedrock_role_docker_tmpfs`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_tmpfs:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_volume_driver`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_volume_driver:
        ```

    ??? variable list "`minecraft_bedrock_role_docker_volumes_from`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_volumes_from:
        ```

    ??? variable bool "`minecraft_bedrock_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_docker_volumes_global:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_working_dir`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`minecraft_bedrock_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_docker_auto_remove:
        ```

    ??? variable bool "`minecraft_bedrock_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_docker_cleanup:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_force_kill`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_force_kill:
        ```

    ??? variable dict "`minecraft_bedrock_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        minecraft_bedrock_role_docker_healthcheck:
        ```

    ??? variable int "`minecraft_bedrock_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        minecraft_bedrock_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`minecraft_bedrock_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_docker_init:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_kill_signal`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_kill_signal:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_log_driver`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_log_driver:
        ```

    ??? variable dict "`minecraft_bedrock_role_docker_log_options`"

        ```yaml
        # Type: dict
        minecraft_bedrock_role_docker_log_options:
        ```

    ??? variable bool "`minecraft_bedrock_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_docker_oom_killer:
        ```

    ??? variable int "`minecraft_bedrock_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        minecraft_bedrock_role_docker_oom_score_adj:
        ```

    ??? variable bool "`minecraft_bedrock_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_docker_output_logs:
        ```

    ??? variable bool "`minecraft_bedrock_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_docker_paused:
        ```

    ??? variable bool "`minecraft_bedrock_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_docker_recreate:
        ```

    ??? variable int "`minecraft_bedrock_role_docker_restart_retries`"

        ```yaml
        # Type: int
        minecraft_bedrock_role_docker_restart_retries:
        ```

    ??? variable int "`minecraft_bedrock_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        minecraft_bedrock_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`minecraft_bedrock_role_docker_capabilities`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_capabilities:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_cgroup_parent:
        ```

    ??? variable list "`minecraft_bedrock_role_docker_commands`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_commands:
        ```

    ??? variable int "`minecraft_bedrock_role_docker_create_timeout`"

        ```yaml
        # Type: int
        minecraft_bedrock_role_docker_create_timeout:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_entrypoint`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_entrypoint:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_env_file`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_env_file:
        ```

    ??? variable dict "`minecraft_bedrock_role_docker_labels`"

        ```yaml
        # Type: dict
        minecraft_bedrock_role_docker_labels:
        ```

    ??? variable bool "`minecraft_bedrock_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_docker_labels_use_common:
        ```

    ??? variable bool "`minecraft_bedrock_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_docker_read_only:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_runtime`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_runtime:
        ```

    ??? variable list "`minecraft_bedrock_role_docker_sysctls`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_sysctls:
        ```

    ??? variable list "`minecraft_bedrock_role_docker_ulimits`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`minecraft_bedrock_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        minecraft_bedrock_role_autoheal_enabled: true
        ```

    ??? variable string "`minecraft_bedrock_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        minecraft_bedrock_role_depends_on: ""
        ```

    ??? variable string "`minecraft_bedrock_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        minecraft_bedrock_role_depends_on_delay: "0"
        ```

    ??? variable string "`minecraft_bedrock_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        minecraft_bedrock_role_depends_on_healthchecks:
        ```

    ??? variable bool "`minecraft_bedrock_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        minecraft_bedrock_role_diun_enabled: true
        ```

    ??? variable bool "`minecraft_bedrock_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        minecraft_bedrock_role_dns_enabled: true
        ```

    ??? variable bool "`minecraft_bedrock_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        minecraft_bedrock_role_docker_controller: true
        ```

    ??? variable string "`minecraft_bedrock_role_docker_image_repo`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_image_repo:
        ```

    ??? variable string "`minecraft_bedrock_role_docker_image_tag`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_image_tag:
        ```

    ??? variable bool "`minecraft_bedrock_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_docker_volumes_download:
        ```

    ??? variable string "`minecraft_bedrock_role_paths_location`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_paths_location:
        ```

    ??? variable string "`minecraft_bedrock_role_version`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_version:
        ```

    ??? variable string "`minecraft_bedrock_role_web_domain`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_web_domain:
        ```

    ??? variable list "`minecraft_bedrock_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        minecraft_bedrock_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            minecraft_bedrock_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "minecraft_bedrock2.{{ user.domain }}"
              - "minecraft_bedrock.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`minecraft_bedrock_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        minecraft_bedrock_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            minecraft_bedrock_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'minecraft_bedrock2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`minecraft_bedrock_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        minecraft_bedrock_role_web_http_port:
        ```

    ??? variable string "`minecraft_bedrock_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        minecraft_bedrock_role_web_http_scheme:
        ```

    ??? variable dict/omit "`minecraft_bedrock_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        minecraft_bedrock_role_web_http_serverstransport:
        ```

    ??? variable string "`minecraft_bedrock_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        minecraft_bedrock_role_web_scheme:
        ```

    ??? variable dict/omit "`minecraft_bedrock_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        minecraft_bedrock_role_web_serverstransport:
        ```

    ??? variable string "`minecraft_bedrock_role_web_subdomain`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
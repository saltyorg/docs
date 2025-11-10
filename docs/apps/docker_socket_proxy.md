---
icon: material/docker
status: wip
---

# Docker Socket Proxy

## Overview

The Socket Proxy is a security-enhanced proxy designed to limit the attack surface when containers like Watchtower or Traefik need access to the Docker socket on a host system.

---

## Deployment

```sh
sb install docker-socket-proxy
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    docker_socket_proxy_role_docker_image_tag: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `docker_socket_proxy_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `docker_socket_proxy_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`docker_socket_proxy_name`"

        ```yaml
        # Type: string
        docker_socket_proxy_name: docker-socket-proxy
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`docker_socket_proxy_role_docker_container`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_container: "{{ docker_socket_proxy_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`docker_socket_proxy_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        docker_socket_proxy_role_docker_image_pull: true
        ```

    ??? variable string "`docker_socket_proxy_role_docker_image_repo`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_image_repo: "lscr.io/linuxserver/socket-proxy"
        ```

    ??? variable string "`docker_socket_proxy_role_docker_image_tag`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_image_tag: "latest"
        ```

    ??? variable string "`docker_socket_proxy_role_docker_image`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='docker_socket_proxy') }}:{{ lookup('role_var', '_docker_image_tag', role='docker_socket_proxy') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`docker_socket_proxy_role_docker_envs_default`"

        ```yaml
        # Type: dict
        docker_socket_proxy_role_docker_envs_default: 
          TZ: "{{ tz }}"
          DISABLE_IPV6: "{{ '0' if dns_ipv6_enabled else '1' }}"
        ```

    ??? variable dict "`docker_socket_proxy_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        docker_socket_proxy_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`docker_socket_proxy_role_docker_volumes_default`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_volumes_default: 
          - "/var/run/docker.sock:/var/run/docker.sock"
        ```

    ??? variable list "`docker_socket_proxy_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_volumes_custom: []
        ```

    <h5>Mounts</h5>

    ??? variable list "`docker_socket_proxy_role_docker_mounts_default`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_mounts_default: 
          - target: /run
            type: tmpfs
        ```

    ??? variable list "`docker_socket_proxy_role_docker_mounts_custom`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_mounts_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`docker_socket_proxy_role_docker_hostname`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_hostname: "{{ docker_socket_proxy_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`docker_socket_proxy_role_docker_networks_alias`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_networks_alias: "{{ docker_socket_proxy_name }}"
        ```

    ??? variable list "`docker_socket_proxy_role_docker_networks_default`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_networks_default: []
        ```

    ??? variable list "`docker_socket_proxy_role_docker_networks_custom`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`docker_socket_proxy_role_docker_restart_policy`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`docker_socket_proxy_role_docker_state`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_state: started
        ```

    <h5>Read Only Filesystem</h5>

    ??? variable bool "`docker_socket_proxy_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        docker_socket_proxy_role_docker_read_only: true
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    <h5>Resource Limits</h5>

    ??? variable int "`docker_socket_proxy_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        docker_socket_proxy_role_docker_blkio_weight:
        ```

    ??? variable int "`docker_socket_proxy_role_docker_cpu_period`"

        ```yaml
        # Type: int
        docker_socket_proxy_role_docker_cpu_period:
        ```

    ??? variable int "`docker_socket_proxy_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        docker_socket_proxy_role_docker_cpu_quota:
        ```

    ??? variable int "`docker_socket_proxy_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        docker_socket_proxy_role_docker_cpu_shares:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_cpus`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_cpus:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_cpuset_cpus:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_cpuset_mems:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_kernel_memory:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_memory`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_memory:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_memory_reservation:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_memory_swap`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_memory_swap:
        ```

    ??? variable int "`docker_socket_proxy_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        docker_socket_proxy_role_docker_memory_swappiness:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`docker_socket_proxy_role_docker_cap_drop`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_cap_drop:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_device_read_bps:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_device_read_iops:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_device_requests`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_device_requests:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_device_write_bps:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_device_write_iops:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_devices`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_devices:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_devices_default`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_devices_default:
        ```

    ??? variable bool "`docker_socket_proxy_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        docker_socket_proxy_role_docker_privileged:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_security_opts`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_security_opts:
        ```

    <h5>Networking</h5>

    ??? variable list "`docker_socket_proxy_role_docker_dns_opts`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_dns_opts:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_dns_search_domains:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_dns_servers`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_dns_servers:
        ```

    ??? variable dict "`docker_socket_proxy_role_docker_hosts`"

        ```yaml
        # Type: dict
        docker_socket_proxy_role_docker_hosts:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_hosts_use_common`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_hosts_use_common:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_network_mode`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_network_mode:
        ```

    <h5>Storage</h5>

    ??? variable bool "`docker_socket_proxy_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        docker_socket_proxy_role_docker_keep_volumes:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_volume_driver`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_volume_driver:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_volumes_from`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_volumes_from:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_volumes_global`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_volumes_global:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_working_dir`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable dict "`docker_socket_proxy_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        docker_socket_proxy_role_docker_healthcheck:
        ```

    ??? variable bool "`docker_socket_proxy_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        docker_socket_proxy_role_docker_init:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_log_driver`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_log_driver:
        ```

    ??? variable dict "`docker_socket_proxy_role_docker_log_options`"

        ```yaml
        # Type: dict
        docker_socket_proxy_role_docker_log_options:
        ```

    ??? variable bool "`docker_socket_proxy_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        docker_socket_proxy_role_docker_output_logs:
        ```

    <h5>Other Options</h5>

    ??? variable bool "`docker_socket_proxy_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        docker_socket_proxy_role_docker_auto_remove:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_capabilities`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_capabilities:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_cgroup_parent:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_cgroupns_mode:
        ```

    ??? variable bool "`docker_socket_proxy_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        docker_socket_proxy_role_docker_cleanup:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_commands`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_commands:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_create_timeout`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_create_timeout:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_domainname`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_domainname:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_entrypoint`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_entrypoint:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_env_file`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_env_file:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_exposed_ports:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_force_kill`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_force_kill:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_groups`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_groups:
        ```

    ??? variable int "`docker_socket_proxy_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        docker_socket_proxy_role_docker_healthy_wait_timeout:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_ipc_mode:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_kill_signal`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_kill_signal:
        ```

    ??? variable dict "`docker_socket_proxy_role_docker_labels`"

        ```yaml
        # Type: dict
        docker_socket_proxy_role_docker_labels:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_labels_use_common`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_labels_use_common:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_links`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_links:
        ```

    ??? variable bool "`docker_socket_proxy_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        docker_socket_proxy_role_docker_oom_killer:
        ```

    ??? variable int "`docker_socket_proxy_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        docker_socket_proxy_role_docker_oom_score_adj:
        ```

    ??? variable bool "`docker_socket_proxy_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        docker_socket_proxy_role_docker_paused:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_pid_mode`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_pid_mode:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_ports`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_ports:
        ```

    ??? variable bool "`docker_socket_proxy_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        docker_socket_proxy_role_docker_recreate:
        ```

    ??? variable int "`docker_socket_proxy_role_docker_restart_retries`"

        ```yaml
        # Type: int
        docker_socket_proxy_role_docker_restart_retries:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_runtime`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_runtime:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_shm_size`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_shm_size:
        ```

    ??? variable int "`docker_socket_proxy_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        docker_socket_proxy_role_docker_stop_timeout:
        ```

    ??? variable dict "`docker_socket_proxy_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        docker_socket_proxy_role_docker_storage_opts:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_sysctls`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_sysctls:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_tmpfs`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_tmpfs:
        ```

    ??? variable list "`docker_socket_proxy_role_docker_ulimits`"

        ```yaml
        # Type: list
        docker_socket_proxy_role_docker_ulimits:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_user`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_user:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_userns_mode`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_userns_mode:
        ```

    ??? variable string "`docker_socket_proxy_role_docker_uts`"

        ```yaml
        # Type: string
        docker_socket_proxy_role_docker_uts:
        ```

=== "Global Override Options"

    ??? variable bool "`docker_socket_proxy_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        docker_socket_proxy_role_autoheal_enabled: true
        ```

    ??? variable string "`docker_socket_proxy_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        docker_socket_proxy_role_depends_on: ""
        ```

    ??? variable string "`docker_socket_proxy_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        docker_socket_proxy_role_depends_on_delay: "0"
        ```

    ??? variable string "`docker_socket_proxy_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        docker_socket_proxy_role_depends_on_healthchecks:
        ```

    ??? variable bool "`docker_socket_proxy_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        docker_socket_proxy_role_diun_enabled: true
        ```

    ??? variable bool "`docker_socket_proxy_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        docker_socket_proxy_role_dns_enabled: true
        ```

    ??? variable bool "`docker_socket_proxy_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        docker_socket_proxy_role_docker_controller: true
        ```

    ??? variable bool "`docker_socket_proxy_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        docker_socket_proxy_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`docker_socket_proxy_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        docker_socket_proxy_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`docker_socket_proxy_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        docker_socket_proxy_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`docker_socket_proxy_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        docker_socket_proxy_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`docker_socket_proxy_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        docker_socket_proxy_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`docker_socket_proxy_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        docker_socket_proxy_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`docker_socket_proxy_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        docker_socket_proxy_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`docker_socket_proxy_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        docker_socket_proxy_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`docker_socket_proxy_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        docker_socket_proxy_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`docker_socket_proxy_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        docker_socket_proxy_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            docker_socket_proxy_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "docker_socket_proxy2.{{ user.domain }}"
              - "docker_socket_proxy.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`docker_socket_proxy_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        docker_socket_proxy_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            docker_socket_proxy_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'docker_socket_proxy2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`docker_socket_proxy_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        docker_socket_proxy_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
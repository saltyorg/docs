---
hide:
  - tags
tags:
  - autoheal
  - docker
  - monitoring
---

# Autoheal

## What is it?

[Autoheal](https://github.com/willfarrell/docker-autoheal) monitors and restarts unhealthy Docker containers. It watches for containers that have a `HEALTHCHECK` defined and automatically restarts them when they become unhealthy, helping maintain service availability without manual intervention.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/willfarrell/docker-autoheal){: .header-icons } | [:octicons-link-16: Docs](https://github.com/willfarrell/docker-autoheal#readme){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/willfarrell/docker-autoheal){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/willfarrell/autoheal){: .header-icons }|

### 1. Installation

``` shell

sb install autoheal

```

### 2. Setup

Autoheal works automatically by monitoring Docker containers with health checks. All Saltbox-deployed containers are configured with the appropriate `autoheal` label, so no additional configuration is required after installation.

You can view Autoheal's activity in the container logs:

``` shell
docker logs autoheal
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    autoheal_role_docker_image_tag: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `autoheal_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `autoheal_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`autoheal_name`"

        ```yaml
        # Type: string
        autoheal_name: autoheal
        ```

=== "Docker"

    Container
    { .sb-h5 }

    ??? variable string "`autoheal_role_docker_container`"

        ```yaml
        # Type: string
        autoheal_role_docker_container: "{{ autoheal_name }}"
        ```

    Image
    { .sb-h5 }

    ??? variable bool "`autoheal_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_image_pull: true
        ```

    ??? variable string "`autoheal_role_docker_image_tag`"

        ```yaml
        # Type: string
        autoheal_role_docker_image_tag: "latest"
        ```

    ??? variable string "`autoheal_role_docker_image`"

        ```yaml
        # Type: string
        autoheal_role_docker_image: "willfarrell/autoheal:{{ autoheal_role_docker_image_tag }}"
        ```

    Envs
    { .sb-h5 }

    ??? variable dict "`autoheal_role_docker_envs_default`"

        ```yaml
        # Type: dict
        autoheal_role_docker_envs_default: 
          AUTOHEAL_CONTAINER_LABEL: "autoheal"
        ```

    ??? variable dict "`autoheal_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        autoheal_role_docker_envs_custom: {}
        ```

    Volumes
    { .sb-h5 }

    ??? variable list "`autoheal_role_docker_volumes_default`"

        ```yaml
        # Type: list
        autoheal_role_docker_volumes_default: 
          - "/var/run/docker.sock:/var/run/docker.sock"
          - "/etc/localtime:/etc/localtime:ro"
        ```

    ??? variable list "`autoheal_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        autoheal_role_docker_volumes_custom: []
        ```

    Hostname
    { .sb-h5 }

    ??? variable string "`autoheal_role_docker_hostname`"

        ```yaml
        # Type: string
        autoheal_role_docker_hostname: "{{ autoheal_name }}"
        ```

    Networks
    { .sb-h5 }

    ??? variable string "`autoheal_role_docker_networks_alias`"

        ```yaml
        # Type: string
        autoheal_role_docker_networks_alias: "{{ autoheal_name }}"
        ```

    ??? variable list "`autoheal_role_docker_networks_default`"

        ```yaml
        # Type: list
        autoheal_role_docker_networks_default: []
        ```

    ??? variable list "`autoheal_role_docker_networks_custom`"

        ```yaml
        # Type: list
        autoheal_role_docker_networks_custom: []
        ```

    Restart Policy
    { .sb-h5 }

    ??? variable string "`autoheal_role_docker_restart_policy`"

        ```yaml
        # Type: string
        autoheal_role_docker_restart_policy: unless-stopped
        ```

    State
    { .sb-h5 }

    ??? variable string "`autoheal_role_docker_state`"

        ```yaml
        # Type: string
        autoheal_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    Resource Limits
    { .sb-h5 }

    ??? variable int "`autoheal_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        autoheal_role_docker_blkio_weight:
        ```

    ??? variable int "`autoheal_role_docker_cpu_period`"

        ```yaml
        # Type: int
        autoheal_role_docker_cpu_period:
        ```

    ??? variable int "`autoheal_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        autoheal_role_docker_cpu_quota:
        ```

    ??? variable int "`autoheal_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        autoheal_role_docker_cpu_shares:
        ```

    ??? variable string "`autoheal_role_docker_cpus`"

        ```yaml
        # Type: string
        autoheal_role_docker_cpus:
        ```

    ??? variable string "`autoheal_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        autoheal_role_docker_cpuset_cpus:
        ```

    ??? variable string "`autoheal_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        autoheal_role_docker_cpuset_mems:
        ```

    ??? variable string "`autoheal_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        autoheal_role_docker_kernel_memory:
        ```

    ??? variable string "`autoheal_role_docker_memory`"

        ```yaml
        # Type: string
        autoheal_role_docker_memory:
        ```

    ??? variable string "`autoheal_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        autoheal_role_docker_memory_reservation:
        ```

    ??? variable string "`autoheal_role_docker_memory_swap`"

        ```yaml
        # Type: string
        autoheal_role_docker_memory_swap:
        ```

    ??? variable int "`autoheal_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        autoheal_role_docker_memory_swappiness:
        ```

    Security & Devices
    { .sb-h5 }

    ??? variable list "`autoheal_role_docker_cap_drop`"

        ```yaml
        # Type: list
        autoheal_role_docker_cap_drop:
        ```

    ??? variable list "`autoheal_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        autoheal_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`autoheal_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        autoheal_role_docker_device_read_bps:
        ```

    ??? variable list "`autoheal_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        autoheal_role_docker_device_read_iops:
        ```

    ??? variable list "`autoheal_role_docker_device_requests`"

        ```yaml
        # Type: list
        autoheal_role_docker_device_requests:
        ```

    ??? variable list "`autoheal_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        autoheal_role_docker_device_write_bps:
        ```

    ??? variable list "`autoheal_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        autoheal_role_docker_device_write_iops:
        ```

    ??? variable list "`autoheal_role_docker_devices`"

        ```yaml
        # Type: list
        autoheal_role_docker_devices:
        ```

    ??? variable string "`autoheal_role_docker_devices_default`"

        ```yaml
        # Type: string
        autoheal_role_docker_devices_default:
        ```

    ??? variable bool "`autoheal_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_privileged:
        ```

    ??? variable list "`autoheal_role_docker_security_opts`"

        ```yaml
        # Type: list
        autoheal_role_docker_security_opts:
        ```

    Networking
    { .sb-h5 }

    ??? variable list "`autoheal_role_docker_dns_opts`"

        ```yaml
        # Type: list
        autoheal_role_docker_dns_opts:
        ```

    ??? variable list "`autoheal_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        autoheal_role_docker_dns_search_domains:
        ```

    ??? variable list "`autoheal_role_docker_dns_servers`"

        ```yaml
        # Type: list
        autoheal_role_docker_dns_servers:
        ```

    ??? variable dict "`autoheal_role_docker_hosts`"

        ```yaml
        # Type: dict
        autoheal_role_docker_hosts:
        ```

    ??? variable string "`autoheal_role_docker_hosts_use_common`"

        ```yaml
        # Type: string
        autoheal_role_docker_hosts_use_common:
        ```

    ??? variable string "`autoheal_role_docker_network_mode`"

        ```yaml
        # Type: string
        autoheal_role_docker_network_mode:
        ```

    Storage
    { .sb-h5 }

    ??? variable bool "`autoheal_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_keep_volumes:
        ```

    ??? variable list "`autoheal_role_docker_mounts`"

        ```yaml
        # Type: list
        autoheal_role_docker_mounts:
        ```

    ??? variable string "`autoheal_role_docker_volume_driver`"

        ```yaml
        # Type: string
        autoheal_role_docker_volume_driver:
        ```

    ??? variable list "`autoheal_role_docker_volumes_from`"

        ```yaml
        # Type: list
        autoheal_role_docker_volumes_from:
        ```

    ??? variable string "`autoheal_role_docker_volumes_global`"

        ```yaml
        # Type: string
        autoheal_role_docker_volumes_global:
        ```

    ??? variable string "`autoheal_role_docker_working_dir`"

        ```yaml
        # Type: string
        autoheal_role_docker_working_dir:
        ```

    Monitoring & Lifecycle
    { .sb-h5 }

    ??? variable dict "`autoheal_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        autoheal_role_docker_healthcheck:
        ```

    ??? variable bool "`autoheal_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_init:
        ```

    ??? variable string "`autoheal_role_docker_log_driver`"

        ```yaml
        # Type: string
        autoheal_role_docker_log_driver:
        ```

    ??? variable dict "`autoheal_role_docker_log_options`"

        ```yaml
        # Type: dict
        autoheal_role_docker_log_options:
        ```

    ??? variable bool "`autoheal_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_output_logs:
        ```

    Other Options
    { .sb-h5 }

    ??? variable bool "`autoheal_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_auto_remove:
        ```

    ??? variable list "`autoheal_role_docker_capabilities`"

        ```yaml
        # Type: list
        autoheal_role_docker_capabilities:
        ```

    ??? variable string "`autoheal_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        autoheal_role_docker_cgroup_parent:
        ```

    ??? variable string "`autoheal_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        autoheal_role_docker_cgroupns_mode:
        ```

    ??? variable bool "`autoheal_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_cleanup:
        ```

    ??? variable list "`autoheal_role_docker_commands`"

        ```yaml
        # Type: list
        autoheal_role_docker_commands:
        ```

    ??? variable string "`autoheal_role_docker_create_timeout`"

        ```yaml
        # Type: string
        autoheal_role_docker_create_timeout:
        ```

    ??? variable string "`autoheal_role_docker_domainname`"

        ```yaml
        # Type: string
        autoheal_role_docker_domainname:
        ```

    ??? variable string "`autoheal_role_docker_entrypoint`"

        ```yaml
        # Type: string
        autoheal_role_docker_entrypoint:
        ```

    ??? variable string "`autoheal_role_docker_env_file`"

        ```yaml
        # Type: string
        autoheal_role_docker_env_file:
        ```

    ??? variable list "`autoheal_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        autoheal_role_docker_exposed_ports:
        ```

    ??? variable string "`autoheal_role_docker_force_kill`"

        ```yaml
        # Type: string
        autoheal_role_docker_force_kill:
        ```

    ??? variable list "`autoheal_role_docker_groups`"

        ```yaml
        # Type: list
        autoheal_role_docker_groups:
        ```

    ??? variable int "`autoheal_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        autoheal_role_docker_healthy_wait_timeout:
        ```

    ??? variable string "`autoheal_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        autoheal_role_docker_ipc_mode:
        ```

    ??? variable string "`autoheal_role_docker_kill_signal`"

        ```yaml
        # Type: string
        autoheal_role_docker_kill_signal:
        ```

    ??? variable dict "`autoheal_role_docker_labels`"

        ```yaml
        # Type: dict
        autoheal_role_docker_labels:
        ```

    ??? variable string "`autoheal_role_docker_labels_use_common`"

        ```yaml
        # Type: string
        autoheal_role_docker_labels_use_common:
        ```

    ??? variable list "`autoheal_role_docker_links`"

        ```yaml
        # Type: list
        autoheal_role_docker_links:
        ```

    ??? variable bool "`autoheal_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_oom_killer:
        ```

    ??? variable int "`autoheal_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        autoheal_role_docker_oom_score_adj:
        ```

    ??? variable bool "`autoheal_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_paused:
        ```

    ??? variable string "`autoheal_role_docker_pid_mode`"

        ```yaml
        # Type: string
        autoheal_role_docker_pid_mode:
        ```

    ??? variable list "`autoheal_role_docker_ports`"

        ```yaml
        # Type: list
        autoheal_role_docker_ports:
        ```

    ??? variable bool "`autoheal_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_read_only:
        ```

    ??? variable bool "`autoheal_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_docker_recreate:
        ```

    ??? variable int "`autoheal_role_docker_restart_retries`"

        ```yaml
        # Type: int
        autoheal_role_docker_restart_retries:
        ```

    ??? variable string "`autoheal_role_docker_runtime`"

        ```yaml
        # Type: string
        autoheal_role_docker_runtime:
        ```

    ??? variable string "`autoheal_role_docker_shm_size`"

        ```yaml
        # Type: string
        autoheal_role_docker_shm_size:
        ```

    ??? variable int "`autoheal_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        autoheal_role_docker_stop_timeout:
        ```

    ??? variable dict "`autoheal_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        autoheal_role_docker_storage_opts:
        ```

    ??? variable list "`autoheal_role_docker_sysctls`"

        ```yaml
        # Type: list
        autoheal_role_docker_sysctls:
        ```

    ??? variable list "`autoheal_role_docker_tmpfs`"

        ```yaml
        # Type: list
        autoheal_role_docker_tmpfs:
        ```

    ??? variable list "`autoheal_role_docker_ulimits`"

        ```yaml
        # Type: list
        autoheal_role_docker_ulimits:
        ```

    ??? variable string "`autoheal_role_docker_user`"

        ```yaml
        # Type: string
        autoheal_role_docker_user:
        ```

    ??? variable string "`autoheal_role_docker_userns_mode`"

        ```yaml
        # Type: string
        autoheal_role_docker_userns_mode:
        ```

    ??? variable string "`autoheal_role_docker_uts`"

        ```yaml
        # Type: string
        autoheal_role_docker_uts:
        ```

=== "Global Override Options"

    ??? variable bool "`autoheal_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        autoheal_role_autoheal_enabled: true
        ```

    ??? variable string "`autoheal_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        autoheal_role_depends_on: ""
        ```

    ??? variable string "`autoheal_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        autoheal_role_depends_on_delay: "0"
        ```

    ??? variable string "`autoheal_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        autoheal_role_depends_on_healthchecks:
        ```

    ??? variable bool "`autoheal_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        autoheal_role_diun_enabled: true
        ```

    ??? variable bool "`autoheal_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        autoheal_role_dns_enabled: true
        ```

    ??? variable bool "`autoheal_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        autoheal_role_docker_controller: true
        ```

    ??? variable bool "`autoheal_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        autoheal_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`autoheal_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        autoheal_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`autoheal_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        autoheal_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`autoheal_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        autoheal_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`autoheal_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`autoheal_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        autoheal_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`autoheal_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        autoheal_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`autoheal_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        autoheal_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`autoheal_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        autoheal_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`autoheal_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        autoheal_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            autoheal_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "autoheal2.{{ user.domain }}"
              - "autoheal.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`autoheal_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        autoheal_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            autoheal_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'autoheal2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`autoheal_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        autoheal_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
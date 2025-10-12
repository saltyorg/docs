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

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        autoheal_role_docker_image_tag: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `autoheal_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `autoheal_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    autoheal_name: autoheal

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    autoheal_role_docker_container: "{{ autoheal_name }}"

    # Image
    # Type: bool (true/false)
    autoheal_role_docker_image_pull: true

    # Type: string
    autoheal_role_docker_image_tag: "latest"

    # Type: string
    autoheal_role_docker_image: "willfarrell/autoheal:{{ autoheal_role_docker_image_tag }}"

    # Envs
    # Type: dict
    autoheal_role_docker_envs_default: 
      AUTOHEAL_CONTAINER_LABEL: "autoheal"

    # Type: dict
    autoheal_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    autoheal_role_docker_volumes_default: 
      - "/var/run/docker.sock:/var/run/docker.sock"
      - "/etc/localtime:/etc/localtime:ro"

    # Type: list
    autoheal_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    autoheal_role_docker_hostname: "{{ autoheal_name }}"

    # Networks
    # Type: string
    autoheal_role_docker_networks_alias: "{{ autoheal_name }}"

    # Type: list
    autoheal_role_docker_networks_default: []

    # Type: list
    autoheal_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    autoheal_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    autoheal_role_docker_state: started


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    autoheal_role_docker_blkio_weight:

    # Type: int
    autoheal_role_docker_cpu_period:

    # Type: int
    autoheal_role_docker_cpu_quota:

    # Type: int
    autoheal_role_docker_cpu_shares:

    # Type: string
    autoheal_role_docker_cpus:

    # Type: string
    autoheal_role_docker_cpuset_cpus:

    # Type: string
    autoheal_role_docker_cpuset_mems:

    # Type: string
    autoheal_role_docker_kernel_memory:

    # Type: string
    autoheal_role_docker_memory:

    # Type: string
    autoheal_role_docker_memory_reservation:

    # Type: string
    autoheal_role_docker_memory_swap:

    # Type: int
    autoheal_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    autoheal_role_docker_cap_drop:

    # Type: list
    autoheal_role_docker_device_cgroup_rules:

    # Type: list
    autoheal_role_docker_device_read_bps:

    # Type: list
    autoheal_role_docker_device_read_iops:

    # Type: list
    autoheal_role_docker_device_requests:

    # Type: list
    autoheal_role_docker_device_write_bps:

    # Type: list
    autoheal_role_docker_device_write_iops:

    # Type: list
    autoheal_role_docker_devices:

    # Type: string
    autoheal_role_docker_devices_default:

    # Type: bool (true/false)
    autoheal_role_docker_privileged:

    # Type: list
    autoheal_role_docker_security_opts:


    # Networking
    # Type: list
    autoheal_role_docker_dns_opts:

    # Type: list
    autoheal_role_docker_dns_search_domains:

    # Type: list
    autoheal_role_docker_dns_servers:

    # Type: dict
    autoheal_role_docker_hosts:

    # Type: string
    autoheal_role_docker_hosts_use_common:

    # Type: string
    autoheal_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    autoheal_role_docker_keep_volumes:

    # Type: list
    autoheal_role_docker_mounts:

    # Type: string
    autoheal_role_docker_volume_driver:

    # Type: list
    autoheal_role_docker_volumes_from:

    # Type: string
    autoheal_role_docker_volumes_global:

    # Type: string
    autoheal_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    autoheal_role_docker_healthcheck:

    # Type: bool (true/false)
    autoheal_role_docker_init:

    # Type: string
    autoheal_role_docker_log_driver:

    # Type: dict
    autoheal_role_docker_log_options:

    # Type: bool (true/false)
    autoheal_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    autoheal_role_docker_auto_remove:

    # Type: list
    autoheal_role_docker_capabilities:

    # Type: string
    autoheal_role_docker_cgroup_parent:

    # Type: string
    autoheal_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    autoheal_role_docker_cleanup:

    # Type: list
    autoheal_role_docker_commands:

    # Type: string
    autoheal_role_docker_create_timeout:

    # Type: string
    autoheal_role_docker_domainname:

    # Type: string
    autoheal_role_docker_entrypoint:

    # Type: string
    autoheal_role_docker_env_file:

    # Type: list
    autoheal_role_docker_exposed_ports:

    # Type: string
    autoheal_role_docker_force_kill:

    # Type: list
    autoheal_role_docker_groups:

    # Type: int
    autoheal_role_docker_healthy_wait_timeout:

    # Type: string
    autoheal_role_docker_ipc_mode:

    # Type: string
    autoheal_role_docker_kill_signal:

    # Type: dict
    autoheal_role_docker_labels:

    # Type: string
    autoheal_role_docker_labels_use_common:

    # Type: list
    autoheal_role_docker_links:

    # Type: bool (true/false)
    autoheal_role_docker_oom_killer:

    # Type: int
    autoheal_role_docker_oom_score_adj:

    # Type: bool (true/false)
    autoheal_role_docker_paused:

    # Type: string
    autoheal_role_docker_pid_mode:

    # Type: list
    autoheal_role_docker_ports:

    # Type: bool (true/false)
    autoheal_role_docker_read_only:

    # Type: bool (true/false)
    autoheal_role_docker_recreate:

    # Type: int
    autoheal_role_docker_restart_retries:

    # Type: string
    autoheal_role_docker_runtime:

    # Type: string
    autoheal_role_docker_shm_size:

    # Type: int
    autoheal_role_docker_stop_timeout:

    # Type: dict
    autoheal_role_docker_storage_opts:

    # Type: list
    autoheal_role_docker_sysctls:

    # Type: list
    autoheal_role_docker_tmpfs:

    # Type: list
    autoheal_role_docker_ulimits:

    # Type: string
    autoheal_role_docker_user:

    # Type: string
    autoheal_role_docker_userns_mode:

    # Type: string
    autoheal_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    autoheal_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    autoheal_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    autoheal_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    autoheal_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    autoheal_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    autoheal_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    autoheal_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    autoheal_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    autoheal_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    autoheal_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    autoheal_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    autoheal_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    autoheal_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    autoheal_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    autoheal_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    autoheal_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    autoheal_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        autoheal_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "autoheal2.{{ user.domain }}"
          - "autoheal.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        autoheal_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'autoheal2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
hide:
  - tags
tags:
  - error-pages
  - traefik
  - error-handling
---

# Error Pages

## What is it?

Custom error pages that display when services return HTTP errors (400-599). Deployed automatically with Traefik.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/tarampampam/error-pages){: .header-icons } | [:octicons-link-16: Docs](https://github.com/tarampampam/error-pages){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/tarampampam/error-pages){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/tarampampam/error-pages){: .header-icons }|

## Installation

Enable in `adv_settings.yml`:

```yaml
traefik:
  error_pages: yes
```

Then install/update Traefik:

```shell
sb install traefik
```

## Configuration

### Change Template

Change the template in your [inventory](../saltbox/inventory/index.md):

```yaml
error_pages_role_template: "ghost"
```

Available templates: `l7` (default), `ghost`, `noise`, `hacker-terminal`, `shuffle`, `lost-in-space`, `app-down`, `connection`, and [more](https://github.com/tarampampam/error-pages).

Rebuild after changing:

```shell
sb install traefik
```

### Disable for Specific Apps

Disable error pages for specific apps in your [inventory](../saltbox/inventory/index.md):

```yaml
plex_role_traefik_error_pages_enabled: false
```

## Notes

- Error pages stored in `/opt/error-pages/`
- Pre-generated at install time from selected template
- Applied globally via Traefik middleware
- Manual edits overwritten on rebuild

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        error_pages_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    error_pages_name: error-pages

    ```

??? example "Config"

    ```yaml
    # Template options listed here https://github.com/tarampampam/error-pages
    # Type: string
    error_pages_role_template: "l7"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    error_pages_role_docker_container: "{{ error_pages_name }}"

    # Image
    # Type: bool (true/false)
    error_pages_role_docker_image_pull: true

    # Type: string
    error_pages_role_docker_image_repo: "tarampampam/error-pages"

    # Type: string
    error_pages_role_docker_image_tag: "latest"

    # Type: string
    error_pages_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='error_pages') }}:{{ lookup('role_var', '_docker_image_tag', role='error_pages') }}"

    # Envs
    # Type: dict
    error_pages_role_docker_envs_default: 
      TEMPLATE_NAME: "{{ lookup('role_var', '_template', role='error_pages') }}"

    # Type: dict
    error_pages_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    error_pages_role_docker_volumes_default: 
      - "/opt/error-pages:/opt/html"

    # Type: list
    error_pages_role_docker_volumes_custom: []

    # Labels
    # Type: dict
    error_pages_role_docker_labels_default: 
      traefik.enable: "true"
      traefik.http.routers.error-pages-router.rule: "PathPrefix(`/`)"
      traefik.http.routers.error-pages-router.priority: "5"
      traefik.http.routers.error-pages-router.entrypoints: "web,websecure"
      traefik.http.routers.error-pages-router.middlewares: "error-pages-middleware"
      traefik.http.middlewares.error-pages-middleware.errors.status: "400-599"
      traefik.http.middlewares.error-pages-middleware.errors.service: "error-pages-service"
      traefik.http.middlewares.error-pages-middleware.errors.query: "/{status}.html"
      traefik.http.services.error-pages-service.loadbalancer.server.port: "8080"

    # Type: dict
    error_pages_role_docker_labels_custom: {}

    # Hostname
    # Type: string
    error_pages_role_docker_hostname: "{{ error_pages_name }}"

    # Networks
    # Type: string
    error_pages_role_docker_networks_alias: "{{ error_pages_name }}"

    # Type: list
    error_pages_role_docker_networks_default: []

    # Type: list
    error_pages_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    error_pages_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    error_pages_role_docker_state: started


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    error_pages_role_docker_blkio_weight:

    # Type: int
    error_pages_role_docker_cpu_period:

    # Type: int
    error_pages_role_docker_cpu_quota:

    # Type: int
    error_pages_role_docker_cpu_shares:

    # Type: string
    error_pages_role_docker_cpus:

    # Type: string
    error_pages_role_docker_cpuset_cpus:

    # Type: string
    error_pages_role_docker_cpuset_mems:

    # Type: string
    error_pages_role_docker_kernel_memory:

    # Type: string
    error_pages_role_docker_memory:

    # Type: string
    error_pages_role_docker_memory_reservation:

    # Type: string
    error_pages_role_docker_memory_swap:

    # Type: int
    error_pages_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    error_pages_role_docker_cap_drop:

    # Type: list
    error_pages_role_docker_device_cgroup_rules:

    # Type: list
    error_pages_role_docker_device_read_bps:

    # Type: list
    error_pages_role_docker_device_read_iops:

    # Type: list
    error_pages_role_docker_device_requests:

    # Type: list
    error_pages_role_docker_device_write_bps:

    # Type: list
    error_pages_role_docker_device_write_iops:

    # Type: list
    error_pages_role_docker_devices:

    # Type: string
    error_pages_role_docker_devices_default:

    # Type: bool (true/false)
    error_pages_role_docker_privileged:

    # Type: list
    error_pages_role_docker_security_opts:


    # Networking
    # Type: list
    error_pages_role_docker_dns_opts:

    # Type: list
    error_pages_role_docker_dns_search_domains:

    # Type: list
    error_pages_role_docker_dns_servers:

    # Type: dict
    error_pages_role_docker_hosts:

    # Type: string
    error_pages_role_docker_hosts_use_common:

    # Type: string
    error_pages_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    error_pages_role_docker_keep_volumes:

    # Type: list
    error_pages_role_docker_mounts:

    # Type: string
    error_pages_role_docker_volume_driver:

    # Type: list
    error_pages_role_docker_volumes_from:

    # Type: string
    error_pages_role_docker_volumes_global:

    # Type: string
    error_pages_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    error_pages_role_docker_healthcheck:

    # Type: bool (true/false)
    error_pages_role_docker_init:

    # Type: string
    error_pages_role_docker_log_driver:

    # Type: dict
    error_pages_role_docker_log_options:

    # Type: bool (true/false)
    error_pages_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    error_pages_role_docker_auto_remove:

    # Type: list
    error_pages_role_docker_capabilities:

    # Type: string
    error_pages_role_docker_cgroup_parent:

    # Type: string
    error_pages_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    error_pages_role_docker_cleanup:

    # Type: list
    error_pages_role_docker_commands:

    # Type: string
    error_pages_role_docker_create_timeout:

    # Type: string
    error_pages_role_docker_domainname:

    # Type: string
    error_pages_role_docker_entrypoint:

    # Type: string
    error_pages_role_docker_env_file:

    # Type: list
    error_pages_role_docker_exposed_ports:

    # Type: string
    error_pages_role_docker_force_kill:

    # Type: list
    error_pages_role_docker_groups:

    # Type: int
    error_pages_role_docker_healthy_wait_timeout:

    # Type: string
    error_pages_role_docker_ipc_mode:

    # Type: string
    error_pages_role_docker_kill_signal:

    # Type: string
    error_pages_role_docker_labels_use_common:

    # Type: list
    error_pages_role_docker_links:

    # Type: bool (true/false)
    error_pages_role_docker_oom_killer:

    # Type: int
    error_pages_role_docker_oom_score_adj:

    # Type: bool (true/false)
    error_pages_role_docker_paused:

    # Type: string
    error_pages_role_docker_pid_mode:

    # Type: list
    error_pages_role_docker_ports:

    # Type: bool (true/false)
    error_pages_role_docker_read_only:

    # Type: bool (true/false)
    error_pages_role_docker_recreate:

    # Type: int
    error_pages_role_docker_restart_retries:

    # Type: string
    error_pages_role_docker_runtime:

    # Type: string
    error_pages_role_docker_shm_size:

    # Type: int
    error_pages_role_docker_stop_timeout:

    # Type: dict
    error_pages_role_docker_storage_opts:

    # Type: list
    error_pages_role_docker_sysctls:

    # Type: list
    error_pages_role_docker_tmpfs:

    # Type: list
    error_pages_role_docker_ulimits:

    # Type: string
    error_pages_role_docker_user:

    # Type: string
    error_pages_role_docker_userns_mode:

    # Type: string
    error_pages_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    error_pages_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    error_pages_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    error_pages_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    error_pages_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    error_pages_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    error_pages_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    error_pages_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    error_pages_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    error_pages_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    error_pages_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    error_pages_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    error_pages_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    error_pages_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    error_pages_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    error_pages_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    error_pages_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    error_pages_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        error_pages_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "error_pages2.{{ user.domain }}"
          - "error_pages.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        error_pages_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'error_pages2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

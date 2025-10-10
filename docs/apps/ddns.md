---
hide:
  - tags
tags:
  - ddns
  - cloudflare
  - dns
  - dynamic-dns
---

# DDNS

## What is it?

A Saltbox-specific Dynamic DNS service that automatically manages DNS records with Cloudflare based on Traefik routes. This container monitors Traefik's API for active routes and automatically creates or updates corresponding DNS records in Cloudflare, supporting both IPv4 and IPv6.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/saltyorg/saltbox){: .header-icons } | [:octicons-link-16: Docs](https://docs.saltbox.dev){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/saltyorg/saltbox){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/saltydk/dns){: .header-icons }|

### 1. Installation

``` shell

sb install ddns

```

### 2. Setup

#### Prerequisites

- Cloudflare must be enabled in your Saltbox configuration
- IPv4 or IPv6 DNS management must be enabled in `adv_settings.yml`
- Valid Cloudflare API credentials must be configured in `accounts.yml`

#### Configuration

The DDNS container automatically monitors Traefik's API endpoint for active routes and creates or updates corresponding DNS records in Cloudflare based on your configured IP version preferences.

#### Custom URLs

You can manage additional custom URLs by setting the `ddns_custom_urls` variable in your [Saltbox inventory](../saltbox/inventory/index.md):

```yaml
ddns_custom_urls: "subdomain1.domain.com,subdomain2.domain.com"
```

#### Notes

- This service only works with Cloudflare DNS
- The container requires access to Traefik's API to discover routes
- DNS records are automatically managed based on active Traefik routes

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        ddns_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    ddns_name: ddns

    ```

??? example "Settings"

    ```yaml
    # Comma separated FQDN's that you want the container to manage
    # Type: string
    ddns_role_custom_urls: ""

    # Type: string
    ddns_role_delay: "60"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    ddns_role_docker_container: "{{ ddns_name }}"

    # Image
    # Type: bool (true/false)
    ddns_role_docker_image_pull: true

    # Type: string
    ddns_role_docker_image_repo: "saltydk/dns"

    # Type: string
    ddns_role_docker_image_tag: "latest"

    # Type: string
    ddns_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='ddns') }}:{{ lookup('role_var', '_docker_image_tag', role='ddns') }}"

    # Envs
    # Type: dict
    ddns_role_docker_envs_default: 
      TZ: "{{ tz }}"
      CLOUDFLARE_API_KEY: "{{ cloudflare.api }}"
      CLOUDFLARE_EMAIL: "{{ cloudflare.email }}"
      CLOUDFLARE_PROXY_DEFAULT: "{{ dns_proxied | string }}"
      TRAEFIK_API_URL: "http://traefik:8080"
      TRAEFIK_ENTRYPOINTS: "websecure,web"
      CUSTOM_URLS: "{{ lookup('role_var', '_custom_urls', role='ddns') if (lookup('role_var', '_custom_urls', role='ddns') | length > 0) else omit }}"
      IP_VERSION: "{{ 'both' if (dns_ipv4_enabled and dns_ipv6_enabled) else ('4' if dns_ipv4_enabled else '6') }}"
      DELAY: "{{ lookup('role_var', '_delay', role='ddns') }}"

    # Type: dict
    ddns_role_docker_envs_custom: {}

    # Volumes
    # Type: bool (true/false)
    ddns_role_docker_volumes_global: false

    # Mounts
    # Type: list
    ddns_role_docker_mounts_default: 
      - target: /tmp
        type: tmpfs

    # Type: list
    ddns_role_docker_mounts_custom: []

    # Hostname
    # Type: string
    ddns_role_docker_hostname: "{{ ddns_name }}"

    # Networks
    # Type: string
    ddns_role_docker_networks_alias: "{{ ddns_name }}"

    # Type: list
    ddns_role_docker_networks_default: []

    # Type: list
    ddns_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    ddns_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    ddns_role_docker_state: started

    # Init
    # Type: bool (true/false)
    ddns_role_docker_init: true

    # Dependencies
    # Type: string
    ddns_role_depends_on: "traefik"

    # Type: string
    ddns_role_depends_on_delay: "10"

    # Type: string
    ddns_role_depends_on_healthchecks: "false"


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    ddns_role_docker_blkio_weight:

    # Type: int
    ddns_role_docker_cpu_period:

    # Type: int
    ddns_role_docker_cpu_quota:

    # Type: int
    ddns_role_docker_cpu_shares:

    # Type: string
    ddns_role_docker_cpus:

    # Type: string
    ddns_role_docker_cpuset_cpus:

    # Type: string
    ddns_role_docker_cpuset_mems:

    # Type: string
    ddns_role_docker_kernel_memory:

    # Type: string
    ddns_role_docker_memory:

    # Type: string
    ddns_role_docker_memory_reservation:

    # Type: string
    ddns_role_docker_memory_swap:

    # Type: int
    ddns_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    ddns_role_docker_cap_drop:

    # Type: list
    ddns_role_docker_device_cgroup_rules:

    # Type: list
    ddns_role_docker_device_read_bps:

    # Type: list
    ddns_role_docker_device_read_iops:

    # Type: list
    ddns_role_docker_device_requests:

    # Type: list
    ddns_role_docker_device_write_bps:

    # Type: list
    ddns_role_docker_device_write_iops:

    # Type: list
    ddns_role_docker_devices:

    # Type: string
    ddns_role_docker_devices_default:

    # Type: bool (true/false)
    ddns_role_docker_privileged:

    # Type: list
    ddns_role_docker_security_opts:


    # Networking
    # Type: list
    ddns_role_docker_dns_opts:

    # Type: list
    ddns_role_docker_dns_search_domains:

    # Type: list
    ddns_role_docker_dns_servers:

    # Type: dict
    ddns_role_docker_hosts:

    # Type: string
    ddns_role_docker_hosts_use_common:

    # Type: string
    ddns_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    ddns_role_docker_keep_volumes:

    # Type: string
    ddns_role_docker_volume_driver:

    # Type: list
    ddns_role_docker_volumes:

    # Type: list
    ddns_role_docker_volumes_from:

    # Type: string
    ddns_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    ddns_role_docker_healthcheck:

    # Type: string
    ddns_role_docker_log_driver:

    # Type: dict
    ddns_role_docker_log_options:

    # Type: bool (true/false)
    ddns_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    ddns_role_docker_auto_remove:

    # Type: list
    ddns_role_docker_capabilities:

    # Type: string
    ddns_role_docker_cgroup_parent:

    # Type: string
    ddns_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    ddns_role_docker_cleanup:

    # Type: list
    ddns_role_docker_commands:

    # Type: string
    ddns_role_docker_create_timeout:

    # Type: string
    ddns_role_docker_domainname:

    # Type: string
    ddns_role_docker_entrypoint:

    # Type: string
    ddns_role_docker_env_file:

    # Type: list
    ddns_role_docker_exposed_ports:

    # Type: string
    ddns_role_docker_force_kill:

    # Type: list
    ddns_role_docker_groups:

    # Type: int
    ddns_role_docker_healthy_wait_timeout:

    # Type: string
    ddns_role_docker_ipc_mode:

    # Type: string
    ddns_role_docker_kill_signal:

    # Type: dict
    ddns_role_docker_labels:

    # Type: string
    ddns_role_docker_labels_use_common:

    # Type: list
    ddns_role_docker_links:

    # Type: bool (true/false)
    ddns_role_docker_oom_killer:

    # Type: int
    ddns_role_docker_oom_score_adj:

    # Type: bool (true/false)
    ddns_role_docker_paused:

    # Type: string
    ddns_role_docker_pid_mode:

    # Type: list
    ddns_role_docker_ports:

    # Type: bool (true/false)
    ddns_role_docker_read_only:

    # Type: bool (true/false)
    ddns_role_docker_recreate:

    # Type: int
    ddns_role_docker_restart_retries:

    # Type: string
    ddns_role_docker_runtime:

    # Type: string
    ddns_role_docker_shm_size:

    # Type: int
    ddns_role_docker_stop_timeout:

    # Type: dict
    ddns_role_docker_storage_opts:

    # Type: list
    ddns_role_docker_sysctls:

    # Type: list
    ddns_role_docker_tmpfs:

    # Type: list
    ddns_role_docker_ulimits:

    # Type: string
    ddns_role_docker_user:

    # Type: string
    ddns_role_docker_userns_mode:

    # Type: string
    ddns_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    ddns_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    ddns_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    ddns_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    ddns_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    ddns_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    ddns_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    ddns_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    ddns_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    ddns_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    ddns_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    ddns_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    ddns_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    ddns_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    ddns_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    ddns_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    ddns_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    ddns_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        ddns_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "ddns2.{{ user.domain }}"
          - "ddns.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        ddns_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'ddns2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

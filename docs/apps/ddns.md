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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        ddns_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `ddns_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `ddns_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`ddns_name`"

        ```yaml
        # Type: string
        ddns_name: ddns
        ```

=== "Settings"

    ??? variable string "`ddns_role_custom_urls`"

        ```yaml
        # Comma separated FQDN's that you want the container to manage
        # Type: string
        ddns_role_custom_urls: ""
        ```

    ??? variable string "`ddns_role_delay`"

        ```yaml
        # Type: string
        ddns_role_delay: "60"
        ```

=== "Docker"

    ##### Container

    ??? variable string "`ddns_role_docker_container`"

        ```yaml
        # Type: string
        ddns_role_docker_container: "{{ ddns_name }}"
        ```

    ##### Image

    ??? variable bool "`ddns_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        ddns_role_docker_image_pull: true
        ```

    ??? variable string "`ddns_role_docker_image_repo`"

        ```yaml
        # Type: string
        ddns_role_docker_image_repo: "saltydk/dns"
        ```

    ??? variable string "`ddns_role_docker_image_tag`"

        ```yaml
        # Type: string
        ddns_role_docker_image_tag: "latest"
        ```

    ??? variable string "`ddns_role_docker_image`"

        ```yaml
        # Type: string
        ddns_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='ddns') }}:{{ lookup('role_var', '_docker_image_tag', role='ddns') }}"
        ```

    ##### Envs

    ??? variable dict "`ddns_role_docker_envs_default`"

        ```yaml
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
        ```

    ??? variable dict "`ddns_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        ddns_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable bool "`ddns_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        ddns_role_docker_volumes_global: false
        ```

    ##### Mounts

    ??? variable list "`ddns_role_docker_mounts_default`"

        ```yaml
        # Type: list
        ddns_role_docker_mounts_default: 
          - target: /tmp
            type: tmpfs
        ```

    ??? variable list "`ddns_role_docker_mounts_custom`"

        ```yaml
        # Type: list
        ddns_role_docker_mounts_custom: []
        ```

    ##### Hostname

    ??? variable string "`ddns_role_docker_hostname`"

        ```yaml
        # Type: string
        ddns_role_docker_hostname: "{{ ddns_name }}"
        ```

    ##### Networks

    ??? variable string "`ddns_role_docker_networks_alias`"

        ```yaml
        # Type: string
        ddns_role_docker_networks_alias: "{{ ddns_name }}"
        ```

    ??? variable list "`ddns_role_docker_networks_default`"

        ```yaml
        # Type: list
        ddns_role_docker_networks_default: []
        ```

    ??? variable list "`ddns_role_docker_networks_custom`"

        ```yaml
        # Type: list
        ddns_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`ddns_role_docker_restart_policy`"

        ```yaml
        # Type: string
        ddns_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`ddns_role_docker_state`"

        ```yaml
        # Type: string
        ddns_role_docker_state: started
        ```

    ##### Init

    ??? variable bool "`ddns_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        ddns_role_docker_init: true
        ```

    ##### Dependencies

    ??? variable string "`ddns_role_depends_on`"

        ```yaml
        # Type: string
        ddns_role_depends_on: "traefik"
        ```

    ??? variable string "`ddns_role_depends_on_delay`"

        ```yaml
        # Type: string
        ddns_role_depends_on_delay: "10"
        ```

    ??? variable string "`ddns_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        ddns_role_depends_on_healthchecks: "false"
        ```

=== "Docker+"

    #### Additional Docker Options

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    ##### Resource Limits

    ??? variable int "`ddns_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        ddns_role_docker_blkio_weight:
        ```

    ??? variable int "`ddns_role_docker_cpu_period`"

        ```yaml
        # Type: int
        ddns_role_docker_cpu_period:
        ```

    ??? variable int "`ddns_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        ddns_role_docker_cpu_quota:
        ```

    ??? variable int "`ddns_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        ddns_role_docker_cpu_shares:
        ```

    ??? variable string "`ddns_role_docker_cpus`"

        ```yaml
        # Type: string
        ddns_role_docker_cpus:
        ```

    ??? variable string "`ddns_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        ddns_role_docker_cpuset_cpus:
        ```

    ??? variable string "`ddns_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        ddns_role_docker_cpuset_mems:
        ```

    ??? variable string "`ddns_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        ddns_role_docker_kernel_memory:
        ```

    ??? variable string "`ddns_role_docker_memory`"

        ```yaml
        # Type: string
        ddns_role_docker_memory:
        ```

    ??? variable string "`ddns_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        ddns_role_docker_memory_reservation:
        ```

    ??? variable string "`ddns_role_docker_memory_swap`"

        ```yaml
        # Type: string
        ddns_role_docker_memory_swap:
        ```

    ??? variable int "`ddns_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        ddns_role_docker_memory_swappiness:
        ```

    ##### Security & Devices

    ??? variable list "`ddns_role_docker_cap_drop`"

        ```yaml
        # Type: list
        ddns_role_docker_cap_drop:
        ```

    ??? variable list "`ddns_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        ddns_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`ddns_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        ddns_role_docker_device_read_bps:
        ```

    ??? variable list "`ddns_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        ddns_role_docker_device_read_iops:
        ```

    ??? variable list "`ddns_role_docker_device_requests`"

        ```yaml
        # Type: list
        ddns_role_docker_device_requests:
        ```

    ??? variable list "`ddns_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        ddns_role_docker_device_write_bps:
        ```

    ??? variable list "`ddns_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        ddns_role_docker_device_write_iops:
        ```

    ??? variable list "`ddns_role_docker_devices`"

        ```yaml
        # Type: list
        ddns_role_docker_devices:
        ```

    ??? variable string "`ddns_role_docker_devices_default`"

        ```yaml
        # Type: string
        ddns_role_docker_devices_default:
        ```

    ??? variable bool "`ddns_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        ddns_role_docker_privileged:
        ```

    ??? variable list "`ddns_role_docker_security_opts`"

        ```yaml
        # Type: list
        ddns_role_docker_security_opts:
        ```

    ##### Networking

    ??? variable list "`ddns_role_docker_dns_opts`"

        ```yaml
        # Type: list
        ddns_role_docker_dns_opts:
        ```

    ??? variable list "`ddns_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        ddns_role_docker_dns_search_domains:
        ```

    ??? variable list "`ddns_role_docker_dns_servers`"

        ```yaml
        # Type: list
        ddns_role_docker_dns_servers:
        ```

    ??? variable dict "`ddns_role_docker_hosts`"

        ```yaml
        # Type: dict
        ddns_role_docker_hosts:
        ```

    ??? variable string "`ddns_role_docker_hosts_use_common`"

        ```yaml
        # Type: string
        ddns_role_docker_hosts_use_common:
        ```

    ??? variable string "`ddns_role_docker_network_mode`"

        ```yaml
        # Type: string
        ddns_role_docker_network_mode:
        ```

    ##### Storage

    ??? variable bool "`ddns_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        ddns_role_docker_keep_volumes:
        ```

    ??? variable string "`ddns_role_docker_volume_driver`"

        ```yaml
        # Type: string
        ddns_role_docker_volume_driver:
        ```

    ??? variable list "`ddns_role_docker_volumes`"

        ```yaml
        # Type: list
        ddns_role_docker_volumes:
        ```

    ??? variable list "`ddns_role_docker_volumes_from`"

        ```yaml
        # Type: list
        ddns_role_docker_volumes_from:
        ```

    ??? variable string "`ddns_role_docker_working_dir`"

        ```yaml
        # Type: string
        ddns_role_docker_working_dir:
        ```

    ##### Monitoring & Lifecycle

    ??? variable dict "`ddns_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        ddns_role_docker_healthcheck:
        ```

    ??? variable string "`ddns_role_docker_log_driver`"

        ```yaml
        # Type: string
        ddns_role_docker_log_driver:
        ```

    ??? variable dict "`ddns_role_docker_log_options`"

        ```yaml
        # Type: dict
        ddns_role_docker_log_options:
        ```

    ??? variable bool "`ddns_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        ddns_role_docker_output_logs:
        ```

    ##### Other Options

    ??? variable bool "`ddns_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        ddns_role_docker_auto_remove:
        ```

    ??? variable list "`ddns_role_docker_capabilities`"

        ```yaml
        # Type: list
        ddns_role_docker_capabilities:
        ```

    ??? variable string "`ddns_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        ddns_role_docker_cgroup_parent:
        ```

    ??? variable string "`ddns_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        ddns_role_docker_cgroupns_mode:
        ```

    ??? variable bool "`ddns_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        ddns_role_docker_cleanup:
        ```

    ??? variable list "`ddns_role_docker_commands`"

        ```yaml
        # Type: list
        ddns_role_docker_commands:
        ```

    ??? variable string "`ddns_role_docker_create_timeout`"

        ```yaml
        # Type: string
        ddns_role_docker_create_timeout:
        ```

    ??? variable string "`ddns_role_docker_domainname`"

        ```yaml
        # Type: string
        ddns_role_docker_domainname:
        ```

    ??? variable string "`ddns_role_docker_entrypoint`"

        ```yaml
        # Type: string
        ddns_role_docker_entrypoint:
        ```

    ??? variable string "`ddns_role_docker_env_file`"

        ```yaml
        # Type: string
        ddns_role_docker_env_file:
        ```

    ??? variable list "`ddns_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        ddns_role_docker_exposed_ports:
        ```

    ??? variable string "`ddns_role_docker_force_kill`"

        ```yaml
        # Type: string
        ddns_role_docker_force_kill:
        ```

    ??? variable list "`ddns_role_docker_groups`"

        ```yaml
        # Type: list
        ddns_role_docker_groups:
        ```

    ??? variable int "`ddns_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        ddns_role_docker_healthy_wait_timeout:
        ```

    ??? variable string "`ddns_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        ddns_role_docker_ipc_mode:
        ```

    ??? variable string "`ddns_role_docker_kill_signal`"

        ```yaml
        # Type: string
        ddns_role_docker_kill_signal:
        ```

    ??? variable dict "`ddns_role_docker_labels`"

        ```yaml
        # Type: dict
        ddns_role_docker_labels:
        ```

    ??? variable string "`ddns_role_docker_labels_use_common`"

        ```yaml
        # Type: string
        ddns_role_docker_labels_use_common:
        ```

    ??? variable list "`ddns_role_docker_links`"

        ```yaml
        # Type: list
        ddns_role_docker_links:
        ```

    ??? variable bool "`ddns_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        ddns_role_docker_oom_killer:
        ```

    ??? variable int "`ddns_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        ddns_role_docker_oom_score_adj:
        ```

    ??? variable bool "`ddns_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        ddns_role_docker_paused:
        ```

    ??? variable string "`ddns_role_docker_pid_mode`"

        ```yaml
        # Type: string
        ddns_role_docker_pid_mode:
        ```

    ??? variable list "`ddns_role_docker_ports`"

        ```yaml
        # Type: list
        ddns_role_docker_ports:
        ```

    ??? variable bool "`ddns_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        ddns_role_docker_read_only:
        ```

    ??? variable bool "`ddns_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        ddns_role_docker_recreate:
        ```

    ??? variable int "`ddns_role_docker_restart_retries`"

        ```yaml
        # Type: int
        ddns_role_docker_restart_retries:
        ```

    ??? variable string "`ddns_role_docker_runtime`"

        ```yaml
        # Type: string
        ddns_role_docker_runtime:
        ```

    ??? variable string "`ddns_role_docker_shm_size`"

        ```yaml
        # Type: string
        ddns_role_docker_shm_size:
        ```

    ??? variable int "`ddns_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        ddns_role_docker_stop_timeout:
        ```

    ??? variable dict "`ddns_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        ddns_role_docker_storage_opts:
        ```

    ??? variable list "`ddns_role_docker_sysctls`"

        ```yaml
        # Type: list
        ddns_role_docker_sysctls:
        ```

    ??? variable list "`ddns_role_docker_tmpfs`"

        ```yaml
        # Type: list
        ddns_role_docker_tmpfs:
        ```

    ??? variable list "`ddns_role_docker_ulimits`"

        ```yaml
        # Type: list
        ddns_role_docker_ulimits:
        ```

    ??? variable string "`ddns_role_docker_user`"

        ```yaml
        # Type: string
        ddns_role_docker_user:
        ```

    ??? variable string "`ddns_role_docker_userns_mode`"

        ```yaml
        # Type: string
        ddns_role_docker_userns_mode:
        ```

    ??? variable string "`ddns_role_docker_uts`"

        ```yaml
        # Type: string
        ddns_role_docker_uts:
        ```

=== "Global Override Options"

    ??? variable bool "`ddns_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        ddns_role_autoheal_enabled: true
        ```

    ??? variable string "`ddns_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        ddns_role_depends_on: ""
        ```

    ??? variable string "`ddns_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        ddns_role_depends_on_delay: "0"
        ```

    ??? variable string "`ddns_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        ddns_role_depends_on_healthchecks:
        ```

    ??? variable bool "`ddns_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        ddns_role_diun_enabled: true
        ```

    ??? variable bool "`ddns_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        ddns_role_dns_enabled: true
        ```

    ??? variable bool "`ddns_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        ddns_role_docker_controller: true
        ```

    ??? variable bool "`ddns_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        ddns_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`ddns_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        ddns_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`ddns_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        ddns_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`ddns_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        ddns_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`ddns_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        ddns_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`ddns_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        ddns_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`ddns_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        ddns_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`ddns_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        ddns_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            ddns_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "ddns2.{{ user.domain }}"
              - "ddns.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`ddns_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        ddns_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            ddns_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'ddns2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`ddns_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        ddns_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
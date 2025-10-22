---
hide:
  - tags
tags:
  - transfer
  - transfer.sh
---

# transfer.sh

## What is it?

[transfer.sh](https://transfer.sh/) is an easy and fast file sharing from the command-line or web gui app.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://transfer.sh/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/dutchcoders/transfer.sh){: .header-icons } | [:octicons-mark-github-16: Github](https://www.github.com/dutchcoders/transfer.sh){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/dutchcoders/transfer.sh){: .header-icons }|

### 1. Installation

``` shell

sb install transfer

```

### 2. URL

- To access transfer.sh, visit `https://transfer.xDOMAIN_NAMEx`

### 3. Setup

- The pre-configured username/password are taken from your Saltbox [`accounts.yml`](../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        transfer_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `transfer_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `transfer_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    transfer_name: transfer

    ```

??? example "Paths"

    ```yaml
    # Type: string
    transfer_role_uploads_location: "/tmp"

    ```

??? example "Web"

    ```yaml
    # Type: string
    transfer_role_web_subdomain: "{{ transfer_name }}"

    # Type: string
    transfer_role_web_domain: "{{ user.domain }}"

    # Type: string
    transfer_role_web_port: "8080"

    # Type: string
    transfer_role_web_user: "{{ user.name }}"

    # Type: string
    transfer_role_web_pass: "{{ user.pass }}"

    # Type: string
    transfer_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='transfer') + '.' + lookup('role_var', '_web_domain', role='transfer')
                            if (lookup('role_var', '_web_subdomain', role='transfer') | length > 0)
                            else lookup('role_var', '_web_domain', role='transfer')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    transfer_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='transfer') }}"

    # Type: string
    transfer_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='transfer') }}"

    # Type: bool (true/false)
    transfer_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    transfer_role_traefik_sso_middleware: ""

    # Type: string
    transfer_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    transfer_role_traefik_middleware_custom: ""

    # Type: string
    transfer_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    transfer_role_traefik_enabled: true

    # Type: bool (true/false)
    transfer_role_traefik_api_enabled: false

    # Type: string
    transfer_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    transfer_role_docker_container: "{{ transfer_name }}"

    # Image
    # Type: bool (true/false)
    transfer_role_docker_image_pull: true

    # Type: string
    transfer_role_docker_image_repo: "dutchcoders/transfer.sh"

    # Type: string
    transfer_role_docker_image_tag: "latest"

    # Type: string
    transfer_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='transfer') }}:{{ lookup('role_var', '_docker_image_tag', role='transfer') }}"

    # Envs
    # Type: dict
    transfer_role_docker_envs_default: 
      TZ: "{{ tz }}"
      BASEDIR: "{{ lookup('role_var', '_uploads_location', role='transfer') }}"
      PROVIDER: "local"
      HTTP_AUTH_USER: "{{ lookup('role_var', '_web_user', role='transfer') }}"
      HTTP_AUTH_PASS: "{{ lookup('role_var', '_web_pass', role='transfer') }}"

    # Type: dict
    transfer_role_docker_envs_custom: {}

    # Mounts
    # Type: list
    transfer_role_docker_mounts_default: 
      - target: /tmp
        type: tmpfs

    # Type: list
    transfer_role_docker_mounts_custom: []

    # Hostname
    # Type: string
    transfer_role_docker_hostname: "{{ transfer_name }}"

    # Networks
    # Type: string
    transfer_role_docker_networks_alias: "{{ transfer_name }}"

    # Type: list
    transfer_role_docker_networks_default: []

    # Type: list
    transfer_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    transfer_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    transfer_role_docker_state: started


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    transfer_role_docker_blkio_weight:

    # Type: int
    transfer_role_docker_cpu_period:

    # Type: int
    transfer_role_docker_cpu_quota:

    # Type: int
    transfer_role_docker_cpu_shares:

    # Type: string
    transfer_role_docker_cpus:

    # Type: string
    transfer_role_docker_cpuset_cpus:

    # Type: string
    transfer_role_docker_cpuset_mems:

    # Type: string
    transfer_role_docker_kernel_memory:

    # Type: string
    transfer_role_docker_memory:

    # Type: string
    transfer_role_docker_memory_reservation:

    # Type: string
    transfer_role_docker_memory_swap:

    # Type: int
    transfer_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    transfer_role_docker_cap_drop:

    # Type: list
    transfer_role_docker_device_cgroup_rules:

    # Type: list
    transfer_role_docker_device_read_bps:

    # Type: list
    transfer_role_docker_device_read_iops:

    # Type: list
    transfer_role_docker_device_requests:

    # Type: list
    transfer_role_docker_device_write_bps:

    # Type: list
    transfer_role_docker_device_write_iops:

    # Type: list
    transfer_role_docker_devices:

    # Type: string
    transfer_role_docker_devices_default:

    # Type: bool (true/false)
    transfer_role_docker_privileged:

    # Type: list
    transfer_role_docker_security_opts:


    # Networking
    # Type: list
    transfer_role_docker_dns_opts:

    # Type: list
    transfer_role_docker_dns_search_domains:

    # Type: list
    transfer_role_docker_dns_servers:

    # Type: dict
    transfer_role_docker_hosts:

    # Type: string
    transfer_role_docker_hosts_use_common:

    # Type: string
    transfer_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    transfer_role_docker_keep_volumes:

    # Type: string
    transfer_role_docker_volume_driver:

    # Type: list
    transfer_role_docker_volumes:

    # Type: list
    transfer_role_docker_volumes_from:

    # Type: string
    transfer_role_docker_volumes_global:

    # Type: string
    transfer_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    transfer_role_docker_healthcheck:

    # Type: bool (true/false)
    transfer_role_docker_init:

    # Type: string
    transfer_role_docker_log_driver:

    # Type: dict
    transfer_role_docker_log_options:

    # Type: bool (true/false)
    transfer_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    transfer_role_docker_auto_remove:

    # Type: list
    transfer_role_docker_capabilities:

    # Type: string
    transfer_role_docker_cgroup_parent:

    # Type: string
    transfer_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    transfer_role_docker_cleanup:

    # Type: list
    transfer_role_docker_commands:

    # Type: string
    transfer_role_docker_create_timeout:

    # Type: string
    transfer_role_docker_domainname:

    # Type: string
    transfer_role_docker_entrypoint:

    # Type: string
    transfer_role_docker_env_file:

    # Type: list
    transfer_role_docker_exposed_ports:

    # Type: string
    transfer_role_docker_force_kill:

    # Type: list
    transfer_role_docker_groups:

    # Type: int
    transfer_role_docker_healthy_wait_timeout:

    # Type: string
    transfer_role_docker_ipc_mode:

    # Type: string
    transfer_role_docker_kill_signal:

    # Type: dict
    transfer_role_docker_labels:

    # Type: string
    transfer_role_docker_labels_use_common:

    # Type: list
    transfer_role_docker_links:

    # Type: bool (true/false)
    transfer_role_docker_oom_killer:

    # Type: int
    transfer_role_docker_oom_score_adj:

    # Type: bool (true/false)
    transfer_role_docker_paused:

    # Type: string
    transfer_role_docker_pid_mode:

    # Type: list
    transfer_role_docker_ports:

    # Type: bool (true/false)
    transfer_role_docker_read_only:

    # Type: bool (true/false)
    transfer_role_docker_recreate:

    # Type: int
    transfer_role_docker_restart_retries:

    # Type: string
    transfer_role_docker_runtime:

    # Type: string
    transfer_role_docker_shm_size:

    # Type: int
    transfer_role_docker_stop_timeout:

    # Type: dict
    transfer_role_docker_storage_opts:

    # Type: list
    transfer_role_docker_sysctls:

    # Type: list
    transfer_role_docker_tmpfs:

    # Type: list
    transfer_role_docker_ulimits:

    # Type: string
    transfer_role_docker_user:

    # Type: string
    transfer_role_docker_userns_mode:

    # Type: string
    transfer_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    transfer_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    transfer_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    transfer_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    transfer_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    transfer_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    transfer_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    transfer_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    transfer_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    transfer_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    transfer_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    transfer_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    transfer_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    transfer_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    transfer_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    transfer_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    transfer_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    transfer_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        transfer_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "transfer2.{{ user.domain }}"
          - "transfer.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        transfer_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'transfer2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
hide:
  - tags
tags:
  - lldap
  - ldap
  - authentication
  - user-management
---

# LLDAP

## What is it?

LLDAP (Light LDAP) is a lightweight, simplified LDAP server for authentication. It provides a user-friendly interface for managing users and groups, with a simplified LDAP implementation that's easier to configure and maintain than traditional LDAP servers like OpenLDAP.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/lldap/lldap){: .header-icons } | [:octicons-link-16: Docs](https://github.com/lldap/lldap/blob/main/README.md){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/lldap/lldap){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/nitnelave/lldap){: .header-icons }|

### 1. Installation

``` shell

sb install lldap

```

### 2. URL

- To access LLDAP, visit `https://lldap._yourdomain.com_`

### 3. Setup

LLDAP provides a lightweight LDAP server with a user-friendly web interface for managing users and groups. The configuration file is at `/opt/lldap/lldap_config.toml`. Optional SMTP settings for password resets can be configured in your [Saltbox inventory](../saltbox/inventory/index.md) using `lldap_role_smtp_*` variables.

Applications can connect using host `lldap`, port 3890 (LDAP) or 17170 (Web UI). To reset LLDAP, run `sb install lldap-reset`.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        lldap_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    lldap_name: "lldap"

    ```

??? example "Settings"

    ```yaml
    # Toggles if the configuration template uses SMTP or not.
    # Type: bool (true/false)
    lldap_role_smtp_enabled: false

    # The SMTP server.
    # Type: string
    lldap_role_smtp_server: "smtp.gmail.com"

    # The SMTP port.
    # Type: string
    lldap_role_smtp_port: "587"

    # How the connection is encrypted, either "NONE" (no encryption), "TLS" or "STARTTLS".
    # Type: string
    lldap_role_smtp_encryption: "TLS"

    # The SMTP user, usually your email address.
    # Type: string
    lldap_role_smtp_user: "sender@gmail.com"

    # The SMTP password.
    # Type: string
    lldap_role_smtp_password: "password"

    # is a free-form name, followed by an email between <>.
    # Type: string
    lldap_role_smtp_from: "LLDAP Admin <sender@gmail.com>"

    # The header field, optional: how the sender appears in the email.
    # The first is a free-form name, followed by an email between <>.
    # Type: string
    lldap_role_smtp_reply_to: "Do not reply <noreply@localhost>"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    lldap_role_paths_folder: "{{ lldap_name }}"

    # Type: string
    lldap_role_paths_location: "{{ server_appdata_path }}/{{ lldap_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    lldap_role_web_subdomain: "lldap"

    # Type: string
    lldap_role_web_domain: "{{ user.domain }}"

    # Type: string
    lldap_role_web_port: "17170"

    # Type: string
    lldap_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='lldap') + '.' + lookup('role_var', '_web_domain', role='lldap')
                         if (lookup('role_var', '_web_subdomain', role='lldap') | length > 0)
                         else lookup('role_var', '_web_domain', role='lldap')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    lldap_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='lldap') }}"

    # Type: string
    lldap_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='lldap') }}"

    # Type: bool (true/false)
    lldap_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    lldap_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    lldap_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    lldap_role_traefik_middleware_custom: ""

    # Type: string
    lldap_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    lldap_role_traefik_enabled: true

    # Type: bool (true/false)
    lldap_role_traefik_api_enabled: false

    # Type: string
    lldap_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    lldap_role_docker_container: "{{ lldap_name }}"

    # Image
    # Type: bool (true/false)
    lldap_role_docker_image_pull: true

    # Type: string
    lldap_role_docker_image_repo: "nitnelave/lldap"

    # Type: string
    lldap_role_docker_image_tag: "stable"

    # Type: string
    lldap_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='lldap') }}:{{ lookup('role_var', '_docker_image_tag', role='lldap') }}"

    # Envs
    # Type: dict
    lldap_role_docker_envs_default: 
      TZ: "{{ tz }}"
      UID: "{{ uid }}"
      GID: "{{ gid }}"

    # Type: dict
    lldap_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    lldap_role_docker_volumes_default: 
      - "{{ lldap_role_paths_location }}:/data"

    # Type: list
    lldap_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    lldap_role_docker_hostname: "{{ lldap_name }}"

    # Networks
    # Type: string
    lldap_role_docker_networks_alias: "{{ lldap_name }}"

    # Type: list
    lldap_role_docker_networks_default: []

    # Type: list
    lldap_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    lldap_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    lldap_role_docker_state: started


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    lldap_role_docker_blkio_weight:

    # Type: int
    lldap_role_docker_cpu_period:

    # Type: int
    lldap_role_docker_cpu_quota:

    # Type: int
    lldap_role_docker_cpu_shares:

    # Type: string
    lldap_role_docker_cpus:

    # Type: string
    lldap_role_docker_cpuset_cpus:

    # Type: string
    lldap_role_docker_cpuset_mems:

    # Type: string
    lldap_role_docker_kernel_memory:

    # Type: string
    lldap_role_docker_memory:

    # Type: string
    lldap_role_docker_memory_reservation:

    # Type: string
    lldap_role_docker_memory_swap:

    # Type: int
    lldap_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    lldap_role_docker_cap_drop:

    # Type: list
    lldap_role_docker_device_cgroup_rules:

    # Type: list
    lldap_role_docker_device_read_bps:

    # Type: list
    lldap_role_docker_device_read_iops:

    # Type: list
    lldap_role_docker_device_requests:

    # Type: list
    lldap_role_docker_device_write_bps:

    # Type: list
    lldap_role_docker_device_write_iops:

    # Type: list
    lldap_role_docker_devices:

    # Type: string
    lldap_role_docker_devices_default:

    # Type: bool (true/false)
    lldap_role_docker_privileged:

    # Type: list
    lldap_role_docker_security_opts:


    # Networking
    # Type: list
    lldap_role_docker_dns_opts:

    # Type: list
    lldap_role_docker_dns_search_domains:

    # Type: list
    lldap_role_docker_dns_servers:

    # Type: dict
    lldap_role_docker_hosts:

    # Type: string
    lldap_role_docker_hosts_use_common:

    # Type: string
    lldap_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    lldap_role_docker_keep_volumes:

    # Type: list
    lldap_role_docker_mounts:

    # Type: string
    lldap_role_docker_volume_driver:

    # Type: list
    lldap_role_docker_volumes_from:

    # Type: string
    lldap_role_docker_volumes_global:

    # Type: string
    lldap_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    lldap_role_docker_healthcheck:

    # Type: bool (true/false)
    lldap_role_docker_init:

    # Type: string
    lldap_role_docker_log_driver:

    # Type: dict
    lldap_role_docker_log_options:

    # Type: bool (true/false)
    lldap_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    lldap_role_docker_auto_remove:

    # Type: list
    lldap_role_docker_capabilities:

    # Type: string
    lldap_role_docker_cgroup_parent:

    # Type: string
    lldap_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    lldap_role_docker_cleanup:

    # Type: list
    lldap_role_docker_commands:

    # Type: string
    lldap_role_docker_create_timeout:

    # Type: string
    lldap_role_docker_domainname:

    # Type: string
    lldap_role_docker_entrypoint:

    # Type: string
    lldap_role_docker_env_file:

    # Type: list
    lldap_role_docker_exposed_ports:

    # Type: string
    lldap_role_docker_force_kill:

    # Type: list
    lldap_role_docker_groups:

    # Type: int
    lldap_role_docker_healthy_wait_timeout:

    # Type: string
    lldap_role_docker_ipc_mode:

    # Type: string
    lldap_role_docker_kill_signal:

    # Type: dict
    lldap_role_docker_labels:

    # Type: string
    lldap_role_docker_labels_use_common:

    # Type: list
    lldap_role_docker_links:

    # Type: bool (true/false)
    lldap_role_docker_oom_killer:

    # Type: int
    lldap_role_docker_oom_score_adj:

    # Type: bool (true/false)
    lldap_role_docker_paused:

    # Type: string
    lldap_role_docker_pid_mode:

    # Type: list
    lldap_role_docker_ports:

    # Type: bool (true/false)
    lldap_role_docker_read_only:

    # Type: bool (true/false)
    lldap_role_docker_recreate:

    # Type: int
    lldap_role_docker_restart_retries:

    # Type: string
    lldap_role_docker_runtime:

    # Type: string
    lldap_role_docker_shm_size:

    # Type: int
    lldap_role_docker_stop_timeout:

    # Type: dict
    lldap_role_docker_storage_opts:

    # Type: list
    lldap_role_docker_sysctls:

    # Type: list
    lldap_role_docker_tmpfs:

    # Type: list
    lldap_role_docker_ulimits:

    # Type: string
    lldap_role_docker_user:

    # Type: string
    lldap_role_docker_userns_mode:

    # Type: string
    lldap_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    lldap_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    lldap_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    lldap_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    lldap_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    lldap_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    lldap_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    lldap_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    lldap_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    lldap_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    lldap_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    lldap_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    lldap_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    lldap_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    lldap_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    lldap_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    lldap_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    lldap_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        lldap_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "lldap2.{{ user.domain }}"
          - "lldap.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        lldap_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'lldap2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

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

## Overview

LLDAP (Light LDAP) is a lightweight, simplified LDAP server for authentication. It provides a user-friendly interface for managing users and groups, with a simplified LDAP implementation that's easier to configure and maintain than traditional LDAP servers like OpenLDAP.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/lldap/lldap){: .header-icons } | [:octicons-link-16: Docs](https://github.com/lldap/lldap/blob/main/README.md){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/lldap/lldap){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/nitnelave/lldap){: .header-icons }|

### 1. Installation

``` shell

sb install lldap

```

### 2. URL

- To access LLDAP, visit <https://lldap.iYOUR_DOMAIN_NAMEi>

### 3. Setup

LLDAP provides a lightweight LDAP server with a user-friendly web interface for managing users and groups. The configuration file is at `/opt/lldap/lldap_config.toml`. Optional SMTP settings for password resets can be configured in your [Saltbox inventory](../saltbox/inventory/index.md) using `lldap_role_smtp_*` variables.

Applications can connect using host `lldap`, port 3890 (LDAP) or 17170 (Web UI). To reset LLDAP, run `sb install lldap-reset`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    lldap_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `lldap_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `lldap_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`lldap_name`"

        ```yaml
        # Type: string
        lldap_name: "lldap"
        ```

=== "Settings"

    ??? variable bool "`lldap_role_smtp_enabled`"

        ```yaml
        # Toggles if the configuration template uses SMTP or not.
        # Type: bool (true/false)
        lldap_role_smtp_enabled: false
        ```

    ??? variable string "`lldap_role_smtp_server`"

        ```yaml
        # The SMTP server.
        # Type: string
        lldap_role_smtp_server: "smtp.gmail.com"
        ```

    ??? variable string "`lldap_role_smtp_port`"

        ```yaml
        # The SMTP port.
        # Type: string
        lldap_role_smtp_port: "587"
        ```

    ??? variable string "`lldap_role_smtp_encryption`"

        ```yaml
        # How the connection is encrypted, either "NONE" (no encryption), "TLS" or "STARTTLS".
        # Type: string
        lldap_role_smtp_encryption: "TLS"
        ```

    ??? variable string "`lldap_role_smtp_user`"

        ```yaml
        # The SMTP user, usually your email address.
        # Type: string
        lldap_role_smtp_user: "sender@gmail.com"
        ```

    ??? variable string "`lldap_role_smtp_password`"

        ```yaml
        # The SMTP password.
        # Type: string
        lldap_role_smtp_password: "password"
        ```

    ??? variable string "`lldap_role_smtp_from`"

        ```yaml
        # is a free-form name, followed by an email between <>.
        # Type: string
        lldap_role_smtp_from: "LLDAP Admin <sender@gmail.com>"
        ```

    ??? variable string "`lldap_role_smtp_reply_to`"

        ```yaml
        # The header field, optional: how the sender appears in the email.
        # The first is a free-form name, followed by an email between <>.
        # Type: string
        lldap_role_smtp_reply_to: "Do not reply <noreply@localhost>"
        ```

=== "Paths"

    ??? variable string "`lldap_role_paths_folder`"

        ```yaml
        # Type: string
        lldap_role_paths_folder: "{{ lldap_name }}"
        ```

    ??? variable string "`lldap_role_paths_location`"

        ```yaml
        # Type: string
        lldap_role_paths_location: "{{ server_appdata_path }}/{{ lldap_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`lldap_role_web_subdomain`"

        ```yaml
        # Type: string
        lldap_role_web_subdomain: "lldap"
        ```

    ??? variable string "`lldap_role_web_domain`"

        ```yaml
        # Type: string
        lldap_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`lldap_role_web_port`"

        ```yaml
        # Type: string
        lldap_role_web_port: "17170"
        ```

    ??? variable string "`lldap_role_web_url`"

        ```yaml
        # Type: string
        lldap_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='lldap') + '.' + lookup('role_var', '_web_domain', role='lldap')
                             if (lookup('role_var', '_web_subdomain', role='lldap') | length > 0)
                             else lookup('role_var', '_web_domain', role='lldap')) }}"
        ```

=== "DNS"

    ??? variable string "`lldap_role_dns_record`"

        ```yaml
        # Type: string
        lldap_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='lldap') }}"
        ```

    ??? variable string "`lldap_role_dns_zone`"

        ```yaml
        # Type: string
        lldap_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='lldap') }}"
        ```

    ??? variable bool "`lldap_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        lldap_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`lldap_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        lldap_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`lldap_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        lldap_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`lldap_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        lldap_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`lldap_role_traefik_certresolver`"

        ```yaml
        # Type: string
        lldap_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`lldap_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        lldap_role_traefik_enabled: true
        ```

    ??? variable bool "`lldap_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        lldap_role_traefik_api_enabled: false
        ```

    ??? variable string "`lldap_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        lldap_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`lldap_role_docker_container`"

        ```yaml
        # Type: string
        lldap_role_docker_container: "{{ lldap_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`lldap_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        lldap_role_docker_image_pull: true
        ```

    ??? variable string "`lldap_role_docker_image_repo`"

        ```yaml
        # Type: string
        lldap_role_docker_image_repo: "nitnelave/lldap"
        ```

    ??? variable string "`lldap_role_docker_image_tag`"

        ```yaml
        # Type: string
        lldap_role_docker_image_tag: "stable"
        ```

    ??? variable string "`lldap_role_docker_image`"

        ```yaml
        # Type: string
        lldap_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='lldap') }}:{{ lookup('role_var', '_docker_image_tag', role='lldap') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`lldap_role_docker_envs_default`"

        ```yaml
        # Type: dict
        lldap_role_docker_envs_default: 
          TZ: "{{ tz }}"
          UID: "{{ uid }}"
          GID: "{{ gid }}"
        ```

    ??? variable dict "`lldap_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        lldap_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`lldap_role_docker_volumes_default`"

        ```yaml
        # Type: list
        lldap_role_docker_volumes_default: 
          - "{{ lldap_role_paths_location }}:/data"
        ```

    ??? variable list "`lldap_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        lldap_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`lldap_role_docker_hostname`"

        ```yaml
        # Type: string
        lldap_role_docker_hostname: "{{ lldap_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`lldap_role_docker_networks_alias`"

        ```yaml
        # Type: string
        lldap_role_docker_networks_alias: "{{ lldap_name }}"
        ```

    ??? variable list "`lldap_role_docker_networks_default`"

        ```yaml
        # Type: list
        lldap_role_docker_networks_default: []
        ```

    ??? variable list "`lldap_role_docker_networks_custom`"

        ```yaml
        # Type: list
        lldap_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`lldap_role_docker_restart_policy`"

        ```yaml
        # Type: string
        lldap_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`lldap_role_docker_state`"

        ```yaml
        # Type: string
        lldap_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    <h5>Resource Limits</h5>

    ??? variable int "`lldap_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        lldap_role_docker_blkio_weight:
        ```

    ??? variable int "`lldap_role_docker_cpu_period`"

        ```yaml
        # Type: int
        lldap_role_docker_cpu_period:
        ```

    ??? variable int "`lldap_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        lldap_role_docker_cpu_quota:
        ```

    ??? variable int "`lldap_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        lldap_role_docker_cpu_shares:
        ```

    ??? variable string "`lldap_role_docker_cpus`"

        ```yaml
        # Type: string
        lldap_role_docker_cpus:
        ```

    ??? variable string "`lldap_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        lldap_role_docker_cpuset_cpus:
        ```

    ??? variable string "`lldap_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        lldap_role_docker_cpuset_mems:
        ```

    ??? variable string "`lldap_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        lldap_role_docker_kernel_memory:
        ```

    ??? variable string "`lldap_role_docker_memory`"

        ```yaml
        # Type: string
        lldap_role_docker_memory:
        ```

    ??? variable string "`lldap_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        lldap_role_docker_memory_reservation:
        ```

    ??? variable string "`lldap_role_docker_memory_swap`"

        ```yaml
        # Type: string
        lldap_role_docker_memory_swap:
        ```

    ??? variable int "`lldap_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        lldap_role_docker_memory_swappiness:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`lldap_role_docker_cap_drop`"

        ```yaml
        # Type: list
        lldap_role_docker_cap_drop:
        ```

    ??? variable list "`lldap_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        lldap_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`lldap_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        lldap_role_docker_device_read_bps:
        ```

    ??? variable list "`lldap_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        lldap_role_docker_device_read_iops:
        ```

    ??? variable list "`lldap_role_docker_device_requests`"

        ```yaml
        # Type: list
        lldap_role_docker_device_requests:
        ```

    ??? variable list "`lldap_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        lldap_role_docker_device_write_bps:
        ```

    ??? variable list "`lldap_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        lldap_role_docker_device_write_iops:
        ```

    ??? variable list "`lldap_role_docker_devices`"

        ```yaml
        # Type: list
        lldap_role_docker_devices:
        ```

    ??? variable string "`lldap_role_docker_devices_default`"

        ```yaml
        # Type: string
        lldap_role_docker_devices_default:
        ```

    ??? variable bool "`lldap_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        lldap_role_docker_privileged:
        ```

    ??? variable list "`lldap_role_docker_security_opts`"

        ```yaml
        # Type: list
        lldap_role_docker_security_opts:
        ```

    <h5>Networking</h5>

    ??? variable list "`lldap_role_docker_dns_opts`"

        ```yaml
        # Type: list
        lldap_role_docker_dns_opts:
        ```

    ??? variable list "`lldap_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        lldap_role_docker_dns_search_domains:
        ```

    ??? variable list "`lldap_role_docker_dns_servers`"

        ```yaml
        # Type: list
        lldap_role_docker_dns_servers:
        ```

    ??? variable dict "`lldap_role_docker_hosts`"

        ```yaml
        # Type: dict
        lldap_role_docker_hosts:
        ```

    ??? variable string "`lldap_role_docker_hosts_use_common`"

        ```yaml
        # Type: string
        lldap_role_docker_hosts_use_common:
        ```

    ??? variable string "`lldap_role_docker_network_mode`"

        ```yaml
        # Type: string
        lldap_role_docker_network_mode:
        ```

    <h5>Storage</h5>

    ??? variable bool "`lldap_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        lldap_role_docker_keep_volumes:
        ```

    ??? variable list "`lldap_role_docker_mounts`"

        ```yaml
        # Type: list
        lldap_role_docker_mounts:
        ```

    ??? variable string "`lldap_role_docker_volume_driver`"

        ```yaml
        # Type: string
        lldap_role_docker_volume_driver:
        ```

    ??? variable list "`lldap_role_docker_volumes_from`"

        ```yaml
        # Type: list
        lldap_role_docker_volumes_from:
        ```

    ??? variable string "`lldap_role_docker_volumes_global`"

        ```yaml
        # Type: string
        lldap_role_docker_volumes_global:
        ```

    ??? variable string "`lldap_role_docker_working_dir`"

        ```yaml
        # Type: string
        lldap_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable dict "`lldap_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        lldap_role_docker_healthcheck:
        ```

    ??? variable bool "`lldap_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        lldap_role_docker_init:
        ```

    ??? variable string "`lldap_role_docker_log_driver`"

        ```yaml
        # Type: string
        lldap_role_docker_log_driver:
        ```

    ??? variable dict "`lldap_role_docker_log_options`"

        ```yaml
        # Type: dict
        lldap_role_docker_log_options:
        ```

    ??? variable bool "`lldap_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        lldap_role_docker_output_logs:
        ```

    <h5>Other Options</h5>

    ??? variable bool "`lldap_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        lldap_role_docker_auto_remove:
        ```

    ??? variable list "`lldap_role_docker_capabilities`"

        ```yaml
        # Type: list
        lldap_role_docker_capabilities:
        ```

    ??? variable string "`lldap_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        lldap_role_docker_cgroup_parent:
        ```

    ??? variable string "`lldap_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        lldap_role_docker_cgroupns_mode:
        ```

    ??? variable bool "`lldap_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        lldap_role_docker_cleanup:
        ```

    ??? variable list "`lldap_role_docker_commands`"

        ```yaml
        # Type: list
        lldap_role_docker_commands:
        ```

    ??? variable string "`lldap_role_docker_create_timeout`"

        ```yaml
        # Type: string
        lldap_role_docker_create_timeout:
        ```

    ??? variable string "`lldap_role_docker_domainname`"

        ```yaml
        # Type: string
        lldap_role_docker_domainname:
        ```

    ??? variable string "`lldap_role_docker_entrypoint`"

        ```yaml
        # Type: string
        lldap_role_docker_entrypoint:
        ```

    ??? variable string "`lldap_role_docker_env_file`"

        ```yaml
        # Type: string
        lldap_role_docker_env_file:
        ```

    ??? variable list "`lldap_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        lldap_role_docker_exposed_ports:
        ```

    ??? variable string "`lldap_role_docker_force_kill`"

        ```yaml
        # Type: string
        lldap_role_docker_force_kill:
        ```

    ??? variable list "`lldap_role_docker_groups`"

        ```yaml
        # Type: list
        lldap_role_docker_groups:
        ```

    ??? variable int "`lldap_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        lldap_role_docker_healthy_wait_timeout:
        ```

    ??? variable string "`lldap_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        lldap_role_docker_ipc_mode:
        ```

    ??? variable string "`lldap_role_docker_kill_signal`"

        ```yaml
        # Type: string
        lldap_role_docker_kill_signal:
        ```

    ??? variable dict "`lldap_role_docker_labels`"

        ```yaml
        # Type: dict
        lldap_role_docker_labels:
        ```

    ??? variable string "`lldap_role_docker_labels_use_common`"

        ```yaml
        # Type: string
        lldap_role_docker_labels_use_common:
        ```

    ??? variable list "`lldap_role_docker_links`"

        ```yaml
        # Type: list
        lldap_role_docker_links:
        ```

    ??? variable bool "`lldap_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        lldap_role_docker_oom_killer:
        ```

    ??? variable int "`lldap_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        lldap_role_docker_oom_score_adj:
        ```

    ??? variable bool "`lldap_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        lldap_role_docker_paused:
        ```

    ??? variable string "`lldap_role_docker_pid_mode`"

        ```yaml
        # Type: string
        lldap_role_docker_pid_mode:
        ```

    ??? variable list "`lldap_role_docker_ports`"

        ```yaml
        # Type: list
        lldap_role_docker_ports:
        ```

    ??? variable bool "`lldap_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        lldap_role_docker_read_only:
        ```

    ??? variable bool "`lldap_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        lldap_role_docker_recreate:
        ```

    ??? variable int "`lldap_role_docker_restart_retries`"

        ```yaml
        # Type: int
        lldap_role_docker_restart_retries:
        ```

    ??? variable string "`lldap_role_docker_runtime`"

        ```yaml
        # Type: string
        lldap_role_docker_runtime:
        ```

    ??? variable string "`lldap_role_docker_shm_size`"

        ```yaml
        # Type: string
        lldap_role_docker_shm_size:
        ```

    ??? variable int "`lldap_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        lldap_role_docker_stop_timeout:
        ```

    ??? variable dict "`lldap_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        lldap_role_docker_storage_opts:
        ```

    ??? variable list "`lldap_role_docker_sysctls`"

        ```yaml
        # Type: list
        lldap_role_docker_sysctls:
        ```

    ??? variable list "`lldap_role_docker_tmpfs`"

        ```yaml
        # Type: list
        lldap_role_docker_tmpfs:
        ```

    ??? variable list "`lldap_role_docker_ulimits`"

        ```yaml
        # Type: list
        lldap_role_docker_ulimits:
        ```

    ??? variable string "`lldap_role_docker_user`"

        ```yaml
        # Type: string
        lldap_role_docker_user:
        ```

    ??? variable string "`lldap_role_docker_userns_mode`"

        ```yaml
        # Type: string
        lldap_role_docker_userns_mode:
        ```

    ??? variable string "`lldap_role_docker_uts`"

        ```yaml
        # Type: string
        lldap_role_docker_uts:
        ```

=== "Global Override Options"

    ??? variable bool "`lldap_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        lldap_role_autoheal_enabled: true
        ```

    ??? variable string "`lldap_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        lldap_role_depends_on: ""
        ```

    ??? variable string "`lldap_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        lldap_role_depends_on_delay: "0"
        ```

    ??? variable string "`lldap_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        lldap_role_depends_on_healthchecks:
        ```

    ??? variable bool "`lldap_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        lldap_role_diun_enabled: true
        ```

    ??? variable bool "`lldap_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        lldap_role_dns_enabled: true
        ```

    ??? variable bool "`lldap_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        lldap_role_docker_controller: true
        ```

    ??? variable bool "`lldap_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        lldap_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`lldap_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        lldap_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`lldap_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        lldap_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`lldap_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        lldap_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`lldap_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        lldap_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`lldap_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        lldap_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`lldap_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        lldap_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`lldap_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        lldap_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`lldap_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        lldap_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`lldap_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        lldap_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            lldap_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "lldap2.{{ user.domain }}"
              - "lldap.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`lldap_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        lldap_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            lldap_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'lldap2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`lldap_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        lldap_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
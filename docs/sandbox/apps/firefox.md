---
icon: material/docker
hide:
  - tags
tags:
  - firefox
  - browser
---

# Firefox

## Overview

[Docker container for Firefox](https://github.com/jlesage/docker-firefox#readme) is a Docker container image that provides the Mozilla Firefox web browser, accessible through a modern web browser or any VNC client.

> [Mozilla Firefox](https://www.firefox.com) is a free and open-source web browser developed by Mozilla Foundation and its subsidiary, Mozilla Corporation.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://github.com/jlesage/docker-firefox/blob/master/README.md#usage){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/jlesage/firefox/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Community**](https://github.com/jlesage/docker-firefox/discussions){ .md-button .md-button--stretch }

</div>

---

## Configuration

Settings are available as [environment variables:octicons-link-external-16:{ .md-icon--sm }](https://github.com/jlesage/docker-firefox#environment-variables) in `/opt/firefox/.env`.

??? tip "Access Control"

    By default, web access is restricted by Authelia and VNC access by SSH authentication; hence, no VNC password is configured. To add this extra layer of authorization, the process is straightforward:

    1. Run the following command:

       ```shell
       $EDITOR /opt/firefox/.vncpass_clear
       ```

    2. Enter your desired password (up to 8 characters in length) and save the file.

    3. At a minimum, a container restart is required for changes to take effect.

## Deployment

```shell
sb install sandbox-firefox
```

## Usage

!!! info inline end inline-fit-content "Downloads Save Location"

    ```
    /mnt/unionfs/downloads/firefox
    ```

### Web

Visit <https://firefox.iYOUR_DOMAIN_NAMEi>.

### VNC

The role supports VNC access over an SSH tunnel (local port forwarding) to Saltbox.

???+ example "Example Command on Local Machine"

    !!! tip ""

        Some VNC apps have this functionality built-in!

    ```shell
    ssh -L localhost:5900:firefox:5900 seed@203.0.113.1 -p 8843 # (1)!
    ```

    1. `-L localhost:5900:firefox:5900`: This part specifies local port forwarding. It tells SSH to listen on port 5900 on your local machine and forward any traffic to the firefox Docker container on port 5900 on the Saltbox host. In other words, it sets up a tunnel between your local port 5900 and the container's port 5900.

        Complete the command with your usual SSH info: `USERNAME@SALTBOX_EXTERNAL_IP -p SSH_PORT`.

While the tunnel is active, you can use a VNC client to access the GUI via the address `localhost:5900`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    firefox_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `firefox_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `firefox_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`firefox_name`"

        ```yaml
        # Type: string
        firefox_name: firefox
        ```

=== "Web"

    ??? variable string "`firefox_role_web_subdomain`"

        ```yaml
        # Type: string
        firefox_role_web_subdomain: "{{ firefox_name }}"
        ```

    ??? variable string "`firefox_role_web_domain`"

        ```yaml
        # Type: string
        firefox_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`firefox_role_web_port`"

        ```yaml
        # Type: string
        firefox_role_web_port: "5800"
        ```

    ??? variable string "`firefox_role_web_url`"

        ```yaml
        # Type: string
        firefox_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='firefox') + '.' + lookup('role_var', '_web_domain', role='firefox')
                               if (lookup('role_var', '_web_subdomain', role='firefox') | length > 0)
                               else lookup('role_var', '_web_domain', role='firefox')) }}"
        ```

=== "VNC"

    ??? variable string "`firefox_role_vnc_port`"

        ```yaml
        # Type: string
        firefox_role_vnc_port: "5900"
        ```

=== "DNS"

    ??? variable string "`firefox_role_dns_record`"

        ```yaml
        # Type: string
        firefox_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='firefox') }}"
        ```

    ??? variable string "`firefox_role_dns_zone`"

        ```yaml
        # Type: string
        firefox_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='firefox') }}"
        ```

    ??? variable bool "`firefox_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`firefox_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        firefox_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`firefox_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        firefox_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`firefox_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        firefox_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`firefox_role_traefik_certresolver`"

        ```yaml
        # Type: string
        firefox_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`firefox_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_traefik_enabled: true
        ```

    ??? variable bool "`firefox_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_traefik_api_enabled: false
        ```

    ??? variable string "`firefox_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        firefox_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`firefox_role_docker_container`"

        ```yaml
        # Type: string
        firefox_role_docker_container: "{{ firefox_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`firefox_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_docker_image_pull: true
        ```

    ??? variable string "`firefox_role_docker_image_repo`"

        ```yaml
        # Type: string
        firefox_role_docker_image_repo: "jlesage/firefox"
        ```

    ??? variable string "`firefox_role_docker_image_tag`"

        ```yaml
        # Type: string
        firefox_role_docker_image_tag: "latest"
        ```

    ??? variable string "`firefox_role_docker_image`"

        ```yaml
        # Type: string
        firefox_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='firefox') }}:{{ lookup('role_var', '_docker_image_tag', role='firefox') }}"
        ```

    <h5>Envs</h5>

    ??? variable string "`firefox_role_docker_env_file`"

        ```yaml
        # Type: string
        firefox_role_docker_env_file: "{{ lookup('role_var', '_paths_env_file_location', role='firefox') }}"
        ```

    <h5>Volumes</h5>

    ??? variable list "`firefox_role_docker_volumes_default`"

        ```yaml
        # Type: list
        firefox_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='firefox') }}:/config"
        ```

    ??? variable list "`firefox_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        firefox_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`firefox_role_docker_hostname`"

        ```yaml
        # Type: string
        firefox_role_docker_hostname: "{{ firefox_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`firefox_role_docker_networks_alias`"

        ```yaml
        # Type: string
        firefox_role_docker_networks_alias: "{{ firefox_name }}"
        ```

    ??? variable list "`firefox_role_docker_networks_default`"

        ```yaml
        # Type: list
        firefox_role_docker_networks_default: []
        ```

    ??? variable list "`firefox_role_docker_networks_custom`"

        ```yaml
        # Type: list
        firefox_role_docker_networks_custom: []
        ```

    <h5>Capabilities</h5>

    ??? variable list "`firefox_role_docker_capabilities_default`"

        ```yaml
        # Type: list
        firefox_role_docker_capabilities_default:
          - "SYS_NICE"
        ```

    ??? variable list "`firefox_role_docker_capabilities_custom`"

        ```yaml
        # Type: list
        firefox_role_docker_capabilities_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`firefox_role_docker_restart_policy`"

        ```yaml
        # Type: string
        firefox_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`firefox_role_docker_state`"

        ```yaml
        # Type: string
        firefox_role_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`firefox_role_docker_blkio_weight`"

        ```yaml
        # Type: int
        firefox_role_docker_blkio_weight:
        ```

    ??? variable int "`firefox_role_docker_cpu_period`"

        ```yaml
        # Type: int
        firefox_role_docker_cpu_period:
        ```

    ??? variable int "`firefox_role_docker_cpu_quota`"

        ```yaml
        # Type: int
        firefox_role_docker_cpu_quota:
        ```

    ??? variable int "`firefox_role_docker_cpu_shares`"

        ```yaml
        # Type: int
        firefox_role_docker_cpu_shares:
        ```

    ??? variable string "`firefox_role_docker_cpus`"

        ```yaml
        # Type: string
        firefox_role_docker_cpus:
        ```

    ??? variable string "`firefox_role_docker_cpuset_cpus`"

        ```yaml
        # Type: string
        firefox_role_docker_cpuset_cpus:
        ```

    ??? variable string "`firefox_role_docker_cpuset_mems`"

        ```yaml
        # Type: string
        firefox_role_docker_cpuset_mems:
        ```

    ??? variable string "`firefox_role_docker_kernel_memory`"

        ```yaml
        # Type: string
        firefox_role_docker_kernel_memory:
        ```

    ??? variable string "`firefox_role_docker_memory`"

        ```yaml
        # Type: string
        firefox_role_docker_memory:
        ```

    ??? variable string "`firefox_role_docker_memory_reservation`"

        ```yaml
        # Type: string
        firefox_role_docker_memory_reservation:
        ```

    ??? variable string "`firefox_role_docker_memory_swap`"

        ```yaml
        # Type: string
        firefox_role_docker_memory_swap:
        ```

    ??? variable int "`firefox_role_docker_memory_swappiness`"

        ```yaml
        # Type: int
        firefox_role_docker_memory_swappiness:
        ```

    ??? variable string "`firefox_role_docker_shm_size`"

        ```yaml
        # Type: string
        firefox_role_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`firefox_role_docker_cap_drop`"

        ```yaml
        # Type: list
        firefox_role_docker_cap_drop:
        ```

    ??? variable string "`firefox_role_docker_cgroupns_mode`"

        ```yaml
        # Type: string
        firefox_role_docker_cgroupns_mode:
        ```

    ??? variable list "`firefox_role_docker_device_cgroup_rules`"

        ```yaml
        # Type: list
        firefox_role_docker_device_cgroup_rules:
        ```

    ??? variable list "`firefox_role_docker_device_read_bps`"

        ```yaml
        # Type: list
        firefox_role_docker_device_read_bps:
        ```

    ??? variable list "`firefox_role_docker_device_read_iops`"

        ```yaml
        # Type: list
        firefox_role_docker_device_read_iops:
        ```

    ??? variable list "`firefox_role_docker_device_requests`"

        ```yaml
        # Type: list
        firefox_role_docker_device_requests:
        ```

    ??? variable list "`firefox_role_docker_device_write_bps`"

        ```yaml
        # Type: list
        firefox_role_docker_device_write_bps:
        ```

    ??? variable list "`firefox_role_docker_device_write_iops`"

        ```yaml
        # Type: list
        firefox_role_docker_device_write_iops:
        ```

    ??? variable list "`firefox_role_docker_devices`"

        ```yaml
        # Type: list
        firefox_role_docker_devices:
        ```

    ??? variable string "`firefox_role_docker_devices_default`"

        ```yaml
        # Type: string
        firefox_role_docker_devices_default:
        ```

    ??? variable list "`firefox_role_docker_groups`"

        ```yaml
        # Type: list
        firefox_role_docker_groups:
        ```

    ??? variable bool "`firefox_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_docker_privileged:
        ```

    ??? variable list "`firefox_role_docker_security_opts`"

        ```yaml
        # Type: list
        firefox_role_docker_security_opts:
        ```

    ??? variable string "`firefox_role_docker_user`"

        ```yaml
        # Type: string
        firefox_role_docker_user:
        ```

    ??? variable string "`firefox_role_docker_userns_mode`"

        ```yaml
        # Type: string
        firefox_role_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`firefox_role_docker_dns_opts`"

        ```yaml
        # Type: list
        firefox_role_docker_dns_opts:
        ```

    ??? variable list "`firefox_role_docker_dns_search_domains`"

        ```yaml
        # Type: list
        firefox_role_docker_dns_search_domains:
        ```

    ??? variable list "`firefox_role_docker_dns_servers`"

        ```yaml
        # Type: list
        firefox_role_docker_dns_servers:
        ```

    ??? variable string "`firefox_role_docker_domainname`"

        ```yaml
        # Type: string
        firefox_role_docker_domainname:
        ```

    ??? variable list "`firefox_role_docker_exposed_ports`"

        ```yaml
        # Type: list
        firefox_role_docker_exposed_ports:
        ```

    ??? variable dict "`firefox_role_docker_hosts`"

        ```yaml
        # Type: dict
        firefox_role_docker_hosts:
        ```

    ??? variable bool "`firefox_role_docker_hosts_use_common`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_docker_hosts_use_common:
        ```

    ??? variable string "`firefox_role_docker_ipc_mode`"

        ```yaml
        # Type: string
        firefox_role_docker_ipc_mode:
        ```

    ??? variable list "`firefox_role_docker_links`"

        ```yaml
        # Type: list
        firefox_role_docker_links:
        ```

    ??? variable string "`firefox_role_docker_network_mode`"

        ```yaml
        # Type: string
        firefox_role_docker_network_mode:
        ```

    ??? variable string "`firefox_role_docker_pid_mode`"

        ```yaml
        # Type: string
        firefox_role_docker_pid_mode:
        ```

    ??? variable list "`firefox_role_docker_ports`"

        ```yaml
        # Type: list
        firefox_role_docker_ports:
        ```

    ??? variable string "`firefox_role_docker_uts`"

        ```yaml
        # Type: string
        firefox_role_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`firefox_role_docker_keep_volumes`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_docker_keep_volumes:
        ```

    ??? variable list "`firefox_role_docker_mounts`"

        ```yaml
        # Type: list
        firefox_role_docker_mounts:
        ```

    ??? variable dict "`firefox_role_docker_storage_opts`"

        ```yaml
        # Type: dict
        firefox_role_docker_storage_opts:
        ```

    ??? variable list "`firefox_role_docker_tmpfs`"

        ```yaml
        # Type: list
        firefox_role_docker_tmpfs:
        ```

    ??? variable string "`firefox_role_docker_volume_driver`"

        ```yaml
        # Type: string
        firefox_role_docker_volume_driver:
        ```

    ??? variable list "`firefox_role_docker_volumes_from`"

        ```yaml
        # Type: list
        firefox_role_docker_volumes_from:
        ```

    ??? variable bool "`firefox_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_docker_volumes_global:
        ```

    ??? variable string "`firefox_role_docker_working_dir`"

        ```yaml
        # Type: string
        firefox_role_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`firefox_role_docker_auto_remove`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_docker_auto_remove:
        ```

    ??? variable bool "`firefox_role_docker_cleanup`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_docker_cleanup:
        ```

    ??? variable string "`firefox_role_docker_force_kill`"

        ```yaml
        # Type: string
        firefox_role_docker_force_kill:
        ```

    ??? variable dict "`firefox_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        firefox_role_docker_healthcheck:
        ```

    ??? variable int "`firefox_role_docker_healthy_wait_timeout`"

        ```yaml
        # Type: int
        firefox_role_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`firefox_role_docker_init`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_docker_init:
        ```

    ??? variable string "`firefox_role_docker_kill_signal`"

        ```yaml
        # Type: string
        firefox_role_docker_kill_signal:
        ```

    ??? variable string "`firefox_role_docker_log_driver`"

        ```yaml
        # Type: string
        firefox_role_docker_log_driver:
        ```

    ??? variable dict "`firefox_role_docker_log_options`"

        ```yaml
        # Type: dict
        firefox_role_docker_log_options:
        ```

    ??? variable bool "`firefox_role_docker_oom_killer`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_docker_oom_killer:
        ```

    ??? variable int "`firefox_role_docker_oom_score_adj`"

        ```yaml
        # Type: int
        firefox_role_docker_oom_score_adj:
        ```

    ??? variable bool "`firefox_role_docker_output_logs`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_docker_output_logs:
        ```

    ??? variable bool "`firefox_role_docker_paused`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_docker_paused:
        ```

    ??? variable bool "`firefox_role_docker_recreate`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_docker_recreate:
        ```

    ??? variable int "`firefox_role_docker_restart_retries`"

        ```yaml
        # Type: int
        firefox_role_docker_restart_retries:
        ```

    ??? variable int "`firefox_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        firefox_role_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable string "`firefox_role_docker_cgroup_parent`"

        ```yaml
        # Type: string
        firefox_role_docker_cgroup_parent:
        ```

    ??? variable list "`firefox_role_docker_commands`"

        ```yaml
        # Type: list
        firefox_role_docker_commands:
        ```

    ??? variable int "`firefox_role_docker_create_timeout`"

        ```yaml
        # Type: int
        firefox_role_docker_create_timeout:
        ```

    ??? variable string "`firefox_role_docker_entrypoint`"

        ```yaml
        # Type: string
        firefox_role_docker_entrypoint:
        ```

    ??? variable dict "`firefox_role_docker_envs`"

        ```yaml
        # Type: dict
        firefox_role_docker_envs:
        ```

    ??? variable dict "`firefox_role_docker_labels`"

        ```yaml
        # Type: dict
        firefox_role_docker_labels:
        ```

    ??? variable bool "`firefox_role_docker_labels_use_common`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_docker_labels_use_common:
        ```

    ??? variable bool "`firefox_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_docker_read_only:
        ```

    ??? variable string "`firefox_role_docker_runtime`"

        ```yaml
        # Type: string
        firefox_role_docker_runtime:
        ```

    ??? variable list "`firefox_role_docker_sysctls`"

        ```yaml
        # Type: list
        firefox_role_docker_sysctls:
        ```

    ??? variable list "`firefox_role_docker_ulimits`"

        ```yaml
        # Type: list
        firefox_role_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`firefox_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        firefox_role_autoheal_enabled: true
        ```

    ??? variable string "`firefox_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        firefox_role_depends_on: ""
        ```

    ??? variable string "`firefox_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        firefox_role_depends_on_delay: "0"
        ```

    ??? variable string "`firefox_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        firefox_role_depends_on_healthchecks:
        ```

    ??? variable bool "`firefox_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        firefox_role_diun_enabled: true
        ```

    ??? variable bool "`firefox_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        firefox_role_dns_enabled: true
        ```

    ??? variable bool "`firefox_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        firefox_role_docker_controller: true
        ```

    ??? variable string "`firefox_role_docker_image_repo`"

        ```yaml
        # Type: string
        firefox_role_docker_image_repo:
        ```

    ??? variable string "`firefox_role_docker_image_tag`"

        ```yaml
        # Type: string
        firefox_role_docker_image_tag:
        ```

    ??? variable bool "`firefox_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_docker_volumes_download:
        ```

    ??? variable string "`firefox_role_paths_env_file_location`"

        ```yaml
        # Type: string
        firefox_role_paths_env_file_location:
        ```

    ??? variable string "`firefox_role_paths_location`"

        ```yaml
        # Type: string
        firefox_role_paths_location:
        ```

    ??? variable string "`firefox_role_themepark_addons`"

        ```yaml
        # Type: string
        firefox_role_themepark_addons:
        ```

    ??? variable string "`firefox_role_themepark_app`"

        ```yaml
        # Type: string
        firefox_role_themepark_app:
        ```

    ??? variable string "`firefox_role_themepark_theme`"

        ```yaml
        # Type: string
        firefox_role_themepark_theme:
        ```

    ??? variable dict/omit "`firefox_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        firefox_role_traefik_api_endpoint:
        ```

    ??? variable string "`firefox_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        firefox_role_traefik_api_middleware:
        ```

    ??? variable string "`firefox_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        firefox_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`firefox_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        firefox_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`firefox_role_traefik_certresolver`"

        ```yaml
        # Type: string
        firefox_role_traefik_certresolver:
        ```

    ??? variable bool "`firefox_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        firefox_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`firefox_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        firefox_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`firefox_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        firefox_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`firefox_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        firefox_role_traefik_middleware_http:
        ```

    ??? variable bool "`firefox_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`firefox_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`firefox_role_traefik_priority`"

        ```yaml
        # Type: string
        firefox_role_traefik_priority:
        ```

    ??? variable bool "`firefox_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        firefox_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`firefox_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        firefox_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`firefox_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        firefox_role_traefik_wildcard_enabled: true
        ```

    ??? variable string "`firefox_role_web_domain`"

        ```yaml
        # Type: string
        firefox_role_web_domain:
        ```

    ??? variable list "`firefox_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        firefox_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            firefox_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "firefox2.{{ user.domain }}"
              - "firefox.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`firefox_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        firefox_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            firefox_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'firefox2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`firefox_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        firefox_role_web_http_port:
        ```

    ??? variable string "`firefox_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        firefox_role_web_http_scheme:
        ```

    ??? variable dict/omit "`firefox_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        firefox_role_web_http_serverstransport:
        ```

    ??? variable string "`firefox_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        firefox_role_web_scheme:
        ```

    ??? variable dict/omit "`firefox_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        firefox_role_web_serverstransport:
        ```

    ??? variable string "`firefox_role_web_subdomain`"

        ```yaml
        # Type: string
        firefox_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
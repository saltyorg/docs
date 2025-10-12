---
hide:
  - tags
tags:
  - petio
---

# Petio

## What is it?

[Petio](https://petio.tv/) is a third party companion app available to Plex server owners to allow their users to request, review and discover content. The app is built to appear instantly familiar and intuitive to even the most tech-agnostic users. Petio will help you manage requests from your users, connect to other third party apps such as Sonarr and Radarr, notify users when content is available and track request progress. Petio also allows users to discover media both on and off your server, quickly and easily find related content and review to leave their opinion for other users.

Petio is an ongoing, forever free, always evolving project currently in alpha prototype stage and now available!

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://petio.tv/){: .header-icons } | [:octicons-link-16: Docs](https://docs.petio.tv/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/petio-team/petio){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/petio){: .header-icons }|

### 1. Installation

``` shell

sb install petio

```

### 2. URL

- To access Petio, visit `https://petio._yourdomain.com_`

### 3. Setup

- Click Login With Plex and follow the steps to log in.

- After you log in with Plex you will need to specify your Petio specific admin credentials, by default it uses your Plex username and email but you still need to specify your own password.

- After setting up your credentials, you need to pick your Plex server.

- MongoDB: Use `petio-mongo:27017` (assumes default instance and therefore default petio_name otherwise it is the value of `petio_name` plus the `-mongo:27017` suffix)

- Once the last step is finished, you will be presented with a login screen. Use your Plex username and the password you set up on Step 2. You can now get started with configuring Radarr, Sonarr and start requesting!

- See the Petio documentation for more information.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        petio_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `petio_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `petio_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    petio_name: petio

    ```

??? example "Settings"

    ```yaml
    # Type: string
    petio_role_mongodb_version: "4.4"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    petio_role_paths_folder: "{{ petio_name }}"

    # Type: string
    petio_role_paths_location: "{{ server_appdata_path }}/{{ petio_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    petio_role_web_subdomain: "{{ petio_name }}"

    # Type: string
    petio_role_web_domain: "{{ user.domain }}"

    # Type: string
    petio_role_web_port: "7777"

    # Type: string
    petio_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='petio') + '.' + lookup('role_var', '_web_domain', role='petio')
                         if (lookup('role_var', '_web_subdomain', role='petio') | length > 0)
                         else lookup('role_var', '_web_domain', role='petio')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    petio_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='petio') }}"

    # Type: string
    petio_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='petio') }}"

    # Type: bool (true/false)
    petio_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    petio_role_traefik_sso_middleware: ""

    # Type: string
    petio_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    petio_role_traefik_middleware_custom: ""

    # Type: string
    petio_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    petio_role_traefik_enabled: true

    # Type: bool (true/false)
    petio_role_traefik_api_enabled: false

    # Type: string
    petio_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    petio_role_docker_container: "{{ petio_name }}"

    # Image
    # Type: bool (true/false)
    petio_role_docker_image_pull: true

    # Type: string
    petio_role_docker_image_repo: "ghcr.io/petio-team/petio"

    # Type: string
    petio_role_docker_image_tag: "latest"

    # Type: string
    petio_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='petio') }}:{{ lookup('role_var', '_docker_image_tag', role='petio') }}"

    # Envs
    # Type: dict
    petio_role_docker_envs_default: 
      TZ: "{{ tz }}"

    # Type: dict
    petio_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    petio_role_docker_volumes_default: 
      - "{{ petio_role_paths_location }}:/app/api/config"

    # Type: list
    petio_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    petio_role_docker_hostname: "{{ petio_name }}"

    # Networks
    # Type: string
    petio_role_docker_networks_alias: "{{ petio_name }}"

    # Type: list
    petio_role_docker_networks_default: []

    # Type: list
    petio_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    petio_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    petio_role_docker_state: started

    # User
    # Type: string
    petio_role_docker_user: "{{ uid }}:{{ gid }}"

    # Dependencies
    # Type: string
    petio_role_depends_on: "{{ petio_name }}-mongo"

    # Type: string
    petio_role_depends_on_delay: "0"

    # Type: string
    petio_role_depends_on_healthchecks: "false"


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    petio_role_docker_blkio_weight:

    # Type: int
    petio_role_docker_cpu_period:

    # Type: int
    petio_role_docker_cpu_quota:

    # Type: int
    petio_role_docker_cpu_shares:

    # Type: string
    petio_role_docker_cpus:

    # Type: string
    petio_role_docker_cpuset_cpus:

    # Type: string
    petio_role_docker_cpuset_mems:

    # Type: string
    petio_role_docker_kernel_memory:

    # Type: string
    petio_role_docker_memory:

    # Type: string
    petio_role_docker_memory_reservation:

    # Type: string
    petio_role_docker_memory_swap:

    # Type: int
    petio_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    petio_role_docker_cap_drop:

    # Type: list
    petio_role_docker_device_cgroup_rules:

    # Type: list
    petio_role_docker_device_read_bps:

    # Type: list
    petio_role_docker_device_read_iops:

    # Type: list
    petio_role_docker_device_requests:

    # Type: list
    petio_role_docker_device_write_bps:

    # Type: list
    petio_role_docker_device_write_iops:

    # Type: list
    petio_role_docker_devices:

    # Type: string
    petio_role_docker_devices_default:

    # Type: bool (true/false)
    petio_role_docker_privileged:

    # Type: list
    petio_role_docker_security_opts:


    # Networking
    # Type: list
    petio_role_docker_dns_opts:

    # Type: list
    petio_role_docker_dns_search_domains:

    # Type: list
    petio_role_docker_dns_servers:

    # Type: dict
    petio_role_docker_hosts:

    # Type: string
    petio_role_docker_hosts_use_common:

    # Type: string
    petio_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    petio_role_docker_keep_volumes:

    # Type: list
    petio_role_docker_mounts:

    # Type: string
    petio_role_docker_volume_driver:

    # Type: list
    petio_role_docker_volumes_from:

    # Type: string
    petio_role_docker_volumes_global:

    # Type: string
    petio_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    petio_role_docker_healthcheck:

    # Type: bool (true/false)
    petio_role_docker_init:

    # Type: string
    petio_role_docker_log_driver:

    # Type: dict
    petio_role_docker_log_options:

    # Type: bool (true/false)
    petio_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    petio_role_docker_auto_remove:

    # Type: list
    petio_role_docker_capabilities:

    # Type: string
    petio_role_docker_cgroup_parent:

    # Type: string
    petio_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    petio_role_docker_cleanup:

    # Type: list
    petio_role_docker_commands:

    # Type: string
    petio_role_docker_create_timeout:

    # Type: string
    petio_role_docker_domainname:

    # Type: string
    petio_role_docker_entrypoint:

    # Type: string
    petio_role_docker_env_file:

    # Type: list
    petio_role_docker_exposed_ports:

    # Type: string
    petio_role_docker_force_kill:

    # Type: list
    petio_role_docker_groups:

    # Type: int
    petio_role_docker_healthy_wait_timeout:

    # Type: string
    petio_role_docker_ipc_mode:

    # Type: string
    petio_role_docker_kill_signal:

    # Type: dict
    petio_role_docker_labels:

    # Type: string
    petio_role_docker_labels_use_common:

    # Type: list
    petio_role_docker_links:

    # Type: bool (true/false)
    petio_role_docker_oom_killer:

    # Type: int
    petio_role_docker_oom_score_adj:

    # Type: bool (true/false)
    petio_role_docker_paused:

    # Type: string
    petio_role_docker_pid_mode:

    # Type: list
    petio_role_docker_ports:

    # Type: bool (true/false)
    petio_role_docker_read_only:

    # Type: bool (true/false)
    petio_role_docker_recreate:

    # Type: int
    petio_role_docker_restart_retries:

    # Type: string
    petio_role_docker_runtime:

    # Type: string
    petio_role_docker_shm_size:

    # Type: int
    petio_role_docker_stop_timeout:

    # Type: dict
    petio_role_docker_storage_opts:

    # Type: list
    petio_role_docker_sysctls:

    # Type: list
    petio_role_docker_tmpfs:

    # Type: list
    petio_role_docker_ulimits:

    # Type: string
    petio_role_docker_userns_mode:

    # Type: string
    petio_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    petio_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    petio_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    petio_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    petio_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    petio_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    petio_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    petio_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    petio_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    petio_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    petio_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    petio_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    petio_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    petio_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    petio_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    petio_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    petio_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    petio_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        petio_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "petio2.{{ user.domain }}"
          - "petio.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        petio_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'petio2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

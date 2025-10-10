---
hide:
  - tags
tags:
  - sab
  - sabnzbd
---

# SABnzbd

# What is it?

[SABnzbd](https://github.com/sabnzbd/sabnzbd) is an Open Source Binary Newsreader written in Python.

It's totally free, easy to use, and works practically everywhere. SABnzbd makes Usenet as simple and streamlined as possible by automating everything we can. All you have to do is add an .nzb. SABnzbd takes over from there, where it will be automatically downloaded, verified, repaired, extracted and filed away with zero human interaction. SABnzbd offers an easy setup wizard and has self-analysis tools to verify your setup.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://sabnzbd.org/){: .header-icons } | [:octicons-link-16: Docs](https://sabnzbd.org/wiki/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/sabnzbd/sabnzbd){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/sabnzbd){: .header-icons }|

## 1. Installation

```shell
sb install sabnzbd
```

## 1. URL

- To access SABnzbd, visit `https://sabnzbd._yourdomain.com_`

## 2. Basics

- Go through the setup wizard.  You will need to enter server details:

![](../images/sabnzbd/02-sabnzbd.png)

- When you get to the end of the wizard, click "Go To SABnzbd"

![](../images/sabnzbd/03-sabnzbd.png)

- Go to SABnzbd Config

![](../images/sabnzbd/04-sabnzbd.png)

- You will need to add in categories for `sonarr`, `radarr`, and `lidarr`.

  Set a relative directory name for each category.

  You will need a category for each instance of `sonarr`/`radarr`/`lidarr` [for example, if you have a `radarr` and `radarr4k` you will need a category for each]

  SABnzbd requires the server to be filled in to set categories up.

  **This needs to be done BEFORE adding SABnzbd as a downloader to any of those apps.**

![](../images/sabnzbd/05-sabnzbd.png)

- Direct unpack is disabled by default. Configure this as you prefer.

- Make note of the API Key in the "General" section

![](../images/sabnzbd/06-sabnzbd.png)

- When creating the connection in the arrs, use API Key rather than user/pass.

![](../images/sabnzbd/07-sabnzbd.png)

   Note that the category matches between Radarr and SABnzbd.  The specific category doesn't matter; just that they match.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        sabnzbd_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    sabnzbd_name: sabnzbd

    ```

??? example "Paths"

    ```yaml
    # Type: string
    sabnzbd_role_paths_folder: "{{ sabnzbd_name }}"

    # Type: string
    sabnzbd_role_paths_location: "{{ server_appdata_path }}/{{ sabnzbd_role_paths_folder }}"

    # Type: string
    sabnzbd_role_paths_downloads_location: "{{ downloads_usenet_path }}/{{ sabnzbd_role_paths_folder }}"

    # Type: string
    sabnzbd_role_paths_config_location: "{{ sabnzbd_role_paths_location }}/sabnzbd.ini"

    ```

??? example "Web"

    ```yaml
    # Type: string
    sabnzbd_role_web_subdomain: "{{ sabnzbd_name }}"

    # Type: string
    sabnzbd_role_web_domain: "{{ user.domain }}"

    # Type: string
    sabnzbd_role_web_port: "8080"

    # Type: string
    sabnzbd_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='sabnzbd') + '.' + lookup('role_var', '_web_domain', role='sabnzbd')
                           if (lookup('role_var', '_web_subdomain', role='sabnzbd') | length > 0)
                           else lookup('role_var', '_web_domain', role='sabnzbd')) }}"

    # Type: string
    sabnzbd_role_web_local_url: "{{ 'http://' + sabnzbd_name + ':' + lookup('role_var', '_web_port', role='sabnzbd') }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    sabnzbd_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='sabnzbd') }}"

    # Type: string
    sabnzbd_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='sabnzbd') }}"

    # Type: bool (true/false)
    sabnzbd_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    sabnzbd_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    sabnzbd_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                 + (',themepark-' + sabnzbd_name
                                                   if (lookup('role_var', '_themepark_enabled', role='sabnzbd') and global_themepark_plugin_enabled)
                                                   else '') }}"

    # Type: string
    sabnzbd_role_traefik_middleware_custom: ""

    # Type: string
    sabnzbd_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    sabnzbd_role_traefik_enabled: true

    # Type: bool (true/false)
    sabnzbd_role_traefik_api_enabled: true

    # Type: string
    sabnzbd_role_traefik_api_endpoint: "PathPrefix(`/api`)"

    ```

??? example "Config"

    ```yaml
    # Type: list
    sabnzbd_role_config_settings_web: 
      # Web
      - { option: "host_whitelist", value: "{{ lookup('role_var', '_web_subdomain', role='sabnzbd') }}.{{ lookup('role_var', '_web_domain', role='sabnzbd') }}, {{ sabnzbd_name }}" }
      - { option: "url_base", value: "" }
      - { option: "log_dir", value: "/config/logs" }

    # Type: list
    sabnzbd_role_config_settings_default: 
      # Web
      - { option: "host_whitelist", value: "{{ lookup('role_var', '_web_subdomain', role='sabnzbd') }}.{{ lookup('role_var', '_web_domain', role='sabnzbd') }}, {{ sabnzbd_name }}" }
      - { option: "url_base", value: "" }
      # Paths
      - { option: "dirscan_dir", value: "{{ lookup('role_var', '_paths_downloads_location', role='sabnzbd') }}/watch" }
      - { option: "download_dir", value: "{{ lookup('role_var', '_paths_downloads_location', role='sabnzbd') }}/incomplete" }
      - { option: "complete_dir", value: "{{ lookup('role_var', '_paths_downloads_location', role='sabnzbd') }}/complete" }
      - { option: "log_dir", value: "/config/logs" }

    # Type: list
    sabnzbd_role_config_settings_custom: []

    # Type: string
    sabnzbd_role_config_settings_list: "{{ lookup('role_var', '_config_settings_default', role='sabnzbd')
                                           + lookup('role_var', '_config_settings_custom', role='sabnzbd') }}"

    ```

??? example "Theme"

    ```yaml
    # Options can be found at https://github.com/themepark-dev/theme.park
    # Type: bool (true/false)
    sabnzbd_role_themepark_enabled: false

    # Type: string
    sabnzbd_role_themepark_app: "sabnzbd"

    # Type: string
    sabnzbd_role_themepark_theme: "{{ global_themepark_theme }}"

    # Type: string
    sabnzbd_role_themepark_domain: "{{ global_themepark_domain }}"

    # Type: list
    sabnzbd_role_themepark_addons: []

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    sabnzbd_role_docker_container: "{{ sabnzbd_name }}"

    # Image
    # Type: bool (true/false)
    sabnzbd_role_docker_image_pull: true

    # Type: string
    sabnzbd_role_docker_image_repo: "ghcr.io/hotio/sabnzbd"

    # Type: string
    sabnzbd_role_docker_image_tag: "latest"

    # Type: string
    sabnzbd_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='sabnzbd') }}:{{ lookup('role_var', '_docker_image_tag', role='sabnzbd') }}"

    # Envs
    # Type: dict
    sabnzbd_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      UMASK: "002"
      TZ: "{{ tz }}"

    # Type: dict
    sabnzbd_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    sabnzbd_role_docker_volumes_default: 
      - "{{ sabnzbd_role_paths_location }}:/config"
      - "{{ server_appdata_path }}/scripts:/scripts"

    # Type: list
    sabnzbd_role_docker_volumes_custom: []

    # Labels
    # Type: dict
    sabnzbd_role_docker_labels_default: {}

    # Type: dict
    sabnzbd_role_docker_labels_custom: {}

    # Hostname
    # Type: string
    sabnzbd_role_docker_hostname: "{{ sabnzbd_name }}"

    # Networks
    # Type: string
    sabnzbd_role_docker_networks_alias: "{{ sabnzbd_name }}"

    # Type: list
    sabnzbd_role_docker_networks_default: []

    # Type: list
    sabnzbd_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    sabnzbd_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    sabnzbd_role_docker_state: started


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    sabnzbd_role_docker_blkio_weight:

    # Type: int
    sabnzbd_role_docker_cpu_period:

    # Type: int
    sabnzbd_role_docker_cpu_quota:

    # Type: int
    sabnzbd_role_docker_cpu_shares:

    # Type: string
    sabnzbd_role_docker_cpus:

    # Type: string
    sabnzbd_role_docker_cpuset_cpus:

    # Type: string
    sabnzbd_role_docker_cpuset_mems:

    # Type: string
    sabnzbd_role_docker_kernel_memory:

    # Type: string
    sabnzbd_role_docker_memory:

    # Type: string
    sabnzbd_role_docker_memory_reservation:

    # Type: string
    sabnzbd_role_docker_memory_swap:

    # Type: int
    sabnzbd_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    sabnzbd_role_docker_cap_drop:

    # Type: list
    sabnzbd_role_docker_device_cgroup_rules:

    # Type: list
    sabnzbd_role_docker_device_read_bps:

    # Type: list
    sabnzbd_role_docker_device_read_iops:

    # Type: list
    sabnzbd_role_docker_device_requests:

    # Type: list
    sabnzbd_role_docker_device_write_bps:

    # Type: list
    sabnzbd_role_docker_device_write_iops:

    # Type: list
    sabnzbd_role_docker_devices:

    # Type: string
    sabnzbd_role_docker_devices_default:

    # Type: bool (true/false)
    sabnzbd_role_docker_privileged:

    # Type: list
    sabnzbd_role_docker_security_opts:


    # Networking
    # Type: list
    sabnzbd_role_docker_dns_opts:

    # Type: list
    sabnzbd_role_docker_dns_search_domains:

    # Type: list
    sabnzbd_role_docker_dns_servers:

    # Type: dict
    sabnzbd_role_docker_hosts:

    # Type: string
    sabnzbd_role_docker_hosts_use_common:

    # Type: string
    sabnzbd_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    sabnzbd_role_docker_keep_volumes:

    # Type: list
    sabnzbd_role_docker_mounts:

    # Type: string
    sabnzbd_role_docker_volume_driver:

    # Type: list
    sabnzbd_role_docker_volumes_from:

    # Type: string
    sabnzbd_role_docker_volumes_global:

    # Type: string
    sabnzbd_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    sabnzbd_role_docker_healthcheck:

    # Type: bool (true/false)
    sabnzbd_role_docker_init:

    # Type: string
    sabnzbd_role_docker_log_driver:

    # Type: dict
    sabnzbd_role_docker_log_options:

    # Type: bool (true/false)
    sabnzbd_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    sabnzbd_role_docker_auto_remove:

    # Type: list
    sabnzbd_role_docker_capabilities:

    # Type: string
    sabnzbd_role_docker_cgroup_parent:

    # Type: string
    sabnzbd_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    sabnzbd_role_docker_cleanup:

    # Type: list
    sabnzbd_role_docker_commands:

    # Type: string
    sabnzbd_role_docker_create_timeout:

    # Type: string
    sabnzbd_role_docker_domainname:

    # Type: string
    sabnzbd_role_docker_entrypoint:

    # Type: string
    sabnzbd_role_docker_env_file:

    # Type: list
    sabnzbd_role_docker_exposed_ports:

    # Type: string
    sabnzbd_role_docker_force_kill:

    # Type: list
    sabnzbd_role_docker_groups:

    # Type: int
    sabnzbd_role_docker_healthy_wait_timeout:

    # Type: string
    sabnzbd_role_docker_ipc_mode:

    # Type: string
    sabnzbd_role_docker_kill_signal:

    # Type: string
    sabnzbd_role_docker_labels_use_common:

    # Type: list
    sabnzbd_role_docker_links:

    # Type: bool (true/false)
    sabnzbd_role_docker_oom_killer:

    # Type: int
    sabnzbd_role_docker_oom_score_adj:

    # Type: bool (true/false)
    sabnzbd_role_docker_paused:

    # Type: string
    sabnzbd_role_docker_pid_mode:

    # Type: list
    sabnzbd_role_docker_ports:

    # Type: bool (true/false)
    sabnzbd_role_docker_read_only:

    # Type: bool (true/false)
    sabnzbd_role_docker_recreate:

    # Type: int
    sabnzbd_role_docker_restart_retries:

    # Type: string
    sabnzbd_role_docker_runtime:

    # Type: string
    sabnzbd_role_docker_shm_size:

    # Type: int
    sabnzbd_role_docker_stop_timeout:

    # Type: dict
    sabnzbd_role_docker_storage_opts:

    # Type: list
    sabnzbd_role_docker_sysctls:

    # Type: list
    sabnzbd_role_docker_tmpfs:

    # Type: list
    sabnzbd_role_docker_ulimits:

    # Type: string
    sabnzbd_role_docker_user:

    # Type: string
    sabnzbd_role_docker_userns_mode:

    # Type: string
    sabnzbd_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    sabnzbd_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    sabnzbd_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    sabnzbd_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    sabnzbd_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    sabnzbd_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    sabnzbd_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    sabnzbd_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    sabnzbd_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    sabnzbd_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    sabnzbd_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    sabnzbd_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    sabnzbd_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    sabnzbd_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    sabnzbd_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    sabnzbd_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    sabnzbd_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    sabnzbd_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        sabnzbd_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "sabnzbd2.{{ user.domain }}"
          - "sabnzbd.otherdomain.tld"
        ```
        
        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries
        

    2.  Example:

        ```yaml
        sabnzbd_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'sabnzbd2.' + user.domain }}`)"
        ```
        
        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule
        

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

## Next

Are you setting Saltbox up for the first time?  Continue to [Qbittorrent](qbittorrent.md).


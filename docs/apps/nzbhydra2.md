---
hide:
  - tags
tags:
  - nzbhydra
  - nzbhydra2
---

# NZBHydra2

# What is it?

[NZBHydra2](https://github.com/theotherp/nzbhydra2), by _TheOtherP_, is a meta search tool for NZB indexers. It provides easy access to a number of NZB indexers. You can search all your indexers from one place and use it as indexer source for tools like Sonarr or CouchPotato.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| :material-home: Project home | [:octicons-link-16: Docs](https://github.com/theotherp/nzbhydra2/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/theotherp/nzbhydra2){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/nzbhydra2){: .header-icons }|

Three Ways to setup NZB indexers with Sonarr/Radarr/Lidarr:

1. Skip this page and add all your NZB Indexers directly into Sonarr/Radarr/Lidarr. Benefit from the seeing indexer sources during manual lookups in Sonarr/Radarr/Lidarr. This method is also useful when diagnosing issues with indexers during failed searches;

2. Add all your NZB Indexers directly into Sonarr/Radarr/Lidarr, but also add them in NZBHydra2, so it could be used a tool for manual downloads; or

3. Add all your NZB indexers in NZBHydra2 and then just add the one NZBHydra2 "indexer" into Sonarr/Radarr/Lidarr. This is the most popular choice among users.

---

To Setup NZBHydra2, follow the steps below.

## 2. URL

- URL to access NZBHydra2, visit `https://nzbhydra2._yourdomain.com_`

## 3. Setup

Enter setup by clicking on "Config" at the top.

### Main

- Under 'Security', click the icon next to the 'API key *' field to generate an API key. Click 'Save'.

### Authorization

- Login settings are preset out of the box (`user` / `passwd` as set in [accounts.yml](../reference/accounts.md)).

### Indexers

- Add your indexers. Click "Save".

### Downloaders

- NZBGet settings are preset out of the box.

## 4. API Key

To find the NZBHydra2 API Key, go to "Config" --> "Main". This will be used later in [Sonarr](sonarr.md) and [Radarr](radarr.md).

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        nzbhydra2_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    nzbhydra2_name: nzbhydra2

    ```

??? example "Paths"

    ```yaml
    # Type: string
    nzbhydra2_role_paths_folder: "{{ nzbhydra2_name }}"

    # Type: string
    nzbhydra2_role_paths_location: "{{ server_appdata_path }}/{{ nzbhydra2_role_paths_folder }}"

    # Type: string
    nzbhydra2_role_paths_downloads_location: "{{ downloads_usenet_path }}/{{ nzbhydra2_role_paths_folder }}"

    # Type: string
    nzbhydra2_role_paths_config_location: "{{ nzbhydra2_role_paths_location }}/nzbhydra.yml"

    ```

??? example "Web"

    ```yaml
    # Type: string
    nzbhydra2_role_web_subdomain: "{{ nzbhydra2_name }}"

    # Type: string
    nzbhydra2_role_web_domain: "{{ user.domain }}"

    # Type: string
    nzbhydra2_role_web_port: "5076"

    # Type: string
    nzbhydra2_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='nzbhydra2') + '.' + lookup('role_var', '_web_domain', role='nzbhydra2')
                             if (lookup('role_var', '_web_subdomain', role='nzbhydra2') | length > 0)
                             else lookup('role_var', '_web_domain', role='nzbhydra2')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    nzbhydra2_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='nzbhydra2') }}"

    # Type: string
    nzbhydra2_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='nzbhydra2') }}"

    # Type: bool (true/false)
    nzbhydra2_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    nzbhydra2_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    nzbhydra2_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                   + (',themepark-' + nzbhydra2_name
                                                     if (lookup('role_var', '_themepark_enabled', role='nzbhydra2') and global_themepark_plugin_enabled)
                                                     else '') }}"

    # Type: string
    nzbhydra2_role_traefik_middleware_custom: ""

    # Type: string
    nzbhydra2_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    nzbhydra2_role_traefik_enabled: true

    # Type: bool (true/false)
    nzbhydra2_role_traefik_api_enabled: true

    # Type: string
    nzbhydra2_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/getnzb`) || PathPrefix(`/gettorrent`) || PathPrefix(`/rss`) || PathPrefix(`/torznab/api`)"

    ```

??? example "Theme"

    ```yaml
    # Options can be found at https://github.com/themepark-dev/theme.park
    # Type: bool (true/false)
    nzbhydra2_role_themepark_enabled: false

    # Type: string
    nzbhydra2_role_themepark_app: "nzbhydra2"

    # Type: string
    nzbhydra2_role_themepark_theme: "{{ global_themepark_theme }}"

    # Type: string
    nzbhydra2_role_themepark_domain: "{{ global_themepark_domain }}"

    # Type: list
    nzbhydra2_role_themepark_addons: []

    ```

??? example "Config"

    ```yaml
    # Type: string
    nzbhydra2_role_config_settings_jvm_memory: "{{ ((ansible_memory_mb.real.total / 1024)
                                                   | round(0, 'ceil') | int >= 8)
                                                   | ternary('512', '256') }}"

    # Type: list
    nzbhydra2_role_config_settings_default: 
      # NZBGet
      - del(.downloading.downloaders)
      - .downloading.downloaders[0].apiKey = "{{ nzbhydra2_sabnzbd_api_lookup | default('not-found') }}"
      - .downloading.downloaders[0].defaultCategory = null
      - .downloading.downloaders[0].downloadType = "NZB" | .downloading.downloaders[0].downloadType style="double"
      - .downloading.downloaders[0].enabled = true
      - .downloading.downloaders[0].iconCssClass = ""
      - .downloading.downloaders[0].name = "SABnzbd" | .downloading.downloaders[0].name style="double"
      - .downloading.downloaders[0].nzbAddingType = "UPLOAD" | .downloading.downloaders[0].nzbAddingType style="double"
      - .downloading.downloaders[0].downloaderType = "SABNZBD" | .downloading.downloaders[0].downloaderType style="double"
      - .downloading.downloaders[0].url = "http://{{ lookup('role_var', '_docker_networks_alias', role='sabnzbd') }}:{{ lookup('role_var', '_web_port', role='sabnzbd') }}" | .downloading.downloaders[0].url style="double"
      - .downloading.downloaders[0].username = null
      - .downloading.downloaders[0].password = null
      - .downloading.downloaders[0].addPaused = false
      # JVM Memory. If RAM >= 8GB, set XMX to 512, else 256.
      - .main.xmx = {{ lookup('role_var', '_config_settings_jvm_memory', role='nzbhydra2') }}

    # Type: list
    nzbhydra2_role_config_settings_custom: []

    # Type: string
    nzbhydra2_role_config_settings_list: "{{ lookup('role_var', '_config_settings_default', role='nzbhydra2')
                                             + lookup('role_var', '_config_settings_custom', role='nzbhydra2') }}"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    nzbhydra2_role_docker_container: "{{ nzbhydra2_name }}"

    # Image
    # Type: bool (true/false)
    nzbhydra2_role_docker_image_pull: true

    # Type: string
    nzbhydra2_role_docker_image_repo: "lscr.io/linuxserver/nzbhydra2"

    # Type: string
    nzbhydra2_role_docker_image_tag: "latest"

    # Type: string
    nzbhydra2_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='nzbhydra2') }}:{{ lookup('role_var', '_docker_image_tag', role='nzbhydra2') }}"

    # Envs
    # Type: dict
    nzbhydra2_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      UMASK: "002"
      TZ: "{{ tz }}"

    # Type: dict
    nzbhydra2_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    nzbhydra2_role_docker_volumes_default: 
      - "{{ nzbhydra2_role_paths_location }}:/config"

    # Type: list
    nzbhydra2_role_docker_volumes_custom: []

    # Labels
    # Type: dict
    nzbhydra2_role_docker_labels_default: {}

    # Type: dict
    nzbhydra2_role_docker_labels_custom: {}

    # Hostname
    # Type: string
    nzbhydra2_role_docker_hostname: "{{ nzbhydra2_name }}"

    # Networks
    # Type: string
    nzbhydra2_role_docker_networks_alias: "{{ nzbhydra2_name }}"

    # Type: list
    nzbhydra2_role_docker_networks_default: []

    # Type: list
    nzbhydra2_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    nzbhydra2_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    nzbhydra2_role_docker_state: started


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    nzbhydra2_role_docker_blkio_weight:

    # Type: int
    nzbhydra2_role_docker_cpu_period:

    # Type: int
    nzbhydra2_role_docker_cpu_quota:

    # Type: int
    nzbhydra2_role_docker_cpu_shares:

    # Type: string
    nzbhydra2_role_docker_cpus:

    # Type: string
    nzbhydra2_role_docker_cpuset_cpus:

    # Type: string
    nzbhydra2_role_docker_cpuset_mems:

    # Type: string
    nzbhydra2_role_docker_kernel_memory:

    # Type: string
    nzbhydra2_role_docker_memory:

    # Type: string
    nzbhydra2_role_docker_memory_reservation:

    # Type: string
    nzbhydra2_role_docker_memory_swap:

    # Type: int
    nzbhydra2_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    nzbhydra2_role_docker_cap_drop:

    # Type: list
    nzbhydra2_role_docker_device_cgroup_rules:

    # Type: list
    nzbhydra2_role_docker_device_read_bps:

    # Type: list
    nzbhydra2_role_docker_device_read_iops:

    # Type: list
    nzbhydra2_role_docker_device_requests:

    # Type: list
    nzbhydra2_role_docker_device_write_bps:

    # Type: list
    nzbhydra2_role_docker_device_write_iops:

    # Type: list
    nzbhydra2_role_docker_devices:

    # Type: string
    nzbhydra2_role_docker_devices_default:

    # Type: bool (true/false)
    nzbhydra2_role_docker_privileged:

    # Type: list
    nzbhydra2_role_docker_security_opts:


    # Networking
    # Type: list
    nzbhydra2_role_docker_dns_opts:

    # Type: list
    nzbhydra2_role_docker_dns_search_domains:

    # Type: list
    nzbhydra2_role_docker_dns_servers:

    # Type: dict
    nzbhydra2_role_docker_hosts:

    # Type: string
    nzbhydra2_role_docker_hosts_use_common:

    # Type: string
    nzbhydra2_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    nzbhydra2_role_docker_keep_volumes:

    # Type: list
    nzbhydra2_role_docker_mounts:

    # Type: string
    nzbhydra2_role_docker_volume_driver:

    # Type: list
    nzbhydra2_role_docker_volumes_from:

    # Type: string
    nzbhydra2_role_docker_volumes_global:

    # Type: string
    nzbhydra2_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    nzbhydra2_role_docker_healthcheck:

    # Type: bool (true/false)
    nzbhydra2_role_docker_init:

    # Type: string
    nzbhydra2_role_docker_log_driver:

    # Type: dict
    nzbhydra2_role_docker_log_options:

    # Type: bool (true/false)
    nzbhydra2_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    nzbhydra2_role_docker_auto_remove:

    # Type: list
    nzbhydra2_role_docker_capabilities:

    # Type: string
    nzbhydra2_role_docker_cgroup_parent:

    # Type: string
    nzbhydra2_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    nzbhydra2_role_docker_cleanup:

    # Type: list
    nzbhydra2_role_docker_commands:

    # Type: string
    nzbhydra2_role_docker_create_timeout:

    # Type: string
    nzbhydra2_role_docker_domainname:

    # Type: string
    nzbhydra2_role_docker_entrypoint:

    # Type: string
    nzbhydra2_role_docker_env_file:

    # Type: list
    nzbhydra2_role_docker_exposed_ports:

    # Type: string
    nzbhydra2_role_docker_force_kill:

    # Type: list
    nzbhydra2_role_docker_groups:

    # Type: int
    nzbhydra2_role_docker_healthy_wait_timeout:

    # Type: string
    nzbhydra2_role_docker_ipc_mode:

    # Type: string
    nzbhydra2_role_docker_kill_signal:

    # Type: string
    nzbhydra2_role_docker_labels_use_common:

    # Type: list
    nzbhydra2_role_docker_links:

    # Type: bool (true/false)
    nzbhydra2_role_docker_oom_killer:

    # Type: int
    nzbhydra2_role_docker_oom_score_adj:

    # Type: bool (true/false)
    nzbhydra2_role_docker_paused:

    # Type: string
    nzbhydra2_role_docker_pid_mode:

    # Type: list
    nzbhydra2_role_docker_ports:

    # Type: bool (true/false)
    nzbhydra2_role_docker_read_only:

    # Type: bool (true/false)
    nzbhydra2_role_docker_recreate:

    # Type: int
    nzbhydra2_role_docker_restart_retries:

    # Type: string
    nzbhydra2_role_docker_runtime:

    # Type: string
    nzbhydra2_role_docker_shm_size:

    # Type: int
    nzbhydra2_role_docker_stop_timeout:

    # Type: dict
    nzbhydra2_role_docker_storage_opts:

    # Type: list
    nzbhydra2_role_docker_sysctls:

    # Type: list
    nzbhydra2_role_docker_tmpfs:

    # Type: list
    nzbhydra2_role_docker_ulimits:

    # Type: string
    nzbhydra2_role_docker_user:

    # Type: string
    nzbhydra2_role_docker_userns_mode:

    # Type: string
    nzbhydra2_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    nzbhydra2_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    nzbhydra2_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    nzbhydra2_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    nzbhydra2_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    nzbhydra2_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    nzbhydra2_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    nzbhydra2_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    nzbhydra2_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    nzbhydra2_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    nzbhydra2_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    nzbhydra2_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    nzbhydra2_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    nzbhydra2_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    nzbhydra2_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    nzbhydra2_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    nzbhydra2_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    nzbhydra2_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        nzbhydra2_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "nzbhydra22.{{ user.domain }}"
          - "nzbhydra2.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        nzbhydra2_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'nzbhydra22.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

## Next

Are you setting Saltbox up for the first time?  Continue to [Jackett](jackett.md).

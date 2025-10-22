---
hide:
  - tags
tags:
  - rutorrent
---

# ruTorrent

THIS PAGE HAS NOT BEEN FULLY UPDATED FOR SALTBOX

# What is it?

[ruTorrent](https://github.com/Novik/ruTorrent) (by Novik) is a front-end for the popular, lightweight, and extensible BitTorrent client [rtorrent](https://github.com/rakshasa/rtorrent) (by Jari Sundell aka rakshasa).

_Note: public trackers are disabled by default in the standard install.  Refer to the FAQ for [instructions on re-enabling them](../faq/rutorrent.md?h=public#enable-access-to-public-torrent-trackers)._

| Details     |             |             |             |             |
|-------------|-------------|-------------|-------------|-------------|
| :material-home: Project home | [:octicons-link-16: Docs](https://github.com/Novik/ruTorrent/wiki){: .header-icons } | [:octicons-mark-github-16: Github ruTorrent](https://github.com/Novik/ruTorrent){: .header-icons } | [:octicons-mark-github-16: Github rTorrent](https://github.com/rakshasa/rtorrent){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/horjulf/rutorrent-autodl){: .header-icons }|

## 1. URL

- To access ruTorrent, visit `https://rutorrent.xDOMAIN_NAMEx`

## 2. Basics

### Setup

The setup for [Sonarr](sonarr.md#__tabbed_4_5), [Radarr](radarr.md#__tabbed_4_5), and [Lidarr](lidarr.md#__tabbed_4_4) are done on their respective wiki pages.

## 3. Enable AutoUnpack

AutoUnpack is a plugin that will automatically unrar/unzip torrent data.

_This will allow Sonarr/Radarr/Lidarr to import the media files that would otherwise be ignored. After Sonarr and Radarr import the media files, [Torrent Cleanup Script](../reference/saltbox-tools.md#torrent-cleanup-script) will then delete the extracted media files and ruTorrent will continue to seed the torrents (until they are either removed manually or automatically via ruTorrent's Ratio Group rules)._

To enable AutoUnpack:

1. Open "Settings" by clicking the gear icon ![](https://github.com/Novik/ruTorrent/wiki/images/icon06settings.png) at the top

2. Go to "Unpack" on the left.

3. Check "Enable autounpacking if torrents label matches filter" and add the following:

```text
   /.*(radarr|sonarr|lidarr).*/i
```

4. Leave the other fields blank.

5. Your settings will now look like this:

   ![](https://i.imgur.com/LqE16E1.png)

6. Click "OK".

## 3. Custom Plugins and Themes

You can have custom plugins and themes imported during Docker container rebuild. Just place them in the following paths:

```text
/opt/rutorrent/plugins/
```

```text
/opt/rutorrent/themes/
```

And then restart the Docker container:

```shell
docker restart rutorrent
```

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        rutorrent_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `rutorrent_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `rutorrent_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    rutorrent_name: rutorrent

    ```

??? example "Paths"

    ```yaml
    # Type: string
    rutorrent_role_paths_folder: "{{ rutorrent_name }}"

    # Type: string
    rutorrent_role_paths_location: "{{ server_appdata_path }}/{{ rutorrent_role_paths_folder }}"

    # Type: string
    rutorrent_role_paths_downloads_location: "{{ downloads_torrents_path }}/{{ rutorrent_role_paths_folder }}"

    # Type: string
    rutorrent_role_paths_config_php_location: "{{ rutorrent_role_paths_location }}/rutorrent/settings/config.php"

    # Type: string
    rutorrent_role_paths_rtorrent_rc_location: "{{ rutorrent_role_paths_location }}/rtorrent/rtorrent.rc"

    # Type: string
    rutorrent_role_paths_php_local_ini_location: "{{ rutorrent_role_paths_location }}/php/php-local.ini"

    # Type: string
    rutorrent_role_paths_plugins_ini_location: "{{ rutorrent_role_paths_location }}/rutorrent/settings/plugins.ini"

    ```

??? example "Web"

    ```yaml
    # Type: string
    rutorrent_role_web_subdomain: "{{ rutorrent_name }}"

    # Type: string
    rutorrent_role_web_domain: "{{ user.domain }}"

    # Type: string
    rutorrent_role_web_port: "80"

    # Type: string
    rutorrent_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='rutorrent') + '.' + lookup('role_var', '_web_domain', role='rutorrent')
                             if (lookup('role_var', '_web_subdomain', role='rutorrent') | length > 0)
                             else lookup('role_var', '_web_domain', role='rutorrent')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    rutorrent_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='rutorrent') }}"

    # Type: string
    rutorrent_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='rutorrent') }}"

    # Type: bool (true/false)
    rutorrent_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    rutorrent_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    rutorrent_role_traefik_middleware_default: "{{ traefik_default_middleware
                                              + (',themepark-' + rutorrent_name
                                                if (lookup('role_var', '_themepark_enabled', role='rutorrent') and global_themepark_plugin_enabled)
                                                else '') }}"

    # Type: string
    rutorrent_role_traefik_middleware_custom: ""

    # Type: string
    rutorrent_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    rutorrent_role_traefik_enabled: true

    # Type: bool (true/false)
    rutorrent_role_traefik_api_enabled: true

    # Type: string
    rutorrent_role_traefik_api_middleware: "rutorrent-auth,{{ traefik_default_middleware_api }}"

    # Type: string
    rutorrent_role_traefik_api_endpoint: "PathPrefix(`/RPC2`)"

    ```

??? example "Config"

    ```yaml
    # Toggles if public tracker functionality is enabled
    # Type: bool (true/false)
    rutorrent_role_config_public_trackers: false

    # Path used by the diskspace plugin to check usage
    # Type: string
    rutorrent_role_config_diskspace_path: "/mnt"

    # Type: list
    rutorrent_role_config_new_installs_rutorrent_rc_settings_default: 
      # Minimum number of peers to connect to per torrent
      - { option: "throttle.min_peers.normal.set", value: "1" }
      # Maximum number of simultaneous upload slots per torrent
      - { option: "throttle.max_uploads.set", value: "1024" }
      # Maximum number of simultaneous download slots, globally
      - { option: "throttle.max_downloads.global.set", value: "1024" }
      # Maximum number of simultaneous upload slots, globally
      - { option: "throttle.max_uploads.global.set", value: "1024" }
      # Maximum download rate, globally (KiB); 0 = unlimited
      - { option: "throttle.global_down.max_rate.set_kb", value: "0" }
      # Maximum upload rate, globally (KiB); 0 = unlimited
      - { option: "throttle.global_up.max_rate.set_kb", value: "0" }
      # Maximum number of open files
      - { option: "network.max_open_files.set", value: "1024" }
      # Maximum XMLRPC payloads
      - { option: "network.xmlrpc.size_limit.set", value: "20M" }
      # Encryption Parameters
      - { option: "protocol.encryption.set", value: "allow_incoming,try_outgoing,enable_retry,prefer_plaintext" }
      # Hash check on completion - disabled
      - { option: "pieces.hash.on_completion.set", value: "no" }
      # Disk space allocation - disabled
      - { option: "system.file.allocate.set", value: "0" }
      # Download Directory
      - { option: "directory.default.set", value: "/mnt/unionfs/downloads/torrents/rutorrent/completed" }
      # Watched Directory
      - { option: "schedule", value: 'watch_directory,5,5,"load.start=/mnt/unionfs/downloads/torrents/rutorrent/watched/*.torrent,d.delete_tied="' }

    # Type: list
    rutorrent_role_config_new_installs_rutorrent_rc_settings_custom: []

    # Type: string
    rutorrent_role_config_new_installs_rutorrent_rc_settings_list: "{{ lookup('role_var', '_config_new_installs_rutorrent_rc_settings_default', role='rutorrent')
                                                                       + lookup('role_var', '_config_new_installs_rutorrent_rc_settings_custom', role='rutorrent') }}"

    # Type: list
    rutorrent_role_config_new_installs_php_local_ini_settings_default: 
      # Maximum Upload File Size via Web Browser (eg Uploading Torrent Files)
      - { option: "upload_max_filesize", value: "20M" }

    # Type: list
    rutorrent_role_config_new_installs_php_local_ini_settings_custom: []

    # Type: string
    rutorrent_role_config_new_installs_php_local_ini_settings_list: "{{ lookup('role_var', '_config_new_installs_php_local_ini_settings_default', role='rutorrent')
                                                                        + lookup('role_var', '_config_new_installs_php_local_ini_settings_custom', role='rutorrent') }}"

    # Type: list
    rutorrent_role_config_existing_installs_rutorrent_rc_settings_default: 
      # Execute - Initiate Plugins
      - { option: "execute", value: "{sh,-c,/usr/bin/php /app/rutorrent/php/initplugins.php abc &}" }
      # IP address that is reported to the tracker
      - { option: "network.local_address.set", value: "{{ ip_address_public }}" }
      # Ports
      - { option: "network.port_range.set", value: "{{ rutorrent_role_docker_ports_51413 }}-{{ rutorrent_role_docker_ports_51413 }}" }
      - { option: "dht.port.set", value: "{{ rutorrent_role_docker_ports_6881 }}" }
      # Enable / Disable Public Trackers
      - { option: "dht.mode.set", value: "{{ lookup('role_var', '_config_public_trackers', role='rutorrent') | ternary('on', 'disable') }}" }
      - { option: "trackers.use_udp.set", value: "{{ lookup('role_var', '_config_public_trackers', role='rutorrent') | ternary('yes', 'no') }}" }
      - { option: "protocol.pex.set", value: "{{ lookup('role_var', '_config_public_trackers', role='rutorrent') | ternary('yes', 'no') }}" }

    # Type: list
    rutorrent_role_config_existing_installs_rutorrent_rc_settings_custom: []

    # Type: string
    rutorrent_role_config_existing_installs_rutorrent_rc_settings_list: "{{ lookup('role_var', '_config_existing_installs_rutorrent_rc_settings_default', role='rutorrent')
                                                                            + lookup('role_var', '_config_existing_installs_rutorrent_rc_settings_custom', role='rutorrent') }}"

    ```

??? example "Theme"

    ```yaml
    # Options can be found at https://github.com/themepark-dev/theme.park
    # Type: bool (true/false)
    rutorrent_role_themepark_enabled: false

    # Type: string
    rutorrent_role_themepark_app: "rutorrent"

    # Type: string
    rutorrent_role_themepark_theme: "{{ global_themepark_theme }}"

    # Type: string
    rutorrent_role_themepark_domain: "{{ global_themepark_domain }}"

    # Type: list
    rutorrent_role_themepark_addons: []

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    rutorrent_role_docker_container: "{{ rutorrent_name }}"

    # Image
    # Type: bool (true/false)
    rutorrent_role_docker_image_pull: true

    # Type: string
    rutorrent_role_docker_image_tag: "latest"

    # Type: string
    rutorrent_role_docker_image_repo: "kudeta/ru-rtorrent"

    # Type: string
    rutorrent_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='rutorrent') }}:{{ lookup('role_var', '_docker_image_tag', role='rutorrent') }}"

    # Ports
    # Type: string
    rutorrent_role_docker_ports_51413: "{{ port_lookup_51413.meta.port
                                        if (port_lookup_51413.meta.port is defined) and (port_lookup_51413.meta.port | trim | length > 0)
                                        else '51413' }}"

    # Type: string
    rutorrent_role_docker_ports_6881: "{{ port_lookup_6881.meta.port
                                       if (port_lookup_6881.meta.port is defined) and (port_lookup_6881.meta.port | trim | length > 0)
                                       else '6881' }}"

    # Type: list
    rutorrent_role_docker_ports_defaults: 
      - "{{ lookup('role_var', '_docker_ports_51413', role='rutorrent') }}:{{ lookup('role_var', '_docker_ports_51413', role='rutorrent') }}"
      - "{{ lookup('role_var', '_docker_ports_51413', role='rutorrent') }}:{{ lookup('role_var', '_docker_ports_51413', role='rutorrent') }}/udp"
      - "{{ lookup('role_var', '_docker_ports_6881', role='rutorrent') }}:{{ lookup('role_var', '_docker_ports_6881', role='rutorrent') }}/udp"

    # Type: list
    rutorrent_role_docker_ports_custom: []

    # Envs
    # Type: dict
    rutorrent_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    rutorrent_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    rutorrent_role_docker_volumes_default: 
      - "{{ rutorrent_role_paths_location }}:/config"
      - "{{ server_appdata_path }}/scripts:/scripts"

    # Type: list
    rutorrent_role_docker_volumes_custom: []

    # Labels
    # Type: dict
    rutorrent_role_docker_labels_default: 
      traefik.http.middlewares.rutorrent-auth.basicauth.usersfile: "/etc/traefik/auth"

    # Type: dict
    rutorrent_role_docker_labels_custom: {}

    # Hostname
    # Type: string
    rutorrent_role_docker_hostname: "{{ rutorrent_name }}"

    # Networks
    # Type: string
    rutorrent_role_docker_networks_alias: "{{ rutorrent_name }}"

    # Type: list
    rutorrent_role_docker_networks_default: []

    # Type: list
    rutorrent_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    rutorrent_role_docker_restart_policy: unless-stopped

    # Stop Timeout
    # Type: int
    rutorrent_role_docker_stop_timeout: 900

    # State
    # Type: string
    rutorrent_role_docker_state: started


    # ---- Additional Docker Options ----
    # The following advanced options are available via create_docker_container
    # but are not defined in the role. See:
    # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    # Resource Limits
    # Type: int
    rutorrent_role_docker_blkio_weight:

    # Type: int
    rutorrent_role_docker_cpu_period:

    # Type: int
    rutorrent_role_docker_cpu_quota:

    # Type: int
    rutorrent_role_docker_cpu_shares:

    # Type: string
    rutorrent_role_docker_cpus:

    # Type: string
    rutorrent_role_docker_cpuset_cpus:

    # Type: string
    rutorrent_role_docker_cpuset_mems:

    # Type: string
    rutorrent_role_docker_kernel_memory:

    # Type: string
    rutorrent_role_docker_memory:

    # Type: string
    rutorrent_role_docker_memory_reservation:

    # Type: string
    rutorrent_role_docker_memory_swap:

    # Type: int
    rutorrent_role_docker_memory_swappiness:


    # Security & Devices
    # Type: list
    rutorrent_role_docker_cap_drop:

    # Type: list
    rutorrent_role_docker_device_cgroup_rules:

    # Type: list
    rutorrent_role_docker_device_read_bps:

    # Type: list
    rutorrent_role_docker_device_read_iops:

    # Type: list
    rutorrent_role_docker_device_requests:

    # Type: list
    rutorrent_role_docker_device_write_bps:

    # Type: list
    rutorrent_role_docker_device_write_iops:

    # Type: list
    rutorrent_role_docker_devices:

    # Type: string
    rutorrent_role_docker_devices_default:

    # Type: bool (true/false)
    rutorrent_role_docker_privileged:

    # Type: list
    rutorrent_role_docker_security_opts:


    # Networking
    # Type: list
    rutorrent_role_docker_dns_opts:

    # Type: list
    rutorrent_role_docker_dns_search_domains:

    # Type: list
    rutorrent_role_docker_dns_servers:

    # Type: dict
    rutorrent_role_docker_hosts:

    # Type: string
    rutorrent_role_docker_hosts_use_common:

    # Type: string
    rutorrent_role_docker_network_mode:


    # Storage
    # Type: bool (true/false)
    rutorrent_role_docker_keep_volumes:

    # Type: list
    rutorrent_role_docker_mounts:

    # Type: string
    rutorrent_role_docker_volume_driver:

    # Type: list
    rutorrent_role_docker_volumes_from:

    # Type: string
    rutorrent_role_docker_volumes_global:

    # Type: string
    rutorrent_role_docker_working_dir:


    # Monitoring & Lifecycle
    # Type: dict
    rutorrent_role_docker_healthcheck:

    # Type: bool (true/false)
    rutorrent_role_docker_init:

    # Type: string
    rutorrent_role_docker_log_driver:

    # Type: dict
    rutorrent_role_docker_log_options:

    # Type: bool (true/false)
    rutorrent_role_docker_output_logs:


    # Other Options
    # Type: bool (true/false)
    rutorrent_role_docker_auto_remove:

    # Type: list
    rutorrent_role_docker_capabilities:

    # Type: string
    rutorrent_role_docker_cgroup_parent:

    # Type: string
    rutorrent_role_docker_cgroupns_mode:

    # Type: bool (true/false)
    rutorrent_role_docker_cleanup:

    # Type: list
    rutorrent_role_docker_commands:

    # Type: string
    rutorrent_role_docker_create_timeout:

    # Type: string
    rutorrent_role_docker_domainname:

    # Type: string
    rutorrent_role_docker_entrypoint:

    # Type: string
    rutorrent_role_docker_env_file:

    # Type: list
    rutorrent_role_docker_exposed_ports:

    # Type: string
    rutorrent_role_docker_force_kill:

    # Type: list
    rutorrent_role_docker_groups:

    # Type: int
    rutorrent_role_docker_healthy_wait_timeout:

    # Type: string
    rutorrent_role_docker_ipc_mode:

    # Type: string
    rutorrent_role_docker_kill_signal:

    # Type: string
    rutorrent_role_docker_labels_use_common:

    # Type: list
    rutorrent_role_docker_links:

    # Type: bool (true/false)
    rutorrent_role_docker_oom_killer:

    # Type: int
    rutorrent_role_docker_oom_score_adj:

    # Type: bool (true/false)
    rutorrent_role_docker_paused:

    # Type: string
    rutorrent_role_docker_pid_mode:

    # Type: bool (true/false)
    rutorrent_role_docker_read_only:

    # Type: bool (true/false)
    rutorrent_role_docker_recreate:

    # Type: int
    rutorrent_role_docker_restart_retries:

    # Type: string
    rutorrent_role_docker_runtime:

    # Type: string
    rutorrent_role_docker_shm_size:

    # Type: dict
    rutorrent_role_docker_storage_opts:

    # Type: list
    rutorrent_role_docker_sysctls:

    # Type: list
    rutorrent_role_docker_tmpfs:

    # Type: list
    rutorrent_role_docker_ulimits:

    # Type: string
    rutorrent_role_docker_user:

    # Type: string
    rutorrent_role_docker_userns_mode:

    # Type: string
    rutorrent_role_docker_uts:

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    rutorrent_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    rutorrent_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    rutorrent_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    rutorrent_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    rutorrent_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    rutorrent_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    rutorrent_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    rutorrent_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    rutorrent_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    rutorrent_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    rutorrent_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    rutorrent_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    rutorrent_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    rutorrent_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    rutorrent_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    rutorrent_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    rutorrent_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        rutorrent_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "rutorrent2.{{ user.domain }}"
          - "rutorrent.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        rutorrent_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'rutorrent2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

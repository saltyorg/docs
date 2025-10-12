---
hide:
  - tags
tags:
  - lidarr
---

# Lidarr

# What is it?

[Lidarr](https://lidarr.audio) is basically Sonarr for music. It functions as a music collection manager for Usenet and BitTorrent users. It can monitor multiple RSS feeds from Bittorrent trackers and Usenet Indexers, looking for new tracks from your favorite artists and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://lidarr.audio){: .header-icons } | [:octicons-link-16: Docs](https://wiki.servarr.com/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Lidarr/Lidarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/lidarr){: .header-icons }|

## URL

- To access Lidarr, visit `https://lidarr._yourdomain.com_`

## Settings

Click on "Settings" in the sidebar.  Click "Show Advanced" at the top of the Settings pane.

Make changes in the following sections:

!!! info "Settings"

    === "Media Management"

        These settings control management of media files.

        === "Movie Naming"

            - "Rename Tracks": `Yes`

            - "Replace Illegal Characters": `Yes`

            - Set your preferred naming format; here are some examples.

            <details>
            <summary>Plex's Naming Preference</summary> <br />

            Example: <br />
            ```
            01 - Shine On You Crazy Diamond (Parts I-V).m4a
            ```

            Standard Track Format: <br />
            ```
            {track:00} - {Track Title}
            ```

            Artist Folder Format: <br />
            ```
            {Artist Name}
            ```

            Album Folder Format: <br />
            ```
            {Artist Name} - {Album Title}
            ```

            Reference: https://support.plex.tv/articles/categories/media-preparation/naming-and-organizing-music-media/
            </details>

        === "Folders"

            - "Create empty artist folders": `No`

            - "Delete empty folders": `No`

        === "Importing"

            - "Skip Free Space Check": `No`

            - "Minimum Free Space": `100` (_can be your preference so long as you use a reasonable value_)

            - "Use Hardlinks instead of Copy": `Yes`

            - "Import Extra Files": `Yes` (_can be your preference_)

            - "Extra File Extensions": `srt` (_can be your preference_)

        === "File Management"

            - "Ignore Deleted Tracks": `No` (_can be your preference_)

            - "Propers and Repacks": `Prefer and Upgrade` (_can be your preference_)

            - "Watch Root Folders for file changes": 'Yes'

            - "Rescan Artist Folder after Refresh": `Never`

            - "Allow Fingerprinting": `For new imports only`

            - "Change File Date": `Album Release Date` (_can be your preference_)

            - "Recycle Bin": _blank_ (Rclone deletes are sent to Gdrive trash folder, anyway)

            - "Recycling Bin Cleanup": '0'

        === "Permissions"

            - Set Permissions: `No`

        === "Save"

            - Click "Save".

    === "Indexers"

        These settings control [indexers](../saltbox/prerequisites/prerequisites.md#usenet-or-bittorrent-sources) and related behavior.

        === "NZBHydra2"

            1. Click Add Indexer (`+`).

            2. Select "Newznab".

            3. Add the following:

                Name: NZBHydra2

                Enable RSS Sync: _Your Preference_

                Enable Automatic Search: _Your Preference_

                Enable Interactive Search: _Your Preference_

                URL: `http://nzbhydra2:5076`

                API Key: [Your NZBHydra2 API Key](../apps/nzbhydra2.md)

                Early Download Limit: _Your Preference_

                Additional Parameters: _Leave Blank_

            4. Your settings will look like this:

                ![Lidarr NZBHydra2](../images/lidarr/lidarr-nzbhydra.png)

            5. Click "Save" to add NZBHydra2.

            Note: The "Test" will keep failing until you add an indexer in [NZBHydra2](../apps/nzbhydra2.md).

        === "Jackett"

            Note: Each Indexer you have defined in Jackett will need to be added separately.

            1. Click Add Indexer (`+`)

            2. Select "Torznab".

            3. Add the following:

                Name: Indexer Name

                Enable RSS Sync: _Your Preference_

                Enable Automatic Search: _Your Preference_

                Enable Interactive Search: _Your Preference_

                URL: [Indexer's Torznab Feed](../apps/jackett.md)

                API Key: [Your Jackett API Key](../apps/jackett.md)

                Early Download Limit: _Your Preference_

                Additional Parameters: _Leave Blank_

            4. Your settings will look like this:

                ![Lidarr Jackett](../images/lidarr/lidarr-jackett.png)

            5. Click "Save" to add the indexer.


    === "Download Clients"

        These settings control downloading behavior and clients.

        === "Completed Download Handling"

            - "Enable": `Yes`

            - "Remove": `Yes` (_can be your preference_)

        === "Failed Download Handling"

            - "Redownload": `Yes`

            - "Remove": `Yes`

        === "NZBGet"

            1. Click Add (`+`)

            2. Add a new "NZBGet" download client.

            3. Add the following:

                Name: NZBGet

                Enable: `Yes`

                Host: `nzbget`

                Port: `6789`

                Username:  [Your NZBGet Username](../apps/nzbget.md)

                Password:  [Your NZBGet Password](../apps/nzbget.md)

                Category: `lidarr`

                Use SSL: `No`

                Add Paused: `No`

            4. Your settings will look like this:

                ![Lidarr NZBGet Downloader](../images/lidarr/01-lidarr-nzbget.png)

            5. Click "Save" to add NZBGet.

        === "ruTorrent"

            1. Click Add (`+`)

            2. Add a new "rTorrent" download client.

            3. Add the following:

                Name: ruTorrent

                Enable: `Yes`

                Host: `rutorrent`

                Port: `80`

                URL Path: `RPC2`

                Use SSL: `No`

                Username: [Your ruTorrent Username](../apps/rutorrent.md)

                Password: [Your ruTorrent Password](../apps/rutorrent.md)

                Category: `lidarr`

                Directory: _Leave Blank_

            4.  Your settings will now look like this:

                ![Radarr ruTorrent Downloader](../images/lidarr/lidarr-rtorrent.png)

            5. Click "Save" to add ruTorrent.

        === "qBittorrent"

            1. Click Add ('+')

            2. Add a new "qBittorrent" download client.

            3. Add the following:

                Name: qBittorrent

                Enable: 'Yes'

                Host: 'qBittorrent'

                Port: '8080'

                Username: [Your qBittorrent Username](../apps/qbittorrent.md)

                Password: [Your qBittorrent Password](../apps/qbittorrent.md)

                Category: 'lidarr'

            4.  Your settings will now look like this:

                ![Lidarr qBittorent Downloader](../images/lidarr/lidarr-qbittorrent.png)

            5.  Click "Save" to add qBittorrent qb

    === "Connect"

        These settings control connections to other applications or systems.

        === "Torrent Cleanup"

            Torrent Cleanup Script is a custom script that will clean up torrents from ruTorrent that were auto-extracted, but still being seeded. So if the script detects that `.rar` files are in the folder that Radarr just imported from, it will delete the imported audio file(s), leaving just the `.rar` files for seeding.

            1. Click "Settings" -> "Connect".

            2. Add a new "Custom Script".

            3. Add the following:

                Name: Torrent Cleanup

                On Grab: `No`

                On Release Import: `Yes`

                On Upgrade:  `Yes`

                On Rename:`No`

                Path: `/scripts/torrents/TorrentCleanup.py`

            4. The settings will look like this:

                ![Lidarr Torrent Cleanup Script CloudBox](../images/lidarr/lidarr-torrentcleanup.png)

            5. Click "Save" to add the Torrent Cleanup script.

        === "Autoscan"

            1. Click "Settings" -> "Connect".

            2. Add a new "Webhook".

            3. Add the following:

                Name: Autoscan

                On Grab: `No`

                On Release Import: `Yes`

                On Upgrade:  `Yes`

                On Rename: `Yes`

                On Track Retag: `No`

                On Health Issue: `No`

                Tags: _Leave Blank_

                URL: `http://autoscan:3030/triggers/lidarr`

                Method:`POST`

                Username: AS SET IN AUTOSCAN CONFIG [defaults to Saltbox Username]

                Password: AS SET IN AUTOSCAN CONFIG [defaults to Saltbox Password]

            4. The settings will look like this:

                ![lidarr Autoscan](../images/lidarr/lidarr-autoscan.png)

            5. Click "Save" to add Autoscan.

    === "General"

        These settings control general aspects of Radarr.

        === "Start-Up"

            - "Bind Address: `*`

            - "Port Number": `8686`

            - "URL Base": _blank_

            - "Enable SSL": `No` (_SSL is handled by Traefik_)

            - "Open browser on start": `No`

        === "Proxy Settings"

            - "Use Proxy": `No`

        === "Logging"

            - "Log Level": `Debug`

        === "Analytics"

            - "Send Anonymous Usage Data": `No` (_your preference_)

        === "Updates"

            - "Branch": `develop`

            - "Automatic": `Off`

        === "Save"

            - Click "Save".

## Music Path

1. When you are ready to add your first artist to Lidarr, click the "Path" drop-down and select "Add a different path".

1. Click the blue "Browse" button, navigate to `/mnt/unionfs/Media/Music`, scroll to the bottom, and select "OK".

1. Click the green "check" button to add the path.

1. All artists added now will have that path set.

## API Key

This is used during the setup of [Organizr](organizr.md).

- Go to "Settings" -> "General" -> "Security" -> "API Key".

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `lidarr_instances`.

    === "Role-level Override"

        Applies to all instances of lidarr:

        ```yaml
        lidarr_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `lidarr2`):

        ```yaml
        lidarr2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `lidarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `lidarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        lidarr_instances: ["lidarr"]

        ```

    === "Example"

        ```yaml
        # Type: list
        lidarr_instances: ["lidarr", "lidarr2"]

        ```

??? example "Settings"

    === "Role-level"

        ```yaml
        # Type: bool (true/false)
        lidarr_role_external_auth: true

        ```

    === "Instance-level"

        ```yaml
        # Type: bool (true/false)
        lidarr2_external_auth: true

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        lidarr_role_paths_folder: "{{ lidarr_name }}"

        # Type: string
        lidarr_role_paths_location: "{{ server_appdata_path }}/{{ lidarr_role_paths_folder }}"

        # Type: string
        lidarr_role_paths_config_location: "{{ lidarr_role_paths_location }}/config.xml"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        lidarr2_paths_folder: "{{ lidarr_name }}"

        # Type: string
        lidarr2_paths_location: "{{ server_appdata_path }}/{{ lidarr_role_paths_folder }}"

        # Type: string
        lidarr2_paths_config_location: "{{ lidarr_role_paths_location }}/config.xml"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        lidarr_role_web_subdomain: "{{ lidarr_name }}"

        # Type: string
        lidarr_role_web_domain: "{{ user.domain }}"

        # Type: string
        lidarr_role_web_port: "8686"

        # Type: string
        lidarr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='lidarr') + '.' + lookup('role_var', '_web_domain', role='lidarr')
                              if (lookup('role_var', '_web_subdomain', role='lidarr') | length > 0)
                              else lookup('role_var', '_web_domain', role='lidarr')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        lidarr2_web_subdomain: "{{ lidarr_name }}"

        # Type: string
        lidarr2_web_domain: "{{ user.domain }}"

        # Type: string
        lidarr2_web_port: "8686"

        # Type: string
        lidarr2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='lidarr') + '.' + lookup('role_var', '_web_domain', role='lidarr')
                          if (lookup('role_var', '_web_subdomain', role='lidarr') | length > 0)
                          else lookup('role_var', '_web_domain', role='lidarr')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        lidarr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='lidarr') }}"

        # Type: string
        lidarr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='lidarr') }}"

        # Type: bool (true/false)
        lidarr_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        lidarr2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='lidarr') }}"

        # Type: string
        lidarr2_dns_zone: "{{ lookup('role_var', '_web_domain', role='lidarr') }}"

        # Type: bool (true/false)
        lidarr2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        lidarr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        lidarr_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                    + (',themepark-' + lidarr_name
                                                      if (lookup('role_var', '_themepark_enabled', role='lidarr') and global_themepark_plugin_enabled)
                                                      else '') }}"

        # Type: string
        lidarr_role_traefik_middleware_custom: ""

        # Type: string
        lidarr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        lidarr_role_traefik_enabled: true

        # Type: bool (true/false)
        lidarr_role_traefik_api_enabled: true

        # Type: string
        lidarr_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/feed`) || PathPrefix(`/ping`)"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        lidarr2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        lidarr2_traefik_middleware_default: "{{ traefik_default_middleware
                                                + (',themepark-' + lidarr_name
                                                  if (lookup('role_var', '_themepark_enabled', role='lidarr') and global_themepark_plugin_enabled)
                                                  else '') }}"

        # Type: string
        lidarr2_traefik_middleware_custom: ""

        # Type: string
        lidarr2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        lidarr2_traefik_enabled: true

        # Type: bool (true/false)
        lidarr2_traefik_api_enabled: true

        # Type: string
        lidarr2_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/feed`) || PathPrefix(`/ping`)"

        ```

??? example "Theme"

    === "Role-level"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        lidarr_role_themepark_enabled: false

        # Type: string
        lidarr_role_themepark_app: "lidarr"

        # Type: string
        lidarr_role_themepark_theme: "{{ global_themepark_theme }}"

        # Type: string
        lidarr_role_themepark_domain: "{{ global_themepark_domain }}"

        # Type: list
        lidarr_role_themepark_addons: []

        ```

    === "Instance-level"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        lidarr2_themepark_enabled: false

        # Type: string
        lidarr2_themepark_app: "lidarr"

        # Type: string
        lidarr2_themepark_theme: "{{ global_themepark_theme }}"

        # Type: string
        lidarr2_themepark_domain: "{{ global_themepark_domain }}"

        # Type: list
        lidarr2_themepark_addons: []

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        lidarr_role_docker_container: "{{ lidarr_name }}"

        # Image
        # Type: bool (true/false)
        lidarr_role_docker_image_pull: true

        # Type: string
        lidarr_role_docker_image_repo: "ghcr.io/hotio/lidarr"

        # Type: string
        lidarr_role_docker_image_tag: "release"

        # Type: string
        lidarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='lidarr') }}:{{ lookup('role_var', '_docker_image_tag', role='lidarr') }}"

        # Envs
        # Type: dict
        lidarr_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          UMASK: "002"
          TZ: "{{ tz }}"

        # Type: dict
        lidarr_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        lidarr_role_docker_volumes_default: 
          - "{{ lidarr_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"

        # Type: list
        lidarr_role_docker_volumes_legacy: 
          - "/mnt/unionfs/Media/Music:/music"

        # Type: list
        lidarr_role_docker_volumes_custom: []

        # Labels
        # Type: dict
        lidarr_role_docker_labels_default: {}

        # Type: dict
        lidarr_role_docker_labels_custom: {}

        # Hostname
        # Type: string
        lidarr_role_docker_hostname: "{{ lidarr_name }}"

        # Networks
        # Type: string
        lidarr_role_docker_networks_alias: "{{ lidarr_name }}"

        # Type: list
        lidarr_role_docker_networks_default: []

        # Type: list
        lidarr_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        lidarr_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        lidarr_role_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via create_docker_container
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        lidarr_role_docker_blkio_weight:

        # Type: int
        lidarr_role_docker_cpu_period:

        # Type: int
        lidarr_role_docker_cpu_quota:

        # Type: int
        lidarr_role_docker_cpu_shares:

        # Type: string
        lidarr_role_docker_cpus:

        # Type: string
        lidarr_role_docker_cpuset_cpus:

        # Type: string
        lidarr_role_docker_cpuset_mems:

        # Type: string
        lidarr_role_docker_kernel_memory:

        # Type: string
        lidarr_role_docker_memory:

        # Type: string
        lidarr_role_docker_memory_reservation:

        # Type: string
        lidarr_role_docker_memory_swap:

        # Type: int
        lidarr_role_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        lidarr_role_docker_cap_drop:

        # Type: list
        lidarr_role_docker_device_cgroup_rules:

        # Type: list
        lidarr_role_docker_device_read_bps:

        # Type: list
        lidarr_role_docker_device_read_iops:

        # Type: list
        lidarr_role_docker_device_requests:

        # Type: list
        lidarr_role_docker_device_write_bps:

        # Type: list
        lidarr_role_docker_device_write_iops:

        # Type: list
        lidarr_role_docker_devices:

        # Type: string
        lidarr_role_docker_devices_default:

        # Type: bool (true/false)
        lidarr_role_docker_privileged:

        # Type: list
        lidarr_role_docker_security_opts:

        # Networking
        # Type: list
        lidarr_role_docker_dns_opts:

        # Type: list
        lidarr_role_docker_dns_search_domains:

        # Type: list
        lidarr_role_docker_dns_servers:

        # Type: dict
        lidarr_role_docker_hosts:

        # Type: string
        lidarr_role_docker_hosts_use_common:

        # Type: string
        lidarr_role_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        lidarr_role_docker_keep_volumes:

        # Type: list
        lidarr_role_docker_mounts:

        # Type: string
        lidarr_role_docker_volume_driver:

        # Type: list
        lidarr_role_docker_volumes_from:

        # Type: string
        lidarr_role_docker_volumes_global:

        # Type: string
        lidarr_role_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        lidarr_role_docker_healthcheck:

        # Type: bool (true/false)
        lidarr_role_docker_init:

        # Type: string
        lidarr_role_docker_log_driver:

        # Type: dict
        lidarr_role_docker_log_options:

        # Type: bool (true/false)
        lidarr_role_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        lidarr_role_docker_auto_remove:

        # Type: list
        lidarr_role_docker_capabilities:

        # Type: string
        lidarr_role_docker_cgroup_parent:

        # Type: string
        lidarr_role_docker_cgroupns_mode:

        # Type: bool (true/false)
        lidarr_role_docker_cleanup:

        # Type: list
        lidarr_role_docker_commands:

        # Type: string
        lidarr_role_docker_create_timeout:

        # Type: string
        lidarr_role_docker_domainname:

        # Type: string
        lidarr_role_docker_entrypoint:

        # Type: string
        lidarr_role_docker_env_file:

        # Type: list
        lidarr_role_docker_exposed_ports:

        # Type: string
        lidarr_role_docker_force_kill:

        # Type: list
        lidarr_role_docker_groups:

        # Type: int
        lidarr_role_docker_healthy_wait_timeout:

        # Type: string
        lidarr_role_docker_ipc_mode:

        # Type: string
        lidarr_role_docker_kill_signal:

        # Type: string
        lidarr_role_docker_labels_use_common:

        # Type: list
        lidarr_role_docker_links:

        # Type: bool (true/false)
        lidarr_role_docker_oom_killer:

        # Type: int
        lidarr_role_docker_oom_score_adj:

        # Type: bool (true/false)
        lidarr_role_docker_paused:

        # Type: string
        lidarr_role_docker_pid_mode:

        # Type: list
        lidarr_role_docker_ports:

        # Type: bool (true/false)
        lidarr_role_docker_read_only:

        # Type: bool (true/false)
        lidarr_role_docker_recreate:

        # Type: int
        lidarr_role_docker_restart_retries:

        # Type: string
        lidarr_role_docker_runtime:

        # Type: string
        lidarr_role_docker_shm_size:

        # Type: int
        lidarr_role_docker_stop_timeout:

        # Type: dict
        lidarr_role_docker_storage_opts:

        # Type: list
        lidarr_role_docker_sysctls:

        # Type: list
        lidarr_role_docker_tmpfs:

        # Type: list
        lidarr_role_docker_ulimits:

        # Type: string
        lidarr_role_docker_user:

        # Type: string
        lidarr_role_docker_userns_mode:

        # Type: string
        lidarr_role_docker_uts:

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        lidarr2_docker_container: "{{ lidarr_name }}"

        # Image
        # Type: bool (true/false)
        lidarr2_docker_image_pull: true

        # Type: string
        lidarr2_docker_image_repo: "ghcr.io/hotio/lidarr"

        # Type: string
        lidarr2_docker_image_tag: "release"

        # Type: string
        lidarr2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='lidarr') }}:{{ lookup('role_var', '_docker_image_tag', role='lidarr') }}"

        # Envs
        # Type: dict
        lidarr2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          UMASK: "002"
          TZ: "{{ tz }}"

        # Type: dict
        lidarr2_docker_envs_custom: {}

        # Volumes
        # Type: list
        lidarr2_docker_volumes_default: 
          - "{{ lidarr_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"

        # Type: list
        lidarr2_docker_volumes_legacy: 
          - "/mnt/unionfs/Media/Music:/music"

        # Type: list
        lidarr2_docker_volumes_custom: []

        # Labels
        # Type: dict
        lidarr2_docker_labels_default: {}

        # Type: dict
        lidarr2_docker_labels_custom: {}

        # Hostname
        # Type: string
        lidarr2_docker_hostname: "{{ lidarr_name }}"

        # Networks
        # Type: string
        lidarr2_docker_networks_alias: "{{ lidarr_name }}"

        # Type: list
        lidarr2_docker_networks_default: []

        # Type: list
        lidarr2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        lidarr2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        lidarr2_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via lookup('docker_var', ...)
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        lidarr2_docker_blkio_weight:
        # Type: int
        lidarr2_docker_cpu_period:
        # Type: int
        lidarr2_docker_cpu_quota:
        # Type: int
        lidarr2_docker_cpu_shares:
        # Type: string
        lidarr2_docker_cpus:
        # Type: string
        lidarr2_docker_cpuset_cpus:
        # Type: string
        lidarr2_docker_cpuset_mems:
        # Type: string
        lidarr2_docker_kernel_memory:
        # Type: string
        lidarr2_docker_memory:
        # Type: string
        lidarr2_docker_memory_reservation:
        # Type: string
        lidarr2_docker_memory_swap:
        # Type: int
        lidarr2_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        lidarr2_docker_cap_drop:
        # Type: list
        lidarr2_docker_device_cgroup_rules:
        # Type: list
        lidarr2_docker_device_read_bps:
        # Type: list
        lidarr2_docker_device_read_iops:
        # Type: list
        lidarr2_docker_device_requests:
        # Type: list
        lidarr2_docker_device_write_bps:
        # Type: list
        lidarr2_docker_device_write_iops:
        # Type: list
        lidarr2_docker_devices:
        # Type: string
        lidarr2_docker_devices_default:
        # Type: bool (true/false)
        lidarr2_docker_privileged:
        # Type: list
        lidarr2_docker_security_opts:

        # Networking
        # Type: list
        lidarr2_docker_dns_opts:
        # Type: list
        lidarr2_docker_dns_search_domains:
        # Type: list
        lidarr2_docker_dns_servers:
        # Type: dict
        lidarr2_docker_hosts:
        # Type: string
        lidarr2_docker_hosts_use_common:
        # Type: string
        lidarr2_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        lidarr2_docker_keep_volumes:
        # Type: list
        lidarr2_docker_mounts:
        # Type: string
        lidarr2_docker_volume_driver:
        # Type: list
        lidarr2_docker_volumes_from:
        # Type: string
        lidarr2_docker_volumes_global:
        # Type: string
        lidarr2_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        lidarr2_docker_healthcheck:
        # Type: bool (true/false)
        lidarr2_docker_init:
        # Type: string
        lidarr2_docker_log_driver:
        # Type: dict
        lidarr2_docker_log_options:
        # Type: bool (true/false)
        lidarr2_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        lidarr2_docker_auto_remove:
        # Type: list
        lidarr2_docker_capabilities:
        # Type: string
        lidarr2_docker_cgroup_parent:
        # Type: string
        lidarr2_docker_cgroupns_mode:
        # Type: bool (true/false)
        lidarr2_docker_cleanup:
        # Type: list
        lidarr2_docker_commands:
        # Type: string
        lidarr2_docker_create_timeout:
        # Type: string
        lidarr2_docker_domainname:
        # Type: string
        lidarr2_docker_entrypoint:
        # Type: string
        lidarr2_docker_env_file:
        # Type: list
        lidarr2_docker_exposed_ports:
        # Type: string
        lidarr2_docker_force_kill:
        # Type: list
        lidarr2_docker_groups:
        # Type: int
        lidarr2_docker_healthy_wait_timeout:
        # Type: string
        lidarr2_docker_ipc_mode:
        # Type: string
        lidarr2_docker_kill_signal:
        # Type: string
        lidarr2_docker_labels_use_common:
        # Type: list
        lidarr2_docker_links:
        # Type: bool (true/false)
        lidarr2_docker_oom_killer:
        # Type: int
        lidarr2_docker_oom_score_adj:
        # Type: bool (true/false)
        lidarr2_docker_paused:
        # Type: string
        lidarr2_docker_pid_mode:
        # Type: list
        lidarr2_docker_ports:
        # Type: bool (true/false)
        lidarr2_docker_read_only:
        # Type: bool (true/false)
        lidarr2_docker_recreate:
        # Type: int
        lidarr2_docker_restart_retries:
        # Type: string
        lidarr2_docker_runtime:
        # Type: string
        lidarr2_docker_shm_size:
        # Type: int
        lidarr2_docker_stop_timeout:
        # Type: dict
        lidarr2_docker_storage_opts:
        # Type: list
        lidarr2_docker_sysctls:
        # Type: list
        lidarr2_docker_tmpfs:
        # Type: list
        lidarr2_docker_ulimits:
        # Type: string
        lidarr2_docker_user:
        # Type: string
        lidarr2_docker_userns_mode:
        # Type: string
        lidarr2_docker_uts:

        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        lidarr_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        lidarr_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        lidarr_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        lidarr_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        lidarr_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        lidarr_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        lidarr_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        lidarr_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        lidarr_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        lidarr_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        lidarr_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        lidarr_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        lidarr_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        lidarr_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        lidarr_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        lidarr_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        lidarr_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            lidarr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "lidarr2.{{ user.domain }}"
              - "lidarr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            lidarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'lidarr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `lidarr2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        lidarr2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        lidarr2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        lidarr2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        lidarr2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        lidarr2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        lidarr2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        lidarr2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        lidarr2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        lidarr2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        lidarr2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        lidarr2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        lidarr2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        lidarr2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        lidarr2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        lidarr2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        lidarr2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        lidarr2_web_scheme:

        ```

        1.  Example:

            ```yaml
            lidarr2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "lidarr2.{{ user.domain }}"
              - "lidarr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            lidarr2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'lidarr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

## Next

Are you setting Saltbox up for the first time?  Continue to [Tautulli](tautulli.md).

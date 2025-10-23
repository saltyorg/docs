---
hide:
  - tags
tags:
  - radarr
---

# Radarr

# What is it?

[Radarr](https://radarr.video/) is a movie collection manager for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new movies and will interface with clients and indexers to grab, sort, and rename them. It can also be configured to automatically upgrade the quality of existing files in the library when a better quality format becomes available.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://radarr.video/){: .header-icons } | [:octicons-link-16: Docs](https://wiki.servarr.com/radarr/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Radarr/Radarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/radarr){: .header-icons }|

## URL

- To access Radarr, visit `https://radarr._yourdomain.com_`

## Settings

Click on "Settings" in the sidebar.  Click "Show Advanced" at the top of the Settings pane.

Make changes in the following sections:

!!! info "Settings"

    === "Media Management"

        These settings control management of media files.

        === "Movie Naming"

            - "Rename Movies": `Yes`

            - "Replace Illegal Characters": `Yes`

            - Colon Replacement Format: `Delete`

            _Note: You could use `Replace with Space Dash` but only if your file naming format is not using spaces (e.g. using dots) to separate words._

            - Set your preferred naming format; here are some examples.

            <details>
            <summary>TRaSH' naming guide [Recommended]</summary> <br />

            Go to the [TRaSH Guides Radarr naming scheme](https://trash-guides.info/Radarr/Radarr-recommended-naming-scheme/) for the latest updates.  These examples may be out of date.

            Example:  <br />
            ```
            The Movie Title (2010) Ultimate Extended Edition [imdb-tt0066921][Surround Sound x264][Bluray-1080p Proper][3D][HDR][10bit][x264][DTS 5.1]-EVOLVE.mkv
            ```

            Standard Movie Format: <br />
            ```
            {Movie CleanTitle} {(Release Year)} {Edition Tags} [imdb-{ImdbId}]{[Custom Formats]}{[Quality Full]}{[MediaInfo 3D]}{[MediaInfo VideoDynamicRange]}[{Mediainfo VideoBitDepth}bit][{Mediainfo VideoCodec}]{[Mediainfo AudioCodec}{ Mediainfo AudioChannels}]{-Release Group}
            ```

            Reference: https://trash-guides.info/Radarr/Radarr-recommended-naming-scheme/
            </details>

            The TRaSH naming guide is recommended since some other tools, notably Kometa, expect it in their default setup.

            <details>
            <summary>Plex's Naming Preference</summary> <br />
            Example: <br />
            ```
            /Guardians of the Galaxy (2014)/Guardians of the Galaxy (2014).mkv
            ```

            Standard Movie Format: <br />
            ```
            {Movie Title} ({Release Year})
            ```

            Movie Folder Format: <br />
            ```
            {Movie Title} ({Release Year})
            ```

            Reference: https://support.plex.tv/articles/200381023-naming-movie-files/
            </details>

            <details>
            <summary>Radarr's Wiki Example</summary> <br />
            Example:  <br />
            ```
            The Movie Title (2010) - [ULTIMATE EXTENDED EDITION][BLURAY-1080P PROPER][DTS 5.1][X264]-EVOLVE.mkv
            ```

            Standard Movie Format: <br />
            ```
            {Movie Title} ({Release Year}) - {[EDITION TAGS]}{[QUALITY FULL]}{[MEDIAINFO AUDIOCODEC}{ MEDIAINFO AUDIOCHANNELS]}{[MEDIAINFO VIDEOCODEC]}{-RELEASE GROUP}
            ```

            Reference: https://github.com/Radarr/Radarr/wiki/Sorting-and-Renaming
            </details>

        === "Folders"

            - "Create empty movie folders": `No`

            - "Automatically Rename Folders": `No`

            - "Movie Paths Default to Static": `No`

        === "Importing"

            - "Skip Free Space Check": `No`

            - "Use Hardlinks instead of Copy": `Yes`

            - "Import Extra Files": `Yes` (_can be your preference_)

            - "Extra File Extensions": `srt, sub, idx`

        === "File Management"

            - "Ignore Deleted Movies": `No` (_can be your preference_)

            - "Download Propers": `No` (_can be your preference_)

            - "Analyse video files": `No`

            - "Change File Date": `None`

            - "Recycle Bin": _blank_ (Rclone deletes are sent to Gdrive trash folder, anyway)

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

                Enable Search: _Your Preference_

                URL: `http://nzbhydra2:5076`

                API Key: [Your NZBHydra2 API Key](../apps/nzbhydra2.md)

                Additional Parameters: _Leave Blank_

            4. Your settings will look like this:

                ![Radarr NZBHydra2](../images/radarr/radarr-nzbhydra.png)

            5. Click "Save" to add NZBHydra2.

            Note: The "Test" will keep failing until you add an indexer in [NZBHydra2](../apps/nzbhydra2.md).

        === "Jackett"

            Note: Each Indexer you have defined in Jackett will need to be added separately.

            1. Click Add Indexer (`+`)

            2. Select "Torznab".

            3. Add the following:

                Name: Indexer Name

                Enable RSS Sync: _Your Preference_

                Enable Search: _Your Preference_

                URL: [Indexer's Torznab Feed](../apps/jackett.md)

                API Key: [Your Jackett API Key](../apps/jackett.md)

                Additional Parameters: _Leave Blank_

            4. Your settings will look like this:

                ![Radarr Jackett](../images/radarr/radarr-jackett.png)

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

                Category: `radarr`

                Use SSL: `No`

                Add Paused: `No`

            4. Your settings will look like this:

                ![Radarr NZBGet Downloader](../images/radarr/radarr-nzbget.png)

            5. Click "Save" to add NZBGet.

        === "SABNzbd"

            1. Click Add (`+`)

            2. Add a new "SABNzbd" download client.

            3. Add the following:

                Name: SABNzbd

                Enable: `Yes`

                Host: `sabnzbd`

                Port: `8080`

                For authentication, you can use either an API key or a username/password.

                === "API Key"

                    API Key:  [Your SABNzbd API Key](../apps/sabnzbd.md)

                === "Username/password"

                    Username:  [Your SABNzbd Username](../apps/sabnzbd.md)

                    Password:  [Your SABNzbd Password](../apps/sabnzbd.md)

                Category: `radarr`

                Use SSL: `No`

                Add Paused: `No`

            4. Your settings will look like this:

                Either API Key **OR** Username/Password should be filled in, **not both**

                ![Radarr Sabnzbd Downloader](../images/radarr/radarr-sabnzbd.png)

            5. Click "Save" to add SABNzbd.

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

                Category: `radarr`

                Directory: _Leave Blank_

            4.  Your settings will now look like this:

                ![Radarr ruTorrent Downloader](../images/radarr/radarr-rtorrent.png)

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

                Category: 'radarr'

            4.  Your settings will now look like this:

                ![Radarr qBittorent Downloader](../images/radarr/radarr-qbittorrent.png)

            5.  Click "Save" to add qBittorrent

    === "Connect"

        These settings control connections to other applications or systems.

        === "Torrent Cleanup"

            Torrent Cleanup Script is a custom script that will cleanup torrents from ruTorrent that were auto-extracted, but still being seeded. So if the script detects that `.rar` files are in the folder that Radarr just imported from, it will delete the imported video file(s), leaving just the `.rar` files for seeding.

            1. Click "Settings" -> "Connect".

            2. Add a new "Custom Script".

            3. Add the following:

                Name: Torrent Cleanup

                On Grab: `No`

                On Download: `Yes`

                On Upgrade:  `Yes`

                On Rename:`No`

                Path: `/scripts/torrents/TorrentCleanup.py`

            4. The settings will look like this:

                ![Radarr Torrent Cleanup Script CloudBox](../images/radarr/radarr-torrentcleanup.png)

            5. Click "Save" to add the Torrent Cleanup script.


        === "Autoscan"
            IMPORTANT:  The Radarr UI may differ from what is shown here; there may be additional events listed in the UI.  

            GENERALLY SPEAKING, if you have events listed that are not explicitly listed below, LEAVE THEM UNCHECKED.  Such events will generate errors in the autoscan logs; those errors can be ignored, but they are errors and can cause panic and confusion.

            MORE SPECIFICALLY, Autoscan is expecting a request that points to an individual file that is ready for Plex. so any event you may have that refers to a movie being added, manual intervention, or anything else that is not "this specific video file ON DISK was imported/upgraded/deleted/etc", LEAVE IT UNCHECKED.

            1. Click "Settings" -> "Connect".

            2. Add a new "Webhook".

            3. Add the following:

                Name: Autoscan

                On Grab: `No`

                On Import: `Yes`

                On Upgrade:  `Yes`

                On Rename: `Yes`

                On Movie Added: `No`

                On Movie Delete: `Yes`

                On Movie File Delete: `Yes`

                On Movie File Delete For Upgrade: `Yes`

                On Health Issue: `No`

                On Health Restored: `No`

                Include Health Warnings: `No`

                On Application Update: `No`

                On Manual Intervention Required: `No`

                Tags: _Leave Blank_

                URL: `http://autoscan:3030/triggers/radarr`

                Method:`POST`

                Username: AS SET IN AUTOSCAN CONFIG [defaults to Saltbox Username]

                Password: AS SET IN AUTOSCAN CONFIG [defaults to Saltbox Password]

                THERE MAY BE OTHER CHECKBOXES AVAILABLE: UNCHECK THEM ALL LEAVING ONLY THE ONES SPECIFICALLY LISTED ABOVE ENABLED.

            4. The settings will look like this:

                ![Radarr Autoscan](../images/radarr/radarr-autoscan.png)


            5. Click "Save" to add Autoscan.

    === "General"

        These settings control general aspects of Radarr.

        === "Start-Up"

            - "Bind Address: `*`

            - "Port Number": `7878`

            - "URL Base": _blank_

            - "Enable SSL": `No` (_SSL is handled by Traefik_)

        === "Proxy Settings"

            - "Use Proxy": `No`

        === "Logging"

            - "Log Level": `Debug`

        === "Analytics"

            - "Enable": `No` (_your preference_)

        === "Updates"

            These settings may be grayed out or unavailable; skip this if that's the case.

            - "Branch": `nightly` or `develop`

            - "Automatic": `Off`

        === "Save"

            - Click "Save".

## Movies Path

1. When you are ready to add your first movie to Radarr, click the "Path" drop-down and select "Add a new path".

2. Click the blue "Browse" button, navigate to `/mnt/unionfs/Media/Movies`, scroll to the bottom, and select "OK".

3. Click the green "check" button to add the path.

4. All movies added now will have that path set.

![Radarr Add](../images/radarr/radarr-add.png)

## API Key

This is used during the setup of [Overseerr](overseerr.md) and [Organizr](organizr.md).

- Go to "Settings" -> "General" -> "Security" -> "API Key".

## Guide

[TraSH Guides](https://trash-guides.info/Radarr/)

## Next

Are you setting Saltbox up for the first time?  Continue to [Lidarr](lidarr.md).

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `radarr_instances`.

    === "Role-level Override"

        Applies to all instances of radarr:

        ```yaml
        radarr_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `radarr2`):

        ```yaml
        radarr2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `radarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `radarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`radarr_instances`"

        ```yaml
        # Type: list
        radarr_instances: ["radarr"]
        ```

        !!! example

            ```yaml
            # Type: list
            radarr_instances: ["radarr", "radarr2"]
            ```

=== "Settings"

    === "Role-level"

        ??? variable bool "`radarr_role_external_auth`"

            ```yaml
            # Type: bool (true/false)
            radarr_role_external_auth: true
            ```

    === "Instance-level"

        ??? variable bool "`radarr2_external_auth`"

            ```yaml
            # Type: bool (true/false)
            radarr2_external_auth: true
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`radarr_role_paths_folder`"

            ```yaml
            # Type: string
            radarr_role_paths_folder: "{{ radarr_name }}"
            ```

        ??? variable string "`radarr_role_paths_location`"

            ```yaml
            # Type: string
            radarr_role_paths_location: "{{ server_appdata_path }}/{{ radarr_role_paths_folder }}"
            ```

        ??? variable string "`radarr_role_paths_config_location`"

            ```yaml
            # Type: string
            radarr_role_paths_config_location: "{{ radarr_role_paths_location }}/config.xml"
            ```

    === "Instance-level"

        ??? variable string "`radarr2_paths_folder`"

            ```yaml
            # Type: string
            radarr2_paths_folder: "{{ radarr_name }}"
            ```

        ??? variable string "`radarr2_paths_location`"

            ```yaml
            # Type: string
            radarr2_paths_location: "{{ server_appdata_path }}/{{ radarr_role_paths_folder }}"
            ```

        ??? variable string "`radarr2_paths_config_location`"

            ```yaml
            # Type: string
            radarr2_paths_config_location: "{{ radarr_role_paths_location }}/config.xml"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`radarr_role_web_subdomain`"

            ```yaml
            # Type: string
            radarr_role_web_subdomain: "{{ radarr_name }}"
            ```

        ??? variable string "`radarr_role_web_domain`"

            ```yaml
            # Type: string
            radarr_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`radarr_role_web_port`"

            ```yaml
            # Type: string
            radarr_role_web_port: "7878"
            ```

        ??? variable string "`radarr_role_web_url`"

            ```yaml
            # Type: string
            radarr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='radarr') + '.' + lookup('role_var', '_web_domain', role='radarr')
                                  if (lookup('role_var', '_web_subdomain', role='radarr') | length > 0)
                                  else lookup('role_var', '_web_domain', role='radarr')) }}"
            ```

    === "Instance-level"

        ??? variable string "`radarr2_web_subdomain`"

            ```yaml
            # Type: string
            radarr2_web_subdomain: "{{ radarr_name }}"
            ```

        ??? variable string "`radarr2_web_domain`"

            ```yaml
            # Type: string
            radarr2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`radarr2_web_port`"

            ```yaml
            # Type: string
            radarr2_web_port: "7878"
            ```

        ??? variable string "`radarr2_web_url`"

            ```yaml
            # Type: string
            radarr2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='radarr') + '.' + lookup('role_var', '_web_domain', role='radarr')
                              if (lookup('role_var', '_web_subdomain', role='radarr') | length > 0)
                              else lookup('role_var', '_web_domain', role='radarr')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`radarr_role_dns_record`"

            ```yaml
            # Type: string
            radarr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='radarr') }}"
            ```

        ??? variable string "`radarr_role_dns_zone`"

            ```yaml
            # Type: string
            radarr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='radarr') }}"
            ```

        ??? variable bool "`radarr_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            radarr_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`radarr2_dns_record`"

            ```yaml
            # Type: string
            radarr2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='radarr') }}"
            ```

        ??? variable string "`radarr2_dns_zone`"

            ```yaml
            # Type: string
            radarr2_dns_zone: "{{ lookup('role_var', '_web_domain', role='radarr') }}"
            ```

        ??? variable bool "`radarr2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            radarr2_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`radarr_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            radarr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`radarr_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            radarr_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                        + (',themepark-' + radarr_name
                                                          if (lookup('role_var', '_themepark_enabled', role='radarr') and global_themepark_plugin_enabled)
                                                          else '') }}"
            ```

        ??? variable string "`radarr_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            radarr_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`radarr_role_traefik_certresolver`"

            ```yaml
            # Type: string
            radarr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`radarr_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            radarr_role_traefik_enabled: true
            ```

        ??? variable bool "`radarr_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            radarr_role_traefik_api_enabled: true
            ```

        ??? variable string "`radarr_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            radarr_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/feed`) || PathPrefix(`/ping`)"
            ```

    === "Instance-level"

        ??? variable string "`radarr2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            radarr2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`radarr2_traefik_middleware_default`"

            ```yaml
            # Type: string
            radarr2_traefik_middleware_default: "{{ traefik_default_middleware
                                                    + (',themepark-' + radarr_name
                                                      if (lookup('role_var', '_themepark_enabled', role='radarr') and global_themepark_plugin_enabled)
                                                      else '') }}"
            ```

        ??? variable string "`radarr2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            radarr2_traefik_middleware_custom: ""
            ```

        ??? variable string "`radarr2_traefik_certresolver`"

            ```yaml
            # Type: string
            radarr2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`radarr2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            radarr2_traefik_enabled: true
            ```

        ??? variable bool "`radarr2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            radarr2_traefik_api_enabled: true
            ```

        ??? variable string "`radarr2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            radarr2_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/feed`) || PathPrefix(`/ping`)"
            ```

=== "Theme"

    === "Role-level"

        ??? variable bool "`radarr_role_themepark_enabled`"

            ```yaml
            # Options can be found at https://github.com/themepark-dev/theme.park
            # Type: bool (true/false)
            radarr_role_themepark_enabled: false
            ```

        ??? variable string "`radarr_role_themepark_app`"

            ```yaml
            # Type: string
            radarr_role_themepark_app: "radarr"
            ```

        ??? variable string "`radarr_role_themepark_theme`"

            ```yaml
            # Type: string
            radarr_role_themepark_theme: "{{ global_themepark_theme }}"
            ```

        ??? variable string "`radarr_role_themepark_domain`"

            ```yaml
            # Type: string
            radarr_role_themepark_domain: "{{ global_themepark_domain }}"
            ```

        ??? variable list "`radarr_role_themepark_addons`"

            ```yaml
            # Type: list
            radarr_role_themepark_addons: []
            ```

    === "Instance-level"

        ??? variable bool "`radarr2_themepark_enabled`"

            ```yaml
            # Options can be found at https://github.com/themepark-dev/theme.park
            # Type: bool (true/false)
            radarr2_themepark_enabled: false
            ```

        ??? variable string "`radarr2_themepark_app`"

            ```yaml
            # Type: string
            radarr2_themepark_app: "radarr"
            ```

        ??? variable string "`radarr2_themepark_theme`"

            ```yaml
            # Type: string
            radarr2_themepark_theme: "{{ global_themepark_theme }}"
            ```

        ??? variable string "`radarr2_themepark_domain`"

            ```yaml
            # Type: string
            radarr2_themepark_domain: "{{ global_themepark_domain }}"
            ```

        ??? variable list "`radarr2_themepark_addons`"

            ```yaml
            # Type: list
            radarr2_themepark_addons: []
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`radarr_role_docker_container`"

            ```yaml
            # Type: string
            radarr_role_docker_container: "{{ radarr_name }}"
            ```

        ##### Image

        ??? variable bool "`radarr_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            radarr_role_docker_image_pull: true
            ```

        ??? variable string "`radarr_role_docker_image_repo`"

            ```yaml
            # Type: string
            radarr_role_docker_image_repo: "ghcr.io/hotio/radarr"
            ```

        ??? variable string "`radarr_role_docker_image_tag`"

            ```yaml
            # Type: string
            radarr_role_docker_image_tag: "release"
            ```

        ??? variable string "`radarr_role_docker_image`"

            ```yaml
            # Type: string
            radarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='radarr') }}:{{ lookup('role_var', '_docker_image_tag', role='radarr') }}"
            ```

        ##### Envs

        ??? variable dict "`radarr_role_docker_envs_default`"

            ```yaml
            # Type: dict
            radarr_role_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              UMASK: "002"
              TZ: "{{ tz }}"
            ```

        ??? variable dict "`radarr_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            radarr_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`radarr_role_docker_volumes_default`"

            ```yaml
            # Type: list
            radarr_role_docker_volumes_default: 
              - "{{ radarr_role_paths_location }}:/config"
              - "{{ server_appdata_path }}/scripts:/scripts"
            ```

        ??? variable list "`radarr_role_docker_volumes_legacy`"

            ```yaml
            # Type: list
            radarr_role_docker_volumes_legacy: 
              - "/mnt/unionfs/Media/Movies:/movies"
            ```

        ??? variable list "`radarr_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            radarr_role_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable dict "`radarr_role_docker_labels_default`"

            ```yaml
            # Type: dict
            radarr_role_docker_labels_default: {}
            ```

        ??? variable dict "`radarr_role_docker_labels_custom`"

            ```yaml
            # Type: dict
            radarr_role_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`radarr_role_docker_hostname`"

            ```yaml
            # Type: string
            radarr_role_docker_hostname: "{{ radarr_name }}"
            ```

        ##### Networks

        ??? variable string "`radarr_role_docker_networks_alias`"

            ```yaml
            # Type: string
            radarr_role_docker_networks_alias: "{{ radarr_name }}"
            ```

        ??? variable list "`radarr_role_docker_networks_default`"

            ```yaml
            # Type: list
            radarr_role_docker_networks_default: []
            ```

        ??? variable list "`radarr_role_docker_networks_custom`"

            ```yaml
            # Type: list
            radarr_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`radarr_role_docker_restart_policy`"

            ```yaml
            # Type: string
            radarr_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`radarr_role_docker_state`"

            ```yaml
            # Type: string
            radarr_role_docker_state: started
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`radarr2_docker_container`"

            ```yaml
            # Type: string
            radarr2_docker_container: "{{ radarr_name }}"
            ```

        ##### Image

        ??? variable bool "`radarr2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            radarr2_docker_image_pull: true
            ```

        ??? variable string "`radarr2_docker_image_repo`"

            ```yaml
            # Type: string
            radarr2_docker_image_repo: "ghcr.io/hotio/radarr"
            ```

        ??? variable string "`radarr2_docker_image_tag`"

            ```yaml
            # Type: string
            radarr2_docker_image_tag: "release"
            ```

        ??? variable string "`radarr2_docker_image`"

            ```yaml
            # Type: string
            radarr2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='radarr') }}:{{ lookup('role_var', '_docker_image_tag', role='radarr') }}"
            ```

        ##### Envs

        ??? variable dict "`radarr2_docker_envs_default`"

            ```yaml
            # Type: dict
            radarr2_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              UMASK: "002"
              TZ: "{{ tz }}"
            ```

        ??? variable dict "`radarr2_docker_envs_custom`"

            ```yaml
            # Type: dict
            radarr2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`radarr2_docker_volumes_default`"

            ```yaml
            # Type: list
            radarr2_docker_volumes_default: 
              - "{{ radarr_role_paths_location }}:/config"
              - "{{ server_appdata_path }}/scripts:/scripts"
            ```

        ??? variable list "`radarr2_docker_volumes_legacy`"

            ```yaml
            # Type: list
            radarr2_docker_volumes_legacy: 
              - "/mnt/unionfs/Media/Movies:/movies"
            ```

        ??? variable list "`radarr2_docker_volumes_custom`"

            ```yaml
            # Type: list
            radarr2_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable dict "`radarr2_docker_labels_default`"

            ```yaml
            # Type: dict
            radarr2_docker_labels_default: {}
            ```

        ??? variable dict "`radarr2_docker_labels_custom`"

            ```yaml
            # Type: dict
            radarr2_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`radarr2_docker_hostname`"

            ```yaml
            # Type: string
            radarr2_docker_hostname: "{{ radarr_name }}"
            ```

        ##### Networks

        ??? variable string "`radarr2_docker_networks_alias`"

            ```yaml
            # Type: string
            radarr2_docker_networks_alias: "{{ radarr_name }}"
            ```

        ??? variable list "`radarr2_docker_networks_default`"

            ```yaml
            # Type: list
            radarr2_docker_networks_default: []
            ```

        ??? variable list "`radarr2_docker_networks_custom`"

            ```yaml
            # Type: list
            radarr2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`radarr2_docker_restart_policy`"

            ```yaml
            # Type: string
            radarr2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`radarr2_docker_state`"

            ```yaml
            # Type: string
            radarr2_docker_state: started
            ```

=== "Docker+"

    #### Additional Docker Options

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    === "Role-level"

        ##### Resource Limits

        ??? variable int "`radarr_role_docker_blkio_weight`"

            ```yaml
            # Type: int
            radarr_role_docker_blkio_weight:
            ```

        ??? variable int "`radarr_role_docker_cpu_period`"

            ```yaml
            # Type: int
            radarr_role_docker_cpu_period:
            ```

        ??? variable int "`radarr_role_docker_cpu_quota`"

            ```yaml
            # Type: int
            radarr_role_docker_cpu_quota:
            ```

        ??? variable int "`radarr_role_docker_cpu_shares`"

            ```yaml
            # Type: int
            radarr_role_docker_cpu_shares:
            ```

        ??? variable string "`radarr_role_docker_cpus`"

            ```yaml
            # Type: string
            radarr_role_docker_cpus:
            ```

        ??? variable string "`radarr_role_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            radarr_role_docker_cpuset_cpus:
            ```

        ??? variable string "`radarr_role_docker_cpuset_mems`"

            ```yaml
            # Type: string
            radarr_role_docker_cpuset_mems:
            ```

        ??? variable string "`radarr_role_docker_kernel_memory`"

            ```yaml
            # Type: string
            radarr_role_docker_kernel_memory:
            ```

        ??? variable string "`radarr_role_docker_memory`"

            ```yaml
            # Type: string
            radarr_role_docker_memory:
            ```

        ??? variable string "`radarr_role_docker_memory_reservation`"

            ```yaml
            # Type: string
            radarr_role_docker_memory_reservation:
            ```

        ??? variable string "`radarr_role_docker_memory_swap`"

            ```yaml
            # Type: string
            radarr_role_docker_memory_swap:
            ```

        ??? variable int "`radarr_role_docker_memory_swappiness`"

            ```yaml
            # Type: int
            radarr_role_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`radarr_role_docker_cap_drop`"

            ```yaml
            # Type: list
            radarr_role_docker_cap_drop:
            ```

        ??? variable list "`radarr_role_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            radarr_role_docker_device_cgroup_rules:
            ```

        ??? variable list "`radarr_role_docker_device_read_bps`"

            ```yaml
            # Type: list
            radarr_role_docker_device_read_bps:
            ```

        ??? variable list "`radarr_role_docker_device_read_iops`"

            ```yaml
            # Type: list
            radarr_role_docker_device_read_iops:
            ```

        ??? variable list "`radarr_role_docker_device_requests`"

            ```yaml
            # Type: list
            radarr_role_docker_device_requests:
            ```

        ??? variable list "`radarr_role_docker_device_write_bps`"

            ```yaml
            # Type: list
            radarr_role_docker_device_write_bps:
            ```

        ??? variable list "`radarr_role_docker_device_write_iops`"

            ```yaml
            # Type: list
            radarr_role_docker_device_write_iops:
            ```

        ??? variable list "`radarr_role_docker_devices`"

            ```yaml
            # Type: list
            radarr_role_docker_devices:
            ```

        ??? variable string "`radarr_role_docker_devices_default`"

            ```yaml
            # Type: string
            radarr_role_docker_devices_default:
            ```

        ??? variable bool "`radarr_role_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            radarr_role_docker_privileged:
            ```

        ??? variable list "`radarr_role_docker_security_opts`"

            ```yaml
            # Type: list
            radarr_role_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`radarr_role_docker_dns_opts`"

            ```yaml
            # Type: list
            radarr_role_docker_dns_opts:
            ```

        ??? variable list "`radarr_role_docker_dns_search_domains`"

            ```yaml
            # Type: list
            radarr_role_docker_dns_search_domains:
            ```

        ??? variable list "`radarr_role_docker_dns_servers`"

            ```yaml
            # Type: list
            radarr_role_docker_dns_servers:
            ```

        ??? variable dict "`radarr_role_docker_hosts`"

            ```yaml
            # Type: dict
            radarr_role_docker_hosts:
            ```

        ??? variable string "`radarr_role_docker_hosts_use_common`"

            ```yaml
            # Type: string
            radarr_role_docker_hosts_use_common:
            ```

        ??? variable string "`radarr_role_docker_network_mode`"

            ```yaml
            # Type: string
            radarr_role_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`radarr_role_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            radarr_role_docker_keep_volumes:
            ```

        ??? variable list "`radarr_role_docker_mounts`"

            ```yaml
            # Type: list
            radarr_role_docker_mounts:
            ```

        ??? variable string "`radarr_role_docker_volume_driver`"

            ```yaml
            # Type: string
            radarr_role_docker_volume_driver:
            ```

        ??? variable list "`radarr_role_docker_volumes_from`"

            ```yaml
            # Type: list
            radarr_role_docker_volumes_from:
            ```

        ??? variable string "`radarr_role_docker_volumes_global`"

            ```yaml
            # Type: string
            radarr_role_docker_volumes_global:
            ```

        ??? variable string "`radarr_role_docker_working_dir`"

            ```yaml
            # Type: string
            radarr_role_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`radarr_role_docker_healthcheck`"

            ```yaml
            # Type: dict
            radarr_role_docker_healthcheck:
            ```

        ??? variable bool "`radarr_role_docker_init`"

            ```yaml
            # Type: bool (true/false)
            radarr_role_docker_init:
            ```

        ??? variable string "`radarr_role_docker_log_driver`"

            ```yaml
            # Type: string
            radarr_role_docker_log_driver:
            ```

        ??? variable dict "`radarr_role_docker_log_options`"

            ```yaml
            # Type: dict
            radarr_role_docker_log_options:
            ```

        ??? variable bool "`radarr_role_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            radarr_role_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`radarr_role_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            radarr_role_docker_auto_remove:
            ```

        ??? variable list "`radarr_role_docker_capabilities`"

            ```yaml
            # Type: list
            radarr_role_docker_capabilities:
            ```

        ??? variable string "`radarr_role_docker_cgroup_parent`"

            ```yaml
            # Type: string
            radarr_role_docker_cgroup_parent:
            ```

        ??? variable string "`radarr_role_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            radarr_role_docker_cgroupns_mode:
            ```

        ??? variable bool "`radarr_role_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            radarr_role_docker_cleanup:
            ```

        ??? variable list "`radarr_role_docker_commands`"

            ```yaml
            # Type: list
            radarr_role_docker_commands:
            ```

        ??? variable string "`radarr_role_docker_create_timeout`"

            ```yaml
            # Type: string
            radarr_role_docker_create_timeout:
            ```

        ??? variable string "`radarr_role_docker_domainname`"

            ```yaml
            # Type: string
            radarr_role_docker_domainname:
            ```

        ??? variable string "`radarr_role_docker_entrypoint`"

            ```yaml
            # Type: string
            radarr_role_docker_entrypoint:
            ```

        ??? variable string "`radarr_role_docker_env_file`"

            ```yaml
            # Type: string
            radarr_role_docker_env_file:
            ```

        ??? variable list "`radarr_role_docker_exposed_ports`"

            ```yaml
            # Type: list
            radarr_role_docker_exposed_ports:
            ```

        ??? variable string "`radarr_role_docker_force_kill`"

            ```yaml
            # Type: string
            radarr_role_docker_force_kill:
            ```

        ??? variable list "`radarr_role_docker_groups`"

            ```yaml
            # Type: list
            radarr_role_docker_groups:
            ```

        ??? variable int "`radarr_role_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            radarr_role_docker_healthy_wait_timeout:
            ```

        ??? variable string "`radarr_role_docker_ipc_mode`"

            ```yaml
            # Type: string
            radarr_role_docker_ipc_mode:
            ```

        ??? variable string "`radarr_role_docker_kill_signal`"

            ```yaml
            # Type: string
            radarr_role_docker_kill_signal:
            ```

        ??? variable string "`radarr_role_docker_labels_use_common`"

            ```yaml
            # Type: string
            radarr_role_docker_labels_use_common:
            ```

        ??? variable list "`radarr_role_docker_links`"

            ```yaml
            # Type: list
            radarr_role_docker_links:
            ```

        ??? variable bool "`radarr_role_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            radarr_role_docker_oom_killer:
            ```

        ??? variable int "`radarr_role_docker_oom_score_adj`"

            ```yaml
            # Type: int
            radarr_role_docker_oom_score_adj:
            ```

        ??? variable bool "`radarr_role_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            radarr_role_docker_paused:
            ```

        ??? variable string "`radarr_role_docker_pid_mode`"

            ```yaml
            # Type: string
            radarr_role_docker_pid_mode:
            ```

        ??? variable list "`radarr_role_docker_ports`"

            ```yaml
            # Type: list
            radarr_role_docker_ports:
            ```

        ??? variable bool "`radarr_role_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            radarr_role_docker_read_only:
            ```

        ??? variable bool "`radarr_role_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            radarr_role_docker_recreate:
            ```

        ??? variable int "`radarr_role_docker_restart_retries`"

            ```yaml
            # Type: int
            radarr_role_docker_restart_retries:
            ```

        ??? variable string "`radarr_role_docker_runtime`"

            ```yaml
            # Type: string
            radarr_role_docker_runtime:
            ```

        ??? variable string "`radarr_role_docker_shm_size`"

            ```yaml
            # Type: string
            radarr_role_docker_shm_size:
            ```

        ??? variable int "`radarr_role_docker_stop_timeout`"

            ```yaml
            # Type: int
            radarr_role_docker_stop_timeout:
            ```

        ??? variable dict "`radarr_role_docker_storage_opts`"

            ```yaml
            # Type: dict
            radarr_role_docker_storage_opts:
            ```

        ??? variable list "`radarr_role_docker_sysctls`"

            ```yaml
            # Type: list
            radarr_role_docker_sysctls:
            ```

        ??? variable list "`radarr_role_docker_tmpfs`"

            ```yaml
            # Type: list
            radarr_role_docker_tmpfs:
            ```

        ??? variable list "`radarr_role_docker_ulimits`"

            ```yaml
            # Type: list
            radarr_role_docker_ulimits:
            ```

        ??? variable string "`radarr_role_docker_user`"

            ```yaml
            # Type: string
            radarr_role_docker_user:
            ```

        ??? variable string "`radarr_role_docker_userns_mode`"

            ```yaml
            # Type: string
            radarr_role_docker_userns_mode:
            ```

        ??? variable string "`radarr_role_docker_uts`"

            ```yaml
            # Type: string
            radarr_role_docker_uts:
            ```

    === "Instance-level"

        ##### Resource Limits

        ??? variable int "`radarr2_docker_blkio_weight`"

            ```yaml
            # Type: int
            radarr2_docker_blkio_weight:
            ```

        ??? variable int "`radarr2_docker_cpu_period`"

            ```yaml
            # Type: int
            radarr2_docker_cpu_period:
            ```

        ??? variable int "`radarr2_docker_cpu_quota`"

            ```yaml
            # Type: int
            radarr2_docker_cpu_quota:
            ```

        ??? variable int "`radarr2_docker_cpu_shares`"

            ```yaml
            # Type: int
            radarr2_docker_cpu_shares:
            ```

        ??? variable string "`radarr2_docker_cpus`"

            ```yaml
            # Type: string
            radarr2_docker_cpus:
            ```

        ??? variable string "`radarr2_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            radarr2_docker_cpuset_cpus:
            ```

        ??? variable string "`radarr2_docker_cpuset_mems`"

            ```yaml
            # Type: string
            radarr2_docker_cpuset_mems:
            ```

        ??? variable string "`radarr2_docker_kernel_memory`"

            ```yaml
            # Type: string
            radarr2_docker_kernel_memory:
            ```

        ??? variable string "`radarr2_docker_memory`"

            ```yaml
            # Type: string
            radarr2_docker_memory:
            ```

        ??? variable string "`radarr2_docker_memory_reservation`"

            ```yaml
            # Type: string
            radarr2_docker_memory_reservation:
            ```

        ??? variable string "`radarr2_docker_memory_swap`"

            ```yaml
            # Type: string
            radarr2_docker_memory_swap:
            ```

        ??? variable int "`radarr2_docker_memory_swappiness`"

            ```yaml
            # Type: int
            radarr2_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`radarr2_docker_cap_drop`"

            ```yaml
            # Type: list
            radarr2_docker_cap_drop:
            ```

        ??? variable list "`radarr2_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            radarr2_docker_device_cgroup_rules:
            ```

        ??? variable list "`radarr2_docker_device_read_bps`"

            ```yaml
            # Type: list
            radarr2_docker_device_read_bps:
            ```

        ??? variable list "`radarr2_docker_device_read_iops`"

            ```yaml
            # Type: list
            radarr2_docker_device_read_iops:
            ```

        ??? variable list "`radarr2_docker_device_requests`"

            ```yaml
            # Type: list
            radarr2_docker_device_requests:
            ```

        ??? variable list "`radarr2_docker_device_write_bps`"

            ```yaml
            # Type: list
            radarr2_docker_device_write_bps:
            ```

        ??? variable list "`radarr2_docker_device_write_iops`"

            ```yaml
            # Type: list
            radarr2_docker_device_write_iops:
            ```

        ??? variable list "`radarr2_docker_devices`"

            ```yaml
            # Type: list
            radarr2_docker_devices:
            ```

        ??? variable string "`radarr2_docker_devices_default`"

            ```yaml
            # Type: string
            radarr2_docker_devices_default:
            ```

        ??? variable bool "`radarr2_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            radarr2_docker_privileged:
            ```

        ??? variable list "`radarr2_docker_security_opts`"

            ```yaml
            # Type: list
            radarr2_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`radarr2_docker_dns_opts`"

            ```yaml
            # Type: list
            radarr2_docker_dns_opts:
            ```

        ??? variable list "`radarr2_docker_dns_search_domains`"

            ```yaml
            # Type: list
            radarr2_docker_dns_search_domains:
            ```

        ??? variable list "`radarr2_docker_dns_servers`"

            ```yaml
            # Type: list
            radarr2_docker_dns_servers:
            ```

        ??? variable dict "`radarr2_docker_hosts`"

            ```yaml
            # Type: dict
            radarr2_docker_hosts:
            ```

        ??? variable string "`radarr2_docker_hosts_use_common`"

            ```yaml
            # Type: string
            radarr2_docker_hosts_use_common:
            ```

        ??? variable string "`radarr2_docker_network_mode`"

            ```yaml
            # Type: string
            radarr2_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`radarr2_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            radarr2_docker_keep_volumes:
            ```

        ??? variable list "`radarr2_docker_mounts`"

            ```yaml
            # Type: list
            radarr2_docker_mounts:
            ```

        ??? variable string "`radarr2_docker_volume_driver`"

            ```yaml
            # Type: string
            radarr2_docker_volume_driver:
            ```

        ??? variable list "`radarr2_docker_volumes_from`"

            ```yaml
            # Type: list
            radarr2_docker_volumes_from:
            ```

        ??? variable string "`radarr2_docker_volumes_global`"

            ```yaml
            # Type: string
            radarr2_docker_volumes_global:
            ```

        ??? variable string "`radarr2_docker_working_dir`"

            ```yaml
            # Type: string
            radarr2_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`radarr2_docker_healthcheck`"

            ```yaml
            # Type: dict
            radarr2_docker_healthcheck:
            ```

        ??? variable bool "`radarr2_docker_init`"

            ```yaml
            # Type: bool (true/false)
            radarr2_docker_init:
            ```

        ??? variable string "`radarr2_docker_log_driver`"

            ```yaml
            # Type: string
            radarr2_docker_log_driver:
            ```

        ??? variable dict "`radarr2_docker_log_options`"

            ```yaml
            # Type: dict
            radarr2_docker_log_options:
            ```

        ??? variable bool "`radarr2_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            radarr2_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`radarr2_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            radarr2_docker_auto_remove:
            ```

        ??? variable list "`radarr2_docker_capabilities`"

            ```yaml
            # Type: list
            radarr2_docker_capabilities:
            ```

        ??? variable string "`radarr2_docker_cgroup_parent`"

            ```yaml
            # Type: string
            radarr2_docker_cgroup_parent:
            ```

        ??? variable string "`radarr2_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            radarr2_docker_cgroupns_mode:
            ```

        ??? variable bool "`radarr2_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            radarr2_docker_cleanup:
            ```

        ??? variable list "`radarr2_docker_commands`"

            ```yaml
            # Type: list
            radarr2_docker_commands:
            ```

        ??? variable string "`radarr2_docker_create_timeout`"

            ```yaml
            # Type: string
            radarr2_docker_create_timeout:
            ```

        ??? variable string "`radarr2_docker_domainname`"

            ```yaml
            # Type: string
            radarr2_docker_domainname:
            ```

        ??? variable string "`radarr2_docker_entrypoint`"

            ```yaml
            # Type: string
            radarr2_docker_entrypoint:
            ```

        ??? variable string "`radarr2_docker_env_file`"

            ```yaml
            # Type: string
            radarr2_docker_env_file:
            ```

        ??? variable list "`radarr2_docker_exposed_ports`"

            ```yaml
            # Type: list
            radarr2_docker_exposed_ports:
            ```

        ??? variable string "`radarr2_docker_force_kill`"

            ```yaml
            # Type: string
            radarr2_docker_force_kill:
            ```

        ??? variable list "`radarr2_docker_groups`"

            ```yaml
            # Type: list
            radarr2_docker_groups:
            ```

        ??? variable int "`radarr2_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            radarr2_docker_healthy_wait_timeout:
            ```

        ??? variable string "`radarr2_docker_ipc_mode`"

            ```yaml
            # Type: string
            radarr2_docker_ipc_mode:
            ```

        ??? variable string "`radarr2_docker_kill_signal`"

            ```yaml
            # Type: string
            radarr2_docker_kill_signal:
            ```

        ??? variable string "`radarr2_docker_labels_use_common`"

            ```yaml
            # Type: string
            radarr2_docker_labels_use_common:
            ```

        ??? variable list "`radarr2_docker_links`"

            ```yaml
            # Type: list
            radarr2_docker_links:
            ```

        ??? variable bool "`radarr2_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            radarr2_docker_oom_killer:
            ```

        ??? variable int "`radarr2_docker_oom_score_adj`"

            ```yaml
            # Type: int
            radarr2_docker_oom_score_adj:
            ```

        ??? variable bool "`radarr2_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            radarr2_docker_paused:
            ```

        ??? variable string "`radarr2_docker_pid_mode`"

            ```yaml
            # Type: string
            radarr2_docker_pid_mode:
            ```

        ??? variable list "`radarr2_docker_ports`"

            ```yaml
            # Type: list
            radarr2_docker_ports:
            ```

        ??? variable bool "`radarr2_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            radarr2_docker_read_only:
            ```

        ??? variable bool "`radarr2_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            radarr2_docker_recreate:
            ```

        ??? variable int "`radarr2_docker_restart_retries`"

            ```yaml
            # Type: int
            radarr2_docker_restart_retries:
            ```

        ??? variable string "`radarr2_docker_runtime`"

            ```yaml
            # Type: string
            radarr2_docker_runtime:
            ```

        ??? variable string "`radarr2_docker_shm_size`"

            ```yaml
            # Type: string
            radarr2_docker_shm_size:
            ```

        ??? variable int "`radarr2_docker_stop_timeout`"

            ```yaml
            # Type: int
            radarr2_docker_stop_timeout:
            ```

        ??? variable dict "`radarr2_docker_storage_opts`"

            ```yaml
            # Type: dict
            radarr2_docker_storage_opts:
            ```

        ??? variable list "`radarr2_docker_sysctls`"

            ```yaml
            # Type: list
            radarr2_docker_sysctls:
            ```

        ??? variable list "`radarr2_docker_tmpfs`"

            ```yaml
            # Type: list
            radarr2_docker_tmpfs:
            ```

        ??? variable list "`radarr2_docker_ulimits`"

            ```yaml
            # Type: list
            radarr2_docker_ulimits:
            ```

        ??? variable string "`radarr2_docker_user`"

            ```yaml
            # Type: string
            radarr2_docker_user:
            ```

        ??? variable string "`radarr2_docker_userns_mode`"

            ```yaml
            # Type: string
            radarr2_docker_userns_mode:
            ```

        ??? variable string "`radarr2_docker_uts`"

            ```yaml
            # Type: string
            radarr2_docker_uts:
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`radarr_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            radarr_role_autoheal_enabled: true
            ```

        ??? variable string "`radarr_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            radarr_role_depends_on: ""
            ```

        ??? variable string "`radarr_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            radarr_role_depends_on_delay: "0"
            ```

        ??? variable string "`radarr_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            radarr_role_depends_on_healthchecks:
            ```

        ??? variable bool "`radarr_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            radarr_role_diun_enabled: true
            ```

        ??? variable bool "`radarr_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            radarr_role_dns_enabled: true
            ```

        ??? variable bool "`radarr_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            radarr_role_docker_controller: true
            ```

        ??? variable bool "`radarr_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            radarr_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`radarr_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            radarr_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`radarr_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            radarr_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`radarr_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            radarr_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`radarr_role_traefik_middleware_http_api_insecure`"

            ```yaml
            # Type: bool (true/false)
            radarr_role_traefik_middleware_http_api_insecure:
            ```

        ??? variable bool "`radarr_role_traefik_middleware_http_insecure`"

            ```yaml
            # Type: bool (true/false)
            radarr_role_traefik_middleware_http_insecure:
            ```

        ??? variable bool "`radarr_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            radarr_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`radarr_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            radarr_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`radarr_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            radarr_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`radarr_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            radarr_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                radarr_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "radarr2.{{ user.domain }}"
                  - "radarr.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`radarr_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            radarr_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                radarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'radarr2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`radarr_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            radarr_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `radarr2`):

        ??? variable bool "`radarr2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            radarr2_autoheal_enabled: true
            ```

        ??? variable string "`radarr2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            radarr2_depends_on: ""
            ```

        ??? variable string "`radarr2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            radarr2_depends_on_delay: "0"
            ```

        ??? variable string "`radarr2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            radarr2_depends_on_healthchecks:
            ```

        ??? variable bool "`radarr2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            radarr2_diun_enabled: true
            ```

        ??? variable bool "`radarr2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            radarr2_dns_enabled: true
            ```

        ??? variable bool "`radarr2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            radarr2_docker_controller: true
            ```

        ??? variable bool "`radarr2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            radarr2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`radarr2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            radarr2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`radarr2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            radarr2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`radarr2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            radarr2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`radarr2_traefik_middleware_http_api_insecure`"

            ```yaml
            # Type: bool (true/false)
            radarr2_traefik_middleware_http_api_insecure:
            ```

        ??? variable bool "`radarr2_traefik_middleware_http_insecure`"

            ```yaml
            # Type: bool (true/false)
            radarr2_traefik_middleware_http_insecure:
            ```

        ??? variable bool "`radarr2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            radarr2_traefik_robot_enabled: true
            ```

        ??? variable bool "`radarr2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            radarr2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`radarr2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            radarr2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`radarr2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            radarr2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                radarr2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "radarr2.{{ user.domain }}"
                  - "radarr.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`radarr2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            radarr2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                radarr2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'radarr2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`radarr2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            radarr2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
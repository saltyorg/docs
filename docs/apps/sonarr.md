---
icon: material/docker
hide:
  - tags
tags:
  - sonarr
---

# Sonarr

## Overview

[Sonarr](https://sonarr.tv/) is a smart Personal Video Recorder (PVR) designed for Usenet and BitTorrent users, automating the process of finding, downloading, and managing TV show episodes.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://sonarr.tv/){: .header-icons } | [:octicons-link-16: Docs](https://wiki.servarr.com/sonarr/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Sonarr/Sonarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/sonarr){: .header-icons }|

---

## Deployment

```sh
sb install sonarr
```

## Usage

To access Sonarr, visit <https://sonarr.iYOUR_DOMAIN_NAMEi>

## Basics

### Settings

Click on "Settings" in the sidebar.  Click "Show Advanced" at the top of the Settings pane.

Make changes in the following sections:

!!! info "Settings"

    === "Media Management"

        These settings control management of media files.

        === "Episode Naming"

            - "Rename Episodes": `Yes`

            - "Replace Illegal Characters": `Yes`

            - Set your preferred naming format; here are some examples:

                <details>
                <summary>TRaSH' naming guide [Recommended]</summary> <br />

                Go to the [TRaSH Guides Sonarr naming scheme](https://trash-guides.info/Sonarr/Sonarr-recommended-naming-scheme/) for the latest updates.  These examples may be out of date.

                Example:  <br />
                ```
                Single Episode:

                The Series Title! (2010) - S01E01 - Episode Title 1 [AMZN WEBDL-1080p Proper][HDR][10bit][x264][DTS 5.1]-RlsGrp

                Multi Episode:

                The Series Title! (2010) - S01E01-E02-E03 - Episode Title [AMZN WEBDL-1080p Proper][HDR][10bit][x264][DTS 5.1]-RlsGrp
                ```

                Standard Episode Format: <br />
                ```
                {Series TitleYear} - S{season:00}E{episode:00} - {Episode CleanTitle} [{Preferred Words }{Quality Full}]{[MediaInfo VideoDynamicRange]}[{MediaInfo VideoBitDepth}bit]{[MediaInfo VideoCodec]}{[Mediainfo AudioCodec}{ Mediainfo AudioChannels]}{MediaInfo AudioLanguages}{-Release Group}
                ```

                for more examples and discussion see the reference: https://trash-guides.info/Sonarr/Sonarr-recommended-naming-scheme/
                </details>

                The TRaSH naming guide is recommended since some other tools, notably Kometa, expect it in their default setup.


                <details>
                <summary>Plex's Naming Preference</summary>

                Example: <br />
                ```
                /Gotham/Season 01/Gotham - s01e01 - Pilot.mkv
                ```

                Standard Episode Format: <br />
                ```
                {Series Title} - s{season:00}e{episode:00} - {Episode Title}
                ```

                Anime Episode Format: <br />
                ```
                {Series Title} - s{season:00}e{episode:00} - {Episode Title}
                ```

                Daily Episode Format: <br />
                ```
                {Series Title} - {Air-Date} - {Episode Title}
                ```

                Season Folder Format: <br />
                ```
                Season {season:00}
                ```

                Multi-Episode Style: <br />
                ```
                Prefixed Range
                ```

                Reference: https://support.plex.tv/articles/200220687-naming-series-season-based-tv-shows/  <br />
                </details>

        === "Folders"

            - "Create empty series folders": `No`

            - "Delete empty folders": `No`

        === "Importing"

            - "Skip Free Space Check": `No`

            - "Use Hardlinks instead of Copy": `Yes`

            - "Import Extra Files": `Yes` (_can be your preference_)

            - "Extra File Extensions": `srt, sub, idx`

        === "File Management"

            - "Ignore Deleted Episodes": `No` (_can be your preference_)

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

                ![Radarr NZBHydra2](../images/sonarr/sonarr-nzbhydra.png)

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

                ![Radarr Jackett](../images/sonarr/sonarr-jackett.png)

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

                Category: `sonarr`

                Use SSL: `No`

                Add Paused: `No`

            4. Your settings will look like this:

                ![Sonarr NZBGet Downloader](../images/sonarr/sonarr-nzbget.png)

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

                Category: `sonarr`

                Use SSL: `No`

                Add Paused: `No`

            4. Your settings will look like this:

                Either API Key **OR** Username/Password should be filled in, **not both**

                ![Sonarr Sabnzbd Downloader](../images/sonarr/sonarr-sabnzbd.png)

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

                Category: `sonarr`

                Directory: _Leave Blank_

            4.  Your settings will now look like this:

                ![sonarr ruTorrent Downloader](../images/sonarr/sonarr-rtorrent.png)

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

                Category: 'sonarr'

            4.  Your settings will now look like this:

                ![Radarr qBittorent Downloader](../images/sonarr/sonarr-qbittorrent.png)

            5.  Click "Save" to add qBittorrent

    === "Connect"

        These settings control connections to other applications or systems.

        === "Torrent Cleanup"

            Torrent Cleanup Script is a custom script that will cleanup torrents from ruTorrent that were auto-extracted, but still being seeded. So if the script detects that `.rar` files are in the folder that Sonarr just imported from, it will delete the imported video file(s), leaving just the `.rar` files for seeding.

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

                ![sonarr Torrent Cleanup Script](../images/sonarr/sonarr-torrentcleanup.png)

            5. Click "Save" to add the Torrent Cleanup script.


        === "Autoscan"

            IMPORTANT:  The Sonarr UI may differ from what is shown here; there may be additional events listed in the UI.  

            GENERALLY SPEAKING, if you have events listed that are not explicitly listed below, LEAVE THEM UNCHECKED.  Such events will generate errors in the autoscan logs; those errors can be ignored, but they are errors and can cause panic and confusion.

            MORE SPECIFICALLY, Autoscan is expecting a request that points to an individual file that is ready for Plex. so any event you may have that refers to a show being added, manual intervention, or anything else that is not "this specific video file ON DISK was imported/upgraded/deleted/etc", LEAVE IT UNCHECKED.


            1. Click "Settings" -> "Connect".

            2. Add a new "Webhook".

            3. Add the following:

                Name: Autoscan

                On Grab: `No`

                On Import: `Yes`

                On Upgrade:  `Yes`

                On Rename: `Yes`

                On Series Delete: `Yes`

                On Episode File Delete: `Yes`

                On Episode File Delete For Upgrade: `Yes`

                Tags: _Leave Blank_

                URL: `http://autoscan:3030/triggers/sonarr`

                Method:`POST`

                Username: AS SET IN AUTOSCAN CONFIG [defaults to Saltbox Username]

                Password: AS SET IN AUTOSCAN CONFIG [defaults to Saltbox Password]

            4. The settings will look like this:

                ![Sonarr Autoscan](../images/sonarr/sonarr-autoscan.png)


            5. Click "Save" to add Autoscan.


    === "General"

        These settings control general aspects of Sonarr.

        === "Start-Up"

            - "Bind Address: `*`

            - "Port Number": `8989`

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

            - "Branch": `main`

            - "Automatic": `Off`

        === "Save"

            - Click "Save".

### TV Path

1. When you are ready to add your first show to Sonarr, click the "Root Path" drop-down and select "Add a different path".

1. Click the blue "Browse" button, navigate to `/mnt/unionfs/Media/TV`, scroll to the bottom, and select "OK".

1. Click the green "check" button to add the path.

1. All TV shows added now will have that path set.

![Sonarr Add](../images/sonarr/sonarr-add.png)

### API Key

This is used during the setup of [Overseer](overseerr.md) and [Organizr](organizr.md).

- Go to "Settings" -> "General" -> "Security" -> "API Key".

### Guides

[TraSH Guides](https://trash-guides.info/Sonarr/)

## Next

<div class="directions-menu" markdown>

Are you setting Saltbox up for the first time?

<div markdown>

[**Continue to Radarr**:material-forward:](radarr.md){ .md-button }

</div>

</div>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `sonarr_instances`.

    ```yaml { .sb-show-on-unchecked title="Applies to all instances of sonarr:" }
    sonarr_role_web_subdomain: "custom"
    ```

    ```yaml { .sb-show-on-checked title="Applies to a specific instance (e.g., `sonarr2`):" }
    sonarr2_web_subdomain: "custom2"
    ```

<label class="md-button md-button--stretch" for="sb-checkbox--var-level">
   <input type="checkbox" id="sb-checkbox--var-level"><span class="sb-show-on-unchecked">Show instance-level variables</span><span class="sb-show-on-checked">Show role-level variables</span>
</label>

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `sonarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `sonarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`sonarr_instances`"

        ```yaml
        # Type: list
        sonarr_instances: ["sonarr"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            sonarr_instances: ["sonarr", "sonarr2"]
            ```

=== "Settings"

    ??? variable bool "`sonarr_role_external_auth`{ .sb-show-on-unchecked }`sonarr2_external_auth`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        sonarr_role_external_auth: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        sonarr2_external_auth: true
        ```

=== "Paths"

    ??? variable string "`sonarr_role_paths_folder`{ .sb-show-on-unchecked }`sonarr2_paths_folder`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_paths_folder: "{{ sonarr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_paths_folder: "{{ sonarr_name }}"
        ```

    ??? variable string "`sonarr_role_paths_location`{ .sb-show-on-unchecked }`sonarr2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_paths_location: "{{ server_appdata_path }}/{{ sonarr_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_paths_location: "{{ server_appdata_path }}/{{ sonarr_role_paths_folder }}"
        ```

    ??? variable string "`sonarr_role_paths_config_location`{ .sb-show-on-unchecked }`sonarr2_paths_config_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_paths_config_location: "{{ sonarr_role_paths_location }}/config.xml"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_paths_config_location: "{{ sonarr_role_paths_location }}/config.xml"
        ```

=== "Web"

    ??? variable string "`sonarr_role_web_subdomain`{ .sb-show-on-unchecked }`sonarr2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_web_subdomain: "{{ sonarr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_web_subdomain: "{{ sonarr_name }}"
        ```

    ??? variable string "`sonarr_role_web_domain`{ .sb-show-on-unchecked }`sonarr2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`sonarr_role_web_port`{ .sb-show-on-unchecked }`sonarr2_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_web_port: "8989"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_web_port: "8989"
        ```

    ??? variable string "`sonarr_role_web_url`{ .sb-show-on-unchecked }`sonarr2_web_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='sonarr') + '.' + lookup('role_var', '_web_domain', role='sonarr')
                              if (lookup('role_var', '_web_subdomain', role='sonarr') | length > 0)
                              else lookup('role_var', '_web_domain', role='sonarr')) }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='sonarr') + '.' + lookup('role_var', '_web_domain', role='sonarr')
                          if (lookup('role_var', '_web_subdomain', role='sonarr') | length > 0)
                          else lookup('role_var', '_web_domain', role='sonarr')) }}"
        ```

=== "DNS"

    ??? variable string "`sonarr_role_dns_record`{ .sb-show-on-unchecked }`sonarr2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='sonarr') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='sonarr') }}"
        ```

    ??? variable string "`sonarr_role_dns_zone`{ .sb-show-on-unchecked }`sonarr2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='sonarr') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_dns_zone: "{{ lookup('role_var', '_web_domain', role='sonarr') }}"
        ```

    ??? variable bool "`sonarr_role_dns_proxy`{ .sb-show-on-unchecked }`sonarr2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        sonarr_role_dns_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        sonarr2_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`sonarr_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`sonarr2_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`sonarr_role_traefik_middleware_default`{ .sb-show-on-unchecked }`sonarr2_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                    + (',themepark-' + sonarr_name
                                                      if (lookup('role_var', '_themepark_enabled', role='sonarr') and global_themepark_plugin_enabled)
                                                      else '') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_traefik_middleware_default: "{{ traefik_default_middleware
                                                + (',themepark-' + sonarr_name
                                                  if (lookup('role_var', '_themepark_enabled', role='sonarr') and global_themepark_plugin_enabled)
                                                  else '') }}"
        ```

    ??? variable string "`sonarr_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`sonarr2_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_traefik_middleware_custom: ""
        ```

    ??? variable string "`sonarr_role_traefik_certresolver`{ .sb-show-on-unchecked }`sonarr2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`sonarr_role_traefik_enabled`{ .sb-show-on-unchecked }`sonarr2_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        sonarr_role_traefik_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        sonarr2_traefik_enabled: true
        ```

    ??? variable bool "`sonarr_role_traefik_api_enabled`{ .sb-show-on-unchecked }`sonarr2_traefik_api_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        sonarr_role_traefik_api_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        sonarr2_traefik_api_enabled: true
        ```

    ??? variable string "`sonarr_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`sonarr2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/feed`) || PathPrefix(`/ping`)"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/feed`) || PathPrefix(`/ping`)"
        ```

=== "Theme"

    ??? variable bool "`sonarr_role_themepark_enabled`{ .sb-show-on-unchecked }`sonarr2_themepark_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        sonarr_role_themepark_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        sonarr2_themepark_enabled: false
        ```

    ??? variable string "`sonarr_role_themepark_app`{ .sb-show-on-unchecked }`sonarr2_themepark_app`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_themepark_app: "sonarr"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_themepark_app: "sonarr"
        ```

    ??? variable string "`sonarr_role_themepark_theme`{ .sb-show-on-unchecked }`sonarr2_themepark_theme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_themepark_theme: "{{ global_themepark_theme }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_themepark_theme: "{{ global_themepark_theme }}"
        ```

    ??? variable string "`sonarr_role_themepark_domain`{ .sb-show-on-unchecked }`sonarr2_themepark_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_themepark_domain: "{{ global_themepark_domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_themepark_domain: "{{ global_themepark_domain }}"
        ```

    ??? variable list "`sonarr_role_themepark_addons`{ .sb-show-on-unchecked }`sonarr2_themepark_addons`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_themepark_addons: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_themepark_addons: []
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`sonarr_role_docker_container`{ .sb-show-on-unchecked }`sonarr2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_container: "{{ sonarr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_container: "{{ sonarr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`sonarr_role_docker_image_pull`{ .sb-show-on-unchecked }`sonarr2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        sonarr_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        sonarr2_docker_image_pull: true
        ```

    ??? variable string "`sonarr_role_docker_image_repo`{ .sb-show-on-unchecked }`sonarr2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_image_repo: "ghcr.io/hotio/sonarr"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_image_repo: "ghcr.io/hotio/sonarr"
        ```

    ??? variable string "`sonarr_role_docker_image_tag`{ .sb-show-on-unchecked }`sonarr2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_image_tag: "release"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_image_tag: "release"
        ```

    ??? variable string "`sonarr_role_docker_image`{ .sb-show-on-unchecked }`sonarr2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='sonarr') }}:{{ lookup('role_var', '_docker_image_tag', role='sonarr') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='sonarr') }}:{{ lookup('role_var', '_docker_image_tag', role='sonarr') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`sonarr_role_docker_envs_default`{ .sb-show-on-unchecked }`sonarr2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        sonarr_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          UMASK: "002"
          TZ: "{{ tz }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        sonarr2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          UMASK: "002"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`sonarr_role_docker_envs_custom`{ .sb-show-on-unchecked }`sonarr2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        sonarr_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        sonarr2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`sonarr_role_docker_volumes_default`{ .sb-show-on-unchecked }`sonarr2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_volumes_default:
          - "{{ sonarr_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_volumes_default: 
          - "{{ sonarr_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
        ```

    ??? variable list "`sonarr_role_docker_volumes_legacy`{ .sb-show-on-unchecked }`sonarr2_docker_volumes_legacy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_volumes_legacy:
          - "/mnt/unionfs/Media/TV:/tv"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_volumes_legacy: 
          - "/mnt/unionfs/Media/TV:/tv"
        ```

    ??? variable list "`sonarr_role_docker_volumes_custom`{ .sb-show-on-unchecked }`sonarr2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable dict "`sonarr_role_docker_labels_default`{ .sb-show-on-unchecked }`sonarr2_docker_labels_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        sonarr_role_docker_labels_default: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        sonarr2_docker_labels_default: {}
        ```

    ??? variable dict "`sonarr_role_docker_labels_custom`{ .sb-show-on-unchecked }`sonarr2_docker_labels_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        sonarr_role_docker_labels_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        sonarr2_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`sonarr_role_docker_hostname`{ .sb-show-on-unchecked }`sonarr2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_hostname: "{{ sonarr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_hostname: "{{ sonarr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`sonarr_role_docker_networks_alias`{ .sb-show-on-unchecked }`sonarr2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_networks_alias: "{{ sonarr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_networks_alias: "{{ sonarr_name }}"
        ```

    ??? variable list "`sonarr_role_docker_networks_default`{ .sb-show-on-unchecked }`sonarr2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_networks_default: []
        ```

    ??? variable list "`sonarr_role_docker_networks_custom`{ .sb-show-on-unchecked }`sonarr2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`sonarr_role_docker_restart_policy`{ .sb-show-on-unchecked }`sonarr2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`sonarr_role_docker_state`{ .sb-show-on-unchecked }`sonarr2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    <h5>Resource Limits</h5>

    ??? variable int "`sonarr_role_docker_blkio_weight`{ .sb-show-on-unchecked }`sonarr2_docker_blkio_weight`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        sonarr_role_docker_blkio_weight:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        sonarr2_docker_blkio_weight:
        ```

    ??? variable int "`sonarr_role_docker_cpu_period`{ .sb-show-on-unchecked }`sonarr2_docker_cpu_period`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        sonarr_role_docker_cpu_period:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        sonarr2_docker_cpu_period:
        ```

    ??? variable int "`sonarr_role_docker_cpu_quota`{ .sb-show-on-unchecked }`sonarr2_docker_cpu_quota`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        sonarr_role_docker_cpu_quota:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        sonarr2_docker_cpu_quota:
        ```

    ??? variable int "`sonarr_role_docker_cpu_shares`{ .sb-show-on-unchecked }`sonarr2_docker_cpu_shares`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        sonarr_role_docker_cpu_shares:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        sonarr2_docker_cpu_shares:
        ```

    ??? variable string "`sonarr_role_docker_cpus`{ .sb-show-on-unchecked }`sonarr2_docker_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_cpus:
        ```

    ??? variable string "`sonarr_role_docker_cpuset_cpus`{ .sb-show-on-unchecked }`sonarr2_docker_cpuset_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_cpuset_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_cpuset_cpus:
        ```

    ??? variable string "`sonarr_role_docker_cpuset_mems`{ .sb-show-on-unchecked }`sonarr2_docker_cpuset_mems`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_cpuset_mems:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_cpuset_mems:
        ```

    ??? variable string "`sonarr_role_docker_kernel_memory`{ .sb-show-on-unchecked }`sonarr2_docker_kernel_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_kernel_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_kernel_memory:
        ```

    ??? variable string "`sonarr_role_docker_memory`{ .sb-show-on-unchecked }`sonarr2_docker_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_memory:
        ```

    ??? variable string "`sonarr_role_docker_memory_reservation`{ .sb-show-on-unchecked }`sonarr2_docker_memory_reservation`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_memory_reservation:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_memory_reservation:
        ```

    ??? variable string "`sonarr_role_docker_memory_swap`{ .sb-show-on-unchecked }`sonarr2_docker_memory_swap`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_memory_swap:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_memory_swap:
        ```

    ??? variable int "`sonarr_role_docker_memory_swappiness`{ .sb-show-on-unchecked }`sonarr2_docker_memory_swappiness`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        sonarr_role_docker_memory_swappiness:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        sonarr2_docker_memory_swappiness:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`sonarr_role_docker_cap_drop`{ .sb-show-on-unchecked }`sonarr2_docker_cap_drop`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_cap_drop:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_cap_drop:
        ```

    ??? variable list "`sonarr_role_docker_device_cgroup_rules`{ .sb-show-on-unchecked }`sonarr2_docker_device_cgroup_rules`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_device_cgroup_rules:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_device_cgroup_rules:
        ```

    ??? variable list "`sonarr_role_docker_device_read_bps`{ .sb-show-on-unchecked }`sonarr2_docker_device_read_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_device_read_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_device_read_bps:
        ```

    ??? variable list "`sonarr_role_docker_device_read_iops`{ .sb-show-on-unchecked }`sonarr2_docker_device_read_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_device_read_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_device_read_iops:
        ```

    ??? variable list "`sonarr_role_docker_device_requests`{ .sb-show-on-unchecked }`sonarr2_docker_device_requests`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_device_requests:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_device_requests:
        ```

    ??? variable list "`sonarr_role_docker_device_write_bps`{ .sb-show-on-unchecked }`sonarr2_docker_device_write_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_device_write_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_device_write_bps:
        ```

    ??? variable list "`sonarr_role_docker_device_write_iops`{ .sb-show-on-unchecked }`sonarr2_docker_device_write_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_device_write_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_device_write_iops:
        ```

    ??? variable list "`sonarr_role_docker_devices`{ .sb-show-on-unchecked }`sonarr2_docker_devices`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_devices:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_devices:
        ```

    ??? variable string "`sonarr_role_docker_devices_default`{ .sb-show-on-unchecked }`sonarr2_docker_devices_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_devices_default:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_devices_default:
        ```

    ??? variable bool "`sonarr_role_docker_privileged`{ .sb-show-on-unchecked }`sonarr2_docker_privileged`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        sonarr_role_docker_privileged:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        sonarr2_docker_privileged:
        ```

    ??? variable list "`sonarr_role_docker_security_opts`{ .sb-show-on-unchecked }`sonarr2_docker_security_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_security_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_security_opts:
        ```

    <h5>Networking</h5>

    ??? variable list "`sonarr_role_docker_dns_opts`{ .sb-show-on-unchecked }`sonarr2_docker_dns_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_dns_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_dns_opts:
        ```

    ??? variable list "`sonarr_role_docker_dns_search_domains`{ .sb-show-on-unchecked }`sonarr2_docker_dns_search_domains`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_dns_search_domains:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_dns_search_domains:
        ```

    ??? variable list "`sonarr_role_docker_dns_servers`{ .sb-show-on-unchecked }`sonarr2_docker_dns_servers`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_dns_servers:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_dns_servers:
        ```

    ??? variable dict "`sonarr_role_docker_hosts`{ .sb-show-on-unchecked }`sonarr2_docker_hosts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        sonarr_role_docker_hosts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        sonarr2_docker_hosts:
        ```

    ??? variable string "`sonarr_role_docker_hosts_use_common`{ .sb-show-on-unchecked }`sonarr2_docker_hosts_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_hosts_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_hosts_use_common:
        ```

    ??? variable string "`sonarr_role_docker_network_mode`{ .sb-show-on-unchecked }`sonarr2_docker_network_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_network_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_network_mode:
        ```

    <h5>Storage</h5>

    ??? variable bool "`sonarr_role_docker_keep_volumes`{ .sb-show-on-unchecked }`sonarr2_docker_keep_volumes`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        sonarr_role_docker_keep_volumes:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        sonarr2_docker_keep_volumes:
        ```

    ??? variable list "`sonarr_role_docker_mounts`{ .sb-show-on-unchecked }`sonarr2_docker_mounts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_mounts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_mounts:
        ```

    ??? variable string "`sonarr_role_docker_volume_driver`{ .sb-show-on-unchecked }`sonarr2_docker_volume_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_volume_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_volume_driver:
        ```

    ??? variable list "`sonarr_role_docker_volumes_from`{ .sb-show-on-unchecked }`sonarr2_docker_volumes_from`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_volumes_from:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_volumes_from:
        ```

    ??? variable string "`sonarr_role_docker_volumes_global`{ .sb-show-on-unchecked }`sonarr2_docker_volumes_global`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_volumes_global:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_volumes_global:
        ```

    ??? variable string "`sonarr_role_docker_working_dir`{ .sb-show-on-unchecked }`sonarr2_docker_working_dir`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_working_dir:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable dict "`sonarr_role_docker_healthcheck`{ .sb-show-on-unchecked }`sonarr2_docker_healthcheck`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        sonarr_role_docker_healthcheck:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        sonarr2_docker_healthcheck:
        ```

    ??? variable bool "`sonarr_role_docker_init`{ .sb-show-on-unchecked }`sonarr2_docker_init`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        sonarr_role_docker_init:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        sonarr2_docker_init:
        ```

    ??? variable string "`sonarr_role_docker_log_driver`{ .sb-show-on-unchecked }`sonarr2_docker_log_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_log_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_log_driver:
        ```

    ??? variable dict "`sonarr_role_docker_log_options`{ .sb-show-on-unchecked }`sonarr2_docker_log_options`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        sonarr_role_docker_log_options:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        sonarr2_docker_log_options:
        ```

    ??? variable bool "`sonarr_role_docker_output_logs`{ .sb-show-on-unchecked }`sonarr2_docker_output_logs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        sonarr_role_docker_output_logs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        sonarr2_docker_output_logs:
        ```

    <h5>Other Options</h5>

    ??? variable bool "`sonarr_role_docker_auto_remove`{ .sb-show-on-unchecked }`sonarr2_docker_auto_remove`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        sonarr_role_docker_auto_remove:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        sonarr2_docker_auto_remove:
        ```

    ??? variable list "`sonarr_role_docker_capabilities`{ .sb-show-on-unchecked }`sonarr2_docker_capabilities`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_capabilities:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_capabilities:
        ```

    ??? variable string "`sonarr_role_docker_cgroup_parent`{ .sb-show-on-unchecked }`sonarr2_docker_cgroup_parent`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_cgroup_parent:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_cgroup_parent:
        ```

    ??? variable string "`sonarr_role_docker_cgroupns_mode`{ .sb-show-on-unchecked }`sonarr2_docker_cgroupns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_cgroupns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_cgroupns_mode:
        ```

    ??? variable bool "`sonarr_role_docker_cleanup`{ .sb-show-on-unchecked }`sonarr2_docker_cleanup`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        sonarr_role_docker_cleanup:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        sonarr2_docker_cleanup:
        ```

    ??? variable list "`sonarr_role_docker_commands`{ .sb-show-on-unchecked }`sonarr2_docker_commands`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_commands:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_commands:
        ```

    ??? variable string "`sonarr_role_docker_create_timeout`{ .sb-show-on-unchecked }`sonarr2_docker_create_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_create_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_create_timeout:
        ```

    ??? variable string "`sonarr_role_docker_domainname`{ .sb-show-on-unchecked }`sonarr2_docker_domainname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_domainname:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_domainname:
        ```

    ??? variable string "`sonarr_role_docker_entrypoint`{ .sb-show-on-unchecked }`sonarr2_docker_entrypoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_entrypoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_entrypoint:
        ```

    ??? variable string "`sonarr_role_docker_env_file`{ .sb-show-on-unchecked }`sonarr2_docker_env_file`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_env_file:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_env_file:
        ```

    ??? variable list "`sonarr_role_docker_exposed_ports`{ .sb-show-on-unchecked }`sonarr2_docker_exposed_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_exposed_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_exposed_ports:
        ```

    ??? variable string "`sonarr_role_docker_force_kill`{ .sb-show-on-unchecked }`sonarr2_docker_force_kill`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_force_kill:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_force_kill:
        ```

    ??? variable list "`sonarr_role_docker_groups`{ .sb-show-on-unchecked }`sonarr2_docker_groups`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_groups:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_groups:
        ```

    ??? variable int "`sonarr_role_docker_healthy_wait_timeout`{ .sb-show-on-unchecked }`sonarr2_docker_healthy_wait_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        sonarr_role_docker_healthy_wait_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        sonarr2_docker_healthy_wait_timeout:
        ```

    ??? variable string "`sonarr_role_docker_ipc_mode`{ .sb-show-on-unchecked }`sonarr2_docker_ipc_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_ipc_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_ipc_mode:
        ```

    ??? variable string "`sonarr_role_docker_kill_signal`{ .sb-show-on-unchecked }`sonarr2_docker_kill_signal`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_kill_signal:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_kill_signal:
        ```

    ??? variable string "`sonarr_role_docker_labels_use_common`{ .sb-show-on-unchecked }`sonarr2_docker_labels_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_labels_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_labels_use_common:
        ```

    ??? variable list "`sonarr_role_docker_links`{ .sb-show-on-unchecked }`sonarr2_docker_links`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_links:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_links:
        ```

    ??? variable bool "`sonarr_role_docker_oom_killer`{ .sb-show-on-unchecked }`sonarr2_docker_oom_killer`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        sonarr_role_docker_oom_killer:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        sonarr2_docker_oom_killer:
        ```

    ??? variable int "`sonarr_role_docker_oom_score_adj`{ .sb-show-on-unchecked }`sonarr2_docker_oom_score_adj`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        sonarr_role_docker_oom_score_adj:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        sonarr2_docker_oom_score_adj:
        ```

    ??? variable bool "`sonarr_role_docker_paused`{ .sb-show-on-unchecked }`sonarr2_docker_paused`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        sonarr_role_docker_paused:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        sonarr2_docker_paused:
        ```

    ??? variable string "`sonarr_role_docker_pid_mode`{ .sb-show-on-unchecked }`sonarr2_docker_pid_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_pid_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_pid_mode:
        ```

    ??? variable list "`sonarr_role_docker_ports`{ .sb-show-on-unchecked }`sonarr2_docker_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_ports:
        ```

    ??? variable bool "`sonarr_role_docker_read_only`{ .sb-show-on-unchecked }`sonarr2_docker_read_only`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        sonarr_role_docker_read_only:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        sonarr2_docker_read_only:
        ```

    ??? variable bool "`sonarr_role_docker_recreate`{ .sb-show-on-unchecked }`sonarr2_docker_recreate`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        sonarr_role_docker_recreate:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        sonarr2_docker_recreate:
        ```

    ??? variable int "`sonarr_role_docker_restart_retries`{ .sb-show-on-unchecked }`sonarr2_docker_restart_retries`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        sonarr_role_docker_restart_retries:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        sonarr2_docker_restart_retries:
        ```

    ??? variable string "`sonarr_role_docker_runtime`{ .sb-show-on-unchecked }`sonarr2_docker_runtime`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_runtime:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_runtime:
        ```

    ??? variable string "`sonarr_role_docker_shm_size`{ .sb-show-on-unchecked }`sonarr2_docker_shm_size`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_shm_size:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_shm_size:
        ```

    ??? variable int "`sonarr_role_docker_stop_timeout`{ .sb-show-on-unchecked }`sonarr2_docker_stop_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        sonarr_role_docker_stop_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        sonarr2_docker_stop_timeout:
        ```

    ??? variable dict "`sonarr_role_docker_storage_opts`{ .sb-show-on-unchecked }`sonarr2_docker_storage_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        sonarr_role_docker_storage_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        sonarr2_docker_storage_opts:
        ```

    ??? variable list "`sonarr_role_docker_sysctls`{ .sb-show-on-unchecked }`sonarr2_docker_sysctls`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_sysctls:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_sysctls:
        ```

    ??? variable list "`sonarr_role_docker_tmpfs`{ .sb-show-on-unchecked }`sonarr2_docker_tmpfs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_tmpfs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_tmpfs:
        ```

    ??? variable list "`sonarr_role_docker_ulimits`{ .sb-show-on-unchecked }`sonarr2_docker_ulimits`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        sonarr_role_docker_ulimits:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        sonarr2_docker_ulimits:
        ```

    ??? variable string "`sonarr_role_docker_user`{ .sb-show-on-unchecked }`sonarr2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_user:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_user:
        ```

    ??? variable string "`sonarr_role_docker_userns_mode`{ .sb-show-on-unchecked }`sonarr2_docker_userns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_userns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_userns_mode:
        ```

    ??? variable string "`sonarr_role_docker_uts`{ .sb-show-on-unchecked }`sonarr2_docker_uts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        sonarr_role_docker_uts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        sonarr2_docker_uts:
        ```

=== "Global Override Options"

    ??? variable bool "`sonarr_role_autoheal_enabled`{ .sb-show-on-unchecked }`sonarr2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        sonarr_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        sonarr2_autoheal_enabled: true
        ```

    ??? variable string "`sonarr_role_depends_on`{ .sb-show-on-unchecked }`sonarr2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        sonarr_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        sonarr2_depends_on: ""
        ```

    ??? variable string "`sonarr_role_depends_on_delay`{ .sb-show-on-unchecked }`sonarr2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        sonarr_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        sonarr2_depends_on_delay: "0"
        ```

    ??? variable string "`sonarr_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`sonarr2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        sonarr_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        sonarr2_depends_on_healthchecks:
        ```

    ??? variable bool "`sonarr_role_diun_enabled`{ .sb-show-on-unchecked }`sonarr2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        sonarr_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        sonarr2_diun_enabled: true
        ```

    ??? variable bool "`sonarr_role_dns_enabled`{ .sb-show-on-unchecked }`sonarr2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        sonarr_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        sonarr2_dns_enabled: true
        ```

    ??? variable bool "`sonarr_role_docker_controller`{ .sb-show-on-unchecked }`sonarr2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        sonarr_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        sonarr2_docker_controller: true
        ```

    ??? variable bool "`sonarr_role_docker_volumes_download`{ .sb-show-on-unchecked }`sonarr2_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        sonarr_role_docker_volumes_download:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        sonarr2_docker_volumes_download:
        ```

    ??? variable bool "`sonarr_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`sonarr2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        sonarr_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        sonarr2_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`sonarr_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`sonarr2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        sonarr_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        sonarr2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`sonarr_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`sonarr2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        sonarr_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        sonarr2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`sonarr_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`sonarr2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        sonarr_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        sonarr2_traefik_gzip_enabled: false
        ```

    ??? variable bool "`sonarr_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`sonarr2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        sonarr_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        sonarr2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`sonarr_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`sonarr2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        sonarr_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        sonarr2_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`sonarr_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`sonarr2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        sonarr_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        sonarr2_traefik_robot_enabled: true
        ```

    ??? variable bool "`sonarr_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`sonarr2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        sonarr_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        sonarr2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`sonarr_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`sonarr2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        sonarr_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        sonarr2_traefik_wildcard_enabled: true
        ```

    ??? variable list "`sonarr_role_web_fqdn_override`{ .sb-show-on-unchecked }`sonarr2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        sonarr_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        sonarr2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            sonarr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "sonarr2.{{ user.domain }}"
              - "sonarr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            sonarr2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "sonarr2.{{ user.domain }}"
              - "sonarr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`sonarr_role_web_host_override`{ .sb-show-on-unchecked }`sonarr2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        sonarr_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        sonarr2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            sonarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'sonarr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            sonarr2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'sonarr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`sonarr_role_web_scheme`{ .sb-show-on-unchecked }`sonarr2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        sonarr_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        sonarr2_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
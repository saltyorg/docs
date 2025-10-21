---
hide:
  - tags
tags:
  - plex
  - pms
---

# Plex

## What is it?

[Plex](https://plex.tv/) is a media server.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://plex.tv/){: .header-icons } | [:octicons-link-16: Docs](https://support.plex.tv/articles/){: .header-icons } | :octicons-mark-github-16: Github | [:material-docker: Docker](https://hub.docker.com/r/plexinc/pms-docker){: .header-icons }|

## URL

1. To access Plex, visit `https://plex._yourdomain.com_`

2. Login with your Plex account

    ![](../images/plex-media-server/plex-01-signin.png)

## Setup Wizard

1. First time you log in, you will be presented with a welcome screen. Click "GOT IT!" to continue.

    ![](../images/plex-media-server/plex-02-intro.png)

2. Next screen will show you your server, with a randomly generated name. Give it a friendly name and click "NEXT".

    ![](../images/plex-media-server/plex-03-server-setup-1.png)

3. On the next screen, click "NEXT" (we will add Libraries later).

    ![](../images/plex-media-server/plex-04-server-setup-2.png)

4. Click "DONE".

    ![](../images/plex-media-server/plex-05-server-setup-3.png)

!!! info "Settings"

    === "Library"

        1. Click the Settings icon (top right) &rightarrow; "Server" (top) &rightarrow; "Library" (left).  Click "SHOW ADVANCED" in the upper right.

        2. Set the following:

            - "Empty trash automatically after every scan": `enabled`

                - THIS IS A CHANGE FROM WHEN _Plex Autoscan_ WAS THE DEFAULT

                - Autoscan is now the default scan app, and it does not empty trash

            - "Allow media deletion": `enabled`

            - "Generate video preview thumbnails": `never`

            - "Generate intro video markers": `never`

            - "Generate chapter thumbnails": `never`

            - "Analyze audio tracks for loudness": `never`

            - "Analyze audio tracks for sonic features": `never`

                > The reasoning behind disabling these things is mostly related to Google Drive API usage, data transfer, and disk space.  Accessing large portions of a given video file to generate thumbnails *may* generate large numbers of Google Drive API calls, and large amounts of data transfer.  Either of these things *may* result in your account suffering one of the various types of 24-hour bans Google hands out, which *may* prevent your server from playing media at all.  Also, storing these images *will* greatly inflate the size of `/opt/plex`, which can affect the speed of backups, your ability to download, and anything else related to disk space usage.  These are generally considered Bad Things, so the recommendation is to avoid the possibility by turning these options off.

         1. Click "SAVE CHANGES".

            ![](../images/plex-media-server/plex-07-library.png)


    === "Network"

        1. Click the Settings icon (top right) &rightarrow; "Server" (top) &rightarrow; "Network" (left).

        2. Set the following:

            - "Secure Connections": `Preferred`.

            - "Enable local network discovery (GDM)": `disabled`.

            - "Remote streams allowed per user": _your preference_.

            - "Custom server access URLs" will be prefilled; do not edit this field as it will be overwritten.

         1. Click "SAVE CHANGES".

            ![Plex Network settings page showing custom server access URLs configuration](../images/plex-media-server/plex-08-network.jpeg)


    === "Transcoder"

        1. Click the Settings icon (top right) &rightarrow; "Server" (top) &rightarrow; "Transcoder" (left).

        2. Set the following:

            - "Transcoder temporary directory": `/transcode`

            - "Transcoder default throttle buffer": `150`

            - "Use hardware acceleration when available": `enabled`

            - "Maximum simultaneous video transcode": `unlimited`

        3. Click "SAVE CHANGES".

            ![](../images/plex-media-server/plex-09-transcoder.png)


    === "DLNA"

        1. Click the Settings icon (top right) &rightarrow; "Server" (top) &rightarrow; "DLNA" (left).

        2. Set the following:

            - "Enable the DLNA server": `disabled`

            - "DLNA server timeline reporting": `disabled`

        3. Click "SAVE CHANGES".

            ![](../images/plex-media-server/plex-10-dlna.png)

    === "Scheduled Tasks"

        1. Click the Settings icon (top right) &rightarrow; "Server" (top) &rightarrow; "Scheduled Tasks" (left).

        2. Set the following:

            - "Update all libraries during maintenance": `disabled`

            - "Upgrade media analysis during maintenance": `disabled`

            - "Perform extensive media analysis during maintenance": `disabled`

        3. Click "SAVE CHANGES".

            ![Plex Scheduled Tasks settings showing extensive media analysis disabled](../images/plex-media-server/plex-11-schedule.jpeg)

    === "Remote Access"

        1. Click the Settings icon (top right) &rightarrow; "Server" (top) &rightarrow; "Remote Access" (left).

        2. Click the grey button labelled "Disable Remote Access"

            - You will see a scary warning.  You are sure, so click the red "Disable" button.

            ![](../images/plex-media-server/plex-11a-remote.png)


## Add Media Libraries

In this section, we will add two libraries: one for Movies and one for TV.

_Note: If you would like to have custom Plex libraries (more than just a Movies and TV one), see [Customizing Plex Libraries](../reference/customizing-plex-libs.md)._

!!! info "Libraries"

    === "Add the Movie Library"

        1. In the main Plex screen (Home icon on the top left), click "+" next to "LIBRARIES".

            ![](../images/plex-media-server/plex-12-add-library.png)

        2. In the "Add Library" window, select "Movies" and click "NEXT".

            ![](../images/plex-media-server/plex-13-movies-lib.png)

        3. Click "BROWSE FOR MEDIA FOLDER".

            ![](../images/plex-media-server/plex-14-movies-add-folder.png)

        4. Navigate to `/mnt/unionfs/Media/Movies`, and then click the "ADD" button.

            ![Plex movie folder selection](../images/plex-media-server/plex-15-movies-choose-folder.png)

        5. You will now see `/mnt/unionfs/Media/Movies` in the text box (don't click "ADD LIBRARY" yet).

            ![](../images/plex-media-server/plex-16-movies-path.png)

        6. Click "Advanced" on the left.

        7. Set the following:

            - "Enable Cinema Trailers": `disabled` (optional)

            - "Enable video preview thumbnails": `disabled`

            - "Find trailers and extras automatically (Plex Pass required)": `disabled` (optional)

        8. Click "ADD LIBRARY".

            ![](../images/plex-media-server/plex-17-movies-advanced.png)

    === "Add the TV Library"

        1. In the main Plex screen (Home icon on the top left), click "+" next to "LIBRARIES".

            ![](../images/plex-media-server/plex-18-add-library.png)

        2. In the "Add Library" window, select "TV Shows" and click "NEXT".

            ![](../images/plex-media-server/plex-19-tv-lib.png)

        3. Click "BROWSE FOR MEDIA FOLDER".

            ![](../images/plex-media-server/plex-20-tv-add-folder.png)

        4. Navigate to `/mnt/unionfs/Media/TV`, and then click the "ADD" button.

            ![Plex TV folder selection](../images/plex-media-server/plex-21-tv-choose-folder.png)

        5. You will now see `/mnt/unionfs/Media/TV` in the text box (don't click "ADD LIBRARY" yet).

            ![](../images/plex-media-server/plex-22-tv-path.png)

        6. Click "Advanced" on the left.

        7. Set the following:

            - "Enable video preview thumbnails": `disabled`

            - "Find trailers and extras automatically (Plex Pass required)": `disabled` (optional)

        8. Click "ADD LIBRARY".

            ![](../images/plex-media-server/plex-23-tv-advanced.png)

## Scan Media libraries

As mentioned in the [Introduction](../saltbox/basics/basics.md) page, [Autoscan](autoscan.md) will automatically scan the media files into Plex as they are downloaded, but this will require the Plex database to not be completely empty. So for every new library that is added, a one-time, manual scan is required.

To do so:

1. Click the 3 dots next to a Plex library.

2. Select "Scan Library Files".

   ![](../images/plex-media-server/plex-24-scan-library.png)

3. Repeat steps 1-2 for each library.

## Webtools

If you want to install Webtools for Plex, set:

```
plex_plugin_webtools: true
```

in the inventory and run [or rerun] the `plex` tag:

```
sb install plex
```

To set up Webtools and install 3rd party add-ons, go to `https://plex-webtools._yourdomain.com_` and log in with your Plex account.

## Next

Are you setting Saltbox up for the first time?  Continue to [Autoscan](autoscan.md).

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `plex_instances`.

    === "Role-level Override"

        Applies to all instances of plex:

        ```yaml
        plex_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `plex2`):

        ```yaml
        plex2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `plex_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `plex_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`plex_instances`"

        ```yaml
        # Type: list
        plex_instances: ["plex"]
        ```

        !!! example

            ```yaml
            # Type: list
            plex_instances: ["plex", "plex2"]
            ```

=== "Settings"

    === "Role-level"

        ??? variable bool "`plex_role_open_main_ports`"

            ```yaml
            # Do not enable globally if deploying multiple instances
            # Type: bool (true/false)
            plex_role_open_main_ports: false
            ```

        ??? variable bool "`plex_role_open_local_ports`"

            ```yaml
            # Do not enable globally if deploying multiple instances
            # Type: bool (true/false)
            plex_role_open_local_ports: false
            ```

        ??? variable bool "`plex_role_plugin_webtools`"

            ```yaml
            # Type: bool (true/false)
            plex_role_plugin_webtools: false
            ```

        ??? variable bool "`plex_role_plugin_sub_zero`"

            ```yaml
            # Type: bool (true/false)
            plex_role_plugin_sub_zero: false
            ```

        ??? variable bool "`plex_role_insecure`"

            ```yaml
            # Disables Traefik's HTTP to HTTPS redirect for Plex
            # Allows older clients with certificate issues to connect insecurely
            # Type: bool (true/false)
            plex_role_insecure: false
            ```

        ??? variable string "`plex_role_lan_ip`"

            ```yaml
            # Adds the IP specified here to the advertised urls Plex broadcasts to clients
            # Useful to avoid traffic going through your WAN when hairpin NAT is not available
            # Type: string
            plex_role_lan_ip: ""
            ```

        ??? variable string "`plex_role_auth_token_proxy`"

            ```yaml
            # For instances this works the same as usual plex2_auth_token_proxy for an instance named plex2.
            # Type: string
            plex_role_auth_token_proxy: ""
            ```

    === "Instance-level"

        ??? variable bool "`plex2_open_main_ports`"

            ```yaml
            # Do not enable globally if deploying multiple instances
            # Type: bool (true/false)
            plex2_open_main_ports: false
            ```

        ??? variable bool "`plex2_open_local_ports`"

            ```yaml
            # Do not enable globally if deploying multiple instances
            # Type: bool (true/false)
            plex2_open_local_ports: false
            ```

        ??? variable bool "`plex2_plugin_webtools`"

            ```yaml
            # Type: bool (true/false)
            plex2_plugin_webtools: false
            ```

        ??? variable bool "`plex2_plugin_sub_zero`"

            ```yaml
            # Type: bool (true/false)
            plex2_plugin_sub_zero: false
            ```

        ??? variable bool "`plex2_insecure`"

            ```yaml
            # Disables Traefik's HTTP to HTTPS redirect for Plex
            # Allows older clients with certificate issues to connect insecurely
            # Type: bool (true/false)
            plex2_insecure: false
            ```

        ??? variable string "`plex2_lan_ip`"

            ```yaml
            # Adds the IP specified here to the advertised urls Plex broadcasts to clients
            # Useful to avoid traffic going through your WAN when hairpin NAT is not available
            # Type: string
            plex2_lan_ip: ""
            ```

        ??? variable string "`plex2_auth_token_proxy`"

            ```yaml
            # For instances this works the same as usual plex2_auth_token_proxy for an instance named plex2.
            # Type: string
            plex2_auth_token_proxy: ""
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`plex_role_paths_folder`"

            ```yaml
            # Type: string
            plex_role_paths_folder: "{{ plex_name }}"
            ```

        ??? variable string "`plex_role_paths_location`"

            ```yaml
            # Type: string
            plex_role_paths_location: "{{ server_appdata_path }}/{{ plex_role_paths_folder }}"
            ```

        ??? variable string "`plex_role_paths_transcodes_location`"

            ```yaml
            # Type: string
            plex_role_paths_transcodes_location: "{{ transcodes_path }}/{{ plex_role_paths_folder }}"
            ```

        ??? variable string "`plex_role_paths_application_support_location`"

            ```yaml
            # Type: string
            plex_role_paths_application_support_location: "{{ plex_role_paths_location }}/Library/Application Support/Plex Media Server"
            ```

        ??? variable string "`plex_role_paths_config_location`"

            ```yaml
            # Type: string
            plex_role_paths_config_location: "{{ plex_role_paths_application_support_location }}/Preferences.xml"
            ```

        ??? variable string "`plex_role_paths_log_location`"

            ```yaml
            # Type: string
            plex_role_paths_log_location: "{{ plex_role_paths_application_support_location }}/Logs"
            ```

        ??? variable string "`plex_role_paths_plugins_location`"

            ```yaml
            # Type: string
            plex_role_paths_plugins_location: "{{ plex_role_paths_application_support_location }}/Plug-ins"
            ```

        ??? variable string "`plex_role_paths_plugin_support_location`"

            ```yaml
            # Type: string
            plex_role_paths_plugin_support_location: "{{ plex_role_paths_application_support_location }}/Plug-in Support"
            ```

        ??? variable string "`plex_role_paths_db_location`"

            ```yaml
            # Type: string
            plex_role_paths_db_location: "{{ plex_role_paths_plugin_support_location }}/Databases/com.plexapp.plugins.library.db"
            ```

        ??? variable string "`plex_role_paths_db_blobs_location`"

            ```yaml
            # Type: string
            plex_role_paths_db_blobs_location: "{{ plex_role_paths_plugin_support_location }}/Databases/com.plexapp.plugins.library.blobs.db"
            ```

    === "Instance-level"

        ??? variable string "`plex2_paths_folder`"

            ```yaml
            # Type: string
            plex2_paths_folder: "{{ plex_name }}"
            ```

        ??? variable string "`plex2_paths_location`"

            ```yaml
            # Type: string
            plex2_paths_location: "{{ server_appdata_path }}/{{ plex_role_paths_folder }}"
            ```

        ??? variable string "`plex2_paths_transcodes_location`"

            ```yaml
            # Type: string
            plex2_paths_transcodes_location: "{{ transcodes_path }}/{{ plex_role_paths_folder }}"
            ```

        ??? variable string "`plex2_paths_application_support_location`"

            ```yaml
            # Type: string
            plex2_paths_application_support_location: "{{ plex_role_paths_location }}/Library/Application Support/Plex Media Server"
            ```

        ??? variable string "`plex2_paths_config_location`"

            ```yaml
            # Type: string
            plex2_paths_config_location: "{{ plex_role_paths_application_support_location }}/Preferences.xml"
            ```

        ??? variable string "`plex2_paths_log_location`"

            ```yaml
            # Type: string
            plex2_paths_log_location: "{{ plex_role_paths_application_support_location }}/Logs"
            ```

        ??? variable string "`plex2_paths_plugins_location`"

            ```yaml
            # Type: string
            plex2_paths_plugins_location: "{{ plex_role_paths_application_support_location }}/Plug-ins"
            ```

        ??? variable string "`plex2_paths_plugin_support_location`"

            ```yaml
            # Type: string
            plex2_paths_plugin_support_location: "{{ plex_role_paths_application_support_location }}/Plug-in Support"
            ```

        ??? variable string "`plex2_paths_db_location`"

            ```yaml
            # Type: string
            plex2_paths_db_location: "{{ plex_role_paths_plugin_support_location }}/Databases/com.plexapp.plugins.library.db"
            ```

        ??? variable string "`plex2_paths_db_blobs_location`"

            ```yaml
            # Type: string
            plex2_paths_db_blobs_location: "{{ plex_role_paths_plugin_support_location }}/Databases/com.plexapp.plugins.library.blobs.db"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`plex_role_web_subdomain`"

            ```yaml
            # Type: string
            plex_role_web_subdomain: "{{ plex_name }}"
            ```

        ??? variable string "`plex_role_web_domain`"

            ```yaml
            # Type: string
            plex_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`plex_role_web_port`"

            ```yaml
            # Type: string
            plex_role_web_port: "32400"
            ```

        ??? variable string "`plex_role_web_http_port`"

            ```yaml
            # Type: string
            plex_role_web_http_port: "32400"
            ```

        ??? variable string "`plex_role_web_url`"

            ```yaml
            # Type: string
            plex_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='plex') + '.' + lookup('role_var', '_web_domain', role='plex')
                                if (lookup('role_var', '_web_subdomain', role='plex') | length > 0)
                                else lookup('role_var', '_web_domain', role='plex')) }}"
            ```

        ??? variable string "`plex_role_webtools_web_subdomain`"

            ```yaml
            # Type: string
            plex_role_webtools_web_subdomain: "{{ plex_name }}-webtools"
            ```

        ??? variable string "`plex_role_webtools_web_domain`"

            ```yaml
            # Type: string
            plex_role_webtools_web_domain: "{{ lookup('role_var', '_web_domain', role='plex') }}"
            ```

        ??? variable string "`plex_role_webtools_web_port`"

            ```yaml
            # Type: string
            plex_role_webtools_web_port: "33400"
            ```

        ??? variable string "`plex_role_webtools_host`"

            ```yaml
            # Type: string
            plex_role_webtools_host: "{{ lookup('role_var', '_webtools_web_subdomain', role='plex') + '.' + lookup('role_var', '_webtools_web_domain', role='plex') }}"
            ```

        ??? variable string "`plex_role_web_insecure_url`"

            ```yaml
            # Type: string
            plex_role_web_insecure_url: "{{ 'http://' + (lookup('role_var', '_web_subdomain', role='plex') + '.' + lookup('role_var', '_web_domain', role='plex')
                                         if (lookup('role_var', '_web_subdomain', role='plex') | length > 0)
                                         else lookup('role_var', '_web_domain', role='plex')) }}"
            ```

    === "Instance-level"

        ??? variable string "`plex2_web_subdomain`"

            ```yaml
            # Type: string
            plex2_web_subdomain: "{{ plex_name }}"
            ```

        ??? variable string "`plex2_web_domain`"

            ```yaml
            # Type: string
            plex2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`plex2_web_port`"

            ```yaml
            # Type: string
            plex2_web_port: "32400"
            ```

        ??? variable string "`plex2_web_http_port`"

            ```yaml
            # Type: string
            plex2_web_http_port: "32400"
            ```

        ??? variable string "`plex2_web_url`"

            ```yaml
            # Type: string
            plex2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='plex') + '.' + lookup('role_var', '_web_domain', role='plex')
                            if (lookup('role_var', '_web_subdomain', role='plex') | length > 0)
                            else lookup('role_var', '_web_domain', role='plex')) }}"
            ```

        ??? variable string "`plex2_webtools_web_subdomain`"

            ```yaml
            # Type: string
            plex2_webtools_web_subdomain: "{{ plex_name }}-webtools"
            ```

        ??? variable string "`plex2_webtools_web_domain`"

            ```yaml
            # Type: string
            plex2_webtools_web_domain: "{{ lookup('role_var', '_web_domain', role='plex') }}"
            ```

        ??? variable string "`plex2_webtools_web_port`"

            ```yaml
            # Type: string
            plex2_webtools_web_port: "33400"
            ```

        ??? variable string "`plex2_webtools_host`"

            ```yaml
            # Type: string
            plex2_webtools_host: "{{ lookup('role_var', '_webtools_web_subdomain', role='plex') + '.' + lookup('role_var', '_webtools_web_domain', role='plex') }}"
            ```

        ??? variable string "`plex2_web_insecure_url`"

            ```yaml
            # Type: string
            plex2_web_insecure_url: "{{ 'http://' + (lookup('role_var', '_web_subdomain', role='plex') + '.' + lookup('role_var', '_web_domain', role='plex')
                                     if (lookup('role_var', '_web_subdomain', role='plex') | length > 0)
                                     else lookup('role_var', '_web_domain', role='plex')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`plex_role_dns_record`"

            ```yaml
            # Type: string
            plex_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='plex') }}"
            ```

        ??? variable string "`plex_role_dns_zone`"

            ```yaml
            # Type: string
            plex_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='plex') }}"
            ```

        ??? variable bool "`plex_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            plex_role_dns_proxy: "{{ dns_proxied }}"
            ```

        ??? variable string "`plex_role_webtools_dns_record`"

            ```yaml
            # Type: string
            plex_role_webtools_dns_record: "{{ lookup('role_var', '_webtools_web_subdomain', role='plex') }}"
            ```

        ??? variable string "`plex_role_webtools_dns_zone`"

            ```yaml
            # Type: string
            plex_role_webtools_dns_zone: "{{ lookup('role_var', '_webtools_web_domain', role='plex') }}"
            ```

        ??? variable bool "`plex_role_webtools_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            plex_role_webtools_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`plex2_dns_record`"

            ```yaml
            # Type: string
            plex2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='plex') }}"
            ```

        ??? variable string "`plex2_dns_zone`"

            ```yaml
            # Type: string
            plex2_dns_zone: "{{ lookup('role_var', '_web_domain', role='plex') }}"
            ```

        ??? variable bool "`plex2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            plex2_dns_proxy: "{{ dns_proxied }}"
            ```

        ??? variable string "`plex2_webtools_dns_record`"

            ```yaml
            # Type: string
            plex2_webtools_dns_record: "{{ lookup('role_var', '_webtools_web_subdomain', role='plex') }}"
            ```

        ??? variable string "`plex2_webtools_dns_zone`"

            ```yaml
            # Type: string
            plex2_webtools_dns_zone: "{{ lookup('role_var', '_webtools_web_domain', role='plex') }}"
            ```

        ??? variable bool "`plex2_webtools_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            plex2_webtools_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`plex_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            plex_role_traefik_sso_middleware: ""
            ```

        ??? variable string "`plex_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            plex_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                      + (',themepark-' + plex_name
                                                        if (lookup('role_var', '_themepark_enabled', role='plex') and global_themepark_plugin_enabled)
                                                        else '') }}"
            ```

        ??? variable string "`plex_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            plex_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`plex_role_traefik_certresolver`"

            ```yaml
            # Type: string
            plex_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`plex_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            plex_role_traefik_enabled: true
            ```

        ??? variable bool "`plex_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            plex_role_traefik_api_enabled: false
            ```

        ??? variable string "`plex_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            plex_role_traefik_api_endpoint: ""
            ```

        ??? variable bool "`plex_role_traefik_error_pages_enabled`"

            ```yaml
            # Type: bool (true/false)
            plex_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`plex_role_traefik_gzip_enabled`"

            ```yaml
            # Type: bool (true/false)
            plex_role_traefik_gzip_enabled: false
            ```

        ??? variable string "`plex_role_traefik_middleware_http`"

            ```yaml
            # Type: string
            plex_role_traefik_middleware_http: "{{ 'globalHeaders@file'
                                                if lookup('role_var', '_insecure', role='plex')
                                                else traefik_default_middleware_default_http }}"
            ```

        ??? variable string "`plex_role_web_serverstransport`"

            ```yaml
            # Type: string
            plex_role_web_serverstransport: "skipverify@file"
            ```

        ??? variable string "`plex_role_webtools_traefik_sso_middleware`"

            ```yaml
            # Type: string
            plex_role_webtools_traefik_sso_middleware: ""
            ```

        ??? variable string "`plex_role_webtools_traefik_middleware_default`"

            ```yaml
            # Type: string
            plex_role_webtools_traefik_middleware_default: "{{ traefik_default_middleware
                                                               + (',' + lookup('role_var', '_webtools_traefik_sso_middleware', role='plex')
                                                                 if (lookup('role_var', '_webtools_traefik_sso_middleware', role='plex') | length > 0)
                                                                 else '') }}"
            ```

        ??? variable string "`plex_role_webtools_traefik_middleware_custom`"

            ```yaml
            # Type: string
            plex_role_webtools_traefik_middleware_custom: ""
            ```

        ??? variable string "`plex_role_webtools_traefik_certresolver`"

            ```yaml
            # Type: string
            plex_role_webtools_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable string "`plex_role_webtools_traefik_router`"

            ```yaml
            # Type: string
            plex_role_webtools_traefik_router: "{{ lookup('role_var', '_webtools_web_subdomain', role='plex') }}"
            ```

    === "Instance-level"

        ??? variable string "`plex2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            plex2_traefik_sso_middleware: ""
            ```

        ??? variable string "`plex2_traefik_middleware_default`"

            ```yaml
            # Type: string
            plex2_traefik_middleware_default: "{{ traefik_default_middleware
                                                  + (',themepark-' + plex_name
                                                    if (lookup('role_var', '_themepark_enabled', role='plex') and global_themepark_plugin_enabled)
                                                    else '') }}"
            ```

        ??? variable string "`plex2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            plex2_traefik_middleware_custom: ""
            ```

        ??? variable string "`plex2_traefik_certresolver`"

            ```yaml
            # Type: string
            plex2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`plex2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            plex2_traefik_enabled: true
            ```

        ??? variable bool "`plex2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            plex2_traefik_api_enabled: false
            ```

        ??? variable string "`plex2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            plex2_traefik_api_endpoint: ""
            ```

        ??? variable bool "`plex2_traefik_error_pages_enabled`"

            ```yaml
            # Type: bool (true/false)
            plex2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`plex2_traefik_gzip_enabled`"

            ```yaml
            # Type: bool (true/false)
            plex2_traefik_gzip_enabled: false
            ```

        ??? variable string "`plex2_traefik_middleware_http`"

            ```yaml
            # Type: string
            plex2_traefik_middleware_http: "{{ 'globalHeaders@file'
                                            if lookup('role_var', '_insecure', role='plex')
                                            else traefik_default_middleware_default_http }}"
            ```

        ??? variable string "`plex2_web_serverstransport`"

            ```yaml
            # Type: string
            plex2_web_serverstransport: "skipverify@file"
            ```

        ??? variable string "`plex2_webtools_traefik_sso_middleware`"

            ```yaml
            # Type: string
            plex2_webtools_traefik_sso_middleware: ""
            ```

        ??? variable string "`plex2_webtools_traefik_middleware_default`"

            ```yaml
            # Type: string
            plex2_webtools_traefik_middleware_default: "{{ traefik_default_middleware
                                                           + (',' + lookup('role_var', '_webtools_traefik_sso_middleware', role='plex')
                                                             if (lookup('role_var', '_webtools_traefik_sso_middleware', role='plex') | length > 0)
                                                             else '') }}"
            ```

        ??? variable string "`plex2_webtools_traefik_middleware_custom`"

            ```yaml
            # Type: string
            plex2_webtools_traefik_middleware_custom: ""
            ```

        ??? variable string "`plex2_webtools_traefik_certresolver`"

            ```yaml
            # Type: string
            plex2_webtools_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable string "`plex2_webtools_traefik_router`"

            ```yaml
            # Type: string
            plex2_webtools_traefik_router: "{{ lookup('role_var', '_webtools_web_subdomain', role='plex') }}"
            ```

=== "Theme"

    === "Role-level"

        ??? variable bool "`plex_role_themepark_enabled`"

            ```yaml
            # Type: bool (true/false)
            plex_role_themepark_enabled: false
            ```

        ??? variable string "`plex_role_themepark_theme`"

            ```yaml
            # Options can be found at https://docs.theme-park.dev/themes/plex/
            # Type: string
            plex_role_themepark_theme: "{{ global_themepark_theme }}"
            ```

        ??? variable string "`plex_role_themepark_domain`"

            ```yaml
            # Allows you to override the url where CSS files can be found
            # Type: string
            plex_role_themepark_domain: "{{ global_themepark_domain }}"
            ```

        ??? variable list "`plex_role_themepark_addons`"

            ```yaml
            # Options can be found at https://docs.theme-park.dev/themes/addons/
            # Type: list
            plex_role_themepark_addons: []
            ```

    === "Instance-level"

        ??? variable bool "`plex2_themepark_enabled`"

            ```yaml
            # Type: bool (true/false)
            plex2_themepark_enabled: false
            ```

        ??? variable string "`plex2_themepark_theme`"

            ```yaml
            # Options can be found at https://docs.theme-park.dev/themes/plex/
            # Type: string
            plex2_themepark_theme: "{{ global_themepark_theme }}"
            ```

        ??? variable string "`plex2_themepark_domain`"

            ```yaml
            # Allows you to override the url where CSS files can be found
            # Type: string
            plex2_themepark_domain: "{{ global_themepark_domain }}"
            ```

        ??? variable list "`plex2_themepark_addons`"

            ```yaml
            # Options can be found at https://docs.theme-park.dev/themes/addons/
            # Type: list
            plex2_themepark_addons: []
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`plex_role_docker_container`"

            ```yaml
            # Type: string
            plex_role_docker_container: "{{ plex_name }}"
            ```

        ##### Image

        ??? variable bool "`plex_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            plex_role_docker_image_pull: true
            ```

        ??? variable string "`plex_role_docker_image_repo`"

            ```yaml
            # Type: string
            plex_role_docker_image_repo: "plexinc/pms-docker"
            ```

        ??? variable string "`plex_role_docker_image_tag`"

            ```yaml
            # Type: string
            plex_role_docker_image_tag: "latest"
            ```

        ??? variable string "`plex_role_docker_image`"

            ```yaml
            # Type: string
            plex_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='plex') }}:{{ lookup('role_var', '_docker_image_tag', role='plex') }}"
            ```

        ##### Ports

        ??? variable string "`plex_role_docker_ports_32400`"

            ```yaml
            # Type: string
            plex_role_docker_ports_32400: "{{ port_lookup_32400.meta.port
                                           if (port_lookup_32400.meta.port is defined) and (port_lookup_32400.meta.port | trim | length > 0)
                                           else '32400' }}"
            ```

        ??? variable list "`plex_role_docker_ports_defaults`"

            ```yaml
            # Type: list
            plex_role_docker_ports_defaults: []
            ```

        ??? variable list "`plex_role_docker_ports_custom`"

            ```yaml
            # Type: list
            plex_role_docker_ports_custom: []
            ```

        ##### Envs

        ??? variable string "`plex_role_docker_envs_advertise_ip_url`"

            ```yaml
            # Type: string
            plex_role_docker_envs_advertise_ip_url: "{{ lookup('role_var', '_web_url', role='plex') + ':443,' + lookup('role_var', '_web_insecure_url', role='plex') + ':80'
                                                     if lookup('role_var', '_insecure', role='plex')
                                                     else lookup('role_var', '_web_url', role='plex') + ':443' }}"
            ```

        ??? variable string "`plex_role_docker_envs_advertise_ip`"

            ```yaml
            # Type: string
            plex_role_docker_envs_advertise_ip: "{{ 'http://' + lookup('role_var', '_lan_ip', role='plex') + ':32400,' + lookup('role_var', '_docker_envs_advertise_ip_url', role='plex')
                                                 if (lookup('role_var', '_lan_ip', role='plex') | length > 0) and lookup('role_var', '_open_main_ports', role='plex')
                                                 else lookup('role_var', '_docker_envs_advertise_ip_url', role='plex') }}"
            ```

        ??? variable dict "`plex_role_docker_envs_default`"

            ```yaml
            # Type: dict
            plex_role_docker_envs_default: 
              PLEX_UID: "{{ uid }}"
              PLEX_GID: "{{ gid }}"
              PLEX_CLAIM: "{{ (plex_claim_code) | default(omit) }}"
              CHANGE_CONFIG_DIR_OWNERSHIP: "false"
              TZ: "{{ tz }}"
              ADVERTISE_IP: "{{ lookup('role_var', '_docker_envs_advertise_ip', role='plex') }}"
            ```

        ??? variable dict "`plex_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            plex_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`plex_role_docker_volumes_default`"

            ```yaml
            # Type: list
            plex_role_docker_volumes_default: 
              - "{{ plex_role_paths_location }}:/config"
              - "{{ server_appdata_path }}/scripts:/scripts"
              - "/dev/shm:/dev/shm"
              - "{{ plex_role_paths_transcodes_location }}:/transcode"
            ```

        ??? variable list "`plex_role_docker_volumes_legacy`"

            ```yaml
            # Type: list
            plex_role_docker_volumes_legacy: 
              - "/mnt/unionfs/Media:/data"
            ```

        ??? variable list "`plex_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            plex_role_docker_volumes_custom: []
            ```

        ##### Mounts

        ??? variable list "`plex_role_docker_mounts_default`"

            ```yaml
            # Type: list
            plex_role_docker_mounts_default: 
              - target: /tmp
                type: tmpfs
            ```

        ??? variable list "`plex_role_docker_mounts_custom`"

            ```yaml
            # Type: list
            plex_role_docker_mounts_custom: []
            ```

        ##### Hosts

        ??? variable dict "`plex_role_docker_hosts_default`"

            ```yaml
            # Type: dict
            plex_role_docker_hosts_default: 
              metric.plex.tv: "{{ ip_address_localhost }}"
              metrics.plex.tv: "{{ ip_address_localhost }}"
              analytics.plex.tv: "{{ ip_address_localhost }}"
            ```

        ??? variable dict "`plex_role_docker_hosts_custom`"

            ```yaml
            # Type: dict
            plex_role_docker_hosts_custom: {}
            ```

        ##### Labels

        ??? variable list "`plex_role_docker_labels_default`"

            ```yaml
            # Type: list
            plex_role_docker_labels_default: 
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}-http.entrypoints": "web" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}-http.service": "{{ lookup("role_var", "_webtools_web_subdomain", role="plex") }}" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}-http.rule": "Host(`{{ lookup("role_var", "_webtools_host", role="plex") }}`)" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}-http.middlewares": "{{ traefik_default_middleware_http }}" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}-http.priority": "20" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}.entrypoints": "websecure" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}.service": "{{ lookup("role_var", "_webtools_web_subdomain", role="plex") }}" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}.rule": "Host(`{{ lookup("role_var", "_webtools_host", role="plex") }}`)" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}.tls.options": "securetls@file" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}.tls.certresolver": "{{ plex_role_webtools_traefik_certresolver }}" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}.middlewares": "{{ plex_role_webtools_traefik_middleware }}" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}.priority": "20" }'
              - '{ "traefik.http.services.{{ plex_role_webtools_traefik_router }}.loadbalancer.server.port": "{{ lookup("role_var", "_web_port", role="plex") }}" }'
            ```

        ??? variable dict "`plex_role_docker_labels_custom`"

            ```yaml
            # Type: dict
            plex_role_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`plex_role_docker_hostname`"

            ```yaml
            # Type: string
            plex_role_docker_hostname: "{{ plex_name }}"
            ```

        ##### Networks

        ??? variable string "`plex_role_docker_networks_alias`"

            ```yaml
            # Type: string
            plex_role_docker_networks_alias: "{{ plex_name }}"
            ```

        ??? variable list "`plex_role_docker_networks_default`"

            ```yaml
            # Type: list
            plex_role_docker_networks_default: []
            ```

        ??? variable list "`plex_role_docker_networks_custom`"

            ```yaml
            # Type: list
            plex_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`plex_role_docker_restart_policy`"

            ```yaml
            # Type: string
            plex_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`plex_role_docker_state`"

            ```yaml
            # Type: string
            plex_role_docker_state: started
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`plex2_docker_container`"

            ```yaml
            # Type: string
            plex2_docker_container: "{{ plex_name }}"
            ```

        ##### Image

        ??? variable bool "`plex2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            plex2_docker_image_pull: true
            ```

        ??? variable string "`plex2_docker_image_repo`"

            ```yaml
            # Type: string
            plex2_docker_image_repo: "plexinc/pms-docker"
            ```

        ??? variable string "`plex2_docker_image_tag`"

            ```yaml
            # Type: string
            plex2_docker_image_tag: "latest"
            ```

        ??? variable string "`plex2_docker_image`"

            ```yaml
            # Type: string
            plex2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='plex') }}:{{ lookup('role_var', '_docker_image_tag', role='plex') }}"
            ```

        ##### Ports

        ??? variable string "`plex2_docker_ports_32400`"

            ```yaml
            # Type: string
            plex2_docker_ports_32400: "{{ port_lookup_32400.meta.port
                                       if (port_lookup_32400.meta.port is defined) and (port_lookup_32400.meta.port | trim | length > 0)
                                       else '32400' }}"
            ```

        ??? variable list "`plex2_docker_ports_defaults`"

            ```yaml
            # Type: list
            plex2_docker_ports_defaults: []
            ```

        ??? variable list "`plex2_docker_ports_custom`"

            ```yaml
            # Type: list
            plex2_docker_ports_custom: []
            ```

        ##### Envs

        ??? variable string "`plex2_docker_envs_advertise_ip_url`"

            ```yaml
            # Type: string
            plex2_docker_envs_advertise_ip_url: "{{ lookup('role_var', '_web_url', role='plex') + ':443,' + lookup('role_var', '_web_insecure_url', role='plex') + ':80'
                                                 if lookup('role_var', '_insecure', role='plex')
                                                 else lookup('role_var', '_web_url', role='plex') + ':443' }}"
            ```

        ??? variable string "`plex2_docker_envs_advertise_ip`"

            ```yaml
            # Type: string
            plex2_docker_envs_advertise_ip: "{{ 'http://' + lookup('role_var', '_lan_ip', role='plex') + ':32400,' + lookup('role_var', '_docker_envs_advertise_ip_url', role='plex')
                                             if (lookup('role_var', '_lan_ip', role='plex') | length > 0) and lookup('role_var', '_open_main_ports', role='plex')
                                             else lookup('role_var', '_docker_envs_advertise_ip_url', role='plex') }}"
            ```

        ??? variable dict "`plex2_docker_envs_default`"

            ```yaml
            # Type: dict
            plex2_docker_envs_default: 
              PLEX_UID: "{{ uid }}"
              PLEX_GID: "{{ gid }}"
              PLEX_CLAIM: "{{ (plex_claim_code) | default(omit) }}"
              CHANGE_CONFIG_DIR_OWNERSHIP: "false"
              TZ: "{{ tz }}"
              ADVERTISE_IP: "{{ lookup('role_var', '_docker_envs_advertise_ip', role='plex') }}"
            ```

        ??? variable dict "`plex2_docker_envs_custom`"

            ```yaml
            # Type: dict
            plex2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`plex2_docker_volumes_default`"

            ```yaml
            # Type: list
            plex2_docker_volumes_default: 
              - "{{ plex_role_paths_location }}:/config"
              - "{{ server_appdata_path }}/scripts:/scripts"
              - "/dev/shm:/dev/shm"
              - "{{ plex_role_paths_transcodes_location }}:/transcode"
            ```

        ??? variable list "`plex2_docker_volumes_legacy`"

            ```yaml
            # Type: list
            plex2_docker_volumes_legacy: 
              - "/mnt/unionfs/Media:/data"
            ```

        ??? variable list "`plex2_docker_volumes_custom`"

            ```yaml
            # Type: list
            plex2_docker_volumes_custom: []
            ```

        ##### Mounts

        ??? variable list "`plex2_docker_mounts_default`"

            ```yaml
            # Type: list
            plex2_docker_mounts_default: 
              - target: /tmp
                type: tmpfs
            ```

        ??? variable list "`plex2_docker_mounts_custom`"

            ```yaml
            # Type: list
            plex2_docker_mounts_custom: []
            ```

        ##### Hosts

        ??? variable dict "`plex2_docker_hosts_default`"

            ```yaml
            # Type: dict
            plex2_docker_hosts_default: 
              metric.plex.tv: "{{ ip_address_localhost }}"
              metrics.plex.tv: "{{ ip_address_localhost }}"
              analytics.plex.tv: "{{ ip_address_localhost }}"
            ```

        ??? variable dict "`plex2_docker_hosts_custom`"

            ```yaml
            # Type: dict
            plex2_docker_hosts_custom: {}
            ```

        ##### Labels

        ??? variable list "`plex2_docker_labels_default`"

            ```yaml
            # Type: list
            plex2_docker_labels_default: 
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}-http.entrypoints": "web" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}-http.service": "{{ lookup("role_var", "_webtools_web_subdomain", role="plex") }}" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}-http.rule": "Host(`{{ lookup("role_var", "_webtools_host", role="plex") }}`)" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}-http.middlewares": "{{ traefik_default_middleware_http }}" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}-http.priority": "20" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}.entrypoints": "websecure" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}.service": "{{ lookup("role_var", "_webtools_web_subdomain", role="plex") }}" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}.rule": "Host(`{{ lookup("role_var", "_webtools_host", role="plex") }}`)" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}.tls.options": "securetls@file" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}.tls.certresolver": "{{ plex_role_webtools_traefik_certresolver }}" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}.middlewares": "{{ plex_role_webtools_traefik_middleware }}" }'
              - '{ "traefik.http.routers.{{ plex_role_webtools_traefik_router }}.priority": "20" }'
              - '{ "traefik.http.services.{{ plex_role_webtools_traefik_router }}.loadbalancer.server.port": "{{ lookup("role_var", "_web_port", role="plex") }}" }'
            ```

        ??? variable dict "`plex2_docker_labels_custom`"

            ```yaml
            # Type: dict
            plex2_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`plex2_docker_hostname`"

            ```yaml
            # Type: string
            plex2_docker_hostname: "{{ plex_name }}"
            ```

        ##### Networks

        ??? variable string "`plex2_docker_networks_alias`"

            ```yaml
            # Type: string
            plex2_docker_networks_alias: "{{ plex_name }}"
            ```

        ??? variable list "`plex2_docker_networks_default`"

            ```yaml
            # Type: list
            plex2_docker_networks_default: []
            ```

        ??? variable list "`plex2_docker_networks_custom`"

            ```yaml
            # Type: list
            plex2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`plex2_docker_restart_policy`"

            ```yaml
            # Type: string
            plex2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`plex2_docker_state`"

            ```yaml
            # Type: string
            plex2_docker_state: started
            ```

=== "Docker+"

    #### Additional Docker Options

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    === "Role-level"

        ##### Resource Limits

        ??? variable int "`plex_role_docker_blkio_weight`"

            ```yaml
            # Type: int
            plex_role_docker_blkio_weight:
            ```

        ??? variable int "`plex_role_docker_cpu_period`"

            ```yaml
            # Type: int
            plex_role_docker_cpu_period:
            ```

        ??? variable int "`plex_role_docker_cpu_quota`"

            ```yaml
            # Type: int
            plex_role_docker_cpu_quota:
            ```

        ??? variable int "`plex_role_docker_cpu_shares`"

            ```yaml
            # Type: int
            plex_role_docker_cpu_shares:
            ```

        ??? variable string "`plex_role_docker_cpus`"

            ```yaml
            # Type: string
            plex_role_docker_cpus:
            ```

        ??? variable string "`plex_role_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            plex_role_docker_cpuset_cpus:
            ```

        ??? variable string "`plex_role_docker_cpuset_mems`"

            ```yaml
            # Type: string
            plex_role_docker_cpuset_mems:
            ```

        ??? variable string "`plex_role_docker_kernel_memory`"

            ```yaml
            # Type: string
            plex_role_docker_kernel_memory:
            ```

        ??? variable string "`plex_role_docker_memory`"

            ```yaml
            # Type: string
            plex_role_docker_memory:
            ```

        ??? variable string "`plex_role_docker_memory_reservation`"

            ```yaml
            # Type: string
            plex_role_docker_memory_reservation:
            ```

        ??? variable string "`plex_role_docker_memory_swap`"

            ```yaml
            # Type: string
            plex_role_docker_memory_swap:
            ```

        ??? variable int "`plex_role_docker_memory_swappiness`"

            ```yaml
            # Type: int
            plex_role_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`plex_role_docker_cap_drop`"

            ```yaml
            # Type: list
            plex_role_docker_cap_drop:
            ```

        ??? variable list "`plex_role_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            plex_role_docker_device_cgroup_rules:
            ```

        ??? variable list "`plex_role_docker_device_read_bps`"

            ```yaml
            # Type: list
            plex_role_docker_device_read_bps:
            ```

        ??? variable list "`plex_role_docker_device_read_iops`"

            ```yaml
            # Type: list
            plex_role_docker_device_read_iops:
            ```

        ??? variable list "`plex_role_docker_device_requests`"

            ```yaml
            # Type: list
            plex_role_docker_device_requests:
            ```

        ??? variable list "`plex_role_docker_device_write_bps`"

            ```yaml
            # Type: list
            plex_role_docker_device_write_bps:
            ```

        ??? variable list "`plex_role_docker_device_write_iops`"

            ```yaml
            # Type: list
            plex_role_docker_device_write_iops:
            ```

        ??? variable list "`plex_role_docker_devices`"

            ```yaml
            # Type: list
            plex_role_docker_devices:
            ```

        ??? variable string "`plex_role_docker_devices_default`"

            ```yaml
            # Type: string
            plex_role_docker_devices_default:
            ```

        ??? variable bool "`plex_role_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            plex_role_docker_privileged:
            ```

        ??? variable list "`plex_role_docker_security_opts`"

            ```yaml
            # Type: list
            plex_role_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`plex_role_docker_dns_opts`"

            ```yaml
            # Type: list
            plex_role_docker_dns_opts:
            ```

        ??? variable list "`plex_role_docker_dns_search_domains`"

            ```yaml
            # Type: list
            plex_role_docker_dns_search_domains:
            ```

        ??? variable list "`plex_role_docker_dns_servers`"

            ```yaml
            # Type: list
            plex_role_docker_dns_servers:
            ```

        ??? variable string "`plex_role_docker_hosts_use_common`"

            ```yaml
            # Type: string
            plex_role_docker_hosts_use_common:
            ```

        ??? variable string "`plex_role_docker_network_mode`"

            ```yaml
            # Type: string
            plex_role_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`plex_role_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            plex_role_docker_keep_volumes:
            ```

        ??? variable string "`plex_role_docker_volume_driver`"

            ```yaml
            # Type: string
            plex_role_docker_volume_driver:
            ```

        ??? variable list "`plex_role_docker_volumes_from`"

            ```yaml
            # Type: list
            plex_role_docker_volumes_from:
            ```

        ??? variable string "`plex_role_docker_volumes_global`"

            ```yaml
            # Type: string
            plex_role_docker_volumes_global:
            ```

        ??? variable string "`plex_role_docker_working_dir`"

            ```yaml
            # Type: string
            plex_role_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`plex_role_docker_healthcheck`"

            ```yaml
            # Type: dict
            plex_role_docker_healthcheck:
            ```

        ??? variable bool "`plex_role_docker_init`"

            ```yaml
            # Type: bool (true/false)
            plex_role_docker_init:
            ```

        ??? variable string "`plex_role_docker_log_driver`"

            ```yaml
            # Type: string
            plex_role_docker_log_driver:
            ```

        ??? variable dict "`plex_role_docker_log_options`"

            ```yaml
            # Type: dict
            plex_role_docker_log_options:
            ```

        ??? variable bool "`plex_role_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            plex_role_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`plex_role_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            plex_role_docker_auto_remove:
            ```

        ??? variable list "`plex_role_docker_capabilities`"

            ```yaml
            # Type: list
            plex_role_docker_capabilities:
            ```

        ??? variable string "`plex_role_docker_cgroup_parent`"

            ```yaml
            # Type: string
            plex_role_docker_cgroup_parent:
            ```

        ??? variable string "`plex_role_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            plex_role_docker_cgroupns_mode:
            ```

        ??? variable bool "`plex_role_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            plex_role_docker_cleanup:
            ```

        ??? variable list "`plex_role_docker_commands`"

            ```yaml
            # Type: list
            plex_role_docker_commands:
            ```

        ??? variable string "`plex_role_docker_create_timeout`"

            ```yaml
            # Type: string
            plex_role_docker_create_timeout:
            ```

        ??? variable string "`plex_role_docker_domainname`"

            ```yaml
            # Type: string
            plex_role_docker_domainname:
            ```

        ??? variable string "`plex_role_docker_entrypoint`"

            ```yaml
            # Type: string
            plex_role_docker_entrypoint:
            ```

        ??? variable string "`plex_role_docker_env_file`"

            ```yaml
            # Type: string
            plex_role_docker_env_file:
            ```

        ??? variable list "`plex_role_docker_exposed_ports`"

            ```yaml
            # Type: list
            plex_role_docker_exposed_ports:
            ```

        ??? variable string "`plex_role_docker_force_kill`"

            ```yaml
            # Type: string
            plex_role_docker_force_kill:
            ```

        ??? variable list "`plex_role_docker_groups`"

            ```yaml
            # Type: list
            plex_role_docker_groups:
            ```

        ??? variable int "`plex_role_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            plex_role_docker_healthy_wait_timeout:
            ```

        ??? variable string "`plex_role_docker_ipc_mode`"

            ```yaml
            # Type: string
            plex_role_docker_ipc_mode:
            ```

        ??? variable string "`plex_role_docker_kill_signal`"

            ```yaml
            # Type: string
            plex_role_docker_kill_signal:
            ```

        ??? variable string "`plex_role_docker_labels_use_common`"

            ```yaml
            # Type: string
            plex_role_docker_labels_use_common:
            ```

        ??? variable list "`plex_role_docker_links`"

            ```yaml
            # Type: list
            plex_role_docker_links:
            ```

        ??? variable bool "`plex_role_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            plex_role_docker_oom_killer:
            ```

        ??? variable int "`plex_role_docker_oom_score_adj`"

            ```yaml
            # Type: int
            plex_role_docker_oom_score_adj:
            ```

        ??? variable bool "`plex_role_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            plex_role_docker_paused:
            ```

        ??? variable string "`plex_role_docker_pid_mode`"

            ```yaml
            # Type: string
            plex_role_docker_pid_mode:
            ```

        ??? variable bool "`plex_role_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            plex_role_docker_read_only:
            ```

        ??? variable bool "`plex_role_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            plex_role_docker_recreate:
            ```

        ??? variable int "`plex_role_docker_restart_retries`"

            ```yaml
            # Type: int
            plex_role_docker_restart_retries:
            ```

        ??? variable string "`plex_role_docker_runtime`"

            ```yaml
            # Type: string
            plex_role_docker_runtime:
            ```

        ??? variable string "`plex_role_docker_shm_size`"

            ```yaml
            # Type: string
            plex_role_docker_shm_size:
            ```

        ??? variable int "`plex_role_docker_stop_timeout`"

            ```yaml
            # Type: int
            plex_role_docker_stop_timeout:
            ```

        ??? variable dict "`plex_role_docker_storage_opts`"

            ```yaml
            # Type: dict
            plex_role_docker_storage_opts:
            ```

        ??? variable list "`plex_role_docker_sysctls`"

            ```yaml
            # Type: list
            plex_role_docker_sysctls:
            ```

        ??? variable list "`plex_role_docker_tmpfs`"

            ```yaml
            # Type: list
            plex_role_docker_tmpfs:
            ```

        ??? variable list "`plex_role_docker_ulimits`"

            ```yaml
            # Type: list
            plex_role_docker_ulimits:
            ```

        ??? variable string "`plex_role_docker_user`"

            ```yaml
            # Type: string
            plex_role_docker_user:
            ```

        ??? variable string "`plex_role_docker_userns_mode`"

            ```yaml
            # Type: string
            plex_role_docker_userns_mode:
            ```

        ??? variable string "`plex_role_docker_uts`"

            ```yaml
            # Type: string
            plex_role_docker_uts:
            ```

    === "Instance-level"

        ##### Resource Limits

        ??? variable int "`plex2_docker_blkio_weight`"

            ```yaml
            # Type: int
            plex2_docker_blkio_weight:
            ```

        ??? variable int "`plex2_docker_cpu_period`"

            ```yaml
            # Type: int
            plex2_docker_cpu_period:
            ```

        ??? variable int "`plex2_docker_cpu_quota`"

            ```yaml
            # Type: int
            plex2_docker_cpu_quota:
            ```

        ??? variable int "`plex2_docker_cpu_shares`"

            ```yaml
            # Type: int
            plex2_docker_cpu_shares:
            ```

        ??? variable string "`plex2_docker_cpus`"

            ```yaml
            # Type: string
            plex2_docker_cpus:
            ```

        ??? variable string "`plex2_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            plex2_docker_cpuset_cpus:
            ```

        ??? variable string "`plex2_docker_cpuset_mems`"

            ```yaml
            # Type: string
            plex2_docker_cpuset_mems:
            ```

        ??? variable string "`plex2_docker_kernel_memory`"

            ```yaml
            # Type: string
            plex2_docker_kernel_memory:
            ```

        ??? variable string "`plex2_docker_memory`"

            ```yaml
            # Type: string
            plex2_docker_memory:
            ```

        ??? variable string "`plex2_docker_memory_reservation`"

            ```yaml
            # Type: string
            plex2_docker_memory_reservation:
            ```

        ??? variable string "`plex2_docker_memory_swap`"

            ```yaml
            # Type: string
            plex2_docker_memory_swap:
            ```

        ??? variable int "`plex2_docker_memory_swappiness`"

            ```yaml
            # Type: int
            plex2_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`plex2_docker_cap_drop`"

            ```yaml
            # Type: list
            plex2_docker_cap_drop:
            ```

        ??? variable list "`plex2_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            plex2_docker_device_cgroup_rules:
            ```

        ??? variable list "`plex2_docker_device_read_bps`"

            ```yaml
            # Type: list
            plex2_docker_device_read_bps:
            ```

        ??? variable list "`plex2_docker_device_read_iops`"

            ```yaml
            # Type: list
            plex2_docker_device_read_iops:
            ```

        ??? variable list "`plex2_docker_device_requests`"

            ```yaml
            # Type: list
            plex2_docker_device_requests:
            ```

        ??? variable list "`plex2_docker_device_write_bps`"

            ```yaml
            # Type: list
            plex2_docker_device_write_bps:
            ```

        ??? variable list "`plex2_docker_device_write_iops`"

            ```yaml
            # Type: list
            plex2_docker_device_write_iops:
            ```

        ??? variable list "`plex2_docker_devices`"

            ```yaml
            # Type: list
            plex2_docker_devices:
            ```

        ??? variable string "`plex2_docker_devices_default`"

            ```yaml
            # Type: string
            plex2_docker_devices_default:
            ```

        ??? variable bool "`plex2_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            plex2_docker_privileged:
            ```

        ??? variable list "`plex2_docker_security_opts`"

            ```yaml
            # Type: list
            plex2_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`plex2_docker_dns_opts`"

            ```yaml
            # Type: list
            plex2_docker_dns_opts:
            ```

        ??? variable list "`plex2_docker_dns_search_domains`"

            ```yaml
            # Type: list
            plex2_docker_dns_search_domains:
            ```

        ??? variable list "`plex2_docker_dns_servers`"

            ```yaml
            # Type: list
            plex2_docker_dns_servers:
            ```

        ??? variable string "`plex2_docker_hosts_use_common`"

            ```yaml
            # Type: string
            plex2_docker_hosts_use_common:
            ```

        ??? variable string "`plex2_docker_network_mode`"

            ```yaml
            # Type: string
            plex2_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`plex2_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            plex2_docker_keep_volumes:
            ```

        ??? variable string "`plex2_docker_volume_driver`"

            ```yaml
            # Type: string
            plex2_docker_volume_driver:
            ```

        ??? variable list "`plex2_docker_volumes_from`"

            ```yaml
            # Type: list
            plex2_docker_volumes_from:
            ```

        ??? variable string "`plex2_docker_volumes_global`"

            ```yaml
            # Type: string
            plex2_docker_volumes_global:
            ```

        ??? variable string "`plex2_docker_working_dir`"

            ```yaml
            # Type: string
            plex2_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`plex2_docker_healthcheck`"

            ```yaml
            # Type: dict
            plex2_docker_healthcheck:
            ```

        ??? variable bool "`plex2_docker_init`"

            ```yaml
            # Type: bool (true/false)
            plex2_docker_init:
            ```

        ??? variable string "`plex2_docker_log_driver`"

            ```yaml
            # Type: string
            plex2_docker_log_driver:
            ```

        ??? variable dict "`plex2_docker_log_options`"

            ```yaml
            # Type: dict
            plex2_docker_log_options:
            ```

        ??? variable bool "`plex2_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            plex2_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`plex2_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            plex2_docker_auto_remove:
            ```

        ??? variable list "`plex2_docker_capabilities`"

            ```yaml
            # Type: list
            plex2_docker_capabilities:
            ```

        ??? variable string "`plex2_docker_cgroup_parent`"

            ```yaml
            # Type: string
            plex2_docker_cgroup_parent:
            ```

        ??? variable string "`plex2_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            plex2_docker_cgroupns_mode:
            ```

        ??? variable bool "`plex2_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            plex2_docker_cleanup:
            ```

        ??? variable list "`plex2_docker_commands`"

            ```yaml
            # Type: list
            plex2_docker_commands:
            ```

        ??? variable string "`plex2_docker_create_timeout`"

            ```yaml
            # Type: string
            plex2_docker_create_timeout:
            ```

        ??? variable string "`plex2_docker_domainname`"

            ```yaml
            # Type: string
            plex2_docker_domainname:
            ```

        ??? variable string "`plex2_docker_entrypoint`"

            ```yaml
            # Type: string
            plex2_docker_entrypoint:
            ```

        ??? variable string "`plex2_docker_env_file`"

            ```yaml
            # Type: string
            plex2_docker_env_file:
            ```

        ??? variable list "`plex2_docker_exposed_ports`"

            ```yaml
            # Type: list
            plex2_docker_exposed_ports:
            ```

        ??? variable string "`plex2_docker_force_kill`"

            ```yaml
            # Type: string
            plex2_docker_force_kill:
            ```

        ??? variable list "`plex2_docker_groups`"

            ```yaml
            # Type: list
            plex2_docker_groups:
            ```

        ??? variable int "`plex2_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            plex2_docker_healthy_wait_timeout:
            ```

        ??? variable string "`plex2_docker_ipc_mode`"

            ```yaml
            # Type: string
            plex2_docker_ipc_mode:
            ```

        ??? variable string "`plex2_docker_kill_signal`"

            ```yaml
            # Type: string
            plex2_docker_kill_signal:
            ```

        ??? variable string "`plex2_docker_labels_use_common`"

            ```yaml
            # Type: string
            plex2_docker_labels_use_common:
            ```

        ??? variable list "`plex2_docker_links`"

            ```yaml
            # Type: list
            plex2_docker_links:
            ```

        ??? variable bool "`plex2_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            plex2_docker_oom_killer:
            ```

        ??? variable int "`plex2_docker_oom_score_adj`"

            ```yaml
            # Type: int
            plex2_docker_oom_score_adj:
            ```

        ??? variable bool "`plex2_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            plex2_docker_paused:
            ```

        ??? variable string "`plex2_docker_pid_mode`"

            ```yaml
            # Type: string
            plex2_docker_pid_mode:
            ```

        ??? variable bool "`plex2_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            plex2_docker_read_only:
            ```

        ??? variable bool "`plex2_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            plex2_docker_recreate:
            ```

        ??? variable int "`plex2_docker_restart_retries`"

            ```yaml
            # Type: int
            plex2_docker_restart_retries:
            ```

        ??? variable string "`plex2_docker_runtime`"

            ```yaml
            # Type: string
            plex2_docker_runtime:
            ```

        ??? variable string "`plex2_docker_shm_size`"

            ```yaml
            # Type: string
            plex2_docker_shm_size:
            ```

        ??? variable int "`plex2_docker_stop_timeout`"

            ```yaml
            # Type: int
            plex2_docker_stop_timeout:
            ```

        ??? variable dict "`plex2_docker_storage_opts`"

            ```yaml
            # Type: dict
            plex2_docker_storage_opts:
            ```

        ??? variable list "`plex2_docker_sysctls`"

            ```yaml
            # Type: list
            plex2_docker_sysctls:
            ```

        ??? variable list "`plex2_docker_tmpfs`"

            ```yaml
            # Type: list
            plex2_docker_tmpfs:
            ```

        ??? variable list "`plex2_docker_ulimits`"

            ```yaml
            # Type: list
            plex2_docker_ulimits:
            ```

        ??? variable string "`plex2_docker_user`"

            ```yaml
            # Type: string
            plex2_docker_user:
            ```

        ??? variable string "`plex2_docker_userns_mode`"

            ```yaml
            # Type: string
            plex2_docker_userns_mode:
            ```

        ??? variable string "`plex2_docker_uts`"

            ```yaml
            # Type: string
            plex2_docker_uts:
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`plex_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            plex_role_autoheal_enabled: true
            ```

        ??? variable string "`plex_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            plex_role_depends_on: ""
            ```

        ??? variable string "`plex_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            plex_role_depends_on_delay: "0"
            ```

        ??? variable string "`plex_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            plex_role_depends_on_healthchecks:
            ```

        ??? variable bool "`plex_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            plex_role_diun_enabled: true
            ```

        ??? variable bool "`plex_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            plex_role_dns_enabled: true
            ```

        ??? variable bool "`plex_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            plex_role_docker_controller: true
            ```

        ??? variable bool "`plex_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            plex_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`plex_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            plex_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`plex_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            plex_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`plex_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            plex_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`plex_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            plex_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`plex_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            plex_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`plex_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            plex_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`plex_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            plex_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                plex_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "plex2.{{ user.domain }}"
                  - "plex.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`plex_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            plex_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                plex_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'plex2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`plex_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            plex_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `plex2`):

        ??? variable bool "`plex2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            plex2_autoheal_enabled: true
            ```

        ??? variable string "`plex2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            plex2_depends_on: ""
            ```

        ??? variable string "`plex2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            plex2_depends_on_delay: "0"
            ```

        ??? variable string "`plex2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            plex2_depends_on_healthchecks:
            ```

        ??? variable bool "`plex2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            plex2_diun_enabled: true
            ```

        ??? variable bool "`plex2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            plex2_dns_enabled: true
            ```

        ??? variable bool "`plex2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            plex2_docker_controller: true
            ```

        ??? variable bool "`plex2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            plex2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`plex2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            plex2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`plex2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            plex2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`plex2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            plex2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`plex2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            plex2_traefik_robot_enabled: true
            ```

        ??? variable bool "`plex2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            plex2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`plex2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            plex2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`plex2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            plex2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                plex2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "plex2.{{ user.domain }}"
                  - "plex.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`plex2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            plex2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                plex2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'plex2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`plex2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            plex2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
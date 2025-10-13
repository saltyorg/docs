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

## Inventory Variables

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
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

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        plex_instances: ["plex"]

        ```

    === "Example"

        ```yaml
        # Type: list
        plex_instances: ["plex", "plex2"]

        ```

??? example "Settings"

    === "Role-level"

        ```yaml
        # Do not enable globally if deploying multiple instances
        # Type: bool (true/false)
        plex_role_open_main_ports: false

        # Do not enable globally if deploying multiple instances
        # Type: bool (true/false)
        plex_role_open_local_ports: false

        # Type: bool (true/false)
        plex_role_plugin_webtools: false

        # Type: bool (true/false)
        plex_role_plugin_sub_zero: false

        # Disables Traefik's HTTP to HTTPS redirect for Plex
        # Allows older clients with certificate issues to connect insecurely
        # Type: bool (true/false)
        plex_role_insecure: false

        # Adds the IP specified here to the advertised urls Plex broadcasts to clients
        # Useful to avoid traffic going through your WAN when hairpin NAT is not available
        # Type: string
        plex_role_lan_ip: ""

        # For instances this works the same as usual plex2_auth_token_proxy for an instance named plex2.
        # Type: string
        plex_role_auth_token_proxy: ""

        ```

    === "Instance-level"

        ```yaml
        # Do not enable globally if deploying multiple instances
        # Type: bool (true/false)
        plex2_open_main_ports: false

        # Do not enable globally if deploying multiple instances
        # Type: bool (true/false)
        plex2_open_local_ports: false

        # Type: bool (true/false)
        plex2_plugin_webtools: false

        # Type: bool (true/false)
        plex2_plugin_sub_zero: false

        # Disables Traefik's HTTP to HTTPS redirect for Plex
        # Allows older clients with certificate issues to connect insecurely
        # Type: bool (true/false)
        plex2_insecure: false

        # Adds the IP specified here to the advertised urls Plex broadcasts to clients
        # Useful to avoid traffic going through your WAN when hairpin NAT is not available
        # Type: string
        plex2_lan_ip: ""

        # For instances this works the same as usual plex2_auth_token_proxy for an instance named plex2.
        # Type: string
        plex2_auth_token_proxy: ""

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        plex_role_paths_folder: "{{ plex_name }}"

        # Type: string
        plex_role_paths_location: "{{ server_appdata_path }}/{{ plex_role_paths_folder }}"

        # Type: string
        plex_role_paths_transcodes_location: "{{ transcodes_path }}/{{ plex_role_paths_folder }}"

        # Type: string
        plex_role_paths_application_support_location: "{{ plex_role_paths_location }}/Library/Application Support/Plex Media Server"

        # Type: string
        plex_role_paths_config_location: "{{ plex_role_paths_application_support_location }}/Preferences.xml"

        # Type: string
        plex_role_paths_log_location: "{{ plex_role_paths_application_support_location }}/Logs"

        # Type: string
        plex_role_paths_plugins_location: "{{ plex_role_paths_application_support_location }}/Plug-ins"

        # Type: string
        plex_role_paths_plugin_support_location: "{{ plex_role_paths_application_support_location }}/Plug-in Support"

        # Type: string
        plex_role_paths_db_location: "{{ plex_role_paths_plugin_support_location }}/Databases/com.plexapp.plugins.library.db"

        # Type: string
        plex_role_paths_db_blobs_location: "{{ plex_role_paths_plugin_support_location }}/Databases/com.plexapp.plugins.library.blobs.db"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        plex2_paths_folder: "{{ plex_name }}"

        # Type: string
        plex2_paths_location: "{{ server_appdata_path }}/{{ plex_role_paths_folder }}"

        # Type: string
        plex2_paths_transcodes_location: "{{ transcodes_path }}/{{ plex_role_paths_folder }}"

        # Type: string
        plex2_paths_application_support_location: "{{ plex_role_paths_location }}/Library/Application Support/Plex Media Server"

        # Type: string
        plex2_paths_config_location: "{{ plex_role_paths_application_support_location }}/Preferences.xml"

        # Type: string
        plex2_paths_log_location: "{{ plex_role_paths_application_support_location }}/Logs"

        # Type: string
        plex2_paths_plugins_location: "{{ plex_role_paths_application_support_location }}/Plug-ins"

        # Type: string
        plex2_paths_plugin_support_location: "{{ plex_role_paths_application_support_location }}/Plug-in Support"

        # Type: string
        plex2_paths_db_location: "{{ plex_role_paths_plugin_support_location }}/Databases/com.plexapp.plugins.library.db"

        # Type: string
        plex2_paths_db_blobs_location: "{{ plex_role_paths_plugin_support_location }}/Databases/com.plexapp.plugins.library.blobs.db"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        plex_role_web_subdomain: "{{ plex_name }}"

        # Type: string
        plex_role_web_domain: "{{ user.domain }}"

        # Type: string
        plex_role_web_port: "32400"

        # Type: string
        plex_role_web_http_port: "32400"

        # Type: string
        plex_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='plex') + '.' + lookup('role_var', '_web_domain', role='plex')
                            if (lookup('role_var', '_web_subdomain', role='plex') | length > 0)
                            else lookup('role_var', '_web_domain', role='plex')) }}"

        # Type: string
        plex_role_webtools_web_subdomain: "{{ plex_name }}-webtools"

        # Type: string
        plex_role_webtools_web_domain: "{{ lookup('role_var', '_web_domain', role='plex') }}"

        # Type: string
        plex_role_webtools_web_port: "33400"

        # Type: string
        plex_role_webtools_host: "{{ lookup('role_var', '_webtools_web_subdomain', role='plex') + '.' + lookup('role_var', '_webtools_web_domain', role='plex') }}"

        # Type: string
        plex_role_web_insecure_url: "{{ 'http://' + (lookup('role_var', '_web_subdomain', role='plex') + '.' + lookup('role_var', '_web_domain', role='plex')
                                     if (lookup('role_var', '_web_subdomain', role='plex') | length > 0)
                                     else lookup('role_var', '_web_domain', role='plex')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        plex2_web_subdomain: "{{ plex_name }}"

        # Type: string
        plex2_web_domain: "{{ user.domain }}"

        # Type: string
        plex2_web_port: "32400"

        # Type: string
        plex2_web_http_port: "32400"

        # Type: string
        plex2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='plex') + '.' + lookup('role_var', '_web_domain', role='plex')
                        if (lookup('role_var', '_web_subdomain', role='plex') | length > 0)
                        else lookup('role_var', '_web_domain', role='plex')) }}"

        # Type: string
        plex2_webtools_web_subdomain: "{{ plex_name }}-webtools"

        # Type: string
        plex2_webtools_web_domain: "{{ lookup('role_var', '_web_domain', role='plex') }}"

        # Type: string
        plex2_webtools_web_port: "33400"

        # Type: string
        plex2_webtools_host: "{{ lookup('role_var', '_webtools_web_subdomain', role='plex') + '.' + lookup('role_var', '_webtools_web_domain', role='plex') }}"

        # Type: string
        plex2_web_insecure_url: "{{ 'http://' + (lookup('role_var', '_web_subdomain', role='plex') + '.' + lookup('role_var', '_web_domain', role='plex')
                                 if (lookup('role_var', '_web_subdomain', role='plex') | length > 0)
                                 else lookup('role_var', '_web_domain', role='plex')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        plex_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='plex') }}"

        # Type: string
        plex_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='plex') }}"

        # Type: bool (true/false)
        plex_role_dns_proxy: "{{ dns_proxied }}"

        # Type: string
        plex_role_webtools_dns_record: "{{ lookup('role_var', '_webtools_web_subdomain', role='plex') }}"

        # Type: string
        plex_role_webtools_dns_zone: "{{ lookup('role_var', '_webtools_web_domain', role='plex') }}"

        # Type: bool (true/false)
        plex_role_webtools_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        plex2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='plex') }}"

        # Type: string
        plex2_dns_zone: "{{ lookup('role_var', '_web_domain', role='plex') }}"

        # Type: bool (true/false)
        plex2_dns_proxy: "{{ dns_proxied }}"

        # Type: string
        plex2_webtools_dns_record: "{{ lookup('role_var', '_webtools_web_subdomain', role='plex') }}"

        # Type: string
        plex2_webtools_dns_zone: "{{ lookup('role_var', '_webtools_web_domain', role='plex') }}"

        # Type: bool (true/false)
        plex2_webtools_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        plex_role_traefik_sso_middleware: ""

        # Type: string
        plex_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                  + (',themepark-' + plex_name
                                                    if (lookup('role_var', '_themepark_enabled', role='plex') and global_themepark_plugin_enabled)
                                                    else '') }}"

        # Type: string
        plex_role_traefik_middleware_custom: ""

        # Type: string
        plex_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        plex_role_traefik_enabled: true

        # Type: bool (true/false)
        plex_role_traefik_api_enabled: false

        # Type: string
        plex_role_traefik_api_endpoint: ""

        # Type: bool (true/false)
        plex_role_traefik_error_pages_enabled: false

        # Type: bool (true/false)
        plex_role_traefik_gzip_enabled: false

        # Type: string
        plex_role_traefik_middleware_http: "{{ 'globalHeaders@file'
                                            if lookup('role_var', '_insecure', role='plex')
                                            else traefik_default_middleware_default_http }}"

        # Type: string
        plex_role_web_serverstransport: "skipverify@file"

        # Type: string
        plex_role_webtools_traefik_sso_middleware: ""

        # Type: string
        plex_role_webtools_traefik_middleware_default: "{{ traefik_default_middleware
                                                           + (',' + lookup('role_var', '_webtools_traefik_sso_middleware', role='plex')
                                                             if (lookup('role_var', '_webtools_traefik_sso_middleware', role='plex') | length > 0)
                                                             else '') }}"

        # Type: string
        plex_role_webtools_traefik_middleware_custom: ""

        # Type: string
        plex_role_webtools_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: string
        plex_role_webtools_traefik_router: "{{ lookup('role_var', '_webtools_web_subdomain', role='plex') }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        plex2_traefik_sso_middleware: ""

        # Type: string
        plex2_traefik_middleware_default: "{{ traefik_default_middleware
                                              + (',themepark-' + plex_name
                                                if (lookup('role_var', '_themepark_enabled', role='plex') and global_themepark_plugin_enabled)
                                                else '') }}"

        # Type: string
        plex2_traefik_middleware_custom: ""

        # Type: string
        plex2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        plex2_traefik_enabled: true

        # Type: bool (true/false)
        plex2_traefik_api_enabled: false

        # Type: string
        plex2_traefik_api_endpoint: ""

        # Type: bool (true/false)
        plex2_traefik_error_pages_enabled: false

        # Type: bool (true/false)
        plex2_traefik_gzip_enabled: false

        # Type: string
        plex2_traefik_middleware_http: "{{ 'globalHeaders@file'
                                        if lookup('role_var', '_insecure', role='plex')
                                        else traefik_default_middleware_default_http }}"

        # Type: string
        plex2_web_serverstransport: "skipverify@file"

        # Type: string
        plex2_webtools_traefik_sso_middleware: ""

        # Type: string
        plex2_webtools_traefik_middleware_default: "{{ traefik_default_middleware
                                                       + (',' + lookup('role_var', '_webtools_traefik_sso_middleware', role='plex')
                                                         if (lookup('role_var', '_webtools_traefik_sso_middleware', role='plex') | length > 0)
                                                         else '') }}"

        # Type: string
        plex2_webtools_traefik_middleware_custom: ""

        # Type: string
        plex2_webtools_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: string
        plex2_webtools_traefik_router: "{{ lookup('role_var', '_webtools_web_subdomain', role='plex') }}"

        ```

??? example "Theme"

    === "Role-level"

        ```yaml
        # Type: bool (true/false)
        plex_role_themepark_enabled: false

        # Options can be found at https://docs.theme-park.dev/themes/plex/
        # Type: string
        plex_role_themepark_theme: "{{ global_themepark_theme }}"

        # Allows you to override the url where CSS files can be found
        # Type: string
        plex_role_themepark_domain: "{{ global_themepark_domain }}"

        # Options can be found at https://docs.theme-park.dev/themes/addons/
        # Type: list
        plex_role_themepark_addons: []

        ```

    === "Instance-level"

        ```yaml
        # Type: bool (true/false)
        plex2_themepark_enabled: false

        # Options can be found at https://docs.theme-park.dev/themes/plex/
        # Type: string
        plex2_themepark_theme: "{{ global_themepark_theme }}"

        # Allows you to override the url where CSS files can be found
        # Type: string
        plex2_themepark_domain: "{{ global_themepark_domain }}"

        # Options can be found at https://docs.theme-park.dev/themes/addons/
        # Type: list
        plex2_themepark_addons: []

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        plex_role_docker_container: "{{ plex_name }}"

        # Image
        # Type: bool (true/false)
        plex_role_docker_image_pull: true

        # Type: string
        plex_role_docker_image_repo: "plexinc/pms-docker"

        # Type: string
        plex_role_docker_image_tag: "latest"

        # Type: string
        plex_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='plex') }}:{{ lookup('role_var', '_docker_image_tag', role='plex') }}"

        # Ports
        # Type: string
        plex_role_docker_ports_32400: "{{ port_lookup_32400.meta.port
                                       if (port_lookup_32400.meta.port is defined) and (port_lookup_32400.meta.port | trim | length > 0)
                                       else '32400' }}"

        # Type: list
        plex_role_docker_ports_defaults: []

        # Type: list
        plex_role_docker_ports_custom: []

        # Envs
        # Type: string
        plex_role_docker_envs_advertise_ip_url: "{{ lookup('role_var', '_web_url', role='plex') + ':443,' + lookup('role_var', '_web_insecure_url', role='plex') + ':80'
                                                 if lookup('role_var', '_insecure', role='plex')
                                                 else lookup('role_var', '_web_url', role='plex') + ':443' }}"

        # Type: string
        plex_role_docker_envs_advertise_ip: "{{ 'http://' + lookup('role_var', '_lan_ip', role='plex') + ':32400,' + lookup('role_var', '_docker_envs_advertise_ip_url', role='plex')
                                             if (lookup('role_var', '_lan_ip', role='plex') | length > 0) and lookup('role_var', '_open_main_ports', role='plex')
                                             else lookup('role_var', '_docker_envs_advertise_ip_url', role='plex') }}"

        # Type: dict
        plex_role_docker_envs_default: 
          PLEX_UID: "{{ uid }}"
          PLEX_GID: "{{ gid }}"
          PLEX_CLAIM: "{{ (plex_claim_code) | default(omit) }}"
          CHANGE_CONFIG_DIR_OWNERSHIP: "false"
          TZ: "{{ tz }}"
          ADVERTISE_IP: "{{ lookup('role_var', '_docker_envs_advertise_ip', role='plex') }}"

        # Type: dict
        plex_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        plex_role_docker_volumes_default: 
          - "{{ plex_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
          - "/dev/shm:/dev/shm"
          - "{{ plex_role_paths_transcodes_location }}:/transcode"

        # Type: list
        plex_role_docker_volumes_legacy: 
          - "/mnt/unionfs/Media:/data"

        # Type: list
        plex_role_docker_volumes_custom: []

        # Mounts
        # Type: list
        plex_role_docker_mounts_default: 
          - target: /tmp
            type: tmpfs

        # Type: list
        plex_role_docker_mounts_custom: []

        # Hosts
        # Type: dict
        plex_role_docker_hosts_default: 
          metric.plex.tv: "{{ ip_address_localhost }}"
          metrics.plex.tv: "{{ ip_address_localhost }}"
          analytics.plex.tv: "{{ ip_address_localhost }}"

        # Type: dict
        plex_role_docker_hosts_custom: {}

        # Labels
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

        # Type: dict
        plex_role_docker_labels_custom: {}

        # Hostname
        # Type: string
        plex_role_docker_hostname: "{{ plex_name }}"

        # Networks
        # Type: string
        plex_role_docker_networks_alias: "{{ plex_name }}"

        # Type: list
        plex_role_docker_networks_default: []

        # Type: list
        plex_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        plex_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        plex_role_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via create_docker_container
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        plex_role_docker_blkio_weight:

        # Type: int
        plex_role_docker_cpu_period:

        # Type: int
        plex_role_docker_cpu_quota:

        # Type: int
        plex_role_docker_cpu_shares:

        # Type: string
        plex_role_docker_cpus:

        # Type: string
        plex_role_docker_cpuset_cpus:

        # Type: string
        plex_role_docker_cpuset_mems:

        # Type: string
        plex_role_docker_kernel_memory:

        # Type: string
        plex_role_docker_memory:

        # Type: string
        plex_role_docker_memory_reservation:

        # Type: string
        plex_role_docker_memory_swap:

        # Type: int
        plex_role_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        plex_role_docker_cap_drop:

        # Type: list
        plex_role_docker_device_cgroup_rules:

        # Type: list
        plex_role_docker_device_read_bps:

        # Type: list
        plex_role_docker_device_read_iops:

        # Type: list
        plex_role_docker_device_requests:

        # Type: list
        plex_role_docker_device_write_bps:

        # Type: list
        plex_role_docker_device_write_iops:

        # Type: list
        plex_role_docker_devices:

        # Type: string
        plex_role_docker_devices_default:

        # Type: bool (true/false)
        plex_role_docker_privileged:

        # Type: list
        plex_role_docker_security_opts:

        # Networking
        # Type: list
        plex_role_docker_dns_opts:

        # Type: list
        plex_role_docker_dns_search_domains:

        # Type: list
        plex_role_docker_dns_servers:

        # Type: string
        plex_role_docker_hosts_use_common:

        # Type: string
        plex_role_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        plex_role_docker_keep_volumes:

        # Type: string
        plex_role_docker_volume_driver:

        # Type: list
        plex_role_docker_volumes_from:

        # Type: string
        plex_role_docker_volumes_global:

        # Type: string
        plex_role_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        plex_role_docker_healthcheck:

        # Type: bool (true/false)
        plex_role_docker_init:

        # Type: string
        plex_role_docker_log_driver:

        # Type: dict
        plex_role_docker_log_options:

        # Type: bool (true/false)
        plex_role_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        plex_role_docker_auto_remove:

        # Type: list
        plex_role_docker_capabilities:

        # Type: string
        plex_role_docker_cgroup_parent:

        # Type: string
        plex_role_docker_cgroupns_mode:

        # Type: bool (true/false)
        plex_role_docker_cleanup:

        # Type: list
        plex_role_docker_commands:

        # Type: string
        plex_role_docker_create_timeout:

        # Type: string
        plex_role_docker_domainname:

        # Type: string
        plex_role_docker_entrypoint:

        # Type: string
        plex_role_docker_env_file:

        # Type: list
        plex_role_docker_exposed_ports:

        # Type: string
        plex_role_docker_force_kill:

        # Type: list
        plex_role_docker_groups:

        # Type: int
        plex_role_docker_healthy_wait_timeout:

        # Type: string
        plex_role_docker_ipc_mode:

        # Type: string
        plex_role_docker_kill_signal:

        # Type: string
        plex_role_docker_labels_use_common:

        # Type: list
        plex_role_docker_links:

        # Type: bool (true/false)
        plex_role_docker_oom_killer:

        # Type: int
        plex_role_docker_oom_score_adj:

        # Type: bool (true/false)
        plex_role_docker_paused:

        # Type: string
        plex_role_docker_pid_mode:

        # Type: bool (true/false)
        plex_role_docker_read_only:

        # Type: bool (true/false)
        plex_role_docker_recreate:

        # Type: int
        plex_role_docker_restart_retries:

        # Type: string
        plex_role_docker_runtime:

        # Type: string
        plex_role_docker_shm_size:

        # Type: int
        plex_role_docker_stop_timeout:

        # Type: dict
        plex_role_docker_storage_opts:

        # Type: list
        plex_role_docker_sysctls:

        # Type: list
        plex_role_docker_tmpfs:

        # Type: list
        plex_role_docker_ulimits:

        # Type: string
        plex_role_docker_user:

        # Type: string
        plex_role_docker_userns_mode:

        # Type: string
        plex_role_docker_uts:

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        plex2_docker_container: "{{ plex_name }}"

        # Image
        # Type: bool (true/false)
        plex2_docker_image_pull: true

        # Type: string
        plex2_docker_image_repo: "plexinc/pms-docker"

        # Type: string
        plex2_docker_image_tag: "latest"

        # Type: string
        plex2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='plex') }}:{{ lookup('role_var', '_docker_image_tag', role='plex') }}"

        # Ports
        # Type: string
        plex2_docker_ports_32400: "{{ port_lookup_32400.meta.port
                                   if (port_lookup_32400.meta.port is defined) and (port_lookup_32400.meta.port | trim | length > 0)
                                   else '32400' }}"

        # Type: list
        plex2_docker_ports_defaults: []

        # Type: list
        plex2_docker_ports_custom: []

        # Envs
        # Type: string
        plex2_docker_envs_advertise_ip_url: "{{ lookup('role_var', '_web_url', role='plex') + ':443,' + lookup('role_var', '_web_insecure_url', role='plex') + ':80'
                                             if lookup('role_var', '_insecure', role='plex')
                                             else lookup('role_var', '_web_url', role='plex') + ':443' }}"

        # Type: string
        plex2_docker_envs_advertise_ip: "{{ 'http://' + lookup('role_var', '_lan_ip', role='plex') + ':32400,' + lookup('role_var', '_docker_envs_advertise_ip_url', role='plex')
                                         if (lookup('role_var', '_lan_ip', role='plex') | length > 0) and lookup('role_var', '_open_main_ports', role='plex')
                                         else lookup('role_var', '_docker_envs_advertise_ip_url', role='plex') }}"

        # Type: dict
        plex2_docker_envs_default: 
          PLEX_UID: "{{ uid }}"
          PLEX_GID: "{{ gid }}"
          PLEX_CLAIM: "{{ (plex_claim_code) | default(omit) }}"
          CHANGE_CONFIG_DIR_OWNERSHIP: "false"
          TZ: "{{ tz }}"
          ADVERTISE_IP: "{{ lookup('role_var', '_docker_envs_advertise_ip', role='plex') }}"

        # Type: dict
        plex2_docker_envs_custom: {}

        # Volumes
        # Type: list
        plex2_docker_volumes_default: 
          - "{{ plex_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
          - "/dev/shm:/dev/shm"
          - "{{ plex_role_paths_transcodes_location }}:/transcode"

        # Type: list
        plex2_docker_volumes_legacy: 
          - "/mnt/unionfs/Media:/data"

        # Type: list
        plex2_docker_volumes_custom: []

        # Mounts
        # Type: list
        plex2_docker_mounts_default: 
          - target: /tmp
            type: tmpfs

        # Type: list
        plex2_docker_mounts_custom: []

        # Hosts
        # Type: dict
        plex2_docker_hosts_default: 
          metric.plex.tv: "{{ ip_address_localhost }}"
          metrics.plex.tv: "{{ ip_address_localhost }}"
          analytics.plex.tv: "{{ ip_address_localhost }}"

        # Type: dict
        plex2_docker_hosts_custom: {}

        # Labels
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

        # Type: dict
        plex2_docker_labels_custom: {}

        # Hostname
        # Type: string
        plex2_docker_hostname: "{{ plex_name }}"

        # Networks
        # Type: string
        plex2_docker_networks_alias: "{{ plex_name }}"

        # Type: list
        plex2_docker_networks_default: []

        # Type: list
        plex2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        plex2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        plex2_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via lookup('docker_var', ...)
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        plex2_docker_blkio_weight:
        # Type: int
        plex2_docker_cpu_period:
        # Type: int
        plex2_docker_cpu_quota:
        # Type: int
        plex2_docker_cpu_shares:
        # Type: string
        plex2_docker_cpus:
        # Type: string
        plex2_docker_cpuset_cpus:
        # Type: string
        plex2_docker_cpuset_mems:
        # Type: string
        plex2_docker_kernel_memory:
        # Type: string
        plex2_docker_memory:
        # Type: string
        plex2_docker_memory_reservation:
        # Type: string
        plex2_docker_memory_swap:
        # Type: int
        plex2_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        plex2_docker_cap_drop:
        # Type: list
        plex2_docker_device_cgroup_rules:
        # Type: list
        plex2_docker_device_read_bps:
        # Type: list
        plex2_docker_device_read_iops:
        # Type: list
        plex2_docker_device_requests:
        # Type: list
        plex2_docker_device_write_bps:
        # Type: list
        plex2_docker_device_write_iops:
        # Type: list
        plex2_docker_devices:
        # Type: string
        plex2_docker_devices_default:
        # Type: bool (true/false)
        plex2_docker_privileged:
        # Type: list
        plex2_docker_security_opts:

        # Networking
        # Type: list
        plex2_docker_dns_opts:
        # Type: list
        plex2_docker_dns_search_domains:
        # Type: list
        plex2_docker_dns_servers:
        # Type: string
        plex2_docker_hosts_use_common:
        # Type: string
        plex2_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        plex2_docker_keep_volumes:
        # Type: string
        plex2_docker_volume_driver:
        # Type: list
        plex2_docker_volumes_from:
        # Type: string
        plex2_docker_volumes_global:
        # Type: string
        plex2_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        plex2_docker_healthcheck:
        # Type: bool (true/false)
        plex2_docker_init:
        # Type: string
        plex2_docker_log_driver:
        # Type: dict
        plex2_docker_log_options:
        # Type: bool (true/false)
        plex2_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        plex2_docker_auto_remove:
        # Type: list
        plex2_docker_capabilities:
        # Type: string
        plex2_docker_cgroup_parent:
        # Type: string
        plex2_docker_cgroupns_mode:
        # Type: bool (true/false)
        plex2_docker_cleanup:
        # Type: list
        plex2_docker_commands:
        # Type: string
        plex2_docker_create_timeout:
        # Type: string
        plex2_docker_domainname:
        # Type: string
        plex2_docker_entrypoint:
        # Type: string
        plex2_docker_env_file:
        # Type: list
        plex2_docker_exposed_ports:
        # Type: string
        plex2_docker_force_kill:
        # Type: list
        plex2_docker_groups:
        # Type: int
        plex2_docker_healthy_wait_timeout:
        # Type: string
        plex2_docker_ipc_mode:
        # Type: string
        plex2_docker_kill_signal:
        # Type: string
        plex2_docker_labels_use_common:
        # Type: list
        plex2_docker_links:
        # Type: bool (true/false)
        plex2_docker_oom_killer:
        # Type: int
        plex2_docker_oom_score_adj:
        # Type: bool (true/false)
        plex2_docker_paused:
        # Type: string
        plex2_docker_pid_mode:
        # Type: bool (true/false)
        plex2_docker_read_only:
        # Type: bool (true/false)
        plex2_docker_recreate:
        # Type: int
        plex2_docker_restart_retries:
        # Type: string
        plex2_docker_runtime:
        # Type: string
        plex2_docker_shm_size:
        # Type: int
        plex2_docker_stop_timeout:
        # Type: dict
        plex2_docker_storage_opts:
        # Type: list
        plex2_docker_sysctls:
        # Type: list
        plex2_docker_tmpfs:
        # Type: list
        plex2_docker_ulimits:
        # Type: string
        plex2_docker_user:
        # Type: string
        plex2_docker_userns_mode:
        # Type: string
        plex2_docker_uts:

        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        plex_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        plex_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        plex_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        plex_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        plex_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        plex_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        plex_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        plex_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        plex_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        plex_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        plex_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        plex_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        plex_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        plex_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        plex_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        plex_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        plex_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            plex_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "plex2.{{ user.domain }}"
              - "plex.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            plex_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'plex2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `plex2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        plex2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        plex2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        plex2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        plex2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        plex2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        plex2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        plex2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        plex2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        plex2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        plex2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        plex2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        plex2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        plex2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        plex2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        plex2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        plex2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        plex2_web_scheme:

        ```

        1.  Example:

            ```yaml
            plex2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "plex2.{{ user.domain }}"
              - "plex.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            plex2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'plex2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
hide:
  - tags
tags:
  - qbittorrent
---

# qBittorrent

## What is it?

[qBittorrent](https://www.qbittorrent.org/) is a bittorrent client programmed in C++ / Qt that uses libtorrent (sometimes called libtorrent-rasterbar) by Arvid Norberg.

It aims to be a good alternative to all other bittorrent clients out there. qBittorrent is fast, stable and provides unicode support as well as many features.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.qbittorrent.org/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/qbittorrent/qBittorrent/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/qbittorrent/qBittorrent){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/saltydk/qbittorrent){: .header-icons }|

### 1. Installation

``` shell

sb install qbittorrent

```

### 2. URL

- To access qBittorrent, visit `https://qbittorrent._yourdomain.com_`

### 3. Setup

- Access qbittorrent at `https://qbittorrent._yourdomain.com_`

- Log in using the username/password you specified in `accounts.yml`

- **OPTIONALLY** go to `Options` -> `Web UI` and set a new username and a strong password.

    ![Authentication Section Screenshot](../images/community/qbit_auth.png)

- Under `Options` -> `Connection`, set the port to 56881.

    ![Port Section Screenshot](../images/community/qbit_port.png)

- Under `Options` -> `Downloads`, set the following;

  - Save files to location: `/mnt/unionfs/downloads/torrents/qbittorrent/completed/`

  - Keep incomplete torrents in: `/mnt/unionfs/downloads/torrents/qbittorrent/incoming/`

  - Copy .torrent files to: `/mnt/unionfs/downloads/torrents/qbittorrent/torrents/`

  - Copy .torrent files for finished downloads to: `/mnt/unionfs/downloads/torrents/qbittorrent/torrents/`

  - Additionally you can set monitored folder to: `/mnt/unionfs/downloads/torrents/qbittorrent/watched/`

  - tick `Run external program on torrent completion` and paste this into the box: `/usr/bin/unrar x -r "%F/." "%F/"`

    ![Hard Disk Section Screenshot](../images/community/qbit_hdd.png)
<!-- markdownlint-disable MD046 -->
!!! warning
      Make sure to choose a strong username/password combination because by default qBittorrent's Web API is completely exposed to the internet!  
      If someone guesses your qBit's credentials, they can, among other things, steal your tracker passkeys and delete torrents (data included).  
      If you don't need the API endpoints exposed, you can disable them using the [inventory system](../saltbox/inventory/index.md) with

      ``` { .yaml }
      qbittorrent_traefik_api_enabled: false
      ```

      and by rerunning the `qbittorrent` tag.
<!-- markdownlint-enable MD046 -->

!!! note
      if you're using private trackers be sure to go to `Options` -> `BitTorrent` and uncheck everything in Privacy section.

## Next

Are you setting Saltbox up for the first time?  Continue to [NZBHydra2](nzbhydra2.md).

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `qbittorrent_instances`.

    === "Role-level Override"

        Applies to all instances of qbittorrent:

        ```yaml
        qbittorrent_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `qbittorrent2`):

        ```yaml
        qbittorrent2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `qbittorrent_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `qbittorrent_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`qbittorrent_instances`"

        ```yaml
        # Type: list
        qbittorrent_instances: ["qbittorrent"]
        ```

        !!! example

            ```yaml
            # Type: list
            qbittorrent_instances: ["qbittorrent", "qbittorrent2"]
            ```

=== "Settings"

    === "Role-level"

        ??? variable bool "`qbittorrent_role_host_install`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent_role_host_install: false
            ```

        ??? variable string "`qbittorrent_role_webui_custom_headers_enabled`"

            ```yaml
            # Type: string
            qbittorrent_role_webui_custom_headers_enabled: "{{ 'true' if lookup('role_var', '_themepark_enabled', role='qbittorrent') and global_themepark_plugin_enabled else 'false' }}"
            ```

        ??? variable string "`qbittorrent_role_webui_custom_headers_default`"

            ```yaml
            # Type: string
            qbittorrent_role_webui_custom_headers_default: "{{ (qbittorrent_role_themepark_headers if lookup('role_var', '_themepark_enabled', role='qbittorrent') and global_themepark_plugin_enabled else '') }}"
            ```

        ??? variable string "`qbittorrent_role_webui_custom_headers_custom`"

            ```yaml
            # Type: string
            qbittorrent_role_webui_custom_headers_custom: ""
            ```

        ??? variable string "`qbittorrent_role_torrent_content_remove_option`"

            ```yaml
            # Options are: Delete or MoveToTrash
            # Type: string
            qbittorrent_role_torrent_content_remove_option: "Delete"
            ```

    === "Instance-level"

        ??? variable bool "`qbittorrent2_host_install`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent2_host_install: false
            ```

        ??? variable string "`qbittorrent2_webui_custom_headers_enabled`"

            ```yaml
            # Type: string
            qbittorrent2_webui_custom_headers_enabled: "{{ 'true' if lookup('role_var', '_themepark_enabled', role='qbittorrent') and global_themepark_plugin_enabled else 'false' }}"
            ```

        ??? variable string "`qbittorrent2_webui_custom_headers_default`"

            ```yaml
            # Type: string
            qbittorrent2_webui_custom_headers_default: "{{ (qbittorrent_role_themepark_headers if lookup('role_var', '_themepark_enabled', role='qbittorrent') and global_themepark_plugin_enabled else '') }}"
            ```

        ??? variable string "`qbittorrent2_webui_custom_headers_custom`"

            ```yaml
            # Type: string
            qbittorrent2_webui_custom_headers_custom: ""
            ```

        ??? variable string "`qbittorrent2_torrent_content_remove_option`"

            ```yaml
            # Options are: Delete or MoveToTrash
            # Type: string
            qbittorrent2_torrent_content_remove_option: "Delete"
            ```

=== "Host Install"

    === "Role-level"

        ??? variable string "`qbittorrent_role_host_branch`"

            ```yaml
            # Options are: libtorrent1 (latest), libtorrent2 (latest) or legacy (4.3.9)
            # Type: string
            qbittorrent_role_host_branch: libtorrent1
            ```

        ??? variable string "`qbittorrent_role_host_specific_version`"

            ```yaml
            # Example being "release-4.4.5_v1.2.18"
            # If this is set then the above branch logic is ignored
            # Type: string
            qbittorrent_role_host_specific_version: ""
            ```

        ??? variable string "`qbittorrent_role_host_download_endpoint`"

            ```yaml
            # Lookup variables
            # Type: string
            qbittorrent_role_host_download_endpoint: "{{ 'https://github.com/userdocs/qbittorrent-nox-static/releases/download/'
                                                      if lookup('role_var', '_host_branch', role='qbittorrent') != 'legacy'
                                                      else 'https://github.com/userdocs/qbittorrent-nox-static-legacy/releases/download/' }}"
            ```

        ??? variable string "`qbittorrent_role_host_download_url`"

            ```yaml
            # Type: string
            qbittorrent_role_host_download_url: "{{ lookup('role_var', '_host_download_endpoint', role='qbittorrent') }}{{ lookup('role_var', '_host_specific_version', role='qbittorrent')
                                                                                                                        if (lookup('role_var', '_host_specific_version', role='qbittorrent') | length > 0)
                                                                                                                        else qbittorrent_release_version.stdout }}/x86_64-qbittorrent-nox"
            ```

        ??? variable string "`qbittorrent_role_host_release_url`"

            ```yaml
            # Type: string
            qbittorrent_role_host_release_url: "{{ 'https://github.com/userdocs/qbittorrent-nox-static/releases/latest/download/dependency-version.json'
                                                if lookup('role_var', '_host_branch', role='qbittorrent') != 'legacy'
                                                else 'https://github.com/userdocs/qbittorrent-nox-static-legacy/releases/latest/download/dependency-version.json' }}"
            ```

        ??? variable string "`qbittorrent_role_host_lookup_libtorrent1`"

            ```yaml
            # Type: string
            qbittorrent_role_host_lookup_libtorrent1: 'release-\(.qbittorrent)_v\(.libtorrent_1_2)'
            ```

        ??? variable string "`qbittorrent_role_host_lookup_libtorrent2`"

            ```yaml
            # Type: string
            qbittorrent_role_host_lookup_libtorrent2: 'release-\(.qbittorrent)_v\(.libtorrent_2_0)'
            ```

        ??? variable string "`qbittorrent_role_host_release_lookup`"

            ```yaml
            # Type: string
            qbittorrent_role_host_release_lookup: "{{ qbittorrent_role_host_lookup_libtorrent2
                                                   if lookup('role_var', '_host_branch', role='qbittorrent') == 'libtorrent2'
                                                   else qbittorrent_role_host_lookup_libtorrent1 }}"
            ```

        ??? variable string "`qbittorrent_role_host_version`"

            ```yaml
            # Type: string
            qbittorrent_role_host_version: |
              curl -sL {{ lookup('role_var', '_host_release_url', role='qbittorrent') }} | jq -r '. | "{{ lookup('role_var', '_host_release_lookup', role='qbittorrent') }}"'
            ```

        ??? variable string "`qbittorrent_role_service_name`"

            ```yaml
            # Type: string
            qbittorrent_role_service_name: "saltbox_managed_{{ qbittorrent_name }}.service"
            ```

        ??? variable string "`qbittorrent_role_service_after`"

            ```yaml
            # Type: string
            qbittorrent_role_service_after: "network-online.target docker.service"
            ```

        ??? variable string "`qbittorrent_role_service_requires`"

            ```yaml
            # Type: string
            qbittorrent_role_service_requires: "network-online.target docker.service"
            ```

        ??? variable string "`qbittorrent_role_service_wants`"

            ```yaml
            # Type: string
            qbittorrent_role_service_wants: ""
            ```

    === "Instance-level"

        ??? variable string "`qbittorrent2_host_branch`"

            ```yaml
            # Options are: libtorrent1 (latest), libtorrent2 (latest) or legacy (4.3.9)
            # Type: string
            qbittorrent2_host_branch: libtorrent1
            ```

        ??? variable string "`qbittorrent2_host_specific_version`"

            ```yaml
            # Example being "release-4.4.5_v1.2.18"
            # If this is set then the above branch logic is ignored
            # Type: string
            qbittorrent2_host_specific_version: ""
            ```

        ??? variable string "`qbittorrent2_host_download_endpoint`"

            ```yaml
            # Lookup variables
            # Type: string
            qbittorrent2_host_download_endpoint: "{{ 'https://github.com/userdocs/qbittorrent-nox-static/releases/download/'
                                                  if lookup('role_var', '_host_branch', role='qbittorrent') != 'legacy'
                                                  else 'https://github.com/userdocs/qbittorrent-nox-static-legacy/releases/download/' }}"
            ```

        ??? variable string "`qbittorrent2_host_download_url`"

            ```yaml
            # Type: string
            qbittorrent2_host_download_url: "{{ lookup('role_var', '_host_download_endpoint', role='qbittorrent') }}{{ lookup('role_var', '_host_specific_version', role='qbittorrent')
                                                                                                                    if (lookup('role_var', '_host_specific_version', role='qbittorrent') | length > 0)
                                                                                                                    else qbittorrent_release_version.stdout }}/x86_64-qbittorrent-nox"
            ```

        ??? variable string "`qbittorrent2_host_release_url`"

            ```yaml
            # Type: string
            qbittorrent2_host_release_url: "{{ 'https://github.com/userdocs/qbittorrent-nox-static/releases/latest/download/dependency-version.json'
                                            if lookup('role_var', '_host_branch', role='qbittorrent') != 'legacy'
                                            else 'https://github.com/userdocs/qbittorrent-nox-static-legacy/releases/latest/download/dependency-version.json' }}"
            ```

        ??? variable string "`qbittorrent2_host_lookup_libtorrent1`"

            ```yaml
            # Type: string
            qbittorrent2_host_lookup_libtorrent1: 'release-\(.qbittorrent)_v\(.libtorrent_1_2)'
            ```

        ??? variable string "`qbittorrent2_host_lookup_libtorrent2`"

            ```yaml
            # Type: string
            qbittorrent2_host_lookup_libtorrent2: 'release-\(.qbittorrent)_v\(.libtorrent_2_0)'
            ```

        ??? variable string "`qbittorrent2_host_release_lookup`"

            ```yaml
            # Type: string
            qbittorrent2_host_release_lookup: "{{ qbittorrent_role_host_lookup_libtorrent2
                                               if lookup('role_var', '_host_branch', role='qbittorrent') == 'libtorrent2'
                                               else qbittorrent_role_host_lookup_libtorrent1 }}"
            ```

        ??? variable string "`qbittorrent2_host_version`"

            ```yaml
            # Type: string
            qbittorrent2_host_version: |
              curl -sL {{ lookup('role_var', '_host_release_url', role='qbittorrent') }} | jq -r '. | "{{ lookup('role_var', '_host_release_lookup', role='qbittorrent') }}"'
            ```

        ??? variable string "`qbittorrent2_service_name`"

            ```yaml
            # Type: string
            qbittorrent2_service_name: "saltbox_managed_{{ qbittorrent_name }}.service"
            ```

        ??? variable string "`qbittorrent2_service_after`"

            ```yaml
            # Type: string
            qbittorrent2_service_after: "network-online.target docker.service"
            ```

        ??? variable string "`qbittorrent2_service_requires`"

            ```yaml
            # Type: string
            qbittorrent2_service_requires: "network-online.target docker.service"
            ```

        ??? variable string "`qbittorrent2_service_wants`"

            ```yaml
            # Type: string
            qbittorrent2_service_wants: ""
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`qbittorrent_role_paths_folder`"

            ```yaml
            # Type: string
            qbittorrent_role_paths_folder: "{{ qbittorrent_name }}"
            ```

        ??? variable string "`qbittorrent_role_paths_location`"

            ```yaml
            # Type: string
            qbittorrent_role_paths_location: "{{ server_appdata_path }}/{{ qbittorrent_role_paths_folder }}"
            ```

        ??? variable string "`qbittorrent_role_paths_downloads_location`"

            ```yaml
            # Type: string
            qbittorrent_role_paths_downloads_location: "{{ downloads_torrents_path }}/{{ qbittorrent_role_paths_folder }}"
            ```

        ??? variable string "`qbittorrent_role_paths_conf`"

            ```yaml
            # Type: string
            qbittorrent_role_paths_conf: "{{ qbittorrent_role_paths_location }}/qBittorrent/qBittorrent.conf"
            ```

    === "Instance-level"

        ??? variable string "`qbittorrent2_paths_folder`"

            ```yaml
            # Type: string
            qbittorrent2_paths_folder: "{{ qbittorrent_name }}"
            ```

        ??? variable string "`qbittorrent2_paths_location`"

            ```yaml
            # Type: string
            qbittorrent2_paths_location: "{{ server_appdata_path }}/{{ qbittorrent_role_paths_folder }}"
            ```

        ??? variable string "`qbittorrent2_paths_downloads_location`"

            ```yaml
            # Type: string
            qbittorrent2_paths_downloads_location: "{{ downloads_torrents_path }}/{{ qbittorrent_role_paths_folder }}"
            ```

        ??? variable string "`qbittorrent2_paths_conf`"

            ```yaml
            # Type: string
            qbittorrent2_paths_conf: "{{ qbittorrent_role_paths_location }}/qBittorrent/qBittorrent.conf"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`qbittorrent_role_web_subdomain`"

            ```yaml
            # Type: string
            qbittorrent_role_web_subdomain: "{{ qbittorrent_name }}"
            ```

        ??? variable string "`qbittorrent_role_web_domain`"

            ```yaml
            # Type: string
            qbittorrent_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`qbittorrent_role_web_port`"

            ```yaml
            # Type: string
            qbittorrent_role_web_port: "8080"
            ```

        ??? variable string "`qbittorrent_role_web_url`"

            ```yaml
            # Type: string
            qbittorrent_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='qbittorrent') + '.' + lookup('role_var', '_web_domain', role='qbittorrent')
                                       if (lookup('role_var', '_web_subdomain', role='qbittorrent') | length > 0)
                                       else lookup('role_var', '_web_domain', role='qbittorrent')) }}"
            ```

    === "Instance-level"

        ??? variable string "`qbittorrent2_web_subdomain`"

            ```yaml
            # Type: string
            qbittorrent2_web_subdomain: "{{ qbittorrent_name }}"
            ```

        ??? variable string "`qbittorrent2_web_domain`"

            ```yaml
            # Type: string
            qbittorrent2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`qbittorrent2_web_port`"

            ```yaml
            # Type: string
            qbittorrent2_web_port: "8080"
            ```

        ??? variable string "`qbittorrent2_web_url`"

            ```yaml
            # Type: string
            qbittorrent2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='qbittorrent') + '.' + lookup('role_var', '_web_domain', role='qbittorrent')
                                   if (lookup('role_var', '_web_subdomain', role='qbittorrent') | length > 0)
                                   else lookup('role_var', '_web_domain', role='qbittorrent')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`qbittorrent_role_dns_record`"

            ```yaml
            # Type: string
            qbittorrent_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='qbittorrent') }}"
            ```

        ??? variable string "`qbittorrent_role_dns_zone`"

            ```yaml
            # Type: string
            qbittorrent_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='qbittorrent') }}"
            ```

        ??? variable bool "`qbittorrent_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`qbittorrent2_dns_record`"

            ```yaml
            # Type: string
            qbittorrent2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='qbittorrent') }}"
            ```

        ??? variable string "`qbittorrent2_dns_zone`"

            ```yaml
            # Type: string
            qbittorrent2_dns_zone: "{{ lookup('role_var', '_web_domain', role='qbittorrent') }}"
            ```

        ??? variable bool "`qbittorrent2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent2_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`qbittorrent_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            qbittorrent_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`qbittorrent_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            qbittorrent_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                             + (',themepark-' + qbittorrent_name
                                                               if (lookup('role_var', '_themepark_enabled', role='qbittorrent') and global_themepark_plugin_enabled)
                                                               else '') }}"
            ```

        ??? variable string "`qbittorrent_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            qbittorrent_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`qbittorrent_role_traefik_certresolver`"

            ```yaml
            # Type: string
            qbittorrent_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`qbittorrent_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent_role_traefik_enabled: true
            ```

        ??? variable bool "`qbittorrent_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent_role_traefik_api_enabled: true
            ```

        ??? variable string "`qbittorrent_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            qbittorrent_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/command`) || PathPrefix(`/query`) || PathPrefix(`/login`) || PathPrefix(`/sync`)"
            ```

    === "Instance-level"

        ??? variable string "`qbittorrent2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            qbittorrent2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`qbittorrent2_traefik_middleware_default`"

            ```yaml
            # Type: string
            qbittorrent2_traefik_middleware_default: "{{ traefik_default_middleware
                                                         + (',themepark-' + qbittorrent_name
                                                           if (lookup('role_var', '_themepark_enabled', role='qbittorrent') and global_themepark_plugin_enabled)
                                                           else '') }}"
            ```

        ??? variable string "`qbittorrent2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            qbittorrent2_traefik_middleware_custom: ""
            ```

        ??? variable string "`qbittorrent2_traefik_certresolver`"

            ```yaml
            # Type: string
            qbittorrent2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`qbittorrent2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent2_traefik_enabled: true
            ```

        ??? variable bool "`qbittorrent2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent2_traefik_api_enabled: true
            ```

        ??? variable string "`qbittorrent2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            qbittorrent2_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/command`) || PathPrefix(`/query`) || PathPrefix(`/login`) || PathPrefix(`/sync`)"
            ```

=== "Theme"

    === "Role-level"

        ??? variable bool "`qbittorrent_role_themepark_enabled`"

            ```yaml
            # Options can be found at https://github.com/themepark-dev/theme.park
            # Type: bool (true/false)
            qbittorrent_role_themepark_enabled: false
            ```

        ??? variable string "`qbittorrent_role_themepark_app`"

            ```yaml
            # Type: string
            qbittorrent_role_themepark_app: "qbittorrent"
            ```

        ??? variable string "`qbittorrent_role_themepark_theme`"

            ```yaml
            # Type: string
            qbittorrent_role_themepark_theme: "{{ global_themepark_theme }}"
            ```

        ??? variable string "`qbittorrent_role_themepark_domain`"

            ```yaml
            # Type: string
            qbittorrent_role_themepark_domain: "{{ global_themepark_domain }}"
            ```

        ??? variable list "`qbittorrent_role_themepark_addons`"

            ```yaml
            # Type: list
            qbittorrent_role_themepark_addons: []
            ```

        ??? variable string "`qbittorrent_role_themepark_headers`"

            ```yaml
            # Type: string
            qbittorrent_role_themepark_headers: "\"content-security-policy: default-src 'self'; style-src 'self' 'unsafe-inline' theme-park.dev raw.githubusercontent.com use.fontawesome.com; img-src 'self' theme-park.dev raw.githubusercontent.com data:; script-src 'self' 'unsafe-inline'; object-src 'none'; form-action 'self'; frame-ancestors 'self'; font-src use.fontawesome.com;\""
            ```

    === "Instance-level"

        ??? variable bool "`qbittorrent2_themepark_enabled`"

            ```yaml
            # Options can be found at https://github.com/themepark-dev/theme.park
            # Type: bool (true/false)
            qbittorrent2_themepark_enabled: false
            ```

        ??? variable string "`qbittorrent2_themepark_app`"

            ```yaml
            # Type: string
            qbittorrent2_themepark_app: "qbittorrent"
            ```

        ??? variable string "`qbittorrent2_themepark_theme`"

            ```yaml
            # Type: string
            qbittorrent2_themepark_theme: "{{ global_themepark_theme }}"
            ```

        ??? variable string "`qbittorrent2_themepark_domain`"

            ```yaml
            # Type: string
            qbittorrent2_themepark_domain: "{{ global_themepark_domain }}"
            ```

        ??? variable list "`qbittorrent2_themepark_addons`"

            ```yaml
            # Type: list
            qbittorrent2_themepark_addons: []
            ```

        ??? variable string "`qbittorrent2_themepark_headers`"

            ```yaml
            # Type: string
            qbittorrent2_themepark_headers: "\"content-security-policy: default-src 'self'; style-src 'self' 'unsafe-inline' theme-park.dev raw.githubusercontent.com use.fontawesome.com; img-src 'self' theme-park.dev raw.githubusercontent.com data:; script-src 'self' 'unsafe-inline'; object-src 'none'; form-action 'self'; frame-ancestors 'self'; font-src use.fontawesome.com;\""
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`qbittorrent_role_docker_container`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_container: "{{ qbittorrent_name }}"
            ```

        ##### Image

        ??? variable bool "`qbittorrent_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent_role_docker_image_pull: true
            ```

        ??? variable string "`qbittorrent_role_docker_image_repo`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_image_repo: "saltydk/qbittorrent"
            ```

        ??? variable string "`qbittorrent_role_docker_image_tag`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_image_tag: "latest"
            ```

        ??? variable string "`qbittorrent_role_docker_image`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='qbittorrent') }}:{{ lookup('role_var', '_docker_image_tag', role='qbittorrent') }}"
            ```

        ##### Ports

        ??? variable string "`qbittorrent_role_docker_ports_56881`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_ports_56881: "{{ port_lookup_56881.meta.port
                                                  if (port_lookup_56881.meta.port is defined) and (port_lookup_56881.meta.port | trim | length > 0)
                                                  else '56881' }}"
            ```

        ??? variable string "`qbittorrent_role_docker_ports_8080`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_ports_8080: "{{ port_lookup_8080.meta.port
                                                 if (port_lookup_8080.meta.port is defined) and (port_lookup_8080.meta.port | trim | length > 0)
                                                 else '8090' }}"
            ```

        ??? variable string "`qbittorrent_role_web_port_lookup`"

            ```yaml
            # Type: string
            qbittorrent_role_web_port_lookup: "{{ lookup('role_var', '_web_port', role='qbittorrent') }}"
            ```

        ??? variable list "`qbittorrent_role_docker_ports_defaults`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_ports_defaults: 
              - "{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}:{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}"
              - "{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}:{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}/udp"
            ```

        ??? variable list "`qbittorrent_role_docker_ports_custom`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_ports_custom: []
            ```

        ##### Envs

        ??? variable dict "`qbittorrent_role_docker_envs_default`"

            ```yaml
            # Type: dict
            qbittorrent_role_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              TZ: "{{ tz }}"
              UMASK_SET: "002"
              S6_SERVICES_GRACETIME: "{{ (lookup('role_var', '_docker_stop_timeout', role='qbittorrent') | int * 1000) | string }}"
            ```

        ??? variable dict "`qbittorrent_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            qbittorrent_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`qbittorrent_role_docker_volumes_default`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_volumes_default: 
              - "{{ qbittorrent_role_paths_location }}:/config"
              - "{{ server_appdata_path }}/scripts:/scripts"
            ```

        ??? variable list "`qbittorrent_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable dict "`qbittorrent_role_docker_labels_default`"

            ```yaml
            # Type: dict
            qbittorrent_role_docker_labels_default: {}
            ```

        ??? variable dict "`qbittorrent_role_docker_labels_custom`"

            ```yaml
            # Type: dict
            qbittorrent_role_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`qbittorrent_role_docker_hostname`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_hostname: "{{ qbittorrent_name }}"
            ```

        ##### Networks

        ??? variable string "`qbittorrent_role_docker_networks_alias`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_networks_alias: "{{ qbittorrent_name }}"
            ```

        ??? variable list "`qbittorrent_role_docker_networks_default`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_networks_default: []
            ```

        ??? variable list "`qbittorrent_role_docker_networks_custom`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`qbittorrent_role_docker_restart_policy`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_restart_policy: unless-stopped
            ```

        ##### Stop Timeout

        ??? variable int "`qbittorrent_role_docker_stop_timeout`"

            ```yaml
            # Type: int
            qbittorrent_role_docker_stop_timeout: 900
            ```

        ##### State

        ??? variable string "`qbittorrent_role_docker_state`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_state: started
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`qbittorrent2_docker_container`"

            ```yaml
            # Type: string
            qbittorrent2_docker_container: "{{ qbittorrent_name }}"
            ```

        ##### Image

        ??? variable bool "`qbittorrent2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent2_docker_image_pull: true
            ```

        ??? variable string "`qbittorrent2_docker_image_repo`"

            ```yaml
            # Type: string
            qbittorrent2_docker_image_repo: "saltydk/qbittorrent"
            ```

        ??? variable string "`qbittorrent2_docker_image_tag`"

            ```yaml
            # Type: string
            qbittorrent2_docker_image_tag: "latest"
            ```

        ??? variable string "`qbittorrent2_docker_image`"

            ```yaml
            # Type: string
            qbittorrent2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='qbittorrent') }}:{{ lookup('role_var', '_docker_image_tag', role='qbittorrent') }}"
            ```

        ##### Ports

        ??? variable string "`qbittorrent2_docker_ports_56881`"

            ```yaml
            # Type: string
            qbittorrent2_docker_ports_56881: "{{ port_lookup_56881.meta.port
                                              if (port_lookup_56881.meta.port is defined) and (port_lookup_56881.meta.port | trim | length > 0)
                                              else '56881' }}"
            ```

        ??? variable string "`qbittorrent2_docker_ports_8080`"

            ```yaml
            # Type: string
            qbittorrent2_docker_ports_8080: "{{ port_lookup_8080.meta.port
                                             if (port_lookup_8080.meta.port is defined) and (port_lookup_8080.meta.port | trim | length > 0)
                                             else '8090' }}"
            ```

        ??? variable string "`qbittorrent2_web_port_lookup`"

            ```yaml
            # Type: string
            qbittorrent2_web_port_lookup: "{{ lookup('role_var', '_web_port', role='qbittorrent') }}"
            ```

        ??? variable list "`qbittorrent2_docker_ports_defaults`"

            ```yaml
            # Type: list
            qbittorrent2_docker_ports_defaults: 
              - "{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}:{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}"
              - "{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}:{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}/udp"
            ```

        ??? variable list "`qbittorrent2_docker_ports_custom`"

            ```yaml
            # Type: list
            qbittorrent2_docker_ports_custom: []
            ```

        ##### Envs

        ??? variable dict "`qbittorrent2_docker_envs_default`"

            ```yaml
            # Type: dict
            qbittorrent2_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              TZ: "{{ tz }}"
              UMASK_SET: "002"
              S6_SERVICES_GRACETIME: "{{ (lookup('role_var', '_docker_stop_timeout', role='qbittorrent') | int * 1000) | string }}"
            ```

        ??? variable dict "`qbittorrent2_docker_envs_custom`"

            ```yaml
            # Type: dict
            qbittorrent2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`qbittorrent2_docker_volumes_default`"

            ```yaml
            # Type: list
            qbittorrent2_docker_volumes_default: 
              - "{{ qbittorrent_role_paths_location }}:/config"
              - "{{ server_appdata_path }}/scripts:/scripts"
            ```

        ??? variable list "`qbittorrent2_docker_volumes_custom`"

            ```yaml
            # Type: list
            qbittorrent2_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable dict "`qbittorrent2_docker_labels_default`"

            ```yaml
            # Type: dict
            qbittorrent2_docker_labels_default: {}
            ```

        ??? variable dict "`qbittorrent2_docker_labels_custom`"

            ```yaml
            # Type: dict
            qbittorrent2_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`qbittorrent2_docker_hostname`"

            ```yaml
            # Type: string
            qbittorrent2_docker_hostname: "{{ qbittorrent_name }}"
            ```

        ##### Networks

        ??? variable string "`qbittorrent2_docker_networks_alias`"

            ```yaml
            # Type: string
            qbittorrent2_docker_networks_alias: "{{ qbittorrent_name }}"
            ```

        ??? variable list "`qbittorrent2_docker_networks_default`"

            ```yaml
            # Type: list
            qbittorrent2_docker_networks_default: []
            ```

        ??? variable list "`qbittorrent2_docker_networks_custom`"

            ```yaml
            # Type: list
            qbittorrent2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`qbittorrent2_docker_restart_policy`"

            ```yaml
            # Type: string
            qbittorrent2_docker_restart_policy: unless-stopped
            ```

        ##### Stop Timeout

        ??? variable int "`qbittorrent2_docker_stop_timeout`"

            ```yaml
            # Type: int
            qbittorrent2_docker_stop_timeout: 900
            ```

        ##### State

        ??? variable string "`qbittorrent2_docker_state`"

            ```yaml
            # Type: string
            qbittorrent2_docker_state: started
            ```

=== "Docker+"

    #### Additional Docker Options

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    === "Role-level"

        ##### Resource Limits

        ??? variable int "`qbittorrent_role_docker_blkio_weight`"

            ```yaml
            # Type: int
            qbittorrent_role_docker_blkio_weight:
            ```

        ??? variable int "`qbittorrent_role_docker_cpu_period`"

            ```yaml
            # Type: int
            qbittorrent_role_docker_cpu_period:
            ```

        ??? variable int "`qbittorrent_role_docker_cpu_quota`"

            ```yaml
            # Type: int
            qbittorrent_role_docker_cpu_quota:
            ```

        ??? variable int "`qbittorrent_role_docker_cpu_shares`"

            ```yaml
            # Type: int
            qbittorrent_role_docker_cpu_shares:
            ```

        ??? variable string "`qbittorrent_role_docker_cpus`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_cpus:
            ```

        ??? variable string "`qbittorrent_role_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_cpuset_cpus:
            ```

        ??? variable string "`qbittorrent_role_docker_cpuset_mems`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_cpuset_mems:
            ```

        ??? variable string "`qbittorrent_role_docker_kernel_memory`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_kernel_memory:
            ```

        ??? variable string "`qbittorrent_role_docker_memory`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_memory:
            ```

        ??? variable string "`qbittorrent_role_docker_memory_reservation`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_memory_reservation:
            ```

        ??? variable string "`qbittorrent_role_docker_memory_swap`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_memory_swap:
            ```

        ??? variable int "`qbittorrent_role_docker_memory_swappiness`"

            ```yaml
            # Type: int
            qbittorrent_role_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`qbittorrent_role_docker_cap_drop`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_cap_drop:
            ```

        ??? variable list "`qbittorrent_role_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_device_cgroup_rules:
            ```

        ??? variable list "`qbittorrent_role_docker_device_read_bps`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_device_read_bps:
            ```

        ??? variable list "`qbittorrent_role_docker_device_read_iops`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_device_read_iops:
            ```

        ??? variable list "`qbittorrent_role_docker_device_requests`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_device_requests:
            ```

        ??? variable list "`qbittorrent_role_docker_device_write_bps`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_device_write_bps:
            ```

        ??? variable list "`qbittorrent_role_docker_device_write_iops`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_device_write_iops:
            ```

        ??? variable list "`qbittorrent_role_docker_devices`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_devices:
            ```

        ??? variable string "`qbittorrent_role_docker_devices_default`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_devices_default:
            ```

        ??? variable bool "`qbittorrent_role_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent_role_docker_privileged:
            ```

        ??? variable list "`qbittorrent_role_docker_security_opts`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`qbittorrent_role_docker_dns_opts`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_dns_opts:
            ```

        ??? variable list "`qbittorrent_role_docker_dns_search_domains`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_dns_search_domains:
            ```

        ??? variable list "`qbittorrent_role_docker_dns_servers`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_dns_servers:
            ```

        ??? variable dict "`qbittorrent_role_docker_hosts`"

            ```yaml
            # Type: dict
            qbittorrent_role_docker_hosts:
            ```

        ??? variable string "`qbittorrent_role_docker_hosts_use_common`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_hosts_use_common:
            ```

        ??? variable string "`qbittorrent_role_docker_network_mode`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`qbittorrent_role_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent_role_docker_keep_volumes:
            ```

        ??? variable list "`qbittorrent_role_docker_mounts`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_mounts:
            ```

        ??? variable string "`qbittorrent_role_docker_volume_driver`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_volume_driver:
            ```

        ??? variable list "`qbittorrent_role_docker_volumes_from`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_volumes_from:
            ```

        ??? variable string "`qbittorrent_role_docker_volumes_global`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_volumes_global:
            ```

        ??? variable string "`qbittorrent_role_docker_working_dir`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`qbittorrent_role_docker_healthcheck`"

            ```yaml
            # Type: dict
            qbittorrent_role_docker_healthcheck:
            ```

        ??? variable bool "`qbittorrent_role_docker_init`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent_role_docker_init:
            ```

        ??? variable string "`qbittorrent_role_docker_log_driver`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_log_driver:
            ```

        ??? variable dict "`qbittorrent_role_docker_log_options`"

            ```yaml
            # Type: dict
            qbittorrent_role_docker_log_options:
            ```

        ??? variable bool "`qbittorrent_role_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent_role_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`qbittorrent_role_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent_role_docker_auto_remove:
            ```

        ??? variable list "`qbittorrent_role_docker_capabilities`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_capabilities:
            ```

        ??? variable string "`qbittorrent_role_docker_cgroup_parent`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_cgroup_parent:
            ```

        ??? variable string "`qbittorrent_role_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_cgroupns_mode:
            ```

        ??? variable bool "`qbittorrent_role_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent_role_docker_cleanup:
            ```

        ??? variable list "`qbittorrent_role_docker_commands`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_commands:
            ```

        ??? variable string "`qbittorrent_role_docker_create_timeout`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_create_timeout:
            ```

        ??? variable string "`qbittorrent_role_docker_domainname`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_domainname:
            ```

        ??? variable string "`qbittorrent_role_docker_entrypoint`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_entrypoint:
            ```

        ??? variable string "`qbittorrent_role_docker_env_file`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_env_file:
            ```

        ??? variable list "`qbittorrent_role_docker_exposed_ports`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_exposed_ports:
            ```

        ??? variable string "`qbittorrent_role_docker_force_kill`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_force_kill:
            ```

        ??? variable list "`qbittorrent_role_docker_groups`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_groups:
            ```

        ??? variable int "`qbittorrent_role_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            qbittorrent_role_docker_healthy_wait_timeout:
            ```

        ??? variable string "`qbittorrent_role_docker_ipc_mode`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_ipc_mode:
            ```

        ??? variable string "`qbittorrent_role_docker_kill_signal`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_kill_signal:
            ```

        ??? variable string "`qbittorrent_role_docker_labels_use_common`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_labels_use_common:
            ```

        ??? variable list "`qbittorrent_role_docker_links`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_links:
            ```

        ??? variable bool "`qbittorrent_role_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent_role_docker_oom_killer:
            ```

        ??? variable int "`qbittorrent_role_docker_oom_score_adj`"

            ```yaml
            # Type: int
            qbittorrent_role_docker_oom_score_adj:
            ```

        ??? variable bool "`qbittorrent_role_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent_role_docker_paused:
            ```

        ??? variable string "`qbittorrent_role_docker_pid_mode`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_pid_mode:
            ```

        ??? variable bool "`qbittorrent_role_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent_role_docker_read_only:
            ```

        ??? variable bool "`qbittorrent_role_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent_role_docker_recreate:
            ```

        ??? variable int "`qbittorrent_role_docker_restart_retries`"

            ```yaml
            # Type: int
            qbittorrent_role_docker_restart_retries:
            ```

        ??? variable string "`qbittorrent_role_docker_runtime`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_runtime:
            ```

        ??? variable string "`qbittorrent_role_docker_shm_size`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_shm_size:
            ```

        ??? variable dict "`qbittorrent_role_docker_storage_opts`"

            ```yaml
            # Type: dict
            qbittorrent_role_docker_storage_opts:
            ```

        ??? variable list "`qbittorrent_role_docker_sysctls`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_sysctls:
            ```

        ??? variable list "`qbittorrent_role_docker_tmpfs`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_tmpfs:
            ```

        ??? variable list "`qbittorrent_role_docker_ulimits`"

            ```yaml
            # Type: list
            qbittorrent_role_docker_ulimits:
            ```

        ??? variable string "`qbittorrent_role_docker_user`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_user:
            ```

        ??? variable string "`qbittorrent_role_docker_userns_mode`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_userns_mode:
            ```

        ??? variable string "`qbittorrent_role_docker_uts`"

            ```yaml
            # Type: string
            qbittorrent_role_docker_uts:
            ```

    === "Instance-level"

        ##### Resource Limits

        ??? variable int "`qbittorrent2_docker_blkio_weight`"

            ```yaml
            # Type: int
            qbittorrent2_docker_blkio_weight:
            ```

        ??? variable int "`qbittorrent2_docker_cpu_period`"

            ```yaml
            # Type: int
            qbittorrent2_docker_cpu_period:
            ```

        ??? variable int "`qbittorrent2_docker_cpu_quota`"

            ```yaml
            # Type: int
            qbittorrent2_docker_cpu_quota:
            ```

        ??? variable int "`qbittorrent2_docker_cpu_shares`"

            ```yaml
            # Type: int
            qbittorrent2_docker_cpu_shares:
            ```

        ??? variable string "`qbittorrent2_docker_cpus`"

            ```yaml
            # Type: string
            qbittorrent2_docker_cpus:
            ```

        ??? variable string "`qbittorrent2_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            qbittorrent2_docker_cpuset_cpus:
            ```

        ??? variable string "`qbittorrent2_docker_cpuset_mems`"

            ```yaml
            # Type: string
            qbittorrent2_docker_cpuset_mems:
            ```

        ??? variable string "`qbittorrent2_docker_kernel_memory`"

            ```yaml
            # Type: string
            qbittorrent2_docker_kernel_memory:
            ```

        ??? variable string "`qbittorrent2_docker_memory`"

            ```yaml
            # Type: string
            qbittorrent2_docker_memory:
            ```

        ??? variable string "`qbittorrent2_docker_memory_reservation`"

            ```yaml
            # Type: string
            qbittorrent2_docker_memory_reservation:
            ```

        ??? variable string "`qbittorrent2_docker_memory_swap`"

            ```yaml
            # Type: string
            qbittorrent2_docker_memory_swap:
            ```

        ??? variable int "`qbittorrent2_docker_memory_swappiness`"

            ```yaml
            # Type: int
            qbittorrent2_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`qbittorrent2_docker_cap_drop`"

            ```yaml
            # Type: list
            qbittorrent2_docker_cap_drop:
            ```

        ??? variable list "`qbittorrent2_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            qbittorrent2_docker_device_cgroup_rules:
            ```

        ??? variable list "`qbittorrent2_docker_device_read_bps`"

            ```yaml
            # Type: list
            qbittorrent2_docker_device_read_bps:
            ```

        ??? variable list "`qbittorrent2_docker_device_read_iops`"

            ```yaml
            # Type: list
            qbittorrent2_docker_device_read_iops:
            ```

        ??? variable list "`qbittorrent2_docker_device_requests`"

            ```yaml
            # Type: list
            qbittorrent2_docker_device_requests:
            ```

        ??? variable list "`qbittorrent2_docker_device_write_bps`"

            ```yaml
            # Type: list
            qbittorrent2_docker_device_write_bps:
            ```

        ??? variable list "`qbittorrent2_docker_device_write_iops`"

            ```yaml
            # Type: list
            qbittorrent2_docker_device_write_iops:
            ```

        ??? variable list "`qbittorrent2_docker_devices`"

            ```yaml
            # Type: list
            qbittorrent2_docker_devices:
            ```

        ??? variable string "`qbittorrent2_docker_devices_default`"

            ```yaml
            # Type: string
            qbittorrent2_docker_devices_default:
            ```

        ??? variable bool "`qbittorrent2_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent2_docker_privileged:
            ```

        ??? variable list "`qbittorrent2_docker_security_opts`"

            ```yaml
            # Type: list
            qbittorrent2_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`qbittorrent2_docker_dns_opts`"

            ```yaml
            # Type: list
            qbittorrent2_docker_dns_opts:
            ```

        ??? variable list "`qbittorrent2_docker_dns_search_domains`"

            ```yaml
            # Type: list
            qbittorrent2_docker_dns_search_domains:
            ```

        ??? variable list "`qbittorrent2_docker_dns_servers`"

            ```yaml
            # Type: list
            qbittorrent2_docker_dns_servers:
            ```

        ??? variable dict "`qbittorrent2_docker_hosts`"

            ```yaml
            # Type: dict
            qbittorrent2_docker_hosts:
            ```

        ??? variable string "`qbittorrent2_docker_hosts_use_common`"

            ```yaml
            # Type: string
            qbittorrent2_docker_hosts_use_common:
            ```

        ??? variable string "`qbittorrent2_docker_network_mode`"

            ```yaml
            # Type: string
            qbittorrent2_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`qbittorrent2_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent2_docker_keep_volumes:
            ```

        ??? variable list "`qbittorrent2_docker_mounts`"

            ```yaml
            # Type: list
            qbittorrent2_docker_mounts:
            ```

        ??? variable string "`qbittorrent2_docker_volume_driver`"

            ```yaml
            # Type: string
            qbittorrent2_docker_volume_driver:
            ```

        ??? variable list "`qbittorrent2_docker_volumes_from`"

            ```yaml
            # Type: list
            qbittorrent2_docker_volumes_from:
            ```

        ??? variable string "`qbittorrent2_docker_volumes_global`"

            ```yaml
            # Type: string
            qbittorrent2_docker_volumes_global:
            ```

        ??? variable string "`qbittorrent2_docker_working_dir`"

            ```yaml
            # Type: string
            qbittorrent2_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`qbittorrent2_docker_healthcheck`"

            ```yaml
            # Type: dict
            qbittorrent2_docker_healthcheck:
            ```

        ??? variable bool "`qbittorrent2_docker_init`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent2_docker_init:
            ```

        ??? variable string "`qbittorrent2_docker_log_driver`"

            ```yaml
            # Type: string
            qbittorrent2_docker_log_driver:
            ```

        ??? variable dict "`qbittorrent2_docker_log_options`"

            ```yaml
            # Type: dict
            qbittorrent2_docker_log_options:
            ```

        ??? variable bool "`qbittorrent2_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent2_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`qbittorrent2_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent2_docker_auto_remove:
            ```

        ??? variable list "`qbittorrent2_docker_capabilities`"

            ```yaml
            # Type: list
            qbittorrent2_docker_capabilities:
            ```

        ??? variable string "`qbittorrent2_docker_cgroup_parent`"

            ```yaml
            # Type: string
            qbittorrent2_docker_cgroup_parent:
            ```

        ??? variable string "`qbittorrent2_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            qbittorrent2_docker_cgroupns_mode:
            ```

        ??? variable bool "`qbittorrent2_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent2_docker_cleanup:
            ```

        ??? variable list "`qbittorrent2_docker_commands`"

            ```yaml
            # Type: list
            qbittorrent2_docker_commands:
            ```

        ??? variable string "`qbittorrent2_docker_create_timeout`"

            ```yaml
            # Type: string
            qbittorrent2_docker_create_timeout:
            ```

        ??? variable string "`qbittorrent2_docker_domainname`"

            ```yaml
            # Type: string
            qbittorrent2_docker_domainname:
            ```

        ??? variable string "`qbittorrent2_docker_entrypoint`"

            ```yaml
            # Type: string
            qbittorrent2_docker_entrypoint:
            ```

        ??? variable string "`qbittorrent2_docker_env_file`"

            ```yaml
            # Type: string
            qbittorrent2_docker_env_file:
            ```

        ??? variable list "`qbittorrent2_docker_exposed_ports`"

            ```yaml
            # Type: list
            qbittorrent2_docker_exposed_ports:
            ```

        ??? variable string "`qbittorrent2_docker_force_kill`"

            ```yaml
            # Type: string
            qbittorrent2_docker_force_kill:
            ```

        ??? variable list "`qbittorrent2_docker_groups`"

            ```yaml
            # Type: list
            qbittorrent2_docker_groups:
            ```

        ??? variable int "`qbittorrent2_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            qbittorrent2_docker_healthy_wait_timeout:
            ```

        ??? variable string "`qbittorrent2_docker_ipc_mode`"

            ```yaml
            # Type: string
            qbittorrent2_docker_ipc_mode:
            ```

        ??? variable string "`qbittorrent2_docker_kill_signal`"

            ```yaml
            # Type: string
            qbittorrent2_docker_kill_signal:
            ```

        ??? variable string "`qbittorrent2_docker_labels_use_common`"

            ```yaml
            # Type: string
            qbittorrent2_docker_labels_use_common:
            ```

        ??? variable list "`qbittorrent2_docker_links`"

            ```yaml
            # Type: list
            qbittorrent2_docker_links:
            ```

        ??? variable bool "`qbittorrent2_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent2_docker_oom_killer:
            ```

        ??? variable int "`qbittorrent2_docker_oom_score_adj`"

            ```yaml
            # Type: int
            qbittorrent2_docker_oom_score_adj:
            ```

        ??? variable bool "`qbittorrent2_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent2_docker_paused:
            ```

        ??? variable string "`qbittorrent2_docker_pid_mode`"

            ```yaml
            # Type: string
            qbittorrent2_docker_pid_mode:
            ```

        ??? variable bool "`qbittorrent2_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent2_docker_read_only:
            ```

        ??? variable bool "`qbittorrent2_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            qbittorrent2_docker_recreate:
            ```

        ??? variable int "`qbittorrent2_docker_restart_retries`"

            ```yaml
            # Type: int
            qbittorrent2_docker_restart_retries:
            ```

        ??? variable string "`qbittorrent2_docker_runtime`"

            ```yaml
            # Type: string
            qbittorrent2_docker_runtime:
            ```

        ??? variable string "`qbittorrent2_docker_shm_size`"

            ```yaml
            # Type: string
            qbittorrent2_docker_shm_size:
            ```

        ??? variable dict "`qbittorrent2_docker_storage_opts`"

            ```yaml
            # Type: dict
            qbittorrent2_docker_storage_opts:
            ```

        ??? variable list "`qbittorrent2_docker_sysctls`"

            ```yaml
            # Type: list
            qbittorrent2_docker_sysctls:
            ```

        ??? variable list "`qbittorrent2_docker_tmpfs`"

            ```yaml
            # Type: list
            qbittorrent2_docker_tmpfs:
            ```

        ??? variable list "`qbittorrent2_docker_ulimits`"

            ```yaml
            # Type: list
            qbittorrent2_docker_ulimits:
            ```

        ??? variable string "`qbittorrent2_docker_user`"

            ```yaml
            # Type: string
            qbittorrent2_docker_user:
            ```

        ??? variable string "`qbittorrent2_docker_userns_mode`"

            ```yaml
            # Type: string
            qbittorrent2_docker_userns_mode:
            ```

        ??? variable string "`qbittorrent2_docker_uts`"

            ```yaml
            # Type: string
            qbittorrent2_docker_uts:
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`qbittorrent_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            qbittorrent_role_autoheal_enabled: true
            ```

        ??? variable string "`qbittorrent_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            qbittorrent_role_depends_on: ""
            ```

        ??? variable string "`qbittorrent_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            qbittorrent_role_depends_on_delay: "0"
            ```

        ??? variable string "`qbittorrent_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            qbittorrent_role_depends_on_healthchecks:
            ```

        ??? variable bool "`qbittorrent_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            qbittorrent_role_diun_enabled: true
            ```

        ??? variable bool "`qbittorrent_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            qbittorrent_role_dns_enabled: true
            ```

        ??? variable bool "`qbittorrent_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            qbittorrent_role_docker_controller: true
            ```

        ??? variable bool "`qbittorrent_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            qbittorrent_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`qbittorrent_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            qbittorrent_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`qbittorrent_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            qbittorrent_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`qbittorrent_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            qbittorrent_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`qbittorrent_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            qbittorrent_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`qbittorrent_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            qbittorrent_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`qbittorrent_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            qbittorrent_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`qbittorrent_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            qbittorrent_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                qbittorrent_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "qbittorrent2.{{ user.domain }}"
                  - "qbittorrent.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`qbittorrent_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            qbittorrent_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                qbittorrent_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'qbittorrent2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`qbittorrent_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            qbittorrent_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `qbittorrent2`):

        ??? variable bool "`qbittorrent2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            qbittorrent2_autoheal_enabled: true
            ```

        ??? variable string "`qbittorrent2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            qbittorrent2_depends_on: ""
            ```

        ??? variable string "`qbittorrent2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            qbittorrent2_depends_on_delay: "0"
            ```

        ??? variable string "`qbittorrent2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            qbittorrent2_depends_on_healthchecks:
            ```

        ??? variable bool "`qbittorrent2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            qbittorrent2_diun_enabled: true
            ```

        ??? variable bool "`qbittorrent2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            qbittorrent2_dns_enabled: true
            ```

        ??? variable bool "`qbittorrent2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            qbittorrent2_docker_controller: true
            ```

        ??? variable bool "`qbittorrent2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            qbittorrent2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`qbittorrent2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            qbittorrent2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`qbittorrent2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            qbittorrent2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`qbittorrent2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            qbittorrent2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`qbittorrent2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            qbittorrent2_traefik_robot_enabled: true
            ```

        ??? variable bool "`qbittorrent2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            qbittorrent2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`qbittorrent2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            qbittorrent2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`qbittorrent2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            qbittorrent2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                qbittorrent2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "qbittorrent2.{{ user.domain }}"
                  - "qbittorrent.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`qbittorrent2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            qbittorrent2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                qbittorrent2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'qbittorrent2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`qbittorrent2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            qbittorrent2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
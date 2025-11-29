---
icon: material/docker
hide:
  - tags
tags:
  - qbittorrent
---

# qBittorrent

## Overview

[qBittorrent](https://www.qbittorrent.org/) is a free, open-source, cross-platform BitTorrent client written in C++ and Qt, designed as a reliable and ad-free alternative to other clients like µTorrent.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.qbittorrent.org/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/qbittorrent/qBittorrent/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/qbittorrent/qBittorrent){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/saltydk/qbittorrent){: .header-icons }|

---

!!! abstract directions "Saltbox Setup Process"

    <div data-search-exclude>

    <div>

    Opting out of torrents?

    <div>

    [**Skip to Sonarr**:material-fast-forward:](sonarr.md){ .md-button }

    </div>

    </div>

    <div>

    Opting for another BitTorrent client?

    <div>

    [**Explore alternatives**:material-shuffle-variant:](index.md#download-client){ .md-button }

    [**Skip to Jackett**:material-fast-forward:](jackett.md){ .md-button }

    </div>

    </div>

    </div>

## Deployment

```sh
sb install qbittorrent
```

## Usage

To access qBittorrent, visit <https://qbittorrent.iYOUR_DOMAIN_NAMEi>

## Basics

1.  Log in using the username/password you specified in `accounts.yml`

1.  **OPTIONALLY** go to `Options` -> `Web UI` and set a new username and a strong password.

    ![Authentication Section Screenshot](../images/community/qbit_auth.png)

1.  Under `Options` -> `Connection`, set the port to 56881.

    ![Port Section Screenshot](../images/community/qbit_port.png)

1.  Under `Options` -> `Downloads`, set the following;

    - Save files to location: `/mnt/unionfs/downloads/torrents/qbittorrent/completed/`

    - Keep incomplete torrents in: `/mnt/unionfs/downloads/torrents/qbittorrent/incoming/`

    - Copy .torrent files to: `/mnt/unionfs/downloads/torrents/qbittorrent/torrents/`

    - Copy .torrent files for finished downloads to: `/mnt/unionfs/downloads/torrents/qbittorrent/torrents/`

    - Additionally you can set monitored folder to: `/mnt/unionfs/downloads/torrents/qbittorrent/watched/`

    - tick `Run external program on torrent completion` and paste this into the box: `/usr/bin/unrar x -r "%F/." "%F/"`

    ![Hard Disk Section Screenshot](../images/community/qbit_hdd.png)

!!! warning

    Make sure to choose a strong username/password combination because by default qBittorrent's Web API is completely exposed to the internet!

    If someone guesses your qBit's credentials, they can, among other things, steal your tracker passkeys and delete torrents (data included).

    If you don't need the API endpoints exposed, you can disable them using the [inventory system](../saltbox/inventory/index.md) with

    ```yaml
    qbittorrent_traefik_api_enabled: false
    ```

    and by rerunning the `qbittorrent` tag.

!!! note

    if you're using private trackers be sure to go to `Options` -> `BitTorrent` and uncheck everything in Privacy section.

## Next

<div class="directions-menu" markdown>

Are you setting Saltbox up for the first time?

<div markdown>

[**Continue to Jackett**:material-forward:](jackett.md){ .md-button }

</div>

</div>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `qbittorrent_instances`.

    ```yaml { .sb-show-on-unchecked title="Applies to all instances of qbittorrent:" }
    qbittorrent_role_web_subdomain: "custom"
    ```

    ```yaml { .sb-show-on-checked title="Applies to a specific instance (e.g., `qbittorrent2`):" }
    qbittorrent2_web_subdomain: "custom2"
    ```

<label class="md-button md-button--stretch" for="sb-checkbox--var-level">
   <input type="checkbox" id="sb-checkbox--var-level"><span class="sb-show-on-unchecked">Show instance-level variables</span><span class="sb-show-on-checked">Show role-level variables</span>
</label>

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `qbittorrent_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `qbittorrent_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`qbittorrent_instances`"

        ```yaml
        # Type: list
        qbittorrent_instances: ["qbittorrent"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            qbittorrent_instances: ["qbittorrent", "qbittorrent2"]
            ```

=== "Settings"

    ??? variable bool "`qbittorrent_role_host_install`{ .sb-show-on-unchecked }`qbittorrent2_host_install`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_host_install: false
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_host_install: false
        ```

    ??? variable string "`qbittorrent_role_webui_custom_headers_enabled`{ .sb-show-on-unchecked }`qbittorrent2_webui_custom_headers_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_webui_custom_headers_enabled: "{{ 'true' if lookup('role_var', '_themepark_enabled', role='qbittorrent') and global_themepark_plugin_enabled else 'false' }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_webui_custom_headers_enabled: "{{ 'true' if lookup('role_var', '_themepark_enabled', role='qbittorrent') and global_themepark_plugin_enabled else 'false' }}"
        ```

    ??? variable string "`qbittorrent_role_webui_custom_headers_default`{ .sb-show-on-unchecked }`qbittorrent2_webui_custom_headers_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_webui_custom_headers_default: "{{ (qbittorrent_role_themepark_headers if lookup('role_var', '_themepark_enabled', role='qbittorrent') and global_themepark_plugin_enabled else '') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_webui_custom_headers_default: "{{ (qbittorrent_role_themepark_headers if lookup('role_var', '_themepark_enabled', role='qbittorrent') and global_themepark_plugin_enabled else '') }}"
        ```

    ??? variable string "`qbittorrent_role_webui_custom_headers_custom`{ .sb-show-on-unchecked }`qbittorrent2_webui_custom_headers_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_webui_custom_headers_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_webui_custom_headers_custom: ""
        ```

    ??? variable string "`qbittorrent_role_torrent_content_remove_option`{ .sb-show-on-unchecked }`qbittorrent2_torrent_content_remove_option`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Options are: Delete or MoveToTrash
        # Type: string
        qbittorrent_role_torrent_content_remove_option: "Delete"
        ```

        ```yaml { .sb-show-on-checked }
        # Options are: Delete or MoveToTrash
        # Type: string
        qbittorrent2_torrent_content_remove_option: "Delete"
        ```

=== "Host Install"

    ??? variable string "`qbittorrent_role_host_branch`{ .sb-show-on-unchecked }`qbittorrent2_host_branch`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Options are: libtorrent1 (latest), libtorrent2 (latest) or legacy (4.3.9)
        # Type: string
        qbittorrent_role_host_branch: libtorrent1
        ```

        ```yaml { .sb-show-on-checked }
        # Options are: libtorrent1 (latest), libtorrent2 (latest) or legacy (4.3.9)
        # Type: string
        qbittorrent2_host_branch: libtorrent1
        ```

    ??? variable string "`qbittorrent_role_host_specific_version`{ .sb-show-on-unchecked }`qbittorrent2_host_specific_version`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Example being "release-4.4.5_v1.2.18"
        # If this is set then the above branch logic is ignored
        # Type: string
        qbittorrent_role_host_specific_version: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Example being "release-4.4.5_v1.2.18"
        # If this is set then the above branch logic is ignored
        # Type: string
        qbittorrent2_host_specific_version: ""
        ```

    ??? variable string "`qbittorrent_role_host_download_endpoint`{ .sb-show-on-unchecked }`qbittorrent2_host_download_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Lookup variables
        # Type: string
        qbittorrent_role_host_download_endpoint: "{{ 'https://github.com/userdocs/qbittorrent-nox-static/releases/download/'
                                                  if lookup('role_var', '_host_branch', role='qbittorrent') != 'legacy'
                                                  else 'https://github.com/userdocs/qbittorrent-nox-static-legacy/releases/download/' }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Lookup variables
        # Type: string
        qbittorrent2_host_download_endpoint: "{{ 'https://github.com/userdocs/qbittorrent-nox-static/releases/download/'
                                              if lookup('role_var', '_host_branch', role='qbittorrent') != 'legacy'
                                              else 'https://github.com/userdocs/qbittorrent-nox-static-legacy/releases/download/' }}"
        ```

    ??? variable string "`qbittorrent_role_host_download_url`{ .sb-show-on-unchecked }`qbittorrent2_host_download_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_host_download_url: "{{ lookup('role_var', '_host_download_endpoint', role='qbittorrent') }}{{ lookup('role_var', '_host_specific_version', role='qbittorrent')
                                                                                                                    if (lookup('role_var', '_host_specific_version', role='qbittorrent') | length > 0)
                                                                                                                    else qbittorrent_release_version.stdout }}/x86_64-qbittorrent-nox"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_host_download_url: "{{ lookup('role_var', '_host_download_endpoint', role='qbittorrent') }}{{ lookup('role_var', '_host_specific_version', role='qbittorrent')
                                                                                                                if (lookup('role_var', '_host_specific_version', role='qbittorrent') | length > 0)
                                                                                                                else qbittorrent_release_version.stdout }}/x86_64-qbittorrent-nox"
        ```

    ??? variable string "`qbittorrent_role_host_release_url`{ .sb-show-on-unchecked }`qbittorrent2_host_release_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_host_release_url: "{{ 'https://github.com/userdocs/qbittorrent-nox-static/releases/latest/download/dependency-version.json'
                                            if lookup('role_var', '_host_branch', role='qbittorrent') != 'legacy'
                                            else 'https://github.com/userdocs/qbittorrent-nox-static-legacy/releases/latest/download/dependency-version.json' }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_host_release_url: "{{ 'https://github.com/userdocs/qbittorrent-nox-static/releases/latest/download/dependency-version.json'
                                        if lookup('role_var', '_host_branch', role='qbittorrent') != 'legacy'
                                        else 'https://github.com/userdocs/qbittorrent-nox-static-legacy/releases/latest/download/dependency-version.json' }}"
        ```

    ??? variable string "`qbittorrent_role_host_lookup_libtorrent1`{ .sb-show-on-unchecked }`qbittorrent2_host_lookup_libtorrent1`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_host_lookup_libtorrent1: 'release-\(.qbittorrent)_v\(.libtorrent_1_2)'
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_host_lookup_libtorrent1: 'release-\(.qbittorrent)_v\(.libtorrent_1_2)'
        ```

    ??? variable string "`qbittorrent_role_host_lookup_libtorrent2`{ .sb-show-on-unchecked }`qbittorrent2_host_lookup_libtorrent2`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_host_lookup_libtorrent2: 'release-\(.qbittorrent)_v\(.libtorrent_2_0)'
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_host_lookup_libtorrent2: 'release-\(.qbittorrent)_v\(.libtorrent_2_0)'
        ```

    ??? variable string "`qbittorrent_role_host_release_lookup`{ .sb-show-on-unchecked }`qbittorrent2_host_release_lookup`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_host_release_lookup: "{{ qbittorrent_role_host_lookup_libtorrent2
                                               if lookup('role_var', '_host_branch', role='qbittorrent') == 'libtorrent2'
                                               else qbittorrent_role_host_lookup_libtorrent1 }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_host_release_lookup: "{{ qbittorrent_role_host_lookup_libtorrent2
                                           if lookup('role_var', '_host_branch', role='qbittorrent') == 'libtorrent2'
                                           else qbittorrent_role_host_lookup_libtorrent1 }}"
        ```

    ??? variable string "`qbittorrent_role_host_version`{ .sb-show-on-unchecked }`qbittorrent2_host_version`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_host_version: |
          curl -sL {{ lookup('role_var', '_host_release_url', role='qbittorrent') }} | jq -r '. | "{{ lookup('role_var', '_host_release_lookup', role='qbittorrent') }}"'
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_host_version: |
          curl -sL {{ lookup('role_var', '_host_release_url', role='qbittorrent') }} | jq -r '. | "{{ lookup('role_var', '_host_release_lookup', role='qbittorrent') }}"'
        ```

    ??? variable string "`qbittorrent_role_service_name`{ .sb-show-on-unchecked }`qbittorrent2_service_name`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_service_name: "saltbox_managed_{{ qbittorrent_name }}.service"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_service_name: "saltbox_managed_{{ qbittorrent_name }}.service"
        ```

    ??? variable string "`qbittorrent_role_service_after`{ .sb-show-on-unchecked }`qbittorrent2_service_after`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_service_after: "network-online.target docker.service"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_service_after: "network-online.target docker.service"
        ```

    ??? variable string "`qbittorrent_role_service_requires`{ .sb-show-on-unchecked }`qbittorrent2_service_requires`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_service_requires: "network-online.target docker.service"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_service_requires: "network-online.target docker.service"
        ```

    ??? variable string "`qbittorrent_role_service_wants`{ .sb-show-on-unchecked }`qbittorrent2_service_wants`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_service_wants: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_service_wants: ""
        ```

    ??? variable string "`qbittorrent_role_service_partof`{ .sb-show-on-unchecked }`qbittorrent2_service_partof`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_service_partof: "docker.service"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_service_partof: "docker.service"
        ```

=== "Paths"

    ??? variable string "`qbittorrent_role_paths_folder`{ .sb-show-on-unchecked }`qbittorrent2_paths_folder`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_paths_folder: "{{ qbittorrent_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_paths_folder: "{{ qbittorrent_name }}"
        ```

    ??? variable string "`qbittorrent_role_paths_location`{ .sb-show-on-unchecked }`qbittorrent2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_paths_location: "{{ server_appdata_path }}/{{ qbittorrent_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_paths_location: "{{ server_appdata_path }}/{{ qbittorrent_role_paths_folder }}"
        ```

    ??? variable string "`qbittorrent_role_paths_downloads_location`{ .sb-show-on-unchecked }`qbittorrent2_paths_downloads_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_paths_downloads_location: "{{ downloads_torrents_path }}/{{ qbittorrent_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_paths_downloads_location: "{{ downloads_torrents_path }}/{{ qbittorrent_role_paths_folder }}"
        ```

    ??? variable string "`qbittorrent_role_paths_conf`{ .sb-show-on-unchecked }`qbittorrent2_paths_conf`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_paths_conf: "{{ qbittorrent_role_paths_location }}/qBittorrent/qBittorrent.conf"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_paths_conf: "{{ qbittorrent_role_paths_location }}/qBittorrent/qBittorrent.conf"
        ```

=== "Web"

    ??? variable string "`qbittorrent_role_web_subdomain`{ .sb-show-on-unchecked }`qbittorrent2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_web_subdomain: "{{ qbittorrent_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_web_subdomain: "{{ qbittorrent_name }}"
        ```

    ??? variable string "`qbittorrent_role_web_domain`{ .sb-show-on-unchecked }`qbittorrent2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`qbittorrent_role_web_port`{ .sb-show-on-unchecked }`qbittorrent2_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_web_port: "8080"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_web_port: "8080"
        ```

    ??? variable string "`qbittorrent_role_web_url`{ .sb-show-on-unchecked }`qbittorrent2_web_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='qbittorrent') + '.' + lookup('role_var', '_web_domain', role='qbittorrent')
                                   if (lookup('role_var', '_web_subdomain', role='qbittorrent') | length > 0)
                                   else lookup('role_var', '_web_domain', role='qbittorrent')) }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='qbittorrent') + '.' + lookup('role_var', '_web_domain', role='qbittorrent')
                               if (lookup('role_var', '_web_subdomain', role='qbittorrent') | length > 0)
                               else lookup('role_var', '_web_domain', role='qbittorrent')) }}"
        ```

=== "DNS"

    ??? variable string "`qbittorrent_role_dns_record`{ .sb-show-on-unchecked }`qbittorrent2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='qbittorrent') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='qbittorrent') }}"
        ```

    ??? variable string "`qbittorrent_role_dns_zone`{ .sb-show-on-unchecked }`qbittorrent2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='qbittorrent') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_dns_zone: "{{ lookup('role_var', '_web_domain', role='qbittorrent') }}"
        ```

    ??? variable bool "`qbittorrent_role_dns_proxy`{ .sb-show-on-unchecked }`qbittorrent2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_dns_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`qbittorrent_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`qbittorrent2_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`qbittorrent_role_traefik_middleware_default`{ .sb-show-on-unchecked }`qbittorrent2_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                         + (',themepark-' + qbittorrent_name
                                                           if (lookup('role_var', '_themepark_enabled', role='qbittorrent') and global_themepark_plugin_enabled)
                                                           else '') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_traefik_middleware_default: "{{ traefik_default_middleware
                                                     + (',themepark-' + qbittorrent_name
                                                       if (lookup('role_var', '_themepark_enabled', role='qbittorrent') and global_themepark_plugin_enabled)
                                                       else '') }}"
        ```

    ??? variable string "`qbittorrent_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`qbittorrent2_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_traefik_middleware_custom: ""
        ```

    ??? variable string "`qbittorrent_role_traefik_certresolver`{ .sb-show-on-unchecked }`qbittorrent2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`qbittorrent_role_traefik_enabled`{ .sb-show-on-unchecked }`qbittorrent2_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_traefik_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_traefik_enabled: true
        ```

    ??? variable bool "`qbittorrent_role_traefik_api_enabled`{ .sb-show-on-unchecked }`qbittorrent2_traefik_api_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_traefik_api_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_traefik_api_enabled: true
        ```

    ??? variable string "`qbittorrent_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`qbittorrent2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/command`) || PathPrefix(`/query`) || PathPrefix(`/login`) || PathPrefix(`/sync`)"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/command`) || PathPrefix(`/query`) || PathPrefix(`/login`) || PathPrefix(`/sync`)"
        ```

=== "Theme"

    ??? variable bool "`qbittorrent_role_themepark_enabled`{ .sb-show-on-unchecked }`qbittorrent2_themepark_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        qbittorrent_role_themepark_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        qbittorrent2_themepark_enabled: false
        ```

    ??? variable string "`qbittorrent_role_themepark_app`{ .sb-show-on-unchecked }`qbittorrent2_themepark_app`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_themepark_app: "qbittorrent"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_themepark_app: "qbittorrent"
        ```

    ??? variable string "`qbittorrent_role_themepark_theme`{ .sb-show-on-unchecked }`qbittorrent2_themepark_theme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_themepark_theme: "{{ global_themepark_theme }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_themepark_theme: "{{ global_themepark_theme }}"
        ```

    ??? variable string "`qbittorrent_role_themepark_domain`{ .sb-show-on-unchecked }`qbittorrent2_themepark_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_themepark_domain: "{{ global_themepark_domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_themepark_domain: "{{ global_themepark_domain }}"
        ```

    ??? variable list "`qbittorrent_role_themepark_addons`{ .sb-show-on-unchecked }`qbittorrent2_themepark_addons`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_themepark_addons: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_themepark_addons: []
        ```

    ??? variable string "`qbittorrent_role_themepark_headers`{ .sb-show-on-unchecked }`qbittorrent2_themepark_headers`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_themepark_headers: "\"content-security-policy: default-src 'self'; style-src 'self' 'unsafe-inline' theme-park.dev raw.githubusercontent.com use.fontawesome.com; img-src 'self' theme-park.dev raw.githubusercontent.com data:; script-src 'self' 'unsafe-inline'; object-src 'none'; form-action 'self'; frame-ancestors 'self'; font-src use.fontawesome.com;\""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_themepark_headers: "\"content-security-policy: default-src 'self'; style-src 'self' 'unsafe-inline' theme-park.dev raw.githubusercontent.com use.fontawesome.com; img-src 'self' theme-park.dev raw.githubusercontent.com data:; script-src 'self' 'unsafe-inline'; object-src 'none'; form-action 'self'; frame-ancestors 'self'; font-src use.fontawesome.com;\""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`qbittorrent_role_docker_container`{ .sb-show-on-unchecked }`qbittorrent2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_container: "{{ qbittorrent_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_container: "{{ qbittorrent_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`qbittorrent_role_docker_image_pull`{ .sb-show-on-unchecked }`qbittorrent2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_docker_image_pull: true
        ```

    ??? variable string "`qbittorrent_role_docker_image_repo`{ .sb-show-on-unchecked }`qbittorrent2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_image_repo: "saltydk/qbittorrent"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_image_repo: "saltydk/qbittorrent"
        ```

    ??? variable string "`qbittorrent_role_docker_image_tag`{ .sb-show-on-unchecked }`qbittorrent2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_image_tag: "latest"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_image_tag: "latest"
        ```

    ??? variable string "`qbittorrent_role_docker_image`{ .sb-show-on-unchecked }`qbittorrent2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='qbittorrent') }}:{{ lookup('role_var', '_docker_image_tag', role='qbittorrent') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='qbittorrent') }}:{{ lookup('role_var', '_docker_image_tag', role='qbittorrent') }}"
        ```

    <h5>Ports</h5>

    ??? variable string "`qbittorrent_role_docker_ports_56881`{ .sb-show-on-unchecked }`qbittorrent2_docker_ports_56881`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_ports_56881: "{{ port_lookup_56881.meta.port
                                              if (port_lookup_56881.meta.port is defined) and (port_lookup_56881.meta.port | trim | length > 0)
                                              else '56881' }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_ports_56881: "{{ port_lookup_56881.meta.port
                                          if (port_lookup_56881.meta.port is defined) and (port_lookup_56881.meta.port | trim | length > 0)
                                          else '56881' }}"
        ```

    ??? variable string "`qbittorrent_role_docker_ports_8080`{ .sb-show-on-unchecked }`qbittorrent2_docker_ports_8080`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_ports_8080: "{{ port_lookup_8080.meta.port
                                             if (port_lookup_8080.meta.port is defined) and (port_lookup_8080.meta.port | trim | length > 0)
                                             else '8090' }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_ports_8080: "{{ port_lookup_8080.meta.port
                                         if (port_lookup_8080.meta.port is defined) and (port_lookup_8080.meta.port | trim | length > 0)
                                         else '8090' }}"
        ```

    ??? variable string "`qbittorrent_role_web_port_lookup`{ .sb-show-on-unchecked }`qbittorrent2_web_port_lookup`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_web_port_lookup: "{{ lookup('role_var', '_web_port', role='qbittorrent') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_web_port_lookup: "{{ lookup('role_var', '_web_port', role='qbittorrent') }}"
        ```

    ??? variable list "`qbittorrent_role_docker_ports_default`{ .sb-show-on-unchecked }`qbittorrent2_docker_ports_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_ports_default:
          - "{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}:{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}"
          - "{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}:{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}/udp"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_ports_default:
          - "{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}:{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}"
          - "{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}:{{ lookup('role_var', '_docker_ports_56881', role='qbittorrent') }}/udp"
        ```

    ??? variable list "`qbittorrent_role_docker_ports_custom`{ .sb-show-on-unchecked }`qbittorrent2_docker_ports_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_ports_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    ??? variable dict "`qbittorrent_role_docker_envs_default`{ .sb-show-on-unchecked }`qbittorrent2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qbittorrent_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          UMASK_SET: "002"
          S6_SERVICES_GRACETIME: "{{ (lookup('role_var', '_docker_stop_timeout', role='qbittorrent') | int * 1000) | string }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qbittorrent2_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          UMASK_SET: "002"
          S6_SERVICES_GRACETIME: "{{ (lookup('role_var', '_docker_stop_timeout', role='qbittorrent') | int * 1000) | string }}"
        ```

    ??? variable dict "`qbittorrent_role_docker_envs_custom`{ .sb-show-on-unchecked }`qbittorrent2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qbittorrent_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qbittorrent2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`qbittorrent_role_docker_volumes_default`{ .sb-show-on-unchecked }`qbittorrent2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_volumes_default:
          - "{{ qbittorrent_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_volumes_default:
          - "{{ qbittorrent_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
        ```

    ??? variable list "`qbittorrent_role_docker_volumes_custom`{ .sb-show-on-unchecked }`qbittorrent2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable dict "`qbittorrent_role_docker_labels_default`{ .sb-show-on-unchecked }`qbittorrent2_docker_labels_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qbittorrent_role_docker_labels_default: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qbittorrent2_docker_labels_default: {}
        ```

    ??? variable dict "`qbittorrent_role_docker_labels_custom`{ .sb-show-on-unchecked }`qbittorrent2_docker_labels_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qbittorrent_role_docker_labels_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qbittorrent2_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`qbittorrent_role_docker_hostname`{ .sb-show-on-unchecked }`qbittorrent2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_hostname: "{{ qbittorrent_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_hostname: "{{ qbittorrent_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`qbittorrent_role_docker_networks_alias`{ .sb-show-on-unchecked }`qbittorrent2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_networks_alias: "{{ qbittorrent_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_networks_alias: "{{ qbittorrent_name }}"
        ```

    ??? variable list "`qbittorrent_role_docker_networks_default`{ .sb-show-on-unchecked }`qbittorrent2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_networks_default: []
        ```

    ??? variable list "`qbittorrent_role_docker_networks_custom`{ .sb-show-on-unchecked }`qbittorrent2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`qbittorrent_role_docker_restart_policy`{ .sb-show-on-unchecked }`qbittorrent2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_restart_policy: unless-stopped
        ```

    <h5>Stop Timeout</h5>

    ??? variable int "`qbittorrent_role_docker_stop_timeout`{ .sb-show-on-unchecked }`qbittorrent2_docker_stop_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrent_role_docker_stop_timeout: 900
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrent2_docker_stop_timeout: 900
        ```

    <h5>State</h5>

    ??? variable string "`qbittorrent_role_docker_state`{ .sb-show-on-unchecked }`qbittorrent2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`qbittorrent_role_docker_blkio_weight`{ .sb-show-on-unchecked }`qbittorrent2_docker_blkio_weight`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrent_role_docker_blkio_weight:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrent2_docker_blkio_weight:
        ```

    ??? variable int "`qbittorrent_role_docker_cpu_period`{ .sb-show-on-unchecked }`qbittorrent2_docker_cpu_period`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrent_role_docker_cpu_period:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrent2_docker_cpu_period:
        ```

    ??? variable int "`qbittorrent_role_docker_cpu_quota`{ .sb-show-on-unchecked }`qbittorrent2_docker_cpu_quota`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrent_role_docker_cpu_quota:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrent2_docker_cpu_quota:
        ```

    ??? variable int "`qbittorrent_role_docker_cpu_shares`{ .sb-show-on-unchecked }`qbittorrent2_docker_cpu_shares`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrent_role_docker_cpu_shares:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrent2_docker_cpu_shares:
        ```

    ??? variable string "`qbittorrent_role_docker_cpus`{ .sb-show-on-unchecked }`qbittorrent2_docker_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_cpus:
        ```

    ??? variable string "`qbittorrent_role_docker_cpuset_cpus`{ .sb-show-on-unchecked }`qbittorrent2_docker_cpuset_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_cpuset_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_cpuset_cpus:
        ```

    ??? variable string "`qbittorrent_role_docker_cpuset_mems`{ .sb-show-on-unchecked }`qbittorrent2_docker_cpuset_mems`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_cpuset_mems:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_cpuset_mems:
        ```

    ??? variable string "`qbittorrent_role_docker_kernel_memory`{ .sb-show-on-unchecked }`qbittorrent2_docker_kernel_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_kernel_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_kernel_memory:
        ```

    ??? variable string "`qbittorrent_role_docker_memory`{ .sb-show-on-unchecked }`qbittorrent2_docker_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_memory:
        ```

    ??? variable string "`qbittorrent_role_docker_memory_reservation`{ .sb-show-on-unchecked }`qbittorrent2_docker_memory_reservation`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_memory_reservation:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_memory_reservation:
        ```

    ??? variable string "`qbittorrent_role_docker_memory_swap`{ .sb-show-on-unchecked }`qbittorrent2_docker_memory_swap`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_memory_swap:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_memory_swap:
        ```

    ??? variable int "`qbittorrent_role_docker_memory_swappiness`{ .sb-show-on-unchecked }`qbittorrent2_docker_memory_swappiness`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrent_role_docker_memory_swappiness:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrent2_docker_memory_swappiness:
        ```

    ??? variable string "`qbittorrent_role_docker_shm_size`{ .sb-show-on-unchecked }`qbittorrent2_docker_shm_size`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_shm_size:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`qbittorrent_role_docker_cap_drop`{ .sb-show-on-unchecked }`qbittorrent2_docker_cap_drop`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_cap_drop:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_cap_drop:
        ```

    ??? variable string "`qbittorrent_role_docker_cgroupns_mode`{ .sb-show-on-unchecked }`qbittorrent2_docker_cgroupns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_cgroupns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_cgroupns_mode:
        ```

    ??? variable list "`qbittorrent_role_docker_device_cgroup_rules`{ .sb-show-on-unchecked }`qbittorrent2_docker_device_cgroup_rules`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_device_cgroup_rules:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_device_cgroup_rules:
        ```

    ??? variable list "`qbittorrent_role_docker_device_read_bps`{ .sb-show-on-unchecked }`qbittorrent2_docker_device_read_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_device_read_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_device_read_bps:
        ```

    ??? variable list "`qbittorrent_role_docker_device_read_iops`{ .sb-show-on-unchecked }`qbittorrent2_docker_device_read_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_device_read_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_device_read_iops:
        ```

    ??? variable list "`qbittorrent_role_docker_device_requests`{ .sb-show-on-unchecked }`qbittorrent2_docker_device_requests`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_device_requests:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_device_requests:
        ```

    ??? variable list "`qbittorrent_role_docker_device_write_bps`{ .sb-show-on-unchecked }`qbittorrent2_docker_device_write_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_device_write_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_device_write_bps:
        ```

    ??? variable list "`qbittorrent_role_docker_device_write_iops`{ .sb-show-on-unchecked }`qbittorrent2_docker_device_write_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_device_write_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_device_write_iops:
        ```

    ??? variable list "`qbittorrent_role_docker_devices`{ .sb-show-on-unchecked }`qbittorrent2_docker_devices`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_devices:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_devices:
        ```

    ??? variable string "`qbittorrent_role_docker_devices_default`{ .sb-show-on-unchecked }`qbittorrent2_docker_devices_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_devices_default:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_devices_default:
        ```

    ??? variable list "`qbittorrent_role_docker_groups`{ .sb-show-on-unchecked }`qbittorrent2_docker_groups`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_groups:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_groups:
        ```

    ??? variable bool "`qbittorrent_role_docker_privileged`{ .sb-show-on-unchecked }`qbittorrent2_docker_privileged`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_docker_privileged:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_docker_privileged:
        ```

    ??? variable list "`qbittorrent_role_docker_security_opts`{ .sb-show-on-unchecked }`qbittorrent2_docker_security_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_security_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_security_opts:
        ```

    ??? variable string "`qbittorrent_role_docker_user`{ .sb-show-on-unchecked }`qbittorrent2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_user:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_user:
        ```

    ??? variable string "`qbittorrent_role_docker_userns_mode`{ .sb-show-on-unchecked }`qbittorrent2_docker_userns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_userns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`qbittorrent_role_docker_dns_opts`{ .sb-show-on-unchecked }`qbittorrent2_docker_dns_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_dns_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_dns_opts:
        ```

    ??? variable list "`qbittorrent_role_docker_dns_search_domains`{ .sb-show-on-unchecked }`qbittorrent2_docker_dns_search_domains`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_dns_search_domains:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_dns_search_domains:
        ```

    ??? variable list "`qbittorrent_role_docker_dns_servers`{ .sb-show-on-unchecked }`qbittorrent2_docker_dns_servers`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_dns_servers:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_dns_servers:
        ```

    ??? variable string "`qbittorrent_role_docker_domainname`{ .sb-show-on-unchecked }`qbittorrent2_docker_domainname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_domainname:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_domainname:
        ```

    ??? variable list "`qbittorrent_role_docker_exposed_ports`{ .sb-show-on-unchecked }`qbittorrent2_docker_exposed_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_exposed_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_exposed_ports:
        ```

    ??? variable dict "`qbittorrent_role_docker_hosts`{ .sb-show-on-unchecked }`qbittorrent2_docker_hosts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qbittorrent_role_docker_hosts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qbittorrent2_docker_hosts:
        ```

    ??? variable bool "`qbittorrent_role_docker_hosts_use_common`{ .sb-show-on-unchecked }`qbittorrent2_docker_hosts_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_docker_hosts_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_docker_hosts_use_common:
        ```

    ??? variable string "`qbittorrent_role_docker_ipc_mode`{ .sb-show-on-unchecked }`qbittorrent2_docker_ipc_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_ipc_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_ipc_mode:
        ```

    ??? variable list "`qbittorrent_role_docker_links`{ .sb-show-on-unchecked }`qbittorrent2_docker_links`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_links:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_links:
        ```

    ??? variable string "`qbittorrent_role_docker_network_mode`{ .sb-show-on-unchecked }`qbittorrent2_docker_network_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_network_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_network_mode:
        ```

    ??? variable string "`qbittorrent_role_docker_pid_mode`{ .sb-show-on-unchecked }`qbittorrent2_docker_pid_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_pid_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_pid_mode:
        ```

    ??? variable string "`qbittorrent_role_docker_uts`{ .sb-show-on-unchecked }`qbittorrent2_docker_uts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_uts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`qbittorrent_role_docker_keep_volumes`{ .sb-show-on-unchecked }`qbittorrent2_docker_keep_volumes`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_docker_keep_volumes:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_docker_keep_volumes:
        ```

    ??? variable list "`qbittorrent_role_docker_mounts`{ .sb-show-on-unchecked }`qbittorrent2_docker_mounts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_mounts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_mounts:
        ```

    ??? variable dict "`qbittorrent_role_docker_storage_opts`{ .sb-show-on-unchecked }`qbittorrent2_docker_storage_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qbittorrent_role_docker_storage_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qbittorrent2_docker_storage_opts:
        ```

    ??? variable list "`qbittorrent_role_docker_tmpfs`{ .sb-show-on-unchecked }`qbittorrent2_docker_tmpfs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_tmpfs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_tmpfs:
        ```

    ??? variable string "`qbittorrent_role_docker_volume_driver`{ .sb-show-on-unchecked }`qbittorrent2_docker_volume_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_volume_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_volume_driver:
        ```

    ??? variable list "`qbittorrent_role_docker_volumes_from`{ .sb-show-on-unchecked }`qbittorrent2_docker_volumes_from`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_volumes_from:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_volumes_from:
        ```

    ??? variable bool "`qbittorrent_role_docker_volumes_global`{ .sb-show-on-unchecked }`qbittorrent2_docker_volumes_global`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_docker_volumes_global:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_docker_volumes_global:
        ```

    ??? variable string "`qbittorrent_role_docker_working_dir`{ .sb-show-on-unchecked }`qbittorrent2_docker_working_dir`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_working_dir:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`qbittorrent_role_docker_auto_remove`{ .sb-show-on-unchecked }`qbittorrent2_docker_auto_remove`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_docker_auto_remove:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_docker_auto_remove:
        ```

    ??? variable bool "`qbittorrent_role_docker_cleanup`{ .sb-show-on-unchecked }`qbittorrent2_docker_cleanup`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_docker_cleanup:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_docker_cleanup:
        ```

    ??? variable string "`qbittorrent_role_docker_force_kill`{ .sb-show-on-unchecked }`qbittorrent2_docker_force_kill`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_force_kill:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_force_kill:
        ```

    ??? variable dict "`qbittorrent_role_docker_healthcheck`{ .sb-show-on-unchecked }`qbittorrent2_docker_healthcheck`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qbittorrent_role_docker_healthcheck:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qbittorrent2_docker_healthcheck:
        ```

    ??? variable int "`qbittorrent_role_docker_healthy_wait_timeout`{ .sb-show-on-unchecked }`qbittorrent2_docker_healthy_wait_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrent_role_docker_healthy_wait_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrent2_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`qbittorrent_role_docker_init`{ .sb-show-on-unchecked }`qbittorrent2_docker_init`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_docker_init:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_docker_init:
        ```

    ??? variable string "`qbittorrent_role_docker_kill_signal`{ .sb-show-on-unchecked }`qbittorrent2_docker_kill_signal`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_kill_signal:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_kill_signal:
        ```

    ??? variable string "`qbittorrent_role_docker_log_driver`{ .sb-show-on-unchecked }`qbittorrent2_docker_log_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_log_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_log_driver:
        ```

    ??? variable dict "`qbittorrent_role_docker_log_options`{ .sb-show-on-unchecked }`qbittorrent2_docker_log_options`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qbittorrent_role_docker_log_options:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qbittorrent2_docker_log_options:
        ```

    ??? variable bool "`qbittorrent_role_docker_oom_killer`{ .sb-show-on-unchecked }`qbittorrent2_docker_oom_killer`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_docker_oom_killer:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_docker_oom_killer:
        ```

    ??? variable int "`qbittorrent_role_docker_oom_score_adj`{ .sb-show-on-unchecked }`qbittorrent2_docker_oom_score_adj`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrent_role_docker_oom_score_adj:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrent2_docker_oom_score_adj:
        ```

    ??? variable bool "`qbittorrent_role_docker_output_logs`{ .sb-show-on-unchecked }`qbittorrent2_docker_output_logs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_docker_output_logs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_docker_output_logs:
        ```

    ??? variable bool "`qbittorrent_role_docker_paused`{ .sb-show-on-unchecked }`qbittorrent2_docker_paused`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_docker_paused:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_docker_paused:
        ```

    ??? variable bool "`qbittorrent_role_docker_recreate`{ .sb-show-on-unchecked }`qbittorrent2_docker_recreate`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_docker_recreate:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_docker_recreate:
        ```

    ??? variable int "`qbittorrent_role_docker_restart_retries`{ .sb-show-on-unchecked }`qbittorrent2_docker_restart_retries`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrent_role_docker_restart_retries:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrent2_docker_restart_retries:
        ```

    <h5>Other Options</h5>

    ??? variable list "`qbittorrent_role_docker_capabilities`{ .sb-show-on-unchecked }`qbittorrent2_docker_capabilities`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_capabilities:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_capabilities:
        ```

    ??? variable string "`qbittorrent_role_docker_cgroup_parent`{ .sb-show-on-unchecked }`qbittorrent2_docker_cgroup_parent`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_cgroup_parent:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_cgroup_parent:
        ```

    ??? variable list "`qbittorrent_role_docker_commands`{ .sb-show-on-unchecked }`qbittorrent2_docker_commands`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_commands:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_commands:
        ```

    ??? variable int "`qbittorrent_role_docker_create_timeout`{ .sb-show-on-unchecked }`qbittorrent2_docker_create_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        qbittorrent_role_docker_create_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        qbittorrent2_docker_create_timeout:
        ```

    ??? variable string "`qbittorrent_role_docker_entrypoint`{ .sb-show-on-unchecked }`qbittorrent2_docker_entrypoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_entrypoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_entrypoint:
        ```

    ??? variable string "`qbittorrent_role_docker_env_file`{ .sb-show-on-unchecked }`qbittorrent2_docker_env_file`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_env_file:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_env_file:
        ```

    ??? variable bool "`qbittorrent_role_docker_labels_use_common`{ .sb-show-on-unchecked }`qbittorrent2_docker_labels_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_docker_labels_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_docker_labels_use_common:
        ```

    ??? variable bool "`qbittorrent_role_docker_read_only`{ .sb-show-on-unchecked }`qbittorrent2_docker_read_only`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_docker_read_only:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_docker_read_only:
        ```

    ??? variable string "`qbittorrent_role_docker_runtime`{ .sb-show-on-unchecked }`qbittorrent2_docker_runtime`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_runtime:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_runtime:
        ```

    ??? variable list "`qbittorrent_role_docker_sysctls`{ .sb-show-on-unchecked }`qbittorrent2_docker_sysctls`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_sysctls:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_sysctls:
        ```

    ??? variable list "`qbittorrent_role_docker_ulimits`{ .sb-show-on-unchecked }`qbittorrent2_docker_ulimits`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qbittorrent_role_docker_ulimits:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qbittorrent2_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`qbittorrent_role_autoheal_enabled`{ .sb-show-on-unchecked }`qbittorrent2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        qbittorrent_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        qbittorrent2_autoheal_enabled: true
        ```

    ??? variable string "`qbittorrent_role_depends_on`{ .sb-show-on-unchecked }`qbittorrent2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        qbittorrent_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        qbittorrent2_depends_on: ""
        ```

    ??? variable string "`qbittorrent_role_depends_on_delay`{ .sb-show-on-unchecked }`qbittorrent2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        qbittorrent_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        qbittorrent2_depends_on_delay: "0"
        ```

    ??? variable string "`qbittorrent_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`qbittorrent2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        qbittorrent_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        qbittorrent2_depends_on_healthchecks:
        ```

    ??? variable bool "`qbittorrent_role_diun_enabled`{ .sb-show-on-unchecked }`qbittorrent2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        qbittorrent_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        qbittorrent2_diun_enabled: true
        ```

    ??? variable bool "`qbittorrent_role_dns_enabled`{ .sb-show-on-unchecked }`qbittorrent2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        qbittorrent_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        qbittorrent2_dns_enabled: true
        ```

    ??? variable bool "`qbittorrent_role_docker_controller`{ .sb-show-on-unchecked }`qbittorrent2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        qbittorrent_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        qbittorrent2_docker_controller: true
        ```

    ??? variable string "`qbittorrent_role_docker_image_repo`{ .sb-show-on-unchecked }`qbittorrent2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_image_repo:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_image_repo:
        ```

    ??? variable string "`qbittorrent_role_docker_image_tag`{ .sb-show-on-unchecked }`qbittorrent2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_docker_image_tag:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_docker_image_tag:
        ```

    ??? variable string "`qbittorrent_role_docker_ports_56881`{ .sb-show-on-unchecked }`qbittorrent2_docker_ports_56881`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        qbittorrent_role_docker_ports_56881:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        qbittorrent2_docker_ports_56881:
        ```

    ??? variable string "`qbittorrent_role_docker_stop_timeout`{ .sb-show-on-unchecked }`qbittorrent2_docker_stop_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        qbittorrent_role_docker_stop_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        qbittorrent2_docker_stop_timeout:
        ```

    ??? variable bool "`qbittorrent_role_docker_volumes_download`{ .sb-show-on-unchecked }`qbittorrent2_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_docker_volumes_download:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_docker_volumes_download:
        ```

    ??? variable string "`qbittorrent_role_host_branch`{ .sb-show-on-unchecked }`qbittorrent2_host_branch`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_host_branch:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_host_branch:
        ```

    ??? variable string "`qbittorrent_role_host_download_endpoint`{ .sb-show-on-unchecked }`qbittorrent2_host_download_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_host_download_endpoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_host_download_endpoint:
        ```

    ??? variable string "`qbittorrent_role_host_release_lookup`{ .sb-show-on-unchecked }`qbittorrent2_host_release_lookup`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_host_release_lookup:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_host_release_lookup:
        ```

    ??? variable string "`qbittorrent_role_host_release_url`{ .sb-show-on-unchecked }`qbittorrent2_host_release_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_host_release_url:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_host_release_url:
        ```

    ??? variable string "`qbittorrent_role_host_specific_version`{ .sb-show-on-unchecked }`qbittorrent2_host_specific_version`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_host_specific_version:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_host_specific_version:
        ```

    ??? variable string "`qbittorrent_role_themepark_addons`{ .sb-show-on-unchecked }`qbittorrent2_themepark_addons`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_themepark_addons:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_themepark_addons:
        ```

    ??? variable string "`qbittorrent_role_themepark_app`{ .sb-show-on-unchecked }`qbittorrent2_themepark_app`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_themepark_app:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_themepark_app:
        ```

    ??? variable bool "`qbittorrent_role_themepark_enabled`{ .sb-show-on-unchecked }`qbittorrent2_themepark_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_themepark_enabled:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_themepark_enabled:
        ```

    ??? variable string "`qbittorrent_role_themepark_theme`{ .sb-show-on-unchecked }`qbittorrent2_themepark_theme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_themepark_theme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_themepark_theme:
        ```

    ??? variable dict/omit "`qbittorrent_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`qbittorrent2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        qbittorrent_role_traefik_api_endpoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        qbittorrent2_traefik_api_endpoint:
        ```

    ??? variable string "`qbittorrent_role_traefik_api_middleware`{ .sb-show-on-unchecked }`qbittorrent2_traefik_api_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_traefik_api_middleware:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_traefik_api_middleware:
        ```

    ??? variable string "`qbittorrent_role_traefik_api_middleware_http`{ .sb-show-on-unchecked }`qbittorrent2_traefik_api_middleware_http`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_traefik_api_middleware_http:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_traefik_api_middleware_http:
        ```

    ??? variable bool "`qbittorrent_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`qbittorrent2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        qbittorrent_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        qbittorrent2_traefik_autodetect_enabled: false
        ```

    ??? variable string "`qbittorrent_role_traefik_certresolver`{ .sb-show-on-unchecked }`qbittorrent2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_traefik_certresolver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_traefik_certresolver:
        ```

    ??? variable bool "`qbittorrent_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`qbittorrent2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        qbittorrent_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        qbittorrent2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`qbittorrent_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`qbittorrent2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        qbittorrent_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        qbittorrent2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`qbittorrent_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`qbittorrent2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        qbittorrent_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        qbittorrent2_traefik_gzip_enabled: false
        ```

    ??? variable string "`qbittorrent_role_traefik_middleware_http`{ .sb-show-on-unchecked }`qbittorrent2_traefik_middleware_http`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_traefik_middleware_http:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_traefik_middleware_http:
        ```

    ??? variable bool "`qbittorrent_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`qbittorrent2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`qbittorrent_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`qbittorrent2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qbittorrent_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qbittorrent2_traefik_middleware_http_insecure:
        ```

    ??? variable string "`qbittorrent_role_traefik_priority`{ .sb-show-on-unchecked }`qbittorrent2_traefik_priority`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_traefik_priority:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_traefik_priority:
        ```

    ??? variable bool "`qbittorrent_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`qbittorrent2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        qbittorrent_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        qbittorrent2_traefik_robot_enabled: true
        ```

    ??? variable bool "`qbittorrent_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`qbittorrent2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        qbittorrent_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        qbittorrent2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`qbittorrent_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`qbittorrent2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        qbittorrent_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        qbittorrent2_traefik_wildcard_enabled: true
        ```

    ??? variable string "`qbittorrent_role_web_domain`{ .sb-show-on-unchecked }`qbittorrent2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_web_domain:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_web_domain:
        ```

    ??? variable list "`qbittorrent_role_web_fqdn_override`{ .sb-show-on-unchecked }`qbittorrent2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        qbittorrent_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        qbittorrent2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            qbittorrent_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "qbittorrent2.{{ user.domain }}"
              - "qbittorrent.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


        !!! example sb-show-on-checked "Example Override"

            ```yaml
            qbittorrent2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "qbittorrent2.{{ user.domain }}"
              - "qbittorrent.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`qbittorrent_role_web_host_override`{ .sb-show-on-unchecked }`qbittorrent2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        qbittorrent_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        qbittorrent2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            qbittorrent_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'qbittorrent2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


        !!! example sb-show-on-checked "Example Override"

            ```yaml
            qbittorrent2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'qbittorrent2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`qbittorrent_role_web_http_port`{ .sb-show-on-unchecked }`qbittorrent2_web_http_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        qbittorrent_role_web_http_port:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        qbittorrent2_web_http_port:
        ```

    ??? variable string "`qbittorrent_role_web_http_scheme`{ .sb-show-on-unchecked }`qbittorrent2_web_http_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string ("http"/"https")
        qbittorrent_role_web_http_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string ("http"/"https")
        qbittorrent2_web_http_scheme:
        ```

    ??? variable dict/omit "`qbittorrent_role_web_http_serverstransport`{ .sb-show-on-unchecked }`qbittorrent2_web_http_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        qbittorrent_role_web_http_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        qbittorrent2_web_http_serverstransport:
        ```

    ??? variable string "`qbittorrent_role_web_port`{ .sb-show-on-unchecked }`qbittorrent2_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        qbittorrent_role_web_port:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        qbittorrent2_web_port:
        ```

    ??? variable string "`qbittorrent_role_web_scheme`{ .sb-show-on-unchecked }`qbittorrent2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        qbittorrent_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        qbittorrent2_web_scheme:
        ```

    ??? variable dict/omit "`qbittorrent_role_web_serverstransport`{ .sb-show-on-unchecked }`qbittorrent2_web_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        qbittorrent_role_web_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        qbittorrent2_web_serverstransport:
        ```

    ??? variable string "`qbittorrent_role_web_subdomain`{ .sb-show-on-unchecked }`qbittorrent2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qbittorrent_role_web_subdomain:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qbittorrent2_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
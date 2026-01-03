---
icon: material/docker
hide:
  - tags
tags:
  - emby
---

# Emby

## Overview

[linuxserver/emby](https://docs.linuxserver.io/images/docker-emby) is a Docker container image for Emby.

> [Emby](https://emby.media) is a media server designed to organize, play, and stream audio and video to a variety of devices. [:material-bookshelf:](https://support.emby.media/support/home) [:fontawesome-solid-people-group:](https://emby.media/community)

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://docs.linuxserver.io/general/container-customization){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/linuxserver/emby/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://linuxserver.io/discord){ .md-button .md-button--stretch }

</div>

---

## Configuration

See [Adding a Subdomain](../reference/subdomain.md) on how to add the subdomain `emby` to your DNS provider.

_Note: You can skip this step if you are using [Cloudflare](../reference/domain.md#__tabbed_1_3) with Saltbox._

## Deployment

```shell
sb install emby
```

## Usage

Visit <https://emby.iYOUR_DOMAIN_NAMEi>.

## Basics

### Initial Setup

1.  Visit <https://emby.iYOUR_DOMAIN_NAMEi>.

1.  Select your **preferred display language**. Click **Next**.

    ![](../images/emby/emby-welcome-english.png)

1.  **Type** the following and click **Next**:

    -   **Username:** _The username you wwant to use to log into Emby_

    -   **New Password:** _A strong password you'll use to log into Emby_

    -   **New Password Confirm:** _That same password again_

    -   **Emby connect username or email address**: _your [Emby Connect username](https://emby.media/connect)_ (important)

    ![](../images/emby/emby-firstuser.png)

1.  Confirm the message by clicking **Got It**.

    ![](../images/emby/emby-added.png)

1.  **Confirm** the link in your email.

    ![](../images/emby/emby-confirm-link.png)

    ![](../images/emby/emby-link-accepted.png)

1.  Skip the adding of the libraries. Click **Next**.

    ![](../images/emby/emby-setup-media-libs.png)

1.  Select your **Preferred Metadata Language** and **Country** (_`English` and `United States` are recommended_) and click **Next**.

    ![](../images/emby/emby-preferred-metadata.png)

1.  Uncheck **Enable automatic port mapping**. Click **Next**.

    ![](../images/emby/emby-config-remote-access.png)

1.  **Check** to accept the terms. Click **Next**.

    ![](../images/emby/emby-terms.png)

1.  Click **Finish**.

    ![](../images/emby/emby-done.png)

1.  You will now be taken to the **Dashboard** view.

### Settings

1. Go to **Settings**.

1.  Go to **Transcoding**.

    ![](../images/emby/emby-transcoding.png)

1.  Under **Enable hardware acceleration when available**, select **Advanced**.

    ![](../images/emby/emby-transcoding-advanced.png)

1.  Under **Transcoding temporary path**, type in or choose `/transcode`.

    ![](../images/emby/emby-transcoding-hardware-path.png)

1.  Click **Save**.

### Libraries

In this section, we will add two libraries: one for Movies and one for TV Shows.

#### Add Movie Library

1.  Go to **Settings**.

1.  Go to **Library**.

    ![](../images/emby/emby-setup-media-libs.png)

1.  Click **+ New Library**.

1.  Under **Content type**, select **Movies**.

    ![](../images/emby/emby-new-library.png)

    ![](../images/emby/emby-new-library-movie-name.png)

1.  Click **+** next to **Folders**.

1.  Type in or choose `/mnt/unionfs/Media/Movies`. Click **OK**.

    _Note: These [paths](../saltbox/basics/paths.md) are for the standard library setup. If you have [customized](../reference/customizing-plex-libs.md) it, use those paths instead._

    ![](../images/emby/emby-new-library-movie-path.png)

1.  Click **OK** once more.

#### Add TV Shows Library

1.  Go to **Settings**.

1.  Go to **Library**.

    ![](../images/emby/emby-setup-media-libs.png)

1.  Click **+ New Library**.

1.  Under **Content type**, select **TV shows**.

    ![](../images/emby/emby-new-library.png)

    ![](../images/emby/emby-new-library-tv-name.png)

1.  Click **+** next to **Folders**.

1.  Type in or choose `/mnt/unionfs/Media/TV`. Click **OK**.

    _Note: These [paths](../saltbox/basics/paths.md) are for the standard library setup. If you have [customized](../reference/customizing-plex-libs.md) it, use those paths instead._

    ![](../images/emby/emby-new-library-tv-path.png)

1.  Click **OK** once more.

### API Key

Instructions below will guide you through creating an API Key for a specific app.

1.  Click the **Settings** icon.

1.  Under **Advanced**, click **API Keys**.

    ![](../images/emby/emby-new-api-key.png)

1.  Click **+ New API Key**.

    ![](../images/emby/emby-new-api-key-name.png)

1.  Fill in an **App name** (e.g. Ombi) and click **OK**.

1.  You have now have created an **Api Key** for your app.

    ![](../images/emby/emby-new-api-show.png)

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults<label class="sb-toggle--override-scope md-annotation__index" title="Supports multiple instances! Click to toggle override level"><input type="checkbox" name="scope" hidden/></label>

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables.<span title="View override details for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  **This role supports multiple instances via `emby_instances`.**

    !!! example sb-show-on-unchecked "Example override"

        ```yaml
        emby_role_web_subdomain: "custom"
        ```

        <div class="result" markdown>

        Applies to all instances of emby.

        </div>

    !!! example sb-show-on-checked "Example override"

        ```yaml
        emby2_web_subdomain: "custom2"
        ```

        <div class="result" markdown>

        Applies to the instance named `emby2`.

        </div>

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `emby_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `emby_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`emby_instances`"

        ```yaml
        # Type: list
        emby_instances: ["emby"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            emby_instances: ["emby", "emby2"]
            ```

=== "Settings"

    ??? variable string "`emby_role_config_settings_is_behind_proxy`{ .sb-show-on-unchecked }`emby2_config_settings_is_behind_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_config_settings_is_behind_proxy: "true"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_config_settings_is_behind_proxy: "true"
        ```

    ??? variable string "`emby_role_config_settings_wan_ddns`{ .sb-show-on-unchecked }`emby2_config_settings_wan_ddns`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_config_settings_wan_ddns: "{{ lookup('role_var', '_web_subdomain', role='emby') }}.{{ lookup('role_var', '_web_domain', role='emby') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_config_settings_wan_ddns: "{{ lookup('role_var', '_web_subdomain', role='emby') }}.{{ lookup('role_var', '_web_domain', role='emby') }}"
        ```

    ??? variable string "`emby_role_config_settings_public_port`{ .sb-show-on-unchecked }`emby2_config_settings_public_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_config_settings_public_port: "80"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_config_settings_public_port: "80"
        ```

    ??? variable string "`emby_role_config_settings_public_https_port`{ .sb-show-on-unchecked }`emby2_config_settings_public_https_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_config_settings_public_https_port: "443"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_config_settings_public_https_port: "443"
        ```

    ??? variable string "`emby_role_config_settings_enable_https`{ .sb-show-on-unchecked }`emby2_config_settings_enable_https`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_config_settings_enable_https: "true"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_config_settings_enable_https: "true"
        ```

    ??? variable string "`emby_role_config_settings_require_https`{ .sb-show-on-unchecked }`emby2_config_settings_require_https`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_config_settings_require_https: "false"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_config_settings_require_https: "false"
        ```

    ??? variable string "`emby_role_config_settings_enable_upnp`{ .sb-show-on-unchecked }`emby2_config_settings_enable_upnp`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_config_settings_enable_upnp: "false"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_config_settings_enable_upnp: "false"
        ```

    ??? variable string "`emby_role_config_settings_database_cache_size_mb`{ .sb-show-on-unchecked }`emby2_config_settings_database_cache_size_mb`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_config_settings_database_cache_size_mb: "1024"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_config_settings_database_cache_size_mb: "1024"
        ```

=== "Web"

    ??? variable string "`emby_role_web_subdomain`{ .sb-show-on-unchecked }`emby2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_web_subdomain: "{{ emby_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_web_subdomain: "{{ emby_name }}"
        ```

    ??? variable string "`emby_role_web_domain`{ .sb-show-on-unchecked }`emby2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`emby_role_web_port`{ .sb-show-on-unchecked }`emby2_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_web_port: "8096"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_web_port: "8096"
        ```

    ??? variable string "`emby_role_web_url`{ .sb-show-on-unchecked }`emby2_web_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='emby') + '.' + lookup('role_var', '_web_domain', role='emby')
                            if (lookup('role_var', '_web_subdomain', role='emby') | length > 0)
                            else lookup('role_var', '_web_domain', role='emby')) }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='emby') + '.' + lookup('role_var', '_web_domain', role='emby')
                        if (lookup('role_var', '_web_subdomain', role='emby') | length > 0)
                        else lookup('role_var', '_web_domain', role='emby')) }}"
        ```

=== "DNS"

    ??? variable string "`emby_role_dns_record`{ .sb-show-on-unchecked }`emby2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='emby') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='emby') }}"
        ```

    ??? variable string "`emby_role_dns_zone`{ .sb-show-on-unchecked }`emby2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='emby') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_dns_zone: "{{ lookup('role_var', '_web_domain', role='emby') }}"
        ```

    ??? variable bool "`emby_role_dns_proxy`{ .sb-show-on-unchecked }`emby2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_dns_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`emby_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`emby2_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_traefik_sso_middleware: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_traefik_sso_middleware: ""
        ```

    ??? variable string "`emby_role_traefik_middleware_default`{ .sb-show-on-unchecked }`emby2_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_traefik_middleware_default: "{{ traefik_default_middleware
                                                  + (',themepark-' + emby_name
                                                    if (lookup('role_var', '_themepark_enabled', role='emby') and global_themepark_plugin_enabled)
                                                    else '') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_traefik_middleware_default: "{{ traefik_default_middleware
                                              + (',themepark-' + emby_name
                                                if (lookup('role_var', '_themepark_enabled', role='emby') and global_themepark_plugin_enabled)
                                                else '') }}"
        ```

    ??? variable string "`emby_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`emby2_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_traefik_middleware_custom: ""
        ```

    ??? variable string "`emby_role_traefik_certresolver`{ .sb-show-on-unchecked }`emby2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`emby_role_traefik_enabled`{ .sb-show-on-unchecked }`emby2_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_traefik_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_traefik_enabled: true
        ```

    ??? variable bool "`emby_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`emby2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_traefik_gzip_enabled: false
        ```

    ??? variable bool "`emby_role_traefik_api_enabled`{ .sb-show-on-unchecked }`emby2_traefik_api_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_traefik_api_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_traefik_api_enabled: false
        ```

    ??? variable string "`emby_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`emby2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_traefik_api_endpoint: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_traefik_api_endpoint: ""
        ```

=== "Theme"

    ??? variable bool "`emby_role_themepark_enabled`{ .sb-show-on-unchecked }`emby2_themepark_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        emby_role_themepark_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        emby2_themepark_enabled: false
        ```

    ??? variable string "`emby_role_themepark_app`{ .sb-show-on-unchecked }`emby2_themepark_app`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_themepark_app: "emby"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_themepark_app: "emby"
        ```

    ??? variable string "`emby_role_themepark_theme`{ .sb-show-on-unchecked }`emby2_themepark_theme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_themepark_theme: "{{ global_themepark_theme }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_themepark_theme: "{{ global_themepark_theme }}"
        ```

    ??? variable string "`emby_role_themepark_domain`{ .sb-show-on-unchecked }`emby2_themepark_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_themepark_domain: "{{ global_themepark_domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_themepark_domain: "{{ global_themepark_domain }}"
        ```

    ??? variable list "`emby_role_themepark_addons`{ .sb-show-on-unchecked }`emby2_themepark_addons`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_themepark_addons: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_themepark_addons: []
        ```

=== "Config"

    ??? variable list "`emby_role_config_settings_default`{ .sb-show-on-unchecked }`emby2_config_settings_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_config_settings_default:
          - xpath: 'IsBehindProxy'
            value: "{{ lookup('role_var', '_config_settings_is_behind_proxy', role='emby') }}"
          - xpath: 'WanDdns'
            value: "{{ lookup('role_var', '_config_settings_wan_ddns', role='emby') }}"
          - xpath: 'PublicPort'
            value: "{{ lookup('role_var', '_config_settings_public_port', role='emby') }}"
          - xpath: 'PublicHttpsPort'
            value: "{{ lookup('role_var', '_config_settings_public_https_port', role='emby') }}"
          - xpath: 'EnableHttps'
            value: "{{ lookup('role_var', '_config_settings_enable_https', role='emby') }}"
          - xpath: 'RequireHttps'
            value: "{{ lookup('role_var', '_config_settings_require_https', role='emby') }}"
          - xpath: 'EnableUPnP'
            value: "{{ lookup('role_var', '_config_settings_enable_upnp', role='emby') }}"
          - xpath: 'DatabaseCacheSizeMB'
            value: "{{ lookup('role_var', '_config_settings_database_cache_size_mb', role='emby') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_config_settings_default:
          - xpath: 'IsBehindProxy'
            value: "{{ lookup('role_var', '_config_settings_is_behind_proxy', role='emby') }}"
          - xpath: 'WanDdns'
            value: "{{ lookup('role_var', '_config_settings_wan_ddns', role='emby') }}"
          - xpath: 'PublicPort'
            value: "{{ lookup('role_var', '_config_settings_public_port', role='emby') }}"
          - xpath: 'PublicHttpsPort'
            value: "{{ lookup('role_var', '_config_settings_public_https_port', role='emby') }}"
          - xpath: 'EnableHttps'
            value: "{{ lookup('role_var', '_config_settings_enable_https', role='emby') }}"
          - xpath: 'RequireHttps'
            value: "{{ lookup('role_var', '_config_settings_require_https', role='emby') }}"
          - xpath: 'EnableUPnP'
            value: "{{ lookup('role_var', '_config_settings_enable_upnp', role='emby') }}"
          - xpath: 'DatabaseCacheSizeMB'
            value: "{{ lookup('role_var', '_config_settings_database_cache_size_mb', role='emby') }}"
        ```

    ??? variable list "`emby_role_config_settings_custom`{ .sb-show-on-unchecked }`emby2_config_settings_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_config_settings_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_config_settings_custom: []
        ```

    ??? variable string "`emby_role_config_settings_list`{ .sb-show-on-unchecked }`emby2_config_settings_list`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_config_settings_list: "{{ lookup('role_var', '_config_settings_default', role='emby') + lookup('role_var', '_config_settings_custom', role='emby') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_config_settings_list: "{{ lookup('role_var', '_config_settings_default', role='emby') + lookup('role_var', '_config_settings_custom', role='emby') }}"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`emby_role_docker_container`{ .sb-show-on-unchecked }`emby2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_container: "{{ emby_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_container: "{{ emby_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`emby_role_docker_image_pull`{ .sb-show-on-unchecked }`emby2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_docker_image_pull: true
        ```

    ??? variable string "`emby_role_docker_image_repo`{ .sb-show-on-unchecked }`emby2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_image_repo: "lscr.io/linuxserver/emby"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_image_repo: "lscr.io/linuxserver/emby"
        ```

    ??? variable string "`emby_role_docker_image_tag`{ .sb-show-on-unchecked }`emby2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_image_tag: "latest"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_image_tag: "latest"
        ```

    ??? variable string "`emby_role_docker_image`{ .sb-show-on-unchecked }`emby2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='emby') }}:{{ lookup('role_var', '_docker_image_tag', role='emby') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='emby') }}:{{ lookup('role_var', '_docker_image_tag', role='emby') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`emby_role_docker_envs_default`{ .sb-show-on-unchecked }`emby2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        emby_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        emby2_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`emby_role_docker_envs_custom`{ .sb-show-on-unchecked }`emby2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        emby_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        emby2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`emby_role_docker_volumes_default`{ .sb-show-on-unchecked }`emby2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_volumes_default:
          - "{{ emby_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
          - "/dev/shm:/dev/shm"
          - "{{ emby_role_paths_transcodes_location }}:/transcode"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_volumes_default:
          - "{{ emby_role_paths_location }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"
          - "/dev/shm:/dev/shm"
          - "{{ emby_role_paths_transcodes_location }}:/transcode"
        ```

    ??? variable list "`emby_role_docker_volumes_legacy`{ .sb-show-on-unchecked }`emby2_docker_volumes_legacy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_volumes_legacy:
          - "/mnt/unionfs/Media:/data"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_volumes_legacy:
          - "/mnt/unionfs/Media:/data"
        ```

    ??? variable list "`emby_role_docker_volumes_custom`{ .sb-show-on-unchecked }`emby2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_volumes_custom: []
        ```

    <h5>Mounts</h5>

    ??? variable list "`emby_role_docker_mounts_default`{ .sb-show-on-unchecked }`emby2_docker_mounts_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_mounts_default:
          - target: /tmp
            type: tmpfs
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_mounts_default:
          - target: /tmp
            type: tmpfs
        ```

    ??? variable list "`emby_role_docker_mounts_custom`{ .sb-show-on-unchecked }`emby2_docker_mounts_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_mounts_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_mounts_custom: []
        ```

    <h5>Labels</h5>

    ??? variable dict "`emby_role_docker_labels_default`{ .sb-show-on-unchecked }`emby2_docker_labels_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        emby_role_docker_labels_default: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        emby2_docker_labels_default: {}
        ```

    ??? variable dict "`emby_role_docker_labels_custom`{ .sb-show-on-unchecked }`emby2_docker_labels_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        emby_role_docker_labels_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        emby2_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`emby_role_docker_hostname`{ .sb-show-on-unchecked }`emby2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_hostname: "{{ emby_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_hostname: "{{ emby_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`emby_role_docker_networks_alias`{ .sb-show-on-unchecked }`emby2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_networks_alias: "{{ emby_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_networks_alias: "{{ emby_name }}"
        ```

    ??? variable list "`emby_role_docker_networks_default`{ .sb-show-on-unchecked }`emby2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_networks_default: []
        ```

    ??? variable list "`emby_role_docker_networks_custom`{ .sb-show-on-unchecked }`emby2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`emby_role_docker_restart_policy`{ .sb-show-on-unchecked }`emby2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`emby_role_docker_state`{ .sb-show-on-unchecked }`emby2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`emby_role_docker_blkio_weight`{ .sb-show-on-unchecked }`emby2_docker_blkio_weight`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        emby_role_docker_blkio_weight:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        emby2_docker_blkio_weight:
        ```

    ??? variable int "`emby_role_docker_cpu_period`{ .sb-show-on-unchecked }`emby2_docker_cpu_period`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        emby_role_docker_cpu_period:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        emby2_docker_cpu_period:
        ```

    ??? variable int "`emby_role_docker_cpu_quota`{ .sb-show-on-unchecked }`emby2_docker_cpu_quota`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        emby_role_docker_cpu_quota:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        emby2_docker_cpu_quota:
        ```

    ??? variable int "`emby_role_docker_cpu_shares`{ .sb-show-on-unchecked }`emby2_docker_cpu_shares`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        emby_role_docker_cpu_shares:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        emby2_docker_cpu_shares:
        ```

    ??? variable string "`emby_role_docker_cpus`{ .sb-show-on-unchecked }`emby2_docker_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_cpus:
        ```

    ??? variable string "`emby_role_docker_cpuset_cpus`{ .sb-show-on-unchecked }`emby2_docker_cpuset_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_cpuset_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_cpuset_cpus:
        ```

    ??? variable string "`emby_role_docker_cpuset_mems`{ .sb-show-on-unchecked }`emby2_docker_cpuset_mems`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_cpuset_mems:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_cpuset_mems:
        ```

    ??? variable string "`emby_role_docker_kernel_memory`{ .sb-show-on-unchecked }`emby2_docker_kernel_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_kernel_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_kernel_memory:
        ```

    ??? variable string "`emby_role_docker_memory`{ .sb-show-on-unchecked }`emby2_docker_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_memory:
        ```

    ??? variable string "`emby_role_docker_memory_reservation`{ .sb-show-on-unchecked }`emby2_docker_memory_reservation`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_memory_reservation:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_memory_reservation:
        ```

    ??? variable string "`emby_role_docker_memory_swap`{ .sb-show-on-unchecked }`emby2_docker_memory_swap`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_memory_swap:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_memory_swap:
        ```

    ??? variable int "`emby_role_docker_memory_swappiness`{ .sb-show-on-unchecked }`emby2_docker_memory_swappiness`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        emby_role_docker_memory_swappiness:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        emby2_docker_memory_swappiness:
        ```

    ??? variable string "`emby_role_docker_shm_size`{ .sb-show-on-unchecked }`emby2_docker_shm_size`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_shm_size:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`emby_role_docker_cap_drop`{ .sb-show-on-unchecked }`emby2_docker_cap_drop`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_cap_drop:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_cap_drop:
        ```

    ??? variable string "`emby_role_docker_cgroupns_mode`{ .sb-show-on-unchecked }`emby2_docker_cgroupns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_cgroupns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_cgroupns_mode:
        ```

    ??? variable list "`emby_role_docker_device_cgroup_rules`{ .sb-show-on-unchecked }`emby2_docker_device_cgroup_rules`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_device_cgroup_rules:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_device_cgroup_rules:
        ```

    ??? variable list "`emby_role_docker_device_read_bps`{ .sb-show-on-unchecked }`emby2_docker_device_read_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_device_read_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_device_read_bps:
        ```

    ??? variable list "`emby_role_docker_device_read_iops`{ .sb-show-on-unchecked }`emby2_docker_device_read_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_device_read_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_device_read_iops:
        ```

    ??? variable list "`emby_role_docker_device_requests`{ .sb-show-on-unchecked }`emby2_docker_device_requests`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_device_requests:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_device_requests:
        ```

    ??? variable list "`emby_role_docker_device_write_bps`{ .sb-show-on-unchecked }`emby2_docker_device_write_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_device_write_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_device_write_bps:
        ```

    ??? variable list "`emby_role_docker_device_write_iops`{ .sb-show-on-unchecked }`emby2_docker_device_write_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_device_write_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_device_write_iops:
        ```

    ??? variable list "`emby_role_docker_devices`{ .sb-show-on-unchecked }`emby2_docker_devices`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_devices:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_devices:
        ```

    ??? variable string "`emby_role_docker_devices_default`{ .sb-show-on-unchecked }`emby2_docker_devices_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_devices_default:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_devices_default:
        ```

    ??? variable list "`emby_role_docker_groups`{ .sb-show-on-unchecked }`emby2_docker_groups`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_groups:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_groups:
        ```

    ??? variable bool "`emby_role_docker_privileged`{ .sb-show-on-unchecked }`emby2_docker_privileged`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_docker_privileged:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_docker_privileged:
        ```

    ??? variable list "`emby_role_docker_security_opts`{ .sb-show-on-unchecked }`emby2_docker_security_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_security_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_security_opts:
        ```

    ??? variable string "`emby_role_docker_user`{ .sb-show-on-unchecked }`emby2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_user:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_user:
        ```

    ??? variable string "`emby_role_docker_userns_mode`{ .sb-show-on-unchecked }`emby2_docker_userns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_userns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`emby_role_docker_dns_opts`{ .sb-show-on-unchecked }`emby2_docker_dns_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_dns_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_dns_opts:
        ```

    ??? variable list "`emby_role_docker_dns_search_domains`{ .sb-show-on-unchecked }`emby2_docker_dns_search_domains`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_dns_search_domains:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_dns_search_domains:
        ```

    ??? variable list "`emby_role_docker_dns_servers`{ .sb-show-on-unchecked }`emby2_docker_dns_servers`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_dns_servers:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_dns_servers:
        ```

    ??? variable string "`emby_role_docker_domainname`{ .sb-show-on-unchecked }`emby2_docker_domainname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_domainname:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_domainname:
        ```

    ??? variable list "`emby_role_docker_exposed_ports`{ .sb-show-on-unchecked }`emby2_docker_exposed_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_exposed_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_exposed_ports:
        ```

    ??? variable dict "`emby_role_docker_hosts`{ .sb-show-on-unchecked }`emby2_docker_hosts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        emby_role_docker_hosts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        emby2_docker_hosts:
        ```

    ??? variable bool "`emby_role_docker_hosts_use_common`{ .sb-show-on-unchecked }`emby2_docker_hosts_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_docker_hosts_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_docker_hosts_use_common:
        ```

    ??? variable string "`emby_role_docker_ipc_mode`{ .sb-show-on-unchecked }`emby2_docker_ipc_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_ipc_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_ipc_mode:
        ```

    ??? variable list "`emby_role_docker_links`{ .sb-show-on-unchecked }`emby2_docker_links`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_links:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_links:
        ```

    ??? variable string "`emby_role_docker_network_mode`{ .sb-show-on-unchecked }`emby2_docker_network_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_network_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_network_mode:
        ```

    ??? variable string "`emby_role_docker_pid_mode`{ .sb-show-on-unchecked }`emby2_docker_pid_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_pid_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_pid_mode:
        ```

    ??? variable list "`emby_role_docker_ports`{ .sb-show-on-unchecked }`emby2_docker_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_ports:
        ```

    ??? variable string "`emby_role_docker_uts`{ .sb-show-on-unchecked }`emby2_docker_uts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_uts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`emby_role_docker_keep_volumes`{ .sb-show-on-unchecked }`emby2_docker_keep_volumes`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_docker_keep_volumes:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_docker_keep_volumes:
        ```

    ??? variable dict "`emby_role_docker_storage_opts`{ .sb-show-on-unchecked }`emby2_docker_storage_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        emby_role_docker_storage_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        emby2_docker_storage_opts:
        ```

    ??? variable list "`emby_role_docker_tmpfs`{ .sb-show-on-unchecked }`emby2_docker_tmpfs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_tmpfs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_tmpfs:
        ```

    ??? variable string "`emby_role_docker_volume_driver`{ .sb-show-on-unchecked }`emby2_docker_volume_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_volume_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_volume_driver:
        ```

    ??? variable list "`emby_role_docker_volumes_from`{ .sb-show-on-unchecked }`emby2_docker_volumes_from`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_volumes_from:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_volumes_from:
        ```

    ??? variable bool "`emby_role_docker_volumes_global`{ .sb-show-on-unchecked }`emby2_docker_volumes_global`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_docker_volumes_global:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_docker_volumes_global:
        ```

    ??? variable string "`emby_role_docker_working_dir`{ .sb-show-on-unchecked }`emby2_docker_working_dir`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_working_dir:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`emby_role_docker_auto_remove`{ .sb-show-on-unchecked }`emby2_docker_auto_remove`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_docker_auto_remove:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_docker_auto_remove:
        ```

    ??? variable bool "`emby_role_docker_cleanup`{ .sb-show-on-unchecked }`emby2_docker_cleanup`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_docker_cleanup:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_docker_cleanup:
        ```

    ??? variable string "`emby_role_docker_force_kill`{ .sb-show-on-unchecked }`emby2_docker_force_kill`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_force_kill:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_force_kill:
        ```

    ??? variable dict "`emby_role_docker_healthcheck`{ .sb-show-on-unchecked }`emby2_docker_healthcheck`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        emby_role_docker_healthcheck:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        emby2_docker_healthcheck:
        ```

    ??? variable int "`emby_role_docker_healthy_wait_timeout`{ .sb-show-on-unchecked }`emby2_docker_healthy_wait_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        emby_role_docker_healthy_wait_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        emby2_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`emby_role_docker_init`{ .sb-show-on-unchecked }`emby2_docker_init`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_docker_init:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_docker_init:
        ```

    ??? variable string "`emby_role_docker_kill_signal`{ .sb-show-on-unchecked }`emby2_docker_kill_signal`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_kill_signal:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_kill_signal:
        ```

    ??? variable string "`emby_role_docker_log_driver`{ .sb-show-on-unchecked }`emby2_docker_log_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_log_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_log_driver:
        ```

    ??? variable dict "`emby_role_docker_log_options`{ .sb-show-on-unchecked }`emby2_docker_log_options`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        emby_role_docker_log_options:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        emby2_docker_log_options:
        ```

    ??? variable bool "`emby_role_docker_oom_killer`{ .sb-show-on-unchecked }`emby2_docker_oom_killer`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_docker_oom_killer:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_docker_oom_killer:
        ```

    ??? variable int "`emby_role_docker_oom_score_adj`{ .sb-show-on-unchecked }`emby2_docker_oom_score_adj`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        emby_role_docker_oom_score_adj:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        emby2_docker_oom_score_adj:
        ```

    ??? variable bool "`emby_role_docker_output_logs`{ .sb-show-on-unchecked }`emby2_docker_output_logs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_docker_output_logs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_docker_output_logs:
        ```

    ??? variable bool "`emby_role_docker_paused`{ .sb-show-on-unchecked }`emby2_docker_paused`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_docker_paused:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_docker_paused:
        ```

    ??? variable bool "`emby_role_docker_recreate`{ .sb-show-on-unchecked }`emby2_docker_recreate`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_docker_recreate:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_docker_recreate:
        ```

    ??? variable int "`emby_role_docker_restart_retries`{ .sb-show-on-unchecked }`emby2_docker_restart_retries`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        emby_role_docker_restart_retries:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        emby2_docker_restart_retries:
        ```

    ??? variable int "`emby_role_docker_stop_timeout`{ .sb-show-on-unchecked }`emby2_docker_stop_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        emby_role_docker_stop_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        emby2_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable list "`emby_role_docker_capabilities`{ .sb-show-on-unchecked }`emby2_docker_capabilities`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_capabilities:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_capabilities:
        ```

    ??? variable string "`emby_role_docker_cgroup_parent`{ .sb-show-on-unchecked }`emby2_docker_cgroup_parent`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_cgroup_parent:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_cgroup_parent:
        ```

    ??? variable list "`emby_role_docker_commands`{ .sb-show-on-unchecked }`emby2_docker_commands`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_commands:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_commands:
        ```

    ??? variable int "`emby_role_docker_create_timeout`{ .sb-show-on-unchecked }`emby2_docker_create_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        emby_role_docker_create_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        emby2_docker_create_timeout:
        ```

    ??? variable string "`emby_role_docker_entrypoint`{ .sb-show-on-unchecked }`emby2_docker_entrypoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_entrypoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_entrypoint:
        ```

    ??? variable string "`emby_role_docker_env_file`{ .sb-show-on-unchecked }`emby2_docker_env_file`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_env_file:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_env_file:
        ```

    ??? variable bool "`emby_role_docker_labels_use_common`{ .sb-show-on-unchecked }`emby2_docker_labels_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_docker_labels_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_docker_labels_use_common:
        ```

    ??? variable bool "`emby_role_docker_read_only`{ .sb-show-on-unchecked }`emby2_docker_read_only`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_docker_read_only:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_docker_read_only:
        ```

    ??? variable string "`emby_role_docker_runtime`{ .sb-show-on-unchecked }`emby2_docker_runtime`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_runtime:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_runtime:
        ```

    ??? variable list "`emby_role_docker_sysctls`{ .sb-show-on-unchecked }`emby2_docker_sysctls`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_sysctls:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_sysctls:
        ```

    ??? variable list "`emby_role_docker_ulimits`{ .sb-show-on-unchecked }`emby2_docker_ulimits`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        emby_role_docker_ulimits:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        emby2_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`emby_role_autoheal_enabled`{ .sb-show-on-unchecked }`emby2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        emby_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        emby2_autoheal_enabled: true
        ```

    ??? variable string "`emby_role_config_settings_custom`{ .sb-show-on-unchecked }`emby2_config_settings_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_config_settings_custom:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_config_settings_custom:
        ```

    ??? variable string "`emby_role_config_settings_database_cache_size_mb`{ .sb-show-on-unchecked }`emby2_config_settings_database_cache_size_mb`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_config_settings_database_cache_size_mb:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_config_settings_database_cache_size_mb:
        ```

    ??? variable string "`emby_role_config_settings_default`{ .sb-show-on-unchecked }`emby2_config_settings_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_config_settings_default:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_config_settings_default:
        ```

    ??? variable string "`emby_role_config_settings_enable_https`{ .sb-show-on-unchecked }`emby2_config_settings_enable_https`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_config_settings_enable_https:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_config_settings_enable_https:
        ```

    ??? variable string "`emby_role_config_settings_enable_upnp`{ .sb-show-on-unchecked }`emby2_config_settings_enable_upnp`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_config_settings_enable_upnp:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_config_settings_enable_upnp:
        ```

    ??? variable bool "`emby_role_config_settings_is_behind_proxy`{ .sb-show-on-unchecked }`emby2_config_settings_is_behind_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_config_settings_is_behind_proxy:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_config_settings_is_behind_proxy:
        ```

    ??? variable string "`emby_role_config_settings_public_https_port`{ .sb-show-on-unchecked }`emby2_config_settings_public_https_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        emby_role_config_settings_public_https_port:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        emby2_config_settings_public_https_port:
        ```

    ??? variable string "`emby_role_config_settings_public_port`{ .sb-show-on-unchecked }`emby2_config_settings_public_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        emby_role_config_settings_public_port:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        emby2_config_settings_public_port:
        ```

    ??? variable string "`emby_role_config_settings_require_https`{ .sb-show-on-unchecked }`emby2_config_settings_require_https`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_config_settings_require_https:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_config_settings_require_https:
        ```

    ??? variable string "`emby_role_config_settings_wan_ddns`{ .sb-show-on-unchecked }`emby2_config_settings_wan_ddns`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_config_settings_wan_ddns:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_config_settings_wan_ddns:
        ```

    ??? variable string "`emby_role_depends_on`{ .sb-show-on-unchecked }`emby2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        emby_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        emby2_depends_on: ""
        ```

    ??? variable string "`emby_role_depends_on_delay`{ .sb-show-on-unchecked }`emby2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        emby_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        emby2_depends_on_delay: "0"
        ```

    ??? variable string "`emby_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`emby2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        emby_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        emby2_depends_on_healthchecks:
        ```

    ??? variable bool "`emby_role_diun_enabled`{ .sb-show-on-unchecked }`emby2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        emby_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        emby2_diun_enabled: true
        ```

    ??? variable bool "`emby_role_dns_enabled`{ .sb-show-on-unchecked }`emby2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        emby_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        emby2_dns_enabled: true
        ```

    ??? variable bool "`emby_role_docker_controller`{ .sb-show-on-unchecked }`emby2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        emby_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        emby2_docker_controller: true
        ```

    ??? variable string "`emby_role_docker_image_repo`{ .sb-show-on-unchecked }`emby2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_image_repo:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_image_repo:
        ```

    ??? variable string "`emby_role_docker_image_tag`{ .sb-show-on-unchecked }`emby2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_docker_image_tag:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_docker_image_tag:
        ```

    ??? variable bool "`emby_role_docker_volumes_download`{ .sb-show-on-unchecked }`emby2_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_docker_volumes_download:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_docker_volumes_download:
        ```

    ??? variable string "`emby_role_themepark_addons`{ .sb-show-on-unchecked }`emby2_themepark_addons`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_themepark_addons:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_themepark_addons:
        ```

    ??? variable string "`emby_role_themepark_app`{ .sb-show-on-unchecked }`emby2_themepark_app`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_themepark_app:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_themepark_app:
        ```

    ??? variable bool "`emby_role_themepark_enabled`{ .sb-show-on-unchecked }`emby2_themepark_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_themepark_enabled:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_themepark_enabled:
        ```

    ??? variable string "`emby_role_themepark_theme`{ .sb-show-on-unchecked }`emby2_themepark_theme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_themepark_theme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_themepark_theme:
        ```

    ??? variable dict "`emby_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`emby2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        emby_role_traefik_api_endpoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        emby2_traefik_api_endpoint:
        ```

    ??? variable string "`emby_role_traefik_api_middleware`{ .sb-show-on-unchecked }`emby2_traefik_api_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_traefik_api_middleware:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_traefik_api_middleware:
        ```

    ??? variable string "`emby_role_traefik_api_middleware_http`{ .sb-show-on-unchecked }`emby2_traefik_api_middleware_http`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_traefik_api_middleware_http:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_traefik_api_middleware_http:
        ```

    ??? variable bool "`emby_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`emby2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        emby_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        emby2_traefik_autodetect_enabled: false
        ```

    ??? variable string "`emby_role_traefik_certresolver`{ .sb-show-on-unchecked }`emby2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_traefik_certresolver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_traefik_certresolver:
        ```

    ??? variable bool "`emby_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`emby2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        emby_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        emby2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`emby_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`emby2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        emby_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        emby2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`emby_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`emby2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        emby_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        emby2_traefik_gzip_enabled: false
        ```

    ??? variable string "`emby_role_traefik_middleware_http`{ .sb-show-on-unchecked }`emby2_traefik_middleware_http`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_traefik_middleware_http:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_traefik_middleware_http:
        ```

    ??? variable bool "`emby_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`emby2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`emby_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`emby2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        emby_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        emby2_traefik_middleware_http_insecure:
        ```

    ??? variable string "`emby_role_traefik_priority`{ .sb-show-on-unchecked }`emby2_traefik_priority`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_traefik_priority:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_traefik_priority:
        ```

    ??? variable bool "`emby_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`emby2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        emby_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        emby2_traefik_robot_enabled: true
        ```

    ??? variable bool "`emby_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`emby2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        emby_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        emby2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`emby_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`emby2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        emby_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        emby2_traefik_wildcard_enabled: true
        ```

    ??? variable string "`emby_role_web_domain`{ .sb-show-on-unchecked }`emby2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_web_domain:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_web_domain:
        ```

    ??? variable list "`emby_role_web_fqdn_override`{ .sb-show-on-unchecked }`emby2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        emby_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        emby2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            emby_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "emby2.{{ user.domain }}"
              - "emby.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


        !!! example sb-show-on-checked "Example Override"

            ```yaml
            emby2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "emby2.{{ user.domain }}"
              - "emby.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`emby_role_web_host_override`{ .sb-show-on-unchecked }`emby2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        emby_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        emby2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            emby_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'emby2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


        !!! example sb-show-on-checked "Example Override"

            ```yaml
            emby2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'emby2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`emby_role_web_http_port`{ .sb-show-on-unchecked }`emby2_web_http_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        emby_role_web_http_port:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        emby2_web_http_port:
        ```

    ??? variable string "`emby_role_web_http_scheme`{ .sb-show-on-unchecked }`emby2_web_http_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string ("http"/"https")
        emby_role_web_http_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string ("http"/"https")
        emby2_web_http_scheme:
        ```

    ??? variable dict "`emby_role_web_http_serverstransport`{ .sb-show-on-unchecked }`emby2_web_http_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        emby_role_web_http_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        emby2_web_http_serverstransport:
        ```

    ??? variable string "`emby_role_web_scheme`{ .sb-show-on-unchecked }`emby2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        emby_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        emby2_web_scheme:
        ```

    ??? variable dict "`emby_role_web_serverstransport`{ .sb-show-on-unchecked }`emby2_web_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        emby_role_web_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        emby2_web_serverstransport:
        ```

    ??? variable string "`emby_role_web_subdomain`{ .sb-show-on-unchecked }`emby2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        emby_role_web_subdomain:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        emby2_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
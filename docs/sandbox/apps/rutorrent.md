---
icon: material/docker
title: ruTorrent
hide:
  - tags
tags:
  - bittorrent
  - p2p
  - rutorrent
  - torrent
saltbox_automation:
  app_links:
    - name: Manual
      url: https://github.com/Novik/ruTorrent/wiki
      type: documentation
      purpose: manual
    - name: Releases
      url: https://hub.docker.com/r/crazymax/rtorrent-rutorrent/tags
      type: docker
      purpose: release
    - name: Community
      url: https://github.com/Novik/ruTorrent/discussions
      type: github
      purpose: community
  project_description:
    name: ruTorrent
    summary: |-
      a front-end for the popular, lightweight, and extensible BitTorrent client rTorrent.
    link: https://github.com/Novik/ruTorrent
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# ruTorrent

## Overview

[ruTorrent](https://github.com/Novik/ruTorrent) is a front-end for the popular, lightweight, and extensible BitTorrent client rTorrent.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://github.com/Novik/ruTorrent/wiki){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/kudeta/ru-rtorrent/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Community**](https://github.com/Novik/ruTorrent/discussions){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

???+warning "Migrating from the old Docker image"

    On November 1, 2026, this role switched to *crazymax/rtorrent-rutorrent*, which uses a different layout for its application data than the previous image.

    There is no automatic migration. The role now stores the data in `/opt/rtorrent-rutorrent` (by default), so the existing `/opt/rutorrent` folder is left untouched. If you wish to carry the data over, you must move the relevant parts to where the new container expects them.

## Deployment

```shell
sb install sandbox-rutorrent
```

## Usage

| Service | URL                                           | Access control |
|---------|-----------------------------------------------|----------------|
| Web     | <https://rutorrent.iYOUR_DOMAIN_NAMEi>        | Traefik SSO    |
| WebDAV  | <https://rutorrent-webdav.iYOUR_DOMAIN_NAMEi> | Basic Auth     |
| API     | <https://rutorrent.iYOUR_DOMAIN_NAMEi/RPC>    | Basic Auth     |

### Unpacking

[Unpackerr](../../apps/unpackerr.md) is the recommended tool for the job. This role removes ruTorrent's *unpack* plugin by default, as its functionality is too limited for standard Saltbox workflows.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults<label class="sb-toggle--override-scope md-annotation__index" title="Supports multiple instances! Click to toggle override scope"><input type="checkbox" name="scope" hidden/></label>

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  **This role supports multiple instances via `rutorrent_instances`.**

    !!! example "Example override"

        === "Role-scoped"

            ```yaml
            rutorrent_role_web_subdomain: "custom"
            ```

            :material-arrow-right-bottom-bold: Applies to all instances of rutorrent

        === "Instance-scoped"

            ```yaml
            rutorrent2_web_subdomain: "custom2"
            ```

            :material-arrow-right-bottom-bold: Applies to the instance named rutorrent2

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `rutorrent_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `rutorrent_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`rutorrent_instances`"

        ```yaml
        # Type: list
        rutorrent_instances: ["rutorrent"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            rutorrent_instances: ["rutorrent", "rutorrent2"]
            ```

=== "Settings"

    ??? variable bool "`rutorrent_role_webdav_enable`{ .sb-show-on-unchecked }`rutorrent2_webdav_enable`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable the WebDAV endpoint
        # Type: bool (true/false)
        rutorrent_role_webdav_enable: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable the WebDAV endpoint
        # Type: bool (true/false)
        rutorrent2_webdav_enable: true
        ```

    ??? variable bool "`rutorrent_role_manage_rt_config_enable`{ .sb-show-on-unchecked }`rutorrent2_manage_rt_config_enable`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Allow the role to manage the rTorrent configuration
        # Type: bool (true/false)
        rutorrent_role_manage_rt_config_enable: true
        ```

        ```yaml { .sb-show-on-checked }
        # Allow the role to manage the rTorrent configuration
        # Type: bool (true/false)
        rutorrent2_manage_rt_config_enable: true
        ```

    ??? variable bool "`rutorrent_role_public_trackers_enable`{ .sb-show-on-unchecked }`rutorrent2_public_trackers_enable`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable public tracker connectivity
        # Type: bool (true/false)
        rutorrent_role_public_trackers_enable: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable public tracker connectivity
        # Type: bool (true/false)
        rutorrent2_public_trackers_enable: false
        ```

    ??? variable bool "`rutorrent_role_trim_plugins_enable`{ .sb-show-on-unchecked }`rutorrent2_trim_plugins_enable`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Remove a curated set of redundant ruTorrent plugins
        # Type: bool (true/false)
        rutorrent_role_trim_plugins_enable: true
        ```

        ```yaml { .sb-show-on-checked }
        # Remove a curated set of redundant ruTorrent plugins
        # Type: bool (true/false)
        rutorrent2_trim_plugins_enable: true
        ```

    ??? variable list "`rutorrent_role_theme_repos`{ .sb-show-on-unchecked }`rutorrent2_theme_repos`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Third-party ruTorrent themes to include through git clone
        # Type: list
        rutorrent_role_theme_repos:
          - { name: "club-QuickBox", url: "https://github.com/QuickBox/club-QuickBox.git", version: "latest" }
        ```

        ```yaml { .sb-show-on-checked }
        # Third-party ruTorrent themes to include through git clone
        # Type: list
        rutorrent2_theme_repos:
          - { name: "club-QuickBox", url: "https://github.com/QuickBox/club-QuickBox.git", version: "latest" }
        ```

    ??? variable list "`rutorrent_role_plugin_repos`{ .sb-show-on-unchecked }`rutorrent2_plugin_repos`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Third-party ruTorrent plugins to include through git clone
        # Same format as `_theme_repos`
        # Type: list
        rutorrent_role_plugin_repos: []
        ```

        ```yaml { .sb-show-on-checked }
        # Third-party ruTorrent plugins to include through git clone
        # Same format as `_theme_repos`
        # Type: list
        rutorrent2_plugin_repos: []
        ```

    ??? variable string "`rutorrent_role_wan_ip`{ .sb-show-on-unchecked }`rutorrent2_wan_ip`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Public IP address reported to the tracker
        # Type: string
        rutorrent_role_wan_ip: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Public IP address reported to the tracker
        # Type: string
        rutorrent2_wan_ip: ""
        ```

    ??? variable string "`rutorrent_role_wan_ip_cmd`{ .sb-show-on-unchecked }`rutorrent2_wan_ip_cmd`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Command to resolve the Public IP address
        # Type: string
        rutorrent_role_wan_ip_cmd: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Command to resolve the Public IP address
        # Type: string
        rutorrent2_wan_ip_cmd: ""
        ```

    ??? variable string "`rutorrent_role_memory_limit`{ .sb-show-on-unchecked }`rutorrent2_memory_limit`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # PHP memory limit
        # Type: string
        rutorrent_role_memory_limit: ""
        ```

        ```yaml { .sb-show-on-checked }
        # PHP memory limit
        # Type: string
        rutorrent2_memory_limit: ""
        ```

    ??? variable string "`rutorrent_role_upload_max_size`{ .sb-show-on-unchecked }`rutorrent2_upload_max_size`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Upload max size
        # Type: string
        rutorrent_role_upload_max_size: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Upload max size
        # Type: string
        rutorrent2_upload_max_size: ""
        ```

    ??? variable string "`rutorrent_role_clear_env`{ .sb-show-on-unchecked }`rutorrent2_clear_env`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Clear environment in FPM workers
        # Valid values: "yes", "no"
        # Type: string
        rutorrent_role_clear_env: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Clear environment in FPM workers
        # Valid values: "yes", "no"
        # Type: string
        rutorrent2_clear_env: ""
        ```

    ??? variable string "`rutorrent_role_opcache_mem_size`{ .sb-show-on-unchecked }`rutorrent2_opcache_mem_size`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # PHP OpCache memory consumption
        # Type: string
        rutorrent_role_opcache_mem_size: ""
        ```

        ```yaml { .sb-show-on-checked }
        # PHP OpCache memory consumption
        # Type: string
        rutorrent2_opcache_mem_size: ""
        ```

    ??? variable string "`rutorrent_role_max_file_uploads`{ .sb-show-on-unchecked }`rutorrent2_max_file_uploads`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Maximum number of files allowed to be uploaded simultaneously
        # Type: string
        rutorrent_role_max_file_uploads: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Maximum number of files allowed to be uploaded simultaneously
        # Type: string
        rutorrent2_max_file_uploads: ""
        ```

    ??? variable string "`rutorrent_role_real_ip_from`{ .sb-show-on-unchecked }`rutorrent2_real_ip_from`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Trusted addresses that are known to send correct replacement addresses
        # Type: string
        rutorrent_role_real_ip_from: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Trusted addresses that are known to send correct replacement addresses
        # Type: string
        rutorrent2_real_ip_from: ""
        ```

    ??? variable string "`rutorrent_role_real_ip_header`{ .sb-show-on-unchecked }`rutorrent2_real_ip_header`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Request header field whose value will be used to replace the client address
        # Type: string
        rutorrent_role_real_ip_header: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Request header field whose value will be used to replace the client address
        # Type: string
        rutorrent2_real_ip_header: ""
        ```

    ??? variable string "`rutorrent_role_log_ip_var`{ .sb-show-on-unchecked }`rutorrent2_log_ip_var`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Another variable to retrieve the remote IP address for access log_format on Nginx
        # Type: string
        rutorrent_role_log_ip_var: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Another variable to retrieve the remote IP address for access log_format on Nginx
        # Type: string
        rutorrent2_log_ip_var: ""
        ```

    ??? variable string "`rutorrent_role_log_access`{ .sb-show-on-unchecked }`rutorrent2_log_access`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable output access log
        # Valid values: "true", "false"
        # Type: string
        rutorrent_role_log_access: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Enable output access log
        # Valid values: "true", "false"
        # Type: string
        rutorrent2_log_access: ""
        ```

    ??? variable string "`rutorrent_role_xmlrpc_size_limit`{ .sb-show-on-unchecked }`rutorrent2_xmlrpc_size_limit`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Maximum body size of XMLRPC calls
        # Type: string
        rutorrent_role_xmlrpc_size_limit: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Maximum body size of XMLRPC calls
        # Type: string
        rutorrent2_xmlrpc_size_limit: ""
        ```

    ??? variable string "`rutorrent_role_rt_log_level`{ .sb-show-on-unchecked }`rutorrent2_rt_log_level`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # rTorrent log level
        # Type: string
        rutorrent_role_rt_log_level: ""
        ```

        ```yaml { .sb-show-on-checked }
        # rTorrent log level
        # Type: string
        rutorrent2_rt_log_level: ""
        ```

    ??? variable string "`rutorrent_role_rt_log_execute`{ .sb-show-on-unchecked }`rutorrent2_rt_log_execute`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Log executed commands to /data/rtorrent/log/execute.log
        # Valid values: "true", "false"
        # Type: string
        rutorrent_role_rt_log_execute: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Log executed commands to /data/rtorrent/log/execute.log
        # Valid values: "true", "false"
        # Type: string
        rutorrent2_rt_log_execute: ""
        ```

    ??? variable string "`rutorrent_role_rt_log_xmlrpc`{ .sb-show-on-unchecked }`rutorrent2_rt_log_xmlrpc`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Log XMLRPC queries to /data/rtorrent/log/xmlrpc.log
        # Valid values: "true", "false"
        # Type: string
        rutorrent_role_rt_log_xmlrpc: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Log XMLRPC queries to /data/rtorrent/log/xmlrpc.log
        # Valid values: "true", "false"
        # Type: string
        rutorrent2_rt_log_xmlrpc: ""
        ```

    ??? variable string "`rutorrent_role_rt_session_save_seconds`{ .sb-show-on-unchecked }`rutorrent2_rt_session_save_seconds`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Seconds between writing torrent information to disk
        # Type: string
        rutorrent_role_rt_session_save_seconds: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Seconds between writing torrent information to disk
        # Type: string
        rutorrent2_rt_session_save_seconds: ""
        ```

    ??? variable string "`rutorrent_role_rt_session_fdatasync`{ .sb-show-on-unchecked }`rutorrent2_rt_session_fdatasync`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Force fdatasync when saving sessions
        # Valid values: "true", "false"
        # Type: string
        rutorrent_role_rt_session_fdatasync: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Force fdatasync when saving sessions
        # Valid values: "true", "false"
        # Type: string
        rutorrent2_rt_session_fdatasync: ""
        ```

    ??? variable string "`rutorrent_role_rt_tracker_delay_scrape`{ .sb-show-on-unchecked }`rutorrent2_rt_tracker_delay_scrape`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay tracker announces at startup
        # Valid values: "true", "false"
        # Type: string
        rutorrent_role_rt_tracker_delay_scrape: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Delay tracker announces at startup
        # Valid values: "true", "false"
        # Type: string
        rutorrent2_rt_tracker_delay_scrape: ""
        ```

    ??? variable string "`rutorrent_role_rt_receive_buffer_size`{ .sb-show-on-unchecked }`rutorrent2_rt_receive_buffer_size`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Sets the default TCP receive buffer size
        # Type: string
        rutorrent_role_rt_receive_buffer_size: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Sets the default TCP receive buffer size
        # Type: string
        rutorrent2_rt_receive_buffer_size: ""
        ```

    ??? variable string "`rutorrent_role_rt_send_buffer_size`{ .sb-show-on-unchecked }`rutorrent2_rt_send_buffer_size`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Sets the default TCP send buffer size
        # Type: string
        rutorrent_role_rt_send_buffer_size: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Sets the default TCP send buffer size
        # Type: string
        rutorrent2_rt_send_buffer_size: ""
        ```

    ??? variable string "`rutorrent_role_rt_preallocate_type`{ .sb-show-on-unchecked }`rutorrent2_rt_preallocate_type`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type of disk space preallocation
        # Valid values: "0", "1", "2"
        # Type: string
        rutorrent_role_rt_preallocate_type: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type of disk space preallocation
        # Valid values: "0", "1", "2"
        # Type: string
        rutorrent2_rt_preallocate_type: ""
        ```

    ??? variable string "`rutorrent_role_rt_dht_port`{ .sb-show-on-unchecked }`rutorrent2_rt_dht_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # DHT UDP port
        # Type: string
        rutorrent_role_rt_dht_port: ""
        ```

        ```yaml { .sb-show-on-checked }
        # DHT UDP port
        # Type: string
        rutorrent2_rt_dht_port: ""
        ```

    ??? variable string "`rutorrent_role_rt_inc_port`{ .sb-show-on-unchecked }`rutorrent2_rt_inc_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Incoming connections port
        # Type: string
        rutorrent_role_rt_inc_port: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Incoming connections port
        # Type: string
        rutorrent2_rt_inc_port: ""
        ```

    ??? variable string "`rutorrent_role_ru_remove_core_plugins`{ .sb-show-on-unchecked }`rutorrent2_ru_remove_core_plugins`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Comma-separated list of core plugins to remove
        # Type: string
        rutorrent_role_ru_remove_core_plugins: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Comma-separated list of core plugins to remove
        # Type: string
        rutorrent2_ru_remove_core_plugins: ""
        ```

    ??? variable string "`rutorrent_role_ru_http_user_agent`{ .sb-show-on-unchecked }`rutorrent2_ru_http_user_agent`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # ruTorrent HTTP user agent
        # Type: string
        rutorrent_role_ru_http_user_agent: ""
        ```

        ```yaml { .sb-show-on-checked }
        # ruTorrent HTTP user agent
        # Type: string
        rutorrent2_ru_http_user_agent: ""
        ```

    ??? variable string "`rutorrent_role_ru_http_time_out`{ .sb-show-on-unchecked }`rutorrent2_ru_http_time_out`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # ruTorrent HTTP timeout in seconds
        # Type: string
        rutorrent_role_ru_http_time_out: ""
        ```

        ```yaml { .sb-show-on-checked }
        # ruTorrent HTTP timeout in seconds
        # Type: string
        rutorrent2_ru_http_time_out: ""
        ```

    ??? variable string "`rutorrent_role_ru_http_use_gzip`{ .sb-show-on-unchecked }`rutorrent2_ru_http_use_gzip`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Use HTTP Gzip compression
        # Valid values: "true", "false"
        # Type: string
        rutorrent_role_ru_http_use_gzip: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Use HTTP Gzip compression
        # Valid values: "true", "false"
        # Type: string
        rutorrent2_ru_http_use_gzip: ""
        ```

    ??? variable string "`rutorrent_role_ru_http_verify_certificates`{ .sb-show-on-unchecked }`rutorrent2_ru_http_verify_certificates`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Verify HTTPS server and proxy certificates
        # Valid values: "true", "false"
        # Type: string
        rutorrent_role_ru_http_verify_certificates: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Verify HTTPS server and proxy certificates
        # Valid values: "true", "false"
        # Type: string
        rutorrent2_ru_http_verify_certificates: ""
        ```

    ??? variable string "`rutorrent_role_ru_rpc_time_out`{ .sb-show-on-unchecked }`rutorrent2_ru_rpc_time_out`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # ruTorrent RPC timeout in seconds
        # Type: string
        rutorrent_role_ru_rpc_time_out: ""
        ```

        ```yaml { .sb-show-on-checked }
        # ruTorrent RPC timeout in seconds
        # Type: string
        rutorrent2_ru_rpc_time_out: ""
        ```

    ??? variable string "`rutorrent_role_ru_log_rpc_calls`{ .sb-show-on-unchecked }`rutorrent2_ru_log_rpc_calls`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Log ruTorrent RPC calls
        # Valid values: "true", "false"
        # Type: string
        rutorrent_role_ru_log_rpc_calls: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Log ruTorrent RPC calls
        # Valid values: "true", "false"
        # Type: string
        rutorrent2_ru_log_rpc_calls: ""
        ```

    ??? variable string "`rutorrent_role_ru_log_rpc_faults`{ .sb-show-on-unchecked }`rutorrent2_ru_log_rpc_faults`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Log ruTorrent RPC faults
        # Valid values: "true", "false"
        # Type: string
        rutorrent_role_ru_log_rpc_faults: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Log ruTorrent RPC faults
        # Valid values: "true", "false"
        # Type: string
        rutorrent2_ru_log_rpc_faults: ""
        ```

    ??? variable string "`rutorrent_role_ru_php_use_gzip`{ .sb-show-on-unchecked }`rutorrent2_ru_php_use_gzip`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Use PHP Gzip compression
        # Valid values: "true", "false"
        # Type: string
        rutorrent_role_ru_php_use_gzip: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Use PHP Gzip compression
        # Valid values: "true", "false"
        # Type: string
        rutorrent2_ru_php_use_gzip: ""
        ```

    ??? variable string "`rutorrent_role_ru_php_gzip_level`{ .sb-show-on-unchecked }`rutorrent2_ru_php_gzip_level`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # PHP Gzip compression level
        # Type: string
        rutorrent_role_ru_php_gzip_level: ""
        ```

        ```yaml { .sb-show-on-checked }
        # PHP Gzip compression level
        # Type: string
        rutorrent2_ru_php_gzip_level: ""
        ```

    ??? variable string "`rutorrent_role_ru_schedule_rand`{ .sb-show-on-unchecked }`rutorrent2_ru_schedule_rand`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Random delay for scheduler start, from 0 to this value in seconds
        # Type: string
        rutorrent_role_ru_schedule_rand: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Random delay for scheduler start, from 0 to this value in seconds
        # Type: string
        rutorrent2_ru_schedule_rand: ""
        ```

    ??? variable string "`rutorrent_role_ru_log_file`{ .sb-show-on-unchecked }`rutorrent2_ru_log_file`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # ruTorrent log file path for error messages
        # Type: string
        rutorrent_role_ru_log_file: ""
        ```

        ```yaml { .sb-show-on-checked }
        # ruTorrent log file path for error messages
        # Type: string
        rutorrent2_ru_log_file: ""
        ```

    ??? variable string "`rutorrent_role_ru_do_diagnostic`{ .sb-show-on-unchecked }`rutorrent2_ru_do_diagnostic`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable ruTorrent diagnostics such as permission checking
        # Valid values: "true", "false"
        # Type: string
        rutorrent_role_ru_do_diagnostic: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Enable ruTorrent diagnostics such as permission checking
        # Valid values: "true", "false"
        # Type: string
        rutorrent2_ru_do_diagnostic: ""
        ```

    ??? variable string "`rutorrent_role_ru_cached_plugin_loading`{ .sb-show-on-unchecked }`rutorrent2_ru_cached_plugin_loading`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable rapid cached loading of ruTorrent plugins
        # Valid values: "true", "false"
        # Type: string
        rutorrent_role_ru_cached_plugin_loading: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Enable rapid cached loading of ruTorrent plugins
        # Valid values: "true", "false"
        # Type: string
        rutorrent2_ru_cached_plugin_loading: ""
        ```

    ??? variable string "`rutorrent_role_ru_save_uploaded_torrents`{ .sb-show-on-unchecked }`rutorrent2_ru_save_uploaded_torrents`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Save torrents added through ruTorrent in /data/rutorrent/share/torrents
        # Valid values: "true", "false"
        # Type: string
        rutorrent_role_ru_save_uploaded_torrents: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Save torrents added through ruTorrent in /data/rutorrent/share/torrents
        # Valid values: "true", "false"
        # Type: string
        rutorrent2_ru_save_uploaded_torrents: ""
        ```

    ??? variable string "`rutorrent_role_ru_overwrite_uploaded_torrents`{ .sb-show-on-unchecked }`rutorrent2_ru_overwrite_uploaded_torrents`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Overwrite existing uploaded .torrent files
        # Valid values: "true", "false"
        # Type: string
        rutorrent_role_ru_overwrite_uploaded_torrents: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Overwrite existing uploaded .torrent files
        # Valid values: "true", "false"
        # Type: string
        rutorrent2_ru_overwrite_uploaded_torrents: ""
        ```

    ??? variable string "`rutorrent_role_ru_forbid_user_settings`{ .sb-show-on-unchecked }`rutorrent2_ru_forbid_user_settings`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Allow a single-user style configuration even with web authentication
        # Valid values: "true", "false"
        # Type: string
        rutorrent_role_ru_forbid_user_settings: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Allow a single-user style configuration even with web authentication
        # Valid values: "true", "false"
        # Type: string
        rutorrent2_ru_forbid_user_settings: ""
        ```

    ??? variable string "`rutorrent_role_ru_locale`{ .sb-show-on-unchecked }`rutorrent2_ru_locale`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Default ruTorrent locale
        # Type: string
        rutorrent_role_ru_locale: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Default ruTorrent locale
        # Type: string
        rutorrent2_ru_locale: ""
        ```

=== "Web"

    ??? variable string "`rutorrent_role_web_subdomain`{ .sb-show-on-unchecked }`rutorrent2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_web_subdomain: "{{ rutorrent_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_web_subdomain: "{{ rutorrent_name }}"
        ```

    ??? variable string "`rutorrent_role_web_domain`{ .sb-show-on-unchecked }`rutorrent2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`rutorrent_role_web_port`{ .sb-show-on-unchecked }`rutorrent2_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_web_port: "8080"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_web_port: "8080"
        ```

    ??? variable string "`rutorrent_role_web_url`{ .sb-show-on-unchecked }`rutorrent2_web_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_web_url: "{{ lookup('role_web', role='rutorrent', scheme='https') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_web_url: "{{ lookup('role_web', role='rutorrent', scheme='https') }}"
        ```

    ??? variable string "`rutorrent_role_web_api_port`{ .sb-show-on-unchecked }`rutorrent2_web_api_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_web_api_port: "8000"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_web_api_port: "8000"
        ```

    ??? variable string "`rutorrent_role_webdav_subdomain`{ .sb-show-on-unchecked }`rutorrent2_webdav_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_webdav_subdomain: "{{ rutorrent_name }}-webdav"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_webdav_subdomain: "{{ rutorrent_name }}-webdav"
        ```

    ??? variable string "`rutorrent_role_webdav_domain`{ .sb-show-on-unchecked }`rutorrent2_webdav_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_webdav_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_webdav_domain: "{{ user.domain }}"
        ```

    ??? variable string "`rutorrent_role_webdav_port`{ .sb-show-on-unchecked }`rutorrent2_webdav_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_webdav_port: "9000"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_webdav_port: "9000"
        ```

    ??? variable string "`rutorrent_role_webdav_host`{ .sb-show-on-unchecked }`rutorrent2_webdav_host`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_webdav_host: "{{ lookup('role_web', role='rutorrent', endpoint='webdav') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_webdav_host: "{{ lookup('role_web', role='rutorrent', endpoint='webdav') }}"
        ```

=== "DNS"

    ??? variable string "`rutorrent_role_dns_record`{ .sb-show-on-unchecked }`rutorrent2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='rutorrent') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='rutorrent') }}"
        ```

    ??? variable string "`rutorrent_role_dns_zone`{ .sb-show-on-unchecked }`rutorrent2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='rutorrent') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_dns_zone: "{{ lookup('role_var', '_web_domain', role='rutorrent') }}"
        ```

    ??? variable bool "`rutorrent_role_dns_proxy`{ .sb-show-on-unchecked }`rutorrent2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_dns_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_dns_proxy: "{{ dns_proxied }}"
        ```

    ??? variable string "`rutorrent_role_webdav_dns_record`{ .sb-show-on-unchecked }`rutorrent2_webdav_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_webdav_dns_record: "{{ lookup('role_var', '_webdav_subdomain', role='rutorrent') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_webdav_dns_record: "{{ lookup('role_var', '_webdav_subdomain', role='rutorrent') }}"
        ```

    ??? variable string "`rutorrent_role_webdav_dns_zone`{ .sb-show-on-unchecked }`rutorrent2_webdav_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_webdav_dns_zone: "{{ lookup('role_var', '_webdav_domain', role='rutorrent') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_webdav_dns_zone: "{{ lookup('role_var', '_webdav_domain', role='rutorrent') }}"
        ```

    ??? variable bool "`rutorrent_role_webdav_dns_proxy`{ .sb-show-on-unchecked }`rutorrent2_webdav_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_webdav_dns_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_webdav_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`rutorrent_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`rutorrent2_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`rutorrent_role_traefik_middleware_default`{ .sb-show-on-unchecked }`rutorrent2_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`rutorrent_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`rutorrent2_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_traefik_middleware_custom: ""
        ```

    ??? variable string "`rutorrent_role_traefik_middleware_basicauth`{ .sb-show-on-unchecked }`rutorrent2_traefik_middleware_basicauth`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_traefik_middleware_basicauth: "{{ rutorrent_name }}-auth,{{ traefik_default_middleware_api }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_traefik_middleware_basicauth: "{{ rutorrent_name }}-auth,{{ traefik_default_middleware_api }}"
        ```

    ??? variable string "`rutorrent_role_traefik_middleware_default_api`{ .sb-show-on-unchecked }`rutorrent2_traefik_middleware_default_api`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_traefik_middleware_default_api: "{{ lookup('role_var', '_traefik_middleware_basicauth', role='rutorrent') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_traefik_middleware_default_api: "{{ lookup('role_var', '_traefik_middleware_basicauth', role='rutorrent') }}"
        ```

    ??? variable string "`rutorrent_role_traefik_middleware_custom_api`{ .sb-show-on-unchecked }`rutorrent2_traefik_middleware_custom_api`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_traefik_middleware_custom_api: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_traefik_middleware_custom_api: ""
        ```

    ??? variable string "`rutorrent_role_traefik_certresolver`{ .sb-show-on-unchecked }`rutorrent2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`rutorrent_role_traefik_enabled`{ .sb-show-on-unchecked }`rutorrent2_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_traefik_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_traefik_enabled: true
        ```

    ??? variable bool "`rutorrent_role_traefik_api_enabled`{ .sb-show-on-unchecked }`rutorrent2_traefik_api_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_traefik_api_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_traefik_api_enabled: true
        ```

    ??? variable string "`rutorrent_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`rutorrent2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_traefik_api_endpoint: "PathPrefix(`/RPC`)"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_traefik_api_endpoint: "PathPrefix(`/RPC`)"
        ```

    ??? variable string "`rutorrent_role_traefik_middleware_webdav`{ .sb-show-on-unchecked }`rutorrent2_traefik_middleware_webdav`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_traefik_middleware_webdav: "{{ lookup('role_var', '_traefik_middleware_basicauth', role='rutorrent') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_traefik_middleware_webdav: "{{ lookup('role_var', '_traefik_middleware_basicauth', role='rutorrent') }}"
        ```

    ??? variable string "`rutorrent_role_traefik_certresolver_webdav`{ .sb-show-on-unchecked }`rutorrent2_traefik_certresolver_webdav`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_traefik_certresolver_webdav: "{{ lookup('role_var', '_traefik_certresolver', role='rutorrent') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_traefik_certresolver_webdav: "{{ lookup('role_var', '_traefik_certresolver', role='rutorrent') }}"
        ```

    ??? variable bool "`rutorrent_role_traefik_webdav_enabled`{ .sb-show-on-unchecked }`rutorrent2_traefik_webdav_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_traefik_webdav_enabled: "{{ lookup('role_var', '_webdav_enable', role='rutorrent') | bool }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_traefik_webdav_enabled: "{{ lookup('role_var', '_webdav_enable', role='rutorrent') | bool }}"
        ```

=== "Ports"

    The role allocates the first available port within the inclusive low and high bounds and retains it while it remains within those bounds and free of conflicts.
    Override an instance's bounds to change the allowed range; set both bounds to the same value to require one exact port, including for an existing assignment.

    Existing assignments are stored in `/opt/saltbox/port-assignments.json`. On each role run, a saved port outside the current bounds or in conflict is reassigned within the current bounds, with a warning showing the old port, new port, and reason.
    These bounds also apply to ports manually changed in that file. If no port is available within the bounds, allocation fails without changing the registry.

    ??? variable int "`rutorrent_role_port_dht_low_bound`{ .sb-show-on-unchecked }`rutorrent2_port_dht_low_bound`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rutorrent_role_port_dht_low_bound: "{{ lookup('role_var', '_rt_dht_port', role='rutorrent', default=6881, default_if_empty=true) | int }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rutorrent2_port_dht_low_bound: "{{ lookup('role_var', '_rt_dht_port', role='rutorrent', default=6881, default_if_empty=true) | int }}"
        ```

    ??? variable string "`rutorrent_role_port_dht_high_bound`{ .sb-show-on-unchecked }`rutorrent2_port_dht_high_bound`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_port_dht_high_bound: "{{ lookup('role_var', '_port_dht_low_bound', role='rutorrent') + 10 }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_port_dht_high_bound: "{{ lookup('role_var', '_port_dht_low_bound', role='rutorrent') + 10 }}"
        ```

    ??? variable int "`rutorrent_role_port_peer_low_bound`{ .sb-show-on-unchecked }`rutorrent2_port_peer_low_bound`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rutorrent_role_port_peer_low_bound: "{{ lookup('role_var', '_rt_inc_port', role='rutorrent', default=50000, default_if_empty=true) | int }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rutorrent2_port_peer_low_bound: "{{ lookup('role_var', '_rt_inc_port', role='rutorrent', default=50000, default_if_empty=true) | int }}"
        ```

    ??? variable string "`rutorrent_role_port_peer_high_bound`{ .sb-show-on-unchecked }`rutorrent2_port_peer_high_bound`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_port_peer_high_bound: "{{ lookup('role_var', '_port_peer_low_bound', role='rutorrent') + 10 }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_port_peer_high_bound: "{{ lookup('role_var', '_port_peer_low_bound', role='rutorrent') + 10 }}"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`rutorrent_role_docker_container`{ .sb-show-on-unchecked }`rutorrent2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_container: "{{ rutorrent_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_container: "{{ rutorrent_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`rutorrent_role_docker_image_pull`{ .sb-show-on-unchecked }`rutorrent2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_docker_image_pull: true
        ```

    ??? variable string "`rutorrent_role_docker_image_repo`{ .sb-show-on-unchecked }`rutorrent2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_image_repo: "crazymax/rtorrent-rutorrent"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_image_repo: "crazymax/rtorrent-rutorrent"
        ```

    ??? variable string "`rutorrent_role_docker_image_tag`{ .sb-show-on-unchecked }`rutorrent2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_image_tag: "latest"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_image_tag: "latest"
        ```

    ??? variable string "`rutorrent_role_docker_image`{ .sb-show-on-unchecked }`rutorrent2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='rutorrent') }}:{{ lookup('role_var', '_docker_image_tag', role='rutorrent') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='rutorrent') }}:{{ lookup('role_var', '_docker_image_tag', role='rutorrent') }}"
        ```

    <h5>Ports</h5>

    ??? variable list "`rutorrent_role_docker_ports_default`{ .sb-show-on-unchecked }`rutorrent2_docker_ports_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_ports_default:
          - "{{ rutorrent_port_assignment.ports.peer }}:{{ rutorrent_port_assignment.ports.peer }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_ports_default:
          - "{{ rutorrent_port_assignment.ports.peer }}:{{ rutorrent_port_assignment.ports.peer }}"
        ```

    ??? variable list "`rutorrent_role_docker_ports_dht`{ .sb-show-on-unchecked }`rutorrent2_docker_ports_dht`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_ports_dht:
          - "{{ rutorrent_port_assignment.ports.dht }}:{{ rutorrent_port_assignment.ports.dht }}/udp"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_ports_dht:
          - "{{ rutorrent_port_assignment.ports.dht }}:{{ rutorrent_port_assignment.ports.dht }}/udp"
        ```

    ??? variable list "`rutorrent_role_docker_ports_custom`{ .sb-show-on-unchecked }`rutorrent2_docker_ports_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_ports_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    <h5>Skip docs</h5>

    ??? variable bool "`rutorrent_role_docker_envs_ru_remove_core_plugins`{ .sb-show-on-unchecked }`rutorrent2_docker_envs_ru_remove_core_plugins`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_docker_envs_ru_remove_core_plugins: "{{ lookup('role_var', '_trim_plugins_enable', role='rutorrent') | bool
                                                               | ternary('_cloudflare,autotools,cookies,extsearch,feeds,ipad,loginmgr,rss,rssurlrewrite,rutracker_check,unpack', '')
                                                               | split(',') | union(lookup('role_var', '_ru_remove_core_plugins', role='rutorrent') | split(','))
                                                               | select | map('trim') | join(',') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_docker_envs_ru_remove_core_plugins: "{{ lookup('role_var', '_trim_plugins_enable', role='rutorrent') | bool
                                                           | ternary('_cloudflare,autotools,cookies,extsearch,feeds,ipad,loginmgr,rss,rssurlrewrite,rutracker_check,unpack', '')
                                                           | split(',') | union(lookup('role_var', '_ru_remove_core_plugins', role='rutorrent') | split(','))
                                                           | select | map('trim') | join(',') }}"
        ```

    ??? variable dict "`rutorrent_role_docker_envs_default`{ .sb-show-on-unchecked }`rutorrent2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        rutorrent_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          WAN_IP: "{{ lookup('role_var', '_wan_ip', role='rutorrent', default=omit, default_if_empty=true) }}"
          WAN_IP_CMD: "{{ lookup('role_var', '_wan_ip_cmd', role='rutorrent', default=omit, default_if_empty=true) }}"
          MEMORY_LIMIT: "{{ lookup('role_var', '_memory_limit', role='rutorrent', default=omit, default_if_empty=true) }}"
          UPLOAD_MAX_SIZE: "{{ lookup('role_var', '_upload_max_size', role='rutorrent', default=omit, default_if_empty=true) }}"
          CLEAR_ENV: "{{ lookup('role_var', '_clear_env', role='rutorrent', default=omit, default_if_empty=true) }}"
          OPCACHE_MEM_SIZE: "{{ lookup('role_var', '_opcache_mem_size', role='rutorrent', default=omit, default_if_empty=true) }}"
          MAX_FILE_UPLOADS: "{{ lookup('role_var', '_max_file_uploads', role='rutorrent', default=omit, default_if_empty=true) }}"
          REAL_IP_FROM: "{{ lookup('role_var', '_real_ip_from', role='rutorrent', default=omit, default_if_empty=true) }}"
          REAL_IP_HEADER: "{{ lookup('role_var', '_real_ip_header', role='rutorrent', default=omit, default_if_empty=true) }}"
          LOG_IP_VAR: "{{ lookup('role_var', '_log_ip_var', role='rutorrent', default=omit, default_if_empty=true) }}"
          LOG_ACCESS: "{{ lookup('role_var', '_log_access', role='rutorrent', default=omit, default_if_empty=true) }}"
          XMLRPC_SIZE_LIMIT: "{{ lookup('role_var', '_xmlrpc_size_limit', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_LOG_LEVEL: "{{ lookup('role_var', '_rt_log_level', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_LOG_EXECUTE: "{{ lookup('role_var', '_rt_log_execute', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_LOG_XMLRPC: "{{ lookup('role_var', '_rt_log_xmlrpc', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_SESSION_SAVE_SECONDS: "{{ lookup('role_var', '_rt_session_save_seconds', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_SESSION_FDATASYNC: "{{ lookup('role_var', '_rt_session_fdatasync', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_TRACKER_DELAY_SCRAPE: "{{ lookup('role_var', '_rt_tracker_delay_scrape', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_RECEIVE_BUFFER_SIZE: "{{ lookup('role_var', '_rt_receive_buffer_size', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_SEND_BUFFER_SIZE: "{{ lookup('role_var', '_rt_send_buffer_size', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_PREALLOCATE_TYPE: "{{ lookup('role_var', '_rt_preallocate_type', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_DHT_PORT: "{{ rutorrent_port_assignment.ports.dht | string
                        if (rutorrent_port_assignment.ports.dht | default(6881)) != 6881
                        else omit }}"
          RT_INC_PORT: "{{ rutorrent_port_assignment.ports.peer | string
                        if (rutorrent_port_assignment.ports.peer | default(50000)) != 50000
                        else omit }}"
          RU_REMOVE_CORE_PLUGINS: "{{ lookup('role_var', '_docker_envs_ru_remove_core_plugins', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_HTTP_USER_AGENT: "{{ lookup('role_var', '_ru_http_user_agent', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_HTTP_TIME_OUT: "{{ lookup('role_var', '_ru_http_time_out', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_HTTP_USE_GZIP: "{{ lookup('role_var', '_ru_http_use_gzip', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_HTTP_VERIFY_CERTIFICATES: "{{ lookup('role_var', '_ru_http_verify_certificates', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_RPC_TIME_OUT: "{{ lookup('role_var', '_ru_rpc_time_out', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_LOG_RPC_CALLS: "{{ lookup('role_var', '_ru_log_rpc_calls', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_LOG_RPC_FAULTS: "{{ lookup('role_var', '_ru_log_rpc_faults', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_PHP_USE_GZIP: "{{ lookup('role_var', '_ru_php_use_gzip', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_PHP_GZIP_LEVEL: "{{ lookup('role_var', '_ru_php_gzip_level', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_SCHEDULE_RAND: "{{ lookup('role_var', '_ru_schedule_rand', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_LOG_FILE: "{{ lookup('role_var', '_ru_log_file', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_DO_DIAGNOSTIC: "{{ lookup('role_var', '_ru_do_diagnostic', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_CACHED_PLUGIN_LOADING: "{{ lookup('role_var', '_ru_cached_plugin_loading', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_SAVE_UPLOADED_TORRENTS: "{{ lookup('role_var', '_ru_save_uploaded_torrents', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_OVERWRITE_UPLOADED_TORRENTS: "{{ lookup('role_var', '_ru_overwrite_uploaded_torrents', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_FORBID_USER_SETTINGS: "{{ lookup('role_var', '_ru_forbid_user_settings', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_LOCALE: "{{ lookup('role_var', '_ru_locale', role='rutorrent', default=omit, default_if_empty=true) }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        rutorrent2_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          WAN_IP: "{{ lookup('role_var', '_wan_ip', role='rutorrent', default=omit, default_if_empty=true) }}"
          WAN_IP_CMD: "{{ lookup('role_var', '_wan_ip_cmd', role='rutorrent', default=omit, default_if_empty=true) }}"
          MEMORY_LIMIT: "{{ lookup('role_var', '_memory_limit', role='rutorrent', default=omit, default_if_empty=true) }}"
          UPLOAD_MAX_SIZE: "{{ lookup('role_var', '_upload_max_size', role='rutorrent', default=omit, default_if_empty=true) }}"
          CLEAR_ENV: "{{ lookup('role_var', '_clear_env', role='rutorrent', default=omit, default_if_empty=true) }}"
          OPCACHE_MEM_SIZE: "{{ lookup('role_var', '_opcache_mem_size', role='rutorrent', default=omit, default_if_empty=true) }}"
          MAX_FILE_UPLOADS: "{{ lookup('role_var', '_max_file_uploads', role='rutorrent', default=omit, default_if_empty=true) }}"
          REAL_IP_FROM: "{{ lookup('role_var', '_real_ip_from', role='rutorrent', default=omit, default_if_empty=true) }}"
          REAL_IP_HEADER: "{{ lookup('role_var', '_real_ip_header', role='rutorrent', default=omit, default_if_empty=true) }}"
          LOG_IP_VAR: "{{ lookup('role_var', '_log_ip_var', role='rutorrent', default=omit, default_if_empty=true) }}"
          LOG_ACCESS: "{{ lookup('role_var', '_log_access', role='rutorrent', default=omit, default_if_empty=true) }}"
          XMLRPC_SIZE_LIMIT: "{{ lookup('role_var', '_xmlrpc_size_limit', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_LOG_LEVEL: "{{ lookup('role_var', '_rt_log_level', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_LOG_EXECUTE: "{{ lookup('role_var', '_rt_log_execute', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_LOG_XMLRPC: "{{ lookup('role_var', '_rt_log_xmlrpc', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_SESSION_SAVE_SECONDS: "{{ lookup('role_var', '_rt_session_save_seconds', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_SESSION_FDATASYNC: "{{ lookup('role_var', '_rt_session_fdatasync', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_TRACKER_DELAY_SCRAPE: "{{ lookup('role_var', '_rt_tracker_delay_scrape', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_RECEIVE_BUFFER_SIZE: "{{ lookup('role_var', '_rt_receive_buffer_size', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_SEND_BUFFER_SIZE: "{{ lookup('role_var', '_rt_send_buffer_size', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_PREALLOCATE_TYPE: "{{ lookup('role_var', '_rt_preallocate_type', role='rutorrent', default=omit, default_if_empty=true) }}"
          RT_DHT_PORT: "{{ rutorrent_port_assignment.ports.dht | string
                        if (rutorrent_port_assignment.ports.dht | default(6881)) != 6881
                        else omit }}"
          RT_INC_PORT: "{{ rutorrent_port_assignment.ports.peer | string
                        if (rutorrent_port_assignment.ports.peer | default(50000)) != 50000
                        else omit }}"
          RU_REMOVE_CORE_PLUGINS: "{{ lookup('role_var', '_docker_envs_ru_remove_core_plugins', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_HTTP_USER_AGENT: "{{ lookup('role_var', '_ru_http_user_agent', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_HTTP_TIME_OUT: "{{ lookup('role_var', '_ru_http_time_out', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_HTTP_USE_GZIP: "{{ lookup('role_var', '_ru_http_use_gzip', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_HTTP_VERIFY_CERTIFICATES: "{{ lookup('role_var', '_ru_http_verify_certificates', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_RPC_TIME_OUT: "{{ lookup('role_var', '_ru_rpc_time_out', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_LOG_RPC_CALLS: "{{ lookup('role_var', '_ru_log_rpc_calls', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_LOG_RPC_FAULTS: "{{ lookup('role_var', '_ru_log_rpc_faults', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_PHP_USE_GZIP: "{{ lookup('role_var', '_ru_php_use_gzip', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_PHP_GZIP_LEVEL: "{{ lookup('role_var', '_ru_php_gzip_level', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_SCHEDULE_RAND: "{{ lookup('role_var', '_ru_schedule_rand', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_LOG_FILE: "{{ lookup('role_var', '_ru_log_file', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_DO_DIAGNOSTIC: "{{ lookup('role_var', '_ru_do_diagnostic', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_CACHED_PLUGIN_LOADING: "{{ lookup('role_var', '_ru_cached_plugin_loading', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_SAVE_UPLOADED_TORRENTS: "{{ lookup('role_var', '_ru_save_uploaded_torrents', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_OVERWRITE_UPLOADED_TORRENTS: "{{ lookup('role_var', '_ru_overwrite_uploaded_torrents', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_FORBID_USER_SETTINGS: "{{ lookup('role_var', '_ru_forbid_user_settings', role='rutorrent', default=omit, default_if_empty=true) }}"
          RU_LOCALE: "{{ lookup('role_var', '_ru_locale', role='rutorrent', default=omit, default_if_empty=true) }}"
        ```

    ??? variable dict "`rutorrent_role_docker_envs_custom`{ .sb-show-on-unchecked }`rutorrent2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        rutorrent_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        rutorrent2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable bool "`rutorrent_role_docker_volumes_download`{ .sb-show-on-unchecked }`rutorrent2_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_docker_volumes_download: false
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_docker_volumes_download: false
        ```

    ??? variable list "`rutorrent_role_docker_volumes_default`{ .sb-show-on-unchecked }`rutorrent2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='rutorrent') }}:/data"
          - "{{ lookup('role_var', '_paths_downloads_location', role='rutorrent') }}:/downloads"
          - "{{ lookup('role_var', '_paths_location', role='rutorrent') }}/passwd:/passwd"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='rutorrent') }}:/data"
          - "{{ lookup('role_var', '_paths_downloads_location', role='rutorrent') }}:/downloads"
          - "{{ lookup('role_var', '_paths_location', role='rutorrent') }}/passwd:/passwd"
        ```

    ??? variable list "`rutorrent_role_docker_volumes_custom`{ .sb-show-on-unchecked }`rutorrent2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable list "`rutorrent_role_docker_labels_default`{ .sb-show-on-unchecked }`rutorrent2_docker_labels_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_labels_default:
          - '{ "traefik.http.middlewares.{{ rutorrent_name }}-auth.basicauth.usersfile": "/etc/traefik/auth" }'
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_labels_default:
          - '{ "traefik.http.middlewares.{{ rutorrent_name }}-auth.basicauth.usersfile": "/etc/traefik/auth" }'
        ```

    ??? variable list "`rutorrent_role_docker_labels_webdav_template`{ .sb-show-on-unchecked }`rutorrent2_docker_labels_webdav_template`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_labels_webdav_template:
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav-http.entrypoints": "{{ traefik_entrypoint_web }}" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav-http.service": "{{ rutorrent_name }}-webdav" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav-http.rule": "Host(`{{ lookup("role_var", "_webdav_host", role="rutorrent") }}`)" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav-http.middlewares": "{{ traefik_default_middleware_http_api }}" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav-http.priority": "20" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav.entrypoints": "{{ traefik_entrypoint_websecure }}" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav.service": "{{ rutorrent_name }}-webdav" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav.rule": "Host(`{{ lookup("role_var", "_webdav_host", role="rutorrent") }}`)" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav.tls.options": "securetls@file" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav.tls.certresolver": "{{ rutorrent_role_docker_labels_webdav_certificate_plan_lookup.certresolver }}" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav.middlewares": "{{ lookup("role_var", "_traefik_middleware_webdav", role="rutorrent") }}" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav.priority": "20" }'
          - '{ "traefik.http.services.{{ rutorrent_name }}-webdav.loadbalancer.server.port": "{{ lookup("role_var", "_webdav_port", role="rutorrent") }}" }'
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_labels_webdav_template:
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav-http.entrypoints": "{{ traefik_entrypoint_web }}" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav-http.service": "{{ rutorrent_name }}-webdav" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav-http.rule": "Host(`{{ lookup("role_var", "_webdav_host", role="rutorrent") }}`)" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav-http.middlewares": "{{ traefik_default_middleware_http_api }}" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav-http.priority": "20" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav.entrypoints": "{{ traefik_entrypoint_websecure }}" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav.service": "{{ rutorrent_name }}-webdav" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav.rule": "Host(`{{ lookup("role_var", "_webdav_host", role="rutorrent") }}`)" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav.tls.options": "securetls@file" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav.tls.certresolver": "{{ rutorrent_role_docker_labels_webdav_certificate_plan_lookup.certresolver }}" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav.middlewares": "{{ lookup("role_var", "_traefik_middleware_webdav", role="rutorrent") }}" }'
          - '{ "traefik.http.routers.{{ rutorrent_name }}-webdav.priority": "20" }'
          - '{ "traefik.http.services.{{ rutorrent_name }}-webdav.loadbalancer.server.port": "{{ lookup("role_var", "_webdav_port", role="rutorrent") }}" }'
        ```

    ??? variable string "`rutorrent_role_docker_labels_webdav_certificate_domains`{ .sb-show-on-unchecked }`rutorrent2_docker_labels_webdav_certificate_domains`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_labels_webdav_certificate_domains: "{{ rutorrent_role_docker_labels_webdav_certificate_plan_lookup.domains }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_labels_webdav_certificate_domains: "{{ rutorrent_role_docker_labels_webdav_certificate_plan_lookup.domains }}"
        ```

    ??? variable dict "`rutorrent_role_docker_labels_webdav_certificates`{ .sb-show-on-unchecked }`rutorrent2_docker_labels_webdav_certificates`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        rutorrent_role_docker_labels_webdav_certificates: "{{ rutorrent_role_docker_labels_webdav_certificate_domains
                                                              | traefik_certificate_labels(rutorrent_name + '-webdav') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        rutorrent2_docker_labels_webdav_certificates: "{{ rutorrent_role_docker_labels_webdav_certificate_domains
                                                          | traefik_certificate_labels(rutorrent_name + '-webdav') }}"
        ```

    ??? variable dict "`rutorrent_role_docker_labels_webdav`{ .sb-show-on-unchecked }`rutorrent2_docker_labels_webdav`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        rutorrent_role_docker_labels_webdav: "{{ ((rutorrent_role_docker_labels_webdav_template | map('from_json') | combine)
                                                  | combine(rutorrent_role_docker_labels_webdav_certificates))
                                              if (lookup('role_var', '_traefik_webdav_enabled', role='rutorrent') | bool)
                                              else {} }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        rutorrent2_docker_labels_webdav: "{{ ((rutorrent_role_docker_labels_webdav_template | map('from_json') | combine)
                                              | combine(rutorrent_role_docker_labels_webdav_certificates))
                                          if (lookup('role_var', '_traefik_webdav_enabled', role='rutorrent') | bool)
                                          else {} }}"
        ```

    ??? variable dict "`rutorrent_role_docker_labels_custom`{ .sb-show-on-unchecked }`rutorrent2_docker_labels_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        rutorrent_role_docker_labels_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        rutorrent2_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`rutorrent_role_docker_hostname`{ .sb-show-on-unchecked }`rutorrent2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_hostname: "{{ rutorrent_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_hostname: "{{ rutorrent_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`rutorrent_role_docker_networks_alias`{ .sb-show-on-unchecked }`rutorrent2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_networks_alias: "{{ rutorrent_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_networks_alias: "{{ rutorrent_name }}"
        ```

    ??? variable list "`rutorrent_role_docker_networks_default`{ .sb-show-on-unchecked }`rutorrent2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_networks_default: []
        ```

    ??? variable list "`rutorrent_role_docker_networks_custom`{ .sb-show-on-unchecked }`rutorrent2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`rutorrent_role_docker_restart_policy`{ .sb-show-on-unchecked }`rutorrent2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_restart_policy: unless-stopped
        ```

    <h5>Stop Timeout</h5>

    ??? variable int "`rutorrent_role_docker_stop_timeout`{ .sb-show-on-unchecked }`rutorrent2_docker_stop_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rutorrent_role_docker_stop_timeout: 10
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rutorrent2_docker_stop_timeout: 10
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    A blank value is YAML null and inherits any lower-precedence role or shared default. Explicit Ansible omit is accepted only for optional Docker settings; default-backed and required settings reject it. Use the documented typed empty value, such as `""`, `[]`, or `{}`, when disabling a guaranteed setting.

    <h5>GPU</h5>

    ??? variable bool "`rutorrent_role_docker_gpu_enabled`{ .sb-show-on-unchecked }`rutorrent2_docker_gpu_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Set this to true to let the app use a GPU.
        # Intel access also requires gpu.intel: true.
        # NVIDIA access also requires nvidia_enabled: true.
        # This setting does not install or enable GPU support on the server.
        # Type: bool (true/false)
        rutorrent_role_docker_gpu_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Set this to true to let the app use a GPU.
        # Intel access also requires gpu.intel: true.
        # NVIDIA access also requires nvidia_enabled: true.
        # This setting does not install or enable GPU support on the server.
        # Type: bool (true/false)
        rutorrent2_docker_gpu_enabled: false
        ```

    ??? variable bool "`rutorrent_role_docker_nvidia_disabled`{ .sb-show-on-unchecked }`rutorrent2_docker_nvidia_disabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Set this to true to turn off automatic NVIDIA access for this app.
        # It only has an effect when the app's _docker_gpu_enabled option and
        # nvidia_enabled are both true.
        # Automatic /dev/dri access may remain.
        # Type: bool (true/false)
        rutorrent_role_docker_nvidia_disabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Set this to true to turn off automatic NVIDIA access for this app.
        # It only has an effect when the app's _docker_gpu_enabled option and
        # nvidia_enabled are both true.
        # Automatic /dev/dri access may remain.
        # Type: bool (true/false)
        rutorrent2_docker_nvidia_disabled: false
        ```

    ??? variable bool "`rutorrent_role_docker_dev_dri_disabled`{ .sb-show-on-unchecked }`rutorrent2_docker_dev_dri_disabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Set this to true to stop Saltbox from automatically sharing the
        # server's /dev/dri video devices with this app.
        # It only has an effect when the app's _docker_gpu_enabled option is true
        # and either gpu.intel or nvidia_enabled is true.
        # NVIDIA-specific access may remain.
        # Type: bool (true/false)
        rutorrent_role_docker_dev_dri_disabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Set this to true to stop Saltbox from automatically sharing the
        # server's /dev/dri video devices with this app.
        # It only has an effect when the app's _docker_gpu_enabled option is true
        # and either gpu.intel or nvidia_enabled is true.
        # NVIDIA-specific access may remain.
        # Type: bool (true/false)
        rutorrent2_docker_dev_dri_disabled: false
        ```

    <h5>Resource Limits</h5>

    ??? variable int "`rutorrent_role_docker_blkio_weight`{ .sb-show-on-unchecked }`rutorrent2_docker_blkio_weight`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rutorrent_role_docker_blkio_weight:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rutorrent2_docker_blkio_weight:
        ```

    ??? variable int "`rutorrent_role_docker_cpu_period`{ .sb-show-on-unchecked }`rutorrent2_docker_cpu_period`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rutorrent_role_docker_cpu_period:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rutorrent2_docker_cpu_period:
        ```

    ??? variable int "`rutorrent_role_docker_cpu_quota`{ .sb-show-on-unchecked }`rutorrent2_docker_cpu_quota`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rutorrent_role_docker_cpu_quota:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rutorrent2_docker_cpu_quota:
        ```

    ??? variable int "`rutorrent_role_docker_cpu_shares`{ .sb-show-on-unchecked }`rutorrent2_docker_cpu_shares`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rutorrent_role_docker_cpu_shares:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rutorrent2_docker_cpu_shares:
        ```

    ??? variable string "`rutorrent_role_docker_cpus`{ .sb-show-on-unchecked }`rutorrent2_docker_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # CPU allocation accepted as a numeric string, such as 1.5
        # Type: string (quoted number)
        rutorrent_role_docker_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # CPU allocation accepted as a numeric string, such as 1.5
        # Type: string (quoted number)
        rutorrent2_docker_cpus:
        ```

    ??? variable string "`rutorrent_role_docker_cpuset_cpus`{ .sb-show-on-unchecked }`rutorrent2_docker_cpuset_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_cpuset_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_cpuset_cpus:
        ```

    ??? variable string "`rutorrent_role_docker_cpuset_mems`{ .sb-show-on-unchecked }`rutorrent2_docker_cpuset_mems`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_cpuset_mems:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_cpuset_mems:
        ```

    ??? variable string "`rutorrent_role_docker_kernel_memory`{ .sb-show-on-unchecked }`rutorrent2_docker_kernel_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_kernel_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_kernel_memory:
        ```

    ??? variable string "`rutorrent_role_docker_memory`{ .sb-show-on-unchecked }`rutorrent2_docker_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_memory:
        ```

    ??? variable string "`rutorrent_role_docker_memory_reservation`{ .sb-show-on-unchecked }`rutorrent2_docker_memory_reservation`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_memory_reservation:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_memory_reservation:
        ```

    ??? variable string "`rutorrent_role_docker_memory_swap`{ .sb-show-on-unchecked }`rutorrent2_docker_memory_swap`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_memory_swap:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_memory_swap:
        ```

    ??? variable int "`rutorrent_role_docker_memory_swappiness`{ .sb-show-on-unchecked }`rutorrent2_docker_memory_swappiness`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rutorrent_role_docker_memory_swappiness:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rutorrent2_docker_memory_swappiness:
        ```

    ??? variable string "`rutorrent_role_docker_shm_size`{ .sb-show-on-unchecked }`rutorrent2_docker_shm_size`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_shm_size:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`rutorrent_role_docker_cap_drop`{ .sb-show-on-unchecked }`rutorrent2_docker_cap_drop`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_cap_drop:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_cap_drop:
        ```

    ??? variable string "`rutorrent_role_docker_cgroupns_mode`{ .sb-show-on-unchecked }`rutorrent2_docker_cgroupns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_cgroupns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_cgroupns_mode:
        ```

    ??? variable list "`rutorrent_role_docker_device_cgroup_rules`{ .sb-show-on-unchecked }`rutorrent2_docker_device_cgroup_rules`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_device_cgroup_rules:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_device_cgroup_rules:
        ```

    ??? variable list "`rutorrent_role_docker_device_read_bps`{ .sb-show-on-unchecked }`rutorrent2_docker_device_read_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_device_read_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_device_read_bps:
        ```

    ??? variable list "`rutorrent_role_docker_device_read_iops`{ .sb-show-on-unchecked }`rutorrent2_docker_device_read_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_device_read_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_device_read_iops:
        ```

    ??? variable list "`rutorrent_role_docker_device_requests`{ .sb-show-on-unchecked }`rutorrent2_docker_device_requests`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_device_requests:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_device_requests:
        ```

    ??? variable list "`rutorrent_role_docker_device_write_bps`{ .sb-show-on-unchecked }`rutorrent2_docker_device_write_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_device_write_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_device_write_bps:
        ```

    ??? variable list "`rutorrent_role_docker_device_write_iops`{ .sb-show-on-unchecked }`rutorrent2_docker_device_write_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_device_write_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_device_write_iops:
        ```

    ??? variable list "`rutorrent_role_docker_devices`{ .sb-show-on-unchecked }`rutorrent2_docker_devices`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_devices:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_devices:
        ```

    ??? variable list "`rutorrent_role_docker_groups`{ .sb-show-on-unchecked }`rutorrent2_docker_groups`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_groups:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_groups:
        ```

    ??? variable bool "`rutorrent_role_docker_privileged`{ .sb-show-on-unchecked }`rutorrent2_docker_privileged`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_docker_privileged:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_docker_privileged:
        ```

    ??? variable list "`rutorrent_role_docker_security_opts`{ .sb-show-on-unchecked }`rutorrent2_docker_security_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_security_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_security_opts:
        ```

    ??? variable string "`rutorrent_role_docker_user`{ .sb-show-on-unchecked }`rutorrent2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_user:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_user:
        ```

    ??? variable string "`rutorrent_role_docker_userns_mode`{ .sb-show-on-unchecked }`rutorrent2_docker_userns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_userns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`rutorrent_role_docker_dns_opts`{ .sb-show-on-unchecked }`rutorrent2_docker_dns_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_dns_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_dns_opts:
        ```

    ??? variable list "`rutorrent_role_docker_dns_search_domains`{ .sb-show-on-unchecked }`rutorrent2_docker_dns_search_domains`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_dns_search_domains:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_dns_search_domains:
        ```

    ??? variable list "`rutorrent_role_docker_dns_servers`{ .sb-show-on-unchecked }`rutorrent2_docker_dns_servers`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_dns_servers:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_dns_servers:
        ```

    ??? variable string "`rutorrent_role_docker_domainname`{ .sb-show-on-unchecked }`rutorrent2_docker_domainname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_domainname:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_domainname:
        ```

    ??? variable list "`rutorrent_role_docker_exposed_ports`{ .sb-show-on-unchecked }`rutorrent2_docker_exposed_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_exposed_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_exposed_ports:
        ```

    ??? variable dict "`rutorrent_role_docker_hosts`{ .sb-show-on-unchecked }`rutorrent2_docker_hosts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        rutorrent_role_docker_hosts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        rutorrent2_docker_hosts:
        ```

    ??? variable bool "`rutorrent_role_docker_hosts_use_common`{ .sb-show-on-unchecked }`rutorrent2_docker_hosts_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_docker_hosts_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_docker_hosts_use_common:
        ```

    ??? variable string "`rutorrent_role_docker_ipc_mode`{ .sb-show-on-unchecked }`rutorrent2_docker_ipc_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_ipc_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_ipc_mode:
        ```

    ??? variable list "`rutorrent_role_docker_links`{ .sb-show-on-unchecked }`rutorrent2_docker_links`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_links:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_links:
        ```

    ??? variable string "`rutorrent_role_docker_network_mode`{ .sb-show-on-unchecked }`rutorrent2_docker_network_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_network_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_network_mode:
        ```

    ??? variable string "`rutorrent_role_docker_pid_mode`{ .sb-show-on-unchecked }`rutorrent2_docker_pid_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_pid_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_pid_mode:
        ```

    ??? variable string "`rutorrent_role_docker_uts`{ .sb-show-on-unchecked }`rutorrent2_docker_uts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_uts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`rutorrent_role_docker_keep_volumes`{ .sb-show-on-unchecked }`rutorrent2_docker_keep_volumes`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_docker_keep_volumes:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_docker_keep_volumes:
        ```

    ??? variable list "`rutorrent_role_docker_mounts`{ .sb-show-on-unchecked }`rutorrent2_docker_mounts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_mounts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_mounts:
        ```

    ??? variable dict "`rutorrent_role_docker_storage_opts`{ .sb-show-on-unchecked }`rutorrent2_docker_storage_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        rutorrent_role_docker_storage_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        rutorrent2_docker_storage_opts:
        ```

    ??? variable list "`rutorrent_role_docker_tmpfs`{ .sb-show-on-unchecked }`rutorrent2_docker_tmpfs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_tmpfs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_tmpfs:
        ```

    ??? variable string "`rutorrent_role_docker_volume_driver`{ .sb-show-on-unchecked }`rutorrent2_docker_volume_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_volume_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_volume_driver:
        ```

    ??? variable list "`rutorrent_role_docker_volumes_from`{ .sb-show-on-unchecked }`rutorrent2_docker_volumes_from`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_volumes_from:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_volumes_from:
        ```

    ??? variable bool "`rutorrent_role_docker_volumes_global`{ .sb-show-on-unchecked }`rutorrent2_docker_volumes_global`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_docker_volumes_global:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_docker_volumes_global:
        ```

    ??? variable string "`rutorrent_role_docker_working_dir`{ .sb-show-on-unchecked }`rutorrent2_docker_working_dir`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_working_dir:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`rutorrent_role_docker_auto_remove`{ .sb-show-on-unchecked }`rutorrent2_docker_auto_remove`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_docker_auto_remove:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_docker_auto_remove:
        ```

    ??? variable bool "`rutorrent_role_docker_cleanup`{ .sb-show-on-unchecked }`rutorrent2_docker_cleanup`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_docker_cleanup:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_docker_cleanup:
        ```

    ??? variable bool "`rutorrent_role_docker_force_kill`{ .sb-show-on-unchecked }`rutorrent2_docker_force_kill`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_docker_force_kill:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_docker_force_kill:
        ```

    ??? variable dict "`rutorrent_role_docker_healthcheck`{ .sb-show-on-unchecked }`rutorrent2_docker_healthcheck`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        rutorrent_role_docker_healthcheck:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        rutorrent2_docker_healthcheck:
        ```

    ??? variable int "`rutorrent_role_docker_healthy_wait_timeout`{ .sb-show-on-unchecked }`rutorrent2_docker_healthy_wait_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Healthy-state wait timeout in seconds
        # Type: int
        rutorrent_role_docker_healthy_wait_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Healthy-state wait timeout in seconds
        # Type: int
        rutorrent2_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`rutorrent_role_docker_init`{ .sb-show-on-unchecked }`rutorrent2_docker_init`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_docker_init:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_docker_init:
        ```

    ??? variable string "`rutorrent_role_docker_kill_signal`{ .sb-show-on-unchecked }`rutorrent2_docker_kill_signal`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_kill_signal:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_kill_signal:
        ```

    ??? variable string "`rutorrent_role_docker_log_driver`{ .sb-show-on-unchecked }`rutorrent2_docker_log_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_log_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_log_driver:
        ```

    ??? variable dict "`rutorrent_role_docker_log_options`{ .sb-show-on-unchecked }`rutorrent2_docker_log_options`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        rutorrent_role_docker_log_options:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        rutorrent2_docker_log_options:
        ```

    ??? variable bool "`rutorrent_role_docker_oom_killer`{ .sb-show-on-unchecked }`rutorrent2_docker_oom_killer`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_docker_oom_killer:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_docker_oom_killer:
        ```

    ??? variable int "`rutorrent_role_docker_oom_score_adj`{ .sb-show-on-unchecked }`rutorrent2_docker_oom_score_adj`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rutorrent_role_docker_oom_score_adj:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rutorrent2_docker_oom_score_adj:
        ```

    ??? variable bool "`rutorrent_role_docker_output_logs`{ .sb-show-on-unchecked }`rutorrent2_docker_output_logs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_docker_output_logs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_docker_output_logs:
        ```

    ??? variable bool "`rutorrent_role_docker_paused`{ .sb-show-on-unchecked }`rutorrent2_docker_paused`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_docker_paused:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_docker_paused:
        ```

    ??? variable bool "`rutorrent_role_docker_recreate`{ .sb-show-on-unchecked }`rutorrent2_docker_recreate`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_docker_recreate:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_docker_recreate:
        ```

    ??? variable int "`rutorrent_role_docker_restart_retries`{ .sb-show-on-unchecked }`rutorrent2_docker_restart_retries`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rutorrent_role_docker_restart_retries:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rutorrent2_docker_restart_retries:
        ```

    ??? variable string "`rutorrent_role_docker_stop_signal`{ .sb-show-on-unchecked }`rutorrent2_docker_stop_signal`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_stop_signal:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_stop_signal:
        ```

    <h5>Other Options</h5>

    ??? variable list "`rutorrent_role_docker_capabilities`{ .sb-show-on-unchecked }`rutorrent2_docker_capabilities`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_capabilities:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_capabilities:
        ```

    ??? variable string "`rutorrent_role_docker_cgroup_parent`{ .sb-show-on-unchecked }`rutorrent2_docker_cgroup_parent`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_cgroup_parent:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_cgroup_parent:
        ```

    ??? variable list "`rutorrent_role_docker_commands`{ .sb-show-on-unchecked }`rutorrent2_docker_commands`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_commands:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_commands:
        ```

    ??? variable int "`rutorrent_role_docker_create_timeout`{ .sb-show-on-unchecked }`rutorrent2_docker_create_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        rutorrent_role_docker_create_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        rutorrent2_docker_create_timeout:
        ```

    ??? variable list "`rutorrent_role_docker_entrypoint`{ .sb-show-on-unchecked }`rutorrent2_docker_entrypoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_entrypoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_entrypoint:
        ```

    ??? variable string "`rutorrent_role_docker_env_file`{ .sb-show-on-unchecked }`rutorrent2_docker_env_file`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_env_file:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_env_file:
        ```

    ??? variable bool "`rutorrent_role_docker_labels_use_common`{ .sb-show-on-unchecked }`rutorrent2_docker_labels_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_docker_labels_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_docker_labels_use_common:
        ```

    ??? variable bool "`rutorrent_role_docker_read_only`{ .sb-show-on-unchecked }`rutorrent2_docker_read_only`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_docker_read_only:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_docker_read_only:
        ```

    ??? variable string "`rutorrent_role_docker_runtime`{ .sb-show-on-unchecked }`rutorrent2_docker_runtime`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_docker_runtime:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_docker_runtime:
        ```

    ??? variable dict "`rutorrent_role_docker_sysctls`{ .sb-show-on-unchecked }`rutorrent2_docker_sysctls`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        rutorrent_role_docker_sysctls:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        rutorrent2_docker_sysctls:
        ```

    ??? variable list "`rutorrent_role_docker_ulimits`{ .sb-show-on-unchecked }`rutorrent2_docker_ulimits`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_ulimits:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`rutorrent_role_autoheal_enabled`{ .sb-show-on-unchecked }`rutorrent2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        rutorrent_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        rutorrent2_autoheal_enabled: true
        ```

    ??? variable string "`rutorrent_role_depends_on`{ .sb-show-on-unchecked }`rutorrent2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        rutorrent_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        rutorrent2_depends_on: ""
        ```

    ??? variable string "`rutorrent_role_depends_on_delay`{ .sb-show-on-unchecked }`rutorrent2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        rutorrent_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        rutorrent2_depends_on_delay: "0"
        ```

    ??? variable string "`rutorrent_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`rutorrent2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        rutorrent_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        rutorrent2_depends_on_healthchecks:
        ```

    ??? variable bool "`rutorrent_role_diun_enabled`{ .sb-show-on-unchecked }`rutorrent2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        rutorrent_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        rutorrent2_diun_enabled: true
        ```

    ??? variable bool "`rutorrent_role_dns_enabled`{ .sb-show-on-unchecked }`rutorrent2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        rutorrent_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        rutorrent2_dns_enabled: true
        ```

    ??? variable bool "`rutorrent_role_docker_controller`{ .sb-show-on-unchecked }`rutorrent2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        rutorrent_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        rutorrent2_docker_controller: true
        ```

    ??? variable list "`rutorrent_role_docker_networks_alias_custom`{ .sb-show-on-unchecked }`rutorrent2_docker_networks_alias_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        rutorrent_role_docker_networks_alias_custom:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        rutorrent2_docker_networks_alias_custom:
        ```

    ??? variable list "`rutorrent_role_paths_folders_list_custom`{ .sb-show-on-unchecked }`rutorrent2_paths_folders_list_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Extra directories to create
        # Type: list
        rutorrent_role_paths_folders_list_custom:
        ```

        ```yaml { .sb-show-on-checked }
        # Extra directories to create
        # Type: list
        rutorrent2_paths_folders_list_custom:
        ```

    ??? variable string "`rutorrent_role_paths_group`{ .sb-show-on-unchecked }`rutorrent2_paths_group`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Group for directories created by the role
        # Type: string
        rutorrent_role_paths_group:
        ```

        ```yaml { .sb-show-on-checked }
        # Group for directories created by the role
        # Type: string
        rutorrent2_paths_group:
        ```

    ??? variable string "`rutorrent_role_paths_owner`{ .sb-show-on-unchecked }`rutorrent2_paths_owner`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Owner for directories created by the role
        # Type: string
        rutorrent_role_paths_owner:
        ```

        ```yaml { .sb-show-on-checked }
        # Owner for directories created by the role
        # Type: string
        rutorrent2_paths_owner:
        ```

    ??? variable string "`rutorrent_role_paths_permissions`{ .sb-show-on-unchecked }`rutorrent2_paths_permissions`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Permissions for directories created by the role
        # Type: string
        rutorrent_role_paths_permissions:
        ```

        ```yaml { .sb-show-on-checked }
        # Permissions for directories created by the role
        # Type: string
        rutorrent2_paths_permissions:
        ```

    ??? variable bool "`rutorrent_role_paths_recursive`{ .sb-show-on-unchecked }`rutorrent2_paths_recursive`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Apply owner and group recursively without changing child modes
        # Type: bool (true/false)
        rutorrent_role_paths_recursive:
        ```

        ```yaml { .sb-show-on-checked }
        # Apply owner and group recursively without changing child modes
        # Type: bool (true/false)
        rutorrent2_paths_recursive:
        ```

    ??? variable list "`rutorrent_role_themepark_addons`{ .sb-show-on-unchecked }`rutorrent2_themepark_addons`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # ThemePark addon names to enable
        # Type: list
        rutorrent_role_themepark_addons:
        ```

        ```yaml { .sb-show-on-checked }
        # ThemePark addon names to enable
        # Type: list
        rutorrent2_themepark_addons:
        ```

    ??? variable string "`rutorrent_role_themepark_app`{ .sb-show-on-unchecked }`rutorrent2_themepark_app`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_themepark_app:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_themepark_app:
        ```

    ??? variable string "`rutorrent_role_themepark_theme`{ .sb-show-on-unchecked }`rutorrent2_themepark_theme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_themepark_theme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_themepark_theme:
        ```

    ??? variable string "`rutorrent_role_traefik_api_middleware_http`{ .sb-show-on-unchecked }`rutorrent2_traefik_api_middleware_http`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_traefik_api_middleware_http:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_traefik_api_middleware_http:
        ```

    ??? variable bool "`rutorrent_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`rutorrent2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        rutorrent_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        rutorrent2_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`rutorrent_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`rutorrent2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        rutorrent_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        rutorrent2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`rutorrent_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`rutorrent2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        rutorrent_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        rutorrent2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`rutorrent_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`rutorrent2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        rutorrent_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        rutorrent2_traefik_gzip_enabled: false
        ```

    ??? variable string "`rutorrent_role_traefik_middleware_http`{ .sb-show-on-unchecked }`rutorrent2_traefik_middleware_http`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_traefik_middleware_http:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_traefik_middleware_http:
        ```

    ??? variable bool "`rutorrent_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`rutorrent2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`rutorrent_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`rutorrent2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        rutorrent_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        rutorrent2_traefik_middleware_http_insecure:
        ```

    ??? variable string "`rutorrent_role_traefik_priority`{ .sb-show-on-unchecked }`rutorrent2_traefik_priority`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        rutorrent_role_traefik_priority:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        rutorrent2_traefik_priority:
        ```

    ??? variable bool "`rutorrent_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`rutorrent2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        rutorrent_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        rutorrent2_traefik_robot_enabled: true
        ```

    ??? variable bool "`rutorrent_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`rutorrent2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        rutorrent_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        rutorrent2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`rutorrent_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`rutorrent2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        rutorrent_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        rutorrent2_traefik_wildcard_enabled: true
        ```

    ??? variable string "`rutorrent_role_web_api_http_port`{ .sb-show-on-unchecked }`rutorrent2_web_api_http_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        rutorrent_role_web_api_http_port:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        rutorrent2_web_api_http_port:
        ```

    ??? variable string "`rutorrent_role_web_api_http_scheme`{ .sb-show-on-unchecked }`rutorrent2_web_api_http_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string ("http"/"https")
        rutorrent_role_web_api_http_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string ("http"/"https")
        rutorrent2_web_api_http_scheme:
        ```

    ??? variable dict "`rutorrent_role_web_api_http_serverstransport`{ .sb-show-on-unchecked }`rutorrent2_web_api_http_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        rutorrent_role_web_api_http_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        rutorrent2_web_api_http_serverstransport:
        ```

    ??? variable string "`rutorrent_role_web_api_scheme`{ .sb-show-on-unchecked }`rutorrent2_web_api_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string ("http"/"https")
        rutorrent_role_web_api_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string ("http"/"https")
        rutorrent2_web_api_scheme:
        ```

    ??? variable dict "`rutorrent_role_web_api_serverstransport`{ .sb-show-on-unchecked }`rutorrent2_web_api_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        rutorrent_role_web_api_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        rutorrent2_web_api_serverstransport:
        ```

    ??? variable list "`rutorrent_role_web_fqdn_override`{ .sb-show-on-unchecked }`rutorrent2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        rutorrent_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        rutorrent2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            rutorrent_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "rutorrent2.{{ user.domain }}"
              - "rutorrent.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


        !!! example sb-show-on-checked "Example Override"

            ```yaml
            rutorrent2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "rutorrent2.{{ user.domain }}"
              - "rutorrent.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`rutorrent_role_web_host_override`{ .sb-show-on-unchecked }`rutorrent2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        rutorrent_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        rutorrent2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            rutorrent_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'rutorrent2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


        !!! example sb-show-on-checked "Example Override"

            ```yaml
            rutorrent2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'rutorrent2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`rutorrent_role_web_http_port`{ .sb-show-on-unchecked }`rutorrent2_web_http_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string (quoted number)
        rutorrent_role_web_http_port:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string (quoted number)
        rutorrent2_web_http_port:
        ```

    ??? variable string "`rutorrent_role_web_http_scheme`{ .sb-show-on-unchecked }`rutorrent2_web_http_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string ("http"/"https")
        rutorrent_role_web_http_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string ("http"/"https")
        rutorrent2_web_http_scheme:
        ```

    ??? variable dict "`rutorrent_role_web_http_serverstransport`{ .sb-show-on-unchecked }`rutorrent2_web_http_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        rutorrent_role_web_http_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        rutorrent2_web_http_serverstransport:
        ```

    ??? variable string "`rutorrent_role_web_scheme`{ .sb-show-on-unchecked }`rutorrent2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        rutorrent_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        rutorrent2_web_scheme:
        ```

    ??? variable dict "`rutorrent_role_web_serverstransport`{ .sb-show-on-unchecked }`rutorrent2_web_serverstransport`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict/omit
        rutorrent_role_web_serverstransport:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict/omit
        rutorrent2_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

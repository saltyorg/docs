---
icon: material/play
status: WIP
---

# Backup

## Overview

Performs a staged backup of user data.

---

## Deployment

```sh
sb install backup
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    backup_ignore_containers: ["item1", "item2"]
    ```

=== "General"

    ??? variable list "`backup_ignore_containers`"

        ```yaml
        # Type: list
        backup_ignore_containers: []
        ```

    ??? variable list "`backup_user_defined_files`"

        ```yaml
        # Type: list
        backup_user_defined_files: []
        ```

    ??? variable dict "`backup_rclone_env`"

        ```yaml
        # Type: dict
        backup_rclone_env: {}
        ```

    ??? variable string "`backup_rclone_upload_speed_limit`"

        ```yaml
        # Options can be found at https://rclone.org/docs/#bwlimit-bandwidth-spec
        # Type: string
        backup_rclone_upload_speed_limit: "off"
        ```

    ??? variable string "`backup_instance`"

        ```yaml
        # Type: string
        backup_instance: "Saltbox"
        ```

=== "Size Check"

    ??? variable list "`backup_size_exclude_folders`"

        ```yaml
        # Type: list
        backup_size_exclude_folders: 
          - "{{ server_appdata_path }}/plex/Library/Application Support/Plex Media Server/Cache/PhotoTranscoder"
          - "{{ server_appdata_path }}/plex/Library/Application Support/Plex Media Server/Cache/Transcode"
        ```

=== "Notifications"

    ??? variable bool "`backup_notify_stop_docker_containers`"

        ```yaml
        # Type: bool (true/false)
        backup_notify_stop_docker_containers: true
        ```

    ??? variable bool "`backup_notify_start_docker_containers`"

        ```yaml
        # Type: bool (true/false)
        backup_notify_start_docker_containers: true
        ```

    ??? variable bool "`backup_notify_size`"

        ```yaml
        # Type: bool (true/false)
        backup_notify_size: true
        ```

    ??? variable bool "`backup_notify_rclone_complete`"

        ```yaml
        # Type: bool (true/false)
        backup_notify_rclone_complete: true
        ```

    ??? variable bool "`backup_notify_rsync_complete`"

        ```yaml
        # Type: bool (true/false)
        backup_notify_rsync_complete: true
        ```

=== "Templates"

    ??? variable string "`backup_google_template`"

        ```yaml
        # Type: string
        backup_google_template: '--drive-chunk-size="{{ backup_rclone_drive_chunk_size }}"'
        ```

    ??? variable string "`backup_dropbox_template`"

        ```yaml
        # Type: string
        backup_dropbox_template: '--dropbox-chunk-size="{{ backup_rclone_dropbox_chunk_size }}" --disable-http2 --dropbox-pacer-min-sleep=250ms'
        ```

    ??? variable string "`backup_sftp_template`"

        ```yaml
        # Type: string
        backup_sftp_template: ""
        ```

    ??? variable string "`backup_user_agent`"

        ```yaml
        # Type: string
        backup_user_agent: "{{ 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36' if backup.rclone.template != 'sftp' else '' }}"
        ```

=== "Cleanup"

    ??? variable int "`backup_cleanup_number`"

        ```yaml
        # Defines how many of the archived backups to keep, so current backup is not counted in this
        # Type: int
        backup_cleanup_number: 99
        ```

    ??? variable bool "`backup_cleanup_enabled`"

        ```yaml
        # Type: bool (true/false)
        backup_cleanup_enabled: false
        ```

    ??? variable string "`backup_cleanup_custom_rclone_flags`"

        ```yaml
        # Type: string
        backup_cleanup_custom_rclone_flags: ""
        ```

=== "Snapshot Defaults"

    ??? variable string "`snapshot_type`"

        ```yaml
        # Type: string
        snapshot_type: ""
        ```

    ??? variable string "`backup_opt_path`"

        ```yaml
        # Type: string
        backup_opt_path: "{{ server_appdata_path }}/"
        ```

    ??? variable bool "`use_snapshot`"

        ```yaml
        # Type: bool (true/false)
        use_snapshot: false
        ```

=== "Global Override Options"

    ??? variable bool "`backup_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        backup_role_autoheal_enabled: true
        ```

    ??? variable string "`backup_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        backup_role_depends_on: ""
        ```

    ??? variable string "`backup_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        backup_role_depends_on_delay: "0"
        ```

    ??? variable string "`backup_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        backup_role_depends_on_healthchecks:
        ```

    ??? variable bool "`backup_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        backup_role_diun_enabled: true
        ```

    ??? variable bool "`backup_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        backup_role_dns_enabled: true
        ```

    ??? variable bool "`backup_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        backup_role_docker_controller: true
        ```

    ??? variable bool "`backup_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        backup_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`backup_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        backup_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`backup_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        backup_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`backup_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        backup_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`backup_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        backup_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`backup_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        backup_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`backup_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        backup_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`backup_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        backup_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`backup_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        backup_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`backup_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        backup_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            backup_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "backup2.{{ user.domain }}"
              - "backup.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`backup_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        backup_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            backup_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'backup2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`backup_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        backup_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
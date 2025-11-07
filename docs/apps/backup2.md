---
icon: material/play
status: WIP
---

# Backup2

## Overview

Performs a streamed backup of user data.

---

## Deployment

```sh
sb install backup2
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    backup2_ignore_containers: "custom_value"
    ```

=== "General"

    ??? variable string "`backup2_ignore_containers`"

        ```yaml
        # Type: string
        backup2_ignore_containers: "{{ backup_ignore_containers }}"
        ```

    ??? variable string "`backup2_user_defined_files`"

        ```yaml
        # Type: string
        backup2_user_defined_files: "{{ backup_user_defined_files }}"
        ```

    ??? variable string "`backup2_async_batch_size`"

        ```yaml
        # Type: string
        backup2_async_batch_size: "{{ lookup('vars', 'backup2_async_batch_size_' + backup.rclone.template, default='1') }}"
        ```

    ??? variable string "`backup2_async_batch_size_sftp`"

        ```yaml
        # Type: string
        backup2_async_batch_size_sftp: "8"
        ```

    ??? variable string "`backup2_async_batch_size_google`"

        ```yaml
        # Type: string
        backup2_async_batch_size_google: "8"
        ```

    ??? variable string "`backup2_async_batch_size_dropbox`"

        ```yaml
        # Type: string
        backup2_async_batch_size_dropbox: "2"
        ```

    ??? variable string "`backup2_rclone_env`"

        ```yaml
        # Type: string
        backup2_rclone_env: "{{ backup_rclone_env }}"
        ```

    ??? variable string "`backup2_rclone_upload_speed_limit`"

        ```yaml
        # Options can be found at https://rclone.org/docs/#bwlimit-bandwidth-spec
        # Type: string
        backup2_rclone_upload_speed_limit: "{{ backup_rclone_upload_speed_limit }}"
        ```

=== "Templates"

    ??? variable string "`backup2_google_template`"

        ```yaml
        # Type: string
        backup2_google_template: '--drive-chunk-size="{{ backup_rclone_drive_chunk_size }}" --drive-stop-on-upload-limit'
        ```

    ??? variable string "`backup2_dropbox_template`"

        ```yaml
        # Type: string
        backup2_dropbox_template: '--dropbox-chunk-size="{{ backup_rclone_dropbox_chunk_size }}" --disable-http2 --dropbox-pacer-min-sleep=1000ms'
        ```

    ??? variable string "`backup2_sftp_template`"

        ```yaml
        # Type: string
        backup2_sftp_template: ""
        ```

    ??? variable string "`backup2_user_agent`"

        ```yaml
        # Type: string
        backup2_user_agent: "{{ 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36' if backup.rclone.template != 'sftp' else '' }}"
        ```

=== "Cleanup"

    ??? variable string "`backup2_cleanup_number`"

        ```yaml
        # Defines how many of the archived backups to keep, so current backup is not counted in this
        # Type: string
        backup2_cleanup_number: "{{ backup_cleanup_number }}" # Int
        ```

    ??? variable string "`backup2_cleanup_enabled`"

        ```yaml
        # Type: string
        backup2_cleanup_enabled: "{{ backup_cleanup_enabled }}" # Bool
        ```

    ??? variable string "`backup2_cleanup_custom_rclone_flags`"

        ```yaml
        # Type: string
        backup2_cleanup_custom_rclone_flags: "{{ backup_cleanup_custom_rclone_flags }}" # String
        ```

=== "Global Override Options"

    ??? variable bool "`backup2_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        backup2_role_autoheal_enabled: true
        ```

    ??? variable string "`backup2_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        backup2_role_depends_on: ""
        ```

    ??? variable string "`backup2_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        backup2_role_depends_on_delay: "0"
        ```

    ??? variable string "`backup2_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        backup2_role_depends_on_healthchecks:
        ```

    ??? variable bool "`backup2_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        backup2_role_diun_enabled: true
        ```

    ??? variable bool "`backup2_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        backup2_role_dns_enabled: true
        ```

    ??? variable bool "`backup2_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        backup2_role_docker_controller: true
        ```

    ??? variable bool "`backup2_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        backup2_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`backup2_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        backup2_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`backup2_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        backup2_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`backup2_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        backup2_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`backup2_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        backup2_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`backup2_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        backup2_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`backup2_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        backup2_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`backup2_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        backup2_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`backup2_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        backup2_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`backup2_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        backup2_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            backup2_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "backup22.{{ user.domain }}"
              - "backup2.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`backup2_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        backup2_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            backup2_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'backup22.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`backup2_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        backup2_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
icon: material/server-network-outline
status: WIP
---

# Remote

## Overview

Manages remote storage mounts.

---

## Deployment

Saltbox dependency.

```shell
sb install mounts
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    user_agent: "custom_value"
    ```

=== "Global"

    ??? variable string "`user_agent`"

        ```yaml
        # Type: string
        user_agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36
        ```

    ??? variable string "`rclone_config_path`"

        ```yaml
        # Type: string
        rclone_config_path: "/home/{{ user.name }}/.config/rclone/rclone.conf"
        ```

    ??? variable string "`rclone_vfs_cache_dir`"

        ```yaml
        # Type: string
        rclone_vfs_cache_dir: ""
        ```

    ??? variable string "`rclone_vfs_cache_dir_lookup`"

        ```yaml
        # Type: string
        rclone_vfs_cache_dir_lookup: "{{ lookup('vars', 'rclone_remote_' + rclone_remote_name + '_vfs_cache_dir', default=rclone_vfs_cache_dir) }}"
        ```

    ??? variable string "`rclone_vfs_cache_min_free_space`"

        ```yaml
        # Type: string
        rclone_vfs_cache_min_free_space: "off"
        ```

    ??? variable string "`rclone_vfs_cache_poll_interval`"

        ```yaml
        # Type: string
        rclone_vfs_cache_poll_interval: "1m0s"
        ```

    ??? variable string "`rclone_cloud_dir_cache_time`"

        ```yaml
        # Type: string
        rclone_cloud_dir_cache_time: "8760h"
        ```

    ??? variable string "`rclone_sftp_dir_cache_time`"

        ```yaml
        # Type: string
        rclone_sftp_dir_cache_time: "1m"
        ```

    ??? variable string "`rclone_sftp_chunk_size`"

        ```yaml
        # Read https://rclone.org/sftp/#sftp-chunk-size if you want to change the chunk size
        # Type: string
        rclone_sftp_chunk_size: "32Ki"
        ```

    ??? variable string "`rclone_sftp_concurrency`"

        ```yaml
        # Type: string
        rclone_sftp_concurrency: "64"
        ```

    ??? variable bool "`rclone_sftp_disable_hashcheck`"

        ```yaml
        # Type: bool (true/false)
        rclone_sftp_disable_hashcheck: false
        ```

    ??? variable string "`rclone_service_template`"

        ```yaml
        # Type: string
        rclone_service_template: "saltbox_managed_rclone_"
        ```

    ??? variable string "`rclone_port_lookup`"

        ```yaml
        # Type: string
        rclone_port_lookup: "{{ port_lookup_rclone.meta.port
                             if (port_lookup_rclone.meta.port is defined) and (port_lookup_rclone.meta.port | trim | length > 0)
                             else '5572' }}"
        ```

    ??? variable string "`rclone_remort_port`"

        ```yaml
        # Type: string
        rclone_remort_port: "{{ lookup('vars', 'rclone_remote_' + rclone_remote_name + '_port', default=rclone_port_lookup) }}"
        ```

    ??? variable int "`rclone_remort_port_low_bound`"

        ```yaml
        # Type: int
        rclone_remort_port_low_bound: 5572
        ```

    ??? variable int "`rclone_remort_port_high_bound`"

        ```yaml
        # Type: int
        rclone_remort_port_high_bound: 6072
        ```

    ??? variable string "`rclone_remote_name`"

        ```yaml
        # Type: string
        rclone_remote_name: "{{ item | filter_rclone_remote_name }}"
        ```

    ??? variable string "`rclone_remote_with_path`"

        ```yaml
        # Type: string
        rclone_remote_with_path: "{{ item | filter_rclone_remote_with_path }}"
        ```

    ??? variable string "`rclone_first_remote_name`"

        ```yaml
        # Type: string
        rclone_first_remote_name: "{{ rclone | filter_rclone_first_remote_name }}"
        ```

    ??? variable string "`rclone_first_remote_name_with_path`"

        ```yaml
        # Type: string
        rclone_first_remote_name_with_path: "{{ rclone | filter_rclone_first_remote_name_with_path }}"
        ```

    ??? variable bool "`remote_update_rclone`"

        ```yaml
        # Type: bool (true/false)
        remote_update_rclone: true
        ```

    ??? variable bool "`rclone_enable_metrics`"

        ```yaml
        # Type: bool (true/false)
        rclone_enable_metrics: false
        ```

=== "Rclone VFS Refresh"

    ??? variable int "`rclone_vfs_refresh_interval`"

        ```yaml
        # Type: int
        rclone_vfs_refresh_interval: 10800
        ```

    ??? variable string "`rclone_vfs_refresh_command`"

        ```yaml
        # Type: string
        rclone_vfs_refresh_command: |-
          /usr/bin/rclone rc vfs/refresh recursive=true --url http://localhost:{{ rclone_remort_port }} _async=true
        ```

=== "NFS"

    ??? variable string "`nfs_opts`"

        ```yaml
        # Type: string
        nfs_opts: "nofail,noatime,nolock,intr,tcp,actimeo=1800"
        ```

=== "Global Override Options"

    ??? variable bool "`remote_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        remote_role_autoheal_enabled: true
        ```

    ??? variable string "`remote_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        remote_role_depends_on: ""
        ```

    ??? variable string "`remote_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        remote_role_depends_on_delay: "0"
        ```

    ??? variable string "`remote_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        remote_role_depends_on_healthchecks:
        ```

    ??? variable bool "`remote_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        remote_role_diun_enabled: true
        ```

    ??? variable bool "`remote_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        remote_role_dns_enabled: true
        ```

    ??? variable bool "`remote_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        remote_role_docker_controller: true
        ```

    ??? variable bool "`remote_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        remote_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`remote_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        remote_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`remote_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        remote_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`remote_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        remote_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`remote_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        remote_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`remote_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        remote_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`remote_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        remote_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`remote_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        remote_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`remote_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        remote_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`remote_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        remote_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            remote_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "remote2.{{ user.domain }}"
              - "remote.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`remote_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        remote_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            remote_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'remote2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`remote_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        remote_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
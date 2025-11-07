---
icon: material/play
status: Outdated
hide:
  - tags
tags:
  - plex-db
---

# Plex DB

## Overview

`plex-db` runs some database maintenance tasks on the plex databases for each of your defined plex instances:

1. Check if main database passes integrity_check
1. Check if blobs database passes integrity_check
1. Back up databases
1. does a sqlite 'VACUUM' operation on the main database
1. does a sqlite 'VACUUM' operation on the blobs database
1. does a sqlite 'REINDEX' operation on the main database
1. does a sqlite 'REINDEX' operation on the blobs database

If any of those operations fail, the backup databases are restored.

The plex containers are stopped for the duration of this process.

### 1. Installation

``` shell

sb install plex-db

```

Further information:

- [:octicons-link-16: Sqlite VACUUM](https://www.sqlite.org/lang_vacuum.html)

- [:octicons-link-16: Sqlite REINDEX](https://www.sqlite.org/lang_reindex.html)

- [:octicons-link-16: A more comprehensive utility with similar purpose](https://github.com/ChuckPa/PlexDBRepair)

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    plex_db_integrity_check_only: true
    ```

=== "General"

    ??? variable bool "`plex_db_integrity_check_only`"

        ```yaml
        # Type: bool (true/false)
        plex_db_integrity_check_only: false
        ```

    ??? variable bool "`plex_db_failed_integrity`"

        ```yaml
        # Type: bool (true/false)
        plex_db_failed_integrity: false
        ```

    ??? variable bool "`plex_db_failed_optimization`"

        ```yaml
        # Type: bool (true/false)
        plex_db_failed_optimization: false
        ```

    ??? variable list "`plex_db_files`"

        ```yaml
        # Do not enable globally if deploying multiple instances
        # Type: list
        plex_db_files: 
          - "com.plexapp.plugins.library.db"
          - "com.plexapp.plugins.library.blobs.db"
        ```

=== "Global Override Options"

    ??? variable bool "`plex_db_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        plex_db_role_autoheal_enabled: true
        ```

    ??? variable string "`plex_db_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        plex_db_role_depends_on: ""
        ```

    ??? variable string "`plex_db_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        plex_db_role_depends_on_delay: "0"
        ```

    ??? variable string "`plex_db_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        plex_db_role_depends_on_healthchecks:
        ```

    ??? variable bool "`plex_db_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        plex_db_role_diun_enabled: true
        ```

    ??? variable bool "`plex_db_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        plex_db_role_dns_enabled: true
        ```

    ??? variable bool "`plex_db_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        plex_db_role_docker_controller: true
        ```

    ??? variable bool "`plex_db_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        plex_db_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`plex_db_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        plex_db_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`plex_db_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        plex_db_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`plex_db_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        plex_db_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`plex_db_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        plex_db_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`plex_db_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        plex_db_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`plex_db_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        plex_db_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`plex_db_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        plex_db_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`plex_db_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        plex_db_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`plex_db_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        plex_db_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            plex_db_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "plex_db2.{{ user.domain }}"
              - "plex_db.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`plex_db_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        plex_db_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            plex_db_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'plex_db2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`plex_db_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        plex_db_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
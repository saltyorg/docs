---
hide:
  - tags
tags:
  - arr_db
  - database
  - postgres
---

# Arr DB

## What is it?

Arr DB is a Saltbox maintenance role that performs database optimization tasks on SQLite databases used by *arr applications (Sonarr, Radarr, Lidarr, Whisparr, Prowlarr) and Tautulli. The role performs integrity checks, vacuuming, and reindexing operations to maintain database health and performance.

!!! warning
    This role is only for instances that use SQLite databases. If you have migrated your *arr applications to PostgreSQL, do not use this role.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/saltyorg/Saltbox){: .header-icons } | [:octicons-link-16: Docs](https://www.sqlite.org/lang_vacuum.html){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/saltyorg/Saltbox){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/sonarr){: .header-icons }|

### 1. Usage

``` shell

sb install arr-db

```

### 2. Setup

Before running the arr_db role, you must enable at least one application in your Saltbox inventory by setting the appropriate variable to `true`:

- `arr_db_sonarr_enabled`
- `arr_db_radarr_enabled`
- `arr_db_lidarr_enabled`
- `arr_db_whisparr_enabled`
- `arr_db_prowlarr_enabled`
- `arr_db_tautulli_enabled`

### 3. What It Does

The arr_db role performs the following operations for each enabled application:

1. **Integrity Check**: Verifies database integrity before proceeding
2. **Backup**: Creates a temporary backup of the database files
3. **Vacuum**: Reclaims unused space and optimizes the database file
4. **Reindex**: Rebuilds database indexes for improved query performance
5. **Cleanup**: Removes temporary backup files after successful completion

!!! info
    The role automatically stops the application container before database operations and restarts it afterward. If any operation fails, the database is automatically restored from backup.

!!! warning
    Only run this role when you have enabled at least one application. The databases must already exist for the role to work.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        arr_db_sonarr_enabled: true
        ```

=== "Settings"

    ??? variable bool "`arr_db_sonarr_enabled`"

        ```yaml
        # Type: bool (true/false)
        arr_db_sonarr_enabled: false
        ```

    ??? variable bool "`arr_db_radarr_enabled`"

        ```yaml
        # Type: bool (true/false)
        arr_db_radarr_enabled: false
        ```

    ??? variable bool "`arr_db_lidarr_enabled`"

        ```yaml
        # Type: bool (true/false)
        arr_db_lidarr_enabled: false
        ```

    ??? variable bool "`arr_db_whisparr_enabled`"

        ```yaml
        # Type: bool (true/false)
        arr_db_whisparr_enabled: false
        ```

    ??? variable bool "`arr_db_prowlarr_enabled`"

        ```yaml
        # Type: bool (true/false)
        arr_db_prowlarr_enabled: false
        ```

    ??? variable bool "`arr_db_tautulli_enabled`"

        ```yaml
        # Type: bool (true/false)
        arr_db_tautulli_enabled: false
        ```

=== "Variables"

    ??? variable string "`arr_path_logs_db`"

        ```yaml
        # Type: string
        arr_path_logs_db: "{{ lookup('vars', arr_type + '_role_paths_location') }}/logs.db"
        ```

    ??? variable string "`arr_path_main_db`"

        ```yaml
        # Type: string
        arr_path_main_db: "{{ lookup('vars', arr_type + '_role_paths_location') }}/{{ arr_type }}.db"
        ```

    ??? variable list "`arr_db_files`"

        ```yaml
        # Type: list
        arr_db_files: 
          - "logs.db"
          - "{{ arr_type }}.db"
        ```

    ??? variable list "`arr_db_temp_files`"

        ```yaml
        # Type: list
        arr_db_temp_files: 
          - "logs.db-wal"
          - "logs.db-shm"
          - "{{ arr_type }}.db-wal"
          - "{{ arr_type }}.db-shm"
        ```

    ??? variable string "`arr_db_tautulli_database`"

        ```yaml
        # Type: string
        arr_db_tautulli_database: "tautulli.db"
        ```

    ??? variable list "`arr_db_tautulli_temp_files`"

        ```yaml
        # Type: list
        arr_db_tautulli_temp_files: 
          - "tautulli.db-wal"
          - "tautulli.db-shm"
        ```

=== "Global Override Options"

    ??? variable bool "`arr_db_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        arr_db_role_autoheal_enabled: true
        ```

    ??? variable string "`arr_db_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        arr_db_role_depends_on: ""
        ```

    ??? variable string "`arr_db_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        arr_db_role_depends_on_delay: "0"
        ```

    ??? variable string "`arr_db_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        arr_db_role_depends_on_healthchecks:
        ```

    ??? variable bool "`arr_db_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        arr_db_role_diun_enabled: true
        ```

    ??? variable bool "`arr_db_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        arr_db_role_dns_enabled: true
        ```

    ??? variable bool "`arr_db_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        arr_db_role_docker_controller: true
        ```

    ??? variable bool "`arr_db_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        arr_db_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`arr_db_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        arr_db_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`arr_db_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        arr_db_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`arr_db_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        arr_db_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`arr_db_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        arr_db_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`arr_db_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        arr_db_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`arr_db_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        arr_db_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`arr_db_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        arr_db_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            arr_db_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "arr_db2.{{ user.domain }}"
              - "arr_db.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`arr_db_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        arr_db_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            arr_db_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'arr_db2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`arr_db_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        arr_db_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
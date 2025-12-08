---
icon: material/play
hide:
  - tags
tags:
  - arr_db
  - database
  - postgres
saltbox_automation:
  inventory:
    hide_sections:
      - Variables
---

# Arr DB

## Overview

Arr DB is a Saltbox maintenance role that performs database optimization tasks on SQLite databases used by *arr applications (Sonarr, Radarr, Lidarr, Whisparr, Prowlarr) and Tautulli. The role performs integrity checks, vacuuming, and reindexing operations to maintain database health and performance.

The arr_db role performs the following operations for each enabled application:

1. **Integrity Check**: Verifies database integrity before proceeding
2. **Backup**: Creates a temporary backup of the database files
3. **Vacuum**: Reclaims unused space and optimizes the database file
4. **Reindex**: Rebuilds database indexes for improved query performance
5. **Cleanup**: Removes temporary backup files after successful completion

---

!!! warning

    This role is only for instances that use SQLite databases. If you have migrated your *arr applications to PostgreSQL, do not use this role.

## Configuration

Before running the arr_db role, you must enable at least one application in your Saltbox inventory by setting the appropriate variable to `true`:

- `arr_db_sonarr_enabled`
- `arr_db_radarr_enabled`
- `arr_db_lidarr_enabled`
- `arr_db_whisparr_enabled`
- `arr_db_prowlarr_enabled`
- `arr_db_tautulli_enabled`

## Deployment

!!! warning

    Only run this role when you have enabled at least one application. The databases must already exist for the role to work.

!!! info

    The role automatically stops the application container before database operations and restarts it afterward. If any operation fails, the database is automatically restored from backup.

```shell
sb install arr-db
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
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
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
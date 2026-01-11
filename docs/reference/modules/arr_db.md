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
  project_description:
    name: Arr DB
    summary: |
      a Saltbox module that performs maintenance operations on SQLite databases used by Sonarr, Radarr, Lidarr, Whisparr, Prowlarr and Tautulli instances.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Arr DB

## Overview

Arr DB is a Saltbox module that performs maintenance operations on SQLite databases used by Sonarr, Radarr, Lidarr, Whisparr, Prowlarr and Tautulli instances.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

!!! warning

    This role is only for instances that use SQLite databases. If you have migrated your *arr applications to PostgreSQL, do not use this role.

## Tasks

The arr_db role performs the following operations for each enabled application:

1. **Integrity Check**: Verifies database integrity before proceeding
2. **Backup**: Creates a temporary backup of the database files
3. **Vacuum**: Reclaims unused space and optimizes the database file
4. **Reindex**: Rebuilds database indexes for improved query performance
5. **Cleanup**: Removes temporary backup files after successful completion

## Configuration

Before running the arr_db role, you must enable at least one application in your Saltbox inventory by setting [the appropriate variable](#role-defaults) to `true`.

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

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

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
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

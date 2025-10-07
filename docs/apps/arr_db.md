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

sb install arr_db

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

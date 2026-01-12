---
icon: material/play
title: Plex DB
status: outdated
hide:
  - tags
tags:
  - plex-db
saltbox_automation:
  project_description:
    name: Plex DB
    summary: |
      a Saltbox module that performs maintenance operations on SQLite databases used by Plex Media Server instances.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Plex DB

## Overview

Plex DB is a Saltbox module that performs maintenance operations on SQLite databases used by Plex Media Server instances.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Tasks

For each of your defined plex instances:

1. Checks if the main database passes integrity_check
1. Checks if the blobs database passes integrity_check
1. Backs up databases
1. does a sqlite 'VACUUM' operation on the main database
1. does a sqlite 'VACUUM' operation on the blobs database
1. does a sqlite 'REINDEX' operation on the main database
1. does a sqlite 'REINDEX' operation on the blobs database

If any of those operations fail, the backup databases are restored.

The plex containers are stopped for the duration of this process.

Further information:

- [:octicons-link-16: Sqlite VACUUM](https://www.sqlite.org/lang_vacuum.html)

- [:octicons-link-16: Sqlite REINDEX](https://www.sqlite.org/lang_reindex.html)

- [:octicons-link-16: A more comprehensive utility with a similar purpose](https://github.com/ChuckPa/PlexDBRepair)

## Deployment

```shell
sb install plex-db
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
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
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

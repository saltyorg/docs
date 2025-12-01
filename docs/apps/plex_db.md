---
icon: material/play
status: outdated
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

---

## Deployment

```shell
sb install plex-db
```

Further information:

- [:octicons-link-16: Sqlite VACUUM](https://www.sqlite.org/lang_vacuum.html)

- [:octicons-link-16: Sqlite REINDEX](https://www.sqlite.org/lang_reindex.html)

- [:octicons-link-16: A more comprehensive utility with similar purpose](https://github.com/ChuckPa/PlexDBRepair)

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    : 
    ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
title: Streamed Backup
hide:
  - tags
tags:
  - backup2
saltbox_automation:
  project_description:
    name: Streamed Backup (backup2)
    summary: |-
      a Saltbox module that performs a backup of your Saltbox managed data, backing up directly to the remote destination.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Streamed Backup (backup2)

## Overview

Streamed Backup (backup2) is a Saltbox module that performs a backup of your Saltbox managed data, backing up directly to the remote destination.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

The standard backup role will tar up all the directories in `/opt`, then once that operation is complete, transfer all those tar archives to an rclone/rsync destination.

Perhaps you are on a system that is space-constrained and does not allow this.

`backup2` supports only rclone targets, and will do the tar operation straight to the rclone destination, directory by directory, without requiring the intermediate step of writing the archive to the local disk.

It will be far less performant than writing the tar archives to a local disk, but exists for use in the event that doing so is not possible.

## Deployment

```shell
sb install backup2
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        backup2_google_template: "custom_value"
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
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
title: Standard Backup
hide:
  - tags
tags:
  - backup
saltbox_automation:
  project_description:
    name: Standard Backup
    summary: |
      a Saltbox module that performs a backup of your Saltbox managed data.
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Standard Backup

## Overview

Standard Backup is a Saltbox module that performs a backup of your Saltbox managed data.

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

With Saltbox you can either run a backup task manually or schedule it to run automatically.

!!! important
    A successful backup will require free space (in `/mnt/local/Backups/Saltbox` by default) *at least* equal to the aggregate size of `/opt`. The backup creates tar archives from the directories in `/opt` and then uploads the tar archives to any destinations that you have set up in the [backup config](../../saltbox/backup/settings.md). These archives are not compressed, so there needs to be enough space for a second copy of `/opt`.

    `sudo ncdu -x /` is one way to verify the size of `/opt`.

    `df -h` is one way to verify the amount of free space available.

This backup will take some time, likely hours, and all your containers may be down the entire time depending on your disk setup.

??? note "Why so long, why are the containers down, and what can I do about this?"

    It stops all containers, creates tar archives of all directories in `/opt`, restarts all containers, then uploads the tar archives to any destinations that you have set up in the [backup config](../../saltbox/backup/settings.md). All your containers will be down for the duration of the `tar` process.

    The containers are down to prevent any applications from writing to their databases or the like while the tar process is ongoing, which could corrupt the backup and the active files. You may ask, "Why not do them one at a time?"  This is effectively impossible since there is no fixed relationship between container and appdata folder, especially with custom containers defined by the user.

    If your `/opt` directory is on a `BTRFS` volume, the containers are down for a few seconds as a snapshot is taken, then they are brought back up and the `tar` operation works from the snapshot. The entire process still takes as long as before, but the containers aren't down the entire time.

    This applies regardless of whether you are running the backup manually or on a schedule.

??? note "My rclone destination has too many saved backups! What can I do about this?"

    You can control the number of backups stored on the rclone destination using the inventory. The inventory variables you would use to do this are described on the [backup config](../../saltbox/backup/settings.md) page.

## Manual Backup

!!! info
    This step assumes you have completed the configuration of the `backup_config.yml` in the configuration [step](../../saltbox/backup/settings.md).

    Specifically, you should make sure you have defined and enabled your desired destination(s) for the backup.

=== "Without Screen"

    ```shell
    sb install backup
    ```

    This will begin the backup in the active terminal; you will not be able to close the terminal or disconnect from your server while the backup proceeds. If you do so (deliberately or accidentally), the backup will be aborted.

=== "With Screen"

    Running the backup in `screen` will allow you to disconnect the SSH session and let the backup continue, or send it to the background while you are doing other things.

    !!! note
        This is a minimal example of using `screen`; it is not intended to teach you what `screen` is or how to use it generally.

    ```shell
    screen -dmS saltbox-backup sb install backup
    ```

    The backup is now running in the background.

    If you want to get a look at what's going on, this command will bring it to the foreground and show you the ongoing output. (this is assuming you have a single thing running in a single `screen`; see the note above about not teaching `screen` generally)

    ```shell
    screen -r
    ```

    To send it to the background again, type:
    ```
    CTRL A + D
    ```

    There are of course alternatives to `screen` that you may prefer.

## Scheduled Backup

!!! info
    This step assumes you have completed the configuration of the `backup_config.yml` in the configuration [step](../../saltbox/backup/settings.md).

    Specifically, you should make sure you have defined and enabled your desired destination(s) for the backup **and** defined a desired cron_time:

    ```yaml
    cron:
      cron_time: weekly
    ```

    Options are: `reboot`, `yearly`, `annually`, `monthly`, `weekly`, `daily`, `hourly`.

=== "Have Saltbox configure cron"

    ```shell
    sb install set-backup
    ```

=== "Configure cron manually"

    Open your crontab file for editing:

    ```shell
    crontab -e
    ```

    Then add this line to the file. This example will run the backup every day at 4AM.

    ```shell
    0 4 * * * sudo PATH='/usr/bin:/bin:/usr/local/bin' env ANSIBLE_CONFIG='/srv/git/saltbox/ansible.cfg' '/usr/local/bin/ansible-playbook' '/srv/git/saltbox/backup.yml' '--tags' 'backup' >> '/srv/git/saltbox/saltbox_backup.log' 2>&1
    ```

    !!! note
        Visit [crontab.guru](https://crontab.guru/) for help with the scheduling format.

    Save and close the file and the schedule will be applied going forward.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        backup_size_exclude_folders: ["item1", "item2"]
        ```

=== "Size Check"

    ??? variable list "`backup_size_exclude_folders`"

        ```yaml
        # Type: list
        backup_size_exclude_folders:
          - "{{ server_appdata_path }}/plex/Library/Application Support/Plex Media Server/Cache/PhotoTranscoder"
          - "{{ server_appdata_path }}/plex/Library/Application Support/Plex Media Server/Cache/Transcode"
        ```

=== "Notifications"

    ??? variable bool "`backup_notify_stop_docker_containers`"

        ```yaml
        # Type: bool (true/false)
        backup_notify_stop_docker_containers: true
        ```

    ??? variable bool "`backup_notify_start_docker_containers`"

        ```yaml
        # Type: bool (true/false)
        backup_notify_start_docker_containers: true
        ```

    ??? variable bool "`backup_notify_size`"

        ```yaml
        # Type: bool (true/false)
        backup_notify_size: true
        ```

    ??? variable bool "`backup_notify_rclone_complete`"

        ```yaml
        # Type: bool (true/false)
        backup_notify_rclone_complete: true
        ```

    ??? variable bool "`backup_notify_rsync_complete`"

        ```yaml
        # Type: bool (true/false)
        backup_notify_rsync_complete: true
        ```

=== "Templates"

    ??? variable string "`backup_google_template`"

        ```yaml
        # Type: string
        backup_google_template: '--drive-chunk-size="{{ backup_rclone_drive_chunk_size }}"'
        ```

    ??? variable string "`backup_dropbox_template`"

        ```yaml
        # Type: string
        backup_dropbox_template: '--dropbox-chunk-size="{{ backup_rclone_dropbox_chunk_size }}" --disable-http2 --dropbox-pacer-min-sleep=250ms'
        ```

    ??? variable string "`backup_sftp_template`"

        ```yaml
        # Type: string
        backup_sftp_template: ""
        ```

    ??? variable string "`backup_user_agent`"

        ```yaml
        # Type: string
        backup_user_agent: "{{ 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36' if backup.rclone.template != 'sftp' else '' }}"
        ```

=== "Cleanup"

    ??? variable int "`backup_cleanup_number`"

        ```yaml
        # Defines how many of the archived backups to keep, so current backup is not counted in this
        # Type: int
        backup_cleanup_number: 99
        ```

    ??? variable bool "`backup_cleanup_enabled`"

        ```yaml
        # Type: bool (true/false)
        backup_cleanup_enabled: false
        ```

    ??? variable string "`backup_cleanup_custom_rclone_flags`"

        ```yaml
        # Type: string
        backup_cleanup_custom_rclone_flags: ""
        ```

=== "Snapshot Defaults"

    ??? variable string "`snapshot_type`"

        ```yaml
        # Type: string
        snapshot_type: ""
        ```

    ??? variable string "`backup_opt_path`"

        ```yaml
        # Type: string
        backup_opt_path: "{{ server_appdata_path }}/"
        ```

    ??? variable bool "`use_snapshot`"

        ```yaml
        # Type: bool (true/false)
        use_snapshot: false
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

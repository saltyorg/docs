---
hide:
  - tags
tags:
  - settings
  - configuration
  - backup
---

# Configuration

The configuration file for backup/restore is called `backup_config.yml` and is located in `/srv/git/saltbox`

``` { .yaml .annotate }
---
backup:
  cron:
    cron_time: weekly # (1)!
  local:
    destination: /home/{{ user.name }}/Backups/Saltbox # (2)!
    enable: true # (3)!
  misc:
    snapshot: true # (4)!
  rclone:
    destination: google:/Backups/Saltbox # (5)!
    enable: true # (6)!
    template: google # (7)!
  restore_service:
    pass: # (8)!
    user: # (9)!
  rsync:
    destination: rsync://somehost.com/Backups/Saltbox # (10)!
    enable: false # (11)!
    port: 22 # (12)!

```

1. Schedule for when the backup task will be executed.

    Options are: `reboot`, `yearly`, `annually`, `monthly`, `weekly`, `daily`, `hourly`.

    Should you desire more granular control over the schedule you can edit the crontab for the Saltbox user once setup.

2. Path used for the local backups. `{{ user.name }}` will be replaced with the user name you enter in the settings.

3. Toggle for keeping a local copy of the backup.

    Options are: `true` or `false`

4. Toggle for BTRFS snaphots.

    Options are: `true` or `false`

    Requires BTRFS on `/` or `/opt`

5. Path used for the Rclone remote. Backups outside of the most recent one will be located in the `archived` folder.

    Make sure that this path is unique if you run multiple instances of Saltbox.

6. Toggle for using Rclone remote backup storage.

    Options are: `true` or `false`

7. Defines which Rclone flags template is used for the backup.

    Options are: `google`, `dropbox`, `sftp` or `custom`

    If you want to use custom you need to define any flags you want to use through the inventory.

    ```yaml
    backup_custom_template: '--some-flag --other-flag'
    ```

    Feel free to submit templates in a PR to Saltbox.

8. Password used to encrypt/decrypt the configuration files in the OPTIONAL restore service.

    Only used on the client side in scripts.

9. Username used for the OPTIONAL restore service.

    Has to be unique across all users of the service. Try sticking with a url for the server `box.domain.tld` unique to each server for something easily remembered.

    Usernames are hashed before requests are sent to the restore service.

10. Path used for the Rsync backups.

11. Toggle for using Rsync backups.

    Options are: `true` or `false`

12. Port used by rsync on the target server.

!!! important

    Nothing that is stored on the rclone or rsync destinations is encrypted by this backup process, so take care not to set those destinations to systems you do not control.

    If you are concerned about that, set up an encrypted rclone remote for use with the backup rather than using the default saltbox unencrypted `google` remote.

    Securing the rsync destination is outside the scoope of this document.

Use of the restore service is optional.  Using it means that [client-side] encrypted copies of your config files are stored on saltbox servers for later use with the `sb restore` command.  If you are uncomfortable with this, leave the username and password blank and the restore server will not be used.

Visit [crontab.guru](https://crontab.guru/) for help with the scheduling format.

!!! important

    These values:

    ``` { .yaml .annotate }
      restore_service:
        pass: # (1)!
        user: # (2)!
    ```

    1. Password used encrypt/decrypt the configuration files for the OPTIONAL restore service. 

        Only used on the client side in scripts.

    2. Username used for the OPTIONAL restore service.

        Has to be unique across all users of the service. Try sticking with a url for the server `box.domain.tld` unique to each server for something easily remembered.

        Usernames are hashed before requests are sent to the restore service.

    SHOULD NOT BE YOUR SERVER ACCOUNT CREDENTIALS.

    These are an *arbitrary* username/password that you make up which are used ONLY with this backup/restore service.  They are used to encrypt your config files before they are placed on the saltbox restore server, and then in the restore command that retrieves the backup for decryption.  They are not sent or stored anywhere else.  If they are not filled in, then your config files will not be sent to the saltbox restore service.

By default, Saltbox will keep all previous backups that have been pushed to an rclone target.

If you wish to change that you can use these variables in your inventory:

``` { .yaml .annotate }
backup_cleanup_number: 99 # (1)!
backup_cleanup_enabled: false # (2)!
backup_cleanup_custom_rclone_flags: "" # (3)!

# When using backup2
backup2_cleanup_number: 99
backup2_cleanup_enabled: false
backup2_cleanup_custom_rclone_flags: ""
```

1. How many previous backups to retain [excluding the most recent]

2. Enable or disable this backup pruning [if this is false, the previous value is ignored]

3. Add these flags to the rclone run that performs the cleanup.

    A use case might be to add `--drive-use-trash=false` to delete immediately from Google Drive.

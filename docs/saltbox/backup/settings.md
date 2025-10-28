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
    user: # (9)!7
  rsync:
    destination: rsync://somehost.com/Backups/Saltbox # (10)!
    enable: false # (11)!
    port: 22 # (12)!

```

1. Schedule for when the backup task will be executed.

    Options are: `reboot`, `yearly`, `annually`, `monthly`, `weekly`, `daily`, `hourly`.

    Should you desire more granular control over the schedule you can edit the crontab for the Saltbox user once setup.

    Visit [crontab.guru](https://crontab.guru/) for help with the scheduling format.

3. Path used for the local backups. `{{ user.name }}` will be replaced with the user name you enter in the settings.

4. Toggle for keeping a local copy of the backup.

    Options are: `true` or `false`

5. Toggle for BTRFS snaphots.

    Options are: `true` or `false`

    Requires BTRFS on `/` or `/opt`

6. Path used for the Rclone remote. Backups outside of the most recent one will be located in the `archived` folder.

    Make sure that this path is unique if you run multiple instances of Saltbox.

7. Toggle for using Rclone remote backup storage.

    Options are: `true` or `false`

8. Defines which Rclone flags template is used for the backup.

    Options are: `google`, `dropbox`, `sftp` or `custom`

    If you want to use custom you need to define any flags you want to use through the inventory.

    ```yaml
    backup_custom_template: '--some-flag --other-flag'
    ```

    Feel free to submit templates in a PR to Saltbox.

9. Password used to encrypt/decrypt the configuration files in the OPTIONAL restore service.

    Only used on the client side in scripts.

10. Username used for the OPTIONAL restore service.

    Has to be unique across all users of the service. Try sticking with a url for the server `box.xYOUR_DOMAIN_NAMEx` unique to each server for something easily remembered.

    Usernames are hashed before requests are sent to the restore service.

11. Path used for the Rsync backups.

12. Toggle for using Rsync backups.

    Options are: `true` or `false`

13. Port used by rsync on the target server.

## Security concerns

!!! important

    Nothing that is stored on the rclone or rsync destinations is encrypted by this backup process, so take care not to set those destinations to systems you do not control.

    If you are concerned about that, set up an encrypted rclone remote for use with the backup rather than using the default saltbox unencrypted `google` remote.

    Securing the rsync destination is outside the scope of this document.

### Restore service

Use of the restore service is optional.  Using it means that [client-side] encrypted copies of your config files are stored on saltbox servers for later use with the `sb restore` command.  

These copies are encrypted on your local saltbox machine using the password you specify in the settings and stored on saltbox servers under the username you specify [which should be a random string rather than anything identifiable].  The password is not sent to saltbox servers; they do not know your password and cannot decrypt these files.  If you are uncomfortable with this, leave the username and password blank and the restore server will not be used.

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
    
        Has to be unique across all users of the service. Try sticking with a url for the server `box.xYOUR_DOMAIN_NAMEx` unique to each server for something easily remembered.
    
        Usernames are hashed before requests are sent to the restore service.
    
    SHOULD NOT BE YOUR SERVER ACCOUNT CREDENTIALS.
    
    These are an *arbitrary* username/password that you make up which are used ONLY with this backup/restore service.  They are used to encrypt your config files before they are placed on the saltbox restore server, and then in the restore command that retrieves the backup for decryption.  They are not sent or stored anywhere else.  If they are not filled in, then your config files will not be sent to the saltbox restore service.
    
    We'd recommend you use some random text for **both** the username and password, like perhaps a randomly-generated password from BitWarden or some other password generator.  This should avoid collisions like someone else choosing the username "saltboxbackup".  This sort of thing:

    ``` { .yaml }
      restore_service:
        pass: T5CIqmRRx5Da6U0s
        user: p1i4IMkEyfiJ9iyG
    ```
    Of course, don't use *those* values.

## Retained backups ['rclone' specific]

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

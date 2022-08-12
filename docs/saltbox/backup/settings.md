# Configuration

The configuration file for backup/restore is called `backup_config.yml` and is located in `/srv/git/saltbox`

``` { .yaml .annotate }
---
backup:
  local:
    enable: true # (1)
    destination: /mnt/local/Backups/Saltbox # (2)
  rclone:
    enable: true # (3)
    destination: google:/Backups/Saltbox # (4)
  rsync:
    enable: false # (5)
    destination: rsync://somehost.com/Backups/Saltbox # (6)
    port: 22 # (7)
  cron:
    cron_time: weekly # (8)
    enable: no # (9)
  restore_service:
    user: # (10)
    pass: # (11)
  misc:
    snapshot: true # (12)
```

1. Toggle for keeping a local copy of the backup.

    Options are: `true` or `false`

2. Path used for the local backups.

3. Toggle for using Rclone remote backup storage.

    Options are: `true` or `false`

4. Path used for the Rclone remote. Backups outside of the most recent one will be located in the `archived` folder.
    
    Make sure that this path is unique if you run multiple instances of Saltbox.

5. Toggle for using Rsync backups.

    Options are: `true` or `false`

6. Path used for the Rsync backups.

7. Port used by rsync on the target server.

8. Schedule for when the backup task will be executed.

    Options are: `reboot`, `yearly`, `annually`, `monthly`, `weekly`, `daily`, `hourly`.

    Should you desire more granular control over the schedule you can edit the crontab for the Saltbox user once setup.

9. Toggle for enabling automatic backups.

    Options are: `no` or `yes`

    Depending on the option set here the cron entry created by Saltbox will be added, removed or modified.

10. Username used for the restore service.

    Has to be unique across all users of the service. Try sticking with a url for the server `box.domain.tld` unique to each server for something easily remembered.

    Usernames are hashed before requests are sent to the restore service.

11. Password used encrypt/decrypt the configuration files. 

    Only used on the client side in scripts.

12. Toggle for BTRFS snaphots.

    Options are: `true` or `false`

    Requires BTRFS on `/` or `/opt`

Visit [crontab.guru](https://crontab.guru/) for help with the scheduling format.

IMPORTANT:

These values:

```yml
  restore_service:
    user: # 
    pass: # 
```

SHOULD NOT BE YOUR SERVER ACCOUNT CREDENTIALS.

These are an *arbitrary* username/password that you make up which are used ONLY with this backup/restore service.  They are used to encrypt your config files before they are placed on the saltbox restore server, and then in the restore command that retrieves the backup for decryption.  They are not sent or stored anywhere else.  If they are not filled in, then your config files will not be sent to the saltbox restore service.

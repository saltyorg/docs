# Backup

With Saltbox you can either run a backup task manually or schedule it to run automatically.

## Manual Backup

!!! info
    This step assumes you have completed the configuration of the `backup_config.yml` in the configuration [step](../../saltbox/backup/settings.md).

=== "Without Screen"
``` shell
sb install backup
```

This will begin the backup in the active terminal; you will not be able to close the terminal or disconnect from your server while the backup  proceeds.  If you do so [deliberately or accidentally], the backup will be aborted.

=== "With Screen"

Running the backup in `screen` will allow you to disconnect the SSH session and let the backup continue, or send it to the background while you are doing other things.

!!! note
    This is a minimal example of using `screen`; it is not intended to teach you what `screen` is or how to use it generally.
    
```shell
screen -dmS saltbox-backup sb install backup
```

The backup is now running in the background.

If you want to get a look at what's going on, this command will bring it to the foreground and show you the ongoing output. [this is assuming you have a single thing running in a single `screen`; see the note above about not teaching `screen` generally]

```shell
screen -r
```

To send it to the background again, type:
```
CTRL A + D
```

## Scheduled Backup

!!! info
    This step assumes you have completed the configuration of the `backup_config.yml` in the configuration [step](../../saltbox/backup/settings.md).

=== "Have Saltbox configure cron"

```shell
    sb install set-backup
```

=== "Configure cron manually"

Open your crontab file for editing:

```shell
    crontab -e
```

Then add this line to the file.  This example will run the backup every day at 4AM.

```shell
    0 4 * * * sudo PATH='/usr/bin:/bin:/usr/local/bin' env ANSIBLE_CONFIG='/srv/git/saltbox/ansible.cfg' '/usr/local/bin/ansible-playbook' '/srv/git/saltbox/backup.yml' >> '/home/seed/logs/saltbox_backup.log' 2>&1
```
!!! note
        Remember to edit the seed username if you changed the Saltbox user in the `accounts.yml`.
        Visit [crontab.guru](https://crontab.guru/) for help with the scheduling format.

Save and close the file and the schedule will be applied going forward.

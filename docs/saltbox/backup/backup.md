# Backup

With Saltbox you can either run a backup task manually or schedule it to run automatically.

!!! important
    A successful backup will require free space [in `/mnt/local/Backups/Saltbox` by default] *at least* equal to the aggregate size of `/opt`.  The backup creates tar archives from the directories in `/opt` and then uploads the tar archives to any destinations that you have set up in the [backup config](../../saltbox/backup/settings.md).  These archives are not compressed, so there needs to be enough space for a second copy of `/opt`.

    `sudo ncdu -x /` is one way to verify the size of `/opt`.
    
    `df -h` is one way to verify the amount of free space available.

This backup will take some time, likely hours, and all your containers may be down the entire time depending on your disk setup.

??? note "Why so long, why are the containers down, and what can I do about this?"

    It stops all containers, creates tar archives of all directories in `/opt`, restarts all containers, then uploads the tar archives to any destinations that you have set up in the [backup config](../../saltbox/backup/settings.md).  All your containers will be down for the duration of the `tar` process.

    The containers are down to prevent any applications from writing to their databases or the like while the tar process is ongoing, which could corrupt the backup and the active files.  You may ask, "Why not do them one at a time?"  This is effectively impossible since there is no fixed relationship between container and appdata folder, especially with custom containers defined by the user.

    If your `/opt` directory is on a `BTRFS` volume, the containers are down for a few seconds as a snapshot is taken, then they are brought back up and the `tar` operation works from the snapshot.  The entire process still takes as long as before, but the containers aren't down the entire time.

    This applies regardless of whether you are running the backup manually or on a schedule.

## Manual Backup

!!! info
    This step assumes you have completed the configuration of the `backup_config.yml` in the configuration [step](../../saltbox/backup/settings.md).

    Specifically, you should make sure you have defined and enabled your desired destination(s) for the backup.


=== "Without Screen"

    ```shell
    sb install backup
    ```

    This will begin the backup in the active terminal; you will not be able to close the terminal or disconnect from your server while the backup proceeds.  If you do so [deliberately or accidentally], the backup will be aborted.

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

    There are of course alternatives to `screen` that you may prefer.

## Scheduled Backup

!!! info
    This step assumes you have completed the configuration of the `backup_config.yml` in the configuration [step](../../saltbox/backup/settings.md).

    Specifically, you should make sure you have defined and enabled your desired destination(s) for the backup, **and** if you want this to **create** the cron task, set `enabled` to `yes`:

    ```yaml
    cron:
      cron_time: weekly 
      enable: yes
    ```


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

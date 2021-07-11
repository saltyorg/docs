# Backup

With Saltbox you can either run a backup task manually or schedule it to run automatically.

## Manual Backup

!!! info
    This step assumes you have completed the configuration of the `backup_config.yml` in the configuration step.

=== "Without Screen"
    ``` shell
    sb install backup
    ```

=== "With Screen"
    ``` shell
    screen -dmS saltbox-backup sb install backup
    ```

    ``` shell
    screen -r
    ```

    ``` shell
    CTRL A + D
    ```

## Scheduled Backup

!!! info
    This step assumes you have completed the configuration of the `backup_config.yml` in the configuration step.

=== "Have Saltbox configure cron"
    ``` shell
    sb install set-backup
    ```

=== "Configure cron manually"
    ``` shell
    crontab -e
    ```

    ``` shell
    0 4 * * * sudo PATH='/usr/bin:/bin:/usr/local/bin' env ANSIBLE_CONFIG='/srv/git/saltbox/ansible.cfg' '/usr/local/bin/ansible-playbook' '/srv/git/saltbox/backup.yml' >> '/home/seed/logs/saltbox_backup.log' 2>&1
    ```

    Remember to edit the seed username if you changed the Saltbox user in the `accounts.yml`.

    Visit [crontab.guru](https://crontab.guru/) for help with the scheduling format.

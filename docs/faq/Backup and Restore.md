
# Backup and Restore

IT IS QUITE PROBABLE THAT SOME INFORMATION HERE IS OUTDATED

[PLEASE OPEN ISSUES](https://github.com/saltyorg/docs/issues)

## What is backed up?

Only app data located in `/opt` and relevant config files (as listed below) are backed up.  The backup script does this by creating tarball files for each folder in `/opt` and placing them into your backup folder (as set in [`backup_config.yml`](../saltbox/backup/settings.md).). The folders in `/opt` are*all* backed up without regard for whether Saltbox created them in the first place.  For example, if you create `/opt/bingbangboing` it will be backed up and restored by Saltbox.

If you have set it up, the Sandbox repo is located in `/opt`, so it will get backed up [this includes any changes you've made in that repo to the config or roles].  There is no catalog kept of what Sandbox roles you may have run, so none of the roles themselves will be run automatically on restore, but the data will be backed up and restored.

Service files from `/etc/systemd/system` are synced to `/opt/systemd-backup` as part of the backup, so they are included in the tarball creation.  This includes things like the `rclone_vfs`, `mergerfs`, `cloudplow`, `plex_autoscan`, and other system service files.  If you have added additional mounts and the like via your own service files [perhaps with tip #44 or `samount` or the like], these extra service files will be backed up, but will not be automatically restored.

Torrent seeding content, NZBGet queue, anything in `/mnt/`, `/home/`, or anywhere else other than the `/opt/` folder, will **NOT** be backed up (media files are moved to the cloud via [Cloudplow](../apps/cloudplow.md), anyway). If you do want to backup your seeding data, check out the scripts located in `/opt/scripts/rclone/` folder.

If Rclone/Rsync are enabled, the backup will be uploaded to a remote destination.

If `keep_local_copy` is enabled, the backup will remain locally in the backup folder; If NOT, the backup will be deleted. If you decide to disable Rclone/Sync, then at least have `keep_local_copy` enabled, or else the backup will be created and then deleted right after.

The config files that are backed up are:

- `ansible.cfg`

- `accounts.yml`

- `settings.yml`

- `adv_settings.yml`

- `rclone.conf`

- `backup_excludes.txt` (if one exists in the `saltbox` folder).

These files are kept separately from the backup tarball files to allow for easy access.

Nice table to see what is restored during simple backup/restore:

| <pre>                         </pre> Items Backed UP              | <pre>     </pre> Backed Up From                   | <pre>     </pre> Restored To |
|:----------------------------- |:-------------------------------- |:----------- |
| Application Data              | `/opt/`                          | `/opt/`     |
| Ansible Config                | `/srv/git/saltbox/ansible.cfg`         |             |
| Account Settings              | `/srv/git/saltbox/accounts.yml`        |             |
| Saltbox Settings             | `/srv/git/saltbox/settings.yml`        |             |
| Saltbox Advanced Settings    | `/srv/git/saltbox/adv_settings.yml`    |             |
| Backup Excludes List (custom) | `/srv/git/saltbox/backup_excludes_list.txt` |  `~/saltbox/backup_excludes_list.txt`           |
| Rclone Config                 | `~/.config/rclone/rclone.conf`   | `~/.config/rclone/rclone.conf`            |

## What is Saltbox Restore Service?

An optional service that allows for easy backing up and restoring of CLIENT-SIDE ENCRYPTED config files.

The config files that are backed up are:

- `ansible.cfg`

- `accounts.yml`

- `settings.yml`

- `adv_settings.yml`

- `backup_config.yml`

- `rclone.conf`

These files are the ones needed to run a successful restore.

!!! note
    `backup_excludes_list.txt` are not backed up into the Restore Service, simply because it is not important for a restore to work and also because it IS automatically restored during the restore process itself.

How does this work?

1. User fills in a username and password for Restore Service in the [`backup_config.yml`](../saltbox/backup/settings.md).

2. During backup, config files are **encrypted** on the client-side, using a **salt-hashed** version of the username and password (your raw username is never sent to the Restore Service), and then uploaded to the Restore Service.

3. When a user needs to restore their backup on a new box, they can pull their backed up config files from the Restore Service with a single command.

The source code for the Restore Service Scripts are listed below:

- <https://github.com/saltyorg/Saltbox/blob/master/roles/backup/tasks/restore_service.yml> (Backup Script)
- <https://github.com/saltyorg/scripts/blob/master/restore.sh> (Restore Script)

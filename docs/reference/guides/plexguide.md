# Migrating from PlexGuide to Saltbox

These are some rough notes on migrating from PlexGuide to Saltbox

Some important files and their locations:

|     file       |           PlexGuide location         |         saltbox default location        |
|:---------------|:-------------------------------------|:----------------------------------------|
| `rclone.conf`  | `/opt/appdata/plexguide/rclone.conf` | `/home/seed/.config/rclone/rclone.conf` |
| SA JSON files  | `/opt/appdata/plexguide/.blitzkeys`  | `/opt/sa/all`                           |


if you are restoring the arrs from pg to saltbox you will need to make these changes in SB

```shell
sudo mkdir /mnt/gdrive
```

```shell
sudo chown $USER:$USER /mnt/gdrive
chmod 775 /mnt/gdrive
```

```shell
sudo cp "/etc/systemd/system/rclone_vfs.service" "/etc/systemd/system/gdrive.service"
sudo nano "/etc/systemd/system/gdrive.service"
```
Changes:
```yaml
  google: /mnt/remote
```

becomes

```yaml
  google: /mnt/gdrive
```
AND

```ini
ExecStop=/bin/fusermount -uz /mnt/remote
```

becomes

```ini
ExecStop=/bin/fusermount -uz /mnt/gdrive
```

```shell
sudo systemctl enable gdrive.service
sudo systemctl start gdrive.service
```

These notes do not represent everything you need to do to migrate; the two systems are very different and there is no automation aroudn migration.

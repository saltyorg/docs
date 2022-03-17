# Migrating from PlexGuide to Saltbox

These are some rough notes on migrating from PlexGuide to Saltbox

PG rclone.conf Location: `/opt/appdata/plexguide/rclone.conf`

PG Service accounts Location: `/opt/appdata/plexguide/.blitzkeys`

if you are restoring the arrs from pg to saltbox you will need to make the below changes in SB

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

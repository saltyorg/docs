# Migrating from PlexGuide to Saltbox

These are some rough notes on migrating from PlexGuide to Saltbox.

If you are a PlexGuide/PTS user moving to Saltbox, additions and corrections to these notes are appreciated and encouraged.  None of the Saltbox Team have used PlexGuide, and these notes have been provided for the most part by people who have made the switch to Saltbox.

If you find things missing or unclear, PLEASE provide updates.

Some important files and their locations:

|     file       |           PlexGuide location         |         saltbox default location        |
|:---------------|:-------------------------------------|:----------------------------------------|
| `rclone.conf`  | `/opt/appdata/plexguide/rclone.conf` | `/home/seed/.config/rclone/rclone.conf` |
| SA JSON files  | `/opt/appdata/plexguide/.blitzkeys`  | `/opt/sa/all`                           |

## Service Accounts

PlexGuide removed the `.json` extension from its service account files, which it called "BlitzKeys".  As with many design decisions in PlexGuide/PTS, the rationale for both the action and the rebranding is unclear.

Most things that interact with service accounts in Saltbox expect that those files will have the extension.  If you want to use these service account files with Cloudplow [for uploading to Google Drive] or SARotate [for spreading Google Drive API usage across service accounts], they will need to have the `.json` extension restored.

One way to add the extension to all these files:

`cd` to the directory containing the "BlitzKeys" and run:

```
rename 's/$/\.json/' *
```

Copy these "BlitzKeys" to `/opt/sa/all` and set appropriate permissions.

## Rclone.conf

Once you have moved the Rclone.conf file, you need to edit it.  At the bottom of the file, you will have something like this:

```ini
[pgunion]
type = union
remotes = gdrive: tdrive: gcrypt: tcrypt: /mnt/move
```

1. Rename pgunion to google
2. Remove /mnt/move
AND
3. If you are using encryption - Remove gdrive: and tdrive
4. If you are not using encryption - Remove gcrypt: and tcrypt: if they exist.

Final should look like:

```ini
[google]
type = union
remotes = gdrive: tdrive:
```

or

```ini
[google]
type = union
remotes = gcrypt: tcrypt:
```

Once this is saved, you need to install the mount service:

```shell
sb install mounts
```
IMPORTANT: if you are going through the initial setup DO NOT RUN THIS `mounts` TAG until you've installed saltbox `core` at least [which will run the `mounts` tag].

## Cloudplow changes

```shell
nano /opt/cloudplow/config.json
```

Under "Remotes":, locate

```json
"upload_remote": "google"
```

Change this to:

```json
"upload_remote": "tdrive:"
```

or

```json
"upload_remote": "tcrypt:"
```

Now we need to add your service accounts..  Under the "uploader" section change:

```json
"service_account_path": ""
```

to

```json
"service_account_path": "/opt/sa/all"
```

^ Assuming you put the service accounts in that location, if not, change accordingly.

## Migrating Arrs

If you are restoring the arrs from pg to saltbox you will need to make these changes in SB.
Repeat for tdrive, gcrypt, and tcrypt as needed for your setup.

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

If you get an error about port 5572 already being in use, you will need to update the port in `gdrive.service`:

```
  --rc-addr=localhost:5572 \
```
to
```
  --rc-addr=localhost:5573 \
```

Or some other unused port number.


These notes do not represent everything you need to do to migrate; the two systems are very different and there is no automation around migration.

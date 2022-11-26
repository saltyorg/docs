# Migrating from PlexGuide to Saltbox

These are some rough notes on migrating from PlexGuide to Saltbox

Some important files and their locations:

|     file       |           PlexGuide location         |         saltbox default location        |
|:---------------|:-------------------------------------|:----------------------------------------|
| `rclone.conf`  | `/opt/appdata/plexguide/rclone.conf` | `/home/seed/.config/rclone/rclone.conf` |
| SA JSON files  | `/opt/appdata/plexguide/.blitzkeys`  | `/opt/sa/all`                           |

## Service Accounts

PlexGuide removed the `.json` extension from its service account files, which it called "BlitzKeys".  Most things that interact with service accounts in saltbox expect that those files will have the extension.

Copy these BlitzKeys and set appropriate permissions.  You do not need to add the .json extention, we just need to make sure they are being referenced later.

## Rclone.conf

Once you have moved the Rclone.conf file, you need to edit it.  At the bottom of the file, you will have something like this:

```
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
```
[google]
type = union
remotes = gcrypt: tcrypt:
```

Once this is saved, you need to install the mount service:

```shell
sb install mounts
```

## Cloudplow changes

If you are using encryption, you definitly need to change this.  If not, unsure but see for yourself:

```shell
nano /opt/cloudplow/config.json
```

Under "Remotes":, locate
```
"upload_remote": "google"
```
Change this to
```
"upload_remote": "tcrypt:"
```

Now we need to add your service accounts..  Under the "uploader" section change:
```
"service_account_path": ""
```
to
```
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

These notes do not represent everything you need to do to migrate; the two systems are very different and there is no automation around migration.

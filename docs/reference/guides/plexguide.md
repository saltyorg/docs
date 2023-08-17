# Migrating from PlexGuide to Saltbox

These are some rough notes on migrating from PlexGuide to Saltbox.

If you are a PlexGuide/PTS user moving to Saltbox, additions and corrections to these notes are appreciated and encouraged.  None of the Saltbox Team have used PlexGuide, and these notes have been provided for the most part by people who have made the switch to Saltbox.

If you find things missing or unclear, PLEASE provide updates.

Some important files and their locations:

|     file       |           PlexGuide location         |         saltbox default location        |
|:---------------|:-------------------------------------|:----------------------------------------|
| `rclone.conf`  | `/opt/appdata/plexguide/rclone.conf` | `/home/seed/.config/rclone/rclone.conf` |
| SA JSON files  | `/opt/appdata/plexguide/.blitzkeys`  | `/opt/sa/all`                           |

Where we'll be changing saltbox files:

|     file         |            saltbox default location                    |
|:-----------------|:-------------------------------------------------------|
| intentory file   | `/srv/git/saltbox/inventories/host_vars/localhost.yml` |
| rclone vfs files | `/etc/systemd/system/gcrypt.service`                   | Only if you enabled encryption
| rclone vfs files | `/etc/systemd/system/tcrypt.service`                   | Only if you enabled encryption AND team drives
| rclone vfs files | `/etc/systemd/system/gdrive.service`                   | Only if you DIDN'T enable encryption
| rclone vfs files | `/etc/systemd/system/tdrive.service`                   | Only if you DIDN'T enable encryption but DID enable team drives.

## Service Accounts

PlexGuide removed the `.json` extension from its service account files, which it called "BlitzKeys".  As with many design decisions in PlexGuide/PTS, the rationale for both the action and the rebranding is unclear.

Most things that interact with service accounts in Saltbox expect that those files will have the extension.  If you want to use these service account files with Cloudplow [for uploading to Google Drive] or SARotate [for spreading Google Drive API usage across service accounts], they will need to have the `.json` extension restored.

Here's one way to add the extension to all these files:

`cd` to the directory containing the "BlitzKeys" and run:

```
rename 's/$/\.json/' *
```

Note: that's not the only way, just one way, offered without warranty.

Copy these "BlitzKeys" to `/opt/sa/all` and set appropriate permissions. 

```
chd /opt/sa/all
sudo chown $USER:$USER *
```


## Rclone.conf

Once you have moved the Rclone.conf file to /home/seed/.config/rclone/rclone.conf, you need to edit it and understand how it's currently configured. 
Here is a sample config with all of the private info removed. You will need to reference the names of each mount you have configured in the rest of the config. This step is important to understand
your config file may vary, you may not have service accounts, you may not have any crypt remotes, you may not have a team remote. In the steps moving forward only repeat them for the mounts you 
have configured here in rclone. 
```
#------------------------------------------
#PGClone| Visit https://pgblitz.com
#------------------------------------------
[gdrive] #Everyone has this mount, it connects rclone to your google drive. no changes
client_id = PRIVATEINFO
client_secret = PRIVATEINFO
type = drive
token = {"access_token":"PRIVATEINFO"}

[gcrypt] #People who chose to encrypt their data will have this mount. It uses the gdrive mount and encrypts everything in the /encrypt folder in gdrive. no changes. will be mounted by the service file at \etc\systemd\system\gcrypt.service
type = crypt
remote = gdrive:/encrypt
filename_encryption = standard
directory_name_encryption = true
password = PRIVATEINFO
password2 = PRIVATEINFO

[tdrive] #Some people will have configured a team drive, most will have service accounts below to upload to this team drive. no changes
client_id = PRIVATEINFO
client_secret = PRIVATEINFO
type = drive
token = {"access_token":"PRIVATEINFO"}
team_drive = PRIVATEINFO

[tcrypt] #Same thing as gcrypt, this encrypts everything in your teamdrive's /encrypt folder. no changes. will be mounted by the service file at \etc\systemd\system\tcrypt.service
type = crypt
remote = tdrive:/encrypt
filename_encryption = standard
directory_name_encryption = true
password = PRIVATEINFO
password2 = PRIVATEINFO

[GDSA01] #This is a service account mount. You will have any number of them, perhaps 10, perhaps 50. You'll need to move the "blitzkeys" to the specified location and update the path here for each one.
type = drive
scope = drive
service_account_file = /opt/appdata/plexguide/.blitzkeys/GDSA01 
team_drive = PRIVATEINFO

[GDSA01C] #This encrypts your service account mount in and uses the /encrypt folder
type = crypt
remote = GDSA01:/encrypt
filename_encryption = standard
directory_name_encryption = true
password = PRIVATEINFO
password2 = PRIVATEINFO

[pgunion] #This was used to join both gcrypt and tcrypt together, you can leave it as is because we'll be using mergerfs to accomplish the same thing. this is replaced by the inventory file at /srv/git/saltbox/inventories/host_vars/localhost.yml 
type = union
remotes = gdrive: tdrive: gcrypt: tcrypt: /mnt/move
```


## Mounting gcrypt and tcrypt or gdrive and tdrive

Create the rclone vfs service files for each mount in your rclone.conf.
Repeat for tdrive, gcrypt, and tcrypt as needed for your setup. If you encrypted everything you only need to do this for gcrypt and tcrypt. If you didn't setup team drives you can skip tcrypt/tdrive
Remember that anything with a colon at the end like gcrypt: tcrypt: gdrive: tdrive: is referencing the name of the remote in your rclone config file so use whatever is there.

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
  gdrive: /mnt/gdrive
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
and
```
--url http://localhost:5572 _async=true
```

to
5573

Or some other unused port number.

## Updating mergerfs to include all mounts:

sudo nano /srv/git/saltbox/inventories/host_vars/localhost.yml

add
```
mergerfs_mount_branches: "/mnt/local=RW:/mnt/tcrypt=NC:/mnt/gcrypt=NC"
```
this combines /mnt/tcrypt, /mnt/gcrypt, /mnt/local all under /mnt/unionfs
only include the mounts that are in your rclone file. if you're unencrypted it will be:
```
mergerfs_mount_branches: "/mnt/local=RW:/mnt/tdrive=NC:/mnt/gdrive=NC"
```

IMPORTANT: if you are going through the initial setup DO NOT RUN THIS `mounts` TAG until you've installed saltbox `core` at least [which will run the `mounts` tag].  The `mounts` tag depends on other things that the `core` tag installs.

```shell
sb install mounts
```

## Cloudplow changes

NOTE: This is assuming you want to keep uploading to the drives you had set up in PG/PTS.

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

#Fixing the media directories
Adding a shortcut between gcrypt:/tv and gcrypt:/Media/TV
https://discordapp.com/channels/853755447970758686/1123075813093408778

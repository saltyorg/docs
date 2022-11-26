# Migrating from PlexGuide to Saltbox

These are some rough notes on migrating from PlexGuide to Saltbox

Some important files and their locations:

|     file       |           PlexGuide location         |         saltbox default location        |
|:---------------|:-------------------------------------|:----------------------------------------|
| `rclone.conf`  | `/opt/appdata/plexguide/rclone.conf` | `/home/seed/.config/rclone/rclone.conf` |
| SA JSON files  | `/opt/appdata/plexguide/.blitzkeys`  | `/opt/sa/all`                           |


Use cloudcmd or ftp to copy keys from .blitzkeys and rename from GDSA01, GDSA02 to 
001.json, 002.json etc. and upload to `/opt/sa/all`
Then copy rclone.conf and edit to look like this:

```shell
[gdrive]
client_id = bingbangbong
client_secret = bongbangbing
type = drive
server_side_across_configs = true
token = tokenbingbang

[tdrive]
type = drive
server_side_across_configs = true
service_account_file = /opt/sa/all/001.json
team_drive = TEAMDRIVEIDbingbang

[google]
type = union
remotes = gdrive: tdrive: /mnt/move
```
Removing the extra lines for:
```
[GDSA01]
type = drive
scope = drive
service_account_file = /opt/appdata/plexguide/.blitzkeys/GDSA01
team_drive = TEAMDRIVEIDbingbang

[GDSA02]
type = drive
scope = drive
service_account_file = /opt/appdata/plexguide/.blitzkeys/GDSA02
team_drive = TEAMDRIVEIDbingbang
```


Then upload to `/home/seed/.config/rclone/` replacing `seed` with your user name if not default.
You will likely need to change paths in Arrs as well, as SB uses different paths.

These notes do not represent everything you need to do to migrate; the two systems are very different and there is no automation around migration.

For example, PlexGuide apparently removed the `.json` extension from its service account files, which it called "BlitzKeys".  Most things that interact with service accounts in saltbox expect that those files will have the extension.

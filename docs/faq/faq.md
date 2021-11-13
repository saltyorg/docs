
---
# FAQ

IT IS QUITE PROBABLE THAT SOME INFORMATION HERE IS OUTDATED

[PLEASE OPEN ISSUES](https://github.com/saltyorg/docs/issues)

## System

### Can I install this on an ARM machine?

ARM is not supported.


### If you are using a Scaleway server...

1. Choose an X86 server (vs ARM).

2. Select "Ubuntu Xenial" as the distribution.

3. Click the server on the list.

4. Under "ADVANCED OPTIONS", click "SHOW".

5. Set "ENABLE LOCAL BOOT" to `off`.

   ![](../images/faq/scaleway-01.png)
   
6. Click the "BOOTSCRIPT" link and select one above > 4.10.

   ![](../images/faq/scaleway-02.png)

7. Start the server.


Reference: https://www.scaleway.com/docs/bootscript-and-how-to-use-it/


### If you are using an OVH server...

If you are having issues upgrading the kernel on ovh, where the kernel upgrade is not taking effect..

 `uname -r` to see if you have `grs` in kernel version string...

 if so, see https://pterodactyl-daemon.readme.io/v0.4/docs/updating-ovh-kernel on how to update the kernel.



### Find your User ID (UID) and Group ID (GID)

Use the following commands to find out your account's user name and group info:

```
id
```
or

```
id `whoami`
```
You'll see a line like the following:

```
uid=XXXX(yourusername) gid=XXXX(yourgroup) groups=XXXX(yourgroup)
```

### How to create a user account

- Run the following commands line by line:

   ```bash
   sudo useradd -m <username>
   sudo usermod -aG sudo <username>
   sudo passwd <username>
   sudo chsh -s /bin/bash <username>
   su <username>
   ```


### Change shell of user account to bash

How to check current shell:

```shell
echo $0
-sh
```

or

```shell
echo ${SHELL}
/bin/sh
```

Run this command to set bash as your shell (where `<user>` is replaced with your username):

```
sudo chsh -s /bin/bash <user>
sudo reboot
```

### How to fix permission issues


 /opt folder

1. Stop all docker containers

   ```
   docker stop $(docker ps -a -q)
   ```

2. Change ownership of /opt. Replace `user` and `group` to match yours' (see [here](FAQfind-your-user-id-uid-and-group-id-gid)).

   ```
   sudo chown -R user:group /opt
   ```

3. Change permission inheritance of /opt.

   ```
   sudo chmod -R ugo+X /opt
   ```

4. Start all docker containers

   ```
   docker start $(docker ps -a -q)
   ```


 /mnt folder


1. Run the `mounts` tag

   ```
   sb install mounts
   ```

## Cloudflare

### API request not authenticated

If you get this error during SB Install:

```
fatal: [localhost]: FAILED! => {"changed": false, "msg": "API request not authenticated; Status: 403; Method: GET: Call: /zones?name=; Error details: code: 9103, error: Unknown X-Auth-Key or X-Auth-Email; "}
```

Make sure:

- The `email` in [settings.yml](../reference/accounts.md) matches the one you have listed for your Cloudflare.com account.

- The `cloudflare_api_key` in  [settings.yml](../reference/accounts.md matches your `domain`'s Cloudflare [Global API Key]().


## Cloud Storage


### Does Saltbox support encrypted data on the cloud?

In short, no. Saltbox does not come with encryption support out-of-box.

### Why does Saltbox not support encryption data on the cloud?

While there are pro's and cons for using either encrypted or unencrypted data on cloud services, we've decided to not deal with encryption for the out of box setup.

However, since Saltbox uses Rclone VFS to mount cloud data, you can tweak the mounts and remotes to do this yourself. But doing so comes with no support/help from us. 


## Saltbox Backup and Restore

### What is backed up?

Only app data located in `/opt` and relevant config files (as listed below) are backed up.  The backup script does this by creating tarball files (*.tar) for each folder in `/opt`/ and placing them into your backup folder (as set in `backup_config.yml`). The folders in `/opt` are *all* backed up without regard for whether Saltbox created them in the first place.  For example, if you create `/opt/bingbangboing` it will be backed up and restored by Saltbox.

If you have set it up, the community repo is located in `/opt`, so it will get backed up [this includes any changes you've made in that repo to the config or roles].  There is no catalog kept of what community roles you may have run, so none of the roles themselves will be run automatically on restore, but the data will be backed up and restored.
 
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

Note that the `.ansible_vault` file is NOT backed up.

Nice table to see what is restored during simple backup/restore:

| <pre>                         </pre> Items Backed UP              | <pre>     </pre> Backed Up From                   | <pre>     </pre> Restored To |
|:----------------------------- |:-------------------------------- |:----------- |
| Application Data              | `/opt/`                          | `/opt/`     |
| Ansible Config                | `~/saltbox/ansible.cfg`         |             |
| Account Settings              | `~/saltbox/accounts.yml`        |             |
| Saltbox Settings             | `~/saltbox/settings.yml`        |             |
| Saltbox Advanced Settings    | `~/saltbox/adv_settings.yml`    |             |
| Backup Excludes List (custom) | `~/saltbox/backup_excludes_list.txt` |  `~/saltbox/backup_excludes_list.txt`           |
| Rclone Config                 | `~/.config/rclone/rclone.conf`   | `~/.config/rclone/rclone.conf`            |

## Saltbox Install

### Ansible Tags

Multiple Tags

Run multiple tags together by separating them with commas, no spaces. Quotes are optional. Order is not important.

Use this to install containers or roles that are not included in "default" install types.  

Example:

```
sb install core,emby,sonarr,radarr,nzbget,nzbhydra2
```

 Error while fetching server API version

Full error message:

```
Error Connecting:  Error while fetching server API version: Timeout value connect was Timeout(connect=60, read=60, total=None), but it must be an int or float.
```


Run `sudo pip install requests==2.10.0` and retry.

### 403 Client Error: Forbidden: endpoint with name \<container name\> already exists in network \<network name\>

Example:

```
fatal: [localhost]: FAILED! => {"changed": false, "failed": true, "msg": "Error starting container 6fb60d4cdabe938986042e06ef482012a1d85a66a099d861f08062d8262c2ef7: 403 Client Error: Forbidden (\"{\"message\":\"endpoint with name jackett already exists in network bridge\"}\")"}
    to retry, use: --limit @/home/seed/saltbox/saltbox.retry
PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=1
```

You have a remnant of the container in the Docker's network.

You can verify with the command below (replace `<network name>` and `<container name>` is replaced with the network name and container name mentioned in the error, respectively):
```
docker inspect network <network name> | grep <container name>
```

To remove the remnant, run this command and try again:

```
docker network disconnect -f <network name> <container name>
```


### 500 Server Error: Internal Server Error: driver failed programming external connectivity on endpoint \<container name\> bind for 0.0.0.0:\<port number\> failed: port is already allocated

```
sudo service docker stop
sudo service docker start
```




## Updating Saltbox

Follow the appropriate steps from [this page](../saltbox/basics/update.md)

## Docker

### Why does Saltbox use the Docker network "saltbox" instead of bridge?

(1) keeps all Saltbox containers organized under one network; and (2), bridge network does not allow network aliases.


## Rclone



### Rclone error: Failed to save config file: open /home/\<user\>/.config/rclone/rclone.conf: permission denied

Replace `user` and `group` to match yours' (see [here](FAQ#find-your-user-id-uid-and-group-id-gid)).


```
sudo chown -R user:group ~/.config/rclone/
sudo chmod -R 0755 ~/.config/rclone/
```



## Remote


### Don't see your remote files in /mnt/remote?

[See here](../community/guides/chazguides/no-media.md)

## Plex


### If you are unable to find your Plex server

You may resolve this by either

 - Installing Saltbox again (do this for new Plex DBs/installs):

   - **THIS WILL DELETE ANY EXISTING PLEX CONFIGURATION SUCH AS LIBRARIES**

   - Remove Plex Container (it may show "Error response from daemon: No such container" if not created yet):

     ```
     sudo docker rm -f plex
     ```

   - Remove the Plex folder:

     ```
     sudo rm -rf /opt/plex
     ```

   - Reinstall the Plex container:

     ```
     sb install plex
     ```

 - Installing Saltbox again (do this for existing Plex DBs/installs):

   - **THIS WILL LEAVE ANY EXISTING PLEX LIBRARIES AND METADATA INTACT**

   - Remove Plex Preferences file. 

     ```
     sudo rm "/opt/plex/Library/Application Support/Plex Media Server/Preferences.xml"
     ```

   - Reinstall the Plex container by running the following command:

     ```
     sb install plex
     ```


 - Using SSH Tunneling to log into Plex and set your credentials:

   - On your host PC (replace `<user>` with your user name and `<yourserveripaddress>` with your serveripaddress - no arrows):

     ```
     ssh <user>@<yourserveripaddress> -L 32400:0.0.0.0:32400 -N
     ```

     This will just hang there without any message. That is normal.

   - In a browser, go to http://localhost:32400/web.

   - Log in with your Plex account.

   - On the "How Plex Works" page, click “GOT IT!”.

   - Close the "Plex Pass" pop-up if you see it.

   - Under "Server Setup", you will see "Great, we found a server!". Give your server a name and tick “Allow me to access my media outside my home”. Click "NEXT".

   - On "Organize Your Media", hit "NEXT" (you will do this later). Then hit "DONE".

   - At this point, you may `Ctrl + c` on the SSH Tunnel to close it.



 If Plex shows you an incorrect title with the filename (eg RARBG releases)

Reorder the Plex agents for TV/Movies so that local assets are at the bottom.


### Fix permission issues with Plex logs


Replace `user` and `group` to match yours' (see [here](FAQ#find-your-user-id-uid-and-group-id-gid)).

```
sudo chown -R user:group /opt/plex/Library/Logs
sudo chmod -R g+s /opt/plex/Library/Logs
```

_Note: If you have a separate Plex and Feeder setup, this will be done on the server where Plex is installed._


## Plex Autoscan

### Newly downloaded media from Sonarr and Radarr are not being added to Plex?

- Test another download and run the following command:
  ```
   tail -f /opt/plex_autoscan/plex_autoscan.log
  ```

- If you see this...

   ```
   terminate called after throwing an instance of 'boost::filesystem::filesystem_error'
   boost::filesystem::create_directories: Permission denied: "/config/Library/Logs"
   ```

  There is an issue with the permissions on that folder that you'll need to fix manually (Saltbox can't fix this as Plex creates this folder after the first scan)

   To fix this, Run the following command. Replace `user` and `group` to match yours' (see [here](FAQ#find-your-user-id-uid-and-group-id-gid)).

   ```
   docker stop plex
   sudo chown -R user:group /opt/plex
   docker start plex
   ```


   Example of a successful scan:

   ```
   2017-10-10 17:48:26,429 -    DEBUG -      PLEX [ 6185]: Waiting for turn in the scan request backlog...
   2017-10-10 17:48:26,429 -     INFO -      PLEX [ 6185]: Scan request is now being processed
   2017-10-10 17:48:26,474 -     INFO -      PLEX [ 6185]: No 'Plex Media Scanner' processes were found.
   2017-10-10 17:48:26,474 -     INFO -      PLEX [ 6185]: Starting Plex Scanner
   2017-10-10 17:48:26,475 -    DEBUG -      PLEX [ 6185]: docker exec -u plex -i plex bash -c 'export LD_LIBRARY_PATH=/usr/lib/plexmediaserver;/usr/lib/plexmediaserver/Plex\ Media\ Scanner --scan --refresh --section 1 --directory '"'"'/data/Movies/Ravenous (1999)'"'"''
   2017-10-10 17:48:33,712 -     INFO -     UTILS [ 6185]: GUI: Scanning Ravenous (1999)
   2017-10-10 17:48:33,959 -     INFO -     UTILS [ 6185]: GUI: Matching 'Ravenous'
   2017-10-10 17:48:38,556 -     INFO -     UTILS [ 6185]: GUI: Score for 'Ravenous' (1999) is 117
   2017-10-10 17:48:38,607 -     INFO -     UTILS [ 6185]: GUI: Requesting metadata for 'Ravenous'
   2017-10-10 17:48:38,705 -     INFO -     UTILS [ 6185]: GUI: Background media analysis on Ravenous
   2017-10-10 17:48:39,201 -     INFO -      PLEX [ 6185]: Finished scan!
   ```


### Plex Autoscan log shows error during empty trash request

```
ERROR - PLEX [10490]: Unexpected response status_code for empty trash request: 401
```

You need to generate another token and re-add that back into the config. See [Plex Autoscan]().



### Plex Autoscan error with metadata item id

Example Log:
```
 2017-11-21 04:26:32,619 -    ERROR -      PLEX [ 7089]: Exception finding metadata_item_id for '/data/TV/Gotham/Season 01/Gotham - S01E01 - Pilot.mkv':
 2017-11-21 04:26:32,619 -     INFO -      PLEX [ 7089]: Aborting analyze of '/data/TV/Gotham/Season 01/Gotham - S01E01 - Pilot.mkv' because could not find a metadata_item_id for it
```


Possible Issues:

- One of the mounts has changed (e.g. Rclone_VFS or MergerFS was restarted).

- Permission issues (see [here]).

Solution 1:

1. Make sure the remote mount is working OK (pick the relevant one below).

   The current default used for mounting cloud storage is Rclone VFS:

   ```
   sudo systemctl status rclone_vfs
   ```

2. Make sure the union mount is working OK. 

   The current default used for creating the union mount is MergerFS:

   ```
   sudo systemctl status mergerfs
   ```

3. Restart Plex:
   ```
   docker stop plex && docker start plex
   ```

Solution 2:

If all else fails, disable analyze in config.

1. Open `/opt/plex_autoscan/config/config.json`

   ```
   nano /opt/plex_autoscan/config/config.json
   ```

1. Make the following edit:

   ```
   "PLEX_ANALYZE_TYPE": "off",
   ```

1. Restart Plex Autoscan

   ```
   sudo systemctl restart plex_autoscan
   ```


### Purpose of a Control File in Plex Autoscan

Every time Sonarr or Radarr downloads a new file, or upgrades a previous one, a request is sent to Plex via Plex Autoscan to scan the movie folder or TV season path and look for changes. Since Sonarr and Radarr delete previous files on upgrades, the scan will cause the new media to show up in your Plex Library, however, the deleted files would be missing, and instead, marked as "unavailable" (i.e. trash icon). When the control file is present and the option in the Plex Autoscan config is enabled (default), Plex Autoscan will empty the trash for you, thereby, removing the deleted media from the library.

If the remote mount for you cloud storage provider (e.g. Google Drive) ever disconnected during a Plex scan of your media, Plex would mark the missing files as unavailable and emptying the trash would cause them to be removed out of the library. To avoid this from happening, Plex Autoscan checks for a control file in the unionfs path (i.e. `/mnt/unionfs/mounted.bin)` before running any empty trash commands. The control file is just a blank file that resides on the root folder of your Rclone remote (i.e. cloud storage provider) and let's Plex Autoscan know that it is still mounted.

Once the remote is remounted, all the files marked unavailable in Plex will be playable again and Plex Autoscan will resume its emptying trash duties post-scan.

To learn more about Plex Autoscan, visit https://github.com/l3uddz/plex_autoscan.

**TLDR: Plex Autoscan will not remove deleted media out of Plex without it.**



### Plex Autoscan Localhost Setup

If you are using an all-in-one Saltbox and don't want to have the Plex Autoscan port open, you may set it up so that it runs on the localhost only.

To do so, follow these steps:

 Option 1


**Plex Autoscan:** (only if changed from default)

1. Open `/opt/plex_autoscan/config/config.json`

   ```
   nano /opt/plex_autoscan/config/config.json
   ```

2. Make the following edit:

   ```
   "SERVER_IP": "0.0.0.0",
   ```

   _Note: This is the default config._

3. Restart Plex Autoscan

   ```
   sudo systemctl restart plex_autoscan
   ```

**Sonarr/Radarr:**

- Retrieve the 'Docker Gateway IP Address' by running the following:

  ```
  docker inspect -f '{{ .NetworkSettings.Networks.saltbox.Gateway }}' sonarr
  ```

- Replace the Plex Autoscan URL with:

  ```
  http://docker_gateway_ip_address:3468/yourserverpass
  ```

- You Plex Autoscan URL will now look like this:

  ```
  http://172.18.0.1:3468/yourserverpass
  ```

 Option 2

Alternatively, you can set it up this way:

_Note: This method benefits from completely closing off Plex Autoscan to the outside._


**Plex Autoscan:**

1. Retrieve the 'Docker Gateway IP Address' by running the following:

   ```
   docker inspect -f '{{ .NetworkSettings.Networks.saltbox.Gateway }}' sonarr
   ```

2. Open `/opt/plex_autoscan/config/config.json`

   ```
   nano /opt/plex_autoscan/config/config.json
   ```

3. Make the following edit:

   ```
   "SERVER_IP": "docker_network_gateway_ip_address",
   ```

4. This will now look like this:

   ```
   "SERVER_IP": "172.18.0.1",
   ```

5. Restart Plex Autoscan

   ```
   sudo systemctl restart plex_autoscan
   ```

**Sonarr/Radarr:**

- Replace the Plex Autoscan URL with:

  ```
  http://docker_gateway_ip_address:3468/yourserverpass
  ```

- You Plex Autoscan URL will now look like this:

  ```
  http://172.18.0.1:3468/yourserverpass
  ```


### Why is SERVER_SCAN_DELAY set to 180 seconds by default?

When Plex Autoscan gets a scan request from Sonarr, it tells Plex to scan the relevant TV Show season folder. So to avoid multiple Plex scans of the same season when more episodes of that same season come in, Plex Autoscan can wait (ala SERVER_SCAN_DELAY) and merge multiple scan requests into a single one. This is particularly noticeable when consecutive episodes are being downloaded/imported into Sonarr. 

During this SERVER_SCAN_DELAY, if another request comes in for the same season folder, it will restart the delay timer again, thus allowing for even more time for new items to come in. 

SERVER_SCAN_DELAY of 180 seconds was calculated with an average episode download time of a few minutes each. 

There is no harm in multiple Plex scans of the same season folder, except for more busyness of Plex, and perhaps more stress to it, so this delay will try to alleviate that. 

Alternative recommended settings are: 120 and 90 seconds. 

## Cloudplow

### Stuck on "Waiting for running upload to finish before proceeding..."

If the activity log is stuck on:

```
2018-06-03 13:44:59,659 - INFO       - cloudplow            - do_upload                      - Waiting for running upload to finish before proceeding...
```

This means that an upload task was prematurely canceled and it left lock file(s) to prevent another upload.

To fix this, run this command:

```
rm -rf /opt/cloudplow/locks/*
```

or

```
sudo systemctl restart cloudplow
```

## ruTorrent

### Change ruTorrent password after installation

1. Stop the container: 

   ```
   docker stop rutorrent
   ```

1. Go into the folder where ruTorrent .htpasswd resides: 

   ```
   cd /opt/rutorrent/nginx
   ```

1. Remove the old .htpasswd: 
   
   ```
   rm .htpasswd
   ```

1. Generate a new .htpasswd (where `USER` is your preferred username): 

   ```
   htpasswd -c .htpasswd USER
   ```

1. Verify that `/opt/rutorrent/nginx/nginx.conf` has the following lines:

   ```
   auth_basic "Restricted Content";
   auth_basic_user_file /config/nginx/.htpasswd;
   ```

1. Start the container: 

   ```
   docker start rutorrent
   ```


### Change ruTorrent download path after installation 

1. Stop ruTorrent Docker container:

   ```
   docker stop rutorrent
   ```

1. Edit the `rtorrent.rc` file:

   ```
   /opt/rutorrent/rtorrent/rtorrent.rc
   ```

1. Set the following options:

   ```
   directory = /downloads/rutorrent
   ```

1. Start ruTorrent Docker container:

   ```
   docker restart rutorrent
   ```

### Enable access to public torrent trackers

By default access to DHT, UDP, and PEX are disabled since most private trackers (and some server providers) do not allow this. Attempting to add a torrent from a public tracker would result in the torrent being stuck, like this:

![](../images/faq/rutorrent-01.png)

To enable access to public trackers, do the following:


1. Stop ruTorrent Docker container:

   ```
   docker stop rutorrent
   ```

2. Edit the `rtorrent.rc` file:

   ```
   /opt/rutorrent/rtorrent/rtorrent.rc
   ```

3. Set the following options:

   ```
   dht.mode.set = on
   ```

   ```
   trackers.use_udp.set = yes
   ```

   ```
   protocol.pex.set = yes
   ```


4. Start ruTorrent Docker container:

   ```
   docker start rutorrent
   ```


## Nextcloud


### Backup/Restore DB

DB data is stored in /opt/mariadb and backed up along with Saltbox Backup.

However, you can separately make a backup of the DB into a single `nextcloud_backup.sql` file, by running the following command.

```
docker exec mariadb /usr/bin/mysqldump -u root --password=password321 nextcloud  > nextcloud_backup.sql

```

And restoring it back:

```
cat nextcloud_backup.sql | docker exec -i mariadb /usr/bin/mysql -u root --password=password321 nextcloud

```

## Misc

### JSON Format Errors

Python or script errors mentioning an issue with the config file is usually due to an invalid JSON format in the file.

Examples:

```python
Traceback (most recent call last):
  File "scan.py", line 52, in <module>
    conf.load()
  File "/opt/plex_autoscan/config.py", line 157, in load
    cfg = self.upgrade(json.load(fp))
  File "/usr/lib/python2.7/json/__init__.py", line 291, in load
    **kw)
  File "/usr/lib/python2.7/json/__init__.py", line 339, in loads
    return _default_decoder.decode(s)
  File "/usr/lib/python2.7/json/decoder.py", line 364, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib/python2.7/json/decoder.py", line 380, in raw_decode
    obj, end = self.scan_once(s, idx)
ValueError: Expecting , delimiter: line 20 column 2 (char 672)
```

```python
Traceback (most recent call last):
  File "/opt/plex_autoscan/scan.py", line 52, in <module>
    conf.load()
  File "/opt/plex_autoscan/config.py", line 157, in load
    cfg = self.upgrade(json.load(fp))
  File "/usr/lib/python2.7/json/init.py", line 291, in load
    **kw)
  File "/usr/lib/python2.7/json/init.py", line 339, in loads
    return _default_decoder.decode(s)
  File "/usr/lib/python2.7/json/decoder.py", line 364, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib/python2.7/json/decoder.py", line 382, in raw_decode
    raise ValueError("No JSON object could be decoded")
ValueError: No JSON object could be decoded
```

```python
Traceback (most recent call last):
  File "/usr/local/bin/cloudplow", line 60, in <module>
    conf.load()
  File "/opt/cloudplow/utils/config.py", line 227, in load
    cfg, upgraded = self.upgrade_settings(json.load(fp))
  File "/usr/lib/python3.5/json/__init__.py", line 268, in load
    parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
  File "/usr/lib/python3.5/json/__init__.py", line 319, in loads
    return _default_decoder.decode(s)
  File "/usr/lib/python3.5/json/decoder.py", line 339, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib/python3.5/json/decoder.py", line 355, in raw_decode
    obj, end = self.scan_once(s, idx)
json.decoder.JSONDecodeError: Expecting ',' delimiter: line 46 column 13 (char 1354)
```


Fixes:

1. Paste the JSON file at https://jsonformatter.curiousconcept.com/ and click `process`. This will tell you what the issue is and fix it for you.

   or

2. Run:

   ```
   jq '.' config.json
   ```

   If there are no issues, it will simply print out the full JSON file.


   If there is an issue, a msg will display the location of the issue:

   ```
   parse error: Expected separator between values at line 7, column 10
   ```

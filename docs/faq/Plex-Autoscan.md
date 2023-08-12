# Plex Autoscan

IT IS QUITE PROBABLE THAT SOME INFORMATION HERE IS OUTDATED

[PLEASE OPEN ISSUES](https://github.com/saltyorg/docs/issues)

## Newly downloaded media from Sonarr and Radarr are not being added to Plex?

- Test another download and run the following command:

  ```shell
   tail -f /opt/plex_autoscan/plex_autoscan.log
  ```

- If you see this...

   ```text
   terminate called after throwing an instance of 'boost::filesystem::filesystem_error'
   boost::filesystem::create_directories: Permission denied: "/config/Library/Logs"
   ```

  There is an issue with the permissions on that folder that you'll need to fix manually (Saltbox can't fix this as Plex creates this folder after the first scan)

   To fix this, Run the following command. Replace `user` and `group` to match yours (see [here](System.md#find-your-user-id-uid-and-group-id-gid)).

   ```shell
   docker stop plex
   sudo chown -R user:group /opt/plex
   docker start plex
   ```

   Example of a successful scan:

   ```text
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

## Plex Autoscan log shows error during empty trash request

```text
ERROR - PLEX [10490]: Unexpected response status_code for empty trash request: 401
```

You need to generate another token and re-add that back into the config.

## Plex Autoscan error with metadata item id

Example Log:

```text
 2017-11-21 04:26:32,619 -    ERROR -      PLEX [ 7089]: Exception finding metadata_item_id for '/data/TV/Gotham/Season 01/Gotham - S01E01 - Pilot.mkv':
 2017-11-21 04:26:32,619 -     INFO -      PLEX [ 7089]: Aborting analyze of '/data/TV/Gotham/Season 01/Gotham - S01E01 - Pilot.mkv' because could not find a metadata_item_id for it
```

Possible Issues:

- One of the mounts has changed (e.g. Rclone_VFS or MergerFS was restarted).

- Permission issues (see [here]).

Solution 1:

1. Make sure the remote mount is working OK (pick the relevant one below).

   The current default used for mounting cloud storage is Rclone VFS:

   ```shell
   sudo systemctl status rclone_vfs
   ```

2. Make sure the union mount is working OK.

   The current default used for creating the union mount is MergerFS:

   ```shell
   sudo systemctl status mergerfs
   ```

3. Restart Plex:

   ```shell
   docker stop plex && docker start plex
   ```

Solution 2:

If all else fails, disable analyze in config.

1. Open `/opt/plex_autoscan/config/config.json`

   ```shell
   nano /opt/plex_autoscan/config/config.json
   ```

1. Make the following edit:

   ```json
   "PLEX_ANALYZE_TYPE": "off",
   ```

1. Restart Plex Autoscan

   ```shell
   sudo systemctl restart plex_autoscan
   ```

## Purpose of a Control File in Plex Autoscan

Every time Sonarr or Radarr downloads a new file, or upgrades a previous one, a request is sent to Plex via Plex Autoscan to scan the movie folder or TV season path and look for changes. Since Sonarr and Radarr delete previous files on upgrades, the scan will cause the new media to show up in your Plex Library, however, the deleted files would be missing, and instead, marked as "unavailable" (i.e. trash icon). When the control file is present and the option in the Plex Autoscan config is enabled (default), Plex Autoscan will empty the trash for you, thereby, removing the deleted media from the library.

If the remote mount for you cloud storage provider (e.g. Google Drive) ever disconnected during a Plex scan of your media, Plex would mark the missing files as unavailable and emptying the trash would cause them to be removed out of the library. To avoid this from happening, Plex Autoscan checks for a control file in the unionfs path (i.e. `/mnt/unionfs/mounted.bin)` before running any empty trash commands. The control file is just a blank file that resides on the root folder of your Rclone remote (i.e. cloud storage provider) and let's Plex Autoscan know that it is still mounted.

Once the remote is remounted, all the files marked unavailable in Plex will be playable again and Plex Autoscan will resume its emptying trash duties post-scan.

To learn more about Plex Autoscan, visit <https://github.com/l3uddz/plex_autoscan>.

**TLDR: Plex Autoscan will not remove deleted media out of Plex without it.**

## Plex Autoscan Localhost Setup

If you are using an all-in-one Saltbox and don't want to have the Plex Autoscan port open, you may set it up so that it runs on the localhost only.

To do so, follow these steps:

 Option 1

**Plex Autoscan:** (only if changed from default)

1. Open `/opt/plex_autoscan/config/config.json`

   ```shell
   nano /opt/plex_autoscan/config/config.json
   ```

2. Make the following edit:

   ```json
   "SERVER_IP": "0.0.0.0",
   ```

   _Note: This is the default config._

3. Restart Plex Autoscan

   ```shell
   sudo systemctl restart plex_autoscan
   ```

**Sonarr/Radarr:**

- Retrieve the 'Docker Gateway IP Address' by running the following:

  ```shell
  docker inspect -f '{{ .NetworkSettings.Networks.saltbox.Gateway }}' sonarr
  ```

- Replace the Plex Autoscan URL with:

  `http://docker_gateway_ip_address:3468/yourserverpass`

- You Plex Autoscan URL will now look like this:

  `http://172.18.0.1:3468/yourserverpass`

 Option 2

Alternatively, you can set it up this way:

_Note: This method benefits from completely closing off Plex Autoscan to the outside._

**Plex Autoscan:**

1. Retrieve the 'Docker Gateway IP Address' by running the following:

   ```shell
   docker inspect -f '{{ .NetworkSettings.Networks.saltbox.Gateway }}' sonarr
   ```

2. Open `/opt/plex_autoscan/config/config.json`

   ```shell
   nano /opt/plex_autoscan/config/config.json
   ```

3. Make the following edit:

   ```json
   "SERVER_IP": "docker_network_gateway_ip_address",
   ```

4. This will now look like this:

   ```json
   "SERVER_IP": "172.18.0.1",
   ```

5. Restart Plex Autoscan

   ```shell
   sudo systemctl restart plex_autoscan
   ```

**Sonarr/Radarr:**

- Replace the Plex Autoscan URL with:

  `http://docker_gateway_ip_address:3468/yourserverpass`

- You Plex Autoscan URL will now look like this:

  `http://172.18.0.1:3468/yourserverpass`

## Why is SERVER_SCAN_DELAY set to 180 seconds by default?

When Plex Autoscan gets a scan request from Sonarr, it tells Plex to scan the relevant TV Show season folder. So to avoid multiple Plex scans of the same season when more episodes of that same season come in, Plex Autoscan can wait (ala SERVER_SCAN_DELAY) and merge multiple scan requests into a single one. This is particularly noticeable when consecutive episodes are being downloaded/imported into Sonarr.

During this SERVER_SCAN_DELAY, if another request comes in for the same season folder, it will restart the delay timer again, thus allowing for even more time for new items to come in.

SERVER_SCAN_DELAY of 180 seconds was calculated with an average episode download time of a few minutes each.

There is no harm in multiple Plex scans of the same season folder, except for more busyness of Plex, and perhaps more stress to it, so this delay will try to alleviate that.

Alternative recommended settings are: 120 and 90 seconds.

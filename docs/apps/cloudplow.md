<!-- TOC depthFrom:1 depthTo:2 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Intro](#intro)
  - [Remote Uploader Function](#remote-uploader-function)
  - [UnionFS Cleaner Function](#unionfs-cleaner-function)
- [Config](#config)
  - [Default config.json file](#default-configjson-file)
  - [Location](#location)
  - [Editing](#editing)
  - [Modify Upload Threshold and Interval](#modify-upload-threshold-and-interval)
  - [Plex Integration](#plex-integration)
  - [Pushover Notifications](#pushover-notifications)
  - [Restart](#restart)
- [CLI](#cli)
  - [Manual Clean](#manual-clean)
  - [Manual Upload](#manual-upload)


<!-- /TOC -->


# Intro

[Cloudplow](https://github.com/l3uddz/cloudplow) (CP) is a script created by [l3uddz](https://github.com/l3uddz) that has two main components (as related to Cloudbox): 

  1. Uploader to Rclone remote: Files are moved off local storage. With support for multiple uploaders (i.e. remote/folder pairings).

  2. UnionFS Cleaner functionality: Deletion of UnionFS-Fuse whiteout files (`*_HIDDEN~`) and their corresponding "whited-out" files on Rclone remotes. With support for multiple remotes (useful if you have multiple Rclone remotes mounted).

## Remote Uploader Function

As setup for Cloudbox, Cloudplow uploads all the content in `/mnt/local/Media/` (see [[Paths|Basics: Cloudbox Paths#clouplow]]) to your cloud storage provider (e.g. Google Drive), after the folder reaches a `200` GB size threshold, when checked every `30` minutes.

_Note: The size threshold and the check interval can be changed via steps mentioned on this page._


<details>
<summary>Google Drive Daily Upload Limit (click to expand)</summary><br />

Recently, Google Drive has a max upload limit of about 750GB per day. When this limit is reached, Google Drive will put you in a 24 hour soft ban. When Cloudplow detects this (with the phrase `Failed to copy: googleapi: Error 403: User rate limit exceeded`), uploading will be suspended for 25 hours (i.e. a 25 hour ban sleep), and upon waking up, it will resume its checking and uploading tasks. This feature is enabled by default. This method is better than running Rclone task with a bwlimit, becasuse you can just upload in bursts when the uploading resumes.

_Note: The keywords or phrases that are used to monitor the ban, and the duration of the sleep time, can be changed at any time by editing the `config.json` file._

</details>



## UnionFS Cleaner Function

On top of uploading your media files to the cloud storage, Cloudplow also functions as a UnionFS whiteout cleaner (i.e. `*_HIDDEN~` files).

<details>
<summary>What are <code>*_HIDDEN~</code> files? (click to expand)</summary><br />

When Sonarr & Radarr upgrade your media files, they attempt delete the previous ones. When that data is still on the local server, it is deleted immediately, but when it has been moved to the cloud storage provider, for example Google Drive, it is unable to do so because the Google Drive mount is set as read-only (via Plexdrive or Rclone VFS). 

Instead, UnionFS will create a whiteout file (a blank file in the format of `filename.ext_HIDDEN~`), at `/mnt/local/.unionfs-fuse/` and that will make the file invisible to whatever tries to access it via the UnionFS mount (.e.g. `/mnt/unionfs/`) and, therefore, Sonarr & Radarr will consider the file deleted, however, the media file will still exist on the cloud. 

To resolve this, on the next upload task (i.e. when size threshold is reached on the next interval check), Cloudplow will scan for the whiteout file(s), remove the corresponding media file from the cloud storage, then remove the whiteout file (since it isn't needed anymore), and as a result, keep your content free of duplicates. 
</details>







# Config

## Default config.json file

See [[Config: Cloudplow]].


## Location

```
/opt/cloudplow/config.json
```

Note: Config changes require a restart: `sudo systemctl restart cloudplow`.

## Editing

Edit in your favorite code editor  (with json highlighting) or even a unix editor like nano. 

```
nano /opt/cloudplow/config.json
```

Note: The cloudplow config file is a JSON file.  JSON files have a particular format and syntax.  If you are unfamiliar with JSON formatting and syntax, don't edit this file until you have gained that familiarity.  Here's a [random YouTube video](https://www.youtube.com/watch?v=GpOO5iKzOmY) that will give you a ten-minute overview.

## Modify Upload Threshold and Interval

```json
    "uploader": {
        "google": {
            "check_interval": 30,
            "exclude_open_files": false,
            "max_size_gb": 200,
            "opened_excludes": [
                "/downloads/"
            ],
            "size_excludes": [
                "downloads/*"
            ]
        }
```


`"check_interval":` How often (in minutes) Cloudplow checks the size of `/mnt/local/Media`.

`"max_size_gb":` Max size (in GB) Cloudplow allows `/mnt/local/Media` to get before starting an upload task.

  - Note: `max_size_gb` is rounded up, so it is advised to have it minimum `2GB` or else it would attempt upload at each interval. Explanation below. 

    - `1GB` is basically anything in there.

    - `2GB` is at least 1GB of data.





## Plex Integration 

Cloudplow can throttle Rclone uploads during active, playing Plex streams (paused streams are ignored).

```json
  "plex": {
      "enabled": false,
      "url": "https://plex.domain.com",
      "token": "",
      "poll_interval": 60,
      "max_streams_before_throttle": 1,
      "rclone": {
          "throttle_speeds": {
              "0": "1000M",
              "1": "50M",
              "2": "40M",
              "3": "30M",
              "4": "20M",
              "5": "10M"
          },
          "url": "http://localhost:7949"
      }
  }
```

`enabled` - Change `false` to `true` to enable.

`url` - Your Plex URL.

`token` - Your [[Plex Access Token]].

`poll_interval` - How often (in seconds) Plex is checked for active streams.

`max_streams_before_throttle` - How many playing streams are allowed before enabling throttling.

`rclone`

  - `url` - Leave as default.

  - `throttle_speeds` - Categorized option to configure upload speeds for various stream counts (where `5` represents 5 or more streams). `M` is MB/s.

     - Format: 
    
       ```json
       "STREAM COUNT": "THROTTLED UPLOAD SPEED",
       ```

## Pushover Notifications

See [[here|Pushover#cloudplow]].


## Restart

Restart Cloudplow to apply the changes to the config. 

```
sudo systemctl restart cloudplow
```


# CLI


You can run a manual Cloudplow task from anywhere by just using the `cloudplow` command. 

## Manual Clean

To clean the hidden files and remove deleted files from the cloud:

```
cloudplow clean
```

## Manual Upload

To start uploading right away, regardless of what the folder size is: 

```
cloudplow upload
```
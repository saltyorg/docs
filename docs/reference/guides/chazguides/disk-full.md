# Why is my disk full?

First, a quick refresher on how the system works:

Your downloader puts files in `/mnt/local/downloads`.
Sonarr/Radarr move [usenet] or copy [default torrent] these files to `/mnt/local/Media`.
[They’re actually moving files to `/mnt/unionfs/Media`, but the mergerfs config routes them in `/mnt/local/Media`]
Once `/mnt/local/Media` hits 200GB, cloudplow uploads the contents to your cloud drive.
Once that’s complete they will show up in `/mnt/remote/Media` as well as `/mnt/unionfs/Media`.
Chances are, if your disk is full, the cause is one of two things:

1. Sonarr/Radarr are not importing downloaded media
1. Cloudplow isn't uploading things to the cloud.

If you are using rclone’s --vfs-cache=full, then there’s a third likely cause:

1. Your rclone vfs cache is filling your disk

This is written assuming Usenet downloads, so filling your disks with seeding torrents isn't covered.  You can use these tools to find out if that's the issue, though.

## Where is the space going?

The first step is to find out where the space is going on your disk; which directories contain all the files.

At a command prompt, type:

```shell
sudo ncdu -x --exclude /opt/plex /
```

What’s that command?

```shell
sudo                 - run with root privileges
ncdu                 - show graphic display of disk usage
-x                   - don’t cross filesystem boundaries [this will show only local space used and won't cross over to remote file systems like your cloud storage]
--exclude /opt/plex  - ignore this directory; it’s full of thousands of tiny files that take forever to scan and MOST LIKELY you’re not going to want to delete anything from here.
/                    - starting point of scan
```

You'll probably see something like this:

```text
ncdu 1.12 ~ Use the arrow keys to navigate, press ? for help
--- / ------------------------------------------------------
  558.0 GiB [##########] /mnt
   20.9 GiB [          ] /var
    3.5 GiB [          ] /usr
```

Drill into /mnt/local:

```text
ncdu 1.12 ~ Use the arrow keys to navigate, press ? for help
--- /mnt/local ---------------------------------------------
                         /..
  472.9 GiB [##########] /downloads
   43.9 GiB [          ] /Media
   37.5 GiB [          ] /Backups
    3.7 GiB [          ] /transcodes
```

Here, I have 473 GB of unimported downloads and 44 GB waiting to be uploaded by Cloudplow.

Rclone vfs cache is more install-dependent.  I’m going to assume that if you’re reading this you didn’t change things from the defaults, and chances are you’ll see something like this:

```text
ncdu 1.12 ~ Use the arrow keys to navigate, press ? for help ------------------------------------------------------------
  252.3 GiB [##########] /home
  119.6 GiB [####      ] /mnt
   29.5 GiB [#         ] /var
    3.4 GiB [          ] /usr
```

Drill into /home/YOUR_USERNAME/:

```text
ncdu 1.12 ~ Use the arrow keys to navigate, press ? for help
--- /home/seed ---------------------------------------------
                         /..
  203.0 GiB [##########] /.cache
   37.9 MiB [          ] /.pkg-cache
   34.5 MiB [          ] /.npm
```

And further into .cache/rclone:

```text
ncdu 1.12 ~ Use the arrow keys to navigate, press ? for help
--- /home/seed/.cache/rclone -------------------------------
                         /..
  202.9 GiB [##########] /vfs
    4.8 MiB [          ] /vfsMeta
   16.0 KiB [          ] /webgui
```

That’s your VFS cache.

## Radarr/Sonarr didn’t import stuff

Drill into downloads to examine what's there in more detail.  Chances are you’ll find /mnt/local/nzbs/nzbget/downloads/completed is where all the files are.  Those are downloads that Radarr/Sonarr didn’t import.

Use Wanted -> Manual Import to find out why particular things weren't imported.

![](../images/../../../images/low-disk/01-low-disk-manual.png)

Perhaps Radarr couldn’t work out what movie a thing was:

![](../images/../../../images/low-disk/02-low-disk-unknown.png)

Maybe it doesn’t look like an upgrade for one reason or another:

![](../images/../../../images/low-disk/03-low-disk-not-upgrade.png)

![](../images/../../../images/low-disk/04-low-disk-filesize.png)

That same information is also available in the logs.

You can import things from here after telling Radarr what movie it is or the like, or you can delete them from within ncdu or via whatever other means.

## Cloudplow isn’t uploading stuff

If the bulk of the space is in staged-for-upload files sitting in `/mnt/local/Media`, then cloudplow hasn’t uploaded those files yet.

This is typically due to one of the following:

- Upload threshold hasn’t been reached.
- You’ve reached the Google Drive upload cap of 750GB/day

The default threshold to start a Google upload is 200GB, so in my case above cloudplow wouldn’t do anything until 150GB more gets put into `/mnt/local/Media`.

At a command prompt, type:

```shell
tail /opt/cloudplow/cloudplow.log
```

You should see something like:

```text
Uploader: google. Local folder size is currently 44 GB. Still have 156 GB remaining before its eligible to begin uploading...
```

If you do, cloudplow is working as expected.  If you want cloudplow to start uploading stuff sooner, you can adjust those thresholds in your cloudplow config file.  At the bottom of `/opt/cloudplow/config.json`, you’ll find something like this:

```json
"google": {
    "check_interval": 30,
    "exclude_open_files": true,
    "max_size_gb": 200,
    "opened_excludes": [
        "/downloads/"
    ],
    "service_account_path": "",
    "size_excludes": [
        "downloads/*"
    ]
}
```

That’s going to check every 30 minutes, and start uploading when the folder reaches 200GB.  Adjust those values to suit your use case. Restart the cloudplow service if you make changes here.

In the default setup, you can upload 750GB per day.

To see if you’ve hit that quota, run a cloudplow upload manually.  At a command prompt, type:

```shell
cloudplow upload
```

This will kick off an upload without regard for the threshold.  You can run this anytime you want to upload whatever’s pending right this very minute.

PAY ATTENTION TO WHAT THE LOG SAYS.  The errors should let you know what’s going on.

If you want more detail:

```shell
cloudplow upload --loglevel=DEBUG
```

You'll get a great deal of information about what cloudplow is doing and why.

If you find yourself hitting that 750GB cap regularly, you may want to set up [service-account uploading](tip44.md).

## Rclone cache is out of control

If the bulk of the space is in your rclone VFS cache, you’ll want to check the vfs_cache configuration for all your mounts to control this.

Perhaps you used a copy-pasted config that is setting the max cache to 200G or so, and applied that to four mounts.  That means your rclone cache might grow to 800GB, so adjust the configs on the mounts you're caching.

Don’t just delete the existing cached files.  You’ll need to stop the mounts first before you adjust the cache sizes.

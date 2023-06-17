# Migrating from Google to [your remote STFP box here]

## Example Setup

### Mediabox: AX51

- standard mediabox sb install

### Storage: Hetzner Server Auction Server

- raidz2 configuration
- Files stored at `/mnt/local/Media`

## Setup New Rclone remote

Pretty self explanitory. I am using SFTP for my remote. Leave the name as whatever else for now.

```bash
[temp-storage]
type = sftp
host = [your ip or domain name]
key_file = ~/.ssh/id_[your-key-name]
use_insecure_cipher = false
user = [your username here]
pass =
known_hosts_file = ~/.ssh/known_hosts
md5sum_command = md5sum
sha1sum_command = sha1sum
concurrency = 2048
chunk_size = 252k
```

Some notes on this config:
This assumes you're SSH'ing to your box with `ssh [name-of-server]` setup in `~/.ssh/config`.
Read [here](https://forum.rclone.org/t/increasing-sftp-transfer-speed/29928/5) on speeding up SFTP transfers. tl;dr I boosted my concurrency because I have ram for days on both systems and packet/chunk size from what I read is capped at 256k so 252k keeps it just low enough to fit any overhead.

## Move all your files from Google to your new box

This is what I ran and never ran into any data cap/tfs limits/errors: `rclone sync google:/Media /mnt/local/Media -vP --bwlimit 100M --tpslimit 12 --fast-list --drive-stop-on-download-limit`. This took a few days running 24/7.

Then once that is done, do one last `cloudplow upload` to make sure everything is on Drive and then run the rclone command above once more to make sure your storage box and Drive have the same files.

## Update the rclone_vfs.service

Take a backup first, just in case.
`sudo cp /etc/systemd/system/rclone_vfs.service /etc/systemd/system/rclone_vfs.service.BACKUP`

Edit the service:
`sudo vi /etc/systemd/system/rclone_vfs.service`

```bash
#########################################################################

[Unit]
Description=Rclone VFS Mount
After=network-online.target

[Service]
User=[**your user**]
Group=[**your group**]
Type=notify
ExecStart=/usr/bin/rclone mount \
  --user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36' \
  --config=/home/[**your user**]/.config/rclone/rclone.conf \
  --allow-other \
  --allow-non-empty \
  --dir-cache-time=1m \
  --max-read-ahead=200M \
  --rc \
  --rc-no-auth \
  --rc-addr=localhost:5572 \
  --use-mmap \
  --vfs-read-ahead=128M \
  --vfs-read-chunk-size=32M \
"/etc/systemd/system/rclone_vfs.service" [readonly] 50L, 1660B                                                                              26,1          26%
  --rc-no-auth \
  --rc-addr=localhost:5572 \
  --use-mmap \
  --vfs-read-ahead=128M \
  --vfs-read-chunk-size=32M \
  --vfs-read-chunk-size-limit=2G \
  --vfs-cache-max-age=504h \
  --vfs-cache-mode=full \
  --vfs-cache-poll-interval=30s \
  --vfs-cache-max-size=2T \
  --timeout=10m \
  --umask=002 \
  --syslog \
  -v \
  google:/mnt/local /mnt/remote
ExecStartPost=/usr/bin/rclone rc vfs/refresh recursive=true --url http://localhost:5572 _async=true
ExecStop=/bin/fusermount -uz /mnt/remote
Restart=on-abort
RestartSec=5
StartLimitInterval=60s
StartLimitBurst=3

[Install]
WantedBy=default.target
```

I removed any Drive specific flags and switched this line:
`google: /mnt/remote`
to
`google:/mnt/local /mnt/remote`. I plan on just leaving "Google" as my remote name so I don't have to mess much with Cloudplow. Change `google:` to whatever you wish.

My setup allows for a larger vfs cache. Double check your values before copying blindly!

## Edit RClone config

Now go back into `~/.config/rclone/rclone.config`. I commented out my Drive setup just in case. Rename `temp-storage` to `google`.

## Edit Cloudplow config

`vi /opt/cloudplow/config.json`
I had to change these lines:

```bash
"sync_remote": "google:/mnt/local/Media",
"upload_folder": "/mnt/local/Media",
"upload_remote": "google:/mnt/local/Media"
```

I ran `cloudplow config-update`. No idea what this does.

## Final Steps

Run `sudo systemctl daemon-reload` to refresh the daemons.

Run `sudo service rclone_vfs restart`. This should switch your Drive mount to your new storage box mount.

That's it! Jump into Plex and play something to test. I noticed a small increase in latency vs Drive but other than that things seem to be running well. I also downloaded another file and tested Cloudplow as well with `cloudplow upload` which seemed to also work.

## Closing Thoughts

You could probably use the Hetzner NFS thing but I don't understand enough of what's going on to use that and the documentation is currently very sparse.

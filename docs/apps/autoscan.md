# Autoscan

## What is it?

[Autoscan](https://github.com/Cloudbox/autoscan){: target=_blank rel="noopener noreferrer" } replaces the default Plex, Emby, and Jellyfin behaviour for picking up file changes on the file system. Autoscan integrates with Sonarr, Radarr, Lidarr and Google Shared Drives to fetch changes in near real-time without relying on the file system.

Autoscan is a rewrite of the original Plex Autoscan written in the Go language. In addition, this rewrite introduces a more modular approach and should be easy to extend in the future.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/Cloudbox/autoscan){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/Cloudbox/autoscan){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/Cloudbox/autoscan){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/cloudb0x/autoscan){: .header-icons target=_blank rel="noopener noreferrer" } |

## Setup

The Saltbox Autoscan role will attempt to partially configure your autoscan config file located at `/opt/autoscan/config.yml`. You should refer to the documentation and adjust this file as suits your own needs. The config generated is very minimal. [a-train](https://github.com/m-rots/a-train/pkgs/container/a-train){: target=_blank rel="noopener noreferrer" } is now replacing the bernard trigger.

The generated config file will look something like this:

```yaml
# <- processor ->

# Override the minimum age before a scan request is sent to the target (Default 10m):
minimum-age: 10m

# Override the delay between processed scans (Default 5s):
scan-delay: 5s

# Set anchor files for remote storage. If these are missing no scans will be sent to the target to avoid files being trashed when a mount fails
anchors:
  - /mnt/unionfs/mounted.bin

# <- triggers ->

# Optionally, protect your webhooks with authentication
authentication:
  username: USERNAME_FROM_SETTINGS
  password: PASSWORD_FROM_SETTINGS

# Port for Autoscan webhooks to listen on
port: 3030

triggers:
  a-train:
      priority: 5
      rewrite: # Global rewrites
        - from: ^/Media/
          to: /mnt/unionfs/Media/


  inotify:
    - priority: 0

      # Filter with regular expressions
      include:
        - ^/mnt/unionfs/Media/
      exclude:
        - '\.(srt|pdf)$'

      # rewrite inotify path to unified filesystem
      rewrite:
        - from: ^/mnt/local/Media/
          to: /mnt/unionfs/Media/

      # Local filesystem paths to monitor
      paths:
        - path: /mnt/local/Media

  sonarr:
    - name: sonarr # /triggers/sonarr
      priority: 2

  radarr:
    - name: radarr # /triggers/radarr
      priority: 2

  lidarr:
    - name: lidarr # /triggers/lidarr
      priority: 1

# <- targets ->

targets:
  plex:
    - url: https://plex.DOMAIN.TLD # plex
      token: YOUR_PLEX_TOKEN
```

Then edit the anchors section:
```yaml
anchors:
  - /mnt/unionfs/mounted.bin
```
To reflect your own configuration.
Example:
```yaml
anchors:
  - /mnt/unionfs/bvoiwepopz-movies_mounted.bin
  - /mnt/unionfs/bvoiwepopz-tv_mounted.bin
```
Everything else should be ready to go for standard usage.

### A-Train

Autoscan can monitor Google Drive changes via a trigger called "Bernard".  The code behind Bernard can sometimes get out of sync with the state of Google Drive and miss things, so now we are using A-Train.
"A-Train" is a rewrite of the Bernard concepts, and is currently available as a second docker image as part of Sandbox.  It will likely be integrated into autoscan.

Enter the names of the remotes you want to monitor in the [sandbox settings.yml](https://docs.saltbox.dev/sandbox/settings/). The Remotes can be either drive remotes or union remotes. You may use ```rclone listremotes``` to get your drive remotes.

Example:
```yaml
a_train:
  remotes: ["bvoiwepopz-Movies", "bvoiwepopz-TV"]
```
or
```yaml
a_train:
  remotes: ["google"]
```

Run the a-train tag to create the container:

```
sb install sandbox-a_train
```

Copy one of your service account files from its current location to `/opt/a-train/account.json`.  Remember to rename your service account file to "`account.json`".

Example:
```
cp /opt/sa/all/160.json /opt/a-train/account.json
```

Run the autoscan tag to rebuild the container:

```
sb install autoscan
```

Run the a-train tag to rebuild the container:

```
sb install sandbox-a_train
```

###Bernard

If for some reason you still wanted to use Bernard, it would look like this:

```yaml
triggers:
  bernard:
    - account: /config/sa.json # Path inside the container where your SA is located
      cron: "*/5 * * * *" # every five minutes (the "" are important)
      priority: 0
      drives:
        - id: drive_id #Friendly title
      # Rewrite gdrive to the local filesystem
      rewrite:
        - from: ^/Media/
          to: /mnt/unionfs/Media/
      # Filter with regular expressions
      include:
        - ^/mnt/unionfs/Media/
      exclude:
        - '\.srt$'
```

Further documentation:

- [A-Train Docker page](https://github.com/users/m-rots/packages/container/package/a-train)

- [A-Train initial documentation](https://gist.github.com/m-rots/f345fd2cfc44585266b620feb9fbd612)

- [:octicons-link-16: Documentation](https://github.com/Cloudbox/autoscan){: .header-icons target=_blank rel="noopener noreferrer" }

## Next

Are you setting Saltbox up for the first time?  Continue to [Sonarr](../sonarr/).

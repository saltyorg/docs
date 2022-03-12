# Autoscan

## What is it?

[Autoscan](https://github.com/Cloudbox/autoscan){: target=_blank rel="noopener noreferrer" } replaces the default Plex, Emby, and Jellyfin behaviour for picking up file changes on the file system. Autoscan integrates with Sonarr, Radarr, Lidarr and Google Share Drives to fetch changes in near real-time without relying on the file system.

Autoscan is a rewrite of the original Plex Autoscan written in the Go language. In addition, this rewrite introduces a more modular approach and should be easy to extend in the future.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home ](https://github.com/Cloudbox/autoscan){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/Cloudbox/autoscan){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github:](https://github.com/Cloudbox/autoscan){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker ](https://hub.docker.com/r/cloudb0x/autoscan){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install autoscan

```

### 2. Setup

The Saltbox Community Autoscan role will attempt to partially configure your autoscan config file located at `/opt/autoscan/config.yml`. You should refer to the documentation and adjust this file as suits your own needs. The config generated is very minimal. If you wish to monitor sharedrive activity you should probably consider using [a-train](https://github.com/m-rots/a-train/pkgs/container/a-train){: target=_blank rel="noopener noreferrer" } rather than soon to be shelved bernard trigger.

### 3. A-Train

Autoscan can monitor Google Drive changes via a trigger called "Bernard".  The code behind Bernard can sometimes get out of sync with the satate of Google Drive and miss things.  

"A-Train" is a rewrite of the Bernard concepts, and is currently available as a second docker image.  At some point it may be integrated into autoscan.

To run A-Train in place of Bernard:

Create an a-train config file:

```
mkdir /opt/a-train
nano  /opt/a-train/a-train.toml
```

Insert the following into `atrain.toml`:

```
# a-train.toml
[autoscan]
# Replace the URL with your Autoscan URL.
url = "http://autoscan:3030"
# If you have set a username and password
# on autoscan enter them here
username = "user"
password = "password"

[drive]
# Path to the Service Account key file,
account = "/data/NAME_OF_SERVICE_FILE.json"
# One or more Shared Drive IDs
# These are IDs, not names
drives = ["driveid1", "driveid2"]
```

Of course, you need to change the details noted in the comments.

This example is assuming you copy one of your service account files from its current location to `/opt/a-train/NAME_OF_SERVICE_FILE.json`.  Chances are you want to use some name other than "`NAME_OF_SERVICE_FILE.json`".

Edit your Autoscan config file: `/opt/autoscan/config.yml`; replace the `bernard` trigger section with the following:

```
  a-train:
      priority: 5
      rewrite: # Global rewrites
        - from: ^/Media/
          to: /mnt/unionfs/Media/
```

Run the autoscan tag to rebuild the container with the new image:

```
sb install autoscan
```

Create and run the a-train container:

```
docker run -d \
    --name a-train \
    --restart unless-stopped \
    -e PUID=1000 \
    -e PGID=1001 \
    -v /opt/a-train:/data \
    --label com.github.saltbox.saltbox_managed=true \
    --network=saltbox \
    --network-alias=a-train \
    ghcr.io/m-rots/a-train
```

Further documentation:

[A-Train Docker page](https://github.com/users/m-rots/packages/container/package/a-train)

[A-Train initial documentation](https://gist.github.com/m-rots/f345fd2cfc44585266b620feb9fbd612)

[Updated Autoscan documentation](https://github.com/Cloudbox/autoscan/tree/bernard-rs#a-train)


- [:octicons-link-16: Documentation](https://github.com/Cloudbox/autoscan){: .header-icons target=_blank rel="noopener noreferrer" }

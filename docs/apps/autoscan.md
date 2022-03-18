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

Enter the names of the remotes you want to monitor in the [sandbox settings.yml](https://docs.saltbox.dev/sandbox/settings/){: target=_blank rel="noopener noreferrer" }. The Remotes can be either drive remotes or union remotes.

```
a_train:
  remotes: ["remote1", "remote2"]
```

This is assuming you copy one of your service account files from its current location to `/opt/a_train/account.json`.  Remember to rename your service account file to "`account.json`".

Edit your Autoscan config file: `/opt/autoscan/config.yml`; replace the `bernard` trigger section with the following:

```
  a-train:
      priority: 5
      rewrite: # Global rewrites
        - from: ^/Media/
          to: /mnt/unionfs/Media/
```

Run the autoscan tag to rebuild the container:

```
sb install autoscan
```

Run the a-train tag to create the container:

```
sb install sandbox-a_train
```

Further documentation:

[A-Train Docker page](https://github.com/users/m-rots/packages/container/package/a-train)

[A-Train initial documentation](https://gist.github.com/m-rots/f345fd2cfc44585266b620feb9fbd612)

- [:octicons-link-16: Documentation](https://github.com/Cloudbox/autoscan){: .header-icons target=_blank rel="noopener noreferrer" }

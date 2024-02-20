---
hide:
  - tags
tags:
  - feeder
  - feedermount
---

# Feeder Mount

# Intro

For setups with separate Feeder and Media boxes, you will have newly downloaded media that will not be instantly available on cloud storage (e.g. Google Drive) and, therefore, inaccessible to Mediabox (e.g. Plex) when Sonarr/Radarr sends a media scan request.

To remedy this issue, you can use Saltbox's Feeder Mounter to mount your Feederbox's `/mnt/local` path, onto your Mediabox's `/mnt/feeder` location, so that you are able to play those newly downloaded media files even if they haven't been uploaded to the cloud.

_Note: Running the below commands will replace your `unionfs.service` or `mergerfs.service` file. If you have any custom paths in there (e.g. `/mnt/rclone`), make sure you back that up and add them back in once you mount/dismount the Feederbox._

## Mount

The following steps will be done on the Mediabox.

1. In `rclone config`, create an `sftp` remote to your Feederbox called `feeder` (Here is an [asciicast](https://asciinema.org/a/184084?t=0&speed=1&size=medium&cols=75&rows=25) video walking through the process).  The general process of creating an rclone remote is discussed [here](../reference/guides/rclone-remote.md).

      _Note: If you don't already have one, add the `feederbox` [subdomain](../reference/subdomain.md) and point it to your Feederbox's IP address. If you are using Cloudflare, make sure CDN/Proxy is not enabled for this subdomain._

1. Edit the `rclone/remotes` section of `settings.yml`:

    ```yaml
    rclone:
      enabled: yes
      remotes:
        # LEAVE OTHER REMOTES IN PLACE IF ANY
        - remote: feeder
          settings:
            mount: yes
            template: sftp
            union: yes
            upload: no
            upload_from: /mnt/local/Media
            vfs_cache:
              enabled: no
              max_age: 504h
              size: 50G
      version: latest
    ```

1. Run the following command:

      ```yaml
      sb install mounts
      ```

1. Your docker containers will restart and media on Feederbox will be available to them.

      _Note: You do not need to do anything to your apps (eg no need to edit Plex library paths etc)._

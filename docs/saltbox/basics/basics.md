---
extra_stylesheets:
  - stylesheets/basics.css
hide:
  - tags
tags:
  - saltbox
  - basics
  - features
  - how
  - operation
---

# Basics

## What is Saltbox?

- [Saltbox](https://github.com/saltyorg/Saltbox) is an [Ansible](https://www.ansible.com/how-ansible-works) and [Docker](https://www.docker.com/what-container) based solution for rapidly deploying a media server using LTS releases of Ubuntu Server 22.04 or 24.04, running on AMD64. Non-LTS releases of Ubuntu or Desktop installations are not supported. Linux distributions other than Ubuntu are not supported. ARM processors, Raspberry Pi notably, are not supported.

- Primary functions are: the automatic acquisition of media, being able to play it back from anywhere and from any device, and, to a lesser extent, storing that media in a remote storage location.

- NOTE: Saltbox does not have a dashboard or GUI of its own. All Saltbox-specific setup and commands are done on the linux command-line.

## Why use Saltbox?

### Custom Domains

- Have your server set up behind your own domain name, securely (e.g. <https://apps.iYOUR_DOMAIN_NAMEi>).

### Fast Deployment

- Have a system running in minutes with minimal input.

### Docker-Based Applications

- Docker containers keep your apps isolated from each other—no more conflicts between apps.

- Docker containers keep your system tidy since none of the apps' files (executables and dependencies) are stored outside the container.

- Quickly install and uninstall apps.

- Built-in config-driven method to deploy multiple instances of many apps [multiple radarr, sonarr, plex, etc.]

### Remote Storage

- Store media in the cloud such as Google Drive, on a NAS, and more...

### Can Choose Your Preferred Media Server Application

- You can decide whether to use Plex, Emby, or Jellyfin.

### Custom Server Deployment

- You can deploy Saltbox on an all-in-one server, for downloading and streaming, or

- You can deploy Saltbox between two servers: a Mediabox, as streaming server, and a Feederbox, as a downloading server.

### Secure

- Saltbox uses secure HTTPS backed by [Let's Encrypt](https://letsencrypt.org/) or [ZeroSSL](https://zerossl.com/) certificates.

### Single-sign-on

- Saltbox can put all your media apps behind Authelia security rather than relying on individual app logins.

### Easy Backup and Restore

- Configuration and data files for all key applications are conveniently stored in /opt, which makes backup so easy. Easily pack up your server and move to another one with Saltbox's built-in Backup.

## How does Saltbox function?

<div class="sb-flow" markdown>

<p class="sb-flow__lede" markdown="span">From the moment Sonarr or Radarr asks for a release to the moment it sits on remote storage, every app works with a single path: `/mnt/unionfs`.</p>

<figure class="sb-flow__figure" markdown>
<div class="sb-flow__canvas" markdown="span">
![How a file moves through Saltbox](../../images/basics-flow-wide.svg#only-light)
![How a file moves through Saltbox](../../images/basics-flow-wide-dark.svg#only-dark)
</div>
<figcaption markdown="span">A new file is written through `/mnt/unionfs`, lands on `/mnt/local`, and is later moved to remote storage by Cloudplow. Its path under `/mnt/unionfs` stays the same the whole time, so Sonarr, Radarr and the media server never notice the move.</figcaption>
</figure>

### The seven steps

<ol class="sb-flow__steps" markdown>
  <li markdown><span class="sb-flow__badge sb-flow__badge--msg">1</span><p markdown="span">**Grab.** [Sonarr](../../apps/sonarr.md) (TV) or [Radarr](../../apps/radarr.md) (movies) sends a release to [SABnzbd](../../apps/sabnzbd.md) for Usenet or [qBittorrent](../../apps/qbittorrent.md) for torrents.[^1] [^2]</p></li>
  <li markdown><span class="sb-flow__badge sb-flow__badge--file">2</span><p markdown="span">**Download.** The client saves it under `/mnt/unionfs/downloads`. Torrents keep seeding from there, and never leave the server, until you or an automation remove them.</p></li>
  <li markdown><span class="sb-flow__badge sb-flow__badge--file">3</span><p markdown="span">**Import.** Sonarr or Radarr moves the file into `/mnt/unionfs/Media`. Torrent files are hardlinked or copied instead, so the seed stays intact.</p></li>
  <li markdown><span class="sb-flow__badge sb-flow__badge--msg">4</span><p markdown="span">**Notify.** Sonarr or Radarr tells [Autoscan](../../apps/autoscan.md) which folder changed.</p></li>
  <li markdown><span class="sb-flow__badge sb-flow__badge--msg">5</span><p markdown="span">**Scan.** Autoscan waits ten minutes,[^3] then asks the media server to scan only that season or movie folder. New media appears sooner than with a full library scan, and there is less risk of cloud storage API bans.</p></li>
  <li markdown><span class="sb-flow__badge sb-flow__badge--read">6</span><p markdown="span">**Play.** [Plex](../../apps/plex.md), [Emby](../../apps/emby.md), or [Jellyfin](../../apps/jellyfin.md) reads everything through `/mnt/unionfs/Media`, wherever the file physically is.</p></li>
  <li markdown><span class="sb-flow__badge sb-flow__badge--file">7</span><p markdown="span">**Upload.** [Cloudplow](../../apps/cloudplow.md) checks every 30 minutes. Once 200 GB is staged in `/mnt/local`, it moves `Media` to remote storage and frees the local disk.[^4]</p></li>
</ol>

<p class="sb-flow__note" markdown="span">`/mnt/unionfs` is a `mergerfs` union of the server's own disk, `/mnt/local`, and an [Rclone](../../apps/rclone.md) VFS mount of your remote storage under `/mnt/remote`. Existing files stay readable and writable wherever they are, but new files are only ever written to `/mnt/local`. See [Paths](paths.md) for the full folder layout.</p>

</div>

!!! tip "Tuning the defaults"
    The ten-minute scan delay and the 200 GB upload threshold are defaults. Change them in the [Autoscan config](../../apps/autoscan.md#usage) and the [Cloudplow upload settings](../../apps/cloudplow.md#upload-settings).

***

[^1]: Some of the applications above can be replaced with similar apps. Plex/Emby/Jellyfin, for example.

[^2]: If you want to use torrents, it is recommended to be a member of a private tracker as opposed to using public ones. If you want to use Usenet, you will need to purchase Usenet provider service (or multiple services) and also be a member of one or more Usenet indexers.

[^3]: The delay ensures that the file is completely copied into the media directory before the media server scans it, and it allows a season of TV to be collected and sent to the media server as a single scan. Each new episode in a given season resets the timer, so the scan request goes to the media server ten minutes after the last episode finished downloading.

[^4]: **Note:** Due to changes in Google Drive, upload limits are much tighter than they used to be, and the multiple shared drives setup is no longer useful or recommended. ~~There is presently a 750GB/day upload limitation on Google accounts. The standard Saltbox setup will create a set of shared drives and service accounts. The service accounts can be enabled in cloudplow to exceed this limit on uploads (750 GB/day/service account).~~

Next, let's discuss the [Prerequisites](../prerequisites/prerequisites.md) for Saltbox installation.

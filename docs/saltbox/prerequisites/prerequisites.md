## Presumptions

Saltbox presumes you have a basic understanding of Linux, Docker containers, BitTorrent, and Usenet, and are also familiar with Sonarr, Radarr, NZBGet, rTorrent/ruTorrent, and Plex/Emby.

The Saltbox setup is all done on the command line in the linux shell.  There is no GUI and there are no plans to add one.  If you want to run Saltbox, you *will need* to be familiar with Linux.

The guides in this wiki are only meant to setup Saltbox specific settings into the various apps that are installed with Saltbox (e.g. Sonarr, Radarr, Plex, etc) and are not meant to be a full setup for, or an introduction to, the workings of these apps. However, you may pick up a few things as you go thru the guides.

If you wish to learn more about them in detail, you can easily find a ton of guides for them online (e.g. [HTPC Guides](https://www.htpcguides.com){target=_blank}, [YouTube](https://www.youtube.com){target=_blank}, etc).

There are, broadly, 4 prerequisites to installing Saltbox:

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [A Server](#server)
- [A Domain Name](#domain)
- [Cloud Storage](#cloud-storage)
- [A Plex Account](#plex-account)
- [Usenet or Bittorrent sources](#usenet-or-bittorrent-sources)

<!-- /TOC -->

## System Requirements

### Operating Systems

At this time, we only support LTS releases of Ubuntu Server [20.04](https://releases.ubuntu.com/20.04/) and [22.04](https://releases.ubuntu.com/22.04/), freshly installed.

!!! warning
    Desktop editions are excluded. While Saltbox may technically run alongside a desktop environment, we will decline all forms of support around this use case.

### Server

For best results, the assumed server environment for Saltbox is:

- a dedicated remote server [not a VPS],
- a processor compliant with the `x86_64`/`amd64` [`arm` NOT SUPPORTED] architecture,
- from a server provider like Hetzner, OVH, kimsufi, etc.,
- nothing else [docker, for example] preinstalled,
- with at least 500GB of disk space, and
- allowing root access.

See [here](../../reference/server.md) for more information about server requirements.

## Domain

**You will need a domain name** as Saltbox apps are only accessed via <https://appname>.*yourdomain.com* (see [Accessing Apps](../basics/accessing_apps.md)).

Ports are [for the most part] bound only to the internal `saltbox` docker network, which means they are not visible on the host; you **won't be able to connect externally** to the apps using `IP:PORT`.

See [here](../../reference/domain.md) for more information about setting up a domain and DNS settings for use with Saltbox.

## Cloud Storage

A base assumption in Saltbox is that you are storing your media on cloud storage.  Saltbox can be set up to use any cloud storage provider that [Rclone](https://rclone.org/) supports. However, Google Drive via [G-Suite Business](https://gsuite.google.com/pricing.html) is the preferred choice among users.  Some of the components are designed expressly for Google Drive, like the Google Drive monitoring in plex-autoscan and the service-account rotation in cloudplow.

See [here](../../reference/cloud.md) for more information about Cloud Storage requirements and running Saltbox without it.

## Plex Account

You'll need a [Plex account](https://www.plex.tv/sign-up/), if you don't already have one, for purposes of the install, *even if you're not planning to use Plex*.

This may change in the future, but for now it's a requirement for the simplest Happy Path install described here.

See [here](../../reference/plex.md) for more information about Plex account requirements.

## Usenet or Bittorrent sources

If you are planning to set up a standard Saltbox or a feederbox, you will need a source of media; [Usenet, Torrents, or both](https://www.htpcguides.com/comparing-usenet-vs-torrents/)

You won't need these particular [media source] details for the initial install, but you will need them for application setup.

See [here](../../reference/usenet-torrent.md) for more information about media source requirements.

Next, let's discuss Saltbox [Install types](../basics/install_types.md).

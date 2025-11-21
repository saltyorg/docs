---
hide:
  - tags
tags:
  - prerequisites
  - assumptions
  - install
  - hardware
  - os
  - requirements
---

# Initial Assumptions

Saltbox presumes you have a basic understanding of Linux, Docker containers, BitTorrent, and Usenet, and are also familiar with Sonarr, Radarr, NZBGet, qBittorrent, and Plex/Emby.

The Saltbox setup is all done on the command line in the linux shell. There is no GUI and there are no plans to add one. If you want to run Saltbox, you *will need* to be familiar with Linux.

The guides in this wiki are only meant to setup Saltbox specific settings into the various apps that are installed with Saltbox (e.g. Sonarr, Radarr, Plex, etc) and are not meant to be a full setup for, or an introduction to, the workings of these apps. However, you may pick up a few things as you go thru the guides.

If you wish to learn more about them in detail, you can easily find a ton of guides for them online (e.g. [HTPC Guides](https://www.htpcguides.com){target=_blank}, [YouTube](https://www.youtube.com){target=_blank}, etc).

There are, broadly, 4 prerequisites to installing Saltbox:

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [A Server](#server)
- [A Domain Name](#domain)
- [Cloud Storage (optional)](#cloud-storage)
- [A Plex Account (optional)](#plex-account)
- [Usenet or Bittorrent sources](#usenet-or-bittorrent-sources)

<!-- /TOC -->

## System Requirements

### Operating Systems

At this time, we only support LTS releases of Ubuntu Server [22.04](https://releases.ubuntu.com/22.04/), or [24.04](https://releases.ubuntu.com/24.04/), freshly installed.

!!! warning
    Desktop editions are excluded. While Saltbox may technically run alongside a desktop environment, we will decline all forms of support around this use case.

### Server

For best results, the assumed server environment for Saltbox is:

- a dedicated remote server [not a VPS or a virtualized setup like proxmox] [see below for important information about Hetzner],
- with a processor compliant with the `x86_64`/`amd64` [`arm` NOT SUPPORTED] architecture,
- running a brand new fresh install of the server version of Ubuntu 22.04, or 24.04,
- from a server provider like Hetzner, OVH, kimsufi, etc.,
- nothing else [docker, for example] preinstalled,
- with at least 500GB of disk space, and
- allowing root access.

See [here](../../reference/server.md) for more details about server requirements.

When you install Ubuntu on the server, do not preinstall anything other than OpenSSH. Notably, do not install Docker along with the OS.

!!! warning
    IF YOUR SERVER IS HOSTED BY HETZNER, AND YOU WANT TO USE PLEX:

    Plex has blocked access to their servers from Hetzner-hosted boxes. so you will need to configure gluetun to route this traffic to Plex.

    Put "gluetun" in the search box above for details on how to set this up.

#### Networking

The server will need to be accessible from the internet via ports 22 [or whatever port you are using for SSH], 80, and 443; if this is a home server most likely you will need to configure port-forwarding in your router to send these ports to this device.

## Domain

**You will need a domain name** as Saltbox apps are only accessed via <https://appname.iYOUR_DOMAIN_NAMEi> (see [Accessing Apps](../basics/accessing-apps.md)).

Ports are [for the most part] bound only to the internal `saltbox` docker network, which means they are not visible on the host; you **won't be able to connect** to the apps using `IP:PORT`.

If you use Cloudflare for DNS [which is free and doesn't require that you register your domain through Cloudflare], the Saltbox setup can make the required DNS settings for you. If you aren't using Cloudflare, you will have to set this up at your DNS provider yourself. See [here](../../reference/domain.md) for more information about setting up a domain and DNS settings for use with Saltbox.

## Cloud Storage

The default assumption in Saltbox is that you are storing your media on cloud storage. Saltbox can be set up to use any cloud storage provider that [Rclone](https://rclone.org/) supports. Google Drive via [G-Suite Business](https://gsuite.google.com/pricing.html) has historically been the preferred choice among users, but with recent changes to the Google offering [Dropbox](https://www.dropbox.com/) was a primary choice for a while, but they have followed Google's lead in tightening restrictions. Both work well as long as you stay within their restrictions, but the days of storing thousands of media files on cloud storage for pennies are past.

Some of the components are designed expressly for Google Drive, like the A-Train Google Drive monitoring in autoscan and the service-account rotation in cloudplow. Recent Google changes have also rendered service accounts of little value with regard to increasing data transfer volume.

THAT SAID, cloud storage is not a requirement; you can run saltbox without it, storing your media locally in a variety of ways.

See [here](../../reference/cloud.md) for more details about Cloud Storage requirements and running Saltbox without it.

## Plex Account

If you want to use Plex you'll need a [Plex account](https://www.plex.tv/sign-up/), if you don't already have one.

Should you not wish to use Plex on a Mediabox install you should look into overriding the `media_servers_enabled` variable using the [inventory](../inventory/index.md).

See [here](../../reference/plex.md) for more details about Plex account requirements.

## Usenet or Bittorrent sources

If you are planning to set up a standard Saltbox or a feederbox, you will need a source of media; [Usenet, Torrents, or both](https://www.htpcguides.com/comparing-usenet-vs-torrents/)

You won't need these particular [media source] details for the initial install, but you will need them for application setup.

See [here](../../reference/usenet-torrent.md) for more details about media source requirements.

Next, let's discuss Saltbox [Install types](../basics/install-types.md).

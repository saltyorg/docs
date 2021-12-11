# SyncLounge

# **NOT INTEGRATED - MAKE SANDBOX REQUEST IF NEEDED**

## What is it?

[SyncLounge](https://synclounge.tv/){: target=_blank rel="noopener noreferrer" } is a tool to sync Plex content across multiple players in multiple locations.

SyncLounge aims to keep multiple viewing sessions in sync regardless of whether the clients are in the same room or across the globe. To do this SyncLounge utilizes a middle-man server to communicate between each of the SyncLounge clients. Users choose their Plex client, decide on a SyncLounge Server and Room name and join up. Your friends/family can do the same. Whoever joins the room first will become the host.

The host has complete control over a room. Commands they send to their client will be sent through to other people in the room (Play, Pause, Seek etc). If the host starts playing something different, SyncLounge will search all of your available Plex Media Servers for an equiavalent copy, even if it is not from the same Plex Media Server as the Host.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home ](https://synclounge.tv/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://docs.synclounge.tv/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github:](https://github.com/synclounge/synclounge){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker ](https://hub.docker.com/r/starbix/synclounge){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install cm-synclounge

```

### 2. URL

- To access SyncLounge, visit `https://synclounge._yourdomain.com_`

### 3. Setup

- Please note that synclounge works directly out of the box without further configurations. SyncLounge does support server autojoin however that feature is currently broken upstream and does not work.

- Visit `https://synclounge._yourdomain.com_` and log in to your plex account on the screen. On the server selection screen you will be presented with 4 options (AU, EU, US and Custom) Select Custom and enter the following address `https://synclounge._yourdomain.com_/slserver`

- [:octicons-link-16: Documentation](https://docs.synclounge.tv/){: .header-icons target=_blank rel="noopener noreferrer" }

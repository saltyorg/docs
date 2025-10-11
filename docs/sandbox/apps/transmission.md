---
hide:
  - tags
tags:
  - transmission
  - download
  - torrent
---

# Transmission

## What is it?

[Transmission](https://transmissionbt.com/) is a fast, easy, and free BitTorrent client.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://transmissionbt.com/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/transmission/transmission/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/transmission/transmission){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/transmission){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-transmission

```

### 2. URL

- To access Transmission, visit `https://transmission._yourdomain.com_`

### 3. Setup

- Suggested desktop client is [Transmission Remote GUI](https://github.com/transmission-remote-gui/transgui). It is to be set up with ssl enabled on port 443

- `/watch` is hard-coded in the software and not editable from the settings.json, see related issue. To get around this the folder is mounted to `/mnt/local/downloads/torrents/transmission{{ rolename }}/watch`

- Do not change the published ports if you want to be connectable.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

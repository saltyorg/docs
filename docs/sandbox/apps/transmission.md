# Transmission

## What is it?

[Transmission](https://transmissionbt.com/){: target=_blank rel="noopener noreferrer" } is a fast, easy, and free BitTorrent client.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home ](https://transmissionbt.com/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/transmission/transmission/wiki){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github:](https://github.com/transmission/transmission){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker ](https://hub.docker.com/r/linuxserver/transmission){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-transmission

```

### 2. URL

- To access Transmission, visit `https://transmission._yourdomain.com_`

### 3. Setup

- Suggested desktop client is [Transmission Remote GUI](https://github.com/transmission-remote-gui/transgui){: target=_blank rel="noopener noreferrer" }. It is to be set up with ssl enabled on port 443

- `/watch` is hard-coded in the software and not editable from the settings.json, see related issue. To get around this the folder is mounted to `/mnt/local/downloads/torrents/transmission{{ rolename }}/watch`

- Do not change the published ports if you want to be connectable.

- [:octicons-link-16: Documentation](https://github.com/transmission/transmission/wiki){: .header-icons target=_blank rel="noopener noreferrer" }

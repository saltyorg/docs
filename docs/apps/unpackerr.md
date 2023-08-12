# Unpackerr

## What is it?

[Unpackerr](https://github.com/davidnewhall/unpackerr){: target=_blank rel="noopener noreferrer" } checks for completed downloads and extracts them so Lidarr, Radarr, Readarr, Sonarr may import them. There are a handful of options out there for extracting and deleting files after your client downloads them.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/davidnewhall/unpackerr){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/davidnewhall/unpackerr/wiki){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/davidnewhall/unpackerr/){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/hotio/unpackerr){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install unpackerr

```

### 2. Setup

- [:octicons-link-16: Documentation](https://github.com/davidnewhall/unpackerr){: .header-icons target=_blank rel="noopener noreferrer" }

The important part of the setup is the setup for the applications.  You'll need to change these three settings for each:

```text
[[sonarr]]
  url = "http://sonarr:8989"
  api_key = "YOUR_API_KEY"
# File system path where downloaded Sonarr items are located.
  paths = ['/mnt/unionfs/downloads/torrents/qbittorrent/completed']
```

The `path` will depend on the torrent client you are using and its configuration.

Same setup is required for radarr, lidarr, and readarr if you are using them.

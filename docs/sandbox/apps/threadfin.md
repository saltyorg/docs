# Threadfin

## What is it?

[Threadfin](https://github.com/Threadfin/Threadfin){: target=_blank rel="noopener noreferrer" } is a M3U proxy server for Plex, Emby and any client and provider which supports the .TS and .M3U8 (HLS) streaming formats.

Threadfin emulates a SiliconDust HDHomeRun OTA tuner, which allows it to expose IPTV style channels to software, which would not normally support it. It is based on xTeve.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/Threadfin/Threadfin){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/Threadfin/Threadfin){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/Threadfin/Threadfin){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/fyb3roptik/threadfin){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-threadfin

```

### 2. URL

- To access Threadfin, visit `https://threadfin._yourdomain.com_/web`

### 3. Setup

- Access xTeVe web GUI, visit `https://threadfin._yourdomain.com_/web`

- Run through the Configuration Wizard.

- Use the following URLs when configuring your media server (e.g. Plex, Emby, Jellyfin)

  - HDHomerun Device Address (Plex) `http://threadfin:34400`

  - Playlist (Emby, Jellyfin) `http://threadfin:34400/m3u/threadfin.m3u`

  - EPG (all) `http://threadfin:34400/xmltv/threadfin.xml`

- [:octicons-link-16: Documentation](https://github.com/Threadfin/Threadfin){: .header-icons target=_blank rel="noopener noreferrer" }

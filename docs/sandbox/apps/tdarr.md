---
hide:
  - tags
tags:
  - tdarr
  - media
  - encoding
---

# Tdarr

## What is it?

[Tdarr](https://tdarr.io/) is a cross-platform conditional based transcoding application for automating media library transcode/remux management in order to process your media files as required. For example, you can set rules for the required codecs, containers, languages etc that your media should have which helps keeps things organized and can increase compatability with your devices. A common use for Tdarr is to simply convert video files from h264 to h265 (hevc), saving 40%-50% in size.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://tdarr.io/){: .header-icons } | [:octicons-link-16: Docs](https://docs.tdarr.io/docs/welcome/what/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/HaveAGitGat/Tdarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/haveagitgat/tdarr){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-tdarr

```

### 2. URL

- To access Tdarr, visit `https://tdarr._yourdomain.com_`

### 3. Setup

Tdarr is configured with the following defaults which can be modified via the inventory system.

``` yaml
tdarr_server_port: "8266"
tdarr_server_external: false
```

By switching `tdarr_server_external` to `true` the Tdarr server will be accessible externally via the specified `tdarr_server_port` on any hostname or IP address pointing directly to the server.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
hide:
  - tags
tags:
  - ytdl-sub
  - youtube
  - downloads
---

# ytdl-sub

## What is it?

[ytdl-sub](https://github.com/jmbannon/ytdl-sub) is a lightweight tool to automate downloading and metadata generation with yt-dlp. It uses YAML files to define subscriptions and prepares media for popular media players like Plex, Jellyfin, Kodi, and Emby.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |
|-------------|-------------|-------------|
| [:octicons-mark-github-16: Github](https://github.com/jmbannon/ytdl-sub){: .header-icons } | [:octicons-link-16: Docs](https://ytdl-sub.readthedocs.io/){: .header-icons } | [:material-docker: Docker](https://github.com/jmbannon/ytdl-sub/pkgs/container/ytdl-sub){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-ytdl-sub
```

### 2. URL

- To access ytdl-sub, visit `https://ytdl-sub._yourdomain.com_`

### 3. Setup

The role supports two image types configurable via inventory:

- **GUI Mode** (`ytdl_sub_image_type: "gui"`): Web-based VS Code interface for full management
- **Headless Mode** (`ytdl_sub_image_type: "headless"`): Command-line focused, lightweight deployment (default)

Configure your subscriptions using YAML files in the config directory.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
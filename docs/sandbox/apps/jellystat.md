---
hide:
  - tags
tags:
  - jellystat
  - jellyfin
  - statistics
---

# Jellystat

## What is it?

[Jellystat](https://github.com/CyferShepard/Jellystat) is a free and open source statistics web application for Jellyfin that provides a dashboard with information about the server, libraries, users, and playback activity. Still in development with some expected functionality gaps.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |
|-------------|-------------|-------------|
| [:octicons-mark-github-16: Github](https://github.com/CyferShepard/Jellystat){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/cyfershepard/jellystat){: .header-icons } | [:octicons-law-16: MIT](https://github.com/CyferShepard/Jellystat/blob/main/LICENSE){: .header-icons } |

### 1. Installation

``` shell
sb install sandbox-jellystat
```

### 2. URL

- To access Jellystat, visit `https://jellystat._yourdomain.com_`
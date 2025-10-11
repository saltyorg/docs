---
hide:
  - tags
tags:
  - plex_utills
  - plex
  - utilities
  - management
---

# Plex Utills

## What is it?

[Plex Utills](https://github.com/jkirkcaldy/plex-utills) is a web-based utility collection for managing and maintaining your Plex Media Server. It provides various tools and helpers for common Plex administration tasks.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/jkirkcaldy/plex-utills){: .header-icons } | [:octicons-link-16: Docs](https://github.com/jkirkcaldy/plex-utills#readme){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/jkirkcaldy/plex-utills){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jkirkcaldy/plex-utills){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-plex_utills

```

### 2. URL

- To access Plex Utills, visit `https://plex-utills._yourdomain.com_`

### 3. Setup

- Configuration files are stored in `/opt/plex-utills`
- Application logs are stored in `/opt/plex-utills/logs`
- The `/mnt` directory is mounted at `/films` for media access
- The web interface runs on port 80 internally

!!! tip
    Configure the application through the web interface after your first login.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

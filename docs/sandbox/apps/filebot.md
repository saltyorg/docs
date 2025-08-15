---
hide:
  - tags
tags:
  - filebot
  - media
  - tools
---

# FileBot

## What is it?

[FileBot](http://www.filebot.net/) is the ultimate tool for organizing and renaming your movies, tv shows or anime, and music well as downloading subtitles and artwork. It's smart and just works.

This is a Docker container for FileBot.

The GUI of the application is accessed through a modern web browser (no installation or configuration needed on the client side) or via any VNC client.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](http://www.filebot.net/){: .header-icons } | [:octicons-link-16: Docs](https://www.filebot.net/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/jlesage/docker-filebot){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jlesage/filebot){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-filebot

```

### 2. URL

- To access FileBot, visit `https://filebot._yourdomain.com_`

### 3. Setup

- The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

- [:octicons-link-16: Documentation: Filebot Docs](https://www.filebot.net/){: .header-icons }

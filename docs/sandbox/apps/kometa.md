---
hide:
  - tags
tags:
  - kometa
  - pmm
  - plex meta manager
---

# Kometa

## What is it?

[Kometa](https://github.com/Kometa-Team/Kometa) can update many metadata fields for movies, shows, collections, seasons, and episodes and can act as a backup if your plex DB goes down. It can even update metadata the plex UI can't like Season Names. If the time is put into the metadata configuration file you can have a way to recreate your library and all its metadata changes with the click of a button.

!!! info
    Kometa is the replacement for Plex Meta Manager. A simple migration for your appdata is available by running `sb install sandbox-pmm-kometa-migration`.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/Kometa-Team/Kometa){: .header-icons } | [:octicons-link-16: Docs](https://kometa.wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Kometa-Team/Kometa){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/kometateam/kometa){: .header-icons }|

### 1. Installation

You will need to create a config file prior to running the tag:

`/opt/kometa/config.yml`

There is a Docker-based walkthrough on the Kometa wiki [here](https://kometa.wiki/en/latest/kometa/install/docker/) that you can use to learn how to create this file.  Once you've created it, move the file into `/opt/kometa/` and then run the tag.

``` shell

sb install sandbox-kometa

```

### 2. Setup

- [:octicons-link-16: Documentation: Kometa Docs](https://kometa.wiki){: .header-icons }

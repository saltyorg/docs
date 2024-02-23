# Plex Meta Manager

## What is it?

[Plex Meta Manager](https://github.com/meisnate12/Plex-Meta-Manager) can update many metadata fields for movies, shows, collections, seasons, and episodes and can act as a backup if your plex DB goes down. It can even update metadata the plex UI can't like Season Names. If the time is put into the metadata configuration file you can have a way to recreate your library and all its metadata changes with the click of a button.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/meisnate12/Plex-Meta-Manager){: .header-icons } | [:octicons-link-16: Docs](https://github.com/meisnate12/Plex-Meta-Manager/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/meisnate12/Plex-Meta-Manager){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/meisnate12/plex-meta-manager){: .header-icons }|

### 1. Installation

You will need to create a config file prior to running the tag:

`/opt/plex-meta-manager/config.yml`

There is a Docker-based walkthrough on the PMM wiki [here](https://github.com/meisnate12/Plex-Meta-Manager/wiki/Walkthrough-Docker) that you can use to learn how to create this file.  Once you've created it, move the file into `/opt/plex-meta-manager/` and then run the tag.

``` shell

sb install sandbox-plex-meta-manager

```

### 2. Setup

- [:octicons-link-16: Documentation: Plex Meta Manager Docs](https://github.com/meisnate12/Plex-Meta-Manager/wiki){: .header-icons }

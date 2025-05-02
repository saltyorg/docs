---
hide:
  - tags
tags:
  - profilarr
  - sonarr
  - radarr
  - recyclarr
---

Configuration management and auto-import tool for Radarr/Sonarr custom formats and profiles.

<div class="grid sb-buttons" markdown data-search-exclude>

[:material-home: Homepage&nbsp;&nbsp;](https://dictionarry.dev/#home-content-profilarr){ .md-button .md-button--stretch }

[:material-bookshelf: Manual&nbsp;&nbsp;](https://dictionarry.dev/wiki/profilarr-setup){ .md-button .md-button--stretch }

[:fontawesome-brands-docker: Releases&nbsp;&nbsp;](https://hub.docker.com/r/santiagosayshey/profilarr/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord: Community&nbsp;&nbsp;](https://discord.gg/ZeN6ggCHBN){ .md-button .md-button--stretch }

</div>

---

!!! warning "Beta software / Modifies PVR configuration"
    Although core features are expected to work, this application is in early stages of development. It's recommended to back up your Radarr and Sonarr databases before running import or sync operations.

## Deployment

```shell
sb install sandbox-profilarr
```

## Usage

Visit `https://profilarr._yourdomain.com_`.
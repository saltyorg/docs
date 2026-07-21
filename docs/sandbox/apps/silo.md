---
icon: material/docker
hide:
  - tags
tags:
  - silo
  - media
  - streaming
  - transcoding
saltbox_automation:
  app_links:
    - name: Manual
      url: https://siloserver.org/docs
      type: documentation
    - name: Releases
      url: https://github.com/Silo-Server/silo-server/pkgs/container/silo-server
      type: github
    - name: Community
      url: https://discord.gg/4RxuUQAEnW
      type: discord
  project_description:
    name: Silo
    summary: |-
      a self-hosted media server for movies, shows, music, and books with direct play, transcoding, and optional Jellyfin-compatible client support.
    link: https://siloserver.org
    categories:
      - Content Delivery Apps > Media Server
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-silo
```

## Usage

Visit <https://silo.iYOUR_DOMAIN_NAMEi>.

Configure libraries against the usual `/mnt/unionfs/...` paths in the admin UI.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

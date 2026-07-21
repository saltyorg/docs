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
      url: https://github.com/Silo-Server/silo-server/tree/main/docs
      type: documentation
    - name: Releases
      url: https://github.com/Silo-Server/silo-server/pkgs/container/silo-server
      type: docker
    - name: Community
      url: https://discord.gg/4RxuUQAEnW
      type: community
  project_description:
    name: Silo
    summary: |-
      a self-hosted media server for movies, shows, music, and books with direct play, transcoding, and optional Jellyfin-compatible client support.
    link: https://github.com/Silo-Server/silo-server
    categories:
      - Content Delivery Apps > Media Server
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
# Silo
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-silo
```

The role also deploys PostgreSQL with pgvector and Redis.

## Usage

Visit <https://silo.iYOUR_DOMAIN_NAMEi>.

Configure libraries against the usual `/mnt/unionfs/...` paths in the admin UI.

Transient transcodes use the configured Saltbox transcodes path and are
mounted at `/tmp/silo-transcode`. Hardware transcoding uses Saltbox's standard
Intel or NVIDIA device configuration.

## Compatible Clients

Silo's Jellyfin-compatible API is disabled by default and listens on a
separate port when enabled. The Sandbox role currently exposes only Silo's
main web service through Traefik.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

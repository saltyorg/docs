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
      purpose: manual
    - name: Releases
      url: https://github.com/Silo-Server/silo-server/pkgs/container/silo-server
      type: github
      purpose: release
    - name: Community
      url: https://discord.gg/4RxuUQAEnW
      type: discord
      purpose: community
  project_description:
    name: Silo
    summary: |-
      a self-hosted media server for movies, shows, music, and books with direct play, transcoding, and optional Jellyfin-compatible client support.
    link: https://siloserver.org
    categories:
      - Content Delivery Apps > Media Server
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Silo

## Overview

[Silo](https://siloserver.org) is a self-hosted media server for movies, shows, music, and books with direct play, transcoding, and optional Jellyfin-compatible client support.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://siloserver.org/docs){ .md-button .md-button--stretch }

[:fontawesome-brands-github:**Releases**](https://github.com/Silo-Server/silo-server/pkgs/container/silo-server){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://discord.gg/4RxuUQAEnW){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-silo
```

### Migrating from the multi-container role

Earlier versions of this role ran PostgreSQL and Redis in separate `silo-postgres` and `silo-redis` containers. The role now deploys Silo's single-container image, which bundles both and keeps its data in `/opt/silo/config`.

`sb install sandbox-silo` refuses to run on an install that still uses the old layout. Migrate it once with:

```shell
sb install sandbox-silo-migrate
```

This stops Silo and its database, copies the PostgreSQL cluster into `/opt/silo/config` using Silo's own migration script, links the `plugins`, `artwork` and `compat` folders, deploys Silo and compares the number of users, media items and watch history entries with the old database. The `silo-postgres` and `silo-redis` containers are removed once this succeeds.

The old `postgres`, `redis`, `plugins`, `artwork` and `compat` folders in `/opt/silo` are left untouched. Delete them once Silo works.

## Usage

Visit <https://silo.iYOUR_DOMAIN_NAMEi>.

Configure libraries against the usual `/mnt/unionfs/...` paths in the admin UI.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

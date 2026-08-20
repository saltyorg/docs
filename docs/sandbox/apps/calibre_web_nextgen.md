---
icon: material/docker
title: Calibre-Web-NextGen
hide:
  - tags
tags:
  - calibre
  - calibre-web-nextgen
  - ebooks
  - reading
saltbox_automation:
  app_links:
    - name: Manual
      url: https://github.com/new-usemame/Calibre-Web-NextGen/wiki
      type: documentation
    - name: Releases
      url: https://github.com/new-usemame/Calibre-Web-NextGen/pkgs/container/calibre-web-nextgen
      type: docker
    - name: Community
      url: https://discord.gg/B8NXZmcp32
      type: discord
  project_description:
    name: Calibre-Web-NextGen
    summary: |-
      a community-maintained continuation of Calibre-Web-Automated, adding automatic format conversion, EPUB repair, metadata enrichment and folder-based ingest on top of Calibre-Web.
    link: https://calibrewebnextgen.com
    categories:
      - Content Delivery Apps > Reader
---

# Calibre-Web-NextGen

## Overview

[Calibre-Web-NextGen](https://calibrewebnextgen.com) is a community-maintained continuation of Calibre-Web-Automated, adding automatic format conversion, EPUB repair, metadata enrichment and folder-based ingest on top of Calibre-Web.

## Pre-deployment

The library location is managed by the role and defaults to `/mnt/unionfs/Media/Books`. To use a different subdirectory, set `calibre_web_nextgen_role_media_subfolder`, detailed in the Settings tab below.

The ingest ("drop zone") location is also managed by the role and defaults to `/mnt/unionfs/downloads/ingest` (based on your [downloads root](../../reference/accounts.md#__tabbed_2_2)), so other apps can drop files there for import. To rename the subdirectory, set `calibre_web_nextgen_role_ingest_subfolder`.

!!! warning "Cloudplow users: exclude the database sidecar files"

    Calibre-Web-NextGen keeps its library database, `metadata.db`, inside the library folder alongside the books, and writes to it in place. The first time it opens that database read/write, SQLite creates `metadata.db-wal` and `metadata.db-shm` next to it.

    Cloudplow's default `rclone_excludes` cover `*.db`, so `metadata.db` itself stays local, but they do not match the `-wal`, `-shm` and `-journal` suffixes. If your library sits in a folder cloudplow uploads from, its periodic sweep moves those sidecar files to the remote and deletes the local copies. rclone cannot serve the in-place partial writes SQLite needs, so every subsequent write to the library then fails with `disk I/O error`.

    Add the sidecar patterns to the relevant remote's `rclone_excludes` in [`/opt/cloudplow/config.json`](../../reference/cloudplow-config.md):

    ```json
    "rclone_excludes": [
        "**partial~",
        "**_HIDDEN~",
        "*.db",
        "*.db-wal",
        "*.db-shm",
        "*.db-journal"
    ],
    ```

    Then restart cloudplow:

    ```shell
    sudo systemctl restart cloudplow
    ```

    If the failure has already happened, stop the container, delete the stranded sidecar files from the remote, and start it again — the database is intact and the sidecars are rebuilt on the next open.

## Deployment

```shell
sb install sandbox-calibre-web-nextgen
```

## Usage

Visit <https://calibre-web-nextgen.iYOUR_DOMAIN_NAMEi>.

-   Default admin login:

    ```yaml
    Username: admin
    Password: admin123
    ```

    Change the default login details immediately.

-   Point the app at an existing Calibre library, or let it create one, at `/calibre-library` inside the container. That path is the library location described above.

-   Drop ebook files into the ingest folder to have them converted, repaired, metadata-matched and imported automatically. Files are removed from the ingest folder once imported.

!!! info "SSO and device sync"

    SSO is enabled on the web interface. The OPDS, Kobo and KOReader sync endpoints (`/opds`, `/kobo`, `/kobo_auth`, `/api/v3`, `/api/UserStorage`, `/kosync`) are served by a separate Traefik router that skips SSO, because those clients cannot complete an interactive login. They still authenticate to the app itself, using HTTP basic auth or a per-user sync token.

    If you enable anonymous browsing in the app's admin settings, the OPDS feed stops requiring credentials. Leave anonymous browsing off if the feed should stay private.

Useful docker commands

  ```shell title="Shell access whilst the container is running:"
  docker exec -it calibre-web-nextgen /bin/bash
  ```

  ```shell title="To monitor the logs of the container in realtime:"
  docker logs -f calibre-web-nextgen
  ```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

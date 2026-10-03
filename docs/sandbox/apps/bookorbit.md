---
icon: material/docker
hide:
  - tags
tags:
  - bookorbit
  - ebooks
  - audiobooks
  - reading
saltbox_automation:
  app_links:
    - name: Manual
      url: https://bookorbit.app/installation
      type: documentation
      purpose: manual
    - name: Releases
      url: https://github.com/bookorbit/bookorbit/pkgs/container/bookorbit
      type: github
      purpose: release
    - name: Community
      url: https://github.com/bookorbit/bookorbit/discussions
      type: github
      purpose: community
  project_description:
    name: BookOrbit
    summary: |-
      a self-hosted, multi-user reading platform for ebooks, PDFs, comics, and audiobooks with metadata management, Kobo and KOReader sync, and OPDS support.
    link: https://bookorbit.app
    categories:
      - Content Delivery Apps > Reader
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Pre-deployment

The role creates the initial administrator account from your Saltbox `user` credentials. BookOrbit requires the password to be at least 8 characters long and contain an uppercase letter, a lowercase letter, and a digit. If your Saltbox password does not meet these rules, set `bookorbit_role_admin_password` in the inventory before deploying.

## Deployment

```shell
sb install sandbox-bookorbit
```

## Usage

Visit <https://bookorbit.iYOUR_DOMAIN_NAMEi>.

-   Log in with your Saltbox username and password (or the `bookorbit_role_admin_*` overrides).
-   Create a library and point it at a folder under `/mnt/unionfs/Media`, for example `/mnt/unionfs/Media/Books`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
icon: material/docker
hide:
  - tags
tags:
  - booklore
  - ebooks
  - grimmory
  - reading
saltbox_automation:
  app_links:
    - name: Manual
      url: https://grimmory.org/docs/getting-started
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/grimmory/grimmory/tags
      type: docker
    - name: Community
      url: https://discord.gg/FwqHeFWk
      type: discord
  project_description:
    name: Booklore
    summary: |-
      a self-hosted application designed to manage your entire book collection in one place.
    link: https://grimmory.org
    categories:
      - Content Delivery Apps > Reader
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

???+ warning "Migration notice for Booklore users"

    1. Remove the existing container and rename the existing directory.

        ```shell
        docker rm -f booklore
        mv /opt/booklore /opt/grimmory
        ```

    1.  [Deploy Grimmory :material-arrow-down-bold:](#deployment)

## Configuration

The [Bookdrop](https://grimmory.org/docs/bookdrop) location is managed by the role and defaults to `/mnt/unionfs/downloads/bookdrop` (based on your [downloads root](../../reference/accounts.md#__tabbed_2_2)), where other apps have access to place downloads in.

To rename the subdirectory, you can use `grimmory_role_bookdrop_subfolder`, detailed in the Settings tab below.

## Deployment

```shell
sb install sandbox-grimmory
```

## Usage

Visit <https://grimmory.iYOUR_DOMAIN_NAMEi>.

-   On your first visit you must create an admin user account.

-   After logging back in with the admin user account, create your first library.

-   Create a directory for your book files (e.g. `/mnt/unionfs/Media/Books`) or use an existing directory.

    Select that path when creating your library.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
icon: material/docker
status: draft
hide:
  - tags
tags:
  - jellyseerr
  - overseerr
  - requests
  - seerr
saltbox_automation:
  app_links:
    - name: Manual
      url: https://docs.seerr.dev/category/using-seerr
      type: documentation
    - name: Releases
      url: https://github.com/hotio/seerr/pkgs/container/seerr
      type: github
    - name: Community
      url: https://discord.gg/seerr
      type: discord
  project_description:
    name: Overseerr
    summary: |-
      a request management and media discovery tool built to work with your existing Plex/Jellyseerr ecosystem.
    link: https://seerr.dev
    categories:
      - Content Delivery Apps > Media Server Accessory > Request
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

!!! abstract cta "Saltbox Setup Process"

    <div data-search-exclude>

    <div>

    Opting out of Plex Media Server / Jellyfin?  
    Opting for another requests manager?

    <div>

    [**Explore alternatives**:material-shuffle-variant:](index.md#request){ .md-button }

    [**Skip to Portainer**:material-fast-forward:](portainer.md){ .md-button }

    </div>

    </div>

    </div>

???+ warning "Migration notice for Overseerr and Jellyseerr users"

    Overseerr/Jellyseerr data must be present in Seerr's directory for its backend to perform automatic migration.

    1. Remove the existing container and rename the existing directory.

        === "Overseerr"

            ```shell
            docker rm -f overseerr
            mv /opt/overseerr /opt/seerr
            ```

        === "Jellyseerr"

            ```shell
            docker rm -f jellyseerr
            mv /opt/jellyseerr /opt/seerr
            ```

    1.  [Deploy Seerr :material-arrow-down-bold:](#deployment)

## Deployment

```shell
sb install seerr
```

## Usage

Visit <https://seerr.iYOUR_DOMAIN_NAMEi>.

First-time setup will be similar to [Overseerr](overseerr.md)'s, so you can refer to that as a loose guide.

## Next

<div class="sb-cta" markdown>

Are you setting Saltbox up for the first time?

<div markdown>

[**Continue to Portainer**:material-forward:](portainer.md){ .md-button }

</div>

</div>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

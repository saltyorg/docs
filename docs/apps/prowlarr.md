# Prowlarr

## What is it?

[Prowlarr](https://prowlarr.com/){: target=_blank rel="noopener noreferrer" } is an indexer manager/proxy built on the popular arr .net/reactjs base stack to integrate with your various PVR apps. Prowlarr supports management of both Torrent Trackers and Usenet Indexers. It integrates seamlessly with Lidarr, Mylar3, Radarr, Readarr, and Sonarr offering complete management of your indexers with no per app Indexer setup required (we do it all).

!!!info
    You need to set up sonarr/radarr before using prowlarr.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://prowlarr.com/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://wiki.servarr.com/prowlarr){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/Prowlarr/Prowlarr/){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/hotio/prowlarr){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install prowlarr

```

### 2. URL

- To access Prowlarr, visit `https://prowlarr._yourdomain.com_`

### 3. Setup

***Adding Indexers to Sonarr/Radarr via Prowlarr***

#### Under **Settings >> Apps**

1. Click the big `+` sign to add an App.
2. Provide a "Name", ie Sonarranime if you have multiple instances.
3. Provide the url for Prowlarr, this should be `http://prowlarr:9696`
4. Provide the url for Sonarr/Radarr, ie `http://sonarr:8989`
5. Click "Add Indexer" to add your favorite indexers (i.e. [torrent trackers](../reference/usenet-torrent.md)).

6. When adding indexers into [Sonarr](../apps/sonarr.md#jackett)/[Radarr](../apps/radarr.md#jackett), you will need:

    1. Indexer's Torznab Feed

         - Copy this by clicking on "Copy Torznab Feed" button next to the Indexer.

         - You will need to replace...

           - `https` with `http`

           - `jackett.yourdomain.com` with `jackett:9117`

- [:octicons-link-16: Documentation](https://wiki.servarr.com/prowlarr){: .header-icons target=_blank rel="noopener noreferrer" }

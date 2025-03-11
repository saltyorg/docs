# Jellyseerr

## What is it?

[Jellyseerr](https://docs.jellyseerr.dev/) is a free and open source software application for managing requests for your media library. It integrates with the media server of your choice: Jellyfin, Plex, and Emby. In addition, it integrates with your existing services, such as Sonarr, Radarr.

- Full Jellyfin/Emby/Plex integration including authentication with user import & management.
- Support for PostgreSQL and SQLite databases.
- Supports Movies, Shows and Mixed Libraries.
- Ability to change email addresses for SMTP purposes.
- Easy integration with your existing services. Currently, Jellyseerr supports Sonarr and Radarr. More to come!
- Jellyfin/Emby/Plex library scan, to keep track of the titles which are already available.
- Customizable request system, which allows users to request individual seasons or movies in a friendly, easy-to-use interface.
- Simple request management UI. Don't dig through the app to simply approve recent requests!
- Granular permission system.
- Support for various notification agents.
- Mobile-friendly design, for when you need to approve requests on the go!
- Support for watchlisting & blacklisting media.

!!!info
    By default, the role is **NOT** protected behind your Authelia/SSO middleware. You will have to log in with Plex, Jellyfin, etc. Make the appropriate changes via inventory to add SSO.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://docs.jellyseerr.dev/){: .header-icons } | [:octicons-link-16: Docs](https://docs.jellyseerr.dev/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/ajnart/Jellyseer){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/fallenbagel/jellyseerr){: .header-icons }|

Recommended install types: Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-jellyseerr

```

### 2. URL

- To access Jellyseerr, visit `https://jellyseerr._yourdomain.com_`

- [:octicons-link-16: Documentation: Jellyseerr Docs](https://docs.jellyseerr.dev/){: .header-icons }

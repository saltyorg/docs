# Homepage

## What is it?

[Homepage](https://github.com/benphelps/homepage) is a modern (fully static, fast), secure (fully proxied), customizable application dashboard with integrations for more than 25 services and translations for over 15 languages. Easily configured via YAML files (or discovery via docker labels).

### Features

- Fast! The entire site is statically generated at build time, so you can expect instant load times
- Full i18n support with automatic language detection
  - Translations for Catalan, Chinese, Dutch, Finnish, French, German, Hebrew, Hungarian, Malay, Norwegian Bokmål, Polish, Portuguese, Portuguese (Brazil), Romanian, Russian, Spanish, Swedish and Yue
- Docker integration
  - Container status (Running / Stopped) & statistics (CPU, Memory, Network)
  - Automatic service discovery (via labels)
- Service integration
  - Sonarr, Radarr, Readarr, Prowlarr, Bazarr, Lidarr, Emby, Jellyfin, Tautulli, Plex and more

!!!info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://gethomepage.dev/){: .header-icons } | [:octicons-link-16: Docs](https://gethomepage.dev/latest/configs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/benphelps/homepage){: .header-icons }|

Recommended install types: Saltbox, Core, Mediabox

### 1. Installation

``` shell

sb install sandbox-homepage

```

### 2. URL

- To access Homepage, visit `https://homepage._yourdomain.com_`

### 3. Setup

This role will add both the homepage container, and the homepage-docker-socket-proxy container. To add services and bookmarks etc. you edit your config files found at `/opt/homepage/config/`. There are several example services and widgets included in the role, just uncomment and fill them in appropriately. The webui will reload and it will be visible shortly after. No need to restart the container.

- [:octicons-link-16: Documentation: Homepage Docs](https://gethomepage.dev/latest/configs/){: .header-icons }

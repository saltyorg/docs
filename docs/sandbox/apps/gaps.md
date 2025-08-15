---
hide:
  - tags
tags:
  - gaps
  - media
  - plex
---

# Gaps

## What is it?

[Gaps](https://github.com/JasonHHouse/gaps) searches through your Plex Server for all movies, then queries for known movies in the same collection. If those movies don't exist in your library, Gaps will recommend getting those movies, legally of course.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will NOT have to log into the app itself, as basic Auth is disabled by default.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/JasonHHouse/gaps){: .header-icons } | [:octicons-link-16: Docs](https://github.com/JasonHHouse/gaps#-usage-){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/JasonHHouse/gaps){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/housewrecker/gaps){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-gaps

```

### 2. URL

- To access gaps, visit `https://gaps._yourdomain.com_`

### 3. Setup

- All you need to get started is a [Plex Auth Token](../../reference/plex_auth_token.md?h=plex+token#saltbox-role), and a TMDB api key.

- [:octicons-link-16: Documentation: Gaps Docs](https://github.com/JasonHHouse/gaps#-usage-){: .header-icons }

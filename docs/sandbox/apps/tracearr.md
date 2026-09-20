---
icon: material/docker
hide:
  - tags
tags:
  - tracearr
  - monitoring
  - statistics
saltbox_automation:
  app_links:
    - name: Manual
      url: https://docs.tracearr.com
      type: documentation
      purpose: manual
    - name: Releases
      url: https://github.com/connorgallopo/Tracearr/pkgs/container/tracearr
      type: github
      purpose: release
    - name: Community
      url: https://discord.gg/a7n3sFd2Yw
      type: discord
      purpose: community
  project_description:
    name: Tracearr
    summary: |-
      a monitoring platform for Plex, Jellyfin, and Emby that tracks active streams, playback history, and account sharing.
    link: https://tracearr.com
    categories:
      - Accessories > For Media Server > Monitoring
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Pre-deployment

For SSO through Authelia or Authentik, create an OIDC client with the redirect URI `https://tracearr.iYOUR_DOMAIN_NAMEi/api/v1/auth/oauth2/callback/oidc` and set `tracearr_role_oidc_issuer_url`, `tracearr_role_oidc_client_id` and `tracearr_role_oidc_client_secret`.

## Deployment

```shell
sb install sandbox-tracearr
```

```shell
sb install sandbox-tracearr-claim # (1)!
```

1. Prints the saved Tracearr claim code and its web URL so you can enter the code and complete Tracearr’s initial setup. Does not install Tracearr itself.

## Usage

Visit <https://tracearr.iYOUR_DOMAIN_NAMEi>.

The first account created becomes the owner. Add media servers by their container address, for example `http://plex:32400` or `http://jellyfin:8096`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

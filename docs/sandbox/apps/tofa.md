---
icon: material/docker
hide:
  - tags
tags:
  - tofa
  - media
  - streaming
  - transcoding
saltbox_automation:
  app_links:
    - name: Manual
      url: https://docs.tofa.tv
      type: documentation
    - name: Releases
      url: https://github.com/orgs/tofatv/packages/container/package/tofa
      type: releases
    - name: Community
      url: https://tofa.tv/discord
      type: discord
  project_description:
    name: tofa
    summary: |-
      a self-hosted media server for streaming your own movie and TV library to web, mobile, and TV apps, with hardware-accelerated transcoding.
    link: https://tofa.tv
    categories:
      - Content Delivery Apps > Media Server
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-tofa
```

## Usage

Visit <https://tofa.iYOUR_DOMAIN_NAMEi>.

The server is claimed once, on first run, which links it to your tofa account. Because the Saltbox install is reached through a public domain, that first claim has to carry the setup token the server generates on boot:

```shell
sudo cat /opt/tofa/identity/setup_key.secret
```

Then open `https://tofa.iYOUR_DOMAIN_NAMEi/setup?setup_token=<token>` and follow the wizard. The token is only consulted while the server is unclaimed.

Add libraries from the usual `/mnt/unionfs/Media` paths in `Admin > Libraries`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

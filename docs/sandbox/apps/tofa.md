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
      url: https://docs.tofa.tv/whats-new.html
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

### First-run setup

The server is claimed once, on first run, which links it to your tofa
account. Because the Saltbox install is reached through a public domain,
that first claim has to carry the setup token the server generates on boot:

```shell
sudo cat /opt/tofa/identity/setup_key.secret
```

Then open `https://tofa.iYOUR_DOMAIN_NAMEi/setup?setup_token=<token>` and
follow the wizard. The token is only consulted while the server is unclaimed.

Add libraries from the usual `/mnt/unionfs/Media` paths in `Admin > Libraries`.

### Hardware transcoding

The role enables GPU access, so the container picks up `/dev/dri` when
`gpu.intel` is set, and the NVIDIA runtime when `nvidia_enabled` is set. The
setup wizard detects what is available and the choice can be changed later in
`Admin > Settings > Transcoding`.

Transcode segments are written to `transcodes_path`, not to the appdata disk.

### Remote access

Clients reach the server over the Traefik URL, which the role advertises to
them automatically. No ports are published on the host.

On a home server, clients on your own network can be given a direct LAN
address instead, so their traffic does not leave and re-enter through your
domain. That needs both `tofa_role_open_main_ports` and `tofa_role_lan_ip`
below.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

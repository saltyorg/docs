---
icon: material/server-network-outline
hide:
  - tags
tags:
  - ddclient
  - dynamic-dns
  - cloudflare
  - dns
---

# DDClient

## Overview

[linuxserver/ddclient](https://docs.linuxserver.io/images/docker-ddclient) is a Docker container image for DDClient.

> [DDClient](https://ddclient.net) is a dynamic DNS client that automatically updates DNS records when your public IP address changes. [:material-bookshelf:](https://ddclient.net/general)

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://docs.linuxserver.io/general/container-customization){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/linuxserver/ddclient/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord:**Community**](https://linuxserver.io/discord){ .md-button .md-button--stretch }

</div>

---

## Deployment

```shell
sb install ddclient
```

## Basics

DDClient is automatically configured for Cloudflare with common Saltbox subdomains. Configuration file is created at `/opt/ddclient/ddclient.conf` - edit this file to customize subdomains.

Requires Cloudflare to be enabled in your Saltbox configuration with valid API credentials in `accounts.yml`.

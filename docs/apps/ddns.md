---
hide:
  - tags
tags:
  - ddns
  - cloudflare
  - dns
  - dynamic-dns
---

# DDNS

## What is it?

A Saltbox-specific Dynamic DNS service that automatically manages DNS records with Cloudflare based on Traefik routes. This container monitors Traefik's API for active routes and automatically creates or updates corresponding DNS records in Cloudflare, supporting both IPv4 and IPv6.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/saltyorg/saltbox){: .header-icons } | [:octicons-link-16: Docs](https://docs.saltbox.dev){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/saltyorg/saltbox){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/saltydk/dns){: .header-icons }|

### 1. Installation

``` shell

sb install ddns

```

### 2. Setup

#### Prerequisites

- Cloudflare must be enabled in your Saltbox configuration
- IPv4 or IPv6 DNS management must be enabled in `adv_settings.yml`
- Valid Cloudflare API credentials must be configured in `accounts.yml`

#### Configuration

The DDNS container automatically monitors Traefik's API endpoint for active routes and creates or updates corresponding DNS records in Cloudflare based on your configured IP version preferences.

#### Custom URLs

You can manage additional custom URLs by setting the `ddns_custom_urls` variable in your [Saltbox inventory](../saltbox/inventory/index.md):

```yaml
ddns_custom_urls: "subdomain1.domain.com,subdomain2.domain.com"
```

#### Notes

- This service only works with Cloudflare DNS
- The container requires access to Traefik's API to discover routes
- DNS records are automatically managed based on active Traefik routes

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

[DDClient](https://ddclient.net/) is a dynamic DNS client that automatically updates DNS records when your public IP address changes. The Saltbox implementation comes pre-configured for Cloudflare with common Saltbox subdomain entries.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://ddclient.net/){: .header-icons } | [:octicons-link-16: Docs](https://ddclient.net/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/ddclient/ddclient){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/ddclient){: .header-icons }|

### 1. Installation

``` shell

sb install ddclient

```

### 2. Setup

DDClient is automatically configured for Cloudflare with common Saltbox subdomains. Configuration file is created at `/opt/ddclient/ddclient.conf` - edit this file to customize subdomains.

Requires Cloudflare to be enabled in your Saltbox configuration with valid API credentials in `accounts.yml`.

- [:octicons-link-16: Documentation: DDClient Wiki](https://github.com/ddclient/ddclient/wiki){: .header-icons }

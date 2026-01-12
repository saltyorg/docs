---
icon: material/server-network-outline
title: DDClient
hide:
  - tags
tags:
  - ddclient
  - dynamic-dns
  - cloudflare
  - dns
saltbox_automation:
  sections:
    inventory: false
  app_links:
    - name: Manual
      url: https://ddclient.net/general
      type: documentation
    - name: Releases
      url: https://hub.docker.com/r/linuxserver/ddclient/tags
      type: releases
    - name: Community
      url:
      type: community
  project_description:
    name: DDClient
    summary: |
      a dynamic DNS client that automatically updates DNS records when your public IP address changes.
    link: https://ddclient.net
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# DDClient

## Overview

[DDClient](https://ddclient.net) is a dynamic DNS client that automatically updates DNS records when your public IP address changes.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://ddclient.net/general){ .md-button .md-button--stretch }

[:fontawesome-solid-newspaper:**Releases**](https://hub.docker.com/r/linuxserver/ddclient/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install ddclient
```

## Basics

DDClient is automatically configured for Cloudflare with common Saltbox subdomains. Configuration file is created at `/opt/ddclient/ddclient.conf` - edit this file to customize subdomains.

Requires Cloudflare to be enabled in your Saltbox configuration with valid API credentials in `accounts.yml`.

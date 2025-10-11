---
tags:
  - Minecraft
---

# Minecraft Bedrock

## What is it?

[Minecraft Bedrock](https://github.com/itzg/docker-minecraft-bedrock-server) is a server for the multi-platform version of Minecraft.

!!! note
    📢 This server will expose the port UDP 19132

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/itzg/docker-minecraft-bedrock-server){: .header-icons } | [:octicons-link-16: Docs](https://github.com/itzg/docker-minecraft-bedrock-server){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/itzg/docker-minecraft-bedrock-server){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/itzg/minecraft-bedrock-server){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-minecraft-bedrock

```

### 2. Join Server

- The server will be accessible at `minecraft-bedrock._yourdomain.com_` or `_yourserverip_:19132`

!!! warning "Cloudflare CDN"
    If you are using Cloudflare, you will need to disable the proxy for the subdomain(s) to work correctly. This can be done by clicking the orange cloud next to the subdomain in the DNS settings. Or specify it in the inventory using `minecraft-bedrock_dns_proxy: false` if you have the global toggle on. Otherwise you won't be able to reach the minecraft server at all.

### Change server version

By default, the server will be using the latest version available. To choose a specific version add `minecraft_bedrock_version: "1.19.31"` to the [inventory system](../../saltbox/inventory/index.md).

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

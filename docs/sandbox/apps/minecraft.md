---
tags:
  - Minecraft
---

# Minecraft

## What is it?

Run one or multiple minecraft servers with custom subdomains. Utilizes Minecraft server and MC-Router to allow each server to have its own subdomain with the default port.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://docker-minecraft-server.readthedocs.io/en/latest/){: .header-icons } | [:octicons-link-16: Docs](https://docker-minecraft-server.readthedocs.io/en/latest/commands/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/itzg/docker-minecraft-server){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-minecraft

```

This will install mc-router and the minecraft server. If you have listed multiple minecraft instances, it will install these too. (See below for multi server instructions)

### 2. Join Server

!!! warning "Cloudflare CDN"
    If you are using Cloudflare, you will need to disable the proxy for the subdomain(s) to work correctly. This can be done by clicking the orange cloud next to the subdomain in the DNS settings. Or specify it in the inventory using `minecraft_dns_proxy: false` if you have the global toggle on. Otherwise you won't be able to reach the minecraft server at all.

- By default, a single server will be accesible at  `minecraft._yourdomain.com_`
- If you have set up multiple instances, these will be accesible by default at `instanceName._yourdomain.com_` (See multi server instructions below)

### 3. Multi Server Set Up

To add multiple instances, add the following to the inventory. See the [inventory configuration instructions](../../saltbox/inventory/index.md).

``` yaml

minecraft_instances: ["mcserver1", "mcserver2"] # (1)!

```

1. This will install two servers, server1 and server2.

These servers will be accesible at `instanceName._yourdomain.com_`

So for the example above, `mcserver1._yourdomain.com_` and `mcserver2._yourdomain.com_`

### 4. Setup

For individual servers, you can change things such as memory using custom docker envs. See the [inventory configuration instructions](../../saltbox/inventory/index.md)

For a single install, the inventory vars will look like this `minecraft_docker_image_tag`.

When you have set up multiple servers, they will all use the `minecraft_docker_image_tag` settings as a default. To override this use the instance name instead. E.g `instanceName_docker_image_tag`.

``` yaml title="Inventory"

minecraft_instances: ["mcserver1", "mcserver2"] # (1)!
mcserver1_docker_image_tag: "itzg/minecraft-server:latest" # (2)!
mcserver2_docker_image_tag: "itzg/minecraft-server:1.17.1" # (3)!

```

1. This will install two servers, mcserver1 and mcserver2.
2. This will install the latest version of the minecraft server on mcserver1.
3. This will install version 1.17.1 of the minecraft server on mcserver2.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
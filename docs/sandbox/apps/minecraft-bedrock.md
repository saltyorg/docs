# Minecraft Bedrock

## What is it?

This is a Minecraft Bedrock server for the multi-platform Minecraft version.

!!! Note
    📢 This server will expose the port UDP 19132

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home ](https://github.com/itzg/docker-minecraft-bedrock-server){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/itzg/docker-minecraft-bedrock-server){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/itzg/docker-minecraft-bedrock-server){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker ](https://hub.docker.com/r/itzg/minecraft-bedrock-server){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install sandbox-minecraft-bedrock

```

### 2. Join Server

- By default, the server will be accesible at `_yourserverip_:19132`
- You can set up a SRV record to access the server at a subdomain of your choice (See SRV instructions below)

### 3. Setup SRV record

!!! Note
    In this example we will be using `minecraft._yourdomain.com_`

- Create A record `minecraft` pointing to your server ip
- Create SRV entry like this
    - Name: `minecraft`
    - Service: `_minecraft`
    - Protocol: UDP
    - Port: 19132
    - Target: `minecraft._yourdomain.com_`
- Now you can access the server at `minecraft._yourdomain.com_`

### Change server version

By default, the server will be using the latest version available. To choose a specific version add `minecraft_bedrock_version: "1.19.31"` to the [inventory system](https://docs.saltbox.dev/saltbox/inventory/).
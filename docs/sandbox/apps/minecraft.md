# Minecraft

## What is it?

Run one or multiple minecraft servers with custom domains. Utilises minecraft server and mc-router to allow each server to have its own subdomain with the default port.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/itzg/docker-minecraft-server){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/itzg/docker-minecraft-server){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/itzg/docker-minecraft-server){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/itzg/minecraft-server){: .header-icons target=_blank rel="noopener noreferrer" }
| [:material-home: Project home](https://github.com/itzg/mc-router){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/itzg/mc-router){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/itzg/mc-router){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/itzg/mc-router){: .header-icons target=_blank rel="noopener noreferrer" }

### 1. Installation

``` shell

sb install sandbox-minecraft

```

This will install mc-router and the minecraft server. If you have listed multiple minecraft instances, it will install these too. (See below for multi server instructions)

### 2. Join Server

- By default, a single server will be accesible at  `minecraft._yourdomain.com_`
- If you have set up multiple instances, these will be accesible by default at `instanceName._yourdomain.com_` (See multi server instructions below)

### 3. Multi Server Set Up

To add multiple instances, add:

```yaml

minecraft_instances: ["server1", "server2"]

```

To the inventory files. [See instuctions on inventory here](https://docs.saltbox.dev/saltbox/inventory/)

These servers will be accesible at `instanceName.__yourdomain.com__`

So for the example above, `server1.youdomain.com` and `server2.yourdomain.com`

### 4. Setup

For individual servers, you can change things such as memory using custom docker envs. [See instuctions on inventory here](https://docs.saltbox.dev/saltbox/inventory/)

For a single install, the inventory paths will look like this `minecraft_docker_image_tag`

When you have set up multiple servers, they will all use the `minecraft_docker_image_tag` settings as a default. To override this use the instance name instead. E.g `instanceName_docker_image_tag`
- [:octicons-link-16: Documentation](https://github.com/itzg/docker-minecraft-server){: .header-icons target=_blank rel="noopener noreferrer" }

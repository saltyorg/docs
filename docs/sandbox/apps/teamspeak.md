---
hide:
  - tags
tags:
  - teamspeak
  - voicechat
---

# TeamSpeak

Software for quality voice communication via the Internet.

<div class="grid sb-buttons" markdown data-search-exclude>

[:material-home: Homepage&nbsp;&nbsp;](https://teamspeak.com){ .md-button .md-button--stretch }

[:material-bookshelf: Manual&nbsp;&nbsp;](https://github.com/docker-library/docs/blob/master/teamspeak/README.md){ .md-button .md-button--stretch }

[:fontawesome-brands-docker: Releases&nbsp;&nbsp;](https://hub.docker.com/_/teamspeak/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-teamspeak: Community&nbsp;&nbsp;](https://community.teamspeak.com){ .md-button .md-button--stretch }

</div>

---

## Configuration

Settings are available as Docker environment variables[<sup>:octicons-link-external-16:</sup>][envs] which you may customize using the Saltbox Inventory[<sup>:octicons-link-24:</sup>][inventory].

## Deployment

```shell
sb install sandbox-teamspeak
```

## Usage

Connect to the server using a TeamSpeak client at `teamspeak._yourdomain.com_` using the default port 9987.

[envs]: https://github.com/docker-library/docs/blob/master/teamspeak/README.md#environment-variables "Access project Docker environment variables reference"
[inventory]: ../../saltbox/inventory/index.md "Access Inventory user guide"

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

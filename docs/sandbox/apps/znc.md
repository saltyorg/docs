---
hide:
  - tags
tags:
  - znc
  - irc
  - bouncer
---

# ZNC

## What is it?

[ZNC](https://wiki.znc.in/ZNC) is an an advanced IRC bouncer that is left connected so an IRC client can disconnect/reconnect without losing the chat session.

It can detach the client from the actual IRC server, and also from selected channels. Multiple clients from different locations can connect to a single ZNC account simultaneously and therefore appear under the same nickname on IRC.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-docker: Docker:](https://wiki.znc.in/ZNC){: .header-icons } | [:octicons-link-16: Docs](https://wiki.znc.in/ZNC){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/linuxserver/docker-znc){: .header-icons } | [:material-docker: Docker:](https://hub.docker.com/r/linuxserver/znc){: .header-icons } |

### 1. Installation

``` shell

sb install sandbox-znc

```

### 2. URL

- To access ZNC, visit `https://znc._yourdomain.com_`

Default user/password: admin/admin

Change that password ASAP.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

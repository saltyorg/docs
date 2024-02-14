# Node Red

## What is it?

[Node Red](https://www.node-red.org/) is a flow-based development tool for visual programming developed originally by IBM for wiring together hardware devices, APIs and online services as part of the Internet of Things.

!!! warning
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.node-red.org/){: .header-icons } | [:octicons-link-16: Docs](https://www.node-red.org/docs){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/advplyr/node-red-web){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/advplyr/node-red){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-node-red

```

### 2. Setup

Addons and/or plugins can be installed to Node Red to add functionality. They are called palettes. To install a palette, go to the menu in the upper right corner (the hamburger, 3 little horizontal lines), select `Manage palette`, then `Install`.

Add this [palette](https://flows.nodered.org/node/node-red-contrib-home-assistant-websocket) to connect to [home assistant](../apps/homeassistant.md).

### 3. URL

- To access node-red, visit `https://node-red._yourdomain.com_`

- [:octicons-link-16: Documentation: Node Red Docs](https://www.node-red.org/docs){: .header-icons }

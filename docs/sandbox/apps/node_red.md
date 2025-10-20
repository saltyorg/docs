---
hide:
  - tags
tags:
  - node-red
  - automation
  - iot
---

# Node Red

## What is it?

[Node Red](https://www.nodered.org/) is a flow-based development tool for visual programming developed originally by IBM for wiring together hardware devices, APIs and online services as part of the Internet of Things.

!!! warning
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.nodered.org/){: .header-icons } | [:octicons-link-16: Docs](https://www.nodered.org/docs/user-guide){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/node-red/node-red){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/nodered/node-red){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-node-red

```

### 2. URL

- To access node-red, visit `https://node-red._yourdomain.com_`

### 3. Setup

Addons and/or plugins can be installed to Node Red to add functionality. In Node Red they are called palettes. To install a palette, go to the menu in the upper right corner (the hamburger, 3 little horizontal lines), select `Manage palette`, then `Install`. You can search for a palette by name, or you can install a palette by pasting the URL of the palette into the `Install` tab.

Add this [palette](https://flows.nodered.org/node/node-red-contrib-home-assistant-websocket) to connect to [Home Assistant](../apps/homeassistant.md). (Requires Home Assistant to be installed and running, and HACS to be installed in Home Assistant.) For more information, see the Home Assistant page.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
hide:
  - tags
tags:
  - homeassistant
  - automation
  - iot
---

# Homeassistant

## What is it?

[Homeassistant](https://www.home-assistant.io/) is a tool designed for (open source) home automation that puts local control and privacy first. Powered by a worldwide community of tinkerers and DIY enthusiasts.

Note that while it will work on a remote server, it takes some doing to get it to interface with a local server or local devices. It is not recommended or supported.

!!! Warning
    By default, the role is NOT protected behind your Authelia/SSO middleware. Home Assistant has its own authentication system (with 2FA), and it is recommended to use that.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.home-assistant.io/){: .header-icons } | [:octicons-link-16: Docs](https://www.home-assistant.io/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/home-assistant/core){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/homeassistant/home-assistant/tags){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-homeassistant

```

### 2. URL

- To access Homeassistant, visit `https://homeassistant._yourdomain.com_`

### 3. Setup

Home Assistant is pretty versatile and works with a lot of different apps/containers, some of which we have roles for. See [MQTT](../apps/mqtt.md) for using Mosquitto to communicate with local and remote devices. We also have [Node Red](../apps/node-red.md), which is a platform for multiple types of automations.

??? Note "Nabu Casa"
    You don't NEED to use Nabu Casa to access Home Assistant remotely. You can use a reverse proxy to access it remotely. However, if you want to use Nabu Casa, you can use the [Nabu Casa](https://www.nabucasa.com/) integration to connect to Home Assistant. It is a paid service, but it is a good way to support the Home Assistant project. That said, the Home Assistant role is set up to work with a reverse proxy, so you can use that instead.

### 4. Addons

You can also use the [Home Assistant Community Store (HACS)](https://hacs.xyz/) to add more functionality to Home Assistant. For instance, adding the Node Red Companion, a "custom" integration for node-red-contrib-home-assistant-websocket. It allows you to integrate Node-RED with Home Assistant. For more information, see the [Node Red](../apps/node-red.md) page.

- [:octicons-link-16: Documentation: Home Assistant Docs](https://www.home-assistant.io/docs/){: .header-icons }

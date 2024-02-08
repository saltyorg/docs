# Homeassistant

## What is it?

[Homeassistant](https://www.home-assistant.io/) is a tool designed for (open source) home automation that puts local control and privacy first. Powered by a worldwide community of tinkerers and DIY enthusiasts.

Note that while it will work on a remote server, it takes some doing to get it to interface with a local server or local devices. It is not recommended or supported.

!!! Warning
    By default, the role is NOT protected behind your Authelia/SSO middleware.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.home-assistant.io/){: .header-icons } | [:octicons-link-16: Docs](https://www.home-assistant.io/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/home-assistant/core){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/homeassistant/home-assistant/tags){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-homeassistant

```

### 2. URL

- To access Homeassistant, visit `https://homeassistant._yourdomain.com_`

### Setup

Home Assistant is pretty versatile and works with a lot of different apps/containers, some of which we have roles for. See [MQTT](../apps/mqtt.md) for using Mosquitto to communicate with local and remote devices.We also have [Node Red](../apps/node-red.md), which is a platform for multiple types of automations.

- [:octicons-link-16: Documentation: homeassistant Docs](https://www.home-assistant.io/docs/){: .header-icons }

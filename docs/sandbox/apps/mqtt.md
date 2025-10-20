---
hide:
  - tags
tags:
  - mqtt
  - automation
  - messaging
---

# MQTT

## What is it?

[MQTT](https://mosquitto.org/) (or Eclipse Mosquitto) is a lightweight messaging protocol that is designed for use in constrained devices and low-bandwidth, high-latency, or unreliable networks. It is commonly used in Internet of Things (IoT) devices/applications for efficient and reliable communication between devices.

Also, MQTT does not have a web interface, so you will need to use a client to interact with it.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://mosquitto.org/){: .header-icons } | [:octicons-link-16: Docs](https://mosquitto.org/man/mosquitto-conf-5.html){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/eclipse/mosquitto){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/eclipse-mosquitto){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-mqtt

```

### 2. Setup

You can connect MQTT to [Home Assistant](homeassistant.md) and [Node Red](node_red.md) via docker hostname. Add the MQTT integration in Home Assistant and use `mqtt` as the hostname/Broker, and 1883 as the port. In Node Red, you can use the `mqtt` node to connect to the MQTT server.

While MQTT can be set up to use a username and password, it is not recommended to expose it to the internet. So by default, MQTT is not exposed to the internet, nor does it have a username and password.

To add a username and password, you will need to edit the `mosquitto.conf` file. You can find the file in the `/opt/mqtt/config/` directory. You will need to add the following lines to the file:

``` shell title="mosquitto.conf"
allow_anonymous false # (1)!
user <username> # (2)!
password <password> # (3)!
```

1. This line will disable anonymous access to the MQTT server. It is currently set to `true` by default.
2. This line will add a username to the MQTT server. Replace `<username>` with your desired username.
3. This line will add a password to the MQTT server. Replace `<password>` with your desired password.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
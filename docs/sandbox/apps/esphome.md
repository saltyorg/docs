---
hide:
  - tags
tags:
  - esphome
  - automation
  - iot
---

# ESPHome

## What is it?

[ESPHome](https://esphome.io/)  is an open-source firmware framework that simplifies the process of creating custom firmware for popular WiFi-enabled microcontrollers.

ESPHome is typically installed as a Homeassistant add-on, but when using Homeassistant in a container add-ons are disabled.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://esphome.io/){: .header-icons } | [:octicons-link-16: Docs](https://esphome.io/components/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/imagegenius/docker-esphome/){: .header-icons } | [:material-docker: Docker](https://ghcr.io/esphome/esphome){: .header-icons }|

Using a docker image from ImageGenius since adds user permission mapping (as of 6/10/2025)

### 1. Installation

``` shell
sb install sandbox-esphome

```

### 2. URL

- To access ESPHome, visit `https://esphome._yourdomain.com_`

### 3. Usage

`https://esphome._yourdomain.com_` is where you can go to manage/add devices, create/store .yaml files, and manage secrets. The .yaml files will be stored in `/opt/esphome/`

See the [ESPHome docs](https://esphome.io/components/) and [ESPHome forums](https://community.home-assistant.io/c/esphome/) for .yaml file creation assistance.

If adding ESPHome into your Homeassistant, it should auto-detect any newly created devices.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
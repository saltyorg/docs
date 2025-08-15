---
hide:
  - tags
tags:
  - apprise
  - notifications
  - alerts
---

# Apprise

## What is it?

[Apprise](https://github.com/caronc/apprise) allows you to send a notification to almost all of the most popular notification services available to us today such as: Telegram, Discord, Slack, Amazon SNS, Gotify, etc.

!!! note
    Saltbox has a built-in Apprise client that can be used to send notifications. This container is not only used to provide a web UI for configuring and managing notifications, but it also exposes an API. This API allows for programmatic interaction, enabling other applications or scripts to send notifications through the Apprise service. For more information, see the [Apprise Client Docs](https://github.com/caronc/apprise/wiki).

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/caronc/apprise){: .header-icons } | [:octicons-link-16: Docs](https://github.com/caronc/apprise/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/caronc/apprise){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/caronc/apprise){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-apprise

```

### 2. URL

- To access apprise, visit `https://apprise._yourdomain.com_`

### 3. Setup

The instance runs on the Docker network accessible to other saltbox network containers at `http://apprise:8000`

The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#__tabbed_2_1) file located in `/srv/git/saltbox/accounts.yml`

A typical apprise URL would look like this:

``` shell

https://apprise._yourdomain.com_/notify?service=discord&title=Hello&body=World

```

- [:octicons-link-16: Documentation: Apprise Client Docs](https://github.com/caronc/apprise/wiki){: .header-icons }

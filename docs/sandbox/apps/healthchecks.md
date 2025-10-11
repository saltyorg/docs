---
hide:
  - tags
tags:
  - healthchecks
  - monitoring
  - cron
---

# Healthchecks

## What is it?

[Healthchecks](https://healthchecks.io/) is a watchdog for your cron jobs. It's a web server that listens for pings from your cron jobs, plus a web interface.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://healthchecks.io/){: .header-icons } | [:octicons-link-16: Docs](https://healthchecks.io/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/healthchecks/healthchecks){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/healthchecks){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-healthchecks

```

### 2. URL

- To access Healthchecks, visit `https://healthchecks._yourdomain.com_`

### 3. Setup

- The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

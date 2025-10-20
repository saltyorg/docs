---
hide:
  - tags
tags:
  - glances
  - monitoring
  - system
---

# Glances

## What is it?

[Glances](http://nicolargo.github.io/glances/) is a cross-platform monitoring tool which aims to present a large amount of monitoring information through a curses or Web based interface. The information dynamically adapts depending on the size of the user interface.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](http://nicolargo.github.io/glances/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/nicolargo/glances/wiki){: .header-icons } | [:octicons-mark-github-16: Github](http://nicolargo.github.io/glances/){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/nicolargo/glances){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-glances-web

```

### 2. URL

- To access Glances, visit `https://glances._yourdomain.com_`

### 3. Setup

- The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
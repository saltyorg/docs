---
hide:
  - tags
tags:
  - speedtest
  - monitoring
  - network
---

# Speedtest

## What is it?

[Speedtest](https://github.com/librespeed/speedtest)  is a very lightweight Speedtest implemented in Javascript, using XMLHttpRequest and Web Workers.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/librespeed/speedtest){: .header-icons } | [:octicons-link-16: Docs](https://github.com/librespeed/speedtest){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/librespeed/speedtest){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/librespeed){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-speedtest

```

### 2. URL

- To access Speedtest, visit `https://speedtest._yourdomain.com_`

### 3. Setup

- [:octicons-link-16: Documentation: Speedtest Docs](https://github.com/librespeed/speedtest){: .header-icons }

To use a custom subdomain, add a custom value for `speedtest_web_subdomain` in the `/srv/git/saltbox/inventories/host_vars/localhost.yml` file. More info can be found [here](../../saltbox/inventory/index.md).

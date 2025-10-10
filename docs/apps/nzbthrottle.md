---
hide:
  - tags
tags:
  - nzbthrottle
  - usenet
  - bandwidth
  - automation
---

# NZBThrottle

## What is it?

NZBThrottle is a utility that automatically throttles Usenet download speeds based on custom schedules and conditions. It can dynamically adjust your download client's speed limits to ensure bandwidth is available when you need it most, such as during work hours or peak usage times.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/daghaian/nzbthrottle){: .header-icons } | [:octicons-link-16: Docs](https://github.com/daghaian/nzbthrottle#readme){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/daghaian/nzbthrottle){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/daghaian/nzbthrottle){: .header-icons }|

### 1. Installation

``` shell

sb install nzbthrottle

```

### 2. Setup

NZBThrottle automatically throttles Usenet download speeds based on custom schedules. Configure your download clients (SABnzbd, NZBGet, etc.) and schedules in `/opt/nzbthrottle/config.json`, then restart with `docker restart nzbthrottle`.

Note: Configuration is file-based with no web interface.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

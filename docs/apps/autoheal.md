---
hide:
  - tags
tags:
  - autoheal
  - docker
  - monitoring
---

# Autoheal

## What is it?

[Autoheal](https://github.com/willfarrell/docker-autoheal) monitors and restarts unhealthy Docker containers. It watches for containers that have a `HEALTHCHECK` defined and automatically restarts them when they become unhealthy, helping maintain service availability without manual intervention.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/willfarrell/docker-autoheal){: .header-icons } | [:octicons-link-16: Docs](https://github.com/willfarrell/docker-autoheal#readme){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/willfarrell/docker-autoheal){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/willfarrell/autoheal){: .header-icons }|

### 1. Installation

``` shell

sb install autoheal

```

### 2. Setup

Autoheal works automatically by monitoring Docker containers with health checks. All Saltbox-deployed containers are configured with the appropriate `autoheal` label, so no additional configuration is required after installation.

You can view Autoheal's activity in the container logs:

``` shell
docker logs autoheal
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
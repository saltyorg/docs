---
hide:
  - tags
tags:
  - cadvisor
  - monitoring
  - docker
---

# cAdvisor

## What is it?

[cAdvisor](https://github.com/google/cadvisor) (Container Advisor) provides container users an understanding of the resource usage and performance characteristics of their running containers. It is a running daemon that collects, aggregates, processes, and exports information about running containers.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/google/cadvisor){: .header-icons } | [:octicons-link-16: Docs](https://github.com/google/cadvisor/tree/master/docs){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/google/cadvisor){: .header-icons } | [:material-docker: Docker](https://gcr.io/cadvisor/cadvisor){: .header-icons }|

### 1. Installation

``` shell

sb install cadvisor

```

### 2. URL

- To access cAdvisor, visit `https://cadvisor._yourdomain.com_`

### 3. Setup

cAdvisor automatically monitors all Docker containers on your system. No additional configuration is required. The web interface provides resource usage, performance metrics, and container information.

cAdvisor is often used with Prometheus and Grafana for advanced metrics collection and visualization.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
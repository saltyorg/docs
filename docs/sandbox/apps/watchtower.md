---
hide:
  - tags
tags:
  - watchtower
  - monitoring
  - docker
---

# Watchtower

## What is it?

[Watchtower](https://containrrr.dev/watchtower/) is a process for automating Docker container base image updates.

With watchtower you can update the running version of your containerized app simply by pushing a new image to the Docker Hub or your own image registry. Watchtower will pull down your new image, gracefully shut down your existing container and restart it with the same options that were used when it was deployed initially.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://containrrr.dev/watchtower/){: .header-icons } | [:octicons-link-16: Docs](https://containrrr.github.io/watchtower){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/containrrr/watchtower){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/containrrr/watchtower){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-watchtower

```

### 2. Setup

- [:octicons-link-16: Documentation: Watchtower Docs](https://containrrr.github.io/watchtower){: .header-icons }

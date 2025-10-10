---
hide:
  - tags
tags:
  - redis
  - database
  - cache
  - key-value
---

# Redis

## What is it?

Redis is an open-source, in-memory data structure store used as a database, cache, message broker, and streaming engine. It supports various data structures such as strings, hashes, lists, sets, and sorted sets, making it extremely versatile and fast.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://redis.io/){: .header-icons } | [:octicons-link-16: Docs](https://redis.io/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/redis/redis){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/redis){: .header-icons }|

### 1. Installation

``` shell

sb install redis

```

### 2. Setup

Redis is deployed using the official Alpine image with data persisting to `/opt/redis/`. Connect from other containers using `redis://redis:6379`. Multiple instances are supported via the `redis_instances` variable in your [Saltbox inventory](../saltbox/inventory/index.md).

For custom configuration, create `redis.conf` in `/opt/redis/` and configure custom volumes in your inventory. Note: No authentication is configured by default.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

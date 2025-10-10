---
hide:
  - tags
tags:
  - postgresql
  - postgres
  - database
  - sql
---

# PostgreSQL Host

## What is it?

A host-based PostgreSQL installation role that deploys PostgreSQL directly on your server (not in Docker). This role supports multiple PostgreSQL versions running simultaneously, each on different ports, with full user and database management capabilities.

!!! warning "Advanced Users Only"
    This role is intended for advanced users who are comfortable running a database server directly on the host system and are aware of the security implications and maintenance considerations involved. Most users should use the [PostgreSQL](postgres.md) Docker container instead.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.postgresql.org/){: .header-icons } | [:octicons-link-16: Docs](https://www.postgresql.org/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/postgres/postgres){: .header-icons } | [:material-docker: Docker](https://www.postgresql.org/){: .header-icons }|

### 1. Installation

``` shell

sb install postgres-host

```

### 2. Setup

PostgreSQL is installed directly on the host with data stored in `/opt/postgresql/`. The default version is 17 (port 5432), with multiple versions supported via `postgres_host_role_versions` in your [Saltbox inventory](../saltbox/inventory/index.md). Each version runs on sequential ports (5432, 5433, etc.) as separate systemd services.

Configure per-version users, databases, and access control using `postgres_host_role_config` in your inventory. Default root superuser is `root`/`password4321` (change this!). Connect from Docker using `host.docker.internal:5432`.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->

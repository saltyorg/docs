---
icon: material/server-network-outline
hide:
  - tags
tags:
  - postgresql
  - postgres
  - database
  - sql
---

# PostgreSQL (Host Install)

## Overview

A host-based PostgreSQL installation role that deploys PostgreSQL directly on your server (not in Docker). This role supports multiple PostgreSQL versions running simultaneously, each on different ports, with full user and database management capabilities.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://www.postgresql.org/docs){ .md-button .md-button--stretch }

[:fontawesome-solid-newspaper:**Releases**](https://www.postgresql.org/ftp/source){ .md-button .md-button--stretch }

[:fontawesome-solid-people-group:**Community**](https://www.postgresql.org/community){ .md-button .md-button--stretch }

</div>

---

!!! warning "Advanced Users Only"

    This role is intended for advanced users who are comfortable running a database server directly on the host system and are aware of the security implications and maintenance considerations involved. Most users should use the [PostgreSQL](postgres.md) Docker container instead.

## Deployment

```shell
sb install postgres-host
```

## Usage

PostgreSQL is installed directly on the host with data stored in `/opt/postgresql/`. The default version is 17 (port 5432), with multiple versions supported via `postgres_host_role_versions` in your [Saltbox inventory](../saltbox/inventory/index.md). Each version runs on sequential ports (5432, 5433, etc.) as separate systemd services.

Configure per-version users, databases, and access control using `postgres_host_role_config` in your inventory. Default root superuser is `root`/`password4321` (change this!). Connect from Docker using `host.docker.internal:5432`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables.<span title="View override details for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        postgres_host_role_versions: ["item1", "item2"]
        ```

=== "Basics"

    ??? variable list "`postgres_host_role_versions`"

        ```yaml
        # Supports any versions from https://wiki.postgresql.org/wiki/Apt
        # Each version is unique and you cannot specify the same version twice
        # Type: list
        postgres_host_role_versions: ["17"]
        ```

=== "Superuser"

    ??? variable bool "`postgres_host_role_create_root_superuser`"

        ```yaml
        # Type: bool (true/false)
        postgres_host_role_create_root_superuser: true
        ```

    ??? variable string "`postgres_host_role_root_superuser_name`"

        ```yaml
        # Type: string
        postgres_host_role_root_superuser_name: "root"
        ```

    ??? variable string "`postgres_host_role_root_superuser_password`"

        ```yaml
        # Type: string
        postgres_host_role_root_superuser_password: "password4321"
        ```

=== "Per-Version Configuration"

    ??? variable dict "`postgres_host_role_config`"

        ```yaml
        # Example:
        # postgres_host_role_config:
        # "16":
        # allowed_hosts:
        # - "172.19.0.0/16"
        # - "10.0.0.0/8"
        # auth_method: "md5"
        # users:
        # - name: "app_user"
        # password: "password1"
        # - name: "app_user2"
        # password: "password2"
        # databases:
        # - name: "app_database"
        # users:
        # - "app_user"
        # - "app_user2"
        # - name: "metrics_db"
        # users:
        # - "app_user"
        # "17":
        # allowed_hosts:
        # - "172.19.0.0/16"
        # auth_method: "scram-sha-256"
        # users:
        # - name: "app_user3"
        # password: "password3"
        # databases:
        # - name: "new_app_database"
        # users:
        # - "app_user3"
        # Type: dict
        postgres_host_role_config: {}
        ```

=== "Access Control"

    ??? variable list "`postgres_host_role_allowed_hosts`"

        ```yaml
        # Type: list
        postgres_host_role_allowed_hosts:
          - "172.19.0.0/16"
        ```

    ??? variable string "`postgres_host_role_auth_method`"

        ```yaml
        # Type: string
        postgres_host_role_auth_method: "scram-sha-256"
        ```

=== "User & Database Configuration"

    ??? variable list "`postgres_host_role_users`"

        ```yaml
        # Type: list
        postgres_host_role_users:
          - name: "{{ user.name }}"
            password: "{{ user.pass }}"
        ```

    ??? variable list "`postgres_host_role_databases`"

        ```yaml
        # Type: list
        postgres_host_role_databases:
          - name: "saltbox"
            users: ["{{ user.name }}"]
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
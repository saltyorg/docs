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
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        postgres_host_role_versions: ["17", "18"]
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "GNU General Public License v3.0                      #"

    ```yaml
    # Type: list
    postgres_host_role_versions: ["17"]

    # Type: string
    postgres_host_role_primary_version: "{{ postgres_host_role_versions[0] }}"

    ```

??? example "Data Directory"

    ```yaml
    # Type: string
    postgres_host_role_data_directory: "/opt/postgresql"

    ```

??? example "Root Superuser"

    ```yaml
    # Type: bool (true/false)
    postgres_host_role_create_root_superuser: true

    # Type: string
    postgres_host_role_root_superuser_name: "root"

    # Type: string
    postgres_host_role_root_superuser_password: "password4321"

    ```

??? example "Per-Version Configuration"

    ```yaml
    # Type: dict
    postgres_host_role_config: {}

    ```

??? example "Access Control"

    ```yaml
    # Type: list
    postgres_host_role_allowed_hosts: 
      - "172.19.0.0/16"

    # Type: string
    postgres_host_role_auth_method: "scram-sha-256"

    ```

??? example "Global Fallback Configuration"

    ```yaml
    # Type: list
    postgres_host_role_users: 
      - name: "{{ user.name }}"
        password: "{{ user.pass }}"

    # Type: list
    postgres_host_role_databases: 
      - name: "saltbox"
        users: ["{{ user.name }}"]

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    postgres_host_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    postgres_host_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    postgres_host_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    postgres_host_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    postgres_host_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    postgres_host_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    postgres_host_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    postgres_host_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    postgres_host_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    postgres_host_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    postgres_host_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    postgres_host_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    postgres_host_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    postgres_host_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    postgres_host_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    postgres_host_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    postgres_host_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        postgres_host_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "postgres_host2.{{ user.domain }}"
          - "postgres_host.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        postgres_host_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'postgres_host2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

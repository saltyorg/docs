---
hide:
  - tags
tags:
  - plex-db
---

# Plex DB

## What is it?

`plex-db` runs some database maintenance tasks on the plex databases for each of your defined plex instances:

1. Check if main database passes integrity_check
1. Check if blobs database passes integrity_check
1. Back up databases
1. does a sqlite 'VACUUM' operation on the main database
1. does a sqlite 'VACUUM' operation on the blobs database
1. does a sqlite 'REINDEX' operation on the main database
1. does a sqlite 'REINDEX' operation on the blobs database

If any of those operations fail, the backup databases are restored.

The plex containers are stopped for the duration of this process.

### 1. Installation

``` shell

sb install plex-db

```

Further information:

- [:octicons-link-16: Sqlite VACUUM](https://www.sqlite.org/lang_vacuum.html)

- [:octicons-link-16: Sqlite REINDEX](https://www.sqlite.org/lang_reindex.html)

- [:octicons-link-16: A more comprehensive utility with similar purpose](https://github.com/ChuckPa/PlexDBRepair)

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        plex_db_integrity_check_only: true
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "GNU General Public License v3.0                      #"

    ```yaml
    # Type: bool (true/false)
    plex_db_integrity_check_only: false

    # Type: bool (true/false)
    plex_db_failed_integrity: false

    # Type: bool (true/false)
    plex_db_failed_optimization: false

    # Do not enable globally if deploying multiple instances
    # Type: list
    plex_db_files: 
      - "com.plexapp.plugins.library.db"
      - "com.plexapp.plugins.library.blobs.db"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    plex_db_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    plex_db_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    plex_db_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    plex_db_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    plex_db_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    plex_db_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    plex_db_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    plex_db_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    plex_db_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    plex_db_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    plex_db_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    plex_db_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    plex_db_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    plex_db_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    plex_db_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    plex_db_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    plex_db_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        plex_db_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "plex_db2.{{ user.domain }}"
          - "plex_db.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        plex_db_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'plex_db2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

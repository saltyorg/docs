---
hide:
  - tags
tags:
  - influxdb
  - database
  - timeseries
---

# InfluxDB

## What is it?

[InfluxDB](https://www.influxdata.com/products/influxdb/) is an open source time series database for recording metrics, events, and analytics.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.influxdata.com/products/influxdb/){: .header-icons } | [:octicons-link-16: Docs](hhttps://docs.influxdata.com/influxdb/v1/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/influxdata/influxdata-docker){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/influxdb){: .header-icons }|

!!! note
    This role is version locked to version `1.8.4` to support the `varken` role. To utilize InfluxDB version 2.0, utilize the `influxdb2` role.

### 1. Installation

``` shell

sb install sandbox-influxdb

```

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        influxdb_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    influxdb_name: influxdb

    ```

??? example "Paths"

    ```yaml
    # Type: string
    influxdb_role_paths_folder: "{{ influxdb_name }}"

    # Type: string
    influxdb_role_paths_location: "{{ server_appdata_path }}/{{ influxdb_role_paths_folder }}"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    influxdb_role_docker_container: "{{ influxdb_name }}"

    # Image
    # Type: bool (true/false)
    influxdb_role_docker_image_pull: true

    # Type: string
    influxdb_role_docker_image_repo: "influxdb"

    # Type: string
    influxdb_role_docker_image_tag: "1.8.4"

    # Type: string
    influxdb_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='influxdb') }}:{{ lookup('role_var', '_docker_image_tag', role='influxdb') }}"

    # Volumes
    # Type: list
    influxdb_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='influxdb') }}:/var/lib/influxdb"

    # Type: list
    influxdb_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    influxdb_role_docker_hostname: "{{ influxdb_name }}"

    # Networks
    # Type: string
    influxdb_role_docker_networks_alias: "{{ influxdb_name }}"

    # Type: list
    influxdb_role_docker_networks_default: []

    # Type: list
    influxdb_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    influxdb_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    influxdb_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    influxdb_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    influxdb_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    influxdb_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    influxdb_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    influxdb_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    influxdb_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    influxdb_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    influxdb_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    influxdb_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    influxdb_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    influxdb_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    influxdb_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    influxdb_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    influxdb_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    influxdb_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    influxdb_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    influxdb_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        influxdb_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "influxdb2.{{ user.domain }}"
          - "influxdb.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        influxdb_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'influxdb2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

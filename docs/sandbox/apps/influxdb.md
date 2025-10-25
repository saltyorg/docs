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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    influxdb_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `influxdb_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `influxdb_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`influxdb_name`"

        ```yaml
        # Type: string
        influxdb_name: influxdb
        ```

=== "Paths"

    ??? variable string "`influxdb_role_paths_folder`"

        ```yaml
        # Type: string
        influxdb_role_paths_folder: "{{ influxdb_name }}"
        ```

    ??? variable string "`influxdb_role_paths_location`"

        ```yaml
        # Type: string
        influxdb_role_paths_location: "{{ server_appdata_path }}/{{ influxdb_role_paths_folder }}"
        ```

    ??? variable bool "`influxdb_role_paths_recursive`"

        ```yaml
        # Type: bool (true/false)
        influxdb_role_paths_recursive: true
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`influxdb_role_docker_container`"

        ```yaml
        # Type: string
        influxdb_role_docker_container: "{{ influxdb_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`influxdb_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        influxdb_role_docker_image_pull: true
        ```

    ??? variable string "`influxdb_role_docker_image_repo`"

        ```yaml
        # Type: string
        influxdb_role_docker_image_repo: "influxdb"
        ```

    ??? variable string "`influxdb_role_docker_image_tag`"

        ```yaml
        # Type: string
        influxdb_role_docker_image_tag: "1.12"
        ```

    ??? variable string "`influxdb_role_docker_image`"

        ```yaml
        # Type: string
        influxdb_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='influxdb') }}:{{ lookup('role_var', '_docker_image_tag', role='influxdb') }}"
        ```

    <h5>Volumes</h5>

    ??? variable list "`influxdb_role_docker_volumes_default`"

        ```yaml
        # Type: list
        influxdb_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='influxdb') }}:/var/lib/influxdb"
        ```

    ??? variable list "`influxdb_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        influxdb_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`influxdb_role_docker_hostname`"

        ```yaml
        # Type: string
        influxdb_role_docker_hostname: "{{ influxdb_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`influxdb_role_docker_networks_alias`"

        ```yaml
        # Type: string
        influxdb_role_docker_networks_alias: "{{ influxdb_name }}"
        ```

    ??? variable list "`influxdb_role_docker_networks_default`"

        ```yaml
        # Type: list
        influxdb_role_docker_networks_default: []
        ```

    ??? variable list "`influxdb_role_docker_networks_custom`"

        ```yaml
        # Type: list
        influxdb_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`influxdb_role_docker_restart_policy`"

        ```yaml
        # Type: string
        influxdb_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`influxdb_role_docker_state`"

        ```yaml
        # Type: string
        influxdb_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`influxdb_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        influxdb_role_autoheal_enabled: true
        ```

    ??? variable string "`influxdb_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        influxdb_role_depends_on: ""
        ```

    ??? variable string "`influxdb_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        influxdb_role_depends_on_delay: "0"
        ```

    ??? variable string "`influxdb_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        influxdb_role_depends_on_healthchecks:
        ```

    ??? variable bool "`influxdb_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        influxdb_role_diun_enabled: true
        ```

    ??? variable bool "`influxdb_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        influxdb_role_dns_enabled: true
        ```

    ??? variable bool "`influxdb_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        influxdb_role_docker_controller: true
        ```

    ??? variable bool "`influxdb_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        influxdb_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`influxdb_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        influxdb_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`influxdb_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        influxdb_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`influxdb_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        influxdb_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`influxdb_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        influxdb_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`influxdb_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        influxdb_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`influxdb_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        influxdb_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`influxdb_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        influxdb_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`influxdb_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        influxdb_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`influxdb_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        influxdb_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            influxdb_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "influxdb2.{{ user.domain }}"
              - "influxdb.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`influxdb_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        influxdb_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            influxdb_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'influxdb2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`influxdb_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        influxdb_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
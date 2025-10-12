---
hide:
  - tags
tags:
  - influxdb2
  - database
  - timeseries
---

# InfluxDB2

## What is it?

[InfluxDB2](https://www.influxdata.com/products/influxdb/) is an open source time series database for recording metrics, events, and analytics.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.influxdata.com/products/influxdb/){: .header-icons } | [:octicons-link-16: Docs](https://docs.influxdata.com/influxdb/latest/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/influxdata/influxdata-docker){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/influxdb){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-influxdb2

```

### 2. URL

- To access InfluxDB2, visit `https://influxdb2._yourdomain.com_`

### 3. Setup

- To setup the initial admin user, token and bucket, visit the UI at the URL above.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `influxdb2_instances`.

    === "Role-level Override"

        Applies to all instances of influxdb2:

        ```yaml
        influxdb2_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `influxdb22`):

        ```yaml
        influxdb22_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `influxdb2_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `influxdb2_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        influxdb2_instances: ["influxdb2"]

        ```

    === "Example"

        ```yaml
        # Type: list
        influxdb2_instances: ["influxdb2", "influxdb22"]

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        influxdb2_role_paths_folder: "{{ influxdb2_name }}"

        # Type: string
        influxdb2_role_paths_location: "{{ server_appdata_path }}/{{ influxdb2_role_paths_folder }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        influxdb22_paths_folder: "{{ influxdb2_name }}"

        # Type: string
        influxdb22_paths_location: "{{ server_appdata_path }}/{{ influxdb2_role_paths_folder }}"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        influxdb2_role_web_subdomain: "{{ influxdb2_name }}"

        # Type: string
        influxdb2_role_web_domain: "{{ user.domain }}"

        # Type: string
        influxdb2_role_web_port: "8086"

        # Type: string
        influxdb2_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='influxdb2') + '.' + lookup('role_var', '_web_domain', role='influxdb2')
                                 if (lookup('role_var', '_web_subdomain', role='influxdb2') | length > 0)
                                 else lookup('role_var', '_web_domain', role='influxdb2')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        influxdb22_web_subdomain: "{{ influxdb2_name }}"

        # Type: string
        influxdb22_web_domain: "{{ user.domain }}"

        # Type: string
        influxdb22_web_port: "8086"

        # Type: string
        influxdb22_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='influxdb2') + '.' + lookup('role_var', '_web_domain', role='influxdb2')
                             if (lookup('role_var', '_web_subdomain', role='influxdb2') | length > 0)
                             else lookup('role_var', '_web_domain', role='influxdb2')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        influxdb2_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='influxdb2') }}"

        # Type: string
        influxdb2_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='influxdb2') }}"

        # Type: bool (true/false)
        influxdb2_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        influxdb22_dns_record: "{{ lookup('role_var', '_web_subdomain', role='influxdb2') }}"

        # Type: string
        influxdb22_dns_zone: "{{ lookup('role_var', '_web_domain', role='influxdb2') }}"

        # Type: bool (true/false)
        influxdb22_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        influxdb2_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        influxdb2_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        influxdb2_role_traefik_middleware_custom: ""

        # Type: string
        influxdb2_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        influxdb2_role_traefik_enabled: true

        # Type: bool (true/false)
        influxdb2_role_traefik_api_enabled: false

        # Type: string
        influxdb2_role_traefik_api_endpoint: ""

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        influxdb22_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        influxdb22_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        influxdb22_traefik_middleware_custom: ""

        # Type: string
        influxdb22_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        influxdb22_traefik_enabled: true

        # Type: bool (true/false)
        influxdb22_traefik_api_enabled: false

        # Type: string
        influxdb22_traefik_api_endpoint: ""

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        influxdb2_role_docker_container: "{{ influxdb2_name }}"

        # Image
        # Type: bool (true/false)
        influxdb2_role_docker_image_pull: true

        # Type: string
        influxdb2_role_docker_image_tag: "2-alpine"

        # Type: string
        influxdb2_role_docker_image_repo: "influxdb"

        # Type: string
        influxdb2_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='influxdb2') }}:{{ lookup('role_var', '_docker_image_tag', role='influxdb2') }}"

        # Volumes
        # Type: list
        influxdb2_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='influxdb2') }}/data:/var/lib/influxdb22"
          - "{{ lookup('role_var', '_paths_location', role='influxdb2') }}/config:/etc/influxdb22"

        # Type: list
        influxdb2_role_docker_volumes_custom: []

        # Hostname
        # Type: string
        influxdb2_role_docker_hostname: "{{ influxdb2_name }}"

        # Networks
        # Type: string
        influxdb2_role_docker_networks_alias: "{{ influxdb2_name }}"

        # Type: list
        influxdb2_role_docker_networks_default: []

        # Type: list
        influxdb2_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        influxdb2_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        influxdb2_role_docker_state: started

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        influxdb22_docker_container: "{{ influxdb2_name }}"

        # Image
        # Type: bool (true/false)
        influxdb22_docker_image_pull: true

        # Type: string
        influxdb22_docker_image_tag: "2-alpine"

        # Type: string
        influxdb22_docker_image_repo: "influxdb"

        # Type: string
        influxdb22_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='influxdb2') }}:{{ lookup('role_var', '_docker_image_tag', role='influxdb2') }}"

        # Volumes
        # Type: list
        influxdb22_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='influxdb2') }}/data:/var/lib/influxdb22"
          - "{{ lookup('role_var', '_paths_location', role='influxdb2') }}/config:/etc/influxdb22"

        # Type: list
        influxdb22_docker_volumes_custom: []

        # Hostname
        # Type: string
        influxdb22_docker_hostname: "{{ influxdb2_name }}"

        # Networks
        # Type: string
        influxdb22_docker_networks_alias: "{{ influxdb2_name }}"

        # Type: list
        influxdb22_docker_networks_default: []

        # Type: list
        influxdb22_docker_networks_custom: []

        # Restart Policy
        # Type: string
        influxdb22_docker_restart_policy: unless-stopped

        # State
        # Type: string
        influxdb22_docker_state: started


        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        influxdb2_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        influxdb2_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        influxdb2_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        influxdb2_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        influxdb2_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        influxdb2_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        influxdb2_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        influxdb2_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        influxdb2_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        influxdb2_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        influxdb2_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            influxdb2_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "influxdb22.{{ user.domain }}"
              - "influxdb2.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            influxdb2_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'influxdb22.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `influxdb22`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        influxdb22_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        influxdb22_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        influxdb22_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        influxdb22_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        influxdb22_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        influxdb22_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        influxdb22_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        influxdb22_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        influxdb22_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        influxdb22_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        influxdb22_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        influxdb22_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        influxdb22_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        influxdb22_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        influxdb22_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        influxdb22_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        influxdb22_web_scheme:

        ```

        1.  Example:

            ```yaml
            influxdb22_web_fqdn_override:
              - "{{ traefik_host }}"
              - "influxdb22.{{ user.domain }}"
              - "influxdb2.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            influxdb22_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'influxdb22.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

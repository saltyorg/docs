---
hide:
  - tags
tags:
  - telegraf
  - monitoring
  - metrics
---

# Telegraf

## What is it?

[Telegraf](https://www.influxdata.com/time-series-platform/telegraf/) is a plugin-driven server agent for collecting and sending metrics and events from databases, systems, and IoT sensors.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.influxdata.com/time-series-platform/telegraf/){: .header-icons } | [:octicons-link-16: Docs](https://docs.influxdata.com/telegraf/v1.20/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/influxdata/telegraf){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/telegraf){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-telegraf

```

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `telegraf_instances`.

    === "Role-level Override"

        Applies to all instances of telegraf:

        ```yaml
        telegraf_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `telegraf2`):

        ```yaml
        telegraf2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        telegraf_instances: ["telegraf"]

        ```

    === "Example"

        ```yaml
        # Type: list
        telegraf_instances: ["telegraf", "telegraf2"]

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        telegraf_role_paths_folder: "telegraf"

        # Type: string
        telegraf_role_paths_location: "{{ server_appdata_path }}/{{ telegraf_role_paths_folder }}"

        # Type: bool (true/false)
        telegraf_role_paths_recursive: true

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        telegraf2_paths_folder: "telegraf"

        # Type: string
        telegraf2_paths_location: "{{ server_appdata_path }}/{{ telegraf_role_paths_folder }}"

        # Type: bool (true/false)
        telegraf2_paths_recursive: true

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        telegraf_role_web_subdomain: "{{ telegraf_name }}"

        # Type: string
        telegraf_role_web_domain: "{{ user.domain }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        telegraf2_web_subdomain: "{{ telegraf_name }}"

        # Type: string
        telegraf2_web_domain: "{{ user.domain }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        telegraf_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='telegraf') }}"

        # Type: string
        telegraf_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='telegraf') }}"

        # Type: bool (true/false)
        telegraf_role_dns_proxy: false

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        telegraf2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='telegraf') }}"

        # Type: string
        telegraf2_dns_zone: "{{ lookup('role_var', '_web_domain', role='telegraf') }}"

        # Type: bool (true/false)
        telegraf2_dns_proxy: false

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        telegraf_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        telegraf_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        telegraf_role_traefik_middleware_custom: ""

        # Type: string
        telegraf_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        telegraf_role_traefik_enabled: true

        # Type: bool (true/false)
        telegraf_role_traefik_api_enabled: false

        # Type: string
        telegraf_role_traefik_api_endpoint: ""

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        telegraf2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        telegraf2_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        telegraf2_traefik_middleware_custom: ""

        # Type: string
        telegraf2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        telegraf2_traefik_enabled: true

        # Type: bool (true/false)
        telegraf2_traefik_api_enabled: false

        # Type: string
        telegraf2_traefik_api_endpoint: ""

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        telegraf_role_docker_container: "{{ telegraf_name }}"

        # Image
        # Type: bool (true/false)
        telegraf_role_docker_image_pull: true

        # Type: string
        telegraf_role_docker_image_repo: "telegraf"

        # Type: string
        telegraf_role_docker_image_tag: "latest"

        # Type: string
        telegraf_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='telegraf') }}:{{ lookup('role_var', '_docker_image_tag', role='telegraf') }}"

        # Envs
        # Type: dict
        telegraf_role_docker_envs_default: 
          TZ: "{{ tz }}"
          EULA: "TRUE"
          UID: "{{ uid }}"
          GID: "{{ gid }}"

        # Type: dict
        telegraf_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        telegraf_role_docker_volumes_default: 
          - "/opt/telegraf/{{ telegraf_name }}:/etc/telegraf:ro"
          - "/var/run/docker.sock:/var/run/docker.sock:ro"
          - "/var/run/utmp:/var/run/utmp"
          - "/:/host:ro"
          - "/sys:/host/sys:ro"
          - "/proc:/host/proc:ro"
          - "/etc:/host/etc:ro"

        # Type: list
        telegraf_role_docker_volumes_custom: []

        # Hostname
        # Type: string
        telegraf_role_docker_hostname: "{{ telegraf_name }}"

        # Networks
        # Type: string
        telegraf_role_docker_networks_alias: "{{ telegraf_name }}"

        # Type: list
        telegraf_role_docker_networks_default: []

        # Type: list
        telegraf_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        telegraf_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        telegraf_role_docker_state: started

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        telegraf2_docker_container: "{{ telegraf_name }}"

        # Image
        # Type: bool (true/false)
        telegraf2_docker_image_pull: true

        # Type: string
        telegraf2_docker_image_repo: "telegraf"

        # Type: string
        telegraf2_docker_image_tag: "latest"

        # Type: string
        telegraf2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='telegraf') }}:{{ lookup('role_var', '_docker_image_tag', role='telegraf') }}"

        # Envs
        # Type: dict
        telegraf2_docker_envs_default: 
          TZ: "{{ tz }}"
          EULA: "TRUE"
          UID: "{{ uid }}"
          GID: "{{ gid }}"

        # Type: dict
        telegraf2_docker_envs_custom: {}

        # Volumes
        # Type: list
        telegraf2_docker_volumes_default: 
          - "/opt/telegraf/{{ telegraf_name }}:/etc/telegraf:ro"
          - "/var/run/docker.sock:/var/run/docker.sock:ro"
          - "/var/run/utmp:/var/run/utmp"
          - "/:/host:ro"
          - "/sys:/host/sys:ro"
          - "/proc:/host/proc:ro"
          - "/etc:/host/etc:ro"

        # Type: list
        telegraf2_docker_volumes_custom: []

        # Hostname
        # Type: string
        telegraf2_docker_hostname: "{{ telegraf_name }}"

        # Networks
        # Type: string
        telegraf2_docker_networks_alias: "{{ telegraf_name }}"

        # Type: list
        telegraf2_docker_networks_default: []

        # Type: list
        telegraf2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        telegraf2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        telegraf2_docker_state: started


        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        telegraf_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        telegraf_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        telegraf_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        telegraf_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        telegraf_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        telegraf_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        telegraf_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        telegraf_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        telegraf_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        telegraf_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        telegraf_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        telegraf_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        telegraf_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        telegraf_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        telegraf_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        telegraf_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        telegraf_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            telegraf_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "telegraf2.{{ user.domain }}"
              - "telegraf.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            telegraf_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'telegraf2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `telegraf2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        telegraf2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        telegraf2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        telegraf2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        telegraf2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        telegraf2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        telegraf2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        telegraf2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        telegraf2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        telegraf2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        telegraf2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        telegraf2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        telegraf2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        telegraf2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        telegraf2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        telegraf2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        telegraf2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        telegraf2_web_scheme:

        ```

        1.  Example:

            ```yaml
            telegraf2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "telegraf2.{{ user.domain }}"
              - "telegraf.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            telegraf2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'telegraf2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
hide:
  - tags
tags:
  - factorio
  - gaming
  - server
---

# Factorio

## What is it?

Run a [Factorio](https://www.factorio.com) headless server.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.factorio.com){: .header-icons } | [:octicons-link-16: Docs](https://wiki.factorio.com/Multiplayer){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/goofball222/factorio){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/goofball222/factorio){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-factorio

```

### 2. Setup

- Set to install the latest Factorio experimental (1.1.x) build. Fix to a certain version using the [inventory system](../../saltbox/inventory/index.md).

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        factorio_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `factorio_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `factorio_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    factorio_name: factorio

    ```

??? example "Paths"

    ```yaml
    # Type: string
    factorio_role_paths_folder: "{{ factorio_name }}"

    # Type: string
    factorio_role_paths_location: "{{ server_appdata_path }}/{{ factorio_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    factorio_role_web_subdomain: "{{ factorio_name }}"

    # Type: string
    factorio_role_web_domain: "{{ user.domain }}"

    # Type: string
    factorio_role_web_port: ""

    ```

??? example "DNS"

    ```yaml
    # Type: string
    factorio_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='factorio') }}"

    # Type: string
    factorio_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='factorio') }}"

    # Type: bool (true/false)
    factorio_role_dns_proxy: false

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    factorio_role_docker_container: "{{ factorio_name }}"

    # Image
    # Type: bool (true/false)
    factorio_role_docker_image_pull: true

    # Type: string
    factorio_role_docker_image_repo: "goofball222/factorio"

    # Type: string
    factorio_role_docker_image_tag: "experimental"

    # Type: string
    factorio_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='factorio') }}:{{ lookup('role_var', '_docker_image_tag', role='factorio') }}"

    # Ports
    # Type: list
    factorio_role_docker_ports_defaults: 
      - "27015:27015/tcp"
      - "34197:34197/udp"

    # Type: list
    factorio_role_docker_ports_custom: []

    # Envs
    # Type: dict
    factorio_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    factorio_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    factorio_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='factorio') }}:/factorio"

    # Type: list
    factorio_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    factorio_role_docker_hostname: "{{ factorio_name }}"

    # Networks
    # Type: string
    factorio_role_docker_networks_alias: "{{ factorio_name }}"

    # Type: list
    factorio_role_docker_networks_default: []

    # Type: list
    factorio_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    factorio_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    factorio_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    factorio_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    factorio_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    factorio_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    factorio_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    factorio_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    factorio_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    factorio_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    factorio_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    factorio_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    factorio_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    factorio_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    factorio_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    factorio_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    factorio_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    factorio_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    factorio_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    factorio_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        factorio_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "factorio2.{{ user.domain }}"
          - "factorio.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        factorio_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'factorio2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
hide:
  - tags
tags:
  - sabthrottle
  - automation
  - bandwidth
---

# SABThrottle

## What is it?

[SABThrottle](https://github.com/8a8al00ey/sabthrottle) Sabthrottle was designed in order to dynamically control the bandwidth allocation when users are actively streaming from Plex to avoid unnecessary buffering while still allowing the user to download at the fastest rate possible. Remember nzbthrottle from daghaian, yes its exactly like that but for SABnzbd with some additional tweaks.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/8a8al00ey/sabthrottle){: .header-icons } | [:octicons-link-16: Docs](https://github.com/8a8al00ey/sabthrottle#installation){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/8a8al00ey/sabthrottle){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/8a8al00ey/sabthrottle){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-sabthrottle

```

### 2. Setup

- See [documentation](https://github.com/8a8al00ey/sabthrottle#installation) for configuration and instructions see the sample configuration and description below it.

  - Running the role will autopopulate plex token and plex url.
  - If you require more then 5 stream count just follow the example and add more using proper yml formatting.
  - You can always check logs via

        ``` shell
        docker logs -f sabthrottle
        ```

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        sabthrottle_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    sabthrottle_name: sabthrottle

    ```

??? example "Paths"

    ```yaml
    # Type: string
    sabthrottle_role_paths_folder: "{{ sabthrottle_name }}"

    # Type: string
    sabthrottle_role_paths_location: "{{ server_appdata_path }}/{{ sabthrottle_role_paths_folder }}"

    # Type: string
    sabthrottle_role_paths_config_location: "{{ sabthrottle_role_paths_location }}/config.json"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    sabthrottle_role_docker_container: "{{ sabthrottle_name }}"

    # Image
    # Type: bool (true/false)
    sabthrottle_role_docker_image_pull: true

    # Type: string
    sabthrottle_role_docker_image_repo: "8a8al00ey/sabthrottle"

    # Type: string
    sabthrottle_role_docker_image_tag: "latest"

    # Type: string
    sabthrottle_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='sabthrottle') }}:{{ lookup('role_var', '_docker_image_tag', role='sabthrottle') }}"

    # Envs
    # Type: dict
    sabthrottle_role_docker_envs_default: 
      TZ: "{{ tz }}"

    # Type: dict
    sabthrottle_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    sabthrottle_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_config_location', role='sabthrottle') }}:/sabthrottle/config.json:ro"

    # Type: list
    sabthrottle_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    sabthrottle_role_docker_hostname: "{{ sabthrottle_name }}"

    # Networks
    # Type: string
    sabthrottle_role_docker_networks_alias: "{{ sabthrottle_name }}"

    # Type: list
    sabthrottle_role_docker_networks_default: []

    # Type: list
    sabthrottle_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    sabthrottle_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    sabthrottle_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    sabthrottle_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    sabthrottle_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    sabthrottle_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    sabthrottle_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    sabthrottle_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    sabthrottle_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    sabthrottle_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    sabthrottle_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    sabthrottle_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    sabthrottle_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    sabthrottle_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    sabthrottle_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    sabthrottle_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    sabthrottle_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    sabthrottle_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    sabthrottle_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    sabthrottle_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        sabthrottle_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "sabthrottle2.{{ user.domain }}"
          - "sabthrottle.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        sabthrottle_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'sabthrottle2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

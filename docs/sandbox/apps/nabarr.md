---
hide:
  - tags
tags:
  - nabarr
  - automation
  - rss
---

# Nabarr

## What is it?

[Nabarr](https://github.com/l3uddz/nabarr) monitors Newznab/Torznab RSS feeds to find new media to add to Sonarr and or Radarr.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-docker: Docker:](https://github.com/l3uddz/nabarr){: .header-icons } | [:octicons-link-16: Docs](https://github.com/l3uddz/nabarr){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/l3uddz/nabarr){: .header-icons } | [:material-docker: Docker:](https://hub.docker.com/r/cloudb0x/nabarr){: .header-icons } |

### 1. Installation

``` shell

sb install sandbox-nabarr

```

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        nabarr_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `nabarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `nabarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    nabarr_name: nabarr

    ```

??? example "Paths"

    ```yaml
    # Type: string
    nabarr_role_paths_folder: "{{ nabarr_name }}"

    # Type: string
    nabarr_role_paths_location: "{{ server_appdata_path }}/{{ nabarr_role_paths_folder }}"

    # Type: string
    nabarr_role_paths_config_location: "{{ nabarr_role_paths_location }}/config.yml"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    nabarr_role_docker_container: "{{ nabarr_name }}"

    # Image
    # Type: bool (true/false)
    nabarr_role_docker_image_pull: true

    # Type: string
    nabarr_role_docker_image_tag: "latest"

    # Type: string
    nabarr_role_docker_image_repo: "saltydk/nabarr"

    # Type: string
    nabarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='nabarr') }}:{{ lookup('role_var', '_docker_image_tag', role='nabarr') }}"

    # Envs
    # Type: dict
    nabarr_role_docker_envs_default: 
      TZ: "{{ tz }}"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      APP_VERBOSITY: "0"

    # Type: dict
    nabarr_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    nabarr_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='nabarr') }}:/config"

    # Type: list
    nabarr_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    nabarr_role_docker_hostname: "{{ nabarr_name }}"

    # Networks
    # Type: string
    nabarr_role_docker_networks_alias: "{{ nabarr_name }}"

    # Type: list
    nabarr_role_docker_networks_default: []

    # Type: list
    nabarr_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    nabarr_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    nabarr_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    nabarr_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    nabarr_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    nabarr_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    nabarr_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    nabarr_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    nabarr_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    nabarr_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    nabarr_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    nabarr_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    nabarr_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    nabarr_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    nabarr_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    nabarr_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    nabarr_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    nabarr_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    nabarr_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    nabarr_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        nabarr_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "nabarr2.{{ user.domain }}"
          - "nabarr.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        nabarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'nabarr2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

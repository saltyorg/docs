---
hide:
  - tags
tags:
  - tauticord
  - discord
  - monitoring
---

# Tauticord

## What is it?

[Tauticord](https://github.com/nwithan8/tauticord) is a Discord bot that
will mirror live Tautulli data into a Discord server, including current stream and bandwidth information, library
statistics, and live playback control.

| Details                                                                                                                         |                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [:material-home: Project home](https://github.com/nwithan8/tauticord){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/nwithan8/tauticord){: .header-icons } |

Recommended install types: Mediabox, Saltbox

### 1. Installation

``` shell
sb install sandbox-tauticord
```

### 2. Setup

Rename `/opt/tauticord/config/config.yml.example` to `/opt/tauticord/config/config.yml` and fill out your configuration details.

See the [Tauticord documentation](https://github.com/nwithan8/tauticord#installation-and-setup) for more information on each setting.

### 3. Usage

Once started, Tauticord will connect to your Tautulli and Discord servers and begin mirroring data.

By default, library statistics are updated once every hour, and stream data is updated once every 15 seconds.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        tauticord_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    tauticord_name: tauticord

    ```

??? example "Paths"

    ```yaml
    # Type: string
    tauticord_role_paths_folder: "{{ tauticord_name }}"

    # Type: string
    tauticord_role_paths_location: "{{ server_appdata_path }}/{{ tauticord_role_paths_folder }}"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    tauticord_role_docker_container: "{{ tauticord_name }}"

    # Image
    # Type: bool (true/false)
    tauticord_role_docker_image_pull: true

    # Type: string
    tauticord_role_docker_image_repo: "nwithan8/tauticord"

    # Type: string
    tauticord_role_docker_image_tag: "latest"

    # Type: string
    tauticord_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='tauticord') }}:{{ lookup('role_var', '_docker_image_tag', role='tauticord') }}"

    # Envs
    # Type: dict
    tauticord_role_docker_envs_default: 
      TZ: "{{ tz }}"
      USER_ID: "{{ uid }}"
      GROUP_ID: "{{ gid }}"
      UMASK: "022"

    # Type: dict
    tauticord_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    tauticord_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='tauticord') }}/config:/config"
      - "{{ lookup('role_var', '_paths_location', role='tauticord') }}/logs:/logs"

    # Type: list
    tauticord_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    tauticord_role_docker_hostname: "{{ tauticord_name }}"

    # Networks
    # Type: string
    tauticord_role_docker_networks_alias: "{{ tauticord_name }}"

    # Type: list
    tauticord_role_docker_networks_default: []

    # Type: list
    tauticord_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    tauticord_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    tauticord_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    tauticord_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    tauticord_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    tauticord_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    tauticord_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    tauticord_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    tauticord_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    tauticord_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    tauticord_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    tauticord_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    tauticord_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    tauticord_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    tauticord_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    tauticord_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    tauticord_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    tauticord_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    tauticord_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    tauticord_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        tauticord_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "tauticord2.{{ user.domain }}"
          - "tauticord.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        tauticord_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'tauticord2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

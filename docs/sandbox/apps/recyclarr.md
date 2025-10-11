---
hide:
  - tags
tags:
  - recyclarr
  - sonarr
  - radarr
---

# Recyclarr

## What is it?

[Recyclarr](https://github.com/recyclarr/recyclarr) automatically synchronizes recommended settings from TRaSH guides to your Sonarr/Radarr instances.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/recyclarr/recyclarr){: .header-icons } | [:octicons-link-16: Docs](https://recyclarr.dev/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/recyclarr/recyclarr){: .header-icons } | [:material-docker: Docker](https://ghcr.io/recyclarr/recyclarr){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-recyclarr

```

### 2. Setup

Edit the Recyclarr section in [sandbox `settings.yml`:](../settings.md) and enter your desired update schedule using standard cron syntax.

``` { .yaml }
     recyclarr:
       cron_schedule: "@daily"
```

!!! note
    If you change this value, you must re-run `sb install sandbox-recyclarr` for it take effect.

If a config file does not exist, a default config is generated but it is not functional out of the box. Edit the file `/opt/recyclarr/recyclarr.yml` to provision your Sonarr/Radarr details and preferred settings.

- Configure Sonarr section

  ``` { .yaml }
      sonarr:
        sonarr:
          base_url: http://sonarr:8989
          api_key: your_sonarr_api_key
  ```

- Configure Radarr section

  ``` { .yaml }
      radarr:
        radarr:
          base_url: http://radarr:7878
          api_key: your_radarr_api_key
  ```

Follow documentation to complete configuration

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        recyclarr_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    recyclarr_name: recyclarr

    ```

??? example "Paths"

    ```yaml
    # Type: string
    recyclarr_role_paths_folder: "{{ recyclarr_name }}"

    # Type: string
    recyclarr_role_paths_location: "{{ server_appdata_path }}/{{ recyclarr_role_paths_folder }}"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    recyclarr_role_docker_container: "{{ recyclarr_name }}"

    # Image
    # Type: bool (true/false)
    recyclarr_role_docker_image_pull: true

    # Type: string
    recyclarr_role_docker_image_repo: "ghcr.io/recyclarr/recyclarr"

    # Type: string
    recyclarr_role_docker_image_tag: "latest"

    # Type: string
    recyclarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='recyclarr') }}:{{ lookup('role_var', '_docker_image_tag', role='recyclarr') }}"

    # Envs
    # Type: dict
    recyclarr_role_docker_envs_default: 
      TZ: "{{ tz }}"
      CRON_SCHEDULE: "{{ recyclarr.cron_schedule }}"
      RECYCLARR_CREATE_CONFIG: "true"

    # Type: dict
    recyclarr_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    recyclarr_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='recyclarr') }}:/config"

    # Type: list
    recyclarr_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    recyclarr_role_docker_hostname: "{{ recyclarr_name }}"

    # Networks
    # Type: string
    recyclarr_role_docker_networks_alias: "{{ recyclarr_name }}"

    # Type: list
    recyclarr_role_docker_networks_default: []

    # Type: list
    recyclarr_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    recyclarr_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    recyclarr_role_docker_state: started

    # User
    # Type: string
    recyclarr_role_docker_user: "{{ uid }}:{{ gid }}"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    recyclarr_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    recyclarr_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    recyclarr_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    recyclarr_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    recyclarr_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    recyclarr_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    recyclarr_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    recyclarr_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    recyclarr_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    recyclarr_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    recyclarr_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    recyclarr_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    recyclarr_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    recyclarr_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    recyclarr_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    recyclarr_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    recyclarr_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        recyclarr_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "recyclarr2.{{ user.domain }}"
          - "recyclarr.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        recyclarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'recyclarr2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

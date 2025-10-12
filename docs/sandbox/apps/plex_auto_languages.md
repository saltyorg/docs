---
hide:
  - tags
tags:
  - plex-auto-languages
  - plex
  - automation
---

# plex_auto_languages

## What is it?

[plex_auto_languages](https://github.com/RemiRigal/Plex-Auto-Languages) auto-updates the language of your Plex TV Show episodes based on the current language you are using without messing with your existing language preferences.

You

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/RemiRigal/Plex-Auto-Languages){: .header-icons } | [:octicons-link-16: Docs](https://github.com/RemiRigal/Plex-Auto-Languages){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/RemiRigal/Plex-Auto-Languages){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/remirigal/plex-auto-languages){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-plex-auto-languages

```

### 2. URL

PLex-auto-languages has no UI; it is driven by a config file

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        plex_auto_languages_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `plex_auto_languages_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `plex_auto_languages_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    plex_auto_languages_name: plex-auto-languages

    ```

??? example "Paths"

    ```yaml
    # Type: string
    plex_auto_languages_role_paths_folder: "{{ plex_auto_languages_name }}"

    # Type: string
    plex_auto_languages_role_paths_location: "{{ server_appdata_path }}/{{ plex_auto_languages_role_paths_folder }}"

    # Type: string
    plex_auto_languages_role_paths_config_location: "{{ plex_auto_languages_role_paths_location }}/config.yaml"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    plex_auto_languages_role_docker_container: "{{ plex_auto_languages_name }}"

    # Image
    # Type: string
    plex_auto_languages_role_docker_image_tag: "latest"

    # Type: string
    plex_auto_languages_role_docker_image_repo: "journeyover/plex-auto-languages"

    # Type: string
    plex_auto_languages_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='plex_auto_languages') }}:{{ lookup('role_var', '_docker_image_tag', role='plex_auto_languages') }}"

    # Type: bool (true/false)
    plex_auto_languages_role_docker_image_pull: true

    # Envs
    # Type: dict
    plex_auto_languages_role_docker_envs_default: 
      TZ: "{{ tz }}"

    # Type: dict
    plex_auto_languages_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    plex_auto_languages_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='plex_auto_languages') }}:/config"

    # Type: list
    plex_auto_languages_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    plex_auto_languages_role_docker_hostname: "{{ plex_auto_languages_name }}"

    # Networks
    # Type: string
    plex_auto_languages_role_docker_networks_alias: "{{ plex_auto_languages_name }}"

    # Type: list
    plex_auto_languages_role_docker_networks_default: []

    # Type: list
    plex_auto_languages_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    plex_auto_languages_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    plex_auto_languages_role_docker_state: started

    # Stop Timeout
    # Type: int
    plex_auto_languages_role_docker_stop_timeout: 10

    # User
    # Type: string
    plex_auto_languages_role_docker_user: "{{ uid }}:{{ gid }}"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    plex_auto_languages_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    plex_auto_languages_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    plex_auto_languages_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    plex_auto_languages_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    plex_auto_languages_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    plex_auto_languages_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    plex_auto_languages_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    plex_auto_languages_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    plex_auto_languages_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    plex_auto_languages_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    plex_auto_languages_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    plex_auto_languages_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    plex_auto_languages_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    plex_auto_languages_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    plex_auto_languages_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    plex_auto_languages_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    plex_auto_languages_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        plex_auto_languages_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "plex_auto_languages2.{{ user.domain }}"
          - "plex_auto_languages.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        plex_auto_languages_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'plex_auto_languages2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

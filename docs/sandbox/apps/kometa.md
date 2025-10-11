---
hide:
  - tags
tags:
  - kometa
  - pmm
  - plex meta manager
---

# Kometa

## What is it?

[Kometa](https://github.com/Kometa-Team/Kometa) can update many metadata fields for movies, shows, collections, seasons, and episodes and can act as a backup if your plex DB goes down. It can even update metadata the plex UI can't like Season Names. If the time is put into the metadata configuration file you can have a way to recreate your library and all its metadata changes with the click of a button.

!!! info
    Kometa is the replacement for Plex Meta Manager. A simple migration for your appdata is available by running `sb install sandbox-pmm-kometa-migration`.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/Kometa-Team/Kometa){: .header-icons } | [:octicons-link-16: Docs](https://kometa.wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Kometa-Team/Kometa){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/kometateam/kometa){: .header-icons }|

### 1. Installation

You will need to create a config file prior to running the tag:

`/opt/kometa/config.yml`

There is a Docker-based walkthrough on the Kometa wiki [here](https://kometa.wiki/en/latest/kometa/install/docker/) that you can use to learn how to create this file.  Once you've created it, move the file into `/opt/kometa/` and then run the tag.

``` shell
sb install sandbox-kometa
```

### 2. Setup

To configure the time that Kometa should run, you may override the `kometa_time` variable via the [inventory system](../../saltbox/inventory/index.md). The default is `"03:00"` or 3:00 AM in the server's time zone.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `kometa_instances`.

    === "Role-level Override"

        Applies to all instances of kometa:

        ```yaml
        kometa_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `kometa2`):

        ```yaml
        kometa2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        kometa_instances: ["kometa"]

        ```

    === "Example"

        ```yaml
        # Type: list
        kometa_instances: ["kometa", "kometa2"]

        ```

??? example "Settings"

    === "Role-level"

        ```yaml
        # Type: string
        kometa_role_time: "03:00"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        kometa2_time: "03:00"

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        kometa_role_paths_folder: "{{ kometa_name }}"

        # Type: string
        kometa_role_paths_location: "{{ server_appdata_path }}/{{ kometa_role_paths_folder }}"

        # Type: bool (true/false)
        kometa_role_paths_recursive: true

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        kometa2_paths_folder: "{{ kometa_name }}"

        # Type: string
        kometa2_paths_location: "{{ server_appdata_path }}/{{ kometa_role_paths_folder }}"

        # Type: bool (true/false)
        kometa2_paths_recursive: true

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        kometa_role_docker_container: "{{ kometa_name }}"

        # Image
        # Type: bool (true/false)
        kometa_role_docker_image_pull: true

        # Type: string
        kometa_role_docker_image_repo: "kometateam/kometa"

        # Type: string
        kometa_role_docker_image_tag: "latest"

        # Type: string
        kometa_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='kometa') }}:{{ lookup('role_var', '_docker_image_tag', role='kometa') }}"

        # Envs
        # Type: dict
        kometa_role_docker_envs_default: 
          TZ: "{{ tz }}"
          LOG_LEVEL: "DEBUG"
          KOMETA_TIMES: "{{ lookup('role_var', '_time', role='kometa') }}"

        # Type: dict
        kometa_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        kometa_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='kometa') }}:/config"

        # Type: list
        kometa_role_docker_volumes_custom: []

        # Hostname
        # Type: string
        kometa_role_docker_hostname: "{{ kometa_name }}"

        # Networks
        # Type: string
        kometa_role_docker_networks_alias: "{{ kometa_name }}"

        # Type: list
        kometa_role_docker_networks_default: []

        # Type: list
        kometa_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        kometa_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        kometa_role_docker_state: started

        # User
        # Type: string
        kometa_role_docker_user: "{{ uid }}:{{ gid }}"

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        kometa2_docker_container: "{{ kometa_name }}"

        # Image
        # Type: bool (true/false)
        kometa2_docker_image_pull: true

        # Type: string
        kometa2_docker_image_repo: "kometateam/kometa"

        # Type: string
        kometa2_docker_image_tag: "latest"

        # Type: string
        kometa2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='kometa') }}:{{ lookup('role_var', '_docker_image_tag', role='kometa') }}"

        # Envs
        # Type: dict
        kometa2_docker_envs_default: 
          TZ: "{{ tz }}"
          LOG_LEVEL: "DEBUG"
          KOMETA_TIMES: "{{ lookup('role_var', '_time', role='kometa') }}"

        # Type: dict
        kometa2_docker_envs_custom: {}

        # Volumes
        # Type: list
        kometa2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='kometa') }}:/config"

        # Type: list
        kometa2_docker_volumes_custom: []

        # Hostname
        # Type: string
        kometa2_docker_hostname: "{{ kometa_name }}"

        # Networks
        # Type: string
        kometa2_docker_networks_alias: "{{ kometa_name }}"

        # Type: list
        kometa2_docker_networks_default: []

        # Type: list
        kometa2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        kometa2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        kometa2_docker_state: started

        # User
        # Type: string
        kometa2_docker_user: "{{ uid }}:{{ gid }}"


        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        kometa_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        kometa_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        kometa_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        kometa_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        kometa_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        kometa_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        kometa_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        kometa_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        kometa_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        kometa_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        kometa_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        kometa_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        kometa_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        kometa_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        kometa_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        kometa_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        kometa_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            kometa_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "kometa2.{{ user.domain }}"
              - "kometa.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            kometa_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'kometa2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `kometa2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        kometa2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        kometa2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        kometa2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        kometa2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        kometa2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        kometa2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        kometa2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        kometa2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        kometa2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        kometa2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        kometa2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        kometa2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        kometa2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        kometa2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        kometa2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        kometa2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        kometa2_web_scheme:

        ```

        1.  Example:

            ```yaml
            kometa2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "kometa2.{{ user.domain }}"
              - "kometa.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            kometa2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'kometa2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

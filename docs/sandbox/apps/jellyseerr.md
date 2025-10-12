---
hide:
  - tags
tags:
  - jellyseerr
  - media
  - requests
---

# Jellyseerr

## What is it?

[Jellyseerr](https://docs.jellyseerr.dev/) is a free and open source software application for managing requests for your media library. It integrates with the media server of your choice: Jellyfin, Plex, and Emby. In addition, it integrates with your existing services, such as Sonarr, Radarr.

- Full Jellyfin/Emby/Plex integration including authentication with user import & management.
- Support for PostgreSQL and SQLite databases.
- Supports Movies, Shows and Mixed Libraries.
- Ability to change email addresses for SMTP purposes.
- Easy integration with your existing services. Currently, Jellyseerr supports Sonarr and Radarr. More to come!
- Jellyfin/Emby/Plex library scan, to keep track of the titles which are already available.
- Customizable request system, which allows users to request individual seasons or movies in a friendly, easy-to-use interface.
- Simple request management UI. Don't dig through the app to simply approve recent requests!
- Granular permission system.
- Support for various notification agents.
- Mobile-friendly design, for when you need to approve requests on the go!
- Support for watchlisting & blacklisting media.

!!! info
    By default, the role is **NOT** protected behind your Authelia/SSO middleware. You will have to log in with Plex, Jellyfin, etc. Make the appropriate changes via inventory to add SSO.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://docs.jellyseerr.dev/){: .header-icons } | [:octicons-link-16: Docs](https://docs.jellyseerr.dev/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/ajnart/Jellyseer){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/fallenbagel/jellyseerr){: .header-icons }|

Recommended install types: Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-jellyseerr

```

### 2. URL

- To access Jellyseerr, visit `https://jellyseerr._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `jellyseerr_instances`.

    === "Role-level Override"

        Applies to all instances of jellyseerr:

        ```yaml
        jellyseerr_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `jellyseerr2`):

        ```yaml
        jellyseerr2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `jellyseerr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `jellyseerr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        jellyseerr_instances: ["jellyseerr"]

        ```

    === "Example"

        ```yaml
        # Type: list
        jellyseerr_instances: ["jellyseerr", "jellyseerr2"]

        ```

??? example "Settings"

    === "Role-level"

        ```yaml
        # Type: string
        jellyseerr_role_log_level: "INFO"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        jellyseerr2_log_level: "INFO"

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        jellyseerr_role_paths_folder: "{{ jellyseerr_name }}"

        # Type: string
        jellyseerr_role_paths_location: "{{ server_appdata_path }}/{{ jellyseerr_role_paths_folder }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        jellyseerr2_paths_folder: "{{ jellyseerr_name }}"

        # Type: string
        jellyseerr2_paths_location: "{{ server_appdata_path }}/{{ jellyseerr_role_paths_folder }}"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        jellyseerr_role_web_subdomain: "{{ jellyseerr_name }}"

        # Type: string
        jellyseerr_role_web_domain: "{{ user.domain }}"

        # Type: string
        jellyseerr_role_web_port: "5055"

        # Type: string
        jellyseerr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='jellyseerr') + '.' + lookup('role_var', '_web_domain', role='jellyseerr')
                                  if (lookup('role_var', '_web_subdomain', role='jellyseerr') | length > 0)
                                  else lookup('role_var', '_web_domain', role='jellyseerr')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        jellyseerr2_web_subdomain: "{{ jellyseerr_name }}"

        # Type: string
        jellyseerr2_web_domain: "{{ user.domain }}"

        # Type: string
        jellyseerr2_web_port: "5055"

        # Type: string
        jellyseerr2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='jellyseerr') + '.' + lookup('role_var', '_web_domain', role='jellyseerr')
                              if (lookup('role_var', '_web_subdomain', role='jellyseerr') | length > 0)
                              else lookup('role_var', '_web_domain', role='jellyseerr')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        jellyseerr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='jellyseerr') }}"

        # Type: string
        jellyseerr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='jellyseerr') }}"

        # Type: bool (true/false)
        jellyseerr_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        jellyseerr2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='jellyseerr') }}"

        # Type: string
        jellyseerr2_dns_zone: "{{ lookup('role_var', '_web_domain', role='jellyseerr') }}"

        # Type: bool (true/false)
        jellyseerr2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        jellyseerr_role_traefik_sso_middleware: ""

        # Type: string
        jellyseerr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        jellyseerr_role_traefik_middleware_custom: ""

        # Type: string
        jellyseerr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        jellyseerr_role_traefik_enabled: true

        # Type: bool (true/false)
        jellyseerr_role_traefik_api_enabled: false

        # Type: string
        jellyseerr_role_traefik_api_endpoint: ""

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        jellyseerr2_traefik_sso_middleware: ""

        # Type: string
        jellyseerr2_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        jellyseerr2_traefik_middleware_custom: ""

        # Type: string
        jellyseerr2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        jellyseerr2_traefik_enabled: true

        # Type: bool (true/false)
        jellyseerr2_traefik_api_enabled: false

        # Type: string
        jellyseerr2_traefik_api_endpoint: ""

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        jellyseerr_role_docker_container: "{{ jellyseerr_name }}"

        # Image
        # Type: bool (true/false)
        jellyseerr_role_docker_image_pull: true

        # Type: string
        jellyseerr_role_docker_image_repo: "fallenbagel/jellyseerr"

        # Type: string
        jellyseerr_role_docker_image_tag: "latest"

        # Type: string
        jellyseerr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='jellyseerr') }}:{{ lookup('role_var', '_docker_image_tag', role='jellyseerr') }}"

        # Envs
        # Type: dict
        jellyseerr_role_docker_envs_default: 
          UMASK: "002"
          TZ: "{{ tz }}"
          LOG_LEVEL: "{{ lookup('role_var', '_log_level', role='jellyseerr') }}"

        # Type: dict
        jellyseerr_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        jellyseerr_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='jellyseerr') }}:/app/config"

        # Type: list
        jellyseerr_role_docker_volumes_custom: []

        # Hostname
        # Type: string
        jellyseerr_role_docker_hostname: "{{ jellyseerr_name }}"

        # Networks
        # Type: string
        jellyseerr_role_docker_networks_alias: "{{ jellyseerr_name }}"

        # Type: list
        jellyseerr_role_docker_networks_default: []

        # Type: list
        jellyseerr_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        jellyseerr_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        jellyseerr_role_docker_state: started

        # User
        # Type: string
        jellyseerr_role_docker_user: "{{ uid }}:{{ gid }}"

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        jellyseerr2_docker_container: "{{ jellyseerr_name }}"

        # Image
        # Type: bool (true/false)
        jellyseerr2_docker_image_pull: true

        # Type: string
        jellyseerr2_docker_image_repo: "fallenbagel/jellyseerr"

        # Type: string
        jellyseerr2_docker_image_tag: "latest"

        # Type: string
        jellyseerr2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='jellyseerr') }}:{{ lookup('role_var', '_docker_image_tag', role='jellyseerr') }}"

        # Envs
        # Type: dict
        jellyseerr2_docker_envs_default: 
          UMASK: "002"
          TZ: "{{ tz }}"
          LOG_LEVEL: "{{ lookup('role_var', '_log_level', role='jellyseerr') }}"

        # Type: dict
        jellyseerr2_docker_envs_custom: {}

        # Volumes
        # Type: list
        jellyseerr2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='jellyseerr') }}:/app/config"

        # Type: list
        jellyseerr2_docker_volumes_custom: []

        # Hostname
        # Type: string
        jellyseerr2_docker_hostname: "{{ jellyseerr_name }}"

        # Networks
        # Type: string
        jellyseerr2_docker_networks_alias: "{{ jellyseerr_name }}"

        # Type: list
        jellyseerr2_docker_networks_default: []

        # Type: list
        jellyseerr2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        jellyseerr2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        jellyseerr2_docker_state: started

        # User
        # Type: string
        jellyseerr2_docker_user: "{{ uid }}:{{ gid }}"


        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        jellyseerr_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        jellyseerr_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        jellyseerr_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        jellyseerr_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        jellyseerr_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        jellyseerr_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        jellyseerr_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        jellyseerr_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        jellyseerr_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        jellyseerr_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        jellyseerr_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        jellyseerr_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        jellyseerr_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        jellyseerr_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        jellyseerr_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        jellyseerr_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        jellyseerr_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            jellyseerr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "jellyseerr2.{{ user.domain }}"
              - "jellyseerr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            jellyseerr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'jellyseerr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `jellyseerr2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        jellyseerr2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        jellyseerr2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        jellyseerr2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        jellyseerr2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        jellyseerr2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        jellyseerr2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        jellyseerr2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        jellyseerr2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        jellyseerr2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        jellyseerr2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        jellyseerr2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        jellyseerr2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        jellyseerr2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        jellyseerr2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        jellyseerr2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        jellyseerr2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        jellyseerr2_web_scheme:

        ```

        1.  Example:

            ```yaml
            jellyseerr2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "jellyseerr2.{{ user.domain }}"
              - "jellyseerr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            jellyseerr2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'jellyseerr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

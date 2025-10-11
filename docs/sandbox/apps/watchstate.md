---
hide:
  - tags
tags:
  - watchstate
  - emby
  - jellyfin
  - plex
---

# WatchState

This tool's primary goal is to sync your backends' play states without relying on third party services. Out of the box, it supports Jellyfin, Plex and Emby media servers.

<div class="grid sb-buttons" markdown data-search-exclude>

[:material-home: Homepage&nbsp;&nbsp;](https://github.com/arabcoders/watchstate){ .md-button .md-button--stretch }

[:material-bookshelf: Manual&nbsp;&nbsp;](https://github.com/ArabCoders/watchstate/blob/master/FAQ.md){ .md-button .md-button--stretch }

[:octicons-container-16: Releases&nbsp;&nbsp;](https://github.com/arabcoders/watchstate/pkgs/container/watchstate){ .md-button .md-button--stretch }

[:fontawesome-brands-discord: Community&nbsp;&nbsp;](https://discord.gg/haUXHJyj6Y){ .md-button .md-button--stretch }

</div>

---

## Deployment

``` shell
sb install sandbox-watchstate
```

## Usage

Visit `https://watchstate._yourdomain.com_`.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `watchstate_instances`.

    === "Role-level Override"

        Applies to all instances of watchstate:

        ```yaml
        watchstate_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `watchstate2`):

        ```yaml
        watchstate2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        watchstate_instances: ["watchstate"]

        ```

    === "Example"

        ```yaml
        # Type: list
        watchstate_instances: ["watchstate", "watchstate2"]

        ```

??? example "Settings"

    === "Role-level"

        ```yaml
        # Type: bool (true/false)
        watchstate_role_api_auto: true

        # Type: bool (true/false)
        watchstate_role_trust_proxy: true

        # Type: bool (true/false)
        watchstate_role_secure_api_endpoints: true

        ```

    === "Instance-level"

        ```yaml
        # Type: bool (true/false)
        watchstate2_api_auto: true

        # Type: bool (true/false)
        watchstate2_trust_proxy: true

        # Type: bool (true/false)
        watchstate2_secure_api_endpoints: true

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        watchstate_role_paths_folder: "{{ watchstate_name }}"

        # Type: string
        watchstate_role_paths_location: "{{ server_appdata_path }}/{{ watchstate_role_paths_folder }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        watchstate2_paths_folder: "{{ watchstate_name }}"

        # Type: string
        watchstate2_paths_location: "{{ server_appdata_path }}/{{ watchstate_role_paths_folder }}"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        watchstate_role_web_subdomain: "{{ watchstate_name }}"

        # Type: string
        watchstate_role_web_domain: "{{ user.domain }}"

        # Type: string
        watchstate_role_web_port: "8080"

        # Type: string
        watchstate_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='watchstate') + '.' + lookup('role_var', '_web_domain', role='watchstate')
                                  if (lookup('role_var', '_web_subdomain', role='watchstate') | length > 0)
                                  else lookup('role_var', '_web_domain', role='watchstate')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        watchstate2_web_subdomain: "{{ watchstate_name }}"

        # Type: string
        watchstate2_web_domain: "{{ user.domain }}"

        # Type: string
        watchstate2_web_port: "8080"

        # Type: string
        watchstate2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='watchstate') + '.' + lookup('role_var', '_web_domain', role='watchstate')
                              if (lookup('role_var', '_web_subdomain', role='watchstate') | length > 0)
                              else lookup('role_var', '_web_domain', role='watchstate')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        watchstate_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='watchstate') }}"

        # Type: string
        watchstate_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='watchstate') }}"

        # Type: bool (true/false)
        watchstate_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        watchstate2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='watchstate') }}"

        # Type: string
        watchstate2_dns_zone: "{{ lookup('role_var', '_web_domain', role='watchstate') }}"

        # Type: bool (true/false)
        watchstate2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        watchstate_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        watchstate_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        watchstate_role_traefik_middleware_custom: ""

        # Type: string
        watchstate_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        watchstate_role_traefik_enabled: true

        # Type: bool (true/false)
        watchstate_role_traefik_api_enabled: true

        # Type: string
        watchstate_role_traefik_api_endpoint: "PathRegexp(`backend/[^/]+/webhook`)"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        watchstate2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        watchstate2_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        watchstate2_traefik_middleware_custom: ""

        # Type: string
        watchstate2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        watchstate2_traefik_enabled: true

        # Type: bool (true/false)
        watchstate2_traefik_api_enabled: true

        # Type: string
        watchstate2_traefik_api_endpoint: "PathRegexp(`backend/[^/]+/webhook`)"

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        watchstate_role_docker_container: "{{ watchstate_name }}"

        # Image
        # Type: bool (true/false)
        watchstate_role_docker_image_pull: true

        # Type: string
        watchstate_role_docker_image_repo: "ghcr.io/arabcoders/watchstate"

        # Type: string
        watchstate_role_docker_image_tag: "latest"

        # Type: string
        watchstate_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='watchstate') }}:{{ lookup('role_var', '_docker_image_tag', role='watchstate') }}"

        # Envs
        # Type: dict
        watchstate_role_docker_envs_default: 
          WS_TZ: "{{ tz }}"
          WS_API_AUTO: "{{ 'true'
                        if lookup('role_var', '_api_auto', role='watchstate')
                        else omit }}"
          WS_TRUST_PROXY: "{{ 'true'
                           if lookup('role_var', '_trust_proxy', role='watchstate')
                           else omit }}"
          WS_SECURE_API_ENDPOINTS: "{{ 'true'
                                    if lookup('role_var', '_secure_api_endpoints', role='watchstate')
                                    else omit }}"

        # Type: dict
        watchstate_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        watchstate_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='watchstate') }}:/config"

        # Type: list
        watchstate_role_docker_volumes_custom: []

        # Hostname
        # Type: string
        watchstate_role_docker_hostname: "{{ watchstate_name }}"

        # Networks
        # Type: string
        watchstate_role_docker_networks_alias: "{{ watchstate_name }}"

        # Type: list
        watchstate_role_docker_networks_default: []

        # Type: list
        watchstate_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        watchstate_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        watchstate_role_docker_state: started

        # User
        # Type: string
        watchstate_role_docker_user: "{{ uid }}:{{ gid }}"

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        watchstate2_docker_container: "{{ watchstate_name }}"

        # Image
        # Type: bool (true/false)
        watchstate2_docker_image_pull: true

        # Type: string
        watchstate2_docker_image_repo: "ghcr.io/arabcoders/watchstate"

        # Type: string
        watchstate2_docker_image_tag: "latest"

        # Type: string
        watchstate2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='watchstate') }}:{{ lookup('role_var', '_docker_image_tag', role='watchstate') }}"

        # Envs
        # Type: dict
        watchstate2_docker_envs_default: 
          WS_TZ: "{{ tz }}"
          WS_API_AUTO: "{{ 'true'
                        if lookup('role_var', '_api_auto', role='watchstate')
                        else omit }}"
          WS_TRUST_PROXY: "{{ 'true'
                           if lookup('role_var', '_trust_proxy', role='watchstate')
                           else omit }}"
          WS_SECURE_API_ENDPOINTS: "{{ 'true'
                                    if lookup('role_var', '_secure_api_endpoints', role='watchstate')
                                    else omit }}"

        # Type: dict
        watchstate2_docker_envs_custom: {}

        # Volumes
        # Type: list
        watchstate2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='watchstate') }}:/config"

        # Type: list
        watchstate2_docker_volumes_custom: []

        # Hostname
        # Type: string
        watchstate2_docker_hostname: "{{ watchstate_name }}"

        # Networks
        # Type: string
        watchstate2_docker_networks_alias: "{{ watchstate_name }}"

        # Type: list
        watchstate2_docker_networks_default: []

        # Type: list
        watchstate2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        watchstate2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        watchstate2_docker_state: started

        # User
        # Type: string
        watchstate2_docker_user: "{{ uid }}:{{ gid }}"


        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        watchstate_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        watchstate_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        watchstate_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        watchstate_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        watchstate_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        watchstate_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        watchstate_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        watchstate_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        watchstate_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        watchstate_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        watchstate_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        watchstate_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        watchstate_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        watchstate_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        watchstate_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        watchstate_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        watchstate_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            watchstate_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "watchstate2.{{ user.domain }}"
              - "watchstate.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            watchstate_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'watchstate2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `watchstate2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        watchstate2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        watchstate2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        watchstate2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        watchstate2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        watchstate2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        watchstate2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        watchstate2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        watchstate2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        watchstate2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        watchstate2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        watchstate2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        watchstate2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        watchstate2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        watchstate2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        watchstate2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        watchstate2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        watchstate2_web_scheme:

        ```

        1.  Example:

            ```yaml
            watchstate2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "watchstate2.{{ user.domain }}"
              - "watchstate.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            watchstate2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'watchstate2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

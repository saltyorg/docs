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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

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

=== "Basics"

    ??? variable list "`jellyseerr_instances`"

        ```yaml
        # Type: list
        jellyseerr_instances: ["jellyseerr"]
        ```

        !!! example

            ```yaml
            # Type: list
            jellyseerr_instances: ["jellyseerr", "jellyseerr2"]
            ```

=== "Settings"

    === "Role-level"

        ??? variable string "`jellyseerr_role_log_level`"

            ```yaml
            # Type: string
            jellyseerr_role_log_level: "INFO"
            ```

    === "Instance-level"

        ??? variable string "`jellyseerr2_log_level`"

            ```yaml
            # Type: string
            jellyseerr2_log_level: "INFO"
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`jellyseerr_role_paths_folder`"

            ```yaml
            # Type: string
            jellyseerr_role_paths_folder: "{{ jellyseerr_name }}"
            ```

        ??? variable string "`jellyseerr_role_paths_location`"

            ```yaml
            # Type: string
            jellyseerr_role_paths_location: "{{ server_appdata_path }}/{{ jellyseerr_role_paths_folder }}"
            ```

    === "Instance-level"

        ??? variable string "`jellyseerr2_paths_folder`"

            ```yaml
            # Type: string
            jellyseerr2_paths_folder: "{{ jellyseerr_name }}"
            ```

        ??? variable string "`jellyseerr2_paths_location`"

            ```yaml
            # Type: string
            jellyseerr2_paths_location: "{{ server_appdata_path }}/{{ jellyseerr_role_paths_folder }}"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`jellyseerr_role_web_subdomain`"

            ```yaml
            # Type: string
            jellyseerr_role_web_subdomain: "{{ jellyseerr_name }}"
            ```

        ??? variable string "`jellyseerr_role_web_domain`"

            ```yaml
            # Type: string
            jellyseerr_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`jellyseerr_role_web_port`"

            ```yaml
            # Type: string
            jellyseerr_role_web_port: "5055"
            ```

        ??? variable string "`jellyseerr_role_web_url`"

            ```yaml
            # Type: string
            jellyseerr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='jellyseerr') + '.' + lookup('role_var', '_web_domain', role='jellyseerr')
                                      if (lookup('role_var', '_web_subdomain', role='jellyseerr') | length > 0)
                                      else lookup('role_var', '_web_domain', role='jellyseerr')) }}"
            ```

    === "Instance-level"

        ??? variable string "`jellyseerr2_web_subdomain`"

            ```yaml
            # Type: string
            jellyseerr2_web_subdomain: "{{ jellyseerr_name }}"
            ```

        ??? variable string "`jellyseerr2_web_domain`"

            ```yaml
            # Type: string
            jellyseerr2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`jellyseerr2_web_port`"

            ```yaml
            # Type: string
            jellyseerr2_web_port: "5055"
            ```

        ??? variable string "`jellyseerr2_web_url`"

            ```yaml
            # Type: string
                    jellyseerr2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='jellyseerr') + '.' + lookup('role_var', '_web_domain', role='jellyseerr')
                                          if (lookup('role_var', '_web_subdomain', role='jellyseerr') | length > 0)
                                          else lookup('role_var', '_web_domain', role='jellyseerr')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`jellyseerr_role_dns_record`"

            ```yaml
            # Type: string
            jellyseerr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='jellyseerr') }}"
            ```

        ??? variable string "`jellyseerr_role_dns_zone`"

            ```yaml
            # Type: string
            jellyseerr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='jellyseerr') }}"
            ```

        ??? variable bool "`jellyseerr_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            jellyseerr_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`jellyseerr2_dns_record`"

            ```yaml
            # Type: string
            jellyseerr2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='jellyseerr') }}"
            ```

        ??? variable string "`jellyseerr2_dns_zone`"

            ```yaml
            # Type: string
            jellyseerr2_dns_zone: "{{ lookup('role_var', '_web_domain', role='jellyseerr') }}"
            ```

        ??? variable bool "`jellyseerr2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            jellyseerr2_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`jellyseerr_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            jellyseerr_role_traefik_sso_middleware: ""
            ```

        ??? variable string "`jellyseerr_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            jellyseerr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`jellyseerr_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            jellyseerr_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`jellyseerr_role_traefik_certresolver`"

            ```yaml
            # Type: string
            jellyseerr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`jellyseerr_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            jellyseerr_role_traefik_enabled: true
            ```

        ??? variable bool "`jellyseerr_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            jellyseerr_role_traefik_api_enabled: false
            ```

        ??? variable string "`jellyseerr_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            jellyseerr_role_traefik_api_endpoint: ""
            ```

    === "Instance-level"

        ??? variable string "`jellyseerr2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            jellyseerr2_traefik_sso_middleware: ""
            ```

        ??? variable string "`jellyseerr2_traefik_middleware_default`"

            ```yaml
            # Type: string
            jellyseerr2_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`jellyseerr2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            jellyseerr2_traefik_middleware_custom: ""
            ```

        ??? variable string "`jellyseerr2_traefik_certresolver`"

            ```yaml
            # Type: string
            jellyseerr2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`jellyseerr2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            jellyseerr2_traefik_enabled: true
            ```

        ??? variable bool "`jellyseerr2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            jellyseerr2_traefik_api_enabled: false
            ```

        ??? variable string "`jellyseerr2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            jellyseerr2_traefik_api_endpoint: ""
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`jellyseerr_role_docker_container`"

            ```yaml
            # Type: string
            jellyseerr_role_docker_container: "{{ jellyseerr_name }}"
            ```

        ##### Image

        ??? variable bool "`jellyseerr_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            jellyseerr_role_docker_image_pull: true
            ```

        ??? variable string "`jellyseerr_role_docker_image_repo`"

            ```yaml
            # Type: string
            jellyseerr_role_docker_image_repo: "fallenbagel/jellyseerr"
            ```

        ??? variable string "`jellyseerr_role_docker_image_tag`"

            ```yaml
            # Type: string
            jellyseerr_role_docker_image_tag: "latest"
            ```

        ??? variable string "`jellyseerr_role_docker_image`"

            ```yaml
            # Type: string
            jellyseerr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='jellyseerr') }}:{{ lookup('role_var', '_docker_image_tag', role='jellyseerr') }}"
            ```

        ##### Envs

        ??? variable dict "`jellyseerr_role_docker_envs_default`"

            ```yaml
            # Type: dict
            jellyseerr_role_docker_envs_default: 
              UMASK: "002"
              TZ: "{{ tz }}"
              LOG_LEVEL: "{{ lookup('role_var', '_log_level', role='jellyseerr') }}"
            ```

        ??? variable dict "`jellyseerr_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            jellyseerr_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`jellyseerr_role_docker_volumes_default`"

            ```yaml
            # Type: list
            jellyseerr_role_docker_volumes_default: 
              - "{{ lookup('role_var', '_paths_location', role='jellyseerr') }}:/app/config"
            ```

        ??? variable list "`jellyseerr_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            jellyseerr_role_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`jellyseerr_role_docker_hostname`"

            ```yaml
            # Type: string
            jellyseerr_role_docker_hostname: "{{ jellyseerr_name }}"
            ```

        ##### Networks

        ??? variable string "`jellyseerr_role_docker_networks_alias`"

            ```yaml
            # Type: string
            jellyseerr_role_docker_networks_alias: "{{ jellyseerr_name }}"
            ```

        ??? variable list "`jellyseerr_role_docker_networks_default`"

            ```yaml
            # Type: list
            jellyseerr_role_docker_networks_default: []
            ```

        ??? variable list "`jellyseerr_role_docker_networks_custom`"

            ```yaml
            # Type: list
            jellyseerr_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`jellyseerr_role_docker_restart_policy`"

            ```yaml
            # Type: string
            jellyseerr_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`jellyseerr_role_docker_state`"

            ```yaml
            # Type: string
            jellyseerr_role_docker_state: started
            ```

        ##### User

        ??? variable string "`jellyseerr_role_docker_user`"

            ```yaml
            # Type: string
            jellyseerr_role_docker_user: "{{ uid }}:{{ gid }}"
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`jellyseerr2_docker_container`"

            ```yaml
            # Type: string
            jellyseerr2_docker_container: "{{ jellyseerr_name }}"
            ```

        ##### Image

        ??? variable bool "`jellyseerr2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            jellyseerr2_docker_image_pull: true
            ```

        ??? variable string "`jellyseerr2_docker_image_repo`"

            ```yaml
            # Type: string
            jellyseerr2_docker_image_repo: "fallenbagel/jellyseerr"
            ```

        ??? variable string "`jellyseerr2_docker_image_tag`"

            ```yaml
            # Type: string
            jellyseerr2_docker_image_tag: "latest"
            ```

        ??? variable string "`jellyseerr2_docker_image`"

            ```yaml
            # Type: string
            jellyseerr2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='jellyseerr') }}:{{ lookup('role_var', '_docker_image_tag', role='jellyseerr') }}"
            ```

        ##### Envs

        ??? variable dict "`jellyseerr2_docker_envs_default`"

            ```yaml
            # Type: dict
                    jellyseerr2_docker_envs_default: 
                      UMASK: "002"
                      TZ: "{{ tz }}"
                      LOG_LEVEL: "{{ lookup('role_var', '_log_level', role='jellyseerr') }}"
            ```

        ??? variable dict "`jellyseerr2_docker_envs_custom`"

            ```yaml
            # Type: dict
            jellyseerr2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`jellyseerr2_docker_volumes_default`"

            ```yaml
            # Type: list
                    jellyseerr2_docker_volumes_default: 
                      - "{{ lookup('role_var', '_paths_location', role='jellyseerr') }}:/app/config"
            ```

        ??? variable list "`jellyseerr2_docker_volumes_custom`"

            ```yaml
            # Type: list
            jellyseerr2_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`jellyseerr2_docker_hostname`"

            ```yaml
            # Type: string
            jellyseerr2_docker_hostname: "{{ jellyseerr_name }}"
            ```

        ##### Networks

        ??? variable string "`jellyseerr2_docker_networks_alias`"

            ```yaml
            # Type: string
            jellyseerr2_docker_networks_alias: "{{ jellyseerr_name }}"
            ```

        ??? variable list "`jellyseerr2_docker_networks_default`"

            ```yaml
            # Type: list
            jellyseerr2_docker_networks_default: []
            ```

        ??? variable list "`jellyseerr2_docker_networks_custom`"

            ```yaml
            # Type: list
            jellyseerr2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`jellyseerr2_docker_restart_policy`"

            ```yaml
            # Type: string
            jellyseerr2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`jellyseerr2_docker_state`"

            ```yaml
            # Type: string
            jellyseerr2_docker_state: started
            ```

        ##### User

        ??? variable string "`jellyseerr2_docker_user`"

            ```yaml
            # Type: string
            jellyseerr2_docker_user: "{{ uid }}:{{ gid }}"
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`jellyseerr_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            jellyseerr_role_autoheal_enabled: true
            ```

        ??? variable string "`jellyseerr_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            jellyseerr_role_depends_on: ""
            ```

        ??? variable string "`jellyseerr_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            jellyseerr_role_depends_on_delay: "0"
            ```

        ??? variable string "`jellyseerr_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            jellyseerr_role_depends_on_healthchecks:
            ```

        ??? variable bool "`jellyseerr_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            jellyseerr_role_diun_enabled: true
            ```

        ??? variable bool "`jellyseerr_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            jellyseerr_role_dns_enabled: true
            ```

        ??? variable bool "`jellyseerr_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            jellyseerr_role_docker_controller: true
            ```

        ??? variable bool "`jellyseerr_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            jellyseerr_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`jellyseerr_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            jellyseerr_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`jellyseerr_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            jellyseerr_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`jellyseerr_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            jellyseerr_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`jellyseerr_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            jellyseerr_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`jellyseerr_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            jellyseerr_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`jellyseerr_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            jellyseerr_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`jellyseerr_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            jellyseerr_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                jellyseerr_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "jellyseerr2.{{ user.domain }}"
                  - "jellyseerr.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`jellyseerr_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            jellyseerr_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                jellyseerr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'jellyseerr2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`jellyseerr_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            jellyseerr_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `jellyseerr2`):

        ??? variable bool "`jellyseerr2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            jellyseerr2_autoheal_enabled: true
            ```

        ??? variable string "`jellyseerr2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            jellyseerr2_depends_on: ""
            ```

        ??? variable string "`jellyseerr2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            jellyseerr2_depends_on_delay: "0"
            ```

        ??? variable string "`jellyseerr2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            jellyseerr2_depends_on_healthchecks:
            ```

        ??? variable bool "`jellyseerr2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            jellyseerr2_diun_enabled: true
            ```

        ??? variable bool "`jellyseerr2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            jellyseerr2_dns_enabled: true
            ```

        ??? variable bool "`jellyseerr2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            jellyseerr2_docker_controller: true
            ```

        ??? variable bool "`jellyseerr2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            jellyseerr2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`jellyseerr2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            jellyseerr2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`jellyseerr2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            jellyseerr2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`jellyseerr2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            jellyseerr2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`jellyseerr2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            jellyseerr2_traefik_robot_enabled: true
            ```

        ??? variable bool "`jellyseerr2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            jellyseerr2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`jellyseerr2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            jellyseerr2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`jellyseerr2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            jellyseerr2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                jellyseerr2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "jellyseerr2.{{ user.domain }}"
                  - "jellyseerr.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`jellyseerr2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            jellyseerr2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                jellyseerr2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'jellyseerr2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`jellyseerr2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            jellyseerr2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
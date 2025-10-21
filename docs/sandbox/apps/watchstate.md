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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

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

    When overriding variables that end in `_default` (like `watchstate_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `watchstate_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`watchstate_instances`"

        ```yaml
        # Type: list
        watchstate_instances: ["watchstate"]
        ```

        !!! example

            ```yaml
            # Type: list
            watchstate_instances: ["watchstate", "watchstate2"]
            ```

=== "Settings"

    === "Role-level"

        ??? variable bool "`watchstate_role_api_auto`"

            ```yaml
            # Type: bool (true/false)
            watchstate_role_api_auto: true
            ```

        ??? variable bool "`watchstate_role_trust_proxy`"

            ```yaml
            # Type: bool (true/false)
            watchstate_role_trust_proxy: true
            ```

        ??? variable bool "`watchstate_role_secure_api_endpoints`"

            ```yaml
            # Type: bool (true/false)
            watchstate_role_secure_api_endpoints: true
            ```

    === "Instance-level"

        ??? variable bool "`watchstate2_api_auto`"

            ```yaml
            # Type: bool (true/false)
            watchstate2_api_auto: true
            ```

        ??? variable bool "`watchstate2_trust_proxy`"

            ```yaml
            # Type: bool (true/false)
            watchstate2_trust_proxy: true
            ```

        ??? variable bool "`watchstate2_secure_api_endpoints`"

            ```yaml
            # Type: bool (true/false)
            watchstate2_secure_api_endpoints: true
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`watchstate_role_paths_folder`"

            ```yaml
            # Type: string
            watchstate_role_paths_folder: "{{ watchstate_name }}"
            ```

        ??? variable string "`watchstate_role_paths_location`"

            ```yaml
            # Type: string
            watchstate_role_paths_location: "{{ server_appdata_path }}/{{ watchstate_role_paths_folder }}"
            ```

    === "Instance-level"

        ??? variable string "`watchstate2_paths_folder`"

            ```yaml
            # Type: string
            watchstate2_paths_folder: "{{ watchstate_name }}"
            ```

        ??? variable string "`watchstate2_paths_location`"

            ```yaml
            # Type: string
            watchstate2_paths_location: "{{ server_appdata_path }}/{{ watchstate_role_paths_folder }}"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`watchstate_role_web_subdomain`"

            ```yaml
            # Type: string
            watchstate_role_web_subdomain: "{{ watchstate_name }}"
            ```

        ??? variable string "`watchstate_role_web_domain`"

            ```yaml
            # Type: string
            watchstate_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`watchstate_role_web_port`"

            ```yaml
            # Type: string
            watchstate_role_web_port: "8080"
            ```

        ??? variable string "`watchstate_role_web_url`"

            ```yaml
            # Type: string
            watchstate_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='watchstate') + '.' + lookup('role_var', '_web_domain', role='watchstate')
                                      if (lookup('role_var', '_web_subdomain', role='watchstate') | length > 0)
                                      else lookup('role_var', '_web_domain', role='watchstate')) }}"
            ```

    === "Instance-level"

        ??? variable string "`watchstate2_web_subdomain`"

            ```yaml
            # Type: string
            watchstate2_web_subdomain: "{{ watchstate_name }}"
            ```

        ??? variable string "`watchstate2_web_domain`"

            ```yaml
            # Type: string
            watchstate2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`watchstate2_web_port`"

            ```yaml
            # Type: string
            watchstate2_web_port: "8080"
            ```

        ??? variable string "`watchstate2_web_url`"

            ```yaml
            # Type: string
                    watchstate2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='watchstate') + '.' + lookup('role_var', '_web_domain', role='watchstate')
                                          if (lookup('role_var', '_web_subdomain', role='watchstate') | length > 0)
                                          else lookup('role_var', '_web_domain', role='watchstate')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`watchstate_role_dns_record`"

            ```yaml
            # Type: string
            watchstate_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='watchstate') }}"
            ```

        ??? variable string "`watchstate_role_dns_zone`"

            ```yaml
            # Type: string
            watchstate_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='watchstate') }}"
            ```

        ??? variable bool "`watchstate_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            watchstate_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`watchstate2_dns_record`"

            ```yaml
            # Type: string
            watchstate2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='watchstate') }}"
            ```

        ??? variable string "`watchstate2_dns_zone`"

            ```yaml
            # Type: string
            watchstate2_dns_zone: "{{ lookup('role_var', '_web_domain', role='watchstate') }}"
            ```

        ??? variable bool "`watchstate2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            watchstate2_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`watchstate_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            watchstate_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`watchstate_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            watchstate_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`watchstate_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            watchstate_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`watchstate_role_traefik_certresolver`"

            ```yaml
            # Type: string
            watchstate_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`watchstate_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            watchstate_role_traefik_enabled: true
            ```

        ??? variable bool "`watchstate_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            watchstate_role_traefik_api_enabled: true
            ```

        ??? variable string "`watchstate_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            watchstate_role_traefik_api_endpoint: "PathRegexp(`backend/[^/]+/webhook`)"
            ```

    === "Instance-level"

        ??? variable string "`watchstate2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            watchstate2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`watchstate2_traefik_middleware_default`"

            ```yaml
            # Type: string
            watchstate2_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`watchstate2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            watchstate2_traefik_middleware_custom: ""
            ```

        ??? variable string "`watchstate2_traefik_certresolver`"

            ```yaml
            # Type: string
            watchstate2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`watchstate2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            watchstate2_traefik_enabled: true
            ```

        ??? variable bool "`watchstate2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            watchstate2_traefik_api_enabled: true
            ```

        ??? variable string "`watchstate2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            watchstate2_traefik_api_endpoint: "PathRegexp(`backend/[^/]+/webhook`)"
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`watchstate_role_docker_container`"

            ```yaml
            # Type: string
            watchstate_role_docker_container: "{{ watchstate_name }}"
            ```

        ##### Image

        ??? variable bool "`watchstate_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            watchstate_role_docker_image_pull: true
            ```

        ??? variable string "`watchstate_role_docker_image_repo`"

            ```yaml
            # Type: string
            watchstate_role_docker_image_repo: "ghcr.io/arabcoders/watchstate"
            ```

        ??? variable string "`watchstate_role_docker_image_tag`"

            ```yaml
            # Type: string
            watchstate_role_docker_image_tag: "latest"
            ```

        ??? variable string "`watchstate_role_docker_image`"

            ```yaml
            # Type: string
            watchstate_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='watchstate') }}:{{ lookup('role_var', '_docker_image_tag', role='watchstate') }}"
            ```

        ##### Envs

        ??? variable dict "`watchstate_role_docker_envs_default`"

            ```yaml
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
            ```

        ??? variable dict "`watchstate_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            watchstate_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`watchstate_role_docker_volumes_default`"

            ```yaml
            # Type: list
            watchstate_role_docker_volumes_default: 
              - "{{ lookup('role_var', '_paths_location', role='watchstate') }}:/config"
            ```

        ??? variable list "`watchstate_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            watchstate_role_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`watchstate_role_docker_hostname`"

            ```yaml
            # Type: string
            watchstate_role_docker_hostname: "{{ watchstate_name }}"
            ```

        ##### Networks

        ??? variable string "`watchstate_role_docker_networks_alias`"

            ```yaml
            # Type: string
            watchstate_role_docker_networks_alias: "{{ watchstate_name }}"
            ```

        ??? variable list "`watchstate_role_docker_networks_default`"

            ```yaml
            # Type: list
            watchstate_role_docker_networks_default: []
            ```

        ??? variable list "`watchstate_role_docker_networks_custom`"

            ```yaml
            # Type: list
            watchstate_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`watchstate_role_docker_restart_policy`"

            ```yaml
            # Type: string
            watchstate_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`watchstate_role_docker_state`"

            ```yaml
            # Type: string
            watchstate_role_docker_state: started
            ```

        ##### User

        ??? variable string "`watchstate_role_docker_user`"

            ```yaml
            # Type: string
            watchstate_role_docker_user: "{{ uid }}:{{ gid }}"
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`watchstate2_docker_container`"

            ```yaml
            # Type: string
            watchstate2_docker_container: "{{ watchstate_name }}"
            ```

        ##### Image

        ??? variable bool "`watchstate2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            watchstate2_docker_image_pull: true
            ```

        ??? variable string "`watchstate2_docker_image_repo`"

            ```yaml
            # Type: string
            watchstate2_docker_image_repo: "ghcr.io/arabcoders/watchstate"
            ```

        ??? variable string "`watchstate2_docker_image_tag`"

            ```yaml
            # Type: string
            watchstate2_docker_image_tag: "latest"
            ```

        ??? variable string "`watchstate2_docker_image`"

            ```yaml
            # Type: string
            watchstate2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='watchstate') }}:{{ lookup('role_var', '_docker_image_tag', role='watchstate') }}"
            ```

        ##### Envs

        ??? variable dict "`watchstate2_docker_envs_default`"

            ```yaml
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
            ```

        ??? variable dict "`watchstate2_docker_envs_custom`"

            ```yaml
            # Type: dict
            watchstate2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`watchstate2_docker_volumes_default`"

            ```yaml
            # Type: list
                    watchstate2_docker_volumes_default: 
                      - "{{ lookup('role_var', '_paths_location', role='watchstate') }}:/config"
            ```

        ??? variable list "`watchstate2_docker_volumes_custom`"

            ```yaml
            # Type: list
            watchstate2_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`watchstate2_docker_hostname`"

            ```yaml
            # Type: string
            watchstate2_docker_hostname: "{{ watchstate_name }}"
            ```

        ##### Networks

        ??? variable string "`watchstate2_docker_networks_alias`"

            ```yaml
            # Type: string
            watchstate2_docker_networks_alias: "{{ watchstate_name }}"
            ```

        ??? variable list "`watchstate2_docker_networks_default`"

            ```yaml
            # Type: list
            watchstate2_docker_networks_default: []
            ```

        ??? variable list "`watchstate2_docker_networks_custom`"

            ```yaml
            # Type: list
            watchstate2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`watchstate2_docker_restart_policy`"

            ```yaml
            # Type: string
            watchstate2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`watchstate2_docker_state`"

            ```yaml
            # Type: string
            watchstate2_docker_state: started
            ```

        ##### User

        ??? variable string "`watchstate2_docker_user`"

            ```yaml
            # Type: string
            watchstate2_docker_user: "{{ uid }}:{{ gid }}"
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`watchstate_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            watchstate_role_autoheal_enabled: true
            ```

        ??? variable string "`watchstate_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            watchstate_role_depends_on: ""
            ```

        ??? variable string "`watchstate_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            watchstate_role_depends_on_delay: "0"
            ```

        ??? variable string "`watchstate_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            watchstate_role_depends_on_healthchecks:
            ```

        ??? variable bool "`watchstate_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            watchstate_role_diun_enabled: true
            ```

        ??? variable bool "`watchstate_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            watchstate_role_dns_enabled: true
            ```

        ??? variable bool "`watchstate_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            watchstate_role_docker_controller: true
            ```

        ??? variable bool "`watchstate_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            watchstate_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`watchstate_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            watchstate_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`watchstate_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            watchstate_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`watchstate_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            watchstate_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`watchstate_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            watchstate_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`watchstate_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            watchstate_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`watchstate_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            watchstate_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`watchstate_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            watchstate_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                watchstate_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "watchstate2.{{ user.domain }}"
                  - "watchstate.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`watchstate_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            watchstate_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                watchstate_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'watchstate2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`watchstate_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            watchstate_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `watchstate2`):

        ??? variable bool "`watchstate2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            watchstate2_autoheal_enabled: true
            ```

        ??? variable string "`watchstate2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            watchstate2_depends_on: ""
            ```

        ??? variable string "`watchstate2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            watchstate2_depends_on_delay: "0"
            ```

        ??? variable string "`watchstate2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            watchstate2_depends_on_healthchecks:
            ```

        ??? variable bool "`watchstate2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            watchstate2_diun_enabled: true
            ```

        ??? variable bool "`watchstate2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            watchstate2_dns_enabled: true
            ```

        ??? variable bool "`watchstate2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            watchstate2_docker_controller: true
            ```

        ??? variable bool "`watchstate2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            watchstate2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`watchstate2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            watchstate2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`watchstate2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            watchstate2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`watchstate2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            watchstate2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`watchstate2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            watchstate2_traefik_robot_enabled: true
            ```

        ??? variable bool "`watchstate2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            watchstate2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`watchstate2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            watchstate2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`watchstate2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            watchstate2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                watchstate2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "watchstate2.{{ user.domain }}"
                  - "watchstate.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`watchstate2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            watchstate2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                watchstate2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'watchstate2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`watchstate2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            watchstate2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
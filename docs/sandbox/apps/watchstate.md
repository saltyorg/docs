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

## Overview

This tool's primary goal is to sync your backends' play states without relying on third party services. Out of the box, it supports Jellyfin, Plex and Emby media servers.

<div class="grid sb-button-grid" markdown data-search-exclude>

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

Visit <https://watchstate.iYOUR_DOMAIN_NAMEi>.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `watchstate_instances`.

    ```yaml { .sb-show-on-unchecked title="Applies to all instances of watchstate:" }
    watchstate_role_web_subdomain: "custom"
    ```

    ```yaml { .sb-show-on-checked title="Applies to a specific instance (e.g., `watchstate2`):" }
    watchstate2_web_subdomain: "custom2"
    ```

<label class="md-button md-button--stretch" for="sb-checkbox--var-level">
   <input type="checkbox" id="sb-checkbox--var-level"><span class="sb-show-on-unchecked">Show instance-level variables</span><span class="sb-show-on-checked">Show role-level variables</span>
</label>

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `watchstate_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `watchstate_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`watchstate_instances`"

        ```yaml
        # Type: list
        watchstate_instances: ["watchstate"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            watchstate_instances: ["watchstate", "watchstate2"]
            ```

=== "Settings"

    ??? variable bool "`watchstate_role_api_auto`{ .sb-show-on-unchecked }`watchstate2_api_auto`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        watchstate_role_api_auto: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        watchstate2_api_auto: true
        ```

    ??? variable bool "`watchstate_role_trust_proxy`{ .sb-show-on-unchecked }`watchstate2_trust_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        watchstate_role_trust_proxy: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        watchstate2_trust_proxy: true
        ```

    ??? variable bool "`watchstate_role_secure_api_endpoints`{ .sb-show-on-unchecked }`watchstate2_secure_api_endpoints`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        watchstate_role_secure_api_endpoints: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        watchstate2_secure_api_endpoints: true
        ```

=== "Paths"

    ??? variable string "`watchstate_role_paths_folder`{ .sb-show-on-unchecked }`watchstate2_paths_folder`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_paths_folder: "{{ watchstate_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_paths_folder: "{{ watchstate_name }}"
        ```

    ??? variable string "`watchstate_role_paths_location`{ .sb-show-on-unchecked }`watchstate2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_paths_location: "{{ server_appdata_path }}/{{ watchstate_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_paths_location: "{{ server_appdata_path }}/{{ watchstate_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`watchstate_role_web_subdomain`{ .sb-show-on-unchecked }`watchstate2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_web_subdomain: "{{ watchstate_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_web_subdomain: "{{ watchstate_name }}"
        ```

    ??? variable string "`watchstate_role_web_domain`{ .sb-show-on-unchecked }`watchstate2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`watchstate_role_web_port`{ .sb-show-on-unchecked }`watchstate2_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_web_port: "8080"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_web_port: "8080"
        ```

    ??? variable string "`watchstate_role_web_url`{ .sb-show-on-unchecked }`watchstate2_web_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='watchstate') + '.' + lookup('role_var', '_web_domain', role='watchstate')
                                  if (lookup('role_var', '_web_subdomain', role='watchstate') | length > 0)
                                  else lookup('role_var', '_web_domain', role='watchstate')) }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='watchstate') + '.' + lookup('role_var', '_web_domain', role='watchstate')
                              if (lookup('role_var', '_web_subdomain', role='watchstate') | length > 0)
                              else lookup('role_var', '_web_domain', role='watchstate')) }}"
        ```

=== "DNS"

    ??? variable string "`watchstate_role_dns_record`{ .sb-show-on-unchecked }`watchstate2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='watchstate') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='watchstate') }}"
        ```

    ??? variable string "`watchstate_role_dns_zone`{ .sb-show-on-unchecked }`watchstate2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='watchstate') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_dns_zone: "{{ lookup('role_var', '_web_domain', role='watchstate') }}"
        ```

    ??? variable bool "`watchstate_role_dns_proxy`{ .sb-show-on-unchecked }`watchstate2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        watchstate_role_dns_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        watchstate2_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`watchstate_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`watchstate2_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`watchstate_role_traefik_middleware_default`{ .sb-show-on-unchecked }`watchstate2_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`watchstate_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`watchstate2_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_traefik_middleware_custom: ""
        ```

    ??? variable string "`watchstate_role_traefik_certresolver`{ .sb-show-on-unchecked }`watchstate2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`watchstate_role_traefik_enabled`{ .sb-show-on-unchecked }`watchstate2_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        watchstate_role_traefik_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        watchstate2_traefik_enabled: true
        ```

    ??? variable bool "`watchstate_role_traefik_api_enabled`{ .sb-show-on-unchecked }`watchstate2_traefik_api_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        watchstate_role_traefik_api_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        watchstate2_traefik_api_enabled: true
        ```

    ??? variable string "`watchstate_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`watchstate2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_traefik_api_endpoint: "PathRegexp(`backend/[^/]+/webhook`)"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_traefik_api_endpoint: "PathRegexp(`backend/[^/]+/webhook`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`watchstate_role_docker_container`{ .sb-show-on-unchecked }`watchstate2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_docker_container: "{{ watchstate_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_docker_container: "{{ watchstate_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`watchstate_role_docker_image_pull`{ .sb-show-on-unchecked }`watchstate2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        watchstate_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        watchstate2_docker_image_pull: true
        ```

    ??? variable string "`watchstate_role_docker_image_repo`{ .sb-show-on-unchecked }`watchstate2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_docker_image_repo: "ghcr.io/arabcoders/watchstate"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_docker_image_repo: "ghcr.io/arabcoders/watchstate"
        ```

    ??? variable string "`watchstate_role_docker_image_tag`{ .sb-show-on-unchecked }`watchstate2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_docker_image_tag: "latest"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_docker_image_tag: "latest"
        ```

    ??? variable string "`watchstate_role_docker_image`{ .sb-show-on-unchecked }`watchstate2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='watchstate') }}:{{ lookup('role_var', '_docker_image_tag', role='watchstate') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='watchstate') }}:{{ lookup('role_var', '_docker_image_tag', role='watchstate') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`watchstate_role_docker_envs_default`{ .sb-show-on-unchecked }`watchstate2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
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

        ```yaml { .sb-show-on-checked }
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

    ??? variable dict "`watchstate_role_docker_envs_custom`{ .sb-show-on-unchecked }`watchstate2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        watchstate_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        watchstate2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`watchstate_role_docker_volumes_default`{ .sb-show-on-unchecked }`watchstate2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        watchstate_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='watchstate') }}:/config"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        watchstate2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='watchstate') }}:/config"
        ```

    ??? variable list "`watchstate_role_docker_volumes_custom`{ .sb-show-on-unchecked }`watchstate2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        watchstate_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        watchstate2_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`watchstate_role_docker_hostname`{ .sb-show-on-unchecked }`watchstate2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_docker_hostname: "{{ watchstate_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_docker_hostname: "{{ watchstate_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`watchstate_role_docker_networks_alias`{ .sb-show-on-unchecked }`watchstate2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_docker_networks_alias: "{{ watchstate_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_docker_networks_alias: "{{ watchstate_name }}"
        ```

    ??? variable list "`watchstate_role_docker_networks_default`{ .sb-show-on-unchecked }`watchstate2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        watchstate_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        watchstate2_docker_networks_default: []
        ```

    ??? variable list "`watchstate_role_docker_networks_custom`{ .sb-show-on-unchecked }`watchstate2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        watchstate_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        watchstate2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`watchstate_role_docker_restart_policy`{ .sb-show-on-unchecked }`watchstate2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`watchstate_role_docker_state`{ .sb-show-on-unchecked }`watchstate2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`watchstate_role_docker_user`{ .sb-show-on-unchecked }`watchstate2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        watchstate_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        watchstate2_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`watchstate_role_autoheal_enabled`{ .sb-show-on-unchecked }`watchstate2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        watchstate_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        watchstate2_autoheal_enabled: true
        ```

    ??? variable string "`watchstate_role_depends_on`{ .sb-show-on-unchecked }`watchstate2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        watchstate_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        watchstate2_depends_on: ""
        ```

    ??? variable string "`watchstate_role_depends_on_delay`{ .sb-show-on-unchecked }`watchstate2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        watchstate_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        watchstate2_depends_on_delay: "0"
        ```

    ??? variable string "`watchstate_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`watchstate2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        watchstate_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        watchstate2_depends_on_healthchecks:
        ```

    ??? variable bool "`watchstate_role_diun_enabled`{ .sb-show-on-unchecked }`watchstate2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        watchstate_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        watchstate2_diun_enabled: true
        ```

    ??? variable bool "`watchstate_role_dns_enabled`{ .sb-show-on-unchecked }`watchstate2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        watchstate_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        watchstate2_dns_enabled: true
        ```

    ??? variable bool "`watchstate_role_docker_controller`{ .sb-show-on-unchecked }`watchstate2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        watchstate_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        watchstate2_docker_controller: true
        ```

    ??? variable bool "`watchstate_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`watchstate2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        watchstate_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        watchstate2_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`watchstate_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`watchstate2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        watchstate_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        watchstate2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`watchstate_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`watchstate2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        watchstate_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        watchstate2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`watchstate_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`watchstate2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        watchstate_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        watchstate2_traefik_gzip_enabled: false
        ```

    ??? variable bool "`watchstate_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`watchstate2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        watchstate_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        watchstate2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`watchstate_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`watchstate2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        watchstate_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        watchstate2_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`watchstate_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`watchstate2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        watchstate_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        watchstate2_traefik_robot_enabled: true
        ```

    ??? variable bool "`watchstate_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`watchstate2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        watchstate_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        watchstate2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`watchstate_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`watchstate2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        watchstate_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        watchstate2_traefik_wildcard_enabled: true
        ```

    ??? variable list "`watchstate_role_web_fqdn_override`{ .sb-show-on-unchecked }`watchstate2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        watchstate_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        watchstate2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            watchstate_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "watchstate2.{{ user.domain }}"
              - "watchstate.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            watchstate2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "watchstate2.{{ user.domain }}"
              - "watchstate.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`watchstate_role_web_host_override`{ .sb-show-on-unchecked }`watchstate2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        watchstate_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        watchstate2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            watchstate_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'watchstate2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            watchstate2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'watchstate2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`watchstate_role_web_scheme`{ .sb-show-on-unchecked }`watchstate2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        watchstate_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        watchstate2_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
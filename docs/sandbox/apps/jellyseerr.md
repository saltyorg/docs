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

    ```yaml { .sb-show-on-unchecked title="Applies to all instances of jellyseerr:" }
    jellyseerr_role_web_subdomain: "custom"
    ```

    ```yaml { .sb-show-on-checked title="Applies to a specific instance (e.g., `jellyseerr2`):" }
    jellyseerr2_web_subdomain: "custom2"
    ```

<label class="md-button md-button--stretch" for="sb-checkbox--var-level">
   <input type="checkbox" id="sb-checkbox--var-level"><span class="sb-show-on-unchecked">Show instance-level variables</span><span class="sb-show-on-checked">Show role-level variables</span>
</label>

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `jellyseerr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `jellyseerr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`jellyseerr_instances`"

        ```yaml
        # Type: list
        jellyseerr_instances: ["jellyseerr"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            jellyseerr_instances: ["jellyseerr", "jellyseerr2"]
            ```

=== "Settings"

    ??? variable string "`jellyseerr_role_log_level`{ .sb-show-on-unchecked }`jellyseerr2_log_level`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_log_level: "INFO"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_log_level: "INFO"
        ```

=== "Paths"

    ??? variable string "`jellyseerr_role_paths_folder`{ .sb-show-on-unchecked }`jellyseerr2_paths_folder`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_paths_folder: "{{ jellyseerr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_paths_folder: "{{ jellyseerr_name }}"
        ```

    ??? variable string "`jellyseerr_role_paths_location`{ .sb-show-on-unchecked }`jellyseerr2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_paths_location: "{{ server_appdata_path }}/{{ jellyseerr_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_paths_location: "{{ server_appdata_path }}/{{ jellyseerr_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`jellyseerr_role_web_subdomain`{ .sb-show-on-unchecked }`jellyseerr2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_web_subdomain: "{{ jellyseerr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_web_subdomain: "{{ jellyseerr_name }}"
        ```

    ??? variable string "`jellyseerr_role_web_domain`{ .sb-show-on-unchecked }`jellyseerr2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`jellyseerr_role_web_port`{ .sb-show-on-unchecked }`jellyseerr2_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_web_port: "5055"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_web_port: "5055"
        ```

    ??? variable string "`jellyseerr_role_web_url`{ .sb-show-on-unchecked }`jellyseerr2_web_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='jellyseerr') + '.' + lookup('role_var', '_web_domain', role='jellyseerr')
                                  if (lookup('role_var', '_web_subdomain', role='jellyseerr') | length > 0)
                                  else lookup('role_var', '_web_domain', role='jellyseerr')) }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='jellyseerr') + '.' + lookup('role_var', '_web_domain', role='jellyseerr')
                              if (lookup('role_var', '_web_subdomain', role='jellyseerr') | length > 0)
                              else lookup('role_var', '_web_domain', role='jellyseerr')) }}"
        ```

=== "DNS"

    ??? variable string "`jellyseerr_role_dns_record`{ .sb-show-on-unchecked }`jellyseerr2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='jellyseerr') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='jellyseerr') }}"
        ```

    ??? variable string "`jellyseerr_role_dns_zone`{ .sb-show-on-unchecked }`jellyseerr2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='jellyseerr') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_dns_zone: "{{ lookup('role_var', '_web_domain', role='jellyseerr') }}"
        ```

    ??? variable bool "`jellyseerr_role_dns_proxy`{ .sb-show-on-unchecked }`jellyseerr2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        jellyseerr_role_dns_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        jellyseerr2_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`jellyseerr_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`jellyseerr2_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_traefik_sso_middleware: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_traefik_sso_middleware: ""
        ```

    ??? variable string "`jellyseerr_role_traefik_middleware_default`{ .sb-show-on-unchecked }`jellyseerr2_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`jellyseerr_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`jellyseerr2_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_traefik_middleware_custom: ""
        ```

    ??? variable string "`jellyseerr_role_traefik_certresolver`{ .sb-show-on-unchecked }`jellyseerr2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`jellyseerr_role_traefik_enabled`{ .sb-show-on-unchecked }`jellyseerr2_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        jellyseerr_role_traefik_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        jellyseerr2_traefik_enabled: true
        ```

    ??? variable bool "`jellyseerr_role_traefik_api_enabled`{ .sb-show-on-unchecked }`jellyseerr2_traefik_api_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        jellyseerr_role_traefik_api_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        jellyseerr2_traefik_api_enabled: false
        ```

    ??? variable string "`jellyseerr_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`jellyseerr2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_traefik_api_endpoint: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`jellyseerr_role_docker_container`{ .sb-show-on-unchecked }`jellyseerr2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_docker_container: "{{ jellyseerr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_docker_container: "{{ jellyseerr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`jellyseerr_role_docker_image_pull`{ .sb-show-on-unchecked }`jellyseerr2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        jellyseerr_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        jellyseerr2_docker_image_pull: true
        ```

    ??? variable string "`jellyseerr_role_docker_image_repo`{ .sb-show-on-unchecked }`jellyseerr2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_docker_image_repo: "fallenbagel/jellyseerr"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_docker_image_repo: "fallenbagel/jellyseerr"
        ```

    ??? variable string "`jellyseerr_role_docker_image_tag`{ .sb-show-on-unchecked }`jellyseerr2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_docker_image_tag: "latest"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_docker_image_tag: "latest"
        ```

    ??? variable string "`jellyseerr_role_docker_image`{ .sb-show-on-unchecked }`jellyseerr2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='jellyseerr') }}:{{ lookup('role_var', '_docker_image_tag', role='jellyseerr') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='jellyseerr') }}:{{ lookup('role_var', '_docker_image_tag', role='jellyseerr') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`jellyseerr_role_docker_envs_default`{ .sb-show-on-unchecked }`jellyseerr2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        jellyseerr_role_docker_envs_default: 
          UMASK: "002"
          TZ: "{{ tz }}"
          LOG_LEVEL: "{{ lookup('role_var', '_log_level', role='jellyseerr') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        jellyseerr2_docker_envs_default: 
          UMASK: "002"
          TZ: "{{ tz }}"
          LOG_LEVEL: "{{ lookup('role_var', '_log_level', role='jellyseerr') }}"
        ```

    ??? variable dict "`jellyseerr_role_docker_envs_custom`{ .sb-show-on-unchecked }`jellyseerr2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        jellyseerr_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        jellyseerr2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`jellyseerr_role_docker_volumes_default`{ .sb-show-on-unchecked }`jellyseerr2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        jellyseerr_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='jellyseerr') }}:/app/config"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        jellyseerr2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='jellyseerr') }}:/app/config"
        ```

    ??? variable list "`jellyseerr_role_docker_volumes_custom`{ .sb-show-on-unchecked }`jellyseerr2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        jellyseerr_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        jellyseerr2_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`jellyseerr_role_docker_hostname`{ .sb-show-on-unchecked }`jellyseerr2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_docker_hostname: "{{ jellyseerr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_docker_hostname: "{{ jellyseerr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`jellyseerr_role_docker_networks_alias`{ .sb-show-on-unchecked }`jellyseerr2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_docker_networks_alias: "{{ jellyseerr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_docker_networks_alias: "{{ jellyseerr_name }}"
        ```

    ??? variable list "`jellyseerr_role_docker_networks_default`{ .sb-show-on-unchecked }`jellyseerr2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        jellyseerr_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        jellyseerr2_docker_networks_default: []
        ```

    ??? variable list "`jellyseerr_role_docker_networks_custom`{ .sb-show-on-unchecked }`jellyseerr2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        jellyseerr_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        jellyseerr2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`jellyseerr_role_docker_restart_policy`{ .sb-show-on-unchecked }`jellyseerr2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`jellyseerr_role_docker_state`{ .sb-show-on-unchecked }`jellyseerr2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`jellyseerr_role_docker_user`{ .sb-show-on-unchecked }`jellyseerr2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        jellyseerr_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        jellyseerr2_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`jellyseerr_role_autoheal_enabled`{ .sb-show-on-unchecked }`jellyseerr2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        jellyseerr_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        jellyseerr2_autoheal_enabled: true
        ```

    ??? variable string "`jellyseerr_role_depends_on`{ .sb-show-on-unchecked }`jellyseerr2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        jellyseerr_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        jellyseerr2_depends_on: ""
        ```

    ??? variable string "`jellyseerr_role_depends_on_delay`{ .sb-show-on-unchecked }`jellyseerr2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        jellyseerr_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        jellyseerr2_depends_on_delay: "0"
        ```

    ??? variable string "`jellyseerr_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`jellyseerr2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        jellyseerr_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        jellyseerr2_depends_on_healthchecks:
        ```

    ??? variable bool "`jellyseerr_role_diun_enabled`{ .sb-show-on-unchecked }`jellyseerr2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        jellyseerr_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        jellyseerr2_diun_enabled: true
        ```

    ??? variable bool "`jellyseerr_role_dns_enabled`{ .sb-show-on-unchecked }`jellyseerr2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        jellyseerr_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        jellyseerr2_dns_enabled: true
        ```

    ??? variable bool "`jellyseerr_role_docker_controller`{ .sb-show-on-unchecked }`jellyseerr2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        jellyseerr_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        jellyseerr2_docker_controller: true
        ```

    ??? variable bool "`jellyseerr_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`jellyseerr2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        jellyseerr_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        jellyseerr2_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`jellyseerr_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`jellyseerr2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        jellyseerr_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        jellyseerr2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`jellyseerr_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`jellyseerr2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        jellyseerr_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        jellyseerr2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`jellyseerr_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`jellyseerr2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        jellyseerr_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        jellyseerr2_traefik_gzip_enabled: false
        ```

    ??? variable bool "`jellyseerr_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`jellyseerr2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        jellyseerr_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        jellyseerr2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`jellyseerr_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`jellyseerr2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        jellyseerr_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        jellyseerr2_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`jellyseerr_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`jellyseerr2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        jellyseerr_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        jellyseerr2_traefik_robot_enabled: true
        ```

    ??? variable bool "`jellyseerr_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`jellyseerr2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        jellyseerr_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        jellyseerr2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`jellyseerr_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`jellyseerr2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        jellyseerr_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        jellyseerr2_traefik_wildcard_enabled: true
        ```

    ??? variable list "`jellyseerr_role_web_fqdn_override`{ .sb-show-on-unchecked }`jellyseerr2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        jellyseerr_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        jellyseerr2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            jellyseerr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "jellyseerr2.{{ user.domain }}"
              - "jellyseerr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            jellyseerr2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "jellyseerr2.{{ user.domain }}"
              - "jellyseerr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`jellyseerr_role_web_host_override`{ .sb-show-on-unchecked }`jellyseerr2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        jellyseerr_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        jellyseerr2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            jellyseerr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'jellyseerr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            jellyseerr2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'jellyseerr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`jellyseerr_role_web_scheme`{ .sb-show-on-unchecked }`jellyseerr2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        jellyseerr_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        jellyseerr2_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
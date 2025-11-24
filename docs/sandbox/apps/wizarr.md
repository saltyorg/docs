---
icon: material/docker
hide:
  - tags
tags:
  - wizarr
  - automation
  - invitations
---

# Wizarr

## Overview

[Wizarr](https://github.com/Wizarrrr/wizarr)  is a automatic user invitation system for Plex, Jellyfin and Emby. Create a unique link and share it to a user and they will automatically be invited to your media Server! They will even be guided to download the client and instructions on how to use your requests software!

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/Wizarrrr/wizarr){: .header-icons } | [:octicons-link-16: Docs](https://docs.wizarr.dev/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Wizarrrr/wizarr){: .header-icons } | [:material-docker: Docker](https://ghcr.io/wizarrrr/wizarr){: .header-icons }|

### 1. Installation

```shell
sb install sandbox-wizarr
```

### 2. Setup

After installation, go to wizarr.xYOUR_DOMAIN_NAMEx, enter a name for your server, enter the plex server, plex token and choose the default librarys. As optional you can setup a request platform. Save, and you're ready to make your first invite URL!

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `wizarr_instances`.

    ```yaml { .sb-show-on-unchecked title="Applies to all instances of wizarr:" }
    wizarr_role_web_subdomain: "custom"
    ```

    ```yaml { .sb-show-on-checked title="Applies to a specific instance (e.g., `wizarr2`):" }
    wizarr2_web_subdomain: "custom2"
    ```

<label class="md-button md-button--stretch" for="sb-checkbox--var-level">
   <input type="checkbox" id="sb-checkbox--var-level"><span class="sb-show-on-unchecked">Show instance-level variables</span><span class="sb-show-on-checked">Show role-level variables</span>
</label>

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `wizarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `wizarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`wizarr_instances`"

        ```yaml
        # Type: list
        wizarr_instances: ["wizarr"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            wizarr_instances: ["wizarr", "wizarr2"]
            ```

=== "Paths"

    ??? variable string "`wizarr_role_paths_folder`{ .sb-show-on-unchecked }`wizarr2_paths_folder`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_paths_folder: "{{ wizarr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_paths_folder: "{{ wizarr_name }}"
        ```

    ??? variable string "`wizarr_role_paths_location`{ .sb-show-on-unchecked }`wizarr2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_paths_location: "{{ server_appdata_path }}/{{ wizarr_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_paths_location: "{{ server_appdata_path }}/{{ wizarr_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`wizarr_role_web_subdomain`{ .sb-show-on-unchecked }`wizarr2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_web_subdomain: "{{ wizarr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_web_subdomain: "{{ wizarr_name }}"
        ```

    ??? variable string "`wizarr_role_web_domain`{ .sb-show-on-unchecked }`wizarr2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`wizarr_role_web_port`{ .sb-show-on-unchecked }`wizarr2_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_web_port: "5690"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_web_port: "5690"
        ```

    ??? variable string "`wizarr_role_web_url`{ .sb-show-on-unchecked }`wizarr2_web_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='wizarr') + '.' + lookup('role_var', '_web_domain', role='wizarr')
                              if (lookup('role_var', '_web_subdomain', role='wizarr') | length > 0)
                              else lookup('role_var', '_web_domain', role='wizarr')) }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='wizarr') + '.' + lookup('role_var', '_web_domain', role='wizarr')
                          if (lookup('role_var', '_web_subdomain', role='wizarr') | length > 0)
                          else lookup('role_var', '_web_domain', role='wizarr')) }}"
        ```

=== "DNS"

    ??? variable string "`wizarr_role_dns_record`{ .sb-show-on-unchecked }`wizarr2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='wizarr') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='wizarr') }}"
        ```

    ??? variable string "`wizarr_role_dns_zone`{ .sb-show-on-unchecked }`wizarr2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='wizarr') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_dns_zone: "{{ lookup('role_var', '_web_domain', role='wizarr') }}"
        ```

    ??? variable bool "`wizarr_role_dns_proxy`{ .sb-show-on-unchecked }`wizarr2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        wizarr_role_dns_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        wizarr2_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`wizarr_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`wizarr2_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`wizarr_role_traefik_middleware_default`{ .sb-show-on-unchecked }`wizarr2_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`wizarr_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`wizarr2_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_traefik_middleware_custom: ""
        ```

    ??? variable string "`wizarr_role_traefik_certresolver`{ .sb-show-on-unchecked }`wizarr2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`wizarr_role_traefik_enabled`{ .sb-show-on-unchecked }`wizarr2_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        wizarr_role_traefik_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        wizarr2_traefik_enabled: true
        ```

    ??? variable bool "`wizarr_role_traefik_api_enabled`{ .sb-show-on-unchecked }`wizarr2_traefik_api_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        wizarr_role_traefik_api_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        wizarr2_traefik_api_enabled: true
        ```

    ??? variable string "`wizarr_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`wizarr2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_traefik_api_endpoint: "PathPrefix(`/join`) || PathPrefix(`/j`) || PathPrefix(`/static`) || PathPrefix(`/setup`) || PathPrefix(`/wizard`) || PathPrefix(`/image-proxy`) || PathPrefix(`/cinema-posters`) || PathPrefix(`/invitation`)"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_traefik_api_endpoint: "PathPrefix(`/join`) || PathPrefix(`/j`) || PathPrefix(`/static`) || PathPrefix(`/setup`) || PathPrefix(`/wizard`) || PathPrefix(`/image-proxy`) || PathPrefix(`/cinema-posters`) || PathPrefix(`/invitation`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`wizarr_role_docker_container`{ .sb-show-on-unchecked }`wizarr2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_docker_container: "{{ wizarr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_docker_container: "{{ wizarr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`wizarr_role_docker_image_pull`{ .sb-show-on-unchecked }`wizarr2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        wizarr_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        wizarr2_docker_image_pull: true
        ```

    ??? variable string "`wizarr_role_docker_image_repo`{ .sb-show-on-unchecked }`wizarr2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_docker_image_repo: "ghcr.io/wizarrrr/wizarr"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_docker_image_repo: "ghcr.io/wizarrrr/wizarr"
        ```

    ??? variable string "`wizarr_role_docker_image_tag`{ .sb-show-on-unchecked }`wizarr2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_docker_image_tag: "latest"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_docker_image_tag: "latest"
        ```

    ??? variable string "`wizarr_role_docker_image`{ .sb-show-on-unchecked }`wizarr2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='wizarr') }}:{{ lookup('role_var', '_docker_image_tag', role='wizarr') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='wizarr') }}:{{ lookup('role_var', '_docker_image_tag', role='wizarr') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`wizarr_role_docker_envs_default`{ .sb-show-on-unchecked }`wizarr2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        wizarr_role_docker_envs_default:
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          DISABLE_BUILTIN_AUTH: "{{ 'true' if (lookup('role_var', '_traefik_sso_middleware', role='wizarr') | length > 0) else 'false' }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        wizarr2_docker_envs_default:
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          DISABLE_BUILTIN_AUTH: "{{ 'true' if (lookup('role_var', '_traefik_sso_middleware', role='wizarr') | length > 0) else 'false' }}"
        ```

    ??? variable dict "`wizarr_role_docker_envs_custom`{ .sb-show-on-unchecked }`wizarr2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        wizarr_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        wizarr2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`wizarr_role_docker_volumes_default`{ .sb-show-on-unchecked }`wizarr2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        wizarr_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='wizarr') }}/database:/data/database"
          - "{{ lookup('role_var', '_paths_location', role='wizarr') }}/wizard:/data/wizard"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        wizarr2_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='wizarr') }}/database:/data/database"
          - "{{ lookup('role_var', '_paths_location', role='wizarr') }}/wizard:/data/wizard"
        ```

    ??? variable list "`wizarr_role_docker_volumes_custom`{ .sb-show-on-unchecked }`wizarr2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        wizarr_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        wizarr2_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`wizarr_role_docker_hostname`{ .sb-show-on-unchecked }`wizarr2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_docker_hostname: "{{ wizarr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_docker_hostname: "{{ wizarr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`wizarr_role_docker_networks_alias`{ .sb-show-on-unchecked }`wizarr2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_docker_networks_alias: "{{ wizarr_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_docker_networks_alias: "{{ wizarr_name }}"
        ```

    ??? variable list "`wizarr_role_docker_networks_default`{ .sb-show-on-unchecked }`wizarr2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        wizarr_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        wizarr2_docker_networks_default: []
        ```

    ??? variable list "`wizarr_role_docker_networks_custom`{ .sb-show-on-unchecked }`wizarr2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        wizarr_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        wizarr2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`wizarr_role_docker_restart_policy`{ .sb-show-on-unchecked }`wizarr2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`wizarr_role_docker_state`{ .sb-show-on-unchecked }`wizarr2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wizarr_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wizarr2_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`wizarr_role_autoheal_enabled`{ .sb-show-on-unchecked }`wizarr2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        wizarr_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        wizarr2_autoheal_enabled: true
        ```

    ??? variable string "`wizarr_role_depends_on`{ .sb-show-on-unchecked }`wizarr2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        wizarr_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        wizarr2_depends_on: ""
        ```

    ??? variable string "`wizarr_role_depends_on_delay`{ .sb-show-on-unchecked }`wizarr2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        wizarr_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        wizarr2_depends_on_delay: "0"
        ```

    ??? variable string "`wizarr_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`wizarr2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        wizarr_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        wizarr2_depends_on_healthchecks:
        ```

    ??? variable bool "`wizarr_role_diun_enabled`{ .sb-show-on-unchecked }`wizarr2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        wizarr_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        wizarr2_diun_enabled: true
        ```

    ??? variable bool "`wizarr_role_dns_enabled`{ .sb-show-on-unchecked }`wizarr2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        wizarr_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        wizarr2_dns_enabled: true
        ```

    ??? variable bool "`wizarr_role_docker_controller`{ .sb-show-on-unchecked }`wizarr2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        wizarr_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        wizarr2_docker_controller: true
        ```

    ??? variable bool "`wizarr_role_docker_volumes_download`{ .sb-show-on-unchecked }`wizarr2_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        wizarr_role_docker_volumes_download:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        wizarr2_docker_volumes_download:
        ```

    ??? variable bool "`wizarr_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`wizarr2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        wizarr_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        wizarr2_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`wizarr_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`wizarr2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        wizarr_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        wizarr2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`wizarr_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`wizarr2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        wizarr_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        wizarr2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`wizarr_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`wizarr2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        wizarr_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        wizarr2_traefik_gzip_enabled: false
        ```

    ??? variable bool "`wizarr_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`wizarr2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        wizarr_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        wizarr2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`wizarr_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`wizarr2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        wizarr_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        wizarr2_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`wizarr_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`wizarr2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        wizarr_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        wizarr2_traefik_robot_enabled: true
        ```

    ??? variable bool "`wizarr_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`wizarr2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        wizarr_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        wizarr2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`wizarr_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`wizarr2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        wizarr_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        wizarr2_traefik_wildcard_enabled: true
        ```

    ??? variable list "`wizarr_role_web_fqdn_override`{ .sb-show-on-unchecked }`wizarr2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        wizarr_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        wizarr2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            wizarr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "wizarr2.{{ user.domain }}"
              - "wizarr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            wizarr2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "wizarr2.{{ user.domain }}"
              - "wizarr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`wizarr_role_web_host_override`{ .sb-show-on-unchecked }`wizarr2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        wizarr_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        wizarr2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            wizarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'wizarr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            wizarr2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'wizarr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`wizarr_role_web_scheme`{ .sb-show-on-unchecked }`wizarr2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        wizarr_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        wizarr2_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
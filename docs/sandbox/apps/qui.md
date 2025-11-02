---
icon: material/docker
hide:
  - tags
tags:
  - qui
  - torrent
  - qbittorrent
---

# Qui

## Overview

[Qui](https://github.com/autobrr/qui) is a fast, modern web interface for qBittorrent. Supports managing multiple qBittorrent instances from a single, lightweight application.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/autobrr/qui){: .header-icons } | [:octicons-link-16: Docs](https://github.com/autobrr/qui?tab=readme-ov-file#configuration){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/autobrr/qui){: .header-icons } | [:material-docker: Docker](https://github.com/autobrr/qui/blob/main/docker-compose.yml){: .header-icons } |

### 1. Installation

``` shell

sb install sandbox-qui

```

### 2. URL

- To access Qui, visit <https://qui.iYOUR_DOMAIN_NAMEi>

### 3. Setup

- Configure your qBittorrent instance connections through the web interface.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `qui_instances`.

    ```yaml { .sb-show-on-unchecked title="Applies to all instances of qui:" }
    qui_role_web_subdomain: "custom"
    ```

    ```yaml { .sb-show-on-checked title="Applies to a specific instance (e.g., `qui2`):" }
    qui2_web_subdomain: "custom2"
    ```

<label class="md-button md-button--stretch" for="sb-checkbox--var-level">
   <input type="checkbox" id="sb-checkbox--var-level"><span class="sb-show-on-unchecked">Show instance-level variables</span><span class="sb-show-on-checked">Show role-level variables</span>
</label>

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `qui_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `qui_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`qui_instances`"

        ```yaml
        # Type: list
        qui_instances: ["qui"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            qui_instances: ["qui", "qui2"]
            ```

=== "Paths"

    ??? variable string "`qui_role_paths_folder`{ .sb-show-on-unchecked }`qui2_paths_folder`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_paths_folder: "{{ qui_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_paths_folder: "{{ qui_name }}"
        ```

    ??? variable string "`qui_role_paths_location`{ .sb-show-on-unchecked }`qui2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_paths_location: "{{ server_appdata_path }}/{{ qui_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_paths_location: "{{ server_appdata_path }}/{{ qui_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`qui_role_web_subdomain`{ .sb-show-on-unchecked }`qui2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_web_subdomain: "{{ qui_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_web_subdomain: "{{ qui_name }}"
        ```

    ??? variable string "`qui_role_web_domain`{ .sb-show-on-unchecked }`qui2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`qui_role_web_port`{ .sb-show-on-unchecked }`qui2_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_web_port: "7476"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_web_port: "7476"
        ```

    ??? variable string "`qui_role_web_url`{ .sb-show-on-unchecked }`qui2_web_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='qui') + '.' + lookup('role_var', '_web_domain', role='qui')
                           if (lookup('role_var', '_web_subdomain', role='qui') | length > 0)
                           else lookup('role_var', '_web_domain', role='qui')) }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='qui') + '.' + lookup('role_var', '_web_domain', role='qui')
                       if (lookup('role_var', '_web_subdomain', role='qui') | length > 0)
                       else lookup('role_var', '_web_domain', role='qui')) }}"
        ```

=== "DNS"

    ??? variable string "`qui_role_dns_record`{ .sb-show-on-unchecked }`qui2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='qui') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='qui') }}"
        ```

    ??? variable string "`qui_role_dns_zone`{ .sb-show-on-unchecked }`qui2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='qui') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_dns_zone: "{{ lookup('role_var', '_web_domain', role='qui') }}"
        ```

    ??? variable bool "`qui_role_dns_proxy`{ .sb-show-on-unchecked }`qui2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qui_role_dns_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qui2_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`qui_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`qui2_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`qui_role_traefik_middleware_default`{ .sb-show-on-unchecked }`qui2_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`qui_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`qui2_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_traefik_middleware_custom: ""
        ```

    ??? variable string "`qui_role_traefik_certresolver`{ .sb-show-on-unchecked }`qui2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`qui_role_traefik_enabled`{ .sb-show-on-unchecked }`qui2_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qui_role_traefik_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qui2_traefik_enabled: true
        ```

    ??? variable bool "`qui_role_traefik_api_enabled`{ .sb-show-on-unchecked }`qui2_traefik_api_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qui_role_traefik_api_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qui2_traefik_api_enabled: true
        ```

    ??? variable string "`qui_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`qui2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_traefik_api_endpoint: "PathPrefix(`/proxy`)"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_traefik_api_endpoint: "PathPrefix(`/proxy`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`qui_role_docker_container`{ .sb-show-on-unchecked }`qui2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_docker_container: "{{ qui_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_docker_container: "{{ qui_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`qui_role_docker_image_pull`{ .sb-show-on-unchecked }`qui2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qui_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qui2_docker_image_pull: true
        ```

    ??? variable string "`qui_role_docker_image_repo`{ .sb-show-on-unchecked }`qui2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_docker_image_repo: "ghcr.io/autobrr/qui"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_docker_image_repo: "ghcr.io/autobrr/qui"
        ```

    ??? variable string "`qui_role_docker_image_tag`{ .sb-show-on-unchecked }`qui2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_docker_image_tag: "latest"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_docker_image_tag: "latest"
        ```

    ??? variable string "`qui_role_docker_image`{ .sb-show-on-unchecked }`qui2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='qui') }}:{{ lookup('role_var', '_docker_image_tag', role='qui') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='qui') }}:{{ lookup('role_var', '_docker_image_tag', role='qui') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`qui_role_docker_envs_default`{ .sb-show-on-unchecked }`qui2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qui_role_docker_envs_default: 
          TZ: "{{ tz }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qui2_docker_envs_default: 
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`qui_role_docker_envs_custom`{ .sb-show-on-unchecked }`qui2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qui_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qui2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`qui_role_docker_volumes_default`{ .sb-show-on-unchecked }`qui2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qui_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='qui') }}:/config"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qui2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='qui') }}:/config"
        ```

    ??? variable list "`qui_role_docker_volumes_custom`{ .sb-show-on-unchecked }`qui2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qui_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qui2_docker_volumes_custom: []
        ```

    <h5>Hosts</h5>

    ??? variable dict "`qui_role_docker_hosts_default`{ .sb-show-on-unchecked }`qui2_docker_hosts_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qui_role_docker_hosts_default: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qui2_docker_hosts_default: {}
        ```

    ??? variable dict "`qui_role_docker_hosts_custom`{ .sb-show-on-unchecked }`qui2_docker_hosts_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        qui_role_docker_hosts_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        qui2_docker_hosts_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`qui_role_docker_hostname`{ .sb-show-on-unchecked }`qui2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_docker_hostname: "{{ qui_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_docker_hostname: "{{ qui_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`qui_role_docker_networks_alias`{ .sb-show-on-unchecked }`qui2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_docker_networks_alias: "{{ qui_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_docker_networks_alias: "{{ qui_name }}"
        ```

    ??? variable list "`qui_role_docker_networks_default`{ .sb-show-on-unchecked }`qui2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qui_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qui2_docker_networks_default: []
        ```

    ??? variable list "`qui_role_docker_networks_custom`{ .sb-show-on-unchecked }`qui2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        qui_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        qui2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`qui_role_docker_restart_policy`{ .sb-show-on-unchecked }`qui2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`qui_role_docker_state`{ .sb-show-on-unchecked }`qui2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`qui_role_docker_user`{ .sb-show-on-unchecked }`qui2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        qui_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        qui2_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`qui_role_autoheal_enabled`{ .sb-show-on-unchecked }`qui2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        qui_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        qui2_autoheal_enabled: true
        ```

    ??? variable string "`qui_role_depends_on`{ .sb-show-on-unchecked }`qui2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        qui_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        qui2_depends_on: ""
        ```

    ??? variable string "`qui_role_depends_on_delay`{ .sb-show-on-unchecked }`qui2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        qui_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        qui2_depends_on_delay: "0"
        ```

    ??? variable string "`qui_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`qui2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        qui_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        qui2_depends_on_healthchecks:
        ```

    ??? variable bool "`qui_role_diun_enabled`{ .sb-show-on-unchecked }`qui2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        qui_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        qui2_diun_enabled: true
        ```

    ??? variable bool "`qui_role_dns_enabled`{ .sb-show-on-unchecked }`qui2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        qui_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        qui2_dns_enabled: true
        ```

    ??? variable bool "`qui_role_docker_controller`{ .sb-show-on-unchecked }`qui2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        qui_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        qui2_docker_controller: true
        ```

    ??? variable bool "`qui_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`qui2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        qui_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        qui2_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`qui_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`qui2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        qui_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        qui2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`qui_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`qui2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        qui_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        qui2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`qui_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`qui2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        qui_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        qui2_traefik_gzip_enabled: false
        ```

    ??? variable bool "`qui_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`qui2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qui_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qui2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`qui_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`qui2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        qui_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        qui2_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`qui_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`qui2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        qui_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        qui2_traefik_robot_enabled: true
        ```

    ??? variable bool "`qui_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`qui2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        qui_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        qui2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`qui_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`qui2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        qui_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        qui2_traefik_wildcard_enabled: true
        ```

    ??? variable list "`qui_role_web_fqdn_override`{ .sb-show-on-unchecked }`qui2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        qui_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        qui2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            qui_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "qui2.{{ user.domain }}"
              - "qui.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            qui2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "qui2.{{ user.domain }}"
              - "qui.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`qui_role_web_host_override`{ .sb-show-on-unchecked }`qui2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        qui_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        qui2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            qui_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'qui2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            qui2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'qui2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`qui_role_web_scheme`{ .sb-show-on-unchecked }`qui2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        qui_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        qui2_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
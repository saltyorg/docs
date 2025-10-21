---
hide:
  - tags
tags:
  - qui
  - torrent
  - qbittorrent
---

# Qui

## What is it?

[Qui](https://github.com/autobrr/qui) is a fast, modern web interface for qBittorrent. Supports managing multiple qBittorrent instances from a single, lightweight application.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/autobrr/qui){: .header-icons } | [:octicons-link-16: Docs](https://github.com/autobrr/qui?tab=readme-ov-file#configuration){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/autobrr/qui){: .header-icons } | [:material-docker: Docker](https://github.com/autobrr/qui/blob/main/docker-compose.yml){: .header-icons } |

### 1. Installation

``` shell

sb install sandbox-qui

```

### 2. URL

- To access Qui, visit `https://qui._yourdomain.com_`

### 3. Setup

- Configure your qBittorrent instance connections through the web interface.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `qui_instances`.

    === "Role-level Override"

        Applies to all instances of qui:

        ```yaml
        qui_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `qui2`):

        ```yaml
        qui2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `qui_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `qui_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`qui_instances`"

        ```yaml
        # Type: list
        qui_instances: ["qui"]
        ```

        !!! example

            ```yaml
            # Type: list
            qui_instances: ["qui", "qui2"]
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`qui_role_paths_folder`"

            ```yaml
            # Type: string
            qui_role_paths_folder: "{{ qui_name }}"
            ```

        ??? variable string "`qui_role_paths_location`"

            ```yaml
            # Type: string
            qui_role_paths_location: "{{ server_appdata_path }}/{{ qui_role_paths_folder }}"
            ```

    === "Instance-level"

        ??? variable string "`qui2_paths_folder`"

            ```yaml
            # Type: string
            qui2_paths_folder: "{{ qui_name }}"
            ```

        ??? variable string "`qui2_paths_location`"

            ```yaml
            # Type: string
            qui2_paths_location: "{{ server_appdata_path }}/{{ qui_role_paths_folder }}"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`qui_role_web_subdomain`"

            ```yaml
            # Type: string
            qui_role_web_subdomain: "{{ qui_name }}"
            ```

        ??? variable string "`qui_role_web_domain`"

            ```yaml
            # Type: string
            qui_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`qui_role_web_port`"

            ```yaml
            # Type: string
            qui_role_web_port: "7476"
            ```

        ??? variable string "`qui_role_web_url`"

            ```yaml
            # Type: string
            qui_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='qui') + '.' + lookup('role_var', '_web_domain', role='qui')
                               if (lookup('role_var', '_web_subdomain', role='qui') | length > 0)
                               else lookup('role_var', '_web_domain', role='qui')) }}"
            ```

    === "Instance-level"

        ??? variable string "`qui2_web_subdomain`"

            ```yaml
            # Type: string
            qui2_web_subdomain: "{{ qui_name }}"
            ```

        ??? variable string "`qui2_web_domain`"

            ```yaml
            # Type: string
            qui2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`qui2_web_port`"

            ```yaml
            # Type: string
            qui2_web_port: "7476"
            ```

        ??? variable string "`qui2_web_url`"

            ```yaml
            # Type: string
            qui2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='qui') + '.' + lookup('role_var', '_web_domain', role='qui')
                           if (lookup('role_var', '_web_subdomain', role='qui') | length > 0)
                           else lookup('role_var', '_web_domain', role='qui')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`qui_role_dns_record`"

            ```yaml
            # Type: string
            qui_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='qui') }}"
            ```

        ??? variable string "`qui_role_dns_zone`"

            ```yaml
            # Type: string
            qui_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='qui') }}"
            ```

        ??? variable bool "`qui_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            qui_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`qui2_dns_record`"

            ```yaml
            # Type: string
            qui2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='qui') }}"
            ```

        ??? variable string "`qui2_dns_zone`"

            ```yaml
            # Type: string
            qui2_dns_zone: "{{ lookup('role_var', '_web_domain', role='qui') }}"
            ```

        ??? variable bool "`qui2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            qui2_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`qui_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            qui_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`qui_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            qui_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`qui_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            qui_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`qui_role_traefik_certresolver`"

            ```yaml
            # Type: string
            qui_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`qui_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            qui_role_traefik_enabled: true
            ```

        ??? variable bool "`qui_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            qui_role_traefik_api_enabled: true
            ```

        ??? variable string "`qui_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            qui_role_traefik_api_endpoint: "PathPrefix(`/proxy`)"
            ```

    === "Instance-level"

        ??? variable string "`qui2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            qui2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`qui2_traefik_middleware_default`"

            ```yaml
            # Type: string
            qui2_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`qui2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            qui2_traefik_middleware_custom: ""
            ```

        ??? variable string "`qui2_traefik_certresolver`"

            ```yaml
            # Type: string
            qui2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`qui2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            qui2_traefik_enabled: true
            ```

        ??? variable bool "`qui2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            qui2_traefik_api_enabled: true
            ```

        ??? variable string "`qui2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            qui2_traefik_api_endpoint: "PathPrefix(`/proxy`)"
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`qui_role_docker_container`"

            ```yaml
            # Type: string
            qui_role_docker_container: "{{ qui_name }}"
            ```

        ##### Image

        ??? variable bool "`qui_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            qui_role_docker_image_pull: true
            ```

        ??? variable string "`qui_role_docker_image_repo`"

            ```yaml
            # Type: string
            qui_role_docker_image_repo: "ghcr.io/autobrr/qui"
            ```

        ??? variable string "`qui_role_docker_image_tag`"

            ```yaml
            # Type: string
            qui_role_docker_image_tag: "latest"
            ```

        ??? variable string "`qui_role_docker_image`"

            ```yaml
            # Type: string
            qui_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='qui') }}:{{ lookup('role_var', '_docker_image_tag', role='qui') }}"
            ```

        ##### Envs

        ??? variable dict "`qui_role_docker_envs_default`"

            ```yaml
            # Type: dict
            qui_role_docker_envs_default: 
              TZ: "{{ tz }}"
            ```

        ??? variable dict "`qui_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            qui_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`qui_role_docker_volumes_default`"

            ```yaml
            # Type: list
            qui_role_docker_volumes_default: 
              - "{{ lookup('role_var', '_paths_location', role='qui') }}:/config"
            ```

        ??? variable list "`qui_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            qui_role_docker_volumes_custom: []
            ```

        ##### Hosts

        ??? variable dict "`qui_role_docker_hosts_default`"

            ```yaml
            # Type: dict
            qui_role_docker_hosts_default: {}
            ```

        ??? variable dict "`qui_role_docker_hosts_custom`"

            ```yaml
            # Type: dict
            qui_role_docker_hosts_custom: {}
            ```

        ##### Hostname

        ??? variable string "`qui_role_docker_hostname`"

            ```yaml
            # Type: string
            qui_role_docker_hostname: "{{ qui_name }}"
            ```

        ##### Networks

        ??? variable string "`qui_role_docker_networks_alias`"

            ```yaml
            # Type: string
            qui_role_docker_networks_alias: "{{ qui_name }}"
            ```

        ??? variable list "`qui_role_docker_networks_default`"

            ```yaml
            # Type: list
            qui_role_docker_networks_default: []
            ```

        ??? variable list "`qui_role_docker_networks_custom`"

            ```yaml
            # Type: list
            qui_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`qui_role_docker_restart_policy`"

            ```yaml
            # Type: string
            qui_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`qui_role_docker_state`"

            ```yaml
            # Type: string
            qui_role_docker_state: started
            ```

        ##### User

        ??? variable string "`qui_role_docker_user`"

            ```yaml
            # Type: string
            qui_role_docker_user: "{{ uid }}:{{ gid }}"
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`qui2_docker_container`"

            ```yaml
            # Type: string
            qui2_docker_container: "{{ qui_name }}"
            ```

        ##### Image

        ??? variable bool "`qui2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            qui2_docker_image_pull: true
            ```

        ??? variable string "`qui2_docker_image_repo`"

            ```yaml
            # Type: string
            qui2_docker_image_repo: "ghcr.io/autobrr/qui"
            ```

        ??? variable string "`qui2_docker_image_tag`"

            ```yaml
            # Type: string
            qui2_docker_image_tag: "latest"
            ```

        ??? variable string "`qui2_docker_image`"

            ```yaml
            # Type: string
            qui2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='qui') }}:{{ lookup('role_var', '_docker_image_tag', role='qui') }}"
            ```

        ##### Envs

        ??? variable dict "`qui2_docker_envs_default`"

            ```yaml
            # Type: dict
            qui2_docker_envs_default: 
              TZ: "{{ tz }}"
            ```

        ??? variable dict "`qui2_docker_envs_custom`"

            ```yaml
            # Type: dict
            qui2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`qui2_docker_volumes_default`"

            ```yaml
            # Type: list
            qui2_docker_volumes_default: 
              - "{{ lookup('role_var', '_paths_location', role='qui') }}:/config"
            ```

        ??? variable list "`qui2_docker_volumes_custom`"

            ```yaml
            # Type: list
            qui2_docker_volumes_custom: []
            ```

        ##### Hosts

        ??? variable dict "`qui2_docker_hosts_default`"

            ```yaml
            # Type: dict
            qui2_docker_hosts_default: {}
            ```

        ??? variable dict "`qui2_docker_hosts_custom`"

            ```yaml
            # Type: dict
            qui2_docker_hosts_custom: {}
            ```

        ##### Hostname

        ??? variable string "`qui2_docker_hostname`"

            ```yaml
            # Type: string
            qui2_docker_hostname: "{{ qui_name }}"
            ```

        ##### Networks

        ??? variable string "`qui2_docker_networks_alias`"

            ```yaml
            # Type: string
            qui2_docker_networks_alias: "{{ qui_name }}"
            ```

        ??? variable list "`qui2_docker_networks_default`"

            ```yaml
            # Type: list
            qui2_docker_networks_default: []
            ```

        ??? variable list "`qui2_docker_networks_custom`"

            ```yaml
            # Type: list
            qui2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`qui2_docker_restart_policy`"

            ```yaml
            # Type: string
            qui2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`qui2_docker_state`"

            ```yaml
            # Type: string
            qui2_docker_state: started
            ```

        ##### User

        ??? variable string "`qui2_docker_user`"

            ```yaml
            # Type: string
            qui2_docker_user: "{{ uid }}:{{ gid }}"
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`qui_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            qui_role_autoheal_enabled: true
            ```

        ??? variable string "`qui_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            qui_role_depends_on: ""
            ```

        ??? variable string "`qui_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            qui_role_depends_on_delay: "0"
            ```

        ??? variable string "`qui_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            qui_role_depends_on_healthchecks:
            ```

        ??? variable bool "`qui_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            qui_role_diun_enabled: true
            ```

        ??? variable bool "`qui_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            qui_role_dns_enabled: true
            ```

        ??? variable bool "`qui_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            qui_role_docker_controller: true
            ```

        ??? variable bool "`qui_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            qui_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`qui_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            qui_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`qui_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            qui_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`qui_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            qui_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`qui_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            qui_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`qui_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            qui_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`qui_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            qui_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`qui_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            qui_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                qui_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "qui2.{{ user.domain }}"
                  - "qui.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`qui_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            qui_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                qui_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'qui2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`qui_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            qui_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `qui2`):

        ??? variable bool "`qui2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            qui2_autoheal_enabled: true
            ```

        ??? variable string "`qui2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            qui2_depends_on: ""
            ```

        ??? variable string "`qui2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            qui2_depends_on_delay: "0"
            ```

        ??? variable string "`qui2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            qui2_depends_on_healthchecks:
            ```

        ??? variable bool "`qui2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            qui2_diun_enabled: true
            ```

        ??? variable bool "`qui2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            qui2_dns_enabled: true
            ```

        ??? variable bool "`qui2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            qui2_docker_controller: true
            ```

        ??? variable bool "`qui2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            qui2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`qui2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            qui2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`qui2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            qui2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`qui2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            qui2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`qui2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            qui2_traefik_robot_enabled: true
            ```

        ??? variable bool "`qui2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            qui2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`qui2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            qui2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`qui2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            qui2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                qui2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "qui2.{{ user.domain }}"
                  - "qui.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`qui2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            qui2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                qui2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'qui2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`qui2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            qui2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
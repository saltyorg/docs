---
hide:
  - tags
tags:
  - requestrr
  - discord
  - automation
---

# Requestrr

## What is it?

[Requestrr](https://github.com/thomst08/requestrr) is a chatbot used to simplify using services like Sonarr/Radarr/Ombi via the use of chat. Current platform is Discord only, but the bot was built around the ideology of quick adaptation for new features as well as new platforms.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/thomst08/requestrr){: .header-icons } | [:octicons-link-16: Docs](https://github.com/thomst08/requestrr/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/thomst08/requestrr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/thomst08/requestrr){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-requestrr

```

### 2. URL

- To access Requestrr, visit `https://requestrr._yourdomain.com_`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `requestrr_instances`.

    === "Role-level Override"

        Applies to all instances of requestrr:

        ```yaml
        requestrr_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `requestrr2`):

        ```yaml
        requestrr2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `requestrr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `requestrr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`requestrr_instances`"

        ```yaml
        # Type: list
        requestrr_instances: ["requestrr"]
        ```

        !!! example

            ```yaml
            # Type: list
            requestrr_instances: ["requestrr", "requestrr2"]
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`requestrr_role_paths_folder`"

            ```yaml
            # Type: string
            requestrr_role_paths_folder: "{{ requestrr_name }}"
            ```

        ??? variable string "`requestrr_role_paths_location`"

            ```yaml
            # Type: string
            requestrr_role_paths_location: "{{ server_appdata_path }}/{{ requestrr_role_paths_folder }}"
            ```

    === "Instance-level"

        ??? variable string "`requestrr2_paths_folder`"

            ```yaml
            # Type: string
            requestrr2_paths_folder: "{{ requestrr_name }}"
            ```

        ??? variable string "`requestrr2_paths_location`"

            ```yaml
            # Type: string
            requestrr2_paths_location: "{{ server_appdata_path }}/{{ requestrr_role_paths_folder }}"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`requestrr_role_web_subdomain`"

            ```yaml
            # Type: string
            requestrr_role_web_subdomain: "{{ requestrr_name }}"
            ```

        ??? variable string "`requestrr_role_web_domain`"

            ```yaml
            # Type: string
            requestrr_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`requestrr_role_web_port`"

            ```yaml
            # Type: string
            requestrr_role_web_port: "4545"
            ```

        ??? variable string "`requestrr_role_web_url`"

            ```yaml
            # Type: string
            requestrr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='requestrr') + '.' + lookup('role_var', '_web_domain', role='requestrr')
                                     if (lookup('role_var', '_web_subdomain', role='requestrr') | length > 0)
                                     else lookup('role_var', '_web_domain', role='requestrr')) }}"
            ```

    === "Instance-level"

        ??? variable string "`requestrr2_web_subdomain`"

            ```yaml
            # Type: string
            requestrr2_web_subdomain: "{{ requestrr_name }}"
            ```

        ??? variable string "`requestrr2_web_domain`"

            ```yaml
            # Type: string
            requestrr2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`requestrr2_web_port`"

            ```yaml
            # Type: string
            requestrr2_web_port: "4545"
            ```

        ??? variable string "`requestrr2_web_url`"

            ```yaml
            # Type: string
            requestrr2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='requestrr') + '.' + lookup('role_var', '_web_domain', role='requestrr')
                                 if (lookup('role_var', '_web_subdomain', role='requestrr') | length > 0)
                                 else lookup('role_var', '_web_domain', role='requestrr')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`requestrr_role_dns_record`"

            ```yaml
            # Type: string
            requestrr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='requestrr') }}"
            ```

        ??? variable string "`requestrr_role_dns_zone`"

            ```yaml
            # Type: string
            requestrr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='requestrr') }}"
            ```

        ??? variable bool "`requestrr_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            requestrr_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`requestrr2_dns_record`"

            ```yaml
            # Type: string
            requestrr2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='requestrr') }}"
            ```

        ??? variable string "`requestrr2_dns_zone`"

            ```yaml
            # Type: string
            requestrr2_dns_zone: "{{ lookup('role_var', '_web_domain', role='requestrr') }}"
            ```

        ??? variable bool "`requestrr2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            requestrr2_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`requestrr_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            requestrr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`requestrr_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            requestrr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`requestrr_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            requestrr_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`requestrr_role_traefik_certresolver`"

            ```yaml
            # Type: string
            requestrr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`requestrr_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            requestrr_role_traefik_enabled: true
            ```

        ??? variable bool "`requestrr_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            requestrr_role_traefik_api_enabled: false
            ```

        ??? variable string "`requestrr_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            requestrr_role_traefik_api_endpoint: ""
            ```

    === "Instance-level"

        ??? variable string "`requestrr2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            requestrr2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`requestrr2_traefik_middleware_default`"

            ```yaml
            # Type: string
            requestrr2_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`requestrr2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            requestrr2_traefik_middleware_custom: ""
            ```

        ??? variable string "`requestrr2_traefik_certresolver`"

            ```yaml
            # Type: string
            requestrr2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`requestrr2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            requestrr2_traefik_enabled: true
            ```

        ??? variable bool "`requestrr2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            requestrr2_traefik_api_enabled: false
            ```

        ??? variable string "`requestrr2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            requestrr2_traefik_api_endpoint: ""
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`requestrr_role_docker_container`"

            ```yaml
            # Type: string
            requestrr_role_docker_container: "{{ requestrr_name }}"
            ```

        ##### Image

        ??? variable bool "`requestrr_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            requestrr_role_docker_image_pull: true
            ```

        ??? variable string "`requestrr_role_docker_image_repo`"

            ```yaml
            # Type: string
            requestrr_role_docker_image_repo: "thomst08/requestrr"
            ```

        ??? variable string "`requestrr_role_docker_image_tag`"

            ```yaml
            # Type: string
            requestrr_role_docker_image_tag: "latest"
            ```

        ??? variable string "`requestrr_role_docker_image`"

            ```yaml
            # Type: string
            requestrr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='requestrr') }}:{{ lookup('role_var', '_docker_image_tag', role='requestrr') }}"
            ```

        ##### Envs

        ??? variable dict "`requestrr_role_docker_envs_default`"

            ```yaml
            # Type: dict
            requestrr_role_docker_envs_default: 
              TZ: "{{ tz }}"
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              UMASK: "002"
            ```

        ??? variable dict "`requestrr_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            requestrr_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`requestrr_role_docker_volumes_default`"

            ```yaml
            # Type: list
            requestrr_role_docker_volumes_default: 
              - "{{ lookup('role_var', '_paths_location', role='requestrr') }}:/root/config"
            ```

        ??? variable list "`requestrr_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            requestrr_role_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`requestrr_role_docker_hostname`"

            ```yaml
            # Type: string
            requestrr_role_docker_hostname: "{{ requestrr_name }}"
            ```

        ##### Networks

        ??? variable string "`requestrr_role_docker_networks_alias`"

            ```yaml
            # Type: string
            requestrr_role_docker_networks_alias: "{{ requestrr_name }}"
            ```

        ??? variable list "`requestrr_role_docker_networks_default`"

            ```yaml
            # Type: list
            requestrr_role_docker_networks_default: []
            ```

        ??? variable list "`requestrr_role_docker_networks_custom`"

            ```yaml
            # Type: list
            requestrr_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`requestrr_role_docker_restart_policy`"

            ```yaml
            # Type: string
            requestrr_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`requestrr_role_docker_state`"

            ```yaml
            # Type: string
            requestrr_role_docker_state: started
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`requestrr2_docker_container`"

            ```yaml
            # Type: string
            requestrr2_docker_container: "{{ requestrr_name }}"
            ```

        ##### Image

        ??? variable bool "`requestrr2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            requestrr2_docker_image_pull: true
            ```

        ??? variable string "`requestrr2_docker_image_repo`"

            ```yaml
            # Type: string
            requestrr2_docker_image_repo: "thomst08/requestrr"
            ```

        ??? variable string "`requestrr2_docker_image_tag`"

            ```yaml
            # Type: string
            requestrr2_docker_image_tag: "latest"
            ```

        ??? variable string "`requestrr2_docker_image`"

            ```yaml
            # Type: string
            requestrr2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='requestrr') }}:{{ lookup('role_var', '_docker_image_tag', role='requestrr') }}"
            ```

        ##### Envs

        ??? variable dict "`requestrr2_docker_envs_default`"

            ```yaml
            # Type: dict
            requestrr2_docker_envs_default: 
              TZ: "{{ tz }}"
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              UMASK: "002"
            ```

        ??? variable dict "`requestrr2_docker_envs_custom`"

            ```yaml
            # Type: dict
            requestrr2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`requestrr2_docker_volumes_default`"

            ```yaml
            # Type: list
            requestrr2_docker_volumes_default: 
              - "{{ lookup('role_var', '_paths_location', role='requestrr') }}:/root/config"
            ```

        ??? variable list "`requestrr2_docker_volumes_custom`"

            ```yaml
            # Type: list
            requestrr2_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`requestrr2_docker_hostname`"

            ```yaml
            # Type: string
            requestrr2_docker_hostname: "{{ requestrr_name }}"
            ```

        ##### Networks

        ??? variable string "`requestrr2_docker_networks_alias`"

            ```yaml
            # Type: string
            requestrr2_docker_networks_alias: "{{ requestrr_name }}"
            ```

        ??? variable list "`requestrr2_docker_networks_default`"

            ```yaml
            # Type: list
            requestrr2_docker_networks_default: []
            ```

        ??? variable list "`requestrr2_docker_networks_custom`"

            ```yaml
            # Type: list
            requestrr2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`requestrr2_docker_restart_policy`"

            ```yaml
            # Type: string
            requestrr2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`requestrr2_docker_state`"

            ```yaml
            # Type: string
            requestrr2_docker_state: started
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`requestrr_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            requestrr_role_autoheal_enabled: true
            ```

        ??? variable string "`requestrr_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            requestrr_role_depends_on: ""
            ```

        ??? variable string "`requestrr_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            requestrr_role_depends_on_delay: "0"
            ```

        ??? variable string "`requestrr_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            requestrr_role_depends_on_healthchecks:
            ```

        ??? variable bool "`requestrr_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            requestrr_role_diun_enabled: true
            ```

        ??? variable bool "`requestrr_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            requestrr_role_dns_enabled: true
            ```

        ??? variable bool "`requestrr_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            requestrr_role_docker_controller: true
            ```

        ??? variable bool "`requestrr_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            requestrr_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`requestrr_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            requestrr_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`requestrr_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            requestrr_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`requestrr_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            requestrr_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`requestrr_role_traefik_middleware_http_api_insecure`"

            ```yaml
            # Type: bool (true/false)
            requestrr_role_traefik_middleware_http_api_insecure:
            ```

        ??? variable bool "`requestrr_role_traefik_middleware_http_insecure`"

            ```yaml
            # Type: bool (true/false)
            requestrr_role_traefik_middleware_http_insecure:
            ```

        ??? variable bool "`requestrr_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            requestrr_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`requestrr_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            requestrr_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`requestrr_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            requestrr_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`requestrr_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            requestrr_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                requestrr_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "requestrr2.{{ user.domain }}"
                  - "requestrr.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`requestrr_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            requestrr_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                requestrr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'requestrr2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`requestrr_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            requestrr_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `requestrr2`):

        ??? variable bool "`requestrr2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            requestrr2_autoheal_enabled: true
            ```

        ??? variable string "`requestrr2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            requestrr2_depends_on: ""
            ```

        ??? variable string "`requestrr2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            requestrr2_depends_on_delay: "0"
            ```

        ??? variable string "`requestrr2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            requestrr2_depends_on_healthchecks:
            ```

        ??? variable bool "`requestrr2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            requestrr2_diun_enabled: true
            ```

        ??? variable bool "`requestrr2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            requestrr2_dns_enabled: true
            ```

        ??? variable bool "`requestrr2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            requestrr2_docker_controller: true
            ```

        ??? variable bool "`requestrr2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            requestrr2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`requestrr2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            requestrr2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`requestrr2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            requestrr2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`requestrr2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            requestrr2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`requestrr2_traefik_middleware_http_api_insecure`"

            ```yaml
            # Type: bool (true/false)
            requestrr2_traefik_middleware_http_api_insecure:
            ```

        ??? variable bool "`requestrr2_traefik_middleware_http_insecure`"

            ```yaml
            # Type: bool (true/false)
            requestrr2_traefik_middleware_http_insecure:
            ```

        ??? variable bool "`requestrr2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            requestrr2_traefik_robot_enabled: true
            ```

        ??? variable bool "`requestrr2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            requestrr2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`requestrr2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            requestrr2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`requestrr2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            requestrr2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                requestrr2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "requestrr2.{{ user.domain }}"
                  - "requestrr.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`requestrr2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            requestrr2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                requestrr2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'requestrr2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`requestrr2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            requestrr2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
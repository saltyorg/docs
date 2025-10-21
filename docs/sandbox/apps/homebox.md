---
hide:
  - tags
tags:
  - homebox
  - productivity
  - inventory
---

# Homebox

## What is it?

[Homebox](https://homebox.software/en/) is the inventory and organization system built for the Home User! With a focus on simplicity and ease of use, Homebox is the perfect solution for your home inventory, organization, and management needs.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://homebox.software/en/){: .header-icons } | [:octicons-link-16: Docs](https://homebox.software/en/quick-start.html){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/sysadminsmedia/homebox){: .header-icons } |

### 1. Installation

``` shell

sb install sandbox-homebox

```

### 2. URL

- To access Homebox, visit `https://homebox._yourdomain.com_`

### 3. Setup

- Create a user in the web ui, add your email and password, then log in.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        homebox_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `homebox_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `homebox_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`homebox_name`"

        ```yaml
        # Type: string
        homebox_name: homebox
        ```

=== "Paths"

    ??? variable string "`homebox_role_paths_folder`"

        ```yaml
        # Type: string
        homebox_role_paths_folder: "{{ homebox_name }}"
        ```

    ??? variable string "`homebox_role_paths_location`"

        ```yaml
        # Type: string
        homebox_role_paths_location: "{{ server_appdata_path }}/{{ homebox_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`homebox_role_web_subdomain`"

        ```yaml
        # Type: string
        homebox_role_web_subdomain: "{{ homebox_name }}"
        ```

    ??? variable string "`homebox_role_web_domain`"

        ```yaml
        # Type: string
        homebox_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`homebox_role_web_port`"

        ```yaml
        # Type: string
        homebox_role_web_port: "7745"
        ```

    ??? variable string "`homebox_role_web_url`"

        ```yaml
        # Type: string
        homebox_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='homebox') + '.' + lookup('role_var', '_web_domain', role='homebox')
                               if (lookup('role_var', '_web_subdomain', role='homebox') | length > 0)
                               else lookup('role_var', '_web_domain', role='homebox')) }}"
        ```

=== "DNS"

    ??? variable string "`homebox_role_dns_record`"

        ```yaml
        # Type: string
        homebox_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='homebox') }}"
        ```

    ??? variable string "`homebox_role_dns_zone`"

        ```yaml
        # Type: string
        homebox_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='homebox') }}"
        ```

    ??? variable bool "`homebox_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`homebox_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        homebox_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`homebox_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        homebox_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`homebox_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        homebox_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`homebox_role_traefik_certresolver`"

        ```yaml
        # Type: string
        homebox_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`homebox_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_traefik_enabled: true
        ```

    ??? variable bool "`homebox_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_traefik_api_enabled: false
        ```

    ??? variable string "`homebox_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        homebox_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`homebox_role_docker_container`"

        ```yaml
        # Type: string
        homebox_role_docker_container: "{{ homebox_name }}"
        ```

    ##### Image

    ??? variable bool "`homebox_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        homebox_role_docker_image_pull: true
        ```

    ??? variable string "`homebox_role_docker_image_repo`"

        ```yaml
        # Type: string
        homebox_role_docker_image_repo: "ghcr.io/sysadminsmedia/homebox"
        ```

    ??? variable string "`homebox_role_docker_image_tag`"

        ```yaml
        # Type: string
        homebox_role_docker_image_tag: "latest"
        ```

    ??? variable string "`homebox_role_docker_image`"

        ```yaml
        # Type: string
        homebox_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='homebox') }}:{{ lookup('role_var', '_docker_image_tag', role='homebox') }}"
        ```

    ##### Envs

    ??? variable dict "`homebox_role_docker_envs_default`"

        ```yaml
        # Type: dict
        homebox_role_docker_envs_default: 
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          HBOX_LOG_LEVEL: "info"
          HBOX_SWAGGER_SCHEMA: "https"
        ```

    ??? variable dict "`homebox_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        homebox_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`homebox_role_docker_volumes_default`"

        ```yaml
        # Type: list
        homebox_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='homebox') }}:/data"
        ```

    ??? variable list "`homebox_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        homebox_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`homebox_role_docker_hostname`"

        ```yaml
        # Type: string
        homebox_role_docker_hostname: "{{ homebox_name }}"
        ```

    ##### Networks

    ??? variable string "`homebox_role_docker_networks_alias`"

        ```yaml
        # Type: string
        homebox_role_docker_networks_alias: "{{ homebox_name }}"
        ```

    ??? variable list "`homebox_role_docker_networks_default`"

        ```yaml
        # Type: list
        homebox_role_docker_networks_default: []
        ```

    ??? variable list "`homebox_role_docker_networks_custom`"

        ```yaml
        # Type: list
        homebox_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`homebox_role_docker_restart_policy`"

        ```yaml
        # Type: string
        homebox_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`homebox_role_docker_state`"

        ```yaml
        # Type: string
        homebox_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`homebox_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        homebox_role_autoheal_enabled: true
        ```

    ??? variable string "`homebox_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        homebox_role_depends_on: ""
        ```

    ??? variable string "`homebox_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        homebox_role_depends_on_delay: "0"
        ```

    ??? variable string "`homebox_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        homebox_role_depends_on_healthchecks:
        ```

    ??? variable bool "`homebox_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        homebox_role_diun_enabled: true
        ```

    ??? variable bool "`homebox_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        homebox_role_dns_enabled: true
        ```

    ??? variable bool "`homebox_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        homebox_role_docker_controller: true
        ```

    ??? variable bool "`homebox_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        homebox_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`homebox_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        homebox_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`homebox_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        homebox_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`homebox_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        homebox_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`homebox_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        homebox_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`homebox_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        homebox_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`homebox_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        homebox_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`homebox_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        homebox_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            homebox_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "homebox2.{{ user.domain }}"
              - "homebox.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`homebox_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        homebox_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            homebox_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'homebox2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`homebox_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        homebox_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
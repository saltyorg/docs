---
hide:
  - tags
tags:
  - node-red
  - automation
  - iot
---

# Node Red

## What is it?

[Node Red](https://www.nodered.org/) is a flow-based development tool for visual programming developed originally by IBM for wiring together hardware devices, APIs and online services as part of the Internet of Things.

!!! warning
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.nodered.org/){: .header-icons } | [:octicons-link-16: Docs](https://www.nodered.org/docs/user-guide){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/node-red/node-red){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/nodered/node-red){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-node-red

```

### 2. URL

- To access node-red, visit `https://node-red._yourdomain.com_`

### 3. Setup

Addons and/or plugins can be installed to Node Red to add functionality. In Node Red they are called palettes. To install a palette, go to the menu in the upper right corner (the hamburger, 3 little horizontal lines), select `Manage palette`, then `Install`. You can search for a palette by name, or you can install a palette by pasting the URL of the palette into the `Install` tab.

Add this [palette](https://flows.nodered.org/node/node-red-contrib-home-assistant-websocket) to connect to [Home Assistant](../apps/homeassistant.md). (Requires Home Assistant to be installed and running, and HACS to be installed in Home Assistant.) For more information, see the Home Assistant page.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `node_red_instances`.

    === "Role-level Override"

        Applies to all instances of node_red:

        ```yaml
        node_red_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `node_red2`):

        ```yaml
        node_red2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `node_red_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `node_red_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`node_red_instances`"

        ```yaml
        # Type: list
        node_red_instances: ["node-red"]
        ```

        !!! example

            ```yaml
            # Type: list
            node_red_instances: ["node_red", "node_red2"]
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`node_red_role_paths_folder`"

            ```yaml
            # Type: string
            node_red_role_paths_folder: "{{ node_red_name }}"
            ```

        ??? variable string "`node_red_role_paths_location`"

            ```yaml
            # Type: string
            node_red_role_paths_location: "{{ server_appdata_path }}/{{ node_red_role_paths_folder }}"
            ```

    === "Instance-level"

        ??? variable string "`node_red2_paths_folder`"

            ```yaml
            # Type: string
            node_red2_paths_folder: "{{ node_red_name }}"
            ```

        ??? variable string "`node_red2_paths_location`"

            ```yaml
            # Type: string
            node_red2_paths_location: "{{ server_appdata_path }}/{{ node_red_role_paths_folder }}"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`node_red_role_web_subdomain`"

            ```yaml
            # Type: string
            node_red_role_web_subdomain: "{{ node_red_name }}"
            ```

        ??? variable string "`node_red_role_web_domain`"

            ```yaml
            # Type: string
            node_red_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`node_red_role_web_port`"

            ```yaml
            # Type: string
            node_red_role_web_port: "1880"
            ```

        ??? variable string "`node_red_role_web_url`"

            ```yaml
            # Type: string
            node_red_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='node_red') + '.' + lookup('role_var', '_web_domain', role='node_red')
                                    if (lookup('role_var', '_web_subdomain', role='node_red') | length > 0)
                                    else lookup('role_var', '_web_domain', role='node_red')) }}"
            ```

    === "Instance-level"

        ??? variable string "`node_red2_web_subdomain`"

            ```yaml
            # Type: string
            node_red2_web_subdomain: "{{ node_red_name }}"
            ```

        ??? variable string "`node_red2_web_domain`"

            ```yaml
            # Type: string
            node_red2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`node_red2_web_port`"

            ```yaml
            # Type: string
            node_red2_web_port: "1880"
            ```

        ??? variable string "`node_red2_web_url`"

            ```yaml
            # Type: string
            node_red2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='node_red') + '.' + lookup('role_var', '_web_domain', role='node_red')
                                if (lookup('role_var', '_web_subdomain', role='node_red') | length > 0)
                                else lookup('role_var', '_web_domain', role='node_red')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`node_red_role_dns_record`"

            ```yaml
            # Type: string
            node_red_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='node_red') }}"
            ```

        ??? variable string "`node_red_role_dns_zone`"

            ```yaml
            # Type: string
            node_red_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='node_red') }}"
            ```

        ??? variable bool "`node_red_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            node_red_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`node_red2_dns_record`"

            ```yaml
            # Type: string
            node_red2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='node_red') }}"
            ```

        ??? variable string "`node_red2_dns_zone`"

            ```yaml
            # Type: string
            node_red2_dns_zone: "{{ lookup('role_var', '_web_domain', role='node_red') }}"
            ```

        ??? variable bool "`node_red2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            node_red2_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`node_red_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            node_red_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`node_red_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            node_red_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`node_red_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            node_red_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`node_red_role_traefik_certresolver`"

            ```yaml
            # Type: string
            node_red_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`node_red_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            node_red_role_traefik_enabled: true
            ```

        ??? variable bool "`node_red_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            node_red_role_traefik_api_enabled: true
            ```

        ??? variable string "`node_red_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            node_red_role_traefik_api_endpoint: "PathPrefix(`/auth`) || PathPrefix(`/settings`) || PathPrefix(`/flows`) || PathPrefix(`/flow`) || PathPrefix(`/nodes`)"
            ```

    === "Instance-level"

        ??? variable string "`node_red2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            node_red2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`node_red2_traefik_middleware_default`"

            ```yaml
            # Type: string
            node_red2_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`node_red2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            node_red2_traefik_middleware_custom: ""
            ```

        ??? variable string "`node_red2_traefik_certresolver`"

            ```yaml
            # Type: string
            node_red2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`node_red2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            node_red2_traefik_enabled: true
            ```

        ??? variable bool "`node_red2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            node_red2_traefik_api_enabled: true
            ```

        ??? variable string "`node_red2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            node_red2_traefik_api_endpoint: "PathPrefix(`/auth`) || PathPrefix(`/settings`) || PathPrefix(`/flows`) || PathPrefix(`/flow`) || PathPrefix(`/nodes`)"
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`node_red_role_docker_container`"

            ```yaml
            # Type: string
            node_red_role_docker_container: "{{ node_red_name }}"
            ```

        ##### Image

        ??? variable bool "`node_red_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            node_red_role_docker_image_pull: true
            ```

        ??? variable string "`node_red_role_docker_image_repo`"

            ```yaml
            # Type: string
            node_red_role_docker_image_repo: "nodered/node-red"
            ```

        ??? variable string "`node_red_role_docker_image_tag`"

            ```yaml
            # Type: string
            node_red_role_docker_image_tag: "latest"
            ```

        ??? variable string "`node_red_role_docker_image`"

            ```yaml
            # Type: string
            node_red_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='node_red') }}:{{ lookup('role_var', '_docker_image_tag', role='node_red') }}"
            ```

        ##### Envs

        ??? variable dict "`node_red_role_docker_envs_default`"

            ```yaml
            # Type: dict
            node_red_role_docker_envs_default: 
              TZ: "{{ tz }}"
            ```

        ??? variable dict "`node_red_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            node_red_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`node_red_role_docker_volumes_default`"

            ```yaml
            # Type: list
            node_red_role_docker_volumes_default: 
              - "{{ lookup('role_var', '_paths_location', role='node_red') }}:/data"
            ```

        ??? variable list "`node_red_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            node_red_role_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`node_red_role_docker_hostname`"

            ```yaml
            # Type: string
            node_red_role_docker_hostname: "{{ node_red_name }}"
            ```

        ##### Networks

        ??? variable string "`node_red_role_docker_networks_alias`"

            ```yaml
            # Type: string
            node_red_role_docker_networks_alias: "{{ node_red_name }}"
            ```

        ??? variable list "`node_red_role_docker_networks_default`"

            ```yaml
            # Type: list
            node_red_role_docker_networks_default: []
            ```

        ??? variable list "`node_red_role_docker_networks_custom`"

            ```yaml
            # Type: list
            node_red_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`node_red_role_docker_restart_policy`"

            ```yaml
            # Type: string
            node_red_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`node_red_role_docker_state`"

            ```yaml
            # Type: string
            node_red_role_docker_state: started
            ```

        ##### User

        ??? variable string "`node_red_role_docker_user`"

            ```yaml
            # Type: string
            node_red_role_docker_user: "{{ uid }}:{{ gid }}"
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`node_red2_docker_container`"

            ```yaml
            # Type: string
            node_red2_docker_container: "{{ node_red_name }}"
            ```

        ##### Image

        ??? variable bool "`node_red2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            node_red2_docker_image_pull: true
            ```

        ??? variable string "`node_red2_docker_image_repo`"

            ```yaml
            # Type: string
            node_red2_docker_image_repo: "nodered/node-red"
            ```

        ??? variable string "`node_red2_docker_image_tag`"

            ```yaml
            # Type: string
            node_red2_docker_image_tag: "latest"
            ```

        ??? variable string "`node_red2_docker_image`"

            ```yaml
            # Type: string
            node_red2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='node_red') }}:{{ lookup('role_var', '_docker_image_tag', role='node_red') }}"
            ```

        ##### Envs

        ??? variable dict "`node_red2_docker_envs_default`"

            ```yaml
            # Type: dict
            node_red2_docker_envs_default: 
              TZ: "{{ tz }}"
            ```

        ??? variable dict "`node_red2_docker_envs_custom`"

            ```yaml
            # Type: dict
            node_red2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`node_red2_docker_volumes_default`"

            ```yaml
            # Type: list
            node_red2_docker_volumes_default: 
              - "{{ lookup('role_var', '_paths_location', role='node_red') }}:/data"
            ```

        ??? variable list "`node_red2_docker_volumes_custom`"

            ```yaml
            # Type: list
            node_red2_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`node_red2_docker_hostname`"

            ```yaml
            # Type: string
            node_red2_docker_hostname: "{{ node_red_name }}"
            ```

        ##### Networks

        ??? variable string "`node_red2_docker_networks_alias`"

            ```yaml
            # Type: string
            node_red2_docker_networks_alias: "{{ node_red_name }}"
            ```

        ??? variable list "`node_red2_docker_networks_default`"

            ```yaml
            # Type: list
            node_red2_docker_networks_default: []
            ```

        ??? variable list "`node_red2_docker_networks_custom`"

            ```yaml
            # Type: list
            node_red2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`node_red2_docker_restart_policy`"

            ```yaml
            # Type: string
            node_red2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`node_red2_docker_state`"

            ```yaml
            # Type: string
            node_red2_docker_state: started
            ```

        ##### User

        ??? variable string "`node_red2_docker_user`"

            ```yaml
            # Type: string
            node_red2_docker_user: "{{ uid }}:{{ gid }}"
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`node_red_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            node_red_role_autoheal_enabled: true
            ```

        ??? variable string "`node_red_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            node_red_role_depends_on: ""
            ```

        ??? variable string "`node_red_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            node_red_role_depends_on_delay: "0"
            ```

        ??? variable string "`node_red_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            node_red_role_depends_on_healthchecks:
            ```

        ??? variable bool "`node_red_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            node_red_role_diun_enabled: true
            ```

        ??? variable bool "`node_red_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            node_red_role_dns_enabled: true
            ```

        ??? variable bool "`node_red_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            node_red_role_docker_controller: true
            ```

        ??? variable bool "`node_red_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            node_red_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`node_red_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            node_red_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`node_red_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            node_red_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`node_red_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            node_red_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`node_red_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            node_red_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`node_red_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            node_red_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`node_red_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            node_red_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`node_red_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            node_red_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                node_red_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "node_red2.{{ user.domain }}"
                  - "node_red.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`node_red_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            node_red_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                node_red_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'node_red2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`node_red_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            node_red_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `node_red2`):

        ??? variable bool "`node_red2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            node_red2_autoheal_enabled: true
            ```

        ??? variable string "`node_red2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            node_red2_depends_on: ""
            ```

        ??? variable string "`node_red2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            node_red2_depends_on_delay: "0"
            ```

        ??? variable string "`node_red2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            node_red2_depends_on_healthchecks:
            ```

        ??? variable bool "`node_red2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            node_red2_diun_enabled: true
            ```

        ??? variable bool "`node_red2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            node_red2_dns_enabled: true
            ```

        ??? variable bool "`node_red2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            node_red2_docker_controller: true
            ```

        ??? variable bool "`node_red2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            node_red2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`node_red2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            node_red2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`node_red2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            node_red2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`node_red2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            node_red2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`node_red2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            node_red2_traefik_robot_enabled: true
            ```

        ??? variable bool "`node_red2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            node_red2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`node_red2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            node_red2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`node_red2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            node_red2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                node_red2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "node_red2.{{ user.domain }}"
                  - "node_red.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`node_red2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            node_red2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                node_red2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'node_red2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`node_red2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            node_red2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
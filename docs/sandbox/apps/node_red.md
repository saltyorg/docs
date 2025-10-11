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

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
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

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        node_red_instances: ["node-red"]

        ```

    === "Example"

        ```yaml
        # Type: list
        node_red_instances: ["node_red", "node_red2"]

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        node_red_role_paths_folder: "{{ node_red_name }}"

        # Type: string
        node_red_role_paths_location: "{{ server_appdata_path }}/{{ node_red_role_paths_folder }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        node_red2_paths_folder: "{{ node_red_name }}"

        # Type: string
        node_red2_paths_location: "{{ server_appdata_path }}/{{ node_red_role_paths_folder }}"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        node_red_role_web_subdomain: "{{ node_red_name }}"

        # Type: string
        node_red_role_web_domain: "{{ user.domain }}"

        # Type: string
        node_red_role_web_port: "1880"

        # Type: string
        node_red_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='node_red') + '.' + lookup('role_var', '_web_domain', role='node_red')
                                if (lookup('role_var', '_web_subdomain', role='node_red') | length > 0)
                                else lookup('role_var', '_web_domain', role='node_red')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        node_red2_web_subdomain: "{{ node_red_name }}"

        # Type: string
        node_red2_web_domain: "{{ user.domain }}"

        # Type: string
        node_red2_web_port: "1880"

        # Type: string
        node_red2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='node_red') + '.' + lookup('role_var', '_web_domain', role='node_red')
                            if (lookup('role_var', '_web_subdomain', role='node_red') | length > 0)
                            else lookup('role_var', '_web_domain', role='node_red')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        node_red_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='node_red') }}"

        # Type: string
        node_red_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='node_red') }}"

        # Type: bool (true/false)
        node_red_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        node_red2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='node_red') }}"

        # Type: string
        node_red2_dns_zone: "{{ lookup('role_var', '_web_domain', role='node_red') }}"

        # Type: bool (true/false)
        node_red2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        node_red_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        node_red_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        node_red_role_traefik_middleware_custom: ""

        # Type: string
        node_red_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        node_red_role_traefik_enabled: true

        # Type: bool (true/false)
        node_red_role_traefik_api_enabled: true

        # Type: string
        node_red_role_traefik_api_endpoint: "PathPrefix(`/auth`) || PathPrefix(`/settings`) || PathPrefix(`/flows`) || PathPrefix(`/flow`) || PathPrefix(`/nodes`)"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        node_red2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        node_red2_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        node_red2_traefik_middleware_custom: ""

        # Type: string
        node_red2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        node_red2_traefik_enabled: true

        # Type: bool (true/false)
        node_red2_traefik_api_enabled: true

        # Type: string
        node_red2_traefik_api_endpoint: "PathPrefix(`/auth`) || PathPrefix(`/settings`) || PathPrefix(`/flows`) || PathPrefix(`/flow`) || PathPrefix(`/nodes`)"

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        node_red_role_docker_container: "{{ node_red_name }}"

        # Image
        # Type: bool (true/false)
        node_red_role_docker_image_pull: true

        # Type: string
        node_red_role_docker_image_repo: "nodered/node-red"

        # Type: string
        node_red_role_docker_image_tag: "latest"

        # Type: string
        node_red_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='node_red') }}:{{ lookup('role_var', '_docker_image_tag', role='node_red') }}"

        # Envs
        # Type: dict
        node_red_role_docker_envs_default: 
          TZ: "{{ tz }}"

        # Type: dict
        node_red_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        node_red_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='node_red') }}:/data"

        # Type: list
        node_red_role_docker_volumes_custom: []

        # Hostname
        # Type: string
        node_red_role_docker_hostname: "{{ node_red_name }}"

        # Networks
        # Type: string
        node_red_role_docker_networks_alias: "{{ node_red_name }}"

        # Type: list
        node_red_role_docker_networks_default: []

        # Type: list
        node_red_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        node_red_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        node_red_role_docker_state: started

        # User
        # Type: string
        node_red_role_docker_user: "{{ uid }}:{{ gid }}"

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        node_red2_docker_container: "{{ node_red_name }}"

        # Image
        # Type: bool (true/false)
        node_red2_docker_image_pull: true

        # Type: string
        node_red2_docker_image_repo: "nodered/node-red"

        # Type: string
        node_red2_docker_image_tag: "latest"

        # Type: string
        node_red2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='node_red') }}:{{ lookup('role_var', '_docker_image_tag', role='node_red') }}"

        # Envs
        # Type: dict
        node_red2_docker_envs_default: 
          TZ: "{{ tz }}"

        # Type: dict
        node_red2_docker_envs_custom: {}

        # Volumes
        # Type: list
        node_red2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='node_red') }}:/data"

        # Type: list
        node_red2_docker_volumes_custom: []

        # Hostname
        # Type: string
        node_red2_docker_hostname: "{{ node_red_name }}"

        # Networks
        # Type: string
        node_red2_docker_networks_alias: "{{ node_red_name }}"

        # Type: list
        node_red2_docker_networks_default: []

        # Type: list
        node_red2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        node_red2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        node_red2_docker_state: started

        # User
        # Type: string
        node_red2_docker_user: "{{ uid }}:{{ gid }}"


        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        node_red_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        node_red_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        node_red_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        node_red_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        node_red_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        node_red_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        node_red_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        node_red_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        node_red_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        node_red_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        node_red_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        node_red_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        node_red_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        node_red_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        node_red_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        node_red_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        node_red_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            node_red_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "node_red2.{{ user.domain }}"
              - "node_red.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            node_red_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'node_red2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `node_red2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        node_red2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        node_red2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        node_red2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        node_red2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        node_red2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        node_red2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        node_red2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        node_red2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        node_red2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        node_red2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        node_red2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        node_red2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        node_red2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        node_red2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        node_red2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        node_red2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        node_red2_web_scheme:

        ```

        1.  Example:

            ```yaml
            node_red2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "node_red2.{{ user.domain }}"
              - "node_red.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            node_red2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'node_red2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

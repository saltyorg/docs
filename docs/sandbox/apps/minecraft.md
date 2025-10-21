---
tags:
  - Minecraft
---

# Minecraft

## What is it?

Run one or multiple minecraft servers with custom subdomains. Utilizes Minecraft server and MC-Router to allow each server to have its own subdomain with the default port.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://docker-minecraft-server.readthedocs.io/en/latest/){: .header-icons } | [:octicons-link-16: Docs](https://docker-minecraft-server.readthedocs.io/en/latest/commands/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/itzg/docker-minecraft-server){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-minecraft

```

This will install mc-router and the minecraft server. If you have listed multiple minecraft instances, it will install these too. (See below for multi server instructions)

### 2. Join Server

!!! warning "Cloudflare CDN"
    If you are using Cloudflare, you will need to disable the proxy for the subdomain(s) to work correctly. This can be done by clicking the orange cloud next to the subdomain in the DNS settings. Or specify it in the inventory using `minecraft_dns_proxy: false` if you have the global toggle on. Otherwise you won't be able to reach the minecraft server at all.

- By default, a single server will be accesible at  `minecraft._yourdomain.com_`
- If you have set up multiple instances, these will be accesible by default at `instanceName._yourdomain.com_` (See multi server instructions below)

### 3. Multi Server Set Up

To add multiple instances, add the following to the inventory. See the [inventory configuration instructions](../../saltbox/inventory/index.md).

``` yaml

minecraft_instances: ["mcserver1", "mcserver2"] # (1)!

```

1. This will install two servers, server1 and server2.

These servers will be accesible at `instanceName._yourdomain.com_`

So for the example above, `mcserver1._yourdomain.com_` and `mcserver2._yourdomain.com_`

### 4. Setup

For individual servers, you can change things such as memory using custom docker envs. See the [inventory configuration instructions](../../saltbox/inventory/index.md)

For a single install, the inventory vars will look like this `minecraft_docker_image_tag`.

When you have set up multiple servers, they will all use the `minecraft_docker_image_tag` settings as a default. To override this use the instance name instead. E.g `instanceName_docker_image_tag`.

``` yaml title="Inventory"

minecraft_instances: ["mcserver1", "mcserver2"] # (1)!
mcserver1_docker_image_tag: "itzg/minecraft-server:latest" # (2)!
mcserver2_docker_image_tag: "itzg/minecraft-server:1.17.1" # (3)!

```

1. This will install two servers, mcserver1 and mcserver2.
2. This will install the latest version of the minecraft server on mcserver1.
3. This will install version 1.17.1 of the minecraft server on mcserver2.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `minecraft_instances`.

    === "Role-level Override"

        Applies to all instances of minecraft:

        ```yaml
        minecraft_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `minecraft2`):

        ```yaml
        minecraft2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `minecraft_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `minecraft_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`minecraft_instances`"

        ```yaml
        # Type: list
        minecraft_instances: ["minecraft"]
        ```

        !!! example

            ```yaml
            # Type: list
            minecraft_instances: ["minecraft", "minecraft2"]
            ```

=== "Settings"

    === "Role-level"

        ??? variable bool "`minecraft_role_dynmap_router_enabled`"

            ```yaml
            # Type: bool (true/false)
            minecraft_role_dynmap_router_enabled: false
            ```

    === "Instance-level"

        ??? variable bool "`minecraft2_dynmap_router_enabled`"

            ```yaml
            # Type: bool (true/false)
            minecraft2_dynmap_router_enabled: false
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`minecraft_role_paths_folder`"

            ```yaml
            # Type: string
            minecraft_role_paths_folder: "minecraft"
            ```

        ??? variable string "`minecraft_role_paths_location`"

            ```yaml
            # Type: string
            minecraft_role_paths_location: "{{ server_appdata_path }}/{{ minecraft_role_paths_folder }}"
            ```

        ??? variable bool "`minecraft_role_paths_recursive`"

            ```yaml
            # Type: bool (true/false)
            minecraft_role_paths_recursive: true
            ```

    === "Instance-level"

        ??? variable string "`minecraft2_paths_folder`"

            ```yaml
            # Type: string
            minecraft2_paths_folder: "minecraft"
            ```

        ??? variable string "`minecraft2_paths_location`"

            ```yaml
            # Type: string
            minecraft2_paths_location: "{{ server_appdata_path }}/{{ minecraft_role_paths_folder }}"
            ```

        ??? variable bool "`minecraft2_paths_recursive`"

            ```yaml
            # Type: bool (true/false)
            minecraft2_paths_recursive: true
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`minecraft_role_web_subdomain`"

            ```yaml
            # Type: string
            minecraft_role_web_subdomain: "{{ minecraft_name }}"
            ```

        ??? variable string "`minecraft_role_web_domain`"

            ```yaml
            # Type: string
            minecraft_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`minecraft_role_web_port`"

            ```yaml
            # Dynmap
            # Type: string
            minecraft_role_web_port: "8123"
            ```

    === "Instance-level"

        ??? variable string "`minecraft2_web_subdomain`"

            ```yaml
            # Type: string
            minecraft2_web_subdomain: "{{ minecraft_name }}"
            ```

        ??? variable string "`minecraft2_web_domain`"

            ```yaml
            # Type: string
            minecraft2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`minecraft2_web_port`"

            ```yaml
            # Dynmap
            # Type: string
            minecraft2_web_port: "8123"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`minecraft_role_dns_record`"

            ```yaml
            # Type: string
            minecraft_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='minecraft') }}"
            ```

        ??? variable string "`minecraft_role_dns_zone`"

            ```yaml
            # Type: string
            minecraft_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='minecraft') }}"
            ```

        ??? variable bool "`minecraft_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            minecraft_role_dns_proxy: false
            ```

    === "Instance-level"

        ??? variable string "`minecraft2_dns_record`"

            ```yaml
            # Type: string
            minecraft2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='minecraft') }}"
            ```

        ??? variable string "`minecraft2_dns_zone`"

            ```yaml
            # Type: string
            minecraft2_dns_zone: "{{ lookup('role_var', '_web_domain', role='minecraft') }}"
            ```

        ??? variable bool "`minecraft2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            minecraft2_dns_proxy: false
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`minecraft_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            minecraft_role_traefik_sso_middleware: ""
            ```

        ??? variable string "`minecraft_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            minecraft_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`minecraft_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            minecraft_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`minecraft_role_traefik_certresolver`"

            ```yaml
            # Type: string
            minecraft_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable string "`minecraft_role_traefik_enabled`"

            ```yaml
            # Type: string
            minecraft_role_traefik_enabled: "{{ lookup('role_var', '_dynmap_router_enabled', role='minecraft') }}"
            ```

    === "Instance-level"

        ??? variable string "`minecraft2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            minecraft2_traefik_sso_middleware: ""
            ```

        ??? variable string "`minecraft2_traefik_middleware_default`"

            ```yaml
            # Type: string
            minecraft2_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`minecraft2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            minecraft2_traefik_middleware_custom: ""
            ```

        ??? variable string "`minecraft2_traefik_certresolver`"

            ```yaml
            # Type: string
            minecraft2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable string "`minecraft2_traefik_enabled`"

            ```yaml
            # Type: string
            minecraft2_traefik_enabled: "{{ lookup('role_var', '_dynmap_router_enabled', role='minecraft') }}"
            ```

=== "Ports"

    === "Role-level"

        ??? variable string "`minecraft_role_docker_ports_25565`"

            ```yaml
            # Type: string
            minecraft_role_docker_ports_25565: "{{ port_lookup_minecraft_tcp.meta.port
                                                if (port_lookup_minecraft_tcp.meta.port is defined) and (port_lookup_minecraft_tcp.meta.port | trim | length > 0)
                                                else '25565' }}"
            ```

    === "Instance-level"

        ??? variable string "`minecraft2_docker_ports_25565`"

            ```yaml
            # Type: string
            minecraft2_docker_ports_25565: "{{ port_lookup_minecraft_tcp.meta.port
                                            if (port_lookup_minecraft_tcp.meta.port is defined) and (port_lookup_minecraft_tcp.meta.port | trim | length > 0)
                                            else '25565' }}"
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`minecraft_role_docker_container`"

            ```yaml
            # Type: string
            minecraft_role_docker_container: "{{ minecraft_name }}"
            ```

        ##### Image

        ??? variable bool "`minecraft_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            minecraft_role_docker_image_pull: true
            ```

        ??? variable string "`minecraft_role_docker_image_repo`"

            ```yaml
            # Type: string
            minecraft_role_docker_image_repo: "itzg/minecraft-server"
            ```

        ??? variable string "`minecraft_role_docker_image_tag`"

            ```yaml
            # Type: string
            minecraft_role_docker_image_tag: "latest"
            ```

        ??? variable string "`minecraft_role_docker_image`"

            ```yaml
            # Type: string
            minecraft_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='minecraft') }}:{{ lookup('role_var', '_docker_image_tag', role='minecraft') }}"
            ```

        ##### Ports

        ??? variable list "`minecraft_role_docker_ports_defaults`"

            ```yaml
            # Type: list
            minecraft_role_docker_ports_defaults: 
              - "{{ lookup('role_var', '_docker_ports_25565', role='minecraft') }}:25565/tcp"
            ```

        ??? variable list "`minecraft_role_docker_ports_custom`"

            ```yaml
            # Type: list
            minecraft_role_docker_ports_custom: []
            ```

        ##### Envs

        ??? variable dict "`minecraft_role_docker_envs_default`"

            ```yaml
            # Type: dict
            minecraft_role_docker_envs_default: 
              TZ: "{{ tz }}"
              EULA: "TRUE"
              UID: "{{ uid }}"
              GID: "{{ gid }}"
            ```

        ??? variable dict "`minecraft_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            minecraft_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`minecraft_role_docker_volumes_default`"

            ```yaml
            # Type: list
            minecraft_role_docker_volumes_default: 
              - "{{ lookup('role_var', '_paths_location', role='minecraft') }}/{{ minecraft_name }}/data:/data"
            ```

        ??? variable list "`minecraft_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            minecraft_role_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`minecraft_role_docker_hostname`"

            ```yaml
            # Type: string
            minecraft_role_docker_hostname: "{{ minecraft_name }}"
            ```

        ##### Networks

        ??? variable string "`minecraft_role_docker_networks_alias`"

            ```yaml
            # Type: string
            minecraft_role_docker_networks_alias: "{{ minecraft_name }}"
            ```

        ??? variable list "`minecraft_role_docker_networks_default`"

            ```yaml
            # Type: list
            minecraft_role_docker_networks_default: []
            ```

        ??? variable list "`minecraft_role_docker_networks_custom`"

            ```yaml
            # Type: list
            minecraft_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`minecraft_role_docker_restart_policy`"

            ```yaml
            # Type: string
            minecraft_role_docker_restart_policy: unless-stopped
            ```

        ##### Stop Timeout

        ??? variable int "`minecraft_role_docker_stop_timeout`"

            ```yaml
            # Type: int
            minecraft_role_docker_stop_timeout: 900
            ```

        ##### State

        ??? variable string "`minecraft_role_docker_state`"

            ```yaml
            # Type: string
            minecraft_role_docker_state: started
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`minecraft2_docker_container`"

            ```yaml
            # Type: string
            minecraft2_docker_container: "{{ minecraft_name }}"
            ```

        ##### Image

        ??? variable bool "`minecraft2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            minecraft2_docker_image_pull: true
            ```

        ??? variable string "`minecraft2_docker_image_repo`"

            ```yaml
            # Type: string
            minecraft2_docker_image_repo: "itzg/minecraft-server"
            ```

        ??? variable string "`minecraft2_docker_image_tag`"

            ```yaml
            # Type: string
            minecraft2_docker_image_tag: "latest"
            ```

        ??? variable string "`minecraft2_docker_image`"

            ```yaml
            # Type: string
            minecraft2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='minecraft') }}:{{ lookup('role_var', '_docker_image_tag', role='minecraft') }}"
            ```

        ##### Ports

        ??? variable list "`minecraft2_docker_ports_defaults`"

            ```yaml
            # Type: list
            minecraft2_docker_ports_defaults: 
              - "{{ lookup('role_var', '_docker_ports_25565', role='minecraft') }}:25565/tcp"
            ```

        ??? variable list "`minecraft2_docker_ports_custom`"

            ```yaml
            # Type: list
            minecraft2_docker_ports_custom: []
            ```

        ##### Envs

        ??? variable dict "`minecraft2_docker_envs_default`"

            ```yaml
            # Type: dict
            minecraft2_docker_envs_default: 
              TZ: "{{ tz }}"
              EULA: "TRUE"
              UID: "{{ uid }}"
              GID: "{{ gid }}"
            ```

        ??? variable dict "`minecraft2_docker_envs_custom`"

            ```yaml
            # Type: dict
            minecraft2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`minecraft2_docker_volumes_default`"

            ```yaml
            # Type: list
            minecraft2_docker_volumes_default: 
              - "{{ lookup('role_var', '_paths_location', role='minecraft') }}/{{ minecraft_name }}/data:/data"
            ```

        ??? variable list "`minecraft2_docker_volumes_custom`"

            ```yaml
            # Type: list
            minecraft2_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`minecraft2_docker_hostname`"

            ```yaml
            # Type: string
            minecraft2_docker_hostname: "{{ minecraft_name }}"
            ```

        ##### Networks

        ??? variable string "`minecraft2_docker_networks_alias`"

            ```yaml
            # Type: string
            minecraft2_docker_networks_alias: "{{ minecraft_name }}"
            ```

        ??? variable list "`minecraft2_docker_networks_default`"

            ```yaml
            # Type: list
            minecraft2_docker_networks_default: []
            ```

        ??? variable list "`minecraft2_docker_networks_custom`"

            ```yaml
            # Type: list
            minecraft2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`minecraft2_docker_restart_policy`"

            ```yaml
            # Type: string
            minecraft2_docker_restart_policy: unless-stopped
            ```

        ##### Stop Timeout

        ??? variable int "`minecraft2_docker_stop_timeout`"

            ```yaml
            # Type: int
            minecraft2_docker_stop_timeout: 900
            ```

        ##### State

        ??? variable string "`minecraft2_docker_state`"

            ```yaml
            # Type: string
            minecraft2_docker_state: started
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`minecraft_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            minecraft_role_autoheal_enabled: true
            ```

        ??? variable string "`minecraft_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            minecraft_role_depends_on: ""
            ```

        ??? variable string "`minecraft_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            minecraft_role_depends_on_delay: "0"
            ```

        ??? variable string "`minecraft_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            minecraft_role_depends_on_healthchecks:
            ```

        ??? variable bool "`minecraft_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            minecraft_role_diun_enabled: true
            ```

        ??? variable bool "`minecraft_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            minecraft_role_dns_enabled: true
            ```

        ??? variable bool "`minecraft_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            minecraft_role_docker_controller: true
            ```

        ??? variable bool "`minecraft_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            minecraft_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`minecraft_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            minecraft_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`minecraft_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            minecraft_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`minecraft_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            minecraft_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`minecraft_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            minecraft_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`minecraft_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            minecraft_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`minecraft_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            minecraft_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`minecraft_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            minecraft_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                minecraft_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "minecraft2.{{ user.domain }}"
                  - "minecraft.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`minecraft_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            minecraft_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                minecraft_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'minecraft2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`minecraft_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            minecraft_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `minecraft2`):

        ??? variable bool "`minecraft2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            minecraft2_autoheal_enabled: true
            ```

        ??? variable string "`minecraft2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            minecraft2_depends_on: ""
            ```

        ??? variable string "`minecraft2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            minecraft2_depends_on_delay: "0"
            ```

        ??? variable string "`minecraft2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            minecraft2_depends_on_healthchecks:
            ```

        ??? variable bool "`minecraft2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            minecraft2_diun_enabled: true
            ```

        ??? variable bool "`minecraft2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            minecraft2_dns_enabled: true
            ```

        ??? variable bool "`minecraft2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            minecraft2_docker_controller: true
            ```

        ??? variable bool "`minecraft2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            minecraft2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`minecraft2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            minecraft2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`minecraft2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            minecraft2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`minecraft2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            minecraft2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`minecraft2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            minecraft2_traefik_robot_enabled: true
            ```

        ??? variable bool "`minecraft2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            minecraft2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`minecraft2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            minecraft2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`minecraft2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            minecraft2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                minecraft2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "minecraft2.{{ user.domain }}"
                  - "minecraft.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`minecraft2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            minecraft2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                minecraft2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'minecraft2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`minecraft2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            minecraft2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
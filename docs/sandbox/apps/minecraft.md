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

    ```yaml { .sb-show-on-unchecked title="Applies to all instances of minecraft:" }
    minecraft_role_web_subdomain: "custom"
    ```

    ```yaml { .sb-show-on-checked title="Applies to a specific instance (e.g., `minecraft2`):" }
    minecraft2_web_subdomain: "custom2"
    ```

<label class="md-button md-button--stretch" for="sb-checkbox--var-level">
   <input type="checkbox" id="sb-checkbox--var-level"><span class="sb-show-on-unchecked">Show instance-level variables</span><span class="sb-show-on-checked">Show role-level variables</span>
</label>

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `minecraft_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `minecraft_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`minecraft_instances`"

        ```yaml
        # Type: list
        minecraft_instances: ["minecraft"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            minecraft_instances: ["minecraft", "minecraft2"]
            ```

=== "Settings"

    ??? variable bool "`minecraft_role_dynmap_router_enabled`{ .sb-show-on-unchecked }`minecraft2_dynmap_router_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        minecraft_role_dynmap_router_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        minecraft2_dynmap_router_enabled: false
        ```

=== "Paths"

    ??? variable string "`minecraft_role_paths_folder`{ .sb-show-on-unchecked }`minecraft2_paths_folder`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_paths_folder: "minecraft"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_paths_folder: "minecraft"
        ```

    ??? variable string "`minecraft_role_paths_location`{ .sb-show-on-unchecked }`minecraft2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_paths_location: "{{ server_appdata_path }}/{{ minecraft_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_paths_location: "{{ server_appdata_path }}/{{ minecraft_role_paths_folder }}"
        ```

    ??? variable bool "`minecraft_role_paths_recursive`{ .sb-show-on-unchecked }`minecraft2_paths_recursive`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        minecraft_role_paths_recursive: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        minecraft2_paths_recursive: true
        ```

=== "Web"

    ??? variable string "`minecraft_role_web_subdomain`{ .sb-show-on-unchecked }`minecraft2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_web_subdomain: "{{ minecraft_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_web_subdomain: "{{ minecraft_name }}"
        ```

    ??? variable string "`minecraft_role_web_domain`{ .sb-show-on-unchecked }`minecraft2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`minecraft_role_web_port`{ .sb-show-on-unchecked }`minecraft2_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Dynmap
        # Type: string
        minecraft_role_web_port: "8123"
        ```

        ```yaml { .sb-show-on-checked }
        # Dynmap
        # Type: string
        minecraft2_web_port: "8123"
        ```

=== "DNS"

    ??? variable string "`minecraft_role_dns_record`{ .sb-show-on-unchecked }`minecraft2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='minecraft') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='minecraft') }}"
        ```

    ??? variable string "`minecraft_role_dns_zone`{ .sb-show-on-unchecked }`minecraft2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='minecraft') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_dns_zone: "{{ lookup('role_var', '_web_domain', role='minecraft') }}"
        ```

    ??? variable bool "`minecraft_role_dns_proxy`{ .sb-show-on-unchecked }`minecraft2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        minecraft_role_dns_proxy: false
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        minecraft2_dns_proxy: false
        ```

=== "Traefik"

    ??? variable string "`minecraft_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`minecraft2_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_traefik_sso_middleware: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_traefik_sso_middleware: ""
        ```

    ??? variable string "`minecraft_role_traefik_middleware_default`{ .sb-show-on-unchecked }`minecraft2_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`minecraft_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`minecraft2_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_traefik_middleware_custom: ""
        ```

    ??? variable string "`minecraft_role_traefik_certresolver`{ .sb-show-on-unchecked }`minecraft2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable string "`minecraft_role_traefik_enabled`{ .sb-show-on-unchecked }`minecraft2_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_traefik_enabled: "{{ lookup('role_var', '_dynmap_router_enabled', role='minecraft') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_traefik_enabled: "{{ lookup('role_var', '_dynmap_router_enabled', role='minecraft') }}"
        ```

=== "Ports"

    ??? variable string "`minecraft_role_docker_ports_25565`{ .sb-show-on-unchecked }`minecraft2_docker_ports_25565`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_docker_ports_25565: "{{ port_lookup_minecraft_tcp.meta.port
                                            if (port_lookup_minecraft_tcp.meta.port is defined) and (port_lookup_minecraft_tcp.meta.port | trim | length > 0)
                                            else '25565' }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_docker_ports_25565: "{{ port_lookup_minecraft_tcp.meta.port
                                        if (port_lookup_minecraft_tcp.meta.port is defined) and (port_lookup_minecraft_tcp.meta.port | trim | length > 0)
                                        else '25565' }}"
        ```

=== "Docker"

    Container
    { .sb-h5 }

    ??? variable string "`minecraft_role_docker_container`{ .sb-show-on-unchecked }`minecraft2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_docker_container: "{{ minecraft_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_docker_container: "{{ minecraft_name }}"
        ```

    Image
    { .sb-h5 }

    ??? variable bool "`minecraft_role_docker_image_pull`{ .sb-show-on-unchecked }`minecraft2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        minecraft_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        minecraft2_docker_image_pull: true
        ```

    ??? variable string "`minecraft_role_docker_image_repo`{ .sb-show-on-unchecked }`minecraft2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_docker_image_repo: "itzg/minecraft-server"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_docker_image_repo: "itzg/minecraft-server"
        ```

    ??? variable string "`minecraft_role_docker_image_tag`{ .sb-show-on-unchecked }`minecraft2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_docker_image_tag: "latest"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_docker_image_tag: "latest"
        ```

    ??? variable string "`minecraft_role_docker_image`{ .sb-show-on-unchecked }`minecraft2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='minecraft') }}:{{ lookup('role_var', '_docker_image_tag', role='minecraft') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='minecraft') }}:{{ lookup('role_var', '_docker_image_tag', role='minecraft') }}"
        ```

    Ports
    { .sb-h5 }

    ??? variable list "`minecraft_role_docker_ports_defaults`{ .sb-show-on-unchecked }`minecraft2_docker_ports_defaults`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        minecraft_role_docker_ports_defaults: 
          - "{{ lookup('role_var', '_docker_ports_25565', role='minecraft') }}:25565/tcp"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        minecraft2_docker_ports_defaults: 
          - "{{ lookup('role_var', '_docker_ports_25565', role='minecraft') }}:25565/tcp"
        ```

    ??? variable list "`minecraft_role_docker_ports_custom`{ .sb-show-on-unchecked }`minecraft2_docker_ports_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        minecraft_role_docker_ports_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        minecraft2_docker_ports_custom: []
        ```

    Envs
    { .sb-h5 }

    ??? variable dict "`minecraft_role_docker_envs_default`{ .sb-show-on-unchecked }`minecraft2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        minecraft_role_docker_envs_default: 
          TZ: "{{ tz }}"
          EULA: "TRUE"
          UID: "{{ uid }}"
          GID: "{{ gid }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        minecraft2_docker_envs_default: 
          TZ: "{{ tz }}"
          EULA: "TRUE"
          UID: "{{ uid }}"
          GID: "{{ gid }}"
        ```

    ??? variable dict "`minecraft_role_docker_envs_custom`{ .sb-show-on-unchecked }`minecraft2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        minecraft_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        minecraft2_docker_envs_custom: {}
        ```

    Volumes
    { .sb-h5 }

    ??? variable list "`minecraft_role_docker_volumes_default`{ .sb-show-on-unchecked }`minecraft2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        minecraft_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='minecraft') }}/{{ minecraft_name }}/data:/data"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        minecraft2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='minecraft') }}/{{ minecraft_name }}/data:/data"
        ```

    ??? variable list "`minecraft_role_docker_volumes_custom`{ .sb-show-on-unchecked }`minecraft2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        minecraft_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        minecraft2_docker_volumes_custom: []
        ```

    Hostname
    { .sb-h5 }

    ??? variable string "`minecraft_role_docker_hostname`{ .sb-show-on-unchecked }`minecraft2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_docker_hostname: "{{ minecraft_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_docker_hostname: "{{ minecraft_name }}"
        ```

    Networks
    { .sb-h5 }

    ??? variable string "`minecraft_role_docker_networks_alias`{ .sb-show-on-unchecked }`minecraft2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_docker_networks_alias: "{{ minecraft_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_docker_networks_alias: "{{ minecraft_name }}"
        ```

    ??? variable list "`minecraft_role_docker_networks_default`{ .sb-show-on-unchecked }`minecraft2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        minecraft_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        minecraft2_docker_networks_default: []
        ```

    ??? variable list "`minecraft_role_docker_networks_custom`{ .sb-show-on-unchecked }`minecraft2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        minecraft_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        minecraft2_docker_networks_custom: []
        ```

    Restart Policy
    { .sb-h5 }

    ??? variable string "`minecraft_role_docker_restart_policy`{ .sb-show-on-unchecked }`minecraft2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_docker_restart_policy: unless-stopped
        ```

    Stop Timeout
    { .sb-h5 }

    ??? variable int "`minecraft_role_docker_stop_timeout`{ .sb-show-on-unchecked }`minecraft2_docker_stop_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        minecraft_role_docker_stop_timeout: 900
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        minecraft2_docker_stop_timeout: 900
        ```

    State
    { .sb-h5 }

    ??? variable string "`minecraft_role_docker_state`{ .sb-show-on-unchecked }`minecraft2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        minecraft_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        minecraft2_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`minecraft_role_autoheal_enabled`{ .sb-show-on-unchecked }`minecraft2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        minecraft_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        minecraft2_autoheal_enabled: true
        ```

    ??? variable string "`minecraft_role_depends_on`{ .sb-show-on-unchecked }`minecraft2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        minecraft_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        minecraft2_depends_on: ""
        ```

    ??? variable string "`minecraft_role_depends_on_delay`{ .sb-show-on-unchecked }`minecraft2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        minecraft_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        minecraft2_depends_on_delay: "0"
        ```

    ??? variable string "`minecraft_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`minecraft2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        minecraft_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        minecraft2_depends_on_healthchecks:
        ```

    ??? variable bool "`minecraft_role_diun_enabled`{ .sb-show-on-unchecked }`minecraft2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        minecraft_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        minecraft2_diun_enabled: true
        ```

    ??? variable bool "`minecraft_role_dns_enabled`{ .sb-show-on-unchecked }`minecraft2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        minecraft_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        minecraft2_dns_enabled: true
        ```

    ??? variable bool "`minecraft_role_docker_controller`{ .sb-show-on-unchecked }`minecraft2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        minecraft_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        minecraft2_docker_controller: true
        ```

    ??? variable bool "`minecraft_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`minecraft2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        minecraft_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        minecraft2_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`minecraft_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`minecraft2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        minecraft_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        minecraft2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`minecraft_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`minecraft2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        minecraft_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        minecraft2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`minecraft_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`minecraft2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        minecraft_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        minecraft2_traefik_gzip_enabled: false
        ```

    ??? variable bool "`minecraft_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`minecraft2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        minecraft_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        minecraft2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`minecraft_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`minecraft2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        minecraft_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        minecraft2_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`minecraft_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`minecraft2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        minecraft_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        minecraft2_traefik_robot_enabled: true
        ```

    ??? variable bool "`minecraft_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`minecraft2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        minecraft_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        minecraft2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`minecraft_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`minecraft2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        minecraft_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        minecraft2_traefik_wildcard_enabled: true
        ```

    ??? variable list "`minecraft_role_web_fqdn_override`{ .sb-show-on-unchecked }`minecraft2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        minecraft_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        minecraft2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            minecraft_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "minecraft2.{{ user.domain }}"
              - "minecraft.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            minecraft2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "minecraft2.{{ user.domain }}"
              - "minecraft.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`minecraft_role_web_host_override`{ .sb-show-on-unchecked }`minecraft2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        minecraft_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        minecraft2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            minecraft_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'minecraft2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            minecraft2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'minecraft2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`minecraft_role_web_scheme`{ .sb-show-on-unchecked }`minecraft2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        minecraft_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        minecraft2_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
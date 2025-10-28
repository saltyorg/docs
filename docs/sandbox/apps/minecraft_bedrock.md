---
tags:
  - Minecraft
---

# Minecraft Bedrock

## What is it?

[Minecraft Bedrock](https://github.com/itzg/docker-minecraft-bedrock-server) is a server for the multi-platform version of Minecraft.

!!! note
    📢 This server will expose the port UDP 19132

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/itzg/docker-minecraft-bedrock-server){: .header-icons } | [:octicons-link-16: Docs](https://github.com/itzg/docker-minecraft-bedrock-server){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/itzg/docker-minecraft-bedrock-server){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/itzg/minecraft-bedrock-server){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-minecraft-bedrock

```

### 2. Join Server

- The server will be accessible at `minecraft-bedrock.xYOUR_DOMAIN_NAMEx` or `_yourserverip_:19132`

!!! warning "Cloudflare CDN"
    If you are using Cloudflare, you will need to disable the proxy for the subdomain(s) to work correctly. This can be done by clicking the orange cloud next to the subdomain in the DNS settings. Or specify it in the inventory using `minecraft-bedrock_dns_proxy: false` if you have the global toggle on. Otherwise you won't be able to reach the minecraft server at all.

### Change server version

By default, the server will be using the latest version available. To choose a specific version add `minecraft_bedrock_version: "1.19.31"` to the [inventory system](../../saltbox/inventory/index.md).

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    minecraft_bedrock_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `minecraft_bedrock_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `minecraft_bedrock_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`minecraft_bedrock_name`"

        ```yaml
        # Type: string
        minecraft_bedrock_name: minecraft-bedrock
        ```

=== "Settings"

    ??? variable string "`minecraft_bedrock_role_version`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_version: "LATEST"
        ```

=== "Paths"

    ??? variable string "`minecraft_bedrock_role_paths_folder`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_paths_folder: "{{ minecraft_bedrock_name }}"
        ```

    ??? variable string "`minecraft_bedrock_role_paths_location`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_paths_location: "{{ server_appdata_path }}/{{ minecraft_bedrock_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`minecraft_bedrock_role_web_subdomain`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_web_subdomain: "{{ minecraft_bedrock_name }}"
        ```

    ??? variable string "`minecraft_bedrock_role_web_domain`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_web_domain: "{{ user.domain }}"
        ```

=== "DNS"

    ??? variable string "`minecraft_bedrock_role_dns_record`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='minecraft_bedrock') }}"
        ```

    ??? variable string "`minecraft_bedrock_role_dns_zone`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='minecraft_bedrock') }}"
        ```

    ??? variable bool "`minecraft_bedrock_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_dns_proxy: false
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`minecraft_bedrock_role_docker_container`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_container: "{{ minecraft_bedrock_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`minecraft_bedrock_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_docker_image_pull: true
        ```

    ??? variable string "`minecraft_bedrock_role_docker_image_tag`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_image_tag: "latest"
        ```

    ??? variable string "`minecraft_bedrock_role_docker_image_repo`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_image_repo: "itzg/minecraft-bedrock-server"
        ```

    ??? variable string "`minecraft_bedrock_role_docker_image`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='minecraft_bedrock') }}:{{ lookup('role_var', '_docker_image_tag', role='minecraft_bedrock') }}"
        ```

    <h5>Ports</h5>

    ??? variable list "`minecraft_bedrock_role_docker_ports_defaults`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_ports_defaults: 
          - "19132:19132/udp"
        ```

    ??? variable list "`minecraft_bedrock_role_docker_ports_custom`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    ??? variable dict "`minecraft_bedrock_role_docker_envs_default`"

        ```yaml
        # Type: dict
        minecraft_bedrock_role_docker_envs_default: 
          TZ: "{{ tz }}"
          UID: "{{ uid }}"
          GID: "{{ gid }}"
          EULA: "TRUE"
          VERSION: "{{ lookup('role_var', '_version', role='minecraft_bedrock') }}"
        ```

    ??? variable dict "`minecraft_bedrock_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        minecraft_bedrock_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`minecraft_bedrock_role_docker_volumes_default`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='minecraft_bedrock') }}:/data"
        ```

    ??? variable list "`minecraft_bedrock_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`minecraft_bedrock_role_docker_hostname`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_hostname: "{{ minecraft_bedrock_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`minecraft_bedrock_role_docker_networks_alias`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_networks_alias: "{{ minecraft_bedrock_name }}"
        ```

    ??? variable list "`minecraft_bedrock_role_docker_networks_default`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_networks_default: []
        ```

    ??? variable list "`minecraft_bedrock_role_docker_networks_custom`"

        ```yaml
        # Type: list
        minecraft_bedrock_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`minecraft_bedrock_role_docker_restart_policy`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`minecraft_bedrock_role_docker_state`"

        ```yaml
        # Type: string
        minecraft_bedrock_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`minecraft_bedrock_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        minecraft_bedrock_role_autoheal_enabled: true
        ```

    ??? variable string "`minecraft_bedrock_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        minecraft_bedrock_role_depends_on: ""
        ```

    ??? variable string "`minecraft_bedrock_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        minecraft_bedrock_role_depends_on_delay: "0"
        ```

    ??? variable string "`minecraft_bedrock_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        minecraft_bedrock_role_depends_on_healthchecks:
        ```

    ??? variable bool "`minecraft_bedrock_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        minecraft_bedrock_role_diun_enabled: true
        ```

    ??? variable bool "`minecraft_bedrock_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        minecraft_bedrock_role_dns_enabled: true
        ```

    ??? variable bool "`minecraft_bedrock_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        minecraft_bedrock_role_docker_controller: true
        ```

    ??? variable bool "`minecraft_bedrock_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        minecraft_bedrock_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`minecraft_bedrock_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        minecraft_bedrock_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`minecraft_bedrock_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        minecraft_bedrock_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`minecraft_bedrock_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        minecraft_bedrock_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`minecraft_bedrock_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`minecraft_bedrock_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        minecraft_bedrock_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`minecraft_bedrock_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        minecraft_bedrock_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`minecraft_bedrock_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        minecraft_bedrock_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`minecraft_bedrock_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        minecraft_bedrock_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`minecraft_bedrock_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        minecraft_bedrock_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            minecraft_bedrock_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "minecraft_bedrock2.{{ user.domain }}"
              - "minecraft_bedrock.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`minecraft_bedrock_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        minecraft_bedrock_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            minecraft_bedrock_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'minecraft_bedrock2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`minecraft_bedrock_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        minecraft_bedrock_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
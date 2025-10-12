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

- The server will be accessible at `minecraft-bedrock._yourdomain.com_` or `_yourserverip_:19132`

!!! warning "Cloudflare CDN"
    If you are using Cloudflare, you will need to disable the proxy for the subdomain(s) to work correctly. This can be done by clicking the orange cloud next to the subdomain in the DNS settings. Or specify it in the inventory using `minecraft-bedrock_dns_proxy: false` if you have the global toggle on. Otherwise you won't be able to reach the minecraft server at all.

### Change server version

By default, the server will be using the latest version available. To choose a specific version add `minecraft_bedrock_version: "1.19.31"` to the [inventory system](../../saltbox/inventory/index.md).

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        minecraft_bedrock_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `minecraft_bedrock_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `minecraft_bedrock_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    minecraft_bedrock_name: minecraft-bedrock

    ```

??? example "Settings"

    ```yaml
    # Type: string
    minecraft_bedrock_role_version: "LATEST"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    minecraft_bedrock_role_paths_folder: "{{ minecraft_bedrock_name }}"

    # Type: string
    minecraft_bedrock_role_paths_location: "{{ server_appdata_path }}/{{ minecraft_bedrock_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    minecraft_bedrock_role_web_subdomain: "{{ minecraft_bedrock_name }}"

    # Type: string
    minecraft_bedrock_role_web_domain: "{{ user.domain }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    minecraft_bedrock_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='minecraft_bedrock') }}"

    # Type: string
    minecraft_bedrock_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='minecraft_bedrock') }}"

    # Type: bool (true/false)
    minecraft_bedrock_role_dns_proxy: false

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    minecraft_bedrock_role_docker_container: "{{ minecraft_bedrock_name }}"

    # Image
    # Type: bool (true/false)
    minecraft_bedrock_role_docker_image_pull: true

    # Type: string
    minecraft_bedrock_role_docker_image_tag: "latest"

    # Type: string
    minecraft_bedrock_role_docker_image_repo: "itzg/minecraft-bedrock-server"

    # Type: string
    minecraft_bedrock_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='minecraft_bedrock') }}:{{ lookup('role_var', '_docker_image_tag', role='minecraft_bedrock') }}"

    # Ports
    # Type: list
    minecraft_bedrock_role_docker_ports_defaults: 
      - "19132:19132/udp"

    # Type: list
    minecraft_bedrock_role_docker_ports_custom: []

    # Envs
    # Type: dict
    minecraft_bedrock_role_docker_envs_default: 
      TZ: "{{ tz }}"
      UID: "{{ uid }}"
      GID: "{{ gid }}"
      EULA: "TRUE"
      VERSION: "{{ lookup('role_var', '_version', role='minecraft_bedrock') }}"

    # Type: dict
    minecraft_bedrock_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    minecraft_bedrock_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='minecraft_bedrock') }}:/data"

    # Type: list
    minecraft_bedrock_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    minecraft_bedrock_role_docker_hostname: "{{ minecraft_bedrock_name }}"

    # Networks
    # Type: string
    minecraft_bedrock_role_docker_networks_alias: "{{ minecraft_bedrock_name }}"

    # Type: list
    minecraft_bedrock_role_docker_networks_default: []

    # Type: list
    minecraft_bedrock_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    minecraft_bedrock_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    minecraft_bedrock_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    minecraft_bedrock_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    minecraft_bedrock_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    minecraft_bedrock_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    minecraft_bedrock_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    minecraft_bedrock_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    minecraft_bedrock_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    minecraft_bedrock_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    minecraft_bedrock_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    minecraft_bedrock_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    minecraft_bedrock_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    minecraft_bedrock_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    minecraft_bedrock_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    minecraft_bedrock_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    minecraft_bedrock_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    minecraft_bedrock_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    minecraft_bedrock_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    minecraft_bedrock_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        minecraft_bedrock_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "minecraft_bedrock2.{{ user.domain }}"
          - "minecraft_bedrock.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        minecraft_bedrock_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'minecraft_bedrock2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
hide:
  - tags
tags:
  - tdarr-node
  - media
  - encoding
---

# Tdarr Node

## What is it?

[Tdarr Node](https://tdarr.io/) is a cross-platform conditional based transcoding application for automating media library transcode/remux management in order to process your media files as required.

- Node is described as: Processes running same/other devices which collect tasks from the Server.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://tdarr.io/){: .header-icons } | [:octicons-link-16: Docs](https://docs.tdarr.io/docs/installation/getting-started){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/HaveAGitGat/Tdarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/haveagitgat/tdarr){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-tdarr-node

```

### 2. Usage

The Tdarr Node is configured with the following defaults which can be modified via the inventory system.

``` yaml
tdarr_node_server_ip: "tdarr"
tdarr_node_server_port: "8266"
tdarr_node_node_id: "MainNode"
tdarr_node_node_port: "8267"
tdarr_node_external: false
```

By switching `tdarr_node_external` to `true` the node will be accessible externally via the specified `tdarr_node_node_port` on any hostname or IP address pointing directly to the server.

To connect the Tdarr node to a Tdarr server, set `tdarr_node_server_ip` and `tdarr_node_server_port` to the IP/hostname and port of the exposed Tdarr server.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        tdarr_node_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `tdarr_node_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `tdarr_node_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    tdarr_node_name: tdarr-node

    ```

??? example "Settings"

    ```yaml
    # Type: string
    tdarr_node_server_ip: "tdarr"

    # Type: string
    tdarr_node_server_port: "8266"

    # Type: string
    tdarr_node_node_id: "MainNode"

    # Type: string
    tdarr_node_node_port: "8267"

    # Type: bool (true/false)
    tdarr_node_external: false

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    tdarr_node_role_docker_container: "{{ tdarr_node_name }}"

    # Image
    # Type: bool (true/false)
    tdarr_node_role_docker_image_pull: true

    # Type: string
    tdarr_node_role_docker_image_repo: "haveagitgat/tdarr_node"

    # Type: string
    tdarr_node_role_docker_image_tag: "latest"

    # Type: string
    tdarr_node_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='tdarr_node') }}:{{ lookup('role_var', '_docker_image_tag', role='tdarr_node') }}"

    # Ports
    # Type: list
    tdarr_node_role_docker_ports_defaults: 
      - "{{ tdarr_node_node_port }}:{{ tdarr_node_node_port }}"

    # Type: list
    tdarr_node_role_docker_ports_custom: []

    # Envs
    # Type: dict
    tdarr_node_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"
      serverIP: "{{ tdarr_node_server_ip }}"
      serverPort: "{{ tdarr_node_server_port }}"
      nodeName: "{{ tdarr_node_node_id }}"
      inContainer: "true"

    # Type: dict
    tdarr_node_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    tdarr_node_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_configs_location', role='tdarr') }}:/app/configs"
      - "{{ lookup('role_var', '_paths_logs_location', role='tdarr') }}:/app/logs"
      - "{{ lookup('role_var', '_paths_transcodes_location', role='tdarr') }}:/temp"
      - "/mnt/unionfs/Media:/media"
      - "/mnt/unionfs/Media/Movies:/movies"
      - "/mnt/unionfs/Media/TV:/tv"
      - "/dev/shm:/dev/shm"

    # Type: list
    tdarr_node_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    tdarr_node_role_docker_hostname: "{{ tdarr_node_name }}"

    # Networks
    # Type: string
    tdarr_node_role_docker_networks_alias: "{{ tdarr_node_name }}"

    # Type: list
    tdarr_node_role_docker_networks_default: []

    # Type: list
    tdarr_node_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    tdarr_node_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    tdarr_node_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    tdarr_node_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    tdarr_node_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    tdarr_node_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    tdarr_node_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    tdarr_node_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    tdarr_node_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    tdarr_node_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    tdarr_node_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    tdarr_node_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    tdarr_node_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    tdarr_node_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    tdarr_node_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    tdarr_node_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    tdarr_node_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    tdarr_node_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    tdarr_node_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    tdarr_node_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        tdarr_node_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "tdarr_node2.{{ user.domain }}"
          - "tdarr_node.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        tdarr_node_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'tdarr_node2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

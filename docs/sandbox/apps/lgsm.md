---
hide:
  - tags
tags:
  - lgsm
  - gaming
  - server
---

# LinuxGSM

## What is it?

[LinuxGSM](https://linuxgsm.com) is a command-line tool for quick and simple deployment and management of Linux dedicated game servers. It aims to make the process of managing game servers hassle-free. With LinuxGSM, we can avoid spending hours trying to configure and manage game servers. It provides a streamlined and efficient solution for setting up and maintaining dedicated game servers on Linux.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://linuxgsm.com){: .header-icons } | [:octicons-link-16: Docs](https://docs.linuxgsm.com){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/GameServerManagers/LinuxGSM){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/gameservermanagers/gameserver){: .header-icons }|

### 1. Installation

To add instances, add the following to the inventory. See these instructions on inventory [here](../../saltbox/inventory/index.md).

``` yaml title="Inventory"

lgsm_instances: ["lgsm_valheim", "lgsm_rust"] # (1)!
lgsm_valheim_docker_image_tag: "vh" # (2)!
lgsm_valheim_docker_ports_defaults: ["2456:2456/udp","2457:2457/udp"] # (3)!
lgsm_rust_docker_ports_defaults: ["28015:28015/udp","28017:28017/udp","28082:28082/udp"] # (4)!

```

1. Example setting image tag to correct shortcode from <https://github.com/GameServerManagers/LinuxGSM/blob/master/lgsm/data/serverlist.csv> using lgsm_shortcode will automatically pull the correct image tag
2. This is the valheim server shortcode
3. ports for valheim need to be exposed. Notice that rust is the image tag for the rust server. This means we don't have to specify it here.
4. The ports for the rust server need to be exposed as well.

Then run:

``` shell

sb install sandbox-lgsm

```

This will start the installation of LinuxGSM using the specified image tag per instance, which allows for the installation and management of multiple game servers.

### 2. Setup

LinuxGSM config files are the configuration files used by the game server to store various game server settings, such as the server name, maximum players, map cycle, etc. These settings can be edited to customise a game server. Different game server configs can use different syntax and work slightly differently, but all do the same basic job of editing a game server settings.

The configs for the lgsm servers are in `/opt/CONTAINERNAME/config-lgsm/LGSMSERVERNAME/`
For our valheim example the config would be `/opt/lgsm_valheim/config-lgsm/vhserver/vhserver.cfg` which is the lgsm instance config for that server.

`/opt/lgsm_valheim/config-lgsm/vhserver/common.cfg` works as well. Can read more [here](https://docs.linuxgsm.com/configuration/game-server-config)

Any actual game server configs will be in the `/opt/CONTAINERNAME/serverfiles/` and are all dependant on the game server installed.

### 3. Join Server

In your game, connect to your ip and default ports for the server. Make sure you set the UDP and TCP for the ports correctly. If everything was setup correctly the game should connect to the server.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `lgsm_instances`.

    === "Role-level Override"

        Applies to all instances of lgsm:

        ```yaml
        lgsm_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `lgsm2`):

        ```yaml
        lgsm2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `lgsm_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `lgsm_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        lgsm_instances: []

        ```

    === "Example"

        ```yaml
        # Type: list
        lgsm_instances: ["lgsm", "lgsm2"]

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        lgsm_role_paths_folder: "{{ lgsm_name }}"

        # Type: string
        lgsm_role_paths_location: "{{ server_appdata_path }}/{{ lgsm_role_paths_folder }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        lgsm2_paths_folder: "{{ lgsm_name }}"

        # Type: string
        lgsm2_paths_location: "{{ server_appdata_path }}/{{ lgsm_role_paths_folder }}"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        lgsm_role_web_subdomain: "{{ lgsm_name }}"

        # Type: string
        lgsm_role_web_domain: "{{ user.domain }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        lgsm2_web_subdomain: "{{ lgsm_name }}"

        # Type: string
        lgsm2_web_domain: "{{ user.domain }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        lgsm_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='lgsm') }}"

        # Type: string
        lgsm_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='lgsm') }}"

        # Type: bool (true/false)
        lgsm_role_dns_proxy: false

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        lgsm2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='lgsm') }}"

        # Type: string
        lgsm2_dns_zone: "{{ lookup('role_var', '_web_domain', role='lgsm') }}"

        # Type: bool (true/false)
        lgsm2_dns_proxy: false

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        lgsm_role_docker_container: "{{ lgsm_name }}"

        # Image
        # Type: bool (true/false)
        lgsm_role_docker_image_pull: true

        # Type: string
        lgsm_role_docker_image_repo: "gameservermanagers/gameserver"

        # Type: string
        lgsm_role_docker_image_tag: "{{ lgsm_name | replace('lgsm_', '') }}"

        # Type: string
        lgsm_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='lgsm') }}:{{ lookup('role_var', '_docker_image_tag', role='lgsm') }}"

        # Volumes
        # Type: list
        lgsm_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='lgsm') }}:/data"

        # Type: list
        lgsm_role_docker_volumes_custom: []

        # Hostname
        # Type: string
        lgsm_role_docker_hostname: "{{ lgsm_name }}"

        # Networks
        # Type: string
        lgsm_role_docker_networks_alias: "{{ lgsm_name }}"

        # Type: list
        lgsm_role_docker_networks_default: []

        # Type: list
        lgsm_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        lgsm_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        lgsm_role_docker_state: started

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        lgsm2_docker_container: "{{ lgsm_name }}"

        # Image
        # Type: bool (true/false)
        lgsm2_docker_image_pull: true

        # Type: string
        lgsm2_docker_image_repo: "gameservermanagers/gameserver"

        # Type: string
        lgsm2_docker_image_tag: "{{ lgsm_name | replace('lgsm_', '') }}"

        # Type: string
        lgsm2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='lgsm') }}:{{ lookup('role_var', '_docker_image_tag', role='lgsm') }}"

        # Volumes
        # Type: list
        lgsm2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='lgsm') }}:/data"

        # Type: list
        lgsm2_docker_volumes_custom: []

        # Hostname
        # Type: string
        lgsm2_docker_hostname: "{{ lgsm_name }}"

        # Networks
        # Type: string
        lgsm2_docker_networks_alias: "{{ lgsm_name }}"

        # Type: list
        lgsm2_docker_networks_default: []

        # Type: list
        lgsm2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        lgsm2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        lgsm2_docker_state: started


        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        lgsm_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        lgsm_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        lgsm_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        lgsm_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        lgsm_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        lgsm_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        lgsm_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        lgsm_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        lgsm_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        lgsm_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        lgsm_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        lgsm_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        lgsm_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        lgsm_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        lgsm_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        lgsm_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        lgsm_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            lgsm_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "lgsm2.{{ user.domain }}"
              - "lgsm.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            lgsm_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'lgsm2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `lgsm2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        lgsm2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        lgsm2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        lgsm2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        lgsm2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        lgsm2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        lgsm2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        lgsm2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        lgsm2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        lgsm2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        lgsm2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        lgsm2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        lgsm2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        lgsm2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        lgsm2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        lgsm2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        lgsm2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        lgsm2_web_scheme:

        ```

        1.  Example:

            ```yaml
            lgsm2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "lgsm2.{{ user.domain }}"
              - "lgsm.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            lgsm2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'lgsm2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

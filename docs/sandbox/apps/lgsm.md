---
icon: material/docker
hide:
  - tags
tags:
  - lgsm
  - gaming
  - server
---

# LinuxGSM

## Overview

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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `lgsm_instances`.

    ```yaml { .sb-show-on-unchecked title="Applies to all instances of lgsm:" }
    lgsm_role_web_subdomain: "custom"
    ```

    ```yaml { .sb-show-on-checked title="Applies to a specific instance (e.g., `lgsm2`):" }
    lgsm2_web_subdomain: "custom2"
    ```

<label class="md-button md-button--stretch" for="sb-checkbox--var-level">
   <input type="checkbox" id="sb-checkbox--var-level"><span class="sb-show-on-unchecked">Show instance-level variables</span><span class="sb-show-on-checked">Show role-level variables</span>
</label>

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `lgsm_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `lgsm_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`lgsm_instances`"

        ```yaml
        # Type: list
        lgsm_instances: []
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            lgsm_instances: ["lgsm", "lgsm2"]
            ```

=== "Paths"

    ??? variable string "`lgsm_role_paths_folder`{ .sb-show-on-unchecked }`lgsm2_paths_folder`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_paths_folder: "{{ lgsm_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_paths_folder: "{{ lgsm_name }}"
        ```

    ??? variable string "`lgsm_role_paths_location`{ .sb-show-on-unchecked }`lgsm2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_paths_location: "{{ server_appdata_path }}/{{ lgsm_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_paths_location: "{{ server_appdata_path }}/{{ lgsm_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`lgsm_role_web_subdomain`{ .sb-show-on-unchecked }`lgsm2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_web_subdomain: "{{ lgsm_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_web_subdomain: "{{ lgsm_name }}"
        ```

    ??? variable string "`lgsm_role_web_domain`{ .sb-show-on-unchecked }`lgsm2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_web_domain: "{{ user.domain }}"
        ```

=== "DNS"

    ??? variable string "`lgsm_role_dns_record`{ .sb-show-on-unchecked }`lgsm2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='lgsm') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='lgsm') }}"
        ```

    ??? variable string "`lgsm_role_dns_zone`{ .sb-show-on-unchecked }`lgsm2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='lgsm') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_dns_zone: "{{ lookup('role_var', '_web_domain', role='lgsm') }}"
        ```

    ??? variable bool "`lgsm_role_dns_proxy`{ .sb-show-on-unchecked }`lgsm2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_dns_proxy: false
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_dns_proxy: false
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`lgsm_role_docker_container`{ .sb-show-on-unchecked }`lgsm2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_container: "{{ lgsm_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_container: "{{ lgsm_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`lgsm_role_docker_image_pull`{ .sb-show-on-unchecked }`lgsm2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_docker_image_pull: true
        ```

    ??? variable string "`lgsm_role_docker_image_repo`{ .sb-show-on-unchecked }`lgsm2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_image_repo: "gameservermanagers/gameserver"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_image_repo: "gameservermanagers/gameserver"
        ```

    ??? variable string "`lgsm_role_docker_image_tag`{ .sb-show-on-unchecked }`lgsm2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_image_tag: "{{ lgsm_name | replace('lgsm_', '') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_image_tag: "{{ lgsm_name | replace('lgsm_', '') }}"
        ```

    ??? variable string "`lgsm_role_docker_image`{ .sb-show-on-unchecked }`lgsm2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='lgsm') }}:{{ lookup('role_var', '_docker_image_tag', role='lgsm') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='lgsm') }}:{{ lookup('role_var', '_docker_image_tag', role='lgsm') }}"
        ```

    <h5>Volumes</h5>

    ??? variable list "`lgsm_role_docker_volumes_default`{ .sb-show-on-unchecked }`lgsm2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='lgsm') }}:/data"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='lgsm') }}:/data"
        ```

    ??? variable list "`lgsm_role_docker_volumes_custom`{ .sb-show-on-unchecked }`lgsm2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`lgsm_role_docker_hostname`{ .sb-show-on-unchecked }`lgsm2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_hostname: "{{ lgsm_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_hostname: "{{ lgsm_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`lgsm_role_docker_networks_alias`{ .sb-show-on-unchecked }`lgsm2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_networks_alias: "{{ lgsm_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_networks_alias: "{{ lgsm_name }}"
        ```

    ??? variable list "`lgsm_role_docker_networks_default`{ .sb-show-on-unchecked }`lgsm2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_networks_default: []
        ```

    ??? variable list "`lgsm_role_docker_networks_custom`{ .sb-show-on-unchecked }`lgsm2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        lgsm_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        lgsm2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`lgsm_role_docker_restart_policy`{ .sb-show-on-unchecked }`lgsm2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`lgsm_role_docker_state`{ .sb-show-on-unchecked }`lgsm2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        lgsm_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        lgsm2_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`lgsm_role_autoheal_enabled`{ .sb-show-on-unchecked }`lgsm2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        lgsm_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        lgsm2_autoheal_enabled: true
        ```

    ??? variable string "`lgsm_role_depends_on`{ .sb-show-on-unchecked }`lgsm2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        lgsm_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        lgsm2_depends_on: ""
        ```

    ??? variable string "`lgsm_role_depends_on_delay`{ .sb-show-on-unchecked }`lgsm2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        lgsm_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        lgsm2_depends_on_delay: "0"
        ```

    ??? variable string "`lgsm_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`lgsm2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        lgsm_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        lgsm2_depends_on_healthchecks:
        ```

    ??? variable bool "`lgsm_role_diun_enabled`{ .sb-show-on-unchecked }`lgsm2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        lgsm_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        lgsm2_diun_enabled: true
        ```

    ??? variable bool "`lgsm_role_dns_enabled`{ .sb-show-on-unchecked }`lgsm2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        lgsm_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        lgsm2_dns_enabled: true
        ```

    ??? variable bool "`lgsm_role_docker_controller`{ .sb-show-on-unchecked }`lgsm2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        lgsm_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        lgsm2_docker_controller: true
        ```

    ??? variable bool "`lgsm_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`lgsm2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        lgsm_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        lgsm2_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`lgsm_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`lgsm2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        lgsm_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        lgsm2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`lgsm_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`lgsm2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        lgsm_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        lgsm2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`lgsm_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`lgsm2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        lgsm_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        lgsm2_traefik_gzip_enabled: false
        ```

    ??? variable bool "`lgsm_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`lgsm2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`lgsm_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`lgsm2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        lgsm_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        lgsm2_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`lgsm_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`lgsm2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        lgsm_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        lgsm2_traefik_robot_enabled: true
        ```

    ??? variable bool "`lgsm_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`lgsm2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        lgsm_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        lgsm2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`lgsm_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`lgsm2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        lgsm_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        lgsm2_traefik_wildcard_enabled: true
        ```

    ??? variable list "`lgsm_role_web_fqdn_override`{ .sb-show-on-unchecked }`lgsm2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        lgsm_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        lgsm2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            lgsm_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "lgsm2.{{ user.domain }}"
              - "lgsm.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            lgsm2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "lgsm2.{{ user.domain }}"
              - "lgsm.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`lgsm_role_web_host_override`{ .sb-show-on-unchecked }`lgsm2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        lgsm_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        lgsm2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            lgsm_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'lgsm2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            lgsm2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'lgsm2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`lgsm_role_web_scheme`{ .sb-show-on-unchecked }`lgsm2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        lgsm_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        lgsm2_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

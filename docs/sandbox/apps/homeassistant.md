---
hide:
  - tags
tags:
  - homeassistant
  - automation
  - iot
---

# Homeassistant

## What is it?

[Homeassistant](https://www.home-assistant.io/) is a tool designed for (open source) home automation that puts local control and privacy first. Powered by a worldwide community of tinkerers and DIY enthusiasts.

Note that while it will work on a remote server, it takes some doing to get it to interface with a local server or local devices. It is not recommended or supported.

!!! warning
    By default, the role is NOT protected behind your Authelia/SSO middleware. Home Assistant has its own authentication system (with 2FA), and it is recommended to use that.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.home-assistant.io/){: .header-icons } | [:octicons-link-16: Docs](https://www.home-assistant.io/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/home-assistant/core){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/homeassistant/home-assistant/tags){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-homeassistant

```

### 2. URL

- To access Homeassistant, visit `https://homeassistant._yourdomain.com_`

### 3. Setup

Home Assistant is pretty versatile and works with a lot of different apps/containers, some of which we have roles for. See [MQTT](mqtt.md) for using Mosquitto to communicate with local and remote devices. We also have [Node Red](node_red.md), which is a platform for multiple types of automations.

??? Note "Nabu Casa"
    You don't NEED to use Nabu Casa to access Home Assistant remotely. You can use a reverse proxy to access it remotely. However, if you want to use Nabu Casa, you can use the [Nabu Casa](https://www.nabucasa.com/) integration to connect to Home Assistant. It is a paid service, but it is a good way to support the Home Assistant project. That said, the Home Assistant role is set up to work with a reverse proxy, so you can use that instead.

### 4. Addons

You can also use the [Home Assistant Community Store (HACS)](https://hacs.xyz/) to add more functionality to Home Assistant. For instance, adding the Node Red Companion, a "custom" integration for node-red-contrib-home-assistant-websocket. It allows you to integrate Node-RED with Home Assistant. For more information, see the [Node Red](node_red.md) page.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        homeassistant_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `homeassistant_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `homeassistant_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`homeassistant_name`"

        ```yaml
        # Type: string
        homeassistant_name: homeassistant
        ```

=== "Paths"

    ??? variable string "`homeassistant_role_paths_folder`"

        ```yaml
        # Type: string
        homeassistant_role_paths_folder: "{{ homeassistant_name }}"
        ```

    ??? variable string "`homeassistant_role_paths_location`"

        ```yaml
        # Type: string
        homeassistant_role_paths_location: "{{ server_appdata_path }}/{{ homeassistant_role_paths_folder }}"
        ```

    ??? variable string "`homeassistant_role_paths_conf`"

        ```yaml
        # Type: string
        homeassistant_role_paths_conf: "{{ homeassistant_role_paths_location }}/configuration.yaml"
        ```

=== "Web"

    ??? variable string "`homeassistant_role_web_subdomain`"

        ```yaml
        # Type: string
        homeassistant_role_web_subdomain: "{{ homeassistant_name }}"
        ```

    ??? variable string "`homeassistant_role_web_domain`"

        ```yaml
        # Type: string
        homeassistant_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`homeassistant_role_web_port`"

        ```yaml
        # Type: string
        homeassistant_role_web_port: "8123"
        ```

    ??? variable string "`homeassistant_role_web_url`"

        ```yaml
        # Type: string
        homeassistant_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='homeassistant') + '.' + lookup('role_var', '_web_domain', role='homeassistant')
                                     if (lookup('role_var', '_web_subdomain', role='homeassistant') | length > 0)
                                     else lookup('role_var', '_web_domain', role='homeassistant')) }}"
        ```

=== "DNS"

    ??? variable string "`homeassistant_role_dns_record`"

        ```yaml
        # Type: string
        homeassistant_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='homeassistant') }}"
        ```

    ??? variable string "`homeassistant_role_dns_zone`"

        ```yaml
        # Type: string
        homeassistant_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='homeassistant') }}"
        ```

    ??? variable bool "`homeassistant_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`homeassistant_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        homeassistant_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`homeassistant_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        homeassistant_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`homeassistant_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        homeassistant_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`homeassistant_role_traefik_certresolver`"

        ```yaml
        # Type: string
        homeassistant_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`homeassistant_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_traefik_enabled: true
        ```

    ??? variable bool "`homeassistant_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_traefik_api_enabled: false
        ```

    ??? variable string "`homeassistant_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        homeassistant_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`homeassistant_role_docker_container`"

        ```yaml
        # Type: string
        homeassistant_role_docker_container: "{{ homeassistant_name }}"
        ```

    ##### Image

    ??? variable bool "`homeassistant_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_docker_image_pull: true
        ```

    ??? variable string "`homeassistant_role_docker_image_repo`"

        ```yaml
        # Type: string
        homeassistant_role_docker_image_repo: "lscr.io/linuxserver/homeassistant"
        ```

    ??? variable string "`homeassistant_role_docker_image_tag`"

        ```yaml
        # Type: string
        homeassistant_role_docker_image_tag: "latest"
        ```

    ??? variable string "`homeassistant_role_docker_image`"

        ```yaml
        # Type: string
        homeassistant_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='homeassistant') }}:{{ lookup('role_var', '_docker_image_tag', role='homeassistant') }}"
        ```

    ##### Envs

    ??? variable dict "`homeassistant_role_docker_envs_default`"

        ```yaml
        # Type: dict
        homeassistant_role_docker_envs_default: 
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
        ```

    ??? variable dict "`homeassistant_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        homeassistant_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`homeassistant_role_docker_volumes_default`"

        ```yaml
        # Type: list
        homeassistant_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='homeassistant') }}:/config"
          - /etc/localtime:/etc/localtime:ro
        ```

    ??? variable list "`homeassistant_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        homeassistant_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`homeassistant_role_docker_hostname`"

        ```yaml
        # Type: string
        homeassistant_role_docker_hostname: "{{ homeassistant_name }}"
        ```

    ##### Networks

    ??? variable string "`homeassistant_role_docker_networks_alias`"

        ```yaml
        # Type: string
        homeassistant_role_docker_networks_alias: "{{ homeassistant_name }}"
        ```

    ??? variable list "`homeassistant_role_docker_networks_default`"

        ```yaml
        # Type: list
        homeassistant_role_docker_networks_default: []
        ```

    ??? variable list "`homeassistant_role_docker_networks_custom`"

        ```yaml
        # Type: list
        homeassistant_role_docker_networks_custom: []
        ```

    ##### Network Mode

    ??? variable string "`homeassistant_role_docker_network_mode`"

        ```yaml
        # Type: string
        homeassistant_role_docker_network_mode: "host"
        ```

    ##### Restart Policy

    ??? variable string "`homeassistant_role_docker_restart_policy`"

        ```yaml
        # Type: string
        homeassistant_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`homeassistant_role_docker_state`"

        ```yaml
        # Type: string
        homeassistant_role_docker_state: started
        ```

    ##### Privileged

    ??? variable bool "`homeassistant_role_docker_privileged`"

        ```yaml
        # Type: bool (true/false)
        homeassistant_role_docker_privileged: true
        ```

=== "Global Override Options"

    ??? variable bool "`homeassistant_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        homeassistant_role_autoheal_enabled: true
        ```

    ??? variable string "`homeassistant_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        homeassistant_role_depends_on: ""
        ```

    ??? variable string "`homeassistant_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        homeassistant_role_depends_on_delay: "0"
        ```

    ??? variable string "`homeassistant_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        homeassistant_role_depends_on_healthchecks:
        ```

    ??? variable bool "`homeassistant_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        homeassistant_role_diun_enabled: true
        ```

    ??? variable bool "`homeassistant_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        homeassistant_role_dns_enabled: true
        ```

    ??? variable bool "`homeassistant_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        homeassistant_role_docker_controller: true
        ```

    ??? variable bool "`homeassistant_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        homeassistant_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`homeassistant_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        homeassistant_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`homeassistant_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        homeassistant_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`homeassistant_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        homeassistant_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`homeassistant_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        homeassistant_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`homeassistant_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        homeassistant_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`homeassistant_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        homeassistant_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`homeassistant_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        homeassistant_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            homeassistant_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "homeassistant2.{{ user.domain }}"
              - "homeassistant.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`homeassistant_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        homeassistant_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            homeassistant_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'homeassistant2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`homeassistant_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        homeassistant_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
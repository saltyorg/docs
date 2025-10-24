---
hide:
  - tags
tags:
  - factorio
  - gaming
  - server
---

# Factorio

## What is it?

Run a [Factorio](https://www.factorio.com) headless server.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.factorio.com){: .header-icons } | [:octicons-link-16: Docs](https://wiki.factorio.com/Multiplayer){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/goofball222/factorio){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/goofball222/factorio){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-factorio

```

### 2. Setup

- Set to install the latest Factorio experimental (1.1.x) build. Fix to a certain version using the [inventory system](../../saltbox/inventory/index.md).

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    factorio_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `factorio_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `factorio_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`factorio_name`"

        ```yaml
        # Type: string
        factorio_name: factorio
        ```

=== "Paths"

    ??? variable string "`factorio_role_paths_folder`"

        ```yaml
        # Type: string
        factorio_role_paths_folder: "{{ factorio_name }}"
        ```

    ??? variable string "`factorio_role_paths_location`"

        ```yaml
        # Type: string
        factorio_role_paths_location: "{{ server_appdata_path }}/{{ factorio_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`factorio_role_web_subdomain`"

        ```yaml
        # Type: string
        factorio_role_web_subdomain: "{{ factorio_name }}"
        ```

    ??? variable string "`factorio_role_web_domain`"

        ```yaml
        # Type: string
        factorio_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`factorio_role_web_port`"

        ```yaml
        # Type: string
        factorio_role_web_port: ""
        ```

=== "DNS"

    ??? variable string "`factorio_role_dns_record`"

        ```yaml
        # Type: string
        factorio_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='factorio') }}"
        ```

    ??? variable string "`factorio_role_dns_zone`"

        ```yaml
        # Type: string
        factorio_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='factorio') }}"
        ```

    ??? variable bool "`factorio_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_dns_proxy: false
        ```

=== "Docker"

    Container
    { .sb-h5 }

    ??? variable string "`factorio_role_docker_container`"

        ```yaml
        # Type: string
        factorio_role_docker_container: "{{ factorio_name }}"
        ```

    Image
    { .sb-h5 }

    ??? variable bool "`factorio_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_docker_image_pull: true
        ```

    ??? variable string "`factorio_role_docker_image_repo`"

        ```yaml
        # Type: string
        factorio_role_docker_image_repo: "goofball222/factorio"
        ```

    ??? variable string "`factorio_role_docker_image_tag`"

        ```yaml
        # Type: string
        factorio_role_docker_image_tag: "experimental"
        ```

    ??? variable string "`factorio_role_docker_image`"

        ```yaml
        # Type: string
        factorio_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='factorio') }}:{{ lookup('role_var', '_docker_image_tag', role='factorio') }}"
        ```

    Ports
    { .sb-h5 }

    ??? variable list "`factorio_role_docker_ports_defaults`"

        ```yaml
        # Type: list
        factorio_role_docker_ports_defaults: 
          - "27015:27015/tcp"
          - "34197:34197/udp"
        ```

    ??? variable list "`factorio_role_docker_ports_custom`"

        ```yaml
        # Type: list
        factorio_role_docker_ports_custom: []
        ```

    Envs
    { .sb-h5 }

    ??? variable dict "`factorio_role_docker_envs_default`"

        ```yaml
        # Type: dict
        factorio_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`factorio_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        factorio_role_docker_envs_custom: {}
        ```

    Volumes
    { .sb-h5 }

    ??? variable list "`factorio_role_docker_volumes_default`"

        ```yaml
        # Type: list
        factorio_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='factorio') }}:/factorio"
        ```

    ??? variable list "`factorio_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        factorio_role_docker_volumes_custom: []
        ```

    Hostname
    { .sb-h5 }

    ??? variable string "`factorio_role_docker_hostname`"

        ```yaml
        # Type: string
        factorio_role_docker_hostname: "{{ factorio_name }}"
        ```

    Networks
    { .sb-h5 }

    ??? variable string "`factorio_role_docker_networks_alias`"

        ```yaml
        # Type: string
        factorio_role_docker_networks_alias: "{{ factorio_name }}"
        ```

    ??? variable list "`factorio_role_docker_networks_default`"

        ```yaml
        # Type: list
        factorio_role_docker_networks_default: []
        ```

    ??? variable list "`factorio_role_docker_networks_custom`"

        ```yaml
        # Type: list
        factorio_role_docker_networks_custom: []
        ```

    Restart Policy
    { .sb-h5 }

    ??? variable string "`factorio_role_docker_restart_policy`"

        ```yaml
        # Type: string
        factorio_role_docker_restart_policy: unless-stopped
        ```

    State
    { .sb-h5 }

    ??? variable string "`factorio_role_docker_state`"

        ```yaml
        # Type: string
        factorio_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`factorio_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        factorio_role_autoheal_enabled: true
        ```

    ??? variable string "`factorio_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        factorio_role_depends_on: ""
        ```

    ??? variable string "`factorio_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        factorio_role_depends_on_delay: "0"
        ```

    ??? variable string "`factorio_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        factorio_role_depends_on_healthchecks:
        ```

    ??? variable bool "`factorio_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        factorio_role_diun_enabled: true
        ```

    ??? variable bool "`factorio_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        factorio_role_dns_enabled: true
        ```

    ??? variable bool "`factorio_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        factorio_role_docker_controller: true
        ```

    ??? variable bool "`factorio_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        factorio_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`factorio_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        factorio_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`factorio_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        factorio_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`factorio_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        factorio_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`factorio_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`factorio_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        factorio_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`factorio_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        factorio_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`factorio_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        factorio_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`factorio_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        factorio_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`factorio_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        factorio_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            factorio_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "factorio2.{{ user.domain }}"
              - "factorio.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`factorio_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        factorio_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            factorio_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'factorio2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`factorio_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        factorio_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
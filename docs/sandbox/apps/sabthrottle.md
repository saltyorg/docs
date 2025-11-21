---
icon: material/docker
hide:
  - tags
tags:
  - sabthrottle
  - automation
  - bandwidth
---

# SABThrottle

## Overview

[SABThrottle](https://github.com/8a8al00ey/sabthrottle) Sabthrottle was designed in order to dynamically control the bandwidth allocation when users are actively streaming from Plex to avoid unnecessary buffering while still allowing the user to download at the fastest rate possible. Remember nzbthrottle from daghaian, yes its exactly like that but for SABnzbd with some additional tweaks.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/8a8al00ey/sabthrottle){: .header-icons } | [:octicons-link-16: Docs](https://github.com/8a8al00ey/sabthrottle#installation){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/8a8al00ey/sabthrottle){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/8a8al00ey/sabthrottle){: .header-icons }|

### 1. Installation

```shell
sb install sandbox-sabthrottle
```

### 2. Setup

- See [documentation](https://github.com/8a8al00ey/sabthrottle#installation) for configuration and instructions see the sample configuration and description below it.

  - Running the role will autopopulate plex token and plex url.
  - If you require more then 5 stream count just follow the example and add more using proper yml formatting.
  - You can always check logs via

        ```shell
        docker logs -f sabthrottle
        ```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    sabthrottle_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `sabthrottle_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `sabthrottle_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`sabthrottle_name`"

        ```yaml
        # Type: string
        sabthrottle_name: sabthrottle
        ```

=== "Paths"

    ??? variable string "`sabthrottle_role_paths_folder`"

        ```yaml
        # Type: string
        sabthrottle_role_paths_folder: "{{ sabthrottle_name }}"
        ```

    ??? variable string "`sabthrottle_role_paths_location`"

        ```yaml
        # Type: string
        sabthrottle_role_paths_location: "{{ server_appdata_path }}/{{ sabthrottle_role_paths_folder }}"
        ```

    ??? variable string "`sabthrottle_role_paths_config_location`"

        ```yaml
        # Type: string
        sabthrottle_role_paths_config_location: "{{ sabthrottle_role_paths_location }}/config.json"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`sabthrottle_role_docker_container`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_container: "{{ sabthrottle_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`sabthrottle_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        sabthrottle_role_docker_image_pull: true
        ```

    ??? variable string "`sabthrottle_role_docker_image_repo`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_image_repo: "8a8al00ey/sabthrottle"
        ```

    ??? variable string "`sabthrottle_role_docker_image_tag`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_image_tag: "latest"
        ```

    ??? variable string "`sabthrottle_role_docker_image`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='sabthrottle') }}:{{ lookup('role_var', '_docker_image_tag', role='sabthrottle') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`sabthrottle_role_docker_envs_default`"

        ```yaml
        # Type: dict
        sabthrottle_role_docker_envs_default:
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`sabthrottle_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        sabthrottle_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`sabthrottle_role_docker_volumes_default`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_config_location', role='sabthrottle') }}:/sabthrottle/config.json:ro"
        ```

    ??? variable list "`sabthrottle_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`sabthrottle_role_docker_hostname`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_hostname: "{{ sabthrottle_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`sabthrottle_role_docker_networks_alias`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_networks_alias: "{{ sabthrottle_name }}"
        ```

    ??? variable list "`sabthrottle_role_docker_networks_default`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_networks_default: []
        ```

    ??? variable list "`sabthrottle_role_docker_networks_custom`"

        ```yaml
        # Type: list
        sabthrottle_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`sabthrottle_role_docker_restart_policy`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`sabthrottle_role_docker_state`"

        ```yaml
        # Type: string
        sabthrottle_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`sabthrottle_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        sabthrottle_role_autoheal_enabled: true
        ```

    ??? variable string "`sabthrottle_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        sabthrottle_role_depends_on: ""
        ```

    ??? variable string "`sabthrottle_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        sabthrottle_role_depends_on_delay: "0"
        ```

    ??? variable string "`sabthrottle_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        sabthrottle_role_depends_on_healthchecks:
        ```

    ??? variable bool "`sabthrottle_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        sabthrottle_role_diun_enabled: true
        ```

    ??? variable bool "`sabthrottle_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        sabthrottle_role_dns_enabled: true
        ```

    ??? variable bool "`sabthrottle_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        sabthrottle_role_docker_controller: true
        ```

    ??? variable bool "`sabthrottle_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        sabthrottle_role_docker_volumes_download:
        ```

    ??? variable bool "`sabthrottle_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        sabthrottle_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`sabthrottle_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        sabthrottle_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`sabthrottle_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        sabthrottle_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`sabthrottle_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        sabthrottle_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`sabthrottle_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        sabthrottle_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`sabthrottle_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        sabthrottle_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`sabthrottle_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        sabthrottle_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`sabthrottle_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        sabthrottle_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`sabthrottle_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        sabthrottle_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`sabthrottle_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        sabthrottle_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            sabthrottle_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "sabthrottle2.{{ user.domain }}"
              - "sabthrottle.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`sabthrottle_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        sabthrottle_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            sabthrottle_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'sabthrottle2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`sabthrottle_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        sabthrottle_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
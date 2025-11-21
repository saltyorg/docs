---
icon: material/docker
hide:
  - tags
tags:
  - nabarr
  - automation
  - rss
---

# Nabarr

## Overview

[Nabarr](https://github.com/l3uddz/nabarr) monitors Newznab/Torznab RSS feeds to find new media to add to Sonarr and or Radarr.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-docker: Docker:](https://github.com/l3uddz/nabarr){: .header-icons } | [:octicons-link-16: Docs](https://github.com/l3uddz/nabarr){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/l3uddz/nabarr){: .header-icons } | [:material-docker: Docker:](https://hub.docker.com/r/cloudb0x/nabarr){: .header-icons } |

### 1. Installation

``` shell

sb install sandbox-nabarr

```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    nabarr_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `nabarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `nabarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`nabarr_name`"

        ```yaml
        # Type: string
        nabarr_name: nabarr
        ```

=== "Paths"

    ??? variable string "`nabarr_role_paths_folder`"

        ```yaml
        # Type: string
        nabarr_role_paths_folder: "{{ nabarr_name }}"
        ```

    ??? variable string "`nabarr_role_paths_location`"

        ```yaml
        # Type: string
        nabarr_role_paths_location: "{{ server_appdata_path }}/{{ nabarr_role_paths_folder }}"
        ```

    ??? variable string "`nabarr_role_paths_config_location`"

        ```yaml
        # Type: string
        nabarr_role_paths_config_location: "{{ nabarr_role_paths_location }}/config.yml"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`nabarr_role_docker_container`"

        ```yaml
        # Type: string
        nabarr_role_docker_container: "{{ nabarr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`nabarr_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        nabarr_role_docker_image_pull: true
        ```

    ??? variable string "`nabarr_role_docker_image_tag`"

        ```yaml
        # Type: string
        nabarr_role_docker_image_tag: "latest"
        ```

    ??? variable string "`nabarr_role_docker_image_repo`"

        ```yaml
        # Type: string
        nabarr_role_docker_image_repo: "saltydk/nabarr"
        ```

    ??? variable string "`nabarr_role_docker_image`"

        ```yaml
        # Type: string
        nabarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='nabarr') }}:{{ lookup('role_var', '_docker_image_tag', role='nabarr') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`nabarr_role_docker_envs_default`"

        ```yaml
        # Type: dict
        nabarr_role_docker_envs_default:
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          APP_VERBOSITY: "0"
        ```

    ??? variable dict "`nabarr_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        nabarr_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`nabarr_role_docker_volumes_default`"

        ```yaml
        # Type: list
        nabarr_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='nabarr') }}:/config"
        ```

    ??? variable list "`nabarr_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        nabarr_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`nabarr_role_docker_hostname`"

        ```yaml
        # Type: string
        nabarr_role_docker_hostname: "{{ nabarr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`nabarr_role_docker_networks_alias`"

        ```yaml
        # Type: string
        nabarr_role_docker_networks_alias: "{{ nabarr_name }}"
        ```

    ??? variable list "`nabarr_role_docker_networks_default`"

        ```yaml
        # Type: list
        nabarr_role_docker_networks_default: []
        ```

    ??? variable list "`nabarr_role_docker_networks_custom`"

        ```yaml
        # Type: list
        nabarr_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`nabarr_role_docker_restart_policy`"

        ```yaml
        # Type: string
        nabarr_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`nabarr_role_docker_state`"

        ```yaml
        # Type: string
        nabarr_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`nabarr_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        nabarr_role_autoheal_enabled: true
        ```

    ??? variable string "`nabarr_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        nabarr_role_depends_on: ""
        ```

    ??? variable string "`nabarr_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        nabarr_role_depends_on_delay: "0"
        ```

    ??? variable string "`nabarr_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        nabarr_role_depends_on_healthchecks:
        ```

    ??? variable bool "`nabarr_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        nabarr_role_diun_enabled: true
        ```

    ??? variable bool "`nabarr_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        nabarr_role_dns_enabled: true
        ```

    ??? variable bool "`nabarr_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        nabarr_role_docker_controller: true
        ```

    ??? variable bool "`nabarr_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        nabarr_role_docker_volumes_download:
        ```

    ??? variable bool "`nabarr_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        nabarr_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`nabarr_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        nabarr_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`nabarr_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        nabarr_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`nabarr_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        nabarr_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`nabarr_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        nabarr_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`nabarr_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        nabarr_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`nabarr_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        nabarr_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`nabarr_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        nabarr_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`nabarr_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        nabarr_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`nabarr_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        nabarr_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            nabarr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "nabarr2.{{ user.domain }}"
              - "nabarr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`nabarr_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        nabarr_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            nabarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'nabarr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`nabarr_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        nabarr_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
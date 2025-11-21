---
icon: material/docker
hide:
  - tags
tags:
  - speedtest
  - monitoring
  - network
---

# Speedtest

## Overview

[Speedtest](https://github.com/librespeed/speedtest)  is a very lightweight Speedtest implemented in Javascript, using XMLHttpRequest and Web Workers.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/librespeed/speedtest){: .header-icons } | [:octicons-link-16: Docs](https://github.com/librespeed/speedtest){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/librespeed/speedtest){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/librespeed){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-speedtest

```

### 2. URL

- To access Speedtest, visit <https://speedtest.iYOUR_DOMAIN_NAMEi>

### 3. Setup

To use a custom subdomain, add a custom value for `speedtest_web_subdomain` in the `/srv/git/saltbox/inventories/host_vars/localhost.yml` file. More info can be found [here](../../saltbox/inventory/index.md).

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    speedtest_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `speedtest_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `speedtest_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`speedtest_name`"

        ```yaml
        # Type: string
        speedtest_name: speedtest
        ```

=== "Paths"

    ??? variable string "`speedtest_role_paths_folder`"

        ```yaml
        # Type: string
        speedtest_role_paths_folder: "{{ speedtest_name }}"
        ```

    ??? variable string "`speedtest_role_paths_location`"

        ```yaml
        # Type: string
        speedtest_role_paths_location: "{{ server_appdata_path }}/{{ speedtest_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`speedtest_role_web_subdomain`"

        ```yaml
        # Type: string
        speedtest_role_web_subdomain: "{{ speedtest_name }}"
        ```

    ??? variable string "`speedtest_role_web_domain`"

        ```yaml
        # Type: string
        speedtest_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`speedtest_role_web_port`"

        ```yaml
        # Type: string
        speedtest_role_web_port: "80"
        ```

    ??? variable string "`speedtest_role_web_url`"

        ```yaml
        # Type: string
        speedtest_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='speedtest') + '.' + lookup('role_var', '_web_domain', role='speedtest')
                                 if (lookup('role_var', '_web_subdomain', role='speedtest') | length > 0)
                                 else lookup('role_var', '_web_domain', role='speedtest')) }}"
        ```

=== "DNS"

    ??? variable string "`speedtest_role_dns_record`"

        ```yaml
        # Type: string
        speedtest_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='speedtest') }}"
        ```

    ??? variable string "`speedtest_role_dns_zone`"

        ```yaml
        # Type: string
        speedtest_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='speedtest') }}"
        ```

    ??? variable bool "`speedtest_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_dns_proxy: false
        ```

=== "Traefik"

    ??? variable string "`speedtest_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        speedtest_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`speedtest_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        speedtest_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`speedtest_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        speedtest_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`speedtest_role_traefik_certresolver`"

        ```yaml
        # Type: string
        speedtest_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`speedtest_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_traefik_enabled: true
        ```

    ??? variable bool "`speedtest_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_traefik_api_enabled: false
        ```

    ??? variable string "`speedtest_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        speedtest_role_traefik_api_endpoint: ""
        ```

=== "Theme"

    ??? variable bool "`speedtest_role_themepark_enabled`"

        ```yaml
        # Options can be found at https://github.com/themepark-dev/theme.park
        # Type: bool (true/false)
        speedtest_role_themepark_enabled: false
        ```

    ??? variable string "`speedtest_role_themepark_theme`"

        ```yaml
        # Type: string
        speedtest_role_themepark_theme: "{{ global_themepark_theme }}"
        ```

    ??? variable string "`speedtest_role_themepark_domain`"

        ```yaml
        # Type: string
        speedtest_role_themepark_domain: "{{ global_themepark_domain }}"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`speedtest_role_docker_container`"

        ```yaml
        # Type: string
        speedtest_role_docker_container: "{{ speedtest_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`speedtest_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_docker_image_pull: true
        ```

    ??? variable string "`speedtest_role_docker_image_repo`"

        ```yaml
        # Type: string
        speedtest_role_docker_image_repo: "lscr.io/linuxserver/librespeed"
        ```

    ??? variable string "`speedtest_role_docker_image_tag`"

        ```yaml
        # Type: string
        speedtest_role_docker_image_tag: "latest"
        ```

    ??? variable string "`speedtest_role_docker_image`"

        ```yaml
        # Type: string
        speedtest_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='speedtest') }}:{{ lookup('role_var', '_docker_image_tag', role='speedtest') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`speedtest_role_docker_envs_default`"

        ```yaml
        # Type: dict
        speedtest_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          PASSWORD: "{{ user.pass }}"
          DB_TYPE: "sqlite"
          DOCKER_MODS: "{{ 'ghcr.io/themepark-dev/theme.park:librespeed' if lookup('role_var', '_themepark_enabled', role='speedtest') else omit }}"
          TP_DOMAIN: "{{ lookup('role_var', '_themepark_domain', role='speedtest') }}"
          TP_THEME: "{{ lookup('role_var', '_themepark_theme', role='speedtest') }}"
        ```

    ??? variable dict "`speedtest_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        speedtest_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`speedtest_role_docker_volumes_default`"

        ```yaml
        # Type: list
        speedtest_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='speedtest') }}:/config"
        ```

    ??? variable list "`speedtest_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        speedtest_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`speedtest_role_docker_hostname`"

        ```yaml
        # Type: string
        speedtest_role_docker_hostname: "{{ speedtest_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`speedtest_role_docker_networks_alias`"

        ```yaml
        # Type: string
        speedtest_role_docker_networks_alias: "{{ speedtest_name }}"
        ```

    ??? variable list "`speedtest_role_docker_networks_default`"

        ```yaml
        # Type: list
        speedtest_role_docker_networks_default: []
        ```

    ??? variable list "`speedtest_role_docker_networks_custom`"

        ```yaml
        # Type: list
        speedtest_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`speedtest_role_docker_restart_policy`"

        ```yaml
        # Type: string
        speedtest_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`speedtest_role_docker_state`"

        ```yaml
        # Type: string
        speedtest_role_docker_state: started
        ```

    <h5>Force Kill</h5>

    ??? variable bool "`speedtest_role_docker_force_kill`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_docker_force_kill: true
        ```

=== "Global Override Options"

    ??? variable bool "`speedtest_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        speedtest_role_autoheal_enabled: true
        ```

    ??? variable string "`speedtest_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        speedtest_role_depends_on: ""
        ```

    ??? variable string "`speedtest_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        speedtest_role_depends_on_delay: "0"
        ```

    ??? variable string "`speedtest_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        speedtest_role_depends_on_healthchecks:
        ```

    ??? variable bool "`speedtest_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        speedtest_role_diun_enabled: true
        ```

    ??? variable bool "`speedtest_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        speedtest_role_dns_enabled: true
        ```

    ??? variable bool "`speedtest_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        speedtest_role_docker_controller: true
        ```

    ??? variable bool "`speedtest_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_docker_volumes_download:
        ```

    ??? variable bool "`speedtest_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        speedtest_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`speedtest_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        speedtest_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`speedtest_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        speedtest_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`speedtest_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        speedtest_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`speedtest_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`speedtest_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        speedtest_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`speedtest_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        speedtest_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`speedtest_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        speedtest_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`speedtest_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        speedtest_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`speedtest_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        speedtest_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            speedtest_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "speedtest2.{{ user.domain }}"
              - "speedtest.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`speedtest_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        speedtest_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            speedtest_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'speedtest2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`speedtest_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        speedtest_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
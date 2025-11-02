---
icon: material/docker
hide:
  - tags
tags:
  - plex-auto-languages
  - plex
  - automation
---

# Plex Auto Languages

## Overview

[plex_auto_languages](https://github.com/RemiRigal/Plex-Auto-Languages) auto-updates the language of your Plex TV Show episodes based on the current language you are using without messing with your existing language preferences.

You

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/RemiRigal/Plex-Auto-Languages){: .header-icons } | [:octicons-link-16: Docs](https://github.com/RemiRigal/Plex-Auto-Languages){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/RemiRigal/Plex-Auto-Languages){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/remirigal/plex-auto-languages){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-plex-auto-languages

```

### 2. URL

PLex-auto-languages has no UI; it is driven by a config file

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    plex_auto_languages_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `plex_auto_languages_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `plex_auto_languages_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`plex_auto_languages_name`"

        ```yaml
        # Type: string
        plex_auto_languages_name: plex-auto-languages
        ```

=== "Paths"

    ??? variable string "`plex_auto_languages_role_paths_folder`"

        ```yaml
        # Type: string
        plex_auto_languages_role_paths_folder: "{{ plex_auto_languages_name }}"
        ```

    ??? variable string "`plex_auto_languages_role_paths_location`"

        ```yaml
        # Type: string
        plex_auto_languages_role_paths_location: "{{ server_appdata_path }}/{{ plex_auto_languages_role_paths_folder }}"
        ```

    ??? variable string "`plex_auto_languages_role_paths_config_location`"

        ```yaml
        # Type: string
        plex_auto_languages_role_paths_config_location: "{{ plex_auto_languages_role_paths_location }}/config.yaml"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`plex_auto_languages_role_docker_container`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_container: "{{ plex_auto_languages_name }}"
        ```

    <h5>Image</h5>

    ??? variable string "`plex_auto_languages_role_docker_image_tag`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_image_tag: "latest"
        ```

    ??? variable string "`plex_auto_languages_role_docker_image_repo`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_image_repo: "journeyover/plex-auto-languages"
        ```

    ??? variable string "`plex_auto_languages_role_docker_image`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='plex_auto_languages') }}:{{ lookup('role_var', '_docker_image_tag', role='plex_auto_languages') }}"
        ```

    ??? variable bool "`plex_auto_languages_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        plex_auto_languages_role_docker_image_pull: true
        ```

    <h5>Envs</h5>

    ??? variable dict "`plex_auto_languages_role_docker_envs_default`"

        ```yaml
        # Type: dict
        plex_auto_languages_role_docker_envs_default: 
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`plex_auto_languages_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        plex_auto_languages_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`plex_auto_languages_role_docker_volumes_default`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='plex_auto_languages') }}:/config"
        ```

    ??? variable list "`plex_auto_languages_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`plex_auto_languages_role_docker_hostname`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_hostname: "{{ plex_auto_languages_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`plex_auto_languages_role_docker_networks_alias`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_networks_alias: "{{ plex_auto_languages_name }}"
        ```

    ??? variable list "`plex_auto_languages_role_docker_networks_default`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_networks_default: []
        ```

    ??? variable list "`plex_auto_languages_role_docker_networks_custom`"

        ```yaml
        # Type: list
        plex_auto_languages_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`plex_auto_languages_role_docker_restart_policy`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`plex_auto_languages_role_docker_state`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_state: started
        ```

    <h5>Stop Timeout</h5>

    ??? variable int "`plex_auto_languages_role_docker_stop_timeout`"

        ```yaml
        # Type: int
        plex_auto_languages_role_docker_stop_timeout: 10
        ```

    <h5>User</h5>

    ??? variable string "`plex_auto_languages_role_docker_user`"

        ```yaml
        # Type: string
        plex_auto_languages_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`plex_auto_languages_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        plex_auto_languages_role_autoheal_enabled: true
        ```

    ??? variable string "`plex_auto_languages_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        plex_auto_languages_role_depends_on: ""
        ```

    ??? variable string "`plex_auto_languages_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        plex_auto_languages_role_depends_on_delay: "0"
        ```

    ??? variable string "`plex_auto_languages_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        plex_auto_languages_role_depends_on_healthchecks:
        ```

    ??? variable bool "`plex_auto_languages_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        plex_auto_languages_role_diun_enabled: true
        ```

    ??? variable bool "`plex_auto_languages_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        plex_auto_languages_role_dns_enabled: true
        ```

    ??? variable bool "`plex_auto_languages_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        plex_auto_languages_role_docker_controller: true
        ```

    ??? variable bool "`plex_auto_languages_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        plex_auto_languages_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`plex_auto_languages_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        plex_auto_languages_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`plex_auto_languages_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        plex_auto_languages_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`plex_auto_languages_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        plex_auto_languages_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`plex_auto_languages_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        plex_auto_languages_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`plex_auto_languages_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        plex_auto_languages_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`plex_auto_languages_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        plex_auto_languages_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`plex_auto_languages_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        plex_auto_languages_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`plex_auto_languages_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        plex_auto_languages_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`plex_auto_languages_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        plex_auto_languages_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            plex_auto_languages_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "plex_auto_languages2.{{ user.domain }}"
              - "plex_auto_languages.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`plex_auto_languages_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        plex_auto_languages_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            plex_auto_languages_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'plex_auto_languages2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`plex_auto_languages_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        plex_auto_languages_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
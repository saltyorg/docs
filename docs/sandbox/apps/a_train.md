---
icon: material/docker
hide:
  - tags
tags:
  - a-train
  - train
  - google
---

# A-Train

## Overview

A-Train is the official Autoscan trigger that listens for changes within Google Drive. It is the successor of Autoscan's Bernard trigger, which unfortunately contains enough logic errors to prompt a rewrite.

- Supports Shared Drives
- Service Account-based authentication
- Does not support My Drive
- Does not support encrypted files
- Does not support alternative authentication methods

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    a_train_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `a_train_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `a_train_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`a_train_name`"

        ```yaml
        # Type: string
        a_train_name: a-train
        ```

=== "Settings"

    ??? variable list "`a_train_role_remotes`"

        ```yaml
        # Type: list
        a_train_role_remotes: [""]
        ```

=== "Paths"

    ??? variable string "`a_train_role_paths_folder`"

        ```yaml
        # Type: string
        a_train_role_paths_folder: "{{ a_train_name }}"
        ```

    ??? variable string "`a_train_role_paths_location`"

        ```yaml
        # Type: string
        a_train_role_paths_location: "{{ server_appdata_path }}/{{ a_train_role_paths_folder }}"
        ```

    ??? variable string "`a_train_role_paths_config_location`"

        ```yaml
        # Type: string
        a_train_role_paths_config_location: "{{ a_train_role_paths_location }}/a-train.toml"
        ```

    ??? variable string "`a_train_role_paths_sa_location`"

        ```yaml
        # Type: string
        a_train_role_paths_sa_location: "{{ a_train_role_paths_location }}/account.json"
        ```

    ??? variable string "`a_train_role_paths_rclone_config_location`"

        ```yaml
        # Type: string
        a_train_role_paths_rclone_config_location: "/home/{{ user.name }}/.config/rclone/rclone.conf"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`a_train_role_docker_container`"

        ```yaml
        # Type: string
        a_train_role_docker_container: "{{ a_train_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`a_train_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        a_train_role_docker_image_pull: true
        ```

    ??? variable string "`a_train_role_docker_image_repo`"

        ```yaml
        # Type: string
        a_train_role_docker_image_repo: "ghcr.io/m-rots/a-train"
        ```

    ??? variable string "`a_train_role_docker_image_tag`"

        ```yaml
        # Type: string
        a_train_role_docker_image_tag: "latest"
        ```

    ??? variable string "`a_train_role_docker_image`"

        ```yaml
        # Type: string
        a_train_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='a_train') }}:{{ lookup('role_var', '_docker_image_tag', role='a_train') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`a_train_role_docker_envs_default`"

        ```yaml
        # Type: dict
        a_train_role_docker_envs_default:
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`a_train_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        a_train_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`a_train_role_docker_volumes_default`"

        ```yaml
        # Type: list
        a_train_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='a_train') }}:/data"
        ```

    ??? variable list "`a_train_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        a_train_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`a_train_role_docker_hostname`"

        ```yaml
        # Type: string
        a_train_role_docker_hostname: "{{ a_train_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`a_train_role_docker_networks_alias`"

        ```yaml
        # Type: string
        a_train_role_docker_networks_alias: "{{ a_train_name }}"
        ```

    ??? variable list "`a_train_role_docker_networks_default`"

        ```yaml
        # Type: list
        a_train_role_docker_networks_default: []
        ```

    ??? variable list "`a_train_role_docker_networks_custom`"

        ```yaml
        # Type: list
        a_train_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`a_train_role_docker_restart_policy`"

        ```yaml
        # Type: string
        a_train_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`a_train_role_docker_state`"

        ```yaml
        # Type: string
        a_train_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`a_train_role_docker_user`"

        ```yaml
        # Type: string
        a_train_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`a_train_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        a_train_role_autoheal_enabled: true
        ```

    ??? variable string "`a_train_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        a_train_role_depends_on: ""
        ```

    ??? variable string "`a_train_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        a_train_role_depends_on_delay: "0"
        ```

    ??? variable string "`a_train_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        a_train_role_depends_on_healthchecks:
        ```

    ??? variable bool "`a_train_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        a_train_role_diun_enabled: true
        ```

    ??? variable bool "`a_train_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        a_train_role_dns_enabled: true
        ```

    ??? variable bool "`a_train_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        a_train_role_docker_controller: true
        ```

    ??? variable bool "`a_train_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        a_train_role_docker_volumes_download:
        ```

    ??? variable bool "`a_train_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        a_train_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`a_train_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        a_train_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`a_train_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        a_train_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`a_train_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        a_train_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`a_train_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        a_train_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`a_train_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        a_train_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`a_train_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        a_train_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`a_train_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        a_train_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`a_train_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        a_train_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`a_train_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        a_train_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            a_train_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "a_train2.{{ user.domain }}"
              - "a_train.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`a_train_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        a_train_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            a_train_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'a_train2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`a_train_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        a_train_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
hide:
  - tags
tags:
  - a-train
  - train
  - google
---

# A-Train

## What is it?

A-Train is the official Autoscan trigger that listens for changes within Google Drive. It is the successor of Autoscan's Bernard trigger, which unfortunately contains enough logic errors to prompt a rewrite.

- Supports Shared Drives
- Service Account-based authentication
- Does not support My Drive
- Does not support encrypted files
- Does not support alternative authentication methods

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        a_train_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `a_train_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `a_train_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    a_train_name: a-train

    ```

??? example "Settings"

    ```yaml
    # Type: list
    a_train_role_remotes: [""]

    ```

??? example "Paths"

    ```yaml
    # Type: string
    a_train_role_paths_folder: "{{ a_train_name }}"

    # Type: string
    a_train_role_paths_location: "{{ server_appdata_path }}/{{ a_train_role_paths_folder }}"

    # Type: string
    a_train_role_paths_config_location: "{{ a_train_role_paths_location }}/a-train.toml"

    # Type: string
    a_train_role_paths_sa_location: "{{ a_train_role_paths_location }}/account.json"

    # Type: string
    a_train_role_paths_rclone_config_location: "/home/{{ user.name }}/.config/rclone/rclone.conf"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    a_train_role_docker_container: "{{ a_train_name }}"

    # Image
    # Type: bool (true/false)
    a_train_role_docker_image_pull: true

    # Type: string
    a_train_role_docker_image_repo: "ghcr.io/m-rots/a-train"

    # Type: string
    a_train_role_docker_image_tag: "latest"

    # Type: string
    a_train_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='a_train') }}:{{ lookup('role_var', '_docker_image_tag', role='a_train') }}"

    # Envs
    # Type: dict
    a_train_role_docker_envs_default: 
      TZ: "{{ tz }}"

    # Type: dict
    a_train_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    a_train_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='a_train') }}:/data"

    # Type: list
    a_train_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    a_train_role_docker_hostname: "{{ a_train_name }}"

    # Networks
    # Type: string
    a_train_role_docker_networks_alias: "{{ a_train_name }}"

    # Type: list
    a_train_role_docker_networks_default: []

    # Type: list
    a_train_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    a_train_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    a_train_role_docker_state: started

    # User
    # Type: string
    a_train_role_docker_user: "{{ uid }}:{{ gid }}"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    a_train_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    a_train_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    a_train_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    a_train_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    a_train_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    a_train_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    a_train_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    a_train_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    a_train_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    a_train_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    a_train_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    a_train_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    a_train_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    a_train_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    a_train_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    a_train_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    a_train_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        a_train_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "a_train2.{{ user.domain }}"
          - "a_train.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        a_train_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'a_train2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

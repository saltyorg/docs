---
hide:
  - tags
tags:
  - speedtest
  - monitoring
  - network
---

# Speedtest

## What is it?

[Speedtest](https://github.com/librespeed/speedtest)  is a very lightweight Speedtest implemented in Javascript, using XMLHttpRequest and Web Workers.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/librespeed/speedtest){: .header-icons } | [:octicons-link-16: Docs](https://github.com/librespeed/speedtest){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/librespeed/speedtest){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/librespeed){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-speedtest

```

### 2. URL

- To access Speedtest, visit `https://speedtest._yourdomain.com_`

### 3. Setup

To use a custom subdomain, add a custom value for `speedtest_web_subdomain` in the `/srv/git/saltbox/inventories/host_vars/localhost.yml` file. More info can be found [here](../../saltbox/inventory/index.md).

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        speedtest_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `speedtest_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `speedtest_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    speedtest_name: speedtest

    ```

??? example "Paths"

    ```yaml
    # Type: string
    speedtest_role_paths_folder: "{{ speedtest_name }}"

    # Type: string
    speedtest_role_paths_location: "{{ server_appdata_path }}/{{ speedtest_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    speedtest_role_web_subdomain: "{{ speedtest_name }}"

    # Type: string
    speedtest_role_web_domain: "{{ user.domain }}"

    # Type: string
    speedtest_role_web_port: "80"

    # Type: string
    speedtest_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='speedtest') + '.' + lookup('role_var', '_web_domain', role='speedtest')
                             if (lookup('role_var', '_web_subdomain', role='speedtest') | length > 0)
                             else lookup('role_var', '_web_domain', role='speedtest')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    speedtest_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='speedtest') }}"

    # Type: string
    speedtest_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='speedtest') }}"

    # Type: bool (true/false)
    speedtest_role_dns_proxy: false

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    speedtest_role_traefik_sso_middleware: ""

    # Type: string
    speedtest_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    speedtest_role_traefik_middleware_custom: ""

    # Type: string
    speedtest_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    speedtest_role_traefik_enabled: true

    # Type: bool (true/false)
    speedtest_role_traefik_api_enabled: false

    # Type: string
    speedtest_role_traefik_api_endpoint: ""

    ```

??? example "Theme"

    ```yaml
    # Options can be found at https://github.com/themepark-dev/theme.park
    # Type: bool (true/false)
    speedtest_role_themepark_enabled: false

    # Type: string
    speedtest_role_themepark_theme: "{{ global_themepark_theme }}"

    # Type: string
    speedtest_role_themepark_domain: "{{ global_themepark_domain }}"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    speedtest_role_docker_container: "{{ speedtest_name }}"

    # Image
    # Type: bool (true/false)
    speedtest_role_docker_image_pull: true

    # Type: string
    speedtest_role_docker_image_repo: "lscr.io/linuxserver/librespeed"

    # Type: string
    speedtest_role_docker_image_tag: "latest"

    # Type: string
    speedtest_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='speedtest') }}:{{ lookup('role_var', '_docker_image_tag', role='speedtest') }}"

    # Envs
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

    # Type: dict
    speedtest_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    speedtest_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='speedtest') }}:/config"

    # Type: list
    speedtest_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    speedtest_role_docker_hostname: "{{ speedtest_name }}"

    # Networks
    # Type: string
    speedtest_role_docker_networks_alias: "{{ speedtest_name }}"

    # Type: list
    speedtest_role_docker_networks_default: []

    # Type: list
    speedtest_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    speedtest_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    speedtest_role_docker_state: started

    # Force Kill
    # Type: bool (true/false)
    speedtest_role_docker_force_kill: true

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    speedtest_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    speedtest_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    speedtest_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    speedtest_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    speedtest_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    speedtest_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    speedtest_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    speedtest_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    speedtest_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    speedtest_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    speedtest_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    speedtest_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    speedtest_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    speedtest_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    speedtest_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    speedtest_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    speedtest_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        speedtest_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "speedtest2.{{ user.domain }}"
          - "speedtest.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        speedtest_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'speedtest2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

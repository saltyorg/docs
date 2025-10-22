---
hide:
  - tags
tags:
  - dockwatch
  - monitoring
  - docker
---

# Dockwatch

## What is it?

[Dockwatch](https://github.com/Notifiarr/dockwatch) is a simple UI driven way to manage updates & notifications for Docker containers.

- Link and control multiple servers
- Automatically locate and match container icons for non Unraid usage
- Update schedules for container image tags by a container basis
- Notifications by a container basis
- Automatically try to restart unhealthy containers
- Mass prune orphan images, volumes & networks
- Mass actions for containers [(re-)start/stop, pull, update]
- Group containers in a table view for easier management

!!! warning
    By default, the role is protected behind your Authelia/SSO middleware.

    Dockwatch is likely unable to take action on containers due to the security posture of the Docker socket proxy. You can override this behavior to allow Dockwatch to take actions by adding `dockwatch_post_enable: true` to your [inventory](../../saltbox/inventory/index.md) entries.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/Notifiarr/dockwatch){: .header-icons } | [:octicons-link-16: Docs](https://github.com/Notifiarr/dockwatch#environment-variables){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Notifiarr/dockwatch){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-dockwatch

```

### 2. URL

- To access dockwatch, visit `https://dockwatch.xDOMAIN_NAMEx`

### 3. Setup

Set up the update options first, if you want to set them all at the same time use the `updates` or `frequency` button in the top right corner.

Add your notifiarr API key in the notification tab in order to set up notifications.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        dockwatch_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `dockwatch_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `dockwatch_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    dockwatch_name: dockwatch

    ```

??? example "Settings"

    ```yaml
    # Type: bool (true/false)
    dockwatch_role_post_enable: false

    ```

??? example "Docker Socket Proxy"

    ```yaml
    # Type: dict
    dockwatch_role_docker_socket_proxy_envs: 
      ALLOW_START: "1"
      ALLOW_STOP: "1"
      ALLOW_RESTARTS: "1"
      CONTAINERS: "1"
      IMAGES: "1"
      NETWORKS: "1"
      PORTS: "1"
      POST: "{{ '1'
             if lookup('role_var', '_post_enable', role='dockwatch')
             else omit }}"
      VOLUMES: "1"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    dockwatch_role_paths_folder: "{{ dockwatch_name }}"

    # Type: string
    dockwatch_role_paths_location: "{{ server_appdata_path }}/{{ dockwatch_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    dockwatch_role_web_subdomain: "{{ dockwatch_name }}"

    # Type: string
    dockwatch_role_web_domain: "{{ user.domain }}"

    # Type: string
    dockwatch_role_web_port: "80"

    # Type: string
    dockwatch_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='dockwatch') + '.' + lookup('role_var', '_web_domain', role='dockwatch')
                             if (lookup('role_var', '_web_subdomain', role='dockwatch') | length > 0)
                             else lookup('role_var', '_web_domain', role='dockwatch')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    dockwatch_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='dockwatch') }}"

    # Type: string
    dockwatch_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='dockwatch') }}"

    # Type: bool (true/false)
    dockwatch_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    dockwatch_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    dockwatch_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    dockwatch_role_traefik_middleware_custom: ""

    # Type: string
    dockwatch_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    dockwatch_role_traefik_enabled: true

    # Type: bool (true/false)
    dockwatch_role_traefik_api_enabled: true

    # Type: string
    dockwatch_role_traefik_api_endpoint: "PathPrefix(`/api`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    dockwatch_role_docker_container: "{{ dockwatch_name }}"

    # Image
    # Type: bool (true/false)
    dockwatch_role_docker_image_pull: true

    # Type: string
    dockwatch_role_docker_image_repo: "ghcr.io/notifiarr/dockwatch"

    # Type: string
    dockwatch_role_docker_image_tag: "main"

    # Type: string
    dockwatch_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='dockwatch') }}:{{ lookup('role_var', '_docker_image_tag', role='dockwatch') }}"

    # Envs
    # Type: dict
    dockwatch_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"
      DOCKER_HOST: "{{ dockwatch_name }}-docker-socket-proxy:2375"

    # Type: dict
    dockwatch_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    dockwatch_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='dockwatch') }}:/config"

    # Type: list
    dockwatch_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    dockwatch_role_docker_hostname: "{{ dockwatch_name }}"

    # Networks
    # Type: string
    dockwatch_role_docker_networks_alias: "{{ dockwatch_name }}"

    # Type: list
    dockwatch_role_docker_networks_default: []

    # Type: list
    dockwatch_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    dockwatch_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    dockwatch_role_docker_state: started

    # Dependencies
    # Type: string
    dockwatch_role_depends_on: "{{ dockwatch_name }}-docker-socket-proxy"

    # Type: string
    dockwatch_role_depends_on_delay: "0"

    # Type: string
    dockwatch_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    dockwatch_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    dockwatch_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    dockwatch_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    dockwatch_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    dockwatch_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    dockwatch_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    dockwatch_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    dockwatch_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    dockwatch_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    dockwatch_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    dockwatch_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    dockwatch_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    dockwatch_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    dockwatch_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    dockwatch_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    dockwatch_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    dockwatch_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        dockwatch_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "dockwatch2.{{ user.domain }}"
          - "dockwatch.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        dockwatch_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'dockwatch2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

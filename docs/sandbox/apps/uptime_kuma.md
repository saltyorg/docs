---
hide:
  - tags
tags:
  - uptime-kuma
  - monitoring
  - uptime
---

# Uptime Kuma

## What is it?

[Uptime Kuma](https://github.com/louislam/uptime-kuma) is a self-hosted monitoring tool like "Uptime Robot".

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/louislam/uptime-kuma){: .header-icons } | [:octicons-link-16: Docs](https://github.com/louislam/uptime-kuma/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/louislam/uptime-kuma){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/louislam/uptime-kuma){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-uptime-kuma

```

### 2. URL

- To access Uptime Kuma, visit `https://uptime._yourdomain.com_`

### 3. Setup

Docker Monitoring: Use TCP/HTTP connection type with this address: `http://uptime-docker-socket-proxy:2375`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        uptime_kuma_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `uptime_kuma_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `uptime_kuma_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    uptime_kuma_name: uptime

    ```

??? example "Docker Socket Proxy"

    ```yaml
    # Type: dict
    uptime_kuma_role_docker_socket_proxy_envs: 
      CONTAINERS: "1"
      IMAGES: "1"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    uptime_kuma_role_paths_folder: "{{ uptime_kuma_name }}"

    # Type: string
    uptime_kuma_role_paths_location: "{{ server_appdata_path }}/{{ uptime_kuma_role_paths_folder }}"

    # Type: bool (true/false)
    uptime_kuma_role_paths_recursive: true

    ```

??? example "Web"

    ```yaml
    # Type: string
    uptime_kuma_role_web_subdomain: "{{ uptime_kuma_name }}"

    # Type: string
    uptime_kuma_role_web_domain: "{{ user.domain }}"

    # Type: string
    uptime_kuma_role_web_port: "3001"

    # Type: string
    uptime_kuma_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='uptime_kuma') + '.' + lookup('role_var', '_web_domain', role='uptime_kuma')
                               if (lookup('role_var', '_web_subdomain', role='uptime_kuma') | length > 0)
                               else lookup('role_var', '_web_domain', role='uptime_kuma')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    uptime_kuma_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='uptime_kuma') }}"

    # Type: string
    uptime_kuma_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='uptime_kuma') }}"

    # Type: bool (true/false)
    uptime_kuma_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    uptime_kuma_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    uptime_kuma_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    uptime_kuma_role_traefik_middleware_custom: ""

    # Type: string
    uptime_kuma_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    uptime_kuma_role_traefik_enabled: true

    # Type: bool (true/false)
    uptime_kuma_role_traefik_api_enabled: true

    # Type: string
    uptime_kuma_role_traefik_api_endpoint: "PathPrefix(`/icon.svg`) || PathPrefix(`/api`) || PathPrefix(`/assets`) || PathPrefix(`/status`) || PathPrefix(`/metrics`) || PathRegexp(`^/$`) || PathRegexp(`/upload/.*`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    uptime_kuma_role_docker_container: "{{ uptime_kuma_name }}"

    # Image
    # Type: bool (true/false)
    uptime_kuma_role_docker_image_pull: true

    # Type: string
    uptime_kuma_role_docker_image_tag: "1" # Temporary until v2 is released and migration is added

    # Type: string
    uptime_kuma_role_docker_image_repo: "louislam/uptime-kuma"

    # Type: string
    uptime_kuma_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='uptime_kuma') }}:{{ lookup('role_var', '_docker_image_tag', role='uptime_kuma') }}"

    # Envs
    # Type: dict
    uptime_kuma_role_docker_envs_default: 
      TZ: "{{ tz }}"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"

    # Type: dict
    uptime_kuma_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    uptime_kuma_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='uptime_kuma') }}:/app/data"

    # Type: list
    uptime_kuma_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    uptime_kuma_role_docker_hostname: "{{ uptime_kuma_name }}"

    # Networks
    # Type: string
    uptime_kuma_role_docker_networks_alias: "{{ uptime_kuma_name }}"

    # Type: list
    uptime_kuma_role_docker_networks_default: []

    # Type: list
    uptime_kuma_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    uptime_kuma_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    uptime_kuma_role_docker_state: started

    # Dependencies
    # Type: string
    uptime_kuma_role_depends_on: "{{ uptime_kuma_name }}-docker-socket-proxy"

    # Type: string
    uptime_kuma_role_depends_on_delay: "0"

    # Type: string
    uptime_kuma_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    uptime_kuma_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    uptime_kuma_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    uptime_kuma_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    uptime_kuma_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    uptime_kuma_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    uptime_kuma_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    uptime_kuma_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    uptime_kuma_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    uptime_kuma_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    uptime_kuma_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    uptime_kuma_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    uptime_kuma_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    uptime_kuma_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    uptime_kuma_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    uptime_kuma_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    uptime_kuma_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    uptime_kuma_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        uptime_kuma_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "uptime_kuma2.{{ user.domain }}"
          - "uptime_kuma.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        uptime_kuma_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'uptime_kuma2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

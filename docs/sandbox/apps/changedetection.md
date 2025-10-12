---
hide:
  - tags
tags:
  - changedetection
  - monitoring
  - websites
---

# Change Detection

## What is it?

[changedetection](https://github.com/dgtlmoon/changedetection.io) is a tool for tracking changes to websites.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://changedetection.io){: .header-icons } | [:octicons-link-16: Docs](https://github.com/dgtlmoon/changedetection.io){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/dgtlmoon/changedetection.io){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/changedetection.io){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-changedetection

```

### 2. URL

- To access changedetection, visit `https://changedetection._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        changedetection_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `changedetection_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `changedetection_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    changedetection_name: changedetection

    ```

??? example "Paths"

    ```yaml
    # Type: string
    changedetection_role_paths_folder: "{{ changedetection_name }}"

    # Type: string
    changedetection_role_paths_location: "{{ server_appdata_path }}/{{ changedetection_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    changedetection_role_web_subdomain: "{{ changedetection_name }}"

    # Type: string
    changedetection_role_web_domain: "{{ user.domain }}"

    # Type: string
    changedetection_role_web_port: "5000"

    # Type: string
    changedetection_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='changedetection') + '.' + lookup('role_var', '_web_domain', role='changedetection')
                                   if (lookup('role_var', '_web_subdomain', role='changedetection') | length > 0)
                                   else lookup('role_var', '_web_domain', role='changedetection')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    changedetection_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='changedetection') }}"

    # Type: string
    changedetection_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='changedetection') }}"

    # Type: bool (true/false)
    changedetection_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    changedetection_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    changedetection_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    changedetection_role_traefik_middleware_custom: ""

    # Type: string
    changedetection_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    changedetection_role_traefik_enabled: true

    # Type: bool (true/false)
    changedetection_role_traefik_api_enabled: true

    # Type: string
    changedetection_role_traefik_api_endpoint: "PathPrefix(`/api`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    changedetection_role_docker_container: "{{ changedetection_name }}"

    # Image
    # Type: bool (true/false)
    changedetection_role_docker_image_pull: true

    # Type: string
    changedetection_role_docker_image_repo: "lscr.io/linuxserver/changedetection.io"

    # Type: string
    changedetection_role_docker_image_tag: "latest"

    # Type: string
    changedetection_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='changedetection') }}:{{ lookup('role_var', '_docker_image_tag', role='changedetection') }}"

    # Envs
    # Type: dict
    changedetection_role_docker_envs_default: 
      TZ: "{{ tz }}"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      BASE_URL: "{{ lookup('role_var', '_web_url', role='changedetection') }}"

    # Type: dict
    changedetection_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    changedetection_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='changedetection') }}:/config"

    # Type: list
    changedetection_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    changedetection_role_docker_hostname: "{{ changedetection_name }}"

    # Networks
    # Type: string
    changedetection_role_docker_networks_alias: "{{ changedetection_name }}"

    # Type: list
    changedetection_role_docker_networks_default: []

    # Type: list
    changedetection_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    changedetection_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    changedetection_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    changedetection_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    changedetection_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    changedetection_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    changedetection_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    changedetection_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    changedetection_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    changedetection_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    changedetection_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    changedetection_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    changedetection_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    changedetection_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    changedetection_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    changedetection_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    changedetection_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    changedetection_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    changedetection_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    changedetection_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        changedetection_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "changedetection2.{{ user.domain }}"
          - "changedetection.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        changedetection_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'changedetection2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

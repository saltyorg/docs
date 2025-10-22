---
hide:
  - tags
tags:
  - vaultwarden
  - passwords
  - security
---

# vaultwarden

## What is it?

[vaultwarden](https://github.com/dani-garcia/vaultwarden) is an alternative implementation of the Bitwarden server API written in Rust and compatible with upstream Bitwarden clients*, perfect for self-hosted deployment where running the official resource-heavy service might not be ideal.

!!! note
      📢 This project was known as Bitwarden_RS and has been renamed to separate itself from the official Bitwarden server in the hopes of avoiding confusion and trademark/branding issues.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/dani-garcia/vaultwarden){: .header-icons } | [:octicons-link-16: Docs](https://github.com/dani-garcia/vaultwarden/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/dani-garcia/vaultwarden){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/vaultwarden/server){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-vaultwarden

```

### 2. URL

- To access vaultwarden, visit `https://vaultwarden.xDOMAIN_NAMEx`

### 3. Setup

  1. Visit the vaultwarden site at `https://vaultwarden.xDOMAIN_NAMEx`

  2. Sign up with any email address and password.

  3. To access the Admin Panel go to `https://vaultwarden.xDOMAIN_NAMEx/admin`

  4. You will need to enter an authentication key which you can find in `/opt/vaultwarden/env`. Look for `ADMIN_TOKEN=`.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        vaultwarden_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `vaultwarden_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `vaultwarden_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    vaultwarden_name: vaultwarden

    ```

??? example "Paths"

    ```yaml
    # Type: string
    vaultwarden_role_paths_folder: "{{ vaultwarden_name }}"

    # Type: string
    vaultwarden_role_paths_location: "{{ server_appdata_path }}/{{ vaultwarden_role_paths_folder }}"

    # Type: string
    vaultwarden_role_paths_config_location: "{{ vaultwarden_role_paths_location }}/env"

    ```

??? example "Web"

    ```yaml
    # Type: string
    vaultwarden_role_web_subdomain: "{{ vaultwarden_name }}"

    # Type: string
    vaultwarden_role_web_domain: "{{ user.domain }}"

    # Type: string
    vaultwarden_role_web_port: "6423"

    # Type: string
    vaultwarden_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='vaultwarden') + '.' + lookup('role_var', '_web_domain', role='vaultwarden')
                               if (lookup('role_var', '_web_subdomain', role='vaultwarden') | length > 0)
                               else lookup('role_var', '_web_domain', role='vaultwarden')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    vaultwarden_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='vaultwarden') }}"

    # Type: string
    vaultwarden_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='vaultwarden') }}"

    # Type: bool (true/false)
    vaultwarden_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    vaultwarden_role_traefik_sso_middleware: ""

    # Type: string
    vaultwarden_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    vaultwarden_role_traefik_middleware_custom: ""

    # Type: string
    vaultwarden_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    vaultwarden_role_traefik_enabled: true

    # Type: bool (true/false)
    vaultwarden_role_traefik_api_enabled: false

    # Type: string
    vaultwarden_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    vaultwarden_role_docker_container: "{{ vaultwarden_name }}"

    # Image
    # Type: bool (true/false)
    vaultwarden_role_docker_image_pull: true

    # Type: string
    vaultwarden_role_docker_image_repo: "vaultwarden/server"

    # Type: string
    vaultwarden_role_docker_image_tag: "latest"

    # Type: string
    vaultwarden_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='vaultwarden') }}:{{ lookup('role_var', '_docker_image_tag', role='vaultwarden') }}"

    # Envs
    # Type: dict
    vaultwarden_role_docker_envs_default: 
      TZ: "{{ tz }}"
      ROCKET_PORT: "{{ lookup('role_var', '_web_port', role='vaultwarden') }}"

    # Type: dict
    vaultwarden_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    vaultwarden_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='vaultwarden') }}:/data"
      - "{{ lookup('role_var', '_paths_location', role='vaultwarden') }}/env:/.env"

    # Type: list
    vaultwarden_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    vaultwarden_role_docker_hostname: "{{ vaultwarden_name }}"

    # Networks
    # Type: string
    vaultwarden_role_docker_networks_alias: "{{ vaultwarden_name }}"

    # Type: list
    vaultwarden_role_docker_networks_default: []

    # Type: list
    vaultwarden_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    vaultwarden_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    vaultwarden_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    vaultwarden_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    vaultwarden_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    vaultwarden_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    vaultwarden_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    vaultwarden_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    vaultwarden_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    vaultwarden_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    vaultwarden_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    vaultwarden_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    vaultwarden_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    vaultwarden_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    vaultwarden_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    vaultwarden_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    vaultwarden_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    vaultwarden_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    vaultwarden_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    vaultwarden_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        vaultwarden_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "vaultwarden2.{{ user.domain }}"
          - "vaultwarden.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        vaultwarden_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'vaultwarden2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

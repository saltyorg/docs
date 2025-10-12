---
hide:
  - tags
tags:
  - barcodebuddy
  - grocy
  - inventory
---

# BarcodeBuddy

## What is it?

[BarcodeBuddy](https://github.com/Forceu/barcodebuddy) is a barcode system for Grocy that enables barcode scanning and product management. It automatically handles known and unknown barcodes, integrating seamlessly with Grocy's inventory management system.

!!! info
    By default, the role is **NOT** protected behind your Authelia/SSO middleware. You will need to configure authentication within the application.

| Details     |             |             |
|-------------|-------------|-------------|
| [:octicons-mark-github-16: Github](https://github.com/Forceu/barcodebuddy){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/f0rc3/barcodebuddy){: .header-icons } | [:octicons-link-16: Docs](https://barcodebuddy-documentation.readthedocs.io/){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-barcodebuddy
```

### 2. URL

- To access BarcodeBuddy, visit `https://barcodebuddy._yourdomain.com_`

### 3. Setup

Configure the connection to your Grocy instance through the application settings and set up user authentication.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        barcodebuddy_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `barcodebuddy_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `barcodebuddy_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    barcodebuddy_name: barcodebuddy

    ```

??? example "Paths"

    ```yaml
    # Type: string
    barcodebuddy_role_paths_folder: "{{ barcodebuddy_name }}"

    # Type: string
    barcodebuddy_role_paths_location: "{{ server_appdata_path }}/{{ barcodebuddy_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    barcodebuddy_role_web_subdomain: "{{ barcodebuddy_name }}"

    # Type: string
    barcodebuddy_role_web_domain: "{{ user.domain }}"

    # Type: string
    barcodebuddy_role_web_port: "80"

    # Type: string
    barcodebuddy_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='barcodebuddy') + '.' + lookup('role_var', '_web_domain', role='barcodebuddy')
                                if (lookup('role_var', '_web_subdomain', role='barcodebuddy') | length > 0)
                                else lookup('role_var', '_web_domain', role='barcodebuddy')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    barcodebuddy_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='barcodebuddy') }}"

    # Type: string
    barcodebuddy_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='barcodebuddy') }}"

    # Type: bool (true/false)
    barcodebuddy_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    barcodebuddy_role_traefik_sso_middleware: ""

    # Type: string
    barcodebuddy_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    barcodebuddy_role_traefik_middleware_custom: ""

    # Type: string
    barcodebuddy_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    barcodebuddy_role_traefik_enabled: true

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    barcodebuddy_role_docker_container: "{{ barcodebuddy_name }}"

    # Image
    # Type: bool (true/false)
    barcodebuddy_role_docker_image_pull: true

    # Type: string
    barcodebuddy_role_docker_image_repo: "f0rc3/barcodebuddy"

    # Type: string
    barcodebuddy_role_docker_image_tag: "latest"

    # Type: string
    barcodebuddy_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='barcodebuddy') }}:{{ lookup('role_var', '_docker_image_tag', role='barcodebuddy') }}"

    # Envs
    # Type: dict
    barcodebuddy_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    barcodebuddy_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    barcodebuddy_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='barcodebuddy') }}:/config"

    # Type: list
    barcodebuddy_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    barcodebuddy_role_docker_hostname: "{{ barcodebuddy_name }}"

    # Networks
    # Type: string
    barcodebuddy_role_docker_networks_alias: "{{ barcodebuddy_name }}"

    # Type: list
    barcodebuddy_role_docker_networks_default: []

    # Type: list
    barcodebuddy_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    barcodebuddy_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    barcodebuddy_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    barcodebuddy_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    barcodebuddy_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    barcodebuddy_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    barcodebuddy_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    barcodebuddy_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    barcodebuddy_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    barcodebuddy_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    barcodebuddy_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    barcodebuddy_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    barcodebuddy_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    barcodebuddy_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    barcodebuddy_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    barcodebuddy_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    barcodebuddy_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    barcodebuddy_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    barcodebuddy_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    barcodebuddy_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        barcodebuddy_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "barcodebuddy2.{{ user.domain }}"
          - "barcodebuddy.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        barcodebuddy_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'barcodebuddy2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

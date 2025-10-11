---
hide:
  - tags
tags:
  - pufferpanel
  - gaming
  - servers
---

# PufferPanel

## What is it?

[PufferPanel](https://pufferpanel.com/) is an open-source web-based game server management system designed for both small networks and personal use. It supports Minecraft, Source Dedicated Servers, BungeeCord, and many other game servers.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://pufferpanel.com/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/pufferpanel/pufferpanel){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/pufferpanel/pufferpanel){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-pufferpanel
```

### 2. URL

- To access PufferPanel, visit `https://pufferpanel._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        pufferpanel_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    pufferpanel_name: pufferpanel

    ```

??? example "Paths"

    ```yaml
    # Type: string
    pufferpanel_role_paths_folder: "{{ pufferpanel_name }}"

    # Type: string
    pufferpanel_role_paths_location: "{{ server_appdata_path }}/{{ pufferpanel_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    pufferpanel_role_web_subdomain: "{{ pufferpanel_name }}"

    # Type: string
    pufferpanel_role_web_domain: "{{ user.domain }}"

    # Type: string
    pufferpanel_role_web_port: "8080"

    # Type: string
    pufferpanel_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='pufferpanel') + '.' + lookup('role_var', '_web_domain', role='pufferpanel')
                               if (lookup('role_var', '_web_subdomain', role='pufferpanel') | length > 0)
                               else lookup('role_var', '_web_domain', role='pufferpanel')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    pufferpanel_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='pufferpanel') }}"

    # Type: string
    pufferpanel_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='pufferpanel') }}"

    # Type: bool (true/false)
    pufferpanel_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    pufferpanel_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    pufferpanel_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    pufferpanel_role_traefik_middleware_custom: ""

    # Type: string
    pufferpanel_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    pufferpanel_role_traefik_enabled: true

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    pufferpanel_role_docker_container: "{{ pufferpanel_name }}"

    # Image
    # Type: bool (true/false)
    pufferpanel_role_docker_image_pull: true

    # Type: string
    pufferpanel_role_docker_image_repo: "pufferpanel/pufferpanel"

    # Type: string
    pufferpanel_role_docker_image_tag: "latest"

    # Type: string
    pufferpanel_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='pufferpanel') }}:{{ lookup('role_var', '_docker_image_tag', role='pufferpanel') }}"

    # Ports
    # Type: list
    pufferpanel_role_docker_ports_defaults: 
      - "5657:5657"

    # Type: list
    pufferpanel_role_docker_ports_custom: []

    # Envs
    # Type: dict
    pufferpanel_role_docker_envs_default: 
      TZ: "{{ tz }}"
      GIN_MODE: "release"

    # Type: dict
    pufferpanel_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    pufferpanel_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='pufferpanel') }}/config:/etc/pufferpanel"
      - "{{ lookup('role_var', '_paths_location', role='pufferpanel') }}/data:/var/lib/pufferpanel"
      - "{{ lookup('role_var', '_paths_location', role='pufferpanel') }}/logs:/var/log/pufferpanel"
      - "/var/run/docker.sock:/var/run/docker.sock"

    # Type: list
    pufferpanel_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    pufferpanel_role_docker_hostname: "{{ pufferpanel_name }}"

    # Networks
    # Type: string
    pufferpanel_role_docker_networks_alias: "{{ pufferpanel_name }}"

    # Type: list
    pufferpanel_role_docker_networks_default: []

    # Type: list
    pufferpanel_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    pufferpanel_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    pufferpanel_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    pufferpanel_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    pufferpanel_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    pufferpanel_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    pufferpanel_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    pufferpanel_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    pufferpanel_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    pufferpanel_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    pufferpanel_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    pufferpanel_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    pufferpanel_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    pufferpanel_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    pufferpanel_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    pufferpanel_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    pufferpanel_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    pufferpanel_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    pufferpanel_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    pufferpanel_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        pufferpanel_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "pufferpanel2.{{ user.domain }}"
          - "pufferpanel.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        pufferpanel_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'pufferpanel2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

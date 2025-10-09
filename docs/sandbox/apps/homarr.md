---
hide:
  - tags
tags:
  - homarr
  - dashboard
  - homepage
---

# Homarr

## What is it?

[Homarr](https://www.homarr.dev/) is a simple and modern homepage for your server that helps you access all of your services in one place. It integrates with the services you use to display useful information or control them. It's easy to install and supports many different devices.

- Integrates with services you use.
- Search the web directly from your homepage.
- Search overseerr directly from your homepage.
- Real-time status indicator for every service.
- Automatically finds icons while you type the name of a service.
- Widgets that can display all types of information.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://homarr.dev/){: .header-icons } | [:octicons-link-16: Docs](https://homarr.dev/docs/getting-started/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/ajnart/homarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/ajnart/homarr/){: .header-icons }|

Recommended install types: Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-homarr

```

### 2. URL

- To access homarr, visit `https://homarr._yourdomain.com_`

### 3. Setup

- Default login:

  ``` { .yaml}

  Password: your_normal_password

  ```

- [:octicons-link-16: Documentation: Homarr Docs](https://homarr.dev/docs/getting-started/){: .header-icons }

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        homarr_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    homarr_name: homarr

    ```

??? example "Docker Socket Proxy"

    ```yaml
    # Type: dict
    homarr_role_docker_socket_proxy_envs: 
      CONTAINERS: "1"
      POST: "0"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    homarr_role_paths_folder: "{{ homarr_name }}"

    # Type: string
    homarr_role_paths_location: "{{ server_appdata_path }}/{{ homarr_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    homarr_role_web_subdomain: "{{ homarr_name }}"

    # Type: string
    homarr_role_web_domain: "{{ user.domain }}"

    # Type: string
    homarr_role_web_port: "7575"

    # Type: string
    homarr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='homarr') + '.' + lookup('role_var', '_web_domain', role='homarr')
                          if (lookup('role_var', '_web_subdomain', role='homarr') | length > 0)
                          else lookup('role_var', '_web_domain', role='homarr')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    homarr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='homarr') }}"

    # Type: string
    homarr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='homarr') }}"

    # Type: bool (true/false)
    homarr_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    homarr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    homarr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    homarr_role_traefik_middleware_custom: ""

    # Type: string
    homarr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    homarr_role_traefik_enabled: true

    # Type: bool (true/false)
    homarr_role_traefik_api_enabled: false

    # Type: string
    homarr_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    homarr_role_docker_container: "{{ homarr_name }}"

    # Image
    # Type: bool (true/false)
    homarr_role_docker_image_pull: true

    # Type: string
    homarr_role_docker_image_repo: "ghcr.io/ajnart/homarr"

    # Type: string
    homarr_role_docker_image_tag: "latest"

    # Type: string
    homarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='homarr') }}:{{ lookup('role_var', '_docker_image_tag', role='homarr') }}"

    # Envs
    # Type: dict
    homarr_role_docker_envs_default: 
      TZ: "{{ tz }}"
      BASE_URL: "{{ lookup('role_var', '_web_subdomain', role='homarr') + '.' + lookup('role_var', '_web_domain', role='homarr') }}"
      PASSWORD: "{{ user.pass }}"
      DOCKER_HOST: "tcp://{{ homarr_name }}-docker-socket-proxy:2375"
      NODE_TLS_REJECT_UNAUTHORIZED: "0"

    # Type: dict
    homarr_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    homarr_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='homarr') }}:/app/data/configs"
      - "{{ lookup('role_var', '_paths_location', role='homarr') }}/icons:/app/public/icons"

    # Type: list
    homarr_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    homarr_role_docker_hostname: "{{ homarr_name }}"

    # Networks
    # Type: string
    homarr_role_docker_networks_alias: "{{ homarr_name }}"

    # Type: list
    homarr_role_docker_networks_default: []

    # Type: list
    homarr_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    homarr_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    homarr_role_docker_state: started

    # Dependencies
    # Type: string
    homarr_role_depends_on: "{{ homarr_name }}-docker-socket-proxy"

    # Type: string
    homarr_role_depends_on_delay: "0"

    # Type: string
    homarr_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    homarr_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    homarr_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    homarr_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    homarr_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    homarr_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    homarr_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    homarr_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    homarr_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    homarr_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    homarr_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    homarr_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    homarr_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    homarr_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    homarr_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    homarr_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    homarr_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    homarr_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        homarr_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "homarr_role_web_fqdn_override2.{{ user.domain }}"
          - "homarr_role_web_fqdn_override.new-domain.tld"
        ```
        
        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries
        

    2.  Example:

        ```yaml
        homarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'homarr_role_web_host_override2.' + user.domain }}`)"
        ```
        
        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule
        

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

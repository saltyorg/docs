---
hide:
  - tags
tags:
  - heimdall
  - dashboard
  - homepage
---

# Heimdall

## What is it?

[Heimdall](https://heimdall.site/) is a way to organise all those links to your most used web sites and web applications in a simple way. Simplicity is the key to Heimdall. Why not use it as your browser start page? It even has the ability to include a search bar using either Google, Bing or DuckDuckGo.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://heimdall.site/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/linuxserver/Heimdall-Apps){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/linuxserver/Heimdall){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/heimdall){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-heimdall

```

### 2. URL

- To access Heimdall, visit `https://heimdall._yourdomain.com_`

### 3. Setup

- The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        heimdall_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    heimdall_name: heimdall

    ```

??? example "Paths"

    ```yaml
    # Type: string
    heimdall_role_paths_folder: "{{ heimdall_name }}"

    # Type: string
    heimdall_role_paths_location: "{{ server_appdata_path }}/{{ heimdall_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    heimdall_role_web_subdomain: "{{ heimdall_name }}"

    # Type: string
    heimdall_role_web_domain: "{{ user.domain }}"

    # Type: string
    heimdall_role_web_port: "80"

    # Type: string
    heimdall_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='heimdall') + '.' + lookup('role_var', '_web_domain', role='heimdall')
                            if (lookup('role_var', '_web_subdomain', role='heimdall') | length > 0)
                            else lookup('role_var', '_web_domain', role='heimdall')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    heimdall_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='heimdall') }}"

    # Type: string
    heimdall_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='heimdall') }}"

    # Type: bool (true/false)
    heimdall_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    heimdall_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    heimdall_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    heimdall_role_traefik_middleware_custom: ""

    # Type: string
    heimdall_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    heimdall_role_traefik_enabled: true

    # Type: bool (true/false)
    heimdall_role_traefik_api_enabled: false

    # Type: string
    heimdall_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    heimdall_role_docker_container: "{{ heimdall_name }}"

    # Image
    # Type: bool (true/false)
    heimdall_role_docker_image_pull: true

    # Type: string
    heimdall_role_docker_image_repo: "lscr.io/linuxserver/heimdall"

    # Type: string
    heimdall_role_docker_image_tag: "latest"

    # Type: string
    heimdall_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='heimdall') }}:{{ lookup('role_var', '_docker_image_tag', role='heimdall') }}"

    # Envs
    # Type: dict
    heimdall_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    heimdall_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    heimdall_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='heimdall') }}:/config"

    # Type: list
    heimdall_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    heimdall_role_docker_hostname: "{{ heimdall_name }}"

    # Networks
    # Type: string
    heimdall_role_docker_networks_alias: "{{ heimdall_name }}"

    # Type: list
    heimdall_role_docker_networks_default: []

    # Type: list
    heimdall_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    heimdall_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    heimdall_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    heimdall_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    heimdall_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    heimdall_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    heimdall_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    heimdall_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    heimdall_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    heimdall_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    heimdall_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    heimdall_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    heimdall_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    heimdall_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    heimdall_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    heimdall_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    heimdall_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    heimdall_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    heimdall_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    heimdall_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        heimdall_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "heimdall2.{{ user.domain }}"
          - "heimdall.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        heimdall_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'heimdall2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

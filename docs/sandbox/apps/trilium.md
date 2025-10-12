---
hide:
  - tags
tags:
  - trilium
  - productivity
  - notes
---

# Trilium Notes

## What is it?

[Trilium Notes](https://github.com/zadam/trilium) is a hierarchical note taking application with focus on building large personal knowledge bases.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/zadam/trilium){: .header-icons } | [:octicons-link-16: Docs](https://github.com/zadam/trilium/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/zadam/trilium){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/zadam/trilium){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-trilium

```

### 2. URL

- To access Trilium Notes, visit `https://trilium._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        trilium_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `trilium_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `trilium_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    trilium_name: trilium

    ```

??? example "Paths"

    ```yaml
    # Type: string
    trilium_role_paths_folder: "{{ trilium_name }}"

    # Type: string
    trilium_role_paths_location: "{{ server_appdata_path }}/{{ trilium_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    trilium_role_web_subdomain: "{{ trilium_name }}"

    # Type: string
    trilium_role_web_domain: "{{ user.domain }}"

    # Type: string
    trilium_role_web_port: "8080"

    # Type: string
    trilium_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='trilium') + '.' + lookup('role_var', '_web_domain', role='trilium')
                           if (lookup('role_var', '_web_subdomain', role='trilium') | length > 0)
                           else lookup('role_var', '_web_domain', role='trilium')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    trilium_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='trilium') }}"

    # Type: string
    trilium_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='trilium') }}"

    # Type: bool (true/false)
    trilium_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    trilium_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    trilium_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    trilium_role_traefik_middleware_custom: ""

    # Type: string
    trilium_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    trilium_role_traefik_enabled: true

    # Type: bool (true/false)
    trilium_role_traefik_api_enabled: false

    # Type: string
    trilium_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    trilium_role_docker_container: "{{ trilium_name }}"

    # Image
    # Type: bool (true/false)
    trilium_role_docker_image_pull: true

    # Type: string
    trilium_role_docker_image_repo: "triliumnext/notes"

    # Type: string
    trilium_role_docker_image_tag: "latest"

    # Type: string
    trilium_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='trilium') }}:{{ lookup('role_var', '_docker_image_tag', role='trilium') }}"

    # Envs
    # Type: dict
    trilium_role_docker_envs_default: 
      USER_UID: "{{ uid }}"
      USER_GID: "{{ gid }}"
      TZ: "{{ tz }}"
      TRILIUM_DATA_DIR: "/home/node/trilium-data"

    # Type: dict
    trilium_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    trilium_role_docker_volumes_default: 
      - "{{ trilium_role_paths_location }}:/home/node/trilium-data"

    # Type: list
    trilium_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    trilium_role_docker_hostname: "{{ trilium_name }}"

    # Networks
    # Type: string
    trilium_role_docker_networks_alias: "{{ trilium_name }}"

    # Type: list
    trilium_role_docker_networks_default: []

    # Type: list
    trilium_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    trilium_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    trilium_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    trilium_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    trilium_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    trilium_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    trilium_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    trilium_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    trilium_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    trilium_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    trilium_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    trilium_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    trilium_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    trilium_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    trilium_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    trilium_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    trilium_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    trilium_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    trilium_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    trilium_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        trilium_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "trilium2.{{ user.domain }}"
          - "trilium.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        trilium_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'trilium2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
hide:
  - tags
tags:
  - unmanic
  - media
  - encoding
---

# Unmanic

## What is it?

[Unmanic](https://github.com/Unmanic/unmanic) is a simple tool for optimising your file library. You can use it to convert your files into a single, uniform format, manage file movements based on timestamps, or execute custom commands against a file based on its file size.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/Unmanic/unmanic){: .header-icons } | [:octicons-link-16: Docs](https://github.com/Unmanic/unmanic/blob/master/docs/configuration/README.md){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Unmanic/unmanic){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/josh5/unmanic){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-unmanic

```

### 2. URL

- To access Unmanic, visit `https://unmanic._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        unmanic_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `unmanic_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `unmanic_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    unmanic_name: unmanic

    ```

??? example "Paths"

    ```yaml
    # Type: string
    unmanic_role_paths_folder: "{{ unmanic_name }}"

    # Type: string
    unmanic_role_paths_location: "{{ server_appdata_path }}/{{ unmanic_role_paths_folder }}"

    # Type: string
    unmanic_role_paths_transcodes_location: "{{ transcodes_path }}/{{ unmanic_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    unmanic_role_web_subdomain: "{{ unmanic_name }}"

    # Type: string
    unmanic_role_web_domain: "{{ user.domain }}"

    # Type: string
    unmanic_role_web_port: "8888"

    # Type: string
    unmanic_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='unmanic') + '.' + lookup('role_var', '_web_domain', role='unmanic')
                           if (lookup('role_var', '_web_subdomain', role='unmanic') | length > 0)
                           else lookup('role_var', '_web_domain', role='unmanic')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    unmanic_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='unmanic') }}"

    # Type: string
    unmanic_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='unmanic') }}"

    # Type: bool (true/false)
    unmanic_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    unmanic_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    unmanic_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    unmanic_role_traefik_middleware_custom: ""

    # Type: string
    unmanic_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    unmanic_role_traefik_enabled: true

    # Type: bool (true/false)
    unmanic_role_traefik_api_enabled: false

    # Type: string
    unmanic_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    unmanic_role_docker_container: "{{ unmanic_name }}"

    # Image
    # Type: bool (true/false)
    unmanic_role_docker_image_pull: true

    # Type: string
    unmanic_role_docker_image_repo: "josh5/unmanic"

    # Type: string
    unmanic_role_docker_image_tag: "latest"

    # Type: string
    unmanic_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='unmanic') }}:{{ lookup('role_var', '_docker_image_tag', role='unmanic') }}"

    # Envs
    # Type: dict
    unmanic_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    unmanic_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    unmanic_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='unmanic') }}:/config"
      - "{{ lookup('role_var', '_paths_transcodes_location', role='unmanic') }}:/tmp/unmanic"
      - "/mnt/unionfs/Media:/library"

    # Type: list
    unmanic_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    unmanic_role_docker_hostname: "{{ unmanic_name }}"

    # Networks
    # Type: string
    unmanic_role_docker_networks_alias: "{{ unmanic_name }}"

    # Type: list
    unmanic_role_docker_networks_default: []

    # Type: list
    unmanic_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    unmanic_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    unmanic_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    unmanic_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    unmanic_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    unmanic_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    unmanic_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    unmanic_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    unmanic_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    unmanic_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    unmanic_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    unmanic_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    unmanic_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    unmanic_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    unmanic_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    unmanic_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    unmanic_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    unmanic_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    unmanic_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    unmanic_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        unmanic_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "unmanic2.{{ user.domain }}"
          - "unmanic.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        unmanic_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'unmanic2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

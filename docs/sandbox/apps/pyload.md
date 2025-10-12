---
hide:
  - tags
tags:
  - pyload
  - download
  - tools
---

# pyload

## THIS DOCUMENTATION IS NOT YET COMPLETED

## What is it?

[pyload](https://pyload.net/) is a...

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://pyload.url){: .header-icons } | [:octicons-link-16: Docs](https://pyload.docs.url){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/pyload/pyload){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/pyload/pyload){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-pyload

```

### 2. URL

- To access pyload, visit `https://pyload._yourdomain.com_`
- Default credentials are - username: pyload - password: pyload

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        pyload_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `pyload_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `pyload_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    pyload_name: pyload

    ```

??? example "Paths"

    ```yaml
    # Type: string
    pyload_role_paths_folder: "{{ pyload_name }}"

    # Type: string
    pyload_role_paths_location: "{{ server_appdata_path }}/{{ pyload_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    pyload_role_web_subdomain: "{{ pyload_name }}"

    # Type: string
    pyload_role_web_domain: "{{ user.domain }}"

    # Type: string
    pyload_role_web_port: "8000"

    # Type: string
    pyload_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='pyload') + '.' + lookup('role_var', '_web_domain', role='pyload')
                          if (lookup('role_var', '_web_subdomain', role='pyload') | length > 0)
                          else lookup('role_var', '_web_domain', role='pyload')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    pyload_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='pyload') }}"

    # Type: string
    pyload_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='pyload') }}"

    # Type: bool (true/false)
    pyload_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    pyload_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    pyload_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    pyload_role_traefik_middleware_custom: ""

    # Type: string
    pyload_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    pyload_role_traefik_enabled: true

    # Type: bool (true/false)
    pyload_role_traefik_api_enabled: false

    # Type: string
    pyload_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    pyload_role_docker_container: "{{ pyload_name }}"

    # Image
    # Type: bool (true/false)
    pyload_role_docker_image_pull: true

    # Type: string
    pyload_role_docker_image_repo: "lscr.io/linuxserver/pyload-ng"

    # Type: string
    pyload_role_docker_image_tag: "latest"

    # Type: string
    pyload_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='pyload') }}:{{ lookup('role_var', '_docker_image_tag', role='pyload') }}"

    # Envs
    # Type: dict
    pyload_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    pyload_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    pyload_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='pyload') }}:/config"

    # Type: list
    pyload_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    pyload_role_docker_hostname: "{{ pyload_name }}"

    # Networks
    # Type: string
    pyload_role_docker_networks_alias: "{{ pyload_name }}"

    # Type: list
    pyload_role_docker_networks_default: []

    # Type: list
    pyload_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    pyload_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    pyload_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    pyload_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    pyload_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    pyload_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    pyload_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    pyload_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    pyload_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    pyload_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    pyload_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    pyload_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    pyload_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    pyload_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    pyload_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    pyload_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    pyload_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    pyload_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    pyload_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    pyload_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        pyload_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "pyload2.{{ user.domain }}"
          - "pyload.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        pyload_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'pyload2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

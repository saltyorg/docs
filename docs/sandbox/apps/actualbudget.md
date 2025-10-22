---
hide:
  - tags
tags:
  - actualbudget
  - budget
  - finance
---

# Actual Budget
## What is it?

[Actual Budget](https://actualbudget.org/) is a super fast, privacy-focused app for managing your finances. Its heart is the well-proven and much-loved Envelope Budgeting methodology.
You own your data and can do whatever you want with it. Featuring multi-device sync, optional end-to-end encryption and so much more.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://actualbudget.org){: .header-icons } | [:octicons-link-16: Docs](https://actualbudget.org/docs){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/actualbudget/actual){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/actualbudget/actual-server){: .header-icons }|

## 1. Installation

``sb install sandbox-actualbudget``

## 2. URL

To access Actual Budget, visit ``https://actualbudget.xDOMAIN_NAMEx``

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        actualbudget_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `actualbudget_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `actualbudget_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    actualbudget_name: actualbudget

    ```

??? example "Paths"

    ```yaml
    # Type: string
    actualbudget_role_paths_folder: "{{ actualbudget_name }}"

    # Type: string
    actualbudget_role_paths_location: "{{ server_appdata_path }}/{{ actualbudget_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    actualbudget_role_web_subdomain: "{{ actualbudget_name }}"

    # Type: string
    actualbudget_role_web_domain: "{{ user.domain }}"

    # Type: string
    actualbudget_role_web_port: "5006"

    # Type: string
    actualbudget_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='actualbudget') + '.' + lookup('role_var', '_web_domain', role='actualbudget')
                                if (lookup('role_var', '_web_subdomain', role='actualbudget') | length > 0)
                                else lookup('role_var', '_web_domain', role='actualbudget')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    actualbudget_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='actualbudget') }}"

    # Type: string
    actualbudget_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='actualbudget') }}"

    # Type: bool (true/false)
    actualbudget_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    actualbudget_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    actualbudget_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    actualbudget_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: string
    actualbudget_role_traefik_middleware_custom: ""

    # Type: bool (true/false)
    actualbudget_role_traefik_enabled: true

    # Type: bool (true/false)
    actualbudget_role_traefik_api_enabled: false

    # Type: string
    actualbudget_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    actualbudget_role_docker_container: "{{ actualbudget_name }}"

    # Image
    # Type: bool (true/false)
    actualbudget_role_docker_image_pull: true

    # Type: string
    actualbudget_role_docker_image_repo: "actualbudget/actual-server"

    # Type: string
    actualbudget_role_docker_image_tag: "latest"

    # Type: string
    actualbudget_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='actualbudget') }}:{{ lookup('role_var', '_docker_image_tag', role='actualbudget') }}"

    # Envs
    # Type: dict
    actualbudget_role_docker_envs_default: 
      TZ: "{{ tz }}"

    # Type: dict
    actualbudget_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    actualbudget_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='actualbudget') }}:/data"
      - "/etc/localtime:/etc/localtime:ro"

    # Type: list
    actualbudget_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    actualbudget_role_docker_hostname: "{{ actualbudget_name }}"

    # Networks
    # Type: string
    actualbudget_role_docker_networks_alias: "{{ actualbudget_name }}"

    # Type: list
    actualbudget_role_docker_networks_default: []

    # Type: list
    actualbudget_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    actualbudget_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    actualbudget_role_docker_state: started

    # User
    # Type: string
    actualbudget_role_docker_user: "{{ uid }}:{{ gid }}"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    actualbudget_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    actualbudget_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    actualbudget_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    actualbudget_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    actualbudget_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    actualbudget_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    actualbudget_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    actualbudget_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    actualbudget_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    actualbudget_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    actualbudget_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    actualbudget_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    actualbudget_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    actualbudget_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    actualbudget_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    actualbudget_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    actualbudget_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        actualbudget_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "actualbudget2.{{ user.domain }}"
          - "actualbudget.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        actualbudget_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'actualbudget2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

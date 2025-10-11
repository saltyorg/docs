---
hide:
  - tags
tags:
  - openobserve
  - observability
  - logs
---

# OpenObserve

## What is it?

[OpenObserve](https://openobserve.ai/) is an open-source observability platform for logs, metrics, and traces with 140x lower storage cost than Elasticsearch. Built for petabyte scale with high performance and ~40x compression.

!!! info
    By default, the role is **NOT** protected behind your Authelia/SSO middleware. You will need to configure authentication within the application.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://openobserve.ai/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/openobserve/openobserve){: .header-icons } | [:octicons-link-16: Docs](https://openobserve.ai/docs/){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-openobserve
```

### 2. URL

- To access OpenObserve, visit `https://openobserve._yourdomain.com_`

### 3. Setup

Default credentials are configured using your user email and password. Root user setup is required for initial access.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        openobserve_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    openobserve_name: openobserve

    ```

??? example "Paths"

    ```yaml
    # Type: string
    openobserve_role_paths_folder: "{{ openobserve_name }}"

    # Type: string
    openobserve_role_paths_location: "{{ server_appdata_path }}/{{ openobserve_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    openobserve_role_web_subdomain: "{{ openobserve_name }}"

    # Type: string
    openobserve_role_web_domain: "{{ user.domain }}"

    # Type: string
    openobserve_role_web_port: "5080"

    # Type: string
    openobserve_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='openobserve') + '.' + lookup('role_var', '_web_domain', role='openobserve')
                               if (lookup('role_var', '_web_subdomain', role='openobserve') | length > 0)
                               else lookup('role_var', '_web_domain', role='openobserve')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    openobserve_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='openobserve') }}"

    # Type: string
    openobserve_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='openobserve') }}"

    # Type: bool (true/false)
    openobserve_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    openobserve_role_traefik_sso_middleware: ""

    # Type: string
    openobserve_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    openobserve_role_traefik_middleware_custom: ""

    # Type: string
    openobserve_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    openobserve_role_traefik_enabled: true

    # Type: bool (true/false)
    openobserve_role_traefik_api_enabled: false

    # Type: string
    openobserve_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    openobserve_role_docker_container: "{{ openobserve_name }}"

    # Image
    # Type: bool (true/false)
    openobserve_role_docker_image_pull: true

    # Type: string
    openobserve_role_docker_image_tag: "latest"

    # Type: string
    openobserve_role_docker_image_repo: "public.ecr.aws/zinclabs/openobserve"

    # Type: string
    openobserve_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='openobserve') }}:{{ lookup('role_var', '_docker_image_tag', role='openobserve') }}"

    # Envs
    # Type: dict
    openobserve_role_docker_envs_default: 
      TZ: "{{ tz }}"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      ZO_ROOT_USER_EMAIL: "{{ user.email }}"
      ZO_ROOT_USER_PASSWORD: "{{ user.pass }}"

    # Type: dict
    openobserve_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    openobserve_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='openobserve') }}:/data"

    # Type: list
    openobserve_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    openobserve_role_docker_hostname: "{{ openobserve_name }}"

    # Networks
    # Type: string
    openobserve_role_docker_networks_alias: "{{ openobserve_name }}"

    # Type: list
    openobserve_role_docker_networks_default: []

    # Type: list
    openobserve_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    openobserve_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    openobserve_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    openobserve_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    openobserve_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    openobserve_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    openobserve_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    openobserve_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    openobserve_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    openobserve_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    openobserve_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    openobserve_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    openobserve_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    openobserve_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    openobserve_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    openobserve_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    openobserve_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    openobserve_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    openobserve_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    openobserve_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        openobserve_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "openobserve2.{{ user.domain }}"
          - "openobserve.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        openobserve_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'openobserve2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
hide:
  - tags
tags:
  - mealie
  - recipes
  - cooking
---

# Mealie

## What is it?

[Mealie](https://mealie.io/) is aan intuitive and easy to use recipe management app. It's designed to make your life easier by being the best recipes management experience on the web and providing you with an easy to use interface to manage your growing collection of recipes.

!!! info
    By default, the role is **NOT** protected behind your Authelia/SSO middleware. You have to log into the role itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://mealie.io/){: .header-icons } | [:octicons-link-16: Docs](https://docs.mealie.io/documentation/getting-started/introduction/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/mealie-recipes/mealie/){: .header-icons } | [:material-docker: Docker](https://ghcr.io/mealie-recipes/mealie){: .header-icons }|

Recommended install types: Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-mealie

```

### 2. URL

- To access Mealie, visit `https://mealie._yourdomain.tld_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        mealie_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `mealie_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `mealie_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    mealie_name: mealie

    ```

??? example "Paths"

    ```yaml
    # Type: string
    mealie_role_paths_folder: "{{ mealie_name }}"

    # Type: string
    mealie_role_paths_location: "{{ server_appdata_path }}/{{ mealie_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    mealie_role_web_subdomain: "{{ mealie_name }}"

    # Type: string
    mealie_role_web_domain: "{{ user.domain }}"

    # Type: string
    mealie_role_web_port: "9000"

    # Type: string
    mealie_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='mealie') + '.' + lookup('role_var', '_web_domain', role='mealie')
                          if (lookup('role_var', '_web_subdomain', role='mealie') | length > 0)
                          else lookup('role_var', '_web_domain', role='mealie')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    mealie_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='mealie') }}"

    # Type: string
    mealie_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='mealie') }}"

    # Type: bool (true/false)
    mealie_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    mealie_role_traefik_sso_middleware: ""

    # Type: string
    mealie_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    mealie_role_traefik_middleware_custom: ""

    # Type: string
    mealie_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    mealie_role_traefik_enabled: true

    # Type: bool (true/false)
    mealie_role_traefik_api_enabled: false

    # Type: string
    mealie_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    mealie_role_docker_container: "{{ mealie_name }}"

    # Image
    # Type: bool (true/false)
    mealie_role_docker_image_pull: true

    # Type: string
    mealie_role_docker_image_tag: "latest"

    # Type: string
    mealie_role_docker_image_repo: "ghcr.io/mealie-recipes/mealie"

    # Type: string
    mealie_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='mealie') }}:{{ lookup('role_var', '_docker_image_tag', role='mealie') }}"

    # Envs
    # Type: dict
    mealie_role_docker_envs_default: 
      ALLOW_SIGNUP: "false"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"
      BASE_URL: "{{ lookup('role_var', '_web_url', role='mealie') }}"

    # Type: dict
    mealie_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    mealie_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='mealie') }}:/app/data"

    # Type: list
    mealie_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    mealie_role_docker_hostname: "{{ mealie_name }}"

    # Networks
    # Type: string
    mealie_role_docker_networks_alias: "{{ mealie_name }}"

    # Type: list
    mealie_role_docker_networks_default: []

    # Type: list
    mealie_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    mealie_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    mealie_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    mealie_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    mealie_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    mealie_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    mealie_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    mealie_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    mealie_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    mealie_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    mealie_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    mealie_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    mealie_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    mealie_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    mealie_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    mealie_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    mealie_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    mealie_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    mealie_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    mealie_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        mealie_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "mealie2.{{ user.domain }}"
          - "mealie.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        mealie_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'mealie2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

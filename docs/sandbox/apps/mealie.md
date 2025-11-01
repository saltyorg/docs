---
hide:
  - tags
tags:
  - mealie
  - recipes
  - cooking
---

# Mealie

## Overview

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

- To access Mealie, visit <https://mealie.iYOUR_DOMAIN_NAMEi>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    mealie_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `mealie_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `mealie_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`mealie_name`"

        ```yaml
        # Type: string
        mealie_name: mealie
        ```

=== "Paths"

    ??? variable string "`mealie_role_paths_folder`"

        ```yaml
        # Type: string
        mealie_role_paths_folder: "{{ mealie_name }}"
        ```

    ??? variable string "`mealie_role_paths_location`"

        ```yaml
        # Type: string
        mealie_role_paths_location: "{{ server_appdata_path }}/{{ mealie_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`mealie_role_web_subdomain`"

        ```yaml
        # Type: string
        mealie_role_web_subdomain: "{{ mealie_name }}"
        ```

    ??? variable string "`mealie_role_web_domain`"

        ```yaml
        # Type: string
        mealie_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`mealie_role_web_port`"

        ```yaml
        # Type: string
        mealie_role_web_port: "9000"
        ```

    ??? variable string "`mealie_role_web_url`"

        ```yaml
        # Type: string
        mealie_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='mealie') + '.' + lookup('role_var', '_web_domain', role='mealie')
                              if (lookup('role_var', '_web_subdomain', role='mealie') | length > 0)
                              else lookup('role_var', '_web_domain', role='mealie')) }}"
        ```

=== "DNS"

    ??? variable string "`mealie_role_dns_record`"

        ```yaml
        # Type: string
        mealie_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='mealie') }}"
        ```

    ??? variable string "`mealie_role_dns_zone`"

        ```yaml
        # Type: string
        mealie_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='mealie') }}"
        ```

    ??? variable bool "`mealie_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        mealie_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`mealie_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        mealie_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`mealie_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        mealie_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`mealie_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        mealie_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`mealie_role_traefik_certresolver`"

        ```yaml
        # Type: string
        mealie_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`mealie_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        mealie_role_traefik_enabled: true
        ```

    ??? variable bool "`mealie_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        mealie_role_traefik_api_enabled: false
        ```

    ??? variable string "`mealie_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        mealie_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`mealie_role_docker_container`"

        ```yaml
        # Type: string
        mealie_role_docker_container: "{{ mealie_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`mealie_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        mealie_role_docker_image_pull: true
        ```

    ??? variable string "`mealie_role_docker_image_tag`"

        ```yaml
        # Type: string
        mealie_role_docker_image_tag: "latest"
        ```

    ??? variable string "`mealie_role_docker_image_repo`"

        ```yaml
        # Type: string
        mealie_role_docker_image_repo: "ghcr.io/mealie-recipes/mealie"
        ```

    ??? variable string "`mealie_role_docker_image`"

        ```yaml
        # Type: string
        mealie_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='mealie') }}:{{ lookup('role_var', '_docker_image_tag', role='mealie') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`mealie_role_docker_envs_default`"

        ```yaml
        # Type: dict
        mealie_role_docker_envs_default: 
          ALLOW_SIGNUP: "false"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          BASE_URL: "{{ lookup('role_var', '_web_url', role='mealie') }}"
        ```

    ??? variable dict "`mealie_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        mealie_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`mealie_role_docker_volumes_default`"

        ```yaml
        # Type: list
        mealie_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='mealie') }}:/app/data"
        ```

    ??? variable list "`mealie_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        mealie_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`mealie_role_docker_hostname`"

        ```yaml
        # Type: string
        mealie_role_docker_hostname: "{{ mealie_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`mealie_role_docker_networks_alias`"

        ```yaml
        # Type: string
        mealie_role_docker_networks_alias: "{{ mealie_name }}"
        ```

    ??? variable list "`mealie_role_docker_networks_default`"

        ```yaml
        # Type: list
        mealie_role_docker_networks_default: []
        ```

    ??? variable list "`mealie_role_docker_networks_custom`"

        ```yaml
        # Type: list
        mealie_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`mealie_role_docker_restart_policy`"

        ```yaml
        # Type: string
        mealie_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`mealie_role_docker_state`"

        ```yaml
        # Type: string
        mealie_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`mealie_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        mealie_role_autoheal_enabled: true
        ```

    ??? variable string "`mealie_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        mealie_role_depends_on: ""
        ```

    ??? variable string "`mealie_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        mealie_role_depends_on_delay: "0"
        ```

    ??? variable string "`mealie_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        mealie_role_depends_on_healthchecks:
        ```

    ??? variable bool "`mealie_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        mealie_role_diun_enabled: true
        ```

    ??? variable bool "`mealie_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        mealie_role_dns_enabled: true
        ```

    ??? variable bool "`mealie_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        mealie_role_docker_controller: true
        ```

    ??? variable bool "`mealie_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        mealie_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`mealie_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        mealie_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`mealie_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        mealie_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`mealie_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        mealie_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`mealie_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        mealie_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`mealie_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        mealie_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`mealie_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        mealie_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`mealie_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        mealie_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`mealie_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        mealie_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`mealie_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        mealie_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            mealie_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "mealie2.{{ user.domain }}"
              - "mealie.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`mealie_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        mealie_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            mealie_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'mealie2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`mealie_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        mealie_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
hide:
  - tags
tags:
  - vaultwarden
  - passwords
  - security
---

# vaultwarden

## Overview

[vaultwarden](https://github.com/dani-garcia/vaultwarden) is an alternative implementation of the Bitwarden server API written in Rust and compatible with upstream Bitwarden clients*, perfect for self-hosted deployment where running the official resource-heavy service might not be ideal.

!!! note
      📢 This project was known as Bitwarden_RS and has been renamed to separate itself from the official Bitwarden server in the hopes of avoiding confusion and trademark/branding issues.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/dani-garcia/vaultwarden){: .header-icons } | [:octicons-link-16: Docs](https://github.com/dani-garcia/vaultwarden/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/dani-garcia/vaultwarden){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/vaultwarden/server){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-vaultwarden

```

### 2. URL

- To access vaultwarden, visit <https://vaultwarden.iYOUR_DOMAIN_NAMEi>

### 3. Setup

  1. Visit the vaultwarden site at <https://vaultwarden.iYOUR_DOMAIN_NAMEi>

  2. Sign up with any email address and password.

  3. To access the Admin Panel go to <https://vaultwarden.iYOUR_DOMAIN_NAMEi/admin>

  4. You will need to enter an authentication key which you can find in `/opt/vaultwarden/env`. Look for `ADMIN_TOKEN=`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    vaultwarden_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `vaultwarden_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `vaultwarden_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`vaultwarden_name`"

        ```yaml
        # Type: string
        vaultwarden_name: vaultwarden
        ```

=== "Paths"

    ??? variable string "`vaultwarden_role_paths_folder`"

        ```yaml
        # Type: string
        vaultwarden_role_paths_folder: "{{ vaultwarden_name }}"
        ```

    ??? variable string "`vaultwarden_role_paths_location`"

        ```yaml
        # Type: string
        vaultwarden_role_paths_location: "{{ server_appdata_path }}/{{ vaultwarden_role_paths_folder }}"
        ```

    ??? variable string "`vaultwarden_role_paths_config_location`"

        ```yaml
        # Type: string
        vaultwarden_role_paths_config_location: "{{ vaultwarden_role_paths_location }}/env"
        ```

=== "Web"

    ??? variable string "`vaultwarden_role_web_subdomain`"

        ```yaml
        # Type: string
        vaultwarden_role_web_subdomain: "{{ vaultwarden_name }}"
        ```

    ??? variable string "`vaultwarden_role_web_domain`"

        ```yaml
        # Type: string
        vaultwarden_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`vaultwarden_role_web_port`"

        ```yaml
        # Type: string
        vaultwarden_role_web_port: "6423"
        ```

    ??? variable string "`vaultwarden_role_web_url`"

        ```yaml
        # Type: string
        vaultwarden_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='vaultwarden') + '.' + lookup('role_var', '_web_domain', role='vaultwarden')
                                   if (lookup('role_var', '_web_subdomain', role='vaultwarden') | length > 0)
                                   else lookup('role_var', '_web_domain', role='vaultwarden')) }}"
        ```

=== "DNS"

    ??? variable string "`vaultwarden_role_dns_record`"

        ```yaml
        # Type: string
        vaultwarden_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='vaultwarden') }}"
        ```

    ??? variable string "`vaultwarden_role_dns_zone`"

        ```yaml
        # Type: string
        vaultwarden_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='vaultwarden') }}"
        ```

    ??? variable bool "`vaultwarden_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`vaultwarden_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        vaultwarden_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`vaultwarden_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        vaultwarden_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`vaultwarden_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        vaultwarden_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`vaultwarden_role_traefik_certresolver`"

        ```yaml
        # Type: string
        vaultwarden_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`vaultwarden_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_traefik_enabled: true
        ```

    ??? variable bool "`vaultwarden_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_traefik_api_enabled: false
        ```

    ??? variable string "`vaultwarden_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        vaultwarden_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`vaultwarden_role_docker_container`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_container: "{{ vaultwarden_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`vaultwarden_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_docker_image_pull: true
        ```

    ??? variable string "`vaultwarden_role_docker_image_repo`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_image_repo: "vaultwarden/server"
        ```

    ??? variable string "`vaultwarden_role_docker_image_tag`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_image_tag: "latest"
        ```

    ??? variable string "`vaultwarden_role_docker_image`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='vaultwarden') }}:{{ lookup('role_var', '_docker_image_tag', role='vaultwarden') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`vaultwarden_role_docker_envs_default`"

        ```yaml
        # Type: dict
        vaultwarden_role_docker_envs_default: 
          TZ: "{{ tz }}"
          ROCKET_PORT: "{{ lookup('role_var', '_web_port', role='vaultwarden') }}"
        ```

    ??? variable dict "`vaultwarden_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        vaultwarden_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`vaultwarden_role_docker_volumes_default`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='vaultwarden') }}:/data"
          - "{{ lookup('role_var', '_paths_location', role='vaultwarden') }}/env:/.env"
        ```

    ??? variable list "`vaultwarden_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`vaultwarden_role_docker_hostname`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_hostname: "{{ vaultwarden_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`vaultwarden_role_docker_networks_alias`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_networks_alias: "{{ vaultwarden_name }}"
        ```

    ??? variable list "`vaultwarden_role_docker_networks_default`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_networks_default: []
        ```

    ??? variable list "`vaultwarden_role_docker_networks_custom`"

        ```yaml
        # Type: list
        vaultwarden_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`vaultwarden_role_docker_restart_policy`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`vaultwarden_role_docker_state`"

        ```yaml
        # Type: string
        vaultwarden_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`vaultwarden_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        vaultwarden_role_autoheal_enabled: true
        ```

    ??? variable string "`vaultwarden_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        vaultwarden_role_depends_on: ""
        ```

    ??? variable string "`vaultwarden_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        vaultwarden_role_depends_on_delay: "0"
        ```

    ??? variable string "`vaultwarden_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        vaultwarden_role_depends_on_healthchecks:
        ```

    ??? variable bool "`vaultwarden_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        vaultwarden_role_diun_enabled: true
        ```

    ??? variable bool "`vaultwarden_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        vaultwarden_role_dns_enabled: true
        ```

    ??? variable bool "`vaultwarden_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        vaultwarden_role_docker_controller: true
        ```

    ??? variable bool "`vaultwarden_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        vaultwarden_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`vaultwarden_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        vaultwarden_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`vaultwarden_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        vaultwarden_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`vaultwarden_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        vaultwarden_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`vaultwarden_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`vaultwarden_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        vaultwarden_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`vaultwarden_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        vaultwarden_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`vaultwarden_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        vaultwarden_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`vaultwarden_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        vaultwarden_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`vaultwarden_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        vaultwarden_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            vaultwarden_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "vaultwarden2.{{ user.domain }}"
              - "vaultwarden.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`vaultwarden_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        vaultwarden_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            vaultwarden_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'vaultwarden2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`vaultwarden_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        vaultwarden_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
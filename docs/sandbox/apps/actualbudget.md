---
icon: material/docker
hide:
  - tags
tags:
  - actualbudget
  - budget
  - finance
---

# Actual Budget

## Overview

[Actual Budget](https://actualbudget.org/) is a super fast, privacy-focused app for managing your finances. Its heart is the well-proven and much-loved Envelope Budgeting methodology.
You own your data and can do whatever you want with it. Featuring multi-device sync, optional end-to-end encryption and so much more.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://actualbudget.org){: .header-icons } | [:octicons-link-16: Docs](https://actualbudget.org/docs){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/actualbudget/actual){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/actualbudget/actual-server){: .header-icons }|

## 1. Installation

``sb install sandbox-actualbudget``

## 2. URL

To access Actual Budget, visit <https://actualbudget.iYOUR_DOMAIN_NAMEi>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    actualbudget_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `actualbudget_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `actualbudget_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`actualbudget_name`"

        ```yaml
        # Type: string
        actualbudget_name: actualbudget
        ```

=== "Paths"

    ??? variable string "`actualbudget_role_paths_folder`"

        ```yaml
        # Type: string
        actualbudget_role_paths_folder: "{{ actualbudget_name }}"
        ```

    ??? variable string "`actualbudget_role_paths_location`"

        ```yaml
        # Type: string
        actualbudget_role_paths_location: "{{ server_appdata_path }}/{{ actualbudget_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`actualbudget_role_web_subdomain`"

        ```yaml
        # Type: string
        actualbudget_role_web_subdomain: "{{ actualbudget_name }}"
        ```

    ??? variable string "`actualbudget_role_web_domain`"

        ```yaml
        # Type: string
        actualbudget_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`actualbudget_role_web_port`"

        ```yaml
        # Type: string
        actualbudget_role_web_port: "5006"
        ```

    ??? variable string "`actualbudget_role_web_url`"

        ```yaml
        # Type: string
        actualbudget_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='actualbudget') + '.' + lookup('role_var', '_web_domain', role='actualbudget')
                                    if (lookup('role_var', '_web_subdomain', role='actualbudget') | length > 0)
                                    else lookup('role_var', '_web_domain', role='actualbudget')) }}"
        ```

=== "DNS"

    ??? variable string "`actualbudget_role_dns_record`"

        ```yaml
        # Type: string
        actualbudget_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='actualbudget') }}"
        ```

    ??? variable string "`actualbudget_role_dns_zone`"

        ```yaml
        # Type: string
        actualbudget_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='actualbudget') }}"
        ```

    ??? variable bool "`actualbudget_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        actualbudget_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`actualbudget_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        actualbudget_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`actualbudget_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        actualbudget_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`actualbudget_role_traefik_certresolver`"

        ```yaml
        # Type: string
        actualbudget_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable string "`actualbudget_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        actualbudget_role_traefik_middleware_custom: ""
        ```

    ??? variable bool "`actualbudget_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        actualbudget_role_traefik_enabled: true
        ```

    ??? variable bool "`actualbudget_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        actualbudget_role_traefik_api_enabled: false
        ```

    ??? variable string "`actualbudget_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        actualbudget_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`actualbudget_role_docker_container`"

        ```yaml
        # Type: string
        actualbudget_role_docker_container: "{{ actualbudget_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`actualbudget_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        actualbudget_role_docker_image_pull: true
        ```

    ??? variable string "`actualbudget_role_docker_image_repo`"

        ```yaml
        # Type: string
        actualbudget_role_docker_image_repo: "actualbudget/actual-server"
        ```

    ??? variable string "`actualbudget_role_docker_image_tag`"

        ```yaml
        # Type: string
        actualbudget_role_docker_image_tag: "latest"
        ```

    ??? variable string "`actualbudget_role_docker_image`"

        ```yaml
        # Type: string
        actualbudget_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='actualbudget') }}:{{ lookup('role_var', '_docker_image_tag', role='actualbudget') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`actualbudget_role_docker_envs_default`"

        ```yaml
        # Type: dict
        actualbudget_role_docker_envs_default: 
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`actualbudget_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        actualbudget_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`actualbudget_role_docker_volumes_default`"

        ```yaml
        # Type: list
        actualbudget_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='actualbudget') }}:/data"
          - "/etc/localtime:/etc/localtime:ro"
        ```

    ??? variable list "`actualbudget_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        actualbudget_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`actualbudget_role_docker_hostname`"

        ```yaml
        # Type: string
        actualbudget_role_docker_hostname: "{{ actualbudget_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`actualbudget_role_docker_networks_alias`"

        ```yaml
        # Type: string
        actualbudget_role_docker_networks_alias: "{{ actualbudget_name }}"
        ```

    ??? variable list "`actualbudget_role_docker_networks_default`"

        ```yaml
        # Type: list
        actualbudget_role_docker_networks_default: []
        ```

    ??? variable list "`actualbudget_role_docker_networks_custom`"

        ```yaml
        # Type: list
        actualbudget_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`actualbudget_role_docker_restart_policy`"

        ```yaml
        # Type: string
        actualbudget_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`actualbudget_role_docker_state`"

        ```yaml
        # Type: string
        actualbudget_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`actualbudget_role_docker_user`"

        ```yaml
        # Type: string
        actualbudget_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`actualbudget_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        actualbudget_role_autoheal_enabled: true
        ```

    ??? variable string "`actualbudget_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        actualbudget_role_depends_on: ""
        ```

    ??? variable string "`actualbudget_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        actualbudget_role_depends_on_delay: "0"
        ```

    ??? variable string "`actualbudget_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        actualbudget_role_depends_on_healthchecks:
        ```

    ??? variable bool "`actualbudget_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        actualbudget_role_diun_enabled: true
        ```

    ??? variable bool "`actualbudget_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        actualbudget_role_dns_enabled: true
        ```

    ??? variable bool "`actualbudget_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        actualbudget_role_docker_controller: true
        ```

    ??? variable bool "`actualbudget_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        actualbudget_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`actualbudget_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        actualbudget_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`actualbudget_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        actualbudget_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`actualbudget_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        actualbudget_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`actualbudget_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        actualbudget_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`actualbudget_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        actualbudget_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`actualbudget_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        actualbudget_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`actualbudget_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        actualbudget_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`actualbudget_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        actualbudget_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`actualbudget_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        actualbudget_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            actualbudget_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "actualbudget2.{{ user.domain }}"
              - "actualbudget.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`actualbudget_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        actualbudget_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            actualbudget_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'actualbudget2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`actualbudget_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        actualbudget_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
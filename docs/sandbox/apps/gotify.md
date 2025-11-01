---
hide:
  - tags
tags:
  - gotify
  - notifications
  - messaging
---

# Gotify

## Overview

[Gotify](https://gotify.net/) a simple server for sending and receiving messages.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://gotify.net/){: .header-icons } | [:octicons-link-16: Docs](https://gotify.github.io/api-docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/gotify/server){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/gotify/server){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-gotify

```

### 2. URL

- To access Gotify, visit <https://gotify.iYOUR_DOMAIN_NAMEi>

### 3. Setup

- The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

!!! info
    Android App <br />
    <https://github.com/gotify/android>
    <https://f-droid.org/de/packages/com.github.gotify/>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    gotify_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `gotify_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `gotify_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`gotify_name`"

        ```yaml
        # Type: string
        gotify_name: gotify
        ```

=== "Paths"

    ??? variable string "`gotify_role_paths_folder`"

        ```yaml
        # Type: string
        gotify_role_paths_folder: "{{ gotify_name }}"
        ```

    ??? variable string "`gotify_role_paths_location`"

        ```yaml
        # Type: string
        gotify_role_paths_location: "{{ server_appdata_path }}/{{ gotify_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`gotify_role_web_subdomain`"

        ```yaml
        # Type: string
        gotify_role_web_subdomain: "{{ gotify_name }}"
        ```

    ??? variable string "`gotify_role_web_domain`"

        ```yaml
        # Type: string
        gotify_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`gotify_role_web_port`"

        ```yaml
        # Type: string
        gotify_role_web_port: "80"
        ```

    ??? variable string "`gotify_role_web_url`"

        ```yaml
        # Type: string
        gotify_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='gotify') + '.' + lookup('role_var', '_web_domain', role='gotify')
                              if (lookup('role_var', '_web_subdomain', role='gotify') | length > 0)
                              else lookup('role_var', '_web_domain', role='gotify')) }}"
        ```

=== "DNS"

    ??? variable string "`gotify_role_dns_record`"

        ```yaml
        # Type: string
        gotify_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='gotify') }}"
        ```

    ??? variable string "`gotify_role_dns_zone`"

        ```yaml
        # Type: string
        gotify_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='gotify') }}"
        ```

    ??? variable bool "`gotify_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        gotify_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`gotify_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        gotify_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`gotify_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        gotify_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`gotify_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        gotify_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`gotify_role_traefik_certresolver`"

        ```yaml
        # Type: string
        gotify_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`gotify_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        gotify_role_traefik_enabled: true
        ```

    ??? variable bool "`gotify_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        gotify_role_traefik_api_enabled: false
        ```

    ??? variable string "`gotify_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        gotify_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`gotify_role_docker_container`"

        ```yaml
        # Type: string
        gotify_role_docker_container: "{{ gotify_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`gotify_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        gotify_role_docker_image_pull: true
        ```

    ??? variable string "`gotify_role_docker_image_repo`"

        ```yaml
        # Type: string
        gotify_role_docker_image_repo: "gotify/server"
        ```

    ??? variable string "`gotify_role_docker_image_tag`"

        ```yaml
        # Type: string
        gotify_role_docker_image_tag: "latest"
        ```

    ??? variable string "`gotify_role_docker_image`"

        ```yaml
        # Type: string
        gotify_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='gotify') }}:{{ lookup('role_var', '_docker_image_tag', role='gotify') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`gotify_role_docker_envs_default`"

        ```yaml
        # Type: dict
        gotify_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          GOTIFY_DEFAULTUSER_NAME: "{{ user.name }}"
          GOTIFY_DEFAULTUSER_PASS: "{{ user.pass }}"
        ```

    ??? variable dict "`gotify_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        gotify_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`gotify_role_docker_volumes_default`"

        ```yaml
        # Type: list
        gotify_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='gotify') }}:/app/data"
        ```

    ??? variable list "`gotify_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        gotify_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`gotify_role_docker_hostname`"

        ```yaml
        # Type: string
        gotify_role_docker_hostname: "{{ gotify_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`gotify_role_docker_networks_alias`"

        ```yaml
        # Type: string
        gotify_role_docker_networks_alias: "{{ gotify_name }}"
        ```

    ??? variable list "`gotify_role_docker_networks_default`"

        ```yaml
        # Type: list
        gotify_role_docker_networks_default: []
        ```

    ??? variable list "`gotify_role_docker_networks_custom`"

        ```yaml
        # Type: list
        gotify_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`gotify_role_docker_restart_policy`"

        ```yaml
        # Type: string
        gotify_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`gotify_role_docker_state`"

        ```yaml
        # Type: string
        gotify_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`gotify_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        gotify_role_autoheal_enabled: true
        ```

    ??? variable string "`gotify_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        gotify_role_depends_on: ""
        ```

    ??? variable string "`gotify_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        gotify_role_depends_on_delay: "0"
        ```

    ??? variable string "`gotify_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        gotify_role_depends_on_healthchecks:
        ```

    ??? variable bool "`gotify_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        gotify_role_diun_enabled: true
        ```

    ??? variable bool "`gotify_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        gotify_role_dns_enabled: true
        ```

    ??? variable bool "`gotify_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        gotify_role_docker_controller: true
        ```

    ??? variable bool "`gotify_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        gotify_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`gotify_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        gotify_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`gotify_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        gotify_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`gotify_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        gotify_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`gotify_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        gotify_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`gotify_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        gotify_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`gotify_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        gotify_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`gotify_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        gotify_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`gotify_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        gotify_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`gotify_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        gotify_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            gotify_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "gotify2.{{ user.domain }}"
              - "gotify.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`gotify_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        gotify_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            gotify_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'gotify2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`gotify_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        gotify_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
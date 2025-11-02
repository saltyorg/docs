---
icon: material/docker
hide:
  - tags
tags:
  - linkding
  - productivity
  - bookmarks
---

# Linkding

## Overview

[Linkding](https://github.com/sissbruecker/linkding#introduction) is a simple bookmark service that you can host yourself. It's designed be to be minimal and fast.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/sissbruecker/linkding#introduction){: .header-icons } | [:octicons-link-16: Docs](https://github.com/sissbruecker/linkding#documentation){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/sissbruecker/linkding){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/sissbruecker/linkding){: .header-icons } |

### 1. Installation

``` shell

sb install sandbox-linkding

```

### 2. URL

- To access linkding, visit <https://linkding.iYOUR_DOMAIN_NAMEi>

### 3. Setup

- Default login:

  ``` { .yaml}
  Username: user from accounts.yml
  Password: password from accounts.yml
  ```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    linkding_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `linkding_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `linkding_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`linkding_name`"

        ```yaml
        # Type: string
        linkding_name: linkding
        ```

=== "Paths"

    ??? variable string "`linkding_role_paths_folder`"

        ```yaml
        # Type: string
        linkding_role_paths_folder: "{{ linkding_name }}"
        ```

    ??? variable string "`linkding_role_paths_location`"

        ```yaml
        # Type: string
        linkding_role_paths_location: "{{ server_appdata_path }}/{{ linkding_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`linkding_role_web_subdomain`"

        ```yaml
        # Type: string
        linkding_role_web_subdomain: "{{ linkding_name }}"
        ```

    ??? variable string "`linkding_role_web_domain`"

        ```yaml
        # Type: string
        linkding_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`linkding_role_web_port`"

        ```yaml
        # Type: string
        linkding_role_web_port: "9090"
        ```

    ??? variable string "`linkding_role_web_url`"

        ```yaml
        # Type: string
        linkding_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='linkding') + '.' + lookup('role_var', '_web_domain', role='linkding')
                                if (lookup('role_var', '_web_subdomain', role='linkding') | length > 0)
                                else lookup('role_var', '_web_domain', role='linkding')) }}"
        ```

=== "DNS"

    ??? variable string "`linkding_role_dns_record`"

        ```yaml
        # Type: string
        linkding_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='linkding') }}"
        ```

    ??? variable string "`linkding_role_dns_zone`"

        ```yaml
        # Type: string
        linkding_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='linkding') }}"
        ```

    ??? variable bool "`linkding_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        linkding_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`linkding_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        linkding_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`linkding_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        linkding_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`linkding_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        linkding_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`linkding_role_traefik_certresolver`"

        ```yaml
        # Type: string
        linkding_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`linkding_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        linkding_role_traefik_enabled: true
        ```

    ??? variable bool "`linkding_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        linkding_role_traefik_api_enabled: true
        ```

    ??? variable string "`linkding_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        linkding_role_traefik_api_endpoint: "PathPrefix(`/api`)"
        ```

    ??? variable string "`linkding_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        linkding_role_traefik_api_middleware_http: "{{ 'dropsecurityheaders@file,' + traefik_default_middleware_http_api }}"
        ```

    ??? variable string "`linkding_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        linkding_role_traefik_api_middleware: "{{ 'dropsecurityheaders@file,' + traefik_default_middleware_api }}"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`linkding_role_docker_container`"

        ```yaml
        # Type: string
        linkding_role_docker_container: "{{ linkding_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`linkding_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        linkding_role_docker_image_pull: true
        ```

    ??? variable string "`linkding_role_docker_image_tag`"

        ```yaml
        # Type: string
        linkding_role_docker_image_tag: "latest"
        ```

    ??? variable string "`linkding_role_docker_image_repo`"

        ```yaml
        # Type: string
        linkding_role_docker_image_repo: "sissbruecker/linkding"
        ```

    ??? variable string "`linkding_role_docker_image`"

        ```yaml
        # Type: string
        linkding_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='linkding') }}:{{ lookup('role_var', '_docker_image_tag', role='linkding') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`linkding_role_docker_envs_default`"

        ```yaml
        # Type: dict
        linkding_role_docker_envs_default: 
          TZ: "{{ tz }}"
          LD_CONTAINER_NAME: "{{ linkding_name }}"
          LD_HOST_PORT: "9090"
          LD_HOST_DATA_DIR: "./data"
          LD_SUPERUSER_NAME: "{{ user.name }}"
          LD_SUPERUSER_PASSWORD: "{{ user.pass }}"
          LD_DISABLE_BACKGROUND_TASKS: "false"
          LD_DISABLE_URL_VALIDATION: "false"
          LD_ENABLE_AUTH_PROXY: "false"
          LD_CSRF_TRUSTED_ORIGINS: "{{ lookup('role_var', '_web_url', role='linkding') }}"
        ```

    ??? variable dict "`linkding_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        linkding_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`linkding_role_docker_volumes_default`"

        ```yaml
        # Type: list
        linkding_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='linkding') }}:/etc/linkding/data"
        ```

    ??? variable list "`linkding_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        linkding_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`linkding_role_docker_hostname`"

        ```yaml
        # Type: string
        linkding_role_docker_hostname: "{{ linkding_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`linkding_role_docker_networks_alias`"

        ```yaml
        # Type: string
        linkding_role_docker_networks_alias: "{{ linkding_name }}"
        ```

    ??? variable list "`linkding_role_docker_networks_default`"

        ```yaml
        # Type: list
        linkding_role_docker_networks_default: []
        ```

    ??? variable list "`linkding_role_docker_networks_custom`"

        ```yaml
        # Type: list
        linkding_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`linkding_role_docker_restart_policy`"

        ```yaml
        # Type: string
        linkding_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`linkding_role_docker_state`"

        ```yaml
        # Type: string
        linkding_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`linkding_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        linkding_role_autoheal_enabled: true
        ```

    ??? variable string "`linkding_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        linkding_role_depends_on: ""
        ```

    ??? variable string "`linkding_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        linkding_role_depends_on_delay: "0"
        ```

    ??? variable string "`linkding_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        linkding_role_depends_on_healthchecks:
        ```

    ??? variable bool "`linkding_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        linkding_role_diun_enabled: true
        ```

    ??? variable bool "`linkding_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        linkding_role_dns_enabled: true
        ```

    ??? variable bool "`linkding_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        linkding_role_docker_controller: true
        ```

    ??? variable bool "`linkding_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        linkding_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`linkding_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        linkding_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`linkding_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        linkding_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`linkding_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        linkding_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`linkding_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        linkding_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`linkding_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        linkding_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`linkding_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        linkding_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`linkding_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        linkding_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`linkding_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        linkding_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`linkding_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        linkding_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            linkding_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "linkding2.{{ user.domain }}"
              - "linkding.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`linkding_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        linkding_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            linkding_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'linkding2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`linkding_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        linkding_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

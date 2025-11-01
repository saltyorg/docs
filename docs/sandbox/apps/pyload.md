---
hide:
  - tags
tags:
  - pyload
  - download
  - tools
---

# pyload

## Overview

## THIS DOCUMENTATION IS NOT YET COMPLETED

[pyload](https://pyload.net/) is a...

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://pyload.url){: .header-icons } | [:octicons-link-16: Docs](https://pyload.docs.url){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/pyload/pyload){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/pyload/pyload){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-pyload

```

### 2. URL

- To access pyload, visit <https://pyload.iYOUR_DOMAIN_NAMEi>
- Default credentials are - username: pyload - password: pyload

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    pyload_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `pyload_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `pyload_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`pyload_name`"

        ```yaml
        # Type: string
        pyload_name: pyload
        ```

=== "Paths"

    ??? variable string "`pyload_role_paths_folder`"

        ```yaml
        # Type: string
        pyload_role_paths_folder: "{{ pyload_name }}"
        ```

    ??? variable string "`pyload_role_paths_location`"

        ```yaml
        # Type: string
        pyload_role_paths_location: "{{ server_appdata_path }}/{{ pyload_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`pyload_role_web_subdomain`"

        ```yaml
        # Type: string
        pyload_role_web_subdomain: "{{ pyload_name }}"
        ```

    ??? variable string "`pyload_role_web_domain`"

        ```yaml
        # Type: string
        pyload_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`pyload_role_web_port`"

        ```yaml
        # Type: string
        pyload_role_web_port: "8000"
        ```

    ??? variable string "`pyload_role_web_url`"

        ```yaml
        # Type: string
        pyload_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='pyload') + '.' + lookup('role_var', '_web_domain', role='pyload')
                              if (lookup('role_var', '_web_subdomain', role='pyload') | length > 0)
                              else lookup('role_var', '_web_domain', role='pyload')) }}"
        ```

=== "DNS"

    ??? variable string "`pyload_role_dns_record`"

        ```yaml
        # Type: string
        pyload_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='pyload') }}"
        ```

    ??? variable string "`pyload_role_dns_zone`"

        ```yaml
        # Type: string
        pyload_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='pyload') }}"
        ```

    ??? variable bool "`pyload_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        pyload_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`pyload_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        pyload_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`pyload_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        pyload_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`pyload_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        pyload_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`pyload_role_traefik_certresolver`"

        ```yaml
        # Type: string
        pyload_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`pyload_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        pyload_role_traefik_enabled: true
        ```

    ??? variable bool "`pyload_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        pyload_role_traefik_api_enabled: false
        ```

    ??? variable string "`pyload_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        pyload_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`pyload_role_docker_container`"

        ```yaml
        # Type: string
        pyload_role_docker_container: "{{ pyload_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`pyload_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        pyload_role_docker_image_pull: true
        ```

    ??? variable string "`pyload_role_docker_image_repo`"

        ```yaml
        # Type: string
        pyload_role_docker_image_repo: "lscr.io/linuxserver/pyload-ng"
        ```

    ??? variable string "`pyload_role_docker_image_tag`"

        ```yaml
        # Type: string
        pyload_role_docker_image_tag: "latest"
        ```

    ??? variable string "`pyload_role_docker_image`"

        ```yaml
        # Type: string
        pyload_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='pyload') }}:{{ lookup('role_var', '_docker_image_tag', role='pyload') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`pyload_role_docker_envs_default`"

        ```yaml
        # Type: dict
        pyload_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`pyload_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        pyload_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`pyload_role_docker_volumes_default`"

        ```yaml
        # Type: list
        pyload_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='pyload') }}:/config"
        ```

    ??? variable list "`pyload_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        pyload_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`pyload_role_docker_hostname`"

        ```yaml
        # Type: string
        pyload_role_docker_hostname: "{{ pyload_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`pyload_role_docker_networks_alias`"

        ```yaml
        # Type: string
        pyload_role_docker_networks_alias: "{{ pyload_name }}"
        ```

    ??? variable list "`pyload_role_docker_networks_default`"

        ```yaml
        # Type: list
        pyload_role_docker_networks_default: []
        ```

    ??? variable list "`pyload_role_docker_networks_custom`"

        ```yaml
        # Type: list
        pyload_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`pyload_role_docker_restart_policy`"

        ```yaml
        # Type: string
        pyload_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`pyload_role_docker_state`"

        ```yaml
        # Type: string
        pyload_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`pyload_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        pyload_role_autoheal_enabled: true
        ```

    ??? variable string "`pyload_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        pyload_role_depends_on: ""
        ```

    ??? variable string "`pyload_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        pyload_role_depends_on_delay: "0"
        ```

    ??? variable string "`pyload_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        pyload_role_depends_on_healthchecks:
        ```

    ??? variable bool "`pyload_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        pyload_role_diun_enabled: true
        ```

    ??? variable bool "`pyload_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        pyload_role_dns_enabled: true
        ```

    ??? variable bool "`pyload_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        pyload_role_docker_controller: true
        ```

    ??? variable bool "`pyload_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        pyload_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`pyload_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        pyload_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`pyload_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        pyload_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`pyload_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        pyload_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`pyload_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        pyload_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`pyload_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        pyload_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`pyload_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        pyload_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`pyload_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        pyload_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`pyload_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        pyload_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`pyload_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        pyload_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            pyload_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "pyload2.{{ user.domain }}"
              - "pyload.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`pyload_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        pyload_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            pyload_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'pyload2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`pyload_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        pyload_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
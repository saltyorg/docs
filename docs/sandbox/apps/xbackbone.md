---
hide:
  - tags
tags:
  - xbackbone
  - file-sharing
  - upload
---

# xbackbone

## THIS DOCUMENTATION IS NOT YET COMPLETED

[xbackbone](https://xbackbone.url) is a...

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://xbackbone.url){: .header-icons } | [:octicons-link-16: Docs](https://xbackbone.docs.url){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/xbackbone/xbackbone){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/xbackbone/xbackbone){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-xbackbone

```

### 2. URL

- To access xbackbone, visit <https://xbackbone.iYOUR_DOMAIN_NAMEi>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    xbackbone_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `xbackbone_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `xbackbone_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`xbackbone_name`"

        ```yaml
        # Type: string
        xbackbone_name: xbackbone
        ```

=== "Paths"

    ??? variable string "`xbackbone_role_paths_folder`"

        ```yaml
        # Type: string
        xbackbone_role_paths_folder: "{{ xbackbone_name }}"
        ```

    ??? variable string "`xbackbone_role_paths_location`"

        ```yaml
        # Type: string
        xbackbone_role_paths_location: "{{ server_appdata_path }}/{{ xbackbone_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`xbackbone_role_web_subdomain`"

        ```yaml
        # Type: string
        xbackbone_role_web_subdomain: "{{ xbackbone_name }}"
        ```

    ??? variable string "`xbackbone_role_web_domain`"

        ```yaml
        # Type: string
        xbackbone_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`xbackbone_role_web_port`"

        ```yaml
        # Type: string
        xbackbone_role_web_port: "80"
        ```

    ??? variable string "`xbackbone_role_web_url`"

        ```yaml
        # Type: string
        xbackbone_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='xbackbone') + '.' + lookup('role_var', '_web_domain', role='xbackbone')
                                 if (lookup('role_var', '_web_subdomain', role='xbackbone') | length > 0)
                                 else lookup('role_var', '_web_domain', role='xbackbone')) }}"
        ```

=== "DNS"

    ??? variable string "`xbackbone_role_dns_record`"

        ```yaml
        # Type: string
        xbackbone_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='xbackbone') }}"
        ```

    ??? variable string "`xbackbone_role_dns_zone`"

        ```yaml
        # Type: string
        xbackbone_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='xbackbone') }}"
        ```

    ??? variable bool "`xbackbone_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        xbackbone_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`xbackbone_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        xbackbone_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`xbackbone_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        xbackbone_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`xbackbone_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        xbackbone_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`xbackbone_role_traefik_certresolver`"

        ```yaml
        # Type: string
        xbackbone_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`xbackbone_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        xbackbone_role_traefik_enabled: true
        ```

    ??? variable bool "`xbackbone_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        xbackbone_role_traefik_api_enabled: false
        ```

    ??? variable string "`xbackbone_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        xbackbone_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`xbackbone_role_docker_container`"

        ```yaml
        # Type: string
        xbackbone_role_docker_container: "{{ xbackbone_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`xbackbone_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        xbackbone_role_docker_image_pull: true
        ```

    ??? variable string "`xbackbone_role_docker_image_repo`"

        ```yaml
        # Type: string
        xbackbone_role_docker_image_repo: "lscr.io/linuxserver/xbackbone"
        ```

    ??? variable string "`xbackbone_role_docker_image_tag`"

        ```yaml
        # Type: string
        xbackbone_role_docker_image_tag: "latest"
        ```

    ??? variable string "`xbackbone_role_docker_image`"

        ```yaml
        # Type: string
        xbackbone_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='xbackbone') }}:{{ lookup('role_var', '_docker_image_tag', role='xbackbone') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`xbackbone_role_docker_envs_default`"

        ```yaml
        # Type: dict
        xbackbone_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`xbackbone_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        xbackbone_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`xbackbone_role_docker_volumes_default`"

        ```yaml
        # Type: list
        xbackbone_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='xbackbone') }}:/config"
        ```

    ??? variable list "`xbackbone_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        xbackbone_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`xbackbone_role_docker_hostname`"

        ```yaml
        # Type: string
        xbackbone_role_docker_hostname: "{{ xbackbone_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`xbackbone_role_docker_networks_alias`"

        ```yaml
        # Type: string
        xbackbone_role_docker_networks_alias: "{{ xbackbone_name }}"
        ```

    ??? variable list "`xbackbone_role_docker_networks_default`"

        ```yaml
        # Type: list
        xbackbone_role_docker_networks_default: []
        ```

    ??? variable list "`xbackbone_role_docker_networks_custom`"

        ```yaml
        # Type: list
        xbackbone_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`xbackbone_role_docker_restart_policy`"

        ```yaml
        # Type: string
        xbackbone_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`xbackbone_role_docker_state`"

        ```yaml
        # Type: string
        xbackbone_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`xbackbone_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        xbackbone_role_autoheal_enabled: true
        ```

    ??? variable string "`xbackbone_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        xbackbone_role_depends_on: ""
        ```

    ??? variable string "`xbackbone_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        xbackbone_role_depends_on_delay: "0"
        ```

    ??? variable string "`xbackbone_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        xbackbone_role_depends_on_healthchecks:
        ```

    ??? variable bool "`xbackbone_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        xbackbone_role_diun_enabled: true
        ```

    ??? variable bool "`xbackbone_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        xbackbone_role_dns_enabled: true
        ```

    ??? variable bool "`xbackbone_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        xbackbone_role_docker_controller: true
        ```

    ??? variable bool "`xbackbone_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        xbackbone_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`xbackbone_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        xbackbone_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`xbackbone_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        xbackbone_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`xbackbone_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        xbackbone_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`xbackbone_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        xbackbone_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`xbackbone_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        xbackbone_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`xbackbone_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        xbackbone_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`xbackbone_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        xbackbone_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`xbackbone_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        xbackbone_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`xbackbone_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        xbackbone_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            xbackbone_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "xbackbone2.{{ user.domain }}"
              - "xbackbone.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`xbackbone_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        xbackbone_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            xbackbone_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'xbackbone2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`xbackbone_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        xbackbone_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
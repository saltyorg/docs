---
hide:
  - tags
tags:
  - heimdall
  - dashboard
  - homepage
---

# Heimdall

## What is it?

[Heimdall](https://heimdall.site/) is a way to organise all those links to your most used web sites and web applications in a simple way. Simplicity is the key to Heimdall. Why not use it as your browser start page? It even has the ability to include a search bar using either Google, Bing or DuckDuckGo.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://heimdall.site/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/linuxserver/Heimdall-Apps){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/linuxserver/Heimdall){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/heimdall){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-heimdall

```

### 2. URL

- To access Heimdall, visit `https://heimdall._yourdomain.com_`

### 3. Setup

- The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    heimdall_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `heimdall_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `heimdall_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`heimdall_name`"

        ```yaml
        # Type: string
        heimdall_name: heimdall
        ```

=== "Paths"

    ??? variable string "`heimdall_role_paths_folder`"

        ```yaml
        # Type: string
        heimdall_role_paths_folder: "{{ heimdall_name }}"
        ```

    ??? variable string "`heimdall_role_paths_location`"

        ```yaml
        # Type: string
        heimdall_role_paths_location: "{{ server_appdata_path }}/{{ heimdall_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`heimdall_role_web_subdomain`"

        ```yaml
        # Type: string
        heimdall_role_web_subdomain: "{{ heimdall_name }}"
        ```

    ??? variable string "`heimdall_role_web_domain`"

        ```yaml
        # Type: string
        heimdall_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`heimdall_role_web_port`"

        ```yaml
        # Type: string
        heimdall_role_web_port: "80"
        ```

    ??? variable string "`heimdall_role_web_url`"

        ```yaml
        # Type: string
        heimdall_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='heimdall') + '.' + lookup('role_var', '_web_domain', role='heimdall')
                                if (lookup('role_var', '_web_subdomain', role='heimdall') | length > 0)
                                else lookup('role_var', '_web_domain', role='heimdall')) }}"
        ```

=== "DNS"

    ??? variable string "`heimdall_role_dns_record`"

        ```yaml
        # Type: string
        heimdall_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='heimdall') }}"
        ```

    ??? variable string "`heimdall_role_dns_zone`"

        ```yaml
        # Type: string
        heimdall_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='heimdall') }}"
        ```

    ??? variable bool "`heimdall_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        heimdall_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`heimdall_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        heimdall_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`heimdall_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        heimdall_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`heimdall_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        heimdall_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`heimdall_role_traefik_certresolver`"

        ```yaml
        # Type: string
        heimdall_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`heimdall_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        heimdall_role_traefik_enabled: true
        ```

    ??? variable bool "`heimdall_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        heimdall_role_traefik_api_enabled: false
        ```

    ??? variable string "`heimdall_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        heimdall_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`heimdall_role_docker_container`"

        ```yaml
        # Type: string
        heimdall_role_docker_container: "{{ heimdall_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`heimdall_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        heimdall_role_docker_image_pull: true
        ```

    ??? variable string "`heimdall_role_docker_image_repo`"

        ```yaml
        # Type: string
        heimdall_role_docker_image_repo: "lscr.io/linuxserver/heimdall"
        ```

    ??? variable string "`heimdall_role_docker_image_tag`"

        ```yaml
        # Type: string
        heimdall_role_docker_image_tag: "latest"
        ```

    ??? variable string "`heimdall_role_docker_image`"

        ```yaml
        # Type: string
        heimdall_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='heimdall') }}:{{ lookup('role_var', '_docker_image_tag', role='heimdall') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`heimdall_role_docker_envs_default`"

        ```yaml
        # Type: dict
        heimdall_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`heimdall_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        heimdall_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`heimdall_role_docker_volumes_default`"

        ```yaml
        # Type: list
        heimdall_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='heimdall') }}:/config"
        ```

    ??? variable list "`heimdall_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        heimdall_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`heimdall_role_docker_hostname`"

        ```yaml
        # Type: string
        heimdall_role_docker_hostname: "{{ heimdall_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`heimdall_role_docker_networks_alias`"

        ```yaml
        # Type: string
        heimdall_role_docker_networks_alias: "{{ heimdall_name }}"
        ```

    ??? variable list "`heimdall_role_docker_networks_default`"

        ```yaml
        # Type: list
        heimdall_role_docker_networks_default: []
        ```

    ??? variable list "`heimdall_role_docker_networks_custom`"

        ```yaml
        # Type: list
        heimdall_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`heimdall_role_docker_restart_policy`"

        ```yaml
        # Type: string
        heimdall_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`heimdall_role_docker_state`"

        ```yaml
        # Type: string
        heimdall_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`heimdall_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        heimdall_role_autoheal_enabled: true
        ```

    ??? variable string "`heimdall_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        heimdall_role_depends_on: ""
        ```

    ??? variable string "`heimdall_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        heimdall_role_depends_on_delay: "0"
        ```

    ??? variable string "`heimdall_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        heimdall_role_depends_on_healthchecks:
        ```

    ??? variable bool "`heimdall_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        heimdall_role_diun_enabled: true
        ```

    ??? variable bool "`heimdall_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        heimdall_role_dns_enabled: true
        ```

    ??? variable bool "`heimdall_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        heimdall_role_docker_controller: true
        ```

    ??? variable bool "`heimdall_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        heimdall_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`heimdall_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        heimdall_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`heimdall_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        heimdall_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`heimdall_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        heimdall_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`heimdall_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        heimdall_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`heimdall_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        heimdall_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`heimdall_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        heimdall_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`heimdall_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        heimdall_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`heimdall_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        heimdall_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`heimdall_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        heimdall_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            heimdall_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "heimdall2.{{ user.domain }}"
              - "heimdall.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`heimdall_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        heimdall_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            heimdall_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'heimdall2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`heimdall_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        heimdall_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
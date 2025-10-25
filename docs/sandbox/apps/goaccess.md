---
hide:
  - tags
tags:
  - goaccess
  - monitoring
  - analytics
---

# GoAccess

## What is it?

[GoAccess](https://goaccess.io/) is an open source real-time web log analyzer and interactive viewer that runs in a terminal in *nix systems or through your browser.

It provides fast and valuable HTTP statistics for system administrators that require a visual server report on the fly.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://goaccess.io/){: .header-icons } | [:octicons-link-16: Docs](https://goaccess.io/man){: .header-icons } | [:octicons-mark-github-16: Github](https://goaccess.io/github){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/gregyankovoy/goaccess){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-goaccess

```

### 2. URL

- To access GoAccess, visit `https://goaccess._yourdomain.com_`

### 3. Setup

- The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    goaccess_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `goaccess_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `goaccess_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`goaccess_name`"

        ```yaml
        # Type: string
        goaccess_name: goaccess
        ```

=== "Paths"

    ??? variable string "`goaccess_role_paths_folder`"

        ```yaml
        # Type: string
        goaccess_role_paths_folder: "{{ goaccess_name }}"
        ```

    ??? variable string "`goaccess_role_paths_location`"

        ```yaml
        # Type: string
        goaccess_role_paths_location: "{{ server_appdata_path }}/{{ goaccess_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`goaccess_role_web_subdomain`"

        ```yaml
        # Type: string
        goaccess_role_web_subdomain: "{{ goaccess_name }}"
        ```

    ??? variable string "`goaccess_role_web_domain`"

        ```yaml
        # Type: string
        goaccess_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`goaccess_role_web_port`"

        ```yaml
        # Type: string
        goaccess_role_web_port: "7889"
        ```

    ??? variable string "`goaccess_role_web_url`"

        ```yaml
        # Type: string
        goaccess_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='goaccess') + '.' + lookup('role_var', '_web_domain', role='goaccess')
                                if (lookup('role_var', '_web_subdomain', role='goaccess') | length > 0)
                                else lookup('role_var', '_web_domain', role='goaccess')) }}"
        ```

=== "DNS"

    ??? variable string "`goaccess_role_dns_record`"

        ```yaml
        # Type: string
        goaccess_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='goaccess') }}"
        ```

    ??? variable string "`goaccess_role_dns_zone`"

        ```yaml
        # Type: string
        goaccess_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='goaccess') }}"
        ```

    ??? variable bool "`goaccess_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        goaccess_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`goaccess_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        goaccess_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`goaccess_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        goaccess_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`goaccess_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        goaccess_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`goaccess_role_traefik_certresolver`"

        ```yaml
        # Type: string
        goaccess_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`goaccess_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        goaccess_role_traefik_enabled: true
        ```

    ??? variable bool "`goaccess_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        goaccess_role_traefik_api_enabled: false
        ```

    ??? variable string "`goaccess_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        goaccess_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`goaccess_role_docker_container`"

        ```yaml
        # Type: string
        goaccess_role_docker_container: "{{ goaccess_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`goaccess_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        goaccess_role_docker_image_pull: true
        ```

    ??? variable string "`goaccess_role_docker_image_repo`"

        ```yaml
        # Type: string
        goaccess_role_docker_image_repo: "gregyankovoy/goaccess"
        ```

    ??? variable string "`goaccess_role_docker_image_tag`"

        ```yaml
        # Type: string
        goaccess_role_docker_image_tag: "latest"
        ```

    ??? variable string "`goaccess_role_docker_image`"

        ```yaml
        # Type: string
        goaccess_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='goaccess') }}:{{ lookup('role_var', '_docker_image_tag', role='goaccess') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`goaccess_role_docker_envs_default`"

        ```yaml
        # Type: dict
        goaccess_role_docker_envs_default: 
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
        ```

    ??? variable dict "`goaccess_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        goaccess_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`goaccess_role_docker_volumes_default`"

        ```yaml
        # Type: list
        goaccess_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='goaccess') }}:/config"
          - "{{ lookup('role_var', '_paths_location', role='traefik') }}:/opt/log"
        ```

    ??? variable list "`goaccess_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        goaccess_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`goaccess_role_docker_hostname`"

        ```yaml
        # Type: string
        goaccess_role_docker_hostname: "{{ goaccess_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`goaccess_role_docker_networks_alias`"

        ```yaml
        # Type: string
        goaccess_role_docker_networks_alias: "{{ goaccess_name }}"
        ```

    ??? variable list "`goaccess_role_docker_networks_default`"

        ```yaml
        # Type: list
        goaccess_role_docker_networks_default: []
        ```

    ??? variable list "`goaccess_role_docker_networks_custom`"

        ```yaml
        # Type: list
        goaccess_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`goaccess_role_docker_restart_policy`"

        ```yaml
        # Type: string
        goaccess_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`goaccess_role_docker_state`"

        ```yaml
        # Type: string
        goaccess_role_docker_state: started
        ```

    <h5>Force Kill</h5>

    ??? variable bool "`goaccess_role_docker_force_kill`"

        ```yaml
        # Type: bool (true/false)
        goaccess_role_docker_force_kill: true
        ```

=== "Global Override Options"

    ??? variable bool "`goaccess_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        goaccess_role_autoheal_enabled: true
        ```

    ??? variable string "`goaccess_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        goaccess_role_depends_on: ""
        ```

    ??? variable string "`goaccess_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        goaccess_role_depends_on_delay: "0"
        ```

    ??? variable string "`goaccess_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        goaccess_role_depends_on_healthchecks:
        ```

    ??? variable bool "`goaccess_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        goaccess_role_diun_enabled: true
        ```

    ??? variable bool "`goaccess_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        goaccess_role_dns_enabled: true
        ```

    ??? variable bool "`goaccess_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        goaccess_role_docker_controller: true
        ```

    ??? variable bool "`goaccess_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        goaccess_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`goaccess_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        goaccess_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`goaccess_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        goaccess_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`goaccess_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        goaccess_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`goaccess_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        goaccess_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`goaccess_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        goaccess_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`goaccess_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        goaccess_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`goaccess_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        goaccess_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`goaccess_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        goaccess_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`goaccess_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        goaccess_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            goaccess_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "goaccess2.{{ user.domain }}"
              - "goaccess.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`goaccess_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        goaccess_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            goaccess_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'goaccess2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`goaccess_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        goaccess_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
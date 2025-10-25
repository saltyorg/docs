---
hide:
  - tags
tags:
  - discoflix
  - requests
  - discord
---

# DiscoFlix

## What is it?

[DiscoFlix](https://github.com/nickheyer/discoflix) is a user-request-management system for your media server. With Radarr / Sonarr / Discord integration, DiscoFlix facilitates requests by your users for your media server.

Also comes with a [REST-API](https://tinyurl.com/discoflix).

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/nickheyer/discoflix){: .header-icons } | [:octicons-link-16: Docs](https://github.com/nickheyer/discoflix/blob/main/README.md){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/nickheyer/discoflix){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/nickheyer/discoflix){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-discoflix

```

### 2. URL

- To access DiscoFlix, visit `https://discoflix._yourdomain.com_`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    discoflix_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `discoflix_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `discoflix_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`discoflix_name`"

        ```yaml
        # Type: string
        discoflix_name: discoflix
        ```

=== "Paths"

    ??? variable string "`discoflix_role_paths_folder`"

        ```yaml
        # Type: string
        discoflix_role_paths_folder: "{{ discoflix_name }}"
        ```

    ??? variable string "`discoflix_role_paths_location`"

        ```yaml
        # Type: string
        discoflix_role_paths_location: "{{ server_appdata_path }}/{{ discoflix_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`discoflix_role_web_subdomain`"

        ```yaml
        # Type: string
        discoflix_role_web_subdomain: "{{ discoflix_name }}"
        ```

    ??? variable string "`discoflix_role_web_domain`"

        ```yaml
        # Type: string
        discoflix_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`discoflix_role_web_port`"

        ```yaml
        # Type: string
        discoflix_role_web_port: "5454"
        ```

    ??? variable string "`discoflix_role_web_url`"

        ```yaml
        # Type: string
        discoflix_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='discoflix') + '.' + lookup('role_var', '_web_domain', role='discoflix')
                                 if (lookup('role_var', '_web_subdomain', role='discoflix') | length > 0)
                                 else lookup('role_var', '_web_domain', role='discoflix')) }}"
        ```

=== "DNS"

    ??? variable string "`discoflix_role_dns_record`"

        ```yaml
        # Type: string
        discoflix_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='discoflix') }}"
        ```

    ??? variable string "`discoflix_role_dns_zone`"

        ```yaml
        # Type: string
        discoflix_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='discoflix') }}"
        ```

    ??? variable bool "`discoflix_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        discoflix_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`discoflix_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        discoflix_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`discoflix_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        discoflix_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`discoflix_role_traefik_certresolver`"

        ```yaml
        # Type: string
        discoflix_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`discoflix_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        discoflix_role_traefik_enabled: true
        ```

    ??? variable bool "`discoflix_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        discoflix_role_traefik_api_enabled: false
        ```

    ??? variable string "`discoflix_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        discoflix_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`discoflix_role_docker_container`"

        ```yaml
        # Type: string
        discoflix_role_docker_container: "{{ discoflix_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`discoflix_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        discoflix_role_docker_image_pull: true
        ```

    ??? variable string "`discoflix_role_docker_image_repo`"

        ```yaml
        # Type: string
        discoflix_role_docker_image_repo: "nickheyer/discoflix"
        ```

    ??? variable string "`discoflix_role_docker_image_tag`"

        ```yaml
        # Type: string
        discoflix_role_docker_image_tag: "latest"
        ```

    ??? variable string "`discoflix_role_docker_image`"

        ```yaml
        # Type: string
        discoflix_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='discoflix') }}:{{ lookup('role_var', '_docker_image_tag', role='discoflix') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`discoflix_role_docker_envs_default`"

        ```yaml
        # Type: dict
        discoflix_role_docker_envs_default: 
          internal_df_url: "http://{{ discoflix_name }}:{{ lookup('role_var', '_web_port', role='discoflix') }}"
        ```

    ??? variable dict "`discoflix_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        discoflix_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`discoflix_role_docker_volumes_default`"

        ```yaml
        # Type: list
        discoflix_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='discoflix') }}/data:/app/data"
        ```

    ??? variable list "`discoflix_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        discoflix_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`discoflix_role_docker_hostname`"

        ```yaml
        # Type: string
        discoflix_role_docker_hostname: "{{ discoflix_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`discoflix_role_docker_networks_alias`"

        ```yaml
        # Type: string
        discoflix_role_docker_networks_alias: "{{ discoflix_name }}"
        ```

    ??? variable list "`discoflix_role_docker_networks_default`"

        ```yaml
        # Type: list
        discoflix_role_docker_networks_default: []
        ```

    ??? variable list "`discoflix_role_docker_networks_custom`"

        ```yaml
        # Type: list
        discoflix_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`discoflix_role_docker_restart_policy`"

        ```yaml
        # Type: string
        discoflix_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`discoflix_role_docker_state`"

        ```yaml
        # Type: string
        discoflix_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`discoflix_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        discoflix_role_autoheal_enabled: true
        ```

    ??? variable string "`discoflix_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        discoflix_role_depends_on: ""
        ```

    ??? variable string "`discoflix_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        discoflix_role_depends_on_delay: "0"
        ```

    ??? variable string "`discoflix_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        discoflix_role_depends_on_healthchecks:
        ```

    ??? variable bool "`discoflix_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        discoflix_role_diun_enabled: true
        ```

    ??? variable bool "`discoflix_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        discoflix_role_dns_enabled: true
        ```

    ??? variable bool "`discoflix_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        discoflix_role_docker_controller: true
        ```

    ??? variable bool "`discoflix_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        discoflix_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`discoflix_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        discoflix_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`discoflix_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        discoflix_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`discoflix_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        discoflix_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`discoflix_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        discoflix_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`discoflix_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        discoflix_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`discoflix_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        discoflix_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`discoflix_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        discoflix_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`discoflix_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        discoflix_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`discoflix_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        discoflix_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            discoflix_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "discoflix2.{{ user.domain }}"
              - "discoflix.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`discoflix_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        discoflix_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            discoflix_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'discoflix2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`discoflix_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        discoflix_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
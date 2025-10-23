---
hide:
  - tags
tags:
  - gaps
  - media
  - plex
---

# Gaps

## What is it?

[Gaps](https://github.com/JasonHHouse/gaps) searches through your Plex Server for all movies, then queries for known movies in the same collection. If those movies don't exist in your library, Gaps will recommend getting those movies, legally of course.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will NOT have to log into the app itself, as basic Auth is disabled by default.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/JasonHHouse/gaps){: .header-icons } | [:octicons-link-16: Docs](https://github.com/JasonHHouse/gaps#-usage-){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/JasonHHouse/gaps){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/housewrecker/gaps){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-gaps

```

### 2. URL

- To access gaps, visit `https://gaps._yourdomain.com_`

### 3. Setup

- All you need to get started is a [Plex Auth Token](../../reference/plex_auth_token.md?h=plex+token#saltbox-role), and a TMDB api key.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        gaps_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `gaps_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `gaps_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`gaps_name`"

        ```yaml
        # Type: string
        gaps_name: gaps
        ```

=== "Paths"

    ??? variable string "`gaps_role_paths_folder`"

        ```yaml
        # Type: string
        gaps_role_paths_folder: "{{ gaps_name }}"
        ```

    ??? variable string "`gaps_role_paths_location`"

        ```yaml
        # Type: string
        gaps_role_paths_location: "{{ server_appdata_path }}/{{ gaps_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`gaps_role_web_subdomain`"

        ```yaml
        # Type: string
        gaps_role_web_subdomain: "{{ gaps_name }}"
        ```

    ??? variable string "`gaps_role_web_domain`"

        ```yaml
        # Type: string
        gaps_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`gaps_role_web_port`"

        ```yaml
        # Type: string
        gaps_role_web_port: "8484"
        ```

    ??? variable string "`gaps_role_web_url`"

        ```yaml
        # Type: string
        gaps_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='gaps') + '.' + lookup('role_var', '_web_domain', role='gaps')
                            if (lookup('role_var', '_web_subdomain', role='gaps') | length > 0)
                            else lookup('role_var', '_web_domain', role='gaps')) }}"
        ```

=== "DNS"

    ??? variable string "`gaps_role_dns_record`"

        ```yaml
        # Type: string
        gaps_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='gaps') }}"
        ```

    ??? variable string "`gaps_role_dns_zone`"

        ```yaml
        # Type: string
        gaps_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='gaps') }}"
        ```

    ??? variable bool "`gaps_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`gaps_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        gaps_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`gaps_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        gaps_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`gaps_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        gaps_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`gaps_role_traefik_certresolver`"

        ```yaml
        # Type: string
        gaps_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`gaps_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_traefik_enabled: true
        ```

    ??? variable bool "`gaps_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_traefik_api_enabled: false
        ```

    ??? variable string "`gaps_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        gaps_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`gaps_role_docker_container`"

        ```yaml
        # Type: string
        gaps_role_docker_container: "{{ gaps_name }}"
        ```

    ##### Image

    ??? variable bool "`gaps_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_docker_image_pull: true
        ```

    ??? variable string "`gaps_role_docker_image_repo`"

        ```yaml
        # Type: string
        gaps_role_docker_image_repo: "housewrecker/gaps"
        ```

    ??? variable string "`gaps_role_docker_image_tag`"

        ```yaml
        # Type: string
        gaps_role_docker_image_tag: "latest"
        ```

    ??? variable string "`gaps_role_docker_image`"

        ```yaml
        # Type: string
        gaps_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='gaps') }}:{{ lookup('role_var', '_docker_image_tag', role='gaps') }}"
        ```

    ##### Envs

    ??? variable dict "`gaps_role_docker_envs_default`"

        ```yaml
        # Type: dict
        gaps_role_docker_envs_default: 
          TZ: "{{ tz }}"
          ENABLE_LOGIN: "false"
          ENABLE_SSL: "false"
        ```

    ??? variable dict "`gaps_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        gaps_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`gaps_role_docker_volumes_default`"

        ```yaml
        # Type: list
        gaps_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='gaps') }}:/usr/data"
        ```

    ??? variable list "`gaps_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        gaps_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`gaps_role_docker_hostname`"

        ```yaml
        # Type: string
        gaps_role_docker_hostname: "{{ gaps_name }}"
        ```

    ##### Networks

    ??? variable string "`gaps_role_docker_networks_alias`"

        ```yaml
        # Type: string
        gaps_role_docker_networks_alias: "{{ gaps_name }}"
        ```

    ??? variable list "`gaps_role_docker_networks_default`"

        ```yaml
        # Type: list
        gaps_role_docker_networks_default: []
        ```

    ??? variable list "`gaps_role_docker_networks_custom`"

        ```yaml
        # Type: list
        gaps_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`gaps_role_docker_restart_policy`"

        ```yaml
        # Type: string
        gaps_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`gaps_role_docker_state`"

        ```yaml
        # Type: string
        gaps_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`gaps_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        gaps_role_autoheal_enabled: true
        ```

    ??? variable string "`gaps_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        gaps_role_depends_on: ""
        ```

    ??? variable string "`gaps_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        gaps_role_depends_on_delay: "0"
        ```

    ??? variable string "`gaps_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        gaps_role_depends_on_healthchecks:
        ```

    ??? variable bool "`gaps_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        gaps_role_diun_enabled: true
        ```

    ??? variable bool "`gaps_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        gaps_role_dns_enabled: true
        ```

    ??? variable bool "`gaps_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        gaps_role_docker_controller: true
        ```

    ??? variable bool "`gaps_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        gaps_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`gaps_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        gaps_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`gaps_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        gaps_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`gaps_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        gaps_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`gaps_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`gaps_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        gaps_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`gaps_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        gaps_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`gaps_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        gaps_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`gaps_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        gaps_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`gaps_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        gaps_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            gaps_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "gaps2.{{ user.domain }}"
              - "gaps.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`gaps_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        gaps_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            gaps_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'gaps2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`gaps_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        gaps_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
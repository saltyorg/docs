---
hide:
  - tags
tags:
  - plex_utills
  - plex
  - utilities
  - management
---

# Plex Utills

## What is it?

[Plex Utills](https://github.com/jkirkcaldy/plex-utills) is a web-based utility collection for managing and maintaining your Plex Media Server. It provides various tools and helpers for common Plex administration tasks.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/jkirkcaldy/plex-utills){: .header-icons } | [:octicons-link-16: Docs](https://github.com/jkirkcaldy/plex-utills#readme){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/jkirkcaldy/plex-utills){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jkirkcaldy/plex-utills){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-plex_utills

```

### 2. URL

- To access Plex Utills, visit `https://plex-utills._yourdomain.com_`

### 3. Setup

- Configuration files are stored in `/opt/plex-utills`
- Application logs are stored in `/opt/plex-utills/logs`
- The `/mnt` directory is mounted at `/films` for media access
- The web interface runs on port 80 internally

!!! tip
    Configure the application through the web interface after your first login.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        plex_utills_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `plex_utills_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `plex_utills_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`plex_utills_name`"

        ```yaml
        # Type: string
        plex_utills_name: plex-utills
        ```

=== "Paths"

    ??? variable string "`plex_utills_role_paths_folder`"

        ```yaml
        # Type: string
        plex_utills_role_paths_folder: "{{ plex_utills_name }}"
        ```

    ??? variable string "`plex_utills_role_paths_location`"

        ```yaml
        # Type: string
        plex_utills_role_paths_location: "{{ server_appdata_path }}/{{ plex_utills_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`plex_utills_role_web_subdomain`"

        ```yaml
        # Type: string
        plex_utills_role_web_subdomain: "{{ plex_utills_name }}"
        ```

    ??? variable string "`plex_utills_role_web_domain`"

        ```yaml
        # Type: string
        plex_utills_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`plex_utills_role_web_port`"

        ```yaml
        # Type: string
        plex_utills_role_web_port: "80"
        ```

    ??? variable string "`plex_utills_role_web_url`"

        ```yaml
        # Type: string
        plex_utills_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='plex_utills') + '.' + lookup('role_var', '_web_domain', role='plex_utills')
                                   if (lookup('role_var', '_web_subdomain', role='plex_utills') | length > 0)
                                   else lookup('role_var', '_web_domain', role='plex_utills')) }}"
        ```

=== "DNS"

    ??? variable string "`plex_utills_role_dns_record`"

        ```yaml
        # Type: string
        plex_utills_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='plex_utills') }}"
        ```

    ??? variable string "`plex_utills_role_dns_zone`"

        ```yaml
        # Type: string
        plex_utills_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='plex_utills') }}"
        ```

    ??? variable bool "`plex_utills_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        plex_utills_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`plex_utills_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        plex_utills_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`plex_utills_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        plex_utills_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`plex_utills_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        plex_utills_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`plex_utills_role_traefik_certresolver`"

        ```yaml
        # Type: string
        plex_utills_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`plex_utills_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        plex_utills_role_traefik_enabled: true
        ```

    ??? variable bool "`plex_utills_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        plex_utills_role_traefik_api_enabled: false
        ```

    ??? variable string "`plex_utills_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        plex_utills_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`plex_utills_role_docker_container`"

        ```yaml
        # Type: string
        plex_utills_role_docker_container: "{{ plex_utills_name }}"
        ```

    ##### Image

    ??? variable bool "`plex_utills_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        plex_utills_role_docker_image_pull: true
        ```

    ??? variable string "`plex_utills_role_docker_image_tag`"

        ```yaml
        # Type: string
        plex_utills_role_docker_image_tag: "latest"
        ```

    ??? variable string "`plex_utills_role_docker_image_repo`"

        ```yaml
        # Type: string
        plex_utills_role_docker_image_repo: "jkirkcaldy/plex-utills"
        ```

    ??? variable string "`plex_utills_role_docker_image`"

        ```yaml
        # Type: string
        plex_utills_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='plex_utills') }}:{{ lookup('role_var', '_docker_image_tag', role='plex_utills') }}"
        ```

    ##### Envs

    ??? variable dict "`plex_utills_role_docker_envs_default`"

        ```yaml
        # Type: dict
        plex_utills_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`plex_utills_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        plex_utills_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`plex_utills_role_docker_volumes_default`"

        ```yaml
        # Type: list
        plex_utills_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='plex_utills') }}:/config"
          - "{{ lookup('role_var', '_paths_location', role='plex_utills') }}/logs:/logs"
          - "/mnt:/films"
        ```

    ??? variable list "`plex_utills_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        plex_utills_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`plex_utills_role_docker_hostname`"

        ```yaml
        # Type: string
        plex_utills_role_docker_hostname: "{{ plex_utills_name }}"
        ```

    ##### Networks

    ??? variable string "`plex_utills_role_docker_networks_alias`"

        ```yaml
        # Type: string
        plex_utills_role_docker_networks_alias: "{{ plex_utills_name }}"
        ```

    ??? variable list "`plex_utills_role_docker_networks_default`"

        ```yaml
        # Type: list
        plex_utills_role_docker_networks_default: []
        ```

    ??? variable list "`plex_utills_role_docker_networks_custom`"

        ```yaml
        # Type: list
        plex_utills_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`plex_utills_role_docker_restart_policy`"

        ```yaml
        # Type: string
        plex_utills_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`plex_utills_role_docker_state`"

        ```yaml
        # Type: string
        plex_utills_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`plex_utills_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        plex_utills_role_autoheal_enabled: true
        ```

    ??? variable string "`plex_utills_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        plex_utills_role_depends_on: ""
        ```

    ??? variable string "`plex_utills_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        plex_utills_role_depends_on_delay: "0"
        ```

    ??? variable string "`plex_utills_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        plex_utills_role_depends_on_healthchecks:
        ```

    ??? variable bool "`plex_utills_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        plex_utills_role_diun_enabled: true
        ```

    ??? variable bool "`plex_utills_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        plex_utills_role_dns_enabled: true
        ```

    ??? variable bool "`plex_utills_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        plex_utills_role_docker_controller: true
        ```

    ??? variable bool "`plex_utills_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        plex_utills_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`plex_utills_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        plex_utills_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`plex_utills_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        plex_utills_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`plex_utills_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        plex_utills_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`plex_utills_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        plex_utills_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`plex_utills_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        plex_utills_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`plex_utills_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        plex_utills_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`plex_utills_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        plex_utills_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            plex_utills_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "plex_utills2.{{ user.domain }}"
              - "plex_utills.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`plex_utills_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        plex_utills_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            plex_utills_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'plex_utills2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`plex_utills_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        plex_utills_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
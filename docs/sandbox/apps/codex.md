---
hide:
  - tags
tags:
  - comic
  - manga
---

# Codex

## Overview

[Codex](https://github.com/ajslater/codex) is a web based comic archive browser and reader

- Codex is a web server.
- GPLv3 Licenced.
- Full text search of metadata and bookmarks.
- Filter and sort on all comic metadata and unread status per user.
- Browse a tree of Publishers, Imprints, Series, Volumes, or your own folder hierarchy, or by tagged Story Arc.
- Read comics in a variety of aspect ratios and directions that fit your screen.
- Watches the filesystem and automatically imports new or changed comics.
- Anonymous browsing and reading or registered users only, to your preference.
- Per user bookmarking & settings, even before you make an account.
- Private Libraries accessible only to certain groups of users.
- Reads CBZ, CBR, CBT, and PDF formatted comics.
- Syndication with OPDS 1 & 2, streaming, search and authentication.
- Add custom covers to Folders, Publishers, Imprints, Series, and Story Arcs.
- Runs in 1GB of RAM, faster with more.

!!! info
    By default, the role is **NOT** protected behind your Authelia/SSO middleware. You will have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/ajslater/codex){: .header-icons } | [:octicons-link-16: Docs](https://github.com/ajslater/codex#%EF%B8%8F-configuration){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/ajslater/codex){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/ajslater/codex){: .header-icons }|

Recommended install types: Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-codex

```

### 2. URL

- To access Codex, visit <https://codex.iYOUR_DOMAIN_NAMEi>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    codex_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `codex_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `codex_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`codex_name`"

        ```yaml
        # Type: string
        codex_name: codex
        ```

=== "Paths"

    ??? variable string "`codex_role_paths_folder`"

        ```yaml
        # Type: string
        codex_role_paths_folder: "{{ codex_name }}"
        ```

    ??? variable string "`codex_role_paths_location`"

        ```yaml
        # Type: string
        codex_role_paths_location: "{{ server_appdata_path }}/{{ codex_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`codex_role_web_subdomain`"

        ```yaml
        # Type: string
        codex_role_web_subdomain: "{{ codex_name }}"
        ```

    ??? variable string "`codex_role_web_domain`"

        ```yaml
        # Type: string
        codex_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`codex_role_web_port`"

        ```yaml
        # Type: string
        codex_role_web_port: "9810"
        ```

    ??? variable string "`codex_role_web_url`"

        ```yaml
        # Type: string
        codex_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='codex') + '.' + lookup('role_var', '_web_domain', role='codex')
                             if (lookup('role_var', '_web_subdomain', role='codex') | length > 0)
                             else lookup('role_var', '_web_domain', role='codex')) }}"
        ```

=== "DNS"

    ??? variable string "`codex_role_dns_record`"

        ```yaml
        # Type: string
        codex_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='codex') }}"
        ```

    ??? variable string "`codex_role_dns_zone`"

        ```yaml
        # Type: string
        codex_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='codex') }}"
        ```

    ??? variable bool "`codex_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        codex_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`codex_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        codex_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`codex_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        codex_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`codex_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        codex_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`codex_role_traefik_certresolver`"

        ```yaml
        # Type: string
        codex_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`codex_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        codex_role_traefik_enabled: true
        ```

    ??? variable bool "`codex_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        codex_role_traefik_api_enabled: false
        ```

    ??? variable string "`codex_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        codex_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`codex_role_docker_container`"

        ```yaml
        # Type: string
        codex_role_docker_container: "{{ codex_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`codex_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        codex_role_docker_image_pull: true
        ```

    ??? variable string "`codex_role_docker_image_repo`"

        ```yaml
        # Type: string
        codex_role_docker_image_repo: "docker.io/ajslater/codex"
        ```

    ??? variable string "`codex_role_docker_image_tag`"

        ```yaml
        # Type: string
        codex_role_docker_image_tag: "latest"
        ```

    ??? variable string "`codex_role_docker_image`"

        ```yaml
        # Type: string
        codex_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='codex') }}:{{ lookup('role_var', '_docker_image_tag', role='codex') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`codex_role_docker_envs_default`"

        ```yaml
        # Type: dict
        codex_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`codex_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        codex_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`codex_role_docker_volumes_default`"

        ```yaml
        # Type: list
        codex_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='codex') }}:/config"
        ```

    ??? variable list "`codex_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        codex_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`codex_role_docker_hostname`"

        ```yaml
        # Type: string
        codex_role_docker_hostname: "{{ codex_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`codex_role_docker_networks_alias`"

        ```yaml
        # Type: string
        codex_role_docker_networks_alias: "{{ codex_name }}"
        ```

    ??? variable list "`codex_role_docker_networks_default`"

        ```yaml
        # Type: list
        codex_role_docker_networks_default: []
        ```

    ??? variable list "`codex_role_docker_networks_custom`"

        ```yaml
        # Type: list
        codex_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`codex_role_docker_restart_policy`"

        ```yaml
        # Type: string
        codex_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`codex_role_docker_state`"

        ```yaml
        # Type: string
        codex_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`codex_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        codex_role_autoheal_enabled: true
        ```

    ??? variable string "`codex_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        codex_role_depends_on: ""
        ```

    ??? variable string "`codex_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        codex_role_depends_on_delay: "0"
        ```

    ??? variable string "`codex_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        codex_role_depends_on_healthchecks:
        ```

    ??? variable bool "`codex_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        codex_role_diun_enabled: true
        ```

    ??? variable bool "`codex_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        codex_role_dns_enabled: true
        ```

    ??? variable bool "`codex_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        codex_role_docker_controller: true
        ```

    ??? variable bool "`codex_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        codex_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`codex_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        codex_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`codex_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        codex_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`codex_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        codex_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`codex_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        codex_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`codex_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        codex_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`codex_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        codex_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`codex_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        codex_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`codex_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        codex_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`codex_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        codex_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            codex_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "codex2.{{ user.domain }}"
              - "codex.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`codex_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        codex_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            codex_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'codex2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`codex_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        codex_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
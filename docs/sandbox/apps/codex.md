---
hide:
  - tags
tags:
  - comic
  - manga
---

# Codex

## What is it?

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

- To access Codex, visit `https://codex.xDOMAIN_NAMEx`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        codex_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `codex_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `codex_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    codex_name: codex

    ```

??? example "Paths"

    ```yaml
    # Type: string
    codex_role_paths_folder: "{{ codex_name }}"

    # Type: string
    codex_role_paths_location: "{{ server_appdata_path }}/{{ codex_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    codex_role_web_subdomain: "{{ codex_name }}"

    # Type: string
    codex_role_web_domain: "{{ user.domain }}"

    # Type: string
    codex_role_web_port: "9810"

    # Type: string
    codex_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='codex') + '.' + lookup('role_var', '_web_domain', role='codex')
                         if (lookup('role_var', '_web_subdomain', role='codex') | length > 0)
                         else lookup('role_var', '_web_domain', role='codex')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    codex_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='codex') }}"

    # Type: string
    codex_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='codex') }}"

    # Type: bool (true/false)
    codex_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    codex_role_traefik_sso_middleware: ""

    # Type: string
    codex_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    codex_role_traefik_middleware_custom: ""

    # Type: string
    codex_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    codex_role_traefik_enabled: true

    # Type: bool (true/false)
    codex_role_traefik_api_enabled: false

    # Type: string
    codex_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    codex_role_docker_container: "{{ codex_name }}"

    # Image
    # Type: bool (true/false)
    codex_role_docker_image_pull: true

    # Type: string
    codex_role_docker_image_repo: "docker.io/ajslater/codex"

    # Type: string
    codex_role_docker_image_tag: "latest"

    # Type: string
    codex_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='codex') }}:{{ lookup('role_var', '_docker_image_tag', role='codex') }}"

    # Envs
    # Type: dict
    codex_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    codex_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    codex_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='codex') }}:/config"

    # Type: list
    codex_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    codex_role_docker_hostname: "{{ codex_name }}"

    # Networks
    # Type: string
    codex_role_docker_networks_alias: "{{ codex_name }}"

    # Type: list
    codex_role_docker_networks_default: []

    # Type: list
    codex_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    codex_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    codex_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    codex_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    codex_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    codex_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    codex_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    codex_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    codex_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    codex_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    codex_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    codex_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    codex_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    codex_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    codex_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    codex_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    codex_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    codex_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    codex_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    codex_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        codex_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "codex2.{{ user.domain }}"
          - "codex.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        codex_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'codex2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

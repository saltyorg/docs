---
hide:
  - tags
tags:
  - wizarr
  - automation
  - invitations
---

# Wizarr

## What is it?

[Wizarr](https://github.com/Wizarrrr/wizarr)  is a automatic user invitation system for Plex, Jellyfin and Emby. Create a unique link and share it to a user and they will automatically be invited to your media Server! They will even be guided to download the client and instructions on how to use your requests software!


| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/Wizarrrr/wizarr){: .header-icons } | [:octicons-link-16: Docs](https://docs.wizarr.dev/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Wizarrrr/wizarr){: .header-icons } | [:material-docker: Docker](https://ghcr.io/wizarrrr/wizarr){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-wizarr

```

### 2. Setup

After installation, go to wizarr.yourdomain.tld, enter a name for your server, enter the plex server, plex token and choose the default librarys. As optional you can setup a request platform. Save, and you're ready to make your first invite URL!

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `wizarr_instances`.

    === "Role-level Override"

        Applies to all instances of wizarr:

        ```yaml
        wizarr_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `wizarr2`):

        ```yaml
        wizarr2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        wizarr_instances: ["wizarr"]

        ```

    === "Example"

        ```yaml
        # Type: list
        wizarr_instances: ["wizarr", "wizarr2"]

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        wizarr_role_paths_folder: "{{ wizarr_name }}"

        # Type: string
        wizarr_role_paths_location: "{{ server_appdata_path }}/{{ wizarr_role_paths_folder }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        wizarr2_paths_folder: "{{ wizarr_name }}"

        # Type: string
        wizarr2_paths_location: "{{ server_appdata_path }}/{{ wizarr_role_paths_folder }}"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        wizarr_role_web_subdomain: "{{ wizarr_name }}"

        # Type: string
        wizarr_role_web_domain: "{{ user.domain }}"

        # Type: string
        wizarr_role_web_port: "5690"

        # Type: string
        wizarr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='wizarr') + '.' + lookup('role_var', '_web_domain', role='wizarr')
                              if (lookup('role_var', '_web_subdomain', role='wizarr') | length > 0)
                              else lookup('role_var', '_web_domain', role='wizarr')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        wizarr2_web_subdomain: "{{ wizarr_name }}"

        # Type: string
        wizarr2_web_domain: "{{ user.domain }}"

        # Type: string
        wizarr2_web_port: "5690"

        # Type: string
        wizarr2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='wizarr') + '.' + lookup('role_var', '_web_domain', role='wizarr')
                          if (lookup('role_var', '_web_subdomain', role='wizarr') | length > 0)
                          else lookup('role_var', '_web_domain', role='wizarr')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        wizarr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='wizarr') }}"

        # Type: string
        wizarr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='wizarr') }}"

        # Type: bool (true/false)
        wizarr_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        wizarr2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='wizarr') }}"

        # Type: string
        wizarr2_dns_zone: "{{ lookup('role_var', '_web_domain', role='wizarr') }}"

        # Type: bool (true/false)
        wizarr2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        wizarr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        wizarr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        wizarr_role_traefik_middleware_custom: ""

        # Type: string
        wizarr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        wizarr_role_traefik_enabled: true

        # Type: bool (true/false)
        wizarr_role_traefik_api_enabled: true

        # Type: string
        wizarr_role_traefik_api_endpoint: "PathPrefix(`/join`) || PathPrefix(`/j`) || PathPrefix(`/static`) || PathPrefix(`/setup`)"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        wizarr2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        wizarr2_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        wizarr2_traefik_middleware_custom: ""

        # Type: string
        wizarr2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        wizarr2_traefik_enabled: true

        # Type: bool (true/false)
        wizarr2_traefik_api_enabled: true

        # Type: string
        wizarr2_traefik_api_endpoint: "PathPrefix(`/join`) || PathPrefix(`/j`) || PathPrefix(`/static`) || PathPrefix(`/setup`)"

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        wizarr_role_docker_container: "{{ wizarr_name }}"

        # Image
        # Type: bool (true/false)
        wizarr_role_docker_image_pull: true

        # Type: string
        wizarr_role_docker_image_repo: "ghcr.io/wizarrrr/wizarr"

        # Type: string
        wizarr_role_docker_image_tag: "latest"

        # Type: string
        wizarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='wizarr') }}:{{ lookup('role_var', '_docker_image_tag', role='wizarr') }}"

        # Envs
        # Type: dict
        wizarr_role_docker_envs_default: 
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          DISABLE_BUILTIN_AUTH: "{{ 'true' if (lookup('role_var', '_traefik_sso_middleware', role='wizarr') | length > 0) else 'false' }}"

        # Type: dict
        wizarr_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        wizarr_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='wizarr') }}/database:/data/database"
          - "{{ lookup('role_var', '_paths_location', role='wizarr') }}/wizard:/data/wizard"

        # Type: list
        wizarr_role_docker_volumes_custom: []

        # Hostname
        # Type: string
        wizarr_role_docker_hostname: "{{ wizarr_name }}"

        # Networks
        # Type: string
        wizarr_role_docker_networks_alias: "{{ wizarr_name }}"

        # Type: list
        wizarr_role_docker_networks_default: []

        # Type: list
        wizarr_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        wizarr_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        wizarr_role_docker_state: started

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        wizarr2_docker_container: "{{ wizarr_name }}"

        # Image
        # Type: bool (true/false)
        wizarr2_docker_image_pull: true

        # Type: string
        wizarr2_docker_image_repo: "ghcr.io/wizarrrr/wizarr"

        # Type: string
        wizarr2_docker_image_tag: "latest"

        # Type: string
        wizarr2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='wizarr') }}:{{ lookup('role_var', '_docker_image_tag', role='wizarr') }}"

        # Envs
        # Type: dict
        wizarr2_docker_envs_default: 
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          DISABLE_BUILTIN_AUTH: "{{ 'true' if (lookup('role_var', '_traefik_sso_middleware', role='wizarr') | length > 0) else 'false' }}"

        # Type: dict
        wizarr2_docker_envs_custom: {}

        # Volumes
        # Type: list
        wizarr2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='wizarr') }}/database:/data/database"
          - "{{ lookup('role_var', '_paths_location', role='wizarr') }}/wizard:/data/wizard"

        # Type: list
        wizarr2_docker_volumes_custom: []

        # Hostname
        # Type: string
        wizarr2_docker_hostname: "{{ wizarr_name }}"

        # Networks
        # Type: string
        wizarr2_docker_networks_alias: "{{ wizarr_name }}"

        # Type: list
        wizarr2_docker_networks_default: []

        # Type: list
        wizarr2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        wizarr2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        wizarr2_docker_state: started


        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        wizarr_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        wizarr_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        wizarr_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        wizarr_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        wizarr_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        wizarr_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        wizarr_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        wizarr_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        wizarr_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        wizarr_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        wizarr_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        wizarr_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        wizarr_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        wizarr_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        wizarr_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        wizarr_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        wizarr_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            wizarr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "wizarr2.{{ user.domain }}"
              - "wizarr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            wizarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'wizarr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `wizarr2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        wizarr2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        wizarr2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        wizarr2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        wizarr2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        wizarr2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        wizarr2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        wizarr2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        wizarr2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        wizarr2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        wizarr2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        wizarr2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        wizarr2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        wizarr2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        wizarr2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        wizarr2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        wizarr2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        wizarr2_web_scheme:

        ```

        1.  Example:

            ```yaml
            wizarr2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "wizarr2.{{ user.domain }}"
              - "wizarr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            wizarr2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'wizarr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

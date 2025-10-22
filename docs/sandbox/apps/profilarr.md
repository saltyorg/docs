---
hide:
  - tags
tags:
  - profilarr
  - sonarr
  - radarr
  - recyclarr
---

# Profilarr

Configuration management and auto-import tool for Radarr/Sonarr custom formats and profiles.

<div class="grid sb-buttons" markdown data-search-exclude>

[:material-home: Homepage&nbsp;&nbsp;](https://dictionarry.dev){ .md-button .md-button--stretch }

[:material-bookshelf: Manual&nbsp;&nbsp;](https://dictionarry.dev/profilarr-setup/101){ .md-button .md-button--stretch }

[:fontawesome-brands-docker: Releases&nbsp;&nbsp;](https://hub.docker.com/r/santiagosayshey/profilarr/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-discord: Community&nbsp;&nbsp;](https://discord.gg/XGdTJP5G8a){ .md-button .md-button--stretch }

</div>

---

!!! warning "Beta software / Modifies PVR configuration"
    Although core features are expected to work, this application is in early stages of development. It's recommended to back up your Radarr and Sonarr databases before running import or sync operations.

## Deployment

```shell
sb install sandbox-profilarr
```

## Usage

Visit `https://profilarr.xDOMAIN_NAMEx`.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        profilarr_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `profilarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `profilarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    profilarr_name: profilarr

    ```

??? example "Paths"

    ```yaml
    # Type: string
    profilarr_role_paths_folder: "{{ profilarr_name }}"

    # Type: string
    profilarr_role_paths_location: "{{ server_appdata_path }}/{{ profilarr_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    profilarr_role_web_subdomain: "{{ profilarr_name }}"

    # Type: string
    profilarr_role_web_domain: "{{ user.domain }}"

    # Type: string
    profilarr_role_web_port: "6868"

    # Type: string
    profilarr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='profilarr') + '.' + lookup('role_var', '_web_domain', role='profilarr')
                             if (lookup('role_var', '_web_subdomain', role='profilarr') | length > 0)
                             else lookup('role_var', '_web_domain', role='profilarr')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    profilarr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='profilarr') }}"

    # Type: string
    profilarr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='profilarr') }}"

    # Type: bool (true/false)
    profilarr_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    profilarr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    profilarr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    profilarr_role_traefik_middleware_custom: ""

    # Type: string
    profilarr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    profilarr_role_traefik_enabled: true

    # Type: bool (true/false)
    profilarr_role_traefik_api_enabled: true

    # Type: string
    profilarr_role_traefik_api_endpoint: "PathPrefix(`/api`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    profilarr_role_docker_container: "{{ profilarr_name }}"

    # Image
    # Type: bool (true/false)
    profilarr_role_docker_image_pull: true

    # Type: string
    profilarr_role_docker_image_repo: "santiagosayshey/profilarr"

    # Type: string
    profilarr_role_docker_image_tag: "latest"

    # Type: string
    profilarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='profilarr') }}:{{ lookup('role_var', '_docker_image_tag', role='profilarr') }}"

    # Envs
    # Type: dict
    profilarr_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    profilarr_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    profilarr_role_docker_volumes_default: 
      - "{{ profilarr_role_paths_location }}:/config"

    # Type: list
    profilarr_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    profilarr_role_docker_hostname: "{{ profilarr_name }}"

    # Networks
    # Type: string
    profilarr_role_docker_networks_alias: "{{ profilarr_name }}"

    # Type: list
    profilarr_role_docker_networks_default: []

    # Type: list
    profilarr_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    profilarr_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    profilarr_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    profilarr_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    profilarr_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    profilarr_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    profilarr_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    profilarr_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    profilarr_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    profilarr_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    profilarr_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    profilarr_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    profilarr_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    profilarr_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    profilarr_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    profilarr_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    profilarr_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    profilarr_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    profilarr_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    profilarr_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        profilarr_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "profilarr2.{{ user.domain }}"
          - "profilarr.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        profilarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'profilarr2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

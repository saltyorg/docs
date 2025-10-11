---
hide:
  - tags
tags:
  - table top
  - gaming
---

# Foundry

## What is it?

[Foundry](https://foundryvtt.com/) is a modern, feature-rich "virtual tabletop" (a "VTT"). Foundry VTT serves as a digital "tabletop" so that you can gather your friends and party members and have an excellent role-playing game experience together digitally.

Foundry VTT provides the full set of digital tools necessary to emulate and (and often surpass!) the experience of playing a game in-person, such as battle maps, integrated character sheets, digital dice, audio, voice / video, and more.

While other VTTs can provide some of these basic elements, the Foundry team prides ourselves on continually pushing the boundaries of the possible, providing rich dynamic lighting/fog of war, immersive audio, interactive map regions, powerful modding capabilities, and much more. Foundry VTT gives you everything you need (and then some) to forge thrilling and memorable moments with your gaming group!

!!! info
    By default, the role is **NOT** protected behind your Authelia/SSO middleware. You will have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://foundryvtt.com/){: .header-icons } | [:octicons-link-16: Docs](https://foundryvtt.com/kb/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/foundryvtt/foundryvtt){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/ajnart/Foundry/){: .header-icons }|

Recommended install types: Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-foundry

```

### 2. URL

- To access foundry, visit `https://foundry._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        foundry_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    foundry_name: foundry

    ```

??? example "Paths"

    ```yaml
    # Type: string
    foundry_role_paths_folder: "{{ foundry_name }}"

    # Type: string
    foundry_role_paths_location: "{{ server_appdata_path }}/{{ foundry_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    foundry_role_web_subdomain: "{{ foundry_name }}"

    # Type: string
    foundry_role_web_domain: "{{ user.domain }}"

    # Type: string
    foundry_role_web_port: "30000"

    # Type: string
    foundry_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='foundry') + '.' + lookup('role_var', '_web_domain', role='foundry')
                           if (lookup('role_var', '_web_subdomain', role='foundry') | length > 0)
                           else lookup('role_var', '_web_domain', role='foundry')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    foundry_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='foundry') }}"

    # Type: string
    foundry_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='foundry') }}"

    # Type: bool (true/false)
    foundry_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    foundry_role_traefik_sso_middleware: ""

    # Type: string
    foundry_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    foundry_role_traefik_middleware_custom: ""

    # Type: string
    foundry_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    foundry_role_traefik_enabled: true

    # Type: bool (true/false)
    foundry_role_traefik_api_enabled: false

    # Type: string
    foundry_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    foundry_role_docker_container: "{{ foundry_name }}"

    # Image
    # Type: bool (true/false)
    foundry_role_docker_image_pull: true

    # Type: string
    foundry_role_docker_image_repo: "felddy/foundryvtt"

    # Type: string
    foundry_role_docker_image_tag: "release"

    # Type: string
    foundry_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='foundry') }}:{{ lookup('role_var', '_docker_image_tag', role='foundry') }}"

    # Envs
    # Type: dict
    foundry_role_docker_envs_default: 
      FOUNDRY_HOSTNAME: "{{ foundry_name }}.{{ user.domain }}"
      FOUNDRY_ADMIN_KEY: "{{ user.pass }}"
      FOUNDRY_GID: "{{ gid }}"
      FOUNDRY_UID: "{{ uid }}"
      CONTAINER_PRESERVE_CONFIG: "true"
      CONTAINER_VERBOSE: "false"
      FOUNDRY_LICENSE_KEY: "{{ foundry.app_key }}"
      FOUNDRY_PROXY_SSL: "true"
      FOUNDRY_USERNAME: "{{ foundry.user }}"
      FOUNDRY_PASSWORD: "{{ foundry.pass }}"
      TIMEZONE: "{{ tz }}"

    # Type: dict
    foundry_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    foundry_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='foundry') }}/data:/data"
      - "{{ lookup('role_var', '_paths_location', role='foundry') }}/container_cache:/container_cache"
      - "/mnt/unionfs/Media/Foundry:/data/Data/Media"

    # Type: list
    foundry_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    foundry_role_docker_hostname: "{{ foundry_name }}"

    # Ports
    # Type: list
    foundry_role_docker_ports_defaults: 
      - "{{ lookup('role_var', '_web_port', role='foundry') }}:{{ lookup('role_var', '_web_port', role='foundry') }}"

    # Type: list
    foundry_role_docker_ports_custom: []

    # Networks
    # Type: string
    foundry_role_docker_networks_alias: "{{ foundry_name }}"

    # Type: list
    foundry_role_docker_networks_default: []

    # Type: list
    foundry_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    foundry_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    foundry_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    foundry_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    foundry_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    foundry_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    foundry_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    foundry_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    foundry_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    foundry_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    foundry_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    foundry_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    foundry_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    foundry_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    foundry_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    foundry_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    foundry_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    foundry_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    foundry_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    foundry_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        foundry_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "foundry2.{{ user.domain }}"
          - "foundry.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        foundry_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'foundry2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

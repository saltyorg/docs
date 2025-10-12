---
hide:
  - tags
tags:
  - stash
  - media
  - organizer
---

# Stash

## What is it?

[Stash](https://stashapp.cc/) is a locally hosted web-based app written in Go which organizes and serves your porn.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://stashapp.cc/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/stashapp/stash/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/stashapp/stash){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/stashapp/stash){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-stash

```

### 2. URL

- To access Stash, visit `https://stash._yourdomain.com_`

### 3. Setup

On a clean installation, Stash only creates its config file when the user has gone through the setup wizard. If you receive errors on future visits to Stash regarding public access, re-run `sb install sandbox-stash` to apply the appropriate config edits to disable these warnings.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        stash_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `stash_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `stash_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    stash_name: stash

    ```

??? example "Paths"

    ```yaml
    # Type: string
    stash_role_paths_folder: "{{ stash_name }}"

    # Type: string
    stash_role_paths_location: "{{ server_appdata_path }}/{{ stash_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    stash_role_web_subdomain: "{{ stash_name }}"

    # Type: string
    stash_role_web_domain: "{{ user.domain }}"

    # Type: string
    stash_role_web_port: "9999"

    # Type: string
    stash_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='stash') + '.' + lookup('role_var', '_web_domain', role='stash')
                         if (lookup('role_var', '_web_subdomain', role='stash') | length > 0)
                         else lookup('role_var', '_web_domain', role='stash')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    stash_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='stash') }}"

    # Type: string
    stash_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='stash') }}"

    # Type: bool (true/false)
    stash_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    stash_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    stash_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    stash_role_traefik_middleware_custom: ""

    # Type: string
    stash_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    stash_role_traefik_enabled: true

    # Type: bool (true/false)
    stash_role_traefik_api_enabled: false

    # Type: string
    stash_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    stash_role_docker_container: "{{ stash_name }}"

    # Image
    # Type: bool (true/false)
    stash_role_docker_image_pull: true

    # Type: string
    stash_role_docker_image_repo: "ghcr.io/hotio/stash"

    # Type: string
    stash_role_docker_image_tag: "latest"

    # Type: string
    stash_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='stash') }}:{{ lookup('role_var', '_docker_image_tag', role='stash') }}"

    # Envs
    # Type: dict
    stash_role_docker_envs_default: 
      TZ: "{{ tz }}"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"

    # Type: dict
    stash_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    stash_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='stash') }}/config:/config"
      - "{{ lookup('role_var', '_paths_location', role='stash') }}/metadata:/metadata"
      - "{{ lookup('role_var', '_paths_location', role='stash') }}/cache:/cache"
      - "{{ lookup('role_var', '_paths_location', role='stash') }}/generated:/generated"
      - "/mnt/unionfs/Media/Adult:/data"

    # Type: list
    stash_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    stash_role_docker_hostname: "{{ stash_name }}"

    # Networks
    # Type: string
    stash_role_docker_networks_alias: "{{ stash_name }}"

    # Type: list
    stash_role_docker_networks_default: []

    # Type: list
    stash_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    stash_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    stash_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    stash_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    stash_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    stash_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    stash_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    stash_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    stash_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    stash_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    stash_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    stash_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    stash_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    stash_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    stash_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    stash_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    stash_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    stash_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    stash_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    stash_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        stash_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "stash2.{{ user.domain }}"
          - "stash.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        stash_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'stash2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

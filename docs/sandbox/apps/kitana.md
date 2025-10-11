---
hide:
  - tags
tags:
  - kitana
  - plex
  - frontend
---

# Kitana

## What is it?

[Kitana](https://github.com/pannal/Kitana) is a responsive Plex plugin web frontend.

Running one instance of Kitana can serve infinite amounts of servers and plugins - you can even expose your Kitana instance to your friends, so they can manage their plugins as well, so they don't have to run their own Kitana instance.

Kitana was built for Sub-Zero originally, but handles other plugins just as well.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/pannal/Kitana){: .header-icons } | [:octicons-link-16: Docs](https://github.com/pannal/Kitana){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/pannal/Kitana){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/pannal/kitana){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-kitana

```

### 2. URL

- To access Kitana, visit `https://kitana._yourdomain.com_`

### 3. Setup

- pen your browser and visit your Kitana instance `https://kitana._yourdomain.com_`

- authenticate against Plex.TV

- select your server (non-owned may not work; local connections are preferred)

- profit

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        kitana_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    kitana_name: kitana

    ```

??? example "Paths"

    ```yaml
    # Type: string
    kitana_role_paths_folder: "{{ kitana_name }}"

    # Type: string
    kitana_role_paths_location: "{{ server_appdata_path }}/{{ kitana_role_paths_folder }}"

    # Type: string
    kitana_role_paths_config_location: "{{ kitana_role_paths_location }}/config.yml"

    ```

??? example "Web"

    ```yaml
    # Type: string
    kitana_role_web_subdomain: "{{ kitana_name }}"

    # Type: string
    kitana_role_web_domain: "{{ user.domain }}"

    # Type: string
    kitana_role_web_port: "31337"

    # Type: string
    kitana_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='kitana') + '.' + lookup('role_var', '_web_domain', role='kitana')
                          if (lookup('role_var', '_web_subdomain', role='kitana') | length > 0)
                          else lookup('role_var', '_web_domain', role='kitana')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    kitana_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='kitana') }}"

    # Type: string
    kitana_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='kitana') }}"

    # Type: bool (true/false)
    kitana_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    kitana_role_traefik_sso_middleware: ""

    # Type: string
    kitana_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    kitana_role_traefik_middleware_custom: ""

    # Type: string
    kitana_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    kitana_role_traefik_enabled: true

    # Type: bool (true/false)
    kitana_role_traefik_api_enabled: false

    # Type: string
    kitana_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    kitana_role_docker_container: "{{ kitana_name }}"

    # Image
    # Type: bool (true/false)
    kitana_role_docker_image_pull: true

    # Type: string
    kitana_role_docker_image_repo: "pannal/kitana"

    # Type: string
    kitana_role_docker_image_tag: "latest"

    # Type: string
    kitana_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='kitana') }}:{{ lookup('role_var', '_docker_image_tag', role='kitana') }}"

    # Envs
    # Type: dict
    kitana_role_docker_envs_default: 
      TZ: "{{ tz }}"

    # Type: dict
    kitana_role_docker_envs_custom: {}

    # Commands
    # Type: list
    kitana_role_docker_commands_default: 
      - "-P"

    # Type: list
    kitana_role_docker_commands_custom: []

    # Volumes
    # Type: list
    kitana_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='kitana') }}:/app/data"

    # Type: list
    kitana_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    kitana_role_docker_hostname: "{{ kitana_name }}"

    # Networks
    # Type: string
    kitana_role_docker_networks_alias: "{{ kitana_name }}"

    # Type: list
    kitana_role_docker_networks_default: []

    # Type: list
    kitana_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    kitana_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    kitana_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    kitana_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    kitana_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    kitana_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    kitana_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    kitana_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    kitana_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    kitana_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    kitana_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    kitana_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    kitana_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    kitana_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    kitana_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    kitana_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    kitana_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    kitana_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    kitana_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    kitana_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        kitana_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "kitana2.{{ user.domain }}"
          - "kitana.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        kitana_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'kitana2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

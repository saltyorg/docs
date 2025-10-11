---
hide:
  - tags
tags:
  - syncthing
  - backup
  - sync
---

# Syncthing

## What is it?

[Syncthing](https://syncthing.net/) is a continuous file synchronization program. It synchronizes files between two or more computers in real time, safely protected from prying eyes. Your data is your data alone and you deserve to choose where it is stored, whether it is shared with some third party, and how it's transmitted over the internet.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://syncthing.comnet/){: .header-icons } | [:octicons-link-16: Docs](https://docs.syncthing.net/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/syncthing/syncthing){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/syncthing){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-syncthing

```

### 2. URL

- To access the Syncthing dashboard, visit `https://syncthing._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        syncthing_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    syncthing_name: syncthing

    ```

??? example "Paths"

    ```yaml
    # Type: string
    syncthing_role_paths_folder: "{{ syncthing_name }}"

    # Type: string
    syncthing_role_paths_location: "{{ server_appdata_path }}/{{ syncthing_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    syncthing_role_web_subdomain: "{{ syncthing_name }}"

    # Type: string
    syncthing_role_web_domain: "{{ user.domain }}"

    # Type: string
    syncthing_role_web_port: "8384"

    # Type: string
    syncthing_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='syncthing') + '.' + lookup('role_var', '_web_domain', role='syncthing')
                             if (lookup('role_var', '_web_subdomain', role='syncthing') | length > 0)
                             else lookup('role_var', '_web_domain', role='syncthing')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    syncthing_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='syncthing') }}"

    # Type: string
    syncthing_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='syncthing') }}"

    # Type: bool (true/false)
    syncthing_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    syncthing_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    syncthing_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    syncthing_role_traefik_middleware_custom: ""

    # Type: string
    syncthing_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    syncthing_role_traefik_enabled: true

    # Type: bool (true/false)
    syncthing_role_traefik_api_enabled: false

    # Type: string
    syncthing_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    syncthing_role_docker_container: "{{ syncthing_name }}"

    # Image
    # Type: bool (true/false)
    syncthing_role_docker_image_pull: true

    # Type: string
    syncthing_role_docker_image_repo: "lscr.io/linuxserver/syncthing"

    # Type: string
    syncthing_role_docker_image_tag: "latest"

    # Type: string
    syncthing_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='syncthing') }}:{{ lookup('role_var', '_docker_image_tag', role='syncthing') }}"

    # Ports
    # Type: list
    syncthing_role_docker_ports_defaults: 
      - "22000:22000/tcp"
      - "22000:22000/udp"
      - "21027:21027/udp"

    # Type: list
    syncthing_role_docker_ports_custom: []

    # Envs
    # Type: dict
    syncthing_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    syncthing_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    syncthing_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='syncthing') }}:/config"

    # Type: list
    syncthing_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    syncthing_role_docker_hostname: "{{ syncthing_name }}"

    # Networks
    # Type: string
    syncthing_role_docker_networks_alias: "{{ syncthing_name }}"

    # Type: list
    syncthing_role_docker_networks_default: []

    # Type: list
    syncthing_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    syncthing_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    syncthing_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    syncthing_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    syncthing_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    syncthing_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    syncthing_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    syncthing_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    syncthing_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    syncthing_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    syncthing_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    syncthing_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    syncthing_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    syncthing_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    syncthing_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    syncthing_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    syncthing_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    syncthing_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    syncthing_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    syncthing_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        syncthing_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "syncthing2.{{ user.domain }}"
          - "syncthing.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        syncthing_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'syncthing2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
hide:
  - tags
tags:
  - medusa
  - media
  - tv
---

# Medusa

## What is it?

[Medusa](https://pymedusa.com/) is an automatic Video Library Manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://pymedusa.com/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/pymedusa/Medusa/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/pymedusa/Medusa){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/medusa){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-medusa

```

### 2. URL

- To access Medusa, visit `https://medusa._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        medusa_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `medusa_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `medusa_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    medusa_name: medusa

    ```

??? example "Paths"

    ```yaml
    # Type: string
    medusa_role_paths_folder: "{{ medusa_name }}"

    # Type: string
    medusa_role_paths_location: "{{ server_appdata_path }}/{{ medusa_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    medusa_role_web_subdomain: "{{ medusa_name }}"

    # Type: string
    medusa_role_web_domain: "{{ user.domain }}"

    # Type: string
    medusa_role_web_port: "8081"

    # Type: string
    medusa_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='medusa') + '.' + lookup('role_var', '_web_domain', role='medusa')
                          if (lookup('role_var', '_web_subdomain', role='medusa') | length > 0)
                          else lookup('role_var', '_web_domain', role='medusa')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    medusa_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='medusa') }}"

    # Type: string
    medusa_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='medusa') }}"

    # Type: bool (true/false)
    medusa_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    medusa_role_traefik_sso_middleware: ""

    # Type: string
    medusa_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    medusa_role_traefik_middleware_custom: ""

    # Type: string
    medusa_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    medusa_role_traefik_enabled: true

    # Type: bool (true/false)
    medusa_role_traefik_api_enabled: false

    # Type: string
    medusa_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    medusa_role_docker_container: "{{ medusa_name }}"

    # Image
    # Type: bool (true/false)
    medusa_role_docker_image_pull: true

    # Type: string
    medusa_role_docker_image_tag: "latest"

    # Type: string
    medusa_role_docker_image_repo: "lscr.io/linuxserver/medusa"

    # Type: string
    medusa_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='medusa') }}:{{ lookup('role_var', '_docker_image_tag', role='medusa') }}"

    # Envs
    # Type: dict
    medusa_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"
      UMASK: "002"

    # Type: dict
    medusa_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    medusa_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='medusa') }}:/config"
      - "/opt/scripts:/scripts"
      - "/mnt/unionfs/Media/TV:/tv"

    # Type: list
    medusa_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    medusa_role_docker_hostname: "{{ medusa_name }}"

    # Networks
    # Type: string
    medusa_role_docker_networks_alias: "{{ medusa_name }}"

    # Type: list
    medusa_role_docker_networks_default: []

    # Type: list
    medusa_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    medusa_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    medusa_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    medusa_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    medusa_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    medusa_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    medusa_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    medusa_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    medusa_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    medusa_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    medusa_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    medusa_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    medusa_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    medusa_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    medusa_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    medusa_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    medusa_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    medusa_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    medusa_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    medusa_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        medusa_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "medusa2.{{ user.domain }}"
          - "medusa.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        medusa_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'medusa2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

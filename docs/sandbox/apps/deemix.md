---
hide:
  - tags
tags:
  - deemix
  - media
  - music
---

# deemix

## What is it?

[deemix](https://deemix.app/) is a barebone deezer downloader library built from the ashes of Deezloader Remix.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://deemix.app/){: .header-icons } | [:octicons-link-16: Docs](https://gitlab.com/Bockiii/deemix-docker){: .header-icons } | [:octicons-mark-github-16: Github](https://gitlab.com/Bockiii/deemix-docker){: .header-icons } | [:material-docker: Docker](https://gitlab.com/Bockiii/deemix-docker){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-deemix

```

### 2. URL

- To access deemix, visit `https://deemix._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        deemix_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    deemix_name: deemix

    ```

??? example "Paths"

    ```yaml
    # Type: string
    deemix_role_paths_folder: "{{ deemix_name }}"

    # Type: string
    deemix_role_paths_location: "{{ server_appdata_path }}/{{ deemix_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    deemix_role_web_subdomain: "{{ deemix_name }}"

    # Type: string
    deemix_role_web_domain: "{{ user.domain }}"

    # Type: string
    deemix_role_web_port: "6595"

    # Type: string
    deemix_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='deemix') + '.' + lookup('role_var', '_web_domain', role='deemix')
                          if (lookup('role_var', '_web_subdomain', role='deemix') | length > 0)
                          else lookup('role_var', '_web_domain', role='deemix')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    deemix_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='deemix') }}"

    # Type: string
    deemix_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='deemix') }}"

    # Type: bool (true/false)
    deemix_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    deemix_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    deemix_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    deemix_role_traefik_middleware_custom: ""

    # Type: string
    deemix_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    deemix_role_traefik_enabled: true

    # Type: bool (true/false)
    deemix_role_traefik_api_enabled: false

    # Type: string
    deemix_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    deemix_role_docker_container: "{{ deemix_name }}"

    # Image
    # Type: bool (true/false)
    deemix_role_docker_image_pull: true

    # Type: string
    deemix_role_docker_image_repo: "registry.gitlab.com/bockiii/deemix-docker"

    # Type: string
    deemix_role_docker_image_tag: "latest"

    # Type: string
    deemix_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='deemix') }}:{{ lookup('role_var', '_docker_image_tag', role='deemix') }}"

    # Envs
    # Type: dict
    deemix_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"
      UMASK_SET: "022"
      REVERSEPROXY: "true"

    # Type: dict
    deemix_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    deemix_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='deemix') }}:/config"

    # Type: list
    deemix_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    deemix_role_docker_hostname: "{{ deemix_name }}"

    # Networks
    # Type: string
    deemix_role_docker_networks_alias: "{{ deemix_name }}"

    # Type: list
    deemix_role_docker_networks_default: []

    # Type: list
    deemix_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    deemix_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    deemix_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    deemix_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    deemix_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    deemix_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    deemix_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    deemix_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    deemix_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    deemix_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    deemix_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    deemix_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    deemix_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    deemix_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    deemix_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    deemix_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    deemix_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    deemix_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    deemix_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    deemix_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        deemix_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "deemix2.{{ user.domain }}"
          - "deemix.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        deemix_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'deemix2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

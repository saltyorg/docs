---
hide:
  - tags
tags:
  - embystat
  - statistics
  - monitoring
---

# EmbyStat

## What is it?

[EmbyStat](https://github.com/mregni/EmbyStat/) is a personal web server that can calculate all kinds of statistics from your (local) Emby or Jellyfin server. Just install this on your server and let him calculate all kinds of fun stuff.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/mregni/EmbyStat/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/mregni/EmbyStat/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/mregni/EmbyStat/){: .header-icons } | [:material-docker: Docker](https://registry.hub.docker.com/r/uping/embystat){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-embystat

```

### 2. URL

- To access EmbyStat, visit `https://embystat.xDOMAIN_NAMEx`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        embystat_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `embystat_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `embystat_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    embystat_name: embystat

    ```

??? example "Paths"

    ```yaml
    # Type: string
    embystat_role_paths_folder: "{{ embystat_name }}"

    # Type: string
    embystat_role_paths_location: "{{ server_appdata_path }}/{{ embystat_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    embystat_role_web_subdomain: "{{ embystat_name }}"

    # Type: string
    embystat_role_web_domain: "{{ user.domain }}"

    # Type: string
    embystat_role_web_port: "6555"

    # Type: string
    embystat_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='embystat') + '.' + lookup('role_var', '_web_domain', role='embystat')
                            if (lookup('role_var', '_web_subdomain', role='embystat') | length > 0)
                            else lookup('role_var', '_web_domain', role='embystat')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    embystat_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='embystat') }}"

    # Type: string
    embystat_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='embystat') }}"

    # Type: bool (true/false)
    embystat_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    embystat_role_traefik_sso_middleware: ""

    # Type: string
    embystat_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    embystat_role_traefik_middleware_custom: ""

    # Type: string
    embystat_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    embystat_role_traefik_enabled: true

    # Type: bool (true/false)
    embystat_role_traefik_api_enabled: false

    # Type: string
    embystat_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    embystat_role_docker_container: "{{ embystat_name }}"

    # Image
    # Type: bool (true/false)
    embystat_role_docker_image_pull: true

    # Type: string
    embystat_role_docker_image_repo: "uping/embystat"

    # Type: string
    embystat_role_docker_image_tag: "beta-linux-x64"

    # Type: string
    embystat_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='embystat') }}:{{ lookup('role_var', '_docker_image_tag', role='embystat') }}"

    # Volumes
    # Type: list
    embystat_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='embystat') }}/config:/app/data"

    # Type: list
    embystat_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    embystat_role_docker_hostname: "{{ embystat_name }}"

    # Networks
    # Type: string
    embystat_role_docker_networks_alias: "{{ embystat_name }}"

    # Type: list
    embystat_role_docker_networks_default: []

    # Type: list
    embystat_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    embystat_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    embystat_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    embystat_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    embystat_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    embystat_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    embystat_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    embystat_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    embystat_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    embystat_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    embystat_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    embystat_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    embystat_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    embystat_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    embystat_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    embystat_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    embystat_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    embystat_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    embystat_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    embystat_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        embystat_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "embystat2.{{ user.domain }}"
          - "embystat.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        embystat_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'embystat2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

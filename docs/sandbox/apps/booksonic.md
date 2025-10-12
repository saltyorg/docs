---
hide:
  - tags
tags:
  - booksonic
  - audiobooks
  - streaming
---

# Booksonic Air

!!! warning
    The upstream Booksonic Docker image has been deprecated and is no longer receiving updates. This means the image is not receiving regular security package updates. The role may be dropped from Sandbox at some point in the future.

## What is it?

[Booksonic Air](http://booksonic.org/) is a platform for accessing the audibooks you own wherever you are. At the moment the platform consists of Booksonic Air - A server for streaming your audiobooks, successor to the original Booksonic server and based on Airsonic. Booksonic App - An DSub based Android app for connection to Booksonic-Air servers.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://booksonic.org/){: .header-icons } | [:octicons-link-16: Docs](https://booksonic.org/how){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/popeen/Booksonic-Air){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/booksonic-air){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-booksonic

```

### 2. URL

- To access Booksonic Air, visit `https://booksonic._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        booksonic_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `booksonic_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `booksonic_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    booksonic_name: booksonic

    ```

??? example "Paths"

    ```yaml
    # Type: string
    booksonic_role_paths_folder: "{{ booksonic_name }}"

    # Type: string
    booksonic_role_paths_location: "{{ server_appdata_path }}/{{ booksonic_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    booksonic_role_web_subdomain: "{{ booksonic_name }}"

    # Type: string
    booksonic_role_web_domain: "{{ user.domain }}"

    # Type: string
    booksonic_role_web_port: "4040"

    # Type: string
    booksonic_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='booksonic') + '.' + lookup('role_var', '_web_domain', role='booksonic')
                             if (lookup('role_var', '_web_subdomain', role='booksonic') | length > 0)
                             else lookup('role_var', '_web_domain', role='booksonic')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    booksonic_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='booksonic') }}"

    # Type: string
    booksonic_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='booksonic') }}"

    # Type: bool (true/false)
    booksonic_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    booksonic_role_traefik_sso_middleware: ""

    # Type: string
    booksonic_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    booksonic_role_traefik_middleware_custom: ""

    # Type: string
    booksonic_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    booksonic_role_traefik_enabled: true

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    booksonic_role_docker_container: "{{ booksonic_name }}"

    # Image
    # Type: bool (true/false)
    booksonic_role_docker_image_pull: true

    # Type: string
    booksonic_role_docker_image_repo: "lscr.io/linuxserver/booksonic-air"

    # Type: string
    booksonic_role_docker_image_tag: "2201.1.0"

    # Type: string
    booksonic_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='booksonic') }}:{{ lookup('role_var', '_docker_image_tag', role='booksonic') }}"

    # Ports
    # Type: list
    booksonic_role_docker_ports_defaults: []

    # Type: list
    booksonic_role_docker_ports_custom: []

    # Envs
    # Type: dict
    booksonic_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"
      JAVA_OPTS: "-Dserver.use-forward-headers=true"

    # Type: dict
    booksonic_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    booksonic_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='booksonic') }}:/config"
      - "/mnt/unionfs/Media/Audiobooks:/audiobooks"
      - "/mnt/unionfs/Media/Podcasts:/podcasts"
      - "/mnt/unionfs/Media:/othermedia"

    # Type: list
    booksonic_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    booksonic_role_docker_hostname: "{{ booksonic_name }}"

    # Networks
    # Type: string
    booksonic_role_docker_networks_alias: "{{ booksonic_name }}"

    # Type: list
    booksonic_role_docker_networks_default: []

    # Type: list
    booksonic_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    booksonic_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    booksonic_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    booksonic_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    booksonic_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    booksonic_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    booksonic_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    booksonic_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    booksonic_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    booksonic_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    booksonic_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    booksonic_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    booksonic_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    booksonic_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    booksonic_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    booksonic_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    booksonic_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    booksonic_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    booksonic_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    booksonic_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        booksonic_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "booksonic2.{{ user.domain }}"
          - "booksonic.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        booksonic_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'booksonic2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
hide:
  - tags
tags:
  - rdtclient
  - download
  - client
---

# rdtclient

## THIS DOCUMENTATION IS NOT YET COMPLETED

## What is it?

[rdtclient](https://rdtclient.url) is a...

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://rdtclient.url){: .header-icons } | [:octicons-link-16: Docs](https://rdtclient.docs.url){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/rdtclient/rdtclient){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/rdtclient/rdtclient){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-rdtclient

```

### 2. URL

- To access rdtclient, visit `https://rdtclient._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        rdtclient_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    rdtclient_name: rdtclient

    ```

??? example "Paths"

    ```yaml
    # Type: string
    rdtclient_role_paths_folder: "{{ rdtclient_name }}"

    # Type: string
    rdtclient_role_paths_location: "{{ server_appdata_path }}/{{ rdtclient_role_paths_folder }}"

    # Type: string
    rdtclient_role_paths_config_location: "{{ rdtclient_role_paths_location }}/config"

    # Type: string
    rdtclient_role_paths_db_location: "{{ rdtclient_role_paths_location }}/db"

    # Type: string
    rdtclient_role_paths_downloads_location: "/mnt/unionfs/downloads/torrents/rdtclient"

    ```

??? example "Web"

    ```yaml
    # Type: string
    rdtclient_role_web_subdomain: "{{ rdtclient_name }}"

    # Type: string
    rdtclient_role_web_domain: "{{ user.domain }}"

    # Type: string
    rdtclient_role_web_port: "6500"

    # Type: string
    rdtclient_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='rdtclient') + '.' + lookup('role_var', '_web_domain', role='rdtclient')
                             if (lookup('role_var', '_web_subdomain', role='rdtclient') | length > 0)
                             else lookup('role_var', '_web_domain', role='rdtclient')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    rdtclient_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='rdtclient') }}"

    # Type: string
    rdtclient_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='rdtclient') }}"

    # Type: bool (true/false)
    rdtclient_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    rdtclient_role_traefik_sso_middleware: ""

    # Type: string
    rdtclient_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    rdtclient_role_traefik_middleware_custom: ""

    # Type: string
    rdtclient_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    rdtclient_role_traefik_enabled: true

    # Type: bool (true/false)
    rdtclient_role_traefik_api_enabled: false

    # Type: string
    rdtclient_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    rdtclient_role_docker_container: "{{ rdtclient_name }}"

    # Image
    # Type: bool (true/false)
    rdtclient_role_docker_image_pull: true

    # Type: string
    rdtclient_role_docker_image_tag: "latest"

    # Type: string
    rdtclient_role_docker_image_repo: "rogerfar/rdtclient"

    # Type: string
    rdtclient_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='rdtclient') }}:{{ lookup('role_var', '_docker_image_tag', role='rdtclient') }}"

    # Envs
    # Type: dict
    rdtclient_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    rdtclient_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    rdtclient_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='rdtclient') }}:/data"
      - "{{ lookup('role_var', '_paths_config_location', role='rdtclient') }}:/data/config"
      - "{{ lookup('role_var', '_paths_db_location', role='rdtclient') }}:/data/db"
      - "{{ lookup('role_var', '_paths_downloads_location', role='rdtclient') }}:/data/downloads"

    # Type: list
    rdtclient_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    rdtclient_role_docker_hostname: "{{ rdtclient_name }}"

    # Networks
    # Type: string
    rdtclient_role_docker_networks_alias: "{{ rdtclient_name }}"

    # Type: list
    rdtclient_role_docker_networks_default: []

    # Type: list
    rdtclient_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    rdtclient_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    rdtclient_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    rdtclient_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    rdtclient_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    rdtclient_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    rdtclient_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    rdtclient_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    rdtclient_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    rdtclient_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    rdtclient_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    rdtclient_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    rdtclient_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    rdtclient_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    rdtclient_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    rdtclient_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    rdtclient_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    rdtclient_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    rdtclient_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    rdtclient_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        rdtclient_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "rdtclient2.{{ user.domain }}"
          - "rdtclient.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        rdtclient_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'rdtclient2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

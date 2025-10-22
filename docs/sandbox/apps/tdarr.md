---
hide:
  - tags
tags:
  - tdarr
  - media
  - encoding
---

# Tdarr

## What is it?

[Tdarr](https://tdarr.io/) is a cross-platform conditional based transcoding application for automating media library transcode/remux management in order to process your media files as required. For example, you can set rules for the required codecs, containers, languages etc that your media should have which helps keeps things organized and can increase compatability with your devices. A common use for Tdarr is to simply convert video files from h264 to h265 (hevc), saving 40%-50% in size.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://tdarr.io/){: .header-icons } | [:octicons-link-16: Docs](https://docs.tdarr.io/docs/welcome/what/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/HaveAGitGat/Tdarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/haveagitgat/tdarr){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-tdarr

```

### 2. URL

- To access Tdarr, visit `https://tdarr.xDOMAIN_NAMEx`

### 3. Setup

Tdarr is configured with the following defaults which can be modified via the inventory system.

``` yaml
tdarr_server_port: "8266"
tdarr_server_external: false
```

By switching `tdarr_server_external` to `true` the Tdarr server will be accessible externally via the specified `tdarr_server_port` on any hostname or IP address pointing directly to the server.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        tdarr_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `tdarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `tdarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    tdarr_name: tdarr

    ```

??? example "Settings"

    ```yaml
    # Type: string
    tdarr_role_server_port: "8266"

    # Type: bool (true/false)
    tdarr_role_server_external: false

    ```

??? example "Paths"

    ```yaml
    # Type: string
    tdarr_role_paths_folder: "{{ tdarr_name }}"

    # Type: string
    tdarr_role_paths_location: "{{ server_appdata_path }}/{{ tdarr_role_paths_folder }}"

    # Type: string
    tdarr_role_paths_server_location: "{{ tdarr_role_paths_location }}/server"

    # Type: string
    tdarr_role_paths_configs_location: "{{ tdarr_role_paths_location }}/configs"

    # Type: string
    tdarr_role_paths_logs_location: "{{ tdarr_role_paths_location }}/logs"

    # Type: string
    tdarr_role_paths_transcodes_location: "{{ transcodes_path }}/{{ tdarr_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    tdarr_role_web_subdomain: "{{ tdarr_name }}"

    # Type: string
    tdarr_role_web_domain: "{{ user.domain }}"

    # Type: string
    tdarr_role_web_port: "8265"

    # Type: string
    tdarr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='tdarr') + '.' + lookup('role_var', '_web_domain', role='tdarr')
                         if (lookup('role_var', '_web_subdomain', role='tdarr') | length > 0)
                         else lookup('role_var', '_web_domain', role='tdarr')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    tdarr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='tdarr') }}"

    # Type: string
    tdarr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='tdarr') }}"

    # Type: bool (true/false)
    tdarr_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    tdarr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    tdarr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    tdarr_role_traefik_middleware_custom: ""

    # Type: string
    tdarr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    tdarr_role_traefik_enabled: true

    # Type: bool (true/false)
    tdarr_role_traefik_api_enabled: false

    # Type: string
    tdarr_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    tdarr_role_docker_container: "{{ tdarr_name }}"

    # Image
    # Type: bool (true/false)
    tdarr_role_docker_image_pull: true

    # Type: string
    tdarr_role_docker_image_repo: "haveagitgat/tdarr"

    # Type: string
    tdarr_role_docker_image_tag: "latest"

    # Type: string
    tdarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='tdarr') }}:{{ lookup('role_var', '_docker_image_tag', role='tdarr') }}"

    # Ports
    # Type: list
    tdarr_role_docker_ports_defaults: 
      - "{{ lookup('role_var', '_server_port', role='tdarr') }}:{{ lookup('role_var', '_server_port', role='tdarr') }}"

    # Type: list
    tdarr_role_docker_ports_custom: []

    # Envs
    # Type: dict
    tdarr_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"
      serverIP: "0.0.0.0"
      webUIPort: "8265"
      serverPort: "{{ lookup('role_var', '_server_port', role='tdarr') }}"
      internalNode: "true"
      inContainer: "true"

    # Type: dict
    tdarr_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    tdarr_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_configs_location', role='tdarr') }}:/app/configs"
      - "{{ lookup('role_var', '_paths_server_location', role='tdarr') }}:/app/server"
      - "{{ lookup('role_var', '_paths_logs_location', role='tdarr') }}:/app/logs"
      - "{{ lookup('role_var', '_paths_transcodes_location', role='tdarr') }}:/temp"
      - "/mnt/unionfs/Media:/media"
      - "/mnt/unionfs/Media/Movies:/movies"
      - "/mnt/unionfs/Media/TV:/tv"
      - "/dev/shm:/dev/shm"

    # Type: list
    tdarr_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    tdarr_role_docker_hostname: "{{ tdarr_name }}"

    # Networks
    # Type: string
    tdarr_role_docker_networks_alias: "{{ tdarr_name }}"

    # Type: list
    tdarr_role_docker_networks_default: []

    # Type: list
    tdarr_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    tdarr_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    tdarr_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    tdarr_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    tdarr_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    tdarr_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    tdarr_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    tdarr_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    tdarr_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    tdarr_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    tdarr_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    tdarr_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    tdarr_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    tdarr_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    tdarr_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    tdarr_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    tdarr_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    tdarr_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    tdarr_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    tdarr_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        tdarr_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "tdarr2.{{ user.domain }}"
          - "tdarr.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        tdarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'tdarr2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

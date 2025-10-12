---
hide:
  - tags
tags:
  - threadfin
  - iptv
  - streaming
---

# Threadfin

## What is it?

[Threadfin](https://github.com/Threadfin/Threadfin) is a M3U proxy server for Plex, Emby and any client and provider which supports the .TS and .M3U8 (HLS) streaming formats.

Threadfin emulates a SiliconDust HDHomeRun OTA tuner, which allows it to expose IPTV style channels to software, which would not normally support it. It is based on xTeve.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/Threadfin/Threadfin){: .header-icons } | [:octicons-link-16: Docs](https://github.com/Threadfin/Threadfin){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Threadfin/Threadfin){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/fyb3roptik/threadfin){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-threadfin

```

### 2. URL

- To access Threadfin, visit `https://threadfin._yourdomain.com_/web`

### 3. Setup

- Access Threadfin web GUI at `https://threadfin._yourdomain.com_/web`

- Run through the Configuration Wizard.

- Use the following URLs when configuring your media server (e.g. Plex, Emby, Jellyfin)

  - HDHomerun Device Address (Plex) `http://threadfin:34400`

  - Playlist (Emby, Jellyfin) `http://threadfin:34400/m3u/threadfin.m3u`

  - EPG (all) `http://threadfin:34400/xmltv/threadfin.xml`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        threadfin_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `threadfin_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `threadfin_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    threadfin_name: threadfin

    ```

??? example "Paths"

    ```yaml
    # Type: string
    threadfin_role_paths_folder: "{{ threadfin_name }}"

    # Type: string
    threadfin_role_paths_location: "{{ server_appdata_path }}/{{ threadfin_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    threadfin_role_web_subdomain: "{{ threadfin_name }}"

    # Type: string
    threadfin_role_web_domain: "{{ user.domain }}"

    # Type: string
    threadfin_role_web_port: "34400"

    # Type: string
    threadfin_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='threadfin') + '.' + lookup('role_var', '_web_domain', role='threadfin')
                             if (lookup('role_var', '_web_subdomain', role='threadfin') | length > 0)
                             else lookup('role_var', '_web_domain', role='threadfin')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    threadfin_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='threadfin') }}"

    # Type: string
    threadfin_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='threadfin') }}"

    # Type: bool (true/false)
    threadfin_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    threadfin_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    threadfin_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    threadfin_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    threadfin_role_traefik_enabled: true

    # Type: bool (true/false)
    threadfin_role_traefik_api_enabled: true

    # Type: string
    threadfin_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/images`) || PathPrefix(`/data_images`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    threadfin_role_docker_container: "{{ threadfin_name }}"

    # Image
    # Type: bool (true/false)
    threadfin_role_docker_image_pull: true

    # Type: string
    threadfin_role_docker_image_repo: "fyb3roptik/threadfin"

    # Type: string
    threadfin_role_docker_image_tag: "latest"

    # Type: string
    threadfin_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='threadfin') }}:{{ lookup('role_var', '_docker_image_tag', role='threadfin') }}"

    # Envs
    # Type: dict
    threadfin_role_docker_envs_default: 
      TZ: "{{ tz }}"
      THREADFIN_BRANCH: "main"
      THREADFIN_DEBUG: "0"

    # Type: dict
    threadfin_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    threadfin_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='threadfin') }}:/home/threadfin/conf"

    # Type: list
    threadfin_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    threadfin_role_docker_hostname: "{{ threadfin_name }}"

    # Networks
    # Type: string
    threadfin_role_docker_networks_alias: "{{ threadfin_name }}"

    # Type: list
    threadfin_role_docker_networks_default: []

    # Type: list
    threadfin_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    threadfin_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    threadfin_role_docker_state: started

    # User
    # Type: string
    threadfin_role_docker_user: "{{ uid }}:{{ gid }}"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    threadfin_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    threadfin_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    threadfin_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    threadfin_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    threadfin_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    threadfin_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    threadfin_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    threadfin_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    threadfin_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    threadfin_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    threadfin_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    threadfin_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    threadfin_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    threadfin_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    threadfin_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    threadfin_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    threadfin_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        threadfin_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "threadfin2.{{ user.domain }}"
          - "threadfin.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        threadfin_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'threadfin2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

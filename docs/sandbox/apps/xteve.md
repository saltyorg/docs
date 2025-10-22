---
hide:
  - tags
tags:
  - xteve
  - iptv
  - streaming
---

# xTeVe

## What is it?

[xTeVe](https://github.com/xteve-project/xTeVe) is a M3U proxy server for Plex, Emby and any client and provider which supports the .TS and .M3U8 (HLS) streaming formats.

xTeVe emulates a SiliconDust HDHomeRun OTA tuner, which allows it to expose IPTV style channels to software, which would not normally support it. This Docker image includes the following packages and features:

- xTeVe v2.1 (Linux) x86 64 bit

- Latest Guide2go (Linux) x86 64 bit (Schedules Direct XMLTV grabber)

- Zap2XML Support (Perl based zap2it / TVguide.com XMLTV grabber)

- Bash, Perl & crond Support

- VLC & ffmpeg Support

- Automated XMLTV Guide Lineups & Cron’s

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/xteve-project/xTeVe){: .header-icons } | [:octicons-link-16: Docs](https://github.com/xteve-project/xTeVe-Documentation/blob/master/en/configuration.md){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/xteve-project/xTeVe){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/dnsforge/xteve){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-xteve

```

### 2. URL

- To access xTeVe, visit `https://ROLENAME.xDOMAIN_NAMEx/web`

### 3. Setup

- Access xTeVe web GUI, visit `https://ROLENAME.xDOMAIN_NAMEx/web`

- Run through the Configuration Wizard.

- Use the following URLs when configuring your media server (e.g. Plex, Emby, Jellyfin)

    * HDHomerun Device Address (Plex) `http://xteve:34400`

    * Playlist (Emby, Jellyfin) `http://xteve:34400/m3u/xteve.m3u`

    * EPG (all) `http://xteve:34400/xmltv/xteve.xml`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        xteve_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `xteve_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `xteve_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    xteve_name: xteve

    ```

??? example "Paths"

    ```yaml
    # Type: string
    xteve_role_paths_folder: "{{ xteve_name }}"

    # Type: string
    xteve_role_paths_location: "{{ server_appdata_path }}/{{ xteve_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    xteve_role_web_subdomain: "{{ xteve_name }}"

    # Type: string
    xteve_role_web_domain: "{{ user.domain }}"

    # Type: string
    xteve_role_web_port: "34400"

    # Type: string
    xteve_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='xteve') + '.' + lookup('role_var', '_web_domain', role='xteve')
                         if (lookup('role_var', '_web_subdomain', role='xteve') | length > 0)
                         else lookup('role_var', '_web_domain', role='xteve')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    xteve_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='xteve') }}"

    # Type: string
    xteve_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='xteve') }}"

    # Type: bool (true/false)
    xteve_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    xteve_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    xteve_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    xteve_role_traefik_middleware_custom: ""

    # Type: string
    xteve_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    xteve_role_traefik_enabled: true

    # Type: bool (true/false)
    xteve_role_traefik_api_enabled: true

    # Type: string
    xteve_role_traefik_api_endpoint: "PathPrefix(`/data_images`) || PathPrefix(`/api`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    xteve_role_docker_container: "{{ xteve_name }}"

    # Image
    # Type: bool (true/false)
    xteve_role_docker_image_pull: true

    # Type: string
    xteve_role_docker_image_repo: "dnsforge/xteve"

    # Type: string
    xteve_role_docker_image_tag: "latest"

    # Type: string
    xteve_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='xteve') }}:{{ lookup('role_var', '_docker_image_tag', role='xteve') }}"

    # Envs
    # Type: dict
    xteve_role_docker_envs_default: 
      TZ: "{{ tz }}"
      XTEVE_BRANCH: "beta"
      XTEVE_UID: "{{ uid }}"
      XTEVE_GID: "{{ gid }}"
      XTEVE_API: "1"

    # Type: dict
    xteve_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    xteve_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='xteve') }}/app/config:/home/xteve/conf"
      - "{{ lookup('role_var', '_paths_location', role='xteve') }}/app/tmp:/tmp/xteve"
      - "{{ lookup('role_var', '_paths_location', role='xteve') }}/app/guide2go:/home/xteve/guide2go/conf"

    # Type: list
    xteve_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    xteve_role_docker_hostname: "{{ xteve_name }}"

    # Networks
    # Type: string
    xteve_role_docker_networks_alias: "{{ xteve_name }}"

    # Type: list
    xteve_role_docker_networks_default: []

    # Type: list
    xteve_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    xteve_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    xteve_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    xteve_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    xteve_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    xteve_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    xteve_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    xteve_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    xteve_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    xteve_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    xteve_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    xteve_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    xteve_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    xteve_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    xteve_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    xteve_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    xteve_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    xteve_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    xteve_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    xteve_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        xteve_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "xteve2.{{ user.domain }}"
          - "xteve.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        xteve_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'xteve2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

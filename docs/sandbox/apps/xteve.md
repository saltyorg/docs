---
icon: material/docker
hide:
  - tags
tags:
  - xteve
  - iptv
  - streaming
---

# xTeVe

## Overview

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

```shell
sb install sandbox-xteve
```

### 2. URL

- To access xTeVe, visit <https://ROLENAME.iYOUR_DOMAIN_NAMEi/web>

### 3. Setup

- Access xTeVe web GUI, visit <https://ROLENAME.iYOUR_DOMAIN_NAMEi/web>

- Run through the Configuration Wizard.

- Use the following URLs when configuring your media server (e.g. Plex, Emby, Jellyfin)

    * HDHomerun Device Address (Plex) `http://xteve:34400`

    * Playlist (Emby, Jellyfin) `http://xteve:34400/m3u/xteve.m3u`

    * EPG (all) `http://xteve:34400/xmltv/xteve.xml`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    xteve_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `xteve_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `xteve_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`xteve_name`"

        ```yaml
        # Type: string
        xteve_name: xteve
        ```

=== "Paths"

    ??? variable string "`xteve_role_paths_folder`"

        ```yaml
        # Type: string
        xteve_role_paths_folder: "{{ xteve_name }}"
        ```

    ??? variable string "`xteve_role_paths_location`"

        ```yaml
        # Type: string
        xteve_role_paths_location: "{{ server_appdata_path }}/{{ xteve_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`xteve_role_web_subdomain`"

        ```yaml
        # Type: string
        xteve_role_web_subdomain: "{{ xteve_name }}"
        ```

    ??? variable string "`xteve_role_web_domain`"

        ```yaml
        # Type: string
        xteve_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`xteve_role_web_port`"

        ```yaml
        # Type: string
        xteve_role_web_port: "34400"
        ```

    ??? variable string "`xteve_role_web_url`"

        ```yaml
        # Type: string
        xteve_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='xteve') + '.' + lookup('role_var', '_web_domain', role='xteve')
                             if (lookup('role_var', '_web_subdomain', role='xteve') | length > 0)
                             else lookup('role_var', '_web_domain', role='xteve')) }}"
        ```

=== "DNS"

    ??? variable string "`xteve_role_dns_record`"

        ```yaml
        # Type: string
        xteve_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='xteve') }}"
        ```

    ??? variable string "`xteve_role_dns_zone`"

        ```yaml
        # Type: string
        xteve_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='xteve') }}"
        ```

    ??? variable bool "`xteve_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        xteve_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`xteve_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        xteve_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`xteve_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        xteve_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`xteve_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        xteve_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`xteve_role_traefik_certresolver`"

        ```yaml
        # Type: string
        xteve_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`xteve_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        xteve_role_traefik_enabled: true
        ```

    ??? variable bool "`xteve_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        xteve_role_traefik_api_enabled: true
        ```

    ??? variable string "`xteve_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        xteve_role_traefik_api_endpoint: "PathPrefix(`/data_images`) || PathPrefix(`/api`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`xteve_role_docker_container`"

        ```yaml
        # Type: string
        xteve_role_docker_container: "{{ xteve_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`xteve_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        xteve_role_docker_image_pull: true
        ```

    ??? variable string "`xteve_role_docker_image_repo`"

        ```yaml
        # Type: string
        xteve_role_docker_image_repo: "dnsforge/xteve"
        ```

    ??? variable string "`xteve_role_docker_image_tag`"

        ```yaml
        # Type: string
        xteve_role_docker_image_tag: "latest"
        ```

    ??? variable string "`xteve_role_docker_image`"

        ```yaml
        # Type: string
        xteve_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='xteve') }}:{{ lookup('role_var', '_docker_image_tag', role='xteve') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`xteve_role_docker_envs_default`"

        ```yaml
        # Type: dict
        xteve_role_docker_envs_default:
          TZ: "{{ tz }}"
          XTEVE_BRANCH: "beta"
          XTEVE_UID: "{{ uid }}"
          XTEVE_GID: "{{ gid }}"
          XTEVE_API: "1"
        ```

    ??? variable dict "`xteve_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        xteve_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`xteve_role_docker_volumes_default`"

        ```yaml
        # Type: list
        xteve_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='xteve') }}/app/config:/home/xteve/conf"
          - "{{ lookup('role_var', '_paths_location', role='xteve') }}/app/tmp:/tmp/xteve"
          - "{{ lookup('role_var', '_paths_location', role='xteve') }}/app/guide2go:/home/xteve/guide2go/conf"
        ```

    ??? variable list "`xteve_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        xteve_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`xteve_role_docker_hostname`"

        ```yaml
        # Type: string
        xteve_role_docker_hostname: "{{ xteve_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`xteve_role_docker_networks_alias`"

        ```yaml
        # Type: string
        xteve_role_docker_networks_alias: "{{ xteve_name }}"
        ```

    ??? variable list "`xteve_role_docker_networks_default`"

        ```yaml
        # Type: list
        xteve_role_docker_networks_default: []
        ```

    ??? variable list "`xteve_role_docker_networks_custom`"

        ```yaml
        # Type: list
        xteve_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`xteve_role_docker_restart_policy`"

        ```yaml
        # Type: string
        xteve_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`xteve_role_docker_state`"

        ```yaml
        # Type: string
        xteve_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`xteve_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        xteve_role_autoheal_enabled: true
        ```

    ??? variable string "`xteve_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        xteve_role_depends_on: ""
        ```

    ??? variable string "`xteve_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        xteve_role_depends_on_delay: "0"
        ```

    ??? variable string "`xteve_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        xteve_role_depends_on_healthchecks:
        ```

    ??? variable bool "`xteve_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        xteve_role_diun_enabled: true
        ```

    ??? variable bool "`xteve_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        xteve_role_dns_enabled: true
        ```

    ??? variable bool "`xteve_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        xteve_role_docker_controller: true
        ```

    ??? variable bool "`xteve_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        xteve_role_docker_volumes_download:
        ```

    ??? variable bool "`xteve_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        xteve_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`xteve_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        xteve_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`xteve_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        xteve_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`xteve_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        xteve_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`xteve_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        xteve_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`xteve_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        xteve_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`xteve_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        xteve_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`xteve_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        xteve_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`xteve_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        xteve_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`xteve_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        xteve_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            xteve_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "xteve2.{{ user.domain }}"
              - "xteve.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`xteve_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        xteve_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            xteve_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'xteve2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`xteve_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        xteve_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
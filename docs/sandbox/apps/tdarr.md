---
icon: material/docker
hide:
  - tags
tags:
  - tdarr
  - media
  - encoding
---

# Tdarr

## Overview

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

- To access Tdarr, visit <https://tdarr.iYOUR_DOMAIN_NAMEi>

### 3. Setup

Tdarr is configured with the following defaults which can be modified via the inventory system.

``` yaml
tdarr_server_port: "8266"
tdarr_server_external: false
```

By switching `tdarr_server_external` to `true` the Tdarr server will be accessible externally via the specified `tdarr_server_port` on any hostname or IP address pointing directly to the server.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    tdarr_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `tdarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `tdarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`tdarr_name`"

        ```yaml
        # Type: string
        tdarr_name: tdarr
        ```

=== "Settings"

    ??? variable string "`tdarr_role_server_port`"

        ```yaml
        # Type: string
        tdarr_role_server_port: "8266"
        ```

    ??? variable bool "`tdarr_role_server_external`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_server_external: false
        ```

=== "Paths"

    ??? variable string "`tdarr_role_paths_folder`"

        ```yaml
        # Type: string
        tdarr_role_paths_folder: "{{ tdarr_name }}"
        ```

    ??? variable string "`tdarr_role_paths_location`"

        ```yaml
        # Type: string
        tdarr_role_paths_location: "{{ server_appdata_path }}/{{ tdarr_role_paths_folder }}"
        ```

    ??? variable string "`tdarr_role_paths_server_location`"

        ```yaml
        # Type: string
        tdarr_role_paths_server_location: "{{ tdarr_role_paths_location }}/server"
        ```

    ??? variable string "`tdarr_role_paths_configs_location`"

        ```yaml
        # Type: string
        tdarr_role_paths_configs_location: "{{ tdarr_role_paths_location }}/configs"
        ```

    ??? variable string "`tdarr_role_paths_logs_location`"

        ```yaml
        # Type: string
        tdarr_role_paths_logs_location: "{{ tdarr_role_paths_location }}/logs"
        ```

    ??? variable string "`tdarr_role_paths_transcodes_location`"

        ```yaml
        # Type: string
        tdarr_role_paths_transcodes_location: "{{ transcodes_path }}/{{ tdarr_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`tdarr_role_web_subdomain`"

        ```yaml
        # Type: string
        tdarr_role_web_subdomain: "{{ tdarr_name }}"
        ```

    ??? variable string "`tdarr_role_web_domain`"

        ```yaml
        # Type: string
        tdarr_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`tdarr_role_web_port`"

        ```yaml
        # Type: string
        tdarr_role_web_port: "8265"
        ```

    ??? variable string "`tdarr_role_web_url`"

        ```yaml
        # Type: string
        tdarr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='tdarr') + '.' + lookup('role_var', '_web_domain', role='tdarr')
                             if (lookup('role_var', '_web_subdomain', role='tdarr') | length > 0)
                             else lookup('role_var', '_web_domain', role='tdarr')) }}"
        ```

=== "DNS"

    ??? variable string "`tdarr_role_dns_record`"

        ```yaml
        # Type: string
        tdarr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='tdarr') }}"
        ```

    ??? variable string "`tdarr_role_dns_zone`"

        ```yaml
        # Type: string
        tdarr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='tdarr') }}"
        ```

    ??? variable bool "`tdarr_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`tdarr_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        tdarr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`tdarr_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        tdarr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`tdarr_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        tdarr_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`tdarr_role_traefik_certresolver`"

        ```yaml
        # Type: string
        tdarr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`tdarr_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_traefik_enabled: true
        ```

    ??? variable bool "`tdarr_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_traefik_api_enabled: false
        ```

    ??? variable string "`tdarr_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        tdarr_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`tdarr_role_docker_container`"

        ```yaml
        # Type: string
        tdarr_role_docker_container: "{{ tdarr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`tdarr_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_docker_image_pull: true
        ```

    ??? variable string "`tdarr_role_docker_image_repo`"

        ```yaml
        # Type: string
        tdarr_role_docker_image_repo: "haveagitgat/tdarr"
        ```

    ??? variable string "`tdarr_role_docker_image_tag`"

        ```yaml
        # Type: string
        tdarr_role_docker_image_tag: "latest"
        ```

    ??? variable string "`tdarr_role_docker_image`"

        ```yaml
        # Type: string
        tdarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='tdarr') }}:{{ lookup('role_var', '_docker_image_tag', role='tdarr') }}"
        ```

    <h5>Ports</h5>

    ??? variable list "`tdarr_role_docker_ports_defaults`"

        ```yaml
        # Type: list
        tdarr_role_docker_ports_defaults: 
          - "{{ lookup('role_var', '_server_port', role='tdarr') }}:{{ lookup('role_var', '_server_port', role='tdarr') }}"
        ```

    ??? variable list "`tdarr_role_docker_ports_custom`"

        ```yaml
        # Type: list
        tdarr_role_docker_ports_custom: []
        ```

    <h5>Envs</h5>

    ??? variable dict "`tdarr_role_docker_envs_default`"

        ```yaml
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
        ```

    ??? variable dict "`tdarr_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        tdarr_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`tdarr_role_docker_volumes_default`"

        ```yaml
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
        ```

    ??? variable list "`tdarr_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        tdarr_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`tdarr_role_docker_hostname`"

        ```yaml
        # Type: string
        tdarr_role_docker_hostname: "{{ tdarr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`tdarr_role_docker_networks_alias`"

        ```yaml
        # Type: string
        tdarr_role_docker_networks_alias: "{{ tdarr_name }}"
        ```

    ??? variable list "`tdarr_role_docker_networks_default`"

        ```yaml
        # Type: list
        tdarr_role_docker_networks_default: []
        ```

    ??? variable list "`tdarr_role_docker_networks_custom`"

        ```yaml
        # Type: list
        tdarr_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`tdarr_role_docker_restart_policy`"

        ```yaml
        # Type: string
        tdarr_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`tdarr_role_docker_state`"

        ```yaml
        # Type: string
        tdarr_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`tdarr_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        tdarr_role_autoheal_enabled: true
        ```

    ??? variable string "`tdarr_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        tdarr_role_depends_on: ""
        ```

    ??? variable string "`tdarr_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        tdarr_role_depends_on_delay: "0"
        ```

    ??? variable string "`tdarr_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        tdarr_role_depends_on_healthchecks:
        ```

    ??? variable bool "`tdarr_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        tdarr_role_diun_enabled: true
        ```

    ??? variable bool "`tdarr_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        tdarr_role_dns_enabled: true
        ```

    ??? variable bool "`tdarr_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        tdarr_role_docker_controller: true
        ```

    ??? variable bool "`tdarr_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_docker_volumes_download:
        ```

    ??? variable bool "`tdarr_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        tdarr_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`tdarr_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        tdarr_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`tdarr_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        tdarr_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`tdarr_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        tdarr_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`tdarr_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`tdarr_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        tdarr_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`tdarr_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        tdarr_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`tdarr_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        tdarr_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`tdarr_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        tdarr_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`tdarr_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        tdarr_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            tdarr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "tdarr2.{{ user.domain }}"
              - "tdarr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`tdarr_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        tdarr_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            tdarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'tdarr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`tdarr_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        tdarr_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
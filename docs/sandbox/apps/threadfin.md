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

- To access Threadfin, visit <https://threadfin.iYOUR_DOMAIN_NAMEi/web>

### 3. Setup

- Access Threadfin web GUI at <https://threadfin.iYOUR_DOMAIN_NAMEi/web>

- Run through the Configuration Wizard.

- Use the following URLs when configuring your media server (e.g. Plex, Emby, Jellyfin)

  - HDHomerun Device Address (Plex) `http://threadfin:34400`

  - Playlist (Emby, Jellyfin) `http://threadfin:34400/m3u/threadfin.m3u`

  - EPG (all) `http://threadfin:34400/xmltv/threadfin.xml`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    threadfin_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `threadfin_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `threadfin_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`threadfin_name`"

        ```yaml
        # Type: string
        threadfin_name: threadfin
        ```

=== "Paths"

    ??? variable string "`threadfin_role_paths_folder`"

        ```yaml
        # Type: string
        threadfin_role_paths_folder: "{{ threadfin_name }}"
        ```

    ??? variable string "`threadfin_role_paths_location`"

        ```yaml
        # Type: string
        threadfin_role_paths_location: "{{ server_appdata_path }}/{{ threadfin_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`threadfin_role_web_subdomain`"

        ```yaml
        # Type: string
        threadfin_role_web_subdomain: "{{ threadfin_name }}"
        ```

    ??? variable string "`threadfin_role_web_domain`"

        ```yaml
        # Type: string
        threadfin_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`threadfin_role_web_port`"

        ```yaml
        # Type: string
        threadfin_role_web_port: "34400"
        ```

    ??? variable string "`threadfin_role_web_url`"

        ```yaml
        # Type: string
        threadfin_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='threadfin') + '.' + lookup('role_var', '_web_domain', role='threadfin')
                                 if (lookup('role_var', '_web_subdomain', role='threadfin') | length > 0)
                                 else lookup('role_var', '_web_domain', role='threadfin')) }}"
        ```

=== "DNS"

    ??? variable string "`threadfin_role_dns_record`"

        ```yaml
        # Type: string
        threadfin_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='threadfin') }}"
        ```

    ??? variable string "`threadfin_role_dns_zone`"

        ```yaml
        # Type: string
        threadfin_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='threadfin') }}"
        ```

    ??? variable bool "`threadfin_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        threadfin_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`threadfin_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        threadfin_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`threadfin_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        threadfin_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`threadfin_role_traefik_certresolver`"

        ```yaml
        # Type: string
        threadfin_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`threadfin_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        threadfin_role_traefik_enabled: true
        ```

    ??? variable bool "`threadfin_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        threadfin_role_traefik_api_enabled: true
        ```

    ??? variable string "`threadfin_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        threadfin_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/images`) || PathPrefix(`/data_images`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`threadfin_role_docker_container`"

        ```yaml
        # Type: string
        threadfin_role_docker_container: "{{ threadfin_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`threadfin_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        threadfin_role_docker_image_pull: true
        ```

    ??? variable string "`threadfin_role_docker_image_repo`"

        ```yaml
        # Type: string
        threadfin_role_docker_image_repo: "fyb3roptik/threadfin"
        ```

    ??? variable string "`threadfin_role_docker_image_tag`"

        ```yaml
        # Type: string
        threadfin_role_docker_image_tag: "latest"
        ```

    ??? variable string "`threadfin_role_docker_image`"

        ```yaml
        # Type: string
        threadfin_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='threadfin') }}:{{ lookup('role_var', '_docker_image_tag', role='threadfin') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`threadfin_role_docker_envs_default`"

        ```yaml
        # Type: dict
        threadfin_role_docker_envs_default: 
          TZ: "{{ tz }}"
          THREADFIN_BRANCH: "main"
          THREADFIN_DEBUG: "0"
        ```

    ??? variable dict "`threadfin_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        threadfin_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`threadfin_role_docker_volumes_default`"

        ```yaml
        # Type: list
        threadfin_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='threadfin') }}:/home/threadfin/conf"
        ```

    ??? variable list "`threadfin_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        threadfin_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`threadfin_role_docker_hostname`"

        ```yaml
        # Type: string
        threadfin_role_docker_hostname: "{{ threadfin_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`threadfin_role_docker_networks_alias`"

        ```yaml
        # Type: string
        threadfin_role_docker_networks_alias: "{{ threadfin_name }}"
        ```

    ??? variable list "`threadfin_role_docker_networks_default`"

        ```yaml
        # Type: list
        threadfin_role_docker_networks_default: []
        ```

    ??? variable list "`threadfin_role_docker_networks_custom`"

        ```yaml
        # Type: list
        threadfin_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`threadfin_role_docker_restart_policy`"

        ```yaml
        # Type: string
        threadfin_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`threadfin_role_docker_state`"

        ```yaml
        # Type: string
        threadfin_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`threadfin_role_docker_user`"

        ```yaml
        # Type: string
        threadfin_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`threadfin_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        threadfin_role_autoheal_enabled: true
        ```

    ??? variable string "`threadfin_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        threadfin_role_depends_on: ""
        ```

    ??? variable string "`threadfin_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        threadfin_role_depends_on_delay: "0"
        ```

    ??? variable string "`threadfin_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        threadfin_role_depends_on_healthchecks:
        ```

    ??? variable bool "`threadfin_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        threadfin_role_diun_enabled: true
        ```

    ??? variable bool "`threadfin_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        threadfin_role_dns_enabled: true
        ```

    ??? variable bool "`threadfin_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        threadfin_role_docker_controller: true
        ```

    ??? variable bool "`threadfin_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        threadfin_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`threadfin_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        threadfin_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`threadfin_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        threadfin_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`threadfin_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        threadfin_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`threadfin_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        threadfin_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`threadfin_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        threadfin_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`threadfin_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        threadfin_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`threadfin_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        threadfin_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`threadfin_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        threadfin_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`threadfin_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        threadfin_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            threadfin_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "threadfin2.{{ user.domain }}"
              - "threadfin.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`threadfin_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        threadfin_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            threadfin_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'threadfin2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`threadfin_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        threadfin_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
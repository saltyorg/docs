---
hide:
  - tags
tags:
  - makemkv
  - media
  - ripping
---

# MakeMKV

## What is it?

[MakeMKV](http://www.makemkv.com/)  is your one-click solution to convert video that you own into free and patents-unencumbered format that can be played everywhere. MakeMKV is a format converter, otherwise called "transcoder". It converts the video clips from proprietary (and usually encrypted) disc into a set of MKV files, preserving most information but not changing it in any way. The MKV format can store multiple video/audio tracks with all meta-information and preserve chapters.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](http://www.makemkv.com/){: .header-icons } | [:octicons-link-16: Docs](https://www.makemkv.com/onlinehelp/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/jlesage/docker-makemkv){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jlesage/makemkv){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-makemkv

```

### 2. URL

- To access makemkv, visit <https://makemkv.iYOUR_DOMAIN_NAMEi>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    makemkv_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `makemkv_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `makemkv_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`makemkv_name`"

        ```yaml
        # Type: string
        makemkv_name: makemkv
        ```

=== "Paths"

    ??? variable string "`makemkv_role_paths_folder`"

        ```yaml
        # Type: string
        makemkv_role_paths_folder: "{{ makemkv_name }}"
        ```

    ??? variable string "`makemkv_role_paths_location`"

        ```yaml
        # Type: string
        makemkv_role_paths_location: "{{ server_appdata_path }}/{{ makemkv_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`makemkv_role_web_subdomain`"

        ```yaml
        # Type: string
        makemkv_role_web_subdomain: "{{ makemkv_name }}"
        ```

    ??? variable string "`makemkv_role_web_domain`"

        ```yaml
        # Type: string
        makemkv_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`makemkv_role_web_port`"

        ```yaml
        # Type: string
        makemkv_role_web_port: "5800"
        ```

    ??? variable string "`makemkv_role_web_url`"

        ```yaml
        # Type: string
        makemkv_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='makemkv') + '.' + lookup('role_var', '_web_domain', role='makemkv')
                               if (lookup('role_var', '_web_subdomain', role='makemkv') | length > 0)
                               else lookup('role_var', '_web_domain', role='makemkv')) }}"
        ```

=== "DNS"

    ??? variable string "`makemkv_role_dns_record`"

        ```yaml
        # Type: string
        makemkv_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='makemkv') }}"
        ```

    ??? variable string "`makemkv_role_dns_zone`"

        ```yaml
        # Type: string
        makemkv_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='makemkv') }}"
        ```

    ??? variable bool "`makemkv_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        makemkv_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`makemkv_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        makemkv_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`makemkv_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        makemkv_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`makemkv_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        makemkv_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`makemkv_role_traefik_certresolver`"

        ```yaml
        # Type: string
        makemkv_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`makemkv_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        makemkv_role_traefik_enabled: true
        ```

    ??? variable bool "`makemkv_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        makemkv_role_traefik_api_enabled: false
        ```

    ??? variable string "`makemkv_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        makemkv_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`makemkv_role_docker_container`"

        ```yaml
        # Type: string
        makemkv_role_docker_container: "{{ makemkv_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`makemkv_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        makemkv_role_docker_image_pull: true
        ```

    ??? variable string "`makemkv_role_docker_image_tag`"

        ```yaml
        # Type: string
        makemkv_role_docker_image_tag: "latest"
        ```

    ??? variable string "`makemkv_role_docker_image_repo`"

        ```yaml
        # Type: string
        makemkv_role_docker_image_repo: "jlesage/makemkv"
        ```

    ??? variable string "`makemkv_role_docker_image`"

        ```yaml
        # Type: string
        makemkv_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='makemkv') }}:{{ lookup('role_var', '_docker_image_tag', role='makemkv') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`makemkv_role_docker_envs_default`"

        ```yaml
        # Type: dict
        makemkv_role_docker_envs_default: 
          TZ: "{{ tz }}"
          USER_ID: "{{ uid }}"
          GROUP_ID: "{{ gid }}"
          KEEP_APP_RUNNING: "1"
        ```

    ??? variable dict "`makemkv_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        makemkv_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`makemkv_role_docker_volumes_default`"

        ```yaml
        # Type: list
        makemkv_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='makemkv') }}:/docker/appdata/makemkv"
          - "/mnt/unionfs:/storage:ro"
          - "/mnt/unionfs/makemkv:/output"
        ```

    ??? variable list "`makemkv_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        makemkv_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`makemkv_role_docker_hostname`"

        ```yaml
        # Type: string
        makemkv_role_docker_hostname: "{{ makemkv_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`makemkv_role_docker_networks_alias`"

        ```yaml
        # Type: string
        makemkv_role_docker_networks_alias: "{{ makemkv_name }}"
        ```

    ??? variable list "`makemkv_role_docker_networks_default`"

        ```yaml
        # Type: list
        makemkv_role_docker_networks_default: []
        ```

    ??? variable list "`makemkv_role_docker_networks_custom`"

        ```yaml
        # Type: list
        makemkv_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`makemkv_role_docker_restart_policy`"

        ```yaml
        # Type: string
        makemkv_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`makemkv_role_docker_state`"

        ```yaml
        # Type: string
        makemkv_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`makemkv_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        makemkv_role_autoheal_enabled: true
        ```

    ??? variable string "`makemkv_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        makemkv_role_depends_on: ""
        ```

    ??? variable string "`makemkv_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        makemkv_role_depends_on_delay: "0"
        ```

    ??? variable string "`makemkv_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        makemkv_role_depends_on_healthchecks:
        ```

    ??? variable bool "`makemkv_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        makemkv_role_diun_enabled: true
        ```

    ??? variable bool "`makemkv_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        makemkv_role_dns_enabled: true
        ```

    ??? variable bool "`makemkv_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        makemkv_role_docker_controller: true
        ```

    ??? variable bool "`makemkv_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        makemkv_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`makemkv_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        makemkv_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`makemkv_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        makemkv_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`makemkv_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        makemkv_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`makemkv_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        makemkv_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`makemkv_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        makemkv_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`makemkv_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        makemkv_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`makemkv_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        makemkv_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`makemkv_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        makemkv_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`makemkv_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        makemkv_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            makemkv_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "makemkv2.{{ user.domain }}"
              - "makemkv.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`makemkv_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        makemkv_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            makemkv_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'makemkv2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`makemkv_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        makemkv_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
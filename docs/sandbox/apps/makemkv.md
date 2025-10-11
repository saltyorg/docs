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

- To access makemkv, visit `https://makemkv._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        makemkv_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    makemkv_name: makemkv

    ```

??? example "Paths"

    ```yaml
    # Type: string
    makemkv_role_paths_folder: "{{ makemkv_name }}"

    # Type: string
    makemkv_role_paths_location: "{{ server_appdata_path }}/{{ makemkv_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    makemkv_role_web_subdomain: "{{ makemkv_name }}"

    # Type: string
    makemkv_role_web_domain: "{{ user.domain }}"

    # Type: string
    makemkv_role_web_port: "5800"

    # Type: string
    makemkv_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='makemkv') + '.' + lookup('role_var', '_web_domain', role='makemkv')
                           if (lookup('role_var', '_web_subdomain', role='makemkv') | length > 0)
                           else lookup('role_var', '_web_domain', role='makemkv')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    makemkv_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='makemkv') }}"

    # Type: string
    makemkv_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='makemkv') }}"

    # Type: bool (true/false)
    makemkv_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    makemkv_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    makemkv_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    makemkv_role_traefik_middleware_custom: ""

    # Type: string
    makemkv_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    makemkv_role_traefik_enabled: true

    # Type: bool (true/false)
    makemkv_role_traefik_api_enabled: false

    # Type: string
    makemkv_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    makemkv_role_docker_container: "{{ makemkv_name }}"

    # Image
    # Type: bool (true/false)
    makemkv_role_docker_image_pull: true

    # Type: string
    makemkv_role_docker_image_tag: "latest"

    # Type: string
    makemkv_role_docker_image_repo: "jlesage/makemkv"

    # Type: string
    makemkv_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='makemkv') }}:{{ lookup('role_var', '_docker_image_tag', role='makemkv') }}"

    # Envs
    # Type: dict
    makemkv_role_docker_envs_default: 
      TZ: "{{ tz }}"
      USER_ID: "{{ uid }}"
      GROUP_ID: "{{ gid }}"
      KEEP_APP_RUNNING: "1"

    # Type: dict
    makemkv_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    makemkv_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='makemkv') }}:/docker/appdata/makemkv"
      - "/mnt/unionfs:/storage:ro"
      - "/mnt/unionfs/makemkv:/output"

    # Type: list
    makemkv_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    makemkv_role_docker_hostname: "{{ makemkv_name }}"

    # Networks
    # Type: string
    makemkv_role_docker_networks_alias: "{{ makemkv_name }}"

    # Type: list
    makemkv_role_docker_networks_default: []

    # Type: list
    makemkv_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    makemkv_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    makemkv_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    makemkv_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    makemkv_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    makemkv_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    makemkv_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    makemkv_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    makemkv_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    makemkv_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    makemkv_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    makemkv_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    makemkv_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    makemkv_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    makemkv_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    makemkv_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    makemkv_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    makemkv_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    makemkv_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    makemkv_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        makemkv_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "makemkv2.{{ user.domain }}"
          - "makemkv.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        makemkv_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'makemkv2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

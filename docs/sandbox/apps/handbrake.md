---
hide:
  - tags
tags:
  - handbrake
  - media
  - encoding
---

# HandBrake

## What is it?

[HandBrake](https://handbrake.fr/) is a tool for converting video from nearly any format to a selection of modern, widely supported codecs.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://handbrake.fr/){: .header-icons } | [:octicons-link-16: Docs](https://handbrake.fr/docs){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/HandBrake/HandBrake){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jlesage/handbrake){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-handbrake

```

### 2. URL

- To access HandBrake, visit `https://handbrake.xDOMAIN_NAMEx`

### 3. Setup

1. Edit the HandBrake section in [sandbox `settings.yml`:](../settings.md) and enter your desired password. Please note that it MUST be less than eight characters.

    ``` { .yaml }
    handbrake:
      handbrake_pass: saltbox
    ```

2. Run the role install command

    ``` { .shell }

    sb install sandbox-handbrake

    ```

3. Access HandBrake `https://handbrake.xDOMAIN_NAMEx`

4. See the HandBrake documentation for usage:
      - [:octicons-link-16: Documentation](https://handbrake.fr/docs){: .header-icons }

!!! tip
      This container has an automatic video converter built in, see the [container documentation here](https://github.com/jlesage/docker-handbrake#automatic-video-conversion){: .header-icons }.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        handbrake_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `handbrake_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `handbrake_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    handbrake_name: handbrake

    ```

??? example "Paths"

    ```yaml
    # Type: string
    handbrake_role_paths_folder: "{{ handbrake_name }}"

    # Type: string
    handbrake_role_paths_location: "{{ server_appdata_path }}/{{ handbrake_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    handbrake_role_web_subdomain: "{{ handbrake_name }}"

    # Type: string
    handbrake_role_web_domain: "{{ user.domain }}"

    # Type: string
    handbrake_role_web_port: "5800"

    # Type: string
    handbrake_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='handbrake') + '.' + lookup('role_var', '_web_domain', role='handbrake')
                             if (lookup('role_var', '_web_subdomain', role='handbrake') | length > 0)
                             else lookup('role_var', '_web_domain', role='handbrake')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    handbrake_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='handbrake') }}"

    # Type: string
    handbrake_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='handbrake') }}"

    # Type: bool (true/false)
    handbrake_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    handbrake_role_traefik_sso_middleware: ""

    # Type: string
    handbrake_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    handbrake_role_traefik_middleware_custom: ""

    # Type: string
    handbrake_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    handbrake_role_traefik_enabled: true

    # Type: bool (true/false)
    handbrake_role_traefik_api_enabled: false

    # Type: string
    handbrake_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    handbrake_role_docker_container: "{{ handbrake_name }}"

    # Image
    # Type: bool (true/false)
    handbrake_role_docker_image_pull: true

    # Type: string
    handbrake_role_docker_image_repo: "jlesage/handbrake"

    # Type: string
    handbrake_role_docker_image_tag: "latest"

    # Type: string
    handbrake_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='handbrake') }}:{{ lookup('role_var', '_docker_image_tag', role='handbrake') }}"

    # Envs
    # Type: dict
    handbrake_role_docker_envs_default: 
      USER_ID: "{{ uid }}"
      GROUP_ID: "{{ gid }}"
      TZ: "{{ tz }}"
      CLEAN_TMP_DIR: "1"
      ENABLE_CJK_FONT: "1"
      VNC_PASSWORD: "{{ handbrake.handbrake_pass | default('saltbox', true) }}"

    # Type: dict
    handbrake_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    handbrake_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='handbrake') }}:/config"
      - "/mnt:/storage:ro"
      - "/mnt/local/downloads/handbrake/watch:/watch"
      - "/mnt/local/downloads/handbrake/output:/output"

    # Type: list
    handbrake_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    handbrake_role_docker_hostname: "{{ handbrake_name }}"

    # Networks
    # Type: string
    handbrake_role_docker_networks_alias: "{{ handbrake_name }}"

    # Type: list
    handbrake_role_docker_networks_default: []

    # Type: list
    handbrake_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    handbrake_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    handbrake_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    handbrake_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    handbrake_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    handbrake_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    handbrake_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    handbrake_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    handbrake_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    handbrake_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    handbrake_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    handbrake_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    handbrake_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    handbrake_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    handbrake_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    handbrake_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    handbrake_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    handbrake_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    handbrake_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    handbrake_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        handbrake_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "handbrake2.{{ user.domain }}"
          - "handbrake.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        handbrake_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'handbrake2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

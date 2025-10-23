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

- To access HandBrake, visit `https://handbrake._yourdomain.com_`

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

3. Access HandBrake `https://handbrake._yourdomain.com_`

4. See the HandBrake documentation for usage:
      - [:octicons-link-16: Documentation](https://handbrake.fr/docs){: .header-icons }

!!! tip
      This container has an automatic video converter built in, see the [container documentation here](https://github.com/jlesage/docker-handbrake#automatic-video-conversion){: .header-icons }.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

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

=== "Basics"

    ??? variable string "`handbrake_name`"

        ```yaml
        # Type: string
        handbrake_name: handbrake
        ```

=== "Paths"

    ??? variable string "`handbrake_role_paths_folder`"

        ```yaml
        # Type: string
        handbrake_role_paths_folder: "{{ handbrake_name }}"
        ```

    ??? variable string "`handbrake_role_paths_location`"

        ```yaml
        # Type: string
        handbrake_role_paths_location: "{{ server_appdata_path }}/{{ handbrake_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`handbrake_role_web_subdomain`"

        ```yaml
        # Type: string
        handbrake_role_web_subdomain: "{{ handbrake_name }}"
        ```

    ??? variable string "`handbrake_role_web_domain`"

        ```yaml
        # Type: string
        handbrake_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`handbrake_role_web_port`"

        ```yaml
        # Type: string
        handbrake_role_web_port: "5800"
        ```

    ??? variable string "`handbrake_role_web_url`"

        ```yaml
        # Type: string
        handbrake_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='handbrake') + '.' + lookup('role_var', '_web_domain', role='handbrake')
                                 if (lookup('role_var', '_web_subdomain', role='handbrake') | length > 0)
                                 else lookup('role_var', '_web_domain', role='handbrake')) }}"
        ```

=== "DNS"

    ??? variable string "`handbrake_role_dns_record`"

        ```yaml
        # Type: string
        handbrake_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='handbrake') }}"
        ```

    ??? variable string "`handbrake_role_dns_zone`"

        ```yaml
        # Type: string
        handbrake_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='handbrake') }}"
        ```

    ??? variable bool "`handbrake_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        handbrake_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`handbrake_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        handbrake_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`handbrake_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        handbrake_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`handbrake_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        handbrake_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`handbrake_role_traefik_certresolver`"

        ```yaml
        # Type: string
        handbrake_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`handbrake_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        handbrake_role_traefik_enabled: true
        ```

    ??? variable bool "`handbrake_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        handbrake_role_traefik_api_enabled: false
        ```

    ??? variable string "`handbrake_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        handbrake_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`handbrake_role_docker_container`"

        ```yaml
        # Type: string
        handbrake_role_docker_container: "{{ handbrake_name }}"
        ```

    ##### Image

    ??? variable bool "`handbrake_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        handbrake_role_docker_image_pull: true
        ```

    ??? variable string "`handbrake_role_docker_image_repo`"

        ```yaml
        # Type: string
        handbrake_role_docker_image_repo: "jlesage/handbrake"
        ```

    ??? variable string "`handbrake_role_docker_image_tag`"

        ```yaml
        # Type: string
        handbrake_role_docker_image_tag: "latest"
        ```

    ??? variable string "`handbrake_role_docker_image`"

        ```yaml
        # Type: string
        handbrake_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='handbrake') }}:{{ lookup('role_var', '_docker_image_tag', role='handbrake') }}"
        ```

    ##### Envs

    ??? variable dict "`handbrake_role_docker_envs_default`"

        ```yaml
        # Type: dict
        handbrake_role_docker_envs_default: 
          USER_ID: "{{ uid }}"
          GROUP_ID: "{{ gid }}"
          TZ: "{{ tz }}"
          CLEAN_TMP_DIR: "1"
          ENABLE_CJK_FONT: "1"
          VNC_PASSWORD: "{{ handbrake.handbrake_pass | default('saltbox', true) }}"
        ```

    ??? variable dict "`handbrake_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        handbrake_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`handbrake_role_docker_volumes_default`"

        ```yaml
        # Type: list
        handbrake_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='handbrake') }}:/config"
          - "/mnt:/storage:ro"
          - "/mnt/local/downloads/handbrake/watch:/watch"
          - "/mnt/local/downloads/handbrake/output:/output"
        ```

    ??? variable list "`handbrake_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        handbrake_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`handbrake_role_docker_hostname`"

        ```yaml
        # Type: string
        handbrake_role_docker_hostname: "{{ handbrake_name }}"
        ```

    ##### Networks

    ??? variable string "`handbrake_role_docker_networks_alias`"

        ```yaml
        # Type: string
        handbrake_role_docker_networks_alias: "{{ handbrake_name }}"
        ```

    ??? variable list "`handbrake_role_docker_networks_default`"

        ```yaml
        # Type: list
        handbrake_role_docker_networks_default: []
        ```

    ??? variable list "`handbrake_role_docker_networks_custom`"

        ```yaml
        # Type: list
        handbrake_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`handbrake_role_docker_restart_policy`"

        ```yaml
        # Type: string
        handbrake_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`handbrake_role_docker_state`"

        ```yaml
        # Type: string
        handbrake_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`handbrake_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        handbrake_role_autoheal_enabled: true
        ```

    ??? variable string "`handbrake_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        handbrake_role_depends_on: ""
        ```

    ??? variable string "`handbrake_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        handbrake_role_depends_on_delay: "0"
        ```

    ??? variable string "`handbrake_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        handbrake_role_depends_on_healthchecks:
        ```

    ??? variable bool "`handbrake_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        handbrake_role_diun_enabled: true
        ```

    ??? variable bool "`handbrake_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        handbrake_role_dns_enabled: true
        ```

    ??? variable bool "`handbrake_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        handbrake_role_docker_controller: true
        ```

    ??? variable bool "`handbrake_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        handbrake_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`handbrake_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        handbrake_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`handbrake_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        handbrake_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`handbrake_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        handbrake_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`handbrake_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        handbrake_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`handbrake_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        handbrake_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`handbrake_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        handbrake_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`handbrake_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        handbrake_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`handbrake_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        handbrake_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`handbrake_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        handbrake_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            handbrake_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "handbrake2.{{ user.domain }}"
              - "handbrake.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`handbrake_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        handbrake_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            handbrake_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'handbrake2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`handbrake_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        handbrake_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
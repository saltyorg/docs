---
icon: material/docker
hide:
  - tags
tags:
  - goplaxt
  - media
  - trakt
---

# Goplaxt

## Overview

[Goplaxt](https://github.com/XanderStrike/goplaxt) scrobbles Plex plays to Trakt with ease!

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/XanderStrike/goplaxt){: .header-icons } | [:octicons-link-16: Docs](https://github.com/XanderStrike/goplaxt){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/XanderStrike/goplaxt){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/xanderstrike/goplaxt){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-goplaxt

```

### 2. URL

- To access Goplaxt, visit <https://goplaxt.iYOUR_DOMAIN_NAMEi>

### 3. Setup

1. Create an API application through Trakt [here](https://trakt.tv/oauth/applications). The Redirect URI should be your goplaxt.domain + `/authorize`, so it reads as: `https://goplaxt.domain.com/authorize`.

2. Edit the Goplaxt section in [saltbox `settings.yml`:](../settings.md) substituting your own `ID` and `secret`.

    ``` { .yaml }
    goplaxt:
      trakt_id: IDHERE
      trakt_secret: SECRETHERE
    ```

3. Run the role install command

    ``` { .shell }

    sb install sandbox-goplaxt

    ```

4. Visit the goplaxt site at `https://goplaxt.domain.com`. <br />
    Enter your `Plex Username` then `Authorize`, and add the Webhook in `Plex Settings`. <br />
    Make sure under your server `Settings > Network` that Webhooks is `enabled`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    goplaxt_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `goplaxt_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `goplaxt_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`goplaxt_name`"

        ```yaml
        # Type: string
        goplaxt_name: goplaxt
        ```

=== "Settings"

    ??? variable string "`goplaxt_role_trakt_id`"

        ```yaml
        # Type: string
        goplaxt_role_trakt_id: ""
        ```

    ??? variable string "`goplaxt_role_trakt_secret`"

        ```yaml
        # Type: string
        goplaxt_role_trakt_secret: ""
        ```

=== "Paths"

    ??? variable string "`goplaxt_role_paths_folder`"

        ```yaml
        # Type: string
        goplaxt_role_paths_folder: "{{ goplaxt_name }}"
        ```

    ??? variable string "`goplaxt_role_paths_location`"

        ```yaml
        # Type: string
        goplaxt_role_paths_location: "{{ server_appdata_path }}/{{ goplaxt_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`goplaxt_role_web_subdomain`"

        ```yaml
        # Type: string
        goplaxt_role_web_subdomain: "{{ goplaxt_name }}"
        ```

    ??? variable string "`goplaxt_role_web_domain`"

        ```yaml
        # Type: string
        goplaxt_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`goplaxt_role_web_port`"

        ```yaml
        # Type: string
        goplaxt_role_web_port: "8000"
        ```

    ??? variable string "`goplaxt_role_web_url`"

        ```yaml
        # Type: string
        goplaxt_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='goplaxt') + '.' + lookup('role_var', '_web_domain', role='goplaxt')
                               if (lookup('role_var', '_web_subdomain', role='goplaxt') | length > 0)
                               else lookup('role_var', '_web_domain', role='goplaxt')) }}"
        ```

=== "DNS"

    ??? variable string "`goplaxt_role_dns_record`"

        ```yaml
        # Type: string
        goplaxt_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='goplaxt') }}"
        ```

    ??? variable string "`goplaxt_role_dns_zone`"

        ```yaml
        # Type: string
        goplaxt_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='goplaxt') }}"
        ```

    ??? variable bool "`goplaxt_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        goplaxt_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`goplaxt_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        goplaxt_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`goplaxt_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        goplaxt_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`goplaxt_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        goplaxt_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`goplaxt_role_traefik_certresolver`"

        ```yaml
        # Type: string
        goplaxt_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`goplaxt_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        goplaxt_role_traefik_enabled: true
        ```

    ??? variable bool "`goplaxt_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        goplaxt_role_traefik_api_enabled: false
        ```

    ??? variable string "`goplaxt_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        goplaxt_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`goplaxt_role_docker_container`"

        ```yaml
        # Type: string
        goplaxt_role_docker_container: "{{ goplaxt_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`goplaxt_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        goplaxt_role_docker_image_pull: true
        ```

    ??? variable string "`goplaxt_role_docker_image_repo`"

        ```yaml
        # Type: string
        goplaxt_role_docker_image_repo: "xanderstrike/goplaxt"
        ```

    ??? variable string "`goplaxt_role_docker_image_tag`"

        ```yaml
        # Type: string
        goplaxt_role_docker_image_tag: "latest"
        ```

    ??? variable string "`goplaxt_role_docker_image`"

        ```yaml
        # Type: string
        goplaxt_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='goplaxt') }}:{{ lookup('role_var', '_docker_image_tag', role='goplaxt') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`goplaxt_role_docker_envs_default`"

        ```yaml
        # Type: dict
        goplaxt_role_docker_envs_default: 
          TZ: "{{ tz }}"
          TRAKT_ID: "{{ lookup('role_var', '_trakt_id', role='goplaxt') }}"
          TRAKT_SECRET: "{{ lookup('role_var', '_trakt_secret', role='goplaxt') }}"
          REDIRECT_URI: "{{ lookup('role_var', '_web_url', role='goplaxt') }}"
        ```

    ??? variable dict "`goplaxt_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        goplaxt_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`goplaxt_role_docker_volumes_default`"

        ```yaml
        # Type: list
        goplaxt_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='goplaxt') }}:/app/keystore"
        ```

    ??? variable list "`goplaxt_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        goplaxt_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`goplaxt_role_docker_hostname`"

        ```yaml
        # Type: string
        goplaxt_role_docker_hostname: "{{ goplaxt_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`goplaxt_role_docker_networks_alias`"

        ```yaml
        # Type: string
        goplaxt_role_docker_networks_alias: "{{ goplaxt_name }}"
        ```

    ??? variable list "`goplaxt_role_docker_networks_default`"

        ```yaml
        # Type: list
        goplaxt_role_docker_networks_default: []
        ```

    ??? variable list "`goplaxt_role_docker_networks_custom`"

        ```yaml
        # Type: list
        goplaxt_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`goplaxt_role_docker_restart_policy`"

        ```yaml
        # Type: string
        goplaxt_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`goplaxt_role_docker_state`"

        ```yaml
        # Type: string
        goplaxt_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`goplaxt_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        goplaxt_role_autoheal_enabled: true
        ```

    ??? variable string "`goplaxt_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        goplaxt_role_depends_on: ""
        ```

    ??? variable string "`goplaxt_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        goplaxt_role_depends_on_delay: "0"
        ```

    ??? variable string "`goplaxt_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        goplaxt_role_depends_on_healthchecks:
        ```

    ??? variable bool "`goplaxt_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        goplaxt_role_diun_enabled: true
        ```

    ??? variable bool "`goplaxt_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        goplaxt_role_dns_enabled: true
        ```

    ??? variable bool "`goplaxt_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        goplaxt_role_docker_controller: true
        ```

    ??? variable bool "`goplaxt_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        goplaxt_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`goplaxt_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        goplaxt_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`goplaxt_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        goplaxt_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`goplaxt_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        goplaxt_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`goplaxt_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        goplaxt_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`goplaxt_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        goplaxt_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`goplaxt_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        goplaxt_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`goplaxt_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        goplaxt_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`goplaxt_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        goplaxt_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`goplaxt_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        goplaxt_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            goplaxt_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "goplaxt2.{{ user.domain }}"
              - "goplaxt.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`goplaxt_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        goplaxt_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            goplaxt_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'goplaxt2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`goplaxt_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        goplaxt_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
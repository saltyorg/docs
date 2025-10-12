---
hide:
  - tags
tags:
  - goplaxt
  - media
  - trakt
---

# Goplaxt

## What is it?

[Goplaxt](https://github.com/XanderStrike/goplaxt) scrobbles Plex plays to Trakt with ease!

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/XanderStrike/goplaxt){: .header-icons } | [:octicons-link-16: Docs](https://github.com/XanderStrike/goplaxt){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/XanderStrike/goplaxt){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/xanderstrike/goplaxt){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-goplaxt

```

### 2. URL

- To access Goplaxt, visit `https://goplaxt._yourdomain.com_`

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

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        goplaxt_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `goplaxt_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `goplaxt_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    goplaxt_name: goplaxt

    ```

??? example "Settings"

    ```yaml
    # Type: string
    goplaxt_role_trakt_id: ""

    # Type: string
    goplaxt_role_trakt_secret: ""

    ```

??? example "Paths"

    ```yaml
    # Type: string
    goplaxt_role_paths_folder: "{{ goplaxt_name }}"

    # Type: string
    goplaxt_role_paths_location: "{{ server_appdata_path }}/{{ goplaxt_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    goplaxt_role_web_subdomain: "{{ goplaxt_name }}"

    # Type: string
    goplaxt_role_web_domain: "{{ user.domain }}"

    # Type: string
    goplaxt_role_web_port: "8000"

    # Type: string
    goplaxt_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='goplaxt') + '.' + lookup('role_var', '_web_domain', role='goplaxt')
                           if (lookup('role_var', '_web_subdomain', role='goplaxt') | length > 0)
                           else lookup('role_var', '_web_domain', role='goplaxt')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    goplaxt_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='goplaxt') }}"

    # Type: string
    goplaxt_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='goplaxt') }}"

    # Type: bool (true/false)
    goplaxt_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    goplaxt_role_traefik_sso_middleware: ""

    # Type: string
    goplaxt_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    goplaxt_role_traefik_middleware_custom: ""

    # Type: string
    goplaxt_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    goplaxt_role_traefik_enabled: true

    # Type: bool (true/false)
    goplaxt_role_traefik_api_enabled: false

    # Type: string
    goplaxt_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    goplaxt_role_docker_container: "{{ goplaxt_name }}"

    # Image
    # Type: bool (true/false)
    goplaxt_role_docker_image_pull: true

    # Type: string
    goplaxt_role_docker_image_repo: "xanderstrike/goplaxt"

    # Type: string
    goplaxt_role_docker_image_tag: "latest"

    # Type: string
    goplaxt_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='goplaxt') }}:{{ lookup('role_var', '_docker_image_tag', role='goplaxt') }}"

    # Envs
    # Type: dict
    goplaxt_role_docker_envs_default: 
      TZ: "{{ tz }}"
      TRAKT_ID: "{{ lookup('role_var', '_trakt_id', role='goplaxt') }}"
      TRAKT_SECRET: "{{ lookup('role_var', '_trakt_secret', role='goplaxt') }}"
      REDIRECT_URI: "{{ lookup('role_var', '_web_url', role='goplaxt') }}"

    # Type: dict
    goplaxt_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    goplaxt_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='goplaxt') }}:/app/keystore"

    # Type: list
    goplaxt_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    goplaxt_role_docker_hostname: "{{ goplaxt_name }}"

    # Networks
    # Type: string
    goplaxt_role_docker_networks_alias: "{{ goplaxt_name }}"

    # Type: list
    goplaxt_role_docker_networks_default: []

    # Type: list
    goplaxt_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    goplaxt_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    goplaxt_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    goplaxt_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    goplaxt_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    goplaxt_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    goplaxt_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    goplaxt_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    goplaxt_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    goplaxt_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    goplaxt_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    goplaxt_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    goplaxt_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    goplaxt_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    goplaxt_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    goplaxt_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    goplaxt_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    goplaxt_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    goplaxt_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    goplaxt_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        goplaxt_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "goplaxt2.{{ user.domain }}"
          - "goplaxt.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        goplaxt_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'goplaxt2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

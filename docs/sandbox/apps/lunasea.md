---
hide:
  - tags
tags:
  - lunasea
  - automation
  - controller
---

# Lunasea

## What is it?

[Lunasea](https://www.lunasea.app/) is a fully featured, open source self-hosted controller focused on giving you a seamless experience between all of your self-hosted media software remotely on your devices.

- Manage new media content fetched via Lidarr, Radarr, and Sonarr.
- View real-time stream information about your Plex Media Server using Tautulli.
- Manage your queue in usenet binary newsreaders, including SABnzbd and NZBGet.
- Search newsgroup indexers and send NZBs directly to your binary newsreaders.

!!! info
    By default, the role **IS** protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.lunasea.app/){: .header-icons } | [:octicons-link-16: Docs](https://docs.lunasea.app/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/JagandeepBrar/lunasea){: .header-icons }|

Recommended install types: Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-lunasea

```

### 2. URL

- To access Lunasea, visit `https://lunasea._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        lunasea_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `lunasea_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `lunasea_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    lunasea_name: lunasea

    ```

??? example "Paths"

    ```yaml
    # Type: string
    lunasea_role_paths_folder: "{{ lunasea_name }}"

    # Type: dict
    lunasea_role_paths_location: {}

    ```

??? example "Web"

    ```yaml
    # Type: string
    lunasea_role_web_subdomain: "{{ lunasea_name }}"

    # Type: string
    lunasea_role_web_domain: "{{ user.domain }}"

    # Type: string
    lunasea_role_web_port: "80"

    # Type: string
    lunasea_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='lunasea') + '.' + lookup('role_var', '_web_domain', role='lunasea')
                           if (lookup('role_var', '_web_subdomain', role='lunasea') | length > 0)
                           else lookup('role_var', '_web_domain', role='lunasea')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    lunasea_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='lunasea') }}"

    # Type: string
    lunasea_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='lunasea') }}"

    # Type: bool (true/false)
    lunasea_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    lunasea_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    lunasea_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    lunasea_role_traefik_middleware_custom: ""

    # Type: string
    lunasea_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    lunasea_role_traefik_enabled: true

    # Type: bool (true/false)
    lunasea_role_traefik_api_enabled: false

    # Type: string
    lunasea_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    lunasea_role_docker_container: "{{ lunasea_name }}"

    # Image
    # Type: bool (true/false)
    lunasea_role_docker_image_pull: true

    # Type: string
    lunasea_role_docker_image_tag: "stable"

    # Type: string
    lunasea_role_docker_image_repo: "ghcr.io/jagandeepbrar/lunasea"

    # Type: string
    lunasea_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='lunasea') }}:{{ lookup('role_var', '_docker_image_tag', role='lunasea') }}"

    # Envs
    # Type: dict
    lunasea_role_docker_envs_default: 
      TZ: "{{ tz }}"

    # Type: dict
    lunasea_role_docker_envs_custom: {}

    # Hostname
    # Type: string
    lunasea_role_docker_hostname: "{{ lunasea_name }}"

    # Networks
    # Type: string
    lunasea_role_docker_networks_alias: "{{ lunasea_name }}"

    # Type: list
    lunasea_role_docker_networks_default: []

    # Type: list
    lunasea_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    lunasea_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    lunasea_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    lunasea_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    lunasea_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    lunasea_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    lunasea_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    lunasea_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    lunasea_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    lunasea_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    lunasea_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    lunasea_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    lunasea_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    lunasea_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    lunasea_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    lunasea_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    lunasea_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    lunasea_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    lunasea_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    lunasea_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        lunasea_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "lunasea2.{{ user.domain }}"
          - "lunasea.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        lunasea_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'lunasea2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

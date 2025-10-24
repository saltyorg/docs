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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    lunasea_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `lunasea_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `lunasea_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`lunasea_name`"

        ```yaml
        # Type: string
        lunasea_name: lunasea
        ```

=== "Paths"

    ??? variable string "`lunasea_role_paths_folder`"

        ```yaml
        # Type: string
        lunasea_role_paths_folder: "{{ lunasea_name }}"
        ```

    ??? variable dict "`lunasea_role_paths_location`"

        ```yaml
        # Type: dict
        lunasea_role_paths_location: {}
        ```

=== "Web"

    ??? variable string "`lunasea_role_web_subdomain`"

        ```yaml
        # Type: string
        lunasea_role_web_subdomain: "{{ lunasea_name }}"
        ```

    ??? variable string "`lunasea_role_web_domain`"

        ```yaml
        # Type: string
        lunasea_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`lunasea_role_web_port`"

        ```yaml
        # Type: string
        lunasea_role_web_port: "80"
        ```

    ??? variable string "`lunasea_role_web_url`"

        ```yaml
        # Type: string
        lunasea_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='lunasea') + '.' + lookup('role_var', '_web_domain', role='lunasea')
                               if (lookup('role_var', '_web_subdomain', role='lunasea') | length > 0)
                               else lookup('role_var', '_web_domain', role='lunasea')) }}"
        ```

=== "DNS"

    ??? variable string "`lunasea_role_dns_record`"

        ```yaml
        # Type: string
        lunasea_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='lunasea') }}"
        ```

    ??? variable string "`lunasea_role_dns_zone`"

        ```yaml
        # Type: string
        lunasea_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='lunasea') }}"
        ```

    ??? variable bool "`lunasea_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        lunasea_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`lunasea_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        lunasea_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`lunasea_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        lunasea_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`lunasea_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        lunasea_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`lunasea_role_traefik_certresolver`"

        ```yaml
        # Type: string
        lunasea_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`lunasea_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        lunasea_role_traefik_enabled: true
        ```

    ??? variable bool "`lunasea_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        lunasea_role_traefik_api_enabled: false
        ```

    ??? variable string "`lunasea_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        lunasea_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    Container
    { .sb-h5 }

    ??? variable string "`lunasea_role_docker_container`"

        ```yaml
        # Type: string
        lunasea_role_docker_container: "{{ lunasea_name }}"
        ```

    Image
    { .sb-h5 }

    ??? variable bool "`lunasea_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        lunasea_role_docker_image_pull: true
        ```

    ??? variable string "`lunasea_role_docker_image_tag`"

        ```yaml
        # Type: string
        lunasea_role_docker_image_tag: "stable"
        ```

    ??? variable string "`lunasea_role_docker_image_repo`"

        ```yaml
        # Type: string
        lunasea_role_docker_image_repo: "ghcr.io/jagandeepbrar/lunasea"
        ```

    ??? variable string "`lunasea_role_docker_image`"

        ```yaml
        # Type: string
        lunasea_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='lunasea') }}:{{ lookup('role_var', '_docker_image_tag', role='lunasea') }}"
        ```

    Envs
    { .sb-h5 }

    ??? variable dict "`lunasea_role_docker_envs_default`"

        ```yaml
        # Type: dict
        lunasea_role_docker_envs_default: 
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`lunasea_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        lunasea_role_docker_envs_custom: {}
        ```

    Hostname
    { .sb-h5 }

    ??? variable string "`lunasea_role_docker_hostname`"

        ```yaml
        # Type: string
        lunasea_role_docker_hostname: "{{ lunasea_name }}"
        ```

    Networks
    { .sb-h5 }

    ??? variable string "`lunasea_role_docker_networks_alias`"

        ```yaml
        # Type: string
        lunasea_role_docker_networks_alias: "{{ lunasea_name }}"
        ```

    ??? variable list "`lunasea_role_docker_networks_default`"

        ```yaml
        # Type: list
        lunasea_role_docker_networks_default: []
        ```

    ??? variable list "`lunasea_role_docker_networks_custom`"

        ```yaml
        # Type: list
        lunasea_role_docker_networks_custom: []
        ```

    Restart Policy
    { .sb-h5 }

    ??? variable string "`lunasea_role_docker_restart_policy`"

        ```yaml
        # Type: string
        lunasea_role_docker_restart_policy: unless-stopped
        ```

    State
    { .sb-h5 }

    ??? variable string "`lunasea_role_docker_state`"

        ```yaml
        # Type: string
        lunasea_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`lunasea_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        lunasea_role_autoheal_enabled: true
        ```

    ??? variable string "`lunasea_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        lunasea_role_depends_on: ""
        ```

    ??? variable string "`lunasea_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        lunasea_role_depends_on_delay: "0"
        ```

    ??? variable string "`lunasea_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        lunasea_role_depends_on_healthchecks:
        ```

    ??? variable bool "`lunasea_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        lunasea_role_diun_enabled: true
        ```

    ??? variable bool "`lunasea_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        lunasea_role_dns_enabled: true
        ```

    ??? variable bool "`lunasea_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        lunasea_role_docker_controller: true
        ```

    ??? variable bool "`lunasea_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        lunasea_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`lunasea_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        lunasea_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`lunasea_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        lunasea_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`lunasea_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        lunasea_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`lunasea_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        lunasea_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`lunasea_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        lunasea_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`lunasea_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        lunasea_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`lunasea_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        lunasea_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`lunasea_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        lunasea_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`lunasea_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        lunasea_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            lunasea_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "lunasea2.{{ user.domain }}"
              - "lunasea.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`lunasea_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        lunasea_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            lunasea_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'lunasea2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`lunasea_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        lunasea_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
hide:
  - tags
tags:
  - stash
  - media
  - organizer
---

# Stash

## What is it?

[Stash](https://stashapp.cc/) is a locally hosted web-based app written in Go which organizes and serves your porn.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://stashapp.cc/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/stashapp/stash/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/stashapp/stash){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/stashapp/stash){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-stash

```

### 2. URL

- To access Stash, visit `https://stash._yourdomain.com_`

### 3. Setup

On a clean installation, Stash only creates its config file when the user has gone through the setup wizard. If you receive errors on future visits to Stash regarding public access, re-run `sb install sandbox-stash` to apply the appropriate config edits to disable these warnings.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        stash_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `stash_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `stash_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`stash_name`"

        ```yaml
        # Type: string
        stash_name: stash
        ```

=== "Paths"

    ??? variable string "`stash_role_paths_folder`"

        ```yaml
        # Type: string
        stash_role_paths_folder: "{{ stash_name }}"
        ```

    ??? variable string "`stash_role_paths_location`"

        ```yaml
        # Type: string
        stash_role_paths_location: "{{ server_appdata_path }}/{{ stash_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`stash_role_web_subdomain`"

        ```yaml
        # Type: string
        stash_role_web_subdomain: "{{ stash_name }}"
        ```

    ??? variable string "`stash_role_web_domain`"

        ```yaml
        # Type: string
        stash_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`stash_role_web_port`"

        ```yaml
        # Type: string
        stash_role_web_port: "9999"
        ```

    ??? variable string "`stash_role_web_url`"

        ```yaml
        # Type: string
        stash_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='stash') + '.' + lookup('role_var', '_web_domain', role='stash')
                             if (lookup('role_var', '_web_subdomain', role='stash') | length > 0)
                             else lookup('role_var', '_web_domain', role='stash')) }}"
        ```

=== "DNS"

    ??? variable string "`stash_role_dns_record`"

        ```yaml
        # Type: string
        stash_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='stash') }}"
        ```

    ??? variable string "`stash_role_dns_zone`"

        ```yaml
        # Type: string
        stash_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='stash') }}"
        ```

    ??? variable bool "`stash_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        stash_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`stash_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        stash_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`stash_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        stash_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`stash_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        stash_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`stash_role_traefik_certresolver`"

        ```yaml
        # Type: string
        stash_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`stash_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        stash_role_traefik_enabled: true
        ```

    ??? variable bool "`stash_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        stash_role_traefik_api_enabled: false
        ```

    ??? variable string "`stash_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        stash_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`stash_role_docker_container`"

        ```yaml
        # Type: string
        stash_role_docker_container: "{{ stash_name }}"
        ```

    ##### Image

    ??? variable bool "`stash_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        stash_role_docker_image_pull: true
        ```

    ??? variable string "`stash_role_docker_image_repo`"

        ```yaml
        # Type: string
        stash_role_docker_image_repo: "ghcr.io/hotio/stash"
        ```

    ??? variable string "`stash_role_docker_image_tag`"

        ```yaml
        # Type: string
        stash_role_docker_image_tag: "latest"
        ```

    ??? variable string "`stash_role_docker_image`"

        ```yaml
        # Type: string
        stash_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='stash') }}:{{ lookup('role_var', '_docker_image_tag', role='stash') }}"
        ```

    ##### Envs

    ??? variable dict "`stash_role_docker_envs_default`"

        ```yaml
        # Type: dict
        stash_role_docker_envs_default: 
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
        ```

    ??? variable dict "`stash_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        stash_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`stash_role_docker_volumes_default`"

        ```yaml
        # Type: list
        stash_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='stash') }}/config:/config"
          - "{{ lookup('role_var', '_paths_location', role='stash') }}/metadata:/metadata"
          - "{{ lookup('role_var', '_paths_location', role='stash') }}/cache:/cache"
          - "{{ lookup('role_var', '_paths_location', role='stash') }}/generated:/generated"
          - "/mnt/unionfs/Media/Adult:/data"
        ```

    ??? variable list "`stash_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        stash_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`stash_role_docker_hostname`"

        ```yaml
        # Type: string
        stash_role_docker_hostname: "{{ stash_name }}"
        ```

    ##### Networks

    ??? variable string "`stash_role_docker_networks_alias`"

        ```yaml
        # Type: string
        stash_role_docker_networks_alias: "{{ stash_name }}"
        ```

    ??? variable list "`stash_role_docker_networks_default`"

        ```yaml
        # Type: list
        stash_role_docker_networks_default: []
        ```

    ??? variable list "`stash_role_docker_networks_custom`"

        ```yaml
        # Type: list
        stash_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`stash_role_docker_restart_policy`"

        ```yaml
        # Type: string
        stash_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`stash_role_docker_state`"

        ```yaml
        # Type: string
        stash_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`stash_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        stash_role_autoheal_enabled: true
        ```

    ??? variable string "`stash_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        stash_role_depends_on: ""
        ```

    ??? variable string "`stash_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        stash_role_depends_on_delay: "0"
        ```

    ??? variable string "`stash_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        stash_role_depends_on_healthchecks:
        ```

    ??? variable bool "`stash_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        stash_role_diun_enabled: true
        ```

    ??? variable bool "`stash_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        stash_role_dns_enabled: true
        ```

    ??? variable bool "`stash_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        stash_role_docker_controller: true
        ```

    ??? variable bool "`stash_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        stash_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`stash_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        stash_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`stash_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        stash_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`stash_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        stash_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`stash_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        stash_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`stash_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        stash_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`stash_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        stash_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`stash_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        stash_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            stash_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "stash2.{{ user.domain }}"
              - "stash.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`stash_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        stash_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            stash_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'stash2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`stash_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        stash_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
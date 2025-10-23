---
hide:
  - tags
tags:
  - kitana
  - plex
  - frontend
---

# Kitana

## What is it?

[Kitana](https://github.com/pannal/Kitana) is a responsive Plex plugin web frontend.

Running one instance of Kitana can serve infinite amounts of servers and plugins - you can even expose your Kitana instance to your friends, so they can manage their plugins as well, so they don't have to run their own Kitana instance.

Kitana was built for Sub-Zero originally, but handles other plugins just as well.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/pannal/Kitana){: .header-icons } | [:octicons-link-16: Docs](https://github.com/pannal/Kitana){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/pannal/Kitana){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/pannal/kitana){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-kitana

```

### 2. URL

- To access Kitana, visit `https://kitana._yourdomain.com_`

### 3. Setup

- pen your browser and visit your Kitana instance `https://kitana._yourdomain.com_`

- authenticate against Plex.TV

- select your server (non-owned may not work; local connections are preferred)

- profit

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        kitana_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `kitana_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `kitana_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`kitana_name`"

        ```yaml
        # Type: string
        kitana_name: kitana
        ```

=== "Paths"

    ??? variable string "`kitana_role_paths_folder`"

        ```yaml
        # Type: string
        kitana_role_paths_folder: "{{ kitana_name }}"
        ```

    ??? variable string "`kitana_role_paths_location`"

        ```yaml
        # Type: string
        kitana_role_paths_location: "{{ server_appdata_path }}/{{ kitana_role_paths_folder }}"
        ```

    ??? variable string "`kitana_role_paths_config_location`"

        ```yaml
        # Type: string
        kitana_role_paths_config_location: "{{ kitana_role_paths_location }}/config.yml"
        ```

=== "Web"

    ??? variable string "`kitana_role_web_subdomain`"

        ```yaml
        # Type: string
        kitana_role_web_subdomain: "{{ kitana_name }}"
        ```

    ??? variable string "`kitana_role_web_domain`"

        ```yaml
        # Type: string
        kitana_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`kitana_role_web_port`"

        ```yaml
        # Type: string
        kitana_role_web_port: "31337"
        ```

    ??? variable string "`kitana_role_web_url`"

        ```yaml
        # Type: string
        kitana_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='kitana') + '.' + lookup('role_var', '_web_domain', role='kitana')
                              if (lookup('role_var', '_web_subdomain', role='kitana') | length > 0)
                              else lookup('role_var', '_web_domain', role='kitana')) }}"
        ```

=== "DNS"

    ??? variable string "`kitana_role_dns_record`"

        ```yaml
        # Type: string
        kitana_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='kitana') }}"
        ```

    ??? variable string "`kitana_role_dns_zone`"

        ```yaml
        # Type: string
        kitana_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='kitana') }}"
        ```

    ??? variable bool "`kitana_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`kitana_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        kitana_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`kitana_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        kitana_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`kitana_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        kitana_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`kitana_role_traefik_certresolver`"

        ```yaml
        # Type: string
        kitana_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`kitana_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_traefik_enabled: true
        ```

    ??? variable bool "`kitana_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_traefik_api_enabled: false
        ```

    ??? variable string "`kitana_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        kitana_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`kitana_role_docker_container`"

        ```yaml
        # Type: string
        kitana_role_docker_container: "{{ kitana_name }}"
        ```

    ##### Image

    ??? variable bool "`kitana_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_docker_image_pull: true
        ```

    ??? variable string "`kitana_role_docker_image_repo`"

        ```yaml
        # Type: string
        kitana_role_docker_image_repo: "pannal/kitana"
        ```

    ??? variable string "`kitana_role_docker_image_tag`"

        ```yaml
        # Type: string
        kitana_role_docker_image_tag: "latest"
        ```

    ??? variable string "`kitana_role_docker_image`"

        ```yaml
        # Type: string
        kitana_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='kitana') }}:{{ lookup('role_var', '_docker_image_tag', role='kitana') }}"
        ```

    ##### Envs

    ??? variable dict "`kitana_role_docker_envs_default`"

        ```yaml
        # Type: dict
        kitana_role_docker_envs_default: 
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`kitana_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        kitana_role_docker_envs_custom: {}
        ```

    ##### Commands

    ??? variable list "`kitana_role_docker_commands_default`"

        ```yaml
        # Type: list
        kitana_role_docker_commands_default: 
          - "-P"
        ```

    ??? variable list "`kitana_role_docker_commands_custom`"

        ```yaml
        # Type: list
        kitana_role_docker_commands_custom: []
        ```

    ##### Volumes

    ??? variable list "`kitana_role_docker_volumes_default`"

        ```yaml
        # Type: list
        kitana_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='kitana') }}:/app/data"
        ```

    ??? variable list "`kitana_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        kitana_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`kitana_role_docker_hostname`"

        ```yaml
        # Type: string
        kitana_role_docker_hostname: "{{ kitana_name }}"
        ```

    ##### Networks

    ??? variable string "`kitana_role_docker_networks_alias`"

        ```yaml
        # Type: string
        kitana_role_docker_networks_alias: "{{ kitana_name }}"
        ```

    ??? variable list "`kitana_role_docker_networks_default`"

        ```yaml
        # Type: list
        kitana_role_docker_networks_default: []
        ```

    ??? variable list "`kitana_role_docker_networks_custom`"

        ```yaml
        # Type: list
        kitana_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`kitana_role_docker_restart_policy`"

        ```yaml
        # Type: string
        kitana_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`kitana_role_docker_state`"

        ```yaml
        # Type: string
        kitana_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`kitana_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        kitana_role_autoheal_enabled: true
        ```

    ??? variable string "`kitana_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        kitana_role_depends_on: ""
        ```

    ??? variable string "`kitana_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        kitana_role_depends_on_delay: "0"
        ```

    ??? variable string "`kitana_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        kitana_role_depends_on_healthchecks:
        ```

    ??? variable bool "`kitana_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        kitana_role_diun_enabled: true
        ```

    ??? variable bool "`kitana_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        kitana_role_dns_enabled: true
        ```

    ??? variable bool "`kitana_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        kitana_role_docker_controller: true
        ```

    ??? variable bool "`kitana_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        kitana_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`kitana_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        kitana_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`kitana_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        kitana_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`kitana_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        kitana_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`kitana_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`kitana_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        kitana_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`kitana_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        kitana_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`kitana_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        kitana_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`kitana_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        kitana_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`kitana_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        kitana_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            kitana_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "kitana2.{{ user.domain }}"
              - "kitana.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`kitana_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        kitana_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            kitana_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'kitana2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`kitana_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        kitana_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
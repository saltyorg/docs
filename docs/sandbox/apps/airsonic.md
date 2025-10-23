---
hide:
  - tags
tags:
  - airsonic
  - music
  - streaming
---

# Airsonic

## What is it?

[Airsonic](https://github.com/airsonic/airsonic) is a free, web-based media streamer, providing ubiquitious access to your music. Use it to share your music with friends, or to listen to your own music while at work. You can stream to multiple players simultaneously, for instance to one player in your kitchen and another in your living room.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/airsonic/airsonic){: .header-icons } | [:octicons-link-16: Docs](https://airsonic.github.io/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/airsonic/airsonic){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/airsonic){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-airsonic

```

### 2. URL

- To access Airsonic, visit `https://airsonic._yourdomain.com_`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        airsonic_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `airsonic_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `airsonic_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`airsonic_name`"

        ```yaml
        # Type: string
        airsonic_name: airsonic
        ```

=== "Paths"

    ??? variable string "`airsonic_role_paths_folder`"

        ```yaml
        # Type: string
        airsonic_role_paths_folder: "{{ airsonic_name }}"
        ```

    ??? variable string "`airsonic_role_paths_location`"

        ```yaml
        # Type: string
        airsonic_role_paths_location: "{{ server_appdata_path }}/{{ airsonic_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`airsonic_role_web_subdomain`"

        ```yaml
        # Type: string
        airsonic_role_web_subdomain: "{{ airsonic_name }}"
        ```

    ??? variable string "`airsonic_role_web_domain`"

        ```yaml
        # Type: string
        airsonic_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`airsonic_role_web_port`"

        ```yaml
        # Type: string
        airsonic_role_web_port: "4040"
        ```

    ??? variable string "`airsonic_role_web_url`"

        ```yaml
        # Type: string
        airsonic_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='airsonic') + '.' + lookup('role_var', '_web_domain', role='airsonic')
                                if (lookup('role_var', '_web_subdomain', role='airsonic') | length > 0)
                                else lookup('role_var', '_web_domain', role='airsonic')) }}"
        ```

=== "DNS"

    ??? variable string "`airsonic_role_dns_record`"

        ```yaml
        # Type: string
        airsonic_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='airsonic') }}"
        ```

    ??? variable string "`airsonic_role_dns_zone`"

        ```yaml
        # Type: string
        airsonic_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='airsonic') }}"
        ```

    ??? variable bool "`airsonic_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        airsonic_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`airsonic_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        airsonic_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`airsonic_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        airsonic_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`airsonic_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        airsonic_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`airsonic_role_traefik_certresolver`"

        ```yaml
        # Type: string
        airsonic_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`airsonic_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        airsonic_role_traefik_enabled: true
        ```

    ??? variable bool "`airsonic_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        airsonic_role_traefik_api_enabled: false
        ```

    ??? variable string "`airsonic_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        airsonic_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`airsonic_role_docker_container`"

        ```yaml
        # Type: string
        airsonic_role_docker_container: "{{ airsonic_name }}"
        ```

    ##### Image

    ??? variable bool "`airsonic_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        airsonic_role_docker_image_pull: true
        ```

    ??? variable string "`airsonic_role_docker_image_repo`"

        ```yaml
        # Type: string
        airsonic_role_docker_image_repo: "lscr.io/linuxserver/airsonic-advanced"
        ```

    ??? variable string "`airsonic_role_docker_image_tag`"

        ```yaml
        # Type: string
        airsonic_role_docker_image_tag: "latest"
        ```

    ??? variable string "`airsonic_role_docker_image`"

        ```yaml
        # Type: string
        airsonic_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='airsonic') }}:{{ lookup('role_var', '_docker_image_tag', role='airsonic') }}"
        ```

    ##### Envs

    ??? variable dict "`airsonic_role_docker_envs_default`"

        ```yaml
        # Type: dict
        airsonic_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          JAVA_OPTS: "-Dserver.use-forward-headers=true"
        ```

    ??? variable dict "`airsonic_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        airsonic_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`airsonic_role_docker_volumes_default`"

        ```yaml
        # Type: list
        airsonic_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='airsonic') }}:/config"
        ```

    ??? variable list "`airsonic_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        airsonic_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`airsonic_role_docker_hostname`"

        ```yaml
        # Type: string
        airsonic_role_docker_hostname: "{{ airsonic_name }}"
        ```

    ##### Networks

    ??? variable string "`airsonic_role_docker_networks_alias`"

        ```yaml
        # Type: string
        airsonic_role_docker_networks_alias: "{{ airsonic_name }}"
        ```

    ??? variable list "`airsonic_role_docker_networks_default`"

        ```yaml
        # Type: list
        airsonic_role_docker_networks_default: []
        ```

    ??? variable list "`airsonic_role_docker_networks_custom`"

        ```yaml
        # Type: list
        airsonic_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`airsonic_role_docker_restart_policy`"

        ```yaml
        # Type: string
        airsonic_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`airsonic_role_docker_state`"

        ```yaml
        # Type: string
        airsonic_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`airsonic_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        airsonic_role_autoheal_enabled: true
        ```

    ??? variable string "`airsonic_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        airsonic_role_depends_on: ""
        ```

    ??? variable string "`airsonic_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        airsonic_role_depends_on_delay: "0"
        ```

    ??? variable string "`airsonic_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        airsonic_role_depends_on_healthchecks:
        ```

    ??? variable bool "`airsonic_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        airsonic_role_diun_enabled: true
        ```

    ??? variable bool "`airsonic_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        airsonic_role_dns_enabled: true
        ```

    ??? variable bool "`airsonic_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        airsonic_role_docker_controller: true
        ```

    ??? variable bool "`airsonic_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        airsonic_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`airsonic_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        airsonic_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`airsonic_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        airsonic_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`airsonic_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        airsonic_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`airsonic_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        airsonic_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`airsonic_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        airsonic_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`airsonic_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        airsonic_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`airsonic_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        airsonic_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`airsonic_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        airsonic_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`airsonic_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        airsonic_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            airsonic_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "airsonic2.{{ user.domain }}"
              - "airsonic.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`airsonic_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        airsonic_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            airsonic_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'airsonic2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`airsonic_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        airsonic_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
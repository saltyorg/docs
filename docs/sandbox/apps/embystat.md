---
hide:
  - tags
tags:
  - embystat
  - statistics
  - monitoring
---

# EmbyStat

## What is it?

[EmbyStat](https://github.com/mregni/EmbyStat/) is a personal web server that can calculate all kinds of statistics from your (local) Emby or Jellyfin server. Just install this on your server and let him calculate all kinds of fun stuff.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/mregni/EmbyStat/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/mregni/EmbyStat/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/mregni/EmbyStat/){: .header-icons } | [:material-docker: Docker](https://registry.hub.docker.com/r/uping/embystat){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-embystat

```

### 2. URL

- To access EmbyStat, visit `https://embystat._yourdomain.com_`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        embystat_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `embystat_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `embystat_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`embystat_name`"

        ```yaml
        # Type: string
        embystat_name: embystat
        ```

=== "Paths"

    ??? variable string "`embystat_role_paths_folder`"

        ```yaml
        # Type: string
        embystat_role_paths_folder: "{{ embystat_name }}"
        ```

    ??? variable string "`embystat_role_paths_location`"

        ```yaml
        # Type: string
        embystat_role_paths_location: "{{ server_appdata_path }}/{{ embystat_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`embystat_role_web_subdomain`"

        ```yaml
        # Type: string
        embystat_role_web_subdomain: "{{ embystat_name }}"
        ```

    ??? variable string "`embystat_role_web_domain`"

        ```yaml
        # Type: string
        embystat_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`embystat_role_web_port`"

        ```yaml
        # Type: string
        embystat_role_web_port: "6555"
        ```

    ??? variable string "`embystat_role_web_url`"

        ```yaml
        # Type: string
        embystat_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='embystat') + '.' + lookup('role_var', '_web_domain', role='embystat')
                                if (lookup('role_var', '_web_subdomain', role='embystat') | length > 0)
                                else lookup('role_var', '_web_domain', role='embystat')) }}"
        ```

=== "DNS"

    ??? variable string "`embystat_role_dns_record`"

        ```yaml
        # Type: string
        embystat_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='embystat') }}"
        ```

    ??? variable string "`embystat_role_dns_zone`"

        ```yaml
        # Type: string
        embystat_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='embystat') }}"
        ```

    ??? variable bool "`embystat_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        embystat_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`embystat_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        embystat_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`embystat_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        embystat_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`embystat_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        embystat_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`embystat_role_traefik_certresolver`"

        ```yaml
        # Type: string
        embystat_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`embystat_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        embystat_role_traefik_enabled: true
        ```

    ??? variable bool "`embystat_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        embystat_role_traefik_api_enabled: false
        ```

    ??? variable string "`embystat_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        embystat_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`embystat_role_docker_container`"

        ```yaml
        # Type: string
        embystat_role_docker_container: "{{ embystat_name }}"
        ```

    ##### Image

    ??? variable bool "`embystat_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        embystat_role_docker_image_pull: true
        ```

    ??? variable string "`embystat_role_docker_image_repo`"

        ```yaml
        # Type: string
        embystat_role_docker_image_repo: "uping/embystat"
        ```

    ??? variable string "`embystat_role_docker_image_tag`"

        ```yaml
        # Type: string
        embystat_role_docker_image_tag: "beta-linux-x64"
        ```

    ??? variable string "`embystat_role_docker_image`"

        ```yaml
        # Type: string
        embystat_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='embystat') }}:{{ lookup('role_var', '_docker_image_tag', role='embystat') }}"
        ```

    ##### Volumes

    ??? variable list "`embystat_role_docker_volumes_default`"

        ```yaml
        # Type: list
        embystat_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='embystat') }}/config:/app/data"
        ```

    ??? variable list "`embystat_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        embystat_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`embystat_role_docker_hostname`"

        ```yaml
        # Type: string
        embystat_role_docker_hostname: "{{ embystat_name }}"
        ```

    ##### Networks

    ??? variable string "`embystat_role_docker_networks_alias`"

        ```yaml
        # Type: string
        embystat_role_docker_networks_alias: "{{ embystat_name }}"
        ```

    ??? variable list "`embystat_role_docker_networks_default`"

        ```yaml
        # Type: list
        embystat_role_docker_networks_default: []
        ```

    ??? variable list "`embystat_role_docker_networks_custom`"

        ```yaml
        # Type: list
        embystat_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`embystat_role_docker_restart_policy`"

        ```yaml
        # Type: string
        embystat_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`embystat_role_docker_state`"

        ```yaml
        # Type: string
        embystat_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`embystat_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        embystat_role_autoheal_enabled: true
        ```

    ??? variable string "`embystat_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        embystat_role_depends_on: ""
        ```

    ??? variable string "`embystat_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        embystat_role_depends_on_delay: "0"
        ```

    ??? variable string "`embystat_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        embystat_role_depends_on_healthchecks:
        ```

    ??? variable bool "`embystat_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        embystat_role_diun_enabled: true
        ```

    ??? variable bool "`embystat_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        embystat_role_dns_enabled: true
        ```

    ??? variable bool "`embystat_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        embystat_role_docker_controller: true
        ```

    ??? variable bool "`embystat_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        embystat_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`embystat_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        embystat_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`embystat_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        embystat_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`embystat_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        embystat_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`embystat_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        embystat_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`embystat_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        embystat_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`embystat_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        embystat_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`embystat_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        embystat_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`embystat_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        embystat_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`embystat_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        embystat_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            embystat_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "embystat2.{{ user.domain }}"
              - "embystat.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`embystat_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        embystat_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            embystat_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'embystat2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`embystat_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        embystat_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
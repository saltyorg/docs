---
hide:
  - tags
tags:
  - audiobookshelf
  - audiobooks
  - podcasts
---

# Audiobookshelf

## What is it?

[audiobookshelf](https://www.audiobookshelf.org/) is a self-hosted audio book and podcast server.

!!! info
    By default, the role is NOT protected behind your Authelia/SSO middleware.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.audiobookshelf.org/){: .header-icons } | [:octicons-link-16: Docs](https://www.audiobookshelf.org/docs){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/advplyr/audiobookshelf-web){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/advplyr/audiobookshelf){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-audiobookshelf

```

### 2. URL

- To access Audiobookshelf, visit `https://audiobookshelf._yourdomain.com_`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        audiobookshelf_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `audiobookshelf_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `audiobookshelf_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`audiobookshelf_name`"

        ```yaml
        # Type: string
        audiobookshelf_name: audiobookshelf
        ```

=== "Paths"

    ??? variable string "`audiobookshelf_role_paths_folder`"

        ```yaml
        # Type: string
        audiobookshelf_role_paths_folder: "{{ audiobookshelf_name }}"
        ```

    ??? variable string "`audiobookshelf_role_paths_location`"

        ```yaml
        # Type: string
        audiobookshelf_role_paths_location: "{{ server_appdata_path }}/{{ audiobookshelf_role_paths_folder }}"
        ```

    ??? variable bool "`audiobookshelf_role_paths_recursive`"

        ```yaml
        # Type: bool (true/false)
        audiobookshelf_role_paths_recursive: true
        ```

=== "Web"

    ??? variable string "`audiobookshelf_role_web_subdomain`"

        ```yaml
        # Type: string
        audiobookshelf_role_web_subdomain: "{{ audiobookshelf_name }}"
        ```

    ??? variable string "`audiobookshelf_role_web_domain`"

        ```yaml
        # Type: string
        audiobookshelf_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`audiobookshelf_role_web_port`"

        ```yaml
        # Type: string
        audiobookshelf_role_web_port: "80"
        ```

    ??? variable string "`audiobookshelf_role_web_url`"

        ```yaml
        # Type: string
        audiobookshelf_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='audiobookshelf') + '.' + lookup('role_var', '_web_domain', role='audiobookshelf')
                                      if (lookup('role_var', '_web_subdomain', role='audiobookshelf') | length > 0)
                                      else lookup('role_var', '_web_domain', role='audiobookshelf')) }}"
        ```

=== "DNS"

    ??? variable string "`audiobookshelf_role_dns_record`"

        ```yaml
        # Type: string
        audiobookshelf_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='audiobookshelf') }}"
        ```

    ??? variable string "`audiobookshelf_role_dns_zone`"

        ```yaml
        # Type: string
        audiobookshelf_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='audiobookshelf') }}"
        ```

    ??? variable bool "`audiobookshelf_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        audiobookshelf_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`audiobookshelf_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        audiobookshelf_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`audiobookshelf_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        audiobookshelf_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`audiobookshelf_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        audiobookshelf_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`audiobookshelf_role_traefik_certresolver`"

        ```yaml
        # Type: string
        audiobookshelf_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`audiobookshelf_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        audiobookshelf_role_traefik_enabled: true
        ```

=== "Docker"

    ##### Container

    ??? variable string "`audiobookshelf_role_docker_container`"

        ```yaml
        # Type: string
        audiobookshelf_role_docker_container: "{{ audiobookshelf_name }}"
        ```

    ##### Image

    ??? variable bool "`audiobookshelf_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        audiobookshelf_role_docker_image_pull: true
        ```

    ??? variable string "`audiobookshelf_role_docker_image_repo`"

        ```yaml
        # Type: string
        audiobookshelf_role_docker_image_repo: "ghcr.io/advplyr/audiobookshelf"
        ```

    ??? variable string "`audiobookshelf_role_docker_image_tag`"

        ```yaml
        # Type: string
        audiobookshelf_role_docker_image_tag: "latest"
        ```

    ??? variable string "`audiobookshelf_role_docker_image`"

        ```yaml
        # Type: string
        audiobookshelf_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='audiobookshelf') }}:{{ lookup('role_var', '_docker_image_tag', role='audiobookshelf') }}"
        ```

    ##### Envs

    ??? variable dict "`audiobookshelf_role_docker_envs_default`"

        ```yaml
        # Type: dict
        audiobookshelf_role_docker_envs_default: 
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`audiobookshelf_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        audiobookshelf_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`audiobookshelf_role_docker_volumes_default`"

        ```yaml
        # Type: list
        audiobookshelf_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='audiobookshelf') }}/config:/config"
          - "{{ lookup('role_var', '_paths_location', role='audiobookshelf') }}/metadata:/metadata"
          - "/mnt/unionfs/Media/Audiobooks:/audiobooks"
          - "/mnt/unionfs/Media/Podcasts:/podcasts"
        ```

    ??? variable list "`audiobookshelf_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        audiobookshelf_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`audiobookshelf_role_docker_hostname`"

        ```yaml
        # Type: string
        audiobookshelf_role_docker_hostname: "{{ audiobookshelf_name }}"
        ```

    ##### Networks

    ??? variable string "`audiobookshelf_role_docker_networks_alias`"

        ```yaml
        # Type: string
        audiobookshelf_role_docker_networks_alias: "{{ audiobookshelf_name }}"
        ```

    ??? variable list "`audiobookshelf_role_docker_networks_default`"

        ```yaml
        # Type: list
        audiobookshelf_role_docker_networks_default: []
        ```

    ??? variable list "`audiobookshelf_role_docker_networks_custom`"

        ```yaml
        # Type: list
        audiobookshelf_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`audiobookshelf_role_docker_restart_policy`"

        ```yaml
        # Type: string
        audiobookshelf_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`audiobookshelf_role_docker_state`"

        ```yaml
        # Type: string
        audiobookshelf_role_docker_state: started
        ```

    ##### User

    ??? variable string "`audiobookshelf_role_docker_user`"

        ```yaml
        # Type: string
        audiobookshelf_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`audiobookshelf_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        audiobookshelf_role_autoheal_enabled: true
        ```

    ??? variable string "`audiobookshelf_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        audiobookshelf_role_depends_on: ""
        ```

    ??? variable string "`audiobookshelf_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        audiobookshelf_role_depends_on_delay: "0"
        ```

    ??? variable string "`audiobookshelf_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        audiobookshelf_role_depends_on_healthchecks:
        ```

    ??? variable bool "`audiobookshelf_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        audiobookshelf_role_diun_enabled: true
        ```

    ??? variable bool "`audiobookshelf_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        audiobookshelf_role_dns_enabled: true
        ```

    ??? variable bool "`audiobookshelf_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        audiobookshelf_role_docker_controller: true
        ```

    ??? variable bool "`audiobookshelf_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        audiobookshelf_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`audiobookshelf_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        audiobookshelf_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`audiobookshelf_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        audiobookshelf_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`audiobookshelf_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        audiobookshelf_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`audiobookshelf_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        audiobookshelf_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`audiobookshelf_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        audiobookshelf_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`audiobookshelf_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        audiobookshelf_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`audiobookshelf_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        audiobookshelf_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`audiobookshelf_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        audiobookshelf_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`audiobookshelf_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        audiobookshelf_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            audiobookshelf_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "audiobookshelf2.{{ user.domain }}"
              - "audiobookshelf.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`audiobookshelf_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        audiobookshelf_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            audiobookshelf_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'audiobookshelf2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`audiobookshelf_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        audiobookshelf_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
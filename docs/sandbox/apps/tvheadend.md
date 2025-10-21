---
hide:
  - tags
tags:
  - tvheadend
  - tv
  - streaming
---

# Tvheadend

## What is it?

[Tvheadend](https://tvheadend.org/) is a TV streaming server and digital video recorder.

It supports the following inputs:

- DVB-C(2)
- DVB-T(2)
- DVB-S(2)
- ATSC
- SAT>IP
- HDHomeRun
- IPTV
  - UDP
  - HTTP

It supports the following outputs:

HTTP
HTSP (own protocol)
SAT>IP

!!! info
    By default, the role **IS** protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://tvheadend.org/){: .header-icons } | [:octicons-link-16: Docs](https://docs.tvheadend.org/documentation){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/tvheadend/tvheadend){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/thealhu/tvheadend){: .header-icons }|

Recommended install types: Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-tvheadend

```

### 2. URL

- To access Tvheadend, visit `https://tvheadend._yourdomain.com_`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        tvheadend_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `tvheadend_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `tvheadend_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`tvheadend_name`"

        ```yaml
        # Type: string
        tvheadend_name: tvheadend
        ```

=== "Paths"

    ??? variable string "`tvheadend_role_paths_folder`"

        ```yaml
        # Type: string
        tvheadend_role_paths_folder: "{{ tvheadend_name }}"
        ```

    ??? variable string "`tvheadend_role_paths_location`"

        ```yaml
        # Type: string
        tvheadend_role_paths_location: "{{ server_appdata_path }}/{{ tvheadend_role_paths_folder }}"
        ```

    ??? variable string "`tvheadend_role_paths_downloads_location`"

        ```yaml
        # Type: string
        tvheadend_role_paths_downloads_location: "{{ downloads_root_path }}/{{ tvheadend_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`tvheadend_role_web_subdomain`"

        ```yaml
        # Type: string
        tvheadend_role_web_subdomain: "{{ tvheadend_name }}"
        ```

    ??? variable string "`tvheadend_role_web_domain`"

        ```yaml
        # Type: string
        tvheadend_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`tvheadend_role_web_port`"

        ```yaml
        # Type: string
        tvheadend_role_web_port: "9981"
        ```

    ??? variable string "`tvheadend_role_web_url`"

        ```yaml
        # Type: string
        tvheadend_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='tvheadend') + '.' + lookup('role_var', '_web_domain', role='tvheadend')
                                 if (lookup('role_var', '_web_subdomain', role='tvheadend') | length > 0)
                                 else lookup('role_var', '_web_domain', role='tvheadend')) }}"
        ```

=== "DNS"

    ??? variable string "`tvheadend_role_dns_record`"

        ```yaml
        # Type: string
        tvheadend_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='tvheadend') }}"
        ```

    ??? variable string "`tvheadend_role_dns_zone`"

        ```yaml
        # Type: string
        tvheadend_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='tvheadend') }}"
        ```

    ??? variable bool "`tvheadend_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        tvheadend_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`tvheadend_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        tvheadend_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`tvheadend_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        tvheadend_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`tvheadend_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        tvheadend_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`tvheadend_role_traefik_certresolver`"

        ```yaml
        # Type: string
        tvheadend_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`tvheadend_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        tvheadend_role_traefik_enabled: true
        ```

    ??? variable bool "`tvheadend_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        tvheadend_role_traefik_api_enabled: false
        ```

    ??? variable string "`tvheadend_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        tvheadend_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`tvheadend_role_docker_container`"

        ```yaml
        # Type: string
        tvheadend_role_docker_container: "{{ tvheadend_name }}"
        ```

    ##### Image

    ??? variable bool "`tvheadend_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        tvheadend_role_docker_image_pull: true
        ```

    ??? variable string "`tvheadend_role_docker_image_repo`"

        ```yaml
        # Type: string
        tvheadend_role_docker_image_repo: "lscr.io/linuxserver/tvheadend"
        ```

    ??? variable string "`tvheadend_role_docker_image_tag`"

        ```yaml
        # Type: string
        tvheadend_role_docker_image_tag: "latest"
        ```

    ??? variable string "`tvheadend_role_docker_image`"

        ```yaml
        # Type: string
        tvheadend_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='tvheadend') }}:{{ lookup('role_var', '_docker_image_tag', role='tvheadend') }}"
        ```

    ##### Envs

    ??? variable dict "`tvheadend_role_docker_envs_default`"

        ```yaml
        # Type: dict
        tvheadend_role_docker_envs_default: 
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
        ```

    ??? variable dict "`tvheadend_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        tvheadend_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`tvheadend_role_docker_volumes_default`"

        ```yaml
        # Type: list
        tvheadend_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='tvheadend') }}:/config"
          - "{{ lookup('role_var', '_paths_downloads_location', role='tvheadend') }}:/recordings"
        ```

    ??? variable list "`tvheadend_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        tvheadend_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`tvheadend_role_docker_hostname`"

        ```yaml
        # Type: string
        tvheadend_role_docker_hostname: "{{ tvheadend_name }}"
        ```

    ##### Networks

    ??? variable string "`tvheadend_role_docker_networks_alias`"

        ```yaml
        # Type: string
        tvheadend_role_docker_networks_alias: "{{ tvheadend_name }}"
        ```

    ??? variable list "`tvheadend_role_docker_networks_default`"

        ```yaml
        # Type: list
        tvheadend_role_docker_networks_default: []
        ```

    ??? variable list "`tvheadend_role_docker_networks_custom`"

        ```yaml
        # Type: list
        tvheadend_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`tvheadend_role_docker_restart_policy`"

        ```yaml
        # Type: string
        tvheadend_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`tvheadend_role_docker_state`"

        ```yaml
        # Type: string
        tvheadend_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`tvheadend_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        tvheadend_role_autoheal_enabled: true
        ```

    ??? variable string "`tvheadend_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        tvheadend_role_depends_on: ""
        ```

    ??? variable string "`tvheadend_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        tvheadend_role_depends_on_delay: "0"
        ```

    ??? variable string "`tvheadend_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        tvheadend_role_depends_on_healthchecks:
        ```

    ??? variable bool "`tvheadend_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        tvheadend_role_diun_enabled: true
        ```

    ??? variable bool "`tvheadend_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        tvheadend_role_dns_enabled: true
        ```

    ??? variable bool "`tvheadend_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        tvheadend_role_docker_controller: true
        ```

    ??? variable bool "`tvheadend_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        tvheadend_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`tvheadend_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        tvheadend_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`tvheadend_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        tvheadend_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`tvheadend_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        tvheadend_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`tvheadend_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        tvheadend_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`tvheadend_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        tvheadend_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`tvheadend_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        tvheadend_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`tvheadend_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        tvheadend_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            tvheadend_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "tvheadend2.{{ user.domain }}"
              - "tvheadend.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`tvheadend_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        tvheadend_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            tvheadend_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'tvheadend2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`tvheadend_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        tvheadend_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
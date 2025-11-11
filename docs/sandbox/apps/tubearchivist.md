---
icon: material/docker
hide:
  - tags
tags:
  - tubearchivist
  - media
  - youtube
---

# Tubearchivist

## Overview

[Tubearchivist](https://www.tubearchivist.com/) is a self hosted Youtube media server.

- Subscribe to your favorite YouTube channels
- Download Videos using yt-dlp
- Index and make videos searchable
- Play videos
- Keep track of viewed and unviewed videos

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.tubearchivist.com/){: .Teader-icons target=_blTnk rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/tubearchivist/tubearchivist/wiki){: .header-icons taTget=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/tubearchivist/tubearchivist){: .header-icoTs target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/bbilly1/tubearchivist){: .header-icons }|

Recommended install types: Feederbox, Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-tubearchivist

```

### 2. URL

- To access tubearchivist, visit <https://tubearchivist.iYOUR_DOMAIN_NAMEi>

### 3. Setup

- Default login:

  ``` { .yaml}

  Username: "your user from accounts.yml"
  Password: your_normal_password

  ```

!!!note
   Tubearchivist adds the downloaded media to `/mnt/unionfs/downloads/tubearchivist/YT_CHANNEL_NAME`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    tubearchivist_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `tubearchivist_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `tubearchivist_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`tubearchivist_name`"

        ```yaml
        # Type: string
        tubearchivist_name: tubearchivist
        ```

=== "Settings"

    ??? variable string "`tubearchivist_role_enable_cast`"

        ```yaml
        # Type: string
        tubearchivist_role_enable_cast: "false"
        ```

=== "Paths"

    ??? variable string "`tubearchivist_role_paths_folder`"

        ```yaml
        # Type: string
        tubearchivist_role_paths_folder: "{{ tubearchivist_name }}"
        ```

    ??? variable string "`tubearchivist_role_paths_location`"

        ```yaml
        # Type: string
        tubearchivist_role_paths_location: "{{ server_appdata_path }}/{{ tubearchivist_role_paths_folder }}/app"
        ```

    ??? variable string "`tubearchivist_role_paths_downloads_location`"

        ```yaml
        # Type: string
        tubearchivist_role_paths_downloads_location: "{{ downloads_root_path }}/{{ tubearchivist_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`tubearchivist_role_web_subdomain`"

        ```yaml
        # Type: string
        tubearchivist_role_web_subdomain: "{{ tubearchivist_name }}"
        ```

    ??? variable string "`tubearchivist_role_web_domain`"

        ```yaml
        # Type: string
        tubearchivist_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`tubearchivist_role_web_port`"

        ```yaml
        # Type: string
        tubearchivist_role_web_port: "8000"
        ```

    ??? variable string "`tubearchivist_role_web_url`"

        ```yaml
        # Type: string
        tubearchivist_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='tubearchivist') + '.' + lookup('role_var', '_web_domain', role='tubearchivist')
                                     if (lookup('role_var', '_web_subdomain', role='tubearchivist') | length > 0)
                                     else lookup('role_var', '_web_domain', role='tubearchivist')) }}"
        ```

=== "DNS"

    ??? variable string "`tubearchivist_role_dns_record`"

        ```yaml
        # Type: string
        tubearchivist_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='tubearchivist') }}"
        ```

    ??? variable string "`tubearchivist_role_dns_zone`"

        ```yaml
        # Type: string
        tubearchivist_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='tubearchivist') }}"
        ```

    ??? variable bool "`tubearchivist_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`tubearchivist_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        tubearchivist_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`tubearchivist_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        tubearchivist_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`tubearchivist_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        tubearchivist_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`tubearchivist_role_traefik_certresolver`"

        ```yaml
        # Type: string
        tubearchivist_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`tubearchivist_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_traefik_enabled: true
        ```

    ??? variable bool "`tubearchivist_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_traefik_api_enabled: true
        ```

    ??? variable string "`tubearchivist_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        tubearchivist_role_traefik_api_endpoint: "PathPrefix(`/api`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`tubearchivist_role_docker_container`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_container: "{{ tubearchivist_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`tubearchivist_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_docker_image_pull: true
        ```

    ??? variable string "`tubearchivist_role_docker_image_tag`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_image_tag: "v0.4.13"
        ```

    ??? variable string "`tubearchivist_role_docker_image_repo`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_image_repo: "bbilly1/tubearchivist"
        ```

    ??? variable string "`tubearchivist_role_docker_image`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='tubearchivist') }}:{{ lookup('role_var', '_docker_image_tag', role='tubearchivist') }}"
        ```

    <h5>Envs</h5>

    ??? variable string "`tubearchivist_role_docker_envs_http_header`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_envs_http_header: "{{ 'HTTP_REMOTE_USER'
                                                     if ('authelia' in lookup('role_var', '_traefik_sso_middleware', role='tubearchivist'))
                                                     else ('HTTP_X_AUTHENTIK_USERNAME'
                                                          if ('authentik' in lookup('role_var', '_traefik_sso_middleware', role='tubearchivist'))
                                                          else '') }}"
        ```

    ??? variable dict "`tubearchivist_role_docker_envs_default`"

        ```yaml
        # Type: dict
        tubearchivist_role_docker_envs_default: 
          TZ: "{{ tz }}"
          ES_URL: "http://{{ tubearchivist_name }}-elasticsearch:9200"
          REDIS_HOST: "{{ tubearchivist_name }}-redis"
          HOST_UID: "{{ uid }}"
          HOST_GID: "{{ gid }}"
          TA_HOST: "localhost 127.0.0.1 {{ tubearchivist_name }} {{ lookup('role_var', '_web_subdomain', role='tubearchivist') + '.' + lookup('role_var', '_web_domain', role='tubearchivist') }} {{ lookup('role_var', '_web_url', role='tubearchivist') }}"
          TA_ENABLE_AUTH_PROXY: "{{ 'true' if (lookup('role_var', '_traefik_sso_middleware', role='tubearchivist') | length > 0) else omit }}"
          TA_AUTH_PROXY_USERNAME_HEADER: "{{ lookup('role_var', '_docker_envs_http_header', role='tubearchivist') if (lookup('role_var', '_traefik_sso_middleware', role='tubearchivist') | length > 0) else omit }}"
          TA_USERNAME: "{{ user.name }}"
          TA_PASSWORD: "{{ user.pass }}"
          ELASTIC_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='elasticsearch') }}"
          ENABLE_CAST: "{{ lookup('role_var', '_enable_cast', role='tubearchivist') }}"
        ```

    ??? variable dict "`tubearchivist_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        tubearchivist_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`tubearchivist_role_docker_volumes_default`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_downloads_location', role='tubearchivist') }}/:/youtube"
          - "{{ lookup('role_var', '_paths_location', role='tubearchivist') }}/cache:/cache"
        ```

    ??? variable list "`tubearchivist_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`tubearchivist_role_docker_hostname`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_hostname: "{{ tubearchivist_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`tubearchivist_role_docker_networks_alias`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_networks_alias: "{{ tubearchivist_name }}"
        ```

    ??? variable list "`tubearchivist_role_docker_networks_default`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_networks_default: []
        ```

    ??? variable list "`tubearchivist_role_docker_networks_custom`"

        ```yaml
        # Type: list
        tubearchivist_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`tubearchivist_role_docker_restart_policy`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`tubearchivist_role_docker_state`"

        ```yaml
        # Type: string
        tubearchivist_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`tubearchivist_role_depends_on`"

        ```yaml
        # Type: string
        tubearchivist_role_depends_on: "{{ tubearchivist_name }}-elasticsearch,{{ tubearchivist_name }}-redis"
        ```

    ??? variable string "`tubearchivist_role_depends_on_delay`"

        ```yaml
        # Type: string
        tubearchivist_role_depends_on_delay: "0"
        ```

    ??? variable string "`tubearchivist_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        tubearchivist_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`tubearchivist_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        tubearchivist_role_autoheal_enabled: true
        ```

    ??? variable string "`tubearchivist_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        tubearchivist_role_depends_on: ""
        ```

    ??? variable string "`tubearchivist_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        tubearchivist_role_depends_on_delay: "0"
        ```

    ??? variable string "`tubearchivist_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        tubearchivist_role_depends_on_healthchecks:
        ```

    ??? variable bool "`tubearchivist_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        tubearchivist_role_diun_enabled: true
        ```

    ??? variable bool "`tubearchivist_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        tubearchivist_role_dns_enabled: true
        ```

    ??? variable bool "`tubearchivist_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        tubearchivist_role_docker_controller: true
        ```

    ??? variable bool "`tubearchivist_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_docker_volumes_download:
        ```

    ??? variable bool "`tubearchivist_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        tubearchivist_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`tubearchivist_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        tubearchivist_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`tubearchivist_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        tubearchivist_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`tubearchivist_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        tubearchivist_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`tubearchivist_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`tubearchivist_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        tubearchivist_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`tubearchivist_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        tubearchivist_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`tubearchivist_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        tubearchivist_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`tubearchivist_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        tubearchivist_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`tubearchivist_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        tubearchivist_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            tubearchivist_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "tubearchivist2.{{ user.domain }}"
              - "tubearchivist.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`tubearchivist_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        tubearchivist_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            tubearchivist_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'tubearchivist2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`tubearchivist_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        tubearchivist_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
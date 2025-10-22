---
hide:
  - tags
tags:
  - tubearchivist
  - media
  - youtube
---

# Tubearchivist

## What is it?

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

- To access tubearchivist, visit `https://tubearchivist.xDOMAIN_NAMEx`

### 3. Setup

- Default login:

  ``` { .yaml}

  Username: "your user from accounts.yml"
  Password: your_normal_password

  ```

!!!note
   Tubearchivist adds the downloaded media to `/mnt/unionfs/downloads/tubearchivist/YT_CHANNEL_NAME`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        tubearchivist_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `tubearchivist_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `tubearchivist_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    tubearchivist_name: tubearchivist

    ```

??? example "Settings"

    ```yaml
    # Type: string
    tubearchivist_role_enable_cast: "false"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    tubearchivist_role_paths_folder: "{{ tubearchivist_name }}"

    # Type: string
    tubearchivist_role_paths_location: "{{ server_appdata_path }}/{{ tubearchivist_role_paths_folder }}/app"

    # Type: string
    tubearchivist_role_paths_downloads_location: "{{ downloads_root_path }}/{{ tubearchivist_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    tubearchivist_role_web_subdomain: "{{ tubearchivist_name }}"

    # Type: string
    tubearchivist_role_web_domain: "{{ user.domain }}"

    # Type: string
    tubearchivist_role_web_port: "8000"

    # Type: string
    tubearchivist_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='tubearchivist') + '.' + lookup('role_var', '_web_domain', role='tubearchivist')
                                 if (lookup('role_var', '_web_subdomain', role='tubearchivist') | length > 0)
                                 else lookup('role_var', '_web_domain', role='tubearchivist')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    tubearchivist_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='tubearchivist') }}"

    # Type: string
    tubearchivist_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='tubearchivist') }}"

    # Type: bool (true/false)
    tubearchivist_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    tubearchivist_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    tubearchivist_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    tubearchivist_role_traefik_middleware_custom: ""

    # Type: string
    tubearchivist_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    tubearchivist_role_traefik_enabled: true

    # Type: bool (true/false)
    tubearchivist_role_traefik_api_enabled: true

    # Type: string
    tubearchivist_role_traefik_api_endpoint: "PathPrefix(`/api`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    tubearchivist_role_docker_container: "{{ tubearchivist_name }}"

    # Image
    # Type: bool (true/false)
    tubearchivist_role_docker_image_pull: true

    # Type: string
    tubearchivist_role_docker_image_tag: "v0.4.13"

    # Type: string
    tubearchivist_role_docker_image_repo: "bbilly1/tubearchivist"

    # Type: string
    tubearchivist_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='tubearchivist') }}:{{ lookup('role_var', '_docker_image_tag', role='tubearchivist') }}"

    # Envs
    # Type: string
    tubearchivist_role_docker_envs_http_header: "{{ 'HTTP_REMOTE_USER'
                                                 if ('authelia' in lookup('role_var', '_traefik_sso_middleware', role='tubearchivist'))
                                                 else ('HTTP_X_AUTHENTIK_USERNAME'
                                                      if ('authentik' in lookup('role_var', '_traefik_sso_middleware', role='tubearchivist'))
                                                      else '') }}"

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

    # Type: dict
    tubearchivist_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    tubearchivist_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_downloads_location', role='tubearchivist') }}/:/youtube"
      - "{{ lookup('role_var', '_paths_location', role='tubearchivist') }}/cache:/cache"

    # Type: list
    tubearchivist_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    tubearchivist_role_docker_hostname: "{{ tubearchivist_name }}"

    # Networks
    # Type: string
    tubearchivist_role_docker_networks_alias: "{{ tubearchivist_name }}"

    # Type: list
    tubearchivist_role_docker_networks_default: []

    # Type: list
    tubearchivist_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    tubearchivist_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    tubearchivist_role_docker_state: started

    # Dependencies
    # Type: string
    tubearchivist_role_depends_on: "{{ tubearchivist_name }}-elasticsearch,{{ tubearchivist_name }}-redis"

    # Type: string
    tubearchivist_role_depends_on_delay: "0"

    # Type: string
    tubearchivist_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    tubearchivist_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    tubearchivist_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    tubearchivist_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    tubearchivist_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    tubearchivist_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    tubearchivist_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    tubearchivist_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    tubearchivist_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    tubearchivist_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    tubearchivist_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    tubearchivist_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    tubearchivist_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    tubearchivist_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    tubearchivist_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    tubearchivist_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    tubearchivist_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    tubearchivist_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        tubearchivist_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "tubearchivist2.{{ user.domain }}"
          - "tubearchivist.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        tubearchivist_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'tubearchivist2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

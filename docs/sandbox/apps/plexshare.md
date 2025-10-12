---
hide:
  - tags
tags:
  - plexshare
  - plex
  - sharing
---

# PlexShare

## What is it?

[PlexShare](https://chewbaka69.github.io/PlexShare/) is a standalone web application that provides management of local users and multiple Plex servers with their libraries. It allows users to access libraries from all registered servers through a single interface without requiring plex.tv registration.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://chewbaka69.github.io/PlexShare/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Chewbaka69/PlexShare){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/chewbaka/plexshare){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-plexshare
```

### 2. URL

- To access PlexShare, visit `https://plexshare._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        plexshare_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `plexshare_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `plexshare_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    plexshare_name: plexshare

    ```

??? example "Paths"

    ```yaml
    # Type: string
    plexshare_role_paths_folder: "{{ plexshare_name }}"

    # Type: string
    plexshare_role_paths_location: "{{ server_appdata_path }}/{{ plexshare_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    plexshare_role_web_subdomain: "{{ plexshare_name }}"

    # Type: string
    plexshare_role_web_domain: "{{ user.domain }}"

    # Type: string
    plexshare_role_web_port: "80"

    # Type: string
    plexshare_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='plexshare') + '.' + lookup('role_var', '_web_domain', role='plexshare')
                             if (lookup('role_var', '_web_subdomain', role='plexshare') | length > 0)
                             else lookup('role_var', '_web_domain', role='plexshare')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    plexshare_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='plexshare') }}"

    # Type: string
    plexshare_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='plexshare') }}"

    # Type: bool (true/false)
    plexshare_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    plexshare_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    plexshare_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    plexshare_role_traefik_middleware_custom: ""

    # Type: string
    plexshare_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    plexshare_role_traefik_enabled: true

    # Type: bool (true/false)
    plexshare_role_traefik_api_enabled: false

    # Type: string
    plexshare_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    plexshare_role_docker_container: "{{ plexshare_name }}"

    # Image
    # Type: bool (true/false)
    plexshare_role_docker_image_pull: true

    # Type: string
    plexshare_role_docker_image_tag: "latest"

    # Type: string
    plexshare_role_docker_image_repo: "chewbaka/plexshare"

    # Type: string
    plexshare_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='plexshare') }}:{{ lookup('role_var', '_docker_image_tag', role='plexshare') }}"

    # Envs
    # Type: dict
    plexshare_role_docker_envs_default: 
      TZ: "{{ tz }}"
      WEB_DOCUMENT_ROOT: "/app/public"
      WEB_DOCUMENT_INDEX: "index.php"
      LOG_STDOUT: "./var/log/plexshare.stdout.log"
      LOG_STDERR: "./var/log/plexshare.stderr.log"
      PHP_POST_MAX_SIZE: "20M"
      PHP_MEMORY_LIMIT: "521M"
      PHP_MAX_EXECUTION_TIME: "300"
      PHP_DATE_TIMEZONE: "{{ tz }}"
      COMPOSER_VERSION: "1"
      BASE_URL: "{{ lookup('role_var', '_web_url', role='plexshare') }}/"

    # Type: dict
    plexshare_role_docker_envs_custom: {}

    # Hostname
    # Type: string
    plexshare_role_docker_hostname: "{{ plexshare_name }}"

    # Networks
    # Type: string
    plexshare_role_docker_networks_alias: "{{ plexshare_name }}"

    # Type: list
    plexshare_role_docker_networks_default: []

    # Type: list
    plexshare_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    plexshare_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    plexshare_role_docker_state: started

    # Dependencies
    # Type: string
    plexshare_role_depends_on: "{{ plexshare_name }}-mariadb"

    # Type: string
    plexshare_role_depends_on_delay: "0"

    # Type: string
    plexshare_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    plexshare_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    plexshare_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    plexshare_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    plexshare_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    plexshare_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    plexshare_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    plexshare_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    plexshare_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    plexshare_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    plexshare_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    plexshare_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    plexshare_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    plexshare_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    plexshare_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    plexshare_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    plexshare_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    plexshare_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        plexshare_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "plexshare2.{{ user.domain }}"
          - "plexshare.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        plexshare_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'plexshare2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

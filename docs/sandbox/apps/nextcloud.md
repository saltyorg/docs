---
hide:
  - tags
tags:
  - nextcloud
  - productivity
  - cloud
---

# Nextcloud

## What is it?

[Nextcloud](https://nextcloud.com/) is safe home for all your data. Access & share your files, calendars, contacts, mail & more from any device, on your terms.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://nextcloud.com/){: .header-icons } | [:octicons-link-16: Docs](https://docs.nextcloud.com/server/latest/admin_manual/contents.html){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/nextcloud/docker){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/nextcloud){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-nextcloud

```

### 2. URL

- To access Nextcloud, visit `https://nextcloud.xDOMAIN_NAMEx`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        nextcloud_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `nextcloud_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `nextcloud_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    nextcloud_name: nextcloud

    ```

??? example "Settings"

    ```yaml
    # Type: string
    nextcloud_role_data_directory: "/var/www/html/data"

    # Type: string
    nextcloud_role_php_memory_limit: "512M"

    # Type: string
    nextcloud_role_php_upload_limit: "512M"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    nextcloud_role_paths_folder: "{{ nextcloud_name }}"

    # Type: string
    nextcloud_role_paths_location: "{{ server_appdata_path }}/{{ nextcloud_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    nextcloud_role_web_subdomain: "{{ nextcloud_name }}"

    # Type: string
    nextcloud_role_web_domain: "{{ user.domain }}"

    # Type: string
    nextcloud_role_web_port: "80"

    # Type: string
    nextcloud_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='nextcloud') + '.' + lookup('role_var', '_web_domain', role='nextcloud')
                             if (lookup('role_var', '_web_subdomain', role='nextcloud') | length > 0)
                             else lookup('role_var', '_web_domain', role='nextcloud')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    nextcloud_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='nextcloud') }}"

    # Type: string
    nextcloud_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='nextcloud') }}"

    # Type: bool (true/false)
    nextcloud_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    nextcloud_role_traefik_sso_middleware: ""

    # Type: string
    nextcloud_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    nextcloud_role_traefik_middleware_custom: ""

    # Type: string
    nextcloud_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    nextcloud_role_traefik_enabled: true

    # Type: bool (true/false)
    nextcloud_role_traefik_api_enabled: false

    # Type: string
    nextcloud_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    nextcloud_role_docker_container: "{{ nextcloud_name }}"

    # Image
    # Type: bool (true/false)
    nextcloud_role_docker_image_pull: true

    # Type: string
    nextcloud_role_docker_image_tag: "latest"

    # Type: string
    nextcloud_role_docker_image_repo: "nextcloud"

    # Type: string
    nextcloud_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='nextcloud') }}:{{ lookup('role_var', '_docker_image_tag', role='nextcloud') }}"

    # Envs
    # Type: dict
    nextcloud_role_docker_envs_default: 
      TZ: "{{ tz }}"
      NEXTCLOUD_ADMIN_USER: "{{ user.name }}"
      NEXTCLOUD_ADMIN_PASSWORD: "{{ user.pass }}"
      NEXTCLOUD_TRUSTED_DOMAINS: "{{ lookup('role_var', '_web_subdomain', role='nextcloud') + '.' + lookup('role_var', '_web_domain', role='nextcloud') }}"
      NEXTCLOUD_DATA_DIR: "{{ lookup('role_var', '_data_directory', role='nextcloud') }}"
      MYSQL_DATABASE: "nextcloud"
      MYSQL_USER: "root"
      MYSQL_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='mariadb') }}"
      MYSQL_HOST: "mariadb"
      OVERWRITEHOST: "{{ lookup('role_var', '_web_subdomain', role='nextcloud') + '.' + lookup('role_var', '_web_domain', role='nextcloud') }}"
      OVERWRITEPROTOCOL: "https"
      OVERWRITECLIURL: "{{ lookup('role_var', '_web_url', role='nextcloud') }}"
      PHP_MEMORY_LIMIT: "{{ lookup('role_var', '_php_memory_limit', role='nextcloud') }}"
      PHP_UPLOAD_LIMIT: "{{ lookup('role_var', '_php_upload_limit', role='nextcloud') }}"
      TRUSTED_PROXIES: "172.19.0.0/16"

    # Type: dict
    nextcloud_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    nextcloud_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='nextcloud') }}:/var/www/html"

    # Type: list
    nextcloud_role_docker_volumes_custom: []

    # Labels
    # Type: dict
    nextcloud_role_docker_labels_default: 
      traefik.http.middlewares.nextcloud-caldav.replacepathregex.regex: "^/.well-known/ca(l|rd)dav"
      traefik.http.middlewares.nextcloud-caldav.replacepathregex.replacement: "/remote.php/dav/"

    # Type: dict
    nextcloud_role_docker_labels_custom: {}

    # Hostname
    # Type: string
    nextcloud_role_docker_hostname: "{{ nextcloud_name }}"

    # Networks
    # Type: string
    nextcloud_role_docker_networks_alias: "{{ nextcloud_name }}"

    # Type: list
    nextcloud_role_docker_networks_default: []

    # Type: list
    nextcloud_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    nextcloud_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    nextcloud_role_docker_state: started

    # User
    # Type: string
    nextcloud_role_docker_user: "{{ uid }}:{{ gid }}"

    # Dependencies
    # Type: string
    nextcloud_role_depends_on: "mariadb"

    # Type: string
    nextcloud_role_depends_on_delay: "0"

    # Type: string
    nextcloud_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    nextcloud_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    nextcloud_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    nextcloud_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    nextcloud_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    nextcloud_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    nextcloud_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    nextcloud_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    nextcloud_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    nextcloud_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    nextcloud_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    nextcloud_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    nextcloud_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    nextcloud_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    nextcloud_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    nextcloud_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    nextcloud_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    nextcloud_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        nextcloud_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "nextcloud2.{{ user.domain }}"
          - "nextcloud.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        nextcloud_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'nextcloud2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

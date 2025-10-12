---
hide:
  - tags
tags:
  - rocketchat
  - communication
  - chat
---

# rocketchat

## THIS DOCUMENTATION IS NOT YET COMPLETED

## What is it?

[rocketchat](https://rocketchat.url) is a...

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://rocketchat.url){: .header-icons } | [:octicons-link-16: Docs](https://rocketchat.docs.url){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/rocketchat/rocketchat){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/rocketchat/rocketchat){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-rocketchat

```

### 2. URL

- To access rocketchat, visit `https://rocketchat._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        rocketchat_mongodb_role_docker_image_tag: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `rocketchat_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `rocketchat_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    rocketchat_name: rocketchat

    ```

??? example "Settings"

    ```yaml
    # Type: string
    rocketchat_mongodb_role_docker_image_tag: "6"

    # Type: list
    rocketchat_mongodb_role_docker_commands: 
      - "mongod --oplogSize 128 --replSet rs0"

    # Type: list
    rocketchat_mongodb_role_docker_volumes_custom: 
      - "{{ lookup('role_var', '_paths_location', role='rocketchat') }}/init-mongo.js:/docker-entrypoint-initdb.d/init-mongo.js:ro"

    # Type: string
    rockatchat_mongodb_role_paths_location: "{{ lookup('role_var', '_paths_location', role='rocketchat') }}/mongo"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    rocketchat_role_paths_folder: "{{ rocketchat_name }}"

    # Type: string
    rocketchat_role_paths_location: "{{ server_appdata_path }}/{{ rocketchat_role_paths_folder }}"

    # Type: string
    rocketchat_role_paths_config_location: "{{ rocketchat_role_paths_location }}/env"

    ```

??? example "Web"

    ```yaml
    # Type: string
    rocketchat_role_web_subdomain: "{{ rocketchat_name }}"

    # Type: string
    rocketchat_role_web_domain: "{{ user.domain }}"

    # Type: string
    rocketchat_role_web_port: "3000"

    # Type: string
    rocketchat_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='rocketchat') + '.' + lookup('role_var', '_web_domain', role='rocketchat')
                              if (lookup('role_var', '_web_subdomain', role='rocketchat') | length > 0)
                              else lookup('role_var', '_web_domain', role='rocketchat')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    rocketchat_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='rocketchat') }}"

    # Type: string
    rocketchat_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='rocketchat') }}"

    # Type: bool (true/false)
    rocketchat_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    rocketchat_role_traefik_sso_middleware: ""

    # Type: string
    rocketchat_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    rocketchat_role_traefik_middleware_custom: ""

    # Type: string
    rocketchat_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    rocketchat_role_traefik_enabled: true

    # Type: bool (true/false)
    rocketchat_role_traefik_api_enabled: false

    # Type: string
    rocketchat_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    rocketchat_role_docker_container: "{{ rocketchat_name }}"

    # Image
    # Type: bool (true/false)
    rocketchat_role_docker_image_pull: true

    # Type: string
    rocketchat_role_docker_image_tag: "latest"

    # Type: string
    rocketchat_role_docker_image_repo: "rocketchat/rocket.chat"

    # Type: string
    rocketchat_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='rocketchat') }}:{{ lookup('role_var', '_docker_image_tag', role='rocketchat') }}"

    # Envs
    # Type: dict
    rocketchat_role_docker_envs_default: 
      TZ: "{{ tz }}"
      ROOT_URL: "{{ lookup('role_var', '_web_url', role='rocketchat') }}"
      MONGO_URL: "mongodb://rocketchat-mongo:27017/rocketchat?replicaSet=rs0&directConnection=true"
      MONGO_OPLOG_URL: "mongodb://rocketchat-mongo:27017/local?replicaSet=rs0&directConnection=true"
      DEPLOY_METHOD: "docker"

    # Type: dict
    rocketchat_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    rocketchat_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='rocketchat') }}/uploads:/app/uploads"

    # Type: list
    rocketchat_role_docker_volumes_custom: []

    # Mounts
    # Type: list
    rocketchat_role_docker_mounts_default: 
      - target: /tmp
        type: tmpfs

    # Type: list
    rocketchat_role_docker_mounts_custom: []

    # Hostname
    # Type: string
    rocketchat_role_docker_hostname: "{{ rocketchat_name }}"

    # Networks
    # Type: string
    rocketchat_role_docker_networks_alias: "{{ rocketchat_name }}"

    # Type: list
    rocketchat_role_docker_networks_default: []

    # Type: list
    rocketchat_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    rocketchat_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    rocketchat_role_docker_state: started

    # Dependencies
    # Type: string
    rocketchat_role_depends_on: "rocketchat_db"

    # Type: string
    rocketchat_role_depends_on_delay: "0"

    # Type: string
    rocketchat_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    rocketchat_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    rocketchat_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    rocketchat_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    rocketchat_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    rocketchat_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    rocketchat_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    rocketchat_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    rocketchat_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    rocketchat_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    rocketchat_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    rocketchat_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    rocketchat_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    rocketchat_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    rocketchat_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    rocketchat_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    rocketchat_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    rocketchat_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        rocketchat_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "rocketchat2.{{ user.domain }}"
          - "rocketchat.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        rocketchat_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'rocketchat2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

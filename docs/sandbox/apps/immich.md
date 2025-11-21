---
icon: material/docker
hide:
  - tags
tags:
  - immich
  - photos
  - backup
---

# Immich

## Overview

[Immich](https://immich.app/) is a self-hosted photo and video backup tool, similar to google photos and apple photos.

### Features

- Bulk Upload (Using the CLI)
- Facial Recognition
- Hardware Transcoding (Experimental)
- Oauth and/or password login
- Libraries
- Mobile App
- Partner Sharing
- Reverse Geocoding
- Smart Search
- XMP Sidecars

!!! info
    By default, Immich is NOT protected behind your Authelia/SSO middleware. You have to create a user with an email and password for Immich upon start up. Its recommended that you use the email and password you set up upon instalation for consistencies sake.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://immich.app/){: .header-icons } | [:octicons-link-16: Docs](https://immich.app/docs/overview/introduction){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/immich-app/immich){: .header-icons }|

### 1. Installation

```shell
sb install sandbox-immich
```

### 2. URL

- To access Immich, visit <https://immich.iYOUR_DOMAIN_NAMEi>

### 3. Setup

!!! info
    📢 Again, no default user is configured until you run through the setup screen, so you would ideally run through setup as soon as immich is deployed to secure the site. It is not behind authelia by default.

???tip
    In Administration > Settings is a button to copy the current admin configuration to your clipboard. So you can just grab it from there, and paste it into a file.

If you would like to have the config file available, create a new config file (e.g. immich.config, and the config format is `.json`) and map it in inventory; just keep in mind that this disallows you from configuring Immich admin settings from the web ui.

```yaml
immich_docker_envs_custom:
  IMMICH_CONFIG_FILE: "/config/immich.config"
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    immich_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `immich_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `immich_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`immich_name`"

        ```yaml
        # Type: string
        immich_name: immich
        ```

=== "Settings"

    ??? variable string "`immich_role_photos_location`"

        ```yaml
        # Type: string
        immich_role_photos_location: "/mnt/unionfs/Media/Photos"
        ```

    ??? variable bool "`immich_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        immich_role_postgres_deploy: true
        ```

    ??? variable string "`immich_role_postgres_name`"

        ```yaml
        # Type: string
        immich_role_postgres_name: "{{ immich_name }}-postgres"
        ```

    ??? variable string "`immich_role_postgres_user`"

        ```yaml
        # Type: string
        immich_role_postgres_user: "{{ postgres_role_docker_env_user }}"
        ```

    ??? variable string "`immich_role_postgres_password`"

        ```yaml
        # Type: string
        immich_role_postgres_password: "{{ postgres_role_docker_env_password }}"
        ```

    ??? variable string "`immich_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        immich_role_postgres_docker_env_db: "{{ immich_name }}"
        ```

    ??? variable string "`immich_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        immich_role_postgres_docker_image_tag: "14-vectorchord0.4.3-pgvectors0.2.0"
        ```

    ??? variable string "`immich_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        immich_role_postgres_docker_image_repo: "ghcr.io/immich-app/postgres"
        ```

    ??? variable dict "`immich_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        immich_role_postgres_docker_healthcheck:
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='immich') }} -U {{ postgres_role_docker_env_user }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`immich_role_postgres_docker_shm_size`"

        ```yaml
        # Type: string
        immich_role_postgres_docker_shm_size: "128M"
        ```

    ??? variable string "`immich_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        immich_role_postgres_paths_folder: "{{ immich_name }}"
        ```

    ??? variable string "`immich_role_postgres_paths_location`"

        ```yaml
        # Type: string
        immich_role_postgres_paths_location: "{{ server_appdata_path }}/{{ immich_role_postgres_paths_folder }}/postgres"
        ```

    ??? variable dict "`immich_role_postgres_docker_envs_custom`"

        ```yaml
        # Type: dict
        immich_role_postgres_docker_envs_custom:
          POSTGRES_INITDB_ARGS: '--data-checksums'
        ```

=== "Paths"

    ??? variable string "`immich_role_paths_folder`"

        ```yaml
        # Type: string
        immich_role_paths_folder: "{{ immich_name }}"
        ```

    ??? variable string "`immich_role_paths_location`"

        ```yaml
        # Type: string
        immich_role_paths_location: "{{ server_appdata_path }}/{{ immich_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`immich_role_web_subdomain`"

        ```yaml
        # Type: string
        immich_role_web_subdomain: "{{ immich_name }}"
        ```

    ??? variable string "`immich_role_web_domain`"

        ```yaml
        # Type: string
        immich_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`immich_role_web_port`"

        ```yaml
        # Type: string
        immich_role_web_port: "8080"
        ```

    ??? variable string "`immich_role_web_url`"

        ```yaml
        # Type: string
        immich_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='immich') + '.' + lookup('role_var', '_web_domain', role='immich')
                              if (lookup('role_var', '_web_subdomain', role='immich') | length > 0)
                              else lookup('role_var', '_web_domain', role='immich')) }}"
        ```

=== "DNS"

    ??? variable string "`immich_role_dns_record`"

        ```yaml
        # Type: string
        immich_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='immich') }}"
        ```

    ??? variable string "`immich_role_dns_zone`"

        ```yaml
        # Type: string
        immich_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='immich') }}"
        ```

    ??? variable bool "`immich_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        immich_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`immich_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        immich_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`immich_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        immich_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`immich_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        immich_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`immich_role_traefik_certresolver`"

        ```yaml
        # Type: string
        immich_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`immich_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        immich_role_traefik_enabled: true
        ```

    ??? variable bool "`immich_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        immich_role_traefik_api_enabled: false
        ```

    ??? variable string "`immich_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        immich_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`immich_role_docker_container`"

        ```yaml
        # Type: string
        immich_role_docker_container: "{{ immich_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`immich_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        immich_role_docker_image_pull: true
        ```

    ??? variable string "`immich_role_docker_image_repo`"

        ```yaml
        # Type: string
        immich_role_docker_image_repo: "ghcr.io/imagegenius/immich"
        ```

    ??? variable string "`immich_role_docker_image_tag`"

        ```yaml
        # Type: string
        immich_role_docker_image_tag: "latest"
        ```

    ??? variable string "`immich_role_docker_image`"

        ```yaml
        # Type: string
        immich_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='immich') }}:{{ lookup('role_var', '_docker_image_tag', role='immich') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`immich_role_docker_envs_default`"

        ```yaml
        # Type: dict
        immich_role_docker_envs_default:
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          DB_HOSTNAME: "{{ lookup('role_var', '_postgres_name', role='immich') }}"
          DB_USERNAME: "{{ lookup('role_var', '_postgres_user', role='immich') }}"
          DB_PASSWORD: "{{ lookup('role_var', '_postgres_password', role='immich') }}"
          DB_DATABASE_NAME: "{{ lookup('role_var', '_postgres_docker_env_db', role='immich') }}"
          REDIS_HOSTNAME: "{{ immich_name }}-redis"
          DISABLE_MACHINE_LEARNING: "false"
          MACHINE_LEARNING_WORKERS: "1"
          MACHINE_LEARNING_WORKER_TIMEOUT: "120"
        ```

    ??? variable dict "`immich_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        immich_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`immich_role_docker_volumes_default`"

        ```yaml
        # Type: list
        immich_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='immich') }}:/config"
          - "{{ lookup('role_var', '_photos_location', role='immich') }}:/photos"
        ```

    ??? variable list "`immich_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        immich_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`immich_role_docker_hostname`"

        ```yaml
        # Type: string
        immich_role_docker_hostname: "{{ immich_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`immich_role_docker_networks_alias`"

        ```yaml
        # Type: string
        immich_role_docker_networks_alias: "{{ immich_name }}"
        ```

    ??? variable list "`immich_role_docker_networks_default`"

        ```yaml
        # Type: list
        immich_role_docker_networks_default: []
        ```

    ??? variable list "`immich_role_docker_networks_custom`"

        ```yaml
        # Type: list
        immich_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`immich_role_docker_restart_policy`"

        ```yaml
        # Type: string
        immich_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`immich_role_docker_state`"

        ```yaml
        # Type: string
        immich_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`immich_role_depends_on`"

        ```yaml
        # Type: string
        immich_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='immich') }},{{ immich_name }}-redis"
        ```

    ??? variable string "`immich_role_depends_on_delay`"

        ```yaml
        # Type: string
        immich_role_depends_on_delay: "0"
        ```

    ??? variable string "`immich_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        immich_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`immich_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        immich_role_autoheal_enabled: true
        ```

    ??? variable string "`immich_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        immich_role_depends_on: ""
        ```

    ??? variable string "`immich_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        immich_role_depends_on_delay: "0"
        ```

    ??? variable string "`immich_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        immich_role_depends_on_healthchecks:
        ```

    ??? variable bool "`immich_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        immich_role_diun_enabled: true
        ```

    ??? variable bool "`immich_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        immich_role_dns_enabled: true
        ```

    ??? variable bool "`immich_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        immich_role_docker_controller: true
        ```

    ??? variable bool "`immich_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        immich_role_docker_volumes_download:
        ```

    ??? variable bool "`immich_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        immich_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`immich_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        immich_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`immich_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        immich_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`immich_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        immich_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`immich_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        immich_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`immich_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        immich_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`immich_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        immich_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`immich_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        immich_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`immich_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        immich_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`immich_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        immich_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            immich_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "immich2.{{ user.domain }}"
              - "immich.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`immich_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        immich_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            immich_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'immich2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`immich_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        immich_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
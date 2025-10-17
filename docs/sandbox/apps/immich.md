---
hide:
  - tags
tags:
  - immich
  - photos
  - backup
---

# Immich

## What is it?

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

``` shell

sb install sandbox-immich

```

### 2. URL

- To access Immich, visit `https://immich._yourdomain.com_`

### 3. Setup

!!! info
    📢 Again, no default user is configured until you run through the setup screen, so you would ideally run through setup as soon as immich is deployed to secure the site. It is not behind authelia by default.

???tip
    In Administration > Settings is a button to copy the current admin configuration to your clipboard. So you can just grab it from there, and paste it into a file.

If you would like to have the config file available, create a new config file (e.g. immich.config, and the config format is `.json`) and map it in inventory; just keep in mind that this disallows you from configuring Immich admin settings from the web ui.

``` yaml

immich_docker_envs_custom:
  IMMICH_CONFIG_FILE: "/config/immich.config"

```

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        immich_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    immich_name: immich

    ```

??? example "Settings"

    ```yaml
    # Type: string
    immich_role_photos_location: "/mnt/unionfs/Media/Photos"

    # Type: bool (true/false)
    immich_role_postgres_deploy: true

    # Type: string
    immich_role_postgres_name: "{{ immich_name }}-postgres"

    # Type: string
    immich_role_postgres_user: "{{ postgres_role_docker_env_user }}"

    # Type: string
    immich_role_postgres_password: "{{ postgres_role_docker_env_password }}"

    # Type: string
    immich_role_postgres_docker_env_db: "{{ immich_name }}"

    # Type: string
    immich_role_postgres_docker_image_tag: "14-vectorchord0.4.3-pgvectors0.2.0"

    # Type: string
    immich_role_postgres_docker_image_repo: "ghcr.io/immich-app/postgres"

    # Type: dict
    immich_role_postgres_docker_healthcheck: 
      test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='immich') }} -U {{ postgres_role_docker_env_user }}"]
      start_period: 20s
      interval: 30s
      retries: 5
      timeout: 5s

    # Type: string
    immich_role_postgres_docker_shm_size: "128M"

    # Type: string
    immich_role_postgres_paths_folder: "{{ immich_name }}"

    # Type: string
    immich_role_postgres_paths_location: "{{ server_appdata_path }}/{{ immich_role_postgres_paths_folder }}/postgres"

    # Type: dict
    immich_role_postgres_docker_envs_custom: 
      POSTGRES_INITDB_ARGS: '--data-checksums'

    ```

??? example "Paths"

    ```yaml
    # Type: string
    immich_role_paths_folder: "{{ immich_name }}"

    # Type: string
    immich_role_paths_location: "{{ server_appdata_path }}/{{ immich_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    immich_role_web_subdomain: "{{ immich_name }}"

    # Type: string
    immich_role_web_domain: "{{ user.domain }}"

    # Type: string
    immich_role_web_port: "8080"

    # Type: string
    immich_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='immich') + '.' + lookup('role_var', '_web_domain', role='immich')
                          if (lookup('role_var', '_web_subdomain', role='immich') | length > 0)
                          else lookup('role_var', '_web_domain', role='immich')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    immich_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='immich') }}"

    # Type: string
    immich_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='immich') }}"

    # Type: bool (true/false)
    immich_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    immich_role_traefik_sso_middleware: ""

    # Type: string
    immich_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    immich_role_traefik_middleware_custom: ""

    # Type: string
    immich_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    immich_role_traefik_enabled: true

    # Type: bool (true/false)
    immich_role_traefik_api_enabled: false

    # Type: string
    immich_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    immich_role_docker_container: "{{ immich_name }}"

    # Image
    # Type: bool (true/false)
    immich_role_docker_image_pull: true

    # Type: string
    immich_role_docker_image_repo: "ghcr.io/imagegenius/immich"

    # Type: string
    immich_role_docker_image_tag: "latest"

    # Type: string
    immich_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='immich') }}:{{ lookup('role_var', '_docker_image_tag', role='immich') }}"

    # Envs
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

    # Type: dict
    immich_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    immich_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='immich') }}:/config"
      - "{{ lookup('role_var', '_photos_location', role='immich') }}:/photos"

    # Type: list
    immich_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    immich_role_docker_hostname: "{{ immich_name }}"

    # Networks
    # Type: string
    immich_role_docker_networks_alias: "{{ immich_name }}"

    # Type: list
    immich_role_docker_networks_default: []

    # Type: list
    immich_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    immich_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    immich_role_docker_state: started

    # Dependencies
    # Type: string
    immich_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='immich') }},{{ immich_name }}-redis"

    # Type: string
    immich_role_depends_on_delay: "0"

    # Type: string
    immich_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    immich_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    immich_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    immich_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    immich_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    immich_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    immich_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    immich_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    immich_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    immich_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    immich_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    immich_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    immich_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    immich_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    immich_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    immich_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    immich_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    immich_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        immich_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "immich2.{{ user.domain }}"
          - "immich.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        immich_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'immich2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
hide:
  - tags
tags:
  - joplin
  - productivity
  - notes
---

# Joplin

## What is it?

[Joplin](https://joplinapp.org/) is an open source note-taking app. Capture your thoughts and securely access them from any device.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://joplinapp.org/){: .header-icons } | [:octicons-link-16: Docs](https://joplinapp.org/desktop/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/laurent22/joplin){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/florider89/joplin-server){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-joplin

```

### 2. URL

- To access Joplin, visit `https://joplin.xDOMAIN_NAMEx`

### 3. Setup

!!! info
    Default login for joplin is
    `email: admin@localhost`
    `password: admin`

Change this asap.

- Visit [here](https://joplinapp.org/e2ee/) to learn how to use end to end encryption. (Very simple)

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        joplin_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `joplin_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `joplin_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    joplin_name: joplin

    ```

??? example "Settings"

    ```yaml
    # Type: bool (true/false)
    joplin_role_postgres_deploy: true

    # Type: string
    joplin_role_postgres_name: "{{ joplin_name }}-postgres"

    # Type: string
    joplin_role_postgres_user: "joplin"

    # Type: string
    joplin_role_postgres_password: "joplin"

    # Type: string
    joplin_role_postgres_docker_env_db: "joplin"

    # Type: string
    joplin_role_postgres_docker_image_tag: "13"

    # Type: string
    joplin_role_postgres_docker_image_repo: "postgres"

    # Type: dict
    joplin_role_postgres_docker_healthcheck: 
      test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='joplin') }} -U {{ lookup('role_var', '_postgres_user', role='joplin') }}"]
      start_period: 20s
      interval: 30s
      retries: 5
      timeout: 5s

    # Type: string
    joplin_role_postgres_paths_folder: "{{ joplin_name }}"

    # Type: string
    joplin_role_postgres_paths_location: "{{ server_appdata_path }}/{{ joplin_role_postgres_paths_folder }}/postgres"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    joplin_role_paths_folder: "{{ joplin_name }}"

    # Type: string
    joplin_role_paths_location: "{{ server_appdata_path }}/{{ joplin_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    joplin_role_web_subdomain: "{{ joplin_name }}"

    # Type: string
    joplin_role_web_domain: "{{ user.domain }}"

    # Type: string
    joplin_role_web_port: "22300"

    # Type: string
    joplin_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='joplin') + '.' + lookup('role_var', '_web_domain', role='joplin')
                          if (lookup('role_var', '_web_subdomain', role='joplin') | length > 0)
                          else lookup('role_var', '_web_domain', role='joplin')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    joplin_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='joplin') }}"

    # Type: string
    joplin_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='joplin') }}"

    # Type: bool (true/false)
    joplin_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    joplin_role_traefik_sso_middleware: ""

    # Type: string
    joplin_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    joplin_role_traefik_middleware_custom: ""

    # Type: string
    joplin_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    joplin_role_traefik_enabled: true

    # Type: bool (true/false)
    joplin_role_traefik_api_enabled: false

    # Type: string
    joplin_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    joplin_role_docker_container: "{{ joplin_name }}"

    # Image
    # Type: bool (true/false)
    joplin_role_docker_image_pull: true

    # Type: string
    joplin_role_docker_image_repo: "joplin/server"

    # Type: string
    joplin_role_docker_image_tag: "latest"

    # Type: string
    joplin_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='joplin') }}:{{ lookup('role_var', '_docker_image_tag', role='joplin') }}"

    # Envs
    # Type: dict
    joplin_role_docker_envs_default: 
      TZ: "{{ tz }}"
      APP_BASE_URL: "{{ lookup('role_var', '_web_url', role='joplin') }}"
      APP_PORT: "22300"
      POSTGRES_PASSWORD: "{{ lookup('role_var', '_postgres_password', role='joplin') }}"
      POSTGRES_DATABASE: "{{ lookup('role_var', '_postgres_docker_env_db', role='joplin') }}"
      POSTGRES_USER: "{{ lookup('role_var', '_postgres_user', role='joplin') }}"
      POSTGRES_PORT: "5432"
      POSTGRES_HOST: "{{ lookup('role_var', '_postgres_name', role='joplin') }}"
      DB_CLIENT: "pg"

    # Type: dict
    joplin_role_docker_envs_custom: {}

    # Hostname
    # Type: string
    joplin_role_docker_hostname: "{{ joplin_name }}"

    # Networks
    # Type: string
    joplin_role_docker_networks_alias: "{{ joplin_name }}"

    # Type: list
    joplin_role_docker_networks_default: []

    # Type: list
    joplin_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    joplin_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    joplin_role_docker_state: started

    # Dependencies
    # Type: string
    joplin_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='joplin') }}"

    # Type: string
    joplin_role_depends_on_delay: "0"

    # Type: string
    joplin_role_depends_on_healthchecks: "false"

    # Create Docker Container Timeout
    # Type: int
    joplin_docker_create_timeout: 300

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    joplin_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    joplin_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    joplin_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    joplin_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    joplin_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    joplin_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    joplin_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    joplin_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    joplin_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    joplin_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    joplin_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    joplin_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    joplin_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    joplin_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    joplin_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    joplin_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    joplin_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        joplin_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "joplin2.{{ user.domain }}"
          - "joplin.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        joplin_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'joplin2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

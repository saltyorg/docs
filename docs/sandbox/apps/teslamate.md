---
hide:
  - tags
tags:
  - teslamate
  - tesla
  - monitoring
---

# Teslamate

## What is it?

[Teslamate](https://github.com/teslamate-org/teslamate) is a powerful, self-hosted data logger for your Tesla.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/teslamate-org/teslamate){: .header-icons } | [:octicons-link-16: Docs](https://github.com/teslamate-org/teslamate){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/teslamate-org/teslamate){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/teslamate/teslamate){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-teslamate

```

### 2. URL

- To access Teslamate, visit `https://teslamate.xDOMAIN_NAMEx`

### 3. Setup

- [:octicons-link-16: Documentation: Teslamate Docs](https://docs.teslamate.org/docs/installation/docker){: .header-icons }

To use a custom subdomain, add a custom value for `teslamate_web_subdomain` in the `/srv/git/saltbox/inventories/host_vars/localhost.yml` file. More info can be found [here](../../saltbox/inventory/index.md).

### 4. Grafana Setup

Once installation is finished, you will need to add the teslamate data source in grafana under connections.

Host URL: This is based upon the `{{ teslamate_name }}-postgres` variable. Default is `teslamate-postgres:5432`
Table: `teslamate`

Authentication for Postgres: Run the command below to have saltbox output the DB password.

``` shell

sb install sandbox-teslamate-postgres-password

```

Save and Test

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        teslamate_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `teslamate_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `teslamate_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "General"

    ```yaml
    # defaults/main.yml
    # Type: string
    teslamate_name: teslamate

    ```

??? example "Settings"

    ```yaml
    # Type: string
    teslamate_secret_key: "{{ teslamate_saltbox_facts.facts.secret_key }}"

    # Type: bool (true/false)
    teslamate_role_postgres_deploy: true

    # Type: string
    teslamate_role_postgres_name: "{{ teslamate_name }}-postgres"

    # Type: string
    teslamate_role_postgres_user: "{{ postgres_role_docker_env_user }}"

    # Type: string
    teslamate_role_postgres_password: "{{ teslamate_saltbox_facts.facts.postgres_password }}"

    # Type: string
    teslamate_role_postgres_docker_env_db: "{{ teslamate_name }}"

    # Type: string
    teslamate_role_postgres_docker_image_tag: "16"

    # Type: string
    teslamate_role_postgres_docker_image_repo: "postgres"

    # Type: dict
    teslamate_role_postgres_docker_healthcheck: 
      test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='teslamate') }} -U {{ postgres_role_docker_env_user }}"]
      start_period: 20s
      interval: 30s
      retries: 5
      timeout: 5s

    # Type: string
    teslamate_role_postgres_paths_folder: "{{ teslamate_name }}"

    # Type: string
    teslamate_role_postgres_paths_location: "{{ server_appdata_path }}/{{ teslamate_role_postgres_paths_folder }}/postgres"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    teslamate_role_paths_folder: "{{ teslamate_name }}"

    # Type: string
    teslamate_role_paths_location: "{{ server_appdata_path }}/{{ teslamate_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    teslamate_role_web_subdomain: "{{ teslamate_name }}"

    # Type: string
    teslamate_role_web_domain: "{{ user.domain }}"

    # Type: string
    teslamate_role_web_port: "4000"

    # Type: string
    teslamate_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='teslamate') + '.' + lookup('role_var', '_web_domain', role='teslamate')
                             if (lookup('role_var', '_web_subdomain', role='teslamate') | length > 0)
                             else lookup('role_var', '_web_domain', role='teslamate')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    teslamate_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='teslamate') }}"

    # Type: string
    teslamate_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='teslamate') }}"

    # Type: bool (true/false)
    teslamate_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    teslamate_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    teslamate_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    teslamate_role_traefik_middleware_custom: ""

    # Type: string
    teslamate_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    teslamate_role_traefik_enabled: true

    # Type: bool (true/false)
    teslamate_role_traefik_api_enabled: false

    # Type: string
    teslamate_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    teslamate_role_docker_container: "{{ teslamate_name }}"

    # Image
    # Type: bool (true/false)
    teslamate_role_docker_image_pull: true

    # Type: string
    teslamate_role_docker_image_tag: "latest"

    # Type: string
    teslamate_role_docker_image_repo: "teslamate/teslamate"

    # Type: string
    teslamate_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='teslamate') }}:{{ lookup('role_var', '_docker_image_tag', role='teslamate') }}"

    # Envs
    # Type: dict
    teslamate_role_docker_envs_default: 
      DATABASE_USER: "{{ lookup('role_var', '_postgres_user', role='teslamate') }}"
      DATABASE_PASS: "{{ lookup('role_var', '_postgres_password', role='teslamate') }}"
      DATABASE_NAME: "{{ lookup('role_var', '_postgres_docker_env_db', role='teslamate') }}"
      ENCRYPTION_KEY: "{{ teslamate_secret_key }}"
      DATABASE_HOST: "{{ lookup('role_var', '_postgres_name', role='teslamate') }}"
      DATABASE_PORT: "5432"
      MQTT_HOST: "mqtt"
      CHECK_ORIGIN: "false"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    teslamate_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    teslamate_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='teslamate') }}:/opt/app/import"

    # Type: list
    teslamate_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    teslamate_role_docker_hostname: "{{ teslamate_name }}"

    # Networks
    # Type: string
    teslamate_role_docker_networks_alias: "{{ teslamate_name }}"

    # Type: list
    teslamate_role_docker_networks_default: []

    # Type: list
    teslamate_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    teslamate_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    teslamate_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    teslamate_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    teslamate_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    teslamate_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    teslamate_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    teslamate_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    teslamate_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    teslamate_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    teslamate_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    teslamate_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    teslamate_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    teslamate_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    teslamate_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    teslamate_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    teslamate_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    teslamate_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    teslamate_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    teslamate_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        teslamate_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "teslamate2.{{ user.domain }}"
          - "teslamate.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        teslamate_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'teslamate2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->


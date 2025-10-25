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

- To access Teslamate, visit `https://teslamate._yourdomain.com_`

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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    teslamate_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `teslamate_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `teslamate_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "General"

    ??? variable string "`teslamate_name`"

        ```yaml
        # defaults/main.yml
        # Type: string
        teslamate_name: teslamate
        ```

=== "Settings"

    ??? variable string "`teslamate_secret_key`"

        ```yaml
        # Type: string
        teslamate_secret_key: "{{ teslamate_saltbox_facts.facts.secret_key }}"
        ```

    ??? variable bool "`teslamate_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_postgres_deploy: true
        ```

    ??? variable string "`teslamate_role_postgres_name`"

        ```yaml
        # Type: string
        teslamate_role_postgres_name: "{{ teslamate_name }}-postgres"
        ```

    ??? variable string "`teslamate_role_postgres_user`"

        ```yaml
        # Type: string
        teslamate_role_postgres_user: "{{ postgres_role_docker_env_user }}"
        ```

    ??? variable string "`teslamate_role_postgres_password`"

        ```yaml
        # Type: string
        teslamate_role_postgres_password: "{{ teslamate_saltbox_facts.facts.postgres_password }}"
        ```

    ??? variable string "`teslamate_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        teslamate_role_postgres_docker_env_db: "{{ teslamate_name }}"
        ```

    ??? variable string "`teslamate_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        teslamate_role_postgres_docker_image_tag: "16"
        ```

    ??? variable string "`teslamate_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        teslamate_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable dict "`teslamate_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        teslamate_role_postgres_docker_healthcheck: 
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='teslamate') }} -U {{ postgres_role_docker_env_user }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`teslamate_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        teslamate_role_postgres_paths_folder: "{{ teslamate_name }}"
        ```

    ??? variable string "`teslamate_role_postgres_paths_location`"

        ```yaml
        # Type: string
        teslamate_role_postgres_paths_location: "{{ server_appdata_path }}/{{ teslamate_role_postgres_paths_folder }}/postgres"
        ```

=== "Paths"

    ??? variable string "`teslamate_role_paths_folder`"

        ```yaml
        # Type: string
        teslamate_role_paths_folder: "{{ teslamate_name }}"
        ```

    ??? variable string "`teslamate_role_paths_location`"

        ```yaml
        # Type: string
        teslamate_role_paths_location: "{{ server_appdata_path }}/{{ teslamate_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`teslamate_role_web_subdomain`"

        ```yaml
        # Type: string
        teslamate_role_web_subdomain: "{{ teslamate_name }}"
        ```

    ??? variable string "`teslamate_role_web_domain`"

        ```yaml
        # Type: string
        teslamate_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`teslamate_role_web_port`"

        ```yaml
        # Type: string
        teslamate_role_web_port: "4000"
        ```

    ??? variable string "`teslamate_role_web_url`"

        ```yaml
        # Type: string
        teslamate_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='teslamate') + '.' + lookup('role_var', '_web_domain', role='teslamate')
                                 if (lookup('role_var', '_web_subdomain', role='teslamate') | length > 0)
                                 else lookup('role_var', '_web_domain', role='teslamate')) }}"
        ```

=== "DNS"

    ??? variable string "`teslamate_role_dns_record`"

        ```yaml
        # Type: string
        teslamate_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='teslamate') }}"
        ```

    ??? variable string "`teslamate_role_dns_zone`"

        ```yaml
        # Type: string
        teslamate_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='teslamate') }}"
        ```

    ??? variable bool "`teslamate_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`teslamate_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        teslamate_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`teslamate_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        teslamate_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`teslamate_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        teslamate_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`teslamate_role_traefik_certresolver`"

        ```yaml
        # Type: string
        teslamate_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`teslamate_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_traefik_enabled: true
        ```

    ??? variable bool "`teslamate_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_traefik_api_enabled: false
        ```

    ??? variable string "`teslamate_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        teslamate_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`teslamate_role_docker_container`"

        ```yaml
        # Type: string
        teslamate_role_docker_container: "{{ teslamate_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`teslamate_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_docker_image_pull: true
        ```

    ??? variable string "`teslamate_role_docker_image_tag`"

        ```yaml
        # Type: string
        teslamate_role_docker_image_tag: "latest"
        ```

    ??? variable string "`teslamate_role_docker_image_repo`"

        ```yaml
        # Type: string
        teslamate_role_docker_image_repo: "teslamate/teslamate"
        ```

    ??? variable string "`teslamate_role_docker_image`"

        ```yaml
        # Type: string
        teslamate_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='teslamate') }}:{{ lookup('role_var', '_docker_image_tag', role='teslamate') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`teslamate_role_docker_envs_default`"

        ```yaml
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
        ```

    ??? variable dict "`teslamate_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        teslamate_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`teslamate_role_docker_volumes_default`"

        ```yaml
        # Type: list
        teslamate_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='teslamate') }}:/opt/app/import"
        ```

    ??? variable list "`teslamate_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        teslamate_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`teslamate_role_docker_hostname`"

        ```yaml
        # Type: string
        teslamate_role_docker_hostname: "{{ teslamate_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`teslamate_role_docker_networks_alias`"

        ```yaml
        # Type: string
        teslamate_role_docker_networks_alias: "{{ teslamate_name }}"
        ```

    ??? variable list "`teslamate_role_docker_networks_default`"

        ```yaml
        # Type: list
        teslamate_role_docker_networks_default: []
        ```

    ??? variable list "`teslamate_role_docker_networks_custom`"

        ```yaml
        # Type: list
        teslamate_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`teslamate_role_docker_restart_policy`"

        ```yaml
        # Type: string
        teslamate_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`teslamate_role_docker_state`"

        ```yaml
        # Type: string
        teslamate_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`teslamate_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        teslamate_role_autoheal_enabled: true
        ```

    ??? variable string "`teslamate_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        teslamate_role_depends_on: ""
        ```

    ??? variable string "`teslamate_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        teslamate_role_depends_on_delay: "0"
        ```

    ??? variable string "`teslamate_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        teslamate_role_depends_on_healthchecks:
        ```

    ??? variable bool "`teslamate_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        teslamate_role_diun_enabled: true
        ```

    ??? variable bool "`teslamate_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        teslamate_role_dns_enabled: true
        ```

    ??? variable bool "`teslamate_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        teslamate_role_docker_controller: true
        ```

    ??? variable bool "`teslamate_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        teslamate_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`teslamate_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        teslamate_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`teslamate_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        teslamate_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`teslamate_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        teslamate_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`teslamate_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`teslamate_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        teslamate_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`teslamate_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        teslamate_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`teslamate_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        teslamate_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`teslamate_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        teslamate_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`teslamate_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        teslamate_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            teslamate_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "teslamate2.{{ user.domain }}"
              - "teslamate.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`teslamate_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        teslamate_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            teslamate_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'teslamate2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`teslamate_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        teslamate_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
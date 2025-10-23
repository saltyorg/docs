---
hide:
  - tags
tags:
  - tandoor
  - recipes
  - planning
---

# Tandoor Recipes

## What is it?

[Tandoor Recipes](https://github.com/TandoorRecipes/recipes)  is an application for managing recipes, planning meals, building shopping lists and much much more!

### Core Features

- 🥗 Manage your recipes with a fast and intuitive editor

- 📆 Plan multiple meals for each day

- 🛒 Shopping lists via the meal plan or straight from recipes

- 📚 Cookbooks collect recipes into books

- 👪 Share and collaborate on recipes with friends and family

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/TandoorRecipes/recipes){: .header-icons } | [:octicons-link-16: Docs](https://docs.tandoor.dev/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/TandoorRecipes/recipes){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/vabene1111/recipes){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-tandoor

```

### 2. Setup

#### How do I add an admin user?

To create your initial user you need to

- execute a shell in the container using `docker exec -it tandoor sh`

- activate the virtual environment `source venv/bin/activate`

- run `python manage.py createsuperuser` and follow the steps shown.

### 3. URL

- To access Tandoor, visit `https://tandoor._yourdomain.com_`

### 4. Other

#### How do I reset passwords?

To reset a lost password if access to the container is lost you need to

- execute a shell in the container using `docker exec -it tandoor sh`

- activate the virtual environment `source venv/bin/activate`

- run `python manage.py changepassword <username>` and follow the steps shown.

To use a custom subdomain, add a custom value for `tandoor_web_subdomain` in the `/srv/git/saltbox/inventories/host_vars/localhost.yml` file. More info can be found [here](../../saltbox/inventory/index.md).

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        tandoor_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `tandoor_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `tandoor_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`tandoor_name`"

        ```yaml
        # Type: string
        tandoor_name: tandoor
        ```

=== "Settings"

    ??? variable bool "`tandoor_role_postgres_deploy`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_postgres_deploy: true
        ```

    ??? variable string "`tandoor_role_postgres_name`"

        ```yaml
        # Type: string
        tandoor_role_postgres_name: "{{ tandoor_name }}-postgres"
        ```

    ??? variable string "`tandoor_role_postgres_user`"

        ```yaml
        # Type: string
        tandoor_role_postgres_user: "{{ postgres_role_docker_env_user }}"
        ```

    ??? variable string "`tandoor_role_postgres_password`"

        ```yaml
        # Type: string
        tandoor_role_postgres_password: "{{ postgres_role_docker_env_password }}"
        ```

    ??? variable string "`tandoor_role_postgres_docker_env_db`"

        ```yaml
        # Type: string
        tandoor_role_postgres_docker_env_db: "{{ tandoor_name }}"
        ```

    ??? variable string "`tandoor_role_postgres_docker_image_tag`"

        ```yaml
        # Type: string
        tandoor_role_postgres_docker_image_tag: "17-alpine"
        ```

    ??? variable string "`tandoor_role_postgres_docker_image_repo`"

        ```yaml
        # Type: string
        tandoor_role_postgres_docker_image_repo: "postgres"
        ```

    ??? variable dict "`tandoor_role_postgres_docker_healthcheck`"

        ```yaml
        # Type: dict
        tandoor_role_postgres_docker_healthcheck: 
          test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='tandoor') }} -U {{ postgres_role_docker_env_user }}"]
          start_period: 20s
          interval: 30s
          retries: 5
          timeout: 5s
        ```

    ??? variable string "`tandoor_role_postgres_paths_folder`"

        ```yaml
        # Type: string
        tandoor_role_postgres_paths_folder: "{{ tandoor_name }}"
        ```

    ??? variable string "`tandoor_role_postgres_paths_location`"

        ```yaml
        # Type: string
        tandoor_role_postgres_paths_location: "{{ server_appdata_path }}/{{ tandoor_role_postgres_paths_folder }}/postgres"
        ```

=== "Paths"

    ??? variable string "`tandoor_role_paths_folder`"

        ```yaml
        # Type: string
        tandoor_role_paths_folder: "{{ tandoor_name }}"
        ```

    ??? variable string "`tandoor_role_paths_location`"

        ```yaml
        # Type: string
        tandoor_role_paths_location: "{{ server_appdata_path }}/{{ tandoor_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`tandoor_role_web_subdomain`"

        ```yaml
        # Type: string
        tandoor_role_web_subdomain: "{{ tandoor_name }}"
        ```

    ??? variable string "`tandoor_role_web_domain`"

        ```yaml
        # Type: string
        tandoor_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`tandoor_role_web_port`"

        ```yaml
        # Type: string
        tandoor_role_web_port: "80"
        ```

    ??? variable string "`tandoor_role_web_url`"

        ```yaml
        # Type: string
        tandoor_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='tandoor') + '.' + lookup('role_var', '_web_domain', role='tandoor')
                               if (lookup('role_var', '_web_subdomain', role='tandoor') | length > 0)
                               else lookup('role_var', '_web_domain', role='tandoor')) }}"
        ```

=== "DNS"

    ??? variable string "`tandoor_role_dns_record`"

        ```yaml
        # Type: string
        tandoor_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='tandoor') }}"
        ```

    ??? variable string "`tandoor_role_dns_zone`"

        ```yaml
        # Type: string
        tandoor_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='tandoor') }}"
        ```

    ??? variable bool "`tandoor_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`tandoor_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        tandoor_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`tandoor_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        tandoor_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`tandoor_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        tandoor_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`tandoor_role_traefik_certresolver`"

        ```yaml
        # Type: string
        tandoor_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`tandoor_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_traefik_enabled: true
        ```

    ??? variable bool "`tandoor_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_traefik_api_enabled: false
        ```

    ??? variable string "`tandoor_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        tandoor_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`tandoor_role_docker_container`"

        ```yaml
        # Type: string
        tandoor_role_docker_container: "{{ tandoor_name }}"
        ```

    ##### Image

    ??? variable bool "`tandoor_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_docker_image_pull: true
        ```

    ??? variable string "`tandoor_role_docker_image_tag`"

        ```yaml
        # Type: string
        tandoor_role_docker_image_tag: "latest"
        ```

    ??? variable string "`tandoor_role_docker_image_repo`"

        ```yaml
        # Type: string
        tandoor_role_docker_image_repo: "vabene1111/recipes"
        ```

    ??? variable string "`tandoor_role_docker_image`"

        ```yaml
        # Type: string
        tandoor_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='tandoor') }}:{{ lookup('role_var', '_docker_image_tag', role='tandoor') }}"
        ```

    ##### Envs

    ??? variable dict "`tandoor_role_docker_envs_default`"

        ```yaml
        # Type: dict
        tandoor_role_docker_envs_default: 
          TZ: "{{ tz }}"
          SECRET_KEY: "{{ tandoor_saltbox_facts.facts.secret_key }}"
          DB_ENGINE: "django.db.backends.postgresql"
          POSTGRES_HOST: "{{ lookup('role_var', '_postgres_name', role='tandoor') }}"
          POSTGRES_PORT: "5432"
          POSTGRES_USER: "{{ lookup('role_var', '_postgres_user', role='tandoor') }}"
          POSTGRES_PASSWORD: "{{ lookup('role_var', '_postgres_password', role='tandoor') }}"
          POSTGRES_DB: "{{ lookup('role_var', '_postgres_docker_env_db', role='tandoor') }}"
          DEBUG: "0"
          GUNICORN_MEDIA: "1"
          REMOTE_USER_AUTH: "1"
        ```

    ??? variable dict "`tandoor_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        tandoor_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`tandoor_role_docker_volumes_default`"

        ```yaml
        # Type: list
        tandoor_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='tandoor') }}/staticfiles:/opt/recipes/staticfiles"
          - "{{ lookup('role_var', '_paths_location', role='tandoor') }}/mediafiles:/opt/recipes/mediafiles"
        ```

    ??? variable list "`tandoor_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        tandoor_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`tandoor_role_docker_hostname`"

        ```yaml
        # Type: string
        tandoor_role_docker_hostname: "{{ tandoor_name }}"
        ```

    ##### Networks

    ??? variable string "`tandoor_role_docker_networks_alias`"

        ```yaml
        # Type: string
        tandoor_role_docker_networks_alias: "{{ tandoor_name }}"
        ```

    ??? variable list "`tandoor_role_docker_networks_default`"

        ```yaml
        # Type: list
        tandoor_role_docker_networks_default: []
        ```

    ??? variable list "`tandoor_role_docker_networks_custom`"

        ```yaml
        # Type: list
        tandoor_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`tandoor_role_docker_restart_policy`"

        ```yaml
        # Type: string
        tandoor_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`tandoor_role_docker_state`"

        ```yaml
        # Type: string
        tandoor_role_docker_state: started
        ```

    ##### Dependencies

    ??? variable string "`tandoor_role_depends_on`"

        ```yaml
        # Type: string
        tandoor_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='tandoor') }}"
        ```

    ??? variable string "`tandoor_role_depends_on_delay`"

        ```yaml
        # Type: string
        tandoor_role_depends_on_delay: "0"
        ```

    ??? variable string "`tandoor_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        tandoor_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`tandoor_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        tandoor_role_autoheal_enabled: true
        ```

    ??? variable string "`tandoor_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        tandoor_role_depends_on: ""
        ```

    ??? variable string "`tandoor_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        tandoor_role_depends_on_delay: "0"
        ```

    ??? variable string "`tandoor_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        tandoor_role_depends_on_healthchecks:
        ```

    ??? variable bool "`tandoor_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        tandoor_role_diun_enabled: true
        ```

    ??? variable bool "`tandoor_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        tandoor_role_dns_enabled: true
        ```

    ??? variable bool "`tandoor_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        tandoor_role_docker_controller: true
        ```

    ??? variable bool "`tandoor_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        tandoor_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`tandoor_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        tandoor_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`tandoor_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        tandoor_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`tandoor_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        tandoor_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`tandoor_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`tandoor_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        tandoor_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`tandoor_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        tandoor_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`tandoor_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        tandoor_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`tandoor_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        tandoor_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`tandoor_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        tandoor_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            tandoor_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "tandoor2.{{ user.domain }}"
              - "tandoor.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`tandoor_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        tandoor_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            tandoor_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'tandoor2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`tandoor_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        tandoor_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
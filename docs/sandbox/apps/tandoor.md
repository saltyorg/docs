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

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
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

??? example "Basics"

    ```yaml
    # Type: string
    tandoor_name: tandoor

    ```

??? example "Settings"

    ```yaml
    # Type: bool (true/false)
    tandoor_role_postgres_deploy: true

    # Type: string
    tandoor_role_postgres_name: "{{ tandoor_name }}-postgres"

    # Type: string
    tandoor_role_postgres_user: "{{ postgres_role_docker_env_user }}"

    # Type: string
    tandoor_role_postgres_password: "{{ postgres_role_docker_env_password }}"

    # Type: string
    tandoor_role_postgres_docker_env_db: "{{ tandoor_name }}"

    # Type: string
    tandoor_role_postgres_docker_image_tag: "17-alpine"

    # Type: string
    tandoor_role_postgres_docker_image_repo: "postgres"

    # Type: dict
    tandoor_role_postgres_docker_healthcheck: 
      test: ["CMD-SHELL", "pg_isready -d {{ lookup('role_var', '_postgres_docker_env_db', role='tandoor') }} -U {{ postgres_role_docker_env_user }}"]
      start_period: 20s
      interval: 30s
      retries: 5
      timeout: 5s

    # Type: string
    tandoor_role_postgres_paths_folder: "{{ tandoor_name }}"

    # Type: string
    tandoor_role_postgres_paths_location: "{{ server_appdata_path }}/{{ tandoor_role_postgres_paths_folder }}/postgres"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    tandoor_role_paths_folder: "{{ tandoor_name }}"

    # Type: string
    tandoor_role_paths_location: "{{ server_appdata_path }}/{{ tandoor_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    tandoor_role_web_subdomain: "{{ tandoor_name }}"

    # Type: string
    tandoor_role_web_domain: "{{ user.domain }}"

    # Type: string
    tandoor_role_web_port: "80"

    # Type: string
    tandoor_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='tandoor') + '.' + lookup('role_var', '_web_domain', role='tandoor')
                           if (lookup('role_var', '_web_subdomain', role='tandoor') | length > 0)
                           else lookup('role_var', '_web_domain', role='tandoor')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    tandoor_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='tandoor') }}"

    # Type: string
    tandoor_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='tandoor') }}"

    # Type: bool (true/false)
    tandoor_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    tandoor_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    tandoor_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    tandoor_role_traefik_middleware_custom: ""

    # Type: string
    tandoor_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    tandoor_role_traefik_enabled: true

    # Type: bool (true/false)
    tandoor_role_traefik_api_enabled: false

    # Type: string
    tandoor_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    tandoor_role_docker_container: "{{ tandoor_name }}"

    # Image
    # Type: bool (true/false)
    tandoor_role_docker_image_pull: true

    # Type: string
    tandoor_role_docker_image_tag: "latest"

    # Type: string
    tandoor_role_docker_image_repo: "vabene1111/recipes"

    # Type: string
    tandoor_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='tandoor') }}:{{ lookup('role_var', '_docker_image_tag', role='tandoor') }}"

    # Envs
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

    # Type: dict
    tandoor_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    tandoor_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='tandoor') }}/staticfiles:/opt/recipes/staticfiles"
      - "{{ lookup('role_var', '_paths_location', role='tandoor') }}/mediafiles:/opt/recipes/mediafiles"

    # Type: list
    tandoor_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    tandoor_role_docker_hostname: "{{ tandoor_name }}"

    # Networks
    # Type: string
    tandoor_role_docker_networks_alias: "{{ tandoor_name }}"

    # Type: list
    tandoor_role_docker_networks_default: []

    # Type: list
    tandoor_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    tandoor_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    tandoor_role_docker_state: started

    # Dependencies
    # Type: string
    tandoor_role_depends_on: "{{ lookup('role_var', '_postgres_name', role='tandoor') }}"

    # Type: string
    tandoor_role_depends_on_delay: "0"

    # Type: string
    tandoor_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    tandoor_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    tandoor_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    tandoor_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    tandoor_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    tandoor_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    tandoor_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    tandoor_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    tandoor_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    tandoor_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    tandoor_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    tandoor_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    tandoor_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    tandoor_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    tandoor_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    tandoor_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    tandoor_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    tandoor_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        tandoor_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "tandoor2.{{ user.domain }}"
          - "tandoor.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        tandoor_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'tandoor2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

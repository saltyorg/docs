---
hide:
  - tags
tags:
  - bookstack
  - wiki
  - documentation
---

# BookStack

## What is it?

[BookStack](https://www.bookstackapp.com/) is a simple, self-hosted, easy-to-use platform for organising and storing information.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.bookstackapp.com/){: .header-icons } | [:octicons-link-16: Docs](https://www.bookstackapp.com/docs){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/BookStackApp/BookStack){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/bookstack){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-bookstack

```

### 2. URL

- To access BookStack, visit `https://bookstack._yourdomain.com_`

### 3. Setup

- Log in using the default admin details `admin@admin.com` with a password of `password`. You should change these details **immediately** after logging in for the first time.

- Optional configuration such as SMTP can be done by editing the `.env` file located at: 

```
/opt/bookstack/www/.env
```

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        bookstack_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `bookstack_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `bookstack_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    bookstack_name: bookstack

    ```

??? example "Paths"

    ```yaml
    # Type: string
    bookstack_role_paths_folder: "{{ bookstack_name }}"

    # Type: string
    bookstack_role_paths_location: "{{ server_appdata_path }}/{{ bookstack_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    bookstack_role_web_subdomain: "{{ bookstack_name }}"

    # Type: string
    bookstack_role_web_domain: "{{ user.domain }}"

    # Type: string
    bookstack_role_web_port: "80"

    # Type: string
    bookstack_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='bookstack') + '.' + lookup('role_var', '_web_domain', role='bookstack')
                             if (lookup('role_var', '_web_subdomain', role='bookstack') | length > 0)
                             else lookup('role_var', '_web_domain', role='bookstack')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    bookstack_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='bookstack') }}"

    # Type: string
    bookstack_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='bookstack') }}"

    # Type: bool (true/false)
    bookstack_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    bookstack_role_traefik_sso_middleware: ""

    # Type: string
    bookstack_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    bookstack_role_traefik_middleware_custom: ""

    # Type: string
    bookstack_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    bookstack_role_traefik_enabled: true

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    bookstack_role_docker_container: "{{ bookstack_name }}"

    # Image
    # Type: bool (true/false)
    bookstack_role_docker_image_pull: true

    # Type: string
    bookstack_role_docker_image_repo: "lscr.io/linuxserver/bookstack"

    # Type: string
    bookstack_role_docker_image_tag: "latest"

    # Type: string
    bookstack_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='bookstack') }}:{{ lookup('role_var', '_docker_image_tag', role='bookstack') }}"

    # Envs
    # Type: dict
    bookstack_role_docker_envs_default: 
      TZ: "{{ tz }}"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      APP_KEY: "{{ bookstack_saltbox_facts.facts.app_key }}"
      APP_URL: "{{ lookup('role_var', '_web_url', role='bookstack') }}"
      DB_HOST: "mariadb"
      DB_PORT: "3306"
      DB_USERNAME: "root"
      DB_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='mariadb') }}"
      DB_DATABASE: bookstackapp

    # Type: dict
    bookstack_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    bookstack_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='bookstack') }}:/config"

    # Type: list
    bookstack_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    bookstack_role_docker_hostname: "{{ bookstack_name }}"

    # Networks
    # Type: string
    bookstack_role_docker_networks_alias: "{{ bookstack_name }}"

    # Type: list
    bookstack_role_docker_networks_default: []

    # Type: list
    bookstack_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    bookstack_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    bookstack_role_docker_state: started

    # Dependencies
    # Type: string
    bookstack_role_depends_on: "mariadb"

    # Type: string
    bookstack_role_depends_on_delay: "0"

    # Type: string
    bookstack_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    bookstack_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    bookstack_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    bookstack_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    bookstack_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    bookstack_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    bookstack_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    bookstack_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    bookstack_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    bookstack_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    bookstack_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    bookstack_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    bookstack_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    bookstack_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    bookstack_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    bookstack_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    bookstack_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    bookstack_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        bookstack_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "bookstack2.{{ user.domain }}"
          - "bookstack.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        bookstack_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'bookstack2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

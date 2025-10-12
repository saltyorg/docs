---
hide:
  - tags
tags:
  - wordpress
  - cms
  - web
---

# WordPress

## What is it?

[WordPress](https://wordpress.org/) is open source software you can use to create a beautiful website, blog, or app.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://wordpress.org/){: .header-icons } | [:octicons-link-16: Docs](https://wordpress.org/support/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/docker-library/wordpress){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/wordpress){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-wordpress

```

### 2. URL

- To access WordPress , visit `https://wordpress._yourdomain.com_`

### 3. Setup

- Visit the wordpress site at `https://wordpress._yourdomain.com_` and the setup screen will appear.

- No default user is configured until you run through the setup screen, so you should ideally run through setup as soon as wordpress is deployed to secure the site.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `wordpress_instances`.

    === "Role-level Override"

        Applies to all instances of wordpress:

        ```yaml
        wordpress_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `wordpress2`):

        ```yaml
        wordpress2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `wordpress_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `wordpress_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        wordpress_instances: ["wordpress"]

        ```

    === "Example"

        ```yaml
        # Type: list
        wordpress_instances: ["wordpress", "wordpress2"]

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        wordpress_role_paths_folder: "{{ wordpress_name }}"

        # Type: string
        wordpress_role_paths_location: "{{ server_appdata_path }}/{{ wordpress_role_paths_folder }}"

        # Type: bool (true/false)
        wordpress_role_paths_recursive: true

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        wordpress2_paths_folder: "{{ wordpress_name }}"

        # Type: string
        wordpress2_paths_location: "{{ server_appdata_path }}/{{ wordpress_role_paths_folder }}"

        # Type: bool (true/false)
        wordpress2_paths_recursive: true

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        wordpress_role_web_subdomain: "{{ wordpress_name }}"

        # Type: string
        wordpress_role_web_domain: "{{ user.domain }}"

        # Type: string
        wordpress_role_web_port: "80"

        # Type: string
        wordpress_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='wordpress') + '.' + lookup('role_var', '_web_domain', role='wordpress')
                                 if (lookup('role_var', '_web_subdomain', role='wordpress') | length > 0)
                                 else lookup('role_var', '_web_domain', role='wordpress')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        wordpress2_web_subdomain: "{{ wordpress_name }}"

        # Type: string
        wordpress2_web_domain: "{{ user.domain }}"

        # Type: string
        wordpress2_web_port: "80"

        # Type: string
        wordpress2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='wordpress') + '.' + lookup('role_var', '_web_domain', role='wordpress')
                             if (lookup('role_var', '_web_subdomain', role='wordpress') | length > 0)
                             else lookup('role_var', '_web_domain', role='wordpress')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        wordpress_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='wordpress') }}"

        # Type: string
        wordpress_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='wordpress') }}"

        # Type: bool (true/false)
        wordpress_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        wordpress2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='wordpress') }}"

        # Type: string
        wordpress2_dns_zone: "{{ lookup('role_var', '_web_domain', role='wordpress') }}"

        # Type: bool (true/false)
        wordpress2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        wordpress_role_traefik_sso_middleware: ""

        # Type: string
        wordpress_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        wordpress_role_traefik_middleware_custom: ""

        # Type: string
        wordpress_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        wordpress_role_traefik_enabled: true

        # Type: bool (true/false)
        wordpress_role_traefik_api_enabled: false

        # Type: string
        wordpress_role_traefik_api_endpoint: ""

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        wordpress2_traefik_sso_middleware: ""

        # Type: string
        wordpress2_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        wordpress2_traefik_middleware_custom: ""

        # Type: string
        wordpress2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        wordpress2_traefik_enabled: true

        # Type: bool (true/false)
        wordpress2_traefik_api_enabled: false

        # Type: string
        wordpress2_traefik_api_endpoint: ""

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        wordpress_role_docker_container: "{{ wordpress_name }}"

        # Image
        # Type: bool (true/false)
        wordpress_role_docker_image_pull: true

        # Type: string
        wordpress_role_docker_image_repo: "wordpress"

        # Type: string
        wordpress_role_docker_image_tag: "latest"

        # Type: string
        wordpress_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='wordpress') }}:{{ lookup('role_var', '_docker_image_tag', role='wordpress') }}"

        # Envs
        # Type: dict
        wordpress_role_docker_envs_default: 
          TZ: "{{ tz }}"
          WORDPRESS_DB_HOST: "mariadb:3306"
          WORDPRESS_DB_USER: "root"
          WORDPRESS_DB_PASSWORD: "password321"
          WORDPRESS_DB_NAME: "{{ wordpress_name }}"

        # Type: dict
        wordpress_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        wordpress_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='wordpress') }}:/var/www/html"

        # Type: list
        wordpress_role_docker_volumes_custom: []

        # Hostname
        # Type: string
        wordpress_role_docker_hostname: "{{ wordpress_name }}"

        # Networks
        # Type: string
        wordpress_role_docker_networks_alias: "{{ wordpress_name }}"

        # Type: list
        wordpress_role_docker_networks_default: []

        # Type: list
        wordpress_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        wordpress_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        wordpress_role_docker_state: started

        # User
        # Type: string
        wordpress_role_docker_user: "{{ uid }}:{{ gid }}"

        # Dependencies
        # Type: string
        wordpress_role_depends_on: "mariadb"

        # Type: string
        wordpress_role_depends_on_delay: "0"

        # Type: string
        wordpress_role_depends_on_healthchecks: "false"

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        wordpress2_docker_container: "{{ wordpress_name }}"

        # Image
        # Type: bool (true/false)
        wordpress2_docker_image_pull: true

        # Type: string
        wordpress2_docker_image_repo: "wordpress"

        # Type: string
        wordpress2_docker_image_tag: "latest"

        # Type: string
        wordpress2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='wordpress') }}:{{ lookup('role_var', '_docker_image_tag', role='wordpress') }}"

        # Envs
        # Type: dict
        wordpress2_docker_envs_default: 
          TZ: "{{ tz }}"
          WORDPRESS_DB_HOST: "mariadb:3306"
          WORDPRESS_DB_USER: "root"
          WORDPRESS_DB_PASSWORD: "password321"
          WORDPRESS_DB_NAME: "{{ wordpress_name }}"

        # Type: dict
        wordpress2_docker_envs_custom: {}

        # Volumes
        # Type: list
        wordpress2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='wordpress') }}:/var/www/html"

        # Type: list
        wordpress2_docker_volumes_custom: []

        # Hostname
        # Type: string
        wordpress2_docker_hostname: "{{ wordpress_name }}"

        # Networks
        # Type: string
        wordpress2_docker_networks_alias: "{{ wordpress_name }}"

        # Type: list
        wordpress2_docker_networks_default: []

        # Type: list
        wordpress2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        wordpress2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        wordpress2_docker_state: started

        # User
        # Type: string
        wordpress2_docker_user: "{{ uid }}:{{ gid }}"

        # Dependencies
        # Type: string
        wordpress2_depends_on: "mariadb"

        # Type: string
        wordpress2_depends_on_delay: "0"

        # Type: string
        wordpress2_depends_on_healthchecks: "false"


        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        wordpress_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        wordpress_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        wordpress_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        wordpress_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        wordpress_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        wordpress_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        wordpress_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        wordpress_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        wordpress_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        wordpress_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        wordpress_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        wordpress_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        wordpress_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        wordpress_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        wordpress_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        wordpress_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        wordpress_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            wordpress_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "wordpress2.{{ user.domain }}"
              - "wordpress.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            wordpress_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'wordpress2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `wordpress2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        wordpress2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        wordpress2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        wordpress2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        wordpress2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        wordpress2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        wordpress2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        wordpress2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        wordpress2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        wordpress2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        wordpress2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        wordpress2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        wordpress2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        wordpress2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        wordpress2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        wordpress2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        wordpress2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        wordpress2_web_scheme:

        ```

        1.  Example:

            ```yaml
            wordpress2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "wordpress2.{{ user.domain }}"
              - "wordpress.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            wordpress2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'wordpress2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

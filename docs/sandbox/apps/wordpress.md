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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

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

=== "Basics"

    ??? variable list "`wordpress_instances`"

        ```yaml
        # Type: list
        wordpress_instances: ["wordpress"]
        ```

        !!! example

            ```yaml
            # Type: list
            wordpress_instances: ["wordpress", "wordpress2"]
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`wordpress_role_paths_folder`"

            ```yaml
            # Type: string
            wordpress_role_paths_folder: "{{ wordpress_name }}"
            ```

        ??? variable string "`wordpress_role_paths_location`"

            ```yaml
            # Type: string
            wordpress_role_paths_location: "{{ server_appdata_path }}/{{ wordpress_role_paths_folder }}"
            ```

        ??? variable bool "`wordpress_role_paths_recursive`"

            ```yaml
            # Type: bool (true/false)
            wordpress_role_paths_recursive: true
            ```

    === "Instance-level"

        ??? variable string "`wordpress2_paths_folder`"

            ```yaml
            # Type: string
            wordpress2_paths_folder: "{{ wordpress_name }}"
            ```

        ??? variable string "`wordpress2_paths_location`"

            ```yaml
            # Type: string
            wordpress2_paths_location: "{{ server_appdata_path }}/{{ wordpress_role_paths_folder }}"
            ```

        ??? variable bool "`wordpress2_paths_recursive`"

            ```yaml
            # Type: bool (true/false)
            wordpress2_paths_recursive: true
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`wordpress_role_web_subdomain`"

            ```yaml
            # Type: string
            wordpress_role_web_subdomain: "{{ wordpress_name }}"
            ```

        ??? variable string "`wordpress_role_web_domain`"

            ```yaml
            # Type: string
            wordpress_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`wordpress_role_web_port`"

            ```yaml
            # Type: string
            wordpress_role_web_port: "80"
            ```

        ??? variable string "`wordpress_role_web_url`"

            ```yaml
            # Type: string
            wordpress_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='wordpress') + '.' + lookup('role_var', '_web_domain', role='wordpress')
                                     if (lookup('role_var', '_web_subdomain', role='wordpress') | length > 0)
                                     else lookup('role_var', '_web_domain', role='wordpress')) }}"
            ```

    === "Instance-level"

        ??? variable string "`wordpress2_web_subdomain`"

            ```yaml
            # Type: string
            wordpress2_web_subdomain: "{{ wordpress_name }}"
            ```

        ??? variable string "`wordpress2_web_domain`"

            ```yaml
            # Type: string
            wordpress2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`wordpress2_web_port`"

            ```yaml
            # Type: string
            wordpress2_web_port: "80"
            ```

        ??? variable string "`wordpress2_web_url`"

            ```yaml
            # Type: string
                    wordpress2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='wordpress') + '.' + lookup('role_var', '_web_domain', role='wordpress')
                                         if (lookup('role_var', '_web_subdomain', role='wordpress') | length > 0)
                                         else lookup('role_var', '_web_domain', role='wordpress')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`wordpress_role_dns_record`"

            ```yaml
            # Type: string
            wordpress_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='wordpress') }}"
            ```

        ??? variable string "`wordpress_role_dns_zone`"

            ```yaml
            # Type: string
            wordpress_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='wordpress') }}"
            ```

        ??? variable bool "`wordpress_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            wordpress_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`wordpress2_dns_record`"

            ```yaml
            # Type: string
            wordpress2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='wordpress') }}"
            ```

        ??? variable string "`wordpress2_dns_zone`"

            ```yaml
            # Type: string
            wordpress2_dns_zone: "{{ lookup('role_var', '_web_domain', role='wordpress') }}"
            ```

        ??? variable bool "`wordpress2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            wordpress2_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`wordpress_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            wordpress_role_traefik_sso_middleware: ""
            ```

        ??? variable string "`wordpress_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            wordpress_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`wordpress_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            wordpress_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`wordpress_role_traefik_certresolver`"

            ```yaml
            # Type: string
            wordpress_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`wordpress_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            wordpress_role_traefik_enabled: true
            ```

        ??? variable bool "`wordpress_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            wordpress_role_traefik_api_enabled: false
            ```

        ??? variable string "`wordpress_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            wordpress_role_traefik_api_endpoint: ""
            ```

    === "Instance-level"

        ??? variable string "`wordpress2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            wordpress2_traefik_sso_middleware: ""
            ```

        ??? variable string "`wordpress2_traefik_middleware_default`"

            ```yaml
            # Type: string
            wordpress2_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`wordpress2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            wordpress2_traefik_middleware_custom: ""
            ```

        ??? variable string "`wordpress2_traefik_certresolver`"

            ```yaml
            # Type: string
            wordpress2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`wordpress2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            wordpress2_traefik_enabled: true
            ```

        ??? variable bool "`wordpress2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            wordpress2_traefik_api_enabled: false
            ```

        ??? variable string "`wordpress2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            wordpress2_traefik_api_endpoint: ""
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`wordpress_role_docker_container`"

            ```yaml
            # Type: string
            wordpress_role_docker_container: "{{ wordpress_name }}"
            ```

        ##### Image

        ??? variable bool "`wordpress_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            wordpress_role_docker_image_pull: true
            ```

        ??? variable string "`wordpress_role_docker_image_repo`"

            ```yaml
            # Type: string
            wordpress_role_docker_image_repo: "wordpress"
            ```

        ??? variable string "`wordpress_role_docker_image_tag`"

            ```yaml
            # Type: string
            wordpress_role_docker_image_tag: "latest"
            ```

        ??? variable string "`wordpress_role_docker_image`"

            ```yaml
            # Type: string
            wordpress_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='wordpress') }}:{{ lookup('role_var', '_docker_image_tag', role='wordpress') }}"
            ```

        ##### Envs

        ??? variable dict "`wordpress_role_docker_envs_default`"

            ```yaml
            # Type: dict
            wordpress_role_docker_envs_default: 
              TZ: "{{ tz }}"
              WORDPRESS_DB_HOST: "mariadb:3306"
              WORDPRESS_DB_USER: "root"
              WORDPRESS_DB_PASSWORD: "password321"
              WORDPRESS_DB_NAME: "{{ wordpress_name }}"
            ```

        ??? variable dict "`wordpress_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            wordpress_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`wordpress_role_docker_volumes_default`"

            ```yaml
            # Type: list
            wordpress_role_docker_volumes_default: 
              - "{{ lookup('role_var', '_paths_location', role='wordpress') }}:/var/www/html"
            ```

        ??? variable list "`wordpress_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            wordpress_role_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`wordpress_role_docker_hostname`"

            ```yaml
            # Type: string
            wordpress_role_docker_hostname: "{{ wordpress_name }}"
            ```

        ##### Networks

        ??? variable string "`wordpress_role_docker_networks_alias`"

            ```yaml
            # Type: string
            wordpress_role_docker_networks_alias: "{{ wordpress_name }}"
            ```

        ??? variable list "`wordpress_role_docker_networks_default`"

            ```yaml
            # Type: list
            wordpress_role_docker_networks_default: []
            ```

        ??? variable list "`wordpress_role_docker_networks_custom`"

            ```yaml
            # Type: list
            wordpress_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`wordpress_role_docker_restart_policy`"

            ```yaml
            # Type: string
            wordpress_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`wordpress_role_docker_state`"

            ```yaml
            # Type: string
            wordpress_role_docker_state: started
            ```

        ##### User

        ??? variable string "`wordpress_role_docker_user`"

            ```yaml
            # Type: string
            wordpress_role_docker_user: "{{ uid }}:{{ gid }}"
            ```

        ##### Dependencies

        ??? variable string "`wordpress_role_depends_on`"

            ```yaml
            # Type: string
            wordpress_role_depends_on: "mariadb"
            ```

        ??? variable string "`wordpress_role_depends_on_delay`"

            ```yaml
            # Type: string
            wordpress_role_depends_on_delay: "0"
            ```

        ??? variable string "`wordpress_role_depends_on_healthchecks`"

            ```yaml
            # Type: string
            wordpress_role_depends_on_healthchecks: "false"
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`wordpress2_docker_container`"

            ```yaml
            # Type: string
            wordpress2_docker_container: "{{ wordpress_name }}"
            ```

        ##### Image

        ??? variable bool "`wordpress2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            wordpress2_docker_image_pull: true
            ```

        ??? variable string "`wordpress2_docker_image_repo`"

            ```yaml
            # Type: string
            wordpress2_docker_image_repo: "wordpress"
            ```

        ??? variable string "`wordpress2_docker_image_tag`"

            ```yaml
            # Type: string
            wordpress2_docker_image_tag: "latest"
            ```

        ??? variable string "`wordpress2_docker_image`"

            ```yaml
            # Type: string
            wordpress2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='wordpress') }}:{{ lookup('role_var', '_docker_image_tag', role='wordpress') }}"
            ```

        ##### Envs

        ??? variable dict "`wordpress2_docker_envs_default`"

            ```yaml
            # Type: dict
                    wordpress2_docker_envs_default: 
                      TZ: "{{ tz }}"
                      WORDPRESS_DB_HOST: "mariadb:3306"
                      WORDPRESS_DB_USER: "root"
                      WORDPRESS_DB_PASSWORD: "password321"
                      WORDPRESS_DB_NAME: "{{ wordpress_name }}"
            ```

        ??? variable dict "`wordpress2_docker_envs_custom`"

            ```yaml
            # Type: dict
            wordpress2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`wordpress2_docker_volumes_default`"

            ```yaml
            # Type: list
                    wordpress2_docker_volumes_default: 
                      - "{{ lookup('role_var', '_paths_location', role='wordpress') }}:/var/www/html"
            ```

        ??? variable list "`wordpress2_docker_volumes_custom`"

            ```yaml
            # Type: list
            wordpress2_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`wordpress2_docker_hostname`"

            ```yaml
            # Type: string
            wordpress2_docker_hostname: "{{ wordpress_name }}"
            ```

        ##### Networks

        ??? variable string "`wordpress2_docker_networks_alias`"

            ```yaml
            # Type: string
            wordpress2_docker_networks_alias: "{{ wordpress_name }}"
            ```

        ??? variable list "`wordpress2_docker_networks_default`"

            ```yaml
            # Type: list
            wordpress2_docker_networks_default: []
            ```

        ??? variable list "`wordpress2_docker_networks_custom`"

            ```yaml
            # Type: list
            wordpress2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`wordpress2_docker_restart_policy`"

            ```yaml
            # Type: string
            wordpress2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`wordpress2_docker_state`"

            ```yaml
            # Type: string
            wordpress2_docker_state: started
            ```

        ##### User

        ??? variable string "`wordpress2_docker_user`"

            ```yaml
            # Type: string
            wordpress2_docker_user: "{{ uid }}:{{ gid }}"
            ```

        ##### Dependencies

        ??? variable string "`wordpress2_depends_on`"

            ```yaml
            # Type: string
            wordpress2_depends_on: "mariadb"
            ```

        ??? variable string "`wordpress2_depends_on_delay`"

            ```yaml
            # Type: string
            wordpress2_depends_on_delay: "0"
            ```

        ??? variable string "`wordpress2_depends_on_healthchecks`"

            ```yaml
            # Type: string
            wordpress2_depends_on_healthchecks: "false"
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`wordpress_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            wordpress_role_autoheal_enabled: true
            ```

        ??? variable string "`wordpress_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            wordpress_role_depends_on: ""
            ```

        ??? variable string "`wordpress_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            wordpress_role_depends_on_delay: "0"
            ```

        ??? variable string "`wordpress_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            wordpress_role_depends_on_healthchecks:
            ```

        ??? variable bool "`wordpress_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            wordpress_role_diun_enabled: true
            ```

        ??? variable bool "`wordpress_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            wordpress_role_dns_enabled: true
            ```

        ??? variable bool "`wordpress_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            wordpress_role_docker_controller: true
            ```

        ??? variable bool "`wordpress_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            wordpress_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`wordpress_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            wordpress_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`wordpress_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            wordpress_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`wordpress_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            wordpress_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`wordpress_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            wordpress_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`wordpress_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            wordpress_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`wordpress_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            wordpress_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`wordpress_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            wordpress_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                wordpress_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "wordpress2.{{ user.domain }}"
                  - "wordpress.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`wordpress_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            wordpress_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                wordpress_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'wordpress2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`wordpress_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            wordpress_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `wordpress2`):

        ??? variable bool "`wordpress2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            wordpress2_autoheal_enabled: true
            ```

        ??? variable string "`wordpress2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            wordpress2_depends_on: ""
            ```

        ??? variable string "`wordpress2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            wordpress2_depends_on_delay: "0"
            ```

        ??? variable string "`wordpress2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            wordpress2_depends_on_healthchecks:
            ```

        ??? variable bool "`wordpress2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            wordpress2_diun_enabled: true
            ```

        ??? variable bool "`wordpress2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            wordpress2_dns_enabled: true
            ```

        ??? variable bool "`wordpress2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            wordpress2_docker_controller: true
            ```

        ??? variable bool "`wordpress2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            wordpress2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`wordpress2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            wordpress2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`wordpress2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            wordpress2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`wordpress2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            wordpress2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`wordpress2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            wordpress2_traefik_robot_enabled: true
            ```

        ??? variable bool "`wordpress2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            wordpress2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`wordpress2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            wordpress2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`wordpress2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            wordpress2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                wordpress2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "wordpress2.{{ user.domain }}"
                  - "wordpress.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`wordpress2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            wordpress2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                wordpress2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'wordpress2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`wordpress2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            wordpress2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
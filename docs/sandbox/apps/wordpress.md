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

- To access WordPress , visit <https://wordpress.iYOUR_DOMAIN_NAMEi>

### 3. Setup

- Visit the wordpress site at <https://wordpress.iYOUR_DOMAIN_NAMEi> and the setup screen will appear.

- No default user is configured until you run through the setup screen, so you should ideally run through setup as soon as wordpress is deployed to secure the site.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `wordpress_instances`.

    ```yaml { .sb-show-on-unchecked title="Applies to all instances of wordpress:" }
    wordpress_role_web_subdomain: "custom"
    ```

    ```yaml { .sb-show-on-checked title="Applies to a specific instance (e.g., `wordpress2`):" }
    wordpress2_web_subdomain: "custom2"
    ```

<label class="md-button md-button--stretch" for="sb-checkbox--var-level">
   <input type="checkbox" id="sb-checkbox--var-level"><span class="sb-show-on-unchecked">Show instance-level variables</span><span class="sb-show-on-checked">Show role-level variables</span>
</label>

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `wordpress_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `wordpress_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`wordpress_instances`"

        ```yaml
        # Type: list
        wordpress_instances: ["wordpress"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            wordpress_instances: ["wordpress", "wordpress2"]
            ```

=== "Paths"

    ??? variable string "`wordpress_role_paths_folder`{ .sb-show-on-unchecked }`wordpress2_paths_folder`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_paths_folder: "{{ wordpress_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_paths_folder: "{{ wordpress_name }}"
        ```

    ??? variable string "`wordpress_role_paths_location`{ .sb-show-on-unchecked }`wordpress2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_paths_location: "{{ server_appdata_path }}/{{ wordpress_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_paths_location: "{{ server_appdata_path }}/{{ wordpress_role_paths_folder }}"
        ```

    ??? variable bool "`wordpress_role_paths_recursive`{ .sb-show-on-unchecked }`wordpress2_paths_recursive`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        wordpress_role_paths_recursive: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        wordpress2_paths_recursive: true
        ```

=== "Web"

    ??? variable string "`wordpress_role_web_subdomain`{ .sb-show-on-unchecked }`wordpress2_web_subdomain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_web_subdomain: "{{ wordpress_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_web_subdomain: "{{ wordpress_name }}"
        ```

    ??? variable string "`wordpress_role_web_domain`{ .sb-show-on-unchecked }`wordpress2_web_domain`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_web_domain: "{{ user.domain }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`wordpress_role_web_port`{ .sb-show-on-unchecked }`wordpress2_web_port`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_web_port: "80"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_web_port: "80"
        ```

    ??? variable string "`wordpress_role_web_url`{ .sb-show-on-unchecked }`wordpress2_web_url`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='wordpress') + '.' + lookup('role_var', '_web_domain', role='wordpress')
                                 if (lookup('role_var', '_web_subdomain', role='wordpress') | length > 0)
                                 else lookup('role_var', '_web_domain', role='wordpress')) }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='wordpress') + '.' + lookup('role_var', '_web_domain', role='wordpress')
                             if (lookup('role_var', '_web_subdomain', role='wordpress') | length > 0)
                             else lookup('role_var', '_web_domain', role='wordpress')) }}"
        ```

=== "DNS"

    ??? variable string "`wordpress_role_dns_record`{ .sb-show-on-unchecked }`wordpress2_dns_record`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='wordpress') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='wordpress') }}"
        ```

    ??? variable string "`wordpress_role_dns_zone`{ .sb-show-on-unchecked }`wordpress2_dns_zone`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='wordpress') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_dns_zone: "{{ lookup('role_var', '_web_domain', role='wordpress') }}"
        ```

    ??? variable bool "`wordpress_role_dns_proxy`{ .sb-show-on-unchecked }`wordpress2_dns_proxy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        wordpress_role_dns_proxy: "{{ dns_proxied }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        wordpress2_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`wordpress_role_traefik_sso_middleware`{ .sb-show-on-unchecked }`wordpress2_traefik_sso_middleware`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_traefik_sso_middleware: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_traefik_sso_middleware: ""
        ```

    ??? variable string "`wordpress_role_traefik_middleware_default`{ .sb-show-on-unchecked }`wordpress2_traefik_middleware_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`wordpress_role_traefik_middleware_custom`{ .sb-show-on-unchecked }`wordpress2_traefik_middleware_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_traefik_middleware_custom: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_traefik_middleware_custom: ""
        ```

    ??? variable string "`wordpress_role_traefik_certresolver`{ .sb-show-on-unchecked }`wordpress2_traefik_certresolver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`wordpress_role_traefik_enabled`{ .sb-show-on-unchecked }`wordpress2_traefik_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        wordpress_role_traefik_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        wordpress2_traefik_enabled: true
        ```

    ??? variable bool "`wordpress_role_traefik_api_enabled`{ .sb-show-on-unchecked }`wordpress2_traefik_api_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        wordpress_role_traefik_api_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        wordpress2_traefik_api_enabled: false
        ```

    ??? variable string "`wordpress_role_traefik_api_endpoint`{ .sb-show-on-unchecked }`wordpress2_traefik_api_endpoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_traefik_api_endpoint: ""
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`wordpress_role_docker_container`{ .sb-show-on-unchecked }`wordpress2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_docker_container: "{{ wordpress_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_docker_container: "{{ wordpress_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`wordpress_role_docker_image_pull`{ .sb-show-on-unchecked }`wordpress2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        wordpress_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        wordpress2_docker_image_pull: true
        ```

    ??? variable string "`wordpress_role_docker_image_repo`{ .sb-show-on-unchecked }`wordpress2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_docker_image_repo: "wordpress"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_docker_image_repo: "wordpress"
        ```

    ??? variable string "`wordpress_role_docker_image_tag`{ .sb-show-on-unchecked }`wordpress2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_docker_image_tag: "latest"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_docker_image_tag: "latest"
        ```

    ??? variable string "`wordpress_role_docker_image`{ .sb-show-on-unchecked }`wordpress2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='wordpress') }}:{{ lookup('role_var', '_docker_image_tag', role='wordpress') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='wordpress') }}:{{ lookup('role_var', '_docker_image_tag', role='wordpress') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`wordpress_role_docker_envs_default`{ .sb-show-on-unchecked }`wordpress2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        wordpress_role_docker_envs_default: 
          TZ: "{{ tz }}"
          WORDPRESS_DB_HOST: "mariadb:3306"
          WORDPRESS_DB_USER: "root"
          WORDPRESS_DB_PASSWORD: "password321"
          WORDPRESS_DB_NAME: "{{ wordpress_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        wordpress2_docker_envs_default: 
          TZ: "{{ tz }}"
          WORDPRESS_DB_HOST: "mariadb:3306"
          WORDPRESS_DB_USER: "root"
          WORDPRESS_DB_PASSWORD: "password321"
          WORDPRESS_DB_NAME: "{{ wordpress_name }}"
        ```

    ??? variable dict "`wordpress_role_docker_envs_custom`{ .sb-show-on-unchecked }`wordpress2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        wordpress_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        wordpress2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`wordpress_role_docker_volumes_default`{ .sb-show-on-unchecked }`wordpress2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        wordpress_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='wordpress') }}:/var/www/html"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        wordpress2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='wordpress') }}:/var/www/html"
        ```

    ??? variable list "`wordpress_role_docker_volumes_custom`{ .sb-show-on-unchecked }`wordpress2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        wordpress_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        wordpress2_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`wordpress_role_docker_hostname`{ .sb-show-on-unchecked }`wordpress2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_docker_hostname: "{{ wordpress_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_docker_hostname: "{{ wordpress_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`wordpress_role_docker_networks_alias`{ .sb-show-on-unchecked }`wordpress2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_docker_networks_alias: "{{ wordpress_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_docker_networks_alias: "{{ wordpress_name }}"
        ```

    ??? variable list "`wordpress_role_docker_networks_default`{ .sb-show-on-unchecked }`wordpress2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        wordpress_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        wordpress2_docker_networks_default: []
        ```

    ??? variable list "`wordpress_role_docker_networks_custom`{ .sb-show-on-unchecked }`wordpress2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        wordpress_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        wordpress2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`wordpress_role_docker_restart_policy`{ .sb-show-on-unchecked }`wordpress2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`wordpress_role_docker_state`{ .sb-show-on-unchecked }`wordpress2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`wordpress_role_docker_user`{ .sb-show-on-unchecked }`wordpress2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_docker_user: "{{ uid }}:{{ gid }}"
        ```

    <h5>Dependencies</h5>

    ??? variable string "`wordpress_role_depends_on`{ .sb-show-on-unchecked }`wordpress2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_depends_on: "mariadb"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_depends_on: "mariadb"
        ```

    ??? variable string "`wordpress_role_depends_on_delay`{ .sb-show-on-unchecked }`wordpress2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_depends_on_delay: "0"
        ```

    ??? variable string "`wordpress_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`wordpress2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        wordpress_role_depends_on_healthchecks: "false"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        wordpress2_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`wordpress_role_autoheal_enabled`{ .sb-show-on-unchecked }`wordpress2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        wordpress_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        wordpress2_autoheal_enabled: true
        ```

    ??? variable string "`wordpress_role_depends_on`{ .sb-show-on-unchecked }`wordpress2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        wordpress_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        wordpress2_depends_on: ""
        ```

    ??? variable string "`wordpress_role_depends_on_delay`{ .sb-show-on-unchecked }`wordpress2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        wordpress_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        wordpress2_depends_on_delay: "0"
        ```

    ??? variable string "`wordpress_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`wordpress2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        wordpress_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        wordpress2_depends_on_healthchecks:
        ```

    ??? variable bool "`wordpress_role_diun_enabled`{ .sb-show-on-unchecked }`wordpress2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        wordpress_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        wordpress2_diun_enabled: true
        ```

    ??? variable bool "`wordpress_role_dns_enabled`{ .sb-show-on-unchecked }`wordpress2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        wordpress_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        wordpress2_dns_enabled: true
        ```

    ??? variable bool "`wordpress_role_docker_controller`{ .sb-show-on-unchecked }`wordpress2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        wordpress_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        wordpress2_docker_controller: true
        ```

    ??? variable bool "`wordpress_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`wordpress2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        wordpress_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        wordpress2_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`wordpress_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`wordpress2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        wordpress_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        wordpress2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`wordpress_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`wordpress2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        wordpress_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        wordpress2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`wordpress_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`wordpress2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        wordpress_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        wordpress2_traefik_gzip_enabled: false
        ```

    ??? variable bool "`wordpress_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`wordpress2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        wordpress_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        wordpress2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`wordpress_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`wordpress2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        wordpress_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        wordpress2_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`wordpress_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`wordpress2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        wordpress_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        wordpress2_traefik_robot_enabled: true
        ```

    ??? variable bool "`wordpress_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`wordpress2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        wordpress_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        wordpress2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`wordpress_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`wordpress2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        wordpress_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        wordpress2_traefik_wildcard_enabled: true
        ```

    ??? variable list "`wordpress_role_web_fqdn_override`{ .sb-show-on-unchecked }`wordpress2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        wordpress_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        wordpress2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            wordpress_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "wordpress2.{{ user.domain }}"
              - "wordpress.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            wordpress2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "wordpress2.{{ user.domain }}"
              - "wordpress.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`wordpress_role_web_host_override`{ .sb-show-on-unchecked }`wordpress2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        wordpress_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        wordpress2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            wordpress_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'wordpress2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            wordpress2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'wordpress2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`wordpress_role_web_scheme`{ .sb-show-on-unchecked }`wordpress2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        wordpress_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        wordpress2_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
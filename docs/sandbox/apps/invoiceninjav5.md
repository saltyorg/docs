---
hide:
  - tags
tags:
  - invoiceninja
  - finance
  - invoicing
---

# Invoice Ninja v5

## What is it?

[InvoiceNinja](https://www.invoiceninja.com/) is a self-hosted accounting system with ability to Quote & Invoice Clients, Time Billable-Tasks, Track Expenses, Get Paid.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.invoiceninja.com/){: .header-icons } | [:octicons-link-16: Docs](https://invoiceninja.github.io/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/invoiceninja/invoiceninja/tree/v5-stable){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/invoiceninja/invoiceninja/){: .header-icons }|

### 1. Installation

Ideally you should set a unique app key in settings.yml.
Generate the key using:

``` shell
docker run --rm -it invoiceninja/invoiceninja php artisan key:generate --show
```

insert this in the invoiceninja.app_key setting in `/opt/sandbox/settings.yml`

``` shell

sb install sandbox-invoiceninja

```

### 2. URL

- To access Invoice Ninja, visit `https://invoiceninja._yourdomain.com_`

### 3. Log in

Enter email, and password from accounts.yml setting.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        invoiceninjav5_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `invoiceninjav5_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `invoiceninjav5_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`invoiceninjav5_name`"

        ```yaml
        # Type: string
        invoiceninjav5_name: "invoiceninja"
        ```

=== "Settings"

    ??? variable bool "`invoiceninjav5_overwrite_nginx_config`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_overwrite_nginx_config: true
        ```

=== "Paths"

    ??? variable string "`invoiceninjav5_role_paths_folder`"

        ```yaml
        # Type: string
        invoiceninjav5_role_paths_folder: "{{ invoiceninjav5_name }}"
        ```

    ??? variable string "`invoiceninjav5_role_paths_location`"

        ```yaml
        # Type: string
        invoiceninjav5_role_paths_location: "{{ server_appdata_path }}/{{ invoiceninjav5_role_paths_folder }}"
        ```

    ??? variable bool "`invoiceninjav5_role_paths_recursive`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_role_paths_recursive: true
        ```

    ??? variable string "`invoiceninjav5_role_paths_owner`"

        ```yaml
        # Type: string
        invoiceninjav5_role_paths_owner: "1500"
        ```

    ??? variable string "`invoiceninjav5_role_paths_group`"

        ```yaml
        # Type: string
        invoiceninjav5_role_paths_group: "1500"
        ```

=== "Web"

    ??? variable string "`invoiceninjav5_role_nginx_web_subdomain`"

        ```yaml
        # Type: string
        invoiceninjav5_role_nginx_web_subdomain: "invoiceninja"
        ```

    ??? variable string "`invoiceninjav5_role_nginx_web_domain`"

        ```yaml
        # Type: string
        invoiceninjav5_role_nginx_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`invoiceninjav5_role_nginx_web_port`"

        ```yaml
        # Type: string
        invoiceninjav5_role_nginx_web_port: "80"
        ```

    ??? variable string "`invoiceninjav5_role_nginx_web_url`"

        ```yaml
        # Type: string
        invoiceninjav5_role_nginx_web_url: "{{ 'https://' + (lookup('role_var', '_nginx_web_subdomain', role='invoiceninjav5') + '.' + lookup('role_var', '_nginx_web_domain', role='invoiceninjav5')
                                            if (lookup('role_var', '_nginx_web_subdomain', role='invoiceninjav5') | length > 0)
                                            else lookup('role_var', '_nginx_web_domain', role='invoiceninjav5')) }}"
        ```

=== "DNS"

    ??? variable string "`invoiceninjav5_role_nginx_dns_record`"

        ```yaml
        # Type: string
        invoiceninjav5_role_nginx_dns_record: "{{ lookup('role_var', '_nginx_web_subdomain', role='invoiceninjav5') }}"
        ```

    ??? variable string "`invoiceninjav5_role_nginx_dns_zone`"

        ```yaml
        # Type: string
        invoiceninjav5_role_nginx_dns_zone: "{{ lookup('role_var', '_nginx_web_domain', role='invoiceninjav5') }}"
        ```

    ??? variable bool "`invoiceninjav5_role_nginx_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_role_nginx_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Docker"

    ##### Container

    ??? variable string "`invoiceninjav5_role_docker_container`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_container: "{{ invoiceninjav5_name }}"
        ```

    ##### Image

    ??? variable bool "`invoiceninjav5_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        invoiceninjav5_role_docker_image_pull: true
        ```

    ??? variable string "`invoiceninjav5_role_docker_image_repo`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_image_repo: "invoiceninja/invoiceninja"
        ```

    ??? variable string "`invoiceninjav5_role_docker_image_tag`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_image_tag: "5"
        ```

    ??? variable string "`invoiceninjav5_role_docker_image`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='invoiceninjav5') }}:{{ lookup('role_var', '_docker_image_tag', role='invoiceninjav5') }}"
        ```

    ##### Envs

    ??? variable dict "`invoiceninjav5_role_docker_envs_default`"

        ```yaml
        # Type: dict
        invoiceninjav5_role_docker_envs_default: 
          TZ: "{{ tz }}"
          APP_URL: "{{ lookup('role_var', '_nginx_web_url', role='invoiceninjav5') }}"
          APP_KEY: "{{ invoiceninja.app_key | default('base64:O1S3kAJEDgo92gPkXtxfdCJpoGShgKloUSdcaHMXmoY=', true) }}"
          APP_ENV: "production"
          APP_DEBUG: "false"
          TRUSTED_PROXIES: "*"
          REQUIRE_HTTPS: "true"
          DB_TYPE: "mysql"
          DB_HOST: "mariadb"
          DB_USERNAME: "root"
          DB_PASSWORD: "password321"
          DB_DATABASE: "invoiceninjav5db"
          DB_PORT: "3306"
          PDF_GENERATOR: "hosted_ninja"
          IS_DOCKER: "true"
          PHANTOMJS_PDF_GENERATION: "false"
          IN_USER_EMAIL: "{{ user.email }}"
          IN_PASSWORD: "{{ user.pass }}"
        ```

    ??? variable dict "`invoiceninjav5_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        invoiceninjav5_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`invoiceninjav5_role_docker_volumes_default`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='invoiceninjav5') }}/public:/var/www/app/public"
          - "{{ lookup('role_var', '_paths_location', role='invoiceninjav5') }}/storage:/var/www/app/storage"
          - "{{ lookup('role_var', '_paths_location', role='invoiceninjav5') }}/php.ini:/usr/local/etc/php/php.ini"
          - "{{ lookup('role_var', '_paths_location', role='invoiceninjav5') }}/php-cli.ini:/usr/local/etc/php/php-cli.ini"
        ```

    ??? variable list "`invoiceninjav5_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`invoiceninjav5_role_docker_hostname`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_hostname: "{{ invoiceninjav5_name }}"
        ```

    ##### Networks

    ??? variable string "`invoiceninjav5_role_docker_networks_alias`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_networks_alias: "{{ invoiceninjav5_name }}"
        ```

    ??? variable list "`invoiceninjav5_role_docker_networks_default`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_networks_default: []
        ```

    ??? variable list "`invoiceninjav5_role_docker_networks_custom`"

        ```yaml
        # Type: list
        invoiceninjav5_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`invoiceninjav5_role_docker_restart_policy`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`invoiceninjav5_role_docker_state`"

        ```yaml
        # Type: string
        invoiceninjav5_role_docker_state: started
        ```

    ##### Dependencies

    ??? variable string "`invoiceninjav5_role_depends_on`"

        ```yaml
        # Type: string
        invoiceninjav5_role_depends_on: "invoiceninja-nginx,mariadb"
        ```

    ??? variable string "`invoiceninjav5_role_depends_on_delay`"

        ```yaml
        # Type: string
        invoiceninjav5_role_depends_on_delay: "0"
        ```

    ??? variable string "`invoiceninjav5_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        invoiceninjav5_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`invoiceninjav5_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        invoiceninjav5_role_autoheal_enabled: true
        ```

    ??? variable string "`invoiceninjav5_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        invoiceninjav5_role_depends_on: ""
        ```

    ??? variable string "`invoiceninjav5_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        invoiceninjav5_role_depends_on_delay: "0"
        ```

    ??? variable string "`invoiceninjav5_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        invoiceninjav5_role_depends_on_healthchecks:
        ```

    ??? variable bool "`invoiceninjav5_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        invoiceninjav5_role_diun_enabled: true
        ```

    ??? variable bool "`invoiceninjav5_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        invoiceninjav5_role_dns_enabled: true
        ```

    ??? variable bool "`invoiceninjav5_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        invoiceninjav5_role_docker_controller: true
        ```

    ??? variable bool "`invoiceninjav5_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        invoiceninjav5_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`invoiceninjav5_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        invoiceninjav5_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`invoiceninjav5_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        invoiceninjav5_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`invoiceninjav5_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        invoiceninjav5_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`invoiceninjav5_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        invoiceninjav5_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`invoiceninjav5_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        invoiceninjav5_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`invoiceninjav5_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        invoiceninjav5_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`invoiceninjav5_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        invoiceninjav5_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            invoiceninjav5_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "invoiceninjav52.{{ user.domain }}"
              - "invoiceninjav5.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`invoiceninjav5_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        invoiceninjav5_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            invoiceninjav5_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'invoiceninjav52.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`invoiceninjav5_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        invoiceninjav5_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
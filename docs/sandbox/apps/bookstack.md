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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

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

=== "Basics"

    ??? variable string "`bookstack_name`"

        ```yaml
        # Type: string
        bookstack_name: bookstack
        ```

=== "Paths"

    ??? variable string "`bookstack_role_paths_folder`"

        ```yaml
        # Type: string
        bookstack_role_paths_folder: "{{ bookstack_name }}"
        ```

    ??? variable string "`bookstack_role_paths_location`"

        ```yaml
        # Type: string
        bookstack_role_paths_location: "{{ server_appdata_path }}/{{ bookstack_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`bookstack_role_web_subdomain`"

        ```yaml
        # Type: string
        bookstack_role_web_subdomain: "{{ bookstack_name }}"
        ```

    ??? variable string "`bookstack_role_web_domain`"

        ```yaml
        # Type: string
        bookstack_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`bookstack_role_web_port`"

        ```yaml
        # Type: string
        bookstack_role_web_port: "80"
        ```

    ??? variable string "`bookstack_role_web_url`"

        ```yaml
        # Type: string
        bookstack_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='bookstack') + '.' + lookup('role_var', '_web_domain', role='bookstack')
                                 if (lookup('role_var', '_web_subdomain', role='bookstack') | length > 0)
                                 else lookup('role_var', '_web_domain', role='bookstack')) }}"
        ```

=== "DNS"

    ??? variable string "`bookstack_role_dns_record`"

        ```yaml
        # Type: string
        bookstack_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='bookstack') }}"
        ```

    ??? variable string "`bookstack_role_dns_zone`"

        ```yaml
        # Type: string
        bookstack_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='bookstack') }}"
        ```

    ??? variable bool "`bookstack_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`bookstack_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        bookstack_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`bookstack_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        bookstack_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`bookstack_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        bookstack_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`bookstack_role_traefik_certresolver`"

        ```yaml
        # Type: string
        bookstack_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`bookstack_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_traefik_enabled: true
        ```

=== "Docker"

    ##### Container

    ??? variable string "`bookstack_role_docker_container`"

        ```yaml
        # Type: string
        bookstack_role_docker_container: "{{ bookstack_name }}"
        ```

    ##### Image

    ??? variable bool "`bookstack_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        bookstack_role_docker_image_pull: true
        ```

    ??? variable string "`bookstack_role_docker_image_repo`"

        ```yaml
        # Type: string
        bookstack_role_docker_image_repo: "lscr.io/linuxserver/bookstack"
        ```

    ??? variable string "`bookstack_role_docker_image_tag`"

        ```yaml
        # Type: string
        bookstack_role_docker_image_tag: "latest"
        ```

    ??? variable string "`bookstack_role_docker_image`"

        ```yaml
        # Type: string
        bookstack_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='bookstack') }}:{{ lookup('role_var', '_docker_image_tag', role='bookstack') }}"
        ```

    ##### Envs

    ??? variable dict "`bookstack_role_docker_envs_default`"

        ```yaml
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
        ```

    ??? variable dict "`bookstack_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        bookstack_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`bookstack_role_docker_volumes_default`"

        ```yaml
        # Type: list
        bookstack_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='bookstack') }}:/config"
        ```

    ??? variable list "`bookstack_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        bookstack_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`bookstack_role_docker_hostname`"

        ```yaml
        # Type: string
        bookstack_role_docker_hostname: "{{ bookstack_name }}"
        ```

    ##### Networks

    ??? variable string "`bookstack_role_docker_networks_alias`"

        ```yaml
        # Type: string
        bookstack_role_docker_networks_alias: "{{ bookstack_name }}"
        ```

    ??? variable list "`bookstack_role_docker_networks_default`"

        ```yaml
        # Type: list
        bookstack_role_docker_networks_default: []
        ```

    ??? variable list "`bookstack_role_docker_networks_custom`"

        ```yaml
        # Type: list
        bookstack_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`bookstack_role_docker_restart_policy`"

        ```yaml
        # Type: string
        bookstack_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`bookstack_role_docker_state`"

        ```yaml
        # Type: string
        bookstack_role_docker_state: started
        ```

    ##### Dependencies

    ??? variable string "`bookstack_role_depends_on`"

        ```yaml
        # Type: string
        bookstack_role_depends_on: "mariadb"
        ```

    ??? variable string "`bookstack_role_depends_on_delay`"

        ```yaml
        # Type: string
        bookstack_role_depends_on_delay: "0"
        ```

    ??? variable string "`bookstack_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        bookstack_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`bookstack_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        bookstack_role_autoheal_enabled: true
        ```

    ??? variable string "`bookstack_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        bookstack_role_depends_on: ""
        ```

    ??? variable string "`bookstack_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        bookstack_role_depends_on_delay: "0"
        ```

    ??? variable string "`bookstack_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        bookstack_role_depends_on_healthchecks:
        ```

    ??? variable bool "`bookstack_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        bookstack_role_diun_enabled: true
        ```

    ??? variable bool "`bookstack_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        bookstack_role_dns_enabled: true
        ```

    ??? variable bool "`bookstack_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        bookstack_role_docker_controller: true
        ```

    ??? variable bool "`bookstack_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        bookstack_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`bookstack_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        bookstack_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`bookstack_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        bookstack_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`bookstack_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        bookstack_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`bookstack_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        bookstack_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`bookstack_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        bookstack_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`bookstack_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        bookstack_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`bookstack_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        bookstack_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            bookstack_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "bookstack2.{{ user.domain }}"
              - "bookstack.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`bookstack_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        bookstack_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            bookstack_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'bookstack2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`bookstack_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        bookstack_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
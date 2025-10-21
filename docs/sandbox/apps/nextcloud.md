---
hide:
  - tags
tags:
  - nextcloud
  - productivity
  - cloud
---

# Nextcloud

## What is it?

[Nextcloud](https://nextcloud.com/) is safe home for all your data. Access & share your files, calendars, contacts, mail & more from any device, on your terms.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://nextcloud.com/){: .header-icons } | [:octicons-link-16: Docs](https://docs.nextcloud.com/server/latest/admin_manual/contents.html){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/nextcloud/docker){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/nextcloud){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-nextcloud

```

### 2. URL

- To access Nextcloud, visit `https://nextcloud._yourdomain.com_`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        nextcloud_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `nextcloud_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `nextcloud_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`nextcloud_name`"

        ```yaml
        # Type: string
        nextcloud_name: nextcloud
        ```

=== "Settings"

    ??? variable string "`nextcloud_role_data_directory`"

        ```yaml
        # Type: string
        nextcloud_role_data_directory: "/var/www/html/data"
        ```

    ??? variable string "`nextcloud_role_php_memory_limit`"

        ```yaml
        # Type: string
        nextcloud_role_php_memory_limit: "512M"
        ```

    ??? variable string "`nextcloud_role_php_upload_limit`"

        ```yaml
        # Type: string
        nextcloud_role_php_upload_limit: "512M"
        ```

=== "Paths"

    ??? variable string "`nextcloud_role_paths_folder`"

        ```yaml
        # Type: string
        nextcloud_role_paths_folder: "{{ nextcloud_name }}"
        ```

    ??? variable string "`nextcloud_role_paths_location`"

        ```yaml
        # Type: string
        nextcloud_role_paths_location: "{{ server_appdata_path }}/{{ nextcloud_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`nextcloud_role_web_subdomain`"

        ```yaml
        # Type: string
        nextcloud_role_web_subdomain: "{{ nextcloud_name }}"
        ```

    ??? variable string "`nextcloud_role_web_domain`"

        ```yaml
        # Type: string
        nextcloud_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`nextcloud_role_web_port`"

        ```yaml
        # Type: string
        nextcloud_role_web_port: "80"
        ```

    ??? variable string "`nextcloud_role_web_url`"

        ```yaml
        # Type: string
        nextcloud_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='nextcloud') + '.' + lookup('role_var', '_web_domain', role='nextcloud')
                                 if (lookup('role_var', '_web_subdomain', role='nextcloud') | length > 0)
                                 else lookup('role_var', '_web_domain', role='nextcloud')) }}"
        ```

=== "DNS"

    ??? variable string "`nextcloud_role_dns_record`"

        ```yaml
        # Type: string
        nextcloud_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='nextcloud') }}"
        ```

    ??? variable string "`nextcloud_role_dns_zone`"

        ```yaml
        # Type: string
        nextcloud_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='nextcloud') }}"
        ```

    ??? variable bool "`nextcloud_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        nextcloud_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`nextcloud_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        nextcloud_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`nextcloud_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        nextcloud_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`nextcloud_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        nextcloud_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`nextcloud_role_traefik_certresolver`"

        ```yaml
        # Type: string
        nextcloud_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`nextcloud_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        nextcloud_role_traefik_enabled: true
        ```

    ??? variable bool "`nextcloud_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        nextcloud_role_traefik_api_enabled: false
        ```

    ??? variable string "`nextcloud_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        nextcloud_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`nextcloud_role_docker_container`"

        ```yaml
        # Type: string
        nextcloud_role_docker_container: "{{ nextcloud_name }}"
        ```

    ##### Image

    ??? variable bool "`nextcloud_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        nextcloud_role_docker_image_pull: true
        ```

    ??? variable string "`nextcloud_role_docker_image_tag`"

        ```yaml
        # Type: string
        nextcloud_role_docker_image_tag: "latest"
        ```

    ??? variable string "`nextcloud_role_docker_image_repo`"

        ```yaml
        # Type: string
        nextcloud_role_docker_image_repo: "nextcloud"
        ```

    ??? variable string "`nextcloud_role_docker_image`"

        ```yaml
        # Type: string
        nextcloud_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='nextcloud') }}:{{ lookup('role_var', '_docker_image_tag', role='nextcloud') }}"
        ```

    ##### Envs

    ??? variable dict "`nextcloud_role_docker_envs_default`"

        ```yaml
        # Type: dict
        nextcloud_role_docker_envs_default: 
          TZ: "{{ tz }}"
          NEXTCLOUD_ADMIN_USER: "{{ user.name }}"
          NEXTCLOUD_ADMIN_PASSWORD: "{{ user.pass }}"
          NEXTCLOUD_TRUSTED_DOMAINS: "{{ lookup('role_var', '_web_subdomain', role='nextcloud') + '.' + lookup('role_var', '_web_domain', role='nextcloud') }}"
          NEXTCLOUD_DATA_DIR: "{{ lookup('role_var', '_data_directory', role='nextcloud') }}"
          MYSQL_DATABASE: "nextcloud"
          MYSQL_USER: "root"
          MYSQL_PASSWORD: "{{ lookup('role_var', '_docker_env_password', role='mariadb') }}"
          MYSQL_HOST: "mariadb"
          OVERWRITEHOST: "{{ lookup('role_var', '_web_subdomain', role='nextcloud') + '.' + lookup('role_var', '_web_domain', role='nextcloud') }}"
          OVERWRITEPROTOCOL: "https"
          OVERWRITECLIURL: "{{ lookup('role_var', '_web_url', role='nextcloud') }}"
          PHP_MEMORY_LIMIT: "{{ lookup('role_var', '_php_memory_limit', role='nextcloud') }}"
          PHP_UPLOAD_LIMIT: "{{ lookup('role_var', '_php_upload_limit', role='nextcloud') }}"
          TRUSTED_PROXIES: "172.19.0.0/16"
        ```

    ??? variable dict "`nextcloud_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        nextcloud_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`nextcloud_role_docker_volumes_default`"

        ```yaml
        # Type: list
        nextcloud_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='nextcloud') }}:/var/www/html"
        ```

    ??? variable list "`nextcloud_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        nextcloud_role_docker_volumes_custom: []
        ```

    ##### Labels

    ??? variable dict "`nextcloud_role_docker_labels_default`"

        ```yaml
        # Type: dict
        nextcloud_role_docker_labels_default: 
          traefik.http.middlewares.nextcloud-caldav.replacepathregex.regex: "^/.well-known/ca(l|rd)dav"
          traefik.http.middlewares.nextcloud-caldav.replacepathregex.replacement: "/remote.php/dav/"
        ```

    ??? variable dict "`nextcloud_role_docker_labels_custom`"

        ```yaml
        # Type: dict
        nextcloud_role_docker_labels_custom: {}
        ```

    ##### Hostname

    ??? variable string "`nextcloud_role_docker_hostname`"

        ```yaml
        # Type: string
        nextcloud_role_docker_hostname: "{{ nextcloud_name }}"
        ```

    ##### Networks

    ??? variable string "`nextcloud_role_docker_networks_alias`"

        ```yaml
        # Type: string
        nextcloud_role_docker_networks_alias: "{{ nextcloud_name }}"
        ```

    ??? variable list "`nextcloud_role_docker_networks_default`"

        ```yaml
        # Type: list
        nextcloud_role_docker_networks_default: []
        ```

    ??? variable list "`nextcloud_role_docker_networks_custom`"

        ```yaml
        # Type: list
        nextcloud_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`nextcloud_role_docker_restart_policy`"

        ```yaml
        # Type: string
        nextcloud_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`nextcloud_role_docker_state`"

        ```yaml
        # Type: string
        nextcloud_role_docker_state: started
        ```

    ##### User

    ??? variable string "`nextcloud_role_docker_user`"

        ```yaml
        # Type: string
        nextcloud_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

    ##### Dependencies

    ??? variable string "`nextcloud_role_depends_on`"

        ```yaml
        # Type: string
        nextcloud_role_depends_on: "mariadb"
        ```

    ??? variable string "`nextcloud_role_depends_on_delay`"

        ```yaml
        # Type: string
        nextcloud_role_depends_on_delay: "0"
        ```

    ??? variable string "`nextcloud_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        nextcloud_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`nextcloud_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        nextcloud_role_autoheal_enabled: true
        ```

    ??? variable string "`nextcloud_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        nextcloud_role_depends_on: ""
        ```

    ??? variable string "`nextcloud_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        nextcloud_role_depends_on_delay: "0"
        ```

    ??? variable string "`nextcloud_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        nextcloud_role_depends_on_healthchecks:
        ```

    ??? variable bool "`nextcloud_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        nextcloud_role_diun_enabled: true
        ```

    ??? variable bool "`nextcloud_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        nextcloud_role_dns_enabled: true
        ```

    ??? variable bool "`nextcloud_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        nextcloud_role_docker_controller: true
        ```

    ??? variable bool "`nextcloud_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        nextcloud_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`nextcloud_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        nextcloud_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`nextcloud_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        nextcloud_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`nextcloud_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        nextcloud_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`nextcloud_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        nextcloud_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`nextcloud_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        nextcloud_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`nextcloud_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        nextcloud_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`nextcloud_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        nextcloud_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            nextcloud_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "nextcloud2.{{ user.domain }}"
              - "nextcloud.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`nextcloud_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        nextcloud_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            nextcloud_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'nextcloud2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`nextcloud_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        nextcloud_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
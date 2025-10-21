---
hide:
  - tags
tags:
  - plexshare
  - plex
  - sharing
---

# PlexShare

## What is it?

[PlexShare](https://chewbaka69.github.io/PlexShare/) is a standalone web application that provides management of local users and multiple Plex servers with their libraries. It allows users to access libraries from all registered servers through a single interface without requiring plex.tv registration.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://chewbaka69.github.io/PlexShare/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Chewbaka69/PlexShare){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/chewbaka/plexshare){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-plexshare
```

### 2. URL

- To access PlexShare, visit `https://plexshare._yourdomain.com_`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        plexshare_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `plexshare_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `plexshare_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`plexshare_name`"

        ```yaml
        # Type: string
        plexshare_name: plexshare
        ```

=== "Paths"

    ??? variable string "`plexshare_role_paths_folder`"

        ```yaml
        # Type: string
        plexshare_role_paths_folder: "{{ plexshare_name }}"
        ```

    ??? variable string "`plexshare_role_paths_location`"

        ```yaml
        # Type: string
        plexshare_role_paths_location: "{{ server_appdata_path }}/{{ plexshare_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`plexshare_role_web_subdomain`"

        ```yaml
        # Type: string
        plexshare_role_web_subdomain: "{{ plexshare_name }}"
        ```

    ??? variable string "`plexshare_role_web_domain`"

        ```yaml
        # Type: string
        plexshare_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`plexshare_role_web_port`"

        ```yaml
        # Type: string
        plexshare_role_web_port: "80"
        ```

    ??? variable string "`plexshare_role_web_url`"

        ```yaml
        # Type: string
        plexshare_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='plexshare') + '.' + lookup('role_var', '_web_domain', role='plexshare')
                                 if (lookup('role_var', '_web_subdomain', role='plexshare') | length > 0)
                                 else lookup('role_var', '_web_domain', role='plexshare')) }}"
        ```

=== "DNS"

    ??? variable string "`plexshare_role_dns_record`"

        ```yaml
        # Type: string
        plexshare_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='plexshare') }}"
        ```

    ??? variable string "`plexshare_role_dns_zone`"

        ```yaml
        # Type: string
        plexshare_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='plexshare') }}"
        ```

    ??? variable bool "`plexshare_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`plexshare_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        plexshare_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`plexshare_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        plexshare_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`plexshare_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        plexshare_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`plexshare_role_traefik_certresolver`"

        ```yaml
        # Type: string
        plexshare_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`plexshare_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_traefik_enabled: true
        ```

    ??? variable bool "`plexshare_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_traefik_api_enabled: false
        ```

    ??? variable string "`plexshare_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        plexshare_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`plexshare_role_docker_container`"

        ```yaml
        # Type: string
        plexshare_role_docker_container: "{{ plexshare_name }}"
        ```

    ##### Image

    ??? variable bool "`plexshare_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        plexshare_role_docker_image_pull: true
        ```

    ??? variable string "`plexshare_role_docker_image_tag`"

        ```yaml
        # Type: string
        plexshare_role_docker_image_tag: "latest"
        ```

    ??? variable string "`plexshare_role_docker_image_repo`"

        ```yaml
        # Type: string
        plexshare_role_docker_image_repo: "chewbaka/plexshare"
        ```

    ??? variable string "`plexshare_role_docker_image`"

        ```yaml
        # Type: string
        plexshare_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='plexshare') }}:{{ lookup('role_var', '_docker_image_tag', role='plexshare') }}"
        ```

    ##### Envs

    ??? variable dict "`plexshare_role_docker_envs_default`"

        ```yaml
        # Type: dict
        plexshare_role_docker_envs_default: 
          TZ: "{{ tz }}"
          WEB_DOCUMENT_ROOT: "/app/public"
          WEB_DOCUMENT_INDEX: "index.php"
          LOG_STDOUT: "./var/log/plexshare.stdout.log"
          LOG_STDERR: "./var/log/plexshare.stderr.log"
          PHP_POST_MAX_SIZE: "20M"
          PHP_MEMORY_LIMIT: "521M"
          PHP_MAX_EXECUTION_TIME: "300"
          PHP_DATE_TIMEZONE: "{{ tz }}"
          COMPOSER_VERSION: "1"
          BASE_URL: "{{ lookup('role_var', '_web_url', role='plexshare') }}/"
        ```

    ??? variable dict "`plexshare_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        plexshare_role_docker_envs_custom: {}
        ```

    ##### Hostname

    ??? variable string "`plexshare_role_docker_hostname`"

        ```yaml
        # Type: string
        plexshare_role_docker_hostname: "{{ plexshare_name }}"
        ```

    ##### Networks

    ??? variable string "`plexshare_role_docker_networks_alias`"

        ```yaml
        # Type: string
        plexshare_role_docker_networks_alias: "{{ plexshare_name }}"
        ```

    ??? variable list "`plexshare_role_docker_networks_default`"

        ```yaml
        # Type: list
        plexshare_role_docker_networks_default: []
        ```

    ??? variable list "`plexshare_role_docker_networks_custom`"

        ```yaml
        # Type: list
        plexshare_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`plexshare_role_docker_restart_policy`"

        ```yaml
        # Type: string
        plexshare_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`plexshare_role_docker_state`"

        ```yaml
        # Type: string
        plexshare_role_docker_state: started
        ```

    ##### Dependencies

    ??? variable string "`plexshare_role_depends_on`"

        ```yaml
        # Type: string
        plexshare_role_depends_on: "{{ plexshare_name }}-mariadb"
        ```

    ??? variable string "`plexshare_role_depends_on_delay`"

        ```yaml
        # Type: string
        plexshare_role_depends_on_delay: "0"
        ```

    ??? variable string "`plexshare_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        plexshare_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`plexshare_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        plexshare_role_autoheal_enabled: true
        ```

    ??? variable string "`plexshare_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        plexshare_role_depends_on: ""
        ```

    ??? variable string "`plexshare_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        plexshare_role_depends_on_delay: "0"
        ```

    ??? variable string "`plexshare_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        plexshare_role_depends_on_healthchecks:
        ```

    ??? variable bool "`plexshare_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        plexshare_role_diun_enabled: true
        ```

    ??? variable bool "`plexshare_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        plexshare_role_dns_enabled: true
        ```

    ??? variable bool "`plexshare_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        plexshare_role_docker_controller: true
        ```

    ??? variable bool "`plexshare_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        plexshare_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`plexshare_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        plexshare_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`plexshare_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        plexshare_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`plexshare_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        plexshare_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`plexshare_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        plexshare_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`plexshare_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        plexshare_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`plexshare_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        plexshare_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`plexshare_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        plexshare_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            plexshare_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "plexshare2.{{ user.domain }}"
              - "plexshare.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`plexshare_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        plexshare_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            plexshare_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'plexshare2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`plexshare_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        plexshare_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
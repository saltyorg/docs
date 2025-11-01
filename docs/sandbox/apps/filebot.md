---
hide:
  - tags
tags:
  - filebot
  - media
  - tools
---

# FileBot

## Overview

[FileBot](http://www.filebot.net/) is the ultimate tool for organizing and renaming your movies, tv shows or anime, and music well as downloading subtitles and artwork. It's smart and just works.

This is a Docker container for FileBot.

The GUI of the application is accessed through a modern web browser (no installation or configuration needed on the client side) or via any VNC client.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](http://www.filebot.net/){: .header-icons } | [:octicons-link-16: Docs](https://www.filebot.net/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/jlesage/docker-filebot){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jlesage/filebot){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-filebot

```

### 2. URL

- To access FileBot, visit <https://filebot.iYOUR_DOMAIN_NAMEi>

### 3. Setup

- The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    filebot_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `filebot_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `filebot_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`filebot_name`"

        ```yaml
        # Type: string
        filebot_name: filebot
        ```

=== "Paths"

    ??? variable string "`filebot_role_paths_folder`"

        ```yaml
        # Type: string
        filebot_role_paths_folder: "{{ filebot_name }}"
        ```

    ??? variable string "`filebot_role_paths_location`"

        ```yaml
        # Type: string
        filebot_role_paths_location: "{{ server_appdata_path }}/{{ filebot_role_paths_folder }}"
        ```

    ??? variable string "`filebot_role_paths_config_location`"

        ```yaml
        # Type: string
        filebot_role_paths_config_location: "{{ filebot_role_paths_location }}/config.yml"
        ```

=== "Web"

    ??? variable string "`filebot_role_web_subdomain`"

        ```yaml
        # Type: string
        filebot_role_web_subdomain: "{{ filebot_name }}"
        ```

    ??? variable string "`filebot_role_web_domain`"

        ```yaml
        # Type: string
        filebot_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`filebot_role_web_port`"

        ```yaml
        # Type: string
        filebot_role_web_port: "5800"
        ```

    ??? variable string "`filebot_role_web_url`"

        ```yaml
        # Type: string
        filebot_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='filebot') + '.' + lookup('role_var', '_web_domain', role='filebot')
                               if (lookup('role_var', '_web_subdomain', role='filebot') | length > 0)
                               else lookup('role_var', '_web_domain', role='filebot')) }}"
        ```

=== "DNS"

    ??? variable string "`filebot_role_dns_record`"

        ```yaml
        # Type: string
        filebot_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='filebot') }}"
        ```

    ??? variable string "`filebot_role_dns_zone`"

        ```yaml
        # Type: string
        filebot_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='filebot') }}"
        ```

    ??? variable bool "`filebot_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        filebot_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`filebot_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        filebot_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`filebot_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        filebot_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`filebot_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        filebot_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`filebot_role_traefik_certresolver`"

        ```yaml
        # Type: string
        filebot_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`filebot_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        filebot_role_traefik_enabled: true
        ```

    ??? variable bool "`filebot_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        filebot_role_traefik_api_enabled: true
        ```

    ??? variable string "`filebot_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        filebot_role_traefik_api_endpoint: "PathPrefix(`/websockify`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`filebot_role_docker_container`"

        ```yaml
        # Type: string
        filebot_role_docker_container: "{{ filebot_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`filebot_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        filebot_role_docker_image_pull: true
        ```

    ??? variable string "`filebot_role_docker_image_repo`"

        ```yaml
        # Type: string
        filebot_role_docker_image_repo: "jlesage/filebot"
        ```

    ??? variable string "`filebot_role_docker_image_tag`"

        ```yaml
        # Type: string
        filebot_role_docker_image_tag: "latest"
        ```

    ??? variable string "`filebot_role_docker_image`"

        ```yaml
        # Type: string
        filebot_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='filebot') }}:{{ lookup('role_var', '_docker_image_tag', role='filebot') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`filebot_role_docker_envs_default`"

        ```yaml
        # Type: dict
        filebot_role_docker_envs_default: 
          TZ: "{{ tz }}"
          USER_ID: "{{ uid }}"
          GROUP_ID: "{{ gid }}"
          UMASK: "022"
        ```

    ??? variable dict "`filebot_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        filebot_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`filebot_role_docker_volumes_default`"

        ```yaml
        # Type: list
        filebot_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='filebot') }}:/config"
          - "/mnt/unionfs/Media/:/storage/Media/"
          - "/mnt/local/downloads:/storage/downloads"
        ```

    ??? variable list "`filebot_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        filebot_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`filebot_role_docker_hostname`"

        ```yaml
        # Type: string
        filebot_role_docker_hostname: "{{ filebot_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`filebot_role_docker_networks_alias`"

        ```yaml
        # Type: string
        filebot_role_docker_networks_alias: "{{ filebot_name }}"
        ```

    ??? variable list "`filebot_role_docker_networks_default`"

        ```yaml
        # Type: list
        filebot_role_docker_networks_default: []
        ```

    ??? variable list "`filebot_role_docker_networks_custom`"

        ```yaml
        # Type: list
        filebot_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`filebot_role_docker_restart_policy`"

        ```yaml
        # Type: string
        filebot_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`filebot_role_docker_state`"

        ```yaml
        # Type: string
        filebot_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`filebot_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        filebot_role_autoheal_enabled: true
        ```

    ??? variable string "`filebot_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        filebot_role_depends_on: ""
        ```

    ??? variable string "`filebot_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        filebot_role_depends_on_delay: "0"
        ```

    ??? variable string "`filebot_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        filebot_role_depends_on_healthchecks:
        ```

    ??? variable bool "`filebot_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        filebot_role_diun_enabled: true
        ```

    ??? variable bool "`filebot_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        filebot_role_dns_enabled: true
        ```

    ??? variable bool "`filebot_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        filebot_role_docker_controller: true
        ```

    ??? variable bool "`filebot_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        filebot_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`filebot_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        filebot_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`filebot_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        filebot_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`filebot_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        filebot_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`filebot_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        filebot_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`filebot_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        filebot_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`filebot_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        filebot_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`filebot_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        filebot_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`filebot_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        filebot_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`filebot_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        filebot_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            filebot_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "filebot2.{{ user.domain }}"
              - "filebot.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`filebot_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        filebot_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            filebot_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'filebot2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`filebot_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        filebot_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
icon: material/docker
hide:
  - tags
tags:
  - moviematch
  - plex
  - recommendations
---

# MovieMatch

## Overview

[MovieMatch](https://github.com/LukeChannings/moviematch) is an app that helps you and your friends pick a movie to watch from a Plex server.

MovieMatch connects to your Plex server and gets a list of movies (from any libraries marked as a movie library).

As many people as you want connect to your MovieMatch server and get a list of shuffled movies. Swipe right to +1, swipe left to -1.

If two (or more) people swipe right on the same movie, it'll show up in everyone's matches. The movies that the most people swiped right on will show up first.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/LukeChannings/moviematch){: .header-icons } | [:octicons-link-16: Docs](https://github.com/LukeChannings/moviematch){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/LukeChannings/moviematch#readme){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/lukechannings/moviematch){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-moviematch

```

### 2. URL

- To access MovieMatch, visit <https://moviematch.iYOUR_DOMAIN_NAMEi>

### 3. Setup

#### Via UI

- If you prefer to set up MovieMatch using a web interface, just start MovieMatch and you will be presented with a configuration screen. <br />
  The configuration will be saved in the working directory.

#### Via YAML

- MovieMatch can be configured with a simple YAML document, which allows connecting to multiple Plex servers. <br />
  Here's a simple example:

  ```YAML
    host: 0.0.0.0
    port: 8000
    servers:
      - url: https://plex.xYOUR_DOMAIN_NAMEx
        token: abcdef12346
  ```

MovieMatch will read the config from `/opt/moviematch/config.yaml` by default.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    moviematch_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `moviematch_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `moviematch_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`moviematch_name`"

        ```yaml
        # Type: string
        moviematch_name: moviematch
        ```

=== "Paths"

    ??? variable string "`moviematch_role_paths_folder`"

        ```yaml
        # Type: string
        moviematch_role_paths_folder: "{{ moviematch_name }}"
        ```

    ??? variable string "`moviematch_role_paths_location`"

        ```yaml
        # Type: string
        moviematch_role_paths_location: "{{ server_appdata_path }}/{{ moviematch_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`moviematch_role_web_subdomain`"

        ```yaml
        # Type: string
        moviematch_role_web_subdomain: "{{ moviematch_name }}"
        ```

    ??? variable string "`moviematch_role_web_domain`"

        ```yaml
        # Type: string
        moviematch_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`moviematch_role_web_port`"

        ```yaml
        # Type: string
        moviematch_role_web_port: "8000"
        ```

    ??? variable string "`moviematch_role_web_url`"

        ```yaml
        # Type: string
        moviematch_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='moviematch') + '.' + lookup('role_var', '_web_domain', role='moviematch')
                                  if (lookup('role_var', '_web_subdomain', role='moviematch') | length > 0)
                                  else lookup('role_var', '_web_domain', role='moviematch')) }}"
        ```

=== "DNS"

    ??? variable string "`moviematch_role_dns_record`"

        ```yaml
        # Type: string
        moviematch_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='moviematch') }}"
        ```

    ??? variable string "`moviematch_role_dns_zone`"

        ```yaml
        # Type: string
        moviematch_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='moviematch') }}"
        ```

    ??? variable bool "`moviematch_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        moviematch_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`moviematch_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        moviematch_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`moviematch_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        moviematch_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`moviematch_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        moviematch_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`moviematch_role_traefik_certresolver`"

        ```yaml
        # Type: string
        moviematch_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`moviematch_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        moviematch_role_traefik_enabled: true
        ```

    ??? variable bool "`moviematch_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        moviematch_role_traefik_api_enabled: false
        ```

    ??? variable string "`moviematch_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        moviematch_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`moviematch_role_docker_container`"

        ```yaml
        # Type: string
        moviematch_role_docker_container: "{{ moviematch_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`moviematch_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        moviematch_role_docker_image_pull: true
        ```

    ??? variable string "`moviematch_role_docker_image_tag`"

        ```yaml
        # Type: string
        moviematch_role_docker_image_tag: "latest"
        ```

    ??? variable string "`moviematch_role_docker_image_repo`"

        ```yaml
        # Type: string
        moviematch_role_docker_image_repo: "lukechannings/moviematch"
        ```

    ??? variable string "`moviematch_role_docker_image`"

        ```yaml
        # Type: string
        moviematch_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='moviematch') }}:{{ lookup('role_var', '_docker_image_tag', role='moviematch') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`moviematch_role_docker_envs_default`"

        ```yaml
        # Type: dict
        moviematch_role_docker_envs_default: 
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          PLEX_URL: "{{ moviematch.plex_url }}"
          PLEX_TOKEN: "{{ plex_auth_token }}"
          LOG_LEVEL: DEBUG
          LIBRARY_FILTER: "{{ moviematch.libraries }}"
        ```

    ??? variable dict "`moviematch_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        moviematch_role_docker_envs_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`moviematch_role_docker_hostname`"

        ```yaml
        # Type: string
        moviematch_role_docker_hostname: "{{ moviematch_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`moviematch_role_docker_networks_alias`"

        ```yaml
        # Type: string
        moviematch_role_docker_networks_alias: "{{ moviematch_name }}"
        ```

    ??? variable list "`moviematch_role_docker_networks_default`"

        ```yaml
        # Type: list
        moviematch_role_docker_networks_default: []
        ```

    ??? variable list "`moviematch_role_docker_networks_custom`"

        ```yaml
        # Type: list
        moviematch_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`moviematch_role_docker_restart_policy`"

        ```yaml
        # Type: string
        moviematch_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`moviematch_role_docker_state`"

        ```yaml
        # Type: string
        moviematch_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`moviematch_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        moviematch_role_autoheal_enabled: true
        ```

    ??? variable string "`moviematch_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        moviematch_role_depends_on: ""
        ```

    ??? variable string "`moviematch_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        moviematch_role_depends_on_delay: "0"
        ```

    ??? variable string "`moviematch_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        moviematch_role_depends_on_healthchecks:
        ```

    ??? variable bool "`moviematch_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        moviematch_role_diun_enabled: true
        ```

    ??? variable bool "`moviematch_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        moviematch_role_dns_enabled: true
        ```

    ??? variable bool "`moviematch_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        moviematch_role_docker_controller: true
        ```

    ??? variable bool "`moviematch_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        moviematch_role_docker_volumes_download:
        ```

    ??? variable bool "`moviematch_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        moviematch_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`moviematch_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        moviematch_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`moviematch_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        moviematch_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`moviematch_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        moviematch_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`moviematch_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        moviematch_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`moviematch_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        moviematch_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`moviematch_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        moviematch_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`moviematch_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        moviematch_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`moviematch_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        moviematch_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`moviematch_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        moviematch_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            moviematch_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "moviematch2.{{ user.domain }}"
              - "moviematch.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`moviematch_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        moviematch_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            moviematch_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'moviematch2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`moviematch_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        moviematch_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
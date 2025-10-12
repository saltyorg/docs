---
hide:
  - tags
tags:
  - moviematch
  - plex
  - recommendations
---

# MovieMatch

## What is it?

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

- To access MovieMatch, visit `https://moviematch._yourdomain.com_`

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
      - url: https://plex.example.com
        token: abcdef12346
  ```

MovieMatch will read the config from `/opt/moviematch/config.yaml` by default.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        moviematch_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `moviematch_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `moviematch_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    moviematch_name: moviematch

    ```

??? example "Paths"

    ```yaml
    # Type: string
    moviematch_role_paths_folder: "{{ moviematch_name }}"

    # Type: string
    moviematch_role_paths_location: "{{ server_appdata_path }}/{{ moviematch_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    moviematch_role_web_subdomain: "{{ moviematch_name }}"

    # Type: string
    moviematch_role_web_domain: "{{ user.domain }}"

    # Type: string
    moviematch_role_web_port: "8000"

    # Type: string
    moviematch_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='moviematch') + '.' + lookup('role_var', '_web_domain', role='moviematch')
                              if (lookup('role_var', '_web_subdomain', role='moviematch') | length > 0)
                              else lookup('role_var', '_web_domain', role='moviematch')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    moviematch_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='moviematch') }}"

    # Type: string
    moviematch_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='moviematch') }}"

    # Type: bool (true/false)
    moviematch_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    moviematch_role_traefik_sso_middleware: ""

    # Type: string
    moviematch_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    moviematch_role_traefik_middleware_custom: ""

    # Type: string
    moviematch_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    moviematch_role_traefik_enabled: true

    # Type: bool (true/false)
    moviematch_role_traefik_api_enabled: false

    # Type: string
    moviematch_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    moviematch_role_docker_container: "{{ moviematch_name }}"

    # Image
    # Type: bool (true/false)
    moviematch_role_docker_image_pull: true

    # Type: string
    moviematch_role_docker_image_tag: "latest"

    # Type: string
    moviematch_role_docker_image_repo: "lukechannings/moviematch"

    # Type: string
    moviematch_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='moviematch') }}:{{ lookup('role_var', '_docker_image_tag', role='moviematch') }}"

    # Envs
    # Type: dict
    moviematch_role_docker_envs_default: 
      TZ: "{{ tz }}"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      PLEX_URL: "{{ moviematch.plex_url }}"
      PLEX_TOKEN: "{{ plex_auth_token }}"
      LOG_LEVEL: DEBUG
      LIBRARY_FILTER: "{{ moviematch.libraries }}"

    # Type: dict
    moviematch_role_docker_envs_custom: {}

    # Hostname
    # Type: string
    moviematch_role_docker_hostname: "{{ moviematch_name }}"

    # Networks
    # Type: string
    moviematch_role_docker_networks_alias: "{{ moviematch_name }}"

    # Type: list
    moviematch_role_docker_networks_default: []

    # Type: list
    moviematch_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    moviematch_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    moviematch_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    moviematch_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    moviematch_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    moviematch_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    moviematch_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    moviematch_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    moviematch_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    moviematch_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    moviematch_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    moviematch_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    moviematch_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    moviematch_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    moviematch_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    moviematch_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    moviematch_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    moviematch_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    moviematch_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    moviematch_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        moviematch_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "moviematch2.{{ user.domain }}"
          - "moviematch.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        moviematch_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'moviematch2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

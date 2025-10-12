---
hide:
  - tags
tags:
  - glances
  - monitoring
  - system
---

# Glances

## What is it?

[Glances](http://nicolargo.github.io/glances/) is a cross-platform monitoring tool which aims to present a large amount of monitoring information through a curses or Web based interface. The information dynamically adapts depending on the size of the user interface.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](http://nicolargo.github.io/glances/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/nicolargo/glances/wiki){: .header-icons } | [:octicons-mark-github-16: Github](http://nicolargo.github.io/glances/){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/nicolargo/glances){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-glances-web

```

### 2. URL

- To access Glances, visit `https://glances._yourdomain.com_`

### 3. Setup

- The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        glances_web_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `glances_web_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `glances_web_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    glances_web_name: glances

    ```

??? example "Docker Socket Proxy"

    ```yaml
    # Type: dict
    glances_role_docker_socket_proxy_envs: 
      CONTAINERS: "1"
      IMAGES: "1"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    glances_web_role_paths_folder: "{{ glances_web_name }}"

    # Type: string
    glances_web_role_paths_location: "{{ server_appdata_path }}/{{ glances_web_role_paths_folder }}"

    # Type: string
    glances_web_role_paths_config_location: "{{ glances_web_role_paths_location }}/config/glances.conf"

    ```

??? example "Web"

    ```yaml
    # Type: string
    glances_web_role_web_subdomain: "{{ glances_web_name }}"

    # Type: string
    glances_web_role_web_domain: "{{ user.domain }}"

    # Type: string
    glances_web_role_web_port: "61208"

    # Type: string
    glances_web_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='glances_web') + '.' + lookup('role_var', '_web_domain', role='glances_web')
                               if (lookup('role_var', '_web_subdomain', role='glances_web') | length > 0)
                               else lookup('role_var', '_web_domain', role='glances_web')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    glances_web_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='glances_web') }}"

    # Type: string
    glances_web_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='glances_web') }}"

    # Type: bool (true/false)
    glances_web_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    glances_web_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    glances_web_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    glances_web_role_traefik_middleware_custom: ""

    # Type: string
    glances_web_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    glances_web_role_traefik_enabled: true

    # Type: bool (true/false)
    glances_web_role_traefik_api_enabled: false

    # Type: string
    glances_web_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    glances_web_role_docker_container: "{{ glances_web_name }}"

    # Image
    # Type: bool (true/false)
    glances_web_role_docker_image_pull: true

    # Type: string
    glances_web_role_docker_image_repo: "nicolargo/glances"

    # Type: string
    glances_web_role_docker_image_tag: "latest-full"

    # Type: string
    glances_web_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='glances_web') }}:{{ lookup('role_var', '_docker_image_tag', role='glances_web') }}"

    # Envs
    # Type: dict
    glances_web_role_docker_envs_default: 
      UID: "{{ uid }}"
      GID: "{{ gid }}"
      TZ: "{{ tz }}"
      GLANCES_OPT: "-w --bind 172.19.0.1"
      DOCKER_HOST: "tcp://{{ glances_web_name }}-docker-socket-proxy:2375"

    # Type: dict
    glances_web_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    glances_web_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_config_location', role='glances_web') }}:/glances/conf/glances.conf"

    # Type: list
    glances_web_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    glances_web_role_docker_hostname: "{{ glances_web_name }}"

    # Networks
    # Type: string
    glances_web_role_docker_network_mode: "host"

    # Restart Policy
    # Type: string
    glances_web_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    glances_web_role_docker_state: started

    # Force Kill
    # Type: bool (true/false)
    glances_web_role_docker_force_kill: true

    # PID Mode
    # Type: string
    glances_web_role_docker_pid_mode: host

    # Dependencies
    # Type: string
    glances_web_role_depends_on: "{{ glances_web_name }}-docker-socket-proxy"

    # Type: string
    glances_web_role_depends_on_delay: "0"

    # Type: string
    glances_web_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    glances_web_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    glances_web_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    glances_web_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    glances_web_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    glances_web_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    glances_web_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    glances_web_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    glances_web_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    glances_web_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    glances_web_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    glances_web_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    glances_web_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    glances_web_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    glances_web_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    glances_web_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    glances_web_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    glances_web_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        glances_web_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "glances_web2.{{ user.domain }}"
          - "glances_web.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        glances_web_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'glances_web2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

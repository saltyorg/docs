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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

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

=== "Basics"

    ??? variable string "`glances_web_name`"

        ```yaml
        # Type: string
        glances_web_name: glances
        ```

=== "Docker Socket Proxy"

    ??? variable dict "`glances_role_docker_socket_proxy_envs`"

        ```yaml
        # Type: dict
        glances_role_docker_socket_proxy_envs: 
          CONTAINERS: "1"
          IMAGES: "1"
        ```

=== "Paths"

    ??? variable string "`glances_web_role_paths_folder`"

        ```yaml
        # Type: string
        glances_web_role_paths_folder: "{{ glances_web_name }}"
        ```

    ??? variable string "`glances_web_role_paths_location`"

        ```yaml
        # Type: string
        glances_web_role_paths_location: "{{ server_appdata_path }}/{{ glances_web_role_paths_folder }}"
        ```

    ??? variable string "`glances_web_role_paths_config_location`"

        ```yaml
        # Type: string
        glances_web_role_paths_config_location: "{{ glances_web_role_paths_location }}/config/glances.conf"
        ```

=== "Web"

    ??? variable string "`glances_web_role_web_subdomain`"

        ```yaml
        # Type: string
        glances_web_role_web_subdomain: "{{ glances_web_name }}"
        ```

    ??? variable string "`glances_web_role_web_domain`"

        ```yaml
        # Type: string
        glances_web_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`glances_web_role_web_port`"

        ```yaml
        # Type: string
        glances_web_role_web_port: "61208"
        ```

    ??? variable string "`glances_web_role_web_url`"

        ```yaml
        # Type: string
        glances_web_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='glances_web') + '.' + lookup('role_var', '_web_domain', role='glances_web')
                                   if (lookup('role_var', '_web_subdomain', role='glances_web') | length > 0)
                                   else lookup('role_var', '_web_domain', role='glances_web')) }}"
        ```

=== "DNS"

    ??? variable string "`glances_web_role_dns_record`"

        ```yaml
        # Type: string
        glances_web_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='glances_web') }}"
        ```

    ??? variable string "`glances_web_role_dns_zone`"

        ```yaml
        # Type: string
        glances_web_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='glances_web') }}"
        ```

    ??? variable bool "`glances_web_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`glances_web_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        glances_web_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`glances_web_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        glances_web_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`glances_web_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        glances_web_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`glances_web_role_traefik_certresolver`"

        ```yaml
        # Type: string
        glances_web_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`glances_web_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_traefik_enabled: true
        ```

    ??? variable bool "`glances_web_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_traefik_api_enabled: false
        ```

    ??? variable string "`glances_web_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        glances_web_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`glances_web_role_docker_container`"

        ```yaml
        # Type: string
        glances_web_role_docker_container: "{{ glances_web_name }}"
        ```

    ##### Image

    ??? variable bool "`glances_web_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_docker_image_pull: true
        ```

    ??? variable string "`glances_web_role_docker_image_repo`"

        ```yaml
        # Type: string
        glances_web_role_docker_image_repo: "nicolargo/glances"
        ```

    ??? variable string "`glances_web_role_docker_image_tag`"

        ```yaml
        # Type: string
        glances_web_role_docker_image_tag: "latest-full"
        ```

    ??? variable string "`glances_web_role_docker_image`"

        ```yaml
        # Type: string
        glances_web_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='glances_web') }}:{{ lookup('role_var', '_docker_image_tag', role='glances_web') }}"
        ```

    ##### Envs

    ??? variable dict "`glances_web_role_docker_envs_default`"

        ```yaml
        # Type: dict
        glances_web_role_docker_envs_default: 
          UID: "{{ uid }}"
          GID: "{{ gid }}"
          TZ: "{{ tz }}"
          GLANCES_OPT: "-w --bind 172.19.0.1"
          DOCKER_HOST: "tcp://{{ glances_web_name }}-docker-socket-proxy:2375"
        ```

    ??? variable dict "`glances_web_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        glances_web_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`glances_web_role_docker_volumes_default`"

        ```yaml
        # Type: list
        glances_web_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_config_location', role='glances_web') }}:/glances/conf/glances.conf"
        ```

    ??? variable list "`glances_web_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        glances_web_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`glances_web_role_docker_hostname`"

        ```yaml
        # Type: string
        glances_web_role_docker_hostname: "{{ glances_web_name }}"
        ```

    ##### Networks

    ??? variable string "`glances_web_role_docker_network_mode`"

        ```yaml
        # Type: string
        glances_web_role_docker_network_mode: "host"
        ```

    ##### Restart Policy

    ??? variable string "`glances_web_role_docker_restart_policy`"

        ```yaml
        # Type: string
        glances_web_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`glances_web_role_docker_state`"

        ```yaml
        # Type: string
        glances_web_role_docker_state: started
        ```

    ##### Force Kill

    ??? variable bool "`glances_web_role_docker_force_kill`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_docker_force_kill: true
        ```

    ##### PID Mode

    ??? variable string "`glances_web_role_docker_pid_mode`"

        ```yaml
        # Type: string
        glances_web_role_docker_pid_mode: host
        ```

    ##### Dependencies

    ??? variable string "`glances_web_role_depends_on`"

        ```yaml
        # Type: string
        glances_web_role_depends_on: "{{ glances_web_name }}-docker-socket-proxy"
        ```

    ??? variable string "`glances_web_role_depends_on_delay`"

        ```yaml
        # Type: string
        glances_web_role_depends_on_delay: "0"
        ```

    ??? variable string "`glances_web_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        glances_web_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`glances_web_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        glances_web_role_autoheal_enabled: true
        ```

    ??? variable string "`glances_web_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        glances_web_role_depends_on: ""
        ```

    ??? variable string "`glances_web_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        glances_web_role_depends_on_delay: "0"
        ```

    ??? variable string "`glances_web_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        glances_web_role_depends_on_healthchecks:
        ```

    ??? variable bool "`glances_web_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        glances_web_role_diun_enabled: true
        ```

    ??? variable bool "`glances_web_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        glances_web_role_dns_enabled: true
        ```

    ??? variable bool "`glances_web_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        glances_web_role_docker_controller: true
        ```

    ??? variable bool "`glances_web_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        glances_web_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`glances_web_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        glances_web_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`glances_web_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        glances_web_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`glances_web_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        glances_web_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`glances_web_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`glances_web_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        glances_web_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`glances_web_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        glances_web_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`glances_web_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        glances_web_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`glances_web_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        glances_web_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`glances_web_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        glances_web_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            glances_web_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "glances_web2.{{ user.domain }}"
              - "glances_web.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`glances_web_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        glances_web_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            glances_web_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'glances_web2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`glances_web_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        glances_web_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
hide:
  - tags
tags:
  - yacht
  - docker
  - management
---

# Yacht

## What is it?

[Yacht](https://yacht.sh/) is a web interface for managing docker containers with an emphasis on templating to provide one-click deployments of dockerized applications. Think of it like a decentralized app store for servers that anyone can make packages for.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://yacht.sh/){: .header-icons } | [:octicons-link-16: Docs](https://yacht.sh/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/SelfhostedPro/Yacht){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/selfhostedpro/yacht){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-yacht

```

### 2. URL

- To access Yacht, visit `https://yacht._yourdomain.com_`

### 3. Setup

- The default login is the email accounts.yml and the password is `pass`

- Check out [the getting started guide](https://yacht.sh/docs/Installation/Getting_Started) if this is the first time you've used Yacht.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    yacht_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `yacht_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `yacht_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`yacht_name`"

        ```yaml
        # Type: string
        yacht_name: yacht
        ```

=== "Docker Socket Proxy"

    ??? variable dict "`yacht_role_docker_socket_proxy_envs`"

        ```yaml
        # Type: dict
        yacht_role_docker_socket_proxy_envs: 
          CONTAINERS: "1"
          POST: "0"
          IMAGES: "1"
          VOLUMES: "1"
          NETWORKS: "1"
        ```

=== "Paths"

    ??? variable string "`yacht_role_paths_folder`"

        ```yaml
        # Type: string
        yacht_role_paths_folder: "{{ yacht_name }}"
        ```

    ??? variable string "`yacht_role_paths_location`"

        ```yaml
        # Type: string
        yacht_role_paths_location: "{{ server_appdata_path }}/{{ yacht_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`yacht_role_web_subdomain`"

        ```yaml
        # Type: string
        yacht_role_web_subdomain: "{{ yacht_name }}"
        ```

    ??? variable string "`yacht_role_web_domain`"

        ```yaml
        # Type: string
        yacht_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`yacht_role_web_port`"

        ```yaml
        # Type: string
        yacht_role_web_port: "8000"
        ```

    ??? variable string "`yacht_role_web_url`"

        ```yaml
        # Type: string
        yacht_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='yacht') + '.' + lookup('role_var', '_web_domain', role='yacht')
                             if (lookup('role_var', '_web_subdomain', role='yacht') | length > 0)
                             else lookup('role_var', '_web_domain', role='yacht')) }}"
        ```

=== "DNS"

    ??? variable string "`yacht_role_dns_record`"

        ```yaml
        # Type: string
        yacht_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='yacht') }}"
        ```

    ??? variable string "`yacht_role_dns_zone`"

        ```yaml
        # Type: string
        yacht_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='yacht') }}"
        ```

    ??? variable bool "`yacht_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        yacht_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`yacht_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        yacht_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`yacht_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        yacht_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`yacht_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        yacht_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`yacht_role_traefik_certresolver`"

        ```yaml
        # Type: string
        yacht_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`yacht_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        yacht_role_traefik_enabled: true
        ```

    ??? variable bool "`yacht_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        yacht_role_traefik_api_enabled: false
        ```

    ??? variable string "`yacht_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        yacht_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    Container
    { .sb-h5 }

    ??? variable string "`yacht_role_docker_container`"

        ```yaml
        # Type: string
        yacht_role_docker_container: "{{ yacht_name }}"
        ```

    Image
    { .sb-h5 }

    ??? variable bool "`yacht_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        yacht_role_docker_image_pull: true
        ```

    ??? variable string "`yacht_role_docker_image_tag`"

        ```yaml
        # Type: string
        yacht_role_docker_image_tag: "latest"
        ```

    ??? variable string "`yacht_role_docker_image_repo`"

        ```yaml
        # Type: string
        yacht_role_docker_image_repo: "selfhostedpro/yacht"
        ```

    ??? variable string "`yacht_role_docker_image`"

        ```yaml
        # Type: string
        yacht_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='yacht') }}:{{ lookup('role_var', '_docker_image_tag', role='yacht') }}"
        ```

    Envs
    { .sb-h5 }

    ??? variable dict "`yacht_role_docker_envs_default`"

        ```yaml
        # Type: dict
        yacht_role_docker_envs_default: 
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          ADMIN_EMAIL: "{{ user.email }}"
          SECRET_KEY: "{{ lookup('password', '/dev/null', chars=['ascii_lowercase', 'digits'], length=16) }}"
          DOCKER_HOST: "tcp://{{ yacht_name }}-docker-socket-proxy:2375"
        ```

    ??? variable dict "`yacht_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        yacht_role_docker_envs_custom: {}
        ```

    Volumes
    { .sb-h5 }

    ??? variable list "`yacht_role_docker_volumes_default`"

        ```yaml
        # Type: list
        yacht_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='yacht') }}/config:/config"
          - "{{ lookup('role_var', '_paths_location', role='yacht') }}/storage:/storage"
        ```

    ??? variable list "`yacht_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        yacht_role_docker_volumes_custom: []
        ```

    Hostname
    { .sb-h5 }

    ??? variable string "`yacht_role_docker_hostname`"

        ```yaml
        # Type: string
        yacht_role_docker_hostname: "{{ yacht_name }}"
        ```

    Networks
    { .sb-h5 }

    ??? variable string "`yacht_role_docker_networks_alias`"

        ```yaml
        # Type: string
        yacht_role_docker_networks_alias: "{{ yacht_name }}"
        ```

    ??? variable list "`yacht_role_docker_networks_default`"

        ```yaml
        # Type: list
        yacht_role_docker_networks_default: []
        ```

    ??? variable list "`yacht_role_docker_networks_custom`"

        ```yaml
        # Type: list
        yacht_role_docker_networks_custom: []
        ```

    Restart Policy
    { .sb-h5 }

    ??? variable string "`yacht_role_docker_restart_policy`"

        ```yaml
        # Type: string
        yacht_role_docker_restart_policy: unless-stopped
        ```

    State
    { .sb-h5 }

    ??? variable string "`yacht_role_docker_state`"

        ```yaml
        # Type: string
        yacht_role_docker_state: started
        ```

    Dependencies
    { .sb-h5 }

    ??? variable string "`yacht_role_depends_on`"

        ```yaml
        # Type: string
        yacht_role_depends_on: "{{ yacht_name }}-docker-socket-proxy"
        ```

    ??? variable string "`yacht_role_depends_on_delay`"

        ```yaml
        # Type: string
        yacht_role_depends_on_delay: "0"
        ```

    ??? variable string "`yacht_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        yacht_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`yacht_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        yacht_role_autoheal_enabled: true
        ```

    ??? variable string "`yacht_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        yacht_role_depends_on: ""
        ```

    ??? variable string "`yacht_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        yacht_role_depends_on_delay: "0"
        ```

    ??? variable string "`yacht_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        yacht_role_depends_on_healthchecks:
        ```

    ??? variable bool "`yacht_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        yacht_role_diun_enabled: true
        ```

    ??? variable bool "`yacht_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        yacht_role_dns_enabled: true
        ```

    ??? variable bool "`yacht_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        yacht_role_docker_controller: true
        ```

    ??? variable bool "`yacht_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        yacht_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`yacht_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        yacht_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`yacht_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        yacht_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`yacht_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        yacht_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`yacht_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        yacht_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`yacht_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        yacht_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`yacht_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        yacht_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`yacht_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        yacht_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`yacht_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        yacht_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`yacht_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        yacht_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            yacht_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "yacht2.{{ user.domain }}"
              - "yacht.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`yacht_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        yacht_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            yacht_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'yacht2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`yacht_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        yacht_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
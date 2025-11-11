---
icon: material/docker
hide:
  - tags
tags:
  - olivetin
  - automation
  - admin
---

# OliveTin

## Overview

[OliveTin](https://olivetin.app/) gives safe and simple access to predefined shell commands from a web interface.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://olivetin.app/){: .header-icons } | [:octicons-link-16: Docs](https://docs.olivetin.app/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/OliveTin/OliveTin){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jamesread/olivetin){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-olivetin

```

### 2. URL

- To access OliveTin, visit <https://olivetin.iYOUR_DOMAIN_NAMEi>

### 3. Configuration

- A barebones configuration is imported by the role to `/opt/olivetin/config.yaml` provisioning a default "Hello world!" item

- Check out [the configuration section of the documentation](https://docs.olivetin.app/config.html) to start building your actions.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    olivetin_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `olivetin_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `olivetin_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`olivetin_name`"

        ```yaml
        # Type: string
        olivetin_name: olivetin
        ```

=== "Paths"

    ??? variable string "`olivetin_role_paths_folder`"

        ```yaml
        # Type: string
        olivetin_role_paths_folder: "{{ olivetin_name }}"
        ```

    ??? variable string "`olivetin_role_paths_location`"

        ```yaml
        # Type: string
        olivetin_role_paths_location: "{{ server_appdata_path }}/{{ olivetin_role_paths_folder }}"
        ```

    ??? variable string "`olivetin_role_paths_config_location`"

        ```yaml
        # Type: string
        olivetin_role_paths_config_location: "{{ olivetin_role_paths_location }}/config.yaml"
        ```

=== "Web"

    ??? variable string "`olivetin_role_web_subdomain`"

        ```yaml
        # Type: string
        olivetin_role_web_subdomain: "{{ olivetin_name }}"
        ```

    ??? variable string "`olivetin_role_web_domain`"

        ```yaml
        # Type: string
        olivetin_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`olivetin_role_web_port`"

        ```yaml
        # Type: string
        olivetin_role_web_port: "1337"
        ```

    ??? variable string "`olivetin_role_web_url`"

        ```yaml
        # Type: string
        olivetin_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='olivetin') + '.' + lookup('role_var', '_web_domain', role='olivetin')
                                if (lookup('role_var', '_web_subdomain', role='olivetin') | length > 0)
                                else lookup('role_var', '_web_domain', role='olivetin')) }}"
        ```

=== "DNS"

    ??? variable string "`olivetin_role_dns_record`"

        ```yaml
        # Type: string
        olivetin_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='olivetin') }}"
        ```

    ??? variable string "`olivetin_role_dns_zone`"

        ```yaml
        # Type: string
        olivetin_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='olivetin') }}"
        ```

    ??? variable bool "`olivetin_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        olivetin_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`olivetin_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        olivetin_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`olivetin_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        olivetin_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`olivetin_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        olivetin_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`olivetin_role_traefik_certresolver`"

        ```yaml
        # Type: string
        olivetin_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`olivetin_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        olivetin_role_traefik_enabled: true
        ```

    ??? variable bool "`olivetin_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        olivetin_role_traefik_api_enabled: false
        ```

    ??? variable string "`olivetin_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        olivetin_role_traefik_api_endpoint: ""
        ```

    ??? variable string "`olivetin_role_traefik_middleware_api`"

        ```yaml
        # Type: string
        olivetin_role_traefik_middleware_api: "{{ traefik_global_middleware }}"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`olivetin_role_docker_container`"

        ```yaml
        # Type: string
        olivetin_role_docker_container: "{{ olivetin_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`olivetin_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        olivetin_role_docker_image_pull: true
        ```

    ??? variable string "`olivetin_role_docker_image_tag`"

        ```yaml
        # Type: string
        olivetin_role_docker_image_tag: "latest"
        ```

    ??? variable string "`olivetin_role_docker_image_repo`"

        ```yaml
        # Type: string
        olivetin_role_docker_image_repo: "jamesread/olivetin"
        ```

    ??? variable string "`olivetin_role_docker_image`"

        ```yaml
        # Type: string
        olivetin_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='olivetin') }}:{{ lookup('role_var', '_docker_image_tag', role='olivetin') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`olivetin_role_docker_envs_default`"

        ```yaml
        # Type: dict
        olivetin_role_docker_envs_default: 
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`olivetin_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        olivetin_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`olivetin_role_docker_volumes_default`"

        ```yaml
        # Type: list
        olivetin_role_docker_volumes_default: 
          - "/var/run/docker.sock:/var/run/docker.sock"
          - "{{ lookup('role_var', '_paths_location', role='olivetin') }}:/config"
        ```

    ??? variable list "`olivetin_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        olivetin_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`olivetin_role_docker_hostname`"

        ```yaml
        # Type: string
        olivetin_role_docker_hostname: "{{ olivetin_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`olivetin_role_docker_networks_alias`"

        ```yaml
        # Type: string
        olivetin_role_docker_networks_alias: "{{ olivetin_name }}"
        ```

    ??? variable list "`olivetin_role_docker_networks_default`"

        ```yaml
        # Type: list
        olivetin_role_docker_networks_default: []
        ```

    ??? variable list "`olivetin_role_docker_networks_custom`"

        ```yaml
        # Type: list
        olivetin_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`olivetin_role_docker_restart_policy`"

        ```yaml
        # Type: string
        olivetin_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`olivetin_role_docker_state`"

        ```yaml
        # Type: string
        olivetin_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`olivetin_role_docker_user`"

        ```yaml
        # Type: string
        olivetin_role_docker_user: "0:0"
        ```

=== "Global Override Options"

    ??? variable bool "`olivetin_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        olivetin_role_autoheal_enabled: true
        ```

    ??? variable string "`olivetin_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        olivetin_role_depends_on: ""
        ```

    ??? variable string "`olivetin_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        olivetin_role_depends_on_delay: "0"
        ```

    ??? variable string "`olivetin_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        olivetin_role_depends_on_healthchecks:
        ```

    ??? variable bool "`olivetin_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        olivetin_role_diun_enabled: true
        ```

    ??? variable bool "`olivetin_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        olivetin_role_dns_enabled: true
        ```

    ??? variable bool "`olivetin_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        olivetin_role_docker_controller: true
        ```

    ??? variable bool "`olivetin_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        olivetin_role_docker_volumes_download:
        ```

    ??? variable bool "`olivetin_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        olivetin_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`olivetin_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        olivetin_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`olivetin_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        olivetin_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`olivetin_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        olivetin_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`olivetin_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        olivetin_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`olivetin_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        olivetin_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`olivetin_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        olivetin_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`olivetin_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        olivetin_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`olivetin_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        olivetin_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`olivetin_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        olivetin_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            olivetin_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "olivetin2.{{ user.domain }}"
              - "olivetin.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`olivetin_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        olivetin_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            olivetin_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'olivetin2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`olivetin_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        olivetin_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
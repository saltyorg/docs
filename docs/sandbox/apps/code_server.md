---
hide:
  - tags
tags:
  - code-server
  - vscode
  - development
---

# code-server

## What is it?

[code-server](https://github.com/coder/code-server). Run [VS Code](https://github.com/Microsoft/vscode) on any machine anywhere and access it in the browser.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/coder/code-server){: .header-icons } | [:octicons-link-16: Docs](https://code.visualstudio.com/docs){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/coder/code-server){: .header-icons } | [:material-docker: Docker](https://registry.hub.docker.com/r/codercom/code-server){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-code-server

```

### 2. URL

- To access code-server, visit `https://code-server._yourdomain.com_`

## Migration from the old `coder` role

The old `coder` role was renamed to `code-server` on Dec 19th 2022.
In order to migrate to the new role, if you aren't using a custom folder for `coder`, rename the inventory variables if you have any, then run:

``` shell

sb install sandbox-code-server -e 'code_server_migrate_coder=true'

```

The `coder` role is currently deprecated and won't receive any updates, so please run the migration to the new role as soon as possible.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    code_server_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `code_server_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `code_server_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`code_server_name`"

        ```yaml
        # Type: string
        code_server_name: code-server
        ```

=== "Paths"

    ??? variable string "`code_server_role_paths_folder`"

        ```yaml
        # Type: string
        code_server_role_paths_folder: "{{ code_server_name }}"
        ```

    ??? variable string "`code_server_role_paths_location`"

        ```yaml
        # Type: string
        code_server_role_paths_location: "{{ server_appdata_path }}/{{ code_server_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`code_server_role_web_subdomain`"

        ```yaml
        # Type: string
        code_server_role_web_subdomain: "{{ code_server_name }}"
        ```

    ??? variable string "`code_server_role_web_domain`"

        ```yaml
        # Type: string
        code_server_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`code_server_role_web_port`"

        ```yaml
        # Type: string
        code_server_role_web_port: "8080"
        ```

    ??? variable string "`code_server_role_web_url`"

        ```yaml
        # Type: string
        code_server_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='code_server') + '.' + lookup('role_var', '_web_domain', role='code_server')
                                   if (lookup('role_var', '_web_subdomain', role='code_server') | length > 0)
                                   else lookup('role_var', '_web_domain', role='code_server')) }}"
        ```

=== "DNS"

    ??? variable string "`code_server_role_dns_record`"

        ```yaml
        # Type: string
        code_server_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='code_server') }}"
        ```

    ??? variable string "`code_server_role_dns_zone`"

        ```yaml
        # Type: string
        code_server_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='code_server') }}"
        ```

    ??? variable bool "`code_server_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        code_server_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`code_server_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        code_server_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`code_server_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        code_server_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`code_server_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        code_server_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`code_server_role_traefik_certresolver`"

        ```yaml
        # Type: string
        code_server_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`code_server_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        code_server_role_traefik_enabled: true
        ```

=== "Docker"

    Container
    { .sb-h5 }

    ??? variable string "`code_server_role_docker_container`"

        ```yaml
        # Type: string
        code_server_role_docker_container: "{{ code_server_name }}"
        ```

    Image
    { .sb-h5 }

    ??? variable bool "`code_server_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        code_server_role_docker_image_pull: true
        ```

    ??? variable string "`code_server_role_docker_image_repo`"

        ```yaml
        # Type: string
        code_server_role_docker_image_repo: "codercom/code-server"
        ```

    ??? variable string "`code_server_role_docker_image_tag`"

        ```yaml
        # Type: string
        code_server_role_docker_image_tag: "latest"
        ```

    ??? variable string "`code_server_role_docker_image`"

        ```yaml
        # Type: string
        code_server_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='code_server') }}:{{ lookup('role_var', '_docker_image_tag', role='code_server') }}"
        ```

    Envs
    { .sb-h5 }

    ??? variable dict "`code_server_role_docker_envs_default`"

        ```yaml
        # Type: dict
        code_server_role_docker_envs_default: 
          UMASK: "002"
          TZ: "{{ tz }}"
          PASSWORD: "{{ user.pass }}"
          DOCKER_USER: "{{ user.name }}"
        ```

    ??? variable dict "`code_server_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        code_server_role_docker_envs_custom: {}
        ```

    Volumes
    { .sb-h5 }

    ??? variable list "`code_server_role_docker_volumes_default`"

        ```yaml
        # Type: list
        code_server_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='code_server') }}/project:/home/coder/project"
          - "{{ lookup('role_var', '_paths_location', role='code_server') }}/.config:/home/coder/.config"
          - "{{ lookup('role_var', '_paths_location', role='code_server') }}/.local:/home/coder/.local"
          - "{{ server_appdata_path }}:/host_opt"
        ```

    ??? variable list "`code_server_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        code_server_role_docker_volumes_custom: []
        ```

    Hostname
    { .sb-h5 }

    ??? variable string "`code_server_role_docker_hostname`"

        ```yaml
        # Type: string
        code_server_role_docker_hostname: "{{ code_server_name }}"
        ```

    Networks
    { .sb-h5 }

    ??? variable string "`code_server_role_docker_networks_alias`"

        ```yaml
        # Type: string
        code_server_role_docker_networks_alias: "{{ code_server_name }}"
        ```

    ??? variable list "`code_server_role_docker_networks_default`"

        ```yaml
        # Type: list
        code_server_role_docker_networks_default: []
        ```

    ??? variable list "`code_server_role_docker_networks_custom`"

        ```yaml
        # Type: list
        code_server_role_docker_networks_custom: []
        ```

    Restart Policy
    { .sb-h5 }

    ??? variable string "`code_server_role_docker_restart_policy`"

        ```yaml
        # Type: string
        code_server_role_docker_restart_policy: unless-stopped
        ```

    State
    { .sb-h5 }

    ??? variable string "`code_server_role_docker_state`"

        ```yaml
        # Type: string
        code_server_role_docker_state: started
        ```

    User
    { .sb-h5 }

    ??? variable string "`code_server_role_docker_user`"

        ```yaml
        # Type: string
        code_server_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`code_server_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        code_server_role_autoheal_enabled: true
        ```

    ??? variable string "`code_server_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        code_server_role_depends_on: ""
        ```

    ??? variable string "`code_server_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        code_server_role_depends_on_delay: "0"
        ```

    ??? variable string "`code_server_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        code_server_role_depends_on_healthchecks:
        ```

    ??? variable bool "`code_server_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        code_server_role_diun_enabled: true
        ```

    ??? variable bool "`code_server_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        code_server_role_dns_enabled: true
        ```

    ??? variable bool "`code_server_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        code_server_role_docker_controller: true
        ```

    ??? variable bool "`code_server_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        code_server_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`code_server_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        code_server_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`code_server_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        code_server_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`code_server_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        code_server_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`code_server_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        code_server_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`code_server_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        code_server_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`code_server_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        code_server_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`code_server_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        code_server_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`code_server_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        code_server_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`code_server_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        code_server_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            code_server_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "code_server2.{{ user.domain }}"
              - "code_server.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`code_server_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        code_server_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            code_server_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'code_server2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`code_server_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        code_server_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
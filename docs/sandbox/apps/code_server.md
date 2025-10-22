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

- To access code-server, visit `https://code-server.xDOMAIN_NAMEx`

## Migration from the old `coder` role

The old `coder` role was renamed to `code-server` on Dec 19th 2022.
In order to migrate to the new role, if you aren't using a custom folder for `coder`, rename the inventory variables if you have any, then run:

``` shell

sb install sandbox-code-server -e 'code_server_migrate_coder=true'

```

The `coder` role is currently deprecated and won't receive any updates, so please run the migration to the new role as soon as possible.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        code_server_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `code_server_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `code_server_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    code_server_name: code-server

    ```

??? example "Paths"

    ```yaml
    # Type: string
    code_server_role_paths_folder: "{{ code_server_name }}"

    # Type: string
    code_server_role_paths_location: "{{ server_appdata_path }}/{{ code_server_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    code_server_role_web_subdomain: "{{ code_server_name }}"

    # Type: string
    code_server_role_web_domain: "{{ user.domain }}"

    # Type: string
    code_server_role_web_port: "8080"

    # Type: string
    code_server_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='code_server') + '.' + lookup('role_var', '_web_domain', role='code_server')
                               if (lookup('role_var', '_web_subdomain', role='code_server') | length > 0)
                               else lookup('role_var', '_web_domain', role='code_server')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    code_server_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='code_server') }}"

    # Type: string
    code_server_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='code_server') }}"

    # Type: bool (true/false)
    code_server_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    code_server_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    code_server_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    code_server_role_traefik_middleware_custom: ""

    # Type: string
    code_server_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    code_server_role_traefik_enabled: true

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    code_server_role_docker_container: "{{ code_server_name }}"

    # Image
    # Type: bool (true/false)
    code_server_role_docker_image_pull: true

    # Type: string
    code_server_role_docker_image_repo: "codercom/code-server"

    # Type: string
    code_server_role_docker_image_tag: "latest"

    # Type: string
    code_server_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='code_server') }}:{{ lookup('role_var', '_docker_image_tag', role='code_server') }}"

    # Envs
    # Type: dict
    code_server_role_docker_envs_default: 
      UMASK: "002"
      TZ: "{{ tz }}"
      PASSWORD: "{{ user.pass }}"
      DOCKER_USER: "{{ user.name }}"

    # Type: dict
    code_server_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    code_server_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='code_server') }}/project:/home/coder/project"
      - "{{ lookup('role_var', '_paths_location', role='code_server') }}/.config:/home/coder/.config"
      - "{{ lookup('role_var', '_paths_location', role='code_server') }}/.local:/home/coder/.local"
      - "{{ server_appdata_path }}:/host_opt"

    # Type: list
    code_server_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    code_server_role_docker_hostname: "{{ code_server_name }}"

    # Networks
    # Type: string
    code_server_role_docker_networks_alias: "{{ code_server_name }}"

    # Type: list
    code_server_role_docker_networks_default: []

    # Type: list
    code_server_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    code_server_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    code_server_role_docker_state: started

    # User
    # Type: string
    code_server_role_docker_user: "{{ uid }}:{{ gid }}"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    code_server_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    code_server_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    code_server_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    code_server_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    code_server_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    code_server_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    code_server_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    code_server_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    code_server_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    code_server_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    code_server_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    code_server_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    code_server_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    code_server_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    code_server_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    code_server_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    code_server_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        code_server_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "code_server2.{{ user.domain }}"
          - "code_server.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        code_server_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'code_server2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
hide:
  - tags
tags:
  - olivetin
  - automation
  - admin
---

# OliveTin

## What is it?

[OliveTin](https://olivetin.app/) gives safe and simple access to predefined shell commands from a web interface.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://olivetin.app/){: .header-icons } | [:octicons-link-16: Docs](https://docs.olivetin.app/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/OliveTin/OliveTin){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jamesread/olivetin){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-olivetin

```

### 2. URL

- To access OliveTin, visit `https://olivetin.xDOMAIN_NAMEx`

### 3. Configuration

- A barebones configuration is imported by the role to `/opt/olivetin/config.yaml` provisioning a default "Hello world!" item

- Check out [the configuration section of the documentation](https://docs.olivetin.app/config.html) to start building your actions.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        olivetin_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `olivetin_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `olivetin_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    olivetin_name: olivetin

    ```

??? example "Paths"

    ```yaml
    # Type: string
    olivetin_role_paths_folder: "{{ olivetin_name }}"

    # Type: string
    olivetin_role_paths_location: "{{ server_appdata_path }}/{{ olivetin_role_paths_folder }}"

    # Type: string
    olivetin_role_paths_config_location: "{{ olivetin_role_paths_location }}/config.yaml"

    ```

??? example "Web"

    ```yaml
    # Type: string
    olivetin_role_web_subdomain: "{{ olivetin_name }}"

    # Type: string
    olivetin_role_web_domain: "{{ user.domain }}"

    # Type: string
    olivetin_role_web_port: "1337"

    # Type: string
    olivetin_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='olivetin') + '.' + lookup('role_var', '_web_domain', role='olivetin')
                            if (lookup('role_var', '_web_subdomain', role='olivetin') | length > 0)
                            else lookup('role_var', '_web_domain', role='olivetin')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    olivetin_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='olivetin') }}"

    # Type: string
    olivetin_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='olivetin') }}"

    # Type: bool (true/false)
    olivetin_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    olivetin_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    olivetin_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    olivetin_role_traefik_middleware_custom: ""

    # Type: string
    olivetin_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    olivetin_role_traefik_enabled: true

    # Type: bool (true/false)
    olivetin_role_traefik_api_enabled: false

    # Type: string
    olivetin_role_traefik_api_endpoint: ""

    # Type: string
    olivetin_role_traefik_middleware_api: "{{ traefik_global_middleware }}"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    olivetin_role_docker_container: "{{ olivetin_name }}"

    # Image
    # Type: bool (true/false)
    olivetin_role_docker_image_pull: true

    # Type: string
    olivetin_role_docker_image_tag: "latest"

    # Type: string
    olivetin_role_docker_image_repo: "jamesread/olivetin"

    # Type: string
    olivetin_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='olivetin') }}:{{ lookup('role_var', '_docker_image_tag', role='olivetin') }}"

    # Envs
    # Type: dict
    olivetin_role_docker_envs_default: 
      TZ: "{{ tz }}"

    # Type: dict
    olivetin_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    olivetin_role_docker_volumes_default: 
      - "/var/run/docker.sock:/var/run/docker.sock"
      - "{{ lookup('role_var', '_paths_location', role='olivetin') }}:/config"

    # Type: list
    olivetin_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    olivetin_role_docker_hostname: "{{ olivetin_name }}"

    # Networks
    # Type: string
    olivetin_role_docker_networks_alias: "{{ olivetin_name }}"

    # Type: list
    olivetin_role_docker_networks_default: []

    # Type: list
    olivetin_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    olivetin_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    olivetin_role_docker_state: started

    # User
    # Type: string
    olivetin_role_docker_user: "0:0"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    olivetin_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    olivetin_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    olivetin_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    olivetin_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    olivetin_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    olivetin_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    olivetin_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    olivetin_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    olivetin_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    olivetin_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    olivetin_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    olivetin_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    olivetin_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    olivetin_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    olivetin_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    olivetin_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    olivetin_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        olivetin_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "olivetin2.{{ user.domain }}"
          - "olivetin.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        olivetin_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'olivetin2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
hide:
  - tags
tags:
  - linkding
  - productivity
  - bookmarks
---

# Linkding

## What is it?

[Linkding](https://github.com/sissbruecker/linkding#introduction) is a simple bookmark service that you can host yourself. It's designed be to be minimal and fast.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/sissbruecker/linkding#introduction){: .header-icons } | [:octicons-link-16: Docs](https://github.com/sissbruecker/linkding#documentation){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/sissbruecker/linkding){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/sissbruecker/linkding){: .header-icons } |

### 1. Installation

``` shell

sb install sandbox-linkding

```

### 2. URL

- To access linkding, visit `https://linkding._yourdomain.com_`

### 3. Setup

- Default login:

  ``` { .yaml}
  Username: user from accounts.yml
  Password: password from accounts.yml
  ```

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        linkding_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    linkding_name: linkding

    ```

??? example "Paths"

    ```yaml
    # Type: string
    linkding_role_paths_folder: "{{ linkding_name }}"

    # Type: string
    linkding_role_paths_location: "{{ server_appdata_path }}/{{ linkding_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    linkding_role_web_subdomain: "{{ linkding_name }}"

    # Type: string
    linkding_role_web_domain: "{{ user.domain }}"

    # Type: string
    linkding_role_web_port: "9090"

    # Type: string
    linkding_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='linkding') + '.' + lookup('role_var', '_web_domain', role='linkding')
                            if (lookup('role_var', '_web_subdomain', role='linkding') | length > 0)
                            else lookup('role_var', '_web_domain', role='linkding')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    linkding_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='linkding') }}"

    # Type: string
    linkding_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='linkding') }}"

    # Type: bool (true/false)
    linkding_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    linkding_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    linkding_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    linkding_role_traefik_middleware_custom: ""

    # Type: string
    linkding_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    linkding_role_traefik_enabled: true

    # Type: bool (true/false)
    linkding_role_traefik_api_enabled: true

    # Type: string
    linkding_role_traefik_api_endpoint: "PathPrefix(`/api`)"

    # Type: string
    linkding_role_traefik_api_middleware_http: "{{ 'dropsecurityheaders@file,' + traefik_default_middleware_http_api }}"

    # Type: string
    linkding_role_traefik_api_middleware: "{{ 'dropsecurityheaders@file,' + traefik_default_middleware_api }}"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    linkding_role_docker_container: "{{ linkding_name }}"

    # Image
    # Type: bool (true/false)
    linkding_role_docker_image_pull: true

    # Type: string
    linkding_role_docker_image_tag: "latest"

    # Type: string
    linkding_role_docker_image_repo: "sissbruecker/linkding"

    # Type: string
    linkding_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='linkding') }}:{{ lookup('role_var', '_docker_image_tag', role='linkding') }}"

    # Envs
    # Type: dict
    linkding_role_docker_envs_default: 
      TZ: "{{ tz }}"
      LD_CONTAINER_NAME: "{{ linkding_name }}"
      LD_HOST_PORT: "9090"
      LD_HOST_DATA_DIR: "./data"
      LD_SUPERUSER_NAME: "{{ user.name }}"
      LD_SUPERUSER_PASSWORD: "{{ user.pass }}"
      LD_DISABLE_BACKGROUND_TASKS: "false"
      LD_DISABLE_URL_VALIDATION: "false"
      LD_ENABLE_AUTH_PROXY: "false"
      LD_CSRF_TRUSTED_ORIGINS: "{{ lookup('role_var', '_web_url', role='linkding') }}"

    # Type: dict
    linkding_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    linkding_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='linkding') }}:/etc/linkding/data"

    # Type: list
    linkding_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    linkding_role_docker_hostname: "{{ linkding_name }}"

    # Networks
    # Type: string
    linkding_role_docker_networks_alias: "{{ linkding_name }}"

    # Type: list
    linkding_role_docker_networks_default: []

    # Type: list
    linkding_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    linkding_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    linkding_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    linkding_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    linkding_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    linkding_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    linkding_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    linkding_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    linkding_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    linkding_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    linkding_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    linkding_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    linkding_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    linkding_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    linkding_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    linkding_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    linkding_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    linkding_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    linkding_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    linkding_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        linkding_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "linkding2.{{ user.domain }}"
          - "linkding.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        linkding_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'linkding2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

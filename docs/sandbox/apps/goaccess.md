---
hide:
  - tags
tags:
  - goaccess
  - monitoring
  - analytics
---

# GoAccess

## What is it?

[GoAccess](https://goaccess.io/) is an open source real-time web log analyzer and interactive viewer that runs in a terminal in *nix systems or through your browser.

It provides fast and valuable HTTP statistics for system administrators that require a visual server report on the fly.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://goaccess.io/){: .header-icons } | [:octicons-link-16: Docs](https://goaccess.io/man){: .header-icons } | [:octicons-mark-github-16: Github](https://goaccess.io/github){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/gregyankovoy/goaccess){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-goaccess

```

### 2. URL

- To access GoAccess, visit `https://goaccess.xDOMAIN_NAMEx`

### 3. Setup

- The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        goaccess_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `goaccess_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `goaccess_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    goaccess_name: goaccess

    ```

??? example "Paths"

    ```yaml
    # Type: string
    goaccess_role_paths_folder: "{{ goaccess_name }}"

    # Type: string
    goaccess_role_paths_location: "{{ server_appdata_path }}/{{ goaccess_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    goaccess_role_web_subdomain: "{{ goaccess_name }}"

    # Type: string
    goaccess_role_web_domain: "{{ user.domain }}"

    # Type: string
    goaccess_role_web_port: "7889"

    # Type: string
    goaccess_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='goaccess') + '.' + lookup('role_var', '_web_domain', role='goaccess')
                            if (lookup('role_var', '_web_subdomain', role='goaccess') | length > 0)
                            else lookup('role_var', '_web_domain', role='goaccess')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    goaccess_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='goaccess') }}"

    # Type: string
    goaccess_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='goaccess') }}"

    # Type: bool (true/false)
    goaccess_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    goaccess_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    goaccess_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    goaccess_role_traefik_middleware_custom: ""

    # Type: string
    goaccess_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    goaccess_role_traefik_enabled: true

    # Type: bool (true/false)
    goaccess_role_traefik_api_enabled: false

    # Type: string
    goaccess_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    goaccess_role_docker_container: "{{ goaccess_name }}"

    # Image
    # Type: bool (true/false)
    goaccess_role_docker_image_pull: true

    # Type: string
    goaccess_role_docker_image_repo: "gregyankovoy/goaccess"

    # Type: string
    goaccess_role_docker_image_tag: "latest"

    # Type: string
    goaccess_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='goaccess') }}:{{ lookup('role_var', '_docker_image_tag', role='goaccess') }}"

    # Envs
    # Type: dict
    goaccess_role_docker_envs_default: 
      TZ: "{{ tz }}"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"

    # Type: dict
    goaccess_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    goaccess_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='goaccess') }}:/config"
      - "{{ lookup('role_var', '_paths_location', role='traefik') }}:/opt/log"

    # Type: list
    goaccess_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    goaccess_role_docker_hostname: "{{ goaccess_name }}"

    # Networks
    # Type: string
    goaccess_role_docker_networks_alias: "{{ goaccess_name }}"

    # Type: list
    goaccess_role_docker_networks_default: []

    # Type: list
    goaccess_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    goaccess_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    goaccess_role_docker_state: started

    # Force Kill
    # Type: bool (true/false)
    goaccess_role_docker_force_kill: true

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    goaccess_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    goaccess_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    goaccess_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    goaccess_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    goaccess_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    goaccess_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    goaccess_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    goaccess_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    goaccess_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    goaccess_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    goaccess_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    goaccess_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    goaccess_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    goaccess_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    goaccess_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    goaccess_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    goaccess_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        goaccess_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "goaccess2.{{ user.domain }}"
          - "goaccess.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        goaccess_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'goaccess2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

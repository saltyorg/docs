---
hide:
  - tags
tags:
  - sshwifty
  - networking
  - ssh
---

# Sshwifty

## What is it?

[Sshwifty](https://github.com/nirui/sshwifty) is an SSH and Telnet connector made for the Web. It can be deployed on your computer or server to provide SSH and Telnet access interface for any compatible (standard) web browser.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/nirui/sshwifty){: .header-icons } | [:octicons-link-16: Docs](https://github.com/nirui/sshwifty){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/nirui/sshwifty){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/niruix/sshwifty){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-sshwifty

```

### 2. URL

- To access Sshwifty, visit `https://sshwifty.xDOMAIN_NAMEx`

### 3. Setup

- The pre-configured password is taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        sshwifty_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `sshwifty_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `sshwifty_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    sshwifty_name: sshwifty

    ```

??? example "Paths"

    ```yaml
    # Type: string
    sshwifty_role_paths_folder: "{{ sshwifty_name }}"

    # Type: string
    sshwifty_role_paths_location: "{{ server_appdata_path }}/{{ sshwifty_role_paths_folder }}"

    # Type: string
    sshwifty_role_paths_config_location: "{{ sshwifty_role_paths_location }}/config/sshwifty.conf.json"

    ```

??? example "Web"

    ```yaml
    # Type: string
    sshwifty_role_web_subdomain: "{{ sshwifty_name }}"

    # Type: string
    sshwifty_role_web_domain: "{{ user.domain }}"

    # Type: string
    sshwifty_role_web_port: "8182"

    # Type: string
    sshwifty_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='sshwifty') + '.' + lookup('role_var', '_web_domain', role='sshwifty')
                            if (lookup('role_var', '_web_subdomain', role='sshwifty') | length > 0)
                            else lookup('role_var', '_web_domain', role='sshwifty')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    sshwifty_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='sshwifty') }}"

    # Type: string
    sshwifty_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='sshwifty') }}"

    # Type: bool (true/false)
    sshwifty_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    sshwifty_role_traefik_sso_middleware: ""

    # Type: string
    sshwifty_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    sshwifty_role_traefik_middleware_custom: ""

    # Type: string
    sshwifty_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    sshwifty_role_traefik_enabled: true

    # Type: bool (true/false)
    sshwifty_role_traefik_api_enabled: false

    # Type: string
    sshwifty_role_traefik_api_endpoint: ""

    # Type: bool (true/false)
    sshwifty_role_traefik_error_pages_enabled: false

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    sshwifty_role_docker_container: "{{ sshwifty_name }}"

    # Image
    # Type: bool (true/false)
    sshwifty_role_docker_image_pull: true

    # Type: string
    sshwifty_role_docker_image_repo: "niruix/sshwifty"

    # Type: string
    sshwifty_role_docker_image_tag: "latest"

    # Type: string
    sshwifty_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='sshwifty') }}:{{ lookup('role_var', '_docker_image_tag', role='sshwifty') }}"

    # Envs
    # Type: dict
    sshwifty_role_docker_envs_default: 
      SSHWIFTY_CONFIG: "/config/sshwifty.conf.json"

    # Type: dict
    sshwifty_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    sshwifty_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='sshwifty') }}/config:/config"

    # Type: list
    sshwifty_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    sshwifty_role_docker_hostname: "{{ sshwifty_name }}"

    # Networks
    # Type: string
    sshwifty_role_docker_networks_alias: "{{ sshwifty_name }}"

    # Type: list
    sshwifty_role_docker_networks_default: []

    # Type: list
    sshwifty_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    sshwifty_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    sshwifty_role_docker_state: started

    # User
    # Type: string
    sshwifty_role_docker_user: "{{ uid }}:{{ gid }}"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    sshwifty_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    sshwifty_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    sshwifty_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    sshwifty_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    sshwifty_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    sshwifty_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    sshwifty_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    sshwifty_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    sshwifty_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    sshwifty_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    sshwifty_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    sshwifty_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    sshwifty_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    sshwifty_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    sshwifty_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    sshwifty_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    sshwifty_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        sshwifty_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "sshwifty2.{{ user.domain }}"
          - "sshwifty.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        sshwifty_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'sshwifty2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

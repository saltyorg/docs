---
hide:
  - tags
tags:
  - healthchecks
  - monitoring
  - cron
---

# Healthchecks

## What is it?

[Healthchecks](https://healthchecks.io/) is a watchdog for your cron jobs. It's a web server that listens for pings from your cron jobs, plus a web interface.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://healthchecks.io/){: .header-icons } | [:octicons-link-16: Docs](https://healthchecks.io/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/healthchecks/healthchecks){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/healthchecks){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-healthchecks

```

### 2. URL

- To access Healthchecks, visit `https://healthchecks._yourdomain.com_`

### 3. Setup

- The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        healthchecks_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `healthchecks_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `healthchecks_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    healthchecks_name: healthchecks

    ```

??? example "Paths"

    ```yaml
    # Type: string
    healthchecks_role_paths_folder: "{{ healthchecks_name }}"

    # Type: string
    healthchecks_role_paths_location: "{{ server_appdata_path }}/{{ healthchecks_role_paths_folder }}"

    # Type: string
    healthchecks_role_paths_config_location: "{{ healthchecks_role_paths_location }}/local_settings.py"

    ```

??? example "Web"

    ```yaml
    # Type: string
    healthchecks_role_web_subdomain: "{{ healthchecks_name }}"

    # Type: string
    healthchecks_role_web_domain: "{{ user.domain }}"

    # Type: string
    healthchecks_role_web_port: "8000"

    # Type: string
    healthchecks_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='healthchecks') + '.' + lookup('role_var', '_web_domain', role='healthchecks')
                                if (lookup('role_var', '_web_subdomain', role='healthchecks') | length > 0)
                                else lookup('role_var', '_web_domain', role='healthchecks')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    healthchecks_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='healthchecks') }}"

    # Type: string
    healthchecks_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='healthchecks') }}"

    # Type: bool (true/false)
    healthchecks_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    healthchecks_role_traefik_sso_middleware: ""

    # Type: string
    healthchecks_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    healthchecks_role_traefik_middleware_custom: ""

    # Type: string
    healthchecks_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    healthchecks_role_traefik_enabled: true

    # Type: bool (true/false)
    healthchecks_role_traefik_api_enabled: false

    # Type: string
    healthchecks_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    healthchecks_role_docker_container: "{{ healthchecks_name }}"

    # Image
    # Type: bool (true/false)
    healthchecks_role_docker_image_pull: true

    # Type: string
    healthchecks_role_docker_image_repo: "lscr.io/linuxserver/healthchecks"

    # Type: string
    healthchecks_role_docker_image_tag: "latest"

    # Type: string
    healthchecks_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='healthchecks') }}:{{ lookup('role_var', '_docker_image_tag', role='healthchecks') }}"

    # Envs
    # Type: dict
    healthchecks_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      DEBUG: "False"
      APPRISE_ENABLED: "True"
      SITE_ROOT: "{{ lookup('role_var', '_web_url', role='healthchecks') }}"
      SITE_NAME: "{{ healthchecks_name }}"
      SUPERUSER_EMAIL: "{{ user.email }}"
      SUPERUSER_PASSWORD: "{{ user.pass }}"
      SECRET_KEY: "{{ lookup('password', '/dev/null', chars=['ascii_letters', 'digits'], length=16) }}"

    # Type: dict
    healthchecks_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    healthchecks_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='healthchecks') }}:/config"

    # Type: list
    healthchecks_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    healthchecks_role_docker_hostname: "{{ healthchecks_name }}"

    # Networks
    # Type: string
    healthchecks_role_docker_networks_alias: "{{ healthchecks_name }}"

    # Type: list
    healthchecks_role_docker_networks_default: []

    # Type: list
    healthchecks_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    healthchecks_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    healthchecks_role_docker_state: started

    # Force Kill
    # Type: bool (true/false)
    healthchecks_role_docker_force_kill: true

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    healthchecks_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    healthchecks_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    healthchecks_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    healthchecks_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    healthchecks_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    healthchecks_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    healthchecks_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    healthchecks_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    healthchecks_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    healthchecks_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    healthchecks_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    healthchecks_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    healthchecks_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    healthchecks_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    healthchecks_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    healthchecks_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    healthchecks_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        healthchecks_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "healthchecks2.{{ user.domain }}"
          - "healthchecks.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        healthchecks_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'healthchecks2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

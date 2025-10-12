---
hide:
  - tags
tags:
  - apprise
  - notifications
  - alerts
---

# Apprise

## What is it?

[Apprise](https://github.com/caronc/apprise) allows you to send a notification to almost all of the most popular notification services available to us today such as: Telegram, Discord, Slack, Amazon SNS, Gotify, etc.

!!! note
    Saltbox has a built-in Apprise client that can be used to send notifications. This container is not only used to provide a web UI for configuring and managing notifications, but it also exposes an API. This API allows for programmatic interaction, enabling other applications or scripts to send notifications through the Apprise service. For more information, see the [Apprise Client Docs](https://github.com/caronc/apprise/wiki).

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/caronc/apprise){: .header-icons } | [:octicons-link-16: Docs](https://github.com/caronc/apprise/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/caronc/apprise){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/caronc/apprise){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-apprise

```

### 2. URL

- To access apprise, visit `https://apprise._yourdomain.com_`

### 3. Setup

The instance runs on the Docker network accessible to other saltbox network containers at `http://apprise:8000`

The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#__tabbed_2_1) file located in `/srv/git/saltbox/accounts.yml`

A typical apprise URL would look like this:

``` shell

https://apprise._yourdomain.com_/notify?service=discord&title=Hello&body=World

```

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        apprise_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `apprise_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `apprise_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    apprise_name: apprise

    ```

??? example "Paths"

    ```yaml
    # Type: string
    apprise_role_paths_folder: "{{ apprise_name }}"

    # Type: string
    apprise_role_paths_location: "{{ server_appdata_path }}/{{ apprise_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    apprise_role_web_subdomain: "{{ apprise_name }}"

    # Type: string
    apprise_role_web_domain: "{{ user.domain }}"

    # Type: string
    apprise_role_web_port: "8000"

    # Type: string
    apprise_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='apprise') + '.' + lookup('role_var', '_web_domain', role='apprise')
                           if (lookup('role_var', '_web_subdomain', role='apprise') | length > 0)
                           else lookup('role_var', '_web_domain', role='apprise')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    apprise_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='apprise') }}"

    # Type: string
    apprise_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='apprise') }}"

    # Type: bool (true/false)
    apprise_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    apprise_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    apprise_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    apprise_role_traefik_middleware_custom: ""

    # Type: string
    apprise_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    apprise_role_traefik_enabled: true

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    apprise_role_docker_container: "{{ apprise_name }}"

    # Image
    # Type: bool (true/false)
    apprise_role_docker_image_pull: true

    # Type: string
    apprise_role_docker_image_repo: "lscr.io/linuxserver/apprise-api"

    # Type: string
    apprise_role_docker_image_tag: "latest"

    # Type: string
    apprise_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='apprise') }}:{{ lookup('role_var', '_docker_image_tag', role='apprise') }}"

    # Envs
    # Type: dict
    apprise_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    apprise_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    apprise_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='apprise') }}:/config"

    # Type: list
    apprise_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    apprise_role_docker_hostname: "{{ apprise_name }}"

    # Networks
    # Type: string
    apprise_role_docker_networks_alias: "{{ apprise_name }}"

    # Type: list
    apprise_role_docker_networks_default: []

    # Type: list
    apprise_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    apprise_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    apprise_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    apprise_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    apprise_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    apprise_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    apprise_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    apprise_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    apprise_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    apprise_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    apprise_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    apprise_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    apprise_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    apprise_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    apprise_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    apprise_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    apprise_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    apprise_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    apprise_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    apprise_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        apprise_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "apprise2.{{ user.domain }}"
          - "apprise.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        apprise_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'apprise2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

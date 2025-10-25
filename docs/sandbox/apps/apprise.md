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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    apprise_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `apprise_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `apprise_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`apprise_name`"

        ```yaml
        # Type: string
        apprise_name: apprise
        ```

=== "Paths"

    ??? variable string "`apprise_role_paths_folder`"

        ```yaml
        # Type: string
        apprise_role_paths_folder: "{{ apprise_name }}"
        ```

    ??? variable string "`apprise_role_paths_location`"

        ```yaml
        # Type: string
        apprise_role_paths_location: "{{ server_appdata_path }}/{{ apprise_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`apprise_role_web_subdomain`"

        ```yaml
        # Type: string
        apprise_role_web_subdomain: "{{ apprise_name }}"
        ```

    ??? variable string "`apprise_role_web_domain`"

        ```yaml
        # Type: string
        apprise_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`apprise_role_web_port`"

        ```yaml
        # Type: string
        apprise_role_web_port: "8000"
        ```

    ??? variable string "`apprise_role_web_url`"

        ```yaml
        # Type: string
        apprise_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='apprise') + '.' + lookup('role_var', '_web_domain', role='apprise')
                               if (lookup('role_var', '_web_subdomain', role='apprise') | length > 0)
                               else lookup('role_var', '_web_domain', role='apprise')) }}"
        ```

=== "DNS"

    ??? variable string "`apprise_role_dns_record`"

        ```yaml
        # Type: string
        apprise_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='apprise') }}"
        ```

    ??? variable string "`apprise_role_dns_zone`"

        ```yaml
        # Type: string
        apprise_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='apprise') }}"
        ```

    ??? variable bool "`apprise_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`apprise_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        apprise_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`apprise_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        apprise_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`apprise_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        apprise_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`apprise_role_traefik_certresolver`"

        ```yaml
        # Type: string
        apprise_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`apprise_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_traefik_enabled: true
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`apprise_role_docker_container`"

        ```yaml
        # Type: string
        apprise_role_docker_container: "{{ apprise_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`apprise_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_docker_image_pull: true
        ```

    ??? variable string "`apprise_role_docker_image_repo`"

        ```yaml
        # Type: string
        apprise_role_docker_image_repo: "lscr.io/linuxserver/apprise-api"
        ```

    ??? variable string "`apprise_role_docker_image_tag`"

        ```yaml
        # Type: string
        apprise_role_docker_image_tag: "latest"
        ```

    ??? variable string "`apprise_role_docker_image`"

        ```yaml
        # Type: string
        apprise_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='apprise') }}:{{ lookup('role_var', '_docker_image_tag', role='apprise') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`apprise_role_docker_envs_default`"

        ```yaml
        # Type: dict
        apprise_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`apprise_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        apprise_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`apprise_role_docker_volumes_default`"

        ```yaml
        # Type: list
        apprise_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='apprise') }}:/config"
        ```

    ??? variable list "`apprise_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        apprise_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`apprise_role_docker_hostname`"

        ```yaml
        # Type: string
        apprise_role_docker_hostname: "{{ apprise_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`apprise_role_docker_networks_alias`"

        ```yaml
        # Type: string
        apprise_role_docker_networks_alias: "{{ apprise_name }}"
        ```

    ??? variable list "`apprise_role_docker_networks_default`"

        ```yaml
        # Type: list
        apprise_role_docker_networks_default: []
        ```

    ??? variable list "`apprise_role_docker_networks_custom`"

        ```yaml
        # Type: list
        apprise_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`apprise_role_docker_restart_policy`"

        ```yaml
        # Type: string
        apprise_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`apprise_role_docker_state`"

        ```yaml
        # Type: string
        apprise_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`apprise_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        apprise_role_autoheal_enabled: true
        ```

    ??? variable string "`apprise_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        apprise_role_depends_on: ""
        ```

    ??? variable string "`apprise_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        apprise_role_depends_on_delay: "0"
        ```

    ??? variable string "`apprise_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        apprise_role_depends_on_healthchecks:
        ```

    ??? variable bool "`apprise_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        apprise_role_diun_enabled: true
        ```

    ??? variable bool "`apprise_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        apprise_role_dns_enabled: true
        ```

    ??? variable bool "`apprise_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        apprise_role_docker_controller: true
        ```

    ??? variable bool "`apprise_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        apprise_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`apprise_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        apprise_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`apprise_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        apprise_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`apprise_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        apprise_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`apprise_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`apprise_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        apprise_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`apprise_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        apprise_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`apprise_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        apprise_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`apprise_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        apprise_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`apprise_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        apprise_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            apprise_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "apprise2.{{ user.domain }}"
              - "apprise.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`apprise_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        apprise_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            apprise_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'apprise2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`apprise_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        apprise_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
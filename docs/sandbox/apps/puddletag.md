---
icon: material/docker
hide:
  - tags
tags:
  - puddletag
  - media
  - tagging
---

# Puddletag

## Overview

[Puddletag](https://docs.puddletag.net/) is an audio tag editor (primarily created) for GNU/Linux similar to the Windows program, Mp3tag. Unlike most taggers for GNU/Linux, it uses a spreadsheet-like layout so that all the tags you want to edit by hand are visible and easily editable.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself. (Basic Auth)

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://docs.puddletag.net/){: .header-icons } | [:octicons-link-16: Docs](https://docs.puddletag.net/docs.html){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Xirg/docker-puddletag){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-puddletag

```

### 2. URL

- To access Puddletag, visit <https://puddletag.iYOUR_DOMAIN_NAMEi>

### 3. Setup

- Default login:

  ``` { .yaml}
  Username: "your user from accounts.yml"
  Password: your_normal_password
  ```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    puddletag_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `puddletag_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `puddletag_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`puddletag_name`"

        ```yaml
        # Type: string
        puddletag_name: puddletag
        ```

=== "Paths"

    ??? variable string "`puddletag_role_paths_folder`"

        ```yaml
        # Type: string
        puddletag_role_paths_folder: "{{ puddletag_name }}"
        ```

    ??? variable string "`puddletag_role_paths_location`"

        ```yaml
        # Type: string
        puddletag_role_paths_location: "{{ server_appdata_path }}/{{ puddletag_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`puddletag_role_web_subdomain`"

        ```yaml
        # Type: string
        puddletag_role_web_subdomain: "{{ puddletag_name }}"
        ```

    ??? variable string "`puddletag_role_web_domain`"

        ```yaml
        # Type: string
        puddletag_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`puddletag_role_web_port`"

        ```yaml
        # Type: string
        puddletag_role_web_port: "8080"
        ```

    ??? variable string "`puddletag_role_web_url`"

        ```yaml
        # Type: string
        puddletag_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='puddletag') + '.' + lookup('role_var', '_web_domain', role='puddletag')
                                 if (lookup('role_var', '_web_subdomain', role='puddletag') | length > 0)
                                 else lookup('role_var', '_web_domain', role='puddletag')) }}"
        ```

=== "DNS"

    ??? variable string "`puddletag_role_dns_record`"

        ```yaml
        # Type: string
        puddletag_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='puddletag') }}"
        ```

    ??? variable string "`puddletag_role_dns_zone`"

        ```yaml
        # Type: string
        puddletag_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='puddletag') }}"
        ```

    ??? variable bool "`puddletag_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        puddletag_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`puddletag_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        puddletag_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`puddletag_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        puddletag_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`puddletag_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        puddletag_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`puddletag_role_traefik_certresolver`"

        ```yaml
        # Type: string
        puddletag_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`puddletag_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        puddletag_role_traefik_enabled: true
        ```

    ??? variable bool "`puddletag_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        puddletag_role_traefik_api_enabled: false
        ```

    ??? variable string "`puddletag_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        puddletag_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`puddletag_role_docker_container`"

        ```yaml
        # Type: string
        puddletag_role_docker_container: "{{ puddletag_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`puddletag_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        puddletag_role_docker_image_pull: true
        ```

    ??? variable string "`puddletag_role_docker_image_repo`"

        ```yaml
        # Type: string
        puddletag_role_docker_image_repo: "xirg/docker-puddletag"
        ```

    ??? variable string "`puddletag_role_docker_image_tag`"

        ```yaml
        # Type: string
        puddletag_role_docker_image_tag: "latest"
        ```

    ??? variable string "`puddletag_role_docker_image`"

        ```yaml
        # Type: string
        puddletag_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='puddletag') }}:{{ lookup('role_var', '_docker_image_tag', role='puddletag') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`puddletag_role_docker_envs_default`"

        ```yaml
        # Type: dict
        puddletag_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          APPNAME: "{{ puddletag_name }}"
          GUAC_USER: "{{ user.name }}"
          GUAC_PASS: "{{ user.pass | hash('md5') }}"
        ```

    ??? variable dict "`puddletag_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        puddletag_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`puddletag_role_docker_volumes_default`"

        ```yaml
        # Type: list
        puddletag_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='puddletag') }}:/config"
        ```

    ??? variable list "`puddletag_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        puddletag_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`puddletag_role_docker_hostname`"

        ```yaml
        # Type: string
        puddletag_role_docker_hostname: "{{ puddletag_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`puddletag_role_docker_networks_alias`"

        ```yaml
        # Type: string
        puddletag_role_docker_networks_alias: "{{ puddletag_name }}"
        ```

    ??? variable list "`puddletag_role_docker_networks_default`"

        ```yaml
        # Type: list
        puddletag_role_docker_networks_default: []
        ```

    ??? variable list "`puddletag_role_docker_networks_custom`"

        ```yaml
        # Type: list
        puddletag_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`puddletag_role_docker_restart_policy`"

        ```yaml
        # Type: string
        puddletag_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`puddletag_role_docker_state`"

        ```yaml
        # Type: string
        puddletag_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`puddletag_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        puddletag_role_autoheal_enabled: true
        ```

    ??? variable string "`puddletag_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        puddletag_role_depends_on: ""
        ```

    ??? variable string "`puddletag_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        puddletag_role_depends_on_delay: "0"
        ```

    ??? variable string "`puddletag_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        puddletag_role_depends_on_healthchecks:
        ```

    ??? variable bool "`puddletag_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        puddletag_role_diun_enabled: true
        ```

    ??? variable bool "`puddletag_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        puddletag_role_dns_enabled: true
        ```

    ??? variable bool "`puddletag_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        puddletag_role_docker_controller: true
        ```

    ??? variable bool "`puddletag_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        puddletag_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`puddletag_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        puddletag_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`puddletag_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        puddletag_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`puddletag_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        puddletag_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`puddletag_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        puddletag_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`puddletag_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        puddletag_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`puddletag_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        puddletag_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`puddletag_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        puddletag_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`puddletag_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        puddletag_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`puddletag_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        puddletag_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            puddletag_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "puddletag2.{{ user.domain }}"
              - "puddletag.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`puddletag_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        puddletag_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            puddletag_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'puddletag2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`puddletag_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        puddletag_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
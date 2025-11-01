---
hide:
  - tags
tags:
  - rdtclient
  - download
  - client
---

# rdtclient

## THIS DOCUMENTATION IS NOT YET COMPLETED

## Overview

[rdtclient](https://rdtclient.url) is a...

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://rdtclient.url){: .header-icons } | [:octicons-link-16: Docs](https://rdtclient.docs.url){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/rdtclient/rdtclient){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/rdtclient/rdtclient){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-rdtclient

```

### 2. URL

- To access rdtclient, visit <https://rdtclient.iYOUR_DOMAIN_NAMEi>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    rdtclient_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `rdtclient_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `rdtclient_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`rdtclient_name`"

        ```yaml
        # Type: string
        rdtclient_name: rdtclient
        ```

=== "Paths"

    ??? variable string "`rdtclient_role_paths_folder`"

        ```yaml
        # Type: string
        rdtclient_role_paths_folder: "{{ rdtclient_name }}"
        ```

    ??? variable string "`rdtclient_role_paths_location`"

        ```yaml
        # Type: string
        rdtclient_role_paths_location: "{{ server_appdata_path }}/{{ rdtclient_role_paths_folder }}"
        ```

    ??? variable string "`rdtclient_role_paths_config_location`"

        ```yaml
        # Type: string
        rdtclient_role_paths_config_location: "{{ rdtclient_role_paths_location }}/config"
        ```

    ??? variable string "`rdtclient_role_paths_db_location`"

        ```yaml
        # Type: string
        rdtclient_role_paths_db_location: "{{ rdtclient_role_paths_location }}/db"
        ```

    ??? variable string "`rdtclient_role_paths_downloads_location`"

        ```yaml
        # Type: string
        rdtclient_role_paths_downloads_location: "/mnt/unionfs/downloads/torrents/rdtclient"
        ```

=== "Web"

    ??? variable string "`rdtclient_role_web_subdomain`"

        ```yaml
        # Type: string
        rdtclient_role_web_subdomain: "{{ rdtclient_name }}"
        ```

    ??? variable string "`rdtclient_role_web_domain`"

        ```yaml
        # Type: string
        rdtclient_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`rdtclient_role_web_port`"

        ```yaml
        # Type: string
        rdtclient_role_web_port: "6500"
        ```

    ??? variable string "`rdtclient_role_web_url`"

        ```yaml
        # Type: string
        rdtclient_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='rdtclient') + '.' + lookup('role_var', '_web_domain', role='rdtclient')
                                 if (lookup('role_var', '_web_subdomain', role='rdtclient') | length > 0)
                                 else lookup('role_var', '_web_domain', role='rdtclient')) }}"
        ```

=== "DNS"

    ??? variable string "`rdtclient_role_dns_record`"

        ```yaml
        # Type: string
        rdtclient_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='rdtclient') }}"
        ```

    ??? variable string "`rdtclient_role_dns_zone`"

        ```yaml
        # Type: string
        rdtclient_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='rdtclient') }}"
        ```

    ??? variable bool "`rdtclient_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        rdtclient_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`rdtclient_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        rdtclient_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`rdtclient_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        rdtclient_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`rdtclient_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        rdtclient_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`rdtclient_role_traefik_certresolver`"

        ```yaml
        # Type: string
        rdtclient_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`rdtclient_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        rdtclient_role_traefik_enabled: true
        ```

    ??? variable bool "`rdtclient_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        rdtclient_role_traefik_api_enabled: false
        ```

    ??? variable string "`rdtclient_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        rdtclient_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`rdtclient_role_docker_container`"

        ```yaml
        # Type: string
        rdtclient_role_docker_container: "{{ rdtclient_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`rdtclient_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        rdtclient_role_docker_image_pull: true
        ```

    ??? variable string "`rdtclient_role_docker_image_tag`"

        ```yaml
        # Type: string
        rdtclient_role_docker_image_tag: "latest"
        ```

    ??? variable string "`rdtclient_role_docker_image_repo`"

        ```yaml
        # Type: string
        rdtclient_role_docker_image_repo: "rogerfar/rdtclient"
        ```

    ??? variable string "`rdtclient_role_docker_image`"

        ```yaml
        # Type: string
        rdtclient_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='rdtclient') }}:{{ lookup('role_var', '_docker_image_tag', role='rdtclient') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`rdtclient_role_docker_envs_default`"

        ```yaml
        # Type: dict
        rdtclient_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`rdtclient_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        rdtclient_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`rdtclient_role_docker_volumes_default`"

        ```yaml
        # Type: list
        rdtclient_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='rdtclient') }}:/data"
          - "{{ lookup('role_var', '_paths_config_location', role='rdtclient') }}:/data/config"
          - "{{ lookup('role_var', '_paths_db_location', role='rdtclient') }}:/data/db"
          - "{{ lookup('role_var', '_paths_downloads_location', role='rdtclient') }}:/data/downloads"
        ```

    ??? variable list "`rdtclient_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        rdtclient_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`rdtclient_role_docker_hostname`"

        ```yaml
        # Type: string
        rdtclient_role_docker_hostname: "{{ rdtclient_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`rdtclient_role_docker_networks_alias`"

        ```yaml
        # Type: string
        rdtclient_role_docker_networks_alias: "{{ rdtclient_name }}"
        ```

    ??? variable list "`rdtclient_role_docker_networks_default`"

        ```yaml
        # Type: list
        rdtclient_role_docker_networks_default: []
        ```

    ??? variable list "`rdtclient_role_docker_networks_custom`"

        ```yaml
        # Type: list
        rdtclient_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`rdtclient_role_docker_restart_policy`"

        ```yaml
        # Type: string
        rdtclient_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`rdtclient_role_docker_state`"

        ```yaml
        # Type: string
        rdtclient_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`rdtclient_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        rdtclient_role_autoheal_enabled: true
        ```

    ??? variable string "`rdtclient_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        rdtclient_role_depends_on: ""
        ```

    ??? variable string "`rdtclient_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        rdtclient_role_depends_on_delay: "0"
        ```

    ??? variable string "`rdtclient_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        rdtclient_role_depends_on_healthchecks:
        ```

    ??? variable bool "`rdtclient_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        rdtclient_role_diun_enabled: true
        ```

    ??? variable bool "`rdtclient_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        rdtclient_role_dns_enabled: true
        ```

    ??? variable bool "`rdtclient_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        rdtclient_role_docker_controller: true
        ```

    ??? variable bool "`rdtclient_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        rdtclient_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`rdtclient_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        rdtclient_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`rdtclient_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        rdtclient_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`rdtclient_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        rdtclient_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`rdtclient_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        rdtclient_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`rdtclient_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        rdtclient_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`rdtclient_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        rdtclient_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`rdtclient_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        rdtclient_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`rdtclient_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        rdtclient_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`rdtclient_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        rdtclient_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            rdtclient_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "rdtclient2.{{ user.domain }}"
              - "rdtclient.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`rdtclient_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        rdtclient_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            rdtclient_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'rdtclient2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`rdtclient_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        rdtclient_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
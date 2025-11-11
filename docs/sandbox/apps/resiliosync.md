---
icon: material/docker
hide:
  - tags
tags:
  - resiliosync
  - backup
  - sync
---

# Resilio Sync

## Overview

[Resilio Sync](https://www.resilio.com/) uses peer-to-peer technology to provide fast, private file sharing for teams and individuals. By skipping the cloud, transfers can be significantly faster because files take the shortest path between devices. Sync does not store your information on servers in the cloud, avoiding cloud privacy concerns.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://www.resilio.com/){: .header-icons } | [:octicons-link-16: Docs](https://help.resilio.com/hc/en-us/categories/200140177-Get-started-with-Sync){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/resilio/sync){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-resiliosync

```

### 2. URL

- To access Resilio Sync, visit <https://resiliosync.iYOUR_DOMAIN_NAMEi>

### 3. Setup

- [:octicons-link-16: Documentation: Resilio Sync Docs](https://help.resilio.com/hc/en-us/articles/204754939-Comprehensive-guide-to-syncing-Desktop-Desktop-){: .header-icons }

- Note: The default data port for this container is 55555. Sync will try to use this port for data transfer, if the port is not open Sync will automatically use a [relay server](https://help.resilio.com/hc/en-us/articles/204754779-What-is-a-Relay-Server-) to make your connection. For best performance, please ensure this port is opened in your firewall.
- Sync's data port can be customized by changing the [Sync settings](https://help.resilio.com/hc/en-us/articles/204762669-Sync-Preferences) as well as adding the following to `/srv/git/saltbox/inventories/host_vars/localhost.yml` and rerunning the installation tag:

 ``` yaml
resiliosync_data_port: "#####"
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    resiliosync_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `resiliosync_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `resiliosync_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`resiliosync_name`"

        ```yaml
        # Type: string
        resiliosync_name: resiliosync
        ```

=== "Settings"

    ??? variable string "`resiliosync_role_data_port`"

        ```yaml
        # Type: string
        resiliosync_role_data_port: "55555"
        ```

=== "Paths"

    ??? variable string "`resiliosync_role_paths_folder`"

        ```yaml
        # Type: string
        resiliosync_role_paths_folder: "{{ resiliosync_name }}"
        ```

    ??? variable string "`resiliosync_role_paths_location`"

        ```yaml
        # Type: string
        resiliosync_role_paths_location: "{{ server_appdata_path }}/{{ resiliosync_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`resiliosync_role_web_subdomain`"

        ```yaml
        # Type: string
        resiliosync_role_web_subdomain: "{{ resiliosync_name }}"
        ```

    ??? variable string "`resiliosync_role_web_domain`"

        ```yaml
        # Type: string
        resiliosync_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`resiliosync_role_web_port`"

        ```yaml
        # Type: string
        resiliosync_role_web_port: "8888"
        ```

    ??? variable string "`resiliosync_role_web_url`"

        ```yaml
        # Type: string
        resiliosync_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='resiliosync') + '.' + lookup('role_var', '_web_domain', role='resiliosync')
                                   if (lookup('role_var', '_web_subdomain', role='resiliosync') | length > 0)
                                   else lookup('role_var', '_web_domain', role='resiliosync')) }}"
        ```

=== "DNS"

    ??? variable string "`resiliosync_role_dns_record`"

        ```yaml
        # Type: string
        resiliosync_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='resiliosync') }}"
        ```

    ??? variable string "`resiliosync_role_dns_zone`"

        ```yaml
        # Type: string
        resiliosync_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='resiliosync') }}"
        ```

    ??? variable bool "`resiliosync_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`resiliosync_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        resiliosync_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`resiliosync_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        resiliosync_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`resiliosync_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        resiliosync_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`resiliosync_role_traefik_certresolver`"

        ```yaml
        # Type: string
        resiliosync_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`resiliosync_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_traefik_enabled: true
        ```

    ??? variable bool "`resiliosync_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_traefik_api_enabled: false
        ```

    ??? variable string "`resiliosync_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        resiliosync_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`resiliosync_role_docker_container`"

        ```yaml
        # Type: string
        resiliosync_role_docker_container: "{{ resiliosync_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`resiliosync_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_docker_image_pull: true
        ```

    ??? variable string "`resiliosync_role_docker_image_repo`"

        ```yaml
        # Type: string
        resiliosync_role_docker_image_repo: "resilio/sync"
        ```

    ??? variable string "`resiliosync_role_docker_image_tag`"

        ```yaml
        # Type: string
        resiliosync_role_docker_image_tag: "latest"
        ```

    ??? variable string "`resiliosync_role_docker_image`"

        ```yaml
        # Type: string
        resiliosync_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='resiliosync') }}:{{ lookup('role_var', '_docker_image_tag', role='resiliosync') }}"
        ```

    <h5>Ports</h5>

    ??? variable list "`resiliosync_role_docker_ports_defaults`"

        ```yaml
        # Type: list
        resiliosync_role_docker_ports_defaults: 
          - "{{ lookup('role_var', '_data_port', role='resiliosync') }}:{{ lookup('role_var', '_data_port', role='resiliosync') }}"
        ```

    ??? variable list "`resiliosync_role_docker_ports_custom`"

        ```yaml
        # Type: list
        resiliosync_role_docker_ports_custom: []
        ```

    <h5>Volumes</h5>

    ??? variable bool "`resiliosync_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_docker_volumes_global: false
        ```

    ??? variable list "`resiliosync_role_docker_volumes_default`"

        ```yaml
        # Type: list
        resiliosync_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='resiliosync') }}:/mnt/sync"
          - "/mnt:/mnt/mounted_folders/mnt"
          - "/home:/mnt/mounted_folders/home"
        ```

    ??? variable list "`resiliosync_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        resiliosync_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`resiliosync_role_docker_hostname`"

        ```yaml
        # Type: string
        resiliosync_role_docker_hostname: "{{ resiliosync_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`resiliosync_role_docker_networks_alias`"

        ```yaml
        # Type: string
        resiliosync_role_docker_networks_alias: "{{ resiliosync_name }}"
        ```

    ??? variable list "`resiliosync_role_docker_networks_default`"

        ```yaml
        # Type: list
        resiliosync_role_docker_networks_default: []
        ```

    ??? variable list "`resiliosync_role_docker_networks_custom`"

        ```yaml
        # Type: list
        resiliosync_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`resiliosync_role_docker_restart_policy`"

        ```yaml
        # Type: string
        resiliosync_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`resiliosync_role_docker_state`"

        ```yaml
        # Type: string
        resiliosync_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`resiliosync_role_docker_user`"

        ```yaml
        # Type: string
        resiliosync_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`resiliosync_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        resiliosync_role_autoheal_enabled: true
        ```

    ??? variable string "`resiliosync_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        resiliosync_role_depends_on: ""
        ```

    ??? variable string "`resiliosync_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        resiliosync_role_depends_on_delay: "0"
        ```

    ??? variable string "`resiliosync_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        resiliosync_role_depends_on_healthchecks:
        ```

    ??? variable bool "`resiliosync_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        resiliosync_role_diun_enabled: true
        ```

    ??? variable bool "`resiliosync_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        resiliosync_role_dns_enabled: true
        ```

    ??? variable bool "`resiliosync_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        resiliosync_role_docker_controller: true
        ```

    ??? variable bool "`resiliosync_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_docker_volumes_download:
        ```

    ??? variable bool "`resiliosync_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        resiliosync_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`resiliosync_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        resiliosync_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`resiliosync_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        resiliosync_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`resiliosync_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        resiliosync_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`resiliosync_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`resiliosync_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        resiliosync_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`resiliosync_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        resiliosync_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`resiliosync_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        resiliosync_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`resiliosync_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        resiliosync_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`resiliosync_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        resiliosync_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            resiliosync_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "resiliosync2.{{ user.domain }}"
              - "resiliosync.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`resiliosync_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        resiliosync_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            resiliosync_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'resiliosync2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`resiliosync_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        resiliosync_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
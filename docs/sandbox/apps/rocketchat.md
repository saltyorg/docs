---
hide:
  - tags
tags:
  - rocketchat
  - communication
  - chat
---

# rocketchat

## Overview

## THIS DOCUMENTATION IS NOT YET COMPLETED

[rocketchat](https://rocketchat.url) is a...

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://rocketchat.url){: .header-icons } | [:octicons-link-16: Docs](https://rocketchat.docs.url){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/rocketchat/rocketchat){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/rocketchat/rocketchat){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-rocketchat

```

### 2. URL

- To access rocketchat, visit <https://rocketchat.iYOUR_DOMAIN_NAMEi>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    rocketchat_mongodb_role_docker_image_tag: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `rocketchat_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `rocketchat_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`rocketchat_name`"

        ```yaml
        # Type: string
        rocketchat_name: rocketchat
        ```

=== "Settings"

    ??? variable string "`rocketchat_mongodb_role_docker_image_tag`"

        ```yaml
        # Type: string
        rocketchat_mongodb_role_docker_image_tag: "6"
        ```

    ??? variable list "`rocketchat_mongodb_role_docker_commands`"

        ```yaml
        # Type: list
        rocketchat_mongodb_role_docker_commands: 
          - "mongod --oplogSize 128 --replSet rs0"
        ```

    ??? variable list "`rocketchat_mongodb_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        rocketchat_mongodb_role_docker_volumes_custom: 
          - "{{ lookup('role_var', '_paths_location', role='rocketchat') }}/init-mongo.js:/docker-entrypoint-initdb.d/init-mongo.js:ro"
        ```

    ??? variable string "`rockatchat_mongodb_role_paths_location`"

        ```yaml
        # Type: string
        rockatchat_mongodb_role_paths_location: "{{ lookup('role_var', '_paths_location', role='rocketchat') }}/mongo"
        ```

=== "Paths"

    ??? variable string "`rocketchat_role_paths_folder`"

        ```yaml
        # Type: string
        rocketchat_role_paths_folder: "{{ rocketchat_name }}"
        ```

    ??? variable string "`rocketchat_role_paths_location`"

        ```yaml
        # Type: string
        rocketchat_role_paths_location: "{{ server_appdata_path }}/{{ rocketchat_role_paths_folder }}"
        ```

    ??? variable string "`rocketchat_role_paths_config_location`"

        ```yaml
        # Type: string
        rocketchat_role_paths_config_location: "{{ rocketchat_role_paths_location }}/env"
        ```

=== "Web"

    ??? variable string "`rocketchat_role_web_subdomain`"

        ```yaml
        # Type: string
        rocketchat_role_web_subdomain: "{{ rocketchat_name }}"
        ```

    ??? variable string "`rocketchat_role_web_domain`"

        ```yaml
        # Type: string
        rocketchat_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`rocketchat_role_web_port`"

        ```yaml
        # Type: string
        rocketchat_role_web_port: "3000"
        ```

    ??? variable string "`rocketchat_role_web_url`"

        ```yaml
        # Type: string
        rocketchat_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='rocketchat') + '.' + lookup('role_var', '_web_domain', role='rocketchat')
                                  if (lookup('role_var', '_web_subdomain', role='rocketchat') | length > 0)
                                  else lookup('role_var', '_web_domain', role='rocketchat')) }}"
        ```

=== "DNS"

    ??? variable string "`rocketchat_role_dns_record`"

        ```yaml
        # Type: string
        rocketchat_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='rocketchat') }}"
        ```

    ??? variable string "`rocketchat_role_dns_zone`"

        ```yaml
        # Type: string
        rocketchat_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='rocketchat') }}"
        ```

    ??? variable bool "`rocketchat_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`rocketchat_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        rocketchat_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`rocketchat_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        rocketchat_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`rocketchat_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        rocketchat_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`rocketchat_role_traefik_certresolver`"

        ```yaml
        # Type: string
        rocketchat_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`rocketchat_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_traefik_enabled: true
        ```

    ??? variable bool "`rocketchat_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_traefik_api_enabled: false
        ```

    ??? variable string "`rocketchat_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        rocketchat_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`rocketchat_role_docker_container`"

        ```yaml
        # Type: string
        rocketchat_role_docker_container: "{{ rocketchat_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`rocketchat_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_docker_image_pull: true
        ```

    ??? variable string "`rocketchat_role_docker_image_tag`"

        ```yaml
        # Type: string
        rocketchat_role_docker_image_tag: "latest"
        ```

    ??? variable string "`rocketchat_role_docker_image_repo`"

        ```yaml
        # Type: string
        rocketchat_role_docker_image_repo: "rocketchat/rocket.chat"
        ```

    ??? variable string "`rocketchat_role_docker_image`"

        ```yaml
        # Type: string
        rocketchat_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='rocketchat') }}:{{ lookup('role_var', '_docker_image_tag', role='rocketchat') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`rocketchat_role_docker_envs_default`"

        ```yaml
        # Type: dict
        rocketchat_role_docker_envs_default: 
          TZ: "{{ tz }}"
          ROOT_URL: "{{ lookup('role_var', '_web_url', role='rocketchat') }}"
          MONGO_URL: "mongodb://rocketchat-mongo:27017/rocketchat?replicaSet=rs0&directConnection=true"
          MONGO_OPLOG_URL: "mongodb://rocketchat-mongo:27017/local?replicaSet=rs0&directConnection=true"
          DEPLOY_METHOD: "docker"
        ```

    ??? variable dict "`rocketchat_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        rocketchat_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`rocketchat_role_docker_volumes_default`"

        ```yaml
        # Type: list
        rocketchat_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='rocketchat') }}/uploads:/app/uploads"
        ```

    ??? variable list "`rocketchat_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        rocketchat_role_docker_volumes_custom: []
        ```

    <h5>Mounts</h5>

    ??? variable list "`rocketchat_role_docker_mounts_default`"

        ```yaml
        # Type: list
        rocketchat_role_docker_mounts_default: 
          - target: /tmp
            type: tmpfs
        ```

    ??? variable list "`rocketchat_role_docker_mounts_custom`"

        ```yaml
        # Type: list
        rocketchat_role_docker_mounts_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`rocketchat_role_docker_hostname`"

        ```yaml
        # Type: string
        rocketchat_role_docker_hostname: "{{ rocketchat_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`rocketchat_role_docker_networks_alias`"

        ```yaml
        # Type: string
        rocketchat_role_docker_networks_alias: "{{ rocketchat_name }}"
        ```

    ??? variable list "`rocketchat_role_docker_networks_default`"

        ```yaml
        # Type: list
        rocketchat_role_docker_networks_default: []
        ```

    ??? variable list "`rocketchat_role_docker_networks_custom`"

        ```yaml
        # Type: list
        rocketchat_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`rocketchat_role_docker_restart_policy`"

        ```yaml
        # Type: string
        rocketchat_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`rocketchat_role_docker_state`"

        ```yaml
        # Type: string
        rocketchat_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`rocketchat_role_depends_on`"

        ```yaml
        # Type: string
        rocketchat_role_depends_on: "rocketchat_db"
        ```

    ??? variable string "`rocketchat_role_depends_on_delay`"

        ```yaml
        # Type: string
        rocketchat_role_depends_on_delay: "0"
        ```

    ??? variable string "`rocketchat_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        rocketchat_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`rocketchat_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        rocketchat_role_autoheal_enabled: true
        ```

    ??? variable string "`rocketchat_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        rocketchat_role_depends_on: ""
        ```

    ??? variable string "`rocketchat_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        rocketchat_role_depends_on_delay: "0"
        ```

    ??? variable string "`rocketchat_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        rocketchat_role_depends_on_healthchecks:
        ```

    ??? variable bool "`rocketchat_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        rocketchat_role_diun_enabled: true
        ```

    ??? variable bool "`rocketchat_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        rocketchat_role_dns_enabled: true
        ```

    ??? variable bool "`rocketchat_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        rocketchat_role_docker_controller: true
        ```

    ??? variable bool "`rocketchat_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        rocketchat_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`rocketchat_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        rocketchat_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`rocketchat_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        rocketchat_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`rocketchat_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        rocketchat_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`rocketchat_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`rocketchat_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        rocketchat_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`rocketchat_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        rocketchat_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`rocketchat_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        rocketchat_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`rocketchat_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        rocketchat_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`rocketchat_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        rocketchat_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            rocketchat_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "rocketchat2.{{ user.domain }}"
              - "rocketchat.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`rocketchat_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        rocketchat_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            rocketchat_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'rocketchat2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`rocketchat_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        rocketchat_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
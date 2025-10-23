---
hide:
  - tags
tags:
  - telegraf
  - monitoring
  - metrics
---

# Telegraf

## What is it?

[Telegraf](https://www.influxdata.com/time-series-platform/telegraf/) is a plugin-driven server agent for collecting and sending metrics and events from databases, systems, and IoT sensors.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.influxdata.com/time-series-platform/telegraf/){: .header-icons } | [:octicons-link-16: Docs](https://docs.influxdata.com/telegraf/v1.20/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/influxdata/telegraf){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/telegraf){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-telegraf

```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `telegraf_instances`.

    === "Role-level Override"

        Applies to all instances of telegraf:

        ```yaml
        telegraf_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `telegraf2`):

        ```yaml
        telegraf2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `telegraf_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `telegraf_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`telegraf_instances`"

        ```yaml
        # Type: list
        telegraf_instances: ["telegraf"]
        ```

        !!! example

            ```yaml
            # Type: list
            telegraf_instances: ["telegraf", "telegraf2"]
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`telegraf_role_paths_folder`"

            ```yaml
            # Type: string
            telegraf_role_paths_folder: "telegraf"
            ```

        ??? variable string "`telegraf_role_paths_location`"

            ```yaml
            # Type: string
            telegraf_role_paths_location: "{{ server_appdata_path }}/{{ telegraf_role_paths_folder }}"
            ```

        ??? variable bool "`telegraf_role_paths_recursive`"

            ```yaml
            # Type: bool (true/false)
            telegraf_role_paths_recursive: true
            ```

    === "Instance-level"

        ??? variable string "`telegraf2_paths_folder`"

            ```yaml
            # Type: string
            telegraf2_paths_folder: "telegraf"
            ```

        ??? variable string "`telegraf2_paths_location`"

            ```yaml
            # Type: string
            telegraf2_paths_location: "{{ server_appdata_path }}/{{ telegraf_role_paths_folder }}"
            ```

        ??? variable bool "`telegraf2_paths_recursive`"

            ```yaml
            # Type: bool (true/false)
            telegraf2_paths_recursive: true
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`telegraf_role_web_subdomain`"

            ```yaml
            # Type: string
            telegraf_role_web_subdomain: "{{ telegraf_name }}"
            ```

        ??? variable string "`telegraf_role_web_domain`"

            ```yaml
            # Type: string
            telegraf_role_web_domain: "{{ user.domain }}"
            ```

    === "Instance-level"

        ??? variable string "`telegraf2_web_subdomain`"

            ```yaml
            # Type: string
            telegraf2_web_subdomain: "{{ telegraf_name }}"
            ```

        ??? variable string "`telegraf2_web_domain`"

            ```yaml
            # Type: string
            telegraf2_web_domain: "{{ user.domain }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`telegraf_role_dns_record`"

            ```yaml
            # Type: string
            telegraf_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='telegraf') }}"
            ```

        ??? variable string "`telegraf_role_dns_zone`"

            ```yaml
            # Type: string
            telegraf_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='telegraf') }}"
            ```

        ??? variable bool "`telegraf_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            telegraf_role_dns_proxy: false
            ```

    === "Instance-level"

        ??? variable string "`telegraf2_dns_record`"

            ```yaml
            # Type: string
            telegraf2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='telegraf') }}"
            ```

        ??? variable string "`telegraf2_dns_zone`"

            ```yaml
            # Type: string
            telegraf2_dns_zone: "{{ lookup('role_var', '_web_domain', role='telegraf') }}"
            ```

        ??? variable bool "`telegraf2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            telegraf2_dns_proxy: false
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`telegraf_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            telegraf_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`telegraf_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            telegraf_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`telegraf_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            telegraf_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`telegraf_role_traefik_certresolver`"

            ```yaml
            # Type: string
            telegraf_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`telegraf_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            telegraf_role_traefik_enabled: true
            ```

        ??? variable bool "`telegraf_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            telegraf_role_traefik_api_enabled: false
            ```

        ??? variable string "`telegraf_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            telegraf_role_traefik_api_endpoint: ""
            ```

    === "Instance-level"

        ??? variable string "`telegraf2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            telegraf2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`telegraf2_traefik_middleware_default`"

            ```yaml
            # Type: string
            telegraf2_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`telegraf2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            telegraf2_traefik_middleware_custom: ""
            ```

        ??? variable string "`telegraf2_traefik_certresolver`"

            ```yaml
            # Type: string
            telegraf2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`telegraf2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            telegraf2_traefik_enabled: true
            ```

        ??? variable bool "`telegraf2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            telegraf2_traefik_api_enabled: false
            ```

        ??? variable string "`telegraf2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            telegraf2_traefik_api_endpoint: ""
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`telegraf_role_docker_container`"

            ```yaml
            # Type: string
            telegraf_role_docker_container: "{{ telegraf_name }}"
            ```

        ##### Image

        ??? variable bool "`telegraf_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            telegraf_role_docker_image_pull: true
            ```

        ??? variable string "`telegraf_role_docker_image_repo`"

            ```yaml
            # Type: string
            telegraf_role_docker_image_repo: "telegraf"
            ```

        ??? variable string "`telegraf_role_docker_image_tag`"

            ```yaml
            # Type: string
            telegraf_role_docker_image_tag: "latest"
            ```

        ??? variable string "`telegraf_role_docker_image`"

            ```yaml
            # Type: string
            telegraf_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='telegraf') }}:{{ lookup('role_var', '_docker_image_tag', role='telegraf') }}"
            ```

        ##### Envs

        ??? variable dict "`telegraf_role_docker_envs_default`"

            ```yaml
            # Type: dict
            telegraf_role_docker_envs_default: 
              TZ: "{{ tz }}"
              EULA: "TRUE"
              UID: "{{ uid }}"
              GID: "{{ gid }}"
            ```

        ??? variable dict "`telegraf_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            telegraf_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`telegraf_role_docker_volumes_default`"

            ```yaml
            # Type: list
            telegraf_role_docker_volumes_default: 
              - "{{ server_appdata_path }}/telegraf/{{ telegraf_name }}:/etc/telegraf:ro"
              - "/var/run/docker.sock:/var/run/docker.sock:ro"
              - "/var/run/utmp:/var/run/utmp"
              - "/:/host:ro"
              - "/sys:/host/sys:ro"
              - "/proc:/host/proc:ro"
              - "/etc:/host/etc:ro"
            ```

        ??? variable list "`telegraf_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            telegraf_role_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`telegraf_role_docker_hostname`"

            ```yaml
            # Type: string
            telegraf_role_docker_hostname: "{{ telegraf_name }}"
            ```

        ##### Networks

        ??? variable string "`telegraf_role_docker_networks_alias`"

            ```yaml
            # Type: string
            telegraf_role_docker_networks_alias: "{{ telegraf_name }}"
            ```

        ??? variable list "`telegraf_role_docker_networks_default`"

            ```yaml
            # Type: list
            telegraf_role_docker_networks_default: []
            ```

        ??? variable list "`telegraf_role_docker_networks_custom`"

            ```yaml
            # Type: list
            telegraf_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`telegraf_role_docker_restart_policy`"

            ```yaml
            # Type: string
            telegraf_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`telegraf_role_docker_state`"

            ```yaml
            # Type: string
            telegraf_role_docker_state: started
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`telegraf2_docker_container`"

            ```yaml
            # Type: string
            telegraf2_docker_container: "{{ telegraf_name }}"
            ```

        ##### Image

        ??? variable bool "`telegraf2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            telegraf2_docker_image_pull: true
            ```

        ??? variable string "`telegraf2_docker_image_repo`"

            ```yaml
            # Type: string
            telegraf2_docker_image_repo: "telegraf"
            ```

        ??? variable string "`telegraf2_docker_image_tag`"

            ```yaml
            # Type: string
            telegraf2_docker_image_tag: "latest"
            ```

        ??? variable string "`telegraf2_docker_image`"

            ```yaml
            # Type: string
            telegraf2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='telegraf') }}:{{ lookup('role_var', '_docker_image_tag', role='telegraf') }}"
            ```

        ##### Envs

        ??? variable dict "`telegraf2_docker_envs_default`"

            ```yaml
            # Type: dict
            telegraf2_docker_envs_default: 
              TZ: "{{ tz }}"
              EULA: "TRUE"
              UID: "{{ uid }}"
              GID: "{{ gid }}"
            ```

        ??? variable dict "`telegraf2_docker_envs_custom`"

            ```yaml
            # Type: dict
            telegraf2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`telegraf2_docker_volumes_default`"

            ```yaml
            # Type: list
            telegraf2_docker_volumes_default: 
              - "{{ server_appdata_path }}/telegraf/{{ telegraf_name }}:/etc/telegraf:ro"
              - "/var/run/docker.sock:/var/run/docker.sock:ro"
              - "/var/run/utmp:/var/run/utmp"
              - "/:/host:ro"
              - "/sys:/host/sys:ro"
              - "/proc:/host/proc:ro"
              - "/etc:/host/etc:ro"
            ```

        ??? variable list "`telegraf2_docker_volumes_custom`"

            ```yaml
            # Type: list
            telegraf2_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`telegraf2_docker_hostname`"

            ```yaml
            # Type: string
            telegraf2_docker_hostname: "{{ telegraf_name }}"
            ```

        ##### Networks

        ??? variable string "`telegraf2_docker_networks_alias`"

            ```yaml
            # Type: string
            telegraf2_docker_networks_alias: "{{ telegraf_name }}"
            ```

        ??? variable list "`telegraf2_docker_networks_default`"

            ```yaml
            # Type: list
            telegraf2_docker_networks_default: []
            ```

        ??? variable list "`telegraf2_docker_networks_custom`"

            ```yaml
            # Type: list
            telegraf2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`telegraf2_docker_restart_policy`"

            ```yaml
            # Type: string
            telegraf2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`telegraf2_docker_state`"

            ```yaml
            # Type: string
            telegraf2_docker_state: started
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`telegraf_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            telegraf_role_autoheal_enabled: true
            ```

        ??? variable string "`telegraf_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            telegraf_role_depends_on: ""
            ```

        ??? variable string "`telegraf_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            telegraf_role_depends_on_delay: "0"
            ```

        ??? variable string "`telegraf_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            telegraf_role_depends_on_healthchecks:
            ```

        ??? variable bool "`telegraf_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            telegraf_role_diun_enabled: true
            ```

        ??? variable bool "`telegraf_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            telegraf_role_dns_enabled: true
            ```

        ??? variable bool "`telegraf_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            telegraf_role_docker_controller: true
            ```

        ??? variable bool "`telegraf_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            telegraf_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`telegraf_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            telegraf_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`telegraf_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            telegraf_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`telegraf_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            telegraf_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`telegraf_role_traefik_middleware_http_api_insecure`"

            ```yaml
            # Type: bool (true/false)
            telegraf_role_traefik_middleware_http_api_insecure:
            ```

        ??? variable bool "`telegraf_role_traefik_middleware_http_insecure`"

            ```yaml
            # Type: bool (true/false)
            telegraf_role_traefik_middleware_http_insecure:
            ```

        ??? variable bool "`telegraf_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            telegraf_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`telegraf_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            telegraf_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`telegraf_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            telegraf_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`telegraf_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            telegraf_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                telegraf_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "telegraf2.{{ user.domain }}"
                  - "telegraf.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`telegraf_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            telegraf_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                telegraf_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'telegraf2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`telegraf_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            telegraf_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `telegraf2`):

        ??? variable bool "`telegraf2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            telegraf2_autoheal_enabled: true
            ```

        ??? variable string "`telegraf2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            telegraf2_depends_on: ""
            ```

        ??? variable string "`telegraf2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            telegraf2_depends_on_delay: "0"
            ```

        ??? variable string "`telegraf2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            telegraf2_depends_on_healthchecks:
            ```

        ??? variable bool "`telegraf2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            telegraf2_diun_enabled: true
            ```

        ??? variable bool "`telegraf2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            telegraf2_dns_enabled: true
            ```

        ??? variable bool "`telegraf2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            telegraf2_docker_controller: true
            ```

        ??? variable bool "`telegraf2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            telegraf2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`telegraf2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            telegraf2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`telegraf2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            telegraf2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`telegraf2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            telegraf2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`telegraf2_traefik_middleware_http_api_insecure`"

            ```yaml
            # Type: bool (true/false)
            telegraf2_traefik_middleware_http_api_insecure:
            ```

        ??? variable bool "`telegraf2_traefik_middleware_http_insecure`"

            ```yaml
            # Type: bool (true/false)
            telegraf2_traefik_middleware_http_insecure:
            ```

        ??? variable bool "`telegraf2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            telegraf2_traefik_robot_enabled: true
            ```

        ??? variable bool "`telegraf2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            telegraf2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`telegraf2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            telegraf2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`telegraf2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            telegraf2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                telegraf2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "telegraf2.{{ user.domain }}"
                  - "telegraf.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`telegraf2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            telegraf2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                telegraf2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'telegraf2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`telegraf2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            telegraf2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
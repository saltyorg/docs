---
hide:
  - tags
tags:
  - watchtower
  - monitoring
  - docker
---

# Watchtower

## What is it?

[Watchtower](https://containrrr.dev/watchtower/) is a process for automating Docker container base image updates.

With watchtower you can update the running version of your containerized app simply by pushing a new image to the Docker Hub or your own image registry. Watchtower will pull down your new image, gracefully shut down your existing container and restart it with the same options that were used when it was deployed initially.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://containrrr.dev/watchtower/){: .header-icons } | [:octicons-link-16: Docs](https://containrrr.github.io/watchtower){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/containrrr/watchtower){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/containrrr/watchtower){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-watchtower

```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `watchtower_instances`.

    === "Role-level Override"

        Applies to all instances of watchtower:

        ```yaml
        watchtower_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `watchtower2`):

        ```yaml
        watchtower2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `watchtower_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `watchtower_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`watchtower_instances`"

        ```yaml
        # Type: list
        watchtower_instances: ["watchtower"]
        ```

        !!! example

            ```yaml
            # Type: list
            watchtower_instances: ["watchtower", "watchtower2"]
            ```

=== "Settings"

    === "Role-level"

        ??? variable bool "`watchtower_role_metrics_enable`"

            ```yaml
            # Type: bool (true/false)
            watchtower_role_metrics_enable: false
            ```

        ??? variable bool "`watchtower_role_metrics_external`"

            ```yaml
            # Type: bool (true/false)
            watchtower_role_metrics_external: false
            ```

        ??? variable string "`watchtower_role_poll_interval`"

            ```yaml
            # Type: string
            watchtower_role_poll_interval: "43200"
            ```

    === "Instance-level"

        ??? variable bool "`watchtower2_metrics_enable`"

            ```yaml
            # Type: bool (true/false)
            watchtower2_metrics_enable: false
            ```

        ??? variable bool "`watchtower2_metrics_external`"

            ```yaml
            # Type: bool (true/false)
            watchtower2_metrics_external: false
            ```

        ??? variable string "`watchtower2_poll_interval`"

            ```yaml
            # Type: string
            watchtower2_poll_interval: "43200"
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`watchtower_role_paths_folder`"

            ```yaml
            # Type: string
            watchtower_role_paths_folder: "{{ watchtower_name }}"
            ```

        ??? variable string "`watchtower_role_paths_location`"

            ```yaml
            # Type: string
            watchtower_role_paths_location: "{{ server_appdata_path }}/{{ watchtower_role_paths_folder }}"
            ```

    === "Instance-level"

        ??? variable string "`watchtower2_paths_folder`"

            ```yaml
            # Type: string
            watchtower2_paths_folder: "{{ watchtower_name }}"
            ```

        ??? variable string "`watchtower2_paths_location`"

            ```yaml
            # Type: string
            watchtower2_paths_location: "{{ server_appdata_path }}/{{ watchtower_role_paths_folder }}"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`watchtower_role_web_subdomain`"

            ```yaml
            # Type: string
            watchtower_role_web_subdomain: "{{ watchtower_name }}"
            ```

        ??? variable string "`watchtower_role_web_domain`"

            ```yaml
            # Type: string
            watchtower_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`watchtower_role_web_port`"

            ```yaml
            # Type: string
            watchtower_role_web_port: "8080"
            ```

        ??? variable string "`watchtower_host`"

            ```yaml
            # Type: string
            watchtower_host: "{{ lookup('role_var', '_web_subdomain', role='watchtower') + '.' + lookup('role_var', '_web_domain', role='watchtower') }}"
            ```

    === "Instance-level"

        ??? variable string "`watchtower2_web_subdomain`"

            ```yaml
            # Type: string
            watchtower2_web_subdomain: "{{ watchtower_name }}"
            ```

        ??? variable string "`watchtower2_web_domain`"

            ```yaml
            # Type: string
            watchtower2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`watchtower2_web_port`"

            ```yaml
            # Type: string
            watchtower2_web_port: "8080"
            ```

        ??? variable string "`watchtower_host`"

            ```yaml
            # Type: string
            watchtower_host: "{{ lookup('role_var', '_web_subdomain', role='watchtower') + '.' + lookup('role_var', '_web_domain', role='watchtower') }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`watchtower_role_dns_record`"

            ```yaml
            # Type: string
            watchtower_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='watchtower') }}"
            ```

        ??? variable string "`watchtower_role_dns_zone`"

            ```yaml
            # Type: string
            watchtower_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='watchtower') }}"
            ```

        ??? variable bool "`watchtower_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            watchtower_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`watchtower2_dns_record`"

            ```yaml
            # Type: string
            watchtower2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='watchtower') }}"
            ```

        ??? variable string "`watchtower2_dns_zone`"

            ```yaml
            # Type: string
            watchtower2_dns_zone: "{{ lookup('role_var', '_web_domain', role='watchtower') }}"
            ```

        ??? variable bool "`watchtower2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            watchtower2_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`watchtower_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            watchtower_role_traefik_sso_middleware: ""
            ```

        ??? variable string "`watchtower_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            watchtower_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`watchtower_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            watchtower_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`watchtower_role_traefik_certresolver`"

            ```yaml
            # Type: string
            watchtower_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable string "`watchtower_role_traefik_enabled`"

            ```yaml
            # Type: string
            watchtower_role_traefik_enabled: "{{ true
                                              if (lookup('role_var', '_metrics_enable', role='watchtower') and lookup('role_var', '_metrics_external', role='watchtower'))
                                              else false }}"
            ```

        ??? variable bool "`watchtower_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            watchtower_role_traefik_api_enabled: false
            ```

        ??? variable string "`watchtower_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            watchtower_role_traefik_api_endpoint: ""
            ```

    === "Instance-level"

        ??? variable string "`watchtower2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            watchtower2_traefik_sso_middleware: ""
            ```

        ??? variable string "`watchtower2_traefik_middleware_default`"

            ```yaml
            # Type: string
            watchtower2_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`watchtower2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            watchtower2_traefik_middleware_custom: ""
            ```

        ??? variable string "`watchtower2_traefik_certresolver`"

            ```yaml
            # Type: string
            watchtower2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable string "`watchtower2_traefik_enabled`"

            ```yaml
            # Type: string
            watchtower2_traefik_enabled: "{{ true
                                          if (lookup('role_var', '_metrics_enable', role='watchtower') and lookup('role_var', '_metrics_external', role='watchtower'))
                                          else false }}"
            ```

        ??? variable bool "`watchtower2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            watchtower2_traefik_api_enabled: false
            ```

        ??? variable string "`watchtower2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            watchtower2_traefik_api_endpoint: ""
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`watchtower_role_docker_container`"

            ```yaml
            # Type: string
            watchtower_role_docker_container: "{{ watchtower_name }}"
            ```

        ##### Image

        ??? variable bool "`watchtower_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            watchtower_role_docker_image_pull: true
            ```

        ??? variable string "`watchtower_role_docker_image_repo`"

            ```yaml
            # Type: string
            watchtower_role_docker_image_repo: "containrrr/watchtower"
            ```

        ??? variable string "`watchtower_role_docker_image_tag`"

            ```yaml
            # Type: string
            watchtower_role_docker_image_tag: "latest"
            ```

        ??? variable string "`watchtower_role_docker_image`"

            ```yaml
            # Type: string
            watchtower_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='watchtower') }}:{{ lookup('role_var', '_docker_image_tag', role='watchtower') }}"
            ```

        ##### Envs

        ??? variable dict "`watchtower_role_docker_envs_default`"

            ```yaml
            # Type: dict
            watchtower_role_docker_envs_default: 
              TZ: "{{ tz }}"
              WATCHTOWER_CLEANUP: "true"
              WATCHTOWER_POLL_INTERVAL: "{{ lookup('role_var', '_poll_interval', role='watchtower') }}"
              WATCHTOWER_HTTP_API_METRICS: "{{ 'true'
                                            if lookup('role_var', '_metrics_enable', role='watchtower')
                                            else omit }}"
            ```

        ??? variable dict "`watchtower_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            watchtower_role_docker_envs_custom: {}
            ```

        ??? variable string "`watchtower_role_docker_env_file`"

            ```yaml
            # Type: string
            watchtower_role_docker_env_file: "{{ lookup('role_var', '_paths_location', role='watchtower') + '/watchtower.env' if watchtower_env.stat.exists else omit }}"
            ```

        ##### Volumes

        ??? variable list "`watchtower_role_docker_volumes_default`"

            ```yaml
            # Type: list
            watchtower_role_docker_volumes_default: 
              - "/var/run/docker.sock:/var/run/docker.sock"
            ```

        ??? variable list "`watchtower_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            watchtower_role_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`watchtower_role_docker_hostname`"

            ```yaml
            # Type: string
            watchtower_role_docker_hostname: "{{ watchtower_name }}"
            ```

        ##### Networks

        ??? variable string "`watchtower_role_docker_networks_alias`"

            ```yaml
            # Type: string
            watchtower_role_docker_networks_alias: "{{ watchtower_name }}"
            ```

        ??? variable list "`watchtower_role_docker_networks_default`"

            ```yaml
            # Type: list
            watchtower_role_docker_networks_default: []
            ```

        ??? variable list "`watchtower_role_docker_networks_custom`"

            ```yaml
            # Type: list
            watchtower_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`watchtower_role_docker_restart_policy`"

            ```yaml
            # Type: string
            watchtower_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`watchtower_role_docker_state`"

            ```yaml
            # Type: string
            watchtower_role_docker_state: started
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`watchtower2_docker_container`"

            ```yaml
            # Type: string
            watchtower2_docker_container: "{{ watchtower_name }}"
            ```

        ##### Image

        ??? variable bool "`watchtower2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            watchtower2_docker_image_pull: true
            ```

        ??? variable string "`watchtower2_docker_image_repo`"

            ```yaml
            # Type: string
            watchtower2_docker_image_repo: "containrrr/watchtower"
            ```

        ??? variable string "`watchtower2_docker_image_tag`"

            ```yaml
            # Type: string
            watchtower2_docker_image_tag: "latest"
            ```

        ??? variable string "`watchtower2_docker_image`"

            ```yaml
            # Type: string
            watchtower2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='watchtower') }}:{{ lookup('role_var', '_docker_image_tag', role='watchtower') }}"
            ```

        ##### Envs

        ??? variable dict "`watchtower2_docker_envs_default`"

            ```yaml
            # Type: dict
            watchtower2_docker_envs_default: 
              TZ: "{{ tz }}"
              WATCHTOWER_CLEANUP: "true"
              WATCHTOWER_POLL_INTERVAL: "{{ lookup('role_var', '_poll_interval', role='watchtower') }}"
              WATCHTOWER_HTTP_API_METRICS: "{{ 'true'
                                            if lookup('role_var', '_metrics_enable', role='watchtower')
                                            else omit }}"
            ```

        ??? variable dict "`watchtower2_docker_envs_custom`"

            ```yaml
            # Type: dict
            watchtower2_docker_envs_custom: {}
            ```

        ??? variable string "`watchtower2_docker_env_file`"

            ```yaml
            # Type: string
            watchtower2_docker_env_file: "{{ lookup('role_var', '_paths_location', role='watchtower') + '/watchtower.env' if watchtower_env.stat.exists else omit }}"
            ```

        ##### Volumes

        ??? variable list "`watchtower2_docker_volumes_default`"

            ```yaml
            # Type: list
            watchtower2_docker_volumes_default: 
              - "/var/run/docker.sock:/var/run/docker.sock"
            ```

        ??? variable list "`watchtower2_docker_volumes_custom`"

            ```yaml
            # Type: list
            watchtower2_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`watchtower2_docker_hostname`"

            ```yaml
            # Type: string
            watchtower2_docker_hostname: "{{ watchtower_name }}"
            ```

        ##### Networks

        ??? variable string "`watchtower2_docker_networks_alias`"

            ```yaml
            # Type: string
            watchtower2_docker_networks_alias: "{{ watchtower_name }}"
            ```

        ??? variable list "`watchtower2_docker_networks_default`"

            ```yaml
            # Type: list
            watchtower2_docker_networks_default: []
            ```

        ??? variable list "`watchtower2_docker_networks_custom`"

            ```yaml
            # Type: list
            watchtower2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`watchtower2_docker_restart_policy`"

            ```yaml
            # Type: string
            watchtower2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`watchtower2_docker_state`"

            ```yaml
            # Type: string
            watchtower2_docker_state: started
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`watchtower_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            watchtower_role_autoheal_enabled: true
            ```

        ??? variable string "`watchtower_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            watchtower_role_depends_on: ""
            ```

        ??? variable string "`watchtower_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            watchtower_role_depends_on_delay: "0"
            ```

        ??? variable string "`watchtower_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            watchtower_role_depends_on_healthchecks:
            ```

        ??? variable bool "`watchtower_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            watchtower_role_diun_enabled: true
            ```

        ??? variable bool "`watchtower_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            watchtower_role_dns_enabled: true
            ```

        ??? variable bool "`watchtower_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            watchtower_role_docker_controller: true
            ```

        ??? variable bool "`watchtower_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            watchtower_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`watchtower_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            watchtower_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`watchtower_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            watchtower_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`watchtower_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            watchtower_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`watchtower_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            watchtower_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`watchtower_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            watchtower_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`watchtower_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            watchtower_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`watchtower_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            watchtower_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                watchtower_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "watchtower2.{{ user.domain }}"
                  - "watchtower.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`watchtower_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            watchtower_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                watchtower_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'watchtower2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`watchtower_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            watchtower_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `watchtower2`):

        ??? variable bool "`watchtower2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            watchtower2_autoheal_enabled: true
            ```

        ??? variable string "`watchtower2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            watchtower2_depends_on: ""
            ```

        ??? variable string "`watchtower2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            watchtower2_depends_on_delay: "0"
            ```

        ??? variable string "`watchtower2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            watchtower2_depends_on_healthchecks:
            ```

        ??? variable bool "`watchtower2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            watchtower2_diun_enabled: true
            ```

        ??? variable bool "`watchtower2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            watchtower2_dns_enabled: true
            ```

        ??? variable bool "`watchtower2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            watchtower2_docker_controller: true
            ```

        ??? variable bool "`watchtower2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            watchtower2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`watchtower2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            watchtower2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`watchtower2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            watchtower2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`watchtower2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            watchtower2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`watchtower2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            watchtower2_traefik_robot_enabled: true
            ```

        ??? variable bool "`watchtower2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            watchtower2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`watchtower2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            watchtower2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`watchtower2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            watchtower2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                watchtower2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "watchtower2.{{ user.domain }}"
                  - "watchtower.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`watchtower2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            watchtower2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                watchtower2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'watchtower2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`watchtower2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            watchtower2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
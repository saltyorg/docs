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

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
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

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        watchtower_instances: ["watchtower"]

        ```

    === "Example"

        ```yaml
        # Type: list
        watchtower_instances: ["watchtower", "watchtower2"]

        ```

??? example "Settings"

    === "Role-level"

        ```yaml
        # Type: bool (true/false)
        watchtower_role_metrics_enable: false

        # Type: bool (true/false)
        watchtower_role_metrics_external: false

        # Type: string
        watchtower_role_poll_interval: "43200"

        ```

    === "Instance-level"

        ```yaml
        # Type: bool (true/false)
        watchtower2_metrics_enable: false

        # Type: bool (true/false)
        watchtower2_metrics_external: false

        # Type: string
        watchtower2_poll_interval: "43200"

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        watchtower_role_paths_folder: "{{ watchtower_name }}"

        # Type: string
        watchtower_role_paths_location: "{{ server_appdata_path }}/{{ watchtower_role_paths_folder }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        watchtower2_paths_folder: "{{ watchtower_name }}"

        # Type: string
        watchtower2_paths_location: "{{ server_appdata_path }}/{{ watchtower_role_paths_folder }}"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        watchtower_role_web_subdomain: "{{ watchtower_name }}"

        # Type: string
        watchtower_role_web_domain: "{{ user.domain }}"

        # Type: string
        watchtower_role_web_port: "8080"

        # Type: string
        watchtower_host: "{{ lookup('role_var', '_web_subdomain', role='watchtower') + '.' + lookup('role_var', '_web_domain', role='watchtower') }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        watchtower2_web_subdomain: "{{ watchtower_name }}"

        # Type: string
        watchtower2_web_domain: "{{ user.domain }}"

        # Type: string
        watchtower2_web_port: "8080"

        # Type: string
        watchtower_host: "{{ lookup('role_var', '_web_subdomain', role='watchtower') + '.' + lookup('role_var', '_web_domain', role='watchtower') }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        watchtower_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='watchtower') }}"

        # Type: string
        watchtower_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='watchtower') }}"

        # Type: bool (true/false)
        watchtower_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        watchtower2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='watchtower') }}"

        # Type: string
        watchtower2_dns_zone: "{{ lookup('role_var', '_web_domain', role='watchtower') }}"

        # Type: bool (true/false)
        watchtower2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        watchtower_role_traefik_sso_middleware: ""

        # Type: string
        watchtower_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        watchtower_role_traefik_middleware_custom: ""

        # Type: string
        watchtower_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: string
        watchtower_role_traefik_enabled: "{{ true
                                          if (lookup('role_var', '_metrics_enable', role='watchtower') and lookup('role_var', '_metrics_external', role='watchtower'))
                                          else false }}"

        # Type: bool (true/false)
        watchtower_role_traefik_api_enabled: false

        # Type: string
        watchtower_role_traefik_api_endpoint: ""

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        watchtower2_traefik_sso_middleware: ""

        # Type: string
        watchtower2_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        watchtower2_traefik_middleware_custom: ""

        # Type: string
        watchtower2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: string
        watchtower2_traefik_enabled: "{{ true
                                      if (lookup('role_var', '_metrics_enable', role='watchtower') and lookup('role_var', '_metrics_external', role='watchtower'))
                                      else false }}"

        # Type: bool (true/false)
        watchtower2_traefik_api_enabled: false

        # Type: string
        watchtower2_traefik_api_endpoint: ""

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        watchtower_role_docker_container: "{{ watchtower_name }}"

        # Image
        # Type: bool (true/false)
        watchtower_role_docker_image_pull: true

        # Type: string
        watchtower_role_docker_image_repo: "containrrr/watchtower"

        # Type: string
        watchtower_role_docker_image_tag: "latest"

        # Type: string
        watchtower_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='watchtower') }}:{{ lookup('role_var', '_docker_image_tag', role='watchtower') }}"

        # Envs
        # Type: dict
        watchtower_role_docker_envs_default: 
          TZ: "{{ tz }}"
          WATCHTOWER_CLEANUP: "true"
          WATCHTOWER_POLL_INTERVAL: "{{ lookup('role_var', '_poll_interval', role='watchtower') }}"
          WATCHTOWER_HTTP_API_METRICS: "{{ 'true'
                                        if lookup('role_var', '_metrics_enable', role='watchtower')
                                        else omit }}"

        # Type: dict
        watchtower_role_docker_envs_custom: {}

        # Type: string
        watchtower_role_docker_env_file: "{{ lookup('role_var', '_paths_location', role='watchtower') + '/watchtower.env' if watchtower_env.stat.exists else omit }}"

        # Volumes
        # Type: list
        watchtower_role_docker_volumes_default: 
          - "/var/run/docker.sock:/var/run/docker.sock"

        # Type: list
        watchtower_role_docker_volumes_custom: []

        # Hostname
        # Type: string
        watchtower_role_docker_hostname: "{{ watchtower_name }}"

        # Networks
        # Type: string
        watchtower_role_docker_networks_alias: "{{ watchtower_name }}"

        # Type: list
        watchtower_role_docker_networks_default: []

        # Type: list
        watchtower_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        watchtower_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        watchtower_role_docker_state: started

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        watchtower2_docker_container: "{{ watchtower_name }}"

        # Image
        # Type: bool (true/false)
        watchtower2_docker_image_pull: true

        # Type: string
        watchtower2_docker_image_repo: "containrrr/watchtower"

        # Type: string
        watchtower2_docker_image_tag: "latest"

        # Type: string
        watchtower2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='watchtower') }}:{{ lookup('role_var', '_docker_image_tag', role='watchtower') }}"

        # Envs
        # Type: dict
        watchtower2_docker_envs_default: 
          TZ: "{{ tz }}"
          WATCHTOWER_CLEANUP: "true"
          WATCHTOWER_POLL_INTERVAL: "{{ lookup('role_var', '_poll_interval', role='watchtower') }}"
          WATCHTOWER_HTTP_API_METRICS: "{{ 'true'
                                        if lookup('role_var', '_metrics_enable', role='watchtower')
                                        else omit }}"

        # Type: dict
        watchtower2_docker_envs_custom: {}

        # Type: string
        watchtower2_docker_env_file: "{{ lookup('role_var', '_paths_location', role='watchtower') + '/watchtower.env' if watchtower_env.stat.exists else omit }}"

        # Volumes
        # Type: list
        watchtower2_docker_volumes_default: 
          - "/var/run/docker.sock:/var/run/docker.sock"

        # Type: list
        watchtower2_docker_volumes_custom: []

        # Hostname
        # Type: string
        watchtower2_docker_hostname: "{{ watchtower_name }}"

        # Networks
        # Type: string
        watchtower2_docker_networks_alias: "{{ watchtower_name }}"

        # Type: list
        watchtower2_docker_networks_default: []

        # Type: list
        watchtower2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        watchtower2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        watchtower2_docker_state: started


        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        watchtower_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        watchtower_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        watchtower_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        watchtower_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        watchtower_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        watchtower_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        watchtower_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        watchtower_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        watchtower_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        watchtower_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        watchtower_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        watchtower_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        watchtower_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        watchtower_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        watchtower_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        watchtower_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        watchtower_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            watchtower_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "watchtower2.{{ user.domain }}"
              - "watchtower.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            watchtower_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'watchtower2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `watchtower2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        watchtower2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        watchtower2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        watchtower2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        watchtower2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        watchtower2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        watchtower2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        watchtower2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        watchtower2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        watchtower2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        watchtower2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        watchtower2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        watchtower2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        watchtower2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        watchtower2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        watchtower2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        watchtower2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        watchtower2_web_scheme:

        ```

        1.  Example:

            ```yaml
            watchtower2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "watchtower2.{{ user.domain }}"
              - "watchtower.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            watchtower2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'watchtower2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

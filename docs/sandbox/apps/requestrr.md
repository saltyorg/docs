---
hide:
  - tags
tags:
  - requestrr
  - discord
  - automation
---

# Requestrr

## What is it?

[Requestrr](https://github.com/thomst08/requestrr) is a chatbot used to simplify using services like Sonarr/Radarr/Ombi via the use of chat. Current platform is Discord only, but the bot was built around the ideology of quick adaptation for new features as well as new platforms.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/thomst08/requestrr){: .header-icons } | [:octicons-link-16: Docs](https://github.com/thomst08/requestrr/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/thomst08/requestrr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/thomst08/requestrr){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-requestrr

```

### 2. URL

- To access Requestrr, visit `https://requestrr.xDOMAIN_NAMEx`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `requestrr_instances`.

    === "Role-level Override"

        Applies to all instances of requestrr:

        ```yaml
        requestrr_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `requestrr2`):

        ```yaml
        requestrr2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `requestrr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `requestrr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        requestrr_instances: ["requestrr"]

        ```

    === "Example"

        ```yaml
        # Type: list
        requestrr_instances: ["requestrr", "requestrr2"]

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        requestrr_role_paths_folder: "{{ requestrr_name }}"

        # Type: string
        requestrr_role_paths_location: "{{ server_appdata_path }}/{{ requestrr_role_paths_folder }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        requestrr2_paths_folder: "{{ requestrr_name }}"

        # Type: string
        requestrr2_paths_location: "{{ server_appdata_path }}/{{ requestrr_role_paths_folder }}"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        requestrr_role_web_subdomain: "{{ requestrr_name }}"

        # Type: string
        requestrr_role_web_domain: "{{ user.domain }}"

        # Type: string
        requestrr_role_web_port: "4545"

        # Type: string
        requestrr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='requestrr') + '.' + lookup('role_var', '_web_domain', role='requestrr')
                                 if (lookup('role_var', '_web_subdomain', role='requestrr') | length > 0)
                                 else lookup('role_var', '_web_domain', role='requestrr')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        requestrr2_web_subdomain: "{{ requestrr_name }}"

        # Type: string
        requestrr2_web_domain: "{{ user.domain }}"

        # Type: string
        requestrr2_web_port: "4545"

        # Type: string
        requestrr2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='requestrr') + '.' + lookup('role_var', '_web_domain', role='requestrr')
                             if (lookup('role_var', '_web_subdomain', role='requestrr') | length > 0)
                             else lookup('role_var', '_web_domain', role='requestrr')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        requestrr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='requestrr') }}"

        # Type: string
        requestrr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='requestrr') }}"

        # Type: bool (true/false)
        requestrr_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        requestrr2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='requestrr') }}"

        # Type: string
        requestrr2_dns_zone: "{{ lookup('role_var', '_web_domain', role='requestrr') }}"

        # Type: bool (true/false)
        requestrr2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        requestrr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        requestrr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        requestrr_role_traefik_middleware_custom: ""

        # Type: string
        requestrr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        requestrr_role_traefik_enabled: true

        # Type: bool (true/false)
        requestrr_role_traefik_api_enabled: false

        # Type: string
        requestrr_role_traefik_api_endpoint: ""

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        requestrr2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        requestrr2_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        requestrr2_traefik_middleware_custom: ""

        # Type: string
        requestrr2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        requestrr2_traefik_enabled: true

        # Type: bool (true/false)
        requestrr2_traefik_api_enabled: false

        # Type: string
        requestrr2_traefik_api_endpoint: ""

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        requestrr_role_docker_container: "{{ requestrr_name }}"

        # Image
        # Type: bool (true/false)
        requestrr_role_docker_image_pull: true

        # Type: string
        requestrr_role_docker_image_repo: "thomst08/requestrr"

        # Type: string
        requestrr_role_docker_image_tag: "latest"

        # Type: string
        requestrr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='requestrr') }}:{{ lookup('role_var', '_docker_image_tag', role='requestrr') }}"

        # Envs
        # Type: dict
        requestrr_role_docker_envs_default: 
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          UMASK: "002"

        # Type: dict
        requestrr_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        requestrr_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='requestrr') }}:/root/config"

        # Type: list
        requestrr_role_docker_volumes_custom: []

        # Hostname
        # Type: string
        requestrr_role_docker_hostname: "{{ requestrr_name }}"

        # Networks
        # Type: string
        requestrr_role_docker_networks_alias: "{{ requestrr_name }}"

        # Type: list
        requestrr_role_docker_networks_default: []

        # Type: list
        requestrr_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        requestrr_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        requestrr_role_docker_state: started

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        requestrr2_docker_container: "{{ requestrr_name }}"

        # Image
        # Type: bool (true/false)
        requestrr2_docker_image_pull: true

        # Type: string
        requestrr2_docker_image_repo: "thomst08/requestrr"

        # Type: string
        requestrr2_docker_image_tag: "latest"

        # Type: string
        requestrr2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='requestrr') }}:{{ lookup('role_var', '_docker_image_tag', role='requestrr') }}"

        # Envs
        # Type: dict
        requestrr2_docker_envs_default: 
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          UMASK: "002"

        # Type: dict
        requestrr2_docker_envs_custom: {}

        # Volumes
        # Type: list
        requestrr2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='requestrr') }}:/root/config"

        # Type: list
        requestrr2_docker_volumes_custom: []

        # Hostname
        # Type: string
        requestrr2_docker_hostname: "{{ requestrr_name }}"

        # Networks
        # Type: string
        requestrr2_docker_networks_alias: "{{ requestrr_name }}"

        # Type: list
        requestrr2_docker_networks_default: []

        # Type: list
        requestrr2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        requestrr2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        requestrr2_docker_state: started


        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        requestrr_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        requestrr_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        requestrr_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        requestrr_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        requestrr_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        requestrr_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        requestrr_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        requestrr_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        requestrr_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        requestrr_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        requestrr_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        requestrr_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        requestrr_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        requestrr_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        requestrr_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        requestrr_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        requestrr_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            requestrr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "requestrr2.{{ user.domain }}"
              - "requestrr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            requestrr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'requestrr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `requestrr2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        requestrr2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        requestrr2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        requestrr2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        requestrr2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        requestrr2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        requestrr2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        requestrr2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        requestrr2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        requestrr2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        requestrr2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        requestrr2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        requestrr2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        requestrr2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        requestrr2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        requestrr2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        requestrr2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        requestrr2_web_scheme:

        ```

        1.  Example:

            ```yaml
            requestrr2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "requestrr2.{{ user.domain }}"
              - "requestrr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            requestrr2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'requestrr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

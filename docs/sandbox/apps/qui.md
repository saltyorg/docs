---
hide:
  - tags
tags:
  - qui
  - torrent
  - qbittorrent
---

# Qui

## What is it?

[Qui](https://github.com/autobrr/qui) is a fast, modern web interface for qBittorrent. Supports managing multiple qBittorrent instances from a single, lightweight application.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/autobrr/qui){: .header-icons } | [:octicons-link-16: Docs](https://github.com/autobrr/qui?tab=readme-ov-file#configuration){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/autobrr/qui){: .header-icons } | [:material-docker: Docker](https://github.com/autobrr/qui/blob/main/docker-compose.yml){: .header-icons } |

### 1. Installation

``` shell

sb install sandbox-qui

```

### 2. URL

- To access Qui, visit `https://qui._yourdomain.com_`

### 3. Setup

- Configure your qBittorrent instance connections through the web interface.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `qui_instances`.

    === "Role-level Override"

        Applies to all instances of qui:

        ```yaml
        qui_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `qui2`):

        ```yaml
        qui2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `qui_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `qui_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        qui_instances: ["qui"]

        ```

    === "Example"

        ```yaml
        # Type: list
        qui_instances: ["qui", "qui2"]

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        qui_role_paths_folder: "{{ qui_name }}"

        # Type: string
        qui_role_paths_location: "{{ server_appdata_path }}/{{ qui_role_paths_folder }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        qui2_paths_folder: "{{ qui_name }}"

        # Type: string
        qui2_paths_location: "{{ server_appdata_path }}/{{ qui_role_paths_folder }}"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        qui_role_web_subdomain: "{{ qui_name }}"

        # Type: string
        qui_role_web_domain: "{{ user.domain }}"

        # Type: string
        qui_role_web_port: "7476"

        # Type: string
        qui_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='qui') + '.' + lookup('role_var', '_web_domain', role='qui')
                           if (lookup('role_var', '_web_subdomain', role='qui') | length > 0)
                           else lookup('role_var', '_web_domain', role='qui')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        qui2_web_subdomain: "{{ qui_name }}"

        # Type: string
        qui2_web_domain: "{{ user.domain }}"

        # Type: string
        qui2_web_port: "7476"

        # Type: string
        qui2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='qui') + '.' + lookup('role_var', '_web_domain', role='qui')
                       if (lookup('role_var', '_web_subdomain', role='qui') | length > 0)
                       else lookup('role_var', '_web_domain', role='qui')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        qui_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='qui') }}"

        # Type: string
        qui_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='qui') }}"

        # Type: bool (true/false)
        qui_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        qui2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='qui') }}"

        # Type: string
        qui2_dns_zone: "{{ lookup('role_var', '_web_domain', role='qui') }}"

        # Type: bool (true/false)
        qui2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        qui_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        qui_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        qui_role_traefik_middleware_custom: ""

        # Type: string
        qui_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        qui_role_traefik_enabled: true

        # Type: bool (true/false)
        qui_role_traefik_api_enabled: true

        # Type: string
        qui_role_traefik_api_endpoint: "PathPrefix(`/proxy`)"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        qui2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        qui2_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        qui2_traefik_middleware_custom: ""

        # Type: string
        qui2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        qui2_traefik_enabled: true

        # Type: bool (true/false)
        qui2_traefik_api_enabled: true

        # Type: string
        qui2_traefik_api_endpoint: "PathPrefix(`/proxy`)"

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        qui_role_docker_container: "{{ qui_name }}"

        # Image
        # Type: bool (true/false)
        qui_role_docker_image_pull: true

        # Type: string
        qui_role_docker_image_repo: "ghcr.io/autobrr/qui"

        # Type: string
        qui_role_docker_image_tag: "latest"

        # Type: string
        qui_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='qui') }}:{{ lookup('role_var', '_docker_image_tag', role='qui') }}"

        # Envs
        # Type: dict
        qui_role_docker_envs_default: 
          TZ: "{{ tz }}"

        # Type: dict
        qui_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        qui_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='qui') }}:/config"

        # Type: list
        qui_role_docker_volumes_custom: []

        # Hosts
        # Type: dict
        qui_role_docker_hosts_default: {}

        # Type: dict
        qui_role_docker_hosts_custom: {}

        # Hostname
        # Type: string
        qui_role_docker_hostname: "{{ qui_name }}"

        # Networks
        # Type: string
        qui_role_docker_networks_alias: "{{ qui_name }}"

        # Type: list
        qui_role_docker_networks_default: []

        # Type: list
        qui_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        qui_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        qui_role_docker_state: started

        # User
        # Type: string
        qui_role_docker_user: "{{ uid }}:{{ gid }}"

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        qui2_docker_container: "{{ qui_name }}"

        # Image
        # Type: bool (true/false)
        qui2_docker_image_pull: true

        # Type: string
        qui2_docker_image_repo: "ghcr.io/autobrr/qui"

        # Type: string
        qui2_docker_image_tag: "latest"

        # Type: string
        qui2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='qui') }}:{{ lookup('role_var', '_docker_image_tag', role='qui') }}"

        # Envs
        # Type: dict
        qui2_docker_envs_default: 
          TZ: "{{ tz }}"

        # Type: dict
        qui2_docker_envs_custom: {}

        # Volumes
        # Type: list
        qui2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='qui') }}:/config"

        # Type: list
        qui2_docker_volumes_custom: []

        # Hosts
        # Type: dict
        qui2_docker_hosts_default: {}

        # Type: dict
        qui2_docker_hosts_custom: {}

        # Hostname
        # Type: string
        qui2_docker_hostname: "{{ qui_name }}"

        # Networks
        # Type: string
        qui2_docker_networks_alias: "{{ qui_name }}"

        # Type: list
        qui2_docker_networks_default: []

        # Type: list
        qui2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        qui2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        qui2_docker_state: started

        # User
        # Type: string
        qui2_docker_user: "{{ uid }}:{{ gid }}"


        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        qui_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        qui_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        qui_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        qui_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        qui_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        qui_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        qui_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        qui_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        qui_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        qui_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        qui_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        qui_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        qui_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        qui_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        qui_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        qui_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        qui_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            qui_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "qui2.{{ user.domain }}"
              - "qui.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            qui_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'qui2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `qui2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        qui2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        qui2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        qui2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        qui2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        qui2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        qui2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        qui2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        qui2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        qui2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        qui2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        qui2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        qui2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        qui2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        qui2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        qui2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        qui2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        qui2_web_scheme:

        ```

        1.  Example:

            ```yaml
            qui2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "qui2.{{ user.domain }}"
              - "qui.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            qui2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'qui2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

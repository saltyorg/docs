---
hide:
  - tags
tags:
  - ombi
  - requests
  - automation
---

# Ombi

## What is it?

[Ombi](https://ombi.io/) is a self-hosted web application that automatically gives your shared Plex or Emby users the ability to request content by themselves!

Ombi can be linked to multiple TV Show and Movie DVR tools to create a seamless end-to-end experience for your users.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://ombi.io/){: .header-icons } | [:octicons-link-16: Docs](https://docs.ombi.app/guides/installation/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Ombi-app/Ombi){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/hotio/ombi){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-ombi

```

### 2. URL

- To access Ombi, visit `https://ombi._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `ombi_instances`.

    === "Role-level Override"

        Applies to all instances of ombi:

        ```yaml
        ombi_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `ombi2`):

        ```yaml
        ombi2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        ombi_instances: ["ombi"]

        ```

    === "Example"

        ```yaml
        # Type: list
        ombi_instances: ["ombi", "ombi2"]

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        ombi_role_paths_folder: "{{ ombi_name }}"

        # Type: string
        ombi_role_paths_location: "{{ server_appdata_path }}/{{ ombi_role_paths_folder }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        ombi2_paths_folder: "{{ ombi_name }}"

        # Type: string
        ombi2_paths_location: "{{ server_appdata_path }}/{{ ombi_role_paths_folder }}"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        ombi_role_web_subdomain: "{{ ombi_name }}"

        # Type: string
        ombi_role_web_domain: "{{ user.domain }}"

        # Type: string
        ombi_role_web_port: "3579"

        # Type: string
        ombi_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='ombi') + '.' + lookup('role_var', '_web_domain', role='ombi')
                            if (lookup('role_var', '_web_subdomain', role='ombi') | length > 0)
                            else lookup('role_var', '_web_domain', role='ombi')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        ombi2_web_subdomain: "{{ ombi_name }}"

        # Type: string
        ombi2_web_domain: "{{ user.domain }}"

        # Type: string
        ombi2_web_port: "3579"

        # Type: string
        ombi2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='ombi') + '.' + lookup('role_var', '_web_domain', role='ombi')
                        if (lookup('role_var', '_web_subdomain', role='ombi') | length > 0)
                        else lookup('role_var', '_web_domain', role='ombi')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        ombi_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='ombi') }}"

        # Type: string
        ombi_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='ombi') }}"

        # Type: bool (true/false)
        ombi_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        ombi2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='ombi') }}"

        # Type: string
        ombi2_dns_zone: "{{ lookup('role_var', '_web_domain', role='ombi') }}"

        # Type: bool (true/false)
        ombi2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        ombi_role_traefik_sso_middleware: ""

        # Type: string
        ombi_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        ombi_role_traefik_middleware_custom: ""

        # Type: string
        ombi_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        ombi_role_traefik_enabled: true

        # Type: bool (true/false)
        ombi_role_traefik_api_enabled: false

        # Type: string
        ombi_role_traefik_api_endpoint: ""

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        ombi2_traefik_sso_middleware: ""

        # Type: string
        ombi2_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        ombi2_traefik_middleware_custom: ""

        # Type: string
        ombi2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        ombi2_traefik_enabled: true

        # Type: bool (true/false)
        ombi2_traefik_api_enabled: false

        # Type: string
        ombi2_traefik_api_endpoint: ""

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        ombi_role_docker_container: "{{ ombi_name }}"

        # Image
        # Type: bool (true/false)
        ombi_role_docker_image_pull: true

        # Type: string
        ombi_role_docker_image_repo: "lscr.io/linuxserver/ombi"

        # Type: string
        ombi_role_docker_image_tag: "latest"

        # Type: string
        ombi_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='ombi') }}:{{ lookup('role_var', '_docker_image_tag', role='ombi') }}"

        # Envs
        # Type: dict
        ombi_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          UMASK: "002"
          TZ: "{{ tz }}"

        # Type: dict
        ombi_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        ombi_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='ombi') }}:/config"

        # Type: list
        ombi_role_docker_volumes_custom: []

        # Hostname
        # Type: string
        ombi_role_docker_hostname: "{{ ombi_name }}"

        # Networks
        # Type: string
        ombi_role_docker_networks_alias: "{{ ombi_name }}"

        # Type: list
        ombi_role_docker_networks_default: []

        # Type: list
        ombi_role_docker_networks_custom: []

        # Restart Policy
        # Type: string
        ombi_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        ombi_role_docker_state: started

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        ombi2_docker_container: "{{ ombi_name }}"

        # Image
        # Type: bool (true/false)
        ombi2_docker_image_pull: true

        # Type: string
        ombi2_docker_image_repo: "lscr.io/linuxserver/ombi"

        # Type: string
        ombi2_docker_image_tag: "latest"

        # Type: string
        ombi2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='ombi') }}:{{ lookup('role_var', '_docker_image_tag', role='ombi') }}"

        # Envs
        # Type: dict
        ombi2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          UMASK: "002"
          TZ: "{{ tz }}"

        # Type: dict
        ombi2_docker_envs_custom: {}

        # Volumes
        # Type: list
        ombi2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='ombi') }}:/config"

        # Type: list
        ombi2_docker_volumes_custom: []

        # Hostname
        # Type: string
        ombi2_docker_hostname: "{{ ombi_name }}"

        # Networks
        # Type: string
        ombi2_docker_networks_alias: "{{ ombi_name }}"

        # Type: list
        ombi2_docker_networks_default: []

        # Type: list
        ombi2_docker_networks_custom: []

        # Restart Policy
        # Type: string
        ombi2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        ombi2_docker_state: started


        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        ombi_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        ombi_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        ombi_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        ombi_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        ombi_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        ombi_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        ombi_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        ombi_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        ombi_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        ombi_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        ombi_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        ombi_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        ombi_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        ombi_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        ombi_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        ombi_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        ombi_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            ombi_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "ombi2.{{ user.domain }}"
              - "ombi.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            ombi_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'ombi2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `ombi2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        ombi2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        ombi2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        ombi2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        ombi2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        ombi2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        ombi2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        ombi2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        ombi2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        ombi2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        ombi2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        ombi2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        ombi2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        ombi2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        ombi2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        ombi2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        ombi2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        ombi2_web_scheme:

        ```

        1.  Example:

            ```yaml
            ombi2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "ombi2.{{ user.domain }}"
              - "ombi.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            ombi2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'ombi2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

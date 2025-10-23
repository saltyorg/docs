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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

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

    When overriding variables that end in `_default` (like `ombi_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `ombi_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`ombi_instances`"

        ```yaml
        # Type: list
        ombi_instances: ["ombi"]
        ```

        !!! example

            ```yaml
            # Type: list
            ombi_instances: ["ombi", "ombi2"]
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`ombi_role_paths_folder`"

            ```yaml
            # Type: string
            ombi_role_paths_folder: "{{ ombi_name }}"
            ```

        ??? variable string "`ombi_role_paths_location`"

            ```yaml
            # Type: string
            ombi_role_paths_location: "{{ server_appdata_path }}/{{ ombi_role_paths_folder }}"
            ```

    === "Instance-level"

        ??? variable string "`ombi2_paths_folder`"

            ```yaml
            # Type: string
            ombi2_paths_folder: "{{ ombi_name }}"
            ```

        ??? variable string "`ombi2_paths_location`"

            ```yaml
            # Type: string
            ombi2_paths_location: "{{ server_appdata_path }}/{{ ombi_role_paths_folder }}"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`ombi_role_web_subdomain`"

            ```yaml
            # Type: string
            ombi_role_web_subdomain: "{{ ombi_name }}"
            ```

        ??? variable string "`ombi_role_web_domain`"

            ```yaml
            # Type: string
            ombi_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`ombi_role_web_port`"

            ```yaml
            # Type: string
            ombi_role_web_port: "3579"
            ```

        ??? variable string "`ombi_role_web_url`"

            ```yaml
            # Type: string
            ombi_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='ombi') + '.' + lookup('role_var', '_web_domain', role='ombi')
                                if (lookup('role_var', '_web_subdomain', role='ombi') | length > 0)
                                else lookup('role_var', '_web_domain', role='ombi')) }}"
            ```

    === "Instance-level"

        ??? variable string "`ombi2_web_subdomain`"

            ```yaml
            # Type: string
            ombi2_web_subdomain: "{{ ombi_name }}"
            ```

        ??? variable string "`ombi2_web_domain`"

            ```yaml
            # Type: string
            ombi2_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`ombi2_web_port`"

            ```yaml
            # Type: string
            ombi2_web_port: "3579"
            ```

        ??? variable string "`ombi2_web_url`"

            ```yaml
            # Type: string
            ombi2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='ombi') + '.' + lookup('role_var', '_web_domain', role='ombi')
                            if (lookup('role_var', '_web_subdomain', role='ombi') | length > 0)
                            else lookup('role_var', '_web_domain', role='ombi')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`ombi_role_dns_record`"

            ```yaml
            # Type: string
            ombi_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='ombi') }}"
            ```

        ??? variable string "`ombi_role_dns_zone`"

            ```yaml
            # Type: string
            ombi_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='ombi') }}"
            ```

        ??? variable bool "`ombi_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            ombi_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`ombi2_dns_record`"

            ```yaml
            # Type: string
            ombi2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='ombi') }}"
            ```

        ??? variable string "`ombi2_dns_zone`"

            ```yaml
            # Type: string
            ombi2_dns_zone: "{{ lookup('role_var', '_web_domain', role='ombi') }}"
            ```

        ??? variable bool "`ombi2_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            ombi2_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`ombi_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            ombi_role_traefik_sso_middleware: ""
            ```

        ??? variable string "`ombi_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            ombi_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`ombi_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            ombi_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`ombi_role_traefik_certresolver`"

            ```yaml
            # Type: string
            ombi_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`ombi_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            ombi_role_traefik_enabled: true
            ```

        ??? variable bool "`ombi_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            ombi_role_traefik_api_enabled: false
            ```

        ??? variable string "`ombi_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            ombi_role_traefik_api_endpoint: ""
            ```

    === "Instance-level"

        ??? variable string "`ombi2_traefik_sso_middleware`"

            ```yaml
            # Type: string
            ombi2_traefik_sso_middleware: ""
            ```

        ??? variable string "`ombi2_traefik_middleware_default`"

            ```yaml
            # Type: string
            ombi2_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`ombi2_traefik_middleware_custom`"

            ```yaml
            # Type: string
            ombi2_traefik_middleware_custom: ""
            ```

        ??? variable string "`ombi2_traefik_certresolver`"

            ```yaml
            # Type: string
            ombi2_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`ombi2_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            ombi2_traefik_enabled: true
            ```

        ??? variable bool "`ombi2_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            ombi2_traefik_api_enabled: false
            ```

        ??? variable string "`ombi2_traefik_api_endpoint`"

            ```yaml
            # Type: string
            ombi2_traefik_api_endpoint: ""
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`ombi_role_docker_container`"

            ```yaml
            # Type: string
            ombi_role_docker_container: "{{ ombi_name }}"
            ```

        ##### Image

        ??? variable bool "`ombi_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            ombi_role_docker_image_pull: true
            ```

        ??? variable string "`ombi_role_docker_image_repo`"

            ```yaml
            # Type: string
            ombi_role_docker_image_repo: "lscr.io/linuxserver/ombi"
            ```

        ??? variable string "`ombi_role_docker_image_tag`"

            ```yaml
            # Type: string
            ombi_role_docker_image_tag: "latest"
            ```

        ??? variable string "`ombi_role_docker_image`"

            ```yaml
            # Type: string
            ombi_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='ombi') }}:{{ lookup('role_var', '_docker_image_tag', role='ombi') }}"
            ```

        ##### Envs

        ??? variable dict "`ombi_role_docker_envs_default`"

            ```yaml
            # Type: dict
            ombi_role_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              UMASK: "002"
              TZ: "{{ tz }}"
            ```

        ??? variable dict "`ombi_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            ombi_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`ombi_role_docker_volumes_default`"

            ```yaml
            # Type: list
            ombi_role_docker_volumes_default: 
              - "{{ lookup('role_var', '_paths_location', role='ombi') }}:/config"
            ```

        ??? variable list "`ombi_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            ombi_role_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`ombi_role_docker_hostname`"

            ```yaml
            # Type: string
            ombi_role_docker_hostname: "{{ ombi_name }}"
            ```

        ##### Networks

        ??? variable string "`ombi_role_docker_networks_alias`"

            ```yaml
            # Type: string
            ombi_role_docker_networks_alias: "{{ ombi_name }}"
            ```

        ??? variable list "`ombi_role_docker_networks_default`"

            ```yaml
            # Type: list
            ombi_role_docker_networks_default: []
            ```

        ??? variable list "`ombi_role_docker_networks_custom`"

            ```yaml
            # Type: list
            ombi_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`ombi_role_docker_restart_policy`"

            ```yaml
            # Type: string
            ombi_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`ombi_role_docker_state`"

            ```yaml
            # Type: string
            ombi_role_docker_state: started
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`ombi2_docker_container`"

            ```yaml
            # Type: string
            ombi2_docker_container: "{{ ombi_name }}"
            ```

        ##### Image

        ??? variable bool "`ombi2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            ombi2_docker_image_pull: true
            ```

        ??? variable string "`ombi2_docker_image_repo`"

            ```yaml
            # Type: string
            ombi2_docker_image_repo: "lscr.io/linuxserver/ombi"
            ```

        ??? variable string "`ombi2_docker_image_tag`"

            ```yaml
            # Type: string
            ombi2_docker_image_tag: "latest"
            ```

        ??? variable string "`ombi2_docker_image`"

            ```yaml
            # Type: string
            ombi2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='ombi') }}:{{ lookup('role_var', '_docker_image_tag', role='ombi') }}"
            ```

        ##### Envs

        ??? variable dict "`ombi2_docker_envs_default`"

            ```yaml
            # Type: dict
            ombi2_docker_envs_default: 
              PUID: "{{ uid }}"
              PGID: "{{ gid }}"
              UMASK: "002"
              TZ: "{{ tz }}"
            ```

        ??? variable dict "`ombi2_docker_envs_custom`"

            ```yaml
            # Type: dict
            ombi2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`ombi2_docker_volumes_default`"

            ```yaml
            # Type: list
            ombi2_docker_volumes_default: 
              - "{{ lookup('role_var', '_paths_location', role='ombi') }}:/config"
            ```

        ??? variable list "`ombi2_docker_volumes_custom`"

            ```yaml
            # Type: list
            ombi2_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`ombi2_docker_hostname`"

            ```yaml
            # Type: string
            ombi2_docker_hostname: "{{ ombi_name }}"
            ```

        ##### Networks

        ??? variable string "`ombi2_docker_networks_alias`"

            ```yaml
            # Type: string
            ombi2_docker_networks_alias: "{{ ombi_name }}"
            ```

        ??? variable list "`ombi2_docker_networks_default`"

            ```yaml
            # Type: list
            ombi2_docker_networks_default: []
            ```

        ??? variable list "`ombi2_docker_networks_custom`"

            ```yaml
            # Type: list
            ombi2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`ombi2_docker_restart_policy`"

            ```yaml
            # Type: string
            ombi2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`ombi2_docker_state`"

            ```yaml
            # Type: string
            ombi2_docker_state: started
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`ombi_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            ombi_role_autoheal_enabled: true
            ```

        ??? variable string "`ombi_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            ombi_role_depends_on: ""
            ```

        ??? variable string "`ombi_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            ombi_role_depends_on_delay: "0"
            ```

        ??? variable string "`ombi_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            ombi_role_depends_on_healthchecks:
            ```

        ??? variable bool "`ombi_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            ombi_role_diun_enabled: true
            ```

        ??? variable bool "`ombi_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            ombi_role_dns_enabled: true
            ```

        ??? variable bool "`ombi_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            ombi_role_docker_controller: true
            ```

        ??? variable bool "`ombi_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            ombi_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`ombi_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            ombi_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`ombi_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            ombi_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`ombi_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            ombi_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`ombi_role_traefik_middleware_http_api_insecure`"

            ```yaml
            # Type: bool (true/false)
            ombi_role_traefik_middleware_http_api_insecure:
            ```

        ??? variable bool "`ombi_role_traefik_middleware_http_insecure`"

            ```yaml
            # Type: bool (true/false)
            ombi_role_traefik_middleware_http_insecure:
            ```

        ??? variable bool "`ombi_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            ombi_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`ombi_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            ombi_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`ombi_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            ombi_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`ombi_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            ombi_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                ombi_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "ombi2.{{ user.domain }}"
                  - "ombi.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`ombi_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            ombi_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                ombi_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'ombi2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`ombi_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            ombi_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `ombi2`):

        ??? variable bool "`ombi2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            ombi2_autoheal_enabled: true
            ```

        ??? variable string "`ombi2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            ombi2_depends_on: ""
            ```

        ??? variable string "`ombi2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            ombi2_depends_on_delay: "0"
            ```

        ??? variable string "`ombi2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            ombi2_depends_on_healthchecks:
            ```

        ??? variable bool "`ombi2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            ombi2_diun_enabled: true
            ```

        ??? variable bool "`ombi2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            ombi2_dns_enabled: true
            ```

        ??? variable bool "`ombi2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            ombi2_docker_controller: true
            ```

        ??? variable bool "`ombi2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            ombi2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`ombi2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            ombi2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`ombi2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            ombi2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`ombi2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            ombi2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`ombi2_traefik_middleware_http_api_insecure`"

            ```yaml
            # Type: bool (true/false)
            ombi2_traefik_middleware_http_api_insecure:
            ```

        ??? variable bool "`ombi2_traefik_middleware_http_insecure`"

            ```yaml
            # Type: bool (true/false)
            ombi2_traefik_middleware_http_insecure:
            ```

        ??? variable bool "`ombi2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            ombi2_traefik_robot_enabled: true
            ```

        ??? variable bool "`ombi2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            ombi2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`ombi2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            ombi2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`ombi2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            ombi2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                ombi2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "ombi2.{{ user.domain }}"
                  - "ombi.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`ombi2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            ombi2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                ombi2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'ombi2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`ombi2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            ombi2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
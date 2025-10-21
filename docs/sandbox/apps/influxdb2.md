---
hide:
  - tags
tags:
  - influxdb2
  - database
  - timeseries
---

# InfluxDB2

## What is it?

[InfluxDB2](https://www.influxdata.com/products/influxdb/) is an open source time series database for recording metrics, events, and analytics.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.influxdata.com/products/influxdb/){: .header-icons } | [:octicons-link-16: Docs](https://docs.influxdata.com/influxdb/latest/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/influxdata/influxdata-docker){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/_/influxdb){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-influxdb2

```

### 2. URL

- To access InfluxDB2, visit `https://influxdb2._yourdomain.com_`

### 3. Setup

- To setup the initial admin user, token and bucket, visit the UI at the URL above.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `influxdb2_instances`.

    === "Role-level Override"

        Applies to all instances of influxdb2:

        ```yaml
        influxdb2_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `influxdb22`):

        ```yaml
        influxdb22_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `influxdb2_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `influxdb2_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`influxdb2_instances`"

        ```yaml
        # Type: list
        influxdb2_instances: ["influxdb2"]
        ```

        !!! example

            ```yaml
            # Type: list
            influxdb2_instances: ["influxdb2", "influxdb22"]
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`influxdb2_role_paths_folder`"

            ```yaml
            # Type: string
            influxdb2_role_paths_folder: "{{ influxdb2_name }}"
            ```

        ??? variable string "`influxdb2_role_paths_location`"

            ```yaml
            # Type: string
            influxdb2_role_paths_location: "{{ server_appdata_path }}/{{ influxdb2_role_paths_folder }}"
            ```

    === "Instance-level"

        ??? variable string "`influxdb22_paths_folder`"

            ```yaml
            # Type: string
            influxdb22_paths_folder: "{{ influxdb2_name }}"
            ```

        ??? variable string "`influxdb22_paths_location`"

            ```yaml
            # Type: string
            influxdb22_paths_location: "{{ server_appdata_path }}/{{ influxdb2_role_paths_folder }}"
            ```

=== "Web"

    === "Role-level"

        ??? variable string "`influxdb2_role_web_subdomain`"

            ```yaml
            # Type: string
            influxdb2_role_web_subdomain: "{{ influxdb2_name }}"
            ```

        ??? variable string "`influxdb2_role_web_domain`"

            ```yaml
            # Type: string
            influxdb2_role_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`influxdb2_role_web_port`"

            ```yaml
            # Type: string
            influxdb2_role_web_port: "8086"
            ```

        ??? variable string "`influxdb2_role_web_url`"

            ```yaml
            # Type: string
            influxdb2_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='influxdb2') + '.' + lookup('role_var', '_web_domain', role='influxdb2')
                                     if (lookup('role_var', '_web_subdomain', role='influxdb2') | length > 0)
                                     else lookup('role_var', '_web_domain', role='influxdb2')) }}"
            ```

    === "Instance-level"

        ??? variable string "`influxdb22_web_subdomain`"

            ```yaml
            # Type: string
            influxdb22_web_subdomain: "{{ influxdb2_name }}"
            ```

        ??? variable string "`influxdb22_web_domain`"

            ```yaml
            # Type: string
            influxdb22_web_domain: "{{ user.domain }}"
            ```

        ??? variable string "`influxdb22_web_port`"

            ```yaml
            # Type: string
            influxdb22_web_port: "8086"
            ```

        ??? variable string "`influxdb22_web_url`"

            ```yaml
            # Type: string
                    influxdb22_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='influxdb2') + '.' + lookup('role_var', '_web_domain', role='influxdb2')
                                         if (lookup('role_var', '_web_subdomain', role='influxdb2') | length > 0)
                                         else lookup('role_var', '_web_domain', role='influxdb2')) }}"
            ```

=== "DNS"

    === "Role-level"

        ??? variable string "`influxdb2_role_dns_record`"

            ```yaml
            # Type: string
            influxdb2_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='influxdb2') }}"
            ```

        ??? variable string "`influxdb2_role_dns_zone`"

            ```yaml
            # Type: string
            influxdb2_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='influxdb2') }}"
            ```

        ??? variable bool "`influxdb2_role_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            influxdb2_role_dns_proxy: "{{ dns_proxied }}"
            ```

    === "Instance-level"

        ??? variable string "`influxdb22_dns_record`"

            ```yaml
            # Type: string
            influxdb22_dns_record: "{{ lookup('role_var', '_web_subdomain', role='influxdb2') }}"
            ```

        ??? variable string "`influxdb22_dns_zone`"

            ```yaml
            # Type: string
            influxdb22_dns_zone: "{{ lookup('role_var', '_web_domain', role='influxdb2') }}"
            ```

        ??? variable bool "`influxdb22_dns_proxy`"

            ```yaml
            # Type: bool (true/false)
            influxdb22_dns_proxy: "{{ dns_proxied }}"
            ```

=== "Traefik"

    === "Role-level"

        ??? variable string "`influxdb2_role_traefik_sso_middleware`"

            ```yaml
            # Type: string
            influxdb2_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`influxdb2_role_traefik_middleware_default`"

            ```yaml
            # Type: string
            influxdb2_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`influxdb2_role_traefik_middleware_custom`"

            ```yaml
            # Type: string
            influxdb2_role_traefik_middleware_custom: ""
            ```

        ??? variable string "`influxdb2_role_traefik_certresolver`"

            ```yaml
            # Type: string
            influxdb2_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`influxdb2_role_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            influxdb2_role_traefik_enabled: true
            ```

        ??? variable bool "`influxdb2_role_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            influxdb2_role_traefik_api_enabled: false
            ```

        ??? variable string "`influxdb2_role_traefik_api_endpoint`"

            ```yaml
            # Type: string
            influxdb2_role_traefik_api_endpoint: ""
            ```

    === "Instance-level"

        ??? variable string "`influxdb22_traefik_sso_middleware`"

            ```yaml
            # Type: string
            influxdb22_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
            ```

        ??? variable string "`influxdb22_traefik_middleware_default`"

            ```yaml
            # Type: string
            influxdb22_traefik_middleware_default: "{{ traefik_default_middleware }}"
            ```

        ??? variable string "`influxdb22_traefik_middleware_custom`"

            ```yaml
            # Type: string
            influxdb22_traefik_middleware_custom: ""
            ```

        ??? variable string "`influxdb22_traefik_certresolver`"

            ```yaml
            # Type: string
            influxdb22_traefik_certresolver: "{{ traefik_default_certresolver }}"
            ```

        ??? variable bool "`influxdb22_traefik_enabled`"

            ```yaml
            # Type: bool (true/false)
            influxdb22_traefik_enabled: true
            ```

        ??? variable bool "`influxdb22_traefik_api_enabled`"

            ```yaml
            # Type: bool (true/false)
            influxdb22_traefik_api_enabled: false
            ```

        ??? variable string "`influxdb22_traefik_api_endpoint`"

            ```yaml
            # Type: string
            influxdb22_traefik_api_endpoint: ""
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`influxdb2_role_docker_container`"

            ```yaml
            # Type: string
            influxdb2_role_docker_container: "{{ influxdb2_name }}"
            ```

        ##### Image

        ??? variable bool "`influxdb2_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            influxdb2_role_docker_image_pull: true
            ```

        ??? variable string "`influxdb2_role_docker_image_tag`"

            ```yaml
            # Type: string
            influxdb2_role_docker_image_tag: "2-alpine"
            ```

        ??? variable string "`influxdb2_role_docker_image_repo`"

            ```yaml
            # Type: string
            influxdb2_role_docker_image_repo: "influxdb"
            ```

        ??? variable string "`influxdb2_role_docker_image`"

            ```yaml
            # Type: string
            influxdb2_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='influxdb2') }}:{{ lookup('role_var', '_docker_image_tag', role='influxdb2') }}"
            ```

        ##### Volumes

        ??? variable list "`influxdb2_role_docker_volumes_default`"

            ```yaml
            # Type: list
            influxdb2_role_docker_volumes_default: 
              - "{{ lookup('role_var', '_paths_location', role='influxdb2') }}/data:/var/lib/influxdb22"
              - "{{ lookup('role_var', '_paths_location', role='influxdb2') }}/config:/etc/influxdb22"
            ```

        ??? variable list "`influxdb2_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            influxdb2_role_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`influxdb2_role_docker_hostname`"

            ```yaml
            # Type: string
            influxdb2_role_docker_hostname: "{{ influxdb2_name }}"
            ```

        ##### Networks

        ??? variable string "`influxdb2_role_docker_networks_alias`"

            ```yaml
            # Type: string
            influxdb2_role_docker_networks_alias: "{{ influxdb2_name }}"
            ```

        ??? variable list "`influxdb2_role_docker_networks_default`"

            ```yaml
            # Type: list
            influxdb2_role_docker_networks_default: []
            ```

        ??? variable list "`influxdb2_role_docker_networks_custom`"

            ```yaml
            # Type: list
            influxdb2_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`influxdb2_role_docker_restart_policy`"

            ```yaml
            # Type: string
            influxdb2_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`influxdb2_role_docker_state`"

            ```yaml
            # Type: string
            influxdb2_role_docker_state: started
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`influxdb22_docker_container`"

            ```yaml
            # Type: string
            influxdb22_docker_container: "{{ influxdb2_name }}"
            ```

        ##### Image

        ??? variable bool "`influxdb22_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            influxdb22_docker_image_pull: true
            ```

        ??? variable string "`influxdb22_docker_image_tag`"

            ```yaml
            # Type: string
            influxdb22_docker_image_tag: "2-alpine"
            ```

        ??? variable string "`influxdb22_docker_image_repo`"

            ```yaml
            # Type: string
            influxdb22_docker_image_repo: "influxdb"
            ```

        ??? variable string "`influxdb22_docker_image`"

            ```yaml
            # Type: string
            influxdb22_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='influxdb2') }}:{{ lookup('role_var', '_docker_image_tag', role='influxdb2') }}"
            ```

        ##### Volumes

        ??? variable list "`influxdb22_docker_volumes_default`"

            ```yaml
            # Type: list
                    influxdb22_docker_volumes_default: 
                      - "{{ lookup('role_var', '_paths_location', role='influxdb2') }}/data:/var/lib/influxdb22"
                      - "{{ lookup('role_var', '_paths_location', role='influxdb2') }}/config:/etc/influxdb22"
            ```

        ??? variable list "`influxdb22_docker_volumes_custom`"

            ```yaml
            # Type: list
            influxdb22_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`influxdb22_docker_hostname`"

            ```yaml
            # Type: string
            influxdb22_docker_hostname: "{{ influxdb2_name }}"
            ```

        ##### Networks

        ??? variable string "`influxdb22_docker_networks_alias`"

            ```yaml
            # Type: string
            influxdb22_docker_networks_alias: "{{ influxdb2_name }}"
            ```

        ??? variable list "`influxdb22_docker_networks_default`"

            ```yaml
            # Type: list
            influxdb22_docker_networks_default: []
            ```

        ??? variable list "`influxdb22_docker_networks_custom`"

            ```yaml
            # Type: list
            influxdb22_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`influxdb22_docker_restart_policy`"

            ```yaml
            # Type: string
            influxdb22_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`influxdb22_docker_state`"

            ```yaml
            # Type: string
            influxdb22_docker_state: started
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`influxdb2_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            influxdb2_role_autoheal_enabled: true
            ```

        ??? variable string "`influxdb2_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            influxdb2_role_depends_on: ""
            ```

        ??? variable string "`influxdb2_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            influxdb2_role_depends_on_delay: "0"
            ```

        ??? variable string "`influxdb2_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            influxdb2_role_depends_on_healthchecks:
            ```

        ??? variable bool "`influxdb2_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            influxdb2_role_diun_enabled: true
            ```

        ??? variable bool "`influxdb2_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            influxdb2_role_dns_enabled: true
            ```

        ??? variable bool "`influxdb2_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            influxdb2_role_docker_controller: true
            ```

        ??? variable bool "`influxdb2_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            influxdb2_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`influxdb2_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            influxdb2_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`influxdb2_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            influxdb2_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`influxdb2_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            influxdb2_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`influxdb2_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            influxdb2_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`influxdb2_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            influxdb2_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`influxdb2_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            influxdb2_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`influxdb2_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            influxdb2_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                influxdb2_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "influxdb22.{{ user.domain }}"
                  - "influxdb2.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`influxdb2_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            influxdb2_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                influxdb2_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'influxdb22.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`influxdb2_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            influxdb2_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `influxdb22`):

        ??? variable bool "`influxdb22_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            influxdb22_autoheal_enabled: true
            ```

        ??? variable string "`influxdb22_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            influxdb22_depends_on: ""
            ```

        ??? variable string "`influxdb22_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            influxdb22_depends_on_delay: "0"
            ```

        ??? variable string "`influxdb22_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            influxdb22_depends_on_healthchecks:
            ```

        ??? variable bool "`influxdb22_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            influxdb22_diun_enabled: true
            ```

        ??? variable bool "`influxdb22_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            influxdb22_dns_enabled: true
            ```

        ??? variable bool "`influxdb22_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            influxdb22_docker_controller: true
            ```

        ??? variable bool "`influxdb22_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            influxdb22_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`influxdb22_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            influxdb22_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`influxdb22_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            influxdb22_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`influxdb22_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            influxdb22_traefik_gzip_enabled: false
            ```

        ??? variable bool "`influxdb22_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            influxdb22_traefik_robot_enabled: true
            ```

        ??? variable bool "`influxdb22_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            influxdb22_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`influxdb22_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            influxdb22_traefik_wildcard_enabled: true
            ```

        ??? variable list "`influxdb22_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            influxdb22_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                influxdb22_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "influxdb22.{{ user.domain }}"
                  - "influxdb2.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`influxdb22_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            influxdb22_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                influxdb22_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'influxdb22.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`influxdb22_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            influxdb22_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
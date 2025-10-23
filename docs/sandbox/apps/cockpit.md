---
hide:
  - tags
tags:
  - cockpit
  - server
  - administration
---

# Cockpit

## What is it?

[Cockpit](https://cockpit-project.org/) is an interactive server admin interface that makes Linux servers discoverable and manageable through a web browser. It provides comprehensive server management capabilities with a modern web interface.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://cockpit-project.org/){: .header-icons } | [:octicons-link-16: Docs](https://cockpit-project.org/documentation.html){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/cockpit-project/cockpit){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-cockpit
```

### 2. URL

- To access Cockpit, visit `https://cockpit._yourdomain.com_`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        cockpit_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `cockpit_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `cockpit_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`cockpit_name`"

        ```yaml
        # Type: string
        cockpit_name: cockpit
        ```

=== "Settings"

    ??? variable bool "`cockpit_role_vm_enabled`"

        ```yaml
        # Type: bool (true/false)
        cockpit_role_vm_enabled: false
        ```

    ??? variable string "`cockpit_role_service_after`"

        ```yaml
        # Type: string
        cockpit_role_service_after: docker.service
        ```

    ??? variable bool "`cockpit_role_put_dpkg_into_hold`"

        ```yaml
        # Type: bool (true/false)
        cockpit_role_put_dpkg_into_hold: true
        ```

    ??? variable bool "`cockpit_role_put_machines_dpkg_into_hold`"

        ```yaml
        # Type: bool (true/false)
        cockpit_role_put_machines_dpkg_into_hold: true
        ```

=== "Paths"

    ??? variable string "`cockpit_role_paths_socket_location`"

        ```yaml
        # Type: string
        cockpit_role_paths_socket_location: "/etc/systemd/system/cockpit.socket.d/listen.conf"
        ```

    ??? variable string "`cockpit_role_paths_socket_override_location`"

        ```yaml
        # Type: string
        cockpit_role_paths_socket_override_location: "/etc/systemd/system/cockpit.socket.d/override.conf"
        ```

    ??? variable string "`cockpit_role_paths_config_location`"

        ```yaml
        # Type: string
        cockpit_role_paths_config_location: "/etc/cockpit/cockpit.conf"
        ```

    ??? variable string "`cockpit_role_paths_traefik_location`"

        ```yaml
        # Type: string
        cockpit_role_paths_traefik_location: "{{ server_appdata_path }}/traefik/cockpit.yml"
        ```

    ??? variable string "`cockpit_role_paths_service_location`"

        ```yaml
        # Type: string
        cockpit_role_paths_service_location: "/lib/systemd/system/cockpit.service"
        ```

    ??? variable string "`cockpit_role_paths_override_location`"

        ```yaml
        # Type: string
        cockpit_role_paths_override_location: "/etc/systemd/system/cockpit.service.d/override.conf"
        ```

=== "Web"

    ??? variable string "`cockpit_role_web_subdomain`"

        ```yaml
        # Type: string
        cockpit_role_web_subdomain: "{{ cockpit_name }}"
        ```

    ??? variable string "`cockpit_role_web_domain`"

        ```yaml
        # Type: string
        cockpit_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`cockpit_role_web_port`"

        ```yaml
        # Type: string
        cockpit_role_web_port: "1337"
        ```

    ??? variable string "`cockpit_role_web_url`"

        ```yaml
        # Type: string
        cockpit_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='cockpit') + '.' + lookup('role_var', '_web_domain', role='cockpit')
                               if (lookup('role_var', '_web_subdomain', role='cockpit') | length > 0)
                               else lookup('role_var', '_web_domain', role='cockpit')) }}"
        ```

=== "DNS"

    ??? variable string "`cockpit_role_dns_record`"

        ```yaml
        # Type: string
        cockpit_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='cockpit') }}"
        ```

    ??? variable string "`cockpit_role_dns_zone`"

        ```yaml
        # Type: string
        cockpit_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='cockpit') }}"
        ```

    ??? variable bool "`cockpit_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        cockpit_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`cockpit_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        cockpit_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`cockpit_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        cockpit_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`cockpit_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        cockpit_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`cockpit_role_traefik_certresolver`"

        ```yaml
        # Type: string
        cockpit_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`cockpit_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        cockpit_role_traefik_enabled: true
        ```

    ??? variable bool "`cockpit_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        cockpit_role_traefik_api_enabled: false
        ```

=== "Global Override Options"

    ??? variable bool "`cockpit_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        cockpit_role_autoheal_enabled: true
        ```

    ??? variable string "`cockpit_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        cockpit_role_depends_on: ""
        ```

    ??? variable string "`cockpit_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        cockpit_role_depends_on_delay: "0"
        ```

    ??? variable string "`cockpit_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        cockpit_role_depends_on_healthchecks:
        ```

    ??? variable bool "`cockpit_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        cockpit_role_diun_enabled: true
        ```

    ??? variable bool "`cockpit_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        cockpit_role_dns_enabled: true
        ```

    ??? variable bool "`cockpit_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        cockpit_role_docker_controller: true
        ```

    ??? variable bool "`cockpit_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        cockpit_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`cockpit_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        cockpit_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`cockpit_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        cockpit_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`cockpit_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        cockpit_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`cockpit_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        cockpit_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`cockpit_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        cockpit_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`cockpit_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        cockpit_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`cockpit_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        cockpit_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`cockpit_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        cockpit_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`cockpit_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        cockpit_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            cockpit_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "cockpit2.{{ user.domain }}"
              - "cockpit.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`cockpit_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        cockpit_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            cockpit_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'cockpit2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`cockpit_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        cockpit_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
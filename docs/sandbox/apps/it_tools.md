---
hide:
  - tags
tags:
  - it-tools
  - development
  - utilities
---

# IT Tools

## What is it?

[IT Tools](https://it-tools.tech/) is a collection of handy online tools for developers with great UX. It provides 71+ developer tools including code conversion, OTP generation, JWT parsing, SQL query building, and password generators.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://it-tools.tech/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/CorentinTh/it-tools){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/corentinth/it-tools){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-it-tools
```

### 2. URL

- To access IT Tools, visit `https://it-tools._yourdomain.com_`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        it_tools_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `it_tools_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `it_tools_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`it_tools_name`"

        ```yaml
        # Type: string
        it_tools_name: it-tools
        ```

=== "Web"

    ??? variable string "`it_tools_role_web_subdomain`"

        ```yaml
        # Type: string
        it_tools_role_web_subdomain: "{{ it_tools_name }}"
        ```

    ??? variable string "`it_tools_role_web_domain`"

        ```yaml
        # Type: string
        it_tools_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`it_tools_role_web_port`"

        ```yaml
        # Type: string
        it_tools_role_web_port: "80"
        ```

    ??? variable string "`it_tools_role_web_url`"

        ```yaml
        # Type: string
        it_tools_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='it_tools') + '.' + lookup('role_var', '_web_domain', role='it_tools')
                                if (lookup('role_var', '_web_subdomain', role='it_tools') | length > 0)
                                else lookup('role_var', '_web_domain', role='it_tools')) }}"
        ```

=== "DNS"

    ??? variable string "`it_tools_role_dns_record`"

        ```yaml
        # Type: string
        it_tools_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='it_tools') }}"
        ```

    ??? variable string "`it_tools_role_dns_zone`"

        ```yaml
        # Type: string
        it_tools_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='it_tools') }}"
        ```

    ??? variable bool "`it_tools_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        it_tools_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`it_tools_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        it_tools_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`it_tools_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        it_tools_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`it_tools_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        it_tools_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`it_tools_role_traefik_certresolver`"

        ```yaml
        # Type: string
        it_tools_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`it_tools_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        it_tools_role_traefik_enabled: true
        ```

    ??? variable bool "`it_tools_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        it_tools_role_traefik_api_enabled: false
        ```

    ??? variable string "`it_tools_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        it_tools_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`it_tools_role_docker_container`"

        ```yaml
        # Type: string
        it_tools_role_docker_container: "{{ it_tools_name }}"
        ```

    ##### Image

    ??? variable bool "`it_tools_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        it_tools_role_docker_image_pull: true
        ```

    ??? variable string "`it_tools_role_docker_image_repo`"

        ```yaml
        # Type: string
        it_tools_role_docker_image_repo: "corentinth/it-tools"
        ```

    ??? variable string "`it_tools_role_docker_image_tag`"

        ```yaml
        # Type: string
        it_tools_role_docker_image_tag: "latest"
        ```

    ??? variable string "`it_tools_role_docker_image`"

        ```yaml
        # Type: string
        it_tools_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='it_tools') }}:{{ lookup('role_var', '_docker_image_tag', role='it_tools') }}"
        ```

    ##### Volumes

    ??? variable bool "`it_tools_role_docker_volumes_global`"

        ```yaml
        # Type: bool (true/false)
        it_tools_role_docker_volumes_global: false
        ```

    ##### Hostname

    ??? variable string "`it_tools_role_docker_hostname`"

        ```yaml
        # Type: string
        it_tools_role_docker_hostname: "{{ it_tools_name }}"
        ```

    ##### Networks

    ??? variable string "`it_tools_role_docker_networks_alias`"

        ```yaml
        # Type: string
        it_tools_role_docker_networks_alias: "{{ it_tools_name }}"
        ```

    ??? variable list "`it_tools_role_docker_networks_default`"

        ```yaml
        # Type: list
        it_tools_role_docker_networks_default: []
        ```

    ??? variable list "`it_tools_role_docker_networks_custom`"

        ```yaml
        # Type: list
        it_tools_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`it_tools_role_docker_restart_policy`"

        ```yaml
        # Type: string
        it_tools_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`it_tools_role_docker_state`"

        ```yaml
        # Type: string
        it_tools_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`it_tools_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        it_tools_role_autoheal_enabled: true
        ```

    ??? variable string "`it_tools_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        it_tools_role_depends_on: ""
        ```

    ??? variable string "`it_tools_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        it_tools_role_depends_on_delay: "0"
        ```

    ??? variable string "`it_tools_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        it_tools_role_depends_on_healthchecks:
        ```

    ??? variable bool "`it_tools_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        it_tools_role_diun_enabled: true
        ```

    ??? variable bool "`it_tools_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        it_tools_role_dns_enabled: true
        ```

    ??? variable bool "`it_tools_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        it_tools_role_docker_controller: true
        ```

    ??? variable bool "`it_tools_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        it_tools_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`it_tools_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        it_tools_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`it_tools_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        it_tools_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`it_tools_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        it_tools_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`it_tools_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        it_tools_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`it_tools_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        it_tools_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`it_tools_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        it_tools_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`it_tools_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        it_tools_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`it_tools_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        it_tools_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`it_tools_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        it_tools_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            it_tools_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "it_tools2.{{ user.domain }}"
              - "it_tools.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`it_tools_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        it_tools_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            it_tools_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'it_tools2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`it_tools_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        it_tools_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
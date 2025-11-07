---
icon: material/play
status: WIP
---

# Traefik Template

## Overview

Generates a Docker Compose template with Traefik provisioning.

---

## Deployment

```sh
generate-traefik-template
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    traefik_template_file: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `traefik_template_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `traefik_template_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Settings"

    ??? variable string "`traefik_template_file`"

        ```yaml
        # Type: string
        traefik_template_file: "/tmp/docker-compose.yml"
        ```

=== "Template Variables"

    ??? variable string "`traefik_template_name`"

        ```yaml
        # Type: string
        traefik_template_name: "{{ service_name.user_input | lower }}"
        ```

    ??? variable string "`traefik_template_role_web_subdomain`"

        ```yaml
        # Type: string
        traefik_template_role_web_subdomain: "{{ service_name.user_input | lower }}"
        ```

    ??? variable string "`traefik_template_role_web_domain`"

        ```yaml
        # Type: string
        traefik_template_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`traefik_template_role_web_port`"

        ```yaml
        # Type: string
        traefik_template_role_web_port: "{{ service_port.user_input }}"
        ```

    ??? variable string "`traefik_template_role_traefik_enabled`"

        ```yaml
        # Type: string
        traefik_template_role_traefik_enabled: "true"
        ```

    ??? variable string "`traefik_template_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        traefik_template_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware if (service_sso_enabled.user_input | bool) else '' }}"
        ```

    ??? variable string "`traefik_template_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        traefik_template_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`traefik_template_role_traefik_api_enabled`"

        ```yaml
        # Type: string
        traefik_template_role_traefik_api_enabled: "{{ (service_api_enabled.user_input | default(false) | bool) | default(false) }}"
        ```

    ??? variable string "`traefik_template_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        traefik_template_role_traefik_api_endpoint: "PathPrefix(`/api`)"
        ```

    ??? variable string "`traefik_template_role_docker_network_mode`"

        ```yaml
        # Type: string
        traefik_template_role_docker_network_mode: "{{ service_gluetun_container.user_input if ((service_gluetun_enabled.user_input | lower) | bool) else docker_networks_name_common }}"
        ```

=== "Global Override Options"

    ??? variable bool "`traefik_template_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        traefik_template_role_autoheal_enabled: true
        ```

    ??? variable string "`traefik_template_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        traefik_template_role_depends_on: ""
        ```

    ??? variable string "`traefik_template_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        traefik_template_role_depends_on_delay: "0"
        ```

    ??? variable string "`traefik_template_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        traefik_template_role_depends_on_healthchecks:
        ```

    ??? variable bool "`traefik_template_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        traefik_template_role_diun_enabled: true
        ```

    ??? variable bool "`traefik_template_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        traefik_template_role_dns_enabled: true
        ```

    ??? variable bool "`traefik_template_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        traefik_template_role_docker_controller: true
        ```

    ??? variable bool "`traefik_template_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        traefik_template_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`traefik_template_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        traefik_template_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`traefik_template_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        traefik_template_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`traefik_template_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        traefik_template_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`traefik_template_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        traefik_template_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`traefik_template_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        traefik_template_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`traefik_template_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        traefik_template_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`traefik_template_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        traefik_template_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`traefik_template_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        traefik_template_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`traefik_template_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        traefik_template_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            traefik_template_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "traefik_template2.{{ user.domain }}"
              - "traefik_template.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`traefik_template_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        traefik_template_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            traefik_template_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'traefik_template2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`traefik_template_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        traefik_template_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
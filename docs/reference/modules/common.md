---
icon: material/cogs
status: WIP
---

# Common

## Overview

Sets up common directories, installs essential packages, handles BTRFS optimizations, and configures basic system tools.

---

## Deployment

Saltbox dependency.

```shell
sb install common
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    nano_syntax_highlighting_enabled: true
    ```

=== "General"

    ??? variable bool "`nano_syntax_highlighting_enabled`"

        ```yaml
        # Type: bool (true/false)
        nano_syntax_highlighting_enabled: true
        ```

    ??? variable bool "`common_create_media_subfolders`"

        ```yaml
        # Type: bool (true/false)
        common_create_media_subfolders: true
        ```

=== "Global Override Options"

    ??? variable bool "`common_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        common_role_autoheal_enabled: true
        ```

    ??? variable string "`common_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        common_role_depends_on: ""
        ```

    ??? variable string "`common_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        common_role_depends_on_delay: "0"
        ```

    ??? variable string "`common_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        common_role_depends_on_healthchecks:
        ```

    ??? variable bool "`common_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        common_role_diun_enabled: true
        ```

    ??? variable bool "`common_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        common_role_dns_enabled: true
        ```

    ??? variable bool "`common_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        common_role_docker_controller: true
        ```

    ??? variable bool "`common_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        common_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`common_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        common_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`common_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        common_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`common_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        common_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`common_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        common_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`common_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        common_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`common_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        common_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`common_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        common_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`common_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        common_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`common_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        common_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            common_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "common2.{{ user.domain }}"
              - "common.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`common_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        common_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            common_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'common2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`common_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        common_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
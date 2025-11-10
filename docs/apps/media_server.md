---
icon: material/tag
status: wip
---

# Media Server

## Overview

Ansible tag for deploying your media server apps stack.

---

## Deployment

```sh
sb install media-server
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    media_servers_enabled: ["item1", "item2"]
    ```

=== "General"

    ??? variable list "`media_servers_enabled`"

        ```yaml
        # Type: list
        media_servers_enabled: ["plex"]
        ```

=== "Global Override Options"

    ??? variable bool "`media_server_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        media_server_role_autoheal_enabled: true
        ```

    ??? variable string "`media_server_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        media_server_role_depends_on: ""
        ```

    ??? variable string "`media_server_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        media_server_role_depends_on_delay: "0"
        ```

    ??? variable string "`media_server_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        media_server_role_depends_on_healthchecks:
        ```

    ??? variable bool "`media_server_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        media_server_role_diun_enabled: true
        ```

    ??? variable bool "`media_server_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        media_server_role_dns_enabled: true
        ```

    ??? variable bool "`media_server_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        media_server_role_docker_controller: true
        ```

    ??? variable bool "`media_server_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        media_server_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`media_server_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        media_server_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`media_server_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        media_server_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`media_server_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        media_server_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`media_server_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        media_server_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`media_server_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        media_server_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`media_server_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        media_server_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`media_server_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        media_server_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`media_server_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        media_server_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`media_server_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        media_server_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            media_server_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "media_server2.{{ user.domain }}"
              - "media_server.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`media_server_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        media_server_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            media_server_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'media_server2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`media_server_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        media_server_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
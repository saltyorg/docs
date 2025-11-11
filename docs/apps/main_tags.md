---
icon: material/tag
status: wip
---

# Main Tags

## Overview

Ansible tags for deploying the main role stacks.

---

## Deployment

```sh
sb install saltbox
```

```sh
sb install mediabox
```

```sh
sb install feederbox
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    saltbox_roles: ["item1", "item2"]
    ```

=== "General"

    ??? variable list "`saltbox_roles`"

        ```yaml
        # Type: list
        saltbox_roles: ["media_server", "download_clients", "download_indexers", "autoscan", "tautulli", "overseerr", "portainer", "organizr", "sonarr", "radarr", "lidarr", "iperf3", "glances", "btop"]
        ```

    ??? variable list "`mediabox_roles`"

        ```yaml
        # Type: list
        mediabox_roles: ["media_server", "autoscan", "tautulli", "overseerr", "iperf3", "glances", "btop"]
        ```

    ??? variable list "`feederbox_roles`"

        ```yaml
        # Type: list
        feederbox_roles: ["download_clients", "download_indexers", "portainer", "organizr", "sonarr", "radarr", "lidarr", "iperf3", "glances", "btop"]
        ```

=== "Global Override Options"

    ??? variable bool "`main_tags_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        main_tags_role_autoheal_enabled: true
        ```

    ??? variable string "`main_tags_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        main_tags_role_depends_on: ""
        ```

    ??? variable string "`main_tags_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        main_tags_role_depends_on_delay: "0"
        ```

    ??? variable string "`main_tags_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        main_tags_role_depends_on_healthchecks:
        ```

    ??? variable bool "`main_tags_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        main_tags_role_diun_enabled: true
        ```

    ??? variable bool "`main_tags_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        main_tags_role_dns_enabled: true
        ```

    ??? variable bool "`main_tags_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        main_tags_role_docker_controller: true
        ```

    ??? variable bool "`main_tags_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        main_tags_role_docker_volumes_download:
        ```

    ??? variable bool "`main_tags_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        main_tags_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`main_tags_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        main_tags_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`main_tags_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        main_tags_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`main_tags_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        main_tags_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`main_tags_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        main_tags_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`main_tags_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        main_tags_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`main_tags_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        main_tags_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`main_tags_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        main_tags_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`main_tags_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        main_tags_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`main_tags_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        main_tags_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            main_tags_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "main_tags2.{{ user.domain }}"
              - "main_tags.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`main_tags_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        main_tags_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            main_tags_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'main_tags2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`main_tags_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        main_tags_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
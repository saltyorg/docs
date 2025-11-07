---
icon: material/server-network-outline
status: WIP
---

# Crowdsec

## Overview

CrowdSec is a free, open-source, and collaborative security automation platform designed to protect servers, services, containers, and virtual machines from cyberattacks by analyzing system logs and HTTP requests for malicious behavior.

---

## Deployment

Opt in via Inventory toggle.

```sh
sb install crowdsec
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    crowdsec_enabled: true
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `crowdsec_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `crowdsec_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Toggle"

    ??? variable bool "`crowdsec_enabled`"

        ```yaml
        # Type: bool (true/false)
        crowdsec_enabled: false
        ```

=== "Configuration"

    ??? variable string "`crowdsec_console_enrollment_key`"

        ```yaml
        # Type: string
        crowdsec_console_enrollment_key: ""
        ```

    ??? variable list "`crowdsec_collections_install_default`"

        ```yaml
        # Type: list
        crowdsec_collections_install_default: 
          - "crowdsecurity/linux"
          - "crowdsecurity/iptables"
          - "crowdsecurity/sshd"
          - "crowdsecurity/whitelist-good-actors"
          - "crowdsecurity/traefik"
          - "crowdsecurity/plex"
        ```

    ??? variable list "`crowdsec_collections_install_custom`"

        ```yaml
        # Type: list
        crowdsec_collections_install_custom: []
        ```

    ??? variable list "`crowdsec_collections_remove_default`"

        ```yaml
        # Type: list
        crowdsec_collections_remove_default: []
        ```

    ??? variable list "`crowdsec_collections_remove_custom`"

        ```yaml
        # Type: list
        crowdsec_collections_remove_custom: []
        ```

    ??? variable list "`crowdsec_scenarios_install_default`"

        ```yaml
        # Type: list
        crowdsec_scenarios_install_default: []
        ```

    ??? variable list "`crowdsec_scenarios_install_custom`"

        ```yaml
        # Type: list
        crowdsec_scenarios_install_custom: []
        ```

    ??? variable list "`crowdsec_scenarios_remove_default`"

        ```yaml
        # Type: list
        crowdsec_scenarios_remove_default: 
          - "crowdsecurity/http-crawl-non_statics"
          - "crowdsecurity/http-probing"
        ```

    ??? variable list "`crowdsec_scenarios_remove_custom`"

        ```yaml
        # Type: list
        crowdsec_scenarios_remove_custom: []
        ```

    ??? variable list "`crowdsec_parsers_install_default`"

        ```yaml
        # Type: list
        crowdsec_parsers_install_default: []
        ```

    ??? variable list "`crowdsec_parsers_install_custom`"

        ```yaml
        # Type: list
        crowdsec_parsers_install_custom: []
        ```

    ??? variable list "`crowdsec_parsers_remove_default`"

        ```yaml
        # Type: list
        crowdsec_parsers_remove_default: []
        ```

    ??? variable list "`crowdsec_parsers_remove_custom`"

        ```yaml
        # Type: list
        crowdsec_parsers_remove_custom: []
        ```

    ??? variable list "`crowdsec_postoverflows_install_default`"

        ```yaml
        # Type: list
        crowdsec_postoverflows_install_default: []
        ```

    ??? variable list "`crowdsec_postoverflows_install_custom`"

        ```yaml
        # Type: list
        crowdsec_postoverflows_install_custom: []
        ```

    ??? variable list "`crowdsec_postoverflows_remove_default`"

        ```yaml
        # Type: list
        crowdsec_postoverflows_remove_default: []
        ```

    ??? variable list "`crowdsec_postoverflows_remove_custom`"

        ```yaml
        # Type: list
        crowdsec_postoverflows_remove_custom: []
        ```

    ??? variable bool "`crowdsec_prometheus_enabled`"

        ```yaml
        # Type: bool (true/false)
        crowdsec_prometheus_enabled: false
        ```

    ??? variable string "`crowdsec_prometheus_level`"

        ```yaml
        # Type: string
        crowdsec_prometheus_level: "full"
        ```

    ??? variable string "`crowdsec_prometheus_listen_addr`"

        ```yaml
        # Type: string
        crowdsec_prometheus_listen_addr: "172.19.0.1"
        ```

    ??? variable string "`crowdsec_prometheus_listen_port`"

        ```yaml
        # Type: string
        crowdsec_prometheus_listen_port: "6060"
        ```

    ??? variable list "`crowdsec_whitelisted_routers`"

        ```yaml
        # Takes a list of exact router names to ignore when parsing Traefik access logs.
        # Include @file or @docker depending on the source of said router:
        # authelia@docker
        # authelia-http@docker
        # Remember to include api/http routers as well if needed.
        # Type: list
        crowdsec_whitelisted_routers: []
        ```

    ??? variable list "`crowdsec_whitelisted_ips`"

        ```yaml
        # Takes list of specific IPs
        # Type: list
        crowdsec_whitelisted_ips: []
        ```

    ??? variable list "`crowdsec_whitelisted_cidrs`"

        ```yaml
        # Takes list of CIDR notation IP ranges
        # Type: list
        crowdsec_whitelisted_cidrs: []
        ```

=== "Lookups"

    ??? variable string "`crowdsec_ports_8080`"

        ```yaml
        # Type: string
        crowdsec_ports_8080: "{{ port_lookup_8080.meta.port
                              if (port_lookup_8080.meta.port is defined) and (port_lookup_8080.meta.port | trim | length > 0)
                              else '8080' }}"
        ```

=== "Bouncers"

    ??? variable string "`crowdsec_bouncer_traefik_path`"

        ```yaml
        # Type: string
        crowdsec_bouncer_traefik_path: "/etc/crowdsec/bouncers/traefik.txt"
        ```

    ??? variable string "`crowdsec_bouncer_traefik_name`"

        ```yaml
        # Type: string
        crowdsec_bouncer_traefik_name: "traefik"
        ```

=== "Global Override Options"

    ??? variable bool "`crowdsec_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        crowdsec_role_autoheal_enabled: true
        ```

    ??? variable string "`crowdsec_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        crowdsec_role_depends_on: ""
        ```

    ??? variable string "`crowdsec_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        crowdsec_role_depends_on_delay: "0"
        ```

    ??? variable string "`crowdsec_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        crowdsec_role_depends_on_healthchecks:
        ```

    ??? variable bool "`crowdsec_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        crowdsec_role_diun_enabled: true
        ```

    ??? variable bool "`crowdsec_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        crowdsec_role_dns_enabled: true
        ```

    ??? variable bool "`crowdsec_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        crowdsec_role_docker_controller: true
        ```

    ??? variable bool "`crowdsec_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        crowdsec_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`crowdsec_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        crowdsec_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`crowdsec_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        crowdsec_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`crowdsec_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        crowdsec_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`crowdsec_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        crowdsec_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`crowdsec_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        crowdsec_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`crowdsec_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        crowdsec_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`crowdsec_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        crowdsec_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`crowdsec_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        crowdsec_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`crowdsec_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        crowdsec_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            crowdsec_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "crowdsec2.{{ user.domain }}"
              - "crowdsec.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`crowdsec_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        crowdsec_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            crowdsec_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'crowdsec2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`crowdsec_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        crowdsec_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
icon: material/server-network-outline
status: wip
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
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
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
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
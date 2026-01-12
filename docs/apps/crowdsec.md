---
icon: material/server-network-outline
title: CrowdSec
status: draft
saltbox_automation:
  inventory:
    show_sections:
    - Toggle
    - Configuration
  app_links:
  - name: Manual
    url:
    type: documentation
  - name: Releases
    url:
    type: releases
  - name: Community
    url:
    type: community
  project_description:
    name: CrowdSec Security Engine
    summary: |
      a powerful, open source solution for detecting and blocking malicious IPs, safeguarding both infrastructure and application security.
    link: https://www.crowdsec.net/security-engine
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# CrowdSec Security Engine

## Overview

[CrowdSec Security Engine](https://www.crowdsec.net/security-engine) is a powerful, open source solution for detecting and blocking malicious IPs, safeguarding both infrastructure and application security.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](){ .md-button .md-button--stretch }

[:fontawesome-solid-newspaper:**Releases**](){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

Opt in via Inventory toggle.

```shell
sb install crowdsec
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        crowdsec_enabled: true
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

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
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
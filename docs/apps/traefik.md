---
icon: material/docker
title: Traefik Proxy
status: draft
saltbox_automation:
  inventory:
    show_sections:
      - Basics
      - Config
      - Web
      - Logging
  app_links:
    - name: Manual
      url: https://doc.traefik.io/traefik
      type: documentation
    - name: Releases
      url: https://hub.docker.com/_/traefik/tags
      type: docker
    - name: Community
      url: https://community.traefik.io
      type: community
  project_description:
    name: Traefik Proxy
    summary: |
      an open-source, dynamic reverse proxy and load balancer designed for modern, distributed, and microservices architectures.
    link: https://traefik.io/traefik
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Traefik Proxy

## Overview

[Traefik Proxy](https://traefik.io/traefik) is an open-source, dynamic reverse proxy and load balancer designed for modern, distributed, and microservices architectures.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://doc.traefik.io/traefik){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/_/traefik/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](https://community.traefik.io){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

Saltbox dependency.

```shell
sb install traefik
```

## Usage

Visit <https://dash.iYOUR_DOMAIN_NAMEi>.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        traefik_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `traefik_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `traefik_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`traefik_name`"

        ```yaml
        # Type: string
        traefik_name: traefik
        ```

=== "Config"

    ??? variable string "`traefik_trusted_ips`"

        ```yaml
        # Type: string
        traefik_trusted_ips: ""
        ```

    ??? variable bool "`traefik_plugin_cloudflarewarp_enabled`"

        ```yaml
        # Type: bool (true/false)
        traefik_plugin_cloudflarewarp_enabled: true
        ```

    ??? variable string "`traefik_file_watch`"

        ```yaml
        # Type: string
        traefik_file_watch: "true"
        ```

    ??? variable string "`traefik_x_robots`"

        ```yaml
        # Type: string
        traefik_x_robots: "none,noarchive,nosnippet,notranslate,noimageindex"
        ```

    ??? variable bool "`traefik_http3`"

        ```yaml
        # HTTP3 can cause issues with some apps
        # Type: bool (true/false)
        traefik_http3: false
        ```

    ??? variable bool "`traefik_tailscale_enabled`"

        ```yaml
        # Type: bool (true/false)
        traefik_tailscale_enabled: false
        ```

    ??? variable string "`traefik_entrypoint_web_port`"

        ```yaml
        # traefik_tailscale_bind_ip: "" # Set to override the WAN IP port binding when server is not connected directly to the Internet.
        # traefik_tailscale_bind_ipv6: "" # Same but IPv6
        # Type: string
        traefik_entrypoint_web_port: "80"
        ```

    ??? variable string "`traefik_entrypoint_web_readtimeout`"

        ```yaml
        # Type: string
        traefik_entrypoint_web_readtimeout: "600"
        ```

    ??? variable string "`traefik_entrypoint_web_writetimeout`"

        ```yaml
        # Type: string
        traefik_entrypoint_web_writetimeout: "0"
        ```

    ??? variable string "`traefik_entrypoint_web_idletimeout`"

        ```yaml
        # Type: string
        traefik_entrypoint_web_idletimeout: "180"
        ```

    ??? variable string "`traefik_entrypoint_web_request_maxheaderbytes`"

        ```yaml
        # Type: string
        traefik_entrypoint_web_request_maxheaderbytes: "1048576"
        ```

    ??? variable string "`traefik_entrypoint_websecure_port`"

        ```yaml
        # Type: string
        traefik_entrypoint_websecure_port: "443"
        ```

    ??? variable string "`traefik_entrypoint_websecure_readtimeout`"

        ```yaml
        # Type: string
        traefik_entrypoint_websecure_readtimeout: "600"
        ```

    ??? variable string "`traefik_entrypoint_websecure_writetimeout`"

        ```yaml
        # Type: string
        traefik_entrypoint_websecure_writetimeout: "0"
        ```

    ??? variable string "`traefik_entrypoint_websecure_idletimeout`"

        ```yaml
        # Type: string
        traefik_entrypoint_websecure_idletimeout: "180"
        ```

    ??? variable string "`traefik_entrypoint_websecure_request_maxheaderbytes`"

        ```yaml
        # Type: string
        traefik_entrypoint_websecure_request_maxheaderbytes: "1048576"
        ```

    ??? variable dict "`traefik_entrypoint_custom`"

        ```yaml
        # Type: dict
        traefik_entrypoint_custom: {}
        ```

    ??? variable string "`traefik_dns_resolvers`"

        ```yaml
        # Format is as follows (address can be empty string "" to bind on every interface):
        # Type options are tcp, udp or both.
        # traefik_entrypoint_custom:
        # tcp-entrypoint:
        # address: "IP"
        # port: "81"
        # tls: false
        # type: tcp
        # tcp-and-udp-entrypoint-with-tls:
        # address: "IP"
        # port: "444"
        # tls: true
        # type: both
        # Type: string
        traefik_dns_resolvers: "1.1.1.1:53,1.0.0.1:53"
        ```

    ??? variable bool "`traefik_disable_propagation_check`"

        ```yaml
        # Type: bool (true/false)
        traefik_disable_propagation_check: false
        ```

    ??? variable string "`traefik_enable_http_validation`"

        ```yaml
        # Type: string
        traefik_enable_http_validation: "{{ traefik_http or (traefik.cert.http_validation | bool) }}"
        ```

    ??? variable bool "`traefik_enable_zerossl`"

        ```yaml
        # Type: bool (true/false)
        traefik_enable_zerossl: true
        ```

    ??? variable string "`traefik_crowdsec_ban_filepath`"

        ```yaml
        # Path is internal to the container, so a host path of /opt/traefik/ban.html becomes /etc/traefik/ban.html
        # Type: string
        traefik_crowdsec_ban_filepath: "/etc/traefik/ban.html"
        ```

    ??? variable bool "`traefik_sanitize_path`"

        ```yaml
        # Entrypoint Path Sanitization Settings
        # Type: bool (true/false)
        traefik_sanitize_path: true
        ```

    ??? variable bool "`traefik_encoded_allow_slash`"

        ```yaml
        # Entrypoint Encoded characters settings (applied to all entrypoints)
        # Type: bool (true/false)
        traefik_encoded_allow_slash: true
        ```

    ??? variable bool "`traefik_encoded_allow_backslash`"

        ```yaml
        # Type: bool (true/false)
        traefik_encoded_allow_backslash: true
        ```

    ??? variable bool "`traefik_encoded_allow_null`"

        ```yaml
        # Type: bool (true/false)
        traefik_encoded_allow_null: true
        ```

    ??? variable bool "`traefik_encoded_allow_semicolon`"

        ```yaml
        # Type: bool (true/false)
        traefik_encoded_allow_semicolon: true
        ```

    ??? variable bool "`traefik_encoded_allow_percent`"

        ```yaml
        # Type: bool (true/false)
        traefik_encoded_allow_percent: true
        ```

    ??? variable bool "`traefik_encoded_allow_question_mark`"

        ```yaml
        # Type: bool (true/false)
        traefik_encoded_allow_question_mark: true
        ```

    ??? variable bool "`traefik_encoded_allow_hash`"

        ```yaml
        # Type: bool (true/false)
        traefik_encoded_allow_hash: true
        ```

=== "Web"

    ??? variable string "`traefik_role_web_subdomain`"

        ```yaml
        # Type: string
        traefik_role_web_subdomain: "{{ traefik.subdomains.dash }}"
        ```

    ??? variable string "`traefik_role_web_domain`"

        ```yaml
        # Type: string
        traefik_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`traefik_role_metrics_subdomain`"

        ```yaml
        # Type: string
        traefik_role_metrics_subdomain: "{{ traefik.subdomains.metrics }}"
        ```

    ??? variable string "`traefik_role_metrics_domain`"

        ```yaml
        # Type: string
        traefik_role_metrics_domain: "{{ user.domain }}"
        ```

=== "Logging"

    ??? variable string "`traefik_role_log_level`"

        ```yaml
        # Type: string
        traefik_role_log_level: "ERROR"
        ```

    ??? variable bool "`traefik_role_log_file`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_log_file: true
        ```

    ??? variable string "`traefik_role_log_max_size`"

        ```yaml
        # Type: string
        traefik_role_log_max_size: "10"
        ```

    ??? variable string "`traefik_role_log_max_backups`"

        ```yaml
        # Type: string
        traefik_role_log_max_backups: "3"
        ```

    ??? variable string "`traefik_role_log_max_age`"

        ```yaml
        # Type: string
        traefik_role_log_max_age: "3"
        ```

    ??? variable string "`traefik_role_log_compress`"

        ```yaml
        # Type: string
        traefik_role_log_compress: "true"
        ```

    ??? variable bool "`traefik_role_access_log`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_access_log: true
        ```

    ??? variable int "`traefik_role_access_buffer`"

        ```yaml
        # Type: int
        traefik_role_access_buffer: 100
        ```

=== "Global Override Options"

    ??? variable bool "`traefik_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        traefik_role_autoheal_enabled: true
        ```

    ??? variable string "`traefik_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        traefik_role_depends_on: ""
        ```

    ??? variable string "`traefik_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        traefik_role_depends_on_delay: "0"
        ```

    ??? variable string "`traefik_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        traefik_role_depends_on_healthchecks:
        ```

    ??? variable bool "`traefik_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        traefik_role_diun_enabled: true
        ```

    ??? variable bool "`traefik_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        traefik_role_dns_enabled: true
        ```

    ??? variable bool "`traefik_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        traefik_role_docker_controller: true
        ```

    ??? variable bool "`traefik_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_docker_volumes_download:
        ```

    ??? variable string "`traefik_role_themepark_addons`"

        ```yaml
        # Type: string
        traefik_role_themepark_addons:
        ```

    ??? variable string "`traefik_role_themepark_app`"

        ```yaml
        # Type: string
        traefik_role_themepark_app:
        ```

    ??? variable string "`traefik_role_themepark_theme`"

        ```yaml
        # Type: string
        traefik_role_themepark_theme:
        ```

    ??? variable dict "`traefik_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        traefik_role_traefik_api_endpoint:
        ```

    ??? variable string "`traefik_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        traefik_role_traefik_api_middleware:
        ```

    ??? variable string "`traefik_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        traefik_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`traefik_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        traefik_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`traefik_role_traefik_certresolver`"

        ```yaml
        # Type: string
        traefik_role_traefik_certresolver:
        ```

    ??? variable bool "`traefik_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        traefik_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`traefik_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        traefik_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`traefik_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        traefik_role_traefik_gzip_enabled: false
        ```

    ??? variable string "`traefik_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        traefik_role_traefik_middleware_http:
        ```

    ??? variable bool "`traefik_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`traefik_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        traefik_role_traefik_middleware_http_insecure:
        ```

    ??? variable string "`traefik_role_traefik_priority`"

        ```yaml
        # Type: string
        traefik_role_traefik_priority:
        ```

    ??? variable bool "`traefik_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        traefik_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`traefik_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        traefik_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`traefik_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        traefik_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`traefik_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        traefik_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            traefik_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "traefik2.{{ user.domain }}"
              - "traefik.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries


    ??? variable string "`traefik_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        traefik_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            traefik_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'traefik2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`traefik_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        traefik_role_web_http_port:
        ```

    ??? variable string "`traefik_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        traefik_role_web_http_scheme:
        ```

    ??? variable dict "`traefik_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        traefik_role_web_http_serverstransport:
        ```

    ??? variable string "`traefik_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        traefik_role_web_scheme:
        ```

    ??? variable dict "`traefik_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        traefik_role_web_serverstransport:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
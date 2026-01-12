---
icon: material/server-network-outline
hide:
  - tags
tags:
  - cockpit
  - server
  - administration
saltbox_automation:
  app_links:
    - name: Manual
      url: https://cockpit-project.org/documentation.html
      type: documentation
    - name: Releases
      url:
      type: releases
    - name: Community
      url:
      type: community
  project_description:
    name: Cockpit
    summary: |
      an interactive server admin interface that makes Linux servers discoverable and manageable through a web browser, providing comprehensive server management capabilities with a modern web interface.
    link: https://cockpit-project.org
---

<!-- BEGIN SALTBOX MANAGED OVERVIEW SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
# Cockpit

## Overview

[Cockpit](https://cockpit-project.org) is an interactive server admin interface that makes Linux servers discoverable and manageable through a web browser, providing comprehensive server management capabilities with a modern web interface.

<div class="grid grid--buttons" markdown data-search-exclude>

[:fontawesome-solid-book-open:**Manual**](https://cockpit-project.org/documentation.html){ .md-button .md-button--stretch }

[:fontawesome-solid-newspaper:**Releases**](){ .md-button .md-button--stretch }

[:fontawesome-solid-comments:**Community**](){ .md-button .md-button--stretch }

</div>

---
<!-- END SALTBOX MANAGED OVERVIEW SECTION -->

## Deployment

```shell
sb install sandbox-cockpit
```

## Usage

Visit <https://cockpit.iYOUR_DOMAIN_NAMEi>.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults

Variables can be customized using the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview }. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  !!! example "Example override"

        ```yaml
        cockpit_name: "custom_value"
        ```

    !!! warning "Avoid overriding variables ending in `_default`"

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

    ??? variable bool "`cockpit_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        cockpit_role_dns_enabled: true
        ```

    ??? variable string "`cockpit_role_themepark_addons`"

        ```yaml
        # Type: string
        cockpit_role_themepark_addons:
        ```

    ??? variable string "`cockpit_role_themepark_app`"

        ```yaml
        # Type: string
        cockpit_role_themepark_app:
        ```

    ??? variable string "`cockpit_role_themepark_theme`"

        ```yaml
        # Type: string
        cockpit_role_themepark_theme:
        ```

    ??? variable dict "`cockpit_role_traefik_api_endpoint`"

        ```yaml
        # Type: dict/omit
        cockpit_role_traefik_api_endpoint:
        ```

    ??? variable string "`cockpit_role_traefik_api_middleware`"

        ```yaml
        # Type: string
        cockpit_role_traefik_api_middleware:
        ```

    ??? variable string "`cockpit_role_traefik_api_middleware_http`"

        ```yaml
        # Type: string
        cockpit_role_traefik_api_middleware_http:
        ```

    ??? variable bool "`cockpit_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        cockpit_role_traefik_autodetect_enabled: false
        ```

    ??? variable string "`cockpit_role_traefik_certresolver`"

        ```yaml
        # Type: string
        cockpit_role_traefik_certresolver:
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

    ??? variable string "`cockpit_role_traefik_middleware_http`"

        ```yaml
        # Type: string
        cockpit_role_traefik_middleware_http:
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

    ??? variable string "`cockpit_role_traefik_priority`"

        ```yaml
        # Type: string
        cockpit_role_traefik_priority:
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

    ??? variable string "`cockpit_role_web_domain`"

        ```yaml
        # Type: string
        cockpit_role_web_domain:
        ```

    ??? variable list "`cockpit_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        cockpit_role_web_fqdn_override:
        ```

        !!! example "Example Override"

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
        cockpit_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            cockpit_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'cockpit2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule


    ??? variable string "`cockpit_role_web_http_port`"

        ```yaml
        # Type: string (quoted number)
        cockpit_role_web_http_port:
        ```

    ??? variable string "`cockpit_role_web_http_scheme`"

        ```yaml
        # Type: string ("http"/"https")
        cockpit_role_web_http_scheme:
        ```

    ??? variable dict "`cockpit_role_web_http_serverstransport`"

        ```yaml
        # Type: dict/omit
        cockpit_role_web_http_serverstransport:
        ```

    ??? variable string "`cockpit_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        cockpit_role_web_scheme:
        ```

    ??? variable dict "`cockpit_role_web_serverstransport`"

        ```yaml
        # Type: dict/omit
        cockpit_role_web_serverstransport:
        ```

    ??? variable string "`cockpit_role_web_subdomain`"

        ```yaml
        # Type: string
        cockpit_role_web_subdomain:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
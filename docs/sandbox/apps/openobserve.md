---
hide:
  - tags
tags:
  - openobserve
  - observability
  - logs
---

# OpenObserve

## What is it?

[OpenObserve](https://openobserve.ai/) is an open-source observability platform for logs, metrics, and traces with 140x lower storage cost than Elasticsearch. Built for petabyte scale with high performance and ~40x compression.

!!! info
    By default, the role is **NOT** protected behind your Authelia/SSO middleware. You will need to configure authentication within the application.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://openobserve.ai/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/openobserve/openobserve){: .header-icons } | [:octicons-link-16: Docs](https://openobserve.ai/docs/){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-openobserve
```

### 2. URL

- To access OpenObserve, visit `https://openobserve._yourdomain.com_`

### 3. Setup

Default credentials are configured using your user email and password. Root user setup is required for initial access.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    openobserve_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `openobserve_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `openobserve_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`openobserve_name`"

        ```yaml
        # Type: string
        openobserve_name: openobserve
        ```

=== "Paths"

    ??? variable string "`openobserve_role_paths_folder`"

        ```yaml
        # Type: string
        openobserve_role_paths_folder: "{{ openobserve_name }}"
        ```

    ??? variable string "`openobserve_role_paths_location`"

        ```yaml
        # Type: string
        openobserve_role_paths_location: "{{ server_appdata_path }}/{{ openobserve_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`openobserve_role_web_subdomain`"

        ```yaml
        # Type: string
        openobserve_role_web_subdomain: "{{ openobserve_name }}"
        ```

    ??? variable string "`openobserve_role_web_domain`"

        ```yaml
        # Type: string
        openobserve_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`openobserve_role_web_port`"

        ```yaml
        # Type: string
        openobserve_role_web_port: "5080"
        ```

    ??? variable string "`openobserve_role_web_url`"

        ```yaml
        # Type: string
        openobserve_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='openobserve') + '.' + lookup('role_var', '_web_domain', role='openobserve')
                                   if (lookup('role_var', '_web_subdomain', role='openobserve') | length > 0)
                                   else lookup('role_var', '_web_domain', role='openobserve')) }}"
        ```

=== "DNS"

    ??? variable string "`openobserve_role_dns_record`"

        ```yaml
        # Type: string
        openobserve_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='openobserve') }}"
        ```

    ??? variable string "`openobserve_role_dns_zone`"

        ```yaml
        # Type: string
        openobserve_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='openobserve') }}"
        ```

    ??? variable bool "`openobserve_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        openobserve_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`openobserve_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        openobserve_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`openobserve_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        openobserve_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`openobserve_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        openobserve_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`openobserve_role_traefik_certresolver`"

        ```yaml
        # Type: string
        openobserve_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`openobserve_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        openobserve_role_traefik_enabled: true
        ```

    ??? variable bool "`openobserve_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        openobserve_role_traefik_api_enabled: false
        ```

    ??? variable string "`openobserve_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        openobserve_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    Container
    { .sb-h5 }

    ??? variable string "`openobserve_role_docker_container`"

        ```yaml
        # Type: string
        openobserve_role_docker_container: "{{ openobserve_name }}"
        ```

    Image
    { .sb-h5 }

    ??? variable bool "`openobserve_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        openobserve_role_docker_image_pull: true
        ```

    ??? variable string "`openobserve_role_docker_image_tag`"

        ```yaml
        # Type: string
        openobserve_role_docker_image_tag: "latest"
        ```

    ??? variable string "`openobserve_role_docker_image_repo`"

        ```yaml
        # Type: string
        openobserve_role_docker_image_repo: "public.ecr.aws/zinclabs/openobserve"
        ```

    ??? variable string "`openobserve_role_docker_image`"

        ```yaml
        # Type: string
        openobserve_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='openobserve') }}:{{ lookup('role_var', '_docker_image_tag', role='openobserve') }}"
        ```

    Envs
    { .sb-h5 }

    ??? variable dict "`openobserve_role_docker_envs_default`"

        ```yaml
        # Type: dict
        openobserve_role_docker_envs_default: 
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          ZO_ROOT_USER_EMAIL: "{{ user.email }}"
          ZO_ROOT_USER_PASSWORD: "{{ user.pass }}"
        ```

    ??? variable dict "`openobserve_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        openobserve_role_docker_envs_custom: {}
        ```

    Volumes
    { .sb-h5 }

    ??? variable list "`openobserve_role_docker_volumes_default`"

        ```yaml
        # Type: list
        openobserve_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='openobserve') }}:/data"
        ```

    ??? variable list "`openobserve_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        openobserve_role_docker_volumes_custom: []
        ```

    Hostname
    { .sb-h5 }

    ??? variable string "`openobserve_role_docker_hostname`"

        ```yaml
        # Type: string
        openobserve_role_docker_hostname: "{{ openobserve_name }}"
        ```

    Networks
    { .sb-h5 }

    ??? variable string "`openobserve_role_docker_networks_alias`"

        ```yaml
        # Type: string
        openobserve_role_docker_networks_alias: "{{ openobserve_name }}"
        ```

    ??? variable list "`openobserve_role_docker_networks_default`"

        ```yaml
        # Type: list
        openobserve_role_docker_networks_default: []
        ```

    ??? variable list "`openobserve_role_docker_networks_custom`"

        ```yaml
        # Type: list
        openobserve_role_docker_networks_custom: []
        ```

    Restart Policy
    { .sb-h5 }

    ??? variable string "`openobserve_role_docker_restart_policy`"

        ```yaml
        # Type: string
        openobserve_role_docker_restart_policy: unless-stopped
        ```

    State
    { .sb-h5 }

    ??? variable string "`openobserve_role_docker_state`"

        ```yaml
        # Type: string
        openobserve_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`openobserve_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        openobserve_role_autoheal_enabled: true
        ```

    ??? variable string "`openobserve_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        openobserve_role_depends_on: ""
        ```

    ??? variable string "`openobserve_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        openobserve_role_depends_on_delay: "0"
        ```

    ??? variable string "`openobserve_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        openobserve_role_depends_on_healthchecks:
        ```

    ??? variable bool "`openobserve_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        openobserve_role_diun_enabled: true
        ```

    ??? variable bool "`openobserve_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        openobserve_role_dns_enabled: true
        ```

    ??? variable bool "`openobserve_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        openobserve_role_docker_controller: true
        ```

    ??? variable bool "`openobserve_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        openobserve_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`openobserve_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        openobserve_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`openobserve_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        openobserve_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`openobserve_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        openobserve_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`openobserve_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        openobserve_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`openobserve_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        openobserve_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`openobserve_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        openobserve_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`openobserve_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        openobserve_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`openobserve_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        openobserve_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`openobserve_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        openobserve_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            openobserve_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "openobserve2.{{ user.domain }}"
              - "openobserve.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`openobserve_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        openobserve_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            openobserve_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'openobserve2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`openobserve_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        openobserve_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
hide:
  - tags
tags:
  - flaresolverr
  - networking
  - proxy
---

# FlareSolverr

## What is it?

[FlareSolverr](https://github.com/FlareSolverr/FlareSolverr) is a proxy server to bypass Cloudflare protection.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/FlareSolverr/FlareSolverr){: .header-icons } | [:octicons-link-16: Docs](https://github.com/FlareSolverr/FlareSolverr){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/FlareSolverr/FlareSolverr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/flaresolverr/flaresolverr){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-flaresolverr

```

### 2. Setup

#### Jackett

- Locate the _FlareSolverr API URL_ field in the main page.
- Input `http://flaresolverr:8191` and apply the settings.

#### Prowlarr

- In the settings, add an Indexer Proxy and select FlareSolverr.
- _Host_ should be `http://flaresolverr:8191`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    flaresolverr_role_docker_image_tag: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `flaresolverr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `flaresolverr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`flaresolverr_name`"

        ```yaml
        # Type: string
        flaresolverr_name: flaresolverr
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`flaresolverr_role_docker_container`"

        ```yaml
        # Type: string
        flaresolverr_role_docker_container: "{{ flaresolverr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`flaresolverr_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        flaresolverr_role_docker_image_pull: true
        ```

    ??? variable string "`flaresolverr_role_docker_image_repo`"

        ```yaml
        # Type: string
        flaresolverr_role_docker_image_repo: "ghcr.io/flaresolverr/flaresolverr"
        ```

    ??? variable string "`flaresolverr_role_docker_image_tag`"

        ```yaml
        # Type: string
        flaresolverr_role_docker_image_tag: "latest"
        ```

    ??? variable string "`flaresolverr_role_docker_image`"

        ```yaml
        # Type: string
        flaresolverr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='flaresolverr') }}:{{ lookup('role_var', '_docker_image_tag', role='flaresolverr') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`flaresolverr_role_docker_envs_default`"

        ```yaml
        # Type: dict
        flaresolverr_role_docker_envs_default: 
          LOG_LEVEL: "info"
          LOG_HTML: "false"
          CAPTCHA_SOLVER: "hcaptcha-solver"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`flaresolverr_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        flaresolverr_role_docker_envs_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`flaresolverr_role_docker_hostname`"

        ```yaml
        # Type: string
        flaresolverr_role_docker_hostname: "{{ flaresolverr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`flaresolverr_role_docker_networks_alias`"

        ```yaml
        # Type: string
        flaresolverr_role_docker_networks_alias: "{{ flaresolverr_name }}"
        ```

    ??? variable list "`flaresolverr_role_docker_networks_default`"

        ```yaml
        # Type: list
        flaresolverr_role_docker_networks_default: []
        ```

    ??? variable list "`flaresolverr_role_docker_networks_custom`"

        ```yaml
        # Type: list
        flaresolverr_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`flaresolverr_role_docker_restart_policy`"

        ```yaml
        # Type: string
        flaresolverr_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`flaresolverr_role_docker_state`"

        ```yaml
        # Type: string
        flaresolverr_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`flaresolverr_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        flaresolverr_role_autoheal_enabled: true
        ```

    ??? variable string "`flaresolverr_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        flaresolverr_role_depends_on: ""
        ```

    ??? variable string "`flaresolverr_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        flaresolverr_role_depends_on_delay: "0"
        ```

    ??? variable string "`flaresolverr_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        flaresolverr_role_depends_on_healthchecks:
        ```

    ??? variable bool "`flaresolverr_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        flaresolverr_role_diun_enabled: true
        ```

    ??? variable bool "`flaresolverr_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        flaresolverr_role_dns_enabled: true
        ```

    ??? variable bool "`flaresolverr_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        flaresolverr_role_docker_controller: true
        ```

    ??? variable bool "`flaresolverr_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        flaresolverr_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`flaresolverr_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        flaresolverr_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`flaresolverr_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        flaresolverr_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`flaresolverr_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        flaresolverr_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`flaresolverr_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        flaresolverr_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`flaresolverr_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        flaresolverr_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`flaresolverr_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        flaresolverr_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`flaresolverr_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        flaresolverr_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`flaresolverr_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        flaresolverr_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`flaresolverr_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        flaresolverr_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            flaresolverr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "flaresolverr2.{{ user.domain }}"
              - "flaresolverr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`flaresolverr_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        flaresolverr_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            flaresolverr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'flaresolverr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`flaresolverr_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        flaresolverr_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
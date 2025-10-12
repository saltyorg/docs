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

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        flaresolverr_role_docker_image_tag: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `flaresolverr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `flaresolverr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    flaresolverr_name: flaresolverr

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    flaresolverr_role_docker_container: "{{ flaresolverr_name }}"

    # Image
    # Type: bool (true/false)
    flaresolverr_role_docker_image_pull: true

    # Type: string
    flaresolverr_role_docker_image_repo: "ghcr.io/flaresolverr/flaresolverr"

    # Type: string
    flaresolverr_role_docker_image_tag: "latest"

    # Type: string
    flaresolverr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='flaresolverr') }}:{{ lookup('role_var', '_docker_image_tag', role='flaresolverr') }}"

    # Envs
    # Type: dict
    flaresolverr_role_docker_envs_default: 
      LOG_LEVEL: "info"
      LOG_HTML: "false"
      CAPTCHA_SOLVER: "hcaptcha-solver"
      TZ: "{{ tz }}"

    # Type: dict
    flaresolverr_role_docker_envs_custom: {}

    # Hostname
    # Type: string
    flaresolverr_role_docker_hostname: "{{ flaresolverr_name }}"

    # Networks
    # Type: string
    flaresolverr_role_docker_networks_alias: "{{ flaresolverr_name }}"

    # Type: list
    flaresolverr_role_docker_networks_default: []

    # Type: list
    flaresolverr_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    flaresolverr_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    flaresolverr_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    flaresolverr_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    flaresolverr_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    flaresolverr_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    flaresolverr_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    flaresolverr_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    flaresolverr_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    flaresolverr_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    flaresolverr_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    flaresolverr_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    flaresolverr_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    flaresolverr_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    flaresolverr_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    flaresolverr_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    flaresolverr_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    flaresolverr_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    flaresolverr_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    flaresolverr_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        flaresolverr_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "flaresolverr2.{{ user.domain }}"
          - "flaresolverr.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        flaresolverr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'flaresolverr2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

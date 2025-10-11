---
hide:
  - tags
tags:
  - tika
  - extraction
  - utility
---

# tika

## THIS DOCUMENTATION IS NOT YET COMPLETED

## What is it?

[tika](https://tika.url) is a...

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://tika.url){: .header-icons } | [:octicons-link-16: Docs](https://tika.docs.url){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/tika/tika){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/tika/tika){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-tika

```

### 2. URL

- To access tika, visit `https://tika._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        tika_role_docker_image_tag: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    tika_name: tika

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    tika_role_docker_container: "{{ tika_name }}"

    # Image
    # Type: bool (true/false)
    tika_role_docker_image_pull: true

    # Type: string
    tika_role_docker_image_repo: "ghcr.io/paperless-ngx/tika"

    # Type: string
    tika_role_docker_image_tag: "latest"

    # Type: string
    tika_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='tika') }}:{{ lookup('role_var', '_docker_image_tag', role='tika') }}"

    # Envs
    # Type: dict
    tika_role_docker_envs_default: 
      TZ: "{{ tz }}"

    # Type: dict
    tika_role_docker_envs_custom: {}

    # Hostname
    # Type: string
    tika_role_docker_hostname: "{{ tika_name }}"

    # Networks
    # Type: string
    tika_role_docker_networks_alias: "{{ tika_name }}"

    # Type: list
    tika_role_docker_networks_default: []

    # Type: list
    tika_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    tika_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    tika_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    tika_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    tika_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    tika_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    tika_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    tika_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    tika_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    tika_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    tika_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    tika_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    tika_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    tika_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    tika_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    tika_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    tika_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    tika_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    tika_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    tika_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        tika_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "tika2.{{ user.domain }}"
          - "tika.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        tika_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'tika2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

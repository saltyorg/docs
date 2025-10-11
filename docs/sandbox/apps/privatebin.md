---
hide:
  - tags
tags:
  - privatebin
  - pastebin
  - privacy
---

# PrivateBin

## What is it?

[PrivateBin](https://privatebin.info/) PrivateBin is a minimalist, open source online pastebin where the server has zero knowledge of pasted data.
It's privacy-preserving and encrypted-by-default.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://privatebin.info/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/PrivateBin/PrivateBin/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/PrivateBin/PrivateBin){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/privatebin/nginx-fpm-alpine){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-privatebin

```

### 2. URL

- To access PrivateBin, visit `https://privatebin._yourdomain.com_`

### 3. Setup

- Edit `/opt/privatebin/conf.php` to customize your instance.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        privatebin_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    privatebin_name: privatebin

    ```

??? example "Paths"

    ```yaml
    # Type: string
    privatebin_role_paths_folder: "{{ privatebin_name }}"

    # Type: string
    privatebin_role_paths_location: "{{ server_appdata_path }}/{{ privatebin_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    privatebin_role_web_subdomain: "{{ privatebin_name }}"

    # Type: string
    privatebin_role_web_domain: "{{ user.domain }}"

    # Type: string
    privatebin_role_web_port: "8080"

    # Type: string
    privatebin_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='privatebin') + '.' + lookup('role_var', '_web_domain', role='privatebin')
                              if (lookup('role_var', '_web_subdomain', role='privatebin') | length > 0)
                              else lookup('role_var', '_web_domain', role='privatebin')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    privatebin_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='privatebin') }}"

    # Type: string
    privatebin_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='privatebin') }}"

    # Type: bool (true/false)
    privatebin_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    privatebin_role_traefik_sso_middleware: ""

    # Type: string
    privatebin_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    privatebin_role_traefik_middleware_custom: ""

    # Type: string
    privatebin_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    privatebin_role_traefik_enabled: true

    # Type: bool (true/false)
    privatebin_role_traefik_api_enabled: false

    # Type: string
    privatebin_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    privatebin_role_docker_container: "{{ privatebin_name }}"

    # Image
    # Type: bool (true/false)
    privatebin_role_docker_image_pull: true

    # Type: string
    privatebin_role_docker_image_tag: "latest"

    # Type: string
    privatebin_role_docker_image: "privatebin/nginx-fpm-alpine:{{ lookup('role_var', '_docker_image_tag', role='privatebin') }}"

    # Envs
    # Type: dict
    privatebin_role_docker_envs_default: 
      TZ: "{{ tz }}"
      PHP_TZ: "{{ tz }}"

    # Type: dict
    privatebin_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    privatebin_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='privatebin') }}:/srv/data"
      - "{{ lookup('role_var', '_paths_location', role='privatebin') }}/conf.php:/srv/cfg/conf.php:ro"
      - "{{ privatebin_name }}_tmpfs_run:/run"

    # Type: list
    privatebin_role_docker_volumes_custom: []

    # Mounts
    # Type: list
    privatebin_role_docker_mounts_default: 
      - target: /tmp
        type: tmpfs
      - target: /var/lib/nginx/tmp
        type: tmpfs

    # Type: list
    privatebin_role_docker_mounts_custom: []

    # Hostname
    # Type: string
    privatebin_role_docker_hostname: "{{ privatebin_name }}"

    # Networks
    # Type: string
    privatebin_role_docker_networks_alias: "{{ privatebin_name }}"

    # Type: list
    privatebin_role_docker_networks_default: []

    # Type: list
    privatebin_role_docker_networks_custom: []

    # Read Only
    # Type: bool (true/false)
    privatebin_role_docker_read_only: true

    # Restart Policy
    # Type: string
    privatebin_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    privatebin_role_docker_state: started

    # User
    # Type: string
    privatebin_role_docker_user: "{{ uid }}:{{ gid }}"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    privatebin_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    privatebin_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    privatebin_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    privatebin_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    privatebin_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    privatebin_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    privatebin_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    privatebin_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    privatebin_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    privatebin_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    privatebin_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    privatebin_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    privatebin_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    privatebin_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    privatebin_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    privatebin_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    privatebin_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        privatebin_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "privatebin2.{{ user.domain }}"
          - "privatebin.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        privatebin_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'privatebin2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

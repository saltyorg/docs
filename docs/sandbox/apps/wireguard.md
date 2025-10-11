---
hide:
  - tags
tags:
  - VPN
  - server
---

# Wireguard

## What is it?

[Wireguard](https://wireguard.com) is an extremely simple yet fast and modern VPN that utilizes state-of-the-art cryptography.

The Wireguard server is deployed using the [WG-Easy](https://github.com/WeeJeWel/wg-easy) image with a simple Web UI for management.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Wireguard](https://www.wireguard.com/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/WeeJeWel/wg-easy){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/wg-easy/wg-easy){: .header-icons } | [:material-docker: Docker:](https://ghcr.io/wg-easy/wg-easy){: .header-icons } |

### 1. Installation

``` shell

sb install sandbox-wireguard

```

### 2. URL

- To access Wireguard, visit `https://wireguard._yourdomain.com_`

The password provisioned is your Saltbox password.

### 3. Setup

- Use the Web UI to configure your clients.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        wireguard_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    wireguard_name: wireguard

    ```

??? example "Settings"

    ```yaml
    # Type: string
    wireguard_listen_port: "51820"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    wireguard_role_paths_folder: "{{ wireguard_name }}"

    # Type: string
    wireguard_role_paths_location: "{{ server_appdata_path }}/{{ wireguard_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    wireguard_role_web_subdomain: "{{ wireguard_name }}"

    # Type: string
    wireguard_role_web_domain: "{{ user.domain }}"

    # Type: string
    wireguard_role_web_port: "51821"

    # Type: string
    wireguard_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='wireguard') + '.' + lookup('role_var', '_web_domain', role='wireguard')
                             if (lookup('role_var', '_web_subdomain', role='wireguard') | length > 0)
                             else lookup('role_var', '_web_domain', role='wireguard')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    wireguard_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='wireguard') }}"

    # Type: string
    wireguard_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='wireguard') }}"

    # Type: bool (true/false)
    wireguard_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    wireguard_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    wireguard_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    wireguard_role_traefik_middleware_custom: ""

    # Type: string
    wireguard_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    wireguard_role_traefik_enabled: true

    # Type: bool (true/false)
    wireguard_role_traefik_api_enabled: false

    # Type: string
    wireguard_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    wireguard_role_docker_container: "{{ wireguard_name }}"

    # Image
    # Type: bool (true/false)
    wireguard_role_docker_image_pull: true

    # Type: string
    wireguard_role_docker_image_repo: "ghcr.io/wg-easy/wg-easy"

    # Type: string
    wireguard_role_docker_image_tag: "14"

    # Type: string
    wireguard_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='wireguard') }}:{{ lookup('role_var', '_docker_image_tag', role='wireguard') }}"

    # Ports
    # Type: list
    wireguard_role_docker_ports_defaults: 
      - "{{ wireguard_listen_port }}:51820/udp"

    # Type: list
    wireguard_role_docker_ports_custom: []

    # Envs
    # Type: dict
    wireguard_role_docker_envs_default: 
      TZ: "{{ tz }}"
      WG_HOST: "{{ ip_address_public }}"
      PASSWORD_HASH: "{{ user.pass | password_hash('bcrypt') }}"
      WG_PORT: "{{ wireguard_listen_port }}"

    # Type: dict
    wireguard_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    wireguard_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='wireguard') }}:/etc/wireguard"

    # Type: list
    wireguard_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    wireguard_role_docker_hostname: "{{ wireguard_name }}"

    # Networks
    # Type: string
    wireguard_role_docker_networks_alias: "{{ wireguard_name }}"

    # Type: list
    wireguard_role_docker_networks_default: []

    # Type: list
    wireguard_role_docker_networks_custom: []

    # Capabilities
    # Type: list
    wireguard_role_docker_capabilities_default: 
      - NET_ADMIN
      - SYS_MODULE

    # Type: list
    wireguard_role_docker_capabilities_custom: []

    # Sysctls
    # Type: dict
    wireguard_role_docker_sysctls: 
      net.ipv4.conf.all.src_valid_mark: "1"
      net.ipv4.ip_forward: "1"

    # Restart Policy
    # Type: string
    wireguard_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    wireguard_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    wireguard_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    wireguard_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    wireguard_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    wireguard_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    wireguard_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    wireguard_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    wireguard_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    wireguard_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    wireguard_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    wireguard_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    wireguard_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    wireguard_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    wireguard_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    wireguard_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    wireguard_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    wireguard_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    wireguard_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        wireguard_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "wireguard2.{{ user.domain }}"
          - "wireguard.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        wireguard_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'wireguard2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

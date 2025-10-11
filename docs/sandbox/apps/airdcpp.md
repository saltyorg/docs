---
hide:
  - tags
tags:
  - airdcpp
  - p2p
  - downloading
---

# AirDC++

## What is it?

[AirDC++](https://www.airdcpp.net/) is an easy to use client for [Advanced Direct Connect](http://en.wikipedia.org/wiki/Advanced_Direct_Connect) and [Direct Connect](http://en.wikipedia.org/wiki/Direct_Connect_(file_sharing)) networks. You are able to join "hubs" with other users, and chat, perform searches and browse the share of each user. It allows you to share files with friends and other people.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.airdcpp.net/){: .header-icons } | [:octicons-link-16: Docs](https://airdcpp-web.github.io/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/gangefors/docker-airdcpp-webclient){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/gangefors/airdcpp-webclient/){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-airdcpp

```

### 2. URL

- To access AirDC++, visit `https://airdcpp._yourdomain.com_`
- Username / password for the default admin account is: admin / password

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        airdcpp_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    airdcpp_name: airdcpp

    ```

??? example "Paths"

    ```yaml
    # Type: string
    airdcpp_role_paths_folder: "{{ airdcpp_name }}"

    # Type: string
    airdcpp_role_paths_location: "{{ server_appdata_path }}/{{ airdcpp_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    airdcpp_role_web_subdomain: "{{ airdcpp_name }}"

    # Type: string
    airdcpp_role_web_domain: "{{ user.domain }}"

    # Type: string
    airdcpp_role_web_port: "5600"

    # Type: string
    airdcpp_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='airdcpp') + '.' + lookup('role_var', '_web_domain', role='airdcpp')
                           if (lookup('role_var', '_web_subdomain', role='airdcpp') | length > 0)
                           else lookup('role_var', '_web_domain', role='airdcpp')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    airdcpp_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='airdcpp') }}"

    # Type: string
    airdcpp_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='airdcpp') }}"

    # Type: bool (true/false)
    airdcpp_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    airdcpp_role_traefik_sso_middleware: ""

    # Type: string
    airdcpp_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    airdcpp_role_traefik_middleware_custom: ""

    # Type: string
    airdcpp_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    airdcpp_role_traefik_enabled: true

    # Type: bool (true/false)
    airdcpp_role_traefik_api_enabled: false

    # Type: string
    airdcpp_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    airdcpp_role_docker_container: "{{ airdcpp_name }}"

    # Image
    # Type: bool (true/false)
    airdcpp_role_docker_image_pull: true

    # Type: string
    airdcpp_role_docker_image_repo: "gangefors/airdcpp-webclient"

    # Type: string
    airdcpp_role_docker_image_tag: "latest"

    # Type: string
    airdcpp_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='airdcpp') }}:{{ lookup('role_var', '_docker_image_tag', role='airdcpp') }}"

    # Ports
    # Type: list
    airdcpp_role_docker_ports_defaults: 
      - "21248:21248"
      - "21248:21248/udp"
      - "21249:21249"

    # Type: list
    airdcpp_role_docker_ports_custom: []

    # Envs
    # Type: dict
    airdcpp_role_docker_envs_default: 
      TZ: "{{ tz }}"

    # Type: dict
    airdcpp_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    airdcpp_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='airdcpp') }}:/.airdcpp"
      - "/mnt/local/downloads/airdcpp:/Downloads"

    # Type: list
    airdcpp_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    airdcpp_role_docker_hostname: "{{ airdcpp_name }}"

    # Networks
    # Type: string
    airdcpp_role_docker_networks_alias: "{{ airdcpp_name }}"

    # Type: list
    airdcpp_role_docker_networks_default: []

    # Type: list
    airdcpp_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    airdcpp_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    airdcpp_role_docker_state: started

    # User
    # Type: string
    airdcpp_role_docker_user: "{{ uid }}:{{ gid }}"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    airdcpp_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    airdcpp_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    airdcpp_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    airdcpp_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    airdcpp_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    airdcpp_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    airdcpp_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    airdcpp_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    airdcpp_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    airdcpp_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    airdcpp_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    airdcpp_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    airdcpp_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    airdcpp_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    airdcpp_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    airdcpp_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    airdcpp_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        airdcpp_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "airdcpp2.{{ user.domain }}"
          - "airdcpp.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        airdcpp_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'airdcpp2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
hide:
  - tags
tags:
  - transmissionvpn
  - download
  - vpn
---

# transmissionvpn

## THIS DOCUMENTATION IS NOT YET COMPLETED

## What is it?

[transmissionvpn](https://transmissionvpn.url) is a...

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://transmissionvpn.url){: .header-icons } | [:octicons-link-16: Docs](https://transmissionvpn.docs.url){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/transmissionvpn/transmissionvpn){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/transmissionvpn/transmissionvpn){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-transmissionvpn

```

### 2. URL

- To access transmissionvpn, visit `https://transmissionvpn.xDOMAIN_NAMEx`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        transmissionvpn_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `transmissionvpn_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `transmissionvpn_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    transmissionvpn_name: transmissionvpn

    ```

??? example "Settings"

    ```yaml
    # Type: string
    transmissionvpn_create_tun_device: "false"

    # Type: string
    transmissionvpn_transmission_home: "/opt/transmissionvpn"

    # Type: string
    transmissionvpn_umask_set: "022"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    transmissionvpn_role_paths_folder: "{{ transmissionvpn_name }}"

    # Type: string
    transmissionvpn_role_paths_location: "{{ server_appdata_path }}/{{ transmissionvpn_role_paths_folder }}"

    # Type: string
    transmissionvpn_role_paths_downloads_location: "{{ downloads_torrents_path }}/{{ transmissionvpn_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    transmissionvpn_role_web_subdomain: "{{ transmissionvpn_name }}"

    # Type: string
    transmissionvpn_role_web_domain: "{{ user.domain }}"

    # Type: string
    transmissionvpn_role_web_port: "9091"

    # Type: string
    transmissionvpn_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='transmissionvpn') + '.' + lookup('role_var', '_web_domain', role='transmissionvpn')
                                   if (lookup('role_var', '_web_subdomain', role='transmissionvpn') | length > 0)
                                   else lookup('role_var', '_web_domain', role='transmissionvpn')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    transmissionvpn_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='transmissionvpn') }}"

    # Type: string
    transmissionvpn_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='transmissionvpn') }}"

    # Type: bool (true/false)
    transmissionvpn_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    transmissionvpn_role_traefik_sso_middleware: ""

    # Type: string
    transmissionvpn_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    transmissionvpn_role_traefik_middleware_custom: ""

    # Type: string
    transmissionvpn_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    transmissionvpn_role_traefik_enabled: true

    # Type: bool (true/false)
    transmissionvpn_role_traefik_api_enabled: false

    # Type: string
    transmissionvpn_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    transmissionvpn_role_docker_container: "{{ transmissionvpn_name }}"

    # Image
    # Type: bool (true/false)
    transmissionvpn_role_docker_image_pull: true

    # Type: string
    transmissionvpn_role_docker_image_repo: "haugene/transmission-openvpn"

    # Type: string
    transmissionvpn_role_docker_image_tag: "latest"

    # Type: string
    transmissionvpn_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='transmissionvpn') }}:{{ lookup('role_var', '_docker_image_tag', role='transmissionvpn') }}"

    # Envs
    # Type: dict
    transmissionvpn_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"
      OPENVPN_PROVIDER: "{{ transmissionvpn.vpn_prov | default('pia', true) }}"
      OPENVPN_USERNAME: "{{ transmissionvpn.vpn_user | default('username', true) }}"
      OPENVPN_PASSWORD: "{{ transmissionvpn.vpn_pass | default('password', true) }}"
      UMASK_SET: "{{ transmissionvpn_umask_set }}"
      CREATE_TUN_DEVICE: "{{ transmissionvpn_create_tun_device }}"
      TRANSMISSION_HOME: "{{ transmissionvpn_transmission_home }}"

    # Type: dict
    transmissionvpn_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    transmissionvpn_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='transmissionvpn') }}:/config"
      - "{{ lookup('role_var', '_paths_location', role='transmissionvpn') }}/data:/opt/transmissionvpn"
      - "{{ server_appdata_path }}/scripts:/scripts"
      - "{{ lookup('role_var', '_paths_location', role='transmissionvpn') }}/vpn:/etc/openvpn/custom"
      - "{{ lookup('role_var', '_paths_downloads_location', role='transmissionvpn') }}:/data"

    # Type: list
    transmissionvpn_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    transmissionvpn_role_docker_hostname: "{{ transmissionvpn_name }}"

    # Networks
    # Type: string
    transmissionvpn_role_docker_networks_alias: "{{ transmissionvpn_name }}"

    # Type: list
    transmissionvpn_role_docker_networks_default: []

    # Type: list
    transmissionvpn_role_docker_networks_custom: []

    # Capabilities
    # Type: list
    transmissionvpn_role_docker_capabilities_default: 
      - NET_ADMIN

    # Type: list
    transmissionvpn_role_docker_capabilities_custom: []

    # Restart Policy
    # Type: string
    transmissionvpn_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    transmissionvpn_role_docker_state: started

    # Sysctls
    # Type: dict
    transmissionvpn_role_docker_sysctls: 
      net.ipv4.conf.all.src_valid_mark: "1"

    # Privileged
    # Type: bool (true/false)
    transmissionvpn_role_docker_privileged: true

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    transmissionvpn_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    transmissionvpn_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    transmissionvpn_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    transmissionvpn_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    transmissionvpn_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    transmissionvpn_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    transmissionvpn_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    transmissionvpn_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    transmissionvpn_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    transmissionvpn_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    transmissionvpn_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    transmissionvpn_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    transmissionvpn_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    transmissionvpn_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    transmissionvpn_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    transmissionvpn_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    transmissionvpn_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        transmissionvpn_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "transmissionvpn2.{{ user.domain }}"
          - "transmissionvpn.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        transmissionvpn_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'transmissionvpn2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

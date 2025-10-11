---
hide:
  - tags
tags:
  - znc
  - irc
  - bouncer
---

# ZNC

## What is it?

[ZNC](https://wiki.znc.in/ZNC) is an an advanced IRC bouncer that is left connected so an IRC client can disconnect/reconnect without losing the chat session.

It can detach the client from the actual IRC server, and also from selected channels. Multiple clients from different locations can connect to a single ZNC account simultaneously and therefore appear under the same nickname on IRC.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-docker: Docker:](https://wiki.znc.in/ZNC){: .header-icons } | [:octicons-link-16: Docs](https://wiki.znc.in/ZNC){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/linuxserver/docker-znc){: .header-icons } | [:material-docker: Docker:](https://hub.docker.com/r/linuxserver/znc){: .header-icons } |

### 1. Installation

``` shell

sb install sandbox-znc

```

### 2. URL

- To access ZNC, visit `https://znc._yourdomain.com_`

Default user/password: admin/admin

Change that password ASAP.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        znc_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    znc_name: znc

    ```

??? example "Paths"

    ```yaml
    # Type: string
    znc_role_paths_folder: "{{ znc_name }}"

    # Type: string
    znc_role_paths_location: "{{ server_appdata_path }}/{{ znc_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    znc_role_web_subdomain: "{{ znc_name }}"

    # Type: string
    znc_role_web_domain: "{{ user.domain }}"

    # Type: string
    znc_role_web_port: "6501"

    # Type: string
    znc_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='znc') + '.' + lookup('role_var', '_web_domain', role='znc')
                       if (lookup('role_var', '_web_subdomain', role='znc') | length > 0)
                       else lookup('role_var', '_web_domain', role='znc')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    znc_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='znc') }}"

    # Type: string
    znc_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='znc') }}"

    # Type: bool (true/false)
    znc_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    znc_role_traefik_sso_middleware: ""

    # Type: string
    znc_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    znc_role_traefik_middleware_custom: ""

    # Type: string
    znc_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    znc_role_traefik_enabled: true

    # Type: bool (true/false)
    znc_role_traefik_api_enabled: false

    # Type: string
    znc_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    znc_role_docker_container: "{{ znc_name }}"

    # Image
    # Type: bool (true/false)
    znc_role_docker_image_pull: true

    # Type: string
    znc_role_docker_image_repo: "lscr.io/linuxserver/znc"

    # Type: string
    znc_role_docker_image_tag: "latest"

    # Type: string
    znc_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='znc') }}:{{ lookup('role_var', '_docker_image_tag', role='znc') }}"

    # Ports
    # Type: list
    znc_role_docker_ports_defaults: 
      - "{{ lookup('role_var', '_web_port', role='znc') }}:{{ lookup('role_var', '_web_port', role='znc') }}"
      - "6502:6502"

    # Type: list
    znc_role_docker_ports_custom: []

    # Envs
    # Type: dict
    znc_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    znc_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    znc_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='znc') }}:/config"

    # Type: list
    znc_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    znc_role_docker_hostname: "{{ znc_name }}"

    # Networks
    # Type: string
    znc_role_docker_networks_alias: "{{ znc_name }}"

    # Type: list
    znc_role_docker_networks_default: []

    # Type: list
    znc_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    znc_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    znc_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    znc_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    znc_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    znc_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    znc_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    znc_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    znc_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    znc_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    znc_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    znc_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    znc_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    znc_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    znc_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    znc_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    znc_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    znc_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    znc_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    znc_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        znc_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "znc2.{{ user.domain }}"
          - "znc.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        znc_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'znc2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

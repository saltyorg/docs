---
hide:
  - tags
tags:
  - puddletag
  - media
  - tagging
---

# Puddletag

## What is it?

[Puddletag](https://docs.puddletag.net/) is an audio tag editor (primarily created) for GNU/Linux similar to the Windows program, Mp3tag. Unlike most taggers for GNU/Linux, it uses a spreadsheet-like layout so that all the tags you want to edit by hand are visible and easily editable.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself. (Basic Auth)

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://docs.puddletag.net/){: .header-icons } | [:octicons-link-16: Docs](https://docs.puddletag.net/docs.html){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Xirg/docker-puddletag){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-puddletag

```

### 2. URL

- To access Puddletag, visit `https://puddletag._yourdomain.com_`

### 3. Setup

- Default login:

  ``` { .yaml}
  Username: "your user from accounts.yml"
  Password: your_normal_password
  ```

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        puddletag_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `puddletag_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `puddletag_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    puddletag_name: puddletag

    ```

??? example "Paths"

    ```yaml
    # Type: string
    puddletag_role_paths_folder: "{{ puddletag_name }}"

    # Type: string
    puddletag_role_paths_location: "{{ server_appdata_path }}/{{ puddletag_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    puddletag_role_web_subdomain: "{{ puddletag_name }}"

    # Type: string
    puddletag_role_web_domain: "{{ user.domain }}"

    # Type: string
    puddletag_role_web_port: "8080"

    # Type: string
    puddletag_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='puddletag') + '.' + lookup('role_var', '_web_domain', role='puddletag')
                             if (lookup('role_var', '_web_subdomain', role='puddletag') | length > 0)
                             else lookup('role_var', '_web_domain', role='puddletag')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    puddletag_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='puddletag') }}"

    # Type: string
    puddletag_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='puddletag') }}"

    # Type: bool (true/false)
    puddletag_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    puddletag_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    puddletag_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    puddletag_role_traefik_middleware_custom: ""

    # Type: string
    puddletag_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    puddletag_role_traefik_enabled: true

    # Type: bool (true/false)
    puddletag_role_traefik_api_enabled: false

    # Type: string
    puddletag_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    puddletag_role_docker_container: "{{ puddletag_name }}"

    # Image
    # Type: bool (true/false)
    puddletag_role_docker_image_pull: true

    # Type: string
    puddletag_role_docker_image_repo: "xirg/docker-puddletag"

    # Type: string
    puddletag_role_docker_image_tag: "latest"

    # Type: string
    puddletag_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='puddletag') }}:{{ lookup('role_var', '_docker_image_tag', role='puddletag') }}"

    # Envs
    # Type: dict
    puddletag_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"
      APPNAME: "{{ puddletag_name }}"
      GUAC_USER: "{{ user.name }}"
      GUAC_PASS: "{{ user.pass | hash('md5') }}"

    # Type: dict
    puddletag_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    puddletag_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='puddletag') }}:/config"

    # Type: list
    puddletag_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    puddletag_role_docker_hostname: "{{ puddletag_name }}"

    # Networks
    # Type: string
    puddletag_role_docker_networks_alias: "{{ puddletag_name }}"

    # Type: list
    puddletag_role_docker_networks_default: []

    # Type: list
    puddletag_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    puddletag_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    puddletag_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    puddletag_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    puddletag_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    puddletag_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    puddletag_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    puddletag_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    puddletag_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    puddletag_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    puddletag_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    puddletag_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    puddletag_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    puddletag_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    puddletag_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    puddletag_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    puddletag_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    puddletag_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    puddletag_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    puddletag_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        puddletag_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "puddletag2.{{ user.domain }}"
          - "puddletag.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        puddletag_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'puddletag2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

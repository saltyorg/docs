---
hide:
  - tags
tags:
  - krusader
  - file-management
  - admin
---

# Krusader

## What is it?

[Krusader](http://www.krusader.org/) is an advanced orthodox file manager for KDE and other desktops in the Unix world. It is similar to the console-based GNU Midnight Commander, GNOME Commander for the GNOME desktop environment, or Total Commander for Windows, all of which can trace their paradigmatic features to the original Norton Commander for DOS. It supports extensive archive handling, mounted filesystem support, FTP, advanced search, viewer/editor, directory synchronisation, file content comparisons, batch renaming, etc.

This is a Docker container for Krusader.

The GUI of the application is accessed through a modern web browser (no installation or configuration needed on the client side).

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](http://www.krusader.org/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/binhex/arch-krusader){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/binhex/arch-krusader){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/binhex/arch-krusader){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-krusader

```

### 2. URL

- To access Krusader, visit `https://krusader._yourdomain.com_`
- Now you can click on vnc.html or vnc_lite.html

### 3. Setup

- The configured password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`
- /mnt is already mounted to /mnt

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        krusader_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    krusader_name: krusader

    ```

??? example "Docker Socket Proxy"

    ```yaml
    # Type: dict
    krusader_role_docker_socket_proxy_envs: 
      CONTAINERS: "1"
      POST: "0"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    krusader_role_paths_folder: "{{ krusader_name }}"

    # Type: string
    krusader_role_paths_location: "{{ server_appdata_path }}/{{ krusader_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    krusader_role_web_subdomain: "{{ krusader_name }}"

    # Type: string
    krusader_role_web_domain: "{{ user.domain }}"

    # Type: string
    krusader_role_web_port: "6080"

    # Type: string
    krusader_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='krusader') + '.' + lookup('role_var', '_web_domain', role='krusader')
                            if (lookup('role_var', '_web_subdomain', role='krusader') | length > 0)
                            else lookup('role_var', '_web_domain', role='krusader')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    krusader_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='krusader') }}"

    # Type: string
    krusader_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='krusader') }}"

    # Type: bool (true/false)
    krusader_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    krusader_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    krusader_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    krusader_role_traefik_middleware_api: "{{ traefik_global_middleware }}"

    # Type: string
    krusader_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    krusader_role_traefik_enabled: true

    # Type: bool (true/false)
    krusader_role_traefik_api_enabled: false

    # Type: string
    krusader_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    krusader_role_docker_container: "{{ krusader_name }}"

    # Image
    # Type: bool (true/false)
    krusader_role_docker_image_pull: true

    # Type: string
    krusader_role_docker_image_tag: "latest"

    # Type: string
    krusader_role_docker_image_repo: "binhex/arch-krusader"

    # Type: string
    krusader_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='krusader') }}:{{ lookup('role_var', '_docker_image_tag', role='krusader') }}"

    # Envs
    # Type: dict
    krusader_role_docker_envs_default: 
      TZ: "{{ tz }}"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      VNC_PASSWORD: "{{ user.pass }}"
      DOCKER_HOST: "tcp://{{ krusader_name }}-docker-socket-proxy:2375"
      WEBPAGE_TITLE: "Krusader File Manager Web"
      TEMP_FOLDER: "/tmp"

    # Type: dict
    krusader_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    krusader_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='krusader') }}/config:/config"

    # Type: list
    krusader_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    krusader_role_docker_hostname: "{{ krusader_name }}"

    # Networks
    # Type: string
    krusader_role_docker_networks_alias: "{{ krusader_name }}"

    # Type: list
    krusader_role_docker_networks_default: []

    # Type: list
    krusader_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    krusader_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    krusader_role_docker_state: started

    # Dependencies
    # Type: string
    krusader_role_depends_on: "{{ krusader_name }}-docker-socket-proxy"

    # Type: string
    krusader_role_depends_on_delay: "0"

    # Type: string
    krusader_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    krusader_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    krusader_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    krusader_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    krusader_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    krusader_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    krusader_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    krusader_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    krusader_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    krusader_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    krusader_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    krusader_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    krusader_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    krusader_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    krusader_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    krusader_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    krusader_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    krusader_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        krusader_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "krusader2.{{ user.domain }}"
          - "krusader.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        krusader_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'krusader2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
hide:
  - tags
tags:
  - komga
  - media
  - comics
---

# Komga

## What is it?

[Komga](https://komga.org/) is a free and open source comics/mangas server.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://komga.org/){: .header-icons } | [:octicons-link-16: Docs](https://komga.org/installation/docker.html){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/gotson/komga){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/gotson/komga){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-komga

```

### 2. URL

- To access Komga, visit `https://komga._yourdomain.com_`

### 3. Setup

- On first opening you will be asked to create a user account. <br />
  Choose an email and password, then click on Create User Account.

- Komga expects comics to be stored in `/mnt/unionfs/Media/Comics`.

- `/mnt` is accessible to the container as well.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        komga_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    komga_name: komga

    ```

??? example "Paths"

    ```yaml
    # Type: string
    komga_role_paths_folder: "{{ komga_name }}"

    # Type: string
    komga_role_paths_location: "{{ server_appdata_path }}/{{ komga_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    komga_role_web_subdomain: "{{ komga_name }}"

    # Type: string
    komga_role_web_domain: "{{ user.domain }}"

    # Type: string
    komga_role_web_port: "25600"

    # Type: string
    komga_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='komga') + '.' + lookup('role_var', '_web_domain', role='komga')
                         if (lookup('role_var', '_web_subdomain', role='komga') | length > 0)
                         else lookup('role_var', '_web_domain', role='komga')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    komga_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='komga') }}"

    # Type: string
    komga_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='komga') }}"

    # Type: bool (true/false)
    komga_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    komga_role_traefik_sso_middleware: ""

    # Type: string
    komga_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    komga_role_traefik_middleware_custom: ""

    # Type: string
    komga_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    komga_role_traefik_enabled: true

    # Type: bool (true/false)
    komga_role_traefik_api_enabled: false

    # Type: string
    komga_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    komga_role_docker_container: "{{ komga_name }}"

    # Image
    # Type: bool (true/false)
    komga_role_docker_image_pull: true

    # Type: string
    komga_role_docker_image_tag: "latest"

    # Type: string
    komga_role_docker_image_repo: "gotson/komga"

    # Type: string
    komga_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='komga') }}:{{ lookup('role_var', '_docker_image_tag', role='komga') }}"

    # Volumes
    # Type: list
    komga_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='komga') }}:/config"
      - "/mnt/unionfs/Media/Comics:/comics"

    # Type: list
    komga_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    komga_role_docker_hostname: "{{ komga_name }}"

    # Networks
    # Type: string
    komga_role_docker_networks_alias: "{{ komga_name }}"

    # Type: list
    komga_role_docker_networks_default: []

    # Type: list
    komga_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    komga_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    komga_role_docker_state: started

    # User
    # Type: string
    komga_role_docker_user: "{{ uid }}:{{ gid }}"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    komga_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    komga_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    komga_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    komga_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    komga_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    komga_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    komga_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    komga_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    komga_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    komga_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    komga_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    komga_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    komga_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    komga_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    komga_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    komga_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    komga_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        komga_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "komga2.{{ user.domain }}"
          - "komga.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        komga_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'komga2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

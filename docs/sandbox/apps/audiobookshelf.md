---
hide:
  - tags
tags:
  - audiobookshelf
  - audiobooks
  - podcasts
---

# Audiobookshelf

## What is it?

[audiobookshelf](https://www.audiobookshelf.org/) is a self-hosted audio book and podcast server.

!!! info
    By default, the role is NOT protected behind your Authelia/SSO middleware.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.audiobookshelf.org/){: .header-icons } | [:octicons-link-16: Docs](https://www.audiobookshelf.org/docs){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/advplyr/audiobookshelf-web){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/advplyr/audiobookshelf){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-audiobookshelf

```

### 2. URL

- To access Audiobookshelf, visit `https://audiobookshelf._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        audiobookshelf_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    audiobookshelf_name: audiobookshelf

    ```

??? example "Paths"

    ```yaml
    # Type: string
    audiobookshelf_role_paths_folder: "{{ audiobookshelf_name }}"

    # Type: string
    audiobookshelf_role_paths_location: "{{ server_appdata_path }}/{{ audiobookshelf_role_paths_folder }}"

    # Type: bool (true/false)
    audiobookshelf_role_paths_recursive: true

    ```

??? example "Web"

    ```yaml
    # Type: string
    audiobookshelf_role_web_subdomain: "{{ audiobookshelf_name }}"

    # Type: string
    audiobookshelf_role_web_domain: "{{ user.domain }}"

    # Type: string
    audiobookshelf_role_web_port: "80"

    # Type: string
    audiobookshelf_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='audiobookshelf') + '.' + lookup('role_var', '_web_domain', role='audiobookshelf')
                                  if (lookup('role_var', '_web_subdomain', role='audiobookshelf') | length > 0)
                                  else lookup('role_var', '_web_domain', role='audiobookshelf')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    audiobookshelf_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='audiobookshelf') }}"

    # Type: string
    audiobookshelf_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='audiobookshelf') }}"

    # Type: bool (true/false)
    audiobookshelf_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    audiobookshelf_role_traefik_sso_middleware: ""

    # Type: string
    audiobookshelf_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    audiobookshelf_role_traefik_middleware_custom: ""

    # Type: string
    audiobookshelf_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    audiobookshelf_role_traefik_enabled: true

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    audiobookshelf_role_docker_container: "{{ audiobookshelf_name }}"

    # Image
    # Type: bool (true/false)
    audiobookshelf_role_docker_image_pull: true

    # Type: string
    audiobookshelf_role_docker_image_repo: "ghcr.io/advplyr/audiobookshelf"

    # Type: string
    audiobookshelf_role_docker_image_tag: "latest"

    # Type: string
    audiobookshelf_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='audiobookshelf') }}:{{ lookup('role_var', '_docker_image_tag', role='audiobookshelf') }}"

    # Envs
    # Type: dict
    audiobookshelf_role_docker_envs_default: 
      TZ: "{{ tz }}"

    # Type: dict
    audiobookshelf_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    audiobookshelf_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='audiobookshelf') }}/config:/config"
      - "{{ lookup('role_var', '_paths_location', role='audiobookshelf') }}/metadata:/metadata"
      - "/mnt/unionfs/Media/Audiobooks:/audiobooks"
      - "/mnt/unionfs/Media/Podcasts:/podcasts"

    # Type: list
    audiobookshelf_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    audiobookshelf_role_docker_hostname: "{{ audiobookshelf_name }}"

    # Networks
    # Type: string
    audiobookshelf_role_docker_networks_alias: "{{ audiobookshelf_name }}"

    # Type: list
    audiobookshelf_role_docker_networks_default: []

    # Type: list
    audiobookshelf_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    audiobookshelf_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    audiobookshelf_role_docker_state: started

    # User
    # Type: string
    audiobookshelf_role_docker_user: "{{ uid }}:{{ gid }}"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    audiobookshelf_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    audiobookshelf_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    audiobookshelf_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    audiobookshelf_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    audiobookshelf_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    audiobookshelf_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    audiobookshelf_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    audiobookshelf_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    audiobookshelf_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    audiobookshelf_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    audiobookshelf_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    audiobookshelf_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    audiobookshelf_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    audiobookshelf_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    audiobookshelf_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    audiobookshelf_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    audiobookshelf_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        audiobookshelf_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "audiobookshelf2.{{ user.domain }}"
          - "audiobookshelf.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        audiobookshelf_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'audiobookshelf2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

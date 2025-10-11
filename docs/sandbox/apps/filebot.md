---
hide:
  - tags
tags:
  - filebot
  - media
  - tools
---

# FileBot

## What is it?

[FileBot](http://www.filebot.net/) is the ultimate tool for organizing and renaming your movies, tv shows or anime, and music well as downloading subtitles and artwork. It's smart and just works.

This is a Docker container for FileBot.

The GUI of the application is accessed through a modern web browser (no installation or configuration needed on the client side) or via any VNC client.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](http://www.filebot.net/){: .header-icons } | [:octicons-link-16: Docs](https://www.filebot.net/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/jlesage/docker-filebot){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jlesage/filebot){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-filebot

```

### 2. URL

- To access FileBot, visit `https://filebot._yourdomain.com_`

### 3. Setup

- The configured username/password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        filebot_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    filebot_name: filebot

    ```

??? example "Paths"

    ```yaml
    # Type: string
    filebot_role_paths_folder: "{{ filebot_name }}"

    # Type: string
    filebot_role_paths_location: "{{ server_appdata_path }}/{{ filebot_role_paths_folder }}"

    # Type: string
    filebot_role_paths_config_location: "{{ filebot_role_paths_location }}/config.yml"

    ```

??? example "Web"

    ```yaml
    # Type: string
    filebot_role_web_subdomain: "{{ filebot_name }}"

    # Type: string
    filebot_role_web_domain: "{{ user.domain }}"

    # Type: string
    filebot_role_web_port: "5800"

    # Type: string
    filebot_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='filebot') + '.' + lookup('role_var', '_web_domain', role='filebot')
                           if (lookup('role_var', '_web_subdomain', role='filebot') | length > 0)
                           else lookup('role_var', '_web_domain', role='filebot')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    filebot_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='filebot') }}"

    # Type: string
    filebot_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='filebot') }}"

    # Type: bool (true/false)
    filebot_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    filebot_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    filebot_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    filebot_role_traefik_middleware_custom: ""

    # Type: string
    filebot_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    filebot_role_traefik_enabled: true

    # Type: bool (true/false)
    filebot_role_traefik_api_enabled: true

    # Type: string
    filebot_role_traefik_api_endpoint: "PathPrefix(`/websockify`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    filebot_role_docker_container: "{{ filebot_name }}"

    # Image
    # Type: bool (true/false)
    filebot_role_docker_image_pull: true

    # Type: string
    filebot_role_docker_image_repo: "jlesage/filebot"

    # Type: string
    filebot_role_docker_image_tag: "latest"

    # Type: string
    filebot_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='filebot') }}:{{ lookup('role_var', '_docker_image_tag', role='filebot') }}"

    # Envs
    # Type: dict
    filebot_role_docker_envs_default: 
      TZ: "{{ tz }}"
      USER_ID: "{{ uid }}"
      GROUP_ID: "{{ gid }}"
      UMASK: "022"

    # Type: dict
    filebot_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    filebot_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='filebot') }}:/config"
      - "/mnt/unionfs/Media/:/storage/Media/"
      - "/mnt/local/downloads:/storage/downloads"

    # Type: list
    filebot_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    filebot_role_docker_hostname: "{{ filebot_name }}"

    # Networks
    # Type: string
    filebot_role_docker_networks_alias: "{{ filebot_name }}"

    # Type: list
    filebot_role_docker_networks_default: []

    # Type: list
    filebot_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    filebot_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    filebot_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    filebot_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    filebot_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    filebot_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    filebot_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    filebot_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    filebot_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    filebot_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    filebot_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    filebot_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    filebot_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    filebot_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    filebot_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    filebot_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    filebot_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    filebot_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    filebot_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    filebot_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        filebot_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "filebot2.{{ user.domain }}"
          - "filebot.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        filebot_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'filebot2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

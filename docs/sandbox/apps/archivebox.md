---
hide:
  - tags
tags:
  - archivebox
  - archiving
  - web
---

# ArchiveBox

## What is it?

[ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) is a powerful, self-hosted internet archiving solution to collect, save, and view sites you want to preserve offline.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/ArchiveBox/ArchiveBox){: .header-icons } | [:octicons-link-16: Docs](https://github.com/ArchiveBox/ArchiveBox/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/ArchiveBox/ArchiveBox){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/archivebox/archivebox){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-archivebox

```

### 2. URL

- To access ArchiveBox, visit `https://archivebox._yourdomain.com_`

### 3. Setup

Initial setup guide thanks to `erisheaded` on CB discord.

1. Run tag:

    ``` { .shell }
    sb install sandbox-archivebox
    ```

2. Connect to container:

   ``` { .shell }
   docker exec -it archivebox /bin/bash
   ```

   - NOTE: (This drops you in the /data folder. DO NOT switch to /data/archive directory)
3. Switch to `archivebox` user for config:

   ``` { .shell }
   su archivebox
   ```

4. Initialize with setup to create a web admin:

   ``` { .shell }
   archivebox init --setup
   ```

5. Enter username, email, and password
6. Load URL and test login

By default, your new installation has a publicly accessible web index, snapshots, and archive addition access. You may not want this for a host of security reasons, so it's recommended to review the [ArchiveBox Security Overview](https://docs.archivebox.io/en/latest/Security-Overview.html){: .header-icons } and tailoring these settings to your preference when setting up.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        archivebox_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    archivebox_name: archivebox

    ```

??? example "Paths"

    ```yaml
    # Type: string
    archivebox_role_paths_folder: "{{ archivebox_name }}"

    # Type: string
    archivebox_role_paths_location: "{{ server_appdata_path }}/{{ archivebox_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    archivebox_role_web_subdomain: "{{ archivebox_name }}"

    # Type: string
    archivebox_role_web_domain: "{{ user.domain }}"

    # Type: string
    archivebox_role_web_port: "8000"

    # Type: string
    archivebox_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='archivebox') + '.' + lookup('role_var', '_web_domain', role='archivebox')
                              if (lookup('role_var', '_web_subdomain', role='archivebox') | length > 0)
                              else lookup('role_var', '_web_domain', role='archivebox')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    archivebox_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='archivebox') }}"

    # Type: string
    archivebox_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='archivebox') }}"

    # Type: bool (true/false)
    archivebox_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    archivebox_role_traefik_sso_middleware: ""

    # Type: string
    archivebox_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    archivebox_role_traefik_middleware_custom: ""

    # Type: string
    archivebox_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    archivebox_role_traefik_enabled: true

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    archivebox_role_docker_container: "{{ archivebox_name }}"

    # Image
    # Type: bool (true/false)
    archivebox_role_docker_image_pull: true

    # Type: string
    archivebox_role_docker_image_repo: "archivebox/archivebox"

    # Type: string
    archivebox_role_docker_image_tag: "latest"

    # Type: string
    archivebox_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='archivebox') }}:{{ lookup('role_var', '_docker_image_tag', role='archivebox') }}"

    # Envs
    # Type: dict
    archivebox_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    archivebox_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    archivebox_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='archivebox') }}:/data"

    # Type: list
    archivebox_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    archivebox_role_docker_hostname: "{{ archivebox_name }}"

    # Networks
    # Type: string
    archivebox_role_docker_networks_alias: "{{ archivebox_name }}"

    # Type: list
    archivebox_role_docker_networks_default: []

    # Type: list
    archivebox_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    archivebox_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    archivebox_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    archivebox_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    archivebox_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    archivebox_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    archivebox_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    archivebox_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    archivebox_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    archivebox_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    archivebox_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    archivebox_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    archivebox_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    archivebox_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    archivebox_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    archivebox_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    archivebox_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    archivebox_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    archivebox_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    archivebox_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        archivebox_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "archivebox2.{{ user.domain }}"
          - "archivebox.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        archivebox_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'archivebox2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

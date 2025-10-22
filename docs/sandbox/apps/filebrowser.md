---
hide:
  - tags
tags:
  - filebrowser
  - file-management
  - admin
---

# File Browser

## What is it?

[File Browser](https://filebrowser.org/) is is a create-your-own-cloud-kind of software where you can install it on a server, direct it to a path and then access your files through a nice web interface. You have many available features!

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://filebrowser.org/){: .header-icons } | [:octicons-link-16: Docs](https://filebrowser.org/features){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/filebrowser/filebrowser){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/filebrowser/filebrowser){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-filebrowser

```

### 2. URL

- To access File Browser, visit `https://filebrowser.xDOMAIN_NAMEx`

!!! info
    The initial `admin` user has a randomly generated password. You may retrieve this password in the container logs via `docker logs filebrowser`. We recommend changing the credentials promptly upon deployment.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        filebrowser_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `filebrowser_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `filebrowser_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    filebrowser_name: filebrowser

    ```

??? example "Paths"

    ```yaml
    # Type: string
    filebrowser_role_paths_folder: "{{ filebrowser_name }}"

    # Type: string
    filebrowser_role_paths_location: "{{ server_appdata_path }}/{{ filebrowser_role_paths_folder }}"

    # Type: string
    filebrowser_role_paths_config_location: "{{ filebrowser_role_paths_location }}/filebrowser.json"

    # Type: string
    filebrowser_role_paths_config_folder: "{{ filebrowser_role_paths_location }}/config"

    # Type: string
    filebrowser_role_paths_db_location: "{{ filebrowser_role_paths_location }}/filebrowser.db"

    # Type: string
    filebrowser_role_paths_db_folder: "{{ filebrowser_role_paths_location }}/database"

    ```

??? example "Web"

    ```yaml
    # Type: string
    filebrowser_role_web_subdomain: "{{ filebrowser_name }}"

    # Type: string
    filebrowser_role_web_domain: "{{ user.domain }}"

    # Type: string
    filebrowser_role_web_port: "80"

    # Type: string
    filebrowser_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='filebrowser') + '.' + lookup('role_var', '_web_domain', role='filebrowser')
                               if (lookup('role_var', '_web_subdomain', role='filebrowser') | length > 0)
                               else lookup('role_var', '_web_domain', role='filebrowser')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    filebrowser_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='filebrowser') }}"

    # Type: string
    filebrowser_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='filebrowser') }}"

    # Type: bool (true/false)
    filebrowser_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    filebrowser_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    filebrowser_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    filebrowser_role_traefik_middleware_custom: ""

    # Type: string
    filebrowser_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    filebrowser_role_traefik_enabled: true

    # Type: bool (true/false)
    filebrowser_role_traefik_api_enabled: true

    # Type: string
    filebrowser_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/share`) || PathPrefix(`/static`) || PathPrefix(`/api/public`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    filebrowser_role_docker_container: "{{ filebrowser_name }}"

    # Image
    # Type: bool (true/false)
    filebrowser_role_docker_image_pull: true

    # Type: string
    filebrowser_role_docker_image_repo: "filebrowser/filebrowser"

    # Type: string
    filebrowser_role_docker_image_tag: "latest"

    # Type: string
    filebrowser_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='filebrowser') }}:{{ lookup('role_var', '_docker_image_tag', role='filebrowser') }}"

    # Envs
    # Type: dict
    filebrowser_role_docker_envs_default: 
      TZ: "{{ tz }}"

    # Type: dict
    filebrowser_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    filebrowser_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_db_folder', role='filebrowser') }}:/database"
      - "{{ lookup('role_var', '_paths_config_folder', role='filebrowser') }}:/config"
      - "/mnt/unionfs:/srv:rslave"

    # Type: list
    filebrowser_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    filebrowser_role_docker_hostname: "{{ filebrowser_name }}"

    # Networks
    # Type: string
    filebrowser_role_docker_networks_alias: "{{ filebrowser_name }}"

    # Type: list
    filebrowser_role_docker_networks_default: []

    # Type: list
    filebrowser_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    filebrowser_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    filebrowser_role_docker_state: started

    # User
    # Type: string
    filebrowser_role_docker_user: "{{ uid }}:{{ gid }}"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    filebrowser_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    filebrowser_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    filebrowser_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    filebrowser_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    filebrowser_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    filebrowser_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    filebrowser_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    filebrowser_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    filebrowser_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    filebrowser_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    filebrowser_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    filebrowser_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    filebrowser_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    filebrowser_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    filebrowser_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    filebrowser_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    filebrowser_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        filebrowser_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "filebrowser2.{{ user.domain }}"
          - "filebrowser.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        filebrowser_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'filebrowser2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

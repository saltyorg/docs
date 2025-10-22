---
hide:
  - tags
tags:
  - navidrome
  - media
  - music
---

# Navidrome

## What is it?

[Navidrome](https://www.navidrome.org/) allows you to enjoy your music collection from anywhere, by making it available through a modern Web UI and through a wide range of third-party compatible mobile apps, for both iOS and Android devices.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.navidrome.org/){: .header-icons } | [:octicons-link-16: Docs](https://www.navidrome.org/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/navidrome/navidrome/issues){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/deluan/navidrome){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-navidrome

```

### 2. URL

- To access Navidrome, visit `https://navidrome.xDOMAIN_NAMEx`

### 3. Setup

- After installing Navidrome in your platform, you need to create your first user. This will be your admin user, a super user that can manage all aspects of Navidrome, including the ability to manage other users. Just browse to Navidrome’s homepage at`https://navidrome.xDOMAIN_NAMEx` and you will be greeted with a screen like this: <br />

     ![](../../images/community/navidrome_first_user.png)

    Just fill out the username and password you want to use, confirm the password and click on the “Create Admin” button.

    That’s it! You should now be able to browse and listen to all your music.

    !!! Note
             It usually take a couple of minutes for your music to start appearing in Navidrome’s UI. <br />
             You can check the logs to see what is the scan progress. If you have a large library this may take some time.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        navidrome_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `navidrome_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `navidrome_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    navidrome_name: navidrome

    ```

??? example "Paths"

    ```yaml
    # Type: string
    navidrome_role_paths_folder: "{{ navidrome_name }}"

    # Type: string
    navidrome_role_paths_location: "{{ server_appdata_path }}/{{ navidrome_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    navidrome_role_web_subdomain: "{{ navidrome_name }}"

    # Type: string
    navidrome_role_web_domain: "{{ user.domain }}"

    # Type: string
    navidrome_role_web_port: "4533"

    # Type: string
    navidrome_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='navidrome') + '.' + lookup('role_var', '_web_domain', role='navidrome')
                             if (lookup('role_var', '_web_subdomain', role='navidrome') | length > 0)
                             else lookup('role_var', '_web_domain', role='navidrome')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    navidrome_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='navidrome') }}"

    # Type: string
    navidrome_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='navidrome') }}"

    # Type: bool (true/false)
    navidrome_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    navidrome_role_traefik_sso_middleware: ""

    # Type: string
    navidrome_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    navidrome_role_traefik_middleware_custom: ""

    # Type: string
    navidrome_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    navidrome_role_traefik_enabled: true

    # Type: bool (true/false)
    navidrome_role_traefik_api_enabled: false

    # Type: string
    navidrome_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    navidrome_role_docker_container: "{{ navidrome_name }}"

    # Image
    # Type: bool (true/false)
    navidrome_role_docker_image_pull: true

    # Type: string
    navidrome_role_docker_image_tag: "latest"

    # Type: string
    navidrome_role_docker_image_repo: "deluan/navidrome"

    # Type: string
    navidrome_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='navidrome') }}:{{ lookup('role_var', '_docker_image_tag', role='navidrome') }}"

    # Volumes
    # Type: list
    navidrome_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='navidrome') }}:/data"
      - "/mnt/unionfs/Media/Music:/music"

    # Type: list
    navidrome_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    navidrome_role_docker_hostname: "{{ navidrome_name }}"

    # Networks
    # Type: string
    navidrome_role_docker_networks_alias: "{{ navidrome_name }}"

    # Type: list
    navidrome_role_docker_networks_default: []

    # Type: list
    navidrome_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    navidrome_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    navidrome_role_docker_state: started

    # User
    # Type: string
    navidrome_role_docker_user: "{{ uid }}:{{ gid }}"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    navidrome_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    navidrome_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    navidrome_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    navidrome_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    navidrome_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    navidrome_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    navidrome_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    navidrome_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    navidrome_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    navidrome_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    navidrome_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    navidrome_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    navidrome_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    navidrome_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    navidrome_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    navidrome_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    navidrome_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        navidrome_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "navidrome2.{{ user.domain }}"
          - "navidrome.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        navidrome_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'navidrome2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

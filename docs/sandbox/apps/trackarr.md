---
hide:
  - tags
tags:
  - trackarr
  - automation
  - tracker
---

# Trackarr

## What is it?

[Trackarr](https://gitlab.com/cloudb0x/trackarr) monitors tracker announce IRC channel, parses the announcements, and forwards those announcements to ARR PVRs (eg Sonarr/Radarr).

!!! info
    By default, the role is **NOT** protected behind your Authelia/SSO middleware. You will have to log into the app itself (basic auth).

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://gitlab.com/cloudb0x/trackarr){: .header-icons } | [:octicons-link-16: Docs](https://gitlab.com/cloudb0x/trackarr/-/wikis/Configuration){: .header-icons } | [:octicons-mark-github-16: Gitlab](https://gitlab.com/cloudb0x/trackarr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/cloudb0x/trackarr){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-trackarr
```

### 2. Setup

- Default login:

  ``` { .yaml}
  Username: "your user from accounts.yml"
  Password: your_normal_password
  ```

The `trackarr` role will provision a config file with your pvr and server info. After you run the role, you will need to set up your config. [Here](https://gitlab.com/cloudb0x/trackarr/-/wikis/Configuration/Sample) is an example config from the wiki that has a broader example of possible options and tracker configuration.

### 3. URL

- To access Trackarr, visit `https://trackarr.xDOMAIN_NAMEx`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        trackarr_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `trackarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `trackarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    trackarr_name: trackarr

    ```

??? example "Paths"

    ```yaml
    # Type: string
    trackarr_role_paths_folder: "{{ trackarr_name }}"

    # Type: string
    trackarr_role_paths_location: "{{ server_appdata_path }}/{{ trackarr_role_paths_folder }}"

    # Type: string
    trackarr_role_paths_config_location: "{{ trackarr_role_paths_location }}/config.yaml"

    ```

??? example "Web"

    ```yaml
    # Type: string
    trackarr_role_web_subdomain: "{{ trackarr_name }}"

    # Type: string
    trackarr_role_web_domain: "{{ user.domain }}"

    # Type: string
    trackarr_role_web_port: "7337"

    # Type: string
    trackarr_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='trackarr') + '.' + lookup('role_var', '_web_domain', role='trackarr')
                            if (lookup('role_var', '_web_subdomain', role='trackarr') | length > 0)
                            else lookup('role_var', '_web_domain', role='trackarr')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    trackarr_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='trackarr') }}"

    # Type: string
    trackarr_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='trackarr') }}"

    # Type: bool (true/false)
    trackarr_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    trackarr_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    trackarr_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    trackarr_role_traefik_middleware_custom: ""

    # Type: string
    trackarr_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    trackarr_role_traefik_enabled: true

    # Type: bool (true/false)
    trackarr_role_traefik_api_enabled: false

    # Type: string
    trackarr_role_traefik_api_endpoint: ""

    ```

??? example "API"

    ```yaml
    # default to blank
    # Type: null
    trackarr_server_apikey: 

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    trackarr_role_docker_container: "{{ trackarr_name }}"

    # Image
    # Type: bool (true/false)
    trackarr_role_docker_image_pull: true

    # Type: string
    trackarr_role_docker_image_repo: "cloudb0x/trackarr"

    # Type: string
    trackarr_role_docker_image_tag: "latest"

    # Type: string
    trackarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='trackarr') }}:{{ lookup('role_var', '_docker_image_tag', role='trackarr') }}"

    # Envs
    # Type: string
    trackarr_role_docker_envs_log_level: "1"

    # Type: dict
    trackarr_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"
      VERBOSE: "{{ lookup('role_var', '_docker_envs_log_level', role='trackarr') }}"

    # Type: dict
    trackarr_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    trackarr_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='trackarr') }}:/config"

    # Type: list
    trackarr_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    trackarr_role_docker_hostname: "{{ trackarr_name }}"

    # Networks
    # Type: string
    trackarr_role_docker_networks_alias: "{{ trackarr_name }}"

    # Type: list
    trackarr_role_docker_networks_default: []

    # Type: list
    trackarr_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    trackarr_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    trackarr_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    trackarr_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    trackarr_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    trackarr_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    trackarr_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    trackarr_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    trackarr_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    trackarr_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    trackarr_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    trackarr_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    trackarr_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    trackarr_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    trackarr_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    trackarr_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    trackarr_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    trackarr_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    trackarr_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    trackarr_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        trackarr_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "trackarr2.{{ user.domain }}"
          - "trackarr.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        trackarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'trackarr2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

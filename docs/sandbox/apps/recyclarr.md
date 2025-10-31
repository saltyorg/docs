---
hide:
  - tags
tags:
  - recyclarr
  - sonarr
  - radarr
---

# Recyclarr

[Recyclarr](https://github.com/recyclarr/recyclarr) automatically synchronizes recommended settings from TRaSH guides to your Sonarr/Radarr instances.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/recyclarr/recyclarr){: .header-icons } | [:octicons-link-16: Docs](https://recyclarr.dev/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/recyclarr/recyclarr){: .header-icons } | [:material-docker: Docker](https://ghcr.io/recyclarr/recyclarr){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-recyclarr

```

### 2. Setup

Edit the Recyclarr section in [sandbox `settings.yml`:](../settings.md) and enter your desired update schedule using standard cron syntax.

``` { .yaml }
     recyclarr:
       cron_schedule: "@daily"
```

!!! note
    If you change this value, you must re-run `sb install sandbox-recyclarr` for it take effect.

If a config file does not exist, a default config is generated but it is not functional out of the box. Edit the file `/opt/recyclarr/recyclarr.yml` to provision your Sonarr/Radarr details and preferred settings.

- Configure Sonarr section

  ``` { .yaml }
      sonarr:
        sonarr:
          base_url: http://sonarr:8989
          api_key: your_sonarr_api_key
  ```

- Configure Radarr section

  ``` { .yaml }
      radarr:
        radarr:
          base_url: http://radarr:7878
          api_key: your_radarr_api_key
  ```

Follow documentation to complete configuration

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    recyclarr_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `recyclarr_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `recyclarr_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`recyclarr_name`"

        ```yaml
        # Type: string
        recyclarr_name: recyclarr
        ```

=== "Settings"

    ??? variable string "`recyclarr_role_cron_schedule`"

        ```yaml
        # Type: string
        recyclarr_role_cron_schedule: "@daily"
        ```

=== "Paths"

    ??? variable string "`recyclarr_role_paths_folder`"

        ```yaml
        # Type: string
        recyclarr_role_paths_folder: "{{ recyclarr_name }}"
        ```

    ??? variable string "`recyclarr_role_paths_location`"

        ```yaml
        # Type: string
        recyclarr_role_paths_location: "{{ server_appdata_path }}/{{ recyclarr_role_paths_folder }}"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`recyclarr_role_docker_container`"

        ```yaml
        # Type: string
        recyclarr_role_docker_container: "{{ recyclarr_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`recyclarr_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        recyclarr_role_docker_image_pull: true
        ```

    ??? variable string "`recyclarr_role_docker_image_repo`"

        ```yaml
        # Type: string
        recyclarr_role_docker_image_repo: "ghcr.io/recyclarr/recyclarr"
        ```

    ??? variable string "`recyclarr_role_docker_image_tag`"

        ```yaml
        # Type: string
        recyclarr_role_docker_image_tag: "latest"
        ```

    ??? variable string "`recyclarr_role_docker_image`"

        ```yaml
        # Type: string
        recyclarr_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='recyclarr') }}:{{ lookup('role_var', '_docker_image_tag', role='recyclarr') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`recyclarr_role_docker_envs_default`"

        ```yaml
        # Type: dict
        recyclarr_role_docker_envs_default: 
          TZ: "{{ tz }}"
          CRON_SCHEDULE: "{{ lookup('role_var', '_cron_schedule', role='recyclarr') }}"
          RECYCLARR_CREATE_CONFIG: "true"
        ```

    ??? variable dict "`recyclarr_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        recyclarr_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`recyclarr_role_docker_volumes_default`"

        ```yaml
        # Type: list
        recyclarr_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='recyclarr') }}:/config"
        ```

    ??? variable list "`recyclarr_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        recyclarr_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`recyclarr_role_docker_hostname`"

        ```yaml
        # Type: string
        recyclarr_role_docker_hostname: "{{ recyclarr_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`recyclarr_role_docker_networks_alias`"

        ```yaml
        # Type: string
        recyclarr_role_docker_networks_alias: "{{ recyclarr_name }}"
        ```

    ??? variable list "`recyclarr_role_docker_networks_default`"

        ```yaml
        # Type: list
        recyclarr_role_docker_networks_default: []
        ```

    ??? variable list "`recyclarr_role_docker_networks_custom`"

        ```yaml
        # Type: list
        recyclarr_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`recyclarr_role_docker_restart_policy`"

        ```yaml
        # Type: string
        recyclarr_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`recyclarr_role_docker_state`"

        ```yaml
        # Type: string
        recyclarr_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`recyclarr_role_docker_user`"

        ```yaml
        # Type: string
        recyclarr_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`recyclarr_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        recyclarr_role_autoheal_enabled: true
        ```

    ??? variable string "`recyclarr_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        recyclarr_role_depends_on: ""
        ```

    ??? variable string "`recyclarr_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        recyclarr_role_depends_on_delay: "0"
        ```

    ??? variable string "`recyclarr_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        recyclarr_role_depends_on_healthchecks:
        ```

    ??? variable bool "`recyclarr_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        recyclarr_role_diun_enabled: true
        ```

    ??? variable bool "`recyclarr_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        recyclarr_role_dns_enabled: true
        ```

    ??? variable bool "`recyclarr_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        recyclarr_role_docker_controller: true
        ```

    ??? variable bool "`recyclarr_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        recyclarr_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`recyclarr_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        recyclarr_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`recyclarr_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        recyclarr_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`recyclarr_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        recyclarr_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`recyclarr_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        recyclarr_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`recyclarr_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        recyclarr_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`recyclarr_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        recyclarr_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`recyclarr_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        recyclarr_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`recyclarr_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        recyclarr_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`recyclarr_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        recyclarr_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            recyclarr_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "recyclarr2.{{ user.domain }}"
              - "recyclarr.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`recyclarr_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        recyclarr_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            recyclarr_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'recyclarr2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`recyclarr_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        recyclarr_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
---
icon: material/docker
hide:
  - tags
tags:
  - kometa
  - pmm
  - plex meta manager
---

# Kometa

## Overview

[Kometa](https://github.com/Kometa-Team/Kometa) can update many metadata fields for movies, shows, collections, seasons, and episodes and can act as a backup if your plex DB goes down. It can even update metadata the plex UI can't like Season Names. If the time is put into the metadata configuration file you can have a way to recreate your library and all its metadata changes with the click of a button.

!!! info
    Kometa is the replacement for Plex Meta Manager. A simple migration for your appdata is available by running `sb install sandbox-pmm-kometa-migration`.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/Kometa-Team/Kometa){: .header-icons } | [:octicons-link-16: Docs](https://kometa.wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Kometa-Team/Kometa){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/kometateam/kometa){: .header-icons }|

### 1. Installation

You will need to create a config file prior to running the tag:

`/opt/kometa/config.yml`

There is a Docker-based walkthrough on the Kometa wiki [here](https://kometa.wiki/en/latest/kometa/install/docker/) that you can use to learn how to create this file. Once you've created it, move the file into `/opt/kometa/` and then run the tag.

``` shell
sb install sandbox-kometa
```

### 2. Setup

To configure the time that Kometa should run, you may override the `kometa_time` variable via the [inventory system](../../saltbox/inventory/index.md). The default is `"03:00"` or 3:00 AM in the server's time zone.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `kometa_instances`.

    ```yaml { .sb-show-on-unchecked title="Applies to all instances of kometa:" }
    kometa_role_web_subdomain: "custom"
    ```

    ```yaml { .sb-show-on-checked title="Applies to a specific instance (e.g., `kometa2`):" }
    kometa2_web_subdomain: "custom2"
    ```

<label class="md-button md-button--stretch" for="sb-checkbox--var-level">
   <input type="checkbox" id="sb-checkbox--var-level"><span class="sb-show-on-unchecked">Show instance-level variables</span><span class="sb-show-on-checked">Show role-level variables</span>
</label>

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `kometa_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `kometa_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`kometa_instances`"

        ```yaml
        # Type: list
        kometa_instances: ["kometa"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            kometa_instances: ["kometa", "kometa2"]
            ```

=== "Settings"

    ??? variable string "`kometa_role_time`{ .sb-show-on-unchecked }`kometa2_time`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        kometa_role_time: "03:00"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        kometa2_time: "03:00"
        ```

=== "Paths"

    ??? variable string "`kometa_role_paths_folder`{ .sb-show-on-unchecked }`kometa2_paths_folder`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        kometa_role_paths_folder: "{{ kometa_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        kometa2_paths_folder: "{{ kometa_name }}"
        ```

    ??? variable string "`kometa_role_paths_location`{ .sb-show-on-unchecked }`kometa2_paths_location`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        kometa_role_paths_location: "{{ server_appdata_path }}/{{ kometa_role_paths_folder }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        kometa2_paths_location: "{{ server_appdata_path }}/{{ kometa_role_paths_folder }}"
        ```

    ??? variable bool "`kometa_role_paths_recursive`{ .sb-show-on-unchecked }`kometa2_paths_recursive`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        kometa_role_paths_recursive: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        kometa2_paths_recursive: true
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`kometa_role_docker_container`{ .sb-show-on-unchecked }`kometa2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        kometa_role_docker_container: "{{ kometa_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        kometa2_docker_container: "{{ kometa_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`kometa_role_docker_image_pull`{ .sb-show-on-unchecked }`kometa2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        kometa_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        kometa2_docker_image_pull: true
        ```

    ??? variable string "`kometa_role_docker_image_repo`{ .sb-show-on-unchecked }`kometa2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        kometa_role_docker_image_repo: "kometateam/kometa"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        kometa2_docker_image_repo: "kometateam/kometa"
        ```

    ??? variable string "`kometa_role_docker_image_tag`{ .sb-show-on-unchecked }`kometa2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        kometa_role_docker_image_tag: "latest"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        kometa2_docker_image_tag: "latest"
        ```

    ??? variable string "`kometa_role_docker_image`{ .sb-show-on-unchecked }`kometa2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        kometa_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='kometa') }}:{{ lookup('role_var', '_docker_image_tag', role='kometa') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        kometa2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='kometa') }}:{{ lookup('role_var', '_docker_image_tag', role='kometa') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`kometa_role_docker_envs_default`{ .sb-show-on-unchecked }`kometa2_docker_envs_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        kometa_role_docker_envs_default:
          TZ: "{{ tz }}"
          LOG_LEVEL: "DEBUG"
          KOMETA_TIMES: "{{ lookup('role_var', '_time', role='kometa') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        kometa2_docker_envs_default: 
          TZ: "{{ tz }}"
          LOG_LEVEL: "DEBUG"
          KOMETA_TIMES: "{{ lookup('role_var', '_time', role='kometa') }}"
        ```

    ??? variable dict "`kometa_role_docker_envs_custom`{ .sb-show-on-unchecked }`kometa2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        kometa_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        kometa2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`kometa_role_docker_volumes_default`{ .sb-show-on-unchecked }`kometa2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        kometa_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='kometa') }}:/config"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        kometa2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='kometa') }}:/config"
        ```

    ??? variable list "`kometa_role_docker_volumes_custom`{ .sb-show-on-unchecked }`kometa2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        kometa_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        kometa2_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`kometa_role_docker_hostname`{ .sb-show-on-unchecked }`kometa2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        kometa_role_docker_hostname: "{{ kometa_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        kometa2_docker_hostname: "{{ kometa_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`kometa_role_docker_networks_alias`{ .sb-show-on-unchecked }`kometa2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        kometa_role_docker_networks_alias: "{{ kometa_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        kometa2_docker_networks_alias: "{{ kometa_name }}"
        ```

    ??? variable list "`kometa_role_docker_networks_default`{ .sb-show-on-unchecked }`kometa2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        kometa_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        kometa2_docker_networks_default: []
        ```

    ??? variable list "`kometa_role_docker_networks_custom`{ .sb-show-on-unchecked }`kometa2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        kometa_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        kometa2_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`kometa_role_docker_restart_policy`{ .sb-show-on-unchecked }`kometa2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        kometa_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        kometa2_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`kometa_role_docker_state`{ .sb-show-on-unchecked }`kometa2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        kometa_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        kometa2_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`kometa_role_docker_user`{ .sb-show-on-unchecked }`kometa2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        kometa_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        kometa2_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`kometa_role_autoheal_enabled`{ .sb-show-on-unchecked }`kometa2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        kometa_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        kometa2_autoheal_enabled: true
        ```

    ??? variable string "`kometa_role_depends_on`{ .sb-show-on-unchecked }`kometa2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        kometa_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        kometa2_depends_on: ""
        ```

    ??? variable string "`kometa_role_depends_on_delay`{ .sb-show-on-unchecked }`kometa2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        kometa_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        kometa2_depends_on_delay: "0"
        ```

    ??? variable string "`kometa_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`kometa2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        kometa_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        kometa2_depends_on_healthchecks:
        ```

    ??? variable bool "`kometa_role_diun_enabled`{ .sb-show-on-unchecked }`kometa2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        kometa_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        kometa2_diun_enabled: true
        ```

    ??? variable bool "`kometa_role_dns_enabled`{ .sb-show-on-unchecked }`kometa2_dns_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        kometa_role_dns_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        kometa2_dns_enabled: true
        ```

    ??? variable bool "`kometa_role_docker_controller`{ .sb-show-on-unchecked }`kometa2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        kometa_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        kometa2_docker_controller: true
        ```

    ??? variable bool "`kometa_role_docker_volumes_download`{ .sb-show-on-unchecked }`kometa2_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        kometa_role_docker_volumes_download:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        kometa2_docker_volumes_download:
        ```

    ??? variable bool "`kometa_role_traefik_autodetect_enabled`{ .sb-show-on-unchecked }`kometa2_traefik_autodetect_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        kometa_role_traefik_autodetect_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        kometa2_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`kometa_role_traefik_crowdsec_enabled`{ .sb-show-on-unchecked }`kometa2_traefik_crowdsec_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        kometa_role_traefik_crowdsec_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        kometa2_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`kometa_role_traefik_error_pages_enabled`{ .sb-show-on-unchecked }`kometa2_traefik_error_pages_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        kometa_role_traefik_error_pages_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        kometa2_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`kometa_role_traefik_gzip_enabled`{ .sb-show-on-unchecked }`kometa2_traefik_gzip_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        kometa_role_traefik_gzip_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        kometa2_traefik_gzip_enabled: false
        ```

    ??? variable bool "`kometa_role_traefik_middleware_http_api_insecure`{ .sb-show-on-unchecked }`kometa2_traefik_middleware_http_api_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        kometa_role_traefik_middleware_http_api_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        kometa2_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`kometa_role_traefik_middleware_http_insecure`{ .sb-show-on-unchecked }`kometa2_traefik_middleware_http_insecure`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        kometa_role_traefik_middleware_http_insecure:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        kometa2_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`kometa_role_traefik_robot_enabled`{ .sb-show-on-unchecked }`kometa2_traefik_robot_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        kometa_role_traefik_robot_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        kometa2_traefik_robot_enabled: true
        ```

    ??? variable bool "`kometa_role_traefik_tailscale_enabled`{ .sb-show-on-unchecked }`kometa2_traefik_tailscale_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        kometa_role_traefik_tailscale_enabled: false
        ```

        ```yaml { .sb-show-on-checked }
        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        kometa2_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`kometa_role_traefik_wildcard_enabled`{ .sb-show-on-unchecked }`kometa2_traefik_wildcard_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        kometa_role_traefik_wildcard_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        kometa2_traefik_wildcard_enabled: true
        ```

    ??? variable list "`kometa_role_web_fqdn_override`{ .sb-show-on-unchecked }`kometa2_web_fqdn_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        kometa_role_web_fqdn_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        kometa2_web_fqdn_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            kometa_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "kometa2.{{ user.domain }}"
              - "kometa.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            kometa2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "kometa2.{{ user.domain }}"
              - "kometa.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`kometa_role_web_host_override`{ .sb-show-on-unchecked }`kometa2_web_host_override`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Override the Traefik web host configuration for containers
        # Type: string
        kometa_role_web_host_override:
        ```

        ```yaml { .sb-show-on-checked }
        # Override the Traefik web host configuration for containers
        # Type: string
        kometa2_web_host_override:
        ```

        !!! example sb-show-on-unchecked "Example Override"

            ```yaml
            kometa_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'kometa2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        !!! example sb-show-on-checked "Example Override"

            ```yaml
            kometa2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'kometa2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`kometa_role_web_scheme`{ .sb-show-on-unchecked }`kometa2_web_scheme`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        kometa_role_web_scheme:
        ```

        ```yaml { .sb-show-on-checked }
        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        kometa2_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
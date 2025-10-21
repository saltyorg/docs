---
hide:
  - tags
tags:
  - kometa
  - pmm
  - plex meta manager
---

# Kometa

## What is it?

[Kometa](https://github.com/Kometa-Team/Kometa) can update many metadata fields for movies, shows, collections, seasons, and episodes and can act as a backup if your plex DB goes down. It can even update metadata the plex UI can't like Season Names. If the time is put into the metadata configuration file you can have a way to recreate your library and all its metadata changes with the click of a button.

!!! info
    Kometa is the replacement for Plex Meta Manager. A simple migration for your appdata is available by running `sb install sandbox-pmm-kometa-migration`.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/Kometa-Team/Kometa){: .header-icons } | [:octicons-link-16: Docs](https://kometa.wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Kometa-Team/Kometa){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/kometateam/kometa){: .header-icons }|

### 1. Installation

You will need to create a config file prior to running the tag:

`/opt/kometa/config.yml`

There is a Docker-based walkthrough on the Kometa wiki [here](https://kometa.wiki/en/latest/kometa/install/docker/) that you can use to learn how to create this file.  Once you've created it, move the file into `/opt/kometa/` and then run the tag.

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

    === "Role-level Override"

        Applies to all instances of kometa:

        ```yaml
        kometa_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `kometa2`):

        ```yaml
        kometa2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `kometa_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `kometa_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`kometa_instances`"

        ```yaml
        # Type: list
        kometa_instances: ["kometa"]
        ```

        !!! example

            ```yaml
            # Type: list
            kometa_instances: ["kometa", "kometa2"]
            ```

=== "Settings"

    === "Role-level"

        ??? variable string "`kometa_role_time`"

            ```yaml
            # Type: string
            kometa_role_time: "03:00"
            ```

    === "Instance-level"

        ??? variable string "`kometa2_time`"

            ```yaml
            # Type: string
            kometa2_time: "03:00"
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`kometa_role_paths_folder`"

            ```yaml
            # Type: string
            kometa_role_paths_folder: "{{ kometa_name }}"
            ```

        ??? variable string "`kometa_role_paths_location`"

            ```yaml
            # Type: string
            kometa_role_paths_location: "{{ server_appdata_path }}/{{ kometa_role_paths_folder }}"
            ```

        ??? variable bool "`kometa_role_paths_recursive`"

            ```yaml
            # Type: bool (true/false)
            kometa_role_paths_recursive: true
            ```

    === "Instance-level"

        ??? variable string "`kometa2_paths_folder`"

            ```yaml
            # Type: string
            kometa2_paths_folder: "{{ kometa_name }}"
            ```

        ??? variable string "`kometa2_paths_location`"

            ```yaml
            # Type: string
            kometa2_paths_location: "{{ server_appdata_path }}/{{ kometa_role_paths_folder }}"
            ```

        ??? variable bool "`kometa2_paths_recursive`"

            ```yaml
            # Type: bool (true/false)
            kometa2_paths_recursive: true
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`kometa_role_docker_container`"

            ```yaml
            # Type: string
            kometa_role_docker_container: "{{ kometa_name }}"
            ```

        ##### Image

        ??? variable bool "`kometa_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            kometa_role_docker_image_pull: true
            ```

        ??? variable string "`kometa_role_docker_image_repo`"

            ```yaml
            # Type: string
            kometa_role_docker_image_repo: "kometateam/kometa"
            ```

        ??? variable string "`kometa_role_docker_image_tag`"

            ```yaml
            # Type: string
            kometa_role_docker_image_tag: "latest"
            ```

        ??? variable string "`kometa_role_docker_image`"

            ```yaml
            # Type: string
            kometa_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='kometa') }}:{{ lookup('role_var', '_docker_image_tag', role='kometa') }}"
            ```

        ##### Envs

        ??? variable dict "`kometa_role_docker_envs_default`"

            ```yaml
            # Type: dict
            kometa_role_docker_envs_default: 
              TZ: "{{ tz }}"
              LOG_LEVEL: "DEBUG"
              KOMETA_TIMES: "{{ lookup('role_var', '_time', role='kometa') }}"
            ```

        ??? variable dict "`kometa_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            kometa_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`kometa_role_docker_volumes_default`"

            ```yaml
            # Type: list
            kometa_role_docker_volumes_default: 
              - "{{ lookup('role_var', '_paths_location', role='kometa') }}:/config"
            ```

        ??? variable list "`kometa_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            kometa_role_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`kometa_role_docker_hostname`"

            ```yaml
            # Type: string
            kometa_role_docker_hostname: "{{ kometa_name }}"
            ```

        ##### Networks

        ??? variable string "`kometa_role_docker_networks_alias`"

            ```yaml
            # Type: string
            kometa_role_docker_networks_alias: "{{ kometa_name }}"
            ```

        ??? variable list "`kometa_role_docker_networks_default`"

            ```yaml
            # Type: list
            kometa_role_docker_networks_default: []
            ```

        ??? variable list "`kometa_role_docker_networks_custom`"

            ```yaml
            # Type: list
            kometa_role_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`kometa_role_docker_restart_policy`"

            ```yaml
            # Type: string
            kometa_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`kometa_role_docker_state`"

            ```yaml
            # Type: string
            kometa_role_docker_state: started
            ```

        ##### User

        ??? variable string "`kometa_role_docker_user`"

            ```yaml
            # Type: string
            kometa_role_docker_user: "{{ uid }}:{{ gid }}"
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`kometa2_docker_container`"

            ```yaml
            # Type: string
            kometa2_docker_container: "{{ kometa_name }}"
            ```

        ##### Image

        ??? variable bool "`kometa2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            kometa2_docker_image_pull: true
            ```

        ??? variable string "`kometa2_docker_image_repo`"

            ```yaml
            # Type: string
            kometa2_docker_image_repo: "kometateam/kometa"
            ```

        ??? variable string "`kometa2_docker_image_tag`"

            ```yaml
            # Type: string
            kometa2_docker_image_tag: "latest"
            ```

        ??? variable string "`kometa2_docker_image`"

            ```yaml
            # Type: string
            kometa2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='kometa') }}:{{ lookup('role_var', '_docker_image_tag', role='kometa') }}"
            ```

        ##### Envs

        ??? variable dict "`kometa2_docker_envs_default`"

            ```yaml
            # Type: dict
            kometa2_docker_envs_default: 
              TZ: "{{ tz }}"
              LOG_LEVEL: "DEBUG"
              KOMETA_TIMES: "{{ lookup('role_var', '_time', role='kometa') }}"
            ```

        ??? variable dict "`kometa2_docker_envs_custom`"

            ```yaml
            # Type: dict
            kometa2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable list "`kometa2_docker_volumes_default`"

            ```yaml
            # Type: list
            kometa2_docker_volumes_default: 
              - "{{ lookup('role_var', '_paths_location', role='kometa') }}:/config"
            ```

        ??? variable list "`kometa2_docker_volumes_custom`"

            ```yaml
            # Type: list
            kometa2_docker_volumes_custom: []
            ```

        ##### Hostname

        ??? variable string "`kometa2_docker_hostname`"

            ```yaml
            # Type: string
            kometa2_docker_hostname: "{{ kometa_name }}"
            ```

        ##### Networks

        ??? variable string "`kometa2_docker_networks_alias`"

            ```yaml
            # Type: string
            kometa2_docker_networks_alias: "{{ kometa_name }}"
            ```

        ??? variable list "`kometa2_docker_networks_default`"

            ```yaml
            # Type: list
            kometa2_docker_networks_default: []
            ```

        ??? variable list "`kometa2_docker_networks_custom`"

            ```yaml
            # Type: list
            kometa2_docker_networks_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`kometa2_docker_restart_policy`"

            ```yaml
            # Type: string
            kometa2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`kometa2_docker_state`"

            ```yaml
            # Type: string
            kometa2_docker_state: started
            ```

        ##### User

        ??? variable string "`kometa2_docker_user`"

            ```yaml
            # Type: string
            kometa2_docker_user: "{{ uid }}:{{ gid }}"
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`kometa_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            kometa_role_autoheal_enabled: true
            ```

        ??? variable string "`kometa_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            kometa_role_depends_on: ""
            ```

        ??? variable string "`kometa_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            kometa_role_depends_on_delay: "0"
            ```

        ??? variable string "`kometa_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            kometa_role_depends_on_healthchecks:
            ```

        ??? variable bool "`kometa_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            kometa_role_diun_enabled: true
            ```

        ??? variable bool "`kometa_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            kometa_role_dns_enabled: true
            ```

        ??? variable bool "`kometa_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            kometa_role_docker_controller: true
            ```

        ??? variable bool "`kometa_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            kometa_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`kometa_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            kometa_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`kometa_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            kometa_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`kometa_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            kometa_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`kometa_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            kometa_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`kometa_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            kometa_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`kometa_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            kometa_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`kometa_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            kometa_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                kometa_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "kometa2.{{ user.domain }}"
                  - "kometa.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`kometa_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            kometa_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                kometa_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'kometa2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`kometa_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            kometa_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `kometa2`):

        ??? variable bool "`kometa2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            kometa2_autoheal_enabled: true
            ```

        ??? variable string "`kometa2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            kometa2_depends_on: ""
            ```

        ??? variable string "`kometa2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            kometa2_depends_on_delay: "0"
            ```

        ??? variable string "`kometa2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            kometa2_depends_on_healthchecks:
            ```

        ??? variable bool "`kometa2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            kometa2_diun_enabled: true
            ```

        ??? variable bool "`kometa2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            kometa2_dns_enabled: true
            ```

        ??? variable bool "`kometa2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            kometa2_docker_controller: true
            ```

        ??? variable bool "`kometa2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            kometa2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`kometa2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            kometa2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`kometa2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            kometa2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`kometa2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            kometa2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`kometa2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            kometa2_traefik_robot_enabled: true
            ```

        ??? variable bool "`kometa2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            kometa2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`kometa2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            kometa2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`kometa2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            kometa2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                kometa2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "kometa2.{{ user.domain }}"
                  - "kometa.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`kometa2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            kometa2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                kometa2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'kometa2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`kometa2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            kometa2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
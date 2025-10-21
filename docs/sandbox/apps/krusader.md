---
hide:
  - tags
tags:
  - krusader
  - file-management
  - admin
---

# Krusader

## What is it?

[Krusader](http://www.krusader.org/) is an advanced orthodox file manager for KDE and other desktops in the Unix world. It is similar to the console-based GNU Midnight Commander, GNOME Commander for the GNOME desktop environment, or Total Commander for Windows, all of which can trace their paradigmatic features to the original Norton Commander for DOS. It supports extensive archive handling, mounted filesystem support, FTP, advanced search, viewer/editor, directory synchronisation, file content comparisons, batch renaming, etc.

This is a Docker container for Krusader.

The GUI of the application is accessed through a modern web browser (no installation or configuration needed on the client side).

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](http://www.krusader.org/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/binhex/arch-krusader){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/binhex/arch-krusader){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/binhex/arch-krusader){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-krusader

```

### 2. URL

- To access Krusader, visit `https://krusader._yourdomain.com_`
- Now you can click on vnc.html or vnc_lite.html

### 3. Setup

- The configured password are taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`
- /mnt is already mounted to /mnt

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        krusader_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `krusader_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `krusader_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`krusader_name`"

        ```yaml
        # Type: string
        krusader_name: krusader
        ```

=== "Docker Socket Proxy"

    ??? variable dict "`krusader_role_docker_socket_proxy_envs`"

        ```yaml
        # Type: dict
        krusader_role_docker_socket_proxy_envs: 
          CONTAINERS: "1"
          POST: "0"
        ```

=== "Paths"

    ??? variable string "`krusader_role_paths_folder`"

        ```yaml
        # Type: string
        krusader_role_paths_folder: "{{ krusader_name }}"
        ```

    ??? variable string "`krusader_role_paths_location`"

        ```yaml
        # Type: string
        krusader_role_paths_location: "{{ server_appdata_path }}/{{ krusader_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`krusader_role_web_subdomain`"

        ```yaml
        # Type: string
        krusader_role_web_subdomain: "{{ krusader_name }}"
        ```

    ??? variable string "`krusader_role_web_domain`"

        ```yaml
        # Type: string
        krusader_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`krusader_role_web_port`"

        ```yaml
        # Type: string
        krusader_role_web_port: "6080"
        ```

    ??? variable string "`krusader_role_web_url`"

        ```yaml
        # Type: string
        krusader_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='krusader') + '.' + lookup('role_var', '_web_domain', role='krusader')
                                if (lookup('role_var', '_web_subdomain', role='krusader') | length > 0)
                                else lookup('role_var', '_web_domain', role='krusader')) }}"
        ```

=== "DNS"

    ??? variable string "`krusader_role_dns_record`"

        ```yaml
        # Type: string
        krusader_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='krusader') }}"
        ```

    ??? variable string "`krusader_role_dns_zone`"

        ```yaml
        # Type: string
        krusader_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='krusader') }}"
        ```

    ??? variable bool "`krusader_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        krusader_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`krusader_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        krusader_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`krusader_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        krusader_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`krusader_role_traefik_middleware_api`"

        ```yaml
        # Type: string
        krusader_role_traefik_middleware_api: "{{ traefik_global_middleware }}"
        ```

    ??? variable string "`krusader_role_traefik_certresolver`"

        ```yaml
        # Type: string
        krusader_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`krusader_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        krusader_role_traefik_enabled: true
        ```

    ??? variable bool "`krusader_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        krusader_role_traefik_api_enabled: false
        ```

    ??? variable string "`krusader_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        krusader_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`krusader_role_docker_container`"

        ```yaml
        # Type: string
        krusader_role_docker_container: "{{ krusader_name }}"
        ```

    ##### Image

    ??? variable bool "`krusader_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        krusader_role_docker_image_pull: true
        ```

    ??? variable string "`krusader_role_docker_image_tag`"

        ```yaml
        # Type: string
        krusader_role_docker_image_tag: "latest"
        ```

    ??? variable string "`krusader_role_docker_image_repo`"

        ```yaml
        # Type: string
        krusader_role_docker_image_repo: "binhex/arch-krusader"
        ```

    ??? variable string "`krusader_role_docker_image`"

        ```yaml
        # Type: string
        krusader_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='krusader') }}:{{ lookup('role_var', '_docker_image_tag', role='krusader') }}"
        ```

    ##### Envs

    ??? variable dict "`krusader_role_docker_envs_default`"

        ```yaml
        # Type: dict
        krusader_role_docker_envs_default: 
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          VNC_PASSWORD: "{{ user.pass }}"
          DOCKER_HOST: "tcp://{{ krusader_name }}-docker-socket-proxy:2375"
          WEBPAGE_TITLE: "Krusader File Manager Web"
          TEMP_FOLDER: "/tmp"
        ```

    ??? variable dict "`krusader_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        krusader_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`krusader_role_docker_volumes_default`"

        ```yaml
        # Type: list
        krusader_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='krusader') }}/config:/config"
        ```

    ??? variable list "`krusader_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        krusader_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`krusader_role_docker_hostname`"

        ```yaml
        # Type: string
        krusader_role_docker_hostname: "{{ krusader_name }}"
        ```

    ##### Networks

    ??? variable string "`krusader_role_docker_networks_alias`"

        ```yaml
        # Type: string
        krusader_role_docker_networks_alias: "{{ krusader_name }}"
        ```

    ??? variable list "`krusader_role_docker_networks_default`"

        ```yaml
        # Type: list
        krusader_role_docker_networks_default: []
        ```

    ??? variable list "`krusader_role_docker_networks_custom`"

        ```yaml
        # Type: list
        krusader_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`krusader_role_docker_restart_policy`"

        ```yaml
        # Type: string
        krusader_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`krusader_role_docker_state`"

        ```yaml
        # Type: string
        krusader_role_docker_state: started
        ```

    ##### Dependencies

    ??? variable string "`krusader_role_depends_on`"

        ```yaml
        # Type: string
        krusader_role_depends_on: "{{ krusader_name }}-docker-socket-proxy"
        ```

    ??? variable string "`krusader_role_depends_on_delay`"

        ```yaml
        # Type: string
        krusader_role_depends_on_delay: "0"
        ```

    ??? variable string "`krusader_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        krusader_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`krusader_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        krusader_role_autoheal_enabled: true
        ```

    ??? variable string "`krusader_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        krusader_role_depends_on: ""
        ```

    ??? variable string "`krusader_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        krusader_role_depends_on_delay: "0"
        ```

    ??? variable string "`krusader_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        krusader_role_depends_on_healthchecks:
        ```

    ??? variable bool "`krusader_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        krusader_role_diun_enabled: true
        ```

    ??? variable bool "`krusader_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        krusader_role_dns_enabled: true
        ```

    ??? variable bool "`krusader_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        krusader_role_docker_controller: true
        ```

    ??? variable bool "`krusader_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        krusader_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`krusader_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        krusader_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`krusader_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        krusader_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`krusader_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        krusader_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`krusader_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        krusader_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`krusader_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        krusader_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`krusader_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        krusader_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`krusader_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        krusader_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            krusader_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "krusader2.{{ user.domain }}"
              - "krusader.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`krusader_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        krusader_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            krusader_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'krusader2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`krusader_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        krusader_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
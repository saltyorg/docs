---
icon: material/docker
hide:
  - tags
tags:
  - firefox
  - browser
---

# Firefox

## Overview

Implements a Docker container for Firefox. The GUI of the application is accessed through a modern web browser (no installation or configuration needed on the client side) or via any VNC client.

<div class="grid sb-button-grid" markdown data-search-exclude>

[:material-home: Homepage&nbsp;&nbsp;](https://jlesage.github.io/docker-apps){ .md-button .md-button--stretch }

[:material-bookshelf: Manual&nbsp;&nbsp;](https://github.com/jlesage/docker-firefox/blob/master/README.md#usage){ .md-button .md-button--stretch }

[:fontawesome-brands-docker: Releases&nbsp;&nbsp;](https://hub.docker.com/r/jlesage/firefox/tags){ .md-button .md-button--stretch }

[:fontawesome-brands-github: Community&nbsp;&nbsp;](https://github.com/jlesage/docker-firefox/discussions){ .md-button .md-button--stretch }

</div>

---

## Configuration

Settings are available as [environment variables:octicons-link-external-16:{ .sb-icon--sm }](https://github.com/jlesage/docker-firefox#environment-variables) in `/opt/firefox/.env`.

???+ question "Security"

    By default, web access is restricted by Authelia, and VNC access is secured through SSH authentication; hence, no VNC password is configured. To add this extra layer of security, the process is straightforward:

    1. Run the following command:
       ```shell
       $EDITOR /opt/firefox/.vncpass_clear
       ```
    
    2. Enter your desired password (up to 8 characters in length) and save the file.
    
    3. At a minimum, a container restart is required for changes to take effect.

## Deployment

``` shell
sb install sandbox-firefox
```

!!! info inline end sb-has-fixed-width "Downloads Save Location"
    ```
    /mnt/unionfs/downloads/firefox
    ```

## Usage

### :material-web: Web

Visit <https://firefox.iYOUR_DOMAIN_NAMEi>.

### :material-remote-desktop: VNC

The role supports VNC access over an SSH tunnel (local port forwarding) to Saltbox.

!!! example "Example Command on Local Machine <span style="float:right;color:#00bfa5">:material-fire: Some VNC apps have this functionality built-in!</span>"
    ```shell
    ssh -L localhost:5900:firefox:5900 seed@203.0.113.1 -p 8843 # (1)!
    ```

    1. `-L localhost:5900:firefox:5900`: This part specifies local port forwarding. It tells SSH to listen on port 5900 on your local machine and forward any traffic to the firefox Docker container on port 5900 on the Saltbox host. In other words, it sets up a tunnel between your local port 5900 and the container's port 5900.

        Complete the command with your usual SSH info: `USERNAME@SALTBOX_EXTERNAL_IP -p SSH_PORT`.

While the tunnel is active, you can use a VNC client to access the GUI via the address `localhost:5900`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    firefox_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `firefox_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `firefox_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`firefox_name`"

        ```yaml
        # Type: string
        firefox_name: firefox
        ```

=== "Paths"

    ??? variable string "`firefox_role_paths_folder`"

        ```yaml
        # Type: string
        firefox_role_paths_folder: "{{ firefox_name }}"
        ```

    ??? variable string "`firefox_role_paths_location`"

        ```yaml
        # Type: string
        firefox_role_paths_location: "{{ server_appdata_path }}/{{ firefox_role_paths_folder }}"
        ```

    ??? variable string "`firefox_role_paths_downloads_location`"

        ```yaml
        # Type: string
        firefox_role_paths_downloads_location: "{{ downloads_root_path }}/{{ firefox_role_paths_folder }}"
        ```

    ??? variable string "`firefox_role_paths_env_file_location`"

        ```yaml
        # Type: string
        firefox_role_paths_env_file_location: "{{ firefox_role_paths_location }}/.env"
        ```

=== "Web"

    ??? variable string "`firefox_role_web_subdomain`"

        ```yaml
        # Type: string
        firefox_role_web_subdomain: "{{ firefox_name }}"
        ```

    ??? variable string "`firefox_role_web_domain`"

        ```yaml
        # Type: string
        firefox_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`firefox_role_web_port`"

        ```yaml
        # Type: string
        firefox_role_web_port: "5800"
        ```

    ??? variable string "`firefox_role_web_url`"

        ```yaml
        # Type: string
        firefox_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='firefox') + '.' + lookup('role_var', '_web_domain', role='firefox')
                               if (lookup('role_var', '_web_subdomain', role='firefox') | length > 0)
                               else lookup('role_var', '_web_domain', role='firefox')) }}"
        ```

=== "VNC"

    ??? variable string "`firefox_role_vnc_port`"

        ```yaml
        # Type: string
        firefox_role_vnc_port: "5900"
        ```

=== "DNS"

    ??? variable string "`firefox_role_dns_record`"

        ```yaml
        # Type: string
        firefox_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='firefox') }}"
        ```

    ??? variable string "`firefox_role_dns_zone`"

        ```yaml
        # Type: string
        firefox_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='firefox') }}"
        ```

    ??? variable bool "`firefox_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`firefox_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        firefox_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`firefox_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        firefox_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`firefox_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        firefox_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`firefox_role_traefik_certresolver`"

        ```yaml
        # Type: string
        firefox_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`firefox_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_traefik_enabled: true
        ```

    ??? variable bool "`firefox_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_traefik_api_enabled: false
        ```

    ??? variable string "`firefox_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        firefox_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`firefox_role_docker_container`"

        ```yaml
        # Type: string
        firefox_role_docker_container: "{{ firefox_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`firefox_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_docker_image_pull: true
        ```

    ??? variable string "`firefox_role_docker_image_repo`"

        ```yaml
        # Type: string
        firefox_role_docker_image_repo: "jlesage/firefox"
        ```

    ??? variable string "`firefox_role_docker_image_tag`"

        ```yaml
        # Type: string
        firefox_role_docker_image_tag: "latest"
        ```

    ??? variable string "`firefox_role_docker_image`"

        ```yaml
        # Type: string
        firefox_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='firefox') }}:{{ lookup('role_var', '_docker_image_tag', role='firefox') }}"
        ```

    <h5>Envs</h5>

    ??? variable string "`firefox_role_docker_env_file`"

        ```yaml
        # Type: string
        firefox_role_docker_env_file: "{{ lookup('role_var', '_paths_env_file_location', role='firefox') }}"
        ```

    <h5>Volumes</h5>

    ??? variable list "`firefox_role_docker_volumes_default`"

        ```yaml
        # Type: list
        firefox_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='firefox') }}:/config"
        ```

    ??? variable list "`firefox_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        firefox_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`firefox_role_docker_hostname`"

        ```yaml
        # Type: string
        firefox_role_docker_hostname: "{{ firefox_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`firefox_role_docker_networks_alias`"

        ```yaml
        # Type: string
        firefox_role_docker_networks_alias: "{{ firefox_name }}"
        ```

    ??? variable list "`firefox_role_docker_networks_default`"

        ```yaml
        # Type: list
        firefox_role_docker_networks_default: []
        ```

    ??? variable list "`firefox_role_docker_networks_custom`"

        ```yaml
        # Type: list
        firefox_role_docker_networks_custom: []
        ```

    <h5>Capabilities</h5>

    ??? variable list "`firefox_role_docker_capabilities_default`"

        ```yaml
        # Type: list
        firefox_role_docker_capabilities_default: 
          - "SYS_NICE"
        ```

    ??? variable list "`firefox_role_docker_capabilities_custom`"

        ```yaml
        # Type: list
        firefox_role_docker_capabilities_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`firefox_role_docker_restart_policy`"

        ```yaml
        # Type: string
        firefox_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`firefox_role_docker_state`"

        ```yaml
        # Type: string
        firefox_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`firefox_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        firefox_role_autoheal_enabled: true
        ```

    ??? variable string "`firefox_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        firefox_role_depends_on: ""
        ```

    ??? variable string "`firefox_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        firefox_role_depends_on_delay: "0"
        ```

    ??? variable string "`firefox_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        firefox_role_depends_on_healthchecks:
        ```

    ??? variable bool "`firefox_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        firefox_role_diun_enabled: true
        ```

    ??? variable bool "`firefox_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        firefox_role_dns_enabled: true
        ```

    ??? variable bool "`firefox_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        firefox_role_docker_controller: true
        ```

    ??? variable bool "`firefox_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_docker_volumes_download:
        ```

    ??? variable bool "`firefox_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        firefox_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`firefox_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        firefox_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`firefox_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        firefox_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`firefox_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        firefox_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`firefox_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`firefox_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        firefox_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`firefox_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        firefox_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`firefox_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        firefox_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`firefox_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        firefox_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`firefox_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        firefox_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            firefox_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "firefox2.{{ user.domain }}"
              - "firefox.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`firefox_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        firefox_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            firefox_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'firefox2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`firefox_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        firefox_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
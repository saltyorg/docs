---
icon: material/docker
hide:
  - tags
tags:
  - navidrome
  - media
  - music
---

# Navidrome

## Overview

[Navidrome](https://www.navidrome.org/) allows you to enjoy your music collection from anywhere, by making it available through a modern Web UI and through a wide range of third-party compatible mobile apps, for both iOS and Android devices.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.navidrome.org/){: .header-icons } | [:octicons-link-16: Docs](https://www.navidrome.org/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/navidrome/navidrome/issues){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/deluan/navidrome){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-navidrome

```

### 2. URL

- To access Navidrome, visit <https://navidrome.iYOUR_DOMAIN_NAMEi>

### 3. Setup

- After installing Navidrome in your platform, you need to create your first user. This will be your admin user, a super user that can manage all aspects of Navidrome, including the ability to manage other users. Just browse to Navidrome’s homepage at <https://navidrome.iYOUR_DOMAIN_NAMEi> and you will be greeted with a screen like this: <br />

     ![](../../images/community/navidrome_first_user.png)

    Just fill out the username and password you want to use, confirm the password and click on the “Create Admin” button.

    That’s it! You should now be able to browse and listen to all your music.

    !!! Note
             It usually take a couple of minutes for your music to start appearing in Navidrome’s UI. <br />
             You can check the logs to see what is the scan progress. If you have a large library this may take some time.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    navidrome_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `navidrome_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `navidrome_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`navidrome_name`"

        ```yaml
        # Type: string
        navidrome_name: navidrome
        ```

=== "Paths"

    ??? variable string "`navidrome_role_paths_folder`"

        ```yaml
        # Type: string
        navidrome_role_paths_folder: "{{ navidrome_name }}"
        ```

    ??? variable string "`navidrome_role_paths_location`"

        ```yaml
        # Type: string
        navidrome_role_paths_location: "{{ server_appdata_path }}/{{ navidrome_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`navidrome_role_web_subdomain`"

        ```yaml
        # Type: string
        navidrome_role_web_subdomain: "{{ navidrome_name }}"
        ```

    ??? variable string "`navidrome_role_web_domain`"

        ```yaml
        # Type: string
        navidrome_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`navidrome_role_web_port`"

        ```yaml
        # Type: string
        navidrome_role_web_port: "4533"
        ```

    ??? variable string "`navidrome_role_web_url`"

        ```yaml
        # Type: string
        navidrome_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='navidrome') + '.' + lookup('role_var', '_web_domain', role='navidrome')
                                 if (lookup('role_var', '_web_subdomain', role='navidrome') | length > 0)
                                 else lookup('role_var', '_web_domain', role='navidrome')) }}"
        ```

=== "DNS"

    ??? variable string "`navidrome_role_dns_record`"

        ```yaml
        # Type: string
        navidrome_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='navidrome') }}"
        ```

    ??? variable string "`navidrome_role_dns_zone`"

        ```yaml
        # Type: string
        navidrome_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='navidrome') }}"
        ```

    ??? variable bool "`navidrome_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        navidrome_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`navidrome_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        navidrome_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`navidrome_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        navidrome_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`navidrome_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        navidrome_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`navidrome_role_traefik_certresolver`"

        ```yaml
        # Type: string
        navidrome_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`navidrome_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        navidrome_role_traefik_enabled: true
        ```

    ??? variable bool "`navidrome_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        navidrome_role_traefik_api_enabled: false
        ```

    ??? variable string "`navidrome_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        navidrome_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`navidrome_role_docker_container`"

        ```yaml
        # Type: string
        navidrome_role_docker_container: "{{ navidrome_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`navidrome_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        navidrome_role_docker_image_pull: true
        ```

    ??? variable string "`navidrome_role_docker_image_tag`"

        ```yaml
        # Type: string
        navidrome_role_docker_image_tag: "latest"
        ```

    ??? variable string "`navidrome_role_docker_image_repo`"

        ```yaml
        # Type: string
        navidrome_role_docker_image_repo: "deluan/navidrome"
        ```

    ??? variable string "`navidrome_role_docker_image`"

        ```yaml
        # Type: string
        navidrome_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='navidrome') }}:{{ lookup('role_var', '_docker_image_tag', role='navidrome') }}"
        ```

    <h5>Volumes</h5>

    ??? variable list "`navidrome_role_docker_volumes_default`"

        ```yaml
        # Type: list
        navidrome_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='navidrome') }}:/data"
          - "/mnt/unionfs/Media/Music:/music"
        ```

    ??? variable list "`navidrome_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        navidrome_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`navidrome_role_docker_hostname`"

        ```yaml
        # Type: string
        navidrome_role_docker_hostname: "{{ navidrome_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`navidrome_role_docker_networks_alias`"

        ```yaml
        # Type: string
        navidrome_role_docker_networks_alias: "{{ navidrome_name }}"
        ```

    ??? variable list "`navidrome_role_docker_networks_default`"

        ```yaml
        # Type: list
        navidrome_role_docker_networks_default: []
        ```

    ??? variable list "`navidrome_role_docker_networks_custom`"

        ```yaml
        # Type: list
        navidrome_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`navidrome_role_docker_restart_policy`"

        ```yaml
        # Type: string
        navidrome_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`navidrome_role_docker_state`"

        ```yaml
        # Type: string
        navidrome_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`navidrome_role_docker_user`"

        ```yaml
        # Type: string
        navidrome_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`navidrome_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        navidrome_role_autoheal_enabled: true
        ```

    ??? variable string "`navidrome_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        navidrome_role_depends_on: ""
        ```

    ??? variable string "`navidrome_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        navidrome_role_depends_on_delay: "0"
        ```

    ??? variable string "`navidrome_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        navidrome_role_depends_on_healthchecks:
        ```

    ??? variable bool "`navidrome_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        navidrome_role_diun_enabled: true
        ```

    ??? variable bool "`navidrome_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        navidrome_role_dns_enabled: true
        ```

    ??? variable bool "`navidrome_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        navidrome_role_docker_controller: true
        ```

    ??? variable bool "`navidrome_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        navidrome_role_docker_volumes_download:
        ```

    ??? variable bool "`navidrome_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        navidrome_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`navidrome_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        navidrome_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`navidrome_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        navidrome_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`navidrome_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        navidrome_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`navidrome_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        navidrome_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`navidrome_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        navidrome_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`navidrome_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        navidrome_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`navidrome_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        navidrome_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`navidrome_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        navidrome_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`navidrome_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        navidrome_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            navidrome_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "navidrome2.{{ user.domain }}"
              - "navidrome.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`navidrome_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        navidrome_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            navidrome_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'navidrome2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`navidrome_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        navidrome_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
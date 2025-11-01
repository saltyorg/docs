---
hide:
  - tags
tags:
  - jdownloader2
  - download
  - tools
---

# JDownloader

## Overview

[JDownloader](https://beta.jdownloader.org/) is a free download-manager that makes downloading as easy, fast and automated as it should be. It's like your personal internet robot that does all the work for you. He will download whole photo albums, playlists or just about anything else with just one click. Go ahead and try it!

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://beta.jdownloader.org/){: .header-icons } | [:octicons-link-16: Docs](https://beta.jdownloader.org/support){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/jlesage/docker-jdownloader-2){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jlesage/jdownloader-2){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-jdownloader2

```

### 2. URL

- To access JDownloader, visit <https://jdownloader2.iYOUR_DOMAIN_NAMEi>

### 3. Setup

1. The configured password is taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

2. Configure your myjdownloader account (Create at <https://my.jdownloader.org/> if needed) and name your instance so you can connect via web or browser extensions. Use clipboard for two step copy and paste if needed. Note that some settings are only accessible via `jdownloader2.xYOUR_DOMAIN_NAMEx`. Premium accounts such as mega.nz can be added via web interface.

3. Use manual import from sonarr / radarr and navigate to `/mnt/local/downloads/myjdownloader/output/` to import your files, note they must be already added as wanted media for import to recognise and identify your downloaded media.

4. See <https://my.jdownloader.org/> for browser extensions and phone apps as desired.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    jdownloader2_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `jdownloader2_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `jdownloader2_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`jdownloader2_name`"

        ```yaml
        # Type: string
        jdownloader2_name: jdownloader2
        ```

=== "Paths"

    ??? variable string "`jdownloader2_role_paths_folder`"

        ```yaml
        # Type: string
        jdownloader2_role_paths_folder: "{{ jdownloader2_name }}"
        ```

    ??? variable string "`jdownloader2_role_paths_location`"

        ```yaml
        # Type: string
        jdownloader2_role_paths_location: "{{ server_appdata_path }}/{{ jdownloader2_role_paths_folder }}"
        ```

    ??? variable string "`jdownloader2_role_paths_downloads_location`"

        ```yaml
        # Type: string
        jdownloader2_role_paths_downloads_location: "/mnt/local/downloads/{{ jdownloader2_name }}/output"
        ```

    ??? variable string "`jdownloader2_role_paths_tools_location`"

        ```yaml
        # Type: string
        jdownloader2_role_paths_tools_location: "{{ jdownloader2_role_paths_location }}/config/libs"
        ```

=== "Web"

    ??? variable string "`jdownloader2_role_web_subdomain`"

        ```yaml
        # Type: string
        jdownloader2_role_web_subdomain: "{{ jdownloader2_name }}"
        ```

    ??? variable string "`jdownloader2_role_web_domain`"

        ```yaml
        # Type: string
        jdownloader2_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`jdownloader2_role_web_port`"

        ```yaml
        # Type: string
        jdownloader2_role_web_port: "5800"
        ```

    ??? variable string "`jdownloader2_role_web_url`"

        ```yaml
        # Type: string
        jdownloader2_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='jdownloader2') + '.' + lookup('role_var', '_web_domain', role='jdownloader2')
                                    if (lookup('role_var', '_web_subdomain', role='jdownloader2') | length > 0)
                                    else lookup('role_var', '_web_domain', role='jdownloader2')) }}"
        ```

=== "DNS"

    ??? variable string "`jdownloader2_role_dns_record`"

        ```yaml
        # Type: string
        jdownloader2_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='jdownloader2') }}"
        ```

    ??? variable string "`jdownloader2_role_dns_zone`"

        ```yaml
        # Type: string
        jdownloader2_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='jdownloader2') }}"
        ```

    ??? variable bool "`jdownloader2_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`jdownloader2_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        jdownloader2_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`jdownloader2_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        jdownloader2_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`jdownloader2_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        jdownloader2_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`jdownloader2_role_traefik_certresolver`"

        ```yaml
        # Type: string
        jdownloader2_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`jdownloader2_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_traefik_enabled: true
        ```

    ??? variable bool "`jdownloader2_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_traefik_api_enabled: false
        ```

    ??? variable string "`jdownloader2_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        jdownloader2_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`jdownloader2_role_docker_container`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_container: "{{ jdownloader2_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`jdownloader2_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_docker_image_pull: true
        ```

    ??? variable string "`jdownloader2_role_docker_image_repo`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_image_repo: "jlesage/jdownloader-2"
        ```

    ??? variable string "`jdownloader2_role_docker_image_tag`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_image_tag: "latest"
        ```

    ??? variable string "`jdownloader2_role_docker_image`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='jdownloader2') }}:{{ lookup('role_var', '_docker_image_tag', role='jdownloader2') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`jdownloader2_role_docker_envs_default`"

        ```yaml
        # Type: dict
        jdownloader2_role_docker_envs_default: 
          USER_ID: "{{ uid }}"
          GROUP_ID: "{{ gid }}"
          TZ: "{{ tz }}"
          DISPLAY_WIDTH: "1280"
          DISPLAY_HEIGHT: "768"
          VNC_PASSWORD: "{{ user.pass }}"
          CLEAN_TMP_DIR: "1"
          UMASK: "000"
          ENABLE_CJK_FONT: "1"
        ```

    ??? variable dict "`jdownloader2_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        jdownloader2_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`jdownloader2_role_docker_volumes_default`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='jdownloader2') }}/config:/config"
          - "{{ lookup('role_var', '_paths_downloads_location', role='jdownloader2') }}:/output"
        ```

    ??? variable list "`jdownloader2_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`jdownloader2_role_docker_hostname`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_hostname: "{{ jdownloader2_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`jdownloader2_role_docker_networks_alias`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_networks_alias: "{{ jdownloader2_name }}"
        ```

    ??? variable list "`jdownloader2_role_docker_networks_default`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_networks_default: []
        ```

    ??? variable list "`jdownloader2_role_docker_networks_custom`"

        ```yaml
        # Type: list
        jdownloader2_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`jdownloader2_role_docker_restart_policy`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`jdownloader2_role_docker_state`"

        ```yaml
        # Type: string
        jdownloader2_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`jdownloader2_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        jdownloader2_role_autoheal_enabled: true
        ```

    ??? variable string "`jdownloader2_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        jdownloader2_role_depends_on: ""
        ```

    ??? variable string "`jdownloader2_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        jdownloader2_role_depends_on_delay: "0"
        ```

    ??? variable string "`jdownloader2_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        jdownloader2_role_depends_on_healthchecks:
        ```

    ??? variable bool "`jdownloader2_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        jdownloader2_role_diun_enabled: true
        ```

    ??? variable bool "`jdownloader2_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        jdownloader2_role_dns_enabled: true
        ```

    ??? variable bool "`jdownloader2_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        jdownloader2_role_docker_controller: true
        ```

    ??? variable bool "`jdownloader2_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        jdownloader2_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`jdownloader2_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        jdownloader2_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`jdownloader2_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        jdownloader2_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`jdownloader2_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        jdownloader2_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`jdownloader2_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`jdownloader2_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        jdownloader2_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`jdownloader2_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        jdownloader2_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`jdownloader2_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        jdownloader2_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`jdownloader2_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        jdownloader2_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`jdownloader2_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        jdownloader2_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            jdownloader2_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "jdownloader22.{{ user.domain }}"
              - "jdownloader2.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`jdownloader2_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        jdownloader2_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            jdownloader2_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'jdownloader22.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`jdownloader2_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        jdownloader2_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
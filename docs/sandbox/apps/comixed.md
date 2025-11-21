---
icon: material/docker
hide:
  - tags
tags:
  - comic
---

# ComiXed

## Overview

[ComiXed](https://github.com/comixed/comixed) is an application for managing digital comics. It seeks to be the ultimate management tool for digital comic books. 

It does the following and more:

- Scrape metadata for comics from various sources, such as ComicVine.
- Update the ComicInfo.xml file within each comic with the current metadata.

It is NOT:

- A comic reading application.

!!!note
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/comixed/comixed){: .header-icons } | [:octicons-link-16: Docs](https://github.com/comixed/comixed/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/comixed/comixed){: .header-icons } | [:material-docker: Docker](https://registry.hub.docker.com/r/comixed/comixed){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-comixed

```

### 2. URL

- To access ComiXed, visit <https://comixed.iYOUR_DOMAIN_NAMEi>

### 3. Setup

!!! info
    📢 ComiXed has 2 default users created when you run the role. It is a good idea to change the passwords for each account from the default asap.

``` shell
Username: comixedadmin@localhost
Password: comixedadmin
```

``` shell
Username: comixedreader@localhost
Password: comixedreader
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    comixed_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `comixed_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `comixed_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`comixed_name`"

        ```yaml
        # Type: string
        comixed_name: comixed
        ```

=== "Paths"

    ??? variable string "`comixed_role_paths_folder`"

        ```yaml
        # Type: string
        comixed_role_paths_folder: "{{ comixed_name }}"
        ```

    ??? variable string "`comixed_role_paths_location`"

        ```yaml
        # Type: string
        comixed_role_paths_location: "{{ server_appdata_path }}/{{ comixed_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`comixed_role_web_subdomain`"

        ```yaml
        # Type: string
        comixed_role_web_subdomain: "{{ comixed_name }}"
        ```

    ??? variable string "`comixed_role_web_domain`"

        ```yaml
        # Type: string
        comixed_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`comixed_role_web_port`"

        ```yaml
        # Type: string
        comixed_role_web_port: "7171"
        ```

    ??? variable string "`comixed_role_web_url`"

        ```yaml
        # Type: string
        comixed_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='comixed') + '.' + lookup('role_var', '_web_domain', role='comixed')
                               if (lookup('role_var', '_web_subdomain', role='comixed') | length > 0)
                               else lookup('role_var', '_web_domain', role='comixed')) }}"
        ```

=== "DNS"

    ??? variable string "`comixed_role_dns_record`"

        ```yaml
        # Type: string
        comixed_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='comixed') }}"
        ```

    ??? variable string "`comixed_role_dns_zone`"

        ```yaml
        # Type: string
        comixed_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='comixed') }}"
        ```

    ??? variable bool "`comixed_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        comixed_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`comixed_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        comixed_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`comixed_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        comixed_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`comixed_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        comixed_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`comixed_role_traefik_certresolver`"

        ```yaml
        # Type: string
        comixed_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`comixed_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        comixed_role_traefik_enabled: true
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`comixed_role_docker_container`"

        ```yaml
        # Type: string
        comixed_role_docker_container: "{{ comixed_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`comixed_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        comixed_role_docker_image_pull: true
        ```

    ??? variable string "`comixed_role_docker_image_repo`"

        ```yaml
        # Type: string
        comixed_role_docker_image_repo: "comixed/comixed"
        ```

    ??? variable string "`comixed_role_docker_image_tag`"

        ```yaml
        # Type: string
        comixed_role_docker_image_tag: "latest"
        ```

    ??? variable string "`comixed_role_docker_image`"

        ```yaml
        # Type: string
        comixed_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='comixed') }}:{{ lookup('role_var', '_docker_image_tag', role='comixed') }}"
        ```

    <h5>Volumes</h5>

    ??? variable list "`comixed_role_docker_volumes_default`"

        ```yaml
        # Type: list
        comixed_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='comixed') }}:/root/.comixed"
          - "/mnt/unionfs/Media/Comics:/comic_dir"
        ```

    ??? variable list "`comixed_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        comixed_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`comixed_role_docker_hostname`"

        ```yaml
        # Type: string
        comixed_role_docker_hostname: "{{ comixed_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`comixed_role_docker_networks_alias`"

        ```yaml
        # Type: string
        comixed_role_docker_networks_alias: "{{ comixed_name }}"
        ```

    ??? variable list "`comixed_role_docker_networks_default`"

        ```yaml
        # Type: list
        comixed_role_docker_networks_default: []
        ```

    ??? variable list "`comixed_role_docker_networks_custom`"

        ```yaml
        # Type: list
        comixed_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`comixed_role_docker_restart_policy`"

        ```yaml
        # Type: string
        comixed_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`comixed_role_docker_state`"

        ```yaml
        # Type: string
        comixed_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`comixed_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        comixed_role_autoheal_enabled: true
        ```

    ??? variable string "`comixed_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        comixed_role_depends_on: ""
        ```

    ??? variable string "`comixed_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        comixed_role_depends_on_delay: "0"
        ```

    ??? variable string "`comixed_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        comixed_role_depends_on_healthchecks:
        ```

    ??? variable bool "`comixed_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        comixed_role_diun_enabled: true
        ```

    ??? variable bool "`comixed_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        comixed_role_dns_enabled: true
        ```

    ??? variable bool "`comixed_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        comixed_role_docker_controller: true
        ```

    ??? variable bool "`comixed_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        comixed_role_docker_volumes_download:
        ```

    ??? variable bool "`comixed_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        comixed_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`comixed_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        comixed_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`comixed_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        comixed_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`comixed_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        comixed_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`comixed_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        comixed_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`comixed_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        comixed_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`comixed_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        comixed_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`comixed_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        comixed_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`comixed_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        comixed_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`comixed_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        comixed_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            comixed_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "comixed2.{{ user.domain }}"
              - "comixed.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`comixed_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        comixed_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            comixed_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'comixed2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`comixed_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        comixed_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
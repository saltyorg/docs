---
hide:
  - tags
tags:
  - komga
  - media
  - comics
---

# Komga

## What is it?

[Komga](https://komga.org/) is a free and open source comics/mangas server.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://komga.org/){: .header-icons } | [:octicons-link-16: Docs](https://komga.org/installation/docker.html){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/gotson/komga){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/gotson/komga){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-komga

```

### 2. URL

- To access Komga, visit `https://komga._yourdomain.com_`

### 3. Setup

- On first opening you will be asked to create a user account. <br />
  Choose an email and password, then click on Create User Account.

- Komga expects comics to be stored in `/mnt/unionfs/Media/Comics`.

- `/mnt` is accessible to the container as well.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    komga_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `komga_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `komga_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`komga_name`"

        ```yaml
        # Type: string
        komga_name: komga
        ```

=== "Paths"

    ??? variable string "`komga_role_paths_folder`"

        ```yaml
        # Type: string
        komga_role_paths_folder: "{{ komga_name }}"
        ```

    ??? variable string "`komga_role_paths_location`"

        ```yaml
        # Type: string
        komga_role_paths_location: "{{ server_appdata_path }}/{{ komga_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`komga_role_web_subdomain`"

        ```yaml
        # Type: string
        komga_role_web_subdomain: "{{ komga_name }}"
        ```

    ??? variable string "`komga_role_web_domain`"

        ```yaml
        # Type: string
        komga_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`komga_role_web_port`"

        ```yaml
        # Type: string
        komga_role_web_port: "25600"
        ```

    ??? variable string "`komga_role_web_url`"

        ```yaml
        # Type: string
        komga_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='komga') + '.' + lookup('role_var', '_web_domain', role='komga')
                             if (lookup('role_var', '_web_subdomain', role='komga') | length > 0)
                             else lookup('role_var', '_web_domain', role='komga')) }}"
        ```

=== "DNS"

    ??? variable string "`komga_role_dns_record`"

        ```yaml
        # Type: string
        komga_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='komga') }}"
        ```

    ??? variable string "`komga_role_dns_zone`"

        ```yaml
        # Type: string
        komga_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='komga') }}"
        ```

    ??? variable bool "`komga_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        komga_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`komga_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        komga_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`komga_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        komga_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`komga_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        komga_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`komga_role_traefik_certresolver`"

        ```yaml
        # Type: string
        komga_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`komga_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        komga_role_traefik_enabled: true
        ```

    ??? variable bool "`komga_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        komga_role_traefik_api_enabled: false
        ```

    ??? variable string "`komga_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        komga_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`komga_role_docker_container`"

        ```yaml
        # Type: string
        komga_role_docker_container: "{{ komga_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`komga_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        komga_role_docker_image_pull: true
        ```

    ??? variable string "`komga_role_docker_image_tag`"

        ```yaml
        # Type: string
        komga_role_docker_image_tag: "latest"
        ```

    ??? variable string "`komga_role_docker_image_repo`"

        ```yaml
        # Type: string
        komga_role_docker_image_repo: "gotson/komga"
        ```

    ??? variable string "`komga_role_docker_image`"

        ```yaml
        # Type: string
        komga_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='komga') }}:{{ lookup('role_var', '_docker_image_tag', role='komga') }}"
        ```

    <h5>Volumes</h5>

    ??? variable list "`komga_role_docker_volumes_default`"

        ```yaml
        # Type: list
        komga_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='komga') }}:/config"
          - "/mnt/unionfs/Media/Comics:/comics"
        ```

    ??? variable list "`komga_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        komga_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`komga_role_docker_hostname`"

        ```yaml
        # Type: string
        komga_role_docker_hostname: "{{ komga_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`komga_role_docker_networks_alias`"

        ```yaml
        # Type: string
        komga_role_docker_networks_alias: "{{ komga_name }}"
        ```

    ??? variable list "`komga_role_docker_networks_default`"

        ```yaml
        # Type: list
        komga_role_docker_networks_default: []
        ```

    ??? variable list "`komga_role_docker_networks_custom`"

        ```yaml
        # Type: list
        komga_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`komga_role_docker_restart_policy`"

        ```yaml
        # Type: string
        komga_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`komga_role_docker_state`"

        ```yaml
        # Type: string
        komga_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`komga_role_docker_user`"

        ```yaml
        # Type: string
        komga_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`komga_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        komga_role_autoheal_enabled: true
        ```

    ??? variable string "`komga_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        komga_role_depends_on: ""
        ```

    ??? variable string "`komga_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        komga_role_depends_on_delay: "0"
        ```

    ??? variable string "`komga_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        komga_role_depends_on_healthchecks:
        ```

    ??? variable bool "`komga_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        komga_role_diun_enabled: true
        ```

    ??? variable bool "`komga_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        komga_role_dns_enabled: true
        ```

    ??? variable bool "`komga_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        komga_role_docker_controller: true
        ```

    ??? variable bool "`komga_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        komga_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`komga_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        komga_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`komga_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        komga_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`komga_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        komga_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`komga_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        komga_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`komga_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        komga_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`komga_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        komga_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`komga_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        komga_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`komga_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        komga_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`komga_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        komga_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            komga_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "komga2.{{ user.domain }}"
              - "komga.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`komga_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        komga_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            komga_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'komga2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`komga_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        komga_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
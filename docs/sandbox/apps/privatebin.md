---
hide:
  - tags
tags:
  - privatebin
  - pastebin
  - privacy
---

# PrivateBin

## What is it?

[PrivateBin](https://privatebin.info/) PrivateBin is a minimalist, open source online pastebin where the server has zero knowledge of pasted data.
It's privacy-preserving and encrypted-by-default.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://privatebin.info/){: .header-icons } | [:octicons-link-16: Docs](https://github.com/PrivateBin/PrivateBin/wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/PrivateBin/PrivateBin){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/privatebin/nginx-fpm-alpine){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-privatebin

```

### 2. URL

- To access PrivateBin, visit <https://privatebin.iYOUR_DOMAIN_NAMEi>

### 3. Setup

- Edit `/opt/privatebin/conf.php` to customize your instance.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    privatebin_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `privatebin_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `privatebin_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`privatebin_name`"

        ```yaml
        # Type: string
        privatebin_name: privatebin
        ```

=== "Paths"

    ??? variable string "`privatebin_role_paths_folder`"

        ```yaml
        # Type: string
        privatebin_role_paths_folder: "{{ privatebin_name }}"
        ```

    ??? variable string "`privatebin_role_paths_location`"

        ```yaml
        # Type: string
        privatebin_role_paths_location: "{{ server_appdata_path }}/{{ privatebin_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`privatebin_role_web_subdomain`"

        ```yaml
        # Type: string
        privatebin_role_web_subdomain: "{{ privatebin_name }}"
        ```

    ??? variable string "`privatebin_role_web_domain`"

        ```yaml
        # Type: string
        privatebin_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`privatebin_role_web_port`"

        ```yaml
        # Type: string
        privatebin_role_web_port: "8080"
        ```

    ??? variable string "`privatebin_role_web_url`"

        ```yaml
        # Type: string
        privatebin_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='privatebin') + '.' + lookup('role_var', '_web_domain', role='privatebin')
                                  if (lookup('role_var', '_web_subdomain', role='privatebin') | length > 0)
                                  else lookup('role_var', '_web_domain', role='privatebin')) }}"
        ```

=== "DNS"

    ??? variable string "`privatebin_role_dns_record`"

        ```yaml
        # Type: string
        privatebin_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='privatebin') }}"
        ```

    ??? variable string "`privatebin_role_dns_zone`"

        ```yaml
        # Type: string
        privatebin_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='privatebin') }}"
        ```

    ??? variable bool "`privatebin_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        privatebin_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`privatebin_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        privatebin_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`privatebin_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        privatebin_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`privatebin_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        privatebin_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`privatebin_role_traefik_certresolver`"

        ```yaml
        # Type: string
        privatebin_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`privatebin_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        privatebin_role_traefik_enabled: true
        ```

    ??? variable bool "`privatebin_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        privatebin_role_traefik_api_enabled: false
        ```

    ??? variable string "`privatebin_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        privatebin_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`privatebin_role_docker_container`"

        ```yaml
        # Type: string
        privatebin_role_docker_container: "{{ privatebin_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`privatebin_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        privatebin_role_docker_image_pull: true
        ```

    ??? variable string "`privatebin_role_docker_image_tag`"

        ```yaml
        # Type: string
        privatebin_role_docker_image_tag: "latest"
        ```

    ??? variable string "`privatebin_role_docker_image`"

        ```yaml
        # Type: string
        privatebin_role_docker_image: "privatebin/nginx-fpm-alpine:{{ lookup('role_var', '_docker_image_tag', role='privatebin') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`privatebin_role_docker_envs_default`"

        ```yaml
        # Type: dict
        privatebin_role_docker_envs_default: 
          TZ: "{{ tz }}"
          PHP_TZ: "{{ tz }}"
        ```

    ??? variable dict "`privatebin_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        privatebin_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`privatebin_role_docker_volumes_default`"

        ```yaml
        # Type: list
        privatebin_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='privatebin') }}:/srv/data"
          - "{{ lookup('role_var', '_paths_location', role='privatebin') }}/conf.php:/srv/cfg/conf.php:ro"
          - "{{ privatebin_name }}_tmpfs_run:/run"
        ```

    ??? variable list "`privatebin_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        privatebin_role_docker_volumes_custom: []
        ```

    <h5>Mounts</h5>

    ??? variable list "`privatebin_role_docker_mounts_default`"

        ```yaml
        # Type: list
        privatebin_role_docker_mounts_default: 
          - target: /tmp
            type: tmpfs
          - target: /var/lib/nginx/tmp
            type: tmpfs
        ```

    ??? variable list "`privatebin_role_docker_mounts_custom`"

        ```yaml
        # Type: list
        privatebin_role_docker_mounts_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`privatebin_role_docker_hostname`"

        ```yaml
        # Type: string
        privatebin_role_docker_hostname: "{{ privatebin_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`privatebin_role_docker_networks_alias`"

        ```yaml
        # Type: string
        privatebin_role_docker_networks_alias: "{{ privatebin_name }}"
        ```

    ??? variable list "`privatebin_role_docker_networks_default`"

        ```yaml
        # Type: list
        privatebin_role_docker_networks_default: []
        ```

    ??? variable list "`privatebin_role_docker_networks_custom`"

        ```yaml
        # Type: list
        privatebin_role_docker_networks_custom: []
        ```

    <h5>Read Only</h5>

    ??? variable bool "`privatebin_role_docker_read_only`"

        ```yaml
        # Type: bool (true/false)
        privatebin_role_docker_read_only: true
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`privatebin_role_docker_restart_policy`"

        ```yaml
        # Type: string
        privatebin_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`privatebin_role_docker_state`"

        ```yaml
        # Type: string
        privatebin_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`privatebin_role_docker_user`"

        ```yaml
        # Type: string
        privatebin_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`privatebin_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        privatebin_role_autoheal_enabled: true
        ```

    ??? variable string "`privatebin_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        privatebin_role_depends_on: ""
        ```

    ??? variable string "`privatebin_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        privatebin_role_depends_on_delay: "0"
        ```

    ??? variable string "`privatebin_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        privatebin_role_depends_on_healthchecks:
        ```

    ??? variable bool "`privatebin_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        privatebin_role_diun_enabled: true
        ```

    ??? variable bool "`privatebin_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        privatebin_role_dns_enabled: true
        ```

    ??? variable bool "`privatebin_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        privatebin_role_docker_controller: true
        ```

    ??? variable bool "`privatebin_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        privatebin_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`privatebin_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        privatebin_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`privatebin_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        privatebin_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`privatebin_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        privatebin_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`privatebin_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        privatebin_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`privatebin_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        privatebin_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`privatebin_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        privatebin_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`privatebin_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        privatebin_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`privatebin_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        privatebin_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`privatebin_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        privatebin_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            privatebin_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "privatebin2.{{ user.domain }}"
              - "privatebin.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`privatebin_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        privatebin_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            privatebin_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'privatebin2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`privatebin_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        privatebin_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
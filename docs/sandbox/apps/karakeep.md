---
hide:
  - tags
tags:
  - karakeep
  - media
  - music
---

# Karakeep

[Karakeep](https://karakeep.app/) is an open source "Bookmark Everything" app that uses AI for automatically tagging the content you throw at it. The app is built with self-hosting as a first class citizen.

The GUI of the application is accessed through a modern web browser (no installation or configuration needed on the client side) or via any VNC client.

<div class="grid" style="grid-template-columns: repeat(auto-fit,minmax(10.5rem,1fr));" markdown>

[:material-bookshelf: Project Docs](https://docs.karakeep.app/){ .md-button .md-button--stretch }

[:material-git: GitHub Repo](https://github.com/karakeep-app/karakeep){ .md-button .md-button--stretch }

</div>

## Configuration

Use the ```sb inventory``` system to set any environment variables that are desired such as OpenAI API keys, downloading videos, document size limits, etc

See [Karakeep Configuration](https://docs.karakeep.app/configuration) for supported variables

## Deployment

``` shell
sb install sandbox-karakeep
```

## Usage

Visit `https://karakeep.app/`.

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    karakeep_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `karakeep_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `karakeep_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`karakeep_name`"

        ```yaml
        # Type: string
        karakeep_name: karakeep
        ```

=== "Container Dependant Variables"

    ??? variable string "`karakeep_meili_name`"

        ```yaml
        # Type: string
        karakeep_meili_name: "meilisearch"
        ```

    ??? variable string "`karakeep_meili_port`"

        ```yaml
        # Type: string
        karakeep_meili_port: "7700"
        ```

    ??? variable string "`karakeep_chrome_name`"

        ```yaml
        # Type: string
        karakeep_chrome_name: "chrome"
        ```

    ??? variable string "`karakeep_chrome_port`"

        ```yaml
        # Type: string
        karakeep_chrome_port: "9222"
        ```

=== "Paths"

    ??? variable string "`karakeep_role_paths_folder`"

        ```yaml
        # Type: string
        karakeep_role_paths_folder: "{{ karakeep_name }}"
        ```

    ??? variable string "`karakeep_role_paths_location`"

        ```yaml
        # Type: string
        karakeep_role_paths_location: "{{ server_appdata_path }}/{{ karakeep_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`karakeep_role_web_subdomain`"

        ```yaml
        # Type: string
        karakeep_role_web_subdomain: "{{ karakeep_name }}"
        ```

    ??? variable string "`karakeep_role_web_domain`"

        ```yaml
        # Type: string
        karakeep_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`karakeep_role_web_port`"

        ```yaml
        # Type: string
        karakeep_role_web_port: "3000"
        ```

    ??? variable string "`karakeep_role_web_url`"

        ```yaml
        # Type: string
        karakeep_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='karakeep') + '.' + lookup('role_var', '_web_domain', role='karakeep')
                                if (lookup('role_var', '_web_subdomain', role='karakeep') | length > 0)
                                else lookup('role_var', '_web_domain', role='karakeep')) }}"
        ```

=== "DNS"

    ??? variable string "`karakeep_role_dns_record`"

        ```yaml
        # Type: string
        karakeep_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='karakeep') }}"
        ```

    ??? variable string "`karakeep_role_dns_zone`"

        ```yaml
        # Type: string
        karakeep_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='karakeep') }}"
        ```

    ??? variable bool "`karakeep_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`karakeep_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        karakeep_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`karakeep_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        karakeep_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`karakeep_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        karakeep_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`karakeep_role_traefik_certresolver`"

        ```yaml
        # Type: string
        karakeep_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`karakeep_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_traefik_enabled: true
        ```

    ??? variable bool "`karakeep_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_traefik_api_enabled: false
        ```

    ??? variable string "`karakeep_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        karakeep_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    Container
    { .sb-h5 }

    ??? variable string "`karakeep_role_docker_container`"

        ```yaml
        # Type: string
        karakeep_role_docker_container: "{{ karakeep_name }}"
        ```

    Image
    { .sb-h5 }

    ??? variable bool "`karakeep_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_docker_image_pull: true
        ```

    ??? variable string "`karakeep_role_docker_image_repo`"

        ```yaml
        # Type: string
        karakeep_role_docker_image_repo: "ghcr.io/karakeep-app/karakeep"
        ```

    ??? variable string "`karakeep_role_docker_image_tag`"

        ```yaml
        # Type: string
        karakeep_role_docker_image_tag: "release"
        ```

    ??? variable string "`karakeep_role_docker_image`"

        ```yaml
        # Type: string
        karakeep_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='karakeep') }}:{{ lookup('role_var', '_docker_image_tag', role='karakeep') }}"
        ```

    Envs
    { .sb-h5 }

    ??? variable dict "`karakeep_role_docker_envs_default`"

        ```yaml
        # Type: dict
        karakeep_role_docker_envs_default: 
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          HOARDER_VERSION: "release"
          MEILI_ADDR: "{{ 'http://' + karakeep_meili_name + ':' + karakeep_meili_port }}"
          BROWSER_WEB_URL: "{{ 'http://' + karakeep_chrome_name + ':' + karakeep_chrome_port }}"
          NEXTAUTH_SECRET: "{{ karakeep_saltbox_facts.facts.secret_key }}"
          MEILI_MASTER_KEY: "{{ meilisearch_saltbox_facts.facts.secret_key }}"
          NEXTAUTH_URL: "{{ lookup('role_var', '_web_url', role='karakeep') }}"
          DATA_DIR: "/data"
        ```

    ??? variable dict "`karakeep_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        karakeep_role_docker_envs_custom: {}
        ```

    Volumes
    { .sb-h5 }

    ??? variable list "`karakeep_role_docker_volumes_default`"

        ```yaml
        # Type: list
        karakeep_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='karakeep') }}/data:/data"
        ```

    ??? variable list "`karakeep_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        karakeep_role_docker_volumes_custom: []
        ```

    Hostname
    { .sb-h5 }

    ??? variable string "`karakeep_role_docker_hostname`"

        ```yaml
        # Type: string
        karakeep_role_docker_hostname: "{{ karakeep_name }}"
        ```

    Networks
    { .sb-h5 }

    ??? variable string "`karakeep_role_docker_networks_alias`"

        ```yaml
        # Type: string
        karakeep_role_docker_networks_alias: "{{ karakeep_name }}"
        ```

    ??? variable list "`karakeep_role_docker_networks_default`"

        ```yaml
        # Type: list
        karakeep_role_docker_networks_default: []
        ```

    ??? variable list "`karakeep_role_docker_networks_custom`"

        ```yaml
        # Type: list
        karakeep_role_docker_networks_custom: []
        ```

    Restart Policy
    { .sb-h5 }

    ??? variable string "`karakeep_role_docker_restart_policy`"

        ```yaml
        # Type: string
        karakeep_role_docker_restart_policy: unless-stopped
        ```

    State
    { .sb-h5 }

    ??? variable string "`karakeep_role_docker_state`"

        ```yaml
        # Type: string
        karakeep_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`karakeep_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        karakeep_role_autoheal_enabled: true
        ```

    ??? variable string "`karakeep_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        karakeep_role_depends_on: ""
        ```

    ??? variable string "`karakeep_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        karakeep_role_depends_on_delay: "0"
        ```

    ??? variable string "`karakeep_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        karakeep_role_depends_on_healthchecks:
        ```

    ??? variable bool "`karakeep_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        karakeep_role_diun_enabled: true
        ```

    ??? variable bool "`karakeep_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        karakeep_role_dns_enabled: true
        ```

    ??? variable bool "`karakeep_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        karakeep_role_docker_controller: true
        ```

    ??? variable bool "`karakeep_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        karakeep_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`karakeep_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        karakeep_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`karakeep_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        karakeep_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`karakeep_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        karakeep_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`karakeep_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`karakeep_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        karakeep_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`karakeep_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        karakeep_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`karakeep_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        karakeep_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`karakeep_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        karakeep_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`karakeep_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        karakeep_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            karakeep_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "karakeep2.{{ user.domain }}"
              - "karakeep.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`karakeep_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        karakeep_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            karakeep_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'karakeep2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`karakeep_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        karakeep_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
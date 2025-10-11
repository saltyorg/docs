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

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        karakeep_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    karakeep_name: karakeep

    ```

??? example "Container Dependant Variables"

    ```yaml
    # Type: string
    karakeep_meili_name: "meilisearch"

    # Type: string
    karakeep_meili_port: "7700"

    # Type: string
    karakeep_chrome_name: "chrome"

    # Type: string
    karakeep_chrome_port: "9222"

    ```

??? example "Paths"

    ```yaml
    # Type: string
    karakeep_role_paths_folder: "{{ karakeep_name }}"

    # Type: string
    karakeep_role_paths_location: "{{ server_appdata_path }}/{{ karakeep_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    karakeep_role_web_subdomain: "{{ karakeep_name }}"

    # Type: string
    karakeep_role_web_domain: "{{ user.domain }}"

    # Type: string
    karakeep_role_web_port: "3000"

    # Type: string
    karakeep_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='karakeep') + '.' + lookup('role_var', '_web_domain', role='karakeep')
                            if (lookup('role_var', '_web_subdomain', role='karakeep') | length > 0)
                            else lookup('role_var', '_web_domain', role='karakeep')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    karakeep_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='karakeep') }}"

    # Type: string
    karakeep_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='karakeep') }}"

    # Type: bool (true/false)
    karakeep_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    karakeep_role_traefik_sso_middleware: ""

    # Type: string
    karakeep_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    karakeep_role_traefik_middleware_custom: ""

    # Type: string
    karakeep_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    karakeep_role_traefik_enabled: true

    # Type: bool (true/false)
    karakeep_role_traefik_api_enabled: false

    # Type: string
    karakeep_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    karakeep_role_docker_container: "{{ karakeep_name }}"

    # Image
    # Type: bool (true/false)
    karakeep_role_docker_image_pull: true

    # Type: string
    karakeep_role_docker_image_repo: "ghcr.io/karakeep-app/karakeep"

    # Type: string
    karakeep_role_docker_image_tag: "release"

    # Type: string
    karakeep_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='karakeep') }}:{{ lookup('role_var', '_docker_image_tag', role='karakeep') }}"

    # Envs
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

    # Type: dict
    karakeep_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    karakeep_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='karakeep') }}/data:/data"

    # Type: list
    karakeep_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    karakeep_role_docker_hostname: "{{ karakeep_name }}"

    # Networks
    # Type: string
    karakeep_role_docker_networks_alias: "{{ karakeep_name }}"

    # Type: list
    karakeep_role_docker_networks_default: []

    # Type: list
    karakeep_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    karakeep_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    karakeep_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    karakeep_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    karakeep_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    karakeep_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    karakeep_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    karakeep_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    karakeep_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    karakeep_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    karakeep_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    karakeep_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    karakeep_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    karakeep_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    karakeep_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    karakeep_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    karakeep_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    karakeep_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    karakeep_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    karakeep_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        karakeep_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "karakeep2.{{ user.domain }}"
          - "karakeep.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        karakeep_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'karakeep2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

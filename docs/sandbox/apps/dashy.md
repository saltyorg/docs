---
hide:
  - tags
tags:
  - dashy
  - dashboard
  - homepage
---

# Dashy

## What is it?

[Dashy](https://dashy.to/) is the "Ultimate homepage for your homelab"

- **Theming**
  - With tons of built-in themes to choose form, plus a UI color palette editor, you can have a unique looking dashboard in no time. There is also support for custom CSS, and since all properties use CSS variables, it is easy to override.
- **Icons**
  - Dashy can auto-fetch icons from the favicon of each of your apps/ services. There is also native support for Font Awesome, Material Design Icons, emoji icons and of course normal images.
- **Status Indicators**
  - Get an instant overview of the health of each of your apps with status indicators. Once enabled, a small dot next to each app will show weather it is up and online, with more info like response time visible on hover.
- **Authentication**
  - Need to protect your dashboard, the simple auth feature is super quick to enable, and has support for multiple users with granular controls. Dashy also has built-in support for Keycloak and other SSO providers.
- **Widgets**
  - Display dynamic content from any API-enabled service. Dashy comes bundled with 50+ pre-built widgets for self-hosted services, productivity and monitoring.
- **Search & Shortcuts**
  - To search, just start typing, results will be filtered instantly. Use the arrow keys or tab to navigate through results, and press enter to launch. You can also create custom shortcuts for frequently used apps, or add custom tags for easier searching. Dashy can also be used to search the web using your favorite search engine.
- **Configuration**
  - Dashy's config is specified in a simple YAML file. But you can also configure the directly through the UI, and have changes written to, and backed up on disk. Real-time validation and hints are in place to help you.
- **Customizable Layouts**
  - Structure your dashboard to fit your use case. From the UI, you can choose between different layouts, item sizes, show/ hide components, switch themes plus more. You can customize pretty much every area of your dashboard. There are config options for custom header, footer, nav bar links, title etc. You can also choose to hide any elements you don't need.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://dashy.to/){: .header-icons } | [:octicons-link-16: Docs](https://dashy.to/docs){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/Lissy93/dashy){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/lissy93/dashy){: .header-icons }|

Recommended install types: Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-dashy

```

### 2. URL

- To access dashy, visit `https://dashy._yourdomain.com_`

### 3. Setup

To edit your config, edit the `.yaml` file in dashys appdata folder, which is typically located at `/opt/dashy/`. You can also edit the config directly through the UI.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        dashy_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `dashy_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `dashy_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    dashy_name: dashy

    ```

??? example "Paths"

    ```yaml
    # Type: string
    dashy_role_paths_folder: "{{ dashy_name }}"

    # Type: string
    dashy_role_paths_location: "{{ server_appdata_path }}/{{ dashy_role_paths_folder }}"

    # Type: string
    dashy_role_paths_config_location: "{{ dashy_role_paths_location }}/conf.yml"

    ```

??? example "Web"

    ```yaml
    # Type: string
    dashy_role_web_subdomain: "{{ dashy_name }}"

    # Type: string
    dashy_role_web_domain: "{{ user.domain }}"

    # Type: string
    dashy_role_web_port: "8080"

    # Type: string
    dashy_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='dashy') + '.' + lookup('role_var', '_web_domain', role='dashy')
                         if (lookup('role_var', '_web_subdomain', role='dashy') | length > 0)
                         else lookup('role_var', '_web_domain', role='dashy')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    dashy_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='dashy') }}"

    # Type: string
    dashy_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='dashy') }}"

    # Type: bool (true/false)
    dashy_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    dashy_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    dashy_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    dashy_role_traefik_middleware_custom: ""

    # Type: string
    dashy_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    dashy_role_traefik_enabled: true

    # Type: bool (true/false)
    dashy_role_traefik_api_enabled: false

    # Type: string
    dashy_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    dashy_role_docker_container: "{{ dashy_name }}"

    # Image
    # Type: bool (true/false)
    dashy_role_docker_image_pull: true

    # Type: string
    dashy_role_docker_image_repo: "lissy93/dashy"

    # Type: string
    dashy_role_docker_image_tag: "latest"

    # Type: string
    dashy_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='dashy') }}:{{ lookup('role_var', '_docker_image_tag', role='dashy') }}"

    # Volumes
    # Type: list
    dashy_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='dashy') }}:/app/user-data"

    # Type: list
    dashy_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    dashy_role_docker_hostname: "{{ dashy_name }}"

    # Networks
    # Type: string
    dashy_role_docker_networks_alias: "{{ dashy_name }}"

    # Type: list
    dashy_role_docker_networks_default: []

    # Type: list
    dashy_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    dashy_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    dashy_role_docker_state: started

    # Healthcheck
    # Type: dict
    dashy_role_docker_healthcheck: 
      test: ["CMD", "yarn", "health-check"]
      interval: 10s
      timeout: 5s
      retries: 10
      start_period: 10s

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    dashy_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    dashy_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    dashy_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    dashy_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    dashy_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    dashy_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    dashy_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    dashy_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    dashy_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    dashy_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    dashy_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    dashy_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    dashy_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    dashy_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    dashy_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    dashy_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    dashy_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        dashy_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "dashy2.{{ user.domain }}"
          - "dashy.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        dashy_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'dashy2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

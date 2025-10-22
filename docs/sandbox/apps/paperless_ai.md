---
hide:
  - tags
tags:
  - paperless-ai
  - documents
  - ai
---

# Paperless AI

## What is it?

[Paperless AI](https://clusterzx.github.io/paperless-ai/) is an AI-enhanced extension for Paperless-ngx that adds automatic classification, smart tagging, and semantic search using OpenAI-compatible APIs. It builds on the community-supported document management system that scans, indexes and archives documents with OCR.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://clusterzx.github.io/paperless-ai/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/clusterzx/paperless-ai){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/clusterzx/paperless-ai){: .header-icons }|

### 1. Installation

``` shell
sb install sandbox-paperless-ai
```

### 2. URL

- To access Paperless AI, visit `https://paperless-ai.xDOMAIN_NAMEx`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        paperless_ai_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `paperless_ai_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `paperless_ai_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    paperless_ai_name: paperless-ai

    ```

??? example "Paths"

    ```yaml
    # Type: string
    paperless_ai_role_paths_folder: "{{ paperless_ai_name }}"

    # Type: string
    paperless_ai_role_paths_location: "{{ server_appdata_path }}/{{ paperless_ai_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    paperless_ai_role_web_subdomain: "{{ paperless_ai_name }}"

    # Type: string
    paperless_ai_role_web_domain: "{{ user.domain }}"

    # Type: string
    paperless_ai_role_web_port: "3000"

    # Type: string
    paperless_ai_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='paperless_ai') + '.' + lookup('role_var', '_web_domain', role='paperless_ai')
                                if (lookup('role_var', '_web_subdomain', role='paperless_ai') | length > 0)
                                else lookup('role_var', '_web_domain', role='paperless_ai')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    paperless_ai_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='paperless_ai') }}"

    # Type: string
    paperless_ai_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='paperless_ai') }}"

    # Type: bool (true/false)
    paperless_ai_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    paperless_ai_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    paperless_ai_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    paperless_ai_role_traefik_middleware_custom: ""

    # Type: string
    paperless_ai_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    paperless_ai_role_traefik_enabled: true

    # Type: bool (true/false)
    paperless_ai_role_traefik_api_enabled: false

    # Type: string
    paperless_ai_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    paperless_ai_role_docker_container: "{{ paperless_ai_name }}"

    # Image
    # Type: bool (true/false)
    paperless_ai_role_docker_image_pull: true

    # Type: string
    paperless_ai_role_docker_image_tag: "latest"

    # Type: string
    paperless_ai_role_docker_image_repo: "clusterzx/paperless-ai"

    # Type: string
    paperless_ai_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='paperless_ai') }}:{{ lookup('role_var', '_docker_image_tag', role='paperless_ai') }}"

    # Envs
    # Type: dict
    paperless_ai_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    paperless_ai_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    paperless_ai_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='paperless_ai') }}:/app/data"

    # Type: list
    paperless_ai_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    paperless_ai_role_docker_hostname: "{{ paperless_ai_name }}"

    # Networks
    # Type: string
    paperless_ai_role_docker_networks_alias: "{{ paperless_ai_name }}"

    # Type: list
    paperless_ai_role_docker_networks_default: []

    # Type: list
    paperless_ai_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    paperless_ai_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    paperless_ai_role_docker_state: started

    # Create Docker Container Timeout
    # Type: int
    paperless_ai_docker_create_timeout: 300

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    paperless_ai_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    paperless_ai_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    paperless_ai_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    paperless_ai_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    paperless_ai_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    paperless_ai_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    paperless_ai_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    paperless_ai_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    paperless_ai_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    paperless_ai_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    paperless_ai_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    paperless_ai_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    paperless_ai_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    paperless_ai_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    paperless_ai_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    paperless_ai_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    paperless_ai_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        paperless_ai_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "paperless_ai2.{{ user.domain }}"
          - "paperless_ai.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        paperless_ai_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'paperless_ai2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

---
hide:
  - tags
tags:
  - photoprism
  - photos
  - ai
---

# Photoprism

## What is it?

[Photoprism®](https://photoprism.app/) is an AI-Powered Photos App for the Decentralized Web. It makes use of the latest technologies to tag and find pictures automatically without getting in your way. You can run it at home, on a private server, or in the cloud.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself. Note: This is not a multi-user app.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://photoprism.app/){: .header-icons } | [:octicons-link-16: Docs](https://docs.photoprism.app/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/photoprism/photoprism){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/photoprism/photoprism){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-photoprism

```

### 2. URL

- To access Photoprism, visit `https://photoprism._yourdomain.com_`

### 3. Setup

- Default login:

  ``` { .yaml}
  Username: admin
  Password: your_normal_password
  ```

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        photoprism_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `photoprism_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `photoprism_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    photoprism_name: photoprism

    ```

??? example "Paths"

    ```yaml
    # Type: string
    photoprism_role_paths_folder: "{{ photoprism_name }}"

    # Type: string
    photoprism_role_paths_location: "{{ server_appdata_path }}/{{ photoprism_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    photoprism_role_web_subdomain: "{{ photoprism_name }}"

    # Type: string
    photoprism_role_web_domain: "{{ user.domain }}"

    # Type: string
    photoprism_role_web_port: "2342"

    # Type: string
    photoprism_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='photoprism') + '.' + lookup('role_var', '_web_domain', role='photoprism')
                              if (lookup('role_var', '_web_subdomain', role='photoprism') | length > 0)
                              else lookup('role_var', '_web_domain', role='photoprism')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    photoprism_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='photoprism') }}"

    # Type: string
    photoprism_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='photoprism') }}"

    # Type: bool (true/false)
    photoprism_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    photoprism_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    photoprism_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    photoprism_role_traefik_middleware_custom: ""

    # Type: string
    photoprism_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    photoprism_role_traefik_enabled: true

    # Type: bool (true/false)
    photoprism_role_traefik_api_enabled: false

    # Type: string
    photoprism_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    photoprism_role_docker_container: "{{ photoprism_name }}"

    # Image
    # Type: bool (true/false)
    photoprism_role_docker_image_pull: true

    # Type: string
    photoprism_role_docker_image_tag: "latest"

    # Type: string
    photoprism_role_docker_image_repo: "photoprism/photoprism"

    # Type: string
    photoprism_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='photoprism') }}:{{ lookup('role_var', '_docker_image_tag', role='photoprism') }}"

    # Envs
    # Type: dict
    photoprism_role_docker_envs_default: 
      PHOTOPRISM_ADMIN_PASSWORD: "{{ user.pass }}"
      PHOTOPRISM_AUTH_MODE: "password"
      PHOTOPRISM_SITE_URL: "{{ lookup('role_var', '_web_url', role='photoprism') }}"
      PHOTOPRISM_ORIGINALS_LIMIT: "5000"
      PHOTOPRISM_HTTP_COMPRESSION: "gzip"
      PHOTOPRISM_LOG_LEVEL: "info"
      PHOTOPRISM_READONLY: "false"
      PHOTOPRISM_EXPERIMENTAL: "false"
      PHOTOPRISM_DISABLE_CHOWN: "false"
      PHOTOPRISM_DISABLE_WEBDAV: "false"
      PHOTOPRISM_DISABLE_SETTINGS: "false"
      PHOTOPRISM_DISABLE_TENSORFLOW: "false"
      PHOTOPRISM_DISABLE_FACES: "false"
      PHOTOPRISM_DISABLE_CLASSIFICATION: "false"
      PHOTOPRISM_DISABLE_RAW: "false"
      PHOTOPRISM_RAW_PRESETS: "false"
      PHOTOPRISM_JPEG_QUALITY: "85"
      PHOTOPRISM_DETECT_NSFW: "false"
      PHOTOPRISM_UPLOAD_NSFW: "false"
      PHOTOPRISM_DATABASE_DRIVER: "mysql"
      PHOTOPRISM_DATABASE_SERVER: "mariadb:3306"
      PHOTOPRISM_DATABASE_NAME: "photoprisms"
      PHOTOPRISM_DATABASE_USER: "root"
      PHOTOPRISM_DATABASE_PASSWORD: "password321"
      PHOTOPRISM_SITE_CAPTION: "AI-Powered Photos App"
      PHOTOPRISM_SITE_DESCRIPTION: "Trying out PhotoPrism!"
      PHOTOPRISM_SITE_AUTHOR: "{{ user.name }}"
      PHOTOPRISM_INIT: "gpu tensorflow"

    # Type: dict
    photoprism_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    photoprism_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='photoprism') }}/originals:/photoprism/originals"
      - "{{ lookup('role_var', '_paths_location', role='photoprism') }}/import:/photoprism/import"
      - "{{ lookup('role_var', '_paths_location', role='photoprism') }}/storage:/photoprism/storage"

    # Type: list
    photoprism_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    photoprism_role_docker_hostname: "{{ photoprism_name }}"

    # Networks
    # Type: string
    photoprism_role_docker_networks_alias: "{{ photoprism_name }}"

    # Type: list
    photoprism_role_docker_networks_default: []

    # Type: list
    photoprism_role_docker_networks_custom: []

    # Security Opts
    # Type: list
    photoprism_role_docker_security_opts_default: 
      - "seccomp=unconfined"
      - "apparmor=unconfined"

    # Type: list
    photoprism_role_docker_security_opts_custom: []

    # Working Directory
    # Type: string
    photoprism_role_docker_working_dir: "/photoprism"

    # Restart Policy
    # Type: string
    photoprism_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    photoprism_role_docker_state: started

    # User
    # Type: string
    photoprism_role_docker_user: "{{ uid }}:{{ gid }}"

    # Dependencies
    # Type: string
    photoprism_role_depends_on: "mariadb"

    # Type: string
    photoprism_role_depends_on_delay: "0"

    # Type: string
    photoprism_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    photoprism_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    photoprism_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    photoprism_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    photoprism_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    photoprism_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    photoprism_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    photoprism_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    photoprism_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    photoprism_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    photoprism_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    photoprism_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    photoprism_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    photoprism_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    photoprism_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    photoprism_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    photoprism_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    photoprism_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        photoprism_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "photoprism2.{{ user.domain }}"
          - "photoprism.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        photoprism_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'photoprism2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

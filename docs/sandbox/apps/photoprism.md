---
icon: material/docker
hide:
  - tags
tags:
  - photoprism
  - photos
  - ai
---

# Photoprism

## Overview

[Photoprism®](https://photoprism.app/) is an AI-Powered Photos App for the Decentralized Web. It makes use of the latest technologies to tag and find pictures automatically without getting in your way. You can run it at home, on a private server, or in the cloud.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself. Note: This is not a multi-user app.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://photoprism.app/){: .header-icons } | [:octicons-link-16: Docs](https://docs.photoprism.app/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/photoprism/photoprism){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/photoprism/photoprism){: .header-icons }|

### 1. Installation

```shell
sb install sandbox-photoprism
```

### 2. URL

- To access Photoprism, visit <https://photoprism.iYOUR_DOMAIN_NAMEi>

### 3. Setup

- Default login:

  ```yaml
  Username: admin
  Password: your_normal_password
  ```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    photoprism_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `photoprism_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `photoprism_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`photoprism_name`"

        ```yaml
        # Type: string
        photoprism_name: photoprism
        ```

=== "Paths"

    ??? variable string "`photoprism_role_paths_folder`"

        ```yaml
        # Type: string
        photoprism_role_paths_folder: "{{ photoprism_name }}"
        ```

    ??? variable string "`photoprism_role_paths_location`"

        ```yaml
        # Type: string
        photoprism_role_paths_location: "{{ server_appdata_path }}/{{ photoprism_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`photoprism_role_web_subdomain`"

        ```yaml
        # Type: string
        photoprism_role_web_subdomain: "{{ photoprism_name }}"
        ```

    ??? variable string "`photoprism_role_web_domain`"

        ```yaml
        # Type: string
        photoprism_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`photoprism_role_web_port`"

        ```yaml
        # Type: string
        photoprism_role_web_port: "2342"
        ```

    ??? variable string "`photoprism_role_web_url`"

        ```yaml
        # Type: string
        photoprism_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='photoprism') + '.' + lookup('role_var', '_web_domain', role='photoprism')
                                  if (lookup('role_var', '_web_subdomain', role='photoprism') | length > 0)
                                  else lookup('role_var', '_web_domain', role='photoprism')) }}"
        ```

=== "DNS"

    ??? variable string "`photoprism_role_dns_record`"

        ```yaml
        # Type: string
        photoprism_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='photoprism') }}"
        ```

    ??? variable string "`photoprism_role_dns_zone`"

        ```yaml
        # Type: string
        photoprism_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='photoprism') }}"
        ```

    ??? variable bool "`photoprism_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`photoprism_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        photoprism_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`photoprism_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        photoprism_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`photoprism_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        photoprism_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`photoprism_role_traefik_certresolver`"

        ```yaml
        # Type: string
        photoprism_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`photoprism_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_traefik_enabled: true
        ```

    ??? variable bool "`photoprism_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_traefik_api_enabled: false
        ```

    ??? variable string "`photoprism_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        photoprism_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`photoprism_role_docker_container`"

        ```yaml
        # Type: string
        photoprism_role_docker_container: "{{ photoprism_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`photoprism_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_docker_image_pull: true
        ```

    ??? variable string "`photoprism_role_docker_image_tag`"

        ```yaml
        # Type: string
        photoprism_role_docker_image_tag: "latest"
        ```

    ??? variable string "`photoprism_role_docker_image_repo`"

        ```yaml
        # Type: string
        photoprism_role_docker_image_repo: "photoprism/photoprism"
        ```

    ??? variable string "`photoprism_role_docker_image`"

        ```yaml
        # Type: string
        photoprism_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='photoprism') }}:{{ lookup('role_var', '_docker_image_tag', role='photoprism') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`photoprism_role_docker_envs_default`"

        ```yaml
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
        ```

    ??? variable dict "`photoprism_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        photoprism_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`photoprism_role_docker_volumes_default`"

        ```yaml
        # Type: list
        photoprism_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='photoprism') }}/originals:/photoprism/originals"
          - "{{ lookup('role_var', '_paths_location', role='photoprism') }}/import:/photoprism/import"
          - "{{ lookup('role_var', '_paths_location', role='photoprism') }}/storage:/photoprism/storage"
        ```

    ??? variable list "`photoprism_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        photoprism_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`photoprism_role_docker_hostname`"

        ```yaml
        # Type: string
        photoprism_role_docker_hostname: "{{ photoprism_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`photoprism_role_docker_networks_alias`"

        ```yaml
        # Type: string
        photoprism_role_docker_networks_alias: "{{ photoprism_name }}"
        ```

    ??? variable list "`photoprism_role_docker_networks_default`"

        ```yaml
        # Type: list
        photoprism_role_docker_networks_default: []
        ```

    ??? variable list "`photoprism_role_docker_networks_custom`"

        ```yaml
        # Type: list
        photoprism_role_docker_networks_custom: []
        ```

    <h5>Security Opts</h5>

    ??? variable list "`photoprism_role_docker_security_opts_default`"

        ```yaml
        # Type: list
        photoprism_role_docker_security_opts_default:
          - "seccomp=unconfined"
          - "apparmor=unconfined"
        ```

    ??? variable list "`photoprism_role_docker_security_opts_custom`"

        ```yaml
        # Type: list
        photoprism_role_docker_security_opts_custom: []
        ```

    <h5>Working Directory</h5>

    ??? variable string "`photoprism_role_docker_working_dir`"

        ```yaml
        # Type: string
        photoprism_role_docker_working_dir: "/photoprism"
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`photoprism_role_docker_restart_policy`"

        ```yaml
        # Type: string
        photoprism_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`photoprism_role_docker_state`"

        ```yaml
        # Type: string
        photoprism_role_docker_state: started
        ```

    <h5>User</h5>

    ??? variable string "`photoprism_role_docker_user`"

        ```yaml
        # Type: string
        photoprism_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

    <h5>Dependencies</h5>

    ??? variable string "`photoprism_role_depends_on`"

        ```yaml
        # Type: string
        photoprism_role_depends_on: "mariadb"
        ```

    ??? variable string "`photoprism_role_depends_on_delay`"

        ```yaml
        # Type: string
        photoprism_role_depends_on_delay: "0"
        ```

    ??? variable string "`photoprism_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        photoprism_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`photoprism_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        photoprism_role_autoheal_enabled: true
        ```

    ??? variable string "`photoprism_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        photoprism_role_depends_on: ""
        ```

    ??? variable string "`photoprism_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        photoprism_role_depends_on_delay: "0"
        ```

    ??? variable string "`photoprism_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        photoprism_role_depends_on_healthchecks:
        ```

    ??? variable bool "`photoprism_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        photoprism_role_diun_enabled: true
        ```

    ??? variable bool "`photoprism_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        photoprism_role_dns_enabled: true
        ```

    ??? variable bool "`photoprism_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        photoprism_role_docker_controller: true
        ```

    ??? variable bool "`photoprism_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_docker_volumes_download:
        ```

    ??? variable bool "`photoprism_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        photoprism_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`photoprism_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        photoprism_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`photoprism_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        photoprism_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`photoprism_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        photoprism_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`photoprism_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`photoprism_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        photoprism_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`photoprism_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        photoprism_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`photoprism_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        photoprism_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`photoprism_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        photoprism_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`photoprism_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        photoprism_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            photoprism_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "photoprism2.{{ user.domain }}"
              - "photoprism.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`photoprism_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        photoprism_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            photoprism_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'photoprism2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`photoprism_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        photoprism_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
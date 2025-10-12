---
hide:
  - tags
tags:
  - duplicati
  - backup
  - sync
---

# Duplicati

## What is it?

[Duplicati](https://duplicati.com/) is a free, open-source backup client that securely stores encrypted, incremental, compressed backups on cloud storage services and remote file servers. It works with a variety of storage types, including FTP, SSH, WebDAV, and cloud services like Backblaze B2, Tardigrade, and Amazon S3.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://duplicati.com/){: .header-icons } | [:octicons-link-16: Docs](https://duplicati.readthedocs.io/en/latest/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/duplicati/duplicati){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/linuxserver/duplicati){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-duplicati

```

### 2. URL

- To access duplicati, visit `https://duplicati._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        duplicati_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `duplicati_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `duplicati_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    duplicati_name: duplicati

    ```

??? example "Paths"

    ```yaml
    # Type: string
    duplicati_role_paths_folder: "{{ duplicati_name }}"

    # Type: string
    duplicati_role_paths_location: "{{ server_appdata_path }}/{{ duplicati_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    duplicati_role_web_subdomain: "{{ duplicati_name }}"

    # Type: string
    duplicati_role_web_domain: "{{ user.domain }}"

    # Type: string
    duplicati_role_web_port: "8200"

    # Type: string
    duplicati_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='duplicati') + '.' + lookup('role_var', '_web_domain', role='duplicati')
                             if (lookup('role_var', '_web_subdomain', role='duplicati') | length > 0)
                             else lookup('role_var', '_web_domain', role='duplicati')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    duplicati_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='duplicati') }}"

    # Type: string
    duplicati_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='duplicati') }}"

    # Type: bool (true/false)
    duplicati_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    duplicati_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    duplicati_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    duplicati_role_traefik_middleware_custom: ""

    # Type: string
    duplicati_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    duplicati_role_traefik_enabled: true

    # Type: bool (true/false)
    duplicati_role_traefik_api_enabled: true

    # Type: string
    duplicati_role_traefik_api_endpoint: "PathPrefix(`/api`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    duplicati_role_docker_container: "{{ duplicati_name }}"

    # Image
    # Type: bool (true/false)
    duplicati_role_docker_image_pull: true

    # Type: string
    duplicati_role_docker_image_repo: "linuxserver/duplicati"

    # Type: string
    duplicati_role_docker_image_tag: "latest"

    # Type: string
    duplicati_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='duplicati') }}:{{ lookup('role_var', '_docker_image_tag', role='duplicati') }}"

    # Envs
    # Type: dict
    duplicati_role_docker_envs_default: 
      TZ: "{{ tz }}"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"

    # Type: dict
    duplicati_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    duplicati_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='duplicati') }}:/config"
      - "/opt:/saltbox/opt"
      - "/srv/git/saltbox:/saltbox/saltbox"

    # Type: list
    duplicati_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    duplicati_role_docker_hostname: "{{ duplicati_name }}"

    # Networks
    # Type: string
    duplicati_role_docker_networks_alias: "{{ duplicati_name }}"

    # Type: list
    duplicati_role_docker_networks_default: []

    # Type: list
    duplicati_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    duplicati_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    duplicati_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    duplicati_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    duplicati_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    duplicati_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    duplicati_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    duplicati_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    duplicati_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    duplicati_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    duplicati_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    duplicati_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    duplicati_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    duplicati_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    duplicati_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    duplicati_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    duplicati_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    duplicati_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    duplicati_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    duplicati_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        duplicati_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "duplicati2.{{ user.domain }}"
          - "duplicati.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        duplicati_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'duplicati2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

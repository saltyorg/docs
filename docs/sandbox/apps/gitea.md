---
hide:
  - tags
tags:
  - gitea
  - development
  - git
---

# Gitea

## What is it?

[Gitea](https://gitea.io/en-us/) is a community managed lightweight code hosting solution written in Go.

Gitea is a painless self-hosted Git service. It is similar to GitHub, Bitbucket, and GitLab. Gitea is a fork of Gogs.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://gitea.io/en-us/){: .header-icons } | [:octicons-link-16: Docs](https://docs.gitea.io/en-us/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/go-gitea/){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/gitea/gitea){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-gitea

```

### 2. URL

- To access Gitea, visit `https://gitea._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        gitea_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `gitea_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `gitea_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    gitea_name: gitea

    ```

??? example "Paths"

    ```yaml
    # Type: string
    gitea_role_paths_folder: "{{ gitea_name }}"

    # Type: string
    gitea_role_paths_location: "{{ server_appdata_path }}/{{ gitea_role_paths_folder }}"

    # Type: bool (true/false)
    gitea_role_paths_recursive: true

    ```

??? example "Web"

    ```yaml
    # Type: string
    gitea_role_web_subdomain: "{{ gitea_name }}"

    # Type: string
    gitea_role_web_domain: "{{ user.domain }}"

    # Type: string
    gitea_role_web_port: "3000"

    # Type: string
    gitea_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='gitea') + '.' + lookup('role_var', '_web_domain', role='gitea')
                         if (lookup('role_var', '_web_subdomain', role='gitea') | length > 0)
                         else lookup('role_var', '_web_domain', role='gitea')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    gitea_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='gitea') }}"

    # Type: string
    gitea_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='gitea') }}"

    # Type: bool (true/false)
    gitea_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    gitea_role_traefik_sso_middleware: ""

    # Type: string
    gitea_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    gitea_role_traefik_middleware_custom: ""

    # Type: string
    gitea_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    gitea_role_traefik_enabled: true

    # Type: bool (true/false)
    gitea_role_traefik_api_enabled: false

    # Type: string
    gitea_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    gitea_role_docker_container: "{{ gitea_name }}"

    # Image
    # Type: bool (true/false)
    gitea_role_docker_image_pull: true

    # Type: string
    gitea_role_docker_image_repo: "gitea/gitea"

    # Type: string
    gitea_role_docker_image_tag: "latest"

    # Type: string
    gitea_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='gitea') }}:{{ lookup('role_var', '_docker_image_tag', role='gitea') }}"

    # Envs
    # Type: dict
    gitea_role_docker_envs_default: 
      USER_UID: "{{ uid }}"
      USER_GID: "{{ gid }}"
      GITEA__database__DB_TYPE: "mysql"
      GITEA__database__HOST: "mariadb:3306"
      GITEA__database__USER: "root"
      GITEA__database__PASSWD: "{{ lookup('role_var', '_docker_env_password', role='mariadb') }}"
      GITEA__database__NAME: "gitea"
      DISABLE_SSH: "true"
      ROOT_URL: "{{ lookup('role_var', '_web_url', role='gitea') }}/"

    # Type: dict
    gitea_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    gitea_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='gitea') }}:/data"
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro

    # Type: list
    gitea_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    gitea_role_docker_hostname: "{{ gitea_name }}"

    # Networks
    # Type: string
    gitea_role_docker_networks_alias: "{{ gitea_name }}"

    # Type: list
    gitea_role_docker_networks_default: []

    # Type: list
    gitea_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    gitea_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    gitea_role_docker_state: started

    # Dependencies
    # Type: string
    gitea_role_depends_on: "mariadb"

    # Type: string
    gitea_role_depends_on_delay: "0"

    # Type: string
    gitea_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    gitea_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    gitea_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    gitea_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    gitea_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    gitea_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    gitea_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    gitea_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    gitea_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    gitea_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    gitea_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    gitea_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    gitea_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    gitea_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    gitea_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    gitea_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    gitea_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    gitea_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        gitea_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "gitea2.{{ user.domain }}"
          - "gitea.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        gitea_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'gitea2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

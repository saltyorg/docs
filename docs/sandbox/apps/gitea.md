---
icon: material/docker
hide:
  - tags
tags:
  - gitea
  - development
  - git
---

# Gitea

## Overview

[Gitea](https://gitea.io/en-us/) is a community managed lightweight code hosting solution written in Go.

Gitea is a painless self-hosted Git service. It is similar to GitHub, Bitbucket, and GitLab. Gitea is a fork of Gogs.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://gitea.io/en-us/){: .header-icons } | [:octicons-link-16: Docs](https://docs.gitea.io/en-us/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/go-gitea/){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/gitea/gitea){: .header-icons }|

### 1. Installation

```shell
sb install sandbox-gitea
```

### 2. URL

- To access Gitea, visit <https://gitea.iYOUR_DOMAIN_NAMEi>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    gitea_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `gitea_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `gitea_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`gitea_name`"

        ```yaml
        # Type: string
        gitea_name: gitea
        ```

=== "Paths"

    ??? variable string "`gitea_role_paths_folder`"

        ```yaml
        # Type: string
        gitea_role_paths_folder: "{{ gitea_name }}"
        ```

    ??? variable string "`gitea_role_paths_location`"

        ```yaml
        # Type: string
        gitea_role_paths_location: "{{ server_appdata_path }}/{{ gitea_role_paths_folder }}"
        ```

    ??? variable bool "`gitea_role_paths_recursive`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_paths_recursive: true
        ```

=== "Web"

    ??? variable string "`gitea_role_web_subdomain`"

        ```yaml
        # Type: string
        gitea_role_web_subdomain: "{{ gitea_name }}"
        ```

    ??? variable string "`gitea_role_web_domain`"

        ```yaml
        # Type: string
        gitea_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`gitea_role_web_port`"

        ```yaml
        # Type: string
        gitea_role_web_port: "3000"
        ```

    ??? variable string "`gitea_role_web_url`"

        ```yaml
        # Type: string
        gitea_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='gitea') + '.' + lookup('role_var', '_web_domain', role='gitea')
                             if (lookup('role_var', '_web_subdomain', role='gitea') | length > 0)
                             else lookup('role_var', '_web_domain', role='gitea')) }}"
        ```

=== "DNS"

    ??? variable string "`gitea_role_dns_record`"

        ```yaml
        # Type: string
        gitea_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='gitea') }}"
        ```

    ??? variable string "`gitea_role_dns_zone`"

        ```yaml
        # Type: string
        gitea_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='gitea') }}"
        ```

    ??? variable bool "`gitea_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`gitea_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        gitea_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`gitea_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        gitea_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`gitea_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        gitea_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`gitea_role_traefik_certresolver`"

        ```yaml
        # Type: string
        gitea_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`gitea_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_traefik_enabled: true
        ```

    ??? variable bool "`gitea_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_traefik_api_enabled: false
        ```

    ??? variable string "`gitea_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        gitea_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`gitea_role_docker_container`"

        ```yaml
        # Type: string
        gitea_role_docker_container: "{{ gitea_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`gitea_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_docker_image_pull: true
        ```

    ??? variable string "`gitea_role_docker_image_repo`"

        ```yaml
        # Type: string
        gitea_role_docker_image_repo: "gitea/gitea"
        ```

    ??? variable string "`gitea_role_docker_image_tag`"

        ```yaml
        # Type: string
        gitea_role_docker_image_tag: "latest"
        ```

    ??? variable string "`gitea_role_docker_image`"

        ```yaml
        # Type: string
        gitea_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='gitea') }}:{{ lookup('role_var', '_docker_image_tag', role='gitea') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`gitea_role_docker_envs_default`"

        ```yaml
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
        ```

    ??? variable dict "`gitea_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        gitea_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`gitea_role_docker_volumes_default`"

        ```yaml
        # Type: list
        gitea_role_docker_volumes_default:
          - "{{ lookup('role_var', '_paths_location', role='gitea') }}:/data"
          - /etc/timezone:/etc/timezone:ro
          - /etc/localtime:/etc/localtime:ro
        ```

    ??? variable list "`gitea_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        gitea_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`gitea_role_docker_hostname`"

        ```yaml
        # Type: string
        gitea_role_docker_hostname: "{{ gitea_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`gitea_role_docker_networks_alias`"

        ```yaml
        # Type: string
        gitea_role_docker_networks_alias: "{{ gitea_name }}"
        ```

    ??? variable list "`gitea_role_docker_networks_default`"

        ```yaml
        # Type: list
        gitea_role_docker_networks_default: []
        ```

    ??? variable list "`gitea_role_docker_networks_custom`"

        ```yaml
        # Type: list
        gitea_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`gitea_role_docker_restart_policy`"

        ```yaml
        # Type: string
        gitea_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`gitea_role_docker_state`"

        ```yaml
        # Type: string
        gitea_role_docker_state: started
        ```

    <h5>Dependencies</h5>

    ??? variable string "`gitea_role_depends_on`"

        ```yaml
        # Type: string
        gitea_role_depends_on: "mariadb"
        ```

    ??? variable string "`gitea_role_depends_on_delay`"

        ```yaml
        # Type: string
        gitea_role_depends_on_delay: "0"
        ```

    ??? variable string "`gitea_role_depends_on_healthchecks`"

        ```yaml
        # Type: string
        gitea_role_depends_on_healthchecks: "false"
        ```

=== "Global Override Options"

    ??? variable bool "`gitea_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        gitea_role_autoheal_enabled: true
        ```

    ??? variable string "`gitea_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        gitea_role_depends_on: ""
        ```

    ??? variable string "`gitea_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        gitea_role_depends_on_delay: "0"
        ```

    ??? variable string "`gitea_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        gitea_role_depends_on_healthchecks:
        ```

    ??? variable bool "`gitea_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        gitea_role_diun_enabled: true
        ```

    ??? variable bool "`gitea_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        gitea_role_dns_enabled: true
        ```

    ??? variable bool "`gitea_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        gitea_role_docker_controller: true
        ```

    ??? variable bool "`gitea_role_docker_volumes_download`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_docker_volumes_download:
        ```

    ??? variable bool "`gitea_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        gitea_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`gitea_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        gitea_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`gitea_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        gitea_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`gitea_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        gitea_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`gitea_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`gitea_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        gitea_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`gitea_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        gitea_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`gitea_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        gitea_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`gitea_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        gitea_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`gitea_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        gitea_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            gitea_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "gitea2.{{ user.domain }}"
              - "gitea.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`gitea_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        gitea_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            gitea_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'gitea2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`gitea_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        gitea_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
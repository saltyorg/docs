---
hide:
  - tags
tags:
  - cherry
  - bookmarks
  - organization
---

# Cherry

## Overview

[Cherry](https://cherry.haishan.me/) is a bookmark service that is open source.

- The code of Cherry service and the browser extension are all available on GitHub.

- It's self-hostable. Your data in in your own hands. Using SQLite, management and backup is a breeze.

- It has a simple UI. But you got all the features you want for a bookmark service. Tags, groups, full text search and browser extensions.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |
|-------------|-------------|-------------|
| [:material-home: Project home](https://cherry.haishan.me/){: .header-icons } | [:octicons-link-16: Docs](https://cherry.haishan.me/docs/intro){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/haishanh/cherry){: .header-icons } |

### 1. Installation

``` shell

sb install sandbox-cherry

```

### 2. URL

- To access Cherry, visit <https://cherry.iYOUR_DOMAIN_NAMEi>

### 3. Setup

- Default login:

  ``` { .yaml}
  Username: "your user from accounts.yml"
  Password: your_normal_password
  ```

!!!note
    To create an additional user, use Cherry cli: `docker exec cherry cherry create-user <email> <password>`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    cherry_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `cherry_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `cherry_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`cherry_name`"

        ```yaml
        # Type: string
        cherry_name: cherry
        ```

=== "Paths"

    ??? variable string "`cherry_role_paths_folder`"

        ```yaml
        # Type: string
        cherry_role_paths_folder: "{{ cherry_name }}"
        ```

    ??? variable string "`cherry_role_paths_location`"

        ```yaml
        # Type: string
        cherry_role_paths_location: "{{ server_appdata_path }}/{{ cherry_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`cherry_role_web_subdomain`"

        ```yaml
        # Type: string
        cherry_role_web_subdomain: "{{ cherry_name }}"
        ```

    ??? variable string "`cherry_role_web_domain`"

        ```yaml
        # Type: string
        cherry_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`cherry_role_web_port`"

        ```yaml
        # Type: string
        cherry_role_web_port: "8000"
        ```

    ??? variable string "`cherry_role_web_url`"

        ```yaml
        # Type: string
        cherry_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='cherry') + '.' + lookup('role_var', '_web_domain', role='cherry')
                              if (lookup('role_var', '_web_subdomain', role='cherry') | length > 0)
                              else lookup('role_var', '_web_domain', role='cherry')) }}"
        ```

=== "DNS"

    ??? variable string "`cherry_role_dns_record`"

        ```yaml
        # Type: string
        cherry_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='cherry') }}"
        ```

    ??? variable string "`cherry_role_dns_zone`"

        ```yaml
        # Type: string
        cherry_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='cherry') }}"
        ```

    ??? variable bool "`cherry_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        cherry_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`cherry_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        cherry_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`cherry_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        cherry_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`cherry_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        cherry_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`cherry_role_traefik_certresolver`"

        ```yaml
        # Type: string
        cherry_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`cherry_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        cherry_role_traefik_enabled: true
        ```

    ??? variable bool "`cherry_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        cherry_role_traefik_api_enabled: true
        ```

    ??? variable string "`cherry_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        cherry_role_traefik_api_endpoint: "PathPrefix(`/api`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`cherry_role_docker_container`"

        ```yaml
        # Type: string
        cherry_role_docker_container: "{{ cherry_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`cherry_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        cherry_role_docker_image_pull: true
        ```

    ??? variable string "`cherry_role_docker_image_repo`"

        ```yaml
        # Type: string
        cherry_role_docker_image_repo: "haishanh/cherry"
        ```

    ??? variable string "`cherry_role_docker_image_tag`"

        ```yaml
        # Type: string
        cherry_role_docker_image_tag: "latest"
        ```

    ??? variable string "`cherry_role_docker_image`"

        ```yaml
        # Type: string
        cherry_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='cherry') }}:{{ lookup('role_var', '_docker_image_tag', role='cherry') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`cherry_role_docker_envs_default`"

        ```yaml
        # Type: dict
        cherry_role_docker_envs_default: 
          TZ: "{{ tz }}"
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          JWT_SECRET: "{{ cherry_secret_key.stdout }}"
          ENABLE_HTTP_REMOTE_USER: "1"
        ```

    ??? variable dict "`cherry_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        cherry_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`cherry_role_docker_volumes_default`"

        ```yaml
        # Type: list
        cherry_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='cherry') }}:/data"
        ```

    ??? variable list "`cherry_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        cherry_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`cherry_role_docker_hostname`"

        ```yaml
        # Type: string
        cherry_role_docker_hostname: "{{ cherry_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`cherry_role_docker_networks_alias`"

        ```yaml
        # Type: string
        cherry_role_docker_networks_alias: "{{ cherry_name }}"
        ```

    ??? variable list "`cherry_role_docker_networks_default`"

        ```yaml
        # Type: list
        cherry_role_docker_networks_default: []
        ```

    ??? variable list "`cherry_role_docker_networks_custom`"

        ```yaml
        # Type: list
        cherry_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`cherry_role_docker_restart_policy`"

        ```yaml
        # Type: string
        cherry_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`cherry_role_docker_state`"

        ```yaml
        # Type: string
        cherry_role_docker_state: started
        ```

    <h5>Healthcheck</h5>

    ??? variable dict "`cherry_role_docker_healthcheck`"

        ```yaml
        # Type: dict
        cherry_role_docker_healthcheck: 
          test: ["NONE"]
        ```

=== "Global Override Options"

    ??? variable bool "`cherry_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        cherry_role_autoheal_enabled: true
        ```

    ??? variable string "`cherry_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        cherry_role_depends_on: ""
        ```

    ??? variable string "`cherry_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        cherry_role_depends_on_delay: "0"
        ```

    ??? variable string "`cherry_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        cherry_role_depends_on_healthchecks:
        ```

    ??? variable bool "`cherry_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        cherry_role_diun_enabled: true
        ```

    ??? variable bool "`cherry_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        cherry_role_dns_enabled: true
        ```

    ??? variable bool "`cherry_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        cherry_role_docker_controller: true
        ```

    ??? variable bool "`cherry_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        cherry_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`cherry_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        cherry_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`cherry_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        cherry_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`cherry_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        cherry_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`cherry_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        cherry_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`cherry_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        cherry_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`cherry_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        cherry_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`cherry_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        cherry_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`cherry_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        cherry_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`cherry_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        cherry_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            cherry_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "cherry2.{{ user.domain }}"
              - "cherry.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`cherry_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        cherry_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            cherry_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'cherry2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`cherry_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        cherry_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
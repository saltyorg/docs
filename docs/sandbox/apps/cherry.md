---
hide:
  - tags
tags:
  - cherry
  - bookmarks
  - organization
---

# Cherry

## What is it?

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

- To access Cherry, visit `https://cherry._yourdomain.com_`

### 3. Setup

- Default login:

  ``` { .yaml}
  Username: "your user from accounts.yml"
  Password: your_normal_password
  ```

!!!note
    To create an additional user, use Cherry cli: `docker exec cherry cherry create-user <email> <password>`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        cherry_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    cherry_name: cherry

    ```

??? example "Paths"

    ```yaml
    # Type: string
    cherry_role_paths_folder: "{{ cherry_name }}"

    # Type: string
    cherry_role_paths_location: "{{ server_appdata_path }}/{{ cherry_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    cherry_role_web_subdomain: "{{ cherry_name }}"

    # Type: string
    cherry_role_web_domain: "{{ user.domain }}"

    # Type: string
    cherry_role_web_port: "8000"

    # Type: string
    cherry_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='cherry') + '.' + lookup('role_var', '_web_domain', role='cherry')
                          if (lookup('role_var', '_web_subdomain', role='cherry') | length > 0)
                          else lookup('role_var', '_web_domain', role='cherry')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    cherry_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='cherry') }}"

    # Type: string
    cherry_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='cherry') }}"

    # Type: bool (true/false)
    cherry_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    cherry_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    cherry_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    cherry_role_traefik_middleware_custom: ""

    # Type: string
    cherry_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    cherry_role_traefik_enabled: true

    # Type: bool (true/false)
    cherry_role_traefik_api_enabled: true

    # Type: string
    cherry_role_traefik_api_endpoint: "PathPrefix(`/api`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    cherry_role_docker_container: "{{ cherry_name }}"

    # Image
    # Type: bool (true/false)
    cherry_role_docker_image_pull: true

    # Type: string
    cherry_role_docker_image_repo: "haishanh/cherry"

    # Type: string
    cherry_role_docker_image_tag: "latest"

    # Type: string
    cherry_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='cherry') }}:{{ lookup('role_var', '_docker_image_tag', role='cherry') }}"

    # Envs
    # Type: dict
    cherry_role_docker_envs_default: 
      TZ: "{{ tz }}"
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      JWT_SECRET: "{{ cherry_secret_key.stdout }}"
      ENABLE_HTTP_REMOTE_USER: "1"

    # Type: dict
    cherry_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    cherry_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='cherry') }}:/data"

    # Type: list
    cherry_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    cherry_role_docker_hostname: "{{ cherry_name }}"

    # Networks
    # Type: string
    cherry_role_docker_networks_alias: "{{ cherry_name }}"

    # Type: list
    cherry_role_docker_networks_default: []

    # Type: list
    cherry_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    cherry_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    cherry_role_docker_state: started

    # Healthcheck
    # Type: dict
    cherry_role_docker_healthcheck: 
      test: ["NONE"]

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    cherry_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    cherry_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    cherry_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    cherry_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    cherry_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    cherry_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    cherry_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    cherry_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    cherry_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    cherry_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    cherry_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    cherry_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    cherry_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    cherry_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    cherry_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    cherry_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    cherry_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        cherry_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "cherry2.{{ user.domain }}"
          - "cherry.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        cherry_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'cherry2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

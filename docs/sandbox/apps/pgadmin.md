---
hide:
  - tags
tags:
  - pgadmin
  - database
  - admin
---

# pgadmin

## What is it?

[pgadmin](https://www.pgadmin.org/) is a popular and feature rich Open Source administration and development platform for PostgreSQL.

!!! info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.pgadmin.org/){: .header-icons } | [:octicons-link-16: Docs](https://www.pgadmin.org/docs/pgadmin4/6.14/getting_started.html){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/pgadmin-org/pgadmin4){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/dpage/pgadmin4/){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-pgadmin

```

### 2. URL

- To access pgadmin, visit `https://pgadmin._yourdomain.com_`

### 3. Setup

- Default login:

  ``` { .yaml}
  Username: "your email from accounts.yml"
  Password: your_normal_password
  ```

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        pgadmin_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `pgadmin_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `pgadmin_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    pgadmin_name: pgadmin

    ```

??? example "Web"

    ```yaml
    # Type: string
    pgadmin_role_web_subdomain: "{{ pgadmin_name }}"

    # Type: string
    pgadmin_role_web_domain: "{{ user.domain }}"

    # Type: string
    pgadmin_role_web_port: "80"

    # Type: string
    pgadmin_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='pgadmin') + '.' + lookup('role_var', '_web_domain', role='pgadmin')
                           if (lookup('role_var', '_web_subdomain', role='pgadmin') | length > 0)
                           else lookup('role_var', '_web_domain', role='pgadmin')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    pgadmin_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='pgadmin') }}"

    # Type: string
    pgadmin_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='pgadmin') }}"

    # Type: bool (true/false)
    pgadmin_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    pgadmin_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    pgadmin_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    pgadmin_role_traefik_middleware_custom: ""

    # Type: string
    pgadmin_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    pgadmin_role_traefik_enabled: true

    # Type: bool (true/false)
    pgadmin_role_traefik_api_enabled: false

    # Type: string
    pgadmin_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    pgadmin_role_docker_container: "{{ pgadmin_name }}"

    # Image
    # Type: bool (true/false)
    pgadmin_role_docker_image_pull: true

    # Type: string
    pgadmin_role_docker_image_tag: "latest"

    # Type: string
    pgadmin_role_docker_image_repo: "dpage/pgadmin4"

    # Type: string
    pgadmin_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='pgadmin') }}:{{ lookup('role_var', '_docker_image_tag', role='pgadmin') }}"

    # Envs
    # Type: dict
    pgadmin_role_docker_envs_default: 
      PGADMIN_DEFAULT_EMAIL: "{{ user.email }}"
      PGADMIN_DEFAULT_PASSWORD: "{{ user.pass }}"

    # Type: dict
    pgadmin_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    pgadmin_role_docker_volumes_default: 
      - "pgadmin:/var/lib/pgadmin"

    # Type: list
    pgadmin_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    pgadmin_role_docker_hostname: "{{ pgadmin_name }}"

    # Networks
    # Type: string
    pgadmin_role_docker_networks_alias: "{{ pgadmin_name }}"

    # Type: list
    pgadmin_role_docker_networks_default: []

    # Type: list
    pgadmin_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    pgadmin_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    pgadmin_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    pgadmin_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    pgadmin_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    pgadmin_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    pgadmin_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    pgadmin_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    pgadmin_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    pgadmin_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    pgadmin_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    pgadmin_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    pgadmin_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    pgadmin_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    pgadmin_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    pgadmin_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    pgadmin_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    pgadmin_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    pgadmin_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    pgadmin_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        pgadmin_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "pgadmin2.{{ user.domain }}"
          - "pgadmin.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        pgadmin_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'pgadmin2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

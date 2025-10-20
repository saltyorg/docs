---
hide:
  - tags
tags:
  - forgejo
  - development
  - git
---

# Forgejo

## What is it?

[Forgejo](https://www.Forgejo.dev/) is a self-hosted lightweight software forge.
Easy to install and low maintenance, it just does the job.

- **Simple software project management**: Ease of use is important to get things done efficiently. Forgejo’s user experience is designed for collaboration and productivity.
- **Self-hosted alternative to GitHub**: Liberate your software from proprietary shackles. Forgejo offers a familiar environment to GitHub users, allowing smooth transition to a platform you own.
- **Easy to install and maintain**: Hosting your own software forge does not require expert skills. With Forgejo you can control your server with minimal effort.
- **Lightweight and performant**: With a rich feature set, Forgejo still has a low server profile and requires an order of magnitude less resources than other forges.
- **Guaranteed 100% Free Software**: Forgejo will always be Free and Open Source Software. Furthermore we exclusively use Free Software for our own project development.
- **Beyond coding, we forge ahead**: An exciting future awaits. We will innovate the Software Forge and enable collaborative software development facilitated by decentralized platforms.

!!! info
    By default, the role is **NOT** protected behind your Authelia/SSO middleware. You have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://Forgejo.dev/){: .header-icons } | [:octicons-link-16: Docs](https://Forgejo.dev/docs/introduction/manage-services){: .header-icons } | [:octicons-mark-github-16: Codeberg](https://codeberg.org/forgejo/forgejo){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/ajnart/Forgejo/){: .header-icons }|

Recommended install types: Saltbox, Core

### 1. Installation

``` shell

sb install sandbox-forgejo

```

### 2. URL

- To access Forgejo, visit `https://forgejo._yourdomain.com_`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        forgejo_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `forgejo_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `forgejo_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    forgejo_name: forgejo

    ```

??? example "Paths"

    ```yaml
    # Type: string
    forgejo_role_paths_folder: "{{ forgejo_name }}"

    # Type: string
    forgejo_role_paths_location: "{{ server_appdata_path }}/{{ forgejo_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    forgejo_role_web_subdomain: "{{ forgejo_name }}"

    # Type: string
    forgejo_role_web_domain: "{{ user.domain }}"

    # Type: string
    forgejo_role_web_port: "3000"

    # Type: string
    forgejo_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='forgejo') + '.' + lookup('role_var', '_web_domain', role='forgejo')
                           if (lookup('role_var', '_web_subdomain', role='forgejo') | length > 0)
                           else lookup('role_var', '_web_domain', role='forgejo')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    forgejo_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='forgejo') }}"

    # Type: string
    forgejo_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='forgejo') }}"

    # Type: bool (true/false)
    forgejo_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    forgejo_role_traefik_sso_middleware: ""

    # Type: string
    forgejo_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    forgejo_role_traefik_middleware_custom: ""

    # Type: string
    forgejo_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    forgejo_role_traefik_enabled: true

    # Type: bool (true/false)
    forgejo_role_traefik_api_enabled: false

    # Type: string
    forgejo_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    forgejo_role_docker_container: "{{ forgejo_name }}"

    # Image
    # Type: bool (true/false)
    forgejo_role_docker_image_pull: true

    # Type: string
    forgejo_role_docker_image_repo: "codeberg.org/forgejo/forgejo"

    # Type: string
    forgejo_role_docker_image_tag: "13" # the Codeberg container registry does not provide a "latest" tag

    # Type: string
    forgejo_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='forgejo') }}:{{ lookup('role_var', '_docker_image_tag', role='forgejo') }}"

    # Envs
    # Type: dict
    forgejo_role_docker_envs_default: 
      USER_UID: "{{ uid }}"
      USER_GID: "{{ gid }}"
      DB_TYPE: "mysql"
      DB_HOST: "mariadb:3306"
      DB_USER: "root"
      DB_PASS: "password321"
      DB_DATABASE: "forgejo"
      DISABLE_SSH: "true"
      ROOT_URL: "{{ lookup('role_var', '_web_url', role='forgejo') }}/"

    # Type: dict
    forgejo_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    forgejo_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='forgejo') }}:/data"
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro

    # Type: list
    forgejo_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    forgejo_role_docker_hostname: "{{ forgejo_name }}"

    # Networks
    # Type: string
    forgejo_role_docker_networks_alias: "{{ forgejo_name }}"

    # Type: list
    forgejo_role_docker_networks_default: []

    # Type: list
    forgejo_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    forgejo_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    forgejo_role_docker_state: started

    # Dependencies
    # Type: string
    forgejo_role_depends_on: "mariadb"

    # Type: string
    forgejo_role_depends_on_delay: "0"

    # Type: string
    forgejo_role_depends_on_healthchecks: "false"

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    forgejo_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    forgejo_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    forgejo_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    forgejo_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    forgejo_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    forgejo_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    forgejo_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    forgejo_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    forgejo_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    forgejo_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    forgejo_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    forgejo_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    forgejo_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    forgejo_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    forgejo_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    forgejo_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    forgejo_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        forgejo_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "forgejo2.{{ user.domain }}"
          - "forgejo.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        forgejo_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'forgejo2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

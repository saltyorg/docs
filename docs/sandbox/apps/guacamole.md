---
hide:
  - tags
tags:
  - guacamole
  - networking
  - remote-access
---

# Guacamole

## What is it?

[Guacamole](https://guacamole.apache.org/) is a clientless remote desktop gateway. It supports standard protocols like VNC, RDP, and SSH.

We call it clientless because no plugins or client software are required.

Thanks to HTML5, once Guacamole is installed on a server, all you need to access your desktops is a web browser.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://guacamole.apache.org/){: .header-icons } | [:octicons-link-16: Docs](https://guacamole.apache.org/doc/gug/){: .header-icons } | [:octicons-mark-github-16: Github](https://www.github.com/jason-bean/docker-guacamole){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jasonbean/guacamole){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-guacamole

```

### 2. URL

- To access Guacamole, visit `https://guacamole.xDOMAIN_NAMEx`

### 3. Setup

- Log in with user and password `guacadmin`. Change the default user and password immediately.

- [:octicons-link-16: Documentation: Guacamole Docs](https://guacamole.apache.org/doc/gug/){: .header-icons }

### 4. Enable Extensions (Optional)

Guacamole supports various authentication extensions that can be enabled through your [Inventory](https://docs.saltbox.dev/saltbox/inventory/). Add any of the following options to enable specific extensions:

=== "TOTP (Two-Factor Authentication)"

    Enable time-based one-time passwords for enhanced security:

    ```yml
    guacamole_docker_envs_custom:
      OPT_TOTP: "Y"
    ```

=== "LDAP"

    Enable LDAP authentication:

    ```yml
    guacamole_docker_envs_custom:
      OPT_LDAP: "Y"
    ```

=== "RADIUS"

    Enable RADIUS authentication:

    ```yml
    guacamole_docker_envs_custom:
      OPT_RADIUS: "Y"
    ```

=== "Duo Security"

    Enable Duo two-factor authentication:

    ```yml
    guacamole_docker_envs_custom:
      OPT_DUO: "Y"
    ```

=== "CAS"

    Enable Central Authentication Service:

    ```yml
    guacamole_docker_envs_custom:
      OPT_CAS: "Y"
    ```

=== "OpenID Connect"

    Enable OpenID Connect authentication:

    ```yml
    guacamole_docker_envs_custom:
      OPT_OPENID: "Y"
    ```

=== "SAML"

    Enable SAML authentication:

    ```yml
    guacamole_docker_envs_custom:
      OPT_SAML: "Y"
    ```

=== "Header Authentication"

    Enable HTTP header-based authentication:

    ```yml
    guacamole_docker_envs_custom:
      OPT_HEADER: "Y"
    ```

After adding any extension options, run `sb install sandbox-guacamole` to apply changes.

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        guacamole_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `guacamole_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `guacamole_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    guacamole_name: guacamole

    ```

??? example "Settings"

    ```yaml
    # Type: bool (true/false)
    guacamole_role_totp_enable: false

    # Type: bool (true/false)
    guacamole_role_ldap_enable: false

    # Type: bool (true/false)
    guacamole_role_radius_enable: false

    # Type: bool (true/false)
    guacamole_role_duo_enable: false

    # Type: bool (true/false)
    guacamole_role_cas_enable: false

    # Type: bool (true/false)
    guacamole_role_openid_enable: false

    # Type: bool (true/false)
    guacamole_role_saml_enable: false

    # Type: bool (true/false)
    guacamole_role_header_enable: false

    ```

??? example "Paths"

    ```yaml
    # Type: string
    guacamole_role_paths_folder: "{{ guacamole_name }}"

    # Type: string
    guacamole_role_paths_location: "{{ server_appdata_path }}/{{ guacamole_role_paths_folder }}"

    ```

??? example "Web"

    ```yaml
    # Type: string
    guacamole_role_web_subdomain: "{{ guacamole_name }}"

    # Type: string
    guacamole_role_web_domain: "{{ user.domain }}"

    # Type: string
    guacamole_role_web_port: "8080"

    # Type: string
    guacamole_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='guacamole') + '.' + lookup('role_var', '_web_domain', role='guacamole')
                             if (lookup('role_var', '_web_subdomain', role='guacamole') | length > 0)
                             else lookup('role_var', '_web_domain', role='guacamole')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    guacamole_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='guacamole') }}"

    # Type: string
    guacamole_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='guacamole') }}"

    # Type: bool (true/false)
    guacamole_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    guacamole_role_traefik_sso_middleware: ""

    # Type: string
    guacamole_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    guacamole_role_traefik_middleware_custom: ""

    # Type: string
    guacamole_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    guacamole_role_traefik_enabled: true

    # Type: bool (true/false)
    guacamole_role_traefik_api_enabled: false

    # Type: string
    guacamole_role_traefik_api_endpoint: ""

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    guacamole_role_docker_container: "{{ guacamole_name }}"

    # Image
    # Type: bool (true/false)
    guacamole_role_docker_image_pull: true

    # Type: string
    guacamole_role_docker_image_repo: "jasonbean/guacamole"

    # Type: string
    guacamole_role_docker_image_tag: "latest"

    # Type: string
    guacamole_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='guacamole') }}:{{ lookup('role_var', '_docker_image_tag', role='guacamole') }}"

    # Envs
    # Type: dict
    guacamole_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      OPT_MYSQL: "Y"
      OPT_TOTP: "{{ 'Y' if lookup('role_var', '_totp_enable', role='guacamole') else omit }}"
      OPT_LDAP: "{{ 'Y' if lookup('role_var', '_ldap_enable', role='guacamole') else omit }}"
      OPT_RADIUS: "{{ 'Y' if lookup('role_var', '_radius_enable', role='guacamole') else omit }}"
      OPT_DUO: "{{ 'Y' if lookup('role_var', '_duo_enable', role='guacamole') else omit }}"
      OPT_CAS: "{{ 'Y' if lookup('role_var', '_cas_enable', role='guacamole') else omit }}"
      OPT_OPENID: "{{ 'Y' if lookup('role_var', '_openid_enable', role='guacamole') else omit }}"
      OPT_SAML: "{{ 'Y' if lookup('role_var', '_saml_enable', role='guacamole') else omit }}"
      OPT_HEADER: "{{ 'Y' if lookup('role_var', '_header_enable', role='guacamole') else omit }}"

    # Type: dict
    guacamole_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    guacamole_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='guacamole') }}/config:/config"

    # Type: list
    guacamole_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    guacamole_role_docker_hostname: "{{ guacamole_name }}"

    # Networks
    # Type: string
    guacamole_role_docker_networks_alias: "{{ guacamole_name }}"

    # Type: list
    guacamole_role_docker_networks_default: []

    # Type: list
    guacamole_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    guacamole_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    guacamole_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    guacamole_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    guacamole_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    guacamole_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    guacamole_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    guacamole_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    guacamole_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    guacamole_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    guacamole_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    guacamole_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    guacamole_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    guacamole_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    guacamole_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    guacamole_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    guacamole_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    guacamole_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    guacamole_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    guacamole_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        guacamole_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "guacamole2.{{ user.domain }}"
          - "guacamole.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        guacamole_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'guacamole2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

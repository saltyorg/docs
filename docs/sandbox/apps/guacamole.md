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

- To access Guacamole, visit <https://guacamole.iYOUR_DOMAIN_NAMEi>

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

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    guacamole_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `guacamole_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `guacamole_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`guacamole_name`"

        ```yaml
        # Type: string
        guacamole_name: guacamole
        ```

=== "Settings"

    ??? variable bool "`guacamole_role_totp_enable`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_totp_enable: false
        ```

    ??? variable bool "`guacamole_role_ldap_enable`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_ldap_enable: false
        ```

    ??? variable bool "`guacamole_role_radius_enable`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_radius_enable: false
        ```

    ??? variable bool "`guacamole_role_duo_enable`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_duo_enable: false
        ```

    ??? variable bool "`guacamole_role_cas_enable`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_cas_enable: false
        ```

    ??? variable bool "`guacamole_role_openid_enable`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_openid_enable: false
        ```

    ??? variable bool "`guacamole_role_saml_enable`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_saml_enable: false
        ```

    ??? variable bool "`guacamole_role_header_enable`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_header_enable: false
        ```

=== "Paths"

    ??? variable string "`guacamole_role_paths_folder`"

        ```yaml
        # Type: string
        guacamole_role_paths_folder: "{{ guacamole_name }}"
        ```

    ??? variable string "`guacamole_role_paths_location`"

        ```yaml
        # Type: string
        guacamole_role_paths_location: "{{ server_appdata_path }}/{{ guacamole_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`guacamole_role_web_subdomain`"

        ```yaml
        # Type: string
        guacamole_role_web_subdomain: "{{ guacamole_name }}"
        ```

    ??? variable string "`guacamole_role_web_domain`"

        ```yaml
        # Type: string
        guacamole_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`guacamole_role_web_port`"

        ```yaml
        # Type: string
        guacamole_role_web_port: "8080"
        ```

    ??? variable string "`guacamole_role_web_url`"

        ```yaml
        # Type: string
        guacamole_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='guacamole') + '.' + lookup('role_var', '_web_domain', role='guacamole')
                                 if (lookup('role_var', '_web_subdomain', role='guacamole') | length > 0)
                                 else lookup('role_var', '_web_domain', role='guacamole')) }}"
        ```

=== "DNS"

    ??? variable string "`guacamole_role_dns_record`"

        ```yaml
        # Type: string
        guacamole_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='guacamole') }}"
        ```

    ??? variable string "`guacamole_role_dns_zone`"

        ```yaml
        # Type: string
        guacamole_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='guacamole') }}"
        ```

    ??? variable bool "`guacamole_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`guacamole_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        guacamole_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`guacamole_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        guacamole_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`guacamole_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        guacamole_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`guacamole_role_traefik_certresolver`"

        ```yaml
        # Type: string
        guacamole_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`guacamole_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_traefik_enabled: true
        ```

    ??? variable bool "`guacamole_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_traefik_api_enabled: false
        ```

    ??? variable string "`guacamole_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        guacamole_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`guacamole_role_docker_container`"

        ```yaml
        # Type: string
        guacamole_role_docker_container: "{{ guacamole_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`guacamole_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_docker_image_pull: true
        ```

    ??? variable string "`guacamole_role_docker_image_repo`"

        ```yaml
        # Type: string
        guacamole_role_docker_image_repo: "jasonbean/guacamole"
        ```

    ??? variable string "`guacamole_role_docker_image_tag`"

        ```yaml
        # Type: string
        guacamole_role_docker_image_tag: "latest"
        ```

    ??? variable string "`guacamole_role_docker_image`"

        ```yaml
        # Type: string
        guacamole_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='guacamole') }}:{{ lookup('role_var', '_docker_image_tag', role='guacamole') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`guacamole_role_docker_envs_default`"

        ```yaml
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
        ```

    ??? variable dict "`guacamole_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        guacamole_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`guacamole_role_docker_volumes_default`"

        ```yaml
        # Type: list
        guacamole_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='guacamole') }}/config:/config"
        ```

    ??? variable list "`guacamole_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        guacamole_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`guacamole_role_docker_hostname`"

        ```yaml
        # Type: string
        guacamole_role_docker_hostname: "{{ guacamole_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`guacamole_role_docker_networks_alias`"

        ```yaml
        # Type: string
        guacamole_role_docker_networks_alias: "{{ guacamole_name }}"
        ```

    ??? variable list "`guacamole_role_docker_networks_default`"

        ```yaml
        # Type: list
        guacamole_role_docker_networks_default: []
        ```

    ??? variable list "`guacamole_role_docker_networks_custom`"

        ```yaml
        # Type: list
        guacamole_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`guacamole_role_docker_restart_policy`"

        ```yaml
        # Type: string
        guacamole_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`guacamole_role_docker_state`"

        ```yaml
        # Type: string
        guacamole_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`guacamole_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        guacamole_role_autoheal_enabled: true
        ```

    ??? variable string "`guacamole_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        guacamole_role_depends_on: ""
        ```

    ??? variable string "`guacamole_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        guacamole_role_depends_on_delay: "0"
        ```

    ??? variable string "`guacamole_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        guacamole_role_depends_on_healthchecks:
        ```

    ??? variable bool "`guacamole_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        guacamole_role_diun_enabled: true
        ```

    ??? variable bool "`guacamole_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        guacamole_role_dns_enabled: true
        ```

    ??? variable bool "`guacamole_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        guacamole_role_docker_controller: true
        ```

    ??? variable bool "`guacamole_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        guacamole_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`guacamole_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        guacamole_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`guacamole_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        guacamole_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`guacamole_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        guacamole_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`guacamole_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`guacamole_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        guacamole_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`guacamole_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        guacamole_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`guacamole_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        guacamole_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`guacamole_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        guacamole_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`guacamole_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        guacamole_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            guacamole_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "guacamole2.{{ user.domain }}"
              - "guacamole.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`guacamole_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        guacamole_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            guacamole_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'guacamole2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`guacamole_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        guacamole_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
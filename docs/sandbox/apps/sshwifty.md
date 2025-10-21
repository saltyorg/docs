---
hide:
  - tags
tags:
  - sshwifty
  - networking
  - ssh
---

# Sshwifty

## What is it?

[Sshwifty](https://github.com/nirui/sshwifty) is an SSH and Telnet connector made for the Web. It can be deployed on your computer or server to provide SSH and Telnet access interface for any compatible (standard) web browser.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/nirui/sshwifty){: .header-icons } | [:octicons-link-16: Docs](https://github.com/nirui/sshwifty){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/nirui/sshwifty){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/niruix/sshwifty){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-sshwifty

```

### 2. URL

- To access Sshwifty, visit `https://sshwifty._yourdomain.com_`

### 3. Setup

- The pre-configured password is taken from your Saltbox [`accounts.yml`](../../saltbox/install/install.md#step-2-configuration) file located in `/srv/git/saltbox/accounts.yml`

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        sshwifty_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `sshwifty_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `sshwifty_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`sshwifty_name`"

        ```yaml
        # Type: string
        sshwifty_name: sshwifty
        ```

=== "Paths"

    ??? variable string "`sshwifty_role_paths_folder`"

        ```yaml
        # Type: string
        sshwifty_role_paths_folder: "{{ sshwifty_name }}"
        ```

    ??? variable string "`sshwifty_role_paths_location`"

        ```yaml
        # Type: string
        sshwifty_role_paths_location: "{{ server_appdata_path }}/{{ sshwifty_role_paths_folder }}"
        ```

    ??? variable string "`sshwifty_role_paths_config_location`"

        ```yaml
        # Type: string
        sshwifty_role_paths_config_location: "{{ sshwifty_role_paths_location }}/config/sshwifty.conf.json"
        ```

=== "Web"

    ??? variable string "`sshwifty_role_web_subdomain`"

        ```yaml
        # Type: string
        sshwifty_role_web_subdomain: "{{ sshwifty_name }}"
        ```

    ??? variable string "`sshwifty_role_web_domain`"

        ```yaml
        # Type: string
        sshwifty_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`sshwifty_role_web_port`"

        ```yaml
        # Type: string
        sshwifty_role_web_port: "8182"
        ```

    ??? variable string "`sshwifty_role_web_url`"

        ```yaml
        # Type: string
        sshwifty_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='sshwifty') + '.' + lookup('role_var', '_web_domain', role='sshwifty')
                                if (lookup('role_var', '_web_subdomain', role='sshwifty') | length > 0)
                                else lookup('role_var', '_web_domain', role='sshwifty')) }}"
        ```

=== "DNS"

    ??? variable string "`sshwifty_role_dns_record`"

        ```yaml
        # Type: string
        sshwifty_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='sshwifty') }}"
        ```

    ??? variable string "`sshwifty_role_dns_zone`"

        ```yaml
        # Type: string
        sshwifty_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='sshwifty') }}"
        ```

    ??? variable bool "`sshwifty_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`sshwifty_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        sshwifty_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`sshwifty_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        sshwifty_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`sshwifty_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        sshwifty_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`sshwifty_role_traefik_certresolver`"

        ```yaml
        # Type: string
        sshwifty_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`sshwifty_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_traefik_enabled: true
        ```

    ??? variable bool "`sshwifty_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_traefik_api_enabled: false
        ```

    ??? variable string "`sshwifty_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        sshwifty_role_traefik_api_endpoint: ""
        ```

    ??? variable bool "`sshwifty_role_traefik_error_pages_enabled`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_traefik_error_pages_enabled: false
        ```

=== "Docker"

    ##### Container

    ??? variable string "`sshwifty_role_docker_container`"

        ```yaml
        # Type: string
        sshwifty_role_docker_container: "{{ sshwifty_name }}"
        ```

    ##### Image

    ??? variable bool "`sshwifty_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        sshwifty_role_docker_image_pull: true
        ```

    ??? variable string "`sshwifty_role_docker_image_repo`"

        ```yaml
        # Type: string
        sshwifty_role_docker_image_repo: "niruix/sshwifty"
        ```

    ??? variable string "`sshwifty_role_docker_image_tag`"

        ```yaml
        # Type: string
        sshwifty_role_docker_image_tag: "latest"
        ```

    ??? variable string "`sshwifty_role_docker_image`"

        ```yaml
        # Type: string
        sshwifty_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='sshwifty') }}:{{ lookup('role_var', '_docker_image_tag', role='sshwifty') }}"
        ```

    ##### Envs

    ??? variable dict "`sshwifty_role_docker_envs_default`"

        ```yaml
        # Type: dict
        sshwifty_role_docker_envs_default: 
          SSHWIFTY_CONFIG: "/config/sshwifty.conf.json"
        ```

    ??? variable dict "`sshwifty_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        sshwifty_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`sshwifty_role_docker_volumes_default`"

        ```yaml
        # Type: list
        sshwifty_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='sshwifty') }}/config:/config"
        ```

    ??? variable list "`sshwifty_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        sshwifty_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`sshwifty_role_docker_hostname`"

        ```yaml
        # Type: string
        sshwifty_role_docker_hostname: "{{ sshwifty_name }}"
        ```

    ##### Networks

    ??? variable string "`sshwifty_role_docker_networks_alias`"

        ```yaml
        # Type: string
        sshwifty_role_docker_networks_alias: "{{ sshwifty_name }}"
        ```

    ??? variable list "`sshwifty_role_docker_networks_default`"

        ```yaml
        # Type: list
        sshwifty_role_docker_networks_default: []
        ```

    ??? variable list "`sshwifty_role_docker_networks_custom`"

        ```yaml
        # Type: list
        sshwifty_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`sshwifty_role_docker_restart_policy`"

        ```yaml
        # Type: string
        sshwifty_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`sshwifty_role_docker_state`"

        ```yaml
        # Type: string
        sshwifty_role_docker_state: started
        ```

    ##### User

    ??? variable string "`sshwifty_role_docker_user`"

        ```yaml
        # Type: string
        sshwifty_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`sshwifty_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        sshwifty_role_autoheal_enabled: true
        ```

    ??? variable string "`sshwifty_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        sshwifty_role_depends_on: ""
        ```

    ??? variable string "`sshwifty_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        sshwifty_role_depends_on_delay: "0"
        ```

    ??? variable string "`sshwifty_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        sshwifty_role_depends_on_healthchecks:
        ```

    ??? variable bool "`sshwifty_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        sshwifty_role_diun_enabled: true
        ```

    ??? variable bool "`sshwifty_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        sshwifty_role_dns_enabled: true
        ```

    ??? variable bool "`sshwifty_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        sshwifty_role_docker_controller: true
        ```

    ??? variable bool "`sshwifty_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        sshwifty_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`sshwifty_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        sshwifty_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`sshwifty_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        sshwifty_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`sshwifty_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        sshwifty_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`sshwifty_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        sshwifty_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`sshwifty_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        sshwifty_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`sshwifty_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        sshwifty_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`sshwifty_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        sshwifty_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            sshwifty_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "sshwifty2.{{ user.domain }}"
              - "sshwifty.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`sshwifty_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        sshwifty_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            sshwifty_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'sshwifty2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`sshwifty_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        sshwifty_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
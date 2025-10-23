---
hide:
  - tags
tags:
  - airdcpp
  - p2p
  - downloading
---

# AirDC++

## What is it?

[AirDC++](https://www.airdcpp.net/) is an easy to use client for [Advanced Direct Connect](http://en.wikipedia.org/wiki/Advanced_Direct_Connect) and [Direct Connect](http://en.wikipedia.org/wiki/Direct_Connect_(file_sharing)) networks. You are able to join "hubs" with other users, and chat, perform searches and browse the share of each user. It allows you to share files with friends and other people.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://www.airdcpp.net/){: .header-icons } | [:octicons-link-16: Docs](https://airdcpp-web.github.io/docs/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/gangefors/docker-airdcpp-webclient){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/gangefors/airdcpp-webclient/){: .header-icons }|

### 1. Installation

``` shell

sb install sandbox-airdcpp

```

### 2. URL

- To access AirDC++, visit `https://airdcpp._yourdomain.com_`
- Username / password for the default admin account is: admin / password

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    === "Example"

        ```yaml
        airdcpp_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `airdcpp_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `airdcpp_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`airdcpp_name`"

        ```yaml
        # Type: string
        airdcpp_name: airdcpp
        ```

=== "Paths"

    ??? variable string "`airdcpp_role_paths_folder`"

        ```yaml
        # Type: string
        airdcpp_role_paths_folder: "{{ airdcpp_name }}"
        ```

    ??? variable string "`airdcpp_role_paths_location`"

        ```yaml
        # Type: string
        airdcpp_role_paths_location: "{{ server_appdata_path }}/{{ airdcpp_role_paths_folder }}"
        ```

=== "Web"

    ??? variable string "`airdcpp_role_web_subdomain`"

        ```yaml
        # Type: string
        airdcpp_role_web_subdomain: "{{ airdcpp_name }}"
        ```

    ??? variable string "`airdcpp_role_web_domain`"

        ```yaml
        # Type: string
        airdcpp_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`airdcpp_role_web_port`"

        ```yaml
        # Type: string
        airdcpp_role_web_port: "5600"
        ```

    ??? variable string "`airdcpp_role_web_url`"

        ```yaml
        # Type: string
        airdcpp_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='airdcpp') + '.' + lookup('role_var', '_web_domain', role='airdcpp')
                               if (lookup('role_var', '_web_subdomain', role='airdcpp') | length > 0)
                               else lookup('role_var', '_web_domain', role='airdcpp')) }}"
        ```

=== "DNS"

    ??? variable string "`airdcpp_role_dns_record`"

        ```yaml
        # Type: string
        airdcpp_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='airdcpp') }}"
        ```

    ??? variable string "`airdcpp_role_dns_zone`"

        ```yaml
        # Type: string
        airdcpp_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='airdcpp') }}"
        ```

    ??? variable bool "`airdcpp_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        airdcpp_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`airdcpp_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        airdcpp_role_traefik_sso_middleware: ""
        ```

    ??? variable string "`airdcpp_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        airdcpp_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`airdcpp_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        airdcpp_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`airdcpp_role_traefik_certresolver`"

        ```yaml
        # Type: string
        airdcpp_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`airdcpp_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        airdcpp_role_traefik_enabled: true
        ```

    ??? variable bool "`airdcpp_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        airdcpp_role_traefik_api_enabled: false
        ```

    ??? variable string "`airdcpp_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        airdcpp_role_traefik_api_endpoint: ""
        ```

=== "Docker"

    ##### Container

    ??? variable string "`airdcpp_role_docker_container`"

        ```yaml
        # Type: string
        airdcpp_role_docker_container: "{{ airdcpp_name }}"
        ```

    ##### Image

    ??? variable bool "`airdcpp_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        airdcpp_role_docker_image_pull: true
        ```

    ??? variable string "`airdcpp_role_docker_image_repo`"

        ```yaml
        # Type: string
        airdcpp_role_docker_image_repo: "gangefors/airdcpp-webclient"
        ```

    ??? variable string "`airdcpp_role_docker_image_tag`"

        ```yaml
        # Type: string
        airdcpp_role_docker_image_tag: "latest"
        ```

    ??? variable string "`airdcpp_role_docker_image`"

        ```yaml
        # Type: string
        airdcpp_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='airdcpp') }}:{{ lookup('role_var', '_docker_image_tag', role='airdcpp') }}"
        ```

    ##### Ports

    ??? variable list "`airdcpp_role_docker_ports_defaults`"

        ```yaml
        # Type: list
        airdcpp_role_docker_ports_defaults: 
          - "21248:21248"
          - "21248:21248/udp"
          - "21249:21249"
        ```

    ??? variable list "`airdcpp_role_docker_ports_custom`"

        ```yaml
        # Type: list
        airdcpp_role_docker_ports_custom: []
        ```

    ##### Envs

    ??? variable dict "`airdcpp_role_docker_envs_default`"

        ```yaml
        # Type: dict
        airdcpp_role_docker_envs_default: 
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`airdcpp_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        airdcpp_role_docker_envs_custom: {}
        ```

    ##### Volumes

    ??? variable list "`airdcpp_role_docker_volumes_default`"

        ```yaml
        # Type: list
        airdcpp_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='airdcpp') }}:/.airdcpp"
          - "/mnt/local/downloads/airdcpp:/Downloads"
        ```

    ??? variable list "`airdcpp_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        airdcpp_role_docker_volumes_custom: []
        ```

    ##### Hostname

    ??? variable string "`airdcpp_role_docker_hostname`"

        ```yaml
        # Type: string
        airdcpp_role_docker_hostname: "{{ airdcpp_name }}"
        ```

    ##### Networks

    ??? variable string "`airdcpp_role_docker_networks_alias`"

        ```yaml
        # Type: string
        airdcpp_role_docker_networks_alias: "{{ airdcpp_name }}"
        ```

    ??? variable list "`airdcpp_role_docker_networks_default`"

        ```yaml
        # Type: list
        airdcpp_role_docker_networks_default: []
        ```

    ??? variable list "`airdcpp_role_docker_networks_custom`"

        ```yaml
        # Type: list
        airdcpp_role_docker_networks_custom: []
        ```

    ##### Restart Policy

    ??? variable string "`airdcpp_role_docker_restart_policy`"

        ```yaml
        # Type: string
        airdcpp_role_docker_restart_policy: unless-stopped
        ```

    ##### State

    ??? variable string "`airdcpp_role_docker_state`"

        ```yaml
        # Type: string
        airdcpp_role_docker_state: started
        ```

    ##### User

    ??? variable string "`airdcpp_role_docker_user`"

        ```yaml
        # Type: string
        airdcpp_role_docker_user: "{{ uid }}:{{ gid }}"
        ```

=== "Global Override Options"

    ??? variable bool "`airdcpp_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        airdcpp_role_autoheal_enabled: true
        ```

    ??? variable string "`airdcpp_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        airdcpp_role_depends_on: ""
        ```

    ??? variable string "`airdcpp_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        airdcpp_role_depends_on_delay: "0"
        ```

    ??? variable string "`airdcpp_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        airdcpp_role_depends_on_healthchecks:
        ```

    ??? variable bool "`airdcpp_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        airdcpp_role_diun_enabled: true
        ```

    ??? variable bool "`airdcpp_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        airdcpp_role_dns_enabled: true
        ```

    ??? variable bool "`airdcpp_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        airdcpp_role_docker_controller: true
        ```

    ??? variable bool "`airdcpp_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        airdcpp_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`airdcpp_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        airdcpp_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`airdcpp_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        airdcpp_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`airdcpp_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        airdcpp_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`airdcpp_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        airdcpp_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`airdcpp_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        airdcpp_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`airdcpp_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        airdcpp_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`airdcpp_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        airdcpp_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`airdcpp_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        airdcpp_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`airdcpp_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        airdcpp_role_web_fqdn_override: # (1)!
        ```

        1.  Example:

            ```yaml
            airdcpp_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "airdcpp2.{{ user.domain }}"
              - "airdcpp.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`airdcpp_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        airdcpp_role_web_host_override: # (1)!
        ```

        1.  Example:

            ```yaml
            airdcpp_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'airdcpp2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`airdcpp_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        airdcpp_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
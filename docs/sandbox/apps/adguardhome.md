---
hide:
  - tags
tags:
  - adguard
  - dns
  - adblock
---

# AdGuard Home

## What is it?

[AdGuard Home](https://hub.docker.com/r/adguard/adguardhome) is a network-wide, open source software for blocking ads & tracking and for gaining control over all traffic in your home network. After you set it up, it'll cover ALL devices in your home Wi-Fi network, and you won't need any client-side software for that. At the same time, it provides a user-friendly web interface that allows you to easily manage the traffic, even from a mobile device.

There are some concerns with the security of running a DNS server remotely so just be aware of this if you choose to run it on a public network.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://adguard.com/en/adguard-home/overview.html){: .header-icons } | [:octicons-link-16: Docs](https://kb.adguard.com/en/home/overview){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/AdguardTeam/AdGuardHome){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/adguard/adguardhome){: .header-icons }|

!!! info
    AdGuard Home is a latency sensitive DNS server, so it's discouraged to use it when your server is far away from you.

### 1. Installation

``` shell

sb install sandbox-adguardhome

```

### 2. URL

- To access AdGuard Home dashboard, visit <https://adguardhome.iYOUR_DOMAIN_NAMEi>

### 3. Usage

- Make sure you have an application that supports DNS over HTTPS, e.g. [Intra for Android](https://play.google.com/store/apps/details?id=app.intra) or [DNSCloak for iOS](https://apps.apple.com/us/app/dnscloak-secure-dns-client/id1452162351)
- Connect to AdGuard Home with one of the above applications using <https://adguardhome.iYOUR_DOMAIN_NAMEi/dns-query>

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    ```yaml title="Example Override"
    adguardhome_name: "custom_value"
    ```

??? warning "Avoid overriding variables ending in `_default`"

    When overriding variables that end in `_default` (like `adguardhome_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `adguardhome_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable string "`adguardhome_name`"

        ```yaml
        # Type: string
        adguardhome_name: adguardhome
        ```

=== "Paths"

    ??? variable string "`adguardhome_role_paths_folder`"

        ```yaml
        # Type: string
        adguardhome_role_paths_folder: "{{ adguardhome_name }}"
        ```

    ??? variable string "`adguardhome_role_paths_location`"

        ```yaml
        # Type: string
        adguardhome_role_paths_location: "{{ server_appdata_path }}/{{ adguardhome_role_paths_folder }}"
        ```

    ??? variable string "`adguardhome_role_paths_config_path`"

        ```yaml
        # Type: string
        adguardhome_role_paths_config_path: "{{ adguardhome_role_paths_location }}/conf/AdGuardHome.yaml"
        ```

=== "Web"

    ??? variable string "`adguardhome_role_web_subdomain`"

        ```yaml
        # Type: string
        adguardhome_role_web_subdomain: "{{ adguardhome_name }}"
        ```

    ??? variable string "`adguardhome_role_web_domain`"

        ```yaml
        # Type: string
        adguardhome_role_web_domain: "{{ user.domain }}"
        ```

    ??? variable string "`adguardhome_role_web_port`"

        ```yaml
        # Type: string
        adguardhome_role_web_port: "3000"
        ```

    ??? variable string "`adguardhome_role_web_url`"

        ```yaml
        # Type: string
        adguardhome_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='adguardhome') + '.' + lookup('role_var', '_web_domain', role='adguardhome')
                                   if (lookup('role_var', '_web_subdomain', role='adguardhome') | length > 0)
                                   else lookup('role_var', '_web_domain', role='adguardhome')) }}"
        ```

=== "DNS"

    ??? variable string "`adguardhome_role_dns_record`"

        ```yaml
        # Type: string
        adguardhome_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='adguardhome') }}"
        ```

    ??? variable string "`adguardhome_role_dns_zone`"

        ```yaml
        # Type: string
        adguardhome_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='adguardhome') }}"
        ```

    ??? variable bool "`adguardhome_role_dns_proxy`"

        ```yaml
        # Type: bool (true/false)
        adguardhome_role_dns_proxy: "{{ dns_proxied }}"
        ```

=== "Traefik"

    ??? variable string "`adguardhome_role_traefik_sso_middleware`"

        ```yaml
        # Type: string
        adguardhome_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"
        ```

    ??? variable string "`adguardhome_role_traefik_middleware_default`"

        ```yaml
        # Type: string
        adguardhome_role_traefik_middleware_default: "{{ traefik_default_middleware }}"
        ```

    ??? variable string "`adguardhome_role_traefik_middleware_custom`"

        ```yaml
        # Type: string
        adguardhome_role_traefik_middleware_custom: ""
        ```

    ??? variable string "`adguardhome_role_traefik_certresolver`"

        ```yaml
        # Type: string
        adguardhome_role_traefik_certresolver: "{{ traefik_default_certresolver }}"
        ```

    ??? variable bool "`adguardhome_role_traefik_enabled`"

        ```yaml
        # Type: bool (true/false)
        adguardhome_role_traefik_enabled: true
        ```

    ??? variable bool "`adguardhome_role_traefik_api_enabled`"

        ```yaml
        # Type: bool (true/false)
        adguardhome_role_traefik_api_enabled: true
        ```

    ??? variable string "`adguardhome_role_traefik_api_endpoint`"

        ```yaml
        # Type: string
        adguardhome_role_traefik_api_endpoint: "PathPrefix(`/dns-query`)"
        ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`adguardhome_role_docker_container`"

        ```yaml
        # Type: string
        adguardhome_role_docker_container: "{{ adguardhome_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`adguardhome_role_docker_image_pull`"

        ```yaml
        # Type: bool (true/false)
        adguardhome_role_docker_image_pull: true
        ```

    ??? variable string "`adguardhome_role_docker_image_repo`"

        ```yaml
        # Type: string
        adguardhome_role_docker_image_repo: "adguard/adguardhome"
        ```

    ??? variable string "`adguardhome_role_docker_image_tag`"

        ```yaml
        # Type: string
        adguardhome_role_docker_image_tag: "latest"
        ```

    ??? variable string "`adguardhome_role_docker_image`"

        ```yaml
        # Type: string
        adguardhome_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='adguardhome') }}:{{ lookup('role_var', '_docker_image_tag', role='adguardhome') }}"
        ```

    <h5>Envs</h5>

    ??? variable dict "`adguardhome_role_docker_envs_default`"

        ```yaml
        # Type: dict
        adguardhome_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
        ```

    ??? variable dict "`adguardhome_role_docker_envs_custom`"

        ```yaml
        # Type: dict
        adguardhome_role_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable list "`adguardhome_role_docker_volumes_default`"

        ```yaml
        # Type: list
        adguardhome_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='adguardhome') }}/work:/opt/adguardhome/work"
          - "{{ lookup('role_var', '_paths_location', role='adguardhome') }}/conf:/opt/adguardhome/conf"
        ```

    ??? variable list "`adguardhome_role_docker_volumes_custom`"

        ```yaml
        # Type: list
        adguardhome_role_docker_volumes_custom: []
        ```

    <h5>Hostname</h5>

    ??? variable string "`adguardhome_role_docker_hostname`"

        ```yaml
        # Type: string
        adguardhome_role_docker_hostname: "{{ adguardhome_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`adguardhome_role_docker_networks_alias`"

        ```yaml
        # Type: string
        adguardhome_role_docker_networks_alias: "{{ adguardhome_name }}"
        ```

    ??? variable list "`adguardhome_role_docker_networks_default`"

        ```yaml
        # Type: list
        adguardhome_role_docker_networks_default: []
        ```

    ??? variable list "`adguardhome_role_docker_networks_custom`"

        ```yaml
        # Type: list
        adguardhome_role_docker_networks_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`adguardhome_role_docker_restart_policy`"

        ```yaml
        # Type: string
        adguardhome_role_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`adguardhome_role_docker_state`"

        ```yaml
        # Type: string
        adguardhome_role_docker_state: started
        ```

=== "Global Override Options"

    ??? variable bool "`adguardhome_role_autoheal_enabled`"

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        adguardhome_role_autoheal_enabled: true
        ```

    ??? variable string "`adguardhome_role_depends_on`"

        ```yaml
        # List of container dependencies that must be running before the container start
        # Type: string
        adguardhome_role_depends_on: ""
        ```

    ??? variable string "`adguardhome_role_depends_on_delay`"

        ```yaml
        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        adguardhome_role_depends_on_delay: "0"
        ```

    ??? variable string "`adguardhome_role_depends_on_healthchecks`"

        ```yaml
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        adguardhome_role_depends_on_healthchecks:
        ```

    ??? variable bool "`adguardhome_role_diun_enabled`"

        ```yaml
        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        adguardhome_role_diun_enabled: true
        ```

    ??? variable bool "`adguardhome_role_dns_enabled`"

        ```yaml
        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        adguardhome_role_dns_enabled: true
        ```

    ??? variable bool "`adguardhome_role_docker_controller`"

        ```yaml
        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        adguardhome_role_docker_controller: true
        ```

    ??? variable bool "`adguardhome_role_traefik_autodetect_enabled`"

        ```yaml
        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        adguardhome_role_traefik_autodetect_enabled: false
        ```

    ??? variable bool "`adguardhome_role_traefik_crowdsec_enabled`"

        ```yaml
        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        adguardhome_role_traefik_crowdsec_enabled: false
        ```

    ??? variable bool "`adguardhome_role_traefik_error_pages_enabled`"

        ```yaml
        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        adguardhome_role_traefik_error_pages_enabled: false
        ```

    ??? variable bool "`adguardhome_role_traefik_gzip_enabled`"

        ```yaml
        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        adguardhome_role_traefik_gzip_enabled: false
        ```

    ??? variable bool "`adguardhome_role_traefik_middleware_http_api_insecure`"

        ```yaml
        # Type: bool (true/false)
        adguardhome_role_traefik_middleware_http_api_insecure:
        ```

    ??? variable bool "`adguardhome_role_traefik_middleware_http_insecure`"

        ```yaml
        # Type: bool (true/false)
        adguardhome_role_traefik_middleware_http_insecure:
        ```

    ??? variable bool "`adguardhome_role_traefik_robot_enabled`"

        ```yaml
        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        adguardhome_role_traefik_robot_enabled: true
        ```

    ??? variable bool "`adguardhome_role_traefik_tailscale_enabled`"

        ```yaml
        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        adguardhome_role_traefik_tailscale_enabled: false
        ```

    ??? variable bool "`adguardhome_role_traefik_wildcard_enabled`"

        ```yaml
        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        adguardhome_role_traefik_wildcard_enabled: true
        ```

    ??? variable list "`adguardhome_role_web_fqdn_override`"

        ```yaml
        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        adguardhome_role_web_fqdn_override:
        ```

        !!! example "Example Override"

            ```yaml
            adguardhome_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "adguardhome2.{{ user.domain }}"
              - "adguardhome.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    ??? variable string "`adguardhome_role_web_host_override`"

        ```yaml
        # Override the Traefik web host configuration for the container
        # Type: string
        adguardhome_role_web_host_override:
        ```

        !!! example "Example Override"

            ```yaml
            adguardhome_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'adguardhome2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    ??? variable string "`adguardhome_role_web_scheme`"

        ```yaml
        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        adguardhome_role_web_scheme:
        ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
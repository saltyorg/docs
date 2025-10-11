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

- To access AdGuard Home dashboard, visit `https://adguardhome._yourdomain.com_`

### 3. Usage

- Make sure you have an application that supports DNS over HTTPS, e.g. [Intra for Android](https://play.google.com/store/apps/details?id=app.intra) or [DNSCloak for iOS](https://apps.apple.com/us/app/dnscloak-secure-dns-client/id1452162351)
- Connect to AdGuard Home with one of the above applications using `https://adguardhome._yourdomain.com/dns-query`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    === "Example"

        ```yaml
        adguardhome_name: "custom_value"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    ```yaml
    # Type: string
    adguardhome_name: adguardhome

    ```

??? example "Paths"

    ```yaml
    # Type: string
    adguardhome_role_paths_folder: "{{ adguardhome_name }}"

    # Type: string
    adguardhome_role_paths_location: "{{ server_appdata_path }}/{{ adguardhome_role_paths_folder }}"

    # Type: string
    adguardhome_role_paths_config_path: "{{ adguardhome_role_paths_location }}/conf/AdGuardHome.yaml"

    ```

??? example "Web"

    ```yaml
    # Type: string
    adguardhome_role_web_subdomain: "{{ adguardhome_name }}"

    # Type: string
    adguardhome_role_web_domain: "{{ user.domain }}"

    # Type: string
    adguardhome_role_web_port: "3000"

    # Type: string
    adguardhome_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='adguardhome') + '.' + lookup('role_var', '_web_domain', role='adguardhome')
                               if (lookup('role_var', '_web_subdomain', role='adguardhome') | length > 0)
                               else lookup('role_var', '_web_domain', role='adguardhome')) }}"

    ```

??? example "DNS"

    ```yaml
    # Type: string
    adguardhome_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='adguardhome') }}"

    # Type: string
    adguardhome_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='adguardhome') }}"

    # Type: bool (true/false)
    adguardhome_role_dns_proxy: "{{ dns_proxied }}"

    ```

??? example "Traefik"

    ```yaml
    # Type: string
    adguardhome_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

    # Type: string
    adguardhome_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

    # Type: string
    adguardhome_role_traefik_middleware_custom: ""

    # Type: string
    adguardhome_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

    # Type: bool (true/false)
    adguardhome_role_traefik_enabled: true

    # Type: bool (true/false)
    adguardhome_role_traefik_api_enabled: true

    # Type: string
    adguardhome_role_traefik_api_endpoint: "PathPrefix(`/dns-query`)"

    ```

??? example "Docker"

    ```yaml
    # Container
    # Type: string
    adguardhome_role_docker_container: "{{ adguardhome_name }}"

    # Image
    # Type: bool (true/false)
    adguardhome_role_docker_image_pull: true

    # Type: string
    adguardhome_role_docker_image_repo: "adguard/adguardhome"

    # Type: string
    adguardhome_role_docker_image_tag: "latest"

    # Type: string
    adguardhome_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='adguardhome') }}:{{ lookup('role_var', '_docker_image_tag', role='adguardhome') }}"

    # Envs
    # Type: dict
    adguardhome_role_docker_envs_default: 
      PUID: "{{ uid }}"
      PGID: "{{ gid }}"
      TZ: "{{ tz }}"

    # Type: dict
    adguardhome_role_docker_envs_custom: {}

    # Volumes
    # Type: list
    adguardhome_role_docker_volumes_default: 
      - "{{ lookup('role_var', '_paths_location', role='adguardhome') }}/work:/opt/adguardhome/work"
      - "{{ lookup('role_var', '_paths_location', role='adguardhome') }}/conf:/opt/adguardhome/conf"

    # Type: list
    adguardhome_role_docker_volumes_custom: []

    # Hostname
    # Type: string
    adguardhome_role_docker_hostname: "{{ adguardhome_name }}"

    # Networks
    # Type: string
    adguardhome_role_docker_networks_alias: "{{ adguardhome_name }}"

    # Type: list
    adguardhome_role_docker_networks_default: []

    # Type: list
    adguardhome_role_docker_networks_custom: []

    # Restart Policy
    # Type: string
    adguardhome_role_docker_restart_policy: unless-stopped

    # State
    # Type: string
    adguardhome_role_docker_state: started

    ```

??? example "Global Override Options"

    ```yaml
    # Enable or disable Autoheal monitoring for the container created when deploying
    # Type: bool (true/false)
    adguardhome_role_autoheal_enabled: true

    # List of container dependencies that must be running before the container start
    # Type: string
    adguardhome_role_depends_on: ""

    # Delay in seconds before starting the container after dependencies are ready
    # Type: string (quoted number)
    adguardhome_role_depends_on_delay: "0"

    # Enable healthcheck waiting for container dependencies
    # Type: string ("true"/"false")
    adguardhome_role_depends_on_healthchecks:

    # Enable or disable Diun update notifications for the container created when deploying
    # Type: bool (true/false)
    adguardhome_role_diun_enabled: true

    # Enable or disable automatic DNS record creation for the container
    # Type: bool (true/false)
    adguardhome_role_dns_enabled: true

    # Enable or disable Saltbox Docker Controller management for the container
    # Type: bool (true/false)
    adguardhome_role_docker_controller: true

    # Enable Traefik autodetect middleware for the container
    # Type: bool (true/false)
    adguardhome_role_traefik_autodetect_enabled: false

    # Enable CrowdSec middleware for the container
    # Type: bool (true/false)
    adguardhome_role_traefik_crowdsec_enabled: false

    # Enable custom error pages middleware for the container
    # Type: bool (true/false)
    adguardhome_role_traefik_error_pages_enabled: false

    # Enable gzip compression middleware for the container
    # Type: bool (true/false)
    adguardhome_role_traefik_gzip_enabled: false

    # Enable robots.txt middleware for the container
    # Type: bool (true/false)
    adguardhome_role_traefik_robot_enabled: true

    # Enable Tailscale-specific Traefik configuration for the container
    # Type: bool (true/false)
    adguardhome_role_traefik_tailscale_enabled: false

    # Enable wildcard certificate for the container
    # Type: bool (true/false)
    adguardhome_role_traefik_wildcard_enabled: true

    # Override the Traefik fully qualified domain name (FQDN) for the container
    # Type: list
    adguardhome_role_web_fqdn_override: # (1)!

    # Override the Traefik web host configuration for the container
    # Type: string
    adguardhome_role_web_host_override: # (2)!

    # URL scheme to use for web access to the container
    # Type: string ("http"/"https")
    adguardhome_role_web_scheme:

    ```

    1.  Example:

        ```yaml
        adguardhome_role_web_fqdn_override:
          - "{{ traefik_host }}"
          - "adguardhome2.{{ user.domain }}"
          - "adguardhome.otherdomain.tld"
        ```

        Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

    2.  Example:

        ```yaml
        adguardhome_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'adguardhome2.' + user.domain }}`)"
        ```

        Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

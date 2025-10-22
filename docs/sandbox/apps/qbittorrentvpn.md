---
hide:
  - tags
tags:
  - qbittorrentvpn
  - download
  - vpn
---

# qBittorrentvpn

## What is it?

[qbittorrentvpn](https://github.com/binhex/arch-qbittorrentvpn) is a qbittorrent container which includes OpenVPN and WireGuard to ensure a secure and private connection to the Internet, including use of iptables to prevent IP leakage when the tunnel is down. It also includes Privoxy to allow unfiltered access to index sites.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/binhex/arch-qbittorrentvpn){: .header-icons } | [:octicons-link-16: Docs](https://github.com/binhex/arch-qbittorrentvpn){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/binhex/arch-qbittorrentvpn){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/binhex/arch-qbittorrentvpn){: .header-icons }|

### 1. Installation

=== "PIA VPN"

    In `/opt/sandbox/settings.yml`, adjust the following:
    
    ```
    qbittorrentvpn:
      vpn_pass: your_vpn_password
      vpn_prov: pia
      vpn_user: your_vpn_username
      vpn_client: wireguard
    ```

    As described in the github readme linked above, then run the role:

    ``` shell

    sb install sandbox-qbittorrentvpn

    ```

=== "Proton VPN (Wireguard)"

    Step 01 - Please login in to [ProtonVPN-Account](https://account.protonvpn.com/account)
    Step 02 - Under "OpenVPN / IKEv2 username" section —> Copy this OpenVPN / IKEv2 username [Yeah, somehow this username is required for Wireguard]
    Step 03 - Go to [ProtonVPN-Downloads](https://account.protonvpn.com/downloads)
    Step 04 - Scroll down to "WireGuard configuration" - Please fill/select your desired settings for the configuration.
    Step 05 - Under "3. Select VPN options" —> Turn on "NAT-PMP (Port Forwarding)" —> Now download the config file and rename it to `wg0.conf`
    
    Now, In `/opt/sandbox/settings.yml`, adjust the following:
    
    ```
    qbittorrentvpn:
      vpn_pass: "protonvpn-account-password"
      vpn_prov: "protonvpn"
      vpn_user: "<OpenVPN / IKEv2 username>+pmp" #which we've copied from Step 02
      vpn_client: "wireguard"
    ```
    Example for reference
    ```
    qbittorrentvpn:
      vpn_pass: "xdfasdicmb"
      vpn_prov: "protonvpn"
      vpn_user: "zuqWGtyy7SMGQM8C+pmp"
      vpn_client: "wireguard"
    ```
    As described in the github readme linked above, then run the role:

    ``` shell

    sb install sandbox-qbittorrentvpn

    ```
    While the above command runs, go to this directory `/opt/qbittorrentvpn/wireguard` (Use FTP file manager like WinSCP)
    if you don't see this directory wait for few seconds, while the previous command creates this.

    Now copy & paste your `wg0.conf' file (Refer Step 05) in this directory & Wait for the command line to complete.
    If everything went well, you should see `Playbook /opt/sandbox/sandbox.yml executed successfully.`

### 2. URL

- To access qbittorrentvpn, visit `https://qbittorrentvpn.xDOMAIN_NAMEx`

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.


    This role supports multiple instances via `qbittorrentvpn_instances`.

    === "Role-level Override"

        Applies to all instances of qbittorrentvpn:

        ```yaml
        qbittorrentvpn_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `qbittorrentvpn2`):

        ```yaml
        qbittorrentvpn2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `qbittorrentvpn_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `qbittorrentvpn_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        qbittorrentvpn_instances: ["qbittorrentvpn"]

        ```

    === "Example"

        ```yaml
        # Type: list
        qbittorrentvpn_instances: ["qbittorrentvpn", "qbittorrentvpn2"]

        ```

??? example "Settings"

    === "Role-level"

        ```yaml
        # Type: string
        qbittorrentvpn_log_level_daemon: info

        # Type: string
        qbittorrentvpn_log_level_web: info

        # Type: string
        qbittorrentvpn_name_servers: "84.200.69.80,1.1.1.1,84.200.70.40,1.0.0.1"

        # Type: string
        qbittorrentvpn_lan_network: "172.19.0.0/16"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        qbittorrentvpn_log_level_daemon: info

        # Type: string
        qbittorrentvpn_log_level_web: info

        # Type: string
        qbittorrentvpn_name_servers: "84.200.69.80,1.1.1.1,84.200.70.40,1.0.0.1"

        # Type: string
        qbittorrentvpn_lan_network: "172.19.0.0/16"

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        qbittorrentvpn_role_paths_folder: "{{ qbittorrentvpn_name }}"

        # Type: string
        qbittorrentvpn_role_paths_location: "{{ server_appdata_path }}/{{ qbittorrentvpn_role_paths_folder }}"

        # Type: string
        qbittorrentvpn_role_paths_downloads_location: "{{ downloads_torrents_path }}/{{ qbittorrentvpn_role_paths_folder }}"

        # Type: string
        qbittorrentvpn_role_paths_conf: "{{ qbittorrentvpn_role_paths_location }}/qBittorrent/config/qBittorrent.conf"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        qbittorrentvpn2_paths_folder: "{{ qbittorrentvpn_name }}"

        # Type: string
        qbittorrentvpn2_paths_location: "{{ server_appdata_path }}/{{ qbittorrentvpn_role_paths_folder }}"

        # Type: string
        qbittorrentvpn2_paths_downloads_location: "{{ downloads_torrents_path }}/{{ qbittorrentvpn_role_paths_folder }}"

        # Type: string
        qbittorrentvpn2_paths_conf: "{{ qbittorrentvpn_role_paths_location }}/qBittorrent/config/qBittorrent.conf"

        ```

??? example "Web"

    === "Role-level"

        ```yaml
        # Type: string
        qbittorrentvpn_role_web_subdomain: "{{ qbittorrentvpn_name }}"

        # Type: string
        qbittorrentvpn_role_web_domain: "{{ user.domain }}"

        # Type: string
        qbittorrentvpn_role_web_port: "8080"

        # Type: string
        qbittorrentvpn_role_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='qbittorrentvpn') + '.' + lookup('role_var', '_web_domain', role='qbittorrentvpn')
                                      if (lookup('role_var', '_web_subdomain', role='qbittorrentvpn') | length > 0)
                                      else lookup('role_var', '_web_domain', role='qbittorrentvpn')) }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        qbittorrentvpn2_web_subdomain: "{{ qbittorrentvpn_name }}"

        # Type: string
        qbittorrentvpn2_web_domain: "{{ user.domain }}"

        # Type: string
        qbittorrentvpn2_web_port: "8080"

        # Type: string
        qbittorrentvpn2_web_url: "{{ 'https://' + (lookup('role_var', '_web_subdomain', role='qbittorrentvpn') + '.' + lookup('role_var', '_web_domain', role='qbittorrentvpn')
                                  if (lookup('role_var', '_web_subdomain', role='qbittorrentvpn') | length > 0)
                                  else lookup('role_var', '_web_domain', role='qbittorrentvpn')) }}"

        ```

??? example "DNS"

    === "Role-level"

        ```yaml
        # Type: string
        qbittorrentvpn_role_dns_record: "{{ lookup('role_var', '_web_subdomain', role='qbittorrentvpn') }}"

        # Type: string
        qbittorrentvpn_role_dns_zone: "{{ lookup('role_var', '_web_domain', role='qbittorrentvpn') }}"

        # Type: bool (true/false)
        qbittorrentvpn_role_dns_proxy: "{{ dns_proxied }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        qbittorrentvpn2_dns_record: "{{ lookup('role_var', '_web_subdomain', role='qbittorrentvpn') }}"

        # Type: string
        qbittorrentvpn2_dns_zone: "{{ lookup('role_var', '_web_domain', role='qbittorrentvpn') }}"

        # Type: bool (true/false)
        qbittorrentvpn2_dns_proxy: "{{ dns_proxied }}"

        ```

??? example "Traefik"

    === "Role-level"

        ```yaml
        # Type: string
        qbittorrentvpn_role_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        qbittorrentvpn_role_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        qbittorrentvpn_role_traefik_middleware_custom: ""

        # Type: string
        qbittorrentvpn_role_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_enabled: true

        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_api_enabled: true

        # Type: string
        qbittorrentvpn_role_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/command`) || PathPrefix(`/query`) || PathPrefix(`/login`) || PathPrefix(`/sync`)"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        qbittorrentvpn2_traefik_sso_middleware: "{{ traefik_default_sso_middleware }}"

        # Type: string
        qbittorrentvpn2_traefik_middleware_default: "{{ traefik_default_middleware }}"

        # Type: string
        qbittorrentvpn2_traefik_middleware_custom: ""

        # Type: string
        qbittorrentvpn2_traefik_certresolver: "{{ traefik_default_certresolver }}"

        # Type: bool (true/false)
        qbittorrentvpn2_traefik_enabled: true

        # Type: bool (true/false)
        qbittorrentvpn2_traefik_api_enabled: true

        # Type: string
        qbittorrentvpn2_traefik_api_endpoint: "PathPrefix(`/api`) || PathPrefix(`/command`) || PathPrefix(`/query`) || PathPrefix(`/login`) || PathPrefix(`/sync`)"

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        qbittorrentvpn_role_docker_container: "{{ qbittorrentvpn_name }}"

        # Image
        # Type: bool (true/false)
        qbittorrentvpn_role_docker_image_pull: true

        # Type: string
        qbittorrentvpn_role_docker_image_repo: "binhex/arch-qbittorrentvpn"

        # Type: string
        qbittorrentvpn_role_docker_image_tag: "latest"

        # Type: string
        qbittorrentvpn_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='qbittorrentvpn') }}:{{ lookup('role_var', '_docker_image_tag', role='qbittorrentvpn') }}"

        # Envs
        # Type: dict
        qbittorrentvpn_role_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          UMASK_SET: "002"
          VPN_ENABLED: "yes"
          VPN_USER: "{{ qbittorrentvpn.vpn_user | default('username', true) }}"
          VPN_PASS: "{{ qbittorrentvpn.vpn_pass | default('password', true) }}"
          VPN_PROV: "{{ qbittorrentvpn.vpn_prov | default('pia', true) }}"
          VPN_CLIENT: "{{ qbittorrentvpn.vpn_client | default('wireguard', true) }}"
          STRICT_PORT_FORWARD: "yes"
          ENABLE_PRIVOXY: "no"
          LAN_NETWORK: "{{ qbittorrentvpn_lan_network }}"
          NAME_SERVERS: "{{ qbittorrentvpn_name_servers }}"

        # Type: dict
        qbittorrentvpn_role_docker_envs_custom: {}

        # Volumes
        # Type: list
        qbittorrentvpn_role_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='qbittorrentvpn') }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"

        # Type: list
        qbittorrentvpn_role_docker_volumes_custom: []

        # Hostname
        # Type: string
        qbittorrentvpn_role_docker_hostname: "{{ qbittorrentvpn_name }}"

        # Networks
        # Type: string
        qbittorrentvpn_role_docker_networks_alias: "{{ qbittorrentvpn_name }}"

        # Type: list
        qbittorrentvpn_role_docker_networks_default: []

        # Type: list
        qbittorrentvpn_role_docker_networks_custom: []

        # Capabilities
        # Type: list
        qbittorrentvpn_role_docker_capabilities_default: 
          - NET_ADMIN

        # Type: list
        qbittorrentvpn_role_docker_capabilities_custom: []

        # Sysctls
        # Type: dict
        qbittorrentvpn_role_docker_sysctls: 
          net.ipv4.conf.all.src_valid_mark: "1"

        # Restart Policy
        # Type: string
        qbittorrentvpn_role_docker_restart_policy: unless-stopped

        # Stop Timeout
        # Type: int
        qbittorrentvpn_role_docker_stop_timeout: 900

        # State
        # Type: string
        qbittorrentvpn_role_docker_state: started

        # Privileged
        # Type: bool (true/false)
        qbittorrentvpn_role_docker_privileged: true

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        qbittorrentvpn2_docker_container: "{{ qbittorrentvpn_name }}"

        # Image
        # Type: bool (true/false)
        qbittorrentvpn2_docker_image_pull: true

        # Type: string
        qbittorrentvpn2_docker_image_repo: "binhex/arch-qbittorrentvpn"

        # Type: string
        qbittorrentvpn2_docker_image_tag: "latest"

        # Type: string
        qbittorrentvpn2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='qbittorrentvpn') }}:{{ lookup('role_var', '_docker_image_tag', role='qbittorrentvpn') }}"

        # Envs
        # Type: dict
        qbittorrentvpn2_docker_envs_default: 
          PUID: "{{ uid }}"
          PGID: "{{ gid }}"
          TZ: "{{ tz }}"
          UMASK_SET: "002"
          VPN_ENABLED: "yes"
          VPN_USER: "{{ qbittorrentvpn.vpn_user | default('username', true) }}"
          VPN_PASS: "{{ qbittorrentvpn.vpn_pass | default('password', true) }}"
          VPN_PROV: "{{ qbittorrentvpn.vpn_prov | default('pia', true) }}"
          VPN_CLIENT: "{{ qbittorrentvpn.vpn_client | default('wireguard', true) }}"
          STRICT_PORT_FORWARD: "yes"
          ENABLE_PRIVOXY: "no"
          LAN_NETWORK: "{{ qbittorrentvpn_lan_network }}"
          NAME_SERVERS: "{{ qbittorrentvpn_name_servers }}"

        # Type: dict
        qbittorrentvpn2_docker_envs_custom: {}

        # Volumes
        # Type: list
        qbittorrentvpn2_docker_volumes_default: 
          - "{{ lookup('role_var', '_paths_location', role='qbittorrentvpn') }}:/config"
          - "{{ server_appdata_path }}/scripts:/scripts"

        # Type: list
        qbittorrentvpn2_docker_volumes_custom: []

        # Hostname
        # Type: string
        qbittorrentvpn2_docker_hostname: "{{ qbittorrentvpn_name }}"

        # Networks
        # Type: string
        qbittorrentvpn2_docker_networks_alias: "{{ qbittorrentvpn_name }}"

        # Type: list
        qbittorrentvpn2_docker_networks_default: []

        # Type: list
        qbittorrentvpn2_docker_networks_custom: []

        # Capabilities
        # Type: list
        qbittorrentvpn2_docker_capabilities_default: 
          - NET_ADMIN

        # Type: list
        qbittorrentvpn2_docker_capabilities_custom: []

        # Sysctls
        # Type: dict
        qbittorrentvpn2_docker_sysctls: 
          net.ipv4.conf.all.src_valid_mark: "1"

        # Restart Policy
        # Type: string
        qbittorrentvpn2_docker_restart_policy: unless-stopped

        # Stop Timeout
        # Type: int
        qbittorrentvpn2_docker_stop_timeout: 900

        # State
        # Type: string
        qbittorrentvpn2_docker_state: started

        # Privileged
        # Type: bool (true/false)
        qbittorrentvpn2_docker_privileged: true


        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        qbittorrentvpn_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        qbittorrentvpn_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        qbittorrentvpn_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        qbittorrentvpn_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        qbittorrentvpn_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        qbittorrentvpn_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        qbittorrentvpn_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        qbittorrentvpn_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        qbittorrentvpn_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        qbittorrentvpn_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        qbittorrentvpn_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            qbittorrentvpn_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "qbittorrentvpn2.{{ user.domain }}"
              - "qbittorrentvpn.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            qbittorrentvpn_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'qbittorrentvpn2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

    === "Instance-level"

        Override for a specific instance (e.g., `qbittorrentvpn2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        qbittorrentvpn2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        qbittorrentvpn2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        qbittorrentvpn2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        qbittorrentvpn2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        qbittorrentvpn2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        qbittorrentvpn2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        qbittorrentvpn2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        qbittorrentvpn2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        qbittorrentvpn2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        qbittorrentvpn2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        qbittorrentvpn2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        qbittorrentvpn2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        qbittorrentvpn2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        qbittorrentvpn2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        qbittorrentvpn2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        qbittorrentvpn2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        qbittorrentvpn2_web_scheme:

        ```

        1.  Example:

            ```yaml
            qbittorrentvpn2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "qbittorrentvpn2.{{ user.domain }}"
              - "qbittorrentvpn.otherdomain.tld"
            ```

            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        2.  Example:

            ```yaml
            qbittorrentvpn2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'qbittorrentvpn2.' + user.domain }}`)"
            ```

            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

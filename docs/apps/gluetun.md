---
hide:
  - tags
tags:
  - gluetun
---

# Gluetun

## What is it?

[Gluetun](https://github.com/qdm12/gluetun) is a VPN client in a thin Docker container for multiple VPN providers, written in Go, and using OpenVPN or Wireguard, DNS over TLS, with a few proxy servers built-in.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/qdm12/gluetun){: .header-icons } | [:octicons-link-16: Docs](https://github.com/qdm12/gluetun-wiki){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/qdm12/gluetun){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/qmcgaw/gluetun){: .header-icons }|

### 1. Configuration

The Gluetun role is configured via the [inventory system](../saltbox/inventory/index.md). It is recommended to review the upstream documentation for your VPN provider to determine the proper configuration. The following variables are available to set and correspond to the similarly named Docker envs.

```yaml
gluetun_vpn_service_provider: ""
gluetun_vpn_type: ""
gluetun_openvpn_custom_config: ""
gluetun_openvpn_endpoint_ip: ""
gluetun_openvpn_endpoint_port: ""
gluetun_openvpn_user: ""
gluetun_openvpn_password: ""
gluetun_openvpn_key_passphrase: ""
gluetun_wireguard_endpoint_ip: ""
gluetun_wireguard_endpoint_port: ""
gluetun_wireguard_public_key: ""
gluetun_wireguard_private_key: ""
gluetun_wireguard_preshared_key: ""
gluetun_wireguard_addresses: ""
gluetun_wireguard_mtu: ""
gluetun_server_countries: ""
gluetun_server_cities: ""
gluetun_server_hostnames: ""
gluetun_server_names: ""
gluetun_server_regions: ""
gluetun_firewall_vpn_input_ports: ""
gluetun_firewall_input_ports: ""
gluetun_firewall_outbound_subnets: ""
```

!!! caution
    Any values which are entirely numeric or contain special characters should be wrapped in quotes:
    
    ```yaml
    gluetun_openvpn_user: "ePWh!Y^fs6p%B*6S"
    gluetun_openvpn_password: "qA5V6&#ASx4DY8qG"
    gluetun_openvpn_endpoint_port: "12345"
    ```
    
    Generally speaking it's safest to just wrap everything in quotes rather than worrying about what needs to be.  Quotes are plentiful and free.


!!! warning
    The role uses the built-in Docker DNS resolver by default instead of using the DoH/DoT functionality Gluetun normally provides.

    If DNS leaks are a problem for your use case you will want to override this behavior with:
    ```yaml
    gluetun_docker_resolver: false
    ```

    Just be aware that this toggle will make any network linked containers unable to resolve docker hostnames.
  

Additional Docker envs may be set via `gluetun_docker_envs_custom`.

### 2. Installation

``` shell
sb install gluetun
```

### 3. Route Plex through Gluetun

!!! caution
    It is important to disable remote access in Plex when using this workaround to avoid having media traffic routed through the VPN. Multiple instances of Plex will need their own unique instance of gluetun due to port conflicts.

To route Plex via your Gluetun container, you must set the following via the inventory system. These settings will also DNS block the metrics servers and use Gluetun's HTTP proxy when connecting with the Plex API for Saltbox tasks such as generating auth tokens:

``` yaml
gluetun_docker_hosts_default:
  "metric.plex.tv": "{{ ip_address_localhost }}"
  "metrics.plex.tv": "{{ ip_address_localhost }}"
  "analytics.plex.tv": "{{ ip_address_localhost }}"

gluetun_docker_networks_alias_custom:
  - "plex"

plex_auth_token_proxy: "http://gluetun:8888"
plex_docker_network_mode_default: "container:gluetun"

# If using multiple instances.
gluetun2_docker_networks_alias_custom:
  - "plex2"
plex2_docker_network_mode_default: "container:gluetun2"
plex2_auth_token_proxy: "http://gluetun2:8888"
```

Once you have made these changes to the inventory, run the plex tag to apply the changes [i.e. `sb install plex`].  This will update all your plex containers.

!!! caution
    When routing Plex through Gluetun, you must access Plex between containers at `http://gluetun:32400` where you would previously use the Plex container name.

    The above note is only the case if you do not add each linked container alias to gluetun like in the config example above.

    Additionally the Plex container will become unable to start if you redeploy gluetun (restart is fine) at any point so you must redeploy Plex in that case.

### 4. Route other containers through Gluetun

Depending on if the role in question supports instances or not there will be two ways to set the network mode.

=== "With instances"

    To route a Saltbox-configured container through Gluetun, you must set `<rolename_instance>_docker_network_mode_default: "container:gluetun"` via the inventory system.
    
    For example, to route `qbittorrent` through Gluetun, the entry would be `qbittorrent_docker_network_mode_default: "container:gluetun"`.

    For example, to route `qbittorrent2` through Gluetun, the entry would be `qbittorrent2_docker_network_mode_default: "container:gluetun2"`.

    !!! important
        The caveat with instances is that each instance will need a unique Gluetun instance to avoid port collision.

=== "Without instances"

    To route a Saltbox-configured container through Gluetun, you must set `<rolename>_docker_network_mode: "container:gluetun"` via the inventory system.
    
    For example, to route `jackett` through Gluetun, the entry would be `jackett_docker_network_mode: "container:gluetun"`.

Once you have made these changes to the inventory, run the relevant tags to apply the changes [i.e. `sb install qbittorrent` or `sb install jackett,sonarr,radarr`].

!!! caution
    While multiple containers may be routed through a single Gluetun instance, you must manually ensure there are no port clashes as all port binds for the connected containers will be through the Gluetun container and must have unique ports inside that container.

### 5. Example Gluetun Configs

Below are some example inventory entries for some common VPN providers. These are intended as templates only and should not be expected to copy and paste without any edits. For a Wireguard implementation, you will typically generate a config file (wg0.conf) with the provider and grab some of the values from that config to configure Gluetun.

=== "Custom Wireguard provider"

    ```yaml
    gluetun_vpn_service_provider: "custom"
    gluetun_vpn_type: "wireguard"
    gluetun_wireguard_private_key: "your_wireguard_private_key"
    gluetun_wireguard_addresses: "your_wireguard_address_with_cidr"
    gluetun_wireguard_public_key: "server_wireguard_public_key"
    gluetun_wireguard_endpoint_ip: "wireguard_server_ip"
    gluetun_wireguard_endpoint_port: "wireguard_server_port"
    # Not always required (only if server is configured to use a pre-shared key)
    gluetun_wireguard_preshared_key: "your_wireguard_preshared_key"
    ```

=== "Proton VPN Free"

    ```yaml
    gluetun_vpn_service_provider: "protonvpn"
    gluetun_openvpn_user: "your_openvpn_user"
    gluetun_openvpn_password: "your_openvpn_password"
    gluetun_docker_envs_custom:
      FREE_ONLY: "on"
    ```

=== "Mullvad"

    ```yaml
    gluetun_vpn_service_provider: "mullvad"
    gluetun_vpn_type: "wireguard"
    gluetun_wireguard_public_key: "your_wireguard_public_key"
    gluetun_wireguard_private_key: "your_wireguard_private_key"
    gluetun_wireguard_addresses: "your_wireguard_address"
    # Include the below line to only connect to Amsterdam servers - replace with a different city if desired
    gluetun_server_cities: "amsterdam"
    ```

=== "Surfshark"

    ```yaml
    gluetun_vpn_service_provider: "surfshark"
    gluetun_vpn_type: "wireguard"
    gluetun_wireguard_private_key: "your_wireguard_private_key"
    gluetun_wireguard_addresses: "your_wireguard_address"
    # Include the below line to only connect to Netherlands servers - replace with a different city if desired
    gluetun_server_countries: "Netherlands"
    ```

=== "AirVPN"

    ```yaml
    gluetun_vpn_service_provider: "airvpn"
    gluetun_vpn_type: "wireguard"
    gluetun_wireguard_public_key: "your_wireguard_public_key"
    gluetun_wireguard_private_key: "your_wireguard_private_key"
    gluetun_wireguard_preshared_key: "your_wireguard_preshared_key"
    gluetun_wireguard_addresses: "your_wireguard_address"
    ```

=== "Custom .ovpn file"

    ```yaml
    # Configure via a ovpn file located on the host at `/opt/gluetun/custom.ovpn`.
    gluetun_vpn_service_provider: "custom"
    gluetun_vpn_type: "openvpn"
    gluetun_openvpn_custom_config: "/gluetun/custom.ovpn"
    ```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
## Role Defaults

!!! info
    Variables can be overridden in `/srv/git/saltbox/inventories/host_vars/localhost.yml`.

    This role supports multiple instances via `gluetun_instances`.

    === "Role-level Override"

        Applies to all instances of gluetun:

        ```yaml
        gluetun_role_web_subdomain: "custom"
        ```

    === "Instance-level Override"

        Applies to a specific instance (e.g., `gluetun2`):

        ```yaml
        gluetun2_web_subdomain: "custom2"
        ```

!!! warning
    **Avoid overriding variables ending in `_default`**

    When overriding variables that end in `_default` (like `gluetun_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `gluetun_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`gluetun_instances`"

        ```yaml
        # Type: list
        gluetun_instances: ["gluetun"]
        ```

        !!! example

            ```yaml
            # Type: list
            gluetun_instances: ["gluetun", "gluetun2"]
            ```

=== "Settings"

    === "Role-level"

        ??? variable string "`gluetun_role_vpn_service_provider`"

            ```yaml
            # These variables map to the appropriate Docker ENVs
            # Review the gluetun wiki (https://github.com/qdm12/gluetun/wiki)
            # Type: string
            gluetun_role_vpn_service_provider: ""
            ```

        ??? variable string "`gluetun_role_vpn_type`"

            ```yaml
            # Type: string
            gluetun_role_vpn_type: ""
            ```

        ??? variable string "`gluetun_role_openvpn_custom_config`"

            ```yaml
            # Type: string
            gluetun_role_openvpn_custom_config: ""
            ```

        ??? variable string "`gluetun_role_openvpn_endpoint_ip`"

            ```yaml
            # Type: string
            gluetun_role_openvpn_endpoint_ip: ""
            ```

        ??? variable string "`gluetun_role_openvpn_endpoint_port`"

            ```yaml
            # Type: string
            gluetun_role_openvpn_endpoint_port: ""
            ```

        ??? variable string "`gluetun_role_openvpn_user`"

            ```yaml
            # Type: string
            gluetun_role_openvpn_user: ""
            ```

        ??? variable string "`gluetun_role_openvpn_password`"

            ```yaml
            # Type: string
            gluetun_role_openvpn_password: ""
            ```

        ??? variable string "`gluetun_role_openvpn_key_passphrase`"

            ```yaml
            # Type: string
            gluetun_role_openvpn_key_passphrase: ""
            ```

        ??? variable string "`gluetun_role_vpn_endpoint_ip`"

            ```yaml
            # Type: string
            gluetun_role_vpn_endpoint_ip: ""
            ```

        ??? variable string "`gluetun_role_vpn_endpoint_port`"

            ```yaml
            # Type: string
            gluetun_role_vpn_endpoint_port: ""
            ```

        ??? variable string "`gluetun_role_wireguard_endpoint_ip`"

            ```yaml
            # Type: string
            gluetun_role_wireguard_endpoint_ip: ""
            ```

        ??? variable string "`gluetun_role_wireguard_endpoint_port`"

            ```yaml
            # Type: string
            gluetun_role_wireguard_endpoint_port: ""
            ```

        ??? variable string "`gluetun_role_wireguard_mtu`"

            ```yaml
            # Type: string
            gluetun_role_wireguard_mtu: ""
            ```

        ??? variable string "`gluetun_role_wireguard_public_key`"

            ```yaml
            # Type: string
            gluetun_role_wireguard_public_key: ""
            ```

        ??? variable string "`gluetun_role_wireguard_private_key`"

            ```yaml
            # Type: string
            gluetun_role_wireguard_private_key: ""
            ```

        ??? variable string "`gluetun_role_wireguard_preshared_key`"

            ```yaml
            # Type: string
            gluetun_role_wireguard_preshared_key: ""
            ```

        ??? variable string "`gluetun_role_wireguard_addresses`"

            ```yaml
            # Type: string
            gluetun_role_wireguard_addresses: ""
            ```

        ??? variable string "`gluetun_role_server_countries`"

            ```yaml
            # Type: string
            gluetun_role_server_countries: ""
            ```

        ??? variable string "`gluetun_role_server_cities`"

            ```yaml
            # Type: string
            gluetun_role_server_cities: ""
            ```

        ??? variable string "`gluetun_role_server_hostnames`"

            ```yaml
            # Type: string
            gluetun_role_server_hostnames: ""
            ```

        ??? variable string "`gluetun_role_server_names`"

            ```yaml
            # Type: string
            gluetun_role_server_names: ""
            ```

        ??? variable string "`gluetun_role_server_regions`"

            ```yaml
            # Type: string
            gluetun_role_server_regions: ""
            ```

        ??? variable string "`gluetun_role_firewall_vpn_input_ports`"

            ```yaml
            # Type: string
            gluetun_role_firewall_vpn_input_ports: ""
            ```

        ??? variable string "`gluetun_role_firewall_input_ports`"

            ```yaml
            # Type: string
            gluetun_role_firewall_input_ports: ""
            ```

        ??? variable string "`gluetun_role_firewall_outbound_subnets`"

            ```yaml
            # Type: string
            gluetun_role_firewall_outbound_subnets: ""
            ```

        ??? variable bool "`gluetun_role_docker_resolver`"

            ```yaml
            # Type: bool (true/false)
            gluetun_role_docker_resolver: true
            ```

    === "Instance-level"

        ??? variable string "`gluetun2_vpn_service_provider`"

            ```yaml
            # These variables map to the appropriate Docker ENVs
            # Review the gluetun wiki (https://github.com/qdm12/gluetun/wiki)
            # Type: string
            gluetun2_vpn_service_provider: ""
            ```

        ??? variable string "`gluetun2_vpn_type`"

            ```yaml
            # Type: string
            gluetun2_vpn_type: ""
            ```

        ??? variable string "`gluetun2_openvpn_custom_config`"

            ```yaml
            # Type: string
            gluetun2_openvpn_custom_config: ""
            ```

        ??? variable string "`gluetun2_openvpn_endpoint_ip`"

            ```yaml
            # Type: string
            gluetun2_openvpn_endpoint_ip: ""
            ```

        ??? variable string "`gluetun2_openvpn_endpoint_port`"

            ```yaml
            # Type: string
            gluetun2_openvpn_endpoint_port: ""
            ```

        ??? variable string "`gluetun2_openvpn_user`"

            ```yaml
            # Type: string
            gluetun2_openvpn_user: ""
            ```

        ??? variable string "`gluetun2_openvpn_password`"

            ```yaml
            # Type: string
            gluetun2_openvpn_password: ""
            ```

        ??? variable string "`gluetun2_openvpn_key_passphrase`"

            ```yaml
            # Type: string
            gluetun2_openvpn_key_passphrase: ""
            ```

        ??? variable string "`gluetun2_vpn_endpoint_ip`"

            ```yaml
            # Type: string
            gluetun2_vpn_endpoint_ip: ""
            ```

        ??? variable string "`gluetun2_vpn_endpoint_port`"

            ```yaml
            # Type: string
            gluetun2_vpn_endpoint_port: ""
            ```

        ??? variable string "`gluetun2_wireguard_endpoint_ip`"

            ```yaml
            # Type: string
            gluetun2_wireguard_endpoint_ip: ""
            ```

        ??? variable string "`gluetun2_wireguard_endpoint_port`"

            ```yaml
            # Type: string
            gluetun2_wireguard_endpoint_port: ""
            ```

        ??? variable string "`gluetun2_wireguard_mtu`"

            ```yaml
            # Type: string
            gluetun2_wireguard_mtu: ""
            ```

        ??? variable string "`gluetun2_wireguard_public_key`"

            ```yaml
            # Type: string
            gluetun2_wireguard_public_key: ""
            ```

        ??? variable string "`gluetun2_wireguard_private_key`"

            ```yaml
            # Type: string
            gluetun2_wireguard_private_key: ""
            ```

        ??? variable string "`gluetun2_wireguard_preshared_key`"

            ```yaml
            # Type: string
            gluetun2_wireguard_preshared_key: ""
            ```

        ??? variable string "`gluetun2_wireguard_addresses`"

            ```yaml
            # Type: string
            gluetun2_wireguard_addresses: ""
            ```

        ??? variable string "`gluetun2_server_countries`"

            ```yaml
            # Type: string
            gluetun2_server_countries: ""
            ```

        ??? variable string "`gluetun2_server_cities`"

            ```yaml
            # Type: string
            gluetun2_server_cities: ""
            ```

        ??? variable string "`gluetun2_server_hostnames`"

            ```yaml
            # Type: string
            gluetun2_server_hostnames: ""
            ```

        ??? variable string "`gluetun2_server_names`"

            ```yaml
            # Type: string
            gluetun2_server_names: ""
            ```

        ??? variable string "`gluetun2_server_regions`"

            ```yaml
            # Type: string
            gluetun2_server_regions: ""
            ```

        ??? variable string "`gluetun2_firewall_vpn_input_ports`"

            ```yaml
            # Type: string
            gluetun2_firewall_vpn_input_ports: ""
            ```

        ??? variable string "`gluetun2_firewall_input_ports`"

            ```yaml
            # Type: string
            gluetun2_firewall_input_ports: ""
            ```

        ??? variable string "`gluetun2_firewall_outbound_subnets`"

            ```yaml
            # Type: string
            gluetun2_firewall_outbound_subnets: ""
            ```

        ??? variable bool "`gluetun2_docker_resolver`"

            ```yaml
            # Type: bool (true/false)
            gluetun2_docker_resolver: true
            ```

=== "Paths"

    === "Role-level"

        ??? variable string "`gluetun_role_paths_folder`"

            ```yaml
            # Type: string
            gluetun_role_paths_folder: "{{ gluetun_name }}"
            ```

        ??? variable string "`gluetun_role_paths_location`"

            ```yaml
            # Type: string
            gluetun_role_paths_location: "{{ server_appdata_path }}/{{ gluetun_role_paths_folder }}"
            ```

    === "Instance-level"

        ??? variable string "`gluetun2_paths_folder`"

            ```yaml
            # Type: string
            gluetun2_paths_folder: "{{ gluetun_name }}"
            ```

        ??? variable string "`gluetun2_paths_location`"

            ```yaml
            # Type: string
            gluetun2_paths_location: "{{ server_appdata_path }}/{{ gluetun_role_paths_folder }}"
            ```

=== "Docker"

    === "Role-level"

        ##### Container

        ??? variable string "`gluetun_role_docker_container`"

            ```yaml
            # Type: string
            gluetun_role_docker_container: "{{ gluetun_name }}"
            ```

        ##### Image

        ??? variable bool "`gluetun_role_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            gluetun_role_docker_image_pull: true
            ```

        ??? variable string "`gluetun_role_docker_image_repo`"

            ```yaml
            # Type: string
            gluetun_role_docker_image_repo: "qmcgaw/gluetun"
            ```

        ??? variable string "`gluetun_role_docker_image_tag`"

            ```yaml
            # Type: string
            gluetun_role_docker_image_tag: "v3"
            ```

        ??? variable string "`gluetun_role_docker_image`"

            ```yaml
            # Type: string
            gluetun_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='gluetun') }}:{{ lookup('role_var', '_docker_image_tag', role='gluetun') }}"
            ```

        ##### Envs

        ??? variable dict "`gluetun_role_docker_envs_default`"

            ```yaml
            # Type: dict
            gluetun_role_docker_envs_default: 
              DNS_KEEP_NAMESERVER: "{{ 'on' if lookup('role_var', '_docker_resolver', role='gluetun') else 'off' }}"
              FIREWALL_INPUT_PORTS: "{{ lookup('role_var', '_firewall_input_ports', role='gluetun') if (lookup('role_var', '_firewall_input_ports', role='gluetun') | length > 0) else omit }}"
              FIREWALL_OUTBOUND_SUBNETS: "{{ lookup('role_var', '_firewall_outbound_subnets', role='gluetun') if (lookup('role_var', '_firewall_outbound_subnets', role='gluetun') | length > 0) else omit }}"
              FIREWALL_VPN_INPUT_PORTS: "{{ lookup('role_var', '_firewall_vpn_input_ports', role='gluetun') if (lookup('role_var', '_firewall_vpn_input_ports', role='gluetun') | length > 0) else omit }}"
              HTTPPROXY: "on"
              HTTPPROXY_STEALTH: "on"
              OPENVPN_CUSTOM_CONFIG: "{{ lookup('role_var', '_openvpn_custom_config', role='gluetun') if (lookup('role_var', '_openvpn_custom_config', role='gluetun') | length > 0) else omit }}"
              OPENVPN_ENDPOINT_IP: "{{ lookup('role_var', '_openvpn_endpoint_ip', role='gluetun') if (lookup('role_var', '_openvpn_endpoint_ip', role='gluetun') | length > 0) else omit }}"
              OPENVPN_ENDPOINT_PORT: "{{ lookup('role_var', '_openvpn_endpoint_port', role='gluetun') if (lookup('role_var', '_openvpn_endpoint_port', role='gluetun') | length > 0) else omit }}"
              OPENVPN_KEY_PASSPHRASE: "{{ lookup('role_var', '_openvpn_key_passphrase', role='gluetun') if (lookup('role_var', '_openvpn_key_passphrase', role='gluetun') | length > 0) else omit }}"
              OPENVPN_PASSWORD: "{{ lookup('role_var', '_openvpn_password', role='gluetun') if (lookup('role_var', '_openvpn_password', role='gluetun') | length > 0) else omit }}"
              OPENVPN_USER: "{{ lookup('role_var', '_openvpn_user', role='gluetun') if (lookup('role_var', '_openvpn_user', role='gluetun') | length > 0) else omit }}"
              PGID: "{{ gid }}"
              PUID: "{{ uid }}"
              SERVER_CITIES: "{{ lookup('role_var', '_server_cities', role='gluetun') if (lookup('role_var', '_server_cities', role='gluetun') | length > 0) else omit }}"
              SERVER_COUNTRIES: "{{ lookup('role_var', '_server_countries', role='gluetun') if (lookup('role_var', '_server_countries', role='gluetun') | length > 0) else omit }}"
              SERVER_HOSTNAMES: "{{ lookup('role_var', '_server_hostnames', role='gluetun') if (lookup('role_var', '_server_hostnames', role='gluetun') | length > 0) else omit }}"
              SERVER_NAMES: "{{ lookup('role_var', '_server_names', role='gluetun') if (lookup('role_var', '_server_names', role='gluetun') | length > 0) else omit }}"
              SERVER_REGIONS: "{{ lookup('role_var', '_server_regions', role='gluetun') if (lookup('role_var', '_server_regions', role='gluetun') | length > 0) else omit }}"
              TZ: "{{ tz }}"
              VPN_ENDPOINT_IP: "{{ lookup('role_var', '_vpn_endpoint_ip', role='gluetun') if (lookup('role_var', '_vpn_endpoint_ip', role='gluetun') | length > 0) else omit }}"
              VPN_ENDPOINT_PORT: "{{ lookup('role_var', '_vpn_endpoint_port', role='gluetun') if (lookup('role_var', '_vpn_endpoint_port', role='gluetun') | length > 0) else omit }}"
              VPN_SERVICE_PROVIDER: "{{ lookup('role_var', '_vpn_service_provider', role='gluetun') if (lookup('role_var', '_vpn_service_provider', role='gluetun') | length > 0) else omit }}"
              VPN_TYPE: "{{ lookup('role_var', '_vpn_type', role='gluetun') if (lookup('role_var', '_vpn_type', role='gluetun') | length > 0) else omit }}"
              WIREGUARD_ADDRESSES: "{{ lookup('role_var', '_wireguard_addresses', role='gluetun') if (lookup('role_var', '_wireguard_addresses', role='gluetun') | length > 0) else omit }}"
              WIREGUARD_ENDPOINT_IP: "{{ lookup('role_var', '_wireguard_endpoint_ip', role='gluetun') if (lookup('role_var', '_wireguard_endpoint_ip', role='gluetun') | length > 0) else omit }}"
              WIREGUARD_ENDPOINT_PORT: "{{ lookup('role_var', '_wireguard_endpoint_port', role='gluetun') if (lookup('role_var', '_wireguard_endpoint_port', role='gluetun') | length > 0) else omit }}"
              WIREGUARD_MTU: "{{ lookup('role_var', '_wireguard_mtu', role='gluetun') if (lookup('role_var', '_wireguard_mtu', role='gluetun') | length > 0) else omit }}"
              WIREGUARD_PRESHARED_KEY: "{{ lookup('role_var', '_wireguard_preshared_key', role='gluetun') if (lookup('role_var', '_wireguard_preshared_key', role='gluetun') | length > 0) else omit }}"
              WIREGUARD_PRIVATE_KEY: "{{ lookup('role_var', '_wireguard_private_key', role='gluetun') if (lookup('role_var', '_wireguard_private_key', role='gluetun') | length > 0) else omit }}"
              WIREGUARD_PUBLIC_KEY: "{{ lookup('role_var', '_wireguard_public_key', role='gluetun') if (lookup('role_var', '_wireguard_public_key', role='gluetun') | length > 0) else omit }}"
            ```

        ??? variable dict "`gluetun_role_docker_envs_custom`"

            ```yaml
            # Type: dict
            gluetun_role_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable bool "`gluetun_role_docker_volumes_global`"

            ```yaml
            # Type: bool (true/false)
            gluetun_role_docker_volumes_global: false
            ```

        ??? variable list "`gluetun_role_docker_volumes_default`"

            ```yaml
            # Type: list
            gluetun_role_docker_volumes_default: 
              - "{{ gluetun_role_paths_location }}:/gluetun"
            ```

        ??? variable list "`gluetun_role_docker_volumes_custom`"

            ```yaml
            # Type: list
            gluetun_role_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable dict "`gluetun_role_docker_labels_default`"

            ```yaml
            # Type: dict
            gluetun_role_docker_labels_default: 
              com.centurylinklabs.watchtower.enable: "false"
            ```

        ??? variable dict "`gluetun_role_docker_labels_custom`"

            ```yaml
            # Type: dict
            gluetun_role_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`gluetun_role_docker_hostname`"

            ```yaml
            # Type: string
            gluetun_role_docker_hostname: "{{ gluetun_name }}"
            ```

        ##### Networks

        ??? variable string "`gluetun_role_docker_networks_alias`"

            ```yaml
            # Type: string
            gluetun_role_docker_networks_alias: "{{ gluetun_name }}"
            ```

        ??? variable list "`gluetun_role_docker_networks_default`"

            ```yaml
            # Type: list
            gluetun_role_docker_networks_default: []
            ```

        ??? variable list "`gluetun_role_docker_networks_custom`"

            ```yaml
            # Type: list
            gluetun_role_docker_networks_custom: []
            ```

        ##### Capabilities

        ??? variable list "`gluetun_role_docker_capabilities_default`"

            ```yaml
            # Type: list
            gluetun_role_docker_capabilities_default: 
              - NET_ADMIN
            ```

        ??? variable list "`gluetun_role_docker_capabilities_custom`"

            ```yaml
            # Type: list
            gluetun_role_docker_capabilities_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`gluetun_role_docker_restart_policy`"

            ```yaml
            # Type: string
            gluetun_role_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`gluetun_role_docker_state`"

            ```yaml
            # Type: string
            gluetun_role_docker_state: started
            ```

    === "Instance-level"

        ##### Container

        ??? variable string "`gluetun2_docker_container`"

            ```yaml
            # Type: string
            gluetun2_docker_container: "{{ gluetun_name }}"
            ```

        ##### Image

        ??? variable bool "`gluetun2_docker_image_pull`"

            ```yaml
            # Type: bool (true/false)
            gluetun2_docker_image_pull: true
            ```

        ??? variable string "`gluetun2_docker_image_repo`"

            ```yaml
            # Type: string
            gluetun2_docker_image_repo: "qmcgaw/gluetun"
            ```

        ??? variable string "`gluetun2_docker_image_tag`"

            ```yaml
            # Type: string
            gluetun2_docker_image_tag: "v3"
            ```

        ??? variable string "`gluetun2_docker_image`"

            ```yaml
            # Type: string
            gluetun2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='gluetun') }}:{{ lookup('role_var', '_docker_image_tag', role='gluetun') }}"
            ```

        ##### Envs

        ??? variable dict "`gluetun2_docker_envs_default`"

            ```yaml
            # Type: dict
            gluetun2_docker_envs_default: 
              DNS_KEEP_NAMESERVER: "{{ 'on' if lookup('role_var', '_docker_resolver', role='gluetun') else 'off' }}"
              FIREWALL_INPUT_PORTS: "{{ lookup('role_var', '_firewall_input_ports', role='gluetun') if (lookup('role_var', '_firewall_input_ports', role='gluetun') | length > 0) else omit }}"
              FIREWALL_OUTBOUND_SUBNETS: "{{ lookup('role_var', '_firewall_outbound_subnets', role='gluetun') if (lookup('role_var', '_firewall_outbound_subnets', role='gluetun') | length > 0) else omit }}"
              FIREWALL_VPN_INPUT_PORTS: "{{ lookup('role_var', '_firewall_vpn_input_ports', role='gluetun') if (lookup('role_var', '_firewall_vpn_input_ports', role='gluetun') | length > 0) else omit }}"
              HTTPPROXY: "on"
              HTTPPROXY_STEALTH: "on"
              OPENVPN_CUSTOM_CONFIG: "{{ lookup('role_var', '_openvpn_custom_config', role='gluetun') if (lookup('role_var', '_openvpn_custom_config', role='gluetun') | length > 0) else omit }}"
              OPENVPN_ENDPOINT_IP: "{{ lookup('role_var', '_openvpn_endpoint_ip', role='gluetun') if (lookup('role_var', '_openvpn_endpoint_ip', role='gluetun') | length > 0) else omit }}"
              OPENVPN_ENDPOINT_PORT: "{{ lookup('role_var', '_openvpn_endpoint_port', role='gluetun') if (lookup('role_var', '_openvpn_endpoint_port', role='gluetun') | length > 0) else omit }}"
              OPENVPN_KEY_PASSPHRASE: "{{ lookup('role_var', '_openvpn_key_passphrase', role='gluetun') if (lookup('role_var', '_openvpn_key_passphrase', role='gluetun') | length > 0) else omit }}"
              OPENVPN_PASSWORD: "{{ lookup('role_var', '_openvpn_password', role='gluetun') if (lookup('role_var', '_openvpn_password', role='gluetun') | length > 0) else omit }}"
              OPENVPN_USER: "{{ lookup('role_var', '_openvpn_user', role='gluetun') if (lookup('role_var', '_openvpn_user', role='gluetun') | length > 0) else omit }}"
              PGID: "{{ gid }}"
              PUID: "{{ uid }}"
              SERVER_CITIES: "{{ lookup('role_var', '_server_cities', role='gluetun') if (lookup('role_var', '_server_cities', role='gluetun') | length > 0) else omit }}"
              SERVER_COUNTRIES: "{{ lookup('role_var', '_server_countries', role='gluetun') if (lookup('role_var', '_server_countries', role='gluetun') | length > 0) else omit }}"
              SERVER_HOSTNAMES: "{{ lookup('role_var', '_server_hostnames', role='gluetun') if (lookup('role_var', '_server_hostnames', role='gluetun') | length > 0) else omit }}"
              SERVER_NAMES: "{{ lookup('role_var', '_server_names', role='gluetun') if (lookup('role_var', '_server_names', role='gluetun') | length > 0) else omit }}"
              SERVER_REGIONS: "{{ lookup('role_var', '_server_regions', role='gluetun') if (lookup('role_var', '_server_regions', role='gluetun') | length > 0) else omit }}"
              TZ: "{{ tz }}"
              VPN_ENDPOINT_IP: "{{ lookup('role_var', '_vpn_endpoint_ip', role='gluetun') if (lookup('role_var', '_vpn_endpoint_ip', role='gluetun') | length > 0) else omit }}"
              VPN_ENDPOINT_PORT: "{{ lookup('role_var', '_vpn_endpoint_port', role='gluetun') if (lookup('role_var', '_vpn_endpoint_port', role='gluetun') | length > 0) else omit }}"
              VPN_SERVICE_PROVIDER: "{{ lookup('role_var', '_vpn_service_provider', role='gluetun') if (lookup('role_var', '_vpn_service_provider', role='gluetun') | length > 0) else omit }}"
              VPN_TYPE: "{{ lookup('role_var', '_vpn_type', role='gluetun') if (lookup('role_var', '_vpn_type', role='gluetun') | length > 0) else omit }}"
              WIREGUARD_ADDRESSES: "{{ lookup('role_var', '_wireguard_addresses', role='gluetun') if (lookup('role_var', '_wireguard_addresses', role='gluetun') | length > 0) else omit }}"
              WIREGUARD_ENDPOINT_IP: "{{ lookup('role_var', '_wireguard_endpoint_ip', role='gluetun') if (lookup('role_var', '_wireguard_endpoint_ip', role='gluetun') | length > 0) else omit }}"
              WIREGUARD_ENDPOINT_PORT: "{{ lookup('role_var', '_wireguard_endpoint_port', role='gluetun') if (lookup('role_var', '_wireguard_endpoint_port', role='gluetun') | length > 0) else omit }}"
              WIREGUARD_MTU: "{{ lookup('role_var', '_wireguard_mtu', role='gluetun') if (lookup('role_var', '_wireguard_mtu', role='gluetun') | length > 0) else omit }}"
              WIREGUARD_PRESHARED_KEY: "{{ lookup('role_var', '_wireguard_preshared_key', role='gluetun') if (lookup('role_var', '_wireguard_preshared_key', role='gluetun') | length > 0) else omit }}"
              WIREGUARD_PRIVATE_KEY: "{{ lookup('role_var', '_wireguard_private_key', role='gluetun') if (lookup('role_var', '_wireguard_private_key', role='gluetun') | length > 0) else omit }}"
              WIREGUARD_PUBLIC_KEY: "{{ lookup('role_var', '_wireguard_public_key', role='gluetun') if (lookup('role_var', '_wireguard_public_key', role='gluetun') | length > 0) else omit }}"
            ```

        ??? variable dict "`gluetun2_docker_envs_custom`"

            ```yaml
            # Type: dict
            gluetun2_docker_envs_custom: {}
            ```

        ##### Volumes

        ??? variable bool "`gluetun2_docker_volumes_global`"

            ```yaml
            # Type: bool (true/false)
            gluetun2_docker_volumes_global: false
            ```

        ??? variable list "`gluetun2_docker_volumes_default`"

            ```yaml
            # Type: list
            gluetun2_docker_volumes_default: 
              - "{{ gluetun_role_paths_location }}:/gluetun"
            ```

        ??? variable list "`gluetun2_docker_volumes_custom`"

            ```yaml
            # Type: list
            gluetun2_docker_volumes_custom: []
            ```

        ##### Labels

        ??? variable dict "`gluetun2_docker_labels_default`"

            ```yaml
            # Type: dict
            gluetun2_docker_labels_default: 
              com.centurylinklabs.watchtower.enable: "false"
            ```

        ??? variable dict "`gluetun2_docker_labels_custom`"

            ```yaml
            # Type: dict
            gluetun2_docker_labels_custom: {}
            ```

        ##### Hostname

        ??? variable string "`gluetun2_docker_hostname`"

            ```yaml
            # Type: string
            gluetun2_docker_hostname: "{{ gluetun_name }}"
            ```

        ##### Networks

        ??? variable string "`gluetun2_docker_networks_alias`"

            ```yaml
            # Type: string
            gluetun2_docker_networks_alias: "{{ gluetun_name }}"
            ```

        ??? variable list "`gluetun2_docker_networks_default`"

            ```yaml
            # Type: list
            gluetun2_docker_networks_default: []
            ```

        ??? variable list "`gluetun2_docker_networks_custom`"

            ```yaml
            # Type: list
            gluetun2_docker_networks_custom: []
            ```

        ##### Capabilities

        ??? variable list "`gluetun2_docker_capabilities_default`"

            ```yaml
            # Type: list
            gluetun2_docker_capabilities_default: 
              - NET_ADMIN
            ```

        ??? variable list "`gluetun2_docker_capabilities_custom`"

            ```yaml
            # Type: list
            gluetun2_docker_capabilities_custom: []
            ```

        ##### Restart Policy

        ??? variable string "`gluetun2_docker_restart_policy`"

            ```yaml
            # Type: string
            gluetun2_docker_restart_policy: unless-stopped
            ```

        ##### State

        ??? variable string "`gluetun2_docker_state`"

            ```yaml
            # Type: string
            gluetun2_docker_state: started
            ```

=== "Docker+"

    #### Additional Docker Options

    The following advanced options are available via create_docker_container but are not defined in the role. See: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

    === "Role-level"

        ##### Resource Limits

        ??? variable int "`gluetun_role_docker_blkio_weight`"

            ```yaml
            # Type: int
            gluetun_role_docker_blkio_weight:
            ```

        ??? variable int "`gluetun_role_docker_cpu_period`"

            ```yaml
            # Type: int
            gluetun_role_docker_cpu_period:
            ```

        ??? variable int "`gluetun_role_docker_cpu_quota`"

            ```yaml
            # Type: int
            gluetun_role_docker_cpu_quota:
            ```

        ??? variable int "`gluetun_role_docker_cpu_shares`"

            ```yaml
            # Type: int
            gluetun_role_docker_cpu_shares:
            ```

        ??? variable string "`gluetun_role_docker_cpus`"

            ```yaml
            # Type: string
            gluetun_role_docker_cpus:
            ```

        ??? variable string "`gluetun_role_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            gluetun_role_docker_cpuset_cpus:
            ```

        ??? variable string "`gluetun_role_docker_cpuset_mems`"

            ```yaml
            # Type: string
            gluetun_role_docker_cpuset_mems:
            ```

        ??? variable string "`gluetun_role_docker_kernel_memory`"

            ```yaml
            # Type: string
            gluetun_role_docker_kernel_memory:
            ```

        ??? variable string "`gluetun_role_docker_memory`"

            ```yaml
            # Type: string
            gluetun_role_docker_memory:
            ```

        ??? variable string "`gluetun_role_docker_memory_reservation`"

            ```yaml
            # Type: string
            gluetun_role_docker_memory_reservation:
            ```

        ??? variable string "`gluetun_role_docker_memory_swap`"

            ```yaml
            # Type: string
            gluetun_role_docker_memory_swap:
            ```

        ??? variable int "`gluetun_role_docker_memory_swappiness`"

            ```yaml
            # Type: int
            gluetun_role_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`gluetun_role_docker_cap_drop`"

            ```yaml
            # Type: list
            gluetun_role_docker_cap_drop:
            ```

        ??? variable list "`gluetun_role_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            gluetun_role_docker_device_cgroup_rules:
            ```

        ??? variable list "`gluetun_role_docker_device_read_bps`"

            ```yaml
            # Type: list
            gluetun_role_docker_device_read_bps:
            ```

        ??? variable list "`gluetun_role_docker_device_read_iops`"

            ```yaml
            # Type: list
            gluetun_role_docker_device_read_iops:
            ```

        ??? variable list "`gluetun_role_docker_device_requests`"

            ```yaml
            # Type: list
            gluetun_role_docker_device_requests:
            ```

        ??? variable list "`gluetun_role_docker_device_write_bps`"

            ```yaml
            # Type: list
            gluetun_role_docker_device_write_bps:
            ```

        ??? variable list "`gluetun_role_docker_device_write_iops`"

            ```yaml
            # Type: list
            gluetun_role_docker_device_write_iops:
            ```

        ??? variable list "`gluetun_role_docker_devices`"

            ```yaml
            # Type: list
            gluetun_role_docker_devices:
            ```

        ??? variable string "`gluetun_role_docker_devices_default`"

            ```yaml
            # Type: string
            gluetun_role_docker_devices_default:
            ```

        ??? variable bool "`gluetun_role_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            gluetun_role_docker_privileged:
            ```

        ??? variable list "`gluetun_role_docker_security_opts`"

            ```yaml
            # Type: list
            gluetun_role_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`gluetun_role_docker_dns_opts`"

            ```yaml
            # Type: list
            gluetun_role_docker_dns_opts:
            ```

        ??? variable list "`gluetun_role_docker_dns_search_domains`"

            ```yaml
            # Type: list
            gluetun_role_docker_dns_search_domains:
            ```

        ??? variable list "`gluetun_role_docker_dns_servers`"

            ```yaml
            # Type: list
            gluetun_role_docker_dns_servers:
            ```

        ??? variable dict "`gluetun_role_docker_hosts`"

            ```yaml
            # Type: dict
            gluetun_role_docker_hosts:
            ```

        ??? variable string "`gluetun_role_docker_hosts_use_common`"

            ```yaml
            # Type: string
            gluetun_role_docker_hosts_use_common:
            ```

        ??? variable string "`gluetun_role_docker_network_mode`"

            ```yaml
            # Type: string
            gluetun_role_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`gluetun_role_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            gluetun_role_docker_keep_volumes:
            ```

        ??? variable list "`gluetun_role_docker_mounts`"

            ```yaml
            # Type: list
            gluetun_role_docker_mounts:
            ```

        ??? variable string "`gluetun_role_docker_volume_driver`"

            ```yaml
            # Type: string
            gluetun_role_docker_volume_driver:
            ```

        ??? variable list "`gluetun_role_docker_volumes_from`"

            ```yaml
            # Type: list
            gluetun_role_docker_volumes_from:
            ```

        ??? variable string "`gluetun_role_docker_working_dir`"

            ```yaml
            # Type: string
            gluetun_role_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`gluetun_role_docker_healthcheck`"

            ```yaml
            # Type: dict
            gluetun_role_docker_healthcheck:
            ```

        ??? variable bool "`gluetun_role_docker_init`"

            ```yaml
            # Type: bool (true/false)
            gluetun_role_docker_init:
            ```

        ??? variable string "`gluetun_role_docker_log_driver`"

            ```yaml
            # Type: string
            gluetun_role_docker_log_driver:
            ```

        ??? variable dict "`gluetun_role_docker_log_options`"

            ```yaml
            # Type: dict
            gluetun_role_docker_log_options:
            ```

        ??? variable bool "`gluetun_role_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            gluetun_role_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`gluetun_role_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            gluetun_role_docker_auto_remove:
            ```

        ??? variable string "`gluetun_role_docker_cgroup_parent`"

            ```yaml
            # Type: string
            gluetun_role_docker_cgroup_parent:
            ```

        ??? variable string "`gluetun_role_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            gluetun_role_docker_cgroupns_mode:
            ```

        ??? variable bool "`gluetun_role_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            gluetun_role_docker_cleanup:
            ```

        ??? variable list "`gluetun_role_docker_commands`"

            ```yaml
            # Type: list
            gluetun_role_docker_commands:
            ```

        ??? variable string "`gluetun_role_docker_create_timeout`"

            ```yaml
            # Type: string
            gluetun_role_docker_create_timeout:
            ```

        ??? variable string "`gluetun_role_docker_domainname`"

            ```yaml
            # Type: string
            gluetun_role_docker_domainname:
            ```

        ??? variable string "`gluetun_role_docker_entrypoint`"

            ```yaml
            # Type: string
            gluetun_role_docker_entrypoint:
            ```

        ??? variable string "`gluetun_role_docker_env_file`"

            ```yaml
            # Type: string
            gluetun_role_docker_env_file:
            ```

        ??? variable list "`gluetun_role_docker_exposed_ports`"

            ```yaml
            # Type: list
            gluetun_role_docker_exposed_ports:
            ```

        ??? variable string "`gluetun_role_docker_force_kill`"

            ```yaml
            # Type: string
            gluetun_role_docker_force_kill:
            ```

        ??? variable list "`gluetun_role_docker_groups`"

            ```yaml
            # Type: list
            gluetun_role_docker_groups:
            ```

        ??? variable int "`gluetun_role_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            gluetun_role_docker_healthy_wait_timeout:
            ```

        ??? variable string "`gluetun_role_docker_ipc_mode`"

            ```yaml
            # Type: string
            gluetun_role_docker_ipc_mode:
            ```

        ??? variable string "`gluetun_role_docker_kill_signal`"

            ```yaml
            # Type: string
            gluetun_role_docker_kill_signal:
            ```

        ??? variable string "`gluetun_role_docker_labels_use_common`"

            ```yaml
            # Type: string
            gluetun_role_docker_labels_use_common:
            ```

        ??? variable list "`gluetun_role_docker_links`"

            ```yaml
            # Type: list
            gluetun_role_docker_links:
            ```

        ??? variable bool "`gluetun_role_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            gluetun_role_docker_oom_killer:
            ```

        ??? variable int "`gluetun_role_docker_oom_score_adj`"

            ```yaml
            # Type: int
            gluetun_role_docker_oom_score_adj:
            ```

        ??? variable bool "`gluetun_role_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            gluetun_role_docker_paused:
            ```

        ??? variable string "`gluetun_role_docker_pid_mode`"

            ```yaml
            # Type: string
            gluetun_role_docker_pid_mode:
            ```

        ??? variable list "`gluetun_role_docker_ports`"

            ```yaml
            # Type: list
            gluetun_role_docker_ports:
            ```

        ??? variable bool "`gluetun_role_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            gluetun_role_docker_read_only:
            ```

        ??? variable bool "`gluetun_role_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            gluetun_role_docker_recreate:
            ```

        ??? variable int "`gluetun_role_docker_restart_retries`"

            ```yaml
            # Type: int
            gluetun_role_docker_restart_retries:
            ```

        ??? variable string "`gluetun_role_docker_runtime`"

            ```yaml
            # Type: string
            gluetun_role_docker_runtime:
            ```

        ??? variable string "`gluetun_role_docker_shm_size`"

            ```yaml
            # Type: string
            gluetun_role_docker_shm_size:
            ```

        ??? variable int "`gluetun_role_docker_stop_timeout`"

            ```yaml
            # Type: int
            gluetun_role_docker_stop_timeout:
            ```

        ??? variable dict "`gluetun_role_docker_storage_opts`"

            ```yaml
            # Type: dict
            gluetun_role_docker_storage_opts:
            ```

        ??? variable list "`gluetun_role_docker_sysctls`"

            ```yaml
            # Type: list
            gluetun_role_docker_sysctls:
            ```

        ??? variable list "`gluetun_role_docker_tmpfs`"

            ```yaml
            # Type: list
            gluetun_role_docker_tmpfs:
            ```

        ??? variable list "`gluetun_role_docker_ulimits`"

            ```yaml
            # Type: list
            gluetun_role_docker_ulimits:
            ```

        ??? variable string "`gluetun_role_docker_user`"

            ```yaml
            # Type: string
            gluetun_role_docker_user:
            ```

        ??? variable string "`gluetun_role_docker_userns_mode`"

            ```yaml
            # Type: string
            gluetun_role_docker_userns_mode:
            ```

        ??? variable string "`gluetun_role_docker_uts`"

            ```yaml
            # Type: string
            gluetun_role_docker_uts:
            ```

    === "Instance-level"

        ##### Resource Limits

        ??? variable int "`gluetun2_docker_blkio_weight`"

            ```yaml
            # Type: int
            gluetun2_docker_blkio_weight:
            ```

        ??? variable int "`gluetun2_docker_cpu_period`"

            ```yaml
            # Type: int
            gluetun2_docker_cpu_period:
            ```

        ??? variable int "`gluetun2_docker_cpu_quota`"

            ```yaml
            # Type: int
            gluetun2_docker_cpu_quota:
            ```

        ??? variable int "`gluetun2_docker_cpu_shares`"

            ```yaml
            # Type: int
            gluetun2_docker_cpu_shares:
            ```

        ??? variable string "`gluetun2_docker_cpus`"

            ```yaml
            # Type: string
            gluetun2_docker_cpus:
            ```

        ??? variable string "`gluetun2_docker_cpuset_cpus`"

            ```yaml
            # Type: string
            gluetun2_docker_cpuset_cpus:
            ```

        ??? variable string "`gluetun2_docker_cpuset_mems`"

            ```yaml
            # Type: string
            gluetun2_docker_cpuset_mems:
            ```

        ??? variable string "`gluetun2_docker_kernel_memory`"

            ```yaml
            # Type: string
            gluetun2_docker_kernel_memory:
            ```

        ??? variable string "`gluetun2_docker_memory`"

            ```yaml
            # Type: string
            gluetun2_docker_memory:
            ```

        ??? variable string "`gluetun2_docker_memory_reservation`"

            ```yaml
            # Type: string
            gluetun2_docker_memory_reservation:
            ```

        ??? variable string "`gluetun2_docker_memory_swap`"

            ```yaml
            # Type: string
            gluetun2_docker_memory_swap:
            ```

        ??? variable int "`gluetun2_docker_memory_swappiness`"

            ```yaml
            # Type: int
            gluetun2_docker_memory_swappiness:
            ```

        ##### Security & Devices

        ??? variable list "`gluetun2_docker_cap_drop`"

            ```yaml
            # Type: list
            gluetun2_docker_cap_drop:
            ```

        ??? variable list "`gluetun2_docker_device_cgroup_rules`"

            ```yaml
            # Type: list
            gluetun2_docker_device_cgroup_rules:
            ```

        ??? variable list "`gluetun2_docker_device_read_bps`"

            ```yaml
            # Type: list
            gluetun2_docker_device_read_bps:
            ```

        ??? variable list "`gluetun2_docker_device_read_iops`"

            ```yaml
            # Type: list
            gluetun2_docker_device_read_iops:
            ```

        ??? variable list "`gluetun2_docker_device_requests`"

            ```yaml
            # Type: list
            gluetun2_docker_device_requests:
            ```

        ??? variable list "`gluetun2_docker_device_write_bps`"

            ```yaml
            # Type: list
            gluetun2_docker_device_write_bps:
            ```

        ??? variable list "`gluetun2_docker_device_write_iops`"

            ```yaml
            # Type: list
            gluetun2_docker_device_write_iops:
            ```

        ??? variable list "`gluetun2_docker_devices`"

            ```yaml
            # Type: list
            gluetun2_docker_devices:
            ```

        ??? variable string "`gluetun2_docker_devices_default`"

            ```yaml
            # Type: string
            gluetun2_docker_devices_default:
            ```

        ??? variable bool "`gluetun2_docker_privileged`"

            ```yaml
            # Type: bool (true/false)
            gluetun2_docker_privileged:
            ```

        ??? variable list "`gluetun2_docker_security_opts`"

            ```yaml
            # Type: list
            gluetun2_docker_security_opts:
            ```

        ##### Networking

        ??? variable list "`gluetun2_docker_dns_opts`"

            ```yaml
            # Type: list
            gluetun2_docker_dns_opts:
            ```

        ??? variable list "`gluetun2_docker_dns_search_domains`"

            ```yaml
            # Type: list
            gluetun2_docker_dns_search_domains:
            ```

        ??? variable list "`gluetun2_docker_dns_servers`"

            ```yaml
            # Type: list
            gluetun2_docker_dns_servers:
            ```

        ??? variable dict "`gluetun2_docker_hosts`"

            ```yaml
            # Type: dict
            gluetun2_docker_hosts:
            ```

        ??? variable string "`gluetun2_docker_hosts_use_common`"

            ```yaml
            # Type: string
            gluetun2_docker_hosts_use_common:
            ```

        ??? variable string "`gluetun2_docker_network_mode`"

            ```yaml
            # Type: string
            gluetun2_docker_network_mode:
            ```

        ##### Storage

        ??? variable bool "`gluetun2_docker_keep_volumes`"

            ```yaml
            # Type: bool (true/false)
            gluetun2_docker_keep_volumes:
            ```

        ??? variable list "`gluetun2_docker_mounts`"

            ```yaml
            # Type: list
            gluetun2_docker_mounts:
            ```

        ??? variable string "`gluetun2_docker_volume_driver`"

            ```yaml
            # Type: string
            gluetun2_docker_volume_driver:
            ```

        ??? variable list "`gluetun2_docker_volumes_from`"

            ```yaml
            # Type: list
            gluetun2_docker_volumes_from:
            ```

        ??? variable string "`gluetun2_docker_working_dir`"

            ```yaml
            # Type: string
            gluetun2_docker_working_dir:
            ```

        ##### Monitoring & Lifecycle

        ??? variable dict "`gluetun2_docker_healthcheck`"

            ```yaml
            # Type: dict
            gluetun2_docker_healthcheck:
            ```

        ??? variable bool "`gluetun2_docker_init`"

            ```yaml
            # Type: bool (true/false)
            gluetun2_docker_init:
            ```

        ??? variable string "`gluetun2_docker_log_driver`"

            ```yaml
            # Type: string
            gluetun2_docker_log_driver:
            ```

        ??? variable dict "`gluetun2_docker_log_options`"

            ```yaml
            # Type: dict
            gluetun2_docker_log_options:
            ```

        ??? variable bool "`gluetun2_docker_output_logs`"

            ```yaml
            # Type: bool (true/false)
            gluetun2_docker_output_logs:
            ```

        ##### Other Options

        ??? variable bool "`gluetun2_docker_auto_remove`"

            ```yaml
            # Type: bool (true/false)
            gluetun2_docker_auto_remove:
            ```

        ??? variable string "`gluetun2_docker_cgroup_parent`"

            ```yaml
            # Type: string
            gluetun2_docker_cgroup_parent:
            ```

        ??? variable string "`gluetun2_docker_cgroupns_mode`"

            ```yaml
            # Type: string
            gluetun2_docker_cgroupns_mode:
            ```

        ??? variable bool "`gluetun2_docker_cleanup`"

            ```yaml
            # Type: bool (true/false)
            gluetun2_docker_cleanup:
            ```

        ??? variable list "`gluetun2_docker_commands`"

            ```yaml
            # Type: list
            gluetun2_docker_commands:
            ```

        ??? variable string "`gluetun2_docker_create_timeout`"

            ```yaml
            # Type: string
            gluetun2_docker_create_timeout:
            ```

        ??? variable string "`gluetun2_docker_domainname`"

            ```yaml
            # Type: string
            gluetun2_docker_domainname:
            ```

        ??? variable string "`gluetun2_docker_entrypoint`"

            ```yaml
            # Type: string
            gluetun2_docker_entrypoint:
            ```

        ??? variable string "`gluetun2_docker_env_file`"

            ```yaml
            # Type: string
            gluetun2_docker_env_file:
            ```

        ??? variable list "`gluetun2_docker_exposed_ports`"

            ```yaml
            # Type: list
            gluetun2_docker_exposed_ports:
            ```

        ??? variable string "`gluetun2_docker_force_kill`"

            ```yaml
            # Type: string
            gluetun2_docker_force_kill:
            ```

        ??? variable list "`gluetun2_docker_groups`"

            ```yaml
            # Type: list
            gluetun2_docker_groups:
            ```

        ??? variable int "`gluetun2_docker_healthy_wait_timeout`"

            ```yaml
            # Type: int
            gluetun2_docker_healthy_wait_timeout:
            ```

        ??? variable string "`gluetun2_docker_ipc_mode`"

            ```yaml
            # Type: string
            gluetun2_docker_ipc_mode:
            ```

        ??? variable string "`gluetun2_docker_kill_signal`"

            ```yaml
            # Type: string
            gluetun2_docker_kill_signal:
            ```

        ??? variable string "`gluetun2_docker_labels_use_common`"

            ```yaml
            # Type: string
            gluetun2_docker_labels_use_common:
            ```

        ??? variable list "`gluetun2_docker_links`"

            ```yaml
            # Type: list
            gluetun2_docker_links:
            ```

        ??? variable bool "`gluetun2_docker_oom_killer`"

            ```yaml
            # Type: bool (true/false)
            gluetun2_docker_oom_killer:
            ```

        ??? variable int "`gluetun2_docker_oom_score_adj`"

            ```yaml
            # Type: int
            gluetun2_docker_oom_score_adj:
            ```

        ??? variable bool "`gluetun2_docker_paused`"

            ```yaml
            # Type: bool (true/false)
            gluetun2_docker_paused:
            ```

        ??? variable string "`gluetun2_docker_pid_mode`"

            ```yaml
            # Type: string
            gluetun2_docker_pid_mode:
            ```

        ??? variable list "`gluetun2_docker_ports`"

            ```yaml
            # Type: list
            gluetun2_docker_ports:
            ```

        ??? variable bool "`gluetun2_docker_read_only`"

            ```yaml
            # Type: bool (true/false)
            gluetun2_docker_read_only:
            ```

        ??? variable bool "`gluetun2_docker_recreate`"

            ```yaml
            # Type: bool (true/false)
            gluetun2_docker_recreate:
            ```

        ??? variable int "`gluetun2_docker_restart_retries`"

            ```yaml
            # Type: int
            gluetun2_docker_restart_retries:
            ```

        ??? variable string "`gluetun2_docker_runtime`"

            ```yaml
            # Type: string
            gluetun2_docker_runtime:
            ```

        ??? variable string "`gluetun2_docker_shm_size`"

            ```yaml
            # Type: string
            gluetun2_docker_shm_size:
            ```

        ??? variable int "`gluetun2_docker_stop_timeout`"

            ```yaml
            # Type: int
            gluetun2_docker_stop_timeout:
            ```

        ??? variable dict "`gluetun2_docker_storage_opts`"

            ```yaml
            # Type: dict
            gluetun2_docker_storage_opts:
            ```

        ??? variable list "`gluetun2_docker_sysctls`"

            ```yaml
            # Type: list
            gluetun2_docker_sysctls:
            ```

        ??? variable list "`gluetun2_docker_tmpfs`"

            ```yaml
            # Type: list
            gluetun2_docker_tmpfs:
            ```

        ??? variable list "`gluetun2_docker_ulimits`"

            ```yaml
            # Type: list
            gluetun2_docker_ulimits:
            ```

        ??? variable string "`gluetun2_docker_user`"

            ```yaml
            # Type: string
            gluetun2_docker_user:
            ```

        ??? variable string "`gluetun2_docker_userns_mode`"

            ```yaml
            # Type: string
            gluetun2_docker_userns_mode:
            ```

        ??? variable string "`gluetun2_docker_uts`"

            ```yaml
            # Type: string
            gluetun2_docker_uts:
            ```

=== "Global Override Options"

    === "Role-level"

        Override for all instances:

        ??? variable bool "`gluetun_role_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            gluetun_role_autoheal_enabled: true
            ```

        ??? variable string "`gluetun_role_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            gluetun_role_depends_on: ""
            ```

        ??? variable string "`gluetun_role_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            gluetun_role_depends_on_delay: "0"
            ```

        ??? variable string "`gluetun_role_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            gluetun_role_depends_on_healthchecks:
            ```

        ??? variable bool "`gluetun_role_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            gluetun_role_diun_enabled: true
            ```

        ??? variable bool "`gluetun_role_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            gluetun_role_dns_enabled: true
            ```

        ??? variable bool "`gluetun_role_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            gluetun_role_docker_controller: true
            ```

        ??? variable bool "`gluetun_role_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            gluetun_role_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`gluetun_role_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            gluetun_role_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`gluetun_role_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            gluetun_role_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`gluetun_role_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            gluetun_role_traefik_gzip_enabled: false
            ```

        ??? variable bool "`gluetun_role_traefik_middleware_http_api_insecure`"

            ```yaml
            # Type: bool (true/false)
            gluetun_role_traefik_middleware_http_api_insecure:
            ```

        ??? variable bool "`gluetun_role_traefik_middleware_http_insecure`"

            ```yaml
            # Type: bool (true/false)
            gluetun_role_traefik_middleware_http_insecure:
            ```

        ??? variable bool "`gluetun_role_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            gluetun_role_traefik_robot_enabled: true
            ```

        ??? variable bool "`gluetun_role_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            gluetun_role_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`gluetun_role_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            gluetun_role_traefik_wildcard_enabled: true
            ```

        ??? variable list "`gluetun_role_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            gluetun_role_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                gluetun_role_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "gluetun2.{{ user.domain }}"
                  - "gluetun.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`gluetun_role_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            gluetun_role_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                gluetun_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'gluetun2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`gluetun_role_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            gluetun_role_web_scheme:
            ```

    === "Instance-level"

        Override for a specific instance (e.g., `gluetun2`):

        ??? variable bool "`gluetun2_autoheal_enabled`"

            ```yaml
            # Enable or disable Autoheal monitoring for containers created when deploying
            # Type: bool (true/false)
            gluetun2_autoheal_enabled: true
            ```

        ??? variable string "`gluetun2_depends_on`"

            ```yaml
            # List of container dependencies that must be running before containers start
            # Type: string
            gluetun2_depends_on: ""
            ```

        ??? variable string "`gluetun2_depends_on_delay`"

            ```yaml
            # Delay in seconds before starting containers after dependencies are ready
            # Type: string (quoted number)
            gluetun2_depends_on_delay: "0"
            ```

        ??? variable string "`gluetun2_depends_on_healthchecks`"

            ```yaml
            # Enable healthcheck waiting for container dependencies
            # Type: string ("true"/"false")
            gluetun2_depends_on_healthchecks:
            ```

        ??? variable bool "`gluetun2_diun_enabled`"

            ```yaml
            # Enable or disable Diun update notifications for containers created when deploying
            # Type: bool (true/false)
            gluetun2_diun_enabled: true
            ```

        ??? variable bool "`gluetun2_dns_enabled`"

            ```yaml
            # Enable or disable automatic DNS record creation for containers
            # Type: bool (true/false)
            gluetun2_dns_enabled: true
            ```

        ??? variable bool "`gluetun2_docker_controller`"

            ```yaml
            # Enable or disable Saltbox Docker Controller management for containers
            # Type: bool (true/false)
            gluetun2_docker_controller: true
            ```

        ??? variable bool "`gluetun2_traefik_autodetect_enabled`"

            ```yaml
            # Enable Traefik autodetect middleware for containers
            # Type: bool (true/false)
            gluetun2_traefik_autodetect_enabled: false
            ```

        ??? variable bool "`gluetun2_traefik_crowdsec_enabled`"

            ```yaml
            # Enable CrowdSec middleware for containers
            # Type: bool (true/false)
            gluetun2_traefik_crowdsec_enabled: false
            ```

        ??? variable bool "`gluetun2_traefik_error_pages_enabled`"

            ```yaml
            # Enable custom error pages middleware for containers
            # Type: bool (true/false)
            gluetun2_traefik_error_pages_enabled: false
            ```

        ??? variable bool "`gluetun2_traefik_gzip_enabled`"

            ```yaml
            # Enable gzip compression middleware for containers
            # Type: bool (true/false)
            gluetun2_traefik_gzip_enabled: false
            ```

        ??? variable bool "`gluetun2_traefik_middleware_http_api_insecure`"

            ```yaml
            # Type: bool (true/false)
            gluetun2_traefik_middleware_http_api_insecure:
            ```

        ??? variable bool "`gluetun2_traefik_middleware_http_insecure`"

            ```yaml
            # Type: bool (true/false)
            gluetun2_traefik_middleware_http_insecure:
            ```

        ??? variable bool "`gluetun2_traefik_robot_enabled`"

            ```yaml
            # Enable robots.txt middleware for containers
            # Type: bool (true/false)
            gluetun2_traefik_robot_enabled: true
            ```

        ??? variable bool "`gluetun2_traefik_tailscale_enabled`"

            ```yaml
            # Enable Tailscale-specific Traefik configuration for containers
            # Type: bool (true/false)
            gluetun2_traefik_tailscale_enabled: false
            ```

        ??? variable bool "`gluetun2_traefik_wildcard_enabled`"

            ```yaml
            # Enable wildcard certificate for containers
            # Type: bool (true/false)
            gluetun2_traefik_wildcard_enabled: true
            ```

        ??? variable list "`gluetun2_web_fqdn_override`"

            ```yaml
            # Override the Traefik fully qualified domain name (FQDN) for containers
            # Type: list
            gluetun2_web_fqdn_override: # (1)!
            ```

            1.  Example:

                ```yaml
                gluetun2_web_fqdn_override:
                  - "{{ traefik_host }}"
                  - "gluetun2.{{ user.domain }}"
                  - "gluetun.otherdomain.tld"
                ```

                Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries

        ??? variable string "`gluetun2_web_host_override`"

            ```yaml
            # Override the Traefik web host configuration for containers
            # Type: string
            gluetun2_web_host_override: # (1)!
            ```

            1.  Example:

                ```yaml
                gluetun2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'gluetun2.' + user.domain }}`)"
                ```

                Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule

        ??? variable string "`gluetun2_web_scheme`"

            ```yaml
            # URL scheme to use for web access to containers
            # Type: string ("http"/"https")
            gluetun2_web_scheme:
            ```

<!-- END SALTBOX MANAGED VARIABLES SECTION -->
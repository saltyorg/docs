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

## Inventory
<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
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

    When overriding variables that end in `_default` (like `{role}_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

    Instead, use the corresponding `_custom` variable (like `{role}_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

??? example "Basics"

    === "Default"

        ```yaml
        # Type: list
        gluetun_instances: ["gluetun"]

        ```

    === "Example"

        ```yaml
        # Type: list
        gluetun_instances: ["gluetun", "gluetun2"]

        ```

??? example "Settings"

    === "Role-level"

        ```yaml
        # These variables map to the appropriate Docker ENVs
        # Review the gluetun wiki (https://github.com/qdm12/gluetun/wiki)
        # Type: string
        gluetun_role_vpn_service_provider: ""

        # Type: string
        gluetun_role_vpn_type: ""

        # Type: string
        gluetun_role_openvpn_custom_config: ""

        # Type: string
        gluetun_role_openvpn_endpoint_ip: ""

        # Type: string
        gluetun_role_openvpn_endpoint_port: ""

        # Type: string
        gluetun_role_openvpn_user: ""

        # Type: string
        gluetun_role_openvpn_password: ""

        # Type: string
        gluetun_role_openvpn_key_passphrase: ""

        # Type: string
        gluetun_role_vpn_endpoint_ip: ""

        # Type: string
        gluetun_role_vpn_endpoint_port: ""

        # Type: string
        gluetun_role_wireguard_endpoint_ip: ""

        # Type: string
        gluetun_role_wireguard_endpoint_port: ""

        # Type: string
        gluetun_role_wireguard_mtu: ""

        # Type: string
        gluetun_role_wireguard_public_key: ""

        # Type: string
        gluetun_role_wireguard_private_key: ""

        # Type: string
        gluetun_role_wireguard_preshared_key: ""

        # Type: string
        gluetun_role_wireguard_addresses: ""

        # Type: string
        gluetun_role_server_countries: ""

        # Type: string
        gluetun_role_server_cities: ""

        # Type: string
        gluetun_role_server_hostnames: ""

        # Type: string
        gluetun_role_server_names: ""

        # Type: string
        gluetun_role_server_regions: ""

        # Type: string
        gluetun_role_firewall_vpn_input_ports: ""

        # Type: string
        gluetun_role_firewall_input_ports: ""

        # Type: string
        gluetun_role_firewall_outbound_subnets: ""

        # Type: bool (true/false)
        gluetun_role_docker_resolver: true

        ```

    === "Instance-level"

        ```yaml
        # These variables map to the appropriate Docker ENVs
        # Review the gluetun wiki (https://github.com/qdm12/gluetun/wiki)
        # Type: string
        gluetun2_vpn_service_provider: ""

        # Type: string
        gluetun2_vpn_type: ""

        # Type: string
        gluetun2_openvpn_custom_config: ""

        # Type: string
        gluetun2_openvpn_endpoint_ip: ""

        # Type: string
        gluetun2_openvpn_endpoint_port: ""

        # Type: string
        gluetun2_openvpn_user: ""

        # Type: string
        gluetun2_openvpn_password: ""

        # Type: string
        gluetun2_openvpn_key_passphrase: ""

        # Type: string
        gluetun2_vpn_endpoint_ip: ""

        # Type: string
        gluetun2_vpn_endpoint_port: ""

        # Type: string
        gluetun2_wireguard_endpoint_ip: ""

        # Type: string
        gluetun2_wireguard_endpoint_port: ""

        # Type: string
        gluetun2_wireguard_mtu: ""

        # Type: string
        gluetun2_wireguard_public_key: ""

        # Type: string
        gluetun2_wireguard_private_key: ""

        # Type: string
        gluetun2_wireguard_preshared_key: ""

        # Type: string
        gluetun2_wireguard_addresses: ""

        # Type: string
        gluetun2_server_countries: ""

        # Type: string
        gluetun2_server_cities: ""

        # Type: string
        gluetun2_server_hostnames: ""

        # Type: string
        gluetun2_server_names: ""

        # Type: string
        gluetun2_server_regions: ""

        # Type: string
        gluetun2_firewall_vpn_input_ports: ""

        # Type: string
        gluetun2_firewall_input_ports: ""

        # Type: string
        gluetun2_firewall_outbound_subnets: ""

        # Type: bool (true/false)
        gluetun2_docker_resolver: true

        ```

??? example "Paths"

    === "Role-level"

        ```yaml
        # Type: string
        gluetun_role_paths_folder: "{{ gluetun_name }}"

        # Type: string
        gluetun_role_paths_location: "{{ server_appdata_path }}/{{ gluetun_role_paths_folder }}"

        ```

    === "Instance-level"

        ```yaml
        # Type: string
        gluetun2_paths_folder: "{{ gluetun_name }}"

        # Type: string
        gluetun2_paths_location: "{{ server_appdata_path }}/{{ gluetun_role_paths_folder }}"

        ```

??? example "Docker"

    === "Role-level"

        ```yaml
        # Container
        # Type: string
        gluetun_role_docker_container: "{{ gluetun_name }}"

        # Image
        # Type: bool (true/false)
        gluetun_role_docker_image_pull: true

        # Type: string
        gluetun_role_docker_image_repo: "qmcgaw/gluetun"

        # Type: string
        gluetun_role_docker_image_tag: "v3"

        # Type: string
        gluetun_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='gluetun') }}:{{ lookup('role_var', '_docker_image_tag', role='gluetun') }}"

        # Envs
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

        # Type: dict
        gluetun_role_docker_envs_custom: {}

        # Volumes
        # Type: bool (true/false)
        gluetun_role_docker_volumes_global: false

        # Type: list
        gluetun_role_docker_volumes_default: 
          - "{{ gluetun_role_paths_location }}:/gluetun"

        # Type: list
        gluetun_role_docker_volumes_custom: []

        # Labels
        # Type: dict
        gluetun_role_docker_labels_default: 
          com.centurylinklabs.watchtower.enable: "false"

        # Type: dict
        gluetun_role_docker_labels_custom: {}

        # Hostname
        # Type: string
        gluetun_role_docker_hostname: "{{ gluetun_name }}"

        # Networks
        # Type: string
        gluetun_role_docker_networks_alias: "{{ gluetun_name }}"

        # Type: list
        gluetun_role_docker_networks_default: []

        # Type: list
        gluetun_role_docker_networks_custom: []

        # Capabilities
        # Type: list
        gluetun_role_docker_capabilities_default: 
          - NET_ADMIN

        # Type: list
        gluetun_role_docker_capabilities_custom: []

        # Restart Policy
        # Type: string
        gluetun_role_docker_restart_policy: unless-stopped

        # State
        # Type: string
        gluetun_role_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via create_docker_container
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        gluetun_role_docker_blkio_weight:

        # Type: int
        gluetun_role_docker_cpu_period:

        # Type: int
        gluetun_role_docker_cpu_quota:

        # Type: int
        gluetun_role_docker_cpu_shares:

        # Type: string
        gluetun_role_docker_cpus:

        # Type: string
        gluetun_role_docker_cpuset_cpus:

        # Type: string
        gluetun_role_docker_cpuset_mems:

        # Type: string
        gluetun_role_docker_kernel_memory:

        # Type: string
        gluetun_role_docker_memory:

        # Type: string
        gluetun_role_docker_memory_reservation:

        # Type: string
        gluetun_role_docker_memory_swap:

        # Type: int
        gluetun_role_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        gluetun_role_docker_cap_drop:

        # Type: list
        gluetun_role_docker_device_cgroup_rules:

        # Type: list
        gluetun_role_docker_device_read_bps:

        # Type: list
        gluetun_role_docker_device_read_iops:

        # Type: list
        gluetun_role_docker_device_requests:

        # Type: list
        gluetun_role_docker_device_write_bps:

        # Type: list
        gluetun_role_docker_device_write_iops:

        # Type: list
        gluetun_role_docker_devices:

        # Type: string
        gluetun_role_docker_devices_default:

        # Type: bool (true/false)
        gluetun_role_docker_privileged:

        # Type: list
        gluetun_role_docker_security_opts:

        # Networking
        # Type: list
        gluetun_role_docker_dns_opts:

        # Type: list
        gluetun_role_docker_dns_search_domains:

        # Type: list
        gluetun_role_docker_dns_servers:

        # Type: dict
        gluetun_role_docker_hosts:

        # Type: string
        gluetun_role_docker_hosts_use_common:

        # Type: string
        gluetun_role_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        gluetun_role_docker_keep_volumes:

        # Type: list
        gluetun_role_docker_mounts:

        # Type: string
        gluetun_role_docker_volume_driver:

        # Type: list
        gluetun_role_docker_volumes_from:

        # Type: string
        gluetun_role_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        gluetun_role_docker_healthcheck:

        # Type: bool (true/false)
        gluetun_role_docker_init:

        # Type: string
        gluetun_role_docker_log_driver:

        # Type: dict
        gluetun_role_docker_log_options:

        # Type: bool (true/false)
        gluetun_role_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        gluetun_role_docker_auto_remove:

        # Type: string
        gluetun_role_docker_cgroup_parent:

        # Type: string
        gluetun_role_docker_cgroupns_mode:

        # Type: bool (true/false)
        gluetun_role_docker_cleanup:

        # Type: list
        gluetun_role_docker_commands:

        # Type: string
        gluetun_role_docker_create_timeout:

        # Type: string
        gluetun_role_docker_domainname:

        # Type: string
        gluetun_role_docker_entrypoint:

        # Type: string
        gluetun_role_docker_env_file:

        # Type: list
        gluetun_role_docker_exposed_ports:

        # Type: string
        gluetun_role_docker_force_kill:

        # Type: list
        gluetun_role_docker_groups:

        # Type: int
        gluetun_role_docker_healthy_wait_timeout:

        # Type: string
        gluetun_role_docker_ipc_mode:

        # Type: string
        gluetun_role_docker_kill_signal:

        # Type: string
        gluetun_role_docker_labels_use_common:

        # Type: list
        gluetun_role_docker_links:

        # Type: bool (true/false)
        gluetun_role_docker_oom_killer:

        # Type: int
        gluetun_role_docker_oom_score_adj:

        # Type: bool (true/false)
        gluetun_role_docker_paused:

        # Type: string
        gluetun_role_docker_pid_mode:

        # Type: list
        gluetun_role_docker_ports:

        # Type: bool (true/false)
        gluetun_role_docker_read_only:

        # Type: bool (true/false)
        gluetun_role_docker_recreate:

        # Type: int
        gluetun_role_docker_restart_retries:

        # Type: string
        gluetun_role_docker_runtime:

        # Type: string
        gluetun_role_docker_shm_size:

        # Type: int
        gluetun_role_docker_stop_timeout:

        # Type: dict
        gluetun_role_docker_storage_opts:

        # Type: list
        gluetun_role_docker_sysctls:

        # Type: list
        gluetun_role_docker_tmpfs:

        # Type: list
        gluetun_role_docker_ulimits:

        # Type: string
        gluetun_role_docker_user:

        # Type: string
        gluetun_role_docker_userns_mode:

        # Type: string
        gluetun_role_docker_uts:

        ```

    === "Instance-level"

        ```yaml
        # Container
        # Type: string
        gluetun2_docker_container: "{{ gluetun_name }}"

        # Image
        # Type: bool (true/false)
        gluetun2_docker_image_pull: true

        # Type: string
        gluetun2_docker_image_repo: "qmcgaw/gluetun"

        # Type: string
        gluetun2_docker_image_tag: "v3"

        # Type: string
        gluetun2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='gluetun') }}:{{ lookup('role_var', '_docker_image_tag', role='gluetun') }}"

        # Envs
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

        # Type: dict
        gluetun2_docker_envs_custom: {}

        # Volumes
        # Type: bool (true/false)
        gluetun2_docker_volumes_global: false

        # Type: list
        gluetun2_docker_volumes_default: 
          - "{{ gluetun_role_paths_location }}:/gluetun"

        # Type: list
        gluetun2_docker_volumes_custom: []

        # Labels
        # Type: dict
        gluetun2_docker_labels_default: 
          com.centurylinklabs.watchtower.enable: "false"

        # Type: dict
        gluetun2_docker_labels_custom: {}

        # Hostname
        # Type: string
        gluetun2_docker_hostname: "{{ gluetun_name }}"

        # Networks
        # Type: string
        gluetun2_docker_networks_alias: "{{ gluetun_name }}"

        # Type: list
        gluetun2_docker_networks_default: []

        # Type: list
        gluetun2_docker_networks_custom: []

        # Capabilities
        # Type: list
        gluetun2_docker_capabilities_default: 
          - NET_ADMIN

        # Type: list
        gluetun2_docker_capabilities_custom: []

        # Restart Policy
        # Type: string
        gluetun2_docker_restart_policy: unless-stopped

        # State
        # Type: string
        gluetun2_docker_state: started


        # ---- Additional Docker Options ----
        # The following advanced options are available via lookup('docker_var', ...)
        # but are not defined in the role. See:
        # https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

        # Resource Limits
        # Type: int
        gluetun2_docker_blkio_weight:
        # Type: int
        gluetun2_docker_cpu_period:
        # Type: int
        gluetun2_docker_cpu_quota:
        # Type: int
        gluetun2_docker_cpu_shares:
        # Type: string
        gluetun2_docker_cpus:
        # Type: string
        gluetun2_docker_cpuset_cpus:
        # Type: string
        gluetun2_docker_cpuset_mems:
        # Type: string
        gluetun2_docker_kernel_memory:
        # Type: string
        gluetun2_docker_memory:
        # Type: string
        gluetun2_docker_memory_reservation:
        # Type: string
        gluetun2_docker_memory_swap:
        # Type: int
        gluetun2_docker_memory_swappiness:

        # Security & Devices
        # Type: list
        gluetun2_docker_cap_drop:
        # Type: list
        gluetun2_docker_device_cgroup_rules:
        # Type: list
        gluetun2_docker_device_read_bps:
        # Type: list
        gluetun2_docker_device_read_iops:
        # Type: list
        gluetun2_docker_device_requests:
        # Type: list
        gluetun2_docker_device_write_bps:
        # Type: list
        gluetun2_docker_device_write_iops:
        # Type: list
        gluetun2_docker_devices:
        # Type: string
        gluetun2_docker_devices_default:
        # Type: bool (true/false)
        gluetun2_docker_privileged:
        # Type: list
        gluetun2_docker_security_opts:

        # Networking
        # Type: list
        gluetun2_docker_dns_opts:
        # Type: list
        gluetun2_docker_dns_search_domains:
        # Type: list
        gluetun2_docker_dns_servers:
        # Type: dict
        gluetun2_docker_hosts:
        # Type: string
        gluetun2_docker_hosts_use_common:
        # Type: string
        gluetun2_docker_network_mode:

        # Storage
        # Type: bool (true/false)
        gluetun2_docker_keep_volumes:
        # Type: list
        gluetun2_docker_mounts:
        # Type: string
        gluetun2_docker_volume_driver:
        # Type: list
        gluetun2_docker_volumes_from:
        # Type: string
        gluetun2_docker_working_dir:

        # Monitoring & Lifecycle
        # Type: dict
        gluetun2_docker_healthcheck:
        # Type: bool (true/false)
        gluetun2_docker_init:
        # Type: string
        gluetun2_docker_log_driver:
        # Type: dict
        gluetun2_docker_log_options:
        # Type: bool (true/false)
        gluetun2_docker_output_logs:

        # Other Options
        # Type: bool (true/false)
        gluetun2_docker_auto_remove:
        # Type: string
        gluetun2_docker_cgroup_parent:
        # Type: string
        gluetun2_docker_cgroupns_mode:
        # Type: bool (true/false)
        gluetun2_docker_cleanup:
        # Type: list
        gluetun2_docker_commands:
        # Type: string
        gluetun2_docker_create_timeout:
        # Type: string
        gluetun2_docker_domainname:
        # Type: string
        gluetun2_docker_entrypoint:
        # Type: string
        gluetun2_docker_env_file:
        # Type: list
        gluetun2_docker_exposed_ports:
        # Type: string
        gluetun2_docker_force_kill:
        # Type: list
        gluetun2_docker_groups:
        # Type: int
        gluetun2_docker_healthy_wait_timeout:
        # Type: string
        gluetun2_docker_ipc_mode:
        # Type: string
        gluetun2_docker_kill_signal:
        # Type: string
        gluetun2_docker_labels_use_common:
        # Type: list
        gluetun2_docker_links:
        # Type: bool (true/false)
        gluetun2_docker_oom_killer:
        # Type: int
        gluetun2_docker_oom_score_adj:
        # Type: bool (true/false)
        gluetun2_docker_paused:
        # Type: string
        gluetun2_docker_pid_mode:
        # Type: list
        gluetun2_docker_ports:
        # Type: bool (true/false)
        gluetun2_docker_read_only:
        # Type: bool (true/false)
        gluetun2_docker_recreate:
        # Type: int
        gluetun2_docker_restart_retries:
        # Type: string
        gluetun2_docker_runtime:
        # Type: string
        gluetun2_docker_shm_size:
        # Type: int
        gluetun2_docker_stop_timeout:
        # Type: dict
        gluetun2_docker_storage_opts:
        # Type: list
        gluetun2_docker_sysctls:
        # Type: list
        gluetun2_docker_tmpfs:
        # Type: list
        gluetun2_docker_ulimits:
        # Type: string
        gluetun2_docker_user:
        # Type: string
        gluetun2_docker_userns_mode:
        # Type: string
        gluetun2_docker_uts:

        ```

??? example "Global Override Options"

    === "Role-level"

        Override for all instances:

        ```yaml
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        gluetun_role_autoheal_enabled: true

        # List of container dependencies that must be running before containers start
        # Type: string
        gluetun_role_depends_on: ""

        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        gluetun_role_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        gluetun_role_depends_on_healthchecks:

        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        gluetun_role_diun_enabled: true

        # Enable or disable automatic DNS record creation for containers
        # Type: bool (true/false)
        gluetun_role_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        gluetun_role_docker_controller: true

        # Enable Traefik autodetect middleware for containers
        # Type: bool (true/false)
        gluetun_role_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for containers
        # Type: bool (true/false)
        gluetun_role_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for containers
        # Type: bool (true/false)
        gluetun_role_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for containers
        # Type: bool (true/false)
        gluetun_role_traefik_gzip_enabled: false

        # Enable robots.txt middleware for containers
        # Type: bool (true/false)
        gluetun_role_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for containers
        # Type: bool (true/false)
        gluetun_role_traefik_tailscale_enabled: false

        # Enable wildcard certificate for containers
        # Type: bool (true/false)
        gluetun_role_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for containers
        # Type: list
        gluetun_role_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for containers
        # Type: string
        gluetun_role_web_host_override: # (2)!

        # URL scheme to use for web access to containers
        # Type: string ("http"/"https")
        gluetun_role_web_scheme:

        ```

        1.  Example:

            ```yaml
            gluetun_role_web_fqdn_override:
              - "{{ traefik_host }}"
              - "gluetun2.{{ user.domain }}"
              - "gluetun.otherdomain.tld"
            ```
            
            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries
            

        2.  Example:

            ```yaml
            gluetun_role_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'gluetun2.' + user.domain }}`)"
            ```
            
            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule
            

    === "Instance-level"

        Override for a specific instance (e.g., `gluetun2`):

        ```yaml
        # Enable or disable Autoheal monitoring for the container created when deploying
        # Type: bool (true/false)
        gluetun2_autoheal_enabled: true

        # List of container dependencies that must be running before the container start
        # Type: string
        gluetun2_depends_on: ""

        # Delay in seconds before starting the container after dependencies are ready
        # Type: string (quoted number)
        gluetun2_depends_on_delay: "0"

        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        gluetun2_depends_on_healthchecks:

        # Enable or disable Diun update notifications for the container created when deploying
        # Type: bool (true/false)
        gluetun2_diun_enabled: true

        # Enable or disable automatic DNS record creation for the container
        # Type: bool (true/false)
        gluetun2_dns_enabled: true

        # Enable or disable Saltbox Docker Controller management for the container
        # Type: bool (true/false)
        gluetun2_docker_controller: true

        # Enable Traefik autodetect middleware for the container
        # Type: bool (true/false)
        gluetun2_traefik_autodetect_enabled: false

        # Enable CrowdSec middleware for the container
        # Type: bool (true/false)
        gluetun2_traefik_crowdsec_enabled: false

        # Enable custom error pages middleware for the container
        # Type: bool (true/false)
        gluetun2_traefik_error_pages_enabled: false

        # Enable gzip compression middleware for the container
        # Type: bool (true/false)
        gluetun2_traefik_gzip_enabled: false

        # Enable robots.txt middleware for the container
        # Type: bool (true/false)
        gluetun2_traefik_robot_enabled: true

        # Enable Tailscale-specific Traefik configuration for the container
        # Type: bool (true/false)
        gluetun2_traefik_tailscale_enabled: false

        # Enable wildcard certificate for the container
        # Type: bool (true/false)
        gluetun2_traefik_wildcard_enabled: true

        # Override the Traefik fully qualified domain name (FQDN) for the container
        # Type: list
        gluetun2_web_fqdn_override: # (1)!

        # Override the Traefik web host configuration for the container
        # Type: string
        gluetun2_web_host_override: # (2)!

        # URL scheme to use for web access to the container
        # Type: string ("http"/"https")
        gluetun2_web_scheme:

        ```

        1.  Example:

            ```yaml
            gluetun2_web_fqdn_override:
              - "{{ traefik_host }}"
              - "gluetun2.{{ user.domain }}"
              - "gluetun.otherdomain.tld"
            ```
            
            Note: Include `{{ traefik_host }}` to preserve the default FQDN alongside your custom entries
            

        2.  Example:

            ```yaml
            gluetun2_web_host_override: "Host(`{{ traefik_host }}`) || Host(`{{ 'gluetun2.' + user.domain }}`)"
            ```
            
            Note: Use `{{ traefik_host }}` to include the default host configuration in your custom rule
            

<!-- END SALTBOX MANAGED VARIABLES SECTION -->

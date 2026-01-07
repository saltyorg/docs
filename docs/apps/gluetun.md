---
icon: material/docker
hide:
  - tags
tags:
  - gluetun
---

# Gluetun

## Overview

[Gluetun](https://github.com/qdm12/gluetun) is a VPN client in a thin Docker container for multiple VPN providers, written in Go, and using OpenVPN or Wireguard, DNS over TLS, with a few proxy servers built-in.

<div class="grid grid--buttons" markdown data-search-exclude>

[:material-bookshelf:**Manual**](https://github.com/qdm12/gluetun-wiki){ .md-button .md-button--stretch }

[:fontawesome-brands-docker:**Releases**](https://hub.docker.com/r/qmcgaw/gluetun/tags){ .md-button .md-button--stretch }

[:fontawesome-solid-people-group:**Community**](){ .md-button .md-button--stretch }

</div>

---

## Configuration

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

    Generally speaking it's safest to just wrap everything in quotes rather than worrying about what needs to be. Quotes are plentiful and free.

Additional Docker envs may be set via `gluetun_docker_envs_custom`.

### Route Plex through Gluetun

!!! caution
    It is important to disable remote access in Plex when using this workaround to avoid having media traffic routed through the VPN. Multiple instances of Plex will need their own unique instance of gluetun due to port conflicts.

To route Plex via your Gluetun container, you must set the following via the inventory system. These settings will also DNS block the metrics servers and use Gluetun's HTTP proxy when connecting with the Plex API for Saltbox tasks such as generating auth tokens:

```yaml
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

Once you have made these changes to the inventory, run the plex tag to apply the changes (i.e. `sb install plex`). This will update all your plex containers.

!!! caution
    When routing Plex through Gluetun, you must access Plex between containers at `http://gluetun:32400` where you would previously use the Plex container name.

    The above note is only the case if you do not add each linked container alias to gluetun like in the config example above.

    Additionally the Plex container will become unable to start if you redeploy gluetun (restart is fine) at any point so you must redeploy Plex in that case.

### Route other containers through Gluetun

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

Once you have made these changes to the inventory, run the relevant tags to apply the changes (i.e. `sb install qbittorrent` or `sb install jackett,sonarr,radarr`).

!!! caution
    While multiple containers may be routed through a single Gluetun instance, you must manually ensure there are no port clashes as all port binds for the connected containers will be through the Gluetun container and must have unique ports inside that container.

### Example Gluetun Configs

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

## Deployment

```shell
sb install gluetun
```

## Usage

To verify VPN connectivity, inspect the container's IP address:

```shell
docker exec gluetun curl ifconfig.me
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by sb-docs - DO NOT EDIT MANUALLY -->
## Role Defaults<label class="sb-toggle--override-scope md-annotation__index" title="Supports multiple instances! Click to toggle override level"><input type="checkbox" name="scope" hidden/></label>

Use the [Inventory](/saltbox/inventory/index.md#overriding-variables){ data-preview } to customize variables. <span title="View override specifics for this role" markdown>(1)</span>
{ .annotate .sb-annotated }

1.  **This role supports multiple instances via `gluetun_instances`.**

    !!! example "Example override"

        === "Role-level"

            ```yaml
            gluetun_role_web_subdomain: "custom"
            ```

            :material-arrow-right-bottom-bold: Applies to all instances of gluetun

        === "Instance-level"

            ```yaml
            gluetun2_web_subdomain: "custom2"
            ```

            :material-arrow-right-bottom-bold: Applies to the instance named gluetun2

    !!! warning "Avoid overriding variables ending in `_default`"

        When overriding variables that end in `_default` (like `gluetun_docker_envs_default`), you replace the entire default configuration. Future updates that add new default values will not be applied to your setup, potentially breaking functionality.

        Instead, use the corresponding `_custom` variable (like `gluetun_docker_envs_custom`) to add your changes. Custom values are merged with defaults, ensuring you receive updates.

=== "Basics"

    ??? variable list "`gluetun_instances`"

        ```yaml
        # Type: list
        gluetun_instances: ["gluetun"]
        ```

        !!! example "Example Override"

            ```yaml
            # Type: list
            gluetun_instances: ["gluetun", "gluetun2"]
            ```

=== "Settings"

    This section is organized into multiple subsections

    === "VPN"

        ??? variable string "`gluetun_role_vpn_service_provider`{ .sb-show-on-unchecked }`gluetun2_vpn_service_provider`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # VPN service provider (e.g., mullvad, nordvpn, private internet access, etc.)
            # Type: string
            gluetun_role_vpn_service_provider: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # VPN service provider (e.g., mullvad, nordvpn, private internet access, etc.)
            # Type: string
            gluetun2_vpn_service_provider: ""
            ```

        ??? variable string "`gluetun_role_vpn_type`{ .sb-show-on-unchecked }`gluetun2_vpn_type`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # VPN type: openvpn or wireguard
            # Type: string
            gluetun_role_vpn_type: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # VPN type: openvpn or wireguard
            # Type: string
            gluetun2_vpn_type: ""
            ```

        ??? variable string "`gluetun_role_vpn_interface`{ .sb-show-on-unchecked }`gluetun2_vpn_interface`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Network interface name for the VPN tunnel (e.g., tun0, wg0)
            # Type: string
            gluetun_role_vpn_interface: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Network interface name for the VPN tunnel (e.g., tun0, wg0)
            # Type: string
            gluetun2_vpn_interface: ""
            ```

        ??? variable string "`gluetun_role_vpn_endpoint_ip`{ .sb-show-on-unchecked }`gluetun2_vpn_endpoint_ip`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # VPN server endpoint IP address (optional override)
            # Type: string
            gluetun_role_vpn_endpoint_ip: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # VPN server endpoint IP address (optional override)
            # Type: string
            gluetun2_vpn_endpoint_ip: ""
            ```

        ??? variable string "`gluetun_role_vpn_endpoint_port`{ .sb-show-on-unchecked }`gluetun2_vpn_endpoint_port`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # VPN server endpoint port (optional override)
            # Type: string
            gluetun_role_vpn_endpoint_port: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # VPN server endpoint port (optional override)
            # Type: string
            gluetun2_vpn_endpoint_port: ""
            ```

    === "OpenVPN"

        ??? variable string "`gluetun_role_openvpn_user`{ .sb-show-on-unchecked }`gluetun2_openvpn_user`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN username for authentication
            # Type: string
            gluetun_role_openvpn_user: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN username for authentication
            # Type: string
            gluetun2_openvpn_user: ""
            ```

        ??? variable string "`gluetun_role_openvpn_password`{ .sb-show-on-unchecked }`gluetun2_openvpn_password`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN password for authentication
            # Type: string
            gluetun_role_openvpn_password: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN password for authentication
            # Type: string
            gluetun2_openvpn_password: ""
            ```

        ??? variable string "`gluetun_role_openvpn_protocol`{ .sb-show-on-unchecked }`gluetun2_openvpn_protocol`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN protocol: udp or tcp
            # Type: string
            gluetun_role_openvpn_protocol: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN protocol: udp or tcp
            # Type: string
            gluetun2_openvpn_protocol: ""
            ```

        ??? variable string "`gluetun_role_openvpn_endpoint_ip`{ .sb-show-on-unchecked }`gluetun2_openvpn_endpoint_ip`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN server endpoint IP (optional override)
            # Type: string
            gluetun_role_openvpn_endpoint_ip: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN server endpoint IP (optional override)
            # Type: string
            gluetun2_openvpn_endpoint_ip: ""
            ```

        ??? variable string "`gluetun_role_openvpn_endpoint_port`{ .sb-show-on-unchecked }`gluetun2_openvpn_endpoint_port`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN server endpoint port (optional override)
            # Type: string
            gluetun_role_openvpn_endpoint_port: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN server endpoint port (optional override)
            # Type: string
            gluetun2_openvpn_endpoint_port: ""
            ```

        ??? variable string "`gluetun_role_openvpn_version`{ .sb-show-on-unchecked }`gluetun2_openvpn_version`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN version: 2.5 or 2.6
            # Type: string
            gluetun_role_openvpn_version: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN version: 2.5 or 2.6
            # Type: string
            gluetun2_openvpn_version: ""
            ```

        ??? variable string "`gluetun_role_openvpn_verbosity`{ .sb-show-on-unchecked }`gluetun2_openvpn_verbosity`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN verbosity level (0-6)
            # Type: string
            gluetun_role_openvpn_verbosity: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN verbosity level (0-6)
            # Type: string
            gluetun2_openvpn_verbosity: ""
            ```

        ??? variable string "`gluetun_role_openvpn_flags`{ .sb-show-on-unchecked }`gluetun2_openvpn_flags`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # Additional OpenVPN flags to pass to the openvpn command
            # Type: string
            gluetun_role_openvpn_flags: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # Additional OpenVPN flags to pass to the openvpn command
            # Type: string
            gluetun2_openvpn_flags: ""
            ```

        ??? variable string "`gluetun_role_openvpn_ciphers`{ .sb-show-on-unchecked }`gluetun2_openvpn_ciphers`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # Comma-separated list of ciphers to use
            # Type: string
            gluetun_role_openvpn_ciphers: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # Comma-separated list of ciphers to use
            # Type: string
            gluetun2_openvpn_ciphers: ""
            ```

        ??? variable string "`gluetun_role_openvpn_auth`{ .sb-show-on-unchecked }`gluetun2_openvpn_auth`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN auth algorithm (e.g., sha256, sha512)
            # Type: string
            gluetun_role_openvpn_auth: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN auth algorithm (e.g., sha256, sha512)
            # Type: string
            gluetun2_openvpn_auth: ""
            ```

        ??? variable string "`gluetun_role_openvpn_process_user`{ .sb-show-on-unchecked }`gluetun2_openvpn_process_user`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # User to run OpenVPN process as (e.g., root, nonroot)
            # Type: string
            gluetun_role_openvpn_process_user: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # User to run OpenVPN process as (e.g., root, nonroot)
            # Type: string
            gluetun2_openvpn_process_user: ""
            ```

        ??? variable string "`gluetun_role_openvpn_mssfix`{ .sb-show-on-unchecked }`gluetun2_openvpn_mssfix`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN MSS fix value
            # Type: string
            gluetun_role_openvpn_mssfix: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN MSS fix value
            # Type: string
            gluetun2_openvpn_mssfix: ""
            ```

        ??? variable string "`gluetun_role_openvpn_custom_config`{ .sb-show-on-unchecked }`gluetun2_openvpn_custom_config`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # Path to custom OpenVPN configuration file
            # Type: string
            gluetun_role_openvpn_custom_config: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # Path to custom OpenVPN configuration file
            # Type: string
            gluetun2_openvpn_custom_config: ""
            ```

        ??? variable string "`gluetun_role_openvpn_cert`{ .sb-show-on-unchecked }`gluetun2_openvpn_cert`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN client certificate (base64 or path)
            # Type: string
            gluetun_role_openvpn_cert: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN client certificate (base64 or path)
            # Type: string
            gluetun2_openvpn_cert: ""
            ```

        ??? variable string "`gluetun_role_openvpn_key`{ .sb-show-on-unchecked }`gluetun2_openvpn_key`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN client private key (base64 or path)
            # Type: string
            gluetun_role_openvpn_key: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # OpenVPN client private key (base64 or path)
            # Type: string
            gluetun2_openvpn_key: ""
            ```

        ??? variable string "`gluetun_role_openvpn_encrypted_key`{ .sb-show-on-unchecked }`gluetun2_openvpn_encrypted_key`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # Set to "yes" if the OpenVPN key is encrypted
            # Type: string
            gluetun_role_openvpn_encrypted_key: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # Set to "yes" if the OpenVPN key is encrypted
            # Type: string
            gluetun2_openvpn_encrypted_key: ""
            ```

        ??? variable string "`gluetun_role_openvpn_key_passphrase`{ .sb-show-on-unchecked }`gluetun2_openvpn_key_passphrase`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # Passphrase to decrypt the OpenVPN key
            # Type: string
            gluetun_role_openvpn_key_passphrase: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/openvpn.md
            # Passphrase to decrypt the OpenVPN key
            # Type: string
            gluetun2_openvpn_key_passphrase: ""
            ```

    === "WireGuard"

        ??? variable string "`gluetun_role_wireguard_private_key`{ .sb-show-on-unchecked }`gluetun2_wireguard_private_key`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # WireGuard client private key
            # Type: string
            gluetun_role_wireguard_private_key: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # WireGuard client private key
            # Type: string
            gluetun2_wireguard_private_key: ""
            ```

        ??? variable string "`gluetun_role_wireguard_preshared_key`{ .sb-show-on-unchecked }`gluetun2_wireguard_preshared_key`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # WireGuard preshared key for additional security
            # Type: string
            gluetun_role_wireguard_preshared_key: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # WireGuard preshared key for additional security
            # Type: string
            gluetun2_wireguard_preshared_key: ""
            ```

        ??? variable string "`gluetun_role_wireguard_public_key`{ .sb-show-on-unchecked }`gluetun2_wireguard_public_key`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # WireGuard server public key
            # Type: string
            gluetun_role_wireguard_public_key: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # WireGuard server public key
            # Type: string
            gluetun2_wireguard_public_key: ""
            ```

        ??? variable string "`gluetun_role_wireguard_addresses`{ .sb-show-on-unchecked }`gluetun2_wireguard_addresses`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # Comma-separated list of IP addresses for the WireGuard interface
            # Type: string
            gluetun_role_wireguard_addresses: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # Comma-separated list of IP addresses for the WireGuard interface
            # Type: string
            gluetun2_wireguard_addresses: ""
            ```

        ??? variable string "`gluetun_role_wireguard_allowed_ips`{ .sb-show-on-unchecked }`gluetun2_wireguard_allowed_ips`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # Comma-separated list of allowed IP ranges
            # Type: string
            gluetun_role_wireguard_allowed_ips: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # Comma-separated list of allowed IP ranges
            # Type: string
            gluetun2_wireguard_allowed_ips: ""
            ```

        ??? variable string "`gluetun_role_wireguard_endpoint_ip`{ .sb-show-on-unchecked }`gluetun2_wireguard_endpoint_ip`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # WireGuard server endpoint IP (optional override)
            # Type: string
            gluetun_role_wireguard_endpoint_ip: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # WireGuard server endpoint IP (optional override)
            # Type: string
            gluetun2_wireguard_endpoint_ip: ""
            ```

        ??? variable string "`gluetun_role_wireguard_endpoint_port`{ .sb-show-on-unchecked }`gluetun2_wireguard_endpoint_port`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # WireGuard server endpoint port (optional override)
            # Type: string
            gluetun_role_wireguard_endpoint_port: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # WireGuard server endpoint port (optional override)
            # Type: string
            gluetun2_wireguard_endpoint_port: ""
            ```

        ??? variable string "`gluetun_role_wireguard_mtu`{ .sb-show-on-unchecked }`gluetun2_wireguard_mtu`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # WireGuard MTU value
            # Type: string
            gluetun_role_wireguard_mtu: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # WireGuard MTU value
            # Type: string
            gluetun2_wireguard_mtu: ""
            ```

        ??? variable string "`gluetun_role_wireguard_implementation`{ .sb-show-on-unchecked }`gluetun2_wireguard_implementation`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # WireGuard implementation: kernelspace or userspace
            # Type: string
            gluetun_role_wireguard_implementation: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # WireGuard implementation: kernelspace or userspace
            # Type: string
            gluetun2_wireguard_implementation: ""
            ```

        ??? variable string "`gluetun_role_wireguard_persistent_keepalive_interval`{ .sb-show-on-unchecked }`gluetun2_wireguard_persistent_keepalive_interval`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # WireGuard persistent keepalive interval (e.g., 25s)
            # Type: string
            gluetun_role_wireguard_persistent_keepalive_interval: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/wireguard.md
            # WireGuard persistent keepalive interval (e.g., 25s)
            # Type: string
            gluetun2_wireguard_persistent_keepalive_interval: ""
            ```

    === "Server Selection"

        ??? variable string "`gluetun_role_server_regions`{ .sb-show-on-unchecked }`gluetun2_server_regions`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Comma-separated list of server regions
            # Type: string
            gluetun_role_server_regions: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Comma-separated list of server regions
            # Type: string
            gluetun2_server_regions: ""
            ```

        ??? variable string "`gluetun_role_server_countries`{ .sb-show-on-unchecked }`gluetun2_server_countries`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Comma-separated list of server countries
            # Type: string
            gluetun_role_server_countries: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Comma-separated list of server countries
            # Type: string
            gluetun2_server_countries: ""
            ```

        ??? variable string "`gluetun_role_server_cities`{ .sb-show-on-unchecked }`gluetun2_server_cities`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Comma-separated list of server cities
            # Type: string
            gluetun_role_server_cities: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Comma-separated list of server cities
            # Type: string
            gluetun2_server_cities: ""
            ```

        ??? variable string "`gluetun_role_server_hostnames`{ .sb-show-on-unchecked }`gluetun2_server_hostnames`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Comma-separated list of server hostnames
            # Type: string
            gluetun_role_server_hostnames: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Comma-separated list of server hostnames
            # Type: string
            gluetun2_server_hostnames: ""
            ```

        ??? variable string "`gluetun_role_server_names`{ .sb-show-on-unchecked }`gluetun2_server_names`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Comma-separated list of server names
            # Type: string
            gluetun_role_server_names: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Comma-separated list of server names
            # Type: string
            gluetun2_server_names: ""
            ```

        ??? variable string "`gluetun_role_server_categories`{ .sb-show-on-unchecked }`gluetun2_server_categories`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Comma-separated list of server categories
            # Type: string
            gluetun_role_server_categories: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Comma-separated list of server categories
            # Type: string
            gluetun2_server_categories: ""
            ```

        ??? variable string "`gluetun_role_server_number`{ .sb-show-on-unchecked }`gluetun2_server_number`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Server number (provider-specific)
            # Type: string
            gluetun_role_server_number: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Server number (provider-specific)
            # Type: string
            gluetun2_server_number: ""
            ```

        ??? variable string "`gluetun_role_isp`{ .sb-show-on-unchecked }`gluetun2_isp`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Filter by ISP name
            # Type: string
            gluetun_role_isp: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Filter by ISP name
            # Type: string
            gluetun2_isp: ""
            ```

        ??? variable string "`gluetun_role_owned_only`{ .sb-show-on-unchecked }`gluetun2_owned_only`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Only use servers owned by the VPN provider (on/off)
            # Type: string
            gluetun_role_owned_only: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Only use servers owned by the VPN provider (on/off)
            # Type: string
            gluetun2_owned_only: ""
            ```

        ??? variable string "`gluetun_role_stream_only`{ .sb-show-on-unchecked }`gluetun2_stream_only`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Only use servers optimized for streaming (on/off)
            # Type: string
            gluetun_role_stream_only: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Only use servers optimized for streaming (on/off)
            # Type: string
            gluetun2_stream_only: ""
            ```

        ??? variable string "`gluetun_role_free_only`{ .sb-show-on-unchecked }`gluetun2_free_only`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Only use free tier servers (on/off)
            # Type: string
            gluetun_role_free_only: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Only use free tier servers (on/off)
            # Type: string
            gluetun2_free_only: ""
            ```

        ??? variable string "`gluetun_role_premium_only`{ .sb-show-on-unchecked }`gluetun2_premium_only`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Only use premium tier servers (on/off)
            # Type: string
            gluetun_role_premium_only: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Only use premium tier servers (on/off)
            # Type: string
            gluetun2_premium_only: ""
            ```

        ??? variable string "`gluetun_role_secure_core_only`{ .sb-show-on-unchecked }`gluetun2_secure_core_only`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Only use Secure Core servers - ProtonVPN (on/off)
            # Type: string
            gluetun_role_secure_core_only: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Only use Secure Core servers - ProtonVPN (on/off)
            # Type: string
            gluetun2_secure_core_only: ""
            ```

        ??? variable string "`gluetun_role_tor_only`{ .sb-show-on-unchecked }`gluetun2_tor_only`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Only use Tor-enabled servers (on/off)
            # Type: string
            gluetun_role_tor_only: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Only use Tor-enabled servers (on/off)
            # Type: string
            gluetun2_tor_only: ""
            ```

        ??? variable string "`gluetun_role_multihop_only`{ .sb-show-on-unchecked }`gluetun2_multihop_only`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Only use multi-hop servers (on/off)
            # Type: string
            gluetun_role_multihop_only: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Only use multi-hop servers (on/off)
            # Type: string
            gluetun2_multihop_only: ""
            ```

        ??? variable string "`gluetun_role_port_forward_only`{ .sb-show-on-unchecked }`gluetun2_port_forward_only`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Only use servers that support port forwarding (on/off)
            # Type: string
            gluetun_role_port_forward_only: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/vpn-server-selection.md
            # Only use servers that support port forwarding (on/off)
            # Type: string
            gluetun2_port_forward_only: ""
            ```

    === "Firewall"

        ??? variable string "`gluetun_role_firewall_vpn_input_ports`{ .sb-show-on-unchecked }`gluetun2_firewall_vpn_input_ports`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/firewall.md
            # Comma-separated list of ports to allow through the VPN firewall
            # Type: string
            gluetun_role_firewall_vpn_input_ports: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/firewall.md
            # Comma-separated list of ports to allow through the VPN firewall
            # Type: string
            gluetun2_firewall_vpn_input_ports: ""
            ```

        ??? variable string "`gluetun_role_firewall_input_ports`{ .sb-show-on-unchecked }`gluetun2_firewall_input_ports`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/firewall.md
            # Comma-separated list of ports to allow on the host side
            # Type: string
            gluetun_role_firewall_input_ports: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/firewall.md
            # Comma-separated list of ports to allow on the host side
            # Type: string
            gluetun2_firewall_input_ports: ""
            ```

        ??? variable string "`gluetun_role_firewall_outbound_subnets`{ .sb-show-on-unchecked }`gluetun2_firewall_outbound_subnets`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/firewall.md
            # Comma-separated list of subnets to allow outbound traffic to
            # Type: string
            gluetun_role_firewall_outbound_subnets: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/firewall.md
            # Comma-separated list of subnets to allow outbound traffic to
            # Type: string
            gluetun2_firewall_outbound_subnets: ""
            ```

        ??? variable string "`gluetun_role_firewall_debug`{ .sb-show-on-unchecked }`gluetun2_firewall_debug`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/firewall.md
            # Enable firewall debug logging (on/off)
            # Type: string
            gluetun_role_firewall_debug: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/firewall.md
            # Enable firewall debug logging (on/off)
            # Type: string
            gluetun2_firewall_debug: ""
            ```

    === "DNS"

        ??? variable string "`gluetun_role_dns_server`{ .sb-show-on-unchecked }`gluetun2_dns_server`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # DNS server type: local or remote
            # Type: string
            gluetun_role_dns_server: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # DNS server type: local or remote
            # Type: string
            gluetun2_dns_server: ""
            ```

        ??? variable string "`gluetun_role_dns_upstream_resolver_type`{ .sb-show-on-unchecked }`gluetun2_dns_upstream_resolver_type`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Upstream resolver type: dot, doh, or plaintext
            # Type: string
            gluetun_role_dns_upstream_resolver_type: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Upstream resolver type: dot, doh, or plaintext
            # Type: string
            gluetun2_dns_upstream_resolver_type: ""
            ```

        ??? variable string "`gluetun_role_dns_upstream_resolvers`{ .sb-show-on-unchecked }`gluetun2_dns_upstream_resolvers`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Comma-separated list of upstream DNS resolvers
            # Type: string
            gluetun_role_dns_upstream_resolvers: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Comma-separated list of upstream DNS resolvers
            # Type: string
            gluetun2_dns_upstream_resolvers: ""
            ```

        ??? variable string "`gluetun_role_dns_caching`{ .sb-show-on-unchecked }`gluetun2_dns_caching`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Enable DNS caching (on/off)
            # Type: string
            gluetun_role_dns_caching: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Enable DNS caching (on/off)
            # Type: string
            gluetun2_dns_caching: ""
            ```

        ??? variable string "`gluetun_role_dns_upstream_ipv6`{ .sb-show-on-unchecked }`gluetun2_dns_upstream_ipv6`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Allow IPv6 DNS queries (on/off)
            # Type: string
            gluetun_role_dns_upstream_ipv6: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Allow IPv6 DNS queries (on/off)
            # Type: string
            gluetun2_dns_upstream_ipv6: ""
            ```

        ??? variable string "`gluetun_role_dns_block_ips`{ .sb-show-on-unchecked }`gluetun2_dns_block_ips`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Comma-separated list of IPs to block in DNS responses
            # Type: string
            gluetun_role_dns_block_ips: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Comma-separated list of IPs to block in DNS responses
            # Type: string
            gluetun2_dns_block_ips: ""
            ```

        ??? variable string "`gluetun_role_dns_block_ip_prefixes`{ .sb-show-on-unchecked }`gluetun2_dns_block_ip_prefixes`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Comma-separated list of IP prefixes to block in DNS responses
            # Type: string
            gluetun_role_dns_block_ip_prefixes: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Comma-separated list of IP prefixes to block in DNS responses
            # Type: string
            gluetun2_dns_block_ip_prefixes: ""
            ```

        ??? variable string "`gluetun_role_block_malicious`{ .sb-show-on-unchecked }`gluetun2_block_malicious`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Block malicious domains (on/off)
            # Type: string
            gluetun_role_block_malicious: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Block malicious domains (on/off)
            # Type: string
            gluetun2_block_malicious: ""
            ```

        ??? variable string "`gluetun_role_block_surveillance`{ .sb-show-on-unchecked }`gluetun2_block_surveillance`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Block surveillance domains (on/off)
            # Type: string
            gluetun_role_block_surveillance: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Block surveillance domains (on/off)
            # Type: string
            gluetun2_block_surveillance: ""
            ```

        ??? variable string "`gluetun_role_block_ads`{ .sb-show-on-unchecked }`gluetun2_block_ads`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Block ads domains (on/off)
            # Type: string
            gluetun_role_block_ads: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Block ads domains (on/off)
            # Type: string
            gluetun2_block_ads: ""
            ```

        ??? variable string "`gluetun_role_dns_unblock_hostnames`{ .sb-show-on-unchecked }`gluetun2_dns_unblock_hostnames`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Comma-separated list of hostnames to unblock
            # Type: string
            gluetun_role_dns_unblock_hostnames: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Comma-separated list of hostnames to unblock
            # Type: string
            gluetun2_dns_unblock_hostnames: ""
            ```

        ??? variable string "`gluetun_role_dns_rebinding_protection_exempt_hostnames`{ .sb-show-on-unchecked }`gluetun2_dns_rebinding_protection_exempt_hostnames`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Comma-separated list of hostnames exempt from DNS rebinding protection
            # Type: string
            gluetun_role_dns_rebinding_protection_exempt_hostnames: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Comma-separated list of hostnames exempt from DNS rebinding protection
            # Type: string
            gluetun2_dns_rebinding_protection_exempt_hostnames: ""
            ```

        ??? variable string "`gluetun_role_dns_private_addresses`{ .sb-show-on-unchecked }`gluetun2_dns_private_addresses`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Comma-separated list of private address ranges for DNS
            # Type: string
            gluetun_role_dns_private_addresses: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Comma-separated list of private address ranges for DNS
            # Type: string
            gluetun2_dns_private_addresses: ""
            ```

        ??? variable string "`gluetun_role_dns_update_period`{ .sb-show-on-unchecked }`gluetun2_dns_update_period`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # DNS blocklists update period (e.g., 24h)
            # Type: string
            gluetun_role_dns_update_period: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # DNS blocklists update period (e.g., 24h)
            # Type: string
            gluetun2_dns_update_period: ""
            ```

        ??? variable string "`gluetun_role_dns_address`{ .sb-show-on-unchecked }`gluetun2_dns_address`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Address for DNS server to listen on (e.g., 127.0.0.1:53)
            # Type: string
            gluetun_role_dns_address: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Address for DNS server to listen on (e.g., 127.0.0.1:53)
            # Type: string
            gluetun2_dns_address: ""
            ```

        ??? variable bool "`gluetun_role_docker_resolver`{ .sb-show-on-unchecked }`gluetun2_docker_resolver`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Keep original nameserver - deprecated in v3.41+, Saltbox default: false
            # Type: bool (true/false)
            gluetun_role_docker_resolver: false
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/dns.md
            # Keep original nameserver - deprecated in v3.41+, Saltbox default: false
            # Type: bool (true/false)
            gluetun2_docker_resolver: false
            ```

    === "Health"

        ??? variable string "`gluetun_role_health_server_address`{ .sb-show-on-unchecked }`gluetun2_health_server_address`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/faq/healthcheck.md
            # Address for the health server to listen on
            # Type: string
            gluetun_role_health_server_address: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/faq/healthcheck.md
            # Address for the health server to listen on
            # Type: string
            gluetun2_health_server_address: ""
            ```

        ??? variable string "`gluetun_role_health_target_addresses`{ .sb-show-on-unchecked }`gluetun2_health_target_addresses`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/faq/healthcheck.md
            # Comma-separated list of addresses to check for health
            # Type: string
            gluetun_role_health_target_addresses: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/faq/healthcheck.md
            # Comma-separated list of addresses to check for health
            # Type: string
            gluetun2_health_target_addresses: ""
            ```

        ??? variable string "`gluetun_role_health_icmp_target_ips`{ .sb-show-on-unchecked }`gluetun2_health_icmp_target_ips`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/faq/healthcheck.md
            # Comma-separated list of IP addresses for ICMP health checks
            # Type: string
            gluetun_role_health_icmp_target_ips: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/faq/healthcheck.md
            # Comma-separated list of IP addresses for ICMP health checks
            # Type: string
            gluetun2_health_icmp_target_ips: ""
            ```

        ??? variable string "`gluetun_role_health_small_check_type`{ .sb-show-on-unchecked }`gluetun2_health_small_check_type`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/faq/healthcheck.md
            # Type of small health check: ping or http
            # Type: string
            gluetun_role_health_small_check_type: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/faq/healthcheck.md
            # Type of small health check: ping or http
            # Type: string
            gluetun2_health_small_check_type: ""
            ```

        ??? variable string "`gluetun_role_health_restart_vpn`{ .sb-show-on-unchecked }`gluetun2_health_restart_vpn`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/faq/healthcheck.md
            # Restart VPN when unhealthy (on/off)
            # Type: string
            gluetun_role_health_restart_vpn: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/faq/healthcheck.md
            # Restart VPN when unhealthy (on/off)
            # Type: string
            gluetun2_health_restart_vpn: ""
            ```

    === "HTTP Proxy"

        ??? variable string "`gluetun_role_httpproxy`{ .sb-show-on-unchecked }`gluetun2_httpproxy`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/http-proxy.md
            # Enable HTTP proxy (on/off)
            # Type: string
            gluetun_role_httpproxy: "on"
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/http-proxy.md
            # Enable HTTP proxy (on/off)
            # Type: string
            gluetun2_httpproxy: "on"
            ```

        ??? variable string "`gluetun_role_httpproxy_stealth`{ .sb-show-on-unchecked }`gluetun2_httpproxy_stealth`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/http-proxy.md
            # Enable stealth mode for HTTP proxy (on/off)
            # Type: string
            gluetun_role_httpproxy_stealth: "on"
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/http-proxy.md
            # Enable stealth mode for HTTP proxy (on/off)
            # Type: string
            gluetun2_httpproxy_stealth: "on"
            ```

        ??? variable string "`gluetun_role_httpproxy_log`{ .sb-show-on-unchecked }`gluetun2_httpproxy_log`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/http-proxy.md
            # Enable HTTP proxy logging (on/off)
            # Type: string
            gluetun_role_httpproxy_log: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/http-proxy.md
            # Enable HTTP proxy logging (on/off)
            # Type: string
            gluetun2_httpproxy_log: ""
            ```

        ??? variable string "`gluetun_role_httpproxy_listening_address`{ .sb-show-on-unchecked }`gluetun2_httpproxy_listening_address`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/http-proxy.md
            # Address for HTTP proxy to listen on (e.g., :8888)
            # Type: string
            gluetun_role_httpproxy_listening_address: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/http-proxy.md
            # Address for HTTP proxy to listen on (e.g., :8888)
            # Type: string
            gluetun2_httpproxy_listening_address: ""
            ```

        ??? variable string "`gluetun_role_httpproxy_user`{ .sb-show-on-unchecked }`gluetun2_httpproxy_user`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/http-proxy.md
            # HTTP proxy authentication username
            # Type: string
            gluetun_role_httpproxy_user: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/http-proxy.md
            # HTTP proxy authentication username
            # Type: string
            gluetun2_httpproxy_user: ""
            ```

        ??? variable string "`gluetun_role_httpproxy_password`{ .sb-show-on-unchecked }`gluetun2_httpproxy_password`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/http-proxy.md
            # HTTP proxy authentication password
            # Type: string
            gluetun_role_httpproxy_password: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/http-proxy.md
            # HTTP proxy authentication password
            # Type: string
            gluetun2_httpproxy_password: ""
            ```

    === "Shadowsocks"

        ??? variable string "`gluetun_role_shadowsocks`{ .sb-show-on-unchecked }`gluetun2_shadowsocks`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/shadowsocks.md
            # Enable Shadowsocks server (on/off)
            # Type: string
            gluetun_role_shadowsocks: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/shadowsocks.md
            # Enable Shadowsocks server (on/off)
            # Type: string
            gluetun2_shadowsocks: ""
            ```

        ??? variable string "`gluetun_role_shadowsocks_log`{ .sb-show-on-unchecked }`gluetun2_shadowsocks_log`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/shadowsocks.md
            # Enable Shadowsocks logging (on/off)
            # Type: string
            gluetun_role_shadowsocks_log: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/shadowsocks.md
            # Enable Shadowsocks logging (on/off)
            # Type: string
            gluetun2_shadowsocks_log: ""
            ```

        ??? variable string "`gluetun_role_shadowsocks_listening_address`{ .sb-show-on-unchecked }`gluetun2_shadowsocks_listening_address`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/shadowsocks.md
            # Address for Shadowsocks to listen on (e.g., :8388)
            # Type: string
            gluetun_role_shadowsocks_listening_address: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/shadowsocks.md
            # Address for Shadowsocks to listen on (e.g., :8388)
            # Type: string
            gluetun2_shadowsocks_listening_address: ""
            ```

        ??? variable string "`gluetun_role_shadowsocks_password`{ .sb-show-on-unchecked }`gluetun2_shadowsocks_password`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/shadowsocks.md
            # Shadowsocks password for authentication
            # Type: string
            gluetun_role_shadowsocks_password: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/shadowsocks.md
            # Shadowsocks password for authentication
            # Type: string
            gluetun2_shadowsocks_password: ""
            ```

        ??? variable string "`gluetun_role_shadowsocks_cipher`{ .sb-show-on-unchecked }`gluetun2_shadowsocks_cipher`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/shadowsocks.md
            # Shadowsocks cipher (e.g., chacha20-ietf-poly1305)
            # Type: string
            gluetun_role_shadowsocks_cipher: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/shadowsocks.md
            # Shadowsocks cipher (e.g., chacha20-ietf-poly1305)
            # Type: string
            gluetun2_shadowsocks_cipher: ""
            ```

    === "Control Server"

        ??? variable string "`gluetun_role_http_control_server_log`{ .sb-show-on-unchecked }`gluetun2_http_control_server_log`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/control-server.md
            # Enable control server logging (on/off)
            # Type: string
            gluetun_role_http_control_server_log: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/control-server.md
            # Enable control server logging (on/off)
            # Type: string
            gluetun2_http_control_server_log: ""
            ```

        ??? variable string "`gluetun_role_http_control_server_address`{ .sb-show-on-unchecked }`gluetun2_http_control_server_address`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/control-server.md
            # Address for control server to listen on (e.g., :8000)
            # Type: string
            gluetun_role_http_control_server_address: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/control-server.md
            # Address for control server to listen on (e.g., :8000)
            # Type: string
            gluetun2_http_control_server_address: ""
            ```

        ??? variable string "`gluetun_role_http_control_server_auth_config_filepath`{ .sb-show-on-unchecked }`gluetun2_http_control_server_auth_config_filepath`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/control-server.md
            # Path to auth config file for control server
            # Type: string
            gluetun_role_http_control_server_auth_config_filepath: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/control-server.md
            # Path to auth config file for control server
            # Type: string
            gluetun2_http_control_server_auth_config_filepath: ""
            ```

        ??? variable string "`gluetun_role_http_control_server_auth_default_role`{ .sb-show-on-unchecked }`gluetun2_http_control_server_auth_default_role`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/control-server.md
            # Default role for control server auth (admin/viewer/none)
            # Type: string
            gluetun_role_http_control_server_auth_default_role: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/control-server.md
            # Default role for control server auth (admin/viewer/none)
            # Type: string
            gluetun2_http_control_server_auth_default_role: ""
            ```

    === "Port Forwarding"

        ??? variable string "`gluetun_role_vpn_port_forwarding`{ .sb-show-on-unchecked }`gluetun2_vpn_port_forwarding`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/port-forwarding.md
            # Enable VPN port forwarding (on/off)
            # Type: string
            gluetun_role_vpn_port_forwarding: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/port-forwarding.md
            # Enable VPN port forwarding (on/off)
            # Type: string
            gluetun2_vpn_port_forwarding: ""
            ```

        ??? variable string "`gluetun_role_vpn_port_forwarding_listening_port`{ .sb-show-on-unchecked }`gluetun2_vpn_port_forwarding_listening_port`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/port-forwarding.md
            # Listening port for port forwarding
            # Type: string
            gluetun_role_vpn_port_forwarding_listening_port: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/port-forwarding.md
            # Listening port for port forwarding
            # Type: string
            gluetun2_vpn_port_forwarding_listening_port: ""
            ```

        ??? variable string "`gluetun_role_vpn_port_forwarding_provider`{ .sb-show-on-unchecked }`gluetun2_vpn_port_forwarding_provider`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/port-forwarding.md
            # Port forwarding provider (e.g., protonvpn, pia)
            # Type: string
            gluetun_role_vpn_port_forwarding_provider: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/port-forwarding.md
            # Port forwarding provider (e.g., protonvpn, pia)
            # Type: string
            gluetun2_vpn_port_forwarding_provider: ""
            ```

        ??? variable string "`gluetun_role_vpn_port_forwarding_status_file`{ .sb-show-on-unchecked }`gluetun2_vpn_port_forwarding_status_file`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/port-forwarding.md
            # Path to file for storing port forwarding status
            # Type: string
            gluetun_role_vpn_port_forwarding_status_file: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/port-forwarding.md
            # Path to file for storing port forwarding status
            # Type: string
            gluetun2_vpn_port_forwarding_status_file: ""
            ```

        ??? variable string "`gluetun_role_vpn_port_forwarding_username`{ .sb-show-on-unchecked }`gluetun2_vpn_port_forwarding_username`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/port-forwarding.md
            # Username for port forwarding authentication
            # Type: string
            gluetun_role_vpn_port_forwarding_username: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/port-forwarding.md
            # Username for port forwarding authentication
            # Type: string
            gluetun2_vpn_port_forwarding_username: ""
            ```

        ??? variable string "`gluetun_role_vpn_port_forwarding_password`{ .sb-show-on-unchecked }`gluetun2_vpn_port_forwarding_password`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/port-forwarding.md
            # Password for port forwarding authentication
            # Type: string
            gluetun_role_vpn_port_forwarding_password: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/port-forwarding.md
            # Password for port forwarding authentication
            # Type: string
            gluetun2_vpn_port_forwarding_password: ""
            ```

        ??? variable string "`gluetun_role_vpn_port_forwarding_up_command`{ .sb-show-on-unchecked }`gluetun2_vpn_port_forwarding_up_command`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/port-forwarding.md
            # Command to run when port forwarding is established
            # Type: string
            gluetun_role_vpn_port_forwarding_up_command: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/port-forwarding.md
            # Command to run when port forwarding is established
            # Type: string
            gluetun2_vpn_port_forwarding_up_command: ""
            ```

        ??? variable string "`gluetun_role_vpn_port_forwarding_down_command`{ .sb-show-on-unchecked }`gluetun2_vpn_port_forwarding_down_command`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/port-forwarding.md
            # Command to run when port forwarding is terminated
            # Type: string
            gluetun_role_vpn_port_forwarding_down_command: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/port-forwarding.md
            # Command to run when port forwarding is terminated
            # Type: string
            gluetun2_vpn_port_forwarding_down_command: ""
            ```

    === "Updater"

        ??? variable string "`gluetun_role_updater_period`{ .sb-show-on-unchecked }`gluetun2_updater_period`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/updater.md
            # Server list update period (e.g., 24h, 0 to disable)
            # Type: string
            gluetun_role_updater_period: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/updater.md
            # Server list update period (e.g., 24h, 0 to disable)
            # Type: string
            gluetun2_updater_period: ""
            ```

        ??? variable string "`gluetun_role_updater_min_ratio`{ .sb-show-on-unchecked }`gluetun2_updater_min_ratio`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/updater.md
            # Minimum ratio of servers to keep when updating
            # Type: string
            gluetun_role_updater_min_ratio: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/updater.md
            # Minimum ratio of servers to keep when updating
            # Type: string
            gluetun2_updater_min_ratio: ""
            ```

        ??? variable string "`gluetun_role_updater_vpn_service_providers`{ .sb-show-on-unchecked }`gluetun2_updater_vpn_service_providers`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/updater.md
            # Comma-separated list of VPN providers to update servers for
            # Type: string
            gluetun_role_updater_vpn_service_providers: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/updater.md
            # Comma-separated list of VPN providers to update servers for
            # Type: string
            gluetun2_updater_vpn_service_providers: ""
            ```

        ??? variable string "`gluetun_role_updater_protonvpn_email`{ .sb-show-on-unchecked }`gluetun2_updater_protonvpn_email`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/updater.md
            # ProtonVPN account email for server list updates
            # Type: string
            gluetun_role_updater_protonvpn_email: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/updater.md
            # ProtonVPN account email for server list updates
            # Type: string
            gluetun2_updater_protonvpn_email: ""
            ```

        ??? variable string "`gluetun_role_updater_protonvpn_password`{ .sb-show-on-unchecked }`gluetun2_updater_protonvpn_password`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/updater.md
            # ProtonVPN account password for server list updates
            # Type: string
            gluetun_role_updater_protonvpn_password: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/updater.md
            # ProtonVPN account password for server list updates
            # Type: string
            gluetun2_updater_protonvpn_password: ""
            ```

    === "Public IP"

        ??? variable string "`gluetun_role_publicip_enabled`{ .sb-show-on-unchecked }`gluetun2_publicip_enabled`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/public-ip.md
            # Enable public IP fetching (on/off)
            # Type: string
            gluetun_role_publicip_enabled: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/public-ip.md
            # Enable public IP fetching (on/off)
            # Type: string
            gluetun2_publicip_enabled: ""
            ```

        ??? variable string "`gluetun_role_publicip_file`{ .sb-show-on-unchecked }`gluetun2_publicip_file`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/public-ip.md
            # Path to file for storing public IP
            # Type: string
            gluetun_role_publicip_file: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/public-ip.md
            # Path to file for storing public IP
            # Type: string
            gluetun2_publicip_file: ""
            ```

        ??? variable string "`gluetun_role_publicip_api`{ .sb-show-on-unchecked }`gluetun2_publicip_api`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/public-ip.md
            # Public IP API to use (e.g., ipinfo, ip2location)
            # Type: string
            gluetun_role_publicip_api: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/public-ip.md
            # Public IP API to use (e.g., ipinfo, ip2location)
            # Type: string
            gluetun2_publicip_api: ""
            ```

        ??? variable string "`gluetun_role_publicip_api_token`{ .sb-show-on-unchecked }`gluetun2_publicip_api_token`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/public-ip.md
            # API token for public IP service
            # Type: string
            gluetun_role_publicip_api_token: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Reference: https://github.com/qdm12/gluetun-wiki/blob/main/setup/options/public-ip.md
            # API token for public IP service
            # Type: string
            gluetun2_publicip_api_token: ""
            ```

    === "Logging"

        ??? variable string "`gluetun_role_log_level`{ .sb-show-on-unchecked }`gluetun2_log_level`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Log level: debug, info, warning, error
            # Type: string
            gluetun_role_log_level: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Log level: debug, info, warning, error
            # Type: string
            gluetun2_log_level: ""
            ```

    === "Provider Specific"

        ??? variable string "`gluetun_role_private_internet_access_openvpn_encryption_preset`{ .sb-show-on-unchecked }`gluetun2_private_internet_access_openvpn_encryption_preset`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # PIA OpenVPN encryption preset: normal, strong, none
            # Type: string
            gluetun_role_private_internet_access_openvpn_encryption_preset: ""
            ```

            ```yaml { .sb-show-on-checked }
            # PIA OpenVPN encryption preset: normal, strong, none
            # Type: string
            gluetun2_private_internet_access_openvpn_encryption_preset: ""
            ```

    === "Misc"

        ??? variable string "`gluetun_role_version_information`{ .sb-show-on-unchecked }`gluetun2_version_information`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Enable version information logging on startup (on/off)
            # Type: string
            gluetun_role_version_information: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Enable version information logging on startup (on/off)
            # Type: string
            gluetun2_version_information: ""
            ```

        ??? variable string "`gluetun_role_storage_filepath`{ .sb-show-on-unchecked }`gluetun2_storage_filepath`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Path to storage file for persisting data
            # Type: string
            gluetun_role_storage_filepath: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Path to storage file for persisting data
            # Type: string
            gluetun2_storage_filepath: ""
            ```

        ??? variable string "`gluetun_role_pprof_enabled`{ .sb-show-on-unchecked }`gluetun2_pprof_enabled`{ .sb-show-on-checked }"

            ```yaml { .sb-show-on-unchecked }
            # Enable pprof profiling server (on/off)
            # Type: string
            gluetun_role_pprof_enabled: ""
            ```

            ```yaml { .sb-show-on-checked }
            # Enable pprof profiling server (on/off)
            # Type: string
            gluetun2_pprof_enabled: ""
            ```

=== "Docker"

    <h5>Container</h5>

    ??? variable string "`gluetun_role_docker_container`{ .sb-show-on-unchecked }`gluetun2_docker_container`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_container: "{{ gluetun_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_container: "{{ gluetun_name }}"
        ```

    <h5>Image</h5>

    ??? variable bool "`gluetun_role_docker_image_pull`{ .sb-show-on-unchecked }`gluetun2_docker_image_pull`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        gluetun_role_docker_image_pull: true
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        gluetun2_docker_image_pull: true
        ```

    ??? variable string "`gluetun_role_docker_image_repo`{ .sb-show-on-unchecked }`gluetun2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_image_repo: "qmcgaw/gluetun"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_image_repo: "qmcgaw/gluetun"
        ```

    ??? variable string "`gluetun_role_docker_image_tag`{ .sb-show-on-unchecked }`gluetun2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_image_tag: "v3.41"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_image_tag: "v3.41"
        ```

    ??? variable string "`gluetun_role_docker_image`{ .sb-show-on-unchecked }`gluetun2_docker_image`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='gluetun') }}:{{ lookup('role_var', '_docker_image_tag', role='gluetun') }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_image: "{{ lookup('role_var', '_docker_image_repo', role='gluetun') }}:{{ lookup('role_var', '_docker_image_tag', role='gluetun') }}"
        ```

    ??? variable dict "`gluetun_role_docker_envs_custom`{ .sb-show-on-unchecked }`gluetun2_docker_envs_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        gluetun_role_docker_envs_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        gluetun2_docker_envs_custom: {}
        ```

    <h5>Volumes</h5>

    ??? variable bool "`gluetun_role_docker_volumes_global`{ .sb-show-on-unchecked }`gluetun2_docker_volumes_global`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        gluetun_role_docker_volumes_global: false
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        gluetun2_docker_volumes_global: false
        ```

    ??? variable list "`gluetun_role_docker_volumes_default`{ .sb-show-on-unchecked }`gluetun2_docker_volumes_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_volumes_default:
          - "{{ gluetun_role_paths_location }}:/gluetun"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_volumes_default:
          - "{{ gluetun_role_paths_location }}:/gluetun"
        ```

    ??? variable list "`gluetun_role_docker_volumes_custom`{ .sb-show-on-unchecked }`gluetun2_docker_volumes_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_volumes_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_volumes_custom: []
        ```

    <h5>Labels</h5>

    ??? variable dict "`gluetun_role_docker_labels_default`{ .sb-show-on-unchecked }`gluetun2_docker_labels_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        gluetun_role_docker_labels_default:
          com.centurylinklabs.watchtower.enable: "false"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        gluetun2_docker_labels_default:
          com.centurylinklabs.watchtower.enable: "false"
        ```

    ??? variable dict "`gluetun_role_docker_labels_custom`{ .sb-show-on-unchecked }`gluetun2_docker_labels_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        gluetun_role_docker_labels_custom: {}
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        gluetun2_docker_labels_custom: {}
        ```

    <h5>Hostname</h5>

    ??? variable string "`gluetun_role_docker_hostname`{ .sb-show-on-unchecked }`gluetun2_docker_hostname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_hostname: "{{ gluetun_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_hostname: "{{ gluetun_name }}"
        ```

    <h5>Networks</h5>

    ??? variable string "`gluetun_role_docker_networks_alias`{ .sb-show-on-unchecked }`gluetun2_docker_networks_alias`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_networks_alias: "{{ gluetun_name }}"
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_networks_alias: "{{ gluetun_name }}"
        ```

    ??? variable list "`gluetun_role_docker_networks_default`{ .sb-show-on-unchecked }`gluetun2_docker_networks_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_networks_default: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_networks_default: []
        ```

    ??? variable list "`gluetun_role_docker_networks_custom`{ .sb-show-on-unchecked }`gluetun2_docker_networks_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_networks_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_networks_custom: []
        ```

    <h5>Capabilities</h5>

    ??? variable list "`gluetun_role_docker_capabilities_default`{ .sb-show-on-unchecked }`gluetun2_docker_capabilities_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_capabilities_default:
          - NET_ADMIN
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_capabilities_default:
          - NET_ADMIN
        ```

    ??? variable list "`gluetun_role_docker_capabilities_custom`{ .sb-show-on-unchecked }`gluetun2_docker_capabilities_custom`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_capabilities_custom: []
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_capabilities_custom: []
        ```

    <h5>Restart Policy</h5>

    ??? variable string "`gluetun_role_docker_restart_policy`{ .sb-show-on-unchecked }`gluetun2_docker_restart_policy`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_restart_policy: unless-stopped
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_restart_policy: unless-stopped
        ```

    <h5>State</h5>

    ??? variable string "`gluetun_role_docker_state`{ .sb-show-on-unchecked }`gluetun2_docker_state`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_state: started
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_state: started
        ```

=== "Docker+"

    The following advanced options are available via create_docker_container but are not defined in the role. See: [docker_container module](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

    <h5>Resource Limits</h5>

    ??? variable int "`gluetun_role_docker_blkio_weight`{ .sb-show-on-unchecked }`gluetun2_docker_blkio_weight`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        gluetun_role_docker_blkio_weight:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        gluetun2_docker_blkio_weight:
        ```

    ??? variable int "`gluetun_role_docker_cpu_period`{ .sb-show-on-unchecked }`gluetun2_docker_cpu_period`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        gluetun_role_docker_cpu_period:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        gluetun2_docker_cpu_period:
        ```

    ??? variable int "`gluetun_role_docker_cpu_quota`{ .sb-show-on-unchecked }`gluetun2_docker_cpu_quota`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        gluetun_role_docker_cpu_quota:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        gluetun2_docker_cpu_quota:
        ```

    ??? variable int "`gluetun_role_docker_cpu_shares`{ .sb-show-on-unchecked }`gluetun2_docker_cpu_shares`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        gluetun_role_docker_cpu_shares:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        gluetun2_docker_cpu_shares:
        ```

    ??? variable string "`gluetun_role_docker_cpus`{ .sb-show-on-unchecked }`gluetun2_docker_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_cpus:
        ```

    ??? variable string "`gluetun_role_docker_cpuset_cpus`{ .sb-show-on-unchecked }`gluetun2_docker_cpuset_cpus`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_cpuset_cpus:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_cpuset_cpus:
        ```

    ??? variable string "`gluetun_role_docker_cpuset_mems`{ .sb-show-on-unchecked }`gluetun2_docker_cpuset_mems`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_cpuset_mems:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_cpuset_mems:
        ```

    ??? variable string "`gluetun_role_docker_kernel_memory`{ .sb-show-on-unchecked }`gluetun2_docker_kernel_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_kernel_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_kernel_memory:
        ```

    ??? variable string "`gluetun_role_docker_memory`{ .sb-show-on-unchecked }`gluetun2_docker_memory`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_memory:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_memory:
        ```

    ??? variable string "`gluetun_role_docker_memory_reservation`{ .sb-show-on-unchecked }`gluetun2_docker_memory_reservation`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_memory_reservation:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_memory_reservation:
        ```

    ??? variable string "`gluetun_role_docker_memory_swap`{ .sb-show-on-unchecked }`gluetun2_docker_memory_swap`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_memory_swap:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_memory_swap:
        ```

    ??? variable int "`gluetun_role_docker_memory_swappiness`{ .sb-show-on-unchecked }`gluetun2_docker_memory_swappiness`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        gluetun_role_docker_memory_swappiness:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        gluetun2_docker_memory_swappiness:
        ```

    ??? variable string "`gluetun_role_docker_shm_size`{ .sb-show-on-unchecked }`gluetun2_docker_shm_size`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_shm_size:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_shm_size:
        ```

    <h5>Security & Devices</h5>

    ??? variable list "`gluetun_role_docker_cap_drop`{ .sb-show-on-unchecked }`gluetun2_docker_cap_drop`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_cap_drop:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_cap_drop:
        ```

    ??? variable string "`gluetun_role_docker_cgroupns_mode`{ .sb-show-on-unchecked }`gluetun2_docker_cgroupns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_cgroupns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_cgroupns_mode:
        ```

    ??? variable list "`gluetun_role_docker_device_cgroup_rules`{ .sb-show-on-unchecked }`gluetun2_docker_device_cgroup_rules`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_device_cgroup_rules:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_device_cgroup_rules:
        ```

    ??? variable list "`gluetun_role_docker_device_read_bps`{ .sb-show-on-unchecked }`gluetun2_docker_device_read_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_device_read_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_device_read_bps:
        ```

    ??? variable list "`gluetun_role_docker_device_read_iops`{ .sb-show-on-unchecked }`gluetun2_docker_device_read_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_device_read_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_device_read_iops:
        ```

    ??? variable list "`gluetun_role_docker_device_requests`{ .sb-show-on-unchecked }`gluetun2_docker_device_requests`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_device_requests:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_device_requests:
        ```

    ??? variable list "`gluetun_role_docker_device_write_bps`{ .sb-show-on-unchecked }`gluetun2_docker_device_write_bps`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_device_write_bps:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_device_write_bps:
        ```

    ??? variable list "`gluetun_role_docker_device_write_iops`{ .sb-show-on-unchecked }`gluetun2_docker_device_write_iops`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_device_write_iops:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_device_write_iops:
        ```

    ??? variable list "`gluetun_role_docker_devices`{ .sb-show-on-unchecked }`gluetun2_docker_devices`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_devices:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_devices:
        ```

    ??? variable string "`gluetun_role_docker_devices_default`{ .sb-show-on-unchecked }`gluetun2_docker_devices_default`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_devices_default:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_devices_default:
        ```

    ??? variable list "`gluetun_role_docker_groups`{ .sb-show-on-unchecked }`gluetun2_docker_groups`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_groups:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_groups:
        ```

    ??? variable bool "`gluetun_role_docker_privileged`{ .sb-show-on-unchecked }`gluetun2_docker_privileged`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        gluetun_role_docker_privileged:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        gluetun2_docker_privileged:
        ```

    ??? variable list "`gluetun_role_docker_security_opts`{ .sb-show-on-unchecked }`gluetun2_docker_security_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_security_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_security_opts:
        ```

    ??? variable string "`gluetun_role_docker_user`{ .sb-show-on-unchecked }`gluetun2_docker_user`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_user:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_user:
        ```

    ??? variable string "`gluetun_role_docker_userns_mode`{ .sb-show-on-unchecked }`gluetun2_docker_userns_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_userns_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_userns_mode:
        ```

    <h5>Networking</h5>

    ??? variable list "`gluetun_role_docker_dns_opts`{ .sb-show-on-unchecked }`gluetun2_docker_dns_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_dns_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_dns_opts:
        ```

    ??? variable list "`gluetun_role_docker_dns_search_domains`{ .sb-show-on-unchecked }`gluetun2_docker_dns_search_domains`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_dns_search_domains:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_dns_search_domains:
        ```

    ??? variable list "`gluetun_role_docker_dns_servers`{ .sb-show-on-unchecked }`gluetun2_docker_dns_servers`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_dns_servers:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_dns_servers:
        ```

    ??? variable string "`gluetun_role_docker_domainname`{ .sb-show-on-unchecked }`gluetun2_docker_domainname`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_domainname:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_domainname:
        ```

    ??? variable list "`gluetun_role_docker_exposed_ports`{ .sb-show-on-unchecked }`gluetun2_docker_exposed_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_exposed_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_exposed_ports:
        ```

    ??? variable dict "`gluetun_role_docker_hosts`{ .sb-show-on-unchecked }`gluetun2_docker_hosts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        gluetun_role_docker_hosts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        gluetun2_docker_hosts:
        ```

    ??? variable bool "`gluetun_role_docker_hosts_use_common`{ .sb-show-on-unchecked }`gluetun2_docker_hosts_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        gluetun_role_docker_hosts_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        gluetun2_docker_hosts_use_common:
        ```

    ??? variable string "`gluetun_role_docker_ipc_mode`{ .sb-show-on-unchecked }`gluetun2_docker_ipc_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_ipc_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_ipc_mode:
        ```

    ??? variable list "`gluetun_role_docker_links`{ .sb-show-on-unchecked }`gluetun2_docker_links`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_links:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_links:
        ```

    ??? variable string "`gluetun_role_docker_network_mode`{ .sb-show-on-unchecked }`gluetun2_docker_network_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_network_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_network_mode:
        ```

    ??? variable string "`gluetun_role_docker_pid_mode`{ .sb-show-on-unchecked }`gluetun2_docker_pid_mode`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_pid_mode:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_pid_mode:
        ```

    ??? variable list "`gluetun_role_docker_ports`{ .sb-show-on-unchecked }`gluetun2_docker_ports`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_ports:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_ports:
        ```

    ??? variable string "`gluetun_role_docker_uts`{ .sb-show-on-unchecked }`gluetun2_docker_uts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_uts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_uts:
        ```

    <h5>Storage</h5>

    ??? variable bool "`gluetun_role_docker_keep_volumes`{ .sb-show-on-unchecked }`gluetun2_docker_keep_volumes`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        gluetun_role_docker_keep_volumes:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        gluetun2_docker_keep_volumes:
        ```

    ??? variable list "`gluetun_role_docker_mounts`{ .sb-show-on-unchecked }`gluetun2_docker_mounts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_mounts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_mounts:
        ```

    ??? variable dict "`gluetun_role_docker_storage_opts`{ .sb-show-on-unchecked }`gluetun2_docker_storage_opts`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        gluetun_role_docker_storage_opts:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        gluetun2_docker_storage_opts:
        ```

    ??? variable list "`gluetun_role_docker_tmpfs`{ .sb-show-on-unchecked }`gluetun2_docker_tmpfs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_tmpfs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_tmpfs:
        ```

    ??? variable string "`gluetun_role_docker_volume_driver`{ .sb-show-on-unchecked }`gluetun2_docker_volume_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_volume_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_volume_driver:
        ```

    ??? variable list "`gluetun_role_docker_volumes_from`{ .sb-show-on-unchecked }`gluetun2_docker_volumes_from`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_volumes_from:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_volumes_from:
        ```

    ??? variable string "`gluetun_role_docker_working_dir`{ .sb-show-on-unchecked }`gluetun2_docker_working_dir`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_working_dir:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_working_dir:
        ```

    <h5>Monitoring & Lifecycle</h5>

    ??? variable bool "`gluetun_role_docker_auto_remove`{ .sb-show-on-unchecked }`gluetun2_docker_auto_remove`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        gluetun_role_docker_auto_remove:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        gluetun2_docker_auto_remove:
        ```

    ??? variable bool "`gluetun_role_docker_cleanup`{ .sb-show-on-unchecked }`gluetun2_docker_cleanup`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        gluetun_role_docker_cleanup:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        gluetun2_docker_cleanup:
        ```

    ??? variable string "`gluetun_role_docker_force_kill`{ .sb-show-on-unchecked }`gluetun2_docker_force_kill`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_force_kill:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_force_kill:
        ```

    ??? variable dict "`gluetun_role_docker_healthcheck`{ .sb-show-on-unchecked }`gluetun2_docker_healthcheck`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        gluetun_role_docker_healthcheck:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        gluetun2_docker_healthcheck:
        ```

    ??? variable int "`gluetun_role_docker_healthy_wait_timeout`{ .sb-show-on-unchecked }`gluetun2_docker_healthy_wait_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        gluetun_role_docker_healthy_wait_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        gluetun2_docker_healthy_wait_timeout:
        ```

    ??? variable bool "`gluetun_role_docker_init`{ .sb-show-on-unchecked }`gluetun2_docker_init`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        gluetun_role_docker_init:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        gluetun2_docker_init:
        ```

    ??? variable string "`gluetun_role_docker_kill_signal`{ .sb-show-on-unchecked }`gluetun2_docker_kill_signal`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_kill_signal:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_kill_signal:
        ```

    ??? variable string "`gluetun_role_docker_log_driver`{ .sb-show-on-unchecked }`gluetun2_docker_log_driver`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_log_driver:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_log_driver:
        ```

    ??? variable dict "`gluetun_role_docker_log_options`{ .sb-show-on-unchecked }`gluetun2_docker_log_options`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: dict
        gluetun_role_docker_log_options:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: dict
        gluetun2_docker_log_options:
        ```

    ??? variable bool "`gluetun_role_docker_oom_killer`{ .sb-show-on-unchecked }`gluetun2_docker_oom_killer`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        gluetun_role_docker_oom_killer:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        gluetun2_docker_oom_killer:
        ```

    ??? variable int "`gluetun_role_docker_oom_score_adj`{ .sb-show-on-unchecked }`gluetun2_docker_oom_score_adj`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        gluetun_role_docker_oom_score_adj:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        gluetun2_docker_oom_score_adj:
        ```

    ??? variable bool "`gluetun_role_docker_output_logs`{ .sb-show-on-unchecked }`gluetun2_docker_output_logs`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        gluetun_role_docker_output_logs:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        gluetun2_docker_output_logs:
        ```

    ??? variable bool "`gluetun_role_docker_paused`{ .sb-show-on-unchecked }`gluetun2_docker_paused`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        gluetun_role_docker_paused:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        gluetun2_docker_paused:
        ```

    ??? variable bool "`gluetun_role_docker_recreate`{ .sb-show-on-unchecked }`gluetun2_docker_recreate`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        gluetun_role_docker_recreate:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        gluetun2_docker_recreate:
        ```

    ??? variable int "`gluetun_role_docker_restart_retries`{ .sb-show-on-unchecked }`gluetun2_docker_restart_retries`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        gluetun_role_docker_restart_retries:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        gluetun2_docker_restart_retries:
        ```

    ??? variable int "`gluetun_role_docker_stop_timeout`{ .sb-show-on-unchecked }`gluetun2_docker_stop_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        gluetun_role_docker_stop_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        gluetun2_docker_stop_timeout:
        ```

    <h5>Other Options</h5>

    ??? variable string "`gluetun_role_docker_cgroup_parent`{ .sb-show-on-unchecked }`gluetun2_docker_cgroup_parent`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_cgroup_parent:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_cgroup_parent:
        ```

    ??? variable list "`gluetun_role_docker_commands`{ .sb-show-on-unchecked }`gluetun2_docker_commands`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_commands:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_commands:
        ```

    ??? variable int "`gluetun_role_docker_create_timeout`{ .sb-show-on-unchecked }`gluetun2_docker_create_timeout`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: int
        gluetun_role_docker_create_timeout:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: int
        gluetun2_docker_create_timeout:
        ```

    ??? variable string "`gluetun_role_docker_entrypoint`{ .sb-show-on-unchecked }`gluetun2_docker_entrypoint`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_entrypoint:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_entrypoint:
        ```

    ??? variable string "`gluetun_role_docker_env_file`{ .sb-show-on-unchecked }`gluetun2_docker_env_file`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_env_file:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_env_file:
        ```

    ??? variable bool "`gluetun_role_docker_labels_use_common`{ .sb-show-on-unchecked }`gluetun2_docker_labels_use_common`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        gluetun_role_docker_labels_use_common:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        gluetun2_docker_labels_use_common:
        ```

    ??? variable bool "`gluetun_role_docker_read_only`{ .sb-show-on-unchecked }`gluetun2_docker_read_only`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        gluetun_role_docker_read_only:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        gluetun2_docker_read_only:
        ```

    ??? variable string "`gluetun_role_docker_runtime`{ .sb-show-on-unchecked }`gluetun2_docker_runtime`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_runtime:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_runtime:
        ```

    ??? variable list "`gluetun_role_docker_sysctls`{ .sb-show-on-unchecked }`gluetun2_docker_sysctls`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_sysctls:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_sysctls:
        ```

    ??? variable list "`gluetun_role_docker_ulimits`{ .sb-show-on-unchecked }`gluetun2_docker_ulimits`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: list
        gluetun_role_docker_ulimits:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: list
        gluetun2_docker_ulimits:
        ```

=== "Global Override Options"

    ??? variable bool "`gluetun_role_autoheal_enabled`{ .sb-show-on-unchecked }`gluetun2_autoheal_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        gluetun_role_autoheal_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Autoheal monitoring for containers created when deploying
        # Type: bool (true/false)
        gluetun2_autoheal_enabled: true
        ```

    ??? variable string "`gluetun_role_depends_on`{ .sb-show-on-unchecked }`gluetun2_depends_on`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # List of container dependencies that must be running before containers start
        # Type: string
        gluetun_role_depends_on: ""
        ```

        ```yaml { .sb-show-on-checked }
        # List of container dependencies that must be running before containers start
        # Type: string
        gluetun2_depends_on: ""
        ```

    ??? variable string "`gluetun_role_depends_on_delay`{ .sb-show-on-unchecked }`gluetun2_depends_on_delay`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        gluetun_role_depends_on_delay: "0"
        ```

        ```yaml { .sb-show-on-checked }
        # Delay in seconds before starting containers after dependencies are ready
        # Type: string (quoted number)
        gluetun2_depends_on_delay: "0"
        ```

    ??? variable string "`gluetun_role_depends_on_healthchecks`{ .sb-show-on-unchecked }`gluetun2_depends_on_healthchecks`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        gluetun_role_depends_on_healthchecks:
        ```

        ```yaml { .sb-show-on-checked }
        # Enable healthcheck waiting for container dependencies
        # Type: string ("true"/"false")
        gluetun2_depends_on_healthchecks:
        ```

    ??? variable bool "`gluetun_role_diun_enabled`{ .sb-show-on-unchecked }`gluetun2_diun_enabled`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        gluetun_role_diun_enabled: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Diun update notifications for containers created when deploying
        # Type: bool (true/false)
        gluetun2_diun_enabled: true
        ```

    ??? variable bool "`gluetun_role_docker_controller`{ .sb-show-on-unchecked }`gluetun2_docker_controller`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        gluetun_role_docker_controller: true
        ```

        ```yaml { .sb-show-on-checked }
        # Enable or disable Saltbox Docker Controller management for containers
        # Type: bool (true/false)
        gluetun2_docker_controller: true
        ```

    ??? variable string "`gluetun_role_docker_image_repo`{ .sb-show-on-unchecked }`gluetun2_docker_image_repo`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_image_repo:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_image_repo:
        ```

    ??? variable string "`gluetun_role_docker_image_tag`{ .sb-show-on-unchecked }`gluetun2_docker_image_tag`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: string
        gluetun_role_docker_image_tag:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: string
        gluetun2_docker_image_tag:
        ```

    ??? variable bool "`gluetun_role_docker_volumes_download`{ .sb-show-on-unchecked }`gluetun2_docker_volumes_download`{ .sb-show-on-checked }"

        ```yaml { .sb-show-on-unchecked }
        # Type: bool (true/false)
        gluetun_role_docker_volumes_download:
        ```

        ```yaml { .sb-show-on-checked }
        # Type: bool (true/false)
        gluetun2_docker_volumes_download:
        ```
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
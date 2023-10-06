# Gluetun

## What is it?

[Gluetun](https://github.com/qdm12/gluetun) is a VPN client in a thin Docker container for multiple VPN providers, written in Go, and using OpenVPN or Wireguard, DNS over TLS, with a few proxy servers built-in.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/qdm12/gluetun){: .header-icons } | [:octicons-link-16: Docs](https://github.com/qdm12/gluetun){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/qdm12/gluetun){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/qmcgaw/gluetun){: .header-icons }|

### 1. Configuration

The Gluetun role is configured via the [inventory system](../saltbox/inventory/index.md). It is recommended to review the upstream documentation for your VPN provider to determine the proper configuration. The following variables are available to set and correspond to the similarly named Docker envs.

```yaml
gluetun_vpn_service_provider:
gluetun_vpn_type:
gluetun_openvpn_custom_config:
gluetun_openvpn_user:
gluetun_openvpn_password:
gluetun_openvpn_key_passphrase:
gluetun_vpn_endpoint_ip:
gluetun_vpn_endpoint_port:
gluetun_wireguard_public_key:
gluetun_wireguard_private_key:
gluetun_wireguard_preshared_key:
gluetun_wireguard_addresses:
gluetun_server_countries:
gluetun_server_cities:
gluetun_server_hostnames:
gluetun_server_names:
gluetun_server_regions:
gluetun_firewall_vpn_input_ports:
gluetun_firewall_input_ports:
gluetun_firewall_outbound_subnets:
```

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

!!! caution
    While multiple containers may be routed through a single Gluetun instance, you must manually ensure there are no port clashes as all port binds for the connected containers will be through the Gluetun container and must have unique ports inside that container.

- [:octicons-link-16: Documentation](https://github.com/qdm12/gluetun){: .header-icons }

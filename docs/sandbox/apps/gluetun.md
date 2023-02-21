# Gluetun

## What is it?

[Gluetun](https://github.com/qdm12/gluetun){: target=_blank rel="noopener noreferrer" } is a VPN client in a thin Docker container for multiple VPN providers, written in Go, and using OpenVPN or Wireguard, DNS over TLS, with a few proxy servers built-in.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/qdm12/gluetun){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/qdm12/gluetun){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/qdm12/gluetun){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/qmcgaw/gluetun){: .header-icons target=_blank rel="noopener noreferrer" }|

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

Additionl Docker envs may be set via `gluetun_docker_envs_custom`.

### 2. Installation

``` shell
sb install sandbox-gluetun
```

### 3. Route a container through Gluetun

To route a Saltbox-configured container through Gluetun, you must set `<rolename>_docker_network_mode: "container:gluetun"` via the inventory system. For example, to route `qbittorrent` through Gluetun, the entry would be `qbittorrent_docker_network_mode: "container:gluetun"`.

!!! caution
While multiple containers may be routed through a single Gluetun instance, you must manually ensure there are no port clashes as all port binds for the connected containers will be through the Gluetun container and must have unique ports inside that container.

### 3. Setup

- [:octicons-link-16: Documentation](https://github.com/qdm12/gluetun){: .header-icons target=_blank rel="noopener noreferrer" }

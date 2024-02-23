# qBittorrentvpn

## What is it?

[qbittorrentvpn](https://github.com/binhex/arch-qbittorrentvpn) is a qbittorrent container which includes OpenVPN and WireGuard to ensure a secure and private connection to the Internet, including use of iptables to prevent IP leakage when the tunnel is down. It also includes Privoxy to allow unfiltered access to index sites.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/binhex/arch-qbittorrentvpn){: .header-icons } | [:octicons-link-16: Docs](https://github.com/binhex/arch-qbittorrentvpn){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/binhex/arch-qbittorrentvpn){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/binhex/arch-qbittorrentvpn){: .header-icons }|

### 1. Installation

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

### 2. URL

- To access qbittorrentvpn, visit `https://qbittorrentvpn._yourdomain.com_`

### 3. Setup

- [:octicons-link-16: Documentation: qBittorrentvpn Docs](https://github.com/binhex/arch-qbittorrentvpn){: .header-icons }

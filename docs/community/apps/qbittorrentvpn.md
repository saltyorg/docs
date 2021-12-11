# qBittorrentVPN

# **NOT INTEGRATED - MAKE SANDBOX REQUEST IF NEEDED**

## What is it?

[qBittorrent](https://www.qbittorrent.org/){: target=_blank rel="noopener noreferrer" } is a bittorrent client programmed in C++ / Qt that uses libtorrent (sometimes called libtorrent-rasterbar) by Arvid Norberg.

It aims to be a good alternative to all other bittorrent clients out there. qBittorrent is fast, stable and provides unicode support as well as many features.

[qBittorrentVPN](https://www.qbittorrent.org/){: target=_blank rel="noopener noreferrer" } is a VPN version of [qBittorrent](../../community/apps/qbittorrent.md) with OpenVPN to ensure a secure and private connection to the Internet, including use of iptables to prevent IP leakage when the tunnel is down.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home ](https://www.qbittorrent.org/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/qbittorrent/qBittorrent/wiki){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github:](https://github.com/qbittorrent/qBittorrent){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker ](https://hub.docker.com/r/saltydk/qbittorrent){: .header-icons target=_blank rel="noopener noreferrer" }|

### 1. Installation

``` shell

sb install cm-qbittorrentvpn

```

### 2. URL

- To access qBittorrentVPN, visit `https://qbittorrentvpn._yourdomain.com_`

### 3. Setup

- Edit the qBittorrentVPN settings in the qbittorrentvpn section in [community `settings.yml`:](../../community/settings.md) as shown below.

   ``` { .yaml }
    qbittorrentvpn:
      vpn_endpoint: netherlands.ovpn
      vpn_user: your_vpn_username
      vpn_pass: your_vpn_password
      vpn_prov: pia
      vpn_client: wireguard # 'wireguard' or 'openvpn'
   ```

- Follow instructions for parent role [qBittorrent](../../community/apps/qbittorrent.md)

- [:octicons-link-16: Documentation](DOCSLINK){: .header-icons target=_blank rel="noopener noreferrer" }

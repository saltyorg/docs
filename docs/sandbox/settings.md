# The Settings File

The configuration file for Saltbox Community settings is called settings.yml and is located at `/opt/community/settings.yml`

settings.yml

``` { .yaml .annotate }
---
example:  # (1)
  roles:
    - podcasts
    - poetry
qbittorrentvpn:  # (2)
  vpn_endpoint: netherlands.ovpn
  vpn_user: your_vpn_username
  vpn_pass: your_vpn_password
  vpn_prov: pia
  vpn_client: wireguard # 'wireguard' or 'openvpn'
unifi:  # (3)
  port: 8080
```

1. Example role, provide a list of "examples's"
    For each listed item an Example instance will be created and the item set to the subdomain.

2. QbittorrentVPN

3. Unifi

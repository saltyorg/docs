# The Settings File

The configuration file for Saltbox Community settings is called settings.yml and is located at `/opt/community/settings.yml`

settings.yml

``` { .yaml .annotate }
---
alternatrrx:  # (1)
  roles:
    - 1080webdl
    - 1080remux
bazarrx:  # (2)
  roles:
    - 1080webdl
    - 1080remux
delugevpn:  # (3)
  vpn_endpoint: netherlands.ovpn
  vpn_pass: your_vpn_password
  vpn_prov: pia
  vpn_user: your_vpn_username
  vpn_client: wireguard # 'wireguard' or 'openvpn'
delugex:  # (4)
  roles:
    - ""
goplaxt:  # (5)
  trakt_id: ~
  trakt_secret: ~
handbrake:  # (6)
  handbrake_pass: saltbox # must be less than eight characters
lidarrx:  # (7)
  roles:
    - flac
    - mp3
moviematch:  # (8)
  libraries: Movies
  plex_url: http://plex:32400
ombix:  # (9)
  roles:
    - 4k
qbittorrentvpn:  # (10)
  vpn_endpoint: netherlands.ovpn
  vpn_user: your_vpn_username
  vpn_pass: your_vpn_password
  vpn_prov: pia
  vpn_client: wireguard # 'wireguard' or 'openvpn'
qbittorrentx:  # (11)
  roles:
    - ""
radarrx:  # (12)
  roles:
    - 1080webdl
    - 1080remux
readarrx:  # (13)
  roles:
    - ebooks
    - audiobooks
requestrrx:  # (14)
  roles:
    - 1080
    - 4k
rfloodx:  # (15)
  roles:
    - ""
sonarrx:  # (16)
  roles:
    - 1080webdl
    - 1080remux
tautullix:  # (17)
  tautulli: plex
  tautulli2: plex2
transmissionvpn:  # (18)
  vpn_endpoint: netherlands.ovpn
  vpn_pass: your_vpn_password
  vpn_prov: NORDVPN
  vpn_user: your_vpn_username
transmissionx:  # (19)
  roles:
    - ""
unifi:  # (20)
  port: 8080
```

1. AlternatorX role, provide a list of "X's"
    For each listed item an Alternator instance will be created and the item set to the subdomain.

2. BazarrX role, provide a list of "X's"
    For each listed item an Bazarr instance will be created and the item set to the subdomain.

3. DelugeVPN settings block, replace the examples given with your own information.

4. DelugeX

5. Goplaxt

6. Handbrake

7. LidarrX

8. Moviematch

9. Ombix

10. QbittorrentVPN

11. QbittorrentX

12. RadarrX

13. ReadarrX

14. RequestrrX

15. RfloodX

16. SonarrX

17. TautulliX

18. TransmissionVPN

19. TransmissionX

20. Unifi


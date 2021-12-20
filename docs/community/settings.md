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
    - 1080webdl
    - 1080remux
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
overseerrx: # (10)
  roles:
    - ""
qbittorrentvpn:  # (11)
  vpn_endpoint: netherlands.ovpn
  vpn_user: your_vpn_username
  vpn_pass: your_vpn_password
  vpn_prov: pia
  vpn_client: wireguard # 'wireguard' or 'openvpn'
qbittorrentx:  # (12)
  roles:
    - 1080webdl
    - 1080remux
radarrx:  # (13)
  roles:
    - 1080webdl
    - 1080remux
readarrx:  # (14)
  roles:
    - ebooks
    - audiobooks
requestrrx:  # (15)
  roles:
    - 1080
    - 4k
rfloodx:  # (16)
  roles:
    - 1080webdl
    - 1080remux
sonarrx:  # (17)
  roles:
    - 1080webdl
    - 1080remux
tautullix:  # (18)
  tautulli: plex
  tautulli2: plex2
transmissionvpn:  # (19)
  vpn_endpoint: netherlands.ovpn
  vpn_pass: your_vpn_password
  vpn_prov: NORDVPN
  vpn_user: your_vpn_username
transmissionx:  # (20)
  roles:
    - 1080webdl
    - 1080remux
```

1. AlternatrrX role, provide a list of "X's"
    For each listed item an Alternatrr instance will be created and the item set to the subdomain.

2. BazarrX role, provide a list of "X's"
    For each listed item a Bazarr instance will be created and the item set to the subdomain.

3. DelugeVPN settings block, replace the examples given with your own information.

4. DelugeX role, provide a list of "X's"
    For each listed item a Deluge instance will be created and the item set to the subdomain.

5. Goplaxt
   Trakt App ID and Secret

6. Handbrake

7. LidarrX role, provide a list of "X's"
    For each listed item a Lidarr instance will be created and the item set to the subdomain.

8. Moviematch

9.  Ombix role, provide a list of "X's"
    For each listed item an Ombi instance will be created and the item set to the subdomain.

10. OverseerrX role, provide a list of "X's"
    For each listed item an Overseerr instance will be created and the item set to the subdomain.

11. QbittorrentVPN

12. QbittorrentX role, provide a list of "X's"
    For each listed item a QBitorrent instance will be created and the item set to the subdomain.

13. RadarrX role, provide a list of "X's"
    For each listed item a Radarr instance will be created and the item set to the subdomain.

14. ReadarrX role, provide a list of "X's"
    For each listed item a Readarr instance will be created and the item set to the subdomain.

15. RequestrrX role, provide a list of "X's"
    For each listed item a Requestrr instance will be created and the item set to the subdomain.

16. RfloodX role, provide a list of "X's"
    For each listed item an RFlood instance will be created and the item set to the subdomain.

17. SonarrX role, provide a list of "X's"
    For each listed item a Sonarr instance will be created and the item set to the subdomain.

18. TautulliX role, provide a list of "X's"
    For each listed item a Tautulli instance will be created and the item set to the subdomain.

19. TransmissionVPN

20. TransmissionX role, provide a list of "X's"
    For each listed item a Transmission instance will be created and the item set to the subdomain.


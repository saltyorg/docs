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
qbittorrentx:  # (11)
  roles:
    - 1080webdl
    - 1080remux
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
    - 1080webdl
    - 1080remux
sonarrx:  # (16)
  roles:
    - 1080webdl
    - 1080remux
tautullix:  # (17)
  tautulli: plex
  tautulli2: plex2
transmissionx:  # (18)
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

9. Ombix role, provide a list of "X's"
   For each listed item an Ombi instance will be created and the item set to the subdomain.

10. OverseerrX role, provide a list of "X's"
    For each listed item an Overseerr instance will be created and the item set to the subdomain.

11. QbittorrentX role, provide a list of "X's"
    For each listed item a QBitorrent instance will be created and the item set to the subdomain.

12. RadarrX role, provide a list of "X's"
    For each listed item a Radarr instance will be created and the item set to the subdomain.

13. ReadarrX role, provide a list of "X's"
    For each listed item a Readarr instance will be created and the item set to the subdomain.

14. RequestrrX role, provide a list of "X's"
    For each listed item a Requestrr instance will be created and the item set to the subdomain.

15. RfloodX role, provide a list of "X's"
    For each listed item an RFlood instance will be created and the item set to the subdomain.

16. SonarrX role, provide a list of "X's"
    For each listed item a Sonarr instance will be created and the item set to the subdomain.

17. TautulliX role, provide a list of "X's"
    For each listed item a Tautulli instance will be created and the item set to the subdomain.

18. TransmissionX role, provide a list of "X's"
    For each listed item a Transmission instance will be created and the item set to the subdomain.


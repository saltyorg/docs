---
hide:
  - navigation
  - toc
---

| **App**           | **Ports**                                    | **Notes**                                                                                                                                  |
| ----------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Emby                |                                              |                                                                                                                                            |
| Jackett             |                                              |                                                                                                                                            |
| Lidarr              |                                              |                                                                                                                                            |
| Traefik           | 80, 443                                      | Used by Saltbox apps when reverse-proxy is enabled.                                                                                        |
| NZBGet              |                                              |                                                                                                                                            |
| NZBHydra            |                                              |                                                                                                                                            |
| NZBHydra2           |                                              |                                                                                                                                            |
| Ombi                |                                              |                                                                                                                                            |
| Organizr            |                                              |                                                                                                                                            |
| Plex (main)       | 32400                                        | Not needed when using reverse proxy. <br> <br> If 32400 needs to be open, set `plex_open_main_ports: true` using the inventory system.     |
| Plex (extras)     | TCP: 3005, 8324, 32469  <br><br> UDP: 1900, 5353, 8324, 32410, 32412, 32413, 32414                           | Non essential for remote servers. See [here](https://support.plex.tv/articles/201543147-what-network-ports-do-i-need-to-allow-through-my-firewall/){target=_blank}. <br><br> If ports need to be open, add the ones needed to `plex_docker_ports_custom: []` using the inventory system.      |
| Autoscan          | 3030                                         |                 |
| Tautulli            |                                              |                                                                                                                                            |
| Portainer           |                                              |                                                                                                                                            |
| Radarr              |                                              |                                                                                                                                            |
| Resilio Sync      | 55555                                        |                                                                                                                                            |
| qBittorrent       | 6881 (UDP), 51413                            |                                                                                                                                            |
| Sonarr              |                                              |                                                                                                                                            |
| Cloudplow           |                                              |                                                                                                                                            |
| Watchtower          |                                              |                                                                                                                                            |
| WebTools for Plex | 33400, 33443                                 |                                                                                                                                            |

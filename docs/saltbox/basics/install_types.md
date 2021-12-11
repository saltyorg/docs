# Saltbox Install Types

Saltbox consists of a "Core" with various extra components added onto that core.  At a minimum, you need to install "core" to do anything further with the Saltbox infrastructure.

|                                                                                                                                                                                                    |       `core`       |     `saltbox`     |     `mediabox`     |    `feederbox`     |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------:|:------------------:|:------------------:|:------------------:|
| System Tweaks                                                                                                                                                      |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |
| [Saltbox MOTD](https://github.com/saltyorg/motd)                                                                                                                   |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |
| Common Tools and Tasks                                                                                                                                             |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |
| [Docker](https://www.docker.com/community-edition)                                                                                                                 |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |
| [Rclone](https://rclone.org)                                                                                                                                       |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |
| Mounts: [MergerFS](https://github.com/trapexit/mergerfs)                                                                                                           |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |
| Mounts: [Rclone VFS](https://rclone.org/commands/rclone_mount/#vfs-virtual-file-system)                                                                            |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |
| Scripts                                                                                                                                                            |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |
| [Traefik](https://traefik.io/traefik/) ([Docker](https://hub.docker.com/_/traefik/))                                                                               |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |
| [Authelia](https://www.authelia.com/) ([Docker](https://hub.docker.com/r/authelia/authelia))                                                                       |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |    ![Yes][yes]     |
| [Plex](https://www.plex.tv) ([Docker](https://github.com/plexinc/pms-docker))                                                                                      |                    |    ![Yes][yes]     |    ![Yes][yes]     |                    |
| [Tautulli](http://tautulli.com/) ([Docker](https://github.com/Tautulli/Tautulli-Docker))                                                                           |                    |    ![Yes][yes]     |    ![Yes][yes]     |                    |
| [Overseerr](https://docs.overseerr.dev/)  ([Docker](https://github.com/sct/overseerr))                                                                             |                    |    ![Yes][yes]     |    ![Yes][yes]     |                    |
| [Plex Autoscan](https://github.com/l3uddz/plex_autoscan) (Media Scanner Helper Script)                                                                             |                    |    ![Yes][yes]     |    ![Yes][yes]     |                    |
| [Portainer](https://portainer.io) ([Docker](https://hub.docker.com/r/portainer/portainer/))                                                                        |                    |    ![Yes][yes]     |                    |    ![Yes][yes]     |
| [Organizr](https://github.com/causefx/Organizr) ([Docker](https://github.com/linuxserver/docker-organizr))                                                         |                    |    ![Yes][yes]     |                    |    ![Yes][yes]     |
| [Cloudplow](https://github.com/l3uddz/cloudplow) (Media Uploader)                                                                                                  |                    |    ![Yes][yes]     |                    |    ![Yes][yes]     |
| [NZBGet](https://nzbget.net) ([Docker](https://github.com/hotio/docker-nzbget))                                                                                    |                    |    ![Yes][yes]     |                    |    ![Yes][yes]     |
| [rTorrent](https://github.com/rakshasa/rtorrent) / [ruTorrent](https://github.com/Novik/ruTorrent) ([Docker](https://github.com/horjulf/docker-rutorrent-autodl))  |                    |    ![Yes][yes]     |                    |    ![Yes][yes]     |
| [Jackett](https://github.com/Jackett/Jackett) ([Docker](https://github.com/hotio/docker-jackett))                                                                  |                    |    ![Yes][yes]     |                    |    ![Yes][yes]     |
| [NZBHydra 2](https://github.com/theotherp/nzbhydra2) ([Docker](https://github.com/hotio/docker-nzbhydra2))                                                         |                    |    ![Yes][yes]     |                    |    ![Yes][yes]     |
| [Sonarr](https://sonarr.tv) ([Docker](https://github.com/hotio/docker-sonarr))                                                                                     |                    |    ![Yes][yes]     |                    |    ![Yes][yes]     |
| [Radarr](https://radarr.video) ([Docker](https://github.com/hotio/docker-radarr))                                                                                  |                    |    ![Yes][yes]     |                    |    ![Yes][yes]     |
| [Lidarr](https://lidarr.audio) ([Docker](https://github.com/hotio/docker-lidarr))                                                                                  |                    |    ![Yes][yes]     |                    |    ![Yes][yes]     |

  [yes]:../../images/check-mark.png
  [no]:../../images/cross-mark.png


Next, let's move on to [Installing Saltbox](../install/install.md).

<!--
:heavy_check_mark:
-->

# Saltbox Install Types

Saltbox consists of a "Core" with various extra components added onto that core.  At a minimum, you need to install "core" to do anything further with the Saltbox infrastructure.

|                                                                                                                      |     `core`    |   `saltbox`   |  `mediabox`   |  `feederbox`  |
|:---------------------------------------------------------------------------------------------------------------------|:-------------:|:-------------:|:-------------:|:-------------:|
| System Tweaks                                                                                                        |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |
| [Saltbox MOTD](https://github.com/saltyorg/motd)                                                                     |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |
| Common Tools and Tasks                                                                                               |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |
| [Docker](https://www.docker.com/community-edition)                                                                   |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |
| [Rclone](https://rclone.org)                                                                                         |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |
| Mounts: [MergerFS](https://github.com/trapexit/mergerfs)                                                             |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |
| Mounts: [Rclone VFS](https://rclone.org/commands/rclone_mount/#vfs-virtual-file-system)                              |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |
| Scripts                                                                                                              |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |
| [Traefik](https://traefik.io/traefik/) ([Docker](https://hub.docker.com/_/traefik/))                                 |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |
| [Authelia](https://www.authelia.com/) ([Docker](https://hub.docker.com/r/authelia/authelia))                         |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |  ![Yes][yes]  |
| [Plex](https://www.plex.tv) ([Docker](https://github.com/plexinc/pms-docker))                                        |               |  ![Yes][yes]  |  ![Yes][yes]  |               |
| [Tautulli](http://tautulli.com/) ([Docker](https://github.com/Tautulli/Tautulli-Docker))                             |               |  ![Yes][yes]  |  ![Yes][yes]  |               |
| [Overseerr](https://docs.overseerr.dev/)  ([Docker](https://github.com/sct/overseerr))                               |               |  ![Yes][yes]  |  ![Yes][yes]  |               |
| [Autoscan](https://github.com/Cloudbox/autoscan) (Media Scanner Helper Script)                                       |               |  ![Yes][yes]  |  ![Yes][yes]  |               |
| [Portainer](https://portainer.io) ([Docker](https://hub.docker.com/r/portainer/portainer/))                          |               |  ![Yes][yes]  |               |  ![Yes][yes]  |
| [Organizr](https://github.com/causefx/Organizr) ([Docker](https://github.com/linuxserver/docker-organizr))           |               |  ![Yes][yes]  |               |  ![Yes][yes]  |
| [Cloudplow](https://github.com/l3uddz/cloudplow) (Media Uploader)                                                    |               |  ![Yes][yes]  |               |  ![Yes][yes]  |
| [NZBGet](https://nzbget.net) ([Docker](https://github.com/hotio/docker-nzbget))                                      |               |  ![Yes][yes][^1]  |               |  ![Yes][yes]  |
| [Qbittorrent](https://github.com/qbittorrent/qBittorrent) ([Docker](https://hub.docker.com/r/saltydk/qbittorrent))   |               |  ![Yes][yes][^1]  |               |  ![Yes][yes]  |
| [Jackett](https://github.com/Jackett/Jackett) ([Docker](https://github.com/hotio/docker-jackett))                    |               |  ![Yes][yes][^1]  |               |  ![Yes][yes]  |
| [NZBHydra 2](https://github.com/theotherp/nzbhydra2) ([Docker](https://github.com/hotio/docker-nzbhydra2))           |               |  ![Yes][yes][^1]  |               |  ![Yes][yes]  |
| [Sonarr](https://sonarr.tv) ([Docker](https://github.com/hotio/docker-sonarr))                                       |               |  ![Yes][yes]  |               |  ![Yes][yes]  |
| [Radarr](https://radarr.video) ([Docker](https://github.com/hotio/docker-radarr))                                    |               |  ![Yes][yes]  |               |  ![Yes][yes]  |
| [Lidarr](https://lidarr.audio) ([Docker](https://github.com/hotio/docker-lidarr))                                    |               |  ![Yes][yes]  |               |  ![Yes][yes]  |

  [yes]:../../images/check-mark.png

[^1]:
    Note that these default download clients and indexers can be overridden with other saltbox tags [NOT SANDBOX] in the [inventory](../inventory/index.md).  If the tags do not exist in saltbox the install will fail.
    ```
    download_clients_enabled: ["qbittorrent", "nzbget"]
    download_indexers_enabled: ["jackett", "nzbhydra2"]
    ```


## Feederbox/Mediabox Setup Considerations

- If your servers will share a domain, it is preferred to run only one instance of Authelia. This can run either on the feederbox or mediabox as you may choose. The server that will host Authelia should be set as `master: yes` under `authelia:` in `settings.yml` - see [here](../install/install.md#__code_8_annotation_6).

- On the server hosting Authelia, it is advised to set the `traefik_trusted_ips` variable in your [Inventories](../inventory/index.md) file following the format below. This is for a mediabox hosting Authelia. If the feederbox will be hosting, the mediabox IP would be substituted.

  ```yaml
  traefik_trusted_ips: "feederboxIPV4/32,feederboxIPV6/64"
  ```

Next, let's move on to [Installing Saltbox](../install/install.md).

<!--
:heavy_check_mark:
-->

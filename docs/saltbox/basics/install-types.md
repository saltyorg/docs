---
hide:
  - tags
tags:
  - install
  - mediabox
  - feederbox
  - saltbox
  - tags
---

# Saltbox Install Types

Saltbox consists of a "Core" with various extra components added onto that core. At a minimum, you need to install "core" to do anything further with the Saltbox infrastructure.

|                                                                                                                      |     `core`    |   `saltbox`[^1]   |  `mediabox`[^1]   |  `feederbox`[^1]  |
|:---------------------------------------------------------------------------------------------------------------------|:-------------:|:-----------------:|:-----------------:|:-----------------:|
| System Tweaks                                                                                                        |  ![Yes][yes]  |  ![Yes][yes]      |  ![Yes][yes]      |  ![Yes][yes]      |
| [Saltbox MOTD](https://github.com/saltyorg/motd)                                                                     |  ![Yes][yes]  |  ![Yes][yes]      |  ![Yes][yes]      |  ![Yes][yes]      |
| Common Tools and Tasks                                                                                               |  ![Yes][yes]  |  ![Yes][yes]      |  ![Yes][yes]      |  ![Yes][yes]      |
| [Docker](https://www.docker.com/community-edition)                                                                   |  ![Yes][yes]  |  ![Yes][yes]      |  ![Yes][yes]      |  ![Yes][yes]      |
| [Rclone](https://rclone.org)                                                                                         |  ![Yes][yes]  |  ![Yes][yes]      |  ![Yes][yes]      |  ![Yes][yes]      |
| Mounts: [MergerFS](https://github.com/trapexit/mergerfs)                                                             |  ![Yes][yes]  |  ![Yes][yes]      |  ![Yes][yes]      |  ![Yes][yes]      |
| Mounts: [Rclone VFS](https://rclone.org/commands/rclone_mount/#vfs-virtual-file-system)                              |  ![Yes][yes]  |  ![Yes][yes]      |  ![Yes][yes]      |  ![Yes][yes]      |
| Scripts                                                                                                              |  ![Yes][yes]  |  ![Yes][yes]      |  ![Yes][yes]      |  ![Yes][yes]      |
| [Traefik](https://traefik.io/traefik/) ([Docker](https://hub.docker.com/_/traefik/))                                 |  ![Yes][yes]  |  ![Yes][yes]      |  ![Yes][yes]      |  ![Yes][yes]      |
| [Authelia](https://www.authelia.com/) ([Docker](https://hub.docker.com/r/authelia/authelia))                         |  ![Yes][yes]  |  ![Yes][yes]      |  ![Yes][yes]      |  ![Yes][yes]      |
| [Plex](https://www.plex.tv) ([Docker](https://github.com/plexinc/pms-docker))                                        |               |  ![Yes][yes][^2]  |  ![Yes][yes][^2]  |                   |
| [Tautulli](http://tautulli.com/) ([Docker](https://github.com/Tautulli/Tautulli-Docker))                             |               |  ![Yes][yes]      |  ![Yes][yes]      |                   |
| [Overseerr](https://docs.overseerr.dev/)  ([Docker](https://github.com/sct/overseerr))                               |               |  ![Yes][yes]      |  ![Yes][yes]      |                   |
| [Autoscan](https://github.com/Cloudbox/autoscan) (Media Scanner Helper Script)                                       |               |  ![Yes][yes]      |  ![Yes][yes]      |                   |
| [Portainer](https://portainer.io) ([Docker](https://hub.docker.com/r/portainer/portainer/))                          |               |  ![Yes][yes]      |                   |  ![Yes][yes]      |
| [Organizr](https://github.com/causefx/Organizr) ([Docker](https://github.com/linuxserver/docker-organizr))           |               |  ![Yes][yes]      |                   |  ![Yes][yes]      |
| [Cloudplow](https://github.com/l3uddz/cloudplow) (Media Uploader)                                                    |               |  ![Yes][yes]      |                   |  ![Yes][yes]      |
| [SABnzbd](https://sabnzbd.org/) ([Docker](https://github.com/hotio/docker-sabnzbd))                                  |               |  ![Yes][yes][^3]  |                   |  ![Yes][yes][^3]  |
| [Qbittorrent](https://github.com/qbittorrent/qBittorrent) ([Docker](https://hub.docker.com/r/saltydk/qbittorrent))   |               |  ![Yes][yes][^3]  |                   |  ![Yes][yes][^3]  |
| [Jackett](https://github.com/Jackett/Jackett) ([Docker](https://github.com/hotio/docker-jackett))                    |               |  ![Yes][yes][^3]  |                   |  ![Yes][yes][^3]  |
| [NZBHydra 2](https://github.com/theotherp/nzbhydra2) ([Docker](https://github.com/hotio/docker-nzbhydra2))           |               |  ![Yes][yes][^3]  |                   |  ![Yes][yes][^3]  |
| [Sonarr](https://sonarr.tv) ([Docker](https://github.com/hotio/docker-sonarr))                                       |               |  ![Yes][yes]      |                   |  ![Yes][yes]      |
| [Radarr](https://radarr.video) ([Docker](https://github.com/hotio/docker-radarr))                                    |               |  ![Yes][yes]      |                   |  ![Yes][yes]      |
| [Lidarr](https://lidarr.audio) ([Docker](https://github.com/hotio/docker-lidarr))                                    |               |  ![Yes][yes]      |                   |  ![Yes][yes]      |

  [yes]:../../images/check-mark.png

[^1]:
    Note that the default apps installed by each top-level tag can be overridden with other Saltbox roles (NOT SANDBOX) in the [inventory](../inventory/index.md). If the roles do not exist in Saltbox the install will fail.

    The relevant variables and their default values are:
    ```
    saltbox_roles: ["media_server", "download_clients", "download_indexers", "tautulli", "overseerr", "portainer", "organizr", "sonarr", "radarr", "lidarr", "iperf3", "nethogs", "glances", "btop"]
    mediabox_roles: ["media_server", "tautulli", "overseerr", "iperf3", "nethogs", "glances", "btop"]
    feederbox_roles: ["download_clients", "download_indexers", "portainer", "organizr", "sonarr", "radarr", "lidarr", "iperf3", "nethogs", "glances", "btop"]
    ```

[^2]:
    Note that the default media server(s) can be overridden with other Saltbox roles (NOT SANDBOX) in the [inventory](../inventory/index.md). If the roles do not exist in Saltbox the install will fail.

    The relevant variables and their default values are:
    ```
    media_servers_enabled: ["plex"]
    ```

[^3]:
    Note that these default download clients and indexers can be overridden with other Saltbox roles (NOT SANDBOX) in the [inventory](../inventory/index.md). If the roles do not exist in Saltbox the install will fail.

    The relevant variables and their default values are:
    ```
    download_clients_enabled: ["qbittorrent", "sabnzbd"]
    download_indexers_enabled: ["jackett", "nzbhydra2"]
    ```

As with any Ansible tags provided by saltbox, it is safe to run these install tag(s) at will. Existing configurations are not overwritten (except for some "reset" tags and the "mounts" tag).

## Feederbox/Mediabox Setup Considerations

- If your servers will share a domain, it is preferred to run only one instance of Authelia. This can run either on the Feederbox or Mediabox as you may choose. The server that will host Authelia should be set as `master: yes` under `authelia:` in `settings.yml` - see [Authelia configuration](../install/install.md#__tabbed_2_2).

- On the server hosting Authelia, it is advised to set the `traefik_trusted_ips` variable in your [Inventories](../inventory/index.md) file following the format below. This is for a Mediabox hosting Authelia. If the Feederbox will be hosting, the Mediabox IP would be substituted.

  ```yaml
  traefik_trusted_ips: "feederboxIPV4/32,feederboxIPV6/64"
  ```

Next, let's move on to [Installing Saltbox](../install/install.md).

<!--
:heavy_check_mark:
-->

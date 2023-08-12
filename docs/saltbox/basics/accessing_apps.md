# Accessing Saltbox Apps

_Note 1: After the initial setup, it will take a a while for the SSL certificates to propagate. A side effect of this will be that certain domains were redirect to other apps (e.g. sonarr.yourdomain.com -> nzbget.yourdomain.com). Just give it a bit of time and this will correct itself._

_Note 2: If pages don't load at all, make sure you've set up your [domain](../../reference/domain.md) properly and also checkout the [FAQ](../../faq/System.md)._

## Default Apps

Saltbox apps will be accessed via appname._yourdomain.com_ (see table below).

| **App  Name**          | **with domain**                           |
|:---------------------- |:----------------------------------------- |
| Jackett                | <https://jackett._yourdomain.com_>        |
| Lidarr                 | <https://lidarr._yourdomain.com_>         |
| NZBGet                 | <https://nzbget._yourdomain.com_>         |
| NZBHydra2              | <https://nzbhydra2._yourdomain.com_>      |
| Organizr               | <https://organizr._yourdomain.com_>       |
| Overseerr              | <https://overseerr._yourdomain.com_>      |
| Plex                   | <https://plex._yourdomain.com_>           |
| WebTools for Plex      | <https://plex-webtools._yourdomain.com_>  |
| Portainer              | <https://portainer._yourdomain.com_>      |
| Radarr                 | <https://radarr._yourdomain.com_>         |
| qbittorrent             | <https://qbittorrent._yourdomain.com_>     |
| Sonarr                 | <https://sonarr._yourdomain.com_>         |
| Tautulli               | <https://tautulli._yourdomain.com_>       |

## Additional Apps

Coming soon.

Next, let's discuss Saltbox' default [paths](paths.md).

# App Update

The info below will show you how to update your Saltbox apps, individually.

## Notes

- To update Saltbox as a whole (i.e. the core part and all the default roles), see [Updating Saltbox](../../saltbox/basics/update.md#updating-saltbox).

- Do not update the following apps within the app itself: Sonarr, Radarr, Lidarr, NZBGet, Ombi, Jackett, NZBHydra2, and Bazarr. If you do you may get the following error: `Update process failed: Cannot install update because startup folder '/app' is not writable by the user 'hotio'.`

## Update to a newer version

| Saltbox Apps  | How to update         |
|:------------- |:--------------------- |
| Plex          | [Ansible tag](../../saltbox/basics/update.md#updating-apps) |
| Tautulli      | [Ansible tag](../../saltbox/basics/update.md#updating-apps) |
| AutoScan      | [Ansible tag](../../saltbox/basics/update.md#updating-apps) |
| Sonarr        | [Ansible tag](../../saltbox/basics/update.md#updating-apps) |
| Radarr        | [Ansible tag](../../saltbox/basics/update.md#updating-apps) |
| NZBGet        | [Ansible tag](../../saltbox/basics/update.md#updating-apps) |
| qbittorrent    | [Ansible tag](../../saltbox/basics/update.md#updating-apps) |
| Jackett       | [Ansible tag](../../saltbox/basics/update.md#updating-apps) |
| NZBHydra2     | [Ansible tag](../../saltbox/basics/update.md#updating-apps) |
| Ombi          | [Ansible tag](../../saltbox/basics/update.md#updating-apps) |
| Organizr      | Update within the app |
| Portainer     | [Ansible tag](../../saltbox/basics/update.md#updating-apps) |
| Cloudplow     | [Ansible tag](../../saltbox/basics/update.md#updating-apps) |
| Emby          | [Ansible tag](../../saltbox/basics/update.md#updating-apps) |
<br />

**"How to update" options:**

- **"Ansible tag"**

   See the next section on how to update Saltbox apps via their Ansible tag.

- **"Update within the app"**

   You can simply update within the app itself. Changes will persist after docker restarts.

- **"Container restart"**

   This means that the Docker container will auto-update the app on container restart.  _Currently nothing in Saltbox is updated in this way._

   ```shell
   docker stop <name> && docker start <name>
   ```

   or

   ```shell
   docker restart <name>
   ```

   _Note: It's recommended to use `docker stop/start <container>` vs `docker restart <container>`, to prevent corrupting data, especially on apps like qbittorrent._

<br />

## Ansible tags to update apps

When in doubt, you can always rerun the relevant Ansible tag to update the app.

| Apps                        | Ansible Tags    |
|:--------------------------- |:--------------- |
| Plex                        | `plex`          |
| Tautulli                    | `tautulli`      |
| Sonarr                      | `sonarr`        |
| Radarr                      | `radarr`        |
| NZBGet                      | `nzbget`        |
| qbittorrent                  | `qbittorrent`     |
| Jackett                     | `jackett`       |
| NZBHydra2                   | `nzbhydra2`     |
| Autoscan                    | `autoscan`      |
| Ombi                        | `ombi`          |
| Organizr                    | `organizr`      |
| Portainer                   | `portainer`     |
| Watchtower                  | `watchtower`    |
| Cloudplow                   | `cloudplow`     |
| Emby                        | `emby`          |
| Traefik                     | `traefik`       |

**Instructions:**

1. Run the tag command:

   ```shell
   sb install TAG
   ```

   Replace `TAG` with one of the above tags from the table.

   You can also run multiple tags, by placing them next to each other, separated by a comma, without spaces (e.g. TAG1,TAG2).

   _Note: If the App is a docker container, running the update tag will rebuild and update the container._

   _Note: If you modified the container with flags like `plex_name`, you'll need to do the same thing here._

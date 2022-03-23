This guide will outline some basic steps to copy/move your Saltbox setup to another server and/or another domain name.

Listed below are some common scenarios and their migration instructions.

## Move Saltbox to Another Server and Keep the Same Domain Name

### Current Server

1. [Back up](backup.md) your current Saltbox server.

### New Server

1. [Restore](restore.md) Saltbox to the new server.

2. If you are not using Cloudflare:

    - Point your domain's [DNS](../prerequisites/prerequisites.md#domain) to the new server.

3. Install the relevant Saltbox type: [Saltbox, Mediabox, or Feederbox](../install/install.md#install-saltbox).

4. Install any extra, not-default containers you had installed previously from [Sandbox](../../sandbox/index.md) or on your own.

5. Check to see if your [Plex Autoscan URL](../../../apps/plex-autoscan/#obtaining-the-plex-autoscan-url) has changed and update [Sonarr](../../apps/sonarr.md), [Radarr](../../apps/radarr.md), and [Lidarr](../../apps/lidarr.md) accordingly, if you are using Plex Autoscan.

## Move Saltbox to Another Server and Change the Domain Name

### Current Server

1. [Back up](backup.md) your current Saltbox server.

### New Server

1. [Restore](restore.md) Saltbox to the new server.

2. Add your new domain name into [Settings](settings.md).

3. If you are using Cloudflare:

    1. Register your domain with [Cloudflare](../../faq/Cloudflare.md).

    2. Add the Cloudflare API into [Settings](settings.md).

4. If you are not using Cloudflare:

    - Point your domain's [DNS](../prerequisites/prerequisites.md#domain) to the new server.

5. Replace the domain name in app specific config files:

    - `/opt/cloudplow/config.json`

    - `/opt/emby/config/system.xml` (only if installed)

    - `/opt/motd/config.json`

    - `/opt/traktarr/config.json` (only if installed)

    - `/opt/plex_dupefinder/config.json` (only if installed)

    - `/opt/plex_patrol/settings.ini` (only if installed)

    - `/opt/sabnzbd/app/sabnzbd.ini` (only if installed)

3. Install the relevant Saltbox type: [Saltbox, Mediabox, or Feederbox](../install/install.md#install-saltbox).

7. Install any extra, not-default containers you had installed previously from [Sandbox](../../sandbox/index.md) or on your own.

5. Check to see if your [Plex Autoscan URL](../../../apps/plex-autoscan/#obtaining-the-plex-autoscan-url) has changed and update [Sonarr](../../apps/sonarr.md), [Radarr](../../apps/radarr.md), and [Lidarr](../../apps/lidarr.md) accordingly, if you are using Plex Autoscan.
6.
## Keep Saltbox on the Same Server but Change the Domain Name

1. [Back up](backup.md) your current Saltbox server.

2. Add your new domain name into [Settings](settings.md).

3. If you are using Cloudflare:

    1. Register your domain with [Cloudflare](../../faq/Cloudflare.md).

    2. Add the Cloudflare API into [Settings](settings.md).

4. If you are not using Cloudflare:

    - Point your domain's [DNS](../prerequisites/prerequisites.md#domain) to the new server.

5. Replace the domain name in app specific config files:

    - `/opt/cloudplow/config.json`

    - `/opt/emby/config/system.xml` (only if installed)

    - `/opt/motd/config.json`

    - `/opt/traktarr/config.json` (only if installed)

    - `/opt/plex_dupefinder/config.json` (only if installed)

    - `/opt/plex_patrol/settings.ini` (only if installed)

    - `/opt/sabnzbd/app/sabnzbd.ini` (only if installed)

3. Install the relevant Saltbox type: [Saltbox, Mediabox, or Feederbox](../install/install.md#install-saltbox).

7. Install any extra, not-default containers you had installed previously from [Sandbox](../../sandbox/index.md) or on your own.

5. Check to see if your [Plex Autoscan URL](../../../apps/plex-autoscan/#obtaining-the-plex-autoscan-url) has changed and update [Sonarr](../../apps/sonarr.md), [Radarr](../../apps/radarr.md), and [Lidarr](../../apps/lidarr.md) accordingly, if you are using Plex Autoscan.

---

# Tauticord

## What is it?

[Tauticord](https://github.com/nwithan8/tauticord) is a Discord bot that
will mirror live Tautulli data into a Discord server, including current stream and bandwidth information, library
statistics, and live playback control.

| Details                                                                                                                         |                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [:material-home: Project home](https://github.com/nwithan8/tauticord){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/nwithan8/tauticord){: .header-icons } |

Recommended install types: Mediabox, Saltbox

### 1. Installation

``` shell
sb install sandbox-tauticord
```

### 2. Setup

Rename `/opt/tauticord/config/config.yml.example` to `/opt/tauticord/config/config.yml` and fill out your configuration details.

See the [Tauticord documentation](https://github.com/nwithan8/tauticord#installation-and-setup) for more information on each setting.

### 3. Usage

Once started, Tauticord will connect to your Tautulli and Discord servers and begin mirroring data.

By default, library statistics are updated once every hour, and stream data is updated once every 15 seconds.

- [:octicons-link-16: Documentation: Tauticord Docs](https://github.com/nwithan8/tauticord){: .header-icons }

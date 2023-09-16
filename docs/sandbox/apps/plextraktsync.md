# PlexTraktSync

## What is it?

[PlexTraktSync](https://github.com/Taxel/PlexTraktSync) adds a two-way-sync between trakt.tv and Plex Media Server. It requires a trakt.tv account but no Plex premium and no Trakt VIP subscriptions, unlike the Plex app provided by Trakt.

| Details     |
|-------------|
| [:octicons-mark-github-16: Github](https://github.com/Taxel/PlexTraktSync){: .header-icons } |

Recommended install types: Mediabox, Saltbox

### 1. Installation

``` shell
sb install sandbox-plextraktsync
```

### 2. Setup

Set your general preferences in `/opt/plextraktsync/config.yml`.

The following command will launch an interactive script prompting you for missing credentials (use this to set up Trakt.tv):

```shell
docker exec -it plextraktsync plextraktsync login
```

By default, the target Plex server is set to your main Plex Saltbox instance, and the sync user is set to that server's owner account. If you wish to reset this, run:

```shell
docker exec -it plextraktsync plextraktsync plex-login
```

### 3. Usage

Unattended, the PlexTraktSync instance's only task is to listen to your configured user's Plex activity and scrobble it.

The following will perform a one-time sync of the data you have specified in the configuration file.

```shell
docker exec -it plextraktsync plextraktsync sync
```

To get a list of commands, run:

```shell
docker exec -it plextraktsync plextraktsync --help
```

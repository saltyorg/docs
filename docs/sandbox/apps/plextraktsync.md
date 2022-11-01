# PlexTraktSync

## What is it?

[PlexTraktSync](https://github.com/Taxel/PlexTraktSync){: target=_blank rel="noopener noreferrer" } adds a two-way-sync between trakt.tv and Plex Media Server. It requires a trakt.tv account but no Plex premium and no Trakt VIP subscriptions, unlike the Plex app provided by Trakt.

| Details     |
|-------------|
| [:octicons-mark-github-16: Github](https://github.com/Taxel/PlexTraktSync){: .header-icons target=_blank rel="noopener noreferrer" } |

Recommended install types: Mediabox, Saltbox

### 1. Installation

``` shell
sb install sandbox-plextraktsync
```

### 2. Setup

Set your general preferences in `/opt/plextraktsync/config.yml`.

The following command will launch an interactive script prompting you for missing credentials (use this to set up Trakt.tv):

```shell
docker exec -it plextraktsync python3 -m plextraktsync login
```

By default, the target Plex server is set to your main Plex Saltbox instance, and the sync user is set to that server's owner account. If you wish to reset this, run:

```shell
docker exec -it plextraktsync python3 -m plextraktsync plex-login
```

Most of these fields can be manually edited in `/opt/plextraktsync/.env`.

### 3. Usage

By default, the PlexTraktSync instance's only assignment is to listen to your configured user's Plex activity and scrobble it. You may also wish to sync your backlog on a schedule, for example, by adding a crontab line containing `docker exec plextraktsync python3 -m plextraktsync`.

To get a list of commands, run:
```shell
docker exec -it plextraktsync python3 -m plextraktsync --help
```

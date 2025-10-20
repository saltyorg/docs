---
hide:
  - tags
tags:
  - plextraktsync
  - trakt.tv
---

# PlexTraktSync

Self-hosted application that adds a two-way-sync between trakt.tv and Plex Media Server. It requires a trakt.tv account but no Plex premium and no Trakt VIP subscriptions, unlike the Plex app provided by Trakt.

<div class="grid sb-buttons" markdown data-search-exclude>

[:material-home: Homepage&nbsp;&nbsp;](https://github.com/Taxel/PlexTraktSync){ .md-button .md-button--stretch }

[:material-bookshelf: Manual&nbsp;&nbsp;](https://github.com/Taxel/PlexTraktSync/blob/main/README.md#setup){ .md-button .md-button--stretch }

[:octicons-container-16: Releases&nbsp;&nbsp;](https://github.com/taxel/PlexTraktSync/pkgs/container/plextraktsync){ .md-button .md-button--stretch }

[:fontawesome-brands-github: Community&nbsp;&nbsp;](https://github.com/Taxel/PlexTraktSync/discussions){ .md-button .md-button--stretch }

</div>

---

## Deployment

``` shell
sb install sandbox-plextraktsync
```

## Configuration

Sync preferences are available to customize in `/opt/plextraktsync/config.yml`.

The following command will launch an interactive script prompting you for missing credentials (use this to set up Trakt.tv):

```shell
docker exec -it plextraktsync plextraktsync login
```

???+ info "Plex"
    The target Plex server is initially set to your main Plex Saltbox instance using the owner account. To reset these credentials:
    ```shell
    docker exec -it plextraktsync plextraktsync plex-login
    ```

## Usage

### Daemon

Once configured, the selected Plex user's streaming activity is automatically scrobbled.

### CLI

To perform a one-time sync of the data you have specified in the configuration file:

```shell
docker exec plextraktsync plextraktsync sync
```

To get a list of available commands:

```shell
docker exec plextraktsync plextraktsync --help
```

<!-- BEGIN SALTBOX MANAGED VARIABLES SECTION -->
<!-- This section is managed by saltbox/test.py - DO NOT EDIT MANUALLY -->
<!-- END SALTBOX MANAGED VARIABLES SECTION -->
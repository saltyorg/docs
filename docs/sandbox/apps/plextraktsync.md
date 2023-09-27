# PlexTraktSync

[PlexTraktSync](https://github.com/Taxel/PlexTraktSync) adds a two-way-sync between Trakt and Plex Media Server. It requires a Trakt account but no Plex Pass and no Trakt VIP membership, contrary to the Plex app provided by Trakt.

<div class="grid" style="grid-template-columns: repeat(auto-fit,minmax(10.5rem,1fr));" markdown>

[:material-bookshelf: Project Docs](https://github.com/Taxel/PlexTraktSync#setup){ .md-button .md-button--stretch }

[:material-github: GitHub Repo](https://github.com/Taxel/PlexTraktSync){ .md-button .md-button--stretch }

[:material-cube: GitHub Packages](https://github.com/taxel/PlexTraktSync/pkgs/container/plextraktsync){ .md-button .md-button--stretch }

</div>

## Deployment

``` shell
sb install sandbox-plextraktsync
```

## Configuration

Set your general preferences in `/opt/plextraktsync/config.yml`.

The following command will launch an interactive script prompting you for missing credentials (use this to set up Trakt.tv):

```shell
docker exec -it plextraktsync plextraktsync login
```

By default, the target Plex server is set to your main Plex Saltbox instance, and the sync user is set to that server's owner account. If you wish to reset this, run:

```shell
docker exec -it plextraktsync plextraktsync plex-login
```

## Usage

Once configured, the daemon simply scrobbles the selected Plex user's streaming activity.

The following will perform a one-time sync of the data you have specified in the configuration file.

```shell
docker exec -it plextraktsync plextraktsync sync
```

To get a list of commands, run:

```shell
docker exec -it plextraktsync plextraktsync --help
```

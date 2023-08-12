THIS PAGE HAS NOT BEEN FULLY UPDATED FOR SALTBOX

# What is it?

[ruTorrent](https://github.com/Novik/ruTorrent) (by Novik) is a front-end for the popular, lightweight, and extensible BitTorrent client [rtorrent](https://github.com/rakshasa/rtorrent) (by Jari Sundell aka rakshasa).

_Note: public trackers are disabled by default in the standard install.  Refer to the FAQ for [instructions on re-enabling them](https://docs.saltbox.dev/faq/ruTorrent/?h=public#enable-access-to-public-torrent-trackers)._

| Details     |             |             |             |             |
|-------------|-------------|-------------|-------------|-------------|
| :material-home: Project home | [:octicons-link-16: Docs](https://github.com/Novik/ruTorrent/wiki){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github ruTorrent](https://github.com/Novik/ruTorrent){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github rTorrent](https://github.com/rakshasa/rtorrent){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/horjulf/rutorrent-autodl){: .header-icons target=_blank rel="noopener noreferrer" }|

## 1. URL

- To access ruTorrent, visit `https://rutorrent._yourdomain.com_`

## 2. Basics

### Setup

The setup for [Sonarr](sonarr.md#rutorrent), [Radarr](radarr.md#rutorrent), and [Lidarr](lidarr.md#rutorrent) are done on their respective wiki pages.

## 3. Enable AutoUnpack

AutoUnpack is a plugin that will automatically unrar/unzip torrent data.

_This will allow Sonarr/Radarr/Lidarr to import the media files that would otherwise be ignored. After Sonarr and Radarr import the media files, [Torrent Cleanup Script](../reference/saltbox-tools.md#torrent-cleanup-script) will then delete the extracted media files and ruTorrent will continue to seed the torrents (until they are either removed manually or automatically via ruTorrent's Ratio Group rules)._

To enable AutoUnpack:

1. Open "Settings" by clicking the gear icon ![](https://github.com/Novik/ruTorrent/wiki/images/icon06settings.png) at the top

2. Go to "Unpack" on the left.

3. Check "Enable autounpacking if torrents label matches filter" and add the following:

```text
   /.*(radarr|sonarr|lidarr).*/i
```

4. Leave the other fields blank.

5. Your settings will now look like this:

   ![](https://i.imgur.com/LqE16E1.png)

6. Click "OK".

## 3. Custom Plugins and Themes

You can have custom plugins and themes imported during Docker container rebuild. Just place them in the following paths:

```text
/opt/rutorrent/plugins/
```

```text
/opt/rutorrent/themes/
```

And then restart the Docker container:

```bash
docker restart rutorrent
```

## 4. Next

Are you setting Saltbox up for the first time?  Continue to [NZBHydra2](nzbhydra2.md).

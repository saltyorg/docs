[ruTorrent](https://github.com/Novik/ruTorrent) (by Novik) is a front-end for the popular, lightweight, and extensible BitTorrent client [rtorrent](https://github.com/rakshasa/rtorrent) (by Jari Sundell aka rakshasa).

_Note: public trackers are disabled by default in the standard install.  Refer to the FAQ for [instructions on re-enabling them](https://github.com/Cloudbox/Cloudbox/wiki/FAQ#enable-access-to-public-torrent-trackers)._

![](https://i.imgur.com/30dxlTc.png)

## 1. URL

- To access ruTorrent, visit https://rutorrent._yourdomain.com_

## 2. Basics


### Login
Login settings are preset out of the box (`user` / `passwd` as set in [[accounts.yml|Install: accounts.yml]]).

_Note: If you need to change the password after installing Cloudbox, see the [[FAQ|FAQ#change-rutorrent-password-after-installation]]._

### Setup

The setup for [[Sonarr|Install: Sonarr#rutorrent]], [[Radarr|Install: Radarr#rutorrent]], and [[Lidarr|Install: Lidarr#rutorrent]] are done on their respective wiki pages.

## 3. Enable AutoUnpack

AutoUnpack is a plugin that will automatically unrar/unzip torrent data. 

_This will allow Sonarr/Radarr/Lidarr to import the media files that would otherwise be ignored. After Sonarr and Radarr import the media files, [[Torrent Cleanup Script|Reference: Cloudbox-Tools#torrent-cleanup-script]] will then delete the extracted media files and ruTorrent will continue to seed the torrents (until they are either removed manually or automatically via ruTorrent's Ratio Group rules)._

To enable AutoUnpack:

1. Open "Settings" by clicking the gear icon ![](https://github.com/Novik/ruTorrent/wiki/images/icon06settings.png) at the top

1. Go to "Unpack" on the left. 

1. Check "Enable autounpacking if torrents label matches filter" and add the following:

   ```
   /.*(radarr|sonarr|lidarr).*/i
   ```

1. Leave the other fields blank. 

1. Your settings will now look like this:

   ![](https://i.imgur.com/LqE16E1.png)

1. Click "OK". 


## 3. Custom Plugins and Themes

You can have custom plugins and themes imported during Docker container rebuild. Just place them in the following paths:

```
/opt/rutorrent/plugins/
```

```
/opt/rutorrent/themes/
```

And then restart the Docker container:

```
docker restart rutorrent
```

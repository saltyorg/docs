# Intro

[Lidarr](https://lidarr.audio) is basically Sonarr for music. It functions as a music collection manager for Usenet and BitTorrent users. It can monitor multiple RSS feeds from Bittorrent trackers and Usenet Indexers, looking for new tracks from your favorite artists and will grab, sort and rename them. It can also be configured to automatically upgrade the quality of files already downloaded when a better quality format becomes available.

![](https://i.imgur.com/MZJEij2.png)

# URL

- To access Lidarr, visit https://lidarr._yourdomain.com_

# Settings

## General

1. Go to "Settings" -> "General".

1. Set "Advanced Settings": `Shown`

### Host

- "Bind Address: `*`

- "Port Number": `8686`

- "URL Base": _blank_

- "Enable SSL": `No` (_SSL is handled by Traefik_)

- "Open browser on start": `No`

### Proxy Settings

- "Use Proxy": `No`

### Logging

- "Log Level": `Debug`

### Analytics

- "Send Anonymous Usage Data": `No` (_your preference_)

### Updates

- "Branch": `develop`

- "Automatic": `Off`

### Save

- Click "Save".


## Media Management

1. Click "Settings" -> "Media Management".

1. Enable "Rename Tracks".

1. Enable "Replace Illegal Characters".

1. Set your preferred naming format (you can use the ones mentioned below).

   <details>
   <summary>Plex's Naming Preference</summary> <br />

      Example: <br />
      `01 - Shine On You Crazy Diamond (Parts I-V).m4a`

      Standard Track Format: <br />
      `{track:00} - {Track Title}`

      Artist Folder Format: <br />
      `{Artist Name}`

      Album Folder Format: <br />
      `{Artist Name} - {Album Title}`

      Ref: https://support.plex.tv/articles/categories/media-preparation/naming-and-organizing-music-media/  <br />
   </details>

1. Disable "Analyse audio files".

1. Click "Save".


## Download Client

1. Click "Settings" -> "Download Client".

1. "Completed Download Handling": `Enabled` Selected (_your preference_)

1. "Failed Download Handling": `Redownload` Selected.


### NZBGet

1. Add a new "NZBGet" download client.

1. Add the following:

   1. Name: NZBGet

   1. Enable: `Yes`

   1. Host: `nzbget`

   1. Port: `6789`

   1. Username:  [[Your NZBGet Username|Install: NZBGet#security]]

   1. Password:  [[Your NZBGet Password|Install: NZBGet#security]]

   1. Category: `lidarr`

   1. Use SSL: `No`

   1. Add Paused: `No`

1. Your settings will now look like this:

    ![Lidarr NZBGet Downloader](https://i.ibb.co/LgDYFWT/image.png)

1. Click "Save" to add NZBGet.


### ruTorrent

1. Add a new "rTorrent" download client.

1. Add the following:

   1. Name: ruTorrent

   1. Enable: `Yes`

   1. Host: `rutorrent`

   1. Port: `80`

   1. URL Path: `RPC2`

   1. Use SSL: `No`

   1. Username: [[Your ruTorrent Username|Install: ruTorrent#login]]

   1. Password: [[Your ruTorrent Password|Install: ruTorrent#login]]

   1. Category: `lidarr`

   1. Directory: _Leave Blank_

1. Your settings will look like this:

   ![Lidarr ruTorrent Downloader](https://i.imgur.com/NbWHz3c.png)

1. Click "Save" to add ruTorrent.



## Indexers

1. Go to "Settings" -> "Indexers".

1. Set "Advanced Settings": `Shown`

1. Add in your your favorite [[indexers|Prerequisites: Usenet vs BitTorrent]].


### NZBHydra2

1. Click "Settings" -> "Indexers".

2. Click Add Indexer (`+`).

3. Select "Newznab".

4. Add the following:

   1. Name: NZBHydra2

   1. Enable RSS Sync: _Your Preference_

   1. Enable Search: _Your Preference_

   1. URL: `http://nzbhydra2:5076`

   1. API Path: `/api`

   1. API Key: [[Your NZBHydra2 API Key|Install: NZBHydra2#7-api-key]]

   1. Additional Parameters: _Leave Blank_

5. Your settings will look like this:

    ![Lidarr NZBHydra2](https://i.imgur.com/isxTYGV.png)

6. Click "Save" to add NZBHydra2.

Note: The "Test" will keep failing until you add an indexer in [[NZBHydra2|Install: NZBHydra2]].

### Jackett

Note: Each Indexer will need to be added separately.

1. Click "Settings" -> "Indexers".

1. Click Add Indexer (`+`)

1. Select "Torznab".

1. Add the following:

   1. Name: Indexer's Name

   1. Enable RSS Sync: _Your Preference_

   1. Enable Search: _Your Preference_

   1. URL: [[Indexer's Torznab Feed|Install: Jackett#3-adding-indexers-to-sonarrradarr]]

   1. API Path: `/api`

   1. API Key: [[Your Jackett API Key|Install: Jackett#3-adding-indexers-to-sonarrradarr]]

   1. Additional Parameters: _Leave Blank_

1. Your settings will look like this:

    ![Lidarr Jackett](https://i.imgur.com/bOhRdSL.png)


1. Click "Save" to add the indexer.


## Connect

### Torrent Cleanup

Torrent Cleanup Script is a custom script that will cleanup torrents from ruTorrent that were auto-extracted, but still being seeded. So if the script detects that `.rar` files are in the folder that Lidarr just imported from, it will delete the imported video file(s), leaving just the `.rar` files for seeding.

1. Click "Settings" -> "Connect".

1. Add a new "Custom Script".

1. Add the following:

   1. Name: Torrent Cleanup

   1. On Grab: `No`

   1. On Download: `Yes`

   1. On Upgrade:  `Yes`

   1. On Rename:`No`

   1. Path: `/scripts/torrents/TorrentCleanup.py`

1. The settings will look like this:

   ![Lidarr Torrent Cleanup Script CloudBox](https://i.imgur.com/i5OsaWi.png)

1. Click "Save" to add the Torrent Cleanup script.


### Plex Autoscan
**Plex Autoscan no longers work with music libraries as of version 1.18, so this feature will not work.**
1. Click "Settings" -> "Connect".

1. Add a new "Webhook".

1. Add the following:

   1. Name: Plex Autoscan

   1. On Grab: `No`

   1. On Download: `Yes`

   1. On Upgrade:  `Yes`

   1. On Rename: `Yes`

   1. URL: [[Your Plex Autoscan URL|Install: Plex-Autoscan#4-obtaining-the-plex-autoscan-url]]

   1. Method:`POST`

   1. Username: _Leave Blank_

   1. Password: _Leave Blank_



1. The settings will look like this:

    ![Lidarr Plex Autoscan](https://i.imgur.com/58MCXxM.png)


1. Click "Save" to add Plex Autoscan.

## Music Path

1. When you are ready to add your first artist to Lidarr, click the "Path" drop-down and select "Add a different path".

1. Click the blue "Browse" button, navigate to `/mnt/unionfs/Media/Music`, scroll to the bottom, and select "OK".

1. Click the green "check" button to add the path.

1. All artist added now will have that path set.


## API Key

This is used during the setup of [[Organizr|Install: Organizr]].

* Go to "Settings" -> "General" -> "Security" -> "API Key".

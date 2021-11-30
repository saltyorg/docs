
# URL

- To access Sonarr, visit https://sonarr._yourdomain.com_

#. Settings

## General

1. Go to "Settings" -> "General".

1. Set "Advanced Settings": `Shown`

### Start-Up

- "Bind Address: `*`

- "Port Number": `8989`

- "URL Base": _blank_

- "Enable SSL": `No` (_SSL is handled by Nginx-Proxy_)

- "Open browser on start": `No` [This setting does not appear in Sonarr v3]

### Proxy Settings

- "Use Proxy": `No`

### Logging

- "Log Level": `Debug`


### Analytics

- "Enable": `No` (_your preference_)

### Updates

- "Branch": `phantom-develop`

- "Automatic": `Off`

### Save

- Click "Save".



## Media Management

1. Go to "Settings" -> "Media Management".

1. Set "Advanced Settings": `Shown`


### Episode Naming

- "Rename Episodes": `Yes`

- "Replace Illegal Characters": `Yes`

- Set your preferred naming format (you can use the ones mentioned below - CLICK to expand).

   <details>
   <summary>Plex's Naming Preference</summary> <br />

    Example: <br />
    ```
    /Gotham/Season 01/Gotham - s01e01 - Pilot.mkv
    ```

    Standard Episode Format: <br />
    ```
    {Series Title} - s{season:00}e{episode:00} - {Episode Title}
    ```

    Anime Episode Format: <br />
    ```
    {Series Title} - s{season:00}e{episode:00} - {Episode Title}
    ```

    Daily Episode Format: <br />
    ```
    {Series Title} - {Air-Date} - {Episode Title}
    ```

    Season Folder Format: <br />
    ```
    Season {season:00}
    ```

    Multi-Episode Style: <br />
    ```
    Prefixed Range
    ```

    Reference: https://support.plex.tv/articles/200220687-naming-series-season-based-tv-shows/  <br />
   </details><br />


   <details>
   <summary>TRaSH' naming guide</summary> <br />

    Example:  <br />
    ```
    Single Episode:

    The Series Title! (2010) - S01E01 - Episode Title 1 [AMZN WEBDL-1080p Proper][HDR][10bit][x264][DTS 5.1]-RlsGrp

    Multi Episode:

    The Series Title! (2010) - S01E01-E02-E03 - Episode Title [AMZN WEBDL-1080p Proper][HDR][10bit][x264][DTS 5.1]-RlsGrp
    ```

    Standard Episode Format: <br />
    ```
    {Series TitleYear} - S{season:00}E{episode:00} - {Episode CleanTitle} [{Preferred Words }{Quality Full}]{[MediaInfo VideoDynamicRange]}[{MediaInfo VideoBitDepth}bit]{[MediaInfo VideoCodec]}{[Mediainfo AudioCodec}{ Mediainfo AudioChannels]}{MediaInfo AudioLanguages}{-Release Group}
    ```

    for more examples and discussion see the reference: https://trash-guides.info/Sonarr/Sonarr-recommended-naming-scheme/
   </details><br />



### Folders

- "Create empty series folders": `No`

- "Delete empty folders": `No`


### Importing

- "Skip Free Space Check": `No`

- "Use Hardlinks instead of Copy": `No`

- "Import Extra Files": `Yes` (_can be your preference_)

- "Extra File Extensions": `srt, sub, idx`

### File Management

- "Ignore Deleted Episodes": `No` (_can be your preference_)

- "Download Propers": `Yes` (_can be your preference_)

- "Analyse video files": `No`

- "Change File Date": `None`

- "Recycle Bin": _blank_ (Rclone deletes are sent to Gdrive trash folder, anyway)


### Permissions

- Set Permissions: `No`

### Save

- Click "Save".


## Download Client

1. Go to "Settings" -> "Download Client".

1. Completed Download Handling

   - Enable: `Yes`

   - Remove: `Yes` (_your preference_)

1. Failed Download Handling

   - Redownload: `Yes`

   - Remove: `Yes`



### NZBGet

1. Add a new "NZBGet" download client.

1. Add the following:

   1. Name: NZBGet

   1. Enable: `Yes`

   1. Host: `nzbget`

   1. Port: `6789`

   1. Username:  [[Your NZBGet Username|Install: NZBGet#security]]

   1. Password:  [[Your NZBGet Password|Install: NZBGet#security]]

   1. Category: `sonarr`

   1. Use SSL: `No`

   1. Add Paused: `No`

1. Your settings will now look like this:

    ![Sonarr NZBGet Downloader](https://i.imgur.com/2wUO8l2.png)

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

   1. Category: `sonarr`

   1. Directory: _Leave Blank_

1. Your settings will look like this:

   ![Sonarr ruTorrent Downloader](https://i.imgur.com/LPGPXHc.png)

1. Click "Save" to add ruTorrent.



## Indexers

1. Go to "Settings" -> "Indexers".

1. Set "Advanced Settings": `Shown`

1. Add in your your favorite [[indexers|Prerequisites: Usenet vs BitTorrent]].


### NZBHydra2

1. Click Add Indexer (`+`).

1. Select "Newznab".

1. Add the following:

   1. Name: NZBHydra2

   1. Enable RSS Sync: _Your Preference_

   1. Enable Search: _Your Preference_

   1. URL: `http://nzbhydra2:5076`

   1. API Path: `/api`

   1. API Key: [[Your NZBHydra2 API Key|Install: NZBHydra2#4-api-key]]

   1. Additional Parameters: _Leave Blank_

1. Your settings will look like this:

    ![Sonarr NZBHydra2](https://i.imgur.com/gPJu1Ur.png)

1. Click "Save" to add NZBHydra2.

Note: The "Test" will keep failing until you add an indexer in [[NZBHydra2|Install: NZBHydra2]].

### Jackett

Note: Each Indexer will need to be added separately.

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

    (Note that the screenshot shows an `https` URL; this is incorrect.  It should be `http` as described above)

    ![Sonarr Jackett](https://i.imgur.com/cdFUhnd.png)


1. Click "Save" to add the indexer.

## v. Connect

1. Go to "Settings" -> "Connect".

1. Set "Advanced Settings": `Shown`


### Torrent Cleanup

Torrent Cleanup Script is a custom script that will cleanup torrents from ruTorrent that were auto-extracted, but still being seeded. So if the script detects that `.rar` files are in the folder that Sonarr just imported from, it will delete the imported video file(s), leaving just the `.rar` files for seeding.


<!--
If the script detects that `.rar` files are in the folder that Sonarr just imported from, it will delete the imported video file(s), leaving just the `.rar` files for seeding.
-->


1. Add a new "Custom Script".

1. Add the following:

   1. Name: Torrent Cleanup

   1. On Grab: `No`

   1. On Download: `Yes`

   1. On Upgrade:  `Yes`

   1. On Rename:`No`

   1. Path: `/scripts/torrents/TorrentCleanup.py`

1. The settings will look like this:

   ![Sonarr Torrent Cleanup Script CloudBox](https://i.imgur.com/JHgExVI.png)

1. Click "Save" to add the Torrent Cleanup script.


### Plex Autoscan

1. Add a new "Webhook".

1. Add the following:

   1. Name: Plex Autoscan

   1. On Grab: `No`

   1. On Download: `Yes`

   1. On Upgrade:  `Yes`

   1. On Rename: `Yes`

   1. Filter Series Tags: _Leave Blank_

   1. URL: [[Your Plex Autoscan URL|Install: Plex-Autoscan#4-obtaining-the-plex-autoscan-url]]

   1. Method:`POST`

   1. Username: _Leave Blank_

   1. Password: _Leave Blank_



1. The settings will look like this:

    ![Sonarr Plex Autoscan](https://i.imgur.com/NLtXVZJ.png)


1. Click "Save" to add Plex Autoscan.

## TV Path

1. When you are ready to add your first show to Sonarr, click the "Path" drop-down and select "Add a different path".

2. Click the blue "Browse" button, navigate to `/mnt/unionfs/Media/TV`, scroll to the bottom, and select "OK".

3. Click the green "check" button to add the path.

4. All TV shows added now will have that path set.


## API Key

This is used during the setup of [Overseer](overseerr.md) and [Organizr](organizr.md).

* Go to "Settings" -> "General" -> "Security" -> "API Key".

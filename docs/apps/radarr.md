<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:0 orderedList:0 -->



- [1. URL](#1-url)
- [2. Settings](#2-settings)
  - [i. General](#i-general)
    - [Start-Up](#start-up)
    - [Security](#security)
    - [Proxy Settings](#proxy-settings)
    - [Logging](#logging)
    - [Analytics](#analytics)
    - [Updates](#updates)
    - [Save](#save)
  - [ii. Media Management](#ii-media-management)
    - [Movie Naming](#movie-naming)
    - [Folders](#folders)
    - [Importing](#importing)
    - [File Management](#file-management)
    - [Permissions](#permissions)
    - [Save](#save-1)
  - [iii. Download Client](#iii-download-client)
    - [NZBGet](#nzbget)
    - [ruTorrent](#rutorrent)
  - [iv. Indexers](#iv-indexers)
    - [NZBHydra2](#nzbhydra2)
    - [Jackett](#jackett)
  - [v. Connect](#v-connect)
    - [Torrent Cleanup](#torrent-cleanup)
    - [Plex Autoscan](#plex-autoscan)
  - [3. Movies Path](#3-movies-path)
  - [4. API Key](#4-api-key)


<!-- /TOC -->

---


# 1. URL

- To access Radarr, visit https://radarr._yourdomain.com_

# 2. Settings


## i. General

1. Go to "Settings" -> "General".

1. Set "Advanced Settings": `Shown`

### Start-Up

- "Bind Address: `*`

- "Port Number": `7878`

- "URL Base": _blank_

- "Enable SSL": `No` (_SSL is handled by Nginx-Proxy_)

- "Open browser on start": `No`

### Security

- "Authentication": `Forms (Login page)` (_can also be set to `Basic (Browser popup)`_)

- "Username": _your Radarr username_

- "Password": _your Radarr password_



### Proxy Settings

- "Use Proxy": `No`

### Logging

- "Log Level": `Debug`

### Analytics

- "Enable": `No` (_your preference_)

### Updates

- "Branch": `nightly` or `develop`

- "Automatic": `Off`

### Save

- Click "Save".

## ii. Media Management

1. Go to "Settings" -> "Media Management".

1. Set "Advanced Settings": `Shown`


### Movie Naming

- "Rename Movies": `Yes`

- "Replace Illegal Characters": `Yes`

- Colon Replacement Format: `Delete`
  
  _Note: You could use `Replace with Space Dash` but only if your file naming format is not using spaces (e.g. using dots) to separate words._ 

- Set your preferred naming format (you can use the ones mentioned below - CLICK to expand).

   <details>
   <summary>Plex's Naming Preference</summary> <br />

    Example: <br />
    ```
    /Guardians of the Galaxy (2014)/Guardians of the Galaxy (2014).mkv
    ```

    Standard Movie Format: <br />
    ```
    {Movie Title} ({Release Year})
    ```

    Movie Folder Format: <br />
    ```
    {Movie Title} ({Release Year})
    ```

    Reference: https://support.plex.tv/articles/200381023-naming-movie-files/  <br />
   </details><br />


   <details>
   <summary>Radarr's Wiki Example</summary> <br />

    Example:  <br />
    ```
    The Movie Title (2010) - [ULTIMATE EXTENDED EDITION][BLURAY-1080P PROPER][DTS 5.1][X264]-EVOLVE.mkv
    ```

    Standard Movie Format: <br />
    ```
    {Movie Title} ({Release Year}) - {[EDITION TAGS]}{[QUALITY FULL]}{[MEDIAINFO AUDIOCODEC}{ MEDIAINFO AUDIOCHANNELS]}{[MEDIAINFO VIDEOCODEC]}{-RELEASE GROUP}
    ```

    Reference: https://github.com/Radarr/Radarr/wiki/Sorting-and-Renaming
   </details><br />


   <details>
   <summary>Desimaniac's Naming Guide</summary> <br />

    Example:  <br />
    ```
    /Guardians of the Galaxy (2014)/Guardians.of.the.Galaxy.2014.1080p.BluRay.x264-SPARKS.mkv
    ```

    Reference: https://github.com/desimaniac/docs/blob/master/my_sonarr_and_radarr_naming_guide.md
   </details>





### Folders

- "Create empty movie folders": `No`

- "Automatically Rename Folders": `No`

- "Movie Paths Default to Static": `No`

### Importing

- "Skip Free Space Check": `No`

- "Use Hardlinks instead of Copy": `No`

- "Import Extra Files": `Yes` (_can your preference_)

- "Extra File Extensions": `srt, sub, idx`

### File Management

- "Ignore Deleted Movies": `No` (_can be your preference_)

- "Download Propers": `No` (_can be your preference_)

- "Analyse video files": `No`

- "Change File Date": `None`

- "Recycle Bin": _blank_ (Rclone deletes are sent to Gdrive trash folder, anyway)

### Permissions

- Set Permissions: `No`

### Save

- Click "Save".

## iii. Download Client

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

   1. Category: `radarr`

   1. Use SSL: `No`

   1. Add Paused: `No`

1. Your settings will look like this:

    ![Radarr NZBGet Downloader](https://i.imgur.com/PxgKer9.png)

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

   1. Category: `radarr`

   1. Directory: _Leave Blank_

1. Your settings will now look like this:

    ![Radarr ruTorrent Downloader](http://i.imgur.com/XHB6NN2.png)

1. Click "Save" to add ruTorrent.



## iv. Indexers

1. Go to "Settings" -> "Indexers".

1. Set "Advanced Settings": `Shown`

1. Add in your your favorite [[indexers|Prerequisites: Usenet vs BitTorrent]].


### NZBHydra2

1. Click "Settings" -> "Indexers".

1. Click Add Indexer (`+`).

1. Select "Newznab".

1. Add the following:

   1. Name: NZBHydra2

   1. Enable RSS Sync: _Your Preference_

   1. Enable Search: _Your Preference_

   1. URL: `http://nzbhydra2:5076`

   1. API Key: [[Your NZBHydra2 API Key|Install: NZBHydra2#4-api-key]]

   1. Additional Parameters: _Leave Blank_

1. Your settings will look like this:

    ![Radarr NZBHydra2](https://i.imgur.com/LRANTOU.png)

1. Click "Save" to add NZBHydra2.

Note: The "Test" will keep failing until you add an indexer in [[NZBHydra2|Install: NZBHydra2]].

### Jackett

Note: Each Indexer will need to be added separately.

1. Click "Settings" -> "Indexers".

1. Click Add Indexer (`+`)

1. Select "Torznab".

1. Add the following:

   1. Name: Indexer Name

   1. Enable RSS Sync: _Your Preference_

   1. Enable Search: _Your Preference_

   1. URL: [[Indexer's Torznab Feed|Install: Jackett#3-adding-indexers-to-sonarrradarr]]

   1. API Key: [[Your Jackett API Key|Install: Jackett#3-adding-indexers-to-sonarrradarr]]

   1. Additional Parameters: _Leave Blank_

1. Your settings will look like this:

    ![Radarr Jackett](https://i.imgur.com/T9vrrAW.png)

1. Click "Save" to add the indexer.


## v. Connect

###  Torrent Cleanup

Torrent Cleanup Script is a custom script that will cleanup torrents from ruTorrent that were auto-extracted, but still being seeded. So if the script detects that `.rar` files are in the folder that Radarr just imported from, it will delete the imported video file(s), leaving just the `.rar` files for seeding.


<!--
If the script detects that `.rar` files are in the folder that Radarr just imported from, it will delete the imported video file(s), leaving just the `.rar` files for seeding.
-->

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

    ![Radarr Torrent Cleanup Script CloudBox](https://i.imgur.com/j4FV9ky.png)

<!--  https://i.imgur.com/WL8Wym4.png -->

1. Click "Save" to add the Torrent Cleanup script.


### Plex Autoscan

1. Click "Settings" -> "Connect".

1. Add a new "Webhook".

1. Add the following:

   1. Name: Plex Autoscan

   1. On Grab: `No`

   1. On Download: `Yes`

   1. On Upgrade:  `Yes`

   1. On Rename: `Yes`

   1. Filter Movie Tags: _Leave Blank_

   1. URL: [[Your Plex Autoscan URL|Install: Plex-Autoscan#4-obtaining-the-plex-autoscan-url]]

   1. Method:`POST`

   1. Username: _Leave Blank_

   1. Password: _Leave Blank_

1. The settings will look like this:

    ![Radarr Plex Autoscan](https://i.imgur.com/jQJyvMA.png)


1. Click "Save" to add Plex Autoscan.



## 3. Movies Path
1. When you are ready to add your first movie to Radarr, click the "Path" drop-down and select "Add a different path".

1. Click the blue "Browse" button, select the `movies` folder, scroll to the bottom, and select "OK".

1. Click the green "check" button to add the path.

1. All movies added now will have that path set.

## 4. API Key

This is used during the setup of [[Ombi|Install: Ombi]] and [[Organizr|Install: Organizr]].

* Go to "Settings" -> "General" -> "Security" -> "API Key".

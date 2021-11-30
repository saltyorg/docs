Radarr is a movie collection manager for Usenet and BitTorrent users. It can monitor multiple RSS feeds for new movies and will interface with clients and indexers to grab, sort, and rename them. It can also be configured to automatically upgrade the quality of existing files in the library when a better quality format becomes available.

# URL

- To access Radarr, visit https://radarr._yourdomain.com_

## Settings


### General

1. Go to "Settings" -> "General".

1. Set "Advanced Settings": `Shown`

#### Start-Up

- "Bind Address: `*`

- "Port Number": `7878`

- "URL Base": _blank_

- "Enable SSL": `No` (_SSL is handled by Traefik_)

- "Open browser on start": `No`

#### Proxy Settings

- "Use Proxy": `No`

#### Logging

- "Log Level": `Debug`

#### Analytics

- "Enable": `No` (_your preference_)

#### Updates

- "Branch": `nightly` or `develop`

- "Automatic": `Off`

#### Save

- Click "Save".

### Media Management

1. Go to "Settings" -> "Media Management".

1. Set "Advanced Settings": `Shown`


#### Movie Naming

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
   <summary>TRaSH' naming guide</summary> <br />

    Example:  <br />
    ```
    The Movie Title (2010) Ultimate Extended Edition [imdb-tt0066921][Surround Sound x264][Bluray-1080p Proper][3D][HDR][10bit][x264][DTS 5.1]-EVOLVE.mkv
    ```

    Standard Movie Format: <br />
    ```
    {Movie CleanTitle} {(Release Year)} {Edition Tags} [imdb-{ImdbId}]{[Custom Formats]}{[Quality Full]}{[MediaInfo 3D]}{[MediaInfo VideoDynamicRange]}[{Mediainfo VideoBitDepth}bit][{Mediainfo VideoCodec}]{[Mediainfo AudioCodec}{ Mediainfo AudioChannels}]{-Release Group}
    ```

    Reference: https://trash-guides.info/Radarr/Radarr-recommended-naming-scheme/
   </details><br />


#### Folders

- "Create empty movie folders": `No`

- "Automatically Rename Folders": `No`

- "Movie Paths Default to Static": `No`

#### Importing

- "Skip Free Space Check": `No`

- "Use Hardlinks instead of Copy": `No`

- "Import Extra Files": `Yes` (_can be your preference_)

- "Extra File Extensions": `srt, sub, idx`

#### File Management

- "Ignore Deleted Movies": `No` (_can be your preference_)

- "Download Propers": `No` (_can be your preference_)

- "Analyse video files": `No`

- "Change File Date": `None`

- "Recycle Bin": _blank_ (Rclone deletes are sent to Gdrive trash folder, anyway)

#### Permissions

- Set Permissions: `No`

#### Save

- Click "Save".

### Download Client

1. Go to "Settings" -> "Download Client".

1. Completed Download Handling

   - Enable: `Yes`

   - Remove: `Yes` (_can be your preference_)

1. Failed Download Handling

   - Redownload: `Yes`

   - Remove: `Yes`

#### NZBGet

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


#### ruTorrent

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



### Indexers

1. Go to "Settings" -> "Indexers".

1. Set "Advanced Settings": `Shown`

1. Add in your your favorite [[indexers|Prerequisites: Usenet vs BitTorrent]].


#### NZBHydra2

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

#### Jackett

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


### Connect

####  Torrent Cleanup

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


#### Plex Autoscan

1. Click "Settings" -> "Connect".

1. Add a new "Webhook".

1. Add the following:

   1. Name: Plex Autoscan

   1. On Grab: `No`

   1. On Download: `Yes`

   1. On Upgrade:  `Yes`

   1. On Rename: `Yes`

   1. Filter Movie Tags: _Leave Blank_

   2. URL: [Your Plex Autoscan URL](plex-autoscan.md#obtaining-the-plex-autoscan-url)

   3. Method:`POST`

   4. Username: _Leave Blank_

   5. Password: _Leave Blank_

2. The settings will look like this:

    ![Radarr Plex Autoscan](https://i.imgur.com/jQJyvMA.png)


3. Click "Save" to add Plex Autoscan.



### Movies Path
1. When you are ready to add your first movie to Radarr, click the "Path" drop-down and select "Add a different path".

2. Click the blue "Browse" button, navigate to `/mnt/unionfs/Media/Movies`, scroll to the bottom, and select "OK".

3. Click the green "check" button to add the path.

4. All movies added now will have that path set.

### API Key

This is used during the setup of [Overseerr](overseerr.md) and [Organizr](organizr.md).

* Go to "Settings" -> "General" -> "Security" -> "API Key".

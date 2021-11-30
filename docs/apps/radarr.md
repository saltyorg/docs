## URL

- To access Radarr, visit https://radarr._yourdomain.com_

## Settings

Click on "Settings" in the sidebar.  Click "Show Advanced" at the top of the Settings pane.

Make changes in the following sections:

=== "Media Management"
    **Movie Naming**

       - "Rename Movies": `Yes`

       - "Replace Illegal Characters": `Yes`

       - Colon Replacement Format: `Delete`
       
       _Note: You could use `Replace with Space Dash` but only if your file naming format is not using spaces (e.g. using dots) to separate words._ 

       - Set your preferred naming format; here are some examples.

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

         Reference: https://support.plex.tv/articles/200381023-naming-movie-files/
       </details>

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
       </details>

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
       </details>


    **Folders**

       - "Create empty movie folders": `No`

       - "Automatically Rename Folders": `No`

       - "Movie Paths Default to Static": `No`

    **Importing**

       - "Skip Free Space Check": `No`

       - "Use Hardlinks instead of Copy": `No`

       - "Import Extra Files": `Yes` (_can be your preference_)

       - "Extra File Extensions": `srt, sub, idx`

    **File Management**

       - "Ignore Deleted Movies": `No` (_can be your preference_)

       - "Download Propers": `No` (_can be your preference_)

       - "Analyse video files": `No`

       - "Change File Date": `None`

       - "Recycle Bin": _blank_ (Rclone deletes are sent to Gdrive trash folder, anyway)

    **Permissions**

       - Set Permissions: `No`

    **Save**

       - Click "Save".
    
=== "Indexers"

    Add in your your favorite [indexers](../saltbox/prerequisites/prerequisites.md#usenet-or-bittorrent-sources).

    **NZBHydra2**

    1. Click "Settings" -> "Indexers".

    2. Click Add Indexer (`+`).

    3. Select "Newznab".

    4. Add the following:

        Name: NZBHydra2

        Enable RSS Sync: _Your Preference_

        Enable Search: _Your Preference_

        URL: `http://nzbhydra2:5076`

        API Key: [Your NZBHydra2 API Key](../apps/nzbhydra2.md)

        Additional Parameters: _Leave Blank_

    5. Your settings will look like this:

        ![Radarr NZBHydra2](../images/radarr/radarr-nzbhydra.png)

    6. Click "Save" to add NZBHydra2.

    Note: The "Test" will keep failing until you add an indexer in [NZBHydra2](../apps/nzbhydra2.md).

    **Jackett**

    Note: Each Indexer will need to be added separately.

    1. Click "Settings" -> "Indexers".

    2. Click Add Indexer (`+`)

    3. Select "Torznab".

    4. Add the following:

        Name: Indexer Name

        Enable RSS Sync: _Your Preference_

        Enable Search: _Your Preference_

        URL: [Indexer's Torznab Feed](../apps/jackett.md)

        API Key: [Your Jackett API Key](../apps/jackett.md)

        Additional Parameters: _Leave Blank_

    5. Your settings will look like this:

        ![Radarr Jackett](../images/radarr/radarr-jackett.png)

    6. Click "Save" to add the indexer.


=== "Download Clients"

    **Completed Download Handling**

       - "Enable": `Yes`

       - "Remove": `Yes` (_can be your preference_)

    **Failed Download Handling**

       - "Redownload": `Yes`

       - "Remove": `Yes`

    **NZBGet**

    1. Add a new "NZBGet" download client.

    2. Add the following:

        Name: NZBGet

        Enable: `Yes`

        Host: `nzbget`

        Port: `6789`

        Username:  [Your NZBGet Username](../apps/nzbget.md)

        Password:  [Your NZBGet Password](../apps/nzbget.md)

        Category: `radarr`

        Use SSL: `No`

        Add Paused: `No`

    3. Your settings will look like this:

        ![Radarr NZBGet Downloader](../images/radarr/radarr-nzbget.png)

    4. Click "Save" to add NZBGet.


    **ruTorrent**

    1. Add a new "rTorrent" download client.

    2. Add the following:

        Name: ruTorrent

        Enable: `Yes`

        Host: `rutorrent`

        Port: `80`

        URL Path: `RPC2`

        Use SSL: `No`

        Username: [Your ruTorrent Username](../rutorrent.md)

        Password: [Your ruTorrent Password](../rutorrent.md)

        Category: `radarr`

        Directory: _Leave Blank_

    3.  Your settings will now look like this:

         ![Radarr ruTorrent Downloader](../images/radarr/radarr-rtorrent.png)

    4. Click "Save" to add ruTorrent.
   
=== "Connect"

    **Torrent Cleanup**

    Torrent Cleanup Script is a custom script that will cleanup torrents from ruTorrent that were auto-extracted, but still being seeded. So if the script detects that `.rar` files are in the folder that Radarr just imported from, it will delete the imported video file(s), leaving just the `.rar` files for seeding.

    1. Click "Settings" -> "Connect".

    2. Add a new "Custom Script".

    3. Add the following:

        Name: Torrent Cleanup

        On Grab: `No`

        On Download: `Yes`

        On Upgrade:  `Yes`

        On Rename:`No`

        Path: `/scripts/torrents/TorrentCleanup.py`

    4. The settings will look like this:

        ![Radarr Torrent Cleanup Script CloudBox](../images/radarr/radarr-torrentcleanup.png)

    5. Click "Save" to add the Torrent Cleanup script.


    **Plex Autoscan**

    1. Click "Settings" -> "Connect".

    2. Add a new "Webhook".

    3. Add the following:

        Name: Plex Autoscan

        On Grab: `No`

        On Download: `Yes`

        On Upgrade:  `Yes`

        On Rename: `Yes`

        Filter Movie Tags: _Leave Blank_

        URL: [Your Plex Autoscan URL](../plex-autoscan/#obtaining-the-plex-autoscan-url)

        Method:`POST`

        Username: _Leave Blank_

        Password: _Leave Blank_

    4. The settings will look like this:

        ![Radarr Plex Autoscan](../images/radarr/radarr-plex_autoscan.png)


    5. Click "Save" to add Plex Autoscan.


=== "General"
    **Start-Up**

       - "Bind Address: `*`

       - "Port Number": `7878`

       - "URL Base": _blank_

       - "Enable SSL": `No` (_SSL is handled by Traefik_)

    **Proxy Settings**

       - "Use Proxy": `No`

    **Logging**

       - "Log Level": `Debug`

    **Analytics**

       - "Enable": `No` (_your preference_)

    **Updates**

       - "Branch": `nightly` or `develop`

       - "Automatic": `Off`

    **Save**

       - Click "Save".



## Movies Path
1. When you are ready to add your first movie to Radarr, click the "Path" drop-down and select "Add a different path".

2. Click the blue "Browse" button, navigate to `/mnt/unionfs/Media/Movies`, scroll to the bottom, and select "OK".

3. Click the green "check" button to add the path.

4. All movies added now will have that path set.

## API Key

This is used during the setup of [Overseerr](overseerr.md) and [Organizr](organizr.md).

* Go to "Settings" -> "General" -> "Security" -> "API Key".

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:0 orderedList:0 -->

- [1. URL](#1-url)
- [2. Setup Wizard](#2-setup-wizard)
- [3. Settings](#3-settings)
  - [Library](#library)
  - [Network](#network)
  - [Transcoder](#transcoder)
  - [DLNA](#dlna)
  - [Scheduled Tasks](#scheduled-tasks)
- [4. Add Media Libraries](#4-add-media-libraries)
  - [Add the Movie Library](#add-the-movie-library)
  - [Add the TV Library](#add-the-tv-library)
- [5. Scan Media libraries](#5-scan-media-libraries)
- [6. Webtools](#6-webtools)

<!-- /TOC -->

---

## 1. URL

1. To access Plex, visit https://plex._yourdomain.com_

2. Login with your Plex account

    ![](https://i.imgur.com/KMVu05O.png)

## 2. Setup Wizard

1. First time you log in, you will be presented with a welcome screen. Click "GOT IT!" to continue.

    ![](https://i.imgur.com/CTG955C.png)

1. Next screen will show you a list of servers, with a randomly generated name. Give it a friendly name and click "NEXT".

    ![](https://i.imgur.com/soGxdGm.png)

1. On the next screen, click "NEXT" (we will add Libraries later).

    ![](https://i.imgur.com/OQxsJd1.png)

1. Click "DONE".

    ![](https://i.imgur.com/uRr3o61.png)


## 3. Settings

### Library

1. Click the Settings icon (top right) &rightarrow; "Server" (top) &rightarrow; "Library" (left).

1. Set the following:

   - "Empty trash automatically after every scan": `disabled`

     - _Plex Autoscan will take care of this._

   - "Allow media deletion": `enabled`

   - "Generate video preview thumbnails": `never`

   - "Generate chapter thumbnails": `never`

> The reasoning behind disabling these thumbnails is related to Google Drive API usage, data transfer, and disk space.  Accessing large portions of a given video file to generate thumbnails *may* generate large numbers of Google Drive API calls, and large amounts of data transfer.  Either of these things *may* result in your account suffering one of the various types of 24-hour bans Google hands out, which *may* prevent your server from playing media at all.  Also, storing these images *will* greatly inflate the size of `/opt/plex`, which can affect the speed of backups, your ability to download, and anything else related to disk space usage.  These are generally considered Bad Things, so the recommendation is to avoid the possibility by turning these options off.

1. Click "SAVE CHANGES".

    ![](https://i.imgur.com/g6RxFdF.jpg)


### Network

1. Click the Settings icon (top right) &rightarrow; "Server" (top) &rightarrow; "Network" (left).

1. Set the following:

   - "Secure Connections": `Preferred`.

   - "Enable local network discovery (GDM)": `disabled`.

   - "Remote streams allowed per user": _your preference_.

   - "Custom server access URLs": `http://plex.yourdomain.com:80/,https://plex.yourdomain.com:443/` (pre-filled)

      - NOTE: Enter your domain as you have it configured in accounts.yml, not literally "yourdomain.com".


1. Click "SAVE CHANGES".

    ![](https://i.imgur.com/Qx9TcHX.jpg)


### Transcoder

1. Click the Settings icon (top right) &rightarrow; "Server" (top) &rightarrow; "Transcoder" (left).

2. Set the following:

   - "Transcoder temporary directory": `/transcode`

   - "Transcoder default throttle buffer": `150`

   - "Use hardware acceleration when available": `enabled`

   - "Maximum simultaneous video transcode": `unlimited`

1. Click "SAVE CHANGES".

    ![](https://i.imgur.com/QH3R8FF.png)



### DLNA

1. Click the Settings icon (top right) &rightarrow; "Server" (top) &rightarrow; "DLNA" (left).


1. Set the following:

    - "Enable the DLNA server": `disabled`

    - "DLNA server timeline reporting": `disabled`

1. Click "SAVE CHANGES".

    ![](https://i.imgur.com/8XiyMEk.png)



### Scheduled Tasks

1. Click the Settings icon (top right) &rightarrow; "Server" (top) &rightarrow; "Scheduled Tasks" (left).


2. Set the following:

    - "Update all libraries during maintenance": `disabled`

    - "Upgrade media analysis during maintenance": `disabled`

    - "Perform extensive media analysis during maintenance": `disabled`

3. Click "SAVE CHANGES".

    ![](https://i.imgur.com/0SHIJCM.jpg)


## 4. Add Media Libraries

In this section, we will add two libraries: one for Movies and one for TV.

_Note: If you would like to have custom Plex libraries (more than just a Movies and TV one), see [[Customizing Plex Libraries]]._

### Add the Movie Library

1. In the main Plex screen (Home icon on the top left), click "+" next to "LIBRARIES".

    ![](https://i.imgur.com/zadq6ca.png)

1. In the "Add Library" window, select "Movies" and click "NEXT".

    ![](https://i.imgur.com/UcUFCix.png)

1. Click "BROWSE FOR MEDIA FOLDER".

    ![](https://i.imgur.com/5kywEro.png)


1. In second column of the "Add Folder" window, select `data`, then `Movies`, and then click the "ADD" button.

    ![ ](https://i.imgur.com/Embc9h9.png)

1. You will now see `/data/Movies` in the text box (don't click "ADD LIBRARY" yet).

    ![](https://i.imgur.com/qzlGMTN.png)

1. Click "Advanced" on the left.

1. Set the following:

   - "Enable Cinema Trailers": `disabled` (optional)

   - "Enable video preview thumbnails": `disabled`

   - "Find trailers and extras automatically (Plex Pass required)": `disabled` (optional) 

1. Click "ADD LIBRARY".

    ![](https://i.imgur.com/4JV0orf.png)



### Add the TV Library

1. In the main Plex screen (Home icon on the top left), click "+" next to "LIBRARIES".

    ![](https://i.imgur.com/zadq6ca.png)

1. In the "Add Library" window, select "TV Shows" and click "NEXT".

    ![](https://i.imgur.com/gZtUgtQ.png)

1. Click "BROWSE FOR MEDIA FOLDER".

    ![](https://i.imgur.com/5kywEro.png)


1. In second column of the "Add Folder" window, select `data`, then `TV`, and then click the "ADD" button.

    ![ ](https://i.imgur.com/Embc9h9.png)

1. You will now see `/data/TV` in the text box (don't click "ADD LIBRARY" yet).

    ![](https://i.imgur.com/i03W0W0.png)

1. Click "Advanced" on the left.

1. Set the following:

   - "Enable video preview thumbnails": `disabled`

   - "Find trailers and extras automatically (Plex Pass required)": `disabled` (optional)

1. Click "ADD LIBRARY".


    ![](https://i.imgur.com/JuZif0B.png)


## 5. Scan Media libraries

As mentioned in the [[Introduction|Basics: Introduction#how-does-cloudbox-function-]] page, [[Plex Autoscan| Install: Plex Autoscan]] will automatically scan the media files into Plex as they are downloaded, but this will require the Plex database to not be completely empty. So for every new library that is added, a one-time, manual scan is required. 

To do so:

1. Click the 3 dots next to a Plex library.

2. Select "Scan Library Files". 

   ![](https://i.imgur.com/38OCwU5.png)

3. Repeat steps 1-2 for each library. 


## 6. Webtools

Webtools for Plex comes preinstalled. If you wish to setup Webtools and install 3rd party add-ons, you can go to https://plex-webtools._yourdomain.com_ and log in with your Plex account.
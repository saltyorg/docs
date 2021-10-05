
<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:1 -->

- [1. Introduction](#1-introduction)
- [2. URL](#2-url)
- [3. Initial Setup](#3-initial-setup)
  - [i. Domain](#i-domain)
  - [ii. Install](#ii-install)
- [4. Setup Wizard](#4-setup-wizard)
- [5. Settings](#5-settings)
  - [i. Users](#i-users)
  - [ii. Transcoding](#ii-transcoding)
  - [iii. Libraries](#iii-libraries)
    - [Add Movie Library](#add-movie-library)
    - [Add TV Shows Library](#add-tv-shows-library)
- [6. API Key](#6-api-key)

<!-- /TOC -->

# 1. Introduction

[Emby](https://emby.media) is a media server designed to organize, play, and stream audio and video to a variety of devices

![](https://i.imgur.com/P3TkSfV.jpg)

# 2. URL

 - To access Emby, visit https://emby._yourdomain.com_

# 3. Initial Setup

## i. Domain

- See [[Adding a Subdomain|Adding a Subdomain]] on how to add the subdomain `emby` to your DNS provider.

- _Note: You can skip this step if you are using [[Cloudflare|Prerequisites: Cloudflare]] with Cloudbox._

## ii. Install

  - Run the following commands:

    ```bash
    cd ~/cloudbox/
    ```

    ```bash
    sudo ansible-playbook cloudbox.yml --tags emby  
    ```

# 4. Setup Wizard

1. Visit https://emby._yourdomain.com_.


1. Select your **preferred display language**. Click **Next**.

   ![](https://i.imgur.com/mbRLNED.png)

1. **Type** the following and click **Next**:

   - **Your first name:** _your name_ 

   - **Emby connect username or email address**: _your [Emby Connect username](https://emby.media/connect)_ (important)

   ![](https://i.imgur.com/IdAHjqP.png)

1. Confirm the message by clicking **Got It**.

   ![](https://i.imgur.com/RvXgVck.png)

1. **Confirm** the link in your email. 

   ![](https://i.imgur.com/Ah8LCBQ.png)

   ![](https://i.imgur.com/8kB6UVI.png)

1. Skip the adding of the libraries. Click **Next**.

   ![](https://i.imgur.com/76WN7KQ.png)

1. Select your **Preferred Metadata Language** and **Country** (_`English` and `United States` are recommended_) and click **Next**.

   ![](https://i.imgur.com/YPFIbfH.png)


1. Check **Allow remote connections to this Emby Server**. Uncheck **Enable automatic port mapping**. Click **Next**.

   ![](https://i.imgur.com/fD1AknT.png)

1. **Check** to accept the terms. Click **Next**.

   ![](https://i.imgur.com/KEhZYFa.png)

1. Click **Finish**.

   ![](https://i.imgur.com/ZJ1m6dZ.png)

1. You will now be taken to the **Dashboard** view.



# 5. Settings

## i. Users

1. Go to **Settings**.

1. Go to **Users**.

   ![](https://i.imgur.com/a1zdnRz.png)

1. Click the **Password** tab at the top.

1. Type in your password in **New password** and **New password confirm**. Click **Save**. 

   ![](https://i.imgur.com/PUTS7AX.png)

1. Click **Save** again.

   ![](https://i.imgur.com/XG8A70a.png)


## ii. Transcoding

1. Go to **Settings**.

1. Go to **Transcoding**.

   ![](https://i.imgur.com/MFZxd88.png)

1. Under **Enable hardware acceleration when available**, select **Advanced**.

   ![](https://i.imgur.com/iReeH6e.png)

1. Under **Preferred Hardware Encoders**, go down to **H.264 (AVC)**, and select **VAAPI H.264** (_for Intel CPUs with Intel Quick Sync Video enabled_). 

   ![](https://i.imgur.com/FM7kODJ.png)

1. Under **Transcoding temporary path**, type in or choose `/transcode`.

   ![](https://i.imgur.com/b9jRVSm.png)

1. Click **Save**.


## iii. Libraries

In this section, we will add two libraries: one for Movies and one for TV Shows.

### Add Movie Library

1. Go to **Settings**.

1. Go to **Library**.

   ![](https://i.imgur.com/Reixrpp.png)

1. Click **Add Media Library**.

1. Under **Content type**, select **Movies**. 

   ![](https://i.imgur.com/Afwb8oH.png)

   ![](https://i.imgur.com/MUqjrm5.png)

1. Click **+** next to **Folders**.

1. Type in or choose `/data/Movies`. Click **OK**.

   _Note: These [[paths|Basics: Cloudbox Paths]] are for the standard library setup. If you have [[customized|Customizing-Plex-Libraries]] it, use those paths instead._

   ![](https://i.imgur.com/UiXspBL.png)

1. Click **OK** once more.

   ![](https://i.imgur.com/gjOtiSy.png)

### Add TV Shows Library

1. Go to **Settings**.

1. Go to **Library**.

   ![](https://i.imgur.com/Reixrpp.png)

1. Click **Add Media Library**.

1. Under **Content type**, select **TV shows**. 

   ![](https://i.imgur.com/Afwb8oH.png)

   ![](https://i.imgur.com/ThVUSyI.png)

1. Click **+** next to **Folders**.

1. Type in or choose `/data/TV`. Click **OK**.

   _Note: These [[paths|Basics: Cloudbox Paths]] are for the standard library setup. If you have [[customized|Customizing-Plex-Libraries]] it, use those paths instead._

   ![](https://i.imgur.com/shR8IZB.png)

1. Click **OK** once more.

   ![](https://i.imgur.com/gI0jAIq.png)


# 6. API Key

Instructions below will guide you through creating an API Key for a specific app.

1. Click the **Settings** icon.

   ![](https://i.imgur.com/ooc9sCL.png)

1. Under **Expert**, click **Advanced**.

   ![](https://i.imgur.com/dslwDdM.png)

1. Click the **Security** tab at the top. 

   ![](https://i.imgur.com/Zd1XW28.png)

1. Under **Api Keys** click **+**. 

   ![](https://i.imgur.com/hcmabil.png)

1. Fill in an **App name** (e.g. Ombi) and click **OK**.

   ![](https://i.imgur.com/CSonhIf.png)

1. And now have created an **Api Key** for your app.

   ![](https://i.imgur.com/Ixi686z.png)
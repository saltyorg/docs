# What is it?

[Organizr](https://organizr.app/) (by CauseFX) is a web-based, HTPC server organizer, that allows you to manage various tools and programs within tabs. Also supports user management, allowing for non admin users or guests to access certain web-pages via Organizr, even if it is behind HTTP authentication. This guide is to help you get Organizr setup and running by no means is this a complete guide to Organizr as you'll see the depth of it is pretty vast and there are plenty of customizations available to you at every turn.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://organizr.app){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://organizr.app/howtos/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/causefx/Organizr){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/organizr/organizr){: .header-icons target=_blank rel="noopener noreferrer" }|

## 2. URL

- To access Organizr, visit `https://organizr._yourdomain_.com`

## 3. Initial Setup

1. The first time you go to the Organizr page, you will be presented with `Install Type`, `Admin Info`, `Security`, `Database` and `Verify` sections.
In the `Install Type` section select `Personal`

    ![Main Setup-Install-Type](https://i.imgur.com/IgStX3L.png)

1. In the `Admin Info` section enter your details such as the preferred password to log in and personal email.
Note: it is suggested to enter your `plex username and password`

    ![Main Setup-Admin-Info](https://i.imgur.com/clOLSdn.png)

1. In the `Security` section enter your fill in the `Hash Key` and `Registration Password` any type of password will do but if you want a secure one then follow these steps;

- First for the `Hash Key` you can head over to [Base64 Encode](https://www.cleancss.com/base64-encode/) and convert a string to Base64. Keep in mind the `Hash Key` can be anywhere between 3 to 30 which mean you can enter string up to 21 characters in Base64

- For the password just use any strong password you prefer, if you want a strong one then [Password Generator](https://passwordsgenerator.net/), there is no limit on the password section go crazy ;)
- The API key should be auto-generated so no need to worry about this if the API key is throwing an error such as shorter than it suppose to be or longer it's most likely due to the web browser auto-fill, make sure it's disabled or just use another browser that doesn't have auto-fill or you don't use much e.g Internet Explorer 👀.
<br> <br>You should have something like this:

   ![Main Setup-Admin-Info](https://i.imgur.com/o7yp3YQ.png)

4. In the `Database` section enter your preferred database name (there is 30 character limit), then after that for the "Database Location" set it as `/config/www` then click test path it should be a success.
<br> <br>You should have something like this:

   ![Main Setup-Database](https://i.imgur.com/kJlIRpY.png)

5. In the `Verify` section you will just need to confirm everything but feel free to take note of your **API** key and save it somewhere safe. After clicking finish you will be taken to a log in the page just enter the `username` and `password` you have inserted in the `Admin info` section.
<br> <br>You should have something like this:

   ![Main Setup-Database](https://i.imgur.com/wbOhf12.png)

## 4. Settings

1. You will now be taken to the main Organizr Page and asked to login with the credentials you created in the previous steps.

    ![Organizr](https://i.imgur.com/J1rVQQk.png)

### Tabs

1. Click "Settings" on the left menu, to be taken to the "Organizr Settings" page.

    ![Settings Tab](https://i.imgur.com/M7wfb1z.png)
    ![Tabs Editor](https://i.imgur.com/DJIvrh2.png)

1. Things to note on this page, the Homepage is disabled by default and note the "Type" is set to "Internal".  Your normal Apps with Saltbox will all need to have a Type: "iFrame" unless you have a particular app you wish to open in another window which is also a Type option.  Go ahead and click "+ on the right". You will be prompted for information regarding the tab.

    ![](https://i.imgur.com/KiXsQUI.png)

1. Before hitting the Edit Tab button in the bottom right, please hit the "Test Tab" button, sometimes the Tab will check for you if iFrame is possible.  This will test if the information you inputted can be open in an iFrame.  Which is the secret sauce in Organizr's tabbed browsing.

    ![New Tab](https://i.imgur.com/7UyBDAA.png)

1. You will need to create multiple tabs with the information below. These are merely a suggestion and examples to get you up and going.  Any changes made, won't be reflected until Organizr is reloaded. You can also drag and drop to change the order of the apps (don't forget to reload)

    | Tab Name      | Tab URL                             | Icon URL                      | Category | Group | Type | Active |
    | ------------- | ----------------------------------- | ----------------------------- |:------:|:----:|:-----:|:---------:|
    | Portainer     | `https://portainer.yourdomain.tld`    | images/organizr.png (default) |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | Sonarr        | `https://sonarr.yourdomain.tld`       | images/sonarr.png             |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | Radarr        | `https://radarr.yourdomain.tld`       | images/radarr.png             |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | NZBGet        | `https://nzbget.yourdomain.tld`       | images/nzbget.png             |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | qbittorrent     | `https://qbittorrent.yourdomain.tld`    | images/qbittorrent.png          |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | NZBHydra2     | `https://nzbhydra2.yourdomain.tld`    | images/hydra.png              |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | Jackett       | `https://jackett.yourdomain.tld`      | images/jackett.png            |   Unsorted   |  Admin   |   iFrame   |     Y     |
    | Plex          | `https://plex.yourdomain.tld`         | images/plex.png               |   Unsorted   |  User    |   iFrame   |     Y     |
    | Tautulli      | `https://tautulli.yourdomain.tld`     | images/tautulli.png           |   Unsorted   |  User    |   iFrame   |     Y     |
    | Ombi          | `https://ombi.yourdomain.tld`         | images/ombi.png               |   Unsorted   |  User    |   iFrame   |     Y     |
    | Overseerr     | `https://overseerr.yourdomain.tld`    | images/overseerr.png          |   Unsorted   |  User    |   iFrame   |     Y     |

    ![Tab Editor](https://i.imgur.com/aXwGxpx.png)

- Note: If Sonarr or Radarr are lagging a lot, you may set it to a specific page in each. (e.g. Sonarr: `https://sonarr.yourdomain.com/calendar` ; Radarr: `https://radarr.yourdomain.com/activity/history`)

### Homepage (Make you have Homepage ACTIVE in Tabs section)

1. Click "Homepage Items" under the Tab Editor section, to be taken to the "Homepage Items" page.

    ![Edit Homepage](https://i.imgur.com/v0rz7Ap.png)

1. Click the Plex icon at the top.

    - You'll have to Enable it and verify the Minimum Authentication

    - Click on the Connection Tab and set "Plex URL": `http://plex:32400`

    - Click "Retrieve" under Get Plex Token
    - Click "Save" icon at the top right
    - Set your preferred options on the remaining tabs

    - Click "SAVE".

    ![  ](https://i.imgur.com/c84B5td.png)

1. Click the Sonarr icon at the top.

    - Enable it.

    - On the Connections Tab, Set "Sonarr URL": `http://sonarr:8989`

    - Set "Sonarr API Key": [[Your Sonarr API Key|Install: Sonarr#9-retrieving-the-api-key]]

    - Go over any other Miscellaneous Options on the next Tab and set your preferences.

    - Click "SAVE".

    ![  ](https://i.imgur.com/04b5Xmb.png)

1. Click the Radarr icon at the top.

    - Enable it.

    - Set "Radarr URL": `http://radarr:7878`

    - Set "Radarr API Key": [[Your Radarr API Key|Install: Radarr#9-retrieving-the-api-key]]

    - Go over any other Miscellaneous Options on the next Tab and set your preferences.

    - Click "SAVE".

    ![  ](https://i.imgur.com/0S1erVG.png)

1. Click the NZBGet icon at the top.

    - Enable it.

    - Set "NZBGet URL": `http://nzbget:6789`

    - For "Username" / "Password": fill in your NZBGet login (see [[NZBGet|Install: NZBGet#2-setup]])

    - Click "SAVE".

    ![  ](https://i.imgur.com/MRzv0Sa.png)

### Homepage Order

1. This is where you organize the apps and other items and how they will appear on your Homepage.  There's no right or wrong order so simply move things around and find out what works for you.

    ![Homepage Order](https://i.imgur.com/A2FPosN.png)

Any additional question please reach out to the [Organizr](https://organizr.app/) team, either via their [Discord Server](https://organizr.app/discord) or their [subreddit](https://www.reddit.com/r/organizr/)

## Next

Are you setting Saltbox up for the first time?  You're ready to explore Saltbox! You can start checking out community apps in [Sandbox](https://docs.saltbox.dev/sandbox/basics/) if you wish.

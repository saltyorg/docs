THIS PAGE HAS NOT BEEN FULLY UPDATED FOR SALTBOX

## What is it?

[Tautulli](http://tautulli.com/) (Tautulli), by JonnyWong16, is a web-based application runs alongside the Plex Media Server to monitor activity and track various statistics (eg most watched media). 

## Project Information

- [:material-home: Tautulli ](http://tautulli.com){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-link-16: Docs](https://github.com/Tautulli/Tautulli/wiki){: .header-icons target=_blank rel="noopener noreferrer" }
- [:octicons-mark-github-16: Github:](https://github.com/Tautulli/Tautulli){: .header-icons target=_blank rel="noopener noreferrer" }
- [:material-docker: Docker: ](https://hub.docker.com/r/hotio/tautulli){: .header-icons target=_blank rel="noopener noreferrer" }

## 2. URL

To access Tautulli, visit https://tautulli._yourdomain_.com

## 3. Setup Wizard

1. First time you go to the PlexPy site, you will be presented with the "Tautulli Setup Wizard". Click `Next`.

    ![ ](https://i.imgur.com/LZPpfLL.png)

1. On the "Plex Authentication" page, sign in with your Plex username and password, and click `Authenticate`. When you see the "Authentication successful." message, click `Next`.

    ![](https://i.imgur.com/8DKkiAy.png)

1. On the "Plex Media Server" page, set the following:

   - "Plex IP or Hostname": `plex`
   - "Port Number": `32400`
   - "Use SSL": disabled
   - "Remote Server": disabled 

   Click `Verify`. When you see the "Server found!" message, click `Next`.

    ![](https://i.imgur.com/0vxUURW.png)

1. On the "Activity Logging" page, select your preferences (default is OK) and click `Next`.

    ![](https://i.imgur.com/XUOpcc8.png)

1. On the "Notifications" page, simply click `Next`.

    ![](https://i.imgur.com/C58KgyJ.png)

1. On the "Database Import" page, click `Finish` to complete the setup.

    ![](https://i.imgur.com/4Rc5eaE.png)

## 4. Settings

1. Once the PlexPy page comes up, go to "Settings".

    ![](https://i.imgur.com/wKukbLR.png)

1. Click "Web Interface" on the left. Fill in "HTTP Username" and "HTTP Password (this will be the login for your Tautulli site), but don't click `Save` yet.  

    ![](https://i.imgur.com/iX6G2ca.png)

1. Click "Plex Media Server" on the left. Click "Show Advanced" at the top. Under "Logs Folder", type in `/logs`. Now you can click `Save`. Also verify 'Use SSL' and 'Remote Server` are unchecked. 

    ![](https://i.imgur.com/Z1Vfi8U.png)

1. On the "Restart" popup window, click `Restart`.

    ![](https://i.imgur.com/rqV7Gci.png)

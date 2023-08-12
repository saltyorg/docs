# What is it?

[Tautulli](http://tautulli.com/) (Tautulli), by JonnyWong16, is a web-based application runs alongside the Plex Media Server to monitor activity and track various statistics (eg most watched media).

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](http://tautulli.com){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://github.com/Tautulli/Tautulli/wiki){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/Tautulli/Tautulli){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/hotio/tautulli){: .header-icons target=_blank rel="noopener noreferrer" }|

## 2. URL

To access Tautulli, visit `https://tautulli._yourdomain_.com`

## 3. Setup Wizard

1. First time you go to the Tautulli site, you will be presented with the "Tautulli Setup Wizard". Click `Next`.

    ![](../images/tautulli/01-tautulli-wizard.png)

2. On the "Plex Authentication" page, sign in with your Plex username and password, and click `Authenticate`. When you see the "Authentication successful." message, click `Next`.

    ![](../images/tautulli/02-tautulli-plex-auth.png)

3. On the "Plex Media Server" page, set the following:

    - "Plex IP or Hostname": `plex`
    - "Port Number": `32400`
    - "Use SSL": disabled
    - "Remote Server": disabled

     Click `Verify`. When you see the "Server found!" message, click `Next`.

     ![](../images/tautulli/03-tautulli-plex-media.png)

4. On the "Activity Logging" page, select your preferences (default is OK) and click `Next`.

    ![](../images/tautulli/04-tautulli-activity.png)

5. On the "Notifications" page, simply click `Next`.

    ![](../images/tautulli/05-tautulli-notifications.png)

6. On the "Database Import" page, click `Finish` to complete the setup.

    ![](../images/tautulli/06-tautulli-database.png)

## 4. Settings

1. Once the Tautulli page comes up, go to "Settings".

    ![](../images/tautulli/07-tautulli-settings.png)

2. Click "Web Interface" on the left. Fill in "HTTP Username" and "HTTP Password (this will be the login for your Tautulli site), but don't click `Save` yet.

    ![](../images/tautulli/08-tautulli-web.png)

3. Click "Plex Media Server" on the left. Click "Show Advanced" at the top. Under "Logs Folder", type in `/logs`. Now you can click `Save`. Also verify 'Use SSL' and 'Remote Server` are unchecked.

    ![](../images/tautulli/09-tautulli-plex.png)

4. On the "Restart" popup window, click `Restart`.

    ![](../images/tautulli/10-tautulli-reboot.png)

## 5. Next

Are you setting Saltbox up for the first time?  Continue to [Overseerr](overseerr.md).

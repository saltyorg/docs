# Maintainerr

# What is it?

[Maintainerr](https://docs.maintainerr.info/Introduction/) makes managing your media easy. No longer do you have to worry about your precious hard drive space being taken up by Movies and TVShows, that aren't even being watched.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://docs.maintainerr.info/Introduction/){: .header-icons } | [:octicons-link-16: Docs](https://docs.maintainerr.info/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/jorenn92/Maintainerr){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/jorenn92/maintainerr){: .header-icons }|

## 1. URL

- To access maintainerr, visit `https://maintainerr._yourdomain.com_`

## 2. Settings

This setup needs to take place **AFTER** you've set up Plex, Radarr, and Sonarr, since it involves connections to all three of those.

You will need your API Keys from both Radarr and Sonarr.

1. Log into your maintainerr url and the inital page will be the plex settings

2. Authenticate into plex

3. Click the refresh button to have maintainer find all plex servers

4. Click on the drop down and choose manual

5. Name it whatever you want

6. Hostname or IP is the name of your container. Default is plex

7. Port of plex server. Default is 32400

8. Leave SSL unchecked

9. Save Changes and Test changes

10. Navigate to Overseerr tab

11. Hostname of overseerr container. Default is overseerr

12. Port of container. Default is 5055

13. API key from overseerr

14. Save and test changes

15. Navigate to Sonarr tab

16. Hostname of sonarr container. Default is sonarr

17. Port of sonarr container. Default is 8989

18. API key from sonarr

19. Save and test changes

20. Navigate to Radarr tab

21. Hostname of radarr container. Default is radarr

22. Port of radarr container. Default is 7878

23. API key from radarr

24. Save and test changes

25. Once Overseerr, Plex, Sonarr, Radarr configurations are in place, you can use the app to you preferences.

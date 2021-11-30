THIS PAGE HAS NOT BEEN FULLY UPDATED FOR SALTBOX

- Install tag: `--tags sabnzbd`

## 1. URL

- To access ruTorrent, visit https://rutorrent._yourdomain.com_

## 2. Basics

- Go through the setup wizard.  YOu will need to enter server details:

![](../images/sabnzbd/02-sabnzbd.png)

- When you get to the end of the wizard, click "Go To SABnzbd"

![](../images/sabnzbd/03-sabnzbd.png)

- Go to SABnzbd Config

![](../images/sabnzbd/04-sabnzbd.png)

- You will need to add in categories for `sonarr`, `radarr`, and `lidarr`. 

  Set a relative directory name for each category.  
  
  You will need a category for each instance of `sonarr`/`radarr`/`lidarr` [for example, if you have a `radarr` and `radarr4k` you will need a category for each]
  
  SABnzbd requires the server to be filled in to set categories up.
  
  **This needs to be done BEFORE adding sabnzbd as a downloader to any of those apps.**

![](../images/sabnzbd/05-sabnzbd.png)

- Direct unpack is disabled by default. Configure this as you prefer.

- Make note of the API Key in the "General" section

![](../images/sabnzbd/06-sabnzbd.png)

- When creating the connection in the arrs, use API Key rather than user/pass.

![](../images/sabnzbd/07-sabnzbd.png)

   Note that the category matches between Radarr and Sab.  The specific category doesn't matter; just that they match.
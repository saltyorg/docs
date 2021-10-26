- Install tag: `--tags sabnzbd`

- Login is set with what's in accounts.yml

![](https://i.ibb.co/s3xkC4P/image.png)

- Go through the setup wizard.  YOu will need to enter server details:

![](https://i.ibb.co/2h2kMpL/image.png)

- When you get to the end of the wizard, click "Go To SABnzbd"

![](https://i.ibb.co/q73xL8L/image.png)

- Go to SABnzbd Config

![](https://i.ibb.co/xjXdkFS/image.png)

- You will need to add in categories for `sonarr`, `radarr`, and `lidarr`. 

  Set a relative directory name for each category.  
  
  You will need a category for each instance of `sonarr`/`radarr`/`lidarr` [for example, if you have a `radarr` and `radarr4k` you will need a category for each]
  
  SABnzbd requires the server to be filled in to set categories up.
  
  **This needs to be done BEFORE adding sabnzbd as a downloader to any of those apps.**

![](https://i.ibb.co/6gRXjJY/image.png)

- Direct unpack is disabled by default. Configure this as you prefer.

- Make note of the API Key in the "General" section

![](https://i.ibb.co/vXptd2H/image.png)

- When creating the connection in the arrs, use API Key rather than user/pass.

![](https://i.ibb.co/ggGcmYj/image.png)

   Note that the category matches between Radarr and Sab.  The specific category doesn't matter; just that they match.
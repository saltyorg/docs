The default Plex Autoscan [PAS] setup does not enable Google Drive Monitoring, and the config does not match the automated shared drive setup.

To utilize Google Drive Monitoring [GDM], you'll need to make a few changes to the config to account for your own shared drives.

If you don't want to enable GDM, you don't need to do this.

!!! info
    GDM is useful if you are planning to add content to your Google Drive directly, outside of Sonarr/Radarr.  It provides a mechanism for PAS to pick up those changes and tell Plex to scan them.  If all your content is coming through Sonarr/Radarr, there's no reason for GDM.

If you used the [scripted rclone method](rclone-manual.md), there is a script in the sb_gd repo that will make the required modifications to the stock Plex Autoscan config.

This script is only useful if you have used the [scripted rclone method](rclone-manual.md).  It is expecting a stock plex autoscan config file as you will have when you have completed the install.

You will have to have completed `sb install saltbox` before using this script.


1. Run the script

    ```shell
        cd /opt/sb_gd
        source sb_gd/bin/activate
        python sb_pas.py
    ```

    If that doesn't work, update to the latest version of the files from the repo with `git pull` and try again.

1.  Next, you will need to authorize Google Drive. To do so, run the following command:

    ```shell
    plex_autoscan authorize
    ```

    If this doesn't work for you, update saltbox and rerun the plex_autoscan role:

    ```shell
    sb update
    sb install plex_autoscan
    ```

1.  Visit the link shown to get the authorization code and paste that in and hit `enter`.

    ```
    Visit https://accounts.google.com/o/oauth2/v2/auth?scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&response_type=code&client_id=&access_type=offline and authorize against the account you wish to use
    Enter authorization code:
    ```

1.  When access token retrieval is successful, you'll see this:

    ```
    2018-06-24 05:57:58,252 -     INFO -    GDRIVE [140007964366656]: Requesting access token for auth code '4/AAAfPHmX9H_kMkMasfdsdfE4r8ImXI_BddbLF-eoCOPsdfasdfHBBzffKto'
    2018-06-24 05:57:58,509 -     INFO -    GDRIVE [140007964366656]: Retrieved first access token!
    2018-06-24 05:57:58,511 -     INFO -  AUTOSCAN [140007964366656]: Access tokens were successfully retrieved!
    ```

    _Note: Ignore any `Segmentation fault` messages._

1. Restart the Plex Autoscan service:

    ```
        sudo systemctl restart plex_autoscan
    ```

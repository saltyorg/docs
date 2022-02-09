The default Plex Autoscan [PAS] setup does not enable Google Drive Monitoring, and the config does not match the automated shared drive setup.

To utilize Google Drive Monitoring [GDM], you'll need to make a few changes to the config to account for your own shared drives.

If you don't want to enable GDM, you don't need to do this.

!!! info
    GDM is useful if you are planning to add content to your Google Drive directly, outside of Sonarr/Radarr.  It provides a mechanism for PAS to pick up those changes and tell Plex to scan them.  If all your content is coming through Sonarr/Radarr, there's no reason for GDM.

If you used the [scripted rclone method](rclone-manual.md), there is a script in the sb_gd repo that will make the required modifications to the stock Plex Autoscan config.

1. Run the script

    ```
        cd /opt/sb_gd
        source sb_gd/bin/activate
        python sb_pas.py
    ```

2. Restart the Plex Autoscan service:

    ```
        sudo systemctl restart plex_autoscan
    ```

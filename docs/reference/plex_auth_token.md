Here are two ways of obtaining a Plex Access Token for your Plex account.

## Saltbox Role

You will need your Plex credentials filled in `~/saltbox/accounts.yml`. If you already do, skip steps 2-4.

1.  Go to the Saltbox folder:

    ```bash
    cd ~/saltbox/
    ```

2.  Open the file for editing:

    ```bash
    nano accounts.yml
    ```

3.  Fill in your Plex credentials:

    ```yaml
    plex:
      user:
      pass:
    ```

4.  Save and exit: <kbd class="platform-all">Ctrl + X</kbd> <kbd class="platform-all">Y</kbd> <kbd class="platform-all">Enter</kbd>.

5.  Run the following command:

    ```shell
    sb install plex_auth_token
    ```

6.  You will be shown your Plex Access Token in the log:

    ```shell
    TASK [plex_auth_token : Display Plex Auth Token] 
    ***********************************************************************************
    Tuesday 29 January 2019  21:08:33 +0100 (0:00:00.104)       0:00:13.905 *******
    ok: [localhost] => {
        "msg": "Your Plex Auth Token is: XXXXXXXXXXXXXXXX"
    }
    ```

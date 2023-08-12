# Plex

DO NOT FOLLOW ANY INSTRUCTIONS HERE UNLESS YOU *FULLY* UNDERSTAND WHAT THESE COMMANDS DO.

SOME COMMANDS ON THIS PAGE IRREVOCABLY DELETE DATA

## If you are unable to find your Plex server

=== "Delete everything and start again"
    
    !!! warning
        **THIS WILL DELETE ANY EXISTING PLEX CONFIGURATION SUCH AS LIBRARIES**

    - Remove Plex Container (it may show "Error response from daemon: No such container" if not created yet):

        ```shell
        sudo docker rm -f plex
        ```

    - Remove the Plex folder:
 
        !!! warning
            **THIS IS DESTRUCTIVE AND WILL DELETE ALL PLEX LIBRARIES AND DATA.  THERE IS NO UNDO.**
    
        <details>
        <summary>I understand the risk!  Show me!</summary>
        <br />

        ```shell
        sudo rm -rf /opt/plex
        ```

        </details>

    - Reinstall the Plex container:

        ```shell
        sb install plex
        ```

=== "Keep my data and rebuild Plex"

    !!! info
        THIS WILL LEAVE ANY EXISTING PLEX LIBRARIES AND METADATA INTACT

    - Remove Plex Preferences file.

       ```shell
       sudo rm "/opt/plex/Library/Application Support/Plex Media Server/Preferences.xml"
       ```

    - Reinstall the Plex container by running the following command:

       ```shell
       sb install plex
       ```

=== "Use SSH to tunnel to my server and claim it"

    - On your local machine (the one that you uise to ssh into your saltbox machine):

       ```shell
       ssh <user>@<yourserveripaddress> -L 32400:0.0.0.0:32400 -N
       ```
       
       Of course, replace `<user>` with your user name and `<yourserveripaddress>` with your serveripaddress - no arrows
       
       This will just hang there without any message. That is normal.

    - In a browser **ON THAT MACHINE**, go to <http://localhost:32400/web>.

    - Log in with your Plex account.

    - On the "How Plex Works" page, click “GOT IT!”.

    - Close the "Plex Pass" pop-up if you see it.

    - Under "Server Setup", you will see "Great, we found a server!". Give your server a name and tick “Allow me to access my media outside my home”. Click "NEXT".

    - On "Organize Your Media", hit "NEXT" (you will do this later). Then hit "DONE".

    - At this point, you may `Ctrl + c` on the SSH Tunnel to close it.

## If Plex shows you an incorrect title with the filename (eg RARBG releases)

Reorder the Plex agents for trhe library so that local assets are at the bottom.

## Fix permission issues with Plex logs

Replace `user` and `group` to match yours' (see [here](System.md#find-your-user-id-uid-and-group-id-gid)).

```shell
sudo chown -R user:group /opt/plex/Library/Logs
sudo chmod -R g+s /opt/plex/Library/Logs
```

_Note: If you have a separate Plex and Feeder setup, this will be done on the server where Plex is installed._

Other options for [Plex Autoscan](https://github.com/l3uddz/plex_autoscan).

# Google Drive Monitoring

In addition to Plex Autoscan receiving scan requests from Sonarr/Radarr/Lidarr, it can also monitor Google Drive directly for updates. When a new file is detected, it is checked against the Plex database and if this file is missing, a new scan request is sent to Plex.

Note: For details on setting up Teamdrives and/or Rclone-crypted remotes, visit https://github.com/l3uddz/plex_autoscan.

To set this up:

1. Edit the config file:

   ```shell
   nano /opt/plex_autoscan/config/config.json
   ```

1. Under the `GOOGLE` section of the config, enable Google Drive monitoring and fill in your [[Google Drive API Client ID and Secret|Google-Drive-API-Client-ID-and-Client-Secret]].

    ```json
    "ENABLED": true,
    "CLIENT_ID": "yourclientid",
    "CLIENT_SECRET": "yourclientsecret",
    ```

1. So that the entire section now looks like this (any order is fine):

   ```json
   "GOOGLE": {
     "ENABLED": true,
     "CLIENT_ID": "abcdefgh",
     "CLIENT_SECRET": "1234567",
     "ALLOWED": {
       "FILE_PATHS": [
         "My Drive/Media/Movies",
         "My Drive/Media/TV",
         "My Drive/Media/Music"
       ],
       "FILE_EXTENSIONS": true,
       "FILE_EXTENSIONS_LIST": [
         "webm","mkv","flv","vob","ogv","ogg","drc","gif",
         "gifv","mng","avi","mov","qt","wmv","yuv","rm",
         "rmvb","asf","amv","mp4","m4p","m4v","mpg","mp2",
         "mpeg","mpe","mpv","m2v","m4v","svi","3gp","3g2",
         "mxf","roq","nsv","f4v","f4p","f4a","f4b","mp3",
         "flac","ts"
       ],
       "MIME_TYPES": true,
       "MIME_TYPES_LIST": [
         "video"
       ]
     },
     "TEAMDRIVE": false,
     "TEAMDRIVES": [],
     "POLL_INTERVAL": 120,
     "SHOW_CACHE_LOGS": false
   },
   ```

1. Google Drive paths (e.g. `"My Drive/Media/Movies/"`) go under `SERVER_PATH_MAPPINGS` and should look like this:

   _Note: This is usually set pre-filled by default._

    ```json
     "SERVER_PATH_MAPPINGS": {
       "/data/Movies/": [
         "/movies/",
         "/mnt/unionfs/Media/Movies/",
         "My Drive/Media/Movies/"
       ],
       "/data/TV/": [
         "/tv/",
         "/mnt/unionfs/Media/TV/",
         "My Drive/Media/TV/"
       ],
       "/data/Music/": [
         "/music/",
         "/mnt/unionfs/Media/Music/",
         "My Drive/Media/Music/"
       ]
    },
    ```

    Note: If you are using [[Scenario 2 Custom Library Setup|Customizing Plex Libraries#scenario-2]], you will need to tweak this section of the config.


1. Save and Exit. 

1. Next, you will need to authorize Google Drive. To do so, run the following command:

   ```shell
   /opt/plex_autoscan/scan.py authorize
   ```

1. Visit the link shown to get the authorization code and paste that in and hit `enter`.

    ```
    Visit https://accounts.google.com/o/oauth2/v2/auth?scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&response_type=code&client_id=&access_type=offline and authorize against the account you wish to use
    Enter authorization code:
    ```

1. When access token retrieval is successfull, you'll see this:

   ```
   2018-06-24 05:57:58,252 -     INFO -    GDRIVE [140007964366656]: Requesting access token for auth code '4/AAAfPHmX9H_kMkMasfdsdfE4r8ImXI_BddbLF-eoCOPsdfasdfHBBzffKto'
   2018-06-24 05:57:58,509 -     INFO -    GDRIVE [140007964366656]: Retrieved first access token!
   2018-06-24 05:57:58,511 -     INFO -  AUTOSCAN [140007964366656]: Access tokens were successfully retrieved!
   ```

   _Note: Ignore any `Segmentation fault` messages._

1. Restart the service:

    ```shell
   sudo systemctl restart plex_autoscan
   ```


1. Plex Autoscan will now start monitoring Google Drive. 


# Make Plex scan a specific file or folder

## Web app

![](https://i.imgur.com/KTrbShI.png)


Setup instructions:

1. Enable `SERVER_ALLOW_MANUAL_SCAN` in your `/opt/plex_autoscan/config/config.json` file.

   ```json
   "SERVER_ALLOW_MANUAL_SCAN": true, 
   ```

2. Visit your [[Plex Autoscan URL|Install: Plex-Autoscan#4-obtaining-the-plex-autoscan-url]] webpage. 

3. Enter in the path to scan. 

   _Note: The path can be in any form (e.g. `/data/Media/...`, `/mnt/unionfs/Media/...`, `My Drive/Media/....`). The 'Server Path Mappings' will redirect the scan to the correct location._

4. The request will now show up under Plex Autoscan logs. 

## HTTP

1. Initiate a scan request via curl or equivalent tool:

   _Note: The path can be in any form (e.g. `/data/Media/...`, `/mnt/unionfs/Media/...`, `My Drive/Media/....`). The 'Server Path Mappings' will redirect the scan to the correct location._

   Format:
   ```
   curl -d "eventType=Manual&filepath=<PATH TO FILE/FOLDER>" <YOUR PLEX AUTOSCAN URL>
   ```

1. Examples:

      ```shell
      curl -d "eventType=Manual&filepath=/mnt/unionfs/Media/Movies/Shut In (2016)/Shut In (2016) - Bluray-1080p.x264.DTS-GECKOS.mkv" http://ipaddress:3468/0c1fa3c9867e48b1bb3aa055cb86`
      ```

      ```shell
      curl -d "eventType=Manual&filepath=/data/Movies/Shut In (2016)/Shut In (2016) - Bluray-1080p.x264.DTS-GECKOS.mkv" http://ipaddress:3468/0c1fa3c9867e48b1bb3aa055cb86`
      ```
 
4. The request will now show up under Plex Autoscan logs. 

For more details on both options, see [[here|https://github.com/l3uddz/plex_autoscan#misc]]. 


## CLI

_Note 1: This is only done on the box where Plex is installed._

_Note 2: The path used here has to be exactly what Plex uses for its library._

_Note 3: This method does not use Plex Autoscan, and therefore, Plex will immediately start scanning the given paths._


### Command

_Note: Replace `<section ID>` ([[Plex Library Section IDs]]) and `<plex library's movie/tv show path>` with yours._

```
docker exec -u plex -i plex bash -c 'export LD_LIBRARY_PATH=/usr/lib/plexmediaserver/lib;/usr/lib/plexmediaserver/Plex\ Media\ Scanner --scan --refresh --section <section ID> --directory '"'"'<movie or tv show path>'"'"''
```

### Examples

Movie (Section ID 1)

```
docker exec -u plex -i plex bash -c 'export LD_LIBRARY_PATH=/usr/lib/plexmediaserver/lib;/usr/lib/plexmediaserver/Plex\ Media\ Scanner --scan --refresh --section 1 --directory '"'"'/data/Movies/The Predator (2018)/'"'"''
```

TV Show (Section ID 2)

```
docker exec -u plex -i plex bash -c 'export LD_LIBRARY_PATH=/usr/lib/plexmediaserver/lib;/usr/lib/plexmediaserver/Plex\ Media\ Scanner --scan --refresh --section 2 --directory '"'"'/data/TV/The Walking Dead/'"'"''
```

TV Show with specific season scanned (Section ID 2)

```
docker exec -u plex -i plex bash -c 'export LD_LIBRARY_PATH=/usr/lib/plexmediaserver/lib;/usr/lib/plexmediaserver/Plex\ Media\ Scanner --scan --refresh --section 2 --directory '"'"'/data/TV/Marvels Daredevil/Season 03/'"'"''
```